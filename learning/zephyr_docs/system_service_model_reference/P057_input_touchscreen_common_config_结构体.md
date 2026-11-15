---
id: learning.zephyr-docs.system-service-model-reference.page-57
title: input_touchscreen_common_config_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structinput__touchscreen__common__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_input\_touchscreen\_common\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structinput__touchscreen__common__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用触摸屏（Touchscreen）配置。

```c
#include <zephyr/input/input_touch.h>
```

<a id="details"></a>

通用触摸屏配置。此结构体必须放在驱动配置结构体的首个位置。更多详情参见原文所列的 `touchscreem-common.yaml`。

译注：官方原文文件名写作 `touchscreem-common.yaml`，此处保留其拼写供对照。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_a35b6d8ccd36aa95d46cc24be2f94144b"></a>

```c
uint32_t screen_width
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[screen_width](#a35b6d8ccd36aa95d46cc24be2f94144b)。

触摸控制器自身坐标空间的水平分辨率。

<a id="r_ae534425e6069853cb80a3925fce8e2ad"></a>

```c
uint32_t screen_height
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[screen_height](#ae534425e6069853cb80a3925fce8e2ad)。

触摸控制器自身坐标空间的垂直分辨率。

<a id="r_a147cc66f165b5bf9e42b591ad77824c5"></a>

```c
bool inverted_x
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[inverted_x](#a147cc66f165b5bf9e42b591ad77824c5)。

X 轴反转。

<a id="r_abba0c9353f867287b047635ea358e057"></a>

```c
bool inverted_y
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[inverted_y](#abba0c9353f867287b047635ea358e057)。

Y 轴反转。

<a id="r_a408e21f2a9e57267d87d24f8a054f999"></a>

```c
bool swapped_x_y
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[swapped_x_y](#a408e21f2a9e57267d87d24f8a054f999)。

X 轴和 Y 轴互换。

<a id="r_ac7e996d150c9fef15ec733f4515bbf48"></a>

```c
uint32_t output_width
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[output_width](#ac7e996d150c9fef15ec733f4515bbf48)。

缩放后面板的水平分辨率；0 表示禁用缩放。

<a id="r_ad93cf875b2f1db32a8d4790296ccc6a3"></a>

```c
uint32_t output_height
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[output_height](#ad93cf875b2f1db32a8d4790296ccc6a3)。

缩放后面板的垂直分辨率；0 表示禁用缩放。

## 57.2\_详细说明（Detailed Documentation）

<a id="a147cc66f165b5bf9e42b591ad77824c5"></a>

### `inverted_x`

```c
bool input_touchscreen_common_config::inverted_x
```

X 轴反转。

<a id="abba0c9353f867287b047635ea358e057"></a>

### `inverted_y`

```c
bool input_touchscreen_common_config::inverted_y
```

Y 轴反转。

<a id="ad93cf875b2f1db32a8d4790296ccc6a3"></a>

### `output_height`

```c
uint32_t input_touchscreen_common_config::output_height
```

缩放后面板的垂直分辨率；0 表示禁用缩放。

<a id="ac7e996d150c9fef15ec733f4515bbf48"></a>

### `output_width`

```c
uint32_t input_touchscreen_common_config::output_width
```

缩放后面板的水平分辨率；0 表示禁用缩放。

<a id="ae534425e6069853cb80a3925fce8e2ad"></a>

### `screen_height`

```c
uint32_t input_touchscreen_common_config::screen_height
```

触摸控制器自身坐标空间的垂直分辨率。

<a id="a35b6d8ccd36aa95d46cc24be2f94144b"></a>

### `screen_width`

```c
uint32_t input_touchscreen_common_config::screen_width
```

触摸控制器自身坐标空间的水平分辨率。

<a id="a408e21f2a9e57267d87d24f8a054f999"></a>

### `swapped_x_y`

```c
bool input_touchscreen_common_config::swapped_x_y
```

X 轴和 Y 轴互换。

本数据类型文档由以下文件生成：

- `zephyr/input/input_touch.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/input/input_touch.h](https://docs.zephyrproject.org/latest/doxygen/html/input__touch_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_input_kbd_matrix_common_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_k_cellmeas_signal_info_结构体.md)
