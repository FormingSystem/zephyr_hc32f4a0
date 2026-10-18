---
id: learning.zephyr-docs.usb.api-179
title: CDC线路编码结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcdc__acm__line__coding.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第179章\_CDC线路编码结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcdc__acm__line__coding.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 179.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

GET_LINE_CODING／SET_LINE_CODING 类请求使用的数据结构。

```c
#include <zephyr/usb/class/usb_cdc.h>
```

GET_LINE_CODING／SET_LINE_CODING 类请求使用的数据结构。

## 179.2\_数据成员（Data Fields）

<a id="r_a14d35b67e6f00b0d6196ba0e9ef6dfab"></a>

```c
uint32_t dwDTERate
```



相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dwDTERate](P179_CDC线路编码结构.md#a14d35b67e6f00b0d6196ba0e9ef6dfab)。

<a id="r_afd2fd70a7da783d7aac0d99f9f267383"></a>

```c
uint8_t bCharFormat
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bCharFormat](P179_CDC线路编码结构.md#afd2fd70a7da783d7aac0d99f9f267383)。

<a id="r_a472270d84e160348e024f756b834cbb8"></a>

```c
uint8_t bParityType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bParityType](P179_CDC线路编码结构.md#a472270d84e160348e024f756b834cbb8)。

<a id="r_ab685d018d83e3e2d38c87c27902cca3e"></a>

```c
uint8_t bDataBits
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDataBits](P179_CDC线路编码结构.md#ab685d018d83e3e2d38c87c27902cca3e)。

## 179.3\_详细说明（Detailed Documentation）

<a id="afd2fd70a7da783d7aac0d99f9f267383"></a>

### 179.3.1\_`bCharFormat`

```c
uint8_t cdc_acm_line_coding::bCharFormat
```

> 译注（源码核对）：该字段对应停止位（Stop Bits）编码：0、1、2 分别对应 1、1.5、2 个停止位，常量见公共头文件。不要直接将浮点数 1.5 写入这个 uint8_t 字段。

<a id="ab685d018d83e3e2d38c87c27902cca3e"></a>

### 179.3.2\_`bDataBits`

```c
uint8_t cdc_acm_line_coding::bDataBits
```

> 译注（源码核对）：该字段对应数据位数（Data Bits）。头文件提供 5、6、7、8 的常量；当前驱动转换函数对未单列值走默认 8 位分支，不等同于对所有非法线路参数返回错误。

<a id="a472270d84e160348e024f756b834cbb8"></a>

### 179.3.3\_`bParityType`

```c
uint8_t cdc_acm_line_coding::bParityType
```

> 译注（源码核对）：该字段对应校验方式（Parity）：无校验、奇校验、偶校验、固定 1 校验（Mark）、固定 0 校验（Space），分别使用头文件中 0～4 的常量。

<a id="a14d35b67e6f00b0d6196ba0e9ef6dfab"></a>

### 179.3.4\_`dwDTERate`

```c
uint32_t cdc_acm_line_coding::dwDTERate
```

> 译注（源码核对）：当前实现用 `sys_le32_to_cpu()` 将此值读入 `uart_config.baudrate`。SET_LINE_CODING 接收完整结构后更新 CDC 实例保存的线路配置，并发布线路编码消息；这一流程不能单独证明外部物理 UART 已按同样的波特率重新配置。

## 179.4\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P178_CDC抽象控制功能描述符.md) · [返回大纲](大纲.md) · [下一章](P180_CDC串行状态通知.md)
