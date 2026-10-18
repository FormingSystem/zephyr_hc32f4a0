---
id: learning.zephyr-docs.audio-video-model-reference.page-21
title: mpipe_element_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__element.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_mpipe\_element\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__element.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

元素基类（Element Base Class）。

```c
#include <zephyr/mpipe/mpipe_element.h>
```

<a id="details"></a>

元素基类（Element base class），是所有元素的基类。元素是多媒体管线（multimedia pipeline）的基本构件，可以具有源连接点（source pad，输出）和接收连接点（sink pad，输入），并可相互连接形成处理链。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_a2a414eb61a9d44a07ea38fecc7db8f07"></a>

```c
struct mpipe_object object
```

相关声明：[mpipe_object](P024_mpipe_object_结构体.md)、[object](#a2a414eb61a9d44a07ea38fecc7db8f07)。

基础对象（base object）。

<a id="r_a4330512249b2c98893cdb59333794d3b"></a>

```c
const char * name
```

相关声明：[name](#a4330512249b2c98893cdb59333794d3b)。

元素名称；元素的初始化函数将其设置为类型名称，可通过 `mpipe_element_set_name` 为单个实例覆盖此名称。

<a id="r_adbdc3105f51b539961e2120ae13e0635"></a>

```c
sys_dlist_t src_pads
```

相关声明：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)、[src_pads](#adbdc3105f51b539961e2120ae13e0635)。

源连接点（source pads）列表。

<a id="r_a7f9ce9f14e2a46228ca02f0866904cf2"></a>

```c
sys_dlist_t sink_pads
```

相关声明：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)、[sink_pads](#a7f9ce9f14e2a46228ca02f0866904cf2)。

接收连接点（sink pads）列表。

<a id="r_a9c819d9a520a157f4211e2e80468808a"></a>

```c
enum mpipe_state current_state
```

相关声明：[mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)、[current_state](#a9c819d9a520a157f4211e2e80468808a)。

元素的当前状态。

<a id="r_a08f3bb36f9d4e3c397a91bb7a97317a8"></a>

```c
int(* set_state )(struct mpipe_element *element, enum mpipe_state state)
```

相关声明：[set_state](#a08f3bb36f9d4e3c397a91bb7a97317a8)、[mpipe_element](P021_mpipe_element_结构体.md)、[mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

设置状态（set state）函数；成功时返回 0，否则返回负值 `errno`。

<a id="r_aae5c0e9104f4c480e0bfafbec6619f3b"></a>

```c
int(* change_state )(struct mpipe_element *element, enum mpipe_state_change transition)
```

相关声明：[change_state](#aae5c0e9104f4c480e0bfafbec6619f3b)、[mpipe_element](P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

切换状态（change state）函数；成功时返回 0，否则返回负值 `errno`。

## 21.2\_详细说明（Detailed Documentation）

<a id="aae5c0e9104f4c480e0bfafbec6619f3b"></a>

### `change_state`

```c
int(* mpipe_element::change_state) (struct mpipe_element *element, enum mpipe_state_change transition)
```

切换状态（change state）函数；成功时返回 0，否则返回负值 `errno`。

<a id="a9c819d9a520a157f4211e2e80468808a"></a>

### `current_state`

```c
enum mpipe_state mpipe_element::current_state
```

元素的当前状态。

<a id="a4330512249b2c98893cdb59333794d3b"></a>

### `name`

```c
const char* mpipe_element::name
```

元素名称；元素的初始化函数将其设置为类型名称，可通过 `mpipe_element_set_name` 为单个实例覆盖此名称。

仅用于调试。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MPIPE_ELEMENT_NAME`。

<a id="a2a414eb61a9d44a07ea38fecc7db8f07"></a>

### `object`

```c
struct mpipe_object mpipe_element::object
```

基础对象（base object）。

<a id="a08f3bb36f9d4e3c397a91bb7a97317a8"></a>

### `set_state`

```c
int(* mpipe_element::set_state) (struct mpipe_element *element, enum mpipe_state state)
```

设置状态（set state）函数；成功时返回 0，否则返回负值 `errno`。

<a id="a7f9ce9f14e2a46228ca02f0866904cf2"></a>

### `sink_pads`

```c
sys_dlist_t mpipe_element::sink_pads
```

接收连接点（sink pads）列表。

<a id="adbdc3105f51b539961e2120ae13e0635"></a>

### `src_pads`

```c
sys_dlist_t mpipe_element::src_pads
```

源连接点（source pads）列表。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_element.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h_source.html)
- [mpipe_object](P024_mpipe_object_结构体.md)
- [mpipe_element_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga89e9dc38e2cff13b63e70177732773e9)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)
- [mpipe_element](P021_mpipe_element_结构体.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [CONFIG_MPIPE_ELEMENT_NAME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_ELEMENT_NAME)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_mpipe_dispatch_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_mpipe_fake_src_结构体.md)
