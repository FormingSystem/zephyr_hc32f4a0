---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-16
title: 系统电源协议（System Power Protocol）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_系统电源协议（System Power Protocol）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通过 SCMI 管理整个系统的电源状态。

<a id="details"></a>

通过 SCMI 管理整个系统的电源状态。

<a id="header-files"></a>
<a id="files"></a>

## 16.1\_文件（Files）

<a id="r_system_2Eh"></a>

```c
file system.h
```

相关声明：[system.h](../api_file_storage_event_reference/P021_zephyr__drivers__firmware__scmi__system.h_文件参考.md)。

系统控制与管理接口（SCMI）系统电源管理协议（System Power Management Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.2\_数据结构（Data Structures）

<a id="r_scmi_5Fsystem_5Fpower_5Fstate_5Fconfig"></a>

```c
struct scmi_system_power_state_config
```

相关声明：[scmi_system_power_state_config](../platform_security_model_reference/P051_scmi_system_power_state_config_结构体.md)。

系统电源状态（System Power State）的配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.3\_宏定义（Macros）

<a id="r_gace76b7c1d6ea89892d6f83ed6ea0b95b"></a>

```c
#define SCMI_SYSTEM_POWER_PROTOCOL_SUPPORTED_VERSION 0x20001
```

相关声明：[SCMI_SYSTEM_POWER_PROTOCOL_SUPPORTED_VERSION](#gace76b7c1d6ea89892d6f83ed6ea0b95b)。

本驱动支持的 SCMI 系统电源协议（System Power Protocol）版本。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.4\_函数（Functions）

<a id="r_ga3b0b9f2097b588584c761517f5f826e5"></a>

```c
int scmi_system_protocol_version (uint32_t *version)
```

相关声明：[scmi_system_protocol_version](#ga3b0b9f2097b588584c761517f5f826e5)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议版本（Protocol Version）。

<a id="r_ga8a247062efb900840f6eeaada9b09ec9"></a>

```c
int scmi_system_protocol_attributes (uint32_t *attributes)
```

相关声明：[scmi_system_protocol_attributes](#ga8a247062efb900840f6eeaada9b09ec9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议属性（Protocol Attributes）。

<a id="r_gaef55839c0e05d236282d3ba9d2459ade"></a>

```c
int scmi_system_protocol_message_attributes (uint32_t message_id, uint32_t *attributes)
```

相关声明：[scmi_system_protocol_message_attributes](#gaef55839c0e05d236282d3ba9d2459ade)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议消息属性（Protocol Message Attributes）。

<a id="r_ga21694e998172f6f1a6077ecae2fa8fc5"></a>

```c
int scmi_system_protocol_version_negotiate (uint32_t version)
```

相关声明：[scmi_system_protocol_version_negotiate](#ga21694e998172f6f1a6077ecae2fa8fc5)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

协商协议版本（Negotiate Protocol Version）。

<a id="r_ga9c72df860c829672862bd2dbca6dbc69"></a>

```c
int scmi_system_power_state_set (struct scmi_system_power_state_config *cfg)
```

相关声明：[scmi_system_power_state_set](#ga9c72df860c829672862bd2dbca6dbc69)、[scmi_system_power_state_config](../platform_security_model_reference/P051_scmi_system_power_state_config_结构体.md)。

设置系统电源状态（System Power State）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 16.5\_标准 SCMI 系统电源状态（Standard System Power States）

<a id="r_ga6c9845f912e72929e91805b83c9ba43d"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_SHUTDOWN 0x00000000U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_SHUTDOWN](#ga6c9845f912e72929e91805b83c9ba43d)。

关机（Shutdown Off）。

<a id="r_gaefed484b8d64d28391f4a830de9268b6"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_COLD_RESET 0x00000001U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_COLD_RESET](#gaefed484b8d64d28391f4a830de9268b6)。

冷复位（Cold Reset）。

<a id="r_ga2046328bded959bfa9d3f6700fde8b6a"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_WARM_RESET 0x00000002U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_WARM_RESET](#ga2046328bded959bfa9d3f6700fde8b6a)。

热复位（Warm Reset）。

<a id="r_gad435091190f8a179421f71d91c4d1fdd"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_POWER_UP 0x00000003U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_POWER_UP](#gad435091190f8a179421f71d91c4d1fdd)。

上电（Power Up）。

<a id="r_ga703f15f314e70fc5b629b8b46ef55b54"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_SUSPEND 0x00000004U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_SUSPEND](#ga703f15f314e70fc5b629b8b46ef55b54)。

挂起（Suspend）。

## 16.6\_系统电源状态标志（System Power State Flags）

<a id="r_gac0b7946a32ff439380dd95f725cd05b3"></a>

```c
#define SCMI_SYSTEM_POWER_FLAG_FORCEFUL (0 << SCMI_SYSTEM_POWER_FLAG_SHIFT)
```

相关声明：[SCMI_SYSTEM_POWER_FLAG_FORCEFUL](#gac0b7946a32ff439380dd95f725cd05b3)。

强制请求（Forceful Request）。

<a id="r_ga9cb7a945ddb4b7460f51c13fbdc86d7d"></a>

```c
#define SCMI_SYSTEM_POWER_FLAG_GRACEFUL (1 << SCMI_SYSTEM_POWER_FLAG_SHIFT)
```

相关声明：[SCMI_SYSTEM_POWER_FLAG_GRACEFUL](#ga9cb7a945ddb4b7460f51c13fbdc86d7d)。

平稳处理请求（Graceful Request）。

## 16.7\_SCMI 系统消息属性（System Message Attributes）

<a id="r_ga24b755881c01b6d69d1430879bd5bfc1"></a>

```c
#define SCMI_SYSTEM_MSG_ATTR_SUSPEND (1 << SCMI_SYSTEM_MSG_ATTR_SUSPEND_SHIFT)
```

相关声明：[SCMI_SYSTEM_MSG_ATTR_SUSPEND](#ga24b755881c01b6d69d1430879bd5bfc1)。

支持系统挂起（System Suspend）。

<a id="r_gabb7ed362750f36e472a436f0674b749e"></a>

```c
#define SCMI_SYSTEM_MSG_ATTR_WARM_RESET (1 << SCMI_SYSTEM_MSG_ATTR_WARM_RESET_SHIFT)
```

相关声明：[SCMI_SYSTEM_MSG_ATTR_WARM_RESET](#gabb7ed362750f36e472a436f0674b749e)。

支持系统热复位（System Warm Reset）。

## 16.8\_详细说明（Detailed Documentation）

<a id="ga24b755881c01b6d69d1430879bd5bfc1"></a>

### `SCMI_SYSTEM_MSG_ATTR_SUSPEND`

```c
#define SCMI_SYSTEM_MSG_ATTR_SUSPEND (1 << SCMI_SYSTEM_MSG_ATTR_SUSPEND_SHIFT)
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

支持系统挂起（System Suspend）。

<a id="gabb7ed362750f36e472a436f0674b749e"></a>

### `SCMI_SYSTEM_MSG_ATTR_WARM_RESET`

```c
#define SCMI_SYSTEM_MSG_ATTR_WARM_RESET (1 << SCMI_SYSTEM_MSG_ATTR_WARM_RESET_SHIFT)
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

支持系统热复位（System Warm Reset）。

<a id="gac0b7946a32ff439380dd95f725cd05b3"></a>

### `SCMI_SYSTEM_POWER_FLAG_FORCEFUL`

```c
#define SCMI_SYSTEM_POWER_FLAG_FORCEFUL (0 << SCMI_SYSTEM_POWER_FLAG_SHIFT)
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

强制请求（Forceful Request）。

<a id="ga9cb7a945ddb4b7460f51c13fbdc86d7d"></a>

### `SCMI_SYSTEM_POWER_FLAG_GRACEFUL`

```c
#define SCMI_SYSTEM_POWER_FLAG_GRACEFUL (1 << SCMI_SYSTEM_POWER_FLAG_SHIFT)
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

平稳处理请求（Graceful Request）。

<a id="gace76b7c1d6ea89892d6f83ed6ea0b95b"></a>

### `SCMI_SYSTEM_POWER_PROTOCOL_SUPPORTED_VERSION`

```c
#define SCMI_SYSTEM_POWER_PROTOCOL_SUPPORTED_VERSION 0x20001
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

本驱动支持的 SCMI 系统电源协议（System Power Protocol）版本。

<a id="gaefed484b8d64d28391f4a830de9268b6"></a>

### `SCMI_SYSTEM_POWER_STATE_COLD_RESET`

```c
#define SCMI_SYSTEM_POWER_STATE_COLD_RESET 0x00000001U
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

冷复位（Cold Reset）。

<a id="gad435091190f8a179421f71d91c4d1fdd"></a>

### `SCMI_SYSTEM_POWER_STATE_POWER_UP`

```c
#define SCMI_SYSTEM_POWER_STATE_POWER_UP 0x00000003U
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

上电（Power Up）。

<a id="ga6c9845f912e72929e91805b83c9ba43d"></a>

### `SCMI_SYSTEM_POWER_STATE_SHUTDOWN`

```c
#define SCMI_SYSTEM_POWER_STATE_SHUTDOWN 0x00000000U
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

关机（Shutdown Off）。

<a id="ga703f15f314e70fc5b629b8b46ef55b54"></a>

### `SCMI_SYSTEM_POWER_STATE_SUSPEND`

```c
#define SCMI_SYSTEM_POWER_STATE_SUSPEND 0x00000004U
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

挂起（Suspend）。

<a id="ga2046328bded959bfa9d3f6700fde8b6a"></a>

### `SCMI_SYSTEM_POWER_STATE_WARM_RESET`

```c
#define SCMI_SYSTEM_POWER_STATE_WARM_RESET 0x00000002U
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

热复位（Warm Reset）。

<a id="ga9c72df860c829672862bd2dbca6dbc69"></a>

### `scmi_system_power_state_set()`

```c
int scmi_system_power_state_set ( struct scmi_system_power_state_config * cfg)
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

设置系统电源状态（System Power State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cfg` | 指向电源状态配置（Power State Configuration）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga8a247062efb900840f6eeaada9b09ec9"></a>

### `scmi_system_protocol_attributes()`

```c
int scmi_system_protocol_attributes ( uint32_t * attributes)
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

获取协议属性（Protocol Attributes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attributes` | 协议属性（Protocol Attributes）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaef55839c0e05d236282d3ba9d2459ade"></a>

### `scmi_system_protocol_message_attributes()`

```c
int scmi_system_protocol_message_attributes ( uint32_t message_id, uint32_t * attributes )
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

获取协议消息属性（Protocol Message Attributes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `message_id` | 消息的消息 ID（Message ID）。 |
| `attributes` | 消息属性（Message Attributes）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga3b0b9f2097b588584c761517f5f826e5"></a>

### `scmi_system_protocol_version()`

```c
int scmi_system_protocol_version ( uint32_t * version)
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

获取协议版本（Protocol Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `version` | 协议版本（Protocol Version）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga21694e998172f6f1a6077ecae2fa8fc5"></a>

### `scmi_system_protocol_version_negotiate()`

```c
int scmi_system_protocol_version_negotiate ( uint32_t version)
```

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

协商协议版本（Negotiate Protocol Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `version` | 期望协议版本（Desired Protocol Version）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 16.9\_原页交叉引用（Cross References）

- [system.h](../api_file_storage_event_reference/P021_zephyr__drivers__firmware__scmi__system.h_文件参考.md)
- [scmi_system_power_state_config](../platform_security_model_reference/P051_scmi_system_power_state_config_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_网络链路地址库（Network Link Address Library）.md) · [返回大纲](大纲.md) · [下一章](P017_传感器——感知子系统（Sensors，Sensing）.md)
