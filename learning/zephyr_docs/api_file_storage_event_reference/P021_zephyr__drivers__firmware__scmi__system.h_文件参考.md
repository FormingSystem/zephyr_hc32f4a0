---
id: learning.zephyr-docs.api-file-storage-event-reference.page-21
title: zephyr__drivers__firmware__scmi__system.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/system_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_system.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/system_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）系统电源管理协议（System Power Management Protocol）的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/firmware/scmi/protocol.h>
#include <stdint.h>
```

查看此文件的源码。

系统控制与管理接口（SCMI）系统电源管理协议（System Power Management Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_scmi_5Fsystem_5Fpower_5Fstate_5Fconfig"></a>

```c
struct scmi_system_power_state_config
```

相关声明：[scmi_system_power_state_config](../platform_security_model_reference/P051_scmi_system_power_state_config_结构体.md)。

系统电源状态（System Power State）的配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="r_gace76b7c1d6ea89892d6f83ed6ea0b95b"></a>

```c
#define SCMI_SYSTEM_POWER_PROTOCOL_SUPPORTED_VERSION 0x20001
```

相关声明：[SCMI_SYSTEM_POWER_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gace76b7c1d6ea89892d6f83ed6ea0b95b)。

本驱动支持的 SCMI 系统电源协议（System Power Protocol）版本。

<a id="define-members-0"></a>

### 标准 SCMI 系统电源状态（Standard System Power States）

<a id="r_ga6c9845f912e72929e91805b83c9ba43d"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_SHUTDOWN 0x00000000U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_SHUTDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga6c9845f912e72929e91805b83c9ba43d)。

关机（Shutdown Off）。

<a id="r_gaefed484b8d64d28391f4a830de9268b6"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_COLD_RESET 0x00000001U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_COLD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gaefed484b8d64d28391f4a830de9268b6)。

冷复位（Cold Reset）。

<a id="r_ga2046328bded959bfa9d3f6700fde8b6a"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_WARM_RESET 0x00000002U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_WARM_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga2046328bded959bfa9d3f6700fde8b6a)。

热复位（Warm Reset）。

<a id="r_gad435091190f8a179421f71d91c4d1fdd"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_POWER_UP 0x00000003U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_POWER_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gad435091190f8a179421f71d91c4d1fdd)。

上电（Power Up）。

<a id="r_ga703f15f314e70fc5b629b8b46ef55b54"></a>

```c
#define SCMI_SYSTEM_POWER_STATE_SUSPEND 0x00000004U
```

相关声明：[SCMI_SYSTEM_POWER_STATE_SUSPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga703f15f314e70fc5b629b8b46ef55b54)。

挂起（Suspend）。

<a id="define-members-1"></a>

### 系统电源状态标志（System Power State Flags）

<a id="r_gac0b7946a32ff439380dd95f725cd05b3"></a>

```c
#define SCMI_SYSTEM_POWER_FLAG_FORCEFUL (0 << SCMI_SYSTEM_POWER_FLAG_SHIFT)
```

相关声明：[SCMI_SYSTEM_POWER_FLAG_FORCEFUL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gac0b7946a32ff439380dd95f725cd05b3)。

强制请求（Forceful Request）。

<a id="r_ga9cb7a945ddb4b7460f51c13fbdc86d7d"></a>

```c
#define SCMI_SYSTEM_POWER_FLAG_GRACEFUL (1 << SCMI_SYSTEM_POWER_FLAG_SHIFT)
```

相关声明：[SCMI_SYSTEM_POWER_FLAG_GRACEFUL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga9cb7a945ddb4b7460f51c13fbdc86d7d)。

平稳处理请求（Graceful Request）。

<a id="define-members-2"></a>

### SCMI 系统消息属性（System Message Attributes）

<a id="r_ga24b755881c01b6d69d1430879bd5bfc1"></a>

```c
#define SCMI_SYSTEM_MSG_ATTR_SUSPEND (1 << SCMI_SYSTEM_MSG_ATTR_SUSPEND_SHIFT)
```

相关声明：[SCMI_SYSTEM_MSG_ATTR_SUSPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga24b755881c01b6d69d1430879bd5bfc1)。

支持系统挂起（System Suspend）。

<a id="r_gabb7ed362750f36e472a436f0674b749e"></a>

```c
#define SCMI_SYSTEM_MSG_ATTR_WARM_RESET (1 << SCMI_SYSTEM_MSG_ATTR_WARM_RESET_SHIFT)
```

相关声明：[SCMI_SYSTEM_MSG_ATTR_WARM_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gabb7ed362750f36e472a436f0674b749e)。

支持系统热复位（System Warm Reset）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.3\_函数（Functions）

<a id="r_ga3b0b9f2097b588584c761517f5f826e5"></a>

```c
int scmi_system_protocol_version (uint32_t *version)
```

相关声明：[scmi_system_protocol_version](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga3b0b9f2097b588584c761517f5f826e5)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议版本（Protocol Version）。

<a id="r_ga8a247062efb900840f6eeaada9b09ec9"></a>

```c
int scmi_system_protocol_attributes (uint32_t *attributes)
```

相关声明：[scmi_system_protocol_attributes](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga8a247062efb900840f6eeaada9b09ec9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议属性（Protocol Attributes）。

<a id="r_gaef55839c0e05d236282d3ba9d2459ade"></a>

```c
int scmi_system_protocol_message_attributes (uint32_t message_id, uint32_t *attributes)
```

相关声明：[scmi_system_protocol_message_attributes](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gaef55839c0e05d236282d3ba9d2459ade)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取协议消息属性（Protocol Message Attributes）。

<a id="r_ga21694e998172f6f1a6077ecae2fa8fc5"></a>

```c
int scmi_system_protocol_version_negotiate (uint32_t version)
```

相关声明：[scmi_system_protocol_version_negotiate](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga21694e998172f6f1a6077ecae2fa8fc5)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

协商协议版本（Negotiate Protocol Version）。

<a id="r_ga9c72df860c829672862bd2dbca6dbc69"></a>

```c
int scmi_system_power_state_set (struct scmi_system_power_state_config *cfg)
```

相关声明：[scmi_system_power_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga9c72df860c829672862bd2dbca6dbc69)、[scmi_system_power_state_config](../platform_security_model_reference/P051_scmi_system_power_state_config_结构体.md)。

设置系统电源状态（System Power State）。


## 21.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/firmware/scmi/protocol.h](../api_source_reference/P156_protocol.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P853_system.h_源码浏览.md)
- [scmi_system_power_state_config](../platform_security_model_reference/P051_scmi_system_power_state_config_结构体.md)
- [SCMI_SYSTEM_POWER_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gace76b7c1d6ea89892d6f83ed6ea0b95b)
- [SCMI_SYSTEM_POWER_STATE_SHUTDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga6c9845f912e72929e91805b83c9ba43d)
- [SCMI_SYSTEM_POWER_STATE_COLD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gaefed484b8d64d28391f4a830de9268b6)
- [SCMI_SYSTEM_POWER_STATE_WARM_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga2046328bded959bfa9d3f6700fde8b6a)
- [SCMI_SYSTEM_POWER_STATE_POWER_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gad435091190f8a179421f71d91c4d1fdd)
- [SCMI_SYSTEM_POWER_STATE_SUSPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga703f15f314e70fc5b629b8b46ef55b54)
- [SCMI_SYSTEM_POWER_FLAG_FORCEFUL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gac0b7946a32ff439380dd95f725cd05b3)
- [SCMI_SYSTEM_POWER_FLAG_GRACEFUL](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga9cb7a945ddb4b7460f51c13fbdc86d7d)
- [SCMI_SYSTEM_MSG_ATTR_SUSPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga24b755881c01b6d69d1430879bd5bfc1)
- [SCMI_SYSTEM_MSG_ATTR_WARM_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gabb7ed362750f36e472a436f0674b749e)
- [scmi_system_protocol_version](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga3b0b9f2097b588584c761517f5f826e5)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [scmi_system_protocol_attributes](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga8a247062efb900840f6eeaada9b09ec9)
- [scmi_system_protocol_message_attributes](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#gaef55839c0e05d236282d3ba9d2459ade)
- [scmi_system_protocol_version_negotiate](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga21694e998172f6f1a6077ecae2fa8fc5)
- [scmi_system_power_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__system.html#ga9c72df860c829672862bd2dbca6dbc69)

<a id="header-details"></a>

---

[上一章](P020_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__store.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__transform.h_文件参考.md)
