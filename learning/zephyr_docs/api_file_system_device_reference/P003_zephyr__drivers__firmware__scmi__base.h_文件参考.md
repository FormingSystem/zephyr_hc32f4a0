---
id: learning.zephyr-docs.api-file-system-device-reference.page-3
title: zephyr__drivers__firmware__scmi__base.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/base_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_base.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/base_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）基础协议（Base Protocol）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

查看此文件的源码。

系统控制与管理接口（SCMI）基础协议（Base Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

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

## 3.2\_宏定义（Macros）

<a id="r_ga0d0b3a552cfacc8613d48d4bafe96f8c"></a>

```c
#define SCMI_BASE_PROTOCOL_SUPPORTED_VERSION 0x20001
```

相关声明：[SCMI_BASE_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga0d0b3a552cfacc8613d48d4bafe96f8c)。

支持的系统控制与管理接口基础协议（SCMI Base protocol）版本。

<a id="r_ga96e448d4c7b1558ec242a2409a94abaa"></a>

```c
#define SCMI_BASE_AGENT_ID_OWN 0xFFFFFFFF
```

相关声明：[SCMI_BASE_AGENT_ID_OWN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga96e448d4c7b1558ec242a2409a94abaa)。

用于向平台请求调用代理（agent）身份的特殊参数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga286e1a0dff35750c88b2ffe9372aae0d"></a>

```c
int scmi_base_get_num_agents (uint8_t *num_agents)
```

相关声明：[scmi_base_get_num_agents](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga286e1a0dff35750c88b2ffe9372aae0d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

SCMI 基础协议：获取代理数量。

<a id="r_ga9be1e92e28837b9ee64d8b792897bacf"></a>

```c
int scmi_base_get_platform_info (struct scmi_platform_info *rev)
```

相关声明：[scmi_base_get_platform_info](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga9be1e92e28837b9ee64d8b792897bacf)、[scmi_platform_info](../platform_security_model_reference/P045_scmi_platform_info_结构体.md)。

SCMI 基础协议：获取平台信息。

<a id="r_gaf4c82d6c1faffae9fc3f2070de52d11a"></a>

```c
int scmi_base_discover_agent (uint32_t agent_id, struct scmi_agent_info *agent_inf)
```

相关声明：[scmi_base_discover_agent](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#gaf4c82d6c1faffae9fc3f2070de52d11a)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[scmi_agent_info](../platform_security_model_reference/P032_scmi_agent_info_结构体.md)。

SCMI 基础协议：发现代理名称及代理 ID。

<a id="r_gacb8772d6c7b59168ab2ae043dc4852f1"></a>

```c
int scmi_base_device_permission (uint32_t agent_id, uint32_t device_id, bool allow)
```

相关声明：[scmi_base_device_permission](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#gacb8772d6c7b59168ab2ae043dc4852f1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SCMI 基础协议：设置代理访问设备的权限。

<a id="r_ga161b383297fe35f90d9d25d02f30633d"></a>

```c
int scmi_base_reset_agent_cfg (uint32_t agent_id, bool reset_perm)
```

相关声明：[scmi_base_reset_agent_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga161b383297fe35f90d9d25d02f30633d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SCMI 基础协议：重置由某个代理配置的平台资源设置。


## 3.4\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/protocol.h](../api_source_reference/P156_protocol.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P052_base.h_源码浏览.md)
- [scmi_platform_info](../platform_security_model_reference/P045_scmi_platform_info_结构体.md)
- [scmi_agent_info](../platform_security_model_reference/P032_scmi_agent_info_结构体.md)
- [SCMI_BASE_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga0d0b3a552cfacc8613d48d4bafe96f8c)
- [SCMI_BASE_AGENT_ID_OWN](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga96e448d4c7b1558ec242a2409a94abaa)
- [scmi_base_get_num_agents](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga286e1a0dff35750c88b2ffe9372aae0d)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [scmi_base_get_platform_info](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga9be1e92e28837b9ee64d8b792897bacf)
- [scmi_base_discover_agent](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#gaf4c82d6c1faffae9fc3f2070de52d11a)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [scmi_base_device_permission](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#gacb8772d6c7b59168ab2ae043dc4852f1)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [scmi_base_reset_agent_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__base.html#ga161b383297fe35f90d9d25d02f30633d)

<a id="header-details"></a>

---

[上一章](P002_zephyr__bluetooth__services__ans.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__sensor__bq274xx.h_文件参考.md)
