---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-13
title: 电源域协议（Power Domain Protocol）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_电源域协议（Power Domain Protocol）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通过 SCMI 进行电源域状态管理。

<a id="details"></a>

通过 SCMI 进行电源域状态管理。

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_power_2Eh"></a>

```c
file power.h
```

相关声明：[power.h](../api_file_network_device_reference/P027_zephyr__drivers__firmware__scmi__power.h_文件参考.md)。

系统控制与管理接口（SCMI）电源域协议（Power Domain Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.2\_数据结构（Data Structures）

<a id="r_scmi_5Fpower_5Fstate_5Fconfig"></a>

```c
struct scmi_power_state_config
```

相关声明：[scmi_power_state_config](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md)。

描述POWER_STATE_SET命令的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.3\_宏定义（Macros）

<a id="r_ga8c95da0a183bcdde6e6fde5b111d9c22"></a>

```c
#define SCMI_POWER_STATE_SET_FLAGS_ASYNC BIT(0)
```

相关声明：[SCMI_POWER_STATE_SET_FLAGS_ASYNC](#ga8c95da0a183bcdde6e6fde5b111d9c22)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`POWER_STATE_SET` 标志：异步执行电源状态变化（Asynchronous Power State Change）。

<a id="r_ga74838410dad55ba27d05e384df279894"></a>

```c
#define SCMI_POWER_DOMAIN_PROTOCOL_SUPPORTED_VERSION 0x30001
```

相关声明：[SCMI_POWER_DOMAIN_PROTOCOL_SUPPORTED_VERSION](#ga74838410dad55ba27d05e384df279894)。

此驱动支持的 SCMI 电源域协议（Power Domain Protocol）版本。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_ga0969968c4d6b94868295172c0408031b"></a>

```c
int scmi_power_state_set (struct scmi_power_state_config *cfg)
```

相关声明：[scmi_power_state_set](#ga0969968c4d6b94868295172c0408031b)、[scmi_power_state_config](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md)。

发送 `POWER_STATE_SET` 命令并取得响应（Reply）。

<a id="r_gadc7a2fbf0c4cab570d3a567ce548c947"></a>

```c
int scmi_power_state_get (uint32_t domain_id, uint32_t *power_state)
```

相关声明：[scmi_power_state_get](#gadc7a2fbf0c4cab570d3a567ce548c947)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询电源域状态（Power Domain State）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 13.5\_SCMI 电源域状态参数（State Parameters）

<a id="r_ga184ce394bf8681e3891d92b73aa0e7fb"></a>

```c
#define SCMI_POWER_STATE_TYPE_SHIFT 30U
```

相关声明：[SCMI_POWER_STATE_TYPE_SHIFT](#ga184ce394bf8681e3891d92b73aa0e7fb)。

电源状态类型字段（Power State Type Field）的移位量。

<a id="r_ga7cf257fa63dd2ad77912612b82eb1fa8"></a>

```c
#define SCMI_POWER_STATE_ID_MASK (BIT(28) - 1)
```

相关声明：[SCMI_POWER_STATE_ID_MASK](#ga7cf257fa63dd2ad77912612b82eb1fa8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电源状态标识字段（Power State ID Field）的掩码。

<a id="r_ga9765bcc859e9f4f550d6f4974d154eab"></a>

```c
#define SCMI_POWER_STATE_PARAM(type, id)
```

相关声明：[SCMI_POWER_STATE_PARAM](#ga9765bcc859e9f4f550d6f4974d154eab)。

构造 SCMI 电源状态参数（Power State Parameter）。

## 13.6\_SCMI 电源域通用状态（Generic States）

<a id="r_ga61d565a37849fcde1b5737bb35b71896"></a>

```c
#define SCMI_POWER_STATE_GENERIC_ON SCMI_POWER_STATE_PARAM(0, 0)
```

相关声明：[SCMI_POWER_STATE_GENERIC_ON](#ga61d565a37849fcde1b5737bb35b71896)、[SCMI_POWER_STATE_PARAM](#ga9765bcc859e9f4f550d6f4974d154eab)。

电源域处于开启状态（ON）。

<a id="r_ga359cfeea3432e62b39ab063855b8227c"></a>

```c
#define SCMI_POWER_STATE_GENERIC_OFF SCMI_POWER_STATE_PARAM(1, 0)
```

相关声明：[SCMI_POWER_STATE_GENERIC_OFF](#ga359cfeea3432e62b39ab063855b8227c)、[SCMI_POWER_STATE_PARAM](#ga9765bcc859e9f4f550d6f4974d154eab)。

电源域处于关闭状态（OFF）。

## 13.7\_详细说明（Detailed Documentation）

<a id="ga74838410dad55ba27d05e384df279894"></a>

### `SCMI_POWER_DOMAIN_PROTOCOL_SUPPORTED_VERSION`

```c
#define SCMI_POWER_DOMAIN_PROTOCOL_SUPPORTED_VERSION 0x30001
```

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

此驱动支持的 SCMI 电源域协议（Power Domain Protocol）版本。

<a id="ga359cfeea3432e62b39ab063855b8227c"></a>

### `SCMI_POWER_STATE_GENERIC_OFF`

```c
#define SCMI_POWER_STATE_GENERIC_OFF SCMI_POWER_STATE_PARAM(1, 0)
```

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

电源域处于关闭状态（OFF）。

<a id="ga61d565a37849fcde1b5737bb35b71896"></a>

### `SCMI_POWER_STATE_GENERIC_ON`

```c
#define SCMI_POWER_STATE_GENERIC_ON SCMI_POWER_STATE_PARAM(0, 0)
```

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

电源域处于开启状态（ON）。

<a id="ga7cf257fa63dd2ad77912612b82eb1fa8"></a>

### `SCMI_POWER_STATE_ID_MASK`

```c
#define SCMI_POWER_STATE_ID_MASK (BIT(28) - 1)
```

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

电源状态标识字段（Power State ID Field）的掩码。

<a id="ga9765bcc859e9f4f550d6f4974d154eab"></a>

### `SCMI_POWER_STATE_PARAM`

```c
#define SCMI_POWER_STATE_PARAM ( type, id )
```

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

展开值（Value）：

```c
((((type) & BIT(0)) << SCMI_POWER_STATE_TYPE_SHIFT) | \
 ((id) & SCMI_POWER_STATE_ID_MASK))
```

构造 SCMI 电源状态参数（Power State Parameter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 电源状态类型（Power State Type）。 |
| `id` | 电源状态标识（Power State ID）。 |

<a id="ga8c95da0a183bcdde6e6fde5b111d9c22"></a>

### `SCMI_POWER_STATE_SET_FLAGS_ASYNC`

```c
#define SCMI_POWER_STATE_SET_FLAGS_ASYNC BIT(0)
```

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

`POWER_STATE_SET` 标志：异步执行电源状态变化（Asynchronous Power State Change）。

<a id="ga184ce394bf8681e3891d92b73aa0e7fb"></a>

### `SCMI_POWER_STATE_TYPE_SHIFT`

```c
#define SCMI_POWER_STATE_TYPE_SHIFT 30U
```

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

电源状态类型字段（Power State Type Field）的移位量。

<a id="gadc7a2fbf0c4cab570d3a567ce548c947"></a>

### `scmi_power_state_get()`

```c
int scmi_power_state_get ( uint32_t domain_id, uint32_t * power_state )
```

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

查询电源域状态（Power Domain State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domain_id` | 本次查询所针对的电源域标识（Power Domain ID）。 |
| `power_state` | 通过此命令设置的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga0969968c4d6b94868295172c0408031b"></a>

### `scmi_power_state_set()`

```c
int scmi_power_state_set ( struct scmi_power_state_config * cfg)
```

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

发送 `POWER_STATE_SET` 命令并取得响应（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cfg` | 指向包含待设置配置的结构体的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 13.8\_原页交叉引用（Cross References）

- [power.h](../api_file_network_device_reference/P027_zephyr__drivers__firmware__scmi__power.h_文件参考.md)
- [scmi_power_state_config](../platform_security_model_reference/P046_scmi_power_state_config_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__scmi__power_html_ga184ce394bf8681e3891d92b73aa0e7fb"></a>
<a id="agroup__scmi__power_html_ga7cf257fa63dd2ad77912612b82eb1fa8"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_RM3100 API主题.md) · [返回大纲](大纲.md) · [下一章](P014_复位域管理协议（Reset domain management Protocol）.md)
