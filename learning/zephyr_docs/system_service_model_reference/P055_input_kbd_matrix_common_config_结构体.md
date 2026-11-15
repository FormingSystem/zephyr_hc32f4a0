---
id: learning.zephyr-docs.system-service-model-reference.page-55
title: input_kbd_matrix_common_config_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structinput__kbd__matrix__common__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_input\_kbd\_matrix\_common\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structinput__kbd__matrix__common__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用键盘矩阵（Keyboard Matrix）配置。

```c
#include <zephyr/input/input_kbd_matrix.h>
```

<a id="details"></a>

通用键盘矩阵配置。此结构体必须放在驱动配置结构体的首个位置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_ace0bafa079826819b7df7950cb3e8212"></a>

```c
const struct input_kbd_matrix_api * api
```

相关声明：[input_kbd_matrix_api](P054_input_kbd_matrix_api_结构体.md)、[api](#ace0bafa079826819b7df7950cb3e8212)。

<a id="r_af3c4f2bcddf50dc2dbf0ad0e54230565"></a>

```c
uint8_t row_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[row_size](#af3c4f2bcddf50dc2dbf0ad0e54230565)。

<a id="r_adfb2b978f1d41bdff28acca17cc4ed3d"></a>

```c
uint8_t col_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[col_size](#adfb2b978f1d41bdff28acca17cc4ed3d)。

<a id="r_a34ce838e3ed4a5cb19c8ce961a9da947"></a>

```c
uint32_t poll_period_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[poll_period_us](#a34ce838e3ed4a5cb19c8ce961a9da947)。

<a id="r_ac67c028c2cf743c1854dc83aed8f4db4"></a>

```c
uint32_t stable_poll_period_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[stable_poll_period_us](#ac67c028c2cf743c1854dc83aed8f4db4)。

<a id="r_a81ccf8e0a1f49361f55737e0149bd656"></a>

```c
uint32_t poll_timeout_ms
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[poll_timeout_ms](#a81ccf8e0a1f49361f55737e0149bd656)。

<a id="r_a004cb35eede1e58b27730a46155540e9"></a>

```c
uint32_t debounce_down_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[debounce_down_us](#a004cb35eede1e58b27730a46155540e9)。

<a id="r_a545fba8a03ced44a95d7bb7f345d763f"></a>

```c
uint32_t debounce_up_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[debounce_up_us](#a545fba8a03ced44a95d7bb7f345d763f)。

<a id="r_a13374b57becd9314ea726ae888f1702a"></a>

```c
uint32_t settle_time_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[settle_time_us](#a13374b57becd9314ea726ae888f1702a)。

<a id="r_a2377a3c7cbd195bb6da3d4dfaf1f5972"></a>

```c
bool ghostkey_check
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ghostkey_check](#a2377a3c7cbd195bb6da3d4dfaf1f5972)。

<a id="r_ac2343c08359099f383f154655b371cf6"></a>

```c
kbd_row_t * actual_key_mask
```

相关声明：[kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)、[actual_key_mask](#ac2343c08359099f383f154655b371cf6)。

<a id="r_aafb384043bed6593b696e11fd34e0f97"></a>

```c
kbd_row_t * matrix_stable_state
```

相关声明：[kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)、[matrix_stable_state](#aafb384043bed6593b696e11fd34e0f97)。

<a id="r_a47d4177495c1e17b76c1f616720a3aa6"></a>

```c
kbd_row_t * matrix_unstable_state
```

相关声明：[kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)、[matrix_unstable_state](#a47d4177495c1e17b76c1f616720a3aa6)。

<a id="r_a361fd7c63b2ca643e4b957a6c1c85ae4"></a>

```c
kbd_row_t * matrix_previous_state
```

相关声明：[kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)、[matrix_previous_state](#a361fd7c63b2ca643e4b957a6c1c85ae4)。

<a id="r_a5da560d28d8bfc527d60c10e4aa29ffb"></a>

```c
kbd_row_t * matrix_new_state
```

相关声明：[kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)、[matrix_new_state](#a5da560d28d8bfc527d60c10e4aa29ffb)。

<a id="r_a0fbc6d10c2f15f3a0126e0c229ec9686"></a>

```c
uint8_t * scan_cycle_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_cycle_idx](#a0fbc6d10c2f15f3a0126e0c229ec9686)。

## 55.2\_详细说明（Detailed Documentation）

<a id="ac2343c08359099f383f154655b371cf6"></a>

### `actual_key_mask`

```c
kbd_row_t* input_kbd_matrix_common_config::actual_key_mask
```

<a id="ace0bafa079826819b7df7950cb3e8212"></a>

### `api`

```c
const struct input_kbd_matrix_api* input_kbd_matrix_common_config::api
```

<a id="adfb2b978f1d41bdff28acca17cc4ed3d"></a>

### `col_size`

```c
uint8_t input_kbd_matrix_common_config::col_size
```

<a id="a004cb35eede1e58b27730a46155540e9"></a>

### `debounce_down_us`

```c
uint32_t input_kbd_matrix_common_config::debounce_down_us
```

<a id="a545fba8a03ced44a95d7bb7f345d763f"></a>

### `debounce_up_us`

```c
uint32_t input_kbd_matrix_common_config::debounce_up_us
```

<a id="a2377a3c7cbd195bb6da3d4dfaf1f5972"></a>

### `ghostkey_check`

```c
bool input_kbd_matrix_common_config::ghostkey_check
```

<a id="a5da560d28d8bfc527d60c10e4aa29ffb"></a>

### `matrix_new_state`

```c
kbd_row_t* input_kbd_matrix_common_config::matrix_new_state
```

<a id="a361fd7c63b2ca643e4b957a6c1c85ae4"></a>

### `matrix_previous_state`

```c
kbd_row_t* input_kbd_matrix_common_config::matrix_previous_state
```

<a id="aafb384043bed6593b696e11fd34e0f97"></a>

### `matrix_stable_state`

```c
kbd_row_t* input_kbd_matrix_common_config::matrix_stable_state
```

<a id="a47d4177495c1e17b76c1f616720a3aa6"></a>

### `matrix_unstable_state`

```c
kbd_row_t* input_kbd_matrix_common_config::matrix_unstable_state
```

<a id="a34ce838e3ed4a5cb19c8ce961a9da947"></a>

### `poll_period_us`

```c
uint32_t input_kbd_matrix_common_config::poll_period_us
```

<a id="a81ccf8e0a1f49361f55737e0149bd656"></a>

### `poll_timeout_ms`

```c
uint32_t input_kbd_matrix_common_config::poll_timeout_ms
```

<a id="af3c4f2bcddf50dc2dbf0ad0e54230565"></a>

### `row_size`

```c
uint8_t input_kbd_matrix_common_config::row_size
```

<a id="a0fbc6d10c2f15f3a0126e0c229ec9686"></a>

### `scan_cycle_idx`

```c
uint8_t* input_kbd_matrix_common_config::scan_cycle_idx
```

<a id="a13374b57becd9314ea726ae888f1702a"></a>

### `settle_time_us`

```c
uint32_t input_kbd_matrix_common_config::settle_time_us
```

<a id="ac67c028c2cf743c1854dc83aed8f4db4"></a>

### `stable_poll_period_us`

```c
uint32_t input_kbd_matrix_common_config::stable_poll_period_us
```

本数据类型文档由以下文件生成：

- `zephyr/input/input_kbd_matrix.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/input/input_kbd_matrix.h](https://docs.zephyrproject.org/latest/doxygen/html/input__kbd__matrix_8h_source.html)
- [input_kbd_matrix_api](P054_input_kbd_matrix_api_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_input_kbd_matrix_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_input_kbd_matrix_common_data_结构体.md)
