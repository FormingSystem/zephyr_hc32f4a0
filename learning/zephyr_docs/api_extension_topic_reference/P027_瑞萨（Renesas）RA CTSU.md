---
id: learning.zephyr-docs.api-extension-topic-reference.page-27
title: 瑞萨（Renesas）RA CTSU
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__ra__ctsu__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_瑞萨（Renesas）RA CTSU

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__ra__ctsu__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

瑞萨 RA 电容触摸传感器单元（Capacitive Touch Sensor Unit）。

<a id="details"></a>

瑞萨 RA 电容触摸传感器单元（Capacitive Touch Sensor Unit）。

<a id="header-files"></a>
<a id="files"></a>

## 27.1\_文件（Files）

<a id="r_input_5Frenesas_5Fra_5Fctsu_2Eh"></a>

```c
file input_renesas_ra_ctsu.h
```

相关声明：[input_renesas_ra_ctsu.h](../api_file_supplement_reference/P049_zephyr__input__input_renesas_ra_ctsu.h_文件参考.md)。

Renesas RA电容触摸感应单元（CTSU）输入驱动的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 27.2\_数据结构（Data Structures）

<a id="r_renesas_5Fra_5Fctsu_5Ftouch_5Fcfg"></a>

```c
struct renesas_ra_ctsu_touch_cfg
```

相关声明：[renesas_ra_ctsu_touch_cfg](../device_power_control_model_reference/P074_renesas_ra_ctsu_touch_cfg_结构体.md)。

Renesas RA电容触摸感应单元（CTSU）设备的配置数据。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.3\_函数（Functions）

<a id="r_ga163c39f1fb4f472f08090d0bc54ac4a2"></a>

```c
int renesas_ra_ctsu_group_configure (const struct device *dev, const struct renesas_ra_ctsu_touch_cfg *cfg)
```

相关声明：[renesas_ra_ctsu_group_configure](#ga163c39f1fb4f472f08090d0bc54ac4a2)、[device](../device_reference/P002_设备对象结构.md)、[renesas_ra_ctsu_touch_cfg](../device_power_control_model_reference/P074_renesas_ra_ctsu_touch_cfg_结构体.md)。

使用 Renesas QE 电容触摸工作流（QE for Capacitive Touch Workflow）生成的配置，配置电容触摸感应单元组设备（CTSU Group Device）。

## 27.4\_详细说明（Detailed Documentation）

<a id="ga163c39f1fb4f472f08090d0bc54ac4a2"></a>

### `renesas_ra_ctsu_group_configure()`

```c
int renesas_ra_ctsu_group_configure ( const struct device * dev, const struct renesas_ra_ctsu_touch_cfg * cfg )
```

```c
#include <zephyr/input/input_renesas_ra_ctsu.h>
```

使用 Renesas QE 电容触摸工作流（QE for Capacitive Touch Workflow）生成的配置，配置电容触摸感应单元组设备（CTSU Group Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向输入设备实例（Input Device Instance）的指针（Pointer）。 |
| `cfg` | 指向设备配置数据（Configuration Data）的指针（Pointer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 未启用 `INPUT_RENESAS_RA_QE_TOUCH_CFG` 时。 |
| `-errno` | 失败。 |


## 27.5\_原页交叉引用（Cross References）

- [input_renesas_ra_ctsu.h](../api_file_supplement_reference/P049_zephyr__input__input_renesas_ra_ctsu.h_文件参考.md)
- [renesas_ra_ctsu_touch_cfg](../device_power_control_model_reference/P074_renesas_ra_ctsu_touch_cfg_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P026_平台环境控制接口（PECI）.md) · [返回大纲](大纲.md) · [下一章](P028_瑞萨（Renesas）RX CTSU.md)
