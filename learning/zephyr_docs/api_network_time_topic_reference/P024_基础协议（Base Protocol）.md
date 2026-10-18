---
id: learning.zephyr-docs.api-network-time-topic-reference.page-24
title: 基础协议（Base Protocol）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_基础协议（Base Protocol）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SCMI 基础协议操作。

<a id="details"></a>

SCMI 基础协议操作。

<a id="header-files"></a>
<a id="files"></a>

## 24.1\_文件（Files）

<a id="r_base_2Eh"></a>

```c
file base.h
```

相关声明：[base.h](../api_file_system_device_reference/P003_zephyr__drivers__firmware__scmi__base.h_文件参考.md)。

系统控制与管理接口（SCMI）基础协议（Base Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 24.2\_数据结构（Data Structures）

<a id="r_scmi_5Fplatform_5Finfo"></a>

```c
struct scmi_platform_info
```

相关声明：[scmi_platform_info](../platform_security_model_reference/P045_scmi_platform_info_结构体.md)。

系统控制与管理接口（SCMI）基础协议的修订版本信息。

<a id="r_scmi_5Fagent_5Finfo"></a>

```c
struct scmi_agent_info
```

相关声明：[scmi_agent_info](../platform_security_model_reference/P032_scmi_agent_info_结构体.md)。

系统控制与管理接口（SCMI）基础协议的代理信息。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.3\_宏定义（Macros）

<a id="r_ga0d0b3a552cfacc8613d48d4bafe96f8c"></a>

```c
#define SCMI_BASE_PROTOCOL_SUPPORTED_VERSION 0x20001
```

相关声明：[SCMI_BASE_PROTOCOL_SUPPORTED_VERSION](#ga0d0b3a552cfacc8613d48d4bafe96f8c)。

支持的系统控制与管理接口基础协议（SCMI Base protocol）版本。

<a id="r_ga96e448d4c7b1558ec242a2409a94abaa"></a>

```c
#define SCMI_BASE_AGENT_ID_OWN 0xFFFFFFFF
```

相关声明：[SCMI_BASE_AGENT_ID_OWN](#ga96e448d4c7b1558ec242a2409a94abaa)。

用于向平台请求调用代理（agent）身份的特殊参数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.4\_函数（Functions）

<a id="r_ga286e1a0dff35750c88b2ffe9372aae0d"></a>

```c
int scmi_base_get_num_agents (uint8_t *num_agents)
```

相关声明：[scmi_base_get_num_agents](#ga286e1a0dff35750c88b2ffe9372aae0d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

SCMI 基础协议：获取代理数量。

<a id="r_ga9be1e92e28837b9ee64d8b792897bacf"></a>

```c
int scmi_base_get_platform_info (struct scmi_platform_info *rev)
```

相关声明：[scmi_base_get_platform_info](#ga9be1e92e28837b9ee64d8b792897bacf)、[scmi_platform_info](../platform_security_model_reference/P045_scmi_platform_info_结构体.md)。

SCMI 基础协议：获取平台信息。

<a id="r_gaf4c82d6c1faffae9fc3f2070de52d11a"></a>

```c
int scmi_base_discover_agent (uint32_t agent_id, struct scmi_agent_info *agent_inf)
```

相关声明：[scmi_base_discover_agent](#gaf4c82d6c1faffae9fc3f2070de52d11a)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[scmi_agent_info](../platform_security_model_reference/P032_scmi_agent_info_结构体.md)。

SCMI 基础协议：发现代理名称及代理 ID。

<a id="r_gacb8772d6c7b59168ab2ae043dc4852f1"></a>

```c
int scmi_base_device_permission (uint32_t agent_id, uint32_t device_id, bool allow)
```

相关声明：[scmi_base_device_permission](#gacb8772d6c7b59168ab2ae043dc4852f1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SCMI 基础协议：设置代理访问设备的权限。

<a id="r_ga161b383297fe35f90d9d25d02f30633d"></a>

```c
int scmi_base_reset_agent_cfg (uint32_t agent_id, bool reset_perm)
```

相关声明：[scmi_base_reset_agent_cfg](#ga161b383297fe35f90d9d25d02f30633d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SCMI 基础协议：重置由某个代理配置的平台资源设置。

## 24.5\_详细说明（Detailed Documentation）

<a id="ga96e448d4c7b1558ec242a2409a94abaa"></a>

### `SCMI_BASE_AGENT_ID_OWN`

```c
#define SCMI_BASE_AGENT_ID_OWN 0xFFFFFFFF
```

```c
#include <zephyr/drivers/firmware/scmi/base.h>
```

用于向平台请求调用代理（agent）身份的特殊参数。

<a id="ga0d0b3a552cfacc8613d48d4bafe96f8c"></a>

### `SCMI_BASE_PROTOCOL_SUPPORTED_VERSION`

```c
#define SCMI_BASE_PROTOCOL_SUPPORTED_VERSION 0x20001
```

```c
#include <zephyr/drivers/firmware/scmi/base.h>
```

支持的系统控制与管理接口基础协议（SCMI Base protocol）版本。

<a id="gacb8772d6c7b59168ab2ae043dc4852f1"></a>

### `scmi_base_device_permission()`

```c
int scmi_base_device_permission ( uint32_t agent_id, uint32_t device_id, bool allow )
```

```c
#include <zephyr/drivers/firmware/scmi/base.h>
```

SCMI 基础协议：设置代理访问设备的权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `agent_id` | SCMI 代理标识符（agent ID）。 |
| `device_id` | SCMI 设备标识符（device ID）。 |
| `allow` | 设为 true 时允许代理访问该设备。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaf4c82d6c1faffae9fc3f2070de52d11a"></a>

### `scmi_base_discover_agent()`

```c
int scmi_base_discover_agent ( uint32_t agent_id, struct scmi_agent_info * agent_inf )
```

```c
#include <zephyr/drivers/firmware/scmi/base.h>
```

SCMI 基础协议：发现代理名称及代理 ID。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `agent_id` | SCMI 代理 ID。设为 `SCMI_BASE_AGENT_ID_OWN` 时，平台返回调用方的 SCMI 代理 ID。 |
| `agent_inf` | 指向 SCMI 代理信息结构体 `scmi_agent_info` 的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga286e1a0dff35750c88b2ffe9372aae0d"></a>

### `scmi_base_get_num_agents()`

```c
int scmi_base_get_num_agents ( uint8_t * num_agents)
```

```c
#include <zephyr/drivers/firmware/scmi/base.h>
```

SCMI 基础协议：获取代理数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `num_agents` | 用于保存代理数量的指针。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负 `errno` 值。

<a id="ga9be1e92e28837b9ee64d8b792897bacf"></a>

### `scmi_base_get_platform_info()`

```c
int scmi_base_get_platform_info ( struct scmi_platform_info * rev)
```

```c
#include <zephyr/drivers/firmware/scmi/base.h>
```

SCMI 基础协议：获取平台信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rev` | 指向平台信息结构体 `scmi_platform_info` 的指针。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负 `errno` 值。

<a id="ga161b383297fe35f90d9d25d02f30633d"></a>

### `scmi_base_reset_agent_cfg()`

```c
int scmi_base_reset_agent_cfg ( uint32_t agent_id, bool reset_perm )
```

```c
#include <zephyr/drivers/firmware/scmi/base.h>
```

SCMI 基础协议：重置由某个代理配置的平台资源设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `agent_id` | SCMI 代理标识符（agent ID）。 |
| `reset_perm` | 设为 true 时重置该代理的全部访问权限设置。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 24.6\_原页交叉引用（Cross References）

- [base.h](../api_file_system_device_reference/P003_zephyr__drivers__firmware__scmi__base.h_文件参考.md)
- [scmi_platform_info](../platform_security_model_reference/P045_scmi_platform_info_结构体.md)
- [scmi_agent_info](../platform_security_model_reference/P032_scmi_agent_info_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P023_NXP FlexIO API主题.md) · [返回大纲](大纲.md) · [下一章](P025_触摸屏事件（Touchscreen Events）.md)
