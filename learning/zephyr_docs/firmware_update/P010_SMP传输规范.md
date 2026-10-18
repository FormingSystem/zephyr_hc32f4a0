---
id: learning.zephyr-docs.firmware_update.mgmt-smp_transport
title: SMP传输规范
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/services/device_mgmt/smp_transport.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第10章\_SMP传输规范

原文：[SMP Transport Specification](https://docs.zephyrproject.org/latest/services/device_mgmt/smp_transport.html)。读取日期：2026-10-12，`latest`。

本章给出实现服务端与客户端 **简单管理协议（Simple Management Protocol，SMP）**传输所需的信息。应用层报文见[SMP协议规范](P009_SMP协议规范.md)。

## 10.1\_蓝牙低功耗

**蓝牙低功耗（Bluetooth Low Energy，LE）**客户端使用如下**通用唯一标识符（Universally Unique Identifier，UUID）**：

| 对象 | UUID |
| --- | --- |
| 服务 | `8D53DC1D-1DB7-4CD3-868B-8A527460AA84` |
| 特征 | `DA2E7828-FBCE-4E01-AE9E-261174997C48` |

全部 SMP 通信用一个**通用属性配置文件（Generic Attribute Profile，GATT）**特征。请求通过 Write Without Response（无响应写）发送；SMP 响应通过 Notification（通知）发送。这里“无响应写”是 GATT 操作方式，不表示没有 SMP 层响应。

请求或响应太大、无法放入一个 GATT 命令时，发送方拆成多包。不增加额外分片头，只切分载荷；GATT 保证顺序投递，因此第一片中的 SMP 头已足以支持重组。

## 10.2\_串口与控制台复用

经**通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）**传输时，控制台编码用基本帧结构支持与其他串口内容复用。每帧前面有两个字节标记，末尾有一个换行字节。

原文说明 MCUmgr 当前限制每帧127字节，这不是协议本身不可更改的限制。限制包括标记和换行，因此中间编码正文最多124字节。

> 译注：原文早段说 Zephyr 尚无“不带帧结构的串口传输”，但同页后半又介绍现有 Raw UART 配置；前一句已与后文不一致。下面分别保留控制台编码和原始串口的规则，不能用这句旧说明否认后者存在。

## 10.3\_四种分片形式与编码容量

每个串口帧包括标记、正文、换行。四种形式为**首帧（Initial）**、**中间帧（Partial）**、**末帧（Partial-Final）**和**首末合一帧（Initial-Final）**。多帧报文从首帧开始，接零个或多个中间帧，最后是末帧。

正文始终使用 **Base64编码（Base64 Encoding）**。记传输帧上限为**最大传输单元（Maximum Transmission Unit，MTU）**，编码正文最多 `MTU - 3` 字节；原文给出的原始数据容量关系为 `N = (MTU - 3) / 4 * 3`。

首帧的编码内容先带两字节大端总长度。这个长度值等于整份原始报文大小再加两字节**16位循环冗余校验（16-bit Cyclic Redundancy Check，CRC16）**，不包括长度字段自身。因此首帧能容纳的报文片段最多 `N - 2` 字节。

原文说原始正文小于 `N - 4` 时，可在首末合一帧中同时放下长度、完整报文和CRC。

> 译注：Base64按每3字节编码为4字节计，应使用 `N = floor((MTU - 3) / 4) × 3`。MTU为127时，N为93，首帧最多91字节报文数据，普通中间帧93字节，末帧91字节，首末合一帧89字节。容量上限包含等号；原文“小于”的说法更保守。这里的原始报文包括SMP头与数据，不是只指**简洁二进制对象表示（Concise Binary Object Representation，CBOR）**载荷。

## 10.4\_首帧与首末合一帧

外层格式相同：

| 内容 | 大小 | 含义 |
| --- | --- | --- |
| `0x06 0x09` | 2字节 | 首帧标记。 |
| `<base64-i>` | 不超过MTU减3字节 | Base64编码的正文。 |
| `0x0a` | 1字节 | 换行结束符。 |

普通首帧解码后包含：

| 内容 | 大小或原表上限 | 含义 |
| --- | --- | --- |
| total length（总长度） | 2字节 | 大端报文长度加2字节CRC，不计本字段。 |
| body（正文片段） | 原表写MTU减5 | 原始报文的一部分；实际编码容量见上节。 |

首末合一帧解码后则为：

| 内容 | 大小或原表上限 | 含义 |
| --- | --- | --- |
| total length | 2字节 | 大端报文长度加2字节CRC，不计本字段。 |
| body | 原表写MTU减7 | 完整原始报文。 |
| crc16 | 2字节 | 整个原始报文的CRC，不包含前置长度字段。 |

> 译注：原表用“MTU减5/减7”直接表示解码后的数据容量，混用了编码前后长度。这里保留原表写法供对照，真正分片要按上节Base64公式扣除长度和CRC，不能按这些较大的数值装入原始数据。

## 10.5\_中间帧与末帧

后续帧使用以下外层格式：

| 内容 | 大小 | 含义 |
| --- | --- | --- |
| `0x04 0x14` | 2字节 | 后续帧标记。 |
| `<base64-i>` | 不超过MTU减3字节 | Base64编码正文。 |
| `0x0a` | 1字节 | 换行结束符。 |

普通中间帧解码后仅有 body（报文片段）；原表上限写“MTU减3”，实际为 N。末帧解码后是 body 与两字节 crc16；原表把正文上限写“MTU减5”，实际为 N减2。CRC针对整个报文，不是仅对最后一片计算。

## 10.6\_CRC细节

终结帧携带的CRC16只覆盖原始报文数据，不包含前置总长度；多项式为 `0x1021`，初始值为0。

> 译注：所核对的 `subsys/mgmt/mcumgr/transport/src/serial_util.c` 先对完整报文计算CRC，再分片；其Base64容量也按3到4比例计算。以上是源代码对照，不是本次发送测试或互操作性验证。

## 10.7\_原始UART传输

Zephyr 另有不使用Base64的原始串口方式，代码更小，传输更快；所有通信直接使用二进制SMP，因此不能与同一UART上的命令行或日志输出混用，也不应接到用于显示 **美国信息交换标准码（American Standard Code for Information Interchange，ASCII）**文本的普通终端。

启用 Kconfig 配置项 [`CONFIG_MCUMGR_TRANSPORT_RAW_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_RAW_UART)，并让 MCUmgr UART控制台驱动工作在原始模式。

## 10.8\_原始串口超时

因为没有控制台帧边界，意外字节可能被解析成很长的报文，使系统等待不会到来的后续数据。超时机制会在规定时间内没有收齐整包时清空接收缓冲区。

原文建议实际UART启用超时；对于 **通用串行总线（Universal Serial Bus，USB）**的**通信设备类（Communications Device Class，CDC）**虚拟串口，如果数据在送入前可验证，则不需要这一选项。配置项 [`CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT) 启用超时，[`CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT_TIME_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT_TIME_MS) 指定毫秒数。

完整**应用程序编程接口（Application Programming Interface，API）**见 [SMP传输参考](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html)。本次没有占用串口、配对蓝牙或更改设备配置。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：SMP协议规范](P009_SMP协议规范.md) · [本模块主线目录](../reading/firmware_update.md) · [全部主线](../reading/README.md) · [下一篇：操作系统管理组](P011_操作系统管理组.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：SMP协议规范](P009_SMP协议规范.md) · [下一章：操作系统管理组](P011_操作系统管理组.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
