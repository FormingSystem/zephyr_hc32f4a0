---
id: learning.zephyr-docs.system-service-model-reference.page-56
title: input_kbd_matrix_common_data_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structinput__kbd__matrix__common__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_input\_kbd\_matrix\_common\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structinput__kbd__matrix__common__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用键盘矩阵（Keyboard Matrix）数据。

```c
#include <zephyr/input/input_kbd_matrix.h>
```

<a id="details"></a>

通用键盘矩阵数据。此结构体必须放在驱动数据结构体的首个位置。

<a id="header-pub-methods"></a>
<a id="pub-methods"></a>

## 56.1\_公开成员函数（Public Member Functions）

<a id="r_ac66f323c17cd346bb1b0b0aa8fc2965a"></a>

```c
K_KERNEL_STACK_MEMBER (thread_stack, CONFIG_INPUT_KBD_MATRIX_THREAD_STACK_SIZE)
```

相关声明：[K_KERNEL_STACK_MEMBER](#ac66f323c17cd346bb1b0b0aa8fc2965a)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.2\_数据成员（Data Fields）

<a id="r_ac54780c609eb2abc67e468470ac3ef83"></a>

```c
uint32_t scan_clk_cycle [30U]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[scan_clk_cycle](#ac54780c609eb2abc67e468470ac3ef83)。

<a id="r_a53b66dca86734fa149b672583455bc61"></a>

```c
uint8_t scan_cycles_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_cycles_idx](#a53b66dca86734fa149b672583455bc61)。

<a id="r_afe0d57cf725c825097ba26b81bd2640c"></a>

```c
struct k_sem poll_lock
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[poll_lock](#afe0d57cf725c825097ba26b81bd2640c)。

<a id="r_a526586907a6f0e4d1316c4304adda336"></a>

```c
struct k_thread thread
```

相关声明：[k_thread](../thread_core_reference/P004_线程对象结构.md)、[thread](#a526586907a6f0e4d1316c4304adda336)。

## 56.3\_详细说明（Detailed Documentation）

<a id="ac66f323c17cd346bb1b0b0aa8fc2965a"></a>

### `K_KERNEL_STACK_MEMBER()`

```c
input_kbd_matrix_common_data::K_KERNEL_STACK_MEMBER ( thread_stack , CONFIG_INPUT_KBD_MATRIX_THREAD_STACK_SIZE )
```

<a id="afe0d57cf725c825097ba26b81bd2640c"></a>

### `poll_lock`

```c
struct k_sem input_kbd_matrix_common_data::poll_lock
```

<a id="ac54780c609eb2abc67e468470ac3ef83"></a>

### `scan_clk_cycle`

```c
uint32_t input_kbd_matrix_common_data::scan_clk_cycle[30U]
```

<a id="a53b66dca86734fa149b672583455bc61"></a>

### `scan_cycles_idx`

```c
uint8_t input_kbd_matrix_common_data::scan_cycles_idx
```

<a id="a526586907a6f0e4d1316c4304adda336"></a>

### `thread`

```c
struct k_thread input_kbd_matrix_common_data::thread
```

本数据类型文档由以下文件生成：

- `zephyr/input/input_kbd_matrix.h`

## 56.4\_原页交叉引用（Cross References）

- [zephyr/input/input_kbd_matrix.h](https://docs.zephyrproject.org/latest/doxygen/html/input__kbd__matrix_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_input_kbd_matrix_common_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_input_touchscreen_common_config_结构体.md)
