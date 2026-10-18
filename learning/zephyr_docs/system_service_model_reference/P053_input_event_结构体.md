---
id: learning.zephyr-docs.system-service-model-reference.page-53
title: input_event_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structinput__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_input\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structinput__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

输入事件（Input Event）结构。

```c
#include <zephyr/input/input.h>
```

<a id="details"></a>

输入事件（Input event）结构体，表示单个输入事件，例如某个按键或按钮的按下事件，或者单个轴的绝对坐标或相对坐标。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_a4022d0ddf8ca5be9b478cd0b2758d067"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#a4022d0ddf8ca5be9b478cd0b2758d067)。

产生事件的设备，或者 `NULL`。

<a id="r_a015732c5d67a5374b93e980282a2a9d7"></a>

```c
uint8_t sync
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sync](#a015732c5d67a5374b93e980282a2a9d7)。

同步标志（Sync flag）。

<a id="r_af74a1741fef30ee375d4a71628a9656e"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#af74a1741fef30ee375d4a71628a9656e)。

事件类型，参见 `INPUT_EV_CODES`。

<a id="r_a5abe903fbf3b29643578be85c17ba6aa"></a>

```c
uint16_t code
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[code](#a5abe903fbf3b29643578be85c17ba6aa)。

事件代码，参见 `INPUT_KEY_CODES`、`INPUT_BTN_CODES`、`INPUT_ABS_CODES`、`INPUT_REL_CODES` 和 `INPUT_MSC_CODES`。

<a id="r_af18b63e5263e73fce8e38838e37d2bae"></a>

```c
int32_t value
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[value](#af18b63e5263e73fce8e38838e37d2bae)。

事件值。

## 53.2\_详细说明（Detailed Documentation）

<a id="a5abe903fbf3b29643578be85c17ba6aa"></a>

### `code`

```c
uint16_t input_event::code
```

事件代码，参见 `INPUT_KEY_CODES`、`INPUT_BTN_CODES`、`INPUT_ABS_CODES`、`INPUT_REL_CODES` 和 `INPUT_MSC_CODES`。

<a id="a4022d0ddf8ca5be9b478cd0b2758d067"></a>

### `dev`

```c
const struct device* input_event::dev
```

产生事件的设备，或者 `NULL`。

<a id="a015732c5d67a5374b93e980282a2a9d7"></a>

### `sync`

```c
uint8_t input_event::sync
```

同步标志（Sync flag）。

<a id="af74a1741fef30ee375d4a71628a9656e"></a>

### `type`

```c
uint8_t input_event::type
```

事件类型，参见 `INPUT_EV_CODES`。

<a id="af18b63e5263e73fce8e38838e37d2bae"></a>

### `value`

```c
int32_t input_event::value
```

事件值。

本数据类型文档由以下文件生成：

- `zephyr/input/input.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/input/input.h](https://docs.zephyrproject.org/latest/doxygen/html/input_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [INPUT_EV_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_EV_CODES)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [INPUT_KEY_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_KEY_CODES)
- [INPUT_BTN_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_BTN_CODES)
- [INPUT_ABS_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_ABS_CODES)
- [INPUT_REL_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_REL_CODES)
- [INPUT_MSC_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_MSC_CODES)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_input_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_input_kbd_matrix_api_结构体.md)
