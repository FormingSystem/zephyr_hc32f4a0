---
id: learning.zephyr-docs.api-extension-topic-reference.page-28
title: 瑞萨（Renesas）RX CTSU
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__rx__ctsu__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_瑞萨（Renesas）RX CTSU

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__rx__ctsu__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

瑞萨 RX 电容触摸传感器单元（Capacitive Touch Sensor Unit）。

<a id="details"></a>

瑞萨 RX 电容触摸传感器单元（Capacitive Touch Sensor Unit）。

<a id="header-files"></a>
<a id="files"></a>

## 28.1\_文件（Files）

<a id="r_input_5Frenesas_5Frx_5Fctsu_2Eh"></a>

```c
file input_renesas_rx_ctsu.h
```

相关声明：[input_renesas_rx_ctsu.h](../api_file_supplement_reference/P050_zephyr__input__input_renesas_rx_ctsu.h_文件参考.md)。

Renesas RX电容触摸感应单元（CTSU）输入驱动的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 28.2\_数据结构（Data Structures）

<a id="r_renesas_5Frx_5Fctsu_5Ftouch_5Fcfg"></a>

```c
struct renesas_rx_ctsu_touch_cfg
```

相关声明：[renesas_rx_ctsu_touch_cfg](../device_power_control_model_reference/P075_renesas_rx_ctsu_touch_cfg_结构体.md)。

Renesas RX电容触摸感应单元（CTSU）设备的配置数据。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.3\_函数（Functions）

<a id="r_ga531fdc46f91ffa0b0fdfc787c7a26145"></a>

```c
int renesas_rx_ctsu_group_configure (const struct device *dev, const struct renesas_rx_ctsu_touch_cfg *cfg)
```

相关声明：[renesas_rx_ctsu_group_configure](#ga531fdc46f91ffa0b0fdfc787c7a26145)、[device](../device_reference/P002_设备对象结构.md)、[renesas_rx_ctsu_touch_cfg](../device_power_control_model_reference/P075_renesas_rx_ctsu_touch_cfg_结构体.md)。

使用 Renesas QE 电容触摸工作流（QE for Capacitive Touch Workflow）生成的配置，配置电容触摸感应单元组设备（CTSU Group Device）。

## 28.4\_详细说明（Detailed Documentation）

<a id="ga531fdc46f91ffa0b0fdfc787c7a26145"></a>

### `renesas_rx_ctsu_group_configure()`

```c
int renesas_rx_ctsu_group_configure ( const struct device * dev, const struct renesas_rx_ctsu_touch_cfg * cfg )
```

```c
#include <zephyr/input/input_renesas_rx_ctsu.h>
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
| `-ENOSYS` | 未启用 `INPUT_RENESAS_RX_QE_TOUCH_CFG` 时。 |
| `-errno` | 失败。 |


## 28.5\_原页交叉引用（Cross References）

- [input_renesas_rx_ctsu.h](../api_file_supplement_reference/P050_zephyr__input__input_renesas_rx_ctsu.h_文件参考.md)
- [renesas_rx_ctsu_touch_cfg](../device_power_control_model_reference/P075_renesas_rx_ctsu_touch_cfg_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P027_瑞萨（Renesas）RA CTSU.md) · [返回大纲](大纲.md) · [下一章](P029_S9706 API主题.md)
