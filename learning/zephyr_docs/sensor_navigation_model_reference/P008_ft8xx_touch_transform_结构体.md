---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-8
title: ft8xx_touch_transform_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structft8xx__touch__transform.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_ft8xx\_touch\_transform\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structft8xx__touch__transform.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存触摸屏校准数据（Touchscreen Calibration Data）的结构。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx.h>
```

<a id="details"></a>

保存触摸屏校准（touchscreen calibration）数据的结构体，其内容由 `ft8xx_calibrate()` 填写。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_aebc5352e00847e41b2d239a9265b5e45"></a>

```c
uint32_t a
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[a](#aebc5352e00847e41b2d239a9265b5e45)。

<a id="r_a307e6438e32a36ac78c76979925e5e1c"></a>

```c
uint32_t b
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[b](#a307e6438e32a36ac78c76979925e5e1c)。

<a id="r_ab86ed8962e01945c63751912c622b623"></a>

```c
uint32_t c
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[c](#ab86ed8962e01945c63751912c622b623)。

<a id="r_aeee5e2153eca64f1c5a6196d910c3d3e"></a>

```c
uint32_t d
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[d](#aeee5e2153eca64f1c5a6196d910c3d3e)。

<a id="r_a8c31db728937a0b69f01b9c3e265287a"></a>

```c
uint32_t e
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[e](#a8c31db728937a0b69f01b9c3e265287a)。

<a id="r_aa72829a35d054aa88fc8fd494e5eecbe"></a>

```c
uint32_t f
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[f](#aa72829a35d054aa88fc8fd494e5eecbe)。

## 8.2\_详细说明（Detailed Documentation）

<a id="aebc5352e00847e41b2d239a9265b5e45"></a>

### `a`

```c
uint32_t ft8xx_touch_transform::a
```

<a id="a307e6438e32a36ac78c76979925e5e1c"></a>

### `b`

```c
uint32_t ft8xx_touch_transform::b
```

<a id="ab86ed8962e01945c63751912c622b623"></a>

### `c`

```c
uint32_t ft8xx_touch_transform::c
```

<a id="aeee5e2153eca64f1c5a6196d910c3d3e"></a>

### `d`

```c
uint32_t ft8xx_touch_transform::d
```

<a id="a8c31db728937a0b69f01b9c3e265287a"></a>

### `e`

```c
uint32_t ft8xx_touch_transform::e
```

<a id="aa72829a35d054aa88fc8fd494e5eecbe"></a>

### `f`

```c
uint32_t ft8xx_touch_transform::f
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/ft8xx/ft8xx.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/ft8xx/ft8xx.h](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ft8xx_calibrate()](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga586f6ff1eddd5b596d2e35fb5fdd8148)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_cy8cmbr3xxx_config_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_gnss_data_结构体.md)
