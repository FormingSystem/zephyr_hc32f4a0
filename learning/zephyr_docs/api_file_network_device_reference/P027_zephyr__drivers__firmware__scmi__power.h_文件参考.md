---
id: learning.zephyr-docs.api-file-network-device-reference.page-27
title: zephyr__drivers__firmware__scmi__power.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/power_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_power.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/power_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）电源域协议（Power Domain Protocol）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

查看此文件的源码。

系统控制与管理接口（SCMI）电源域协议（Power Domain Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 27.1\_数据结构（Data Structures）

<a id="r_scmi_5Fpower_5Fstate_5Fconfig"></a>

```c
struct scmi_power_state_config
```

相关声明：[scmi_power_state_config](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md)。

描述POWER_STATE_SET命令的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.2\_宏定义（Macros）

<a id="r_ga8c95da0a183bcdde6e6fde5b111d9c22"></a>

```c
#define SCMI_POWER_STATE_SET_FLAGS_ASYNC BIT(0)
```

相关声明：[SCMI_POWER_STATE_SET_FLAGS_ASYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga8c95da0a183bcdde6e6fde5b111d9c22)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`POWER_STATE_SET` 标志：异步执行电源状态变化（Asynchronous Power State Change）。

<a id="r_ga74838410dad55ba27d05e384df279894"></a>

```c
#define SCMI_POWER_DOMAIN_PROTOCOL_SUPPORTED_VERSION 0x30001
```

相关声明：[SCMI_POWER_DOMAIN_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga74838410dad55ba27d05e384df279894)。

此驱动支持的 SCMI 电源域协议（Power Domain Protocol）版本。

<a id="define-members-0"></a>

### SCMI 电源域状态参数（State Parameters）

<a id="r_ga184ce394bf8681e3891d92b73aa0e7fb"></a>

```c
#define SCMI_POWER_STATE_TYPE_SHIFT 30U
```

相关声明：[SCMI_POWER_STATE_TYPE_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga184ce394bf8681e3891d92b73aa0e7fb)。

电源状态类型字段（Power State Type Field）的移位量。

<a id="r_ga7cf257fa63dd2ad77912612b82eb1fa8"></a>

```c
#define SCMI_POWER_STATE_ID_MASK (BIT(28) - 1)
```

相关声明：[SCMI_POWER_STATE_ID_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga7cf257fa63dd2ad77912612b82eb1fa8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电源状态标识字段（Power State ID Field）的掩码。

<a id="r_ga9765bcc859e9f4f550d6f4974d154eab"></a>

```c
#define SCMI_POWER_STATE_PARAM(type, id)
```

相关声明：[SCMI_POWER_STATE_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga9765bcc859e9f4f550d6f4974d154eab)。

构造 SCMI 电源状态参数（Power State Parameter）。

<a id="define-members-1"></a>

### SCMI 电源域通用状态（Generic States）

<a id="r_ga61d565a37849fcde1b5737bb35b71896"></a>

```c
#define SCMI_POWER_STATE_GENERIC_ON SCMI_POWER_STATE_PARAM(0, 0)
```

相关声明：[SCMI_POWER_STATE_GENERIC_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga61d565a37849fcde1b5737bb35b71896)、[SCMI_POWER_STATE_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga9765bcc859e9f4f550d6f4974d154eab)。

电源域处于开启状态（ON）。

<a id="r_ga359cfeea3432e62b39ab063855b8227c"></a>

```c
#define SCMI_POWER_STATE_GENERIC_OFF SCMI_POWER_STATE_PARAM(1, 0)
```

相关声明：[SCMI_POWER_STATE_GENERIC_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga359cfeea3432e62b39ab063855b8227c)、[SCMI_POWER_STATE_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga9765bcc859e9f4f550d6f4974d154eab)。

电源域处于关闭状态（OFF）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.3\_函数（Functions）

<a id="r_ga0969968c4d6b94868295172c0408031b"></a>

```c
int scmi_power_state_set (struct scmi_power_state_config *cfg)
```

相关声明：[scmi_power_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga0969968c4d6b94868295172c0408031b)、[scmi_power_state_config](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md)。

发送 `POWER_STATE_SET` 命令并取得响应（Reply）。

<a id="r_gadc7a2fbf0c4cab570d3a567ce548c947"></a>

```c
int scmi_power_state_get (uint32_t domain_id, uint32_t *power_state)
```

相关声明：[scmi_power_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#gadc7a2fbf0c4cab570d3a567ce548c947)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询电源域状态（Power Domain State）。


## 27.4\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/protocol.h](../api_source_reference/P156_protocol.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P669_power.h_源码浏览.md)
- [scmi_power_state_config](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md)
- [SCMI_POWER_STATE_SET_FLAGS_ASYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga8c95da0a183bcdde6e6fde5b111d9c22)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SCMI_POWER_DOMAIN_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga74838410dad55ba27d05e384df279894)
- [SCMI_POWER_STATE_TYPE_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga184ce394bf8681e3891d92b73aa0e7fb)
- [SCMI_POWER_STATE_ID_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga7cf257fa63dd2ad77912612b82eb1fa8)
- [SCMI_POWER_STATE_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga9765bcc859e9f4f550d6f4974d154eab)
- [SCMI_POWER_STATE_GENERIC_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga61d565a37849fcde1b5737bb35b71896)
- [SCMI_POWER_STATE_GENERIC_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga359cfeea3432e62b39ab063855b8227c)
- [scmi_power_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga0969968c4d6b94868295172c0408031b)
- [scmi_power_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#gadc7a2fbf0c4cab570d3a567ce548c947)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[上一章](P026_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rcar-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__drivers__pwm__pwm_utils.h_文件参考.md)
