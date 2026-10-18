---
id: learning.zephyr-docs.usb.api-174
title: CDC公共头文件与常量
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__cdc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第174章\_CDC公共头文件与常量

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__cdc_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 174.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

USB 通信设备类（Communications Device Class，CDC）公共头文件。

USB 通信设备类（Communications Device Class，CDC）公共头文件。

本头文件遵循通信设备规范（Communications Devices Specification，CDC120-20101103-track.pdf）、公共交换电话网设备规范（PSTN Devices Specification，PSTN120.pdf）和以太网控制模型设备规范（Ethernet Control Model Devices Specification，ECM120.pdf）中的类定义。头文件限于 ACM 和 ECM 子类。

> 译注（源码核对）：上方“限于 ACM 和 ECM”保留原文；当前同一头文件还声明 NCM 描述符与能力位，并包含以太网仿真模型（Ethernet Emulation Model，EEM）的子类／协议常量，原概述没有覆盖这些后续内容。

## 174.2\_数据结构（Data Structures）

<a id="r_cdc_5Fheader_5Fdescriptor"></a>

```c
struct cdc_header_descriptor
```

头部功能描述符（Header Functional Descriptor）。

相关声明：[cdc_header_descriptor](P175_CDC头部功能描述符.md)。

<a id="r_cdc_5Funion_5Fdescriptor"></a>

```c
struct cdc_union_descriptor
```

联合接口功能描述符（Union Interface Functional Descriptor）。

相关声明：[cdc_union_descriptor](P176_CDC联合接口功能描述符.md)。

<a id="r_cdc_5Fcm_5Fdescriptor"></a>

```c
struct cdc_cm_descriptor
```

呼叫管理功能描述符（Call Management Functional Descriptor）。

相关声明：[cdc_cm_descriptor](P177_CDC呼叫管理功能描述符.md)。

<a id="r_cdc_5Facm_5Fdescriptor"></a>

```c
struct cdc_acm_descriptor
```

抽象控制管理功能描述符（Abstract Control Management Functional Descriptor）。

相关声明：[cdc_acm_descriptor](P178_CDC抽象控制功能描述符.md)。

<a id="r_cdc_5Facm_5Fline_5Fcoding"></a>

```c
struct cdc_acm_line_coding
```

GET_LINE_CODING／SET_LINE_CODING 类请求使用的数据结构。

相关声明：[cdc_acm_line_coding](P179_CDC线路编码结构.md)。

<a id="r_cdc_5Facm_5Fnotification"></a>

```c
struct cdc_acm_notification
```

串行状态（SerialState）通知使用的数据结构。

相关声明：[cdc_acm_notification](P180_CDC串行状态通知.md)。

<a id="r_cdc_5Fecm_5Fdescriptor"></a>

```c
struct cdc_ecm_descriptor
```

以太网网络功能描述符（Ethernet Networking Functional Descriptor）。

相关声明：[cdc_ecm_descriptor](P181_CDC以太网功能描述符.md)。

<a id="r_cdc_5Fncm_5Fdescriptor"></a>

```c
struct cdc_ncm_descriptor
```

以太网网络控制模型描述符（Ethernet Network Control Model，NCM Descriptor）。

相关声明：[cdc_ncm_descriptor](P182_CDC网络控制模型描述符.md)。

## 174.3\_宏定义（Macros）

<a id="r_a2d44425b0b0c5e525885c5764348ec54"></a>

```c
#define CDC_SRN_1_20 0x0120 __DEPRECATED_MACRO
```

以二进制编码的十进制格式（Binary-coded Decimal，BCD）表示的 CDC 规范版本号。

相关声明：[CDC_SRN_1_20](P174_CDC公共头文件与常量.md#a2d44425b0b0c5e525885c5764348ec54)。

<a id="r_a01b7a28004a035df52334b64308e4b22"></a>

```c
#define ACM_SUBCLASS 0x02
```

通信类子类代码（Communications Class Subclass Codes）。

相关声明：[ACM_SUBCLASS](P174_CDC公共头文件与常量.md#a01b7a28004a035df52334b64308e4b22)。

<a id="r_a39f776a70d5139575ed84be1a9faee5d"></a>

```c
#define ECM_SUBCLASS 0x06
```



相关声明：[ECM_SUBCLASS](P174_CDC公共头文件与常量.md#a39f776a70d5139575ed84be1a9faee5d)。

<a id="r_a73503e51ff8700620866be15a8d7ab43"></a>

```c
#define EEM_SUBCLASS 0x0c
```



相关声明：[EEM_SUBCLASS](P174_CDC公共头文件与常量.md#a73503e51ff8700620866be15a8d7ab43)。

<a id="r_af4edeebbc1d4fb6f3a727083a36e731e"></a>

```c
#define NCM_SUBCLASS 0x0d
```



相关声明：[NCM_SUBCLASS](P174_CDC公共头文件与常量.md#af4edeebbc1d4fb6f3a727083a36e731e)。

<a id="r_aaf98d38c2b9c859cf86e281bb67f27b0"></a>

```c
#define AT_CMD_V250_PROTOCOL 0x01
```

通信类协议代码（Communications Class Protocol Codes）。

相关声明：[AT_CMD_V250_PROTOCOL](P174_CDC公共头文件与常量.md#aaf98d38c2b9c859cf86e281bb67f27b0)。

<a id="r_ab4f22c3c42b5a4efe7735bafebc1cb9b"></a>

```c
#define EEM_PROTOCOL 0x07
```



相关声明：[EEM_PROTOCOL](P174_CDC公共头文件与常量.md#ab4f22c3c42b5a4efe7735bafebc1cb9b)。

<a id="r_a20396bb325a1e947b2e4b0017a134082"></a>

```c
#define ACM_VENDOR_PROTOCOL 0xFF
```



相关声明：[ACM_VENDOR_PROTOCOL](P174_CDC公共头文件与常量.md#a20396bb325a1e947b2e4b0017a134082)。

<a id="r_a6577856e991bddc829d93af0ea527ef6"></a>

```c
#define NCM_DATA_PROTOCOL 0x01
```



相关声明：[NCM_DATA_PROTOCOL](P174_CDC公共头文件与常量.md#a6577856e991bddc829d93af0ea527ef6)。

<a id="r_ae4044b943c9e54cb7a64c8c35acaf8bc"></a>

```c
#define DATA_INTERFACE_CLASS 0x0A
```

数据类接口代码（Data Class Interface Codes）。

相关声明：[DATA_INTERFACE_CLASS](P174_CDC公共头文件与常量.md#ae4044b943c9e54cb7a64c8c35acaf8bc)。

<a id="r_a008b7d343c5a1876a78c885f7a496b66"></a>

```c
#define HEADER_FUNC_DESC 0x00
```

通信类功能描述符的 bDescriptor SubType（描述符子类型）。

相关声明：[HEADER_FUNC_DESC](P174_CDC公共头文件与常量.md#a008b7d343c5a1876a78c885f7a496b66)。

<a id="r_a60552aa9506dc2c6dede5146c5251aaf"></a>

```c
#define CALL_MANAGEMENT_FUNC_DESC 0x01
```



相关声明：[CALL_MANAGEMENT_FUNC_DESC](P174_CDC公共头文件与常量.md#a60552aa9506dc2c6dede5146c5251aaf)。

<a id="r_a057b9de28602442b66a8c3a7befd62a7"></a>

```c
#define ACM_FUNC_DESC 0x02
```



相关声明：[ACM_FUNC_DESC](P174_CDC公共头文件与常量.md#a057b9de28602442b66a8c3a7befd62a7)。

<a id="r_aab7f21ab95fc5916f758e66087caef25"></a>

```c
#define UNION_FUNC_DESC 0x06
```



相关声明：[UNION_FUNC_DESC](P174_CDC公共头文件与常量.md#aab7f21ab95fc5916f758e66087caef25)。

<a id="r_a22b2b55d7ab3cdd4206df07cddcc44e9"></a>

```c
#define ETHERNET_FUNC_DESC 0x0F
```



相关声明：[ETHERNET_FUNC_DESC](P174_CDC公共头文件与常量.md#a22b2b55d7ab3cdd4206df07cddcc44e9)。

<a id="r_ad788a76ba44ab5d02c699b110856e18e"></a>

```c
#define ETHERNET_FUNC_DESC_NCM 0x1a
```



相关声明：[ETHERNET_FUNC_DESC_NCM](P174_CDC公共头文件与常量.md#ad788a76ba44ab5d02c699b110856e18e)。

<a id="r_a7e9384e6a613e38c543d7eba05f64c07"></a>

```c
#define USB_CDC_NETWORK_CONNECTION 0x00
```

通信类通知代码（Communications Class Notification Codes）。

相关声明：[USB_CDC_NETWORK_CONNECTION](P174_CDC公共头文件与常量.md#a7e9384e6a613e38c543d7eba05f64c07)。

<a id="r_a970045b850b0195b5a4a2913d5a0b918"></a>

```c
#define USB_CDC_RESPONSE_AVAILABLE 0x01
```

响应可用通知（Response Available Notification）。

相关声明：[USB_CDC_RESPONSE_AVAILABLE](P174_CDC公共头文件与常量.md#a970045b850b0195b5a4a2913d5a0b918)。

<a id="r_af4d27c4b8118b7fa6574c4892291adf9"></a>

```c
#define USB_CDC_CONNECTION_SPEED_CHANGE 0x2A
```

连接速率变化通知（Connection Speed Change Notification）。

相关声明：[USB_CDC_CONNECTION_SPEED_CHANGE](P174_CDC公共头文件与常量.md#af4d27c4b8118b7fa6574c4892291adf9)。

<a id="r_a926f6444745d1cdc991d97e4f1d265ad"></a>

```c
#define CDC_SEND_ENC_CMD 0x00
```

ACM 设备的 PSTN 子类专用请求（PSTN Subclass Specific Requests）。

相关声明：[CDC_SEND_ENC_CMD](P174_CDC公共头文件与常量.md#a926f6444745d1cdc991d97e4f1d265ad)。

<a id="r_ac9008f0dc0d4fc7141de9dd12352caa8"></a>

```c
#define CDC_GET_ENC_RSP 0x01
```



相关声明：[CDC_GET_ENC_RSP](P174_CDC公共头文件与常量.md#ac9008f0dc0d4fc7141de9dd12352caa8)。

<a id="r_a91a9c047339a1a5918b6a923af6d1af6"></a>

```c
#define SET_LINE_CODING 0x20
```



相关声明：[SET_LINE_CODING](P174_CDC公共头文件与常量.md#a91a9c047339a1a5918b6a923af6d1af6)。

<a id="r_a6698d8d2ca56fafdc943aec2cede1daf"></a>

```c
#define GET_LINE_CODING 0x21
```



相关声明：[GET_LINE_CODING](P174_CDC公共头文件与常量.md#a6698d8d2ca56fafdc943aec2cede1daf)。

<a id="r_a437869c339749d5d011060cd5676659e"></a>

```c
#define SET_CONTROL_LINE_STATE 0x22
```



相关声明：[SET_CONTROL_LINE_STATE](P174_CDC公共头文件与常量.md#a437869c339749d5d011060cd5676659e)。

<a id="r_afdeb5f862a52b953653b9ab567979cec"></a>

```c
#define USB_CDC_AUX_JACK_HOOK_STATE 0x08
```

PSTN 子类的类专用通知代码（Class-Specific Notification Codes）。

相关声明：[USB_CDC_AUX_JACK_HOOK_STATE](P174_CDC公共头文件与常量.md#afdeb5f862a52b953653b9ab567979cec)。

<a id="r_a52452ce9272b97203fece115b5005aff"></a>

```c
#define USB_CDC_RING_DETECT 0x09
```

振铃检测通知（Ring Detect Notification）。

相关声明：[USB_CDC_RING_DETECT](P174_CDC公共头文件与常量.md#a52452ce9272b97203fece115b5005aff)。

<a id="r_ac167f480370c73b830281d98ad5899b1"></a>

```c
#define USB_CDC_SERIAL_STATE 0x20
```

串行状态通知（Serial State Notification）。

相关声明：[USB_CDC_SERIAL_STATE](P174_CDC公共头文件与常量.md#ac167f480370c73b830281d98ad5899b1)。

<a id="r_ac63891d7c3321f7f4eb297f87c0978f6"></a>

```c
#define USB_CDC_LINE_STATE_CHANGE 0x23
```

线路状态变化通知（Line State Change Notification）。

相关声明：[USB_CDC_LINE_STATE_CHANGE](P174_CDC公共头文件与常量.md#ac63891d7c3321f7f4eb297f87c0978f6)。

<a id="r_a6bb6650664f82fd25330af0357e5831e"></a>

```c
#define USB_CDC_CALL_STATE_CHANGE 0x28
```

呼叫状态变化通知（Call State Change Notification）。

相关声明：[USB_CDC_CALL_STATE_CHANGE](P174_CDC公共头文件与常量.md#a6bb6650664f82fd25330af0357e5831e)。

<a id="r_a504f682d66f714730f35d282ce0b9177"></a>

```c
#define USB_CDC_SERIAL_STATE_OVERRUN BIT(6)
```

PSTN 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）状态位图值。

相关声明：[USB_CDC_SERIAL_STATE_OVERRUN](P174_CDC公共头文件与常量.md#a504f682d66f714730f35d282ce0b9177)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1ff82c5d551211d2298128bd84eeb60a"></a>

```c
#define USB_CDC_SERIAL_STATE_PARITY BIT(5)
```



相关声明：[USB_CDC_SERIAL_STATE_PARITY](P174_CDC公共头文件与常量.md#a1ff82c5d551211d2298128bd84eeb60a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a59f5f1ebab838621cdc67668541432ca"></a>

```c
#define USB_CDC_SERIAL_STATE_FRAMING BIT(4)
```



相关声明：[USB_CDC_SERIAL_STATE_FRAMING](P174_CDC公共头文件与常量.md#a59f5f1ebab838621cdc67668541432ca)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a60f22cb2ae47789875e2542063899876"></a>

```c
#define USB_CDC_SERIAL_STATE_RINGSIGNAL BIT(3)
```



相关声明：[USB_CDC_SERIAL_STATE_RINGSIGNAL](P174_CDC公共头文件与常量.md#a60f22cb2ae47789875e2542063899876)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a15f3c90969106ecdf3b1cdf258cad5df"></a>

```c
#define USB_CDC_SERIAL_STATE_BREAK BIT(2)
```



相关声明：[USB_CDC_SERIAL_STATE_BREAK](P174_CDC公共头文件与常量.md#a15f3c90969106ecdf3b1cdf258cad5df)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab96b4f63f2de0ef913862878bce1029f"></a>

```c
#define USB_CDC_SERIAL_STATE_TXCARRIER BIT(1)
```



相关声明：[USB_CDC_SERIAL_STATE_TXCARRIER](P174_CDC公共头文件与常量.md#ab96b4f63f2de0ef913862878bce1029f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad720be9e3738bcba7e37dc9392c3b6e8"></a>

```c
#define USB_CDC_SERIAL_STATE_RXCARRIER BIT(0)
```



相关声明：[USB_CDC_SERIAL_STATE_RXCARRIER](P174_CDC公共头文件与常量.md#ad720be9e3738bcba7e37dc9392c3b6e8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a00788c95fb39c2636d7d5a427282399f"></a>

```c
#define SET_CONTROL_LINE_STATE_RTS 0x02
```

SetControlLineState 的控制信号位图值（Control Signal Bitmap Values）。

相关声明：[SET_CONTROL_LINE_STATE_RTS](P174_CDC公共头文件与常量.md#a00788c95fb39c2636d7d5a427282399f)。

<a id="r_a07623c40153f936c863627a3dc30da7a"></a>

```c
#define SET_CONTROL_LINE_STATE_DTR 0x01
```



相关声明：[SET_CONTROL_LINE_STATE_DTR](P174_CDC公共头文件与常量.md#a07623c40153f936c863627a3dc30da7a)。

<a id="r_a89554d686630d67d642e228b7ee0dc2c"></a>

```c
#define USB_CDC_LINE_CTRL_BAUD_RATE UART_LINE_CTRL_BAUD_RATE
```

为 uart_line_ctrl 枚举补充 CDC 专用值。

相关声明：[USB_CDC_LINE_CTRL_BAUD_RATE](P174_CDC公共头文件与常量.md#a89554d686630d67d642e228b7ee0dc2c)、[UART_LINE_CTRL_BAUD_RATE](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b)。

<a id="r_a7e6b9bb33debc489b7ac7e0fb0e94947"></a>

```c
#define USB_CDC_LINE_CTRL_DCD UART_LINE_CTRL_DCD
```



相关声明：[USB_CDC_LINE_CTRL_DCD](P174_CDC公共头文件与常量.md#a7e6b9bb33debc489b7ac7e0fb0e94947)、[UART_LINE_CTRL_DCD](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97)。

<a id="r_a6876caf1b77477e259bb391216309799"></a>

```c
#define USB_CDC_LINE_CTRL_DSR UART_LINE_CTRL_DSR
```



相关声明：[USB_CDC_LINE_CTRL_DSR](P174_CDC公共头文件与常量.md#a6876caf1b77477e259bb391216309799)、[UART_LINE_CTRL_DSR](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c)。

<a id="r_a716d9aaf772e1fa3f8b555077048ecbb"></a>

```c
#define USB_CDC_LINE_CTRL_BREAK BIT(5)
```



相关声明：[USB_CDC_LINE_CTRL_BREAK](P174_CDC公共头文件与常量.md#a716d9aaf772e1fa3f8b555077048ecbb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8ec9b8c619c567cc174c0473dda5a5fd"></a>

```c
#define USB_CDC_LINE_CTRL_RING_SIGNAL BIT(6)
```



相关声明：[USB_CDC_LINE_CTRL_RING_SIGNAL](P174_CDC公共头文件与常量.md#a8ec9b8c619c567cc174c0473dda5a5fd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a263186a0a64d9a8e7e9e97a54b951bdf"></a>

```c
#define USB_CDC_LINE_CTRL_FRAMING BIT(7)
```



相关声明：[USB_CDC_LINE_CTRL_FRAMING](P174_CDC公共头文件与常量.md#a263186a0a64d9a8e7e9e97a54b951bdf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae2779672a5b5ab49a2ed7240e463f9e8"></a>

```c
#define USB_CDC_LINE_CTRL_PARITY BIT(8)
```



相关声明：[USB_CDC_LINE_CTRL_PARITY](P174_CDC公共头文件与常量.md#ae2779672a5b5ab49a2ed7240e463f9e8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8bf1722f98bf48394605efddf6be1295"></a>

```c
#define USB_CDC_LINE_CTRL_OVER_RUN BIT(9)
```



相关声明：[USB_CDC_LINE_CTRL_OVER_RUN](P174_CDC公共头文件与常量.md#a8bf1722f98bf48394605efddf6be1295)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae38825267009563e0aa82a58a7fc4fd2"></a>

```c
#define SERIAL_STATE_OVER_RUN 0x40
```

UART 状态位图值（State Bitmap Values）。

相关声明：[SERIAL_STATE_OVER_RUN](P174_CDC公共头文件与常量.md#ae38825267009563e0aa82a58a7fc4fd2)。

<a id="r_a738f180df5795376763ff233fb8aa68d"></a>

```c
#define SERIAL_STATE_PARITY 0x20
```



相关声明：[SERIAL_STATE_PARITY](P174_CDC公共头文件与常量.md#a738f180df5795376763ff233fb8aa68d)。

<a id="r_aacd68fe3a081441ee684bf2ef6312bec"></a>

```c
#define SERIAL_STATE_FRAMING 0x10
```



相关声明：[SERIAL_STATE_FRAMING](P174_CDC公共头文件与常量.md#aacd68fe3a081441ee684bf2ef6312bec)。

<a id="r_a935c772da45984e8d796396146413037"></a>

```c
#define SERIAL_STATE_RING_SIGNAL 0x08
```



相关声明：[SERIAL_STATE_RING_SIGNAL](P174_CDC公共头文件与常量.md#a935c772da45984e8d796396146413037)。

<a id="r_aa66ab791abfcf7ef5a37758c1b33138a"></a>

```c
#define SERIAL_STATE_BREAK 0x04
```



相关声明：[SERIAL_STATE_BREAK](P174_CDC公共头文件与常量.md#aa66ab791abfcf7ef5a37758c1b33138a)。

<a id="r_a22cd80b90c53ff44a4c1de08310ba3c2"></a>

```c
#define SERIAL_STATE_TX_CARRIER 0x02
```



相关声明：[SERIAL_STATE_TX_CARRIER](P174_CDC公共头文件与常量.md#a22cd80b90c53ff44a4c1de08310ba3c2)。

<a id="r_a9677c612766f3e788ad2960a17ad0791"></a>

```c
#define SERIAL_STATE_RX_CARRIER 0x01
```



相关声明：[SERIAL_STATE_RX_CARRIER](P174_CDC公共头文件与常量.md#a9677c612766f3e788ad2960a17ad0791)。

<a id="r_a8a06b3413e1c665f13ba4895c220d608"></a>

```c
#define USB_CDC_LINE_CODING_STOP_BITS_1 0
```

PSTN 子类线路编码值（Line Coding Values）。

相关声明：[USB_CDC_LINE_CODING_STOP_BITS_1](P174_CDC公共头文件与常量.md#a8a06b3413e1c665f13ba4895c220d608)。

<a id="r_a4159f50590d647510a6a1f38875e012e"></a>

```c
#define USB_CDC_LINE_CODING_STOP_BITS_1_5 1
```



相关声明：[USB_CDC_LINE_CODING_STOP_BITS_1_5](P174_CDC公共头文件与常量.md#a4159f50590d647510a6a1f38875e012e)。

<a id="r_a7e7fc73b4490a694aa982b4862782157"></a>

```c
#define USB_CDC_LINE_CODING_STOP_BITS_2 2
```



相关声明：[USB_CDC_LINE_CODING_STOP_BITS_2](P174_CDC公共头文件与常量.md#a7e7fc73b4490a694aa982b4862782157)。

<a id="r_a549181d2cc92c42b4db8c3c34927d97f"></a>

```c
#define USB_CDC_LINE_CODING_PARITY_NO 0
```



相关声明：[USB_CDC_LINE_CODING_PARITY_NO](P174_CDC公共头文件与常量.md#a549181d2cc92c42b4db8c3c34927d97f)。

<a id="r_a44d808ad4f27ecf3502b9c14da2aa9b9"></a>

```c
#define USB_CDC_LINE_CODING_PARITY_ODD 1
```



相关声明：[USB_CDC_LINE_CODING_PARITY_ODD](P174_CDC公共头文件与常量.md#a44d808ad4f27ecf3502b9c14da2aa9b9)。

<a id="r_a327b5f99ab7e5cfc99d7592d1f9c1c25"></a>

```c
#define USB_CDC_LINE_CODING_PARITY_EVEN 2
```



相关声明：[USB_CDC_LINE_CODING_PARITY_EVEN](P174_CDC公共头文件与常量.md#a327b5f99ab7e5cfc99d7592d1f9c1c25)。

<a id="r_a490d381698ce91db4ab8bb24dd70820a"></a>

```c
#define USB_CDC_LINE_CODING_PARITY_MARK 3
```



相关声明：[USB_CDC_LINE_CODING_PARITY_MARK](P174_CDC公共头文件与常量.md#a490d381698ce91db4ab8bb24dd70820a)。

<a id="r_a5aa1b5cf30cb4020442131f66170fec6"></a>

```c
#define USB_CDC_LINE_CODING_PARITY_SPACE 4
```



相关声明：[USB_CDC_LINE_CODING_PARITY_SPACE](P174_CDC公共头文件与常量.md#a5aa1b5cf30cb4020442131f66170fec6)。

<a id="r_a327c495a9930b3e5519f0a9c7cd9ed18"></a>

```c
#define USB_CDC_LINE_CODING_DATA_BITS_5 5
```



相关声明：[USB_CDC_LINE_CODING_DATA_BITS_5](P174_CDC公共头文件与常量.md#a327c495a9930b3e5519f0a9c7cd9ed18)。

<a id="r_a231932add6d9ceef4f5332a0db1b9f55"></a>

```c
#define USB_CDC_LINE_CODING_DATA_BITS_6 6
```



相关声明：[USB_CDC_LINE_CODING_DATA_BITS_6](P174_CDC公共头文件与常量.md#a231932add6d9ceef4f5332a0db1b9f55)。

<a id="r_a6a276593bc4587671df5e6da8cce5ebb"></a>

```c
#define USB_CDC_LINE_CODING_DATA_BITS_7 7
```



相关声明：[USB_CDC_LINE_CODING_DATA_BITS_7](P174_CDC公共头文件与常量.md#a6a276593bc4587671df5e6da8cce5ebb)。

<a id="r_a64e296aec72bbd8f9bdc1aefa5aab654"></a>

```c
#define USB_CDC_LINE_CODING_DATA_BITS_8 8
```



相关声明：[USB_CDC_LINE_CODING_DATA_BITS_8](P174_CDC公共头文件与常量.md#a64e296aec72bbd8f9bdc1aefa5aab654)。

<a id="r_a4dce35ee8cf2337bab3c90081200a9f6"></a>

```c
#define SET_ETHERNET_MULTICAST_FILTERS 0x40
```

以太网子类的类专用请求代码（Class-Specific Request Codes）。

相关声明：[SET_ETHERNET_MULTICAST_FILTERS](P174_CDC公共头文件与常量.md#a4dce35ee8cf2337bab3c90081200a9f6)。

<a id="r_a1506deda422ee354040b0feeb09ad4b6"></a>

```c
#define SET_ETHERNET_PM_FILTER 0x41
```



相关声明：[SET_ETHERNET_PM_FILTER](P174_CDC公共头文件与常量.md#a1506deda422ee354040b0feeb09ad4b6)。

<a id="r_a53ea6ae0e1fe8a88350740fd594507fd"></a>

```c
#define GET_ETHERNET_PM_FILTER 0x42
```



相关声明：[GET_ETHERNET_PM_FILTER](P174_CDC公共头文件与常量.md#a53ea6ae0e1fe8a88350740fd594507fd)。

<a id="r_adae019242224bbbc9d0f853da3733f1c"></a>

```c
#define SET_ETHERNET_PACKET_FILTER 0x43
```



相关声明：[SET_ETHERNET_PACKET_FILTER](P174_CDC公共头文件与常量.md#adae019242224bbbc9d0f853da3733f1c)。

<a id="r_a7dffeba1576d6660fb930eabc5c515b7"></a>

```c
#define GET_ETHERNET_STATISTIC 0x44
```



相关声明：[GET_ETHERNET_STATISTIC](P174_CDC公共头文件与常量.md#a7dffeba1576d6660fb930eabc5c515b7)。

<a id="r_a44e5dd539b8b41ccc9c61dd95ee4fb2e"></a>

```c
#define GET_NTB_PARAMETERS 0x80
```

NCM 子类的类专用请求代码。

相关声明：[GET_NTB_PARAMETERS](P174_CDC公共头文件与常量.md#a44e5dd539b8b41ccc9c61dd95ee4fb2e)。

<a id="r_a58701f26151379cd5dd8b7a7350dcda5"></a>

```c
#define GET_NET_ADDRESS 0x81
```



相关声明：[GET_NET_ADDRESS](P174_CDC公共头文件与常量.md#a58701f26151379cd5dd8b7a7350dcda5)。

<a id="r_a2d8525d02e54ec44143a7732a15ad5b0"></a>

```c
#define SET_NET_ADDRESS 0x82
```



相关声明：[SET_NET_ADDRESS](P174_CDC公共头文件与常量.md#a2d8525d02e54ec44143a7732a15ad5b0)。

<a id="r_a2ba9ad377b20364fc811ec6d5bb74995"></a>

```c
#define GET_NTB_FORMAT 0x83
```



相关声明：[GET_NTB_FORMAT](P174_CDC公共头文件与常量.md#a2ba9ad377b20364fc811ec6d5bb74995)。

<a id="r_a9c48d4f5685678b1429ba90f7c0a7d9b"></a>

```c
#define SET_NTB_FORMAT 0x84
```



相关声明：[SET_NTB_FORMAT](P174_CDC公共头文件与常量.md#a9c48d4f5685678b1429ba90f7c0a7d9b)。

<a id="r_ae5ab2b5f3c10b1fc42d5873f8e8082c0"></a>

```c
#define GET_NTB_INPUT_SIZE 0x85
```



相关声明：[GET_NTB_INPUT_SIZE](P174_CDC公共头文件与常量.md#ae5ab2b5f3c10b1fc42d5873f8e8082c0)。

<a id="r_a485fd89a465fb5ad82c09a686ba3bc1b"></a>

```c
#define SET_NTB_INPUT_SIZE 0x86
```



相关声明：[SET_NTB_INPUT_SIZE](P174_CDC公共头文件与常量.md#a485fd89a465fb5ad82c09a686ba3bc1b)。

<a id="r_aca024f2e7bb9f99d3376753589fa7c3f"></a>

```c
#define GET_MAX_DATAGRAM_SIZE 0x87
```



相关声明：[GET_MAX_DATAGRAM_SIZE](P174_CDC公共头文件与常量.md#aca024f2e7bb9f99d3376753589fa7c3f)。

<a id="r_a4d224c04ec87088b4494f43c59c59b86"></a>

```c
#define SET_MAX_DATAGRAM_SIZE 0x88
```



相关声明：[SET_MAX_DATAGRAM_SIZE](P174_CDC公共头文件与常量.md#a4d224c04ec87088b4494f43c59c59b86)。

<a id="r_a9dd7dad1bd3421f42a67f280826d464b"></a>

```c
#define GET_CRC_MODE 0x89
```



相关声明：[GET_CRC_MODE](P174_CDC公共头文件与常量.md#a9dd7dad1bd3421f42a67f280826d464b)。

<a id="r_a634a3403221f33ae8506481b38840c2c"></a>

```c
#define SET_CRC_MODE 0x8A
```



相关声明：[SET_CRC_MODE](P174_CDC公共头文件与常量.md#a634a3403221f33ae8506481b38840c2c)。

<a id="r_a4abfd25c9ca3e70c5b33b89ee9456087"></a>

```c
#define PACKET_TYPE_MULTICAST 0x10
```

以太网包过滤器位图（Ethernet Packet Filter Bitmap）。

相关声明：[PACKET_TYPE_MULTICAST](P174_CDC公共头文件与常量.md#a4abfd25c9ca3e70c5b33b89ee9456087)。

<a id="r_a3143cff5f7275d394f259c3b83e54e4b"></a>

```c
#define PACKET_TYPE_BROADCAST 0x08
```



相关声明：[PACKET_TYPE_BROADCAST](P174_CDC公共头文件与常量.md#a3143cff5f7275d394f259c3b83e54e4b)。

<a id="r_a5a2d0aa22741a4a48b976cddc6f57f98"></a>

```c
#define PACKET_TYPE_DIRECTED 0x04
```



相关声明：[PACKET_TYPE_DIRECTED](P174_CDC公共头文件与常量.md#a5a2d0aa22741a4a48b976cddc6f57f98)。

<a id="r_aac32de24c40e08d0d32d3db264fa964a"></a>

```c
#define PACKET_TYPE_ALL_MULTICAST 0x02
```



相关声明：[PACKET_TYPE_ALL_MULTICAST](P174_CDC公共头文件与常量.md#aac32de24c40e08d0d32d3db264fa964a)。

<a id="r_a7be4d4e65526efb94ea1ef71da62f835"></a>

```c
#define PACKET_TYPE_PROMISCUOUS 0x01
```



相关声明：[PACKET_TYPE_PROMISCUOUS](P174_CDC公共头文件与常量.md#a7be4d4e65526efb94ea1ef71da62f835)。

<a id="r_a8a3a6287eea23dfb919f37690e6a1f09"></a>

```c
#define USB_CDC_ECM_STAT_RESERVED 0x00
```

ECM 子类的以太网统计特性选择器代码（Ethernet Statistics Feature Selector Codes）。

相关声明：[USB_CDC_ECM_STAT_RESERVED](P174_CDC公共头文件与常量.md#a8a3a6287eea23dfb919f37690e6a1f09)。

<a id="r_a9dd668f37ce388faee799e4e65cd2dd3"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_OK 0x01
```

无错误发送的帧。

相关声明：[USB_CDC_ECM_STAT_XMIT_OK](P174_CDC公共头文件与常量.md#a9dd668f37ce388faee799e4e65cd2dd3)。

<a id="r_addc379e31c784df36649bf4fc2e85bc4"></a>

```c
#define USB_CDC_ECM_STAT_RCV_OK 0x02
```

无错误接收的帧。

相关声明：[USB_CDC_ECM_STAT_RCV_OK](P174_CDC公共头文件与常量.md#addc379e31c784df36649bf4fc2e85bc4)。

<a id="r_abe83d17d2d5cf21938fd0c2f528fa949"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_ERROR 0x03
```

未发送或发送时出错的帧。

相关声明：[USB_CDC_ECM_STAT_XMIT_ERROR](P174_CDC公共头文件与常量.md#abe83d17d2d5cf21938fd0c2f528fa949)。

<a id="r_a42de1fa8d3d9b8a290f2011072930b9d"></a>

```c
#define USB_CDC_ECM_STAT_RCV_ERROR 0x04
```

接收时出错的帧。

相关声明：[USB_CDC_ECM_STAT_RCV_ERROR](P174_CDC公共头文件与常量.md#a42de1fa8d3d9b8a290f2011072930b9d)。

<a id="r_a78e10547a06b6005f758e62d524b118e"></a>

```c
#define USB_CDC_ECM_STAT_RCV_NO_BUFFER 0x05
```

因没有缓冲区而丢失的帧。

相关声明：[USB_CDC_ECM_STAT_RCV_NO_BUFFER](P174_CDC公共头文件与常量.md#a78e10547a06b6005f758e62d524b118e)。

<a id="r_a8acf4c7d14eabe4eae249d42821819ca"></a>

```c
#define USB_CDC_ECM_STAT_DIRECTED_BYTES_XMIT 0x06
```

无错误发送的定向字节数（Directed Bytes）。

相关声明：[USB_CDC_ECM_STAT_DIRECTED_BYTES_XMIT](P174_CDC公共头文件与常量.md#a8acf4c7d14eabe4eae249d42821819ca)。

<a id="r_a90b2d280305cbf076c15c2ca9ebd8978"></a>

```c
#define USB_CDC_ECM_STAT_DIRECTED_FRAMES_XMIT 0x07
```

无错误发送的定向帧数（Directed Frames）。

相关声明：[USB_CDC_ECM_STAT_DIRECTED_FRAMES_XMIT](P174_CDC公共头文件与常量.md#a90b2d280305cbf076c15c2ca9ebd8978)。

<a id="r_a6e803a0b9acde93c8342e35d607de039"></a>

```c
#define USB_CDC_ECM_STAT_MULTICAST_BYTES_XMIT 0x08
```

无错误发送的组播字节数（Multicast Bytes）。

相关声明：[USB_CDC_ECM_STAT_MULTICAST_BYTES_XMIT](P174_CDC公共头文件与常量.md#a6e803a0b9acde93c8342e35d607de039)。

<a id="r_a3bb5879ce4c9508bb31da4ddf0ae8015"></a>

```c
#define USB_CDC_ECM_STAT_MULTICAST_FRAMES_XMIT 0x09
```

无错误发送的组播帧数（Multicast Frames）。

相关声明：[USB_CDC_ECM_STAT_MULTICAST_FRAMES_XMIT](P174_CDC公共头文件与常量.md#a3bb5879ce4c9508bb31da4ddf0ae8015)。

<a id="r_a4d37333fbbf9442f2a28a61e652a4426"></a>

```c
#define USB_CDC_ECM_STAT_BROADCAST_BYTES_XMIT 0x0A
```

无错误发送的广播字节数（Broadcast Bytes）。

相关声明：[USB_CDC_ECM_STAT_BROADCAST_BYTES_XMIT](P174_CDC公共头文件与常量.md#a4d37333fbbf9442f2a28a61e652a4426)。

<a id="r_ab4e3c05639f0c86614884910ae1cd937"></a>

```c
#define USB_CDC_ECM_STAT_BROADCAST_FRAMES_XMIT 0x0B
```

无错误发送的广播帧数（Broadcast Frames）。

相关声明：[USB_CDC_ECM_STAT_BROADCAST_FRAMES_XMIT](P174_CDC公共头文件与常量.md#ab4e3c05639f0c86614884910ae1cd937)。

<a id="r_af977e58284466c37ec967c3e336b97a4"></a>

```c
#define USB_CDC_ECM_STAT_DIRECTED_BYTES_RCV 0x0C
```

无错误接收的定向字节数。

相关声明：[USB_CDC_ECM_STAT_DIRECTED_BYTES_RCV](P174_CDC公共头文件与常量.md#af977e58284466c37ec967c3e336b97a4)。

<a id="r_a606d28a80fc09463af47ec8078004ce4"></a>

```c
#define USB_CDC_ECM_STAT_DIRECTED_FRAMES_RCV 0x0D
```

无错误接收的定向帧数。

相关声明：[USB_CDC_ECM_STAT_DIRECTED_FRAMES_RCV](P174_CDC公共头文件与常量.md#a606d28a80fc09463af47ec8078004ce4)。

<a id="r_a80b3b190bcb1bddf9ac799812fbf109e"></a>

```c
#define USB_CDC_ECM_STAT_MULTICAST_BYTES_RCV 0x0E
```

无错误接收的组播字节数。

相关声明：[USB_CDC_ECM_STAT_MULTICAST_BYTES_RCV](P174_CDC公共头文件与常量.md#a80b3b190bcb1bddf9ac799812fbf109e)。

<a id="r_a7d0140bb5fd40d0420eaa2c2fc027ab3"></a>

```c
#define USB_CDC_ECM_STAT_MULTICAST_FRAMES_RCV 0x0F
```

无错误接收的组播帧数。

相关声明：[USB_CDC_ECM_STAT_MULTICAST_FRAMES_RCV](P174_CDC公共头文件与常量.md#a7d0140bb5fd40d0420eaa2c2fc027ab3)。

<a id="r_a6ab384b2a8cc40b6bb3af2d8530c665f"></a>

```c
#define USB_CDC_ECM_STAT_BROADCAST_BYTES_RCV 0x10
```

无错误接收的广播字节数。

相关声明：[USB_CDC_ECM_STAT_BROADCAST_BYTES_RCV](P174_CDC公共头文件与常量.md#a6ab384b2a8cc40b6bb3af2d8530c665f)。

<a id="r_a7648fb96a19bccda7e9ed0aa08607f2a"></a>

```c
#define USB_CDC_ECM_STAT_BROADCAST_FRAMES_RCV 0x11
```

无错误接收的广播帧数。

相关声明：[USB_CDC_ECM_STAT_BROADCAST_FRAMES_RCV](P174_CDC公共头文件与常量.md#a7648fb96a19bccda7e9ed0aa08607f2a)。

<a id="r_a96abb72574dc846b5d60efd0f9155816"></a>

```c
#define USB_CDC_ECM_STAT_RCV_CRC_ERROR 0x12
```

接收到的具有循环冗余校验（Cyclic Redundancy Check，CRC）或帧校验序列（Frame Check Sequence，FCS）错误的帧。

相关声明：[USB_CDC_ECM_STAT_RCV_CRC_ERROR](P174_CDC公共头文件与常量.md#a96abb72574dc846b5d60efd0f9155816)。

<a id="r_a60c4b72c79b395e7d45dde83fc5e87d4"></a>

```c
#define USB_CDC_ECM_STAT_TRANSMIT_QUEUE_LENGTH 0x13
```

发送队列长度（Transmit Queue Length）。

相关声明：[USB_CDC_ECM_STAT_TRANSMIT_QUEUE_LENGTH](P174_CDC公共头文件与常量.md#a60c4b72c79b395e7d45dde83fc5e87d4)。

<a id="r_a45962112cfe844e249d5ff263516f82e"></a>

```c
#define USB_CDC_ECM_STAT_RCV_ERROR_ALIGNMENT 0x14
```

接收到的具有对齐错误（Alignment Error）的帧。

相关声明：[USB_CDC_ECM_STAT_RCV_ERROR_ALIGNMENT](P174_CDC公共头文件与常量.md#a45962112cfe844e249d5ff263516f82e)。

<a id="r_a24e59a0da48bd65d6a3f7934bbf98de5"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_ONE_COLLISION 0x15
```

经历一次冲突（Collision）后发送的帧。

相关声明：[USB_CDC_ECM_STAT_XMIT_ONE_COLLISION](P174_CDC公共头文件与常量.md#a24e59a0da48bd65d6a3f7934bbf98de5)。

<a id="r_aeecc735f46b53d71486b293a32406e9b"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_MORE_COLLISIONS 0x16
```

经历多次冲突后发送的帧。

相关声明：[USB_CDC_ECM_STAT_XMIT_MORE_COLLISIONS](P174_CDC公共头文件与常量.md#aeecc735f46b53d71486b293a32406e9b)。

<a id="r_a42c632d102aa9dafa70cfa77749ffd68"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_DEFERRED 0x17
```

推迟发送（Deferral）后发出的帧。

相关声明：[USB_CDC_ECM_STAT_XMIT_DEFERRED](P174_CDC公共头文件与常量.md#a42c632d102aa9dafa70cfa77749ffd68)。

<a id="r_ae59b357a968425200037bf9b9ae435c1"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_MAX_COLLISIONS 0x18
```

因冲突而未发送的帧。

相关声明：[USB_CDC_ECM_STAT_XMIT_MAX_COLLISIONS](P174_CDC公共头文件与常量.md#ae59b357a968425200037bf9b9ae435c1)。

<a id="r_a16857cb77498bff5f68ef178469ed76a"></a>

```c
#define USB_CDC_ECM_STAT_RCV_OVERRUN 0x19
```

因接收溢出（Overrun）而未接收的帧。

相关声明：[USB_CDC_ECM_STAT_RCV_OVERRUN](P174_CDC公共头文件与常量.md#a16857cb77498bff5f68ef178469ed76a)。

<a id="r_a62dfdfd23176ffeb599bc1c6b2e37778"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_UNDERRUN 0x1A
```

因发送欠载（Underrun）而未发送的帧。

相关声明：[USB_CDC_ECM_STAT_XMIT_UNDERRUN](P174_CDC公共头文件与常量.md#a62dfdfd23176ffeb599bc1c6b2e37778)。

<a id="r_a6ae1493bbd0908f77ba698b918a37de2"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_HEARTBEAT_FAILURE 0x1B
```

伴随心跳失败（Heartbeat Failure）发送的帧。

相关声明：[USB_CDC_ECM_STAT_XMIT_HEARTBEAT_FAILURE](P174_CDC公共头文件与常量.md#a6ae1493bbd0908f77ba698b918a37de2)。

<a id="r_acb41a221f1d8a8b4b91619b36440018c"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_TIMES_CRS_LOST 0x1C
```

发送期间载波侦听信号（Carrier Sense Signal）丢失的次数。

相关声明：[USB_CDC_ECM_STAT_XMIT_TIMES_CRS_LOST](P174_CDC公共头文件与常量.md#acb41a221f1d8a8b4b91619b36440018c)。

<a id="r_a39fb612d95ebfb5eebb12679dfd0996e"></a>

```c
#define USB_CDC_ECM_STAT_XMIT_LATE_COLLISIONS 0x1D
```

检测到的迟发冲突（Late Collisions）。

相关声明：[USB_CDC_ECM_STAT_XMIT_LATE_COLLISIONS](P174_CDC公共头文件与常量.md#a39fb612d95ebfb5eebb12679dfd0996e)。

<a id="define-members-0"></a>

**NCM 功能描述符的网络能力位图（Network Capabilities Bitmap）。**

**注意：NCM100.pdf，第 5.2.1 节，表 5-2。**

<a id="r_ac8f5072c29a253caa7ff5b86c970833b"></a>

```c
#define USB_CDC_NCM_NCAP_ETH_FILTER BIT(0)
```

该功能可处理 SetEthernetPacketFilter 请求。

相关声明：[USB_CDC_NCM_NCAP_ETH_FILTER](P174_CDC公共头文件与常量.md#ac8f5072c29a253caa7ff5b86c970833b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a025cef345a9e8fa2aaa80cbd415fd96a"></a>

```c
#define USB_CDC_NCM_NCAP_NET_ADDRESS BIT(1)
```

该功能可处理 GetNetAddress 和 SetNetAddress 请求。

相关声明：[USB_CDC_NCM_NCAP_NET_ADDRESS](P174_CDC公共头文件与常量.md#a025cef345a9e8fa2aaa80cbd415fd96a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a777dc95478bf44c064e741792d1e5040"></a>

```c
#define USB_CDC_NCM_NCAP_ENCAP_COMMAND BIT(2)
```

该功能可处理 SendEncapsulatedCommand 和 GetEncapsulatedResponse 请求。

相关声明：[USB_CDC_NCM_NCAP_ENCAP_COMMAND](P174_CDC公共头文件与常量.md#a777dc95478bf44c064e741792d1e5040)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aff5d253ea0c61b7280ef9228baf01310"></a>

```c
#define USB_CDC_NCM_NCAP_MAX_DATAGRAM_SIZE BIT(3)
```

该功能可处理 SetMaxDatagramSize 和 GetMaxDatagramSize 请求。

相关声明：[USB_CDC_NCM_NCAP_MAX_DATAGRAM_SIZE](P174_CDC公共头文件与常量.md#aff5d253ea0c61b7280ef9228baf01310)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aded07d3176c06558cfe2ac61787b4ddb"></a>

```c
#define USB_CDC_NCM_NCAP_CRC_MODE BIT(4)
```

该功能可处理 SetCrcMode 和 GetCrcMode 请求。

相关声明：[USB_CDC_NCM_NCAP_CRC_MODE](P174_CDC公共头文件与常量.md#aded07d3176c06558cfe2ac61787b4ddb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_af5988c179c02598b7ffa3441cebbe756"></a>

```c
#define USB_CDC_NCM_NCAP_NTB_INPUT_SIZE BIT(5)
```

该功能可处理 8 字节形式的 GetNtbInputSize 和 SetNtbInputSize 请求。

相关声明：[USB_CDC_NCM_NCAP_NTB_INPUT_SIZE](P174_CDC公共头文件与常量.md#af5988c179c02598b7ffa3441cebbe756)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

## 174.4\_详细说明（Detailed Documentation）

<a id="a057b9de28602442b66a8c3a7befd62a7"></a>

### 174.4.1\_`ACM_FUNC_DESC`

```c
#define ACM_FUNC_DESC 0x02
```

<a id="a01b7a28004a035df52334b64308e4b22"></a>

### 174.4.2\_`ACM_SUBCLASS`

```c
#define ACM_SUBCLASS 0x02
```

通信类子类代码（Communications Class Subclass Codes）。

<a id="a20396bb325a1e947b2e4b0017a134082"></a>

### 174.4.3\_`ACM_VENDOR_PROTOCOL`

```c
#define ACM_VENDOR_PROTOCOL 0xFF
```

<a id="aaf98d38c2b9c859cf86e281bb67f27b0"></a>

### 174.4.4\_`AT_CMD_V250_PROTOCOL`

```c
#define AT_CMD_V250_PROTOCOL 0x01
```

通信类协议代码（Communications Class Protocol Codes）。

<a id="a60552aa9506dc2c6dede5146c5251aaf"></a>

### 174.4.5\_`CALL_MANAGEMENT_FUNC_DESC`

```c
#define CALL_MANAGEMENT_FUNC_DESC 0x01
```

<a id="ac9008f0dc0d4fc7141de9dd12352caa8"></a>

### 174.4.6\_`CDC_GET_ENC_RSP`

```c
#define CDC_GET_ENC_RSP 0x01
```

<a id="a926f6444745d1cdc991d97e4f1d265ad"></a>

### 174.4.7\_`CDC_SEND_ENC_CMD`

```c
#define CDC_SEND_ENC_CMD 0x00
```

ACM 设备的 PSTN 子类专用请求（PSTN Subclass Specific Requests）。

**注意（Note）**：PSTN120.pdf，第 6.3 节，表 13。

<a id="a2d44425b0b0c5e525885c5764348ec54"></a>

### 174.4.8\_`CDC_SRN_1_20`

```c
#define CDC_SRN_1_20 0x0120 __DEPRECATED_MACRO
```

以二进制编码的十进制格式（Binary-coded Decimal，BCD）表示的 CDC 规范版本号。

> 译注（源码核对）：原始声明带有 `__DEPRECATED_MACRO` 弃用标记，数值仍按原文保留。该标记针对这个宏，不能据此把整个 CDC 公共头文件或所有 CDC 功能都标为弃用。

<a id="ae4044b943c9e54cb7a64c8c35acaf8bc"></a>

### 174.4.9\_`DATA_INTERFACE_CLASS`

```c
#define DATA_INTERFACE_CLASS 0x0A
```

数据类接口代码（Data Class Interface Codes）。

**注意（Note）**：CDC120-20101103-track.pdf，第 4.5 节，表 6。

<a id="a39f776a70d5139575ed84be1a9faee5d"></a>

### 174.4.10\_`ECM_SUBCLASS`

```c
#define ECM_SUBCLASS 0x06
```

<a id="ab4f22c3c42b5a4efe7735bafebc1cb9b"></a>

### 174.4.11\_`EEM_PROTOCOL`

```c
#define EEM_PROTOCOL 0x07
```

<a id="a73503e51ff8700620866be15a8d7ab43"></a>

### 174.4.12\_`EEM_SUBCLASS`

```c
#define EEM_SUBCLASS 0x0c
```

<a id="a22b2b55d7ab3cdd4206df07cddcc44e9"></a>

### 174.4.13\_`ETHERNET_FUNC_DESC`

```c
#define ETHERNET_FUNC_DESC 0x0F
```

<a id="ad788a76ba44ab5d02c699b110856e18e"></a>

### 174.4.14\_`ETHERNET_FUNC_DESC_NCM`

```c
#define ETHERNET_FUNC_DESC_NCM 0x1a
```

<a id="a9dd7dad1bd3421f42a67f280826d464b"></a>

### 174.4.15\_`GET_CRC_MODE`

```c
#define GET_CRC_MODE 0x89
```

<a id="a53ea6ae0e1fe8a88350740fd594507fd"></a>

### 174.4.16\_`GET_ETHERNET_PM_FILTER`

```c
#define GET_ETHERNET_PM_FILTER 0x42
```

<a id="a7dffeba1576d6660fb930eabc5c515b7"></a>

### 174.4.17\_`GET_ETHERNET_STATISTIC`

```c
#define GET_ETHERNET_STATISTIC 0x44
```

<a id="a6698d8d2ca56fafdc943aec2cede1daf"></a>

### 174.4.18\_`GET_LINE_CODING`

```c
#define GET_LINE_CODING 0x21
```

<a id="aca024f2e7bb9f99d3376753589fa7c3f"></a>

### 174.4.19\_`GET_MAX_DATAGRAM_SIZE`

```c
#define GET_MAX_DATAGRAM_SIZE 0x87
```

<a id="a58701f26151379cd5dd8b7a7350dcda5"></a>

### 174.4.20\_`GET_NET_ADDRESS`

```c
#define GET_NET_ADDRESS 0x81
```

<a id="a2ba9ad377b20364fc811ec6d5bb74995"></a>

### 174.4.21\_`GET_NTB_FORMAT`

```c
#define GET_NTB_FORMAT 0x83
```

<a id="ae5ab2b5f3c10b1fc42d5873f8e8082c0"></a>

### 174.4.22\_`GET_NTB_INPUT_SIZE`

```c
#define GET_NTB_INPUT_SIZE 0x85
```

<a id="a44e5dd539b8b41ccc9c61dd95ee4fb2e"></a>

### 174.4.23\_`GET_NTB_PARAMETERS`

```c
#define GET_NTB_PARAMETERS 0x80
```

NCM 子类的类专用请求代码。

**注意（Note）**：NCM100.pdf，第 6.2 节，表 6-2。

<a id="a008b7d343c5a1876a78c885f7a496b66"></a>

### 174.4.24\_`HEADER_FUNC_DESC`

```c
#define HEADER_FUNC_DESC 0x00
```

通信类功能描述符的 bDescriptor SubType（描述符子类型）。

**注意（Note）**：CDC120-20101103-track.pdf，第 5.2.3 节，表 13。

<a id="a6577856e991bddc829d93af0ea527ef6"></a>

### 174.4.25\_`NCM_DATA_PROTOCOL`

```c
#define NCM_DATA_PROTOCOL 0x01
```

<a id="af4edeebbc1d4fb6f3a727083a36e731e"></a>

### 174.4.26\_`NCM_SUBCLASS`

```c
#define NCM_SUBCLASS 0x0d
```

<a id="aac32de24c40e08d0d32d3db264fa964a"></a>

### 174.4.27\_`PACKET_TYPE_ALL_MULTICAST`

```c
#define PACKET_TYPE_ALL_MULTICAST 0x02
```

<a id="a3143cff5f7275d394f259c3b83e54e4b"></a>

### 174.4.28\_`PACKET_TYPE_BROADCAST`

```c
#define PACKET_TYPE_BROADCAST 0x08
```

<a id="a5a2d0aa22741a4a48b976cddc6f57f98"></a>

### 174.4.29\_`PACKET_TYPE_DIRECTED`

```c
#define PACKET_TYPE_DIRECTED 0x04
```

<a id="a4abfd25c9ca3e70c5b33b89ee9456087"></a>

### 174.4.30\_`PACKET_TYPE_MULTICAST`

```c
#define PACKET_TYPE_MULTICAST 0x10
```

以太网包过滤器位图（Ethernet Packet Filter Bitmap）。

<a id="a7be4d4e65526efb94ea1ef71da62f835"></a>

### 174.4.31\_`PACKET_TYPE_PROMISCUOUS`

```c
#define PACKET_TYPE_PROMISCUOUS 0x01
```

<a id="aa66ab791abfcf7ef5a37758c1b33138a"></a>

### 174.4.32\_`SERIAL_STATE_BREAK`

```c
#define SERIAL_STATE_BREAK 0x04
```

<a id="aacd68fe3a081441ee684bf2ef6312bec"></a>

### 174.4.33\_`SERIAL_STATE_FRAMING`

```c
#define SERIAL_STATE_FRAMING 0x10
```

<a id="ae38825267009563e0aa82a58a7fc4fd2"></a>

### 174.4.34\_`SERIAL_STATE_OVER_RUN`

```c
#define SERIAL_STATE_OVER_RUN 0x40
```

UART 状态位图值（State Bitmap Values）。

<a id="a738f180df5795376763ff233fb8aa68d"></a>

### 174.4.35\_`SERIAL_STATE_PARITY`

```c
#define SERIAL_STATE_PARITY 0x20
```

<a id="a935c772da45984e8d796396146413037"></a>

### 174.4.36\_`SERIAL_STATE_RING_SIGNAL`

```c
#define SERIAL_STATE_RING_SIGNAL 0x08
```

<a id="a9677c612766f3e788ad2960a17ad0791"></a>

### 174.4.37\_`SERIAL_STATE_RX_CARRIER`

```c
#define SERIAL_STATE_RX_CARRIER 0x01
```

<a id="a22cd80b90c53ff44a4c1de08310ba3c2"></a>

### 174.4.38\_`SERIAL_STATE_TX_CARRIER`

```c
#define SERIAL_STATE_TX_CARRIER 0x02
```

<a id="a437869c339749d5d011060cd5676659e"></a>

### 174.4.39\_`SET_CONTROL_LINE_STATE`

```c
#define SET_CONTROL_LINE_STATE 0x22
```

<a id="a07623c40153f936c863627a3dc30da7a"></a>

### 174.4.40\_`SET_CONTROL_LINE_STATE_DTR`

```c
#define SET_CONTROL_LINE_STATE_DTR 0x01
```

<a id="a00788c95fb39c2636d7d5a427282399f"></a>

### 174.4.41\_`SET_CONTROL_LINE_STATE_RTS`

```c
#define SET_CONTROL_LINE_STATE_RTS 0x02
```

SetControlLineState 的控制信号位图值（Control Signal Bitmap Values）。

<a id="a634a3403221f33ae8506481b38840c2c"></a>

### 174.4.42\_`SET_CRC_MODE`

```c
#define SET_CRC_MODE 0x8A
```

<a id="a4dce35ee8cf2337bab3c90081200a9f6"></a>

### 174.4.43\_`SET_ETHERNET_MULTICAST_FILTERS`

```c
#define SET_ETHERNET_MULTICAST_FILTERS 0x40
```

以太网子类的类专用请求代码（Class-Specific Request Codes）。

**注意（Note）**：ECM120.pdf，第 6.2 节，表 6。

<a id="adae019242224bbbc9d0f853da3733f1c"></a>

### 174.4.44\_`SET_ETHERNET_PACKET_FILTER`

```c
#define SET_ETHERNET_PACKET_FILTER 0x43
```

<a id="a1506deda422ee354040b0feeb09ad4b6"></a>

### 174.4.45\_`SET_ETHERNET_PM_FILTER`

```c
#define SET_ETHERNET_PM_FILTER 0x41
```

<a id="a91a9c047339a1a5918b6a923af6d1af6"></a>

### 174.4.46\_`SET_LINE_CODING`

```c
#define SET_LINE_CODING 0x20
```

<a id="a4d224c04ec87088b4494f43c59c59b86"></a>

### 174.4.47\_`SET_MAX_DATAGRAM_SIZE`

```c
#define SET_MAX_DATAGRAM_SIZE 0x88
```

<a id="a2d8525d02e54ec44143a7732a15ad5b0"></a>

### 174.4.48\_`SET_NET_ADDRESS`

```c
#define SET_NET_ADDRESS 0x82
```

<a id="a9c48d4f5685678b1429ba90f7c0a7d9b"></a>

### 174.4.49\_`SET_NTB_FORMAT`

```c
#define SET_NTB_FORMAT 0x84
```

<a id="a485fd89a465fb5ad82c09a686ba3bc1b"></a>

### 174.4.50\_`SET_NTB_INPUT_SIZE`

```c
#define SET_NTB_INPUT_SIZE 0x86
```

<a id="aab7f21ab95fc5916f758e66087caef25"></a>

### 174.4.51\_`UNION_FUNC_DESC`

```c
#define UNION_FUNC_DESC 0x06
```

<a id="afdeb5f862a52b953653b9ab567979cec"></a>

### 174.4.52\_`USB_CDC_AUX_JACK_HOOK_STATE`

```c
#define USB_CDC_AUX_JACK_HOOK_STATE 0x08
```

PSTN 子类的类专用通知代码（Class-Specific Notification Codes）。

**注意（Note）**：PSTN120.pdf，第 6.5 节，表 30；辅助插孔摘挂机状态通知（Auxiliary Jack Hook State Notification）。

<a id="a6bb6650664f82fd25330af0357e5831e"></a>

### 174.4.53\_`USB_CDC_CALL_STATE_CHANGE`

```c
#define USB_CDC_CALL_STATE_CHANGE 0x28
```

呼叫状态变化通知（Call State Change Notification）。

<a id="af4d27c4b8118b7fa6574c4892291adf9"></a>

### 174.4.54\_`USB_CDC_CONNECTION_SPEED_CHANGE`

```c
#define USB_CDC_CONNECTION_SPEED_CHANGE 0x2A
```

连接速率变化通知（Connection Speed Change Notification）。

<a id="a6ab384b2a8cc40b6bb3af2d8530c665f"></a>

### 174.4.55\_`USB_CDC_ECM_STAT_BROADCAST_BYTES_RCV`

```c
#define USB_CDC_ECM_STAT_BROADCAST_BYTES_RCV 0x10
```

无错误接收的广播字节数。

<a id="a4d37333fbbf9442f2a28a61e652a4426"></a>

### 174.4.56\_`USB_CDC_ECM_STAT_BROADCAST_BYTES_XMIT`

```c
#define USB_CDC_ECM_STAT_BROADCAST_BYTES_XMIT 0x0A
```

无错误发送的广播字节数（Broadcast Bytes）。

<a id="a7648fb96a19bccda7e9ed0aa08607f2a"></a>

### 174.4.57\_`USB_CDC_ECM_STAT_BROADCAST_FRAMES_RCV`

```c
#define USB_CDC_ECM_STAT_BROADCAST_FRAMES_RCV 0x11
```

无错误接收的广播帧数。

<a id="ab4e3c05639f0c86614884910ae1cd937"></a>

### 174.4.58\_`USB_CDC_ECM_STAT_BROADCAST_FRAMES_XMIT`

```c
#define USB_CDC_ECM_STAT_BROADCAST_FRAMES_XMIT 0x0B
```

无错误发送的广播帧数（Broadcast Frames）。

<a id="af977e58284466c37ec967c3e336b97a4"></a>

### 174.4.59\_`USB_CDC_ECM_STAT_DIRECTED_BYTES_RCV`

```c
#define USB_CDC_ECM_STAT_DIRECTED_BYTES_RCV 0x0C
```

无错误接收的定向字节数。

<a id="a8acf4c7d14eabe4eae249d42821819ca"></a>

### 174.4.60\_`USB_CDC_ECM_STAT_DIRECTED_BYTES_XMIT`

```c
#define USB_CDC_ECM_STAT_DIRECTED_BYTES_XMIT 0x06
```

无错误发送的定向字节数（Directed Bytes）。

<a id="a606d28a80fc09463af47ec8078004ce4"></a>

### 174.4.61\_`USB_CDC_ECM_STAT_DIRECTED_FRAMES_RCV`

```c
#define USB_CDC_ECM_STAT_DIRECTED_FRAMES_RCV 0x0D
```

无错误接收的定向帧数。

<a id="a90b2d280305cbf076c15c2ca9ebd8978"></a>

### 174.4.62\_`USB_CDC_ECM_STAT_DIRECTED_FRAMES_XMIT`

```c
#define USB_CDC_ECM_STAT_DIRECTED_FRAMES_XMIT 0x07
```

无错误发送的定向帧数（Directed Frames）。

<a id="a80b3b190bcb1bddf9ac799812fbf109e"></a>

### 174.4.63\_`USB_CDC_ECM_STAT_MULTICAST_BYTES_RCV`

```c
#define USB_CDC_ECM_STAT_MULTICAST_BYTES_RCV 0x0E
```

无错误接收的组播字节数。

<a id="a6e803a0b9acde93c8342e35d607de039"></a>

### 174.4.64\_`USB_CDC_ECM_STAT_MULTICAST_BYTES_XMIT`

```c
#define USB_CDC_ECM_STAT_MULTICAST_BYTES_XMIT 0x08
```

无错误发送的组播字节数（Multicast Bytes）。

<a id="a7d0140bb5fd40d0420eaa2c2fc027ab3"></a>

### 174.4.65\_`USB_CDC_ECM_STAT_MULTICAST_FRAMES_RCV`

```c
#define USB_CDC_ECM_STAT_MULTICAST_FRAMES_RCV 0x0F
```

无错误接收的组播帧数。

<a id="a3bb5879ce4c9508bb31da4ddf0ae8015"></a>

### 174.4.66\_`USB_CDC_ECM_STAT_MULTICAST_FRAMES_XMIT`

```c
#define USB_CDC_ECM_STAT_MULTICAST_FRAMES_XMIT 0x09
```

无错误发送的组播帧数（Multicast Frames）。

<a id="a96abb72574dc846b5d60efd0f9155816"></a>

### 174.4.67\_`USB_CDC_ECM_STAT_RCV_CRC_ERROR`

```c
#define USB_CDC_ECM_STAT_RCV_CRC_ERROR 0x12
```

接收到的具有循环冗余校验（Cyclic Redundancy Check，CRC）或帧校验序列（Frame Check Sequence，FCS）错误的帧。

> 译注（源码核对）：原注释将 CRC 英文写作 circular redundancy check；常用术语为 Cyclic Redundancy Check，正文按“循环冗余校验”翻译，并在此标明原文拼写差异。

<a id="a42de1fa8d3d9b8a290f2011072930b9d"></a>

### 174.4.68\_`USB_CDC_ECM_STAT_RCV_ERROR`

```c
#define USB_CDC_ECM_STAT_RCV_ERROR 0x04
```

接收时出错的帧。

<a id="a45962112cfe844e249d5ff263516f82e"></a>

### 174.4.69\_`USB_CDC_ECM_STAT_RCV_ERROR_ALIGNMENT`

```c
#define USB_CDC_ECM_STAT_RCV_ERROR_ALIGNMENT 0x14
```

接收到的具有对齐错误（Alignment Error）的帧。

<a id="a78e10547a06b6005f758e62d524b118e"></a>

### 174.4.70\_`USB_CDC_ECM_STAT_RCV_NO_BUFFER`

```c
#define USB_CDC_ECM_STAT_RCV_NO_BUFFER 0x05
```

因没有缓冲区而丢失的帧。

<a id="addc379e31c784df36649bf4fc2e85bc4"></a>

### 174.4.71\_`USB_CDC_ECM_STAT_RCV_OK`

```c
#define USB_CDC_ECM_STAT_RCV_OK 0x02
```

无错误接收的帧。

<a id="a16857cb77498bff5f68ef178469ed76a"></a>

### 174.4.72\_`USB_CDC_ECM_STAT_RCV_OVERRUN`

```c
#define USB_CDC_ECM_STAT_RCV_OVERRUN 0x19
```

因接收溢出（Overrun）而未接收的帧。

<a id="a8a3a6287eea23dfb919f37690e6a1f09"></a>

### 174.4.73\_`USB_CDC_ECM_STAT_RESERVED`

```c
#define USB_CDC_ECM_STAT_RESERVED 0x00
```

ECM 子类的以太网统计特性选择器代码（Ethernet Statistics Feature Selector Codes）。

**注意（Note）**：ECM120.pdf，第 6.2.5 节，表 9；保留供将来使用（Reserved for Future Use）。

<a id="a60c4b72c79b395e7d45dde83fc5e87d4"></a>

### 174.4.74\_`USB_CDC_ECM_STAT_TRANSMIT_QUEUE_LENGTH`

```c
#define USB_CDC_ECM_STAT_TRANSMIT_QUEUE_LENGTH 0x13
```

发送队列长度（Transmit Queue Length）。

<a id="a42c632d102aa9dafa70cfa77749ffd68"></a>

### 174.4.75\_`USB_CDC_ECM_STAT_XMIT_DEFERRED`

```c
#define USB_CDC_ECM_STAT_XMIT_DEFERRED 0x17
```

推迟发送（Deferral）后发出的帧。

<a id="abe83d17d2d5cf21938fd0c2f528fa949"></a>

### 174.4.76\_`USB_CDC_ECM_STAT_XMIT_ERROR`

```c
#define USB_CDC_ECM_STAT_XMIT_ERROR 0x03
```

未发送或发送时出错的帧。

<a id="a6ae1493bbd0908f77ba698b918a37de2"></a>

### 174.4.77\_`USB_CDC_ECM_STAT_XMIT_HEARTBEAT_FAILURE`

```c
#define USB_CDC_ECM_STAT_XMIT_HEARTBEAT_FAILURE 0x1B
```

伴随心跳失败（Heartbeat Failure）发送的帧。

<a id="a39fb612d95ebfb5eebb12679dfd0996e"></a>

### 174.4.78\_`USB_CDC_ECM_STAT_XMIT_LATE_COLLISIONS`

```c
#define USB_CDC_ECM_STAT_XMIT_LATE_COLLISIONS 0x1D
```

检测到的迟发冲突（Late Collisions）。

<a id="ae59b357a968425200037bf9b9ae435c1"></a>

### 174.4.79\_`USB_CDC_ECM_STAT_XMIT_MAX_COLLISIONS`

```c
#define USB_CDC_ECM_STAT_XMIT_MAX_COLLISIONS 0x18
```

因冲突而未发送的帧。

<a id="aeecc735f46b53d71486b293a32406e9b"></a>

### 174.4.80\_`USB_CDC_ECM_STAT_XMIT_MORE_COLLISIONS`

```c
#define USB_CDC_ECM_STAT_XMIT_MORE_COLLISIONS 0x16
```

经历多次冲突后发送的帧。

<a id="a9dd668f37ce388faee799e4e65cd2dd3"></a>

### 174.4.81\_`USB_CDC_ECM_STAT_XMIT_OK`

```c
#define USB_CDC_ECM_STAT_XMIT_OK 0x01
```

无错误发送的帧。

<a id="a24e59a0da48bd65d6a3f7934bbf98de5"></a>

### 174.4.82\_`USB_CDC_ECM_STAT_XMIT_ONE_COLLISION`

```c
#define USB_CDC_ECM_STAT_XMIT_ONE_COLLISION 0x15
```

经历一次冲突（Collision）后发送的帧。

<a id="acb41a221f1d8a8b4b91619b36440018c"></a>

### 174.4.83\_`USB_CDC_ECM_STAT_XMIT_TIMES_CRS_LOST`

```c
#define USB_CDC_ECM_STAT_XMIT_TIMES_CRS_LOST 0x1C
```

发送期间载波侦听信号（Carrier Sense Signal）丢失的次数。

<a id="a62dfdfd23176ffeb599bc1c6b2e37778"></a>

### 174.4.84\_`USB_CDC_ECM_STAT_XMIT_UNDERRUN`

```c
#define USB_CDC_ECM_STAT_XMIT_UNDERRUN 0x1A
```

因发送欠载（Underrun）而未发送的帧。

<a id="a327c495a9930b3e5519f0a9c7cd9ed18"></a>

### 174.4.85\_`USB_CDC_LINE_CODING_DATA_BITS_5`

```c
#define USB_CDC_LINE_CODING_DATA_BITS_5 5
```

<a id="a231932add6d9ceef4f5332a0db1b9f55"></a>

### 174.4.86\_`USB_CDC_LINE_CODING_DATA_BITS_6`

```c
#define USB_CDC_LINE_CODING_DATA_BITS_6 6
```

<a id="a6a276593bc4587671df5e6da8cce5ebb"></a>

### 174.4.87\_`USB_CDC_LINE_CODING_DATA_BITS_7`

```c
#define USB_CDC_LINE_CODING_DATA_BITS_7 7
```

<a id="a64e296aec72bbd8f9bdc1aefa5aab654"></a>

### 174.4.88\_`USB_CDC_LINE_CODING_DATA_BITS_8`

```c
#define USB_CDC_LINE_CODING_DATA_BITS_8 8
```

<a id="a327b5f99ab7e5cfc99d7592d1f9c1c25"></a>

### 174.4.89\_`USB_CDC_LINE_CODING_PARITY_EVEN`

```c
#define USB_CDC_LINE_CODING_PARITY_EVEN 2
```

<a id="a490d381698ce91db4ab8bb24dd70820a"></a>

### 174.4.90\_`USB_CDC_LINE_CODING_PARITY_MARK`

```c
#define USB_CDC_LINE_CODING_PARITY_MARK 3
```

<a id="a549181d2cc92c42b4db8c3c34927d97f"></a>

### 174.4.91\_`USB_CDC_LINE_CODING_PARITY_NO`

```c
#define USB_CDC_LINE_CODING_PARITY_NO 0
```

<a id="a44d808ad4f27ecf3502b9c14da2aa9b9"></a>

### 174.4.92\_`USB_CDC_LINE_CODING_PARITY_ODD`

```c
#define USB_CDC_LINE_CODING_PARITY_ODD 1
```

<a id="a5aa1b5cf30cb4020442131f66170fec6"></a>

### 174.4.93\_`USB_CDC_LINE_CODING_PARITY_SPACE`

```c
#define USB_CDC_LINE_CODING_PARITY_SPACE 4
```

<a id="a8a06b3413e1c665f13ba4895c220d608"></a>

### 174.4.94\_`USB_CDC_LINE_CODING_STOP_BITS_1`

```c
#define USB_CDC_LINE_CODING_STOP_BITS_1 0
```

PSTN 子类线路编码值（Line Coding Values）。

**注意（Note）**：PSTN120.pdf，第 6.3.11 节，表 17。

<a id="a4159f50590d647510a6a1f38875e012e"></a>

### 174.4.95\_`USB_CDC_LINE_CODING_STOP_BITS_1_5`

```c
#define USB_CDC_LINE_CODING_STOP_BITS_1_5 1
```

<a id="a7e7fc73b4490a694aa982b4862782157"></a>

### 174.4.96\_`USB_CDC_LINE_CODING_STOP_BITS_2`

```c
#define USB_CDC_LINE_CODING_STOP_BITS_2 2
```

<a id="a89554d686630d67d642e228b7ee0dc2c"></a>

### 174.4.97\_`USB_CDC_LINE_CTRL_BAUD_RATE`

```c
#define USB_CDC_LINE_CTRL_BAUD_RATE UART_LINE_CTRL_BAUD_RATE
```

为 uart_line_ctrl 枚举补充 CDC 专用值。

> 译注（源码核对）：`USB_CDC_LINE_CTRL_*` 是供 UART 线路控制接口使用的值；`USB_CDC_SERIAL_STATE_*` 则用于 USB 串行状态通知的协议位图。驱动 cdc_acm_line_ctrl_set() 在两者之间映射，不能因为名称相近就把不同位图直接互换。

<a id="a716d9aaf772e1fa3f8b555077048ecbb"></a>

### 174.4.98\_`USB_CDC_LINE_CTRL_BREAK`

```c
#define USB_CDC_LINE_CTRL_BREAK BIT(5)
```

<a id="a7e6b9bb33debc489b7ac7e0fb0e94947"></a>

### 174.4.99\_`USB_CDC_LINE_CTRL_DCD`

```c
#define USB_CDC_LINE_CTRL_DCD UART_LINE_CTRL_DCD
```

<a id="a6876caf1b77477e259bb391216309799"></a>

### 174.4.100\_`USB_CDC_LINE_CTRL_DSR`

```c
#define USB_CDC_LINE_CTRL_DSR UART_LINE_CTRL_DSR
```

<a id="a263186a0a64d9a8e7e9e97a54b951bdf"></a>

### 174.4.101\_`USB_CDC_LINE_CTRL_FRAMING`

```c
#define USB_CDC_LINE_CTRL_FRAMING BIT(7)
```

<a id="a8bf1722f98bf48394605efddf6be1295"></a>

### 174.4.102\_`USB_CDC_LINE_CTRL_OVER_RUN`

```c
#define USB_CDC_LINE_CTRL_OVER_RUN BIT(9)
```

<a id="ae2779672a5b5ab49a2ed7240e463f9e8"></a>

### 174.4.103\_`USB_CDC_LINE_CTRL_PARITY`

```c
#define USB_CDC_LINE_CTRL_PARITY BIT(8)
```

<a id="a8ec9b8c619c567cc174c0473dda5a5fd"></a>

### 174.4.104\_`USB_CDC_LINE_CTRL_RING_SIGNAL`

```c
#define USB_CDC_LINE_CTRL_RING_SIGNAL BIT(6)
```

<a id="ac63891d7c3321f7f4eb297f87c0978f6"></a>

### 174.4.105\_`USB_CDC_LINE_STATE_CHANGE`

```c
#define USB_CDC_LINE_STATE_CHANGE 0x23
```

线路状态变化通知（Line State Change Notification）。

<a id="aded07d3176c06558cfe2ac61787b4ddb"></a>

### 174.4.106\_`USB_CDC_NCM_NCAP_CRC_MODE`

```c
#define USB_CDC_NCM_NCAP_CRC_MODE BIT(4)
```

该功能可处理 SetCrcMode 和 GetCrcMode 请求。

<a id="a777dc95478bf44c064e741792d1e5040"></a>

### 174.4.107\_`USB_CDC_NCM_NCAP_ENCAP_COMMAND`

```c
#define USB_CDC_NCM_NCAP_ENCAP_COMMAND BIT(2)
```

该功能可处理 SendEncapsulatedCommand 和 GetEncapsulatedResponse 请求。

<a id="ac8f5072c29a253caa7ff5b86c970833b"></a>

### 174.4.108\_`USB_CDC_NCM_NCAP_ETH_FILTER`

```c
#define USB_CDC_NCM_NCAP_ETH_FILTER BIT(0)
```

该功能可处理 SetEthernetPacketFilter 请求。

<a id="aff5d253ea0c61b7280ef9228baf01310"></a>

### 174.4.109\_`USB_CDC_NCM_NCAP_MAX_DATAGRAM_SIZE`

```c
#define USB_CDC_NCM_NCAP_MAX_DATAGRAM_SIZE BIT(3)
```

该功能可处理 SetMaxDatagramSize 和 GetMaxDatagramSize 请求。

<a id="a025cef345a9e8fa2aaa80cbd415fd96a"></a>

### 174.4.110\_`USB_CDC_NCM_NCAP_NET_ADDRESS`

```c
#define USB_CDC_NCM_NCAP_NET_ADDRESS BIT(1)
```

该功能可处理 GetNetAddress 和 SetNetAddress 请求。

<a id="af5988c179c02598b7ffa3441cebbe756"></a>

### 174.4.111\_`USB_CDC_NCM_NCAP_NTB_INPUT_SIZE`

```c
#define USB_CDC_NCM_NCAP_NTB_INPUT_SIZE BIT(5)
```

该功能可处理 8 字节形式的 GetNtbInputSize 和 SetNtbInputSize 请求。

<a id="a7e9384e6a613e38c543d7eba05f64c07"></a>

### 174.4.112\_`USB_CDC_NETWORK_CONNECTION`

```c
#define USB_CDC_NETWORK_CONNECTION 0x00
```

通信类通知代码（Communications Class Notification Codes）。

**注意（Note）**：CDC120-20101103-track.pdf，第 6.3 节，表 20；网络连接通知（Network Connection Notification）。

<a id="a970045b850b0195b5a4a2913d5a0b918"></a>

### 174.4.113\_`USB_CDC_RESPONSE_AVAILABLE`

```c
#define USB_CDC_RESPONSE_AVAILABLE 0x01
```

响应可用通知（Response Available Notification）。

<a id="a52452ce9272b97203fece115b5005aff"></a>

### 174.4.114\_`USB_CDC_RING_DETECT`

```c
#define USB_CDC_RING_DETECT 0x09
```

振铃检测通知（Ring Detect Notification）。

<a id="ac167f480370c73b830281d98ad5899b1"></a>

### 174.4.115\_`USB_CDC_SERIAL_STATE`

```c
#define USB_CDC_SERIAL_STATE 0x20
```

串行状态通知（Serial State Notification）。

<a id="a15f3c90969106ecdf3b1cdf258cad5df"></a>

### 174.4.116\_`USB_CDC_SERIAL_STATE_BREAK`

```c
#define USB_CDC_SERIAL_STATE_BREAK BIT(2)
```

<a id="a59f5f1ebab838621cdc67668541432ca"></a>

### 174.4.117\_`USB_CDC_SERIAL_STATE_FRAMING`

```c
#define USB_CDC_SERIAL_STATE_FRAMING BIT(4)
```

<a id="a504f682d66f714730f35d282ce0b9177"></a>

### 174.4.118\_`USB_CDC_SERIAL_STATE_OVERRUN`

```c
#define USB_CDC_SERIAL_STATE_OVERRUN BIT(6)
```

PSTN 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）状态位图值。

**注意（Note）**：PSTN120.pdf，第 6.5.4 节，表 31。

<a id="a1ff82c5d551211d2298128bd84eeb60a"></a>

### 174.4.119\_`USB_CDC_SERIAL_STATE_PARITY`

```c
#define USB_CDC_SERIAL_STATE_PARITY BIT(5)
```

<a id="a60f22cb2ae47789875e2542063899876"></a>

### 174.4.120\_`USB_CDC_SERIAL_STATE_RINGSIGNAL`

```c
#define USB_CDC_SERIAL_STATE_RINGSIGNAL BIT(3)
```

<a id="ad720be9e3738bcba7e37dc9392c3b6e8"></a>

### 174.4.121\_`USB_CDC_SERIAL_STATE_RXCARRIER`

```c
#define USB_CDC_SERIAL_STATE_RXCARRIER BIT(0)
```

<a id="ab96b4f63f2de0ef913862878bce1029f"></a>

### 174.4.122\_`USB_CDC_SERIAL_STATE_TXCARRIER`

```c
#define USB_CDC_SERIAL_STATE_TXCARRIER BIT(1)
```

## 174.5\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P173_USB第9章头文件源码.md) · [返回大纲](大纲.md) · [下一章](P175_CDC头部功能描述符.md)
