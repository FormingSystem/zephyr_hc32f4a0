---
id: learning.zephyr-docs.firmware_update.mgmt-smp_protocol
title: SMP协议规范
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/services/device_mgmt/smp_protocol.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第9章\_SMP协议规范

原文：[SMP Protocol Specification](https://docs.zephyrproject.org/latest/services/device_mgmt/smp_protocol.html)。读取日期：2026-10-12，`latest`。

本章描述 MCUmgr 用于向设备发送请求、接收响应的**简单管理协议（Simple Management Protocol，SMP）**。它是应用层协议，底层传输方式另见[传输规范](P010_SMP传输规范.md)。

**原文注意：**这里的 SMP 与蓝牙的 **安全管理协议（Security Manager Protocol）**不是同一协议；MCUmgr 的 SMP 只是可以通过蓝牙传输。

## 9.1\_帧头与载荷

每帧包含头部和数据；如果底层支持分片，Data Length（数据长度）可用于重组。多字节字段采用**大端序（Big Endian）**，也称网络字节序。原图所表达的八字节头部如下，字节按传输顺序排列：

| 字节位置 | 位或宽度 | 字段 |
| --- | --- | --- |
| 0 | 位7至5，3位 | Res（保留）。 |
| 0 | 位4至3，2位 | Ver（版本）。 |
| 0 | 位2至0，3位 | OP（操作）。 |
| 1 | 8位 | Flags（标志）。 |
| 2至3 | 16位，大端 | Data Length（数据长度）。 |
| 4至5 | 16位，大端 | Group ID（组标识）。 |
| 6 | 8位 | Sequence Num（序列号）。 |
| 7 | 8位 | Command ID（命令标识）。 |
| 8起 | Data Length字节 | Data（可选数据）。 |

**原文注意：**早期规范要求同时接受**小端序（Little Endian）**和大端序帧，但实际 MCUmgr 库固定将网络侧按大端序处理。数据长度为零时没有数据字段，其余情况下数据编码由目标组和命令决定。

## 9.2\_字段含义

| 字段 | 规则 |
| --- | --- |
| Res | 未使用，必须为0。 |
| Ver | 设为 `0b01` 使用具有组错误映射的新协议；`0b00` 使用旧协议。`0b10`、`0b11` 保留，不应使用。 |
| OP | 枚举 [`mcumgr_op_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gae06a618f492f18e856742b4affab80dd) 表示向设备写入还是请求读取，以及请求或响应方向。 |
| Flags | 尚无已定义标志，应为0。 |
| Data Length | 数据字段的长度，不含八字节头部。 |
| Group ID | 枚举 [`mcumgr_group_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga81f98b9a0c3810f7d607b783f8e259b5) 表示管理组。 |
| Sequence Num | 每次请求递增，响应序列号应与对应请求相同。 |
| Command ID | 管理组内部的命令编号。 |
| Data | 长度指定的载荷；为零时省略。内容取决于操作、组和命令。 |

> 译注：版本位 `0b00` 对应后文称为 SMP version 1 的旧协议，`0b01` 对应 SMP version 2；两位的编码值并不等于人类命名的版本号。序列号仅八位，不能把它当作永不重复的全局请求标识。

## 9.3\_管理组编号

协议提供预定义组，也允许用户自定义。原表列出以下十进制编号：

| 编号 | 管理组 |
| --- | --- |
| 0 | 默认/操作系统管理。 |
| 1 | 应用或软件镜像管理。 |
| 2 | 统计。 |
| 3 | 设置/配置。 |
| 4 | 应用/系统日志，Zephyr当前未使用。 |
| 5 | 运行时测试，Zephyr未使用。 |
| 6 | 拆分镜像管理，Zephyr未使用。 |
| 7 | 应用崩溃测试，Zephyr未使用。 |
| 8 | 文件系统管理。 |
| 9 | 命令行管理。 |
| 63 | Zephyr管理。 |
| 64起 | 应用自定义管理组。 |

上述标准组的载荷使用**简洁二进制对象表示（Concise Binary Object Representation，CBOR）**编码；64及以上的用户组可自定义数据通信方案。

> 译注：原表没有列出10和11，但本页末尾和 MCUmgr概览另外列出枚举管理组与传输管理组。应结合当前版本完整组定义使用，不能因表中省略就认为这些编号可自由分配。

## 9.4\_最小响应与错误格式

原文要求，发出命令后，只要另一端存在响应服务，就应收到由头部和 CBOR **映射（Map）**容器组成的响应。仅当没有 SMP 服务或设备无响应时才允许没有回复。

> 译注：原文此处将请求另一端称作 client；按上下文应理解为处理请求的服务端或响应端。此处最小 CBOR 响应约定描述标准管理通信；自定义组的编码仍须按组规范实现。

SMP第2版的组错误表示为以下结构。代码中的 `(str)`、`(uint)` 是规范的类型标注，不是可直接发送的 **JavaScript对象表示法（JavaScript Object Notation，JSON）** 文本：

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

旧第1版，以及第2版中不属于具体组的 SMP 错误，使用以下形式：

```text
{
    (str)"rc"       : (int)
}
```

`err.group` 指枚举 `mcumgr_group_t` 的组编号，只有第2版组错误时出现；`err.rc` 是该组内非零错误编号。顶层 `rc` 则是枚举 [`mcumgr_err_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5) 的非零通用错误码。

没有错误时不会带 `rc` 或 `err`，最小响应可以是空映射。响应没有这些错误字段时，可按协议视为请求成功；第2版客户端必须同时处理组错误与通用 `rc` 错误，不能只检查其中一种。

## 9.5\_Zephyr支持的组规范

完整组规范分别为[操作系统](P011_操作系统管理组.md)、[镜像](P012_镜像管理组.md)、[统计](P013_统计管理组.md)、[设置](P014_设置管理组.md)、[文件系统](P015_文件系统管理组.md)、[命令行](P016_Shell管理组.md)、[枚举](P017_枚举管理组.md)、[传输](P018_传输管理组.md)和[Zephyr](P019_Zephyr管理组.md)。本次未生成、发送或抓取协议报文。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：管理回调](P008_管理回调.md) · [本模块主线目录](../reading/firmware_update.md) · [全部主线](../reading/README.md) · [下一篇：SMP传输规范](P010_SMP传输规范.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：管理回调](P008_管理回调.md) · [下一章：SMP传输规范](P010_SMP传输规范.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
