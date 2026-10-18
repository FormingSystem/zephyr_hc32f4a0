---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-78
title: sd_switch_caps_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsd__switch__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_sd\_switch\_caps\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsd__switch__caps.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD切换能力（Switch Capabilities）。

```c
#include <zephyr/sd/sd_spec.h>
```

<a id="details"></a>

SD 切换能力（Switch capabilities）。记录 SD 卡的切换能力，通过 `CMD6` 设置和查询这些能力。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 78.1\_数据成员（Data Fields）

<a id="r_a7465b3fe6bd1f317eeb3283a25da7278"></a>

```c
enum hs_max_data_rate hs_max_dtr
```

相关声明：[hs_max_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a2093143614e52f69e173289391d7e91c)、[hs_max_dtr](#a7465b3fe6bd1f317eeb3283a25da7278)。

<a id="r_ab09d80f61bc79857ee39604959c8a578"></a>

```c
enum uhs_max_data_rate uhs_max_dtr
```

相关声明：[uhs_max_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a5466ef2e30578d03c61831aa09fd7b9a)、[uhs_max_dtr](#ab09d80f61bc79857ee39604959c8a578)。

<a id="r_a29024de744d65fb3d8fe51c4d4424aee"></a>

```c
enum sd_bus_speed bus_speed
```

相关声明：[sd_bus_speed](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a6b42b86d8f2ba4f29787c7c6f3d97f36)、[bus_speed](#a29024de744d65fb3d8fe51c4d4424aee)。

<a id="r_a7262e4be5e3f59d047e569e1c24f04b3"></a>

```c
enum sd_driver_type sd_drv_type
```

相关声明：[sd_driver_type](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a314c38b1b0603c003e67b5dec2228d4b)、[sd_drv_type](#a7262e4be5e3f59d047e569e1c24f04b3)。

<a id="r_a4b531af598bea14c90b8973daf1422dc"></a>

```c
enum sd_current_limit sd_current_limit
```

相关声明：[sd_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a238de48c0cb55d173b6b874f4930c537)、[sd_current_limit](#a4b531af598bea14c90b8973daf1422dc)。

## 78.2\_详细说明（Detailed Documentation）

<a id="a29024de744d65fb3d8fe51c4d4424aee"></a>

### `bus_speed`

```c
enum sd_bus_speed sd_switch_caps::bus_speed
```

<a id="a7465b3fe6bd1f317eeb3283a25da7278"></a>

### `hs_max_dtr`

```c
enum hs_max_data_rate sd_switch_caps::hs_max_dtr
```

<a id="a4b531af598bea14c90b8973daf1422dc"></a>

### `sd_current_limit`

```c
enum sd_current_limit sd_switch_caps::sd_current_limit
```

<a id="a7262e4be5e3f59d047e569e1c24f04b3"></a>

### `sd_drv_type`

```c
enum sd_driver_type sd_switch_caps::sd_drv_type
```

<a id="ab09d80f61bc79857ee39604959c8a578"></a>

### `uhs_max_dtr`

```c
enum uhs_max_data_rate sd_switch_caps::uhs_max_dtr
```

本数据类型文档由以下文件生成：

- `zephyr/sd/sd_spec.h`

## 78.3\_原页交叉引用（Cross References）

- [zephyr/sd/sd_spec.h](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)
- [hs_max_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a2093143614e52f69e173289391d7e91c)
- [uhs_max_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a5466ef2e30578d03c61831aa09fd7b9a)
- [sd_bus_speed](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a6b42b86d8f2ba4f29787c7c6f3d97f36)
- [sd_driver_type](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a314c38b1b0603c003e67b5dec2228d4b)
- [sd_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a238de48c0cb55d173b6b874f4930c537)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P077_sd_scr_结构体.md) · [返回大纲](大纲.md) · [下一章](P079_sdhc_command_结构体.md)
