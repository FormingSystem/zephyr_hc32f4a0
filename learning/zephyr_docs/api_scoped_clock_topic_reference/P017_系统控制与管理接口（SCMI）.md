---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-17
title: 系统控制与管理接口（SCMI）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_系统控制与管理接口（SCMI）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ARM 系统控制与管理接口（System Control and Management Interface，SCMI）。

<a id="details"></a>

ARM 系统控制与管理接口（System Control and Management Interface，SCMI）。

<a id="header-groups"></a>
<a id="groups"></a>

## 17.1\_主题（Topics）

<a id="r_scmi_5Fprotocols"></a>

相关声明：[协议（Protocols）](../api_topic_reference/P059_协议（Protocols）.md)。

标准 SCMI 协议定义。

<a id="r_scmi_5Ftransport"></a>

相关声明：[传输（Transport）](../api_extension_topic_reference/P030_传输（Transport）.md)。

SCMI 传输层的抽象与定义。

<a id="r_scmi_5Futil"></a>

相关声明：[实用工具（Utilities）](../api_buffer_paging_topic_reference/P018_实用工具（Utilities）.md)。

SCMI 驱动的辅助宏和工具。

<a id="header-files"></a>
<a id="files"></a>

## 17.2\_文件（Files）

<a id="r_protocol_2Eh"></a>

```c
file protocol.h
```

相关声明：[protocol.h](../api_file_paging_wakeup_reference/P002_zephyr__drivers__firmware__scmi__protocol.h_文件参考.md)。

系统控制与管理接口（System Control and Management Interface，SCMI）驱动API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.3\_数据结构（Data Structures）

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

## 17.4\_宏定义（Macros）

<a id="r_gaff6ceb886b06b1187018d8a2b8dd73e3"></a>

```c
#define SCMI_SHORT_NAME_MAX_SIZE 16
```

相关声明：[SCMI_SHORT_NAME_MAX_SIZE](#gaff6ceb886b06b1187018d8a2b8dd73e3)。

描述 SCMI 名称的字符串最大大小，包含 NUL 终止符（Terminator）。

<a id="r_ga100155d2238e9f860e2cab8ad8209a8a"></a>

```c
#define SCMI_MESSAGE_HDR_MAKE(id, type, proto, token)
```

相关声明：[SCMI_MESSAGE_HDR_MAKE](#ga100155d2238e9f860e2cab8ad8209a8a)。

构造 SCMI 消息头（Message Header）。

<a id="r_ga434a417ef8751e84b88eb4204974cc09"></a>

```c
#define SCMI_MESSAGE_HDR_TAKE_MSGID(hdr)
```

相关声明：[SCMI_MESSAGE_HDR_TAKE_MSGID](#ga434a417ef8751e84b88eb4204974cc09)。

从 SCMI 消息头提取消息 ID（Message ID），位 `[7:0]`。

<a id="r_ga24dffd8abf8f25b6a7bc6b68ddf6e380"></a>

```c
#define SCMI_MESSAGE_HDR_TAKE_TYPE(hdr)
```

相关声明：[SCMI_MESSAGE_HDR_TAKE_TYPE](#ga24dffd8abf8f25b6a7bc6b68ddf6e380)。

从 SCMI 消息头提取消息类型（Message Type），位 `[9:8]`。

<a id="r_gab1105b614d2ae1307826c48f86cb80ce"></a>

```c
#define SCMI_MESSAGE_HDR_TAKE_PROTOCOL(hdr)
```

相关声明：[SCMI_MESSAGE_HDR_TAKE_PROTOCOL](#gab1105b614d2ae1307826c48f86cb80ce)。

从 SCMI 消息头提取协议 ID（Protocol ID），位 `[17:10]`。

<a id="r_ga5276d897f75f150887e4958b0c7eabe2"></a>

```c
#define SCMI_MESSAGE_HDR_TAKE_TOKEN(hdr)
```

相关声明：[SCMI_MESSAGE_HDR_TAKE_TOKEN](#ga5276d897f75f150887e4958b0c7eabe2)。

从 SCMI 消息头提取令牌（Token），位 `[27:18]`。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 17.5\_类型定义（Typedefs）

<a id="r_ga8430a8fd8a2f84d0f5613a88b8d86650"></a>

```c
typedef void(* scmi_protocol_event_callback) (struct scmi_protocol *proto, uint32_t msg_id)
```

相关声明：[scmi_protocol_event_callback](#ga8430a8fd8a2f84d0f5613a88b8d86650)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

由 SCMI 核心调用的每协议通知回调（Per-protocol Notification Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.6\_枚举（Enumerations）

<a id="r_ga0c1b38acb21bc918714720c781e50d77"></a>

```c
enum scmi_message_type { SCMI_COMMAND = 0x0 , SCMI_DELAYED_REPLY = 0x2 , SCMI_NOTIFICATION = 0x3 }
```

相关声明：[scmi_message_type](#ga0c1b38acb21bc918714720c781e50d77)、[SCMI_COMMAND](#gga0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8)、[SCMI_DELAYED_REPLY](#gga0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668)、[SCMI_NOTIFICATION](#gga0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04)。

SCMI 消息类型（Message Type）。

<a id="r_ga451a39b7d2f3ffafa9d69b21c7e249b2"></a>

```c
enum scmi_status_code { SCMI_SUCCESS = 0 , SCMI_NOT_SUPPORTED = -1 , SCMI_INVALID_PARAMETERS = -2 , SCMI_DENIED = -3 , SCMI_NOT_FOUND = -4 , SCMI_OUT_OF_RANGE = -5 , SCMI_BUSY = -6 , SCMI_COMMS_ERROR = -7 , SCMI_GENERIC_ERROR = -8 , SCMI_HARDWARE_ERROR = -9 , SCMI_PROTOCOL_ERROR = -10 , SCMI_IN_USE = -11 }
```

相关声明：[scmi_status_code](#ga451a39b7d2f3ffafa9d69b21c7e249b2)、[SCMI_SUCCESS](#gga451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4)、[SCMI_NOT_SUPPORTED](#gga451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089)、[SCMI_INVALID_PARAMETERS](#gga451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0)、[SCMI_DENIED](#gga451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf)、[SCMI_NOT_FOUND](#gga451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc)、[SCMI_OUT_OF_RANGE](#gga451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e)、[SCMI_BUSY](#gga451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa)、[SCMI_COMMS_ERROR](#gga451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d)、[SCMI_GENERIC_ERROR](#gga451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763)、[SCMI_HARDWARE_ERROR](#gga451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6)、[SCMI_PROTOCOL_ERROR](#gga451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4)、[SCMI_IN_USE](#gga451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60)。

SCMI 状态码（Status Codes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.7\_函数（Functions）

<a id="r_gaec0ffd1352d0106633fd15be8fc20aa2"></a>

```c
int scmi_status_to_errno (int scmi_status)
```

相关声明：[scmi_status_to_errno](#gaec0ffd1352d0106633fd15be8fc20aa2)。

在可能的情况下，将 SCMI 状态码（Status Code）转换为 Linux 中的等价值。

<a id="r_gacba26fb193852024636dda1e4ef0ee53"></a>

```c
int scmi_send_message (struct scmi_protocol *proto, struct scmi_message *msg, struct scmi_message *reply, bool use_polling)
```

相关声明：[scmi_send_message](#gacba26fb193852024636dda1e4ef0ee53)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

发送 SCMI 消息（Message）并等待回复（Reply）。

<a id="r_gaa97701c4c038fa5403e5696ac84e6149"></a>

```c
int scmi_protocol_get_version (struct scmi_protocol *proto, uint32_t *version)
```

相关声明：[scmi_protocol_get_version](#gaa97701c4c038fa5403e5696ac84e6149)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议版本（Protocol Version）。

<a id="r_gac6afb98180e88ade7d235a96e72b7ca6"></a>

```c
int scmi_protocol_attributes_get (struct scmi_protocol *proto, uint32_t *attributes)
```

相关声明：[scmi_protocol_attributes_get](#gac6afb98180e88ade7d235a96e72b7ca6)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议属性（Protocol Attributes）。

<a id="r_ga0f5d5c4382c41a507b21741e88cbcac0"></a>

```c
int scmi_protocol_message_attributes_get (struct scmi_protocol *proto, uint32_t message_id, uint32_t *attributes)
```

相关声明：[scmi_protocol_message_attributes_get](#ga0f5d5c4382c41a507b21741e88cbcac0)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议消息属性（Protocol Message Attributes）。

<a id="r_gae58fdab329d4f0d2a4b16c6f2a668fe6"></a>

```c
int scmi_protocol_version_negotiate (struct scmi_protocol *proto, uint32_t version)
```

相关声明：[scmi_protocol_version_negotiate](#gae58fdab329d4f0d2a4b16c6f2a668fe6)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

协商协议版本（Negotiate Protocol Version）。

<a id="r_gae5326d8ffd8fc7ed76ba73a0aee95d49"></a>

```c
int scmi_read_message (struct scmi_protocol *proto, struct scmi_message *msg)
```

相关声明：[scmi_read_message](#gae5326d8ffd8fc7ed76ba73a0aee95d49)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)。

读取 SCMI 通知（Notification）或延迟回复（Delayed Reply）。

## 17.8\_详细说明（Detailed Documentation）

<a id="ga100155d2238e9f860e2cab8ad8209a8a"></a>

### `SCMI_MESSAGE_HDR_MAKE`

```c
#define SCMI_MESSAGE_HDR_MAKE ( id, type, proto, token )
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

展开值（Value）：

```c
(SCMI_FIELD_MAKE(id, GENMASK(7, 0), 0) | SCMI_FIELD_MAKE(type, GENMASK(1, 0), 8) |         \
 SCMI_FIELD_MAKE(proto, GENMASK(7, 0), 10) | SCMI_FIELD_MAKE(token, GENMASK(9, 0), 18))
```

构造 SCMI 消息头（Message Header）。

根据组成字段构造系统控制与管理接口（SCMI）消息头。生成的 32 位头部布局如下：

- 位 [7:0]：消息标识符（Message ID）。
- 位 [9:8]：消息类型（Message Type），参见 scmi_message_type。
- 位 [17:10]：协议标识符（Protocol ID）。
- 位 [27:18]：消息令牌（Message Token）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 消息编号（Message ID）。 |
| `type` | 消息类型（Message Type）。 |
| `proto` | 协议 ID（Protocol ID）。 |
| `token` | 消息令牌（Message Token）。 |

<a id="ga434a417ef8751e84b88eb4204974cc09"></a>

### `SCMI_MESSAGE_HDR_TAKE_MSGID`

```c
#define SCMI_MESSAGE_HDR_TAKE_MSGID ( hdr)
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

展开值（Value）：

```c
FIELD_GET(GENMASK(7, 0), (hdr))
```

从 SCMI 消息头提取消息 ID（Message ID），位 `[7:0]`。

<a id="gab1105b614d2ae1307826c48f86cb80ce"></a>

### `SCMI_MESSAGE_HDR_TAKE_PROTOCOL`

```c
#define SCMI_MESSAGE_HDR_TAKE_PROTOCOL ( hdr)
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

展开值（Value）：

```c
FIELD_GET(GENMASK(17, 10), (hdr))
```

从 SCMI 消息头提取协议 ID（Protocol ID），位 `[17:10]`。

<a id="ga5276d897f75f150887e4958b0c7eabe2"></a>

### `SCMI_MESSAGE_HDR_TAKE_TOKEN`

```c
#define SCMI_MESSAGE_HDR_TAKE_TOKEN ( hdr)
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

展开值（Value）：

```c
FIELD_GET(GENMASK(27, 18), (hdr))
```

从 SCMI 消息头提取令牌（Token），位 `[27:18]`。

<a id="ga24dffd8abf8f25b6a7bc6b68ddf6e380"></a>

### `SCMI_MESSAGE_HDR_TAKE_TYPE`

```c
#define SCMI_MESSAGE_HDR_TAKE_TYPE ( hdr)
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

展开值（Value）：

```c
FIELD_GET(GENMASK(9, 8), (hdr))
```

从 SCMI 消息头提取消息类型（Message Type），位 `[9:8]`。

<a id="gaff6ceb886b06b1187018d8a2b8dd73e3"></a>

### `SCMI_SHORT_NAME_MAX_SIZE`

```c
#define SCMI_SHORT_NAME_MAX_SIZE 16
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

描述 SCMI 名称的字符串最大大小，包含 NUL 终止符（Terminator）。

<a id="ga8430a8fd8a2f84d0f5613a88b8d86650"></a>

### `scmi_protocol_event_callback`

```c
typedef void(* scmi_protocol_event_callback) (struct scmi_protocol *proto, uint32_t msg_id)
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

由 SCMI 核心调用的每协议通知回调（Per-protocol Notification Callback）。

在各 SCMI 协议的静态注册阶段（Static Registration Phase）定义事件特定信息。收到平台到代理（P2A）的通知／中断时，SCMI 核心解码消息并将其分发到相应协议的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向收到通知的 SCMI 协议实例（Protocol Instance）的指针。 |
| `msg_id` | 协议专用消息标识符（Protocol-specific Message ID）。 |

<a id="ga0c1b38acb21bc918714720c781e50d77"></a>

### `scmi_message_type`

```c
enum scmi_message_type
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

SCMI 消息类型（Message Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SCMI_COMMAND` | 命令消息（Command Message）。 |
| `SCMI_DELAYED_REPLY` | 延迟回复消息（Delayed Reply Message）。 |
| `SCMI_NOTIFICATION` | 通知消息（Notification Message）。 |

<a id="ga451a39b7d2f3ffafa9d69b21c7e249b2"></a>

### `scmi_status_code`

```c
enum scmi_status_code
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

SCMI 状态码（Status Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SCMI_SUCCESS` | 成功完成（Successful Completion）。 |
| `SCMI_NOT_SUPPORTED` | 不支持该命令（Command）。 |
| `SCMI_INVALID_PARAMETERS` | 一个或多个参数无效（Invalid Parameters）。 |
| `SCMI_DENIED` | 调用者无权执行该操作（Operation）。 |
| `SCMI_NOT_FOUND` | 未找到命令引用的实体（Entity）。 |
| `SCMI_OUT_OF_RANGE` | 参数或值超出支持范围（Supported Range）。 |
| `SCMI_BUSY` | 平台忙碌（Busy），无法处理该命令。 |
| `SCMI_COMMS_ERROR` | 发生通信错误（Communication Error）。 |
| `SCMI_GENERIC_ERROR` | 发生未指定错误（Unspecified Error）。 |
| `SCMI_HARDWARE_ERROR` | 发生硬件错误（Hardware Error）。 |
| `SCMI_PROTOCOL_ERROR` | 发生协议错误（Protocol Error），例如消息格式错误（Malformed Message）。 |
| `SCMI_IN_USE` | 资源已在使用中（Already in Use）。 |

<a id="gac6afb98180e88ade7d235a96e72b7ca6"></a>

### `scmi_protocol_attributes_get()`

```c
int scmi_protocol_attributes_get ( struct scmi_protocol * proto, uint32_t * attributes )
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

获取协议属性（Protocol Attributes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 协议实例（Protocol Instance）。 |
| `attributes` | 用于存储协议属性（Protocol Attributes）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaa97701c4c038fa5403e5696ac84e6149"></a>

### `scmi_protocol_get_version()`

```c
int scmi_protocol_get_version ( struct scmi_protocol * proto, uint32_t * version )
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

获取协议版本（Protocol Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 协议实例（Protocol Instance）。 |
| `version` | 用于存储协议版本（Protocol Version）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga0f5d5c4382c41a507b21741e88cbcac0"></a>

### `scmi_protocol_message_attributes_get()`

```c
int scmi_protocol_message_attributes_get ( struct scmi_protocol * proto, uint32_t message_id, uint32_t * attributes )
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

获取协议消息属性（Protocol Message Attributes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 协议实例（Protocol Instance）。 |
| `message_id` | 要查询的消息标识符（Message ID）。 |
| `attributes` | 用于存储消息属性（Message Attributes）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gae58fdab329d4f0d2a4b16c6f2a668fe6"></a>

### `scmi_protocol_version_negotiate()`

```c
int scmi_protocol_version_negotiate ( struct scmi_protocol * proto, uint32_t version )
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

协商协议版本（Negotiate Protocol Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 协议实例（Protocol Instance）。 |
| `version` | 期望协议版本（Desired Protocol Version）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gae5326d8ffd8fc7ed76ba73a0aee95d49"></a>

### `scmi_read_message()`

```c
int scmi_read_message ( struct scmi_protocol * proto, struct scmi_message * msg )
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

读取 SCMI 通知（Notification）或延迟回复（Delayed Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 协议（Protocol）的指针。 |
| `msg` | 指向待读取 SCMI 消息（Message）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 失败时的 `errno` 错误码。 |

<a id="gacba26fb193852024636dda1e4ef0ee53"></a>

### `scmi_send_message()`

```c
int scmi_send_message ( struct scmi_protocol * proto, struct scmi_message * msg, struct scmi_message * reply, bool use_polling )
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

发送 SCMI 消息（Message）并等待回复（Reply）。

阻塞函数（Blocking Function），用于通过给定通道发送 SCMI 消息并等待回复。

- true：轮询模式（Polling Mode），平台主动检查消息状态，确定消息是否已被处理。
- false：中断模式（Interrupt Mode），平台依赖 SCMI 中断来检测消息是否已被处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 协议（Protocol）的指针。 |
| `msg` | 指向待发送 SCMI 消息（Message）的指针。 |
| `reply` | 指向 SCMI 消息（Message）的指针，将在其中写入回复。 |
| `use_polling` | 指定 SCMI 平台与代理（Agents）交互所用的通信机制（Communication Mechanism）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaec0ffd1352d0106633fd15be8fc20aa2"></a>

### `scmi_status_to_errno()`

```c
int scmi_status_to_errno ( int scmi_status)
```

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

在可能的情况下，将 SCMI 状态码（Status Code）转换为 Linux 中的等价值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `scmi_status` | SCMI 状态码（Status Code），见枚举 scmi_status_code。 |

返回（Returns）：给定 SCMI 状态码对应的 Linux 错误码（errno）。


## 17.9\_原页交叉引用（Cross References）

- [协议（Protocols）](../api_topic_reference/P059_协议（Protocols）.md)
- [传输（Transport）](../api_extension_topic_reference/P030_传输（Transport）.md)
- [实用工具（Utilities）](../api_buffer_paging_topic_reference/P018_实用工具（Utilities）.md)
- [protocol.h](../api_file_paging_wakeup_reference/P002_zephyr__drivers__firmware__scmi__protocol.h_文件参考.md)
- [scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)
- [scmi_protocol_events](../platform_security_model_reference/P048_scmi_protocol_events_结构体.md)
- [scmi_protocol_version](../platform_security_model_reference/P049_scmi_protocol_version_结构体.md)
- [scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [SCMI_FIELD_MAKE](../api_buffer_paging_topic_reference/P018_实用工具（Utilities）.md#ga21b369f9fa6d1a965ece4a589df88581)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [FIELD_GET](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa49a456f06f7bdbedfcf3517e461947e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__scmi__util_html_ga21b369f9fa6d1a965ece4a589df88581"></a>
<a id="agroup__sys-util_html_ga58530d20924859d16358c7400c37738d"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8"></a>
<a id="gga0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668"></a>
<a id="gga0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4"></a>
<a id="gga451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_点对点协议二层_驱动支持函数（PPP L2_driver Support Functions）.md) · [返回大纲](大纲.md) · [下一章](P018_感知（Sensing）.md)
