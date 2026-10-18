---
id: learning.zephyr-docs.system-service-model-reference.page-54
title: input_kbd_matrix_api_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structinput__kbd__matrix__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_input\_kbd\_matrix\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structinput__kbd__matrix__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

键盘矩阵（Keyboard Matrix）的内部API。

```c
#include <zephyr/input/input_kbd_matrix.h>
```

<a id="details"></a>

键盘矩阵（Keyboard Matrix）的内部API。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_af8211d738527ac44876dd07869862f20"></a>

```c
void(* drive_column )(const struct device *dev, int col)
```

相关声明：[drive_column](#af8211d738527ac44876dd07869862f20)、[device](../device_reference/P002_设备对象结构.md)。

请求驱动指定列。

<a id="r_af04e3f78fde3297a70a63c8a8addb477"></a>

```c
kbd_row_t(* read_row )(const struct device *dev)
```

相关声明：[kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)、[read_row](#af04e3f78fde3297a70a63c8a8addb477)、[device](../device_reference/P002_设备对象结构.md)。

读取矩阵行。

<a id="r_aaae2b1eb357fb4b7f1881ef496d79560"></a>

```c
void(* set_detect_mode )(const struct device *dev, bool enabled)
```

相关声明：[set_detect_mode](#aaae2b1eb357fb4b7f1881ef496d79560)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

请求将矩阵置于检测模式（detection mode）。

## 54.2\_详细说明（Detailed Documentation）

<a id="af8211d738527ac44876dd07869862f20"></a>

### `drive_column`

```c
void(* input_kbd_matrix_api::drive_column) (const struct device *dev, int col)
```

请求驱动指定列。

请求驱动指定矩阵列、不驱动任何列或驱动所有列。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向键盘矩阵（keyboard matrix）设备的指针。 |
| `col` | 要驱动的列，或者 `INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE`、`INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL`。 |

<a id="af04e3f78fde3297a70a63c8a8addb477"></a>

### `read_row`

```c
kbd_row_t(* input_kbd_matrix_api::read_row) (const struct device *dev)
```

读取矩阵行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向键盘矩阵（keyboard matrix）设备的指针。 |

<a id="aaae2b1eb357fb4b7f1881ef496d79560"></a>

### `set_detect_mode`

```c
void(* input_kbd_matrix_api::set_detect_mode) (const struct device *dev, bool enabled)
```

请求将矩阵置于检测模式（detection mode）。

请求将驱动置于检测模式。在请求驱动所有列之后调用，通常需要重新启用行引脚变化中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向键盘矩阵（keyboard matrix）设备的指针。 |
| `enabled` | 应启用还是禁用检测模式。 |

本数据类型文档由以下文件生成：

- `zephyr/input/input_kbd_matrix.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/input/input_kbd_matrix.h](https://docs.zephyrproject.org/latest/doxygen/html/input__kbd__matrix_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga2f35f23d426f93f71057a31f612a88de)
- [INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga6d27ba5612c09d80087e854b21fb9e65)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_input_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_input_kbd_matrix_common_config_结构体.md)
