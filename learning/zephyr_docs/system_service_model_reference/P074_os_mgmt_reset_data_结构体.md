---
id: learning.zephyr-docs.system-service-model-reference.page-74
title: os_mgmt_reset_data_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__reset__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_os\_mgmt\_reset\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__reset__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_OS_MGMT_RESET通知回调中提供的结构。该回调用于将待处理的设备重启请求（Device Reboot Request）通知应用，并授权或拒绝该请求。

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h>
```

<a id="details"></a>

MGMT_EVT_OP_OS_MGMT_RESET通知回调中提供的结构。该回调用于将待处理的设备重启请求（Device Reboot Request）通知应用，并授权或拒绝该请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 74.1\_数据成员（Data Fields）

<a id="r_aa9defc41c1e9aff601b5c98cb307bc01"></a>

```c
bool force
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[force](#aa9defc41c1e9aff601b5c98cb307bc01)。

包含 `force` 参数的值。

<a id="r_acefd2b805d33ea0127a5577148439ecc"></a>

```c
uint8_t boot_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[boot_mode](#acefd2b805d33ea0127a5577148439ecc)。

包含 `boot_mode` 参数的值。

## 74.2\_详细说明（Detailed Documentation）

<a id="acefd2b805d33ea0127a5577148439ecc"></a>

### `boot_mode`

```c
uint8_t os_mgmt_reset_data::boot_mode
```

包含 `boot_mode` 参数的值。

<a id="aa9defc41c1e9aff601b5c98cb307bc01"></a>

### `force`

```c
bool os_mgmt_reset_data::force
```

包含 `force` 参数的值。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h`

## 74.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_OS_MGMT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52)
- [zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P073_os_mgmt_info_check_结构体.md) · [返回大纲](大纲.md) · [下一章](P075_regset_target_lib_config_结构体.md)
