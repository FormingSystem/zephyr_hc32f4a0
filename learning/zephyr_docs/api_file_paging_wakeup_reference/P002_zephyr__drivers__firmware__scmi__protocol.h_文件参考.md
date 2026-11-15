---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-2
title: zephyr__drivers__firmware__scmi__protocol.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_protocol.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（System Control and Management Interface，SCMI）驱动API的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/firmware/scmi/util.h>
#include <stdint.h>
#include <errno.h>
```

查看此文件的源码。

系统控制与管理接口（System Control and Management Interface，SCMI）驱动API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_scmi_5Fprotocol"></a>

```c
struct scmi_protocol
```

相关声明：[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)。

系统控制与管理接口（SCMI）的协议结构。

<a id="r_scmi_5Fprotocol_5Fevents"></a>

```c
struct scmi_protocol_events
```

相关声明：[scmi_protocol_events](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md)。

系统控制与管理接口（SCMI）的协议事件结构。

<a id="r_scmi_5Fprotocol_5Fversion"></a>

```c
struct scmi_protocol_version
```

相关声明：[scmi_protocol_version](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md)。

系统控制与管理接口（SCMI）的协议版本。

<a id="r_scmi_5Fmessage"></a>

```c
struct scmi_message
```

相关声明：[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)。

系统控制与管理接口（SCMI）的消息结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_gaff6ceb886b06b1187018d8a2b8dd73e3"></a>

```c
#define SCMI_SHORT_NAME_MAX_SIZE 16
```

相关声明：[SCMI_SHORT_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaff6ceb886b06b1187018d8a2b8dd73e3)。

描述 SCMI 名称的字符串最大大小，包含 NUL 终止符（Terminator）。

<a id="r_ga100155d2238e9f860e2cab8ad8209a8a"></a>

```c
#define SCMI_MESSAGE_HDR_MAKE(id, type, proto, token)
```

相关声明：[SCMI_MESSAGE_HDR_MAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga100155d2238e9f860e2cab8ad8209a8a)。

构造 SCMI 消息头（Message Header）。

<a id="r_ga434a417ef8751e84b88eb4204974cc09"></a>

```c
#define SCMI_MESSAGE_HDR_TAKE_MSGID(hdr)
```

相关声明：[SCMI_MESSAGE_HDR_TAKE_MSGID](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga434a417ef8751e84b88eb4204974cc09)。

从 SCMI 消息头提取消息 ID（Message ID），位 `[7:0]`。

<a id="r_ga24dffd8abf8f25b6a7bc6b68ddf6e380"></a>

```c
#define SCMI_MESSAGE_HDR_TAKE_TYPE(hdr)
```

相关声明：[SCMI_MESSAGE_HDR_TAKE_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga24dffd8abf8f25b6a7bc6b68ddf6e380)。

从 SCMI 消息头提取消息类型（Message Type），位 `[9:8]`。

<a id="r_gab1105b614d2ae1307826c48f86cb80ce"></a>

```c
#define SCMI_MESSAGE_HDR_TAKE_PROTOCOL(hdr)
```

相关声明：[SCMI_MESSAGE_HDR_TAKE_PROTOCOL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gab1105b614d2ae1307826c48f86cb80ce)。

从 SCMI 消息头提取协议 ID（Protocol ID），位 `[17:10]`。

<a id="r_ga5276d897f75f150887e4958b0c7eabe2"></a>

```c
#define SCMI_MESSAGE_HDR_TAKE_TOKEN(hdr)
```

相关声明：[SCMI_MESSAGE_HDR_TAKE_TOKEN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga5276d897f75f150887e4958b0c7eabe2)。

从 SCMI 消息头提取令牌（Token），位 `[27:18]`。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_ga8430a8fd8a2f84d0f5613a88b8d86650"></a>

```c
typedef void(* scmi_protocol_event_callback) (struct scmi_protocol *proto, uint32_t msg_id)
```

相关声明：[scmi_protocol_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga8430a8fd8a2f84d0f5613a88b8d86650)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

由 SCMI 核心调用的每协议通知回调（Per-protocol Notification Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_ga0c1b38acb21bc918714720c781e50d77"></a>

```c
enum scmi_message_type { SCMI_COMMAND = 0x0 , SCMI_DELAYED_REPLY = 0x2 , SCMI_NOTIFICATION = 0x3 }
```

相关声明：[scmi_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga0c1b38acb21bc918714720c781e50d77)、[SCMI_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8)、[SCMI_DELAYED_REPLY](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668)、[SCMI_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04)。

SCMI 消息类型（Message Type）。

<a id="r_ga451a39b7d2f3ffafa9d69b21c7e249b2"></a>

```c
enum scmi_status_code { SCMI_SUCCESS = 0 , SCMI_NOT_SUPPORTED = -1 , SCMI_INVALID_PARAMETERS = -2 , SCMI_DENIED = -3 , SCMI_NOT_FOUND = -4 , SCMI_OUT_OF_RANGE = -5 , SCMI_BUSY = -6 , SCMI_COMMS_ERROR = -7 , SCMI_GENERIC_ERROR = -8 , SCMI_HARDWARE_ERROR = -9 , SCMI_PROTOCOL_ERROR = -10 , SCMI_IN_USE = -11 }
```

相关声明：[scmi_status_code](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga451a39b7d2f3ffafa9d69b21c7e249b2)、[SCMI_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4)、[SCMI_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089)、[SCMI_INVALID_PARAMETERS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0)、[SCMI_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf)、[SCMI_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc)、[SCMI_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e)、[SCMI_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa)、[SCMI_COMMS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d)、[SCMI_GENERIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763)、[SCMI_HARDWARE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6)、[SCMI_PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4)、[SCMI_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60)。

SCMI 状态码（Status Codes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_gaec0ffd1352d0106633fd15be8fc20aa2"></a>

```c
int scmi_status_to_errno (int scmi_status)
```

相关声明：[scmi_status_to_errno](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaec0ffd1352d0106633fd15be8fc20aa2)。

在可能的情况下，将 SCMI 状态码（Status Code）转换为 Linux 中的等价值。

<a id="r_gacba26fb193852024636dda1e4ef0ee53"></a>

```c
int scmi_send_message (struct scmi_protocol *proto, struct scmi_message *msg, struct scmi_message *reply, bool use_polling)
```

相关声明：[scmi_send_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gacba26fb193852024636dda1e4ef0ee53)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

发送 SCMI 消息（Message）并等待回复（Reply）。

<a id="r_gaa97701c4c038fa5403e5696ac84e6149"></a>

```c
int scmi_protocol_get_version (struct scmi_protocol *proto, uint32_t *version)
```

相关声明：[scmi_protocol_get_version](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaa97701c4c038fa5403e5696ac84e6149)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议版本（Protocol Version）。

<a id="r_gac6afb98180e88ade7d235a96e72b7ca6"></a>

```c
int scmi_protocol_attributes_get (struct scmi_protocol *proto, uint32_t *attributes)
```

相关声明：[scmi_protocol_attributes_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gac6afb98180e88ade7d235a96e72b7ca6)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议属性（Protocol Attributes）。

<a id="r_ga0f5d5c4382c41a507b21741e88cbcac0"></a>

```c
int scmi_protocol_message_attributes_get (struct scmi_protocol *proto, uint32_t message_id, uint32_t *attributes)
```

相关声明：[scmi_protocol_message_attributes_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga0f5d5c4382c41a507b21741e88cbcac0)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议消息属性（Protocol Message Attributes）。

<a id="r_gae58fdab329d4f0d2a4b16c6f2a668fe6"></a>

```c
int scmi_protocol_version_negotiate (struct scmi_protocol *proto, uint32_t version)
```

相关声明：[scmi_protocol_version_negotiate](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gae58fdab329d4f0d2a4b16c6f2a668fe6)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

协商协议版本（Negotiate Protocol Version）。

<a id="r_gae5326d8ffd8fc7ed76ba73a0aee95d49"></a>

```c
int scmi_read_message (struct scmi_protocol *proto, struct scmi_message *msg)
```

相关声明：[scmi_read_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gae5326d8ffd8fc7ed76ba73a0aee95d49)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)。

读取 SCMI 通知（Notification）或延迟回复（Delayed Reply）。


## 2.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/firmware/scmi/util.h](../api_source_system_reference/P009_util.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P156_protocol.h_源码浏览.md)
- [scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)
- [scmi_protocol_events](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md)
- [scmi_protocol_version](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md)
- [scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)
- [SCMI_SHORT_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaff6ceb886b06b1187018d8a2b8dd73e3)
- [SCMI_MESSAGE_HDR_MAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga100155d2238e9f860e2cab8ad8209a8a)
- [SCMI_MESSAGE_HDR_TAKE_MSGID](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga434a417ef8751e84b88eb4204974cc09)
- [SCMI_MESSAGE_HDR_TAKE_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga24dffd8abf8f25b6a7bc6b68ddf6e380)
- [SCMI_MESSAGE_HDR_TAKE_PROTOCOL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gab1105b614d2ae1307826c48f86cb80ce)
- [SCMI_MESSAGE_HDR_TAKE_TOKEN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga5276d897f75f150887e4958b0c7eabe2)
- [scmi_protocol_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga8430a8fd8a2f84d0f5613a88b8d86650)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [scmi_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga0c1b38acb21bc918714720c781e50d77)
- [SCMI_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8)
- [SCMI_DELAYED_REPLY](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668)
- [SCMI_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04)
- [scmi_status_code](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga451a39b7d2f3ffafa9d69b21c7e249b2)
- [SCMI_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4)
- [SCMI_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089)
- [SCMI_INVALID_PARAMETERS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0)
- [SCMI_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf)
- [SCMI_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc)
- [SCMI_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e)
- [SCMI_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa)
- [SCMI_COMMS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d)
- [SCMI_GENERIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763)
- [SCMI_HARDWARE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6)
- [SCMI_PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4)
- [SCMI_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gga451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60)
- [scmi_status_to_errno](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaec0ffd1352d0106633fd15be8fc20aa2)
- [scmi_send_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gacba26fb193852024636dda1e4ef0ee53)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [scmi_protocol_get_version](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaa97701c4c038fa5403e5696ac84e6149)
- [scmi_protocol_attributes_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gac6afb98180e88ade7d235a96e72b7ca6)
- [scmi_protocol_message_attributes_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga0f5d5c4382c41a507b21741e88cbcac0)
- [scmi_protocol_version_negotiate](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gae58fdab329d4f0d2a4b16c6f2a668fe6)
- [scmi_read_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gae5326d8ffd8fc7ed76ba73a0aee95d49)

<a id="header-details"></a>

---

[上一章](P001_zephyr__kernel__mm__demand_paging.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__wuc.h_文件参考.md)
