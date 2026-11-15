---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-9
title: 源（Sources）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_源（Sources）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

产生缓冲区并驱动协商过程的元素。

<a id="details"></a>

产生缓冲区并驱动协商的元素（Elements）。源（Source）只有一个源焊盘（Source Pad），没有接收焊盘（Sink Pad）；数据从这里进入处理图（Graph），可来自设备、文件，也可由源自行产生。源拥有其推送缓冲区所属的缓冲池（Buffer Pool）。

源还承担其他基类没有的职责：它位于图的起点，因此在从 READY 转为 PAUSED 时驱动协商（Negotiation）。它逐一向下游提出自己支持的能力（Capabilities），保留整条链都接受的第一个能力，将其确定为单一格式，并通过事件宣布；然后执行缓冲池查询，配置并启动自己的池。派生源提供各部分信息——支持的内容、选定格式后的动作、所需缓冲区——由基类执行遍历。

`num_buffers` 属性限定在源宣布流结束（End of Stream）前产生的缓冲区数量；0 表示持续运行直到被停止。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_mpipe_5Ffake_5Fsrc_2Eh"></a>

```c
file mpipe_fake_src.h
```

相关声明：[mpipe_fake_src.h](../api_file_configuration_reference/P056_zephyr__mpipe__mpipe_fake_src.h_文件参考.md)。

模拟源元素（Fake Source Element）。

<a id="r_mpipe_5Fsrc_2Eh"></a>

```c
file mpipe_src.h
```

相关声明：[mpipe_src.h](../api_file_interface_reference/P033_zephyr__mpipe__mpipe_src.h_文件参考.md)。

源（Source）：产生缓冲区的元素。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.2\_数据结构（Data Structures）

<a id="r_mpipe_5Ffake_5Fsrc"></a>

```c
struct mpipe_fake_src
```

相关声明：[mpipe_fake_src](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md)。

模拟源元素（Fake Source Element）的结构。

<a id="r_mpipe_5Fsrc"></a>

```c
struct mpipe_src
```

相关声明：[mpipe_src](../audio_video_model_reference/P030_mpipe_src_结构体.md)。

基础源元素（Base Source Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.3\_枚举（Enumerations）

<a id="r_gae7fdcd5a2bfe2bfb28fa5f430349355e"></a>

```c
enum mpipe_prop_src { MPIPE_PROP_SRC_NUM_BUFS , MPIPE_PROP_SRC_LAST }
```

相关声明：[mpipe_prop_src](#gae7fdcd5a2bfe2bfb28fa5f430349355e)、[MPIPE_PROP_SRC_NUM_BUFS](#ggae7fdcd5a2bfe2bfb28fa5f430349355ea23225c0f2e18cb85fb0f054b5da50d0b)、[MPIPE_PROP_SRC_LAST](#ggae7fdcd5a2bfe2bfb28fa5f430349355ea7607aa8978e84a6b6e89fb9a8bf59e8e)。

基础源元素（base source element）的属性。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.4\_函数（Functions）

<a id="r_ga1eed36753b4c3d29b2e8c94e74ee832c"></a>

```c
int mpipe_fake_src_init (struct mpipe_fake_src *fsrc, uint8_t id)
```

相关声明：[mpipe_fake_src_init](#ga1eed36753b4c3d29b2e8c94e74ee832c)、[mpipe_fake_src](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化伪源元素（Fake Source Element）。

<a id="r_gab96ba2e8ce9cbe6bf2bb27587710bbf0"></a>

```c
int mpipe_src_init (struct mpipe_src *src, uint8_t id)
```

相关声明：[mpipe_src_init](#gab96ba2e8ce9cbe6bf2bb27587710bbf0)、[mpipe_src](../audio_video_model_reference/P030_mpipe_src_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化源元素（source element）。

<a id="r_ga53dfd90c1a3942949337f1d222317700"></a>

```c
int mpipe_src_change_state (struct mpipe_element *self, enum mpipe_state_change transition)
```

相关声明：[mpipe_src_change_state](#ga53dfd90c1a3942949337f1d222317700)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

基础源元素的状态变更函数（change state function）。

<a id="r_ga867c427e847edb78082607cbe9d5a87b"></a>

```c
int mpipe_src_set_property (struct mpipe_object *obj, uint32_t key, const void *val)
```

相关声明：[mpipe_src_set_property](#ga867c427e847edb78082607cbe9d5a87b)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置源元素的属性。

<a id="r_ga31c1f53bbb8ee29228766cf33f49f924"></a>

```c
int mpipe_src_get_property (struct mpipe_object *obj, uint32_t key, void *val)
```

相关声明：[mpipe_src_get_property](#ga31c1f53bbb8ee29228766cf33f49f924)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取源元素的属性。

## 9.5\_详细说明（Detailed Documentation）

<a id="gae7fdcd5a2bfe2bfb28fa5f430349355e"></a>

### `mpipe_prop_src`

```c
enum mpipe_prop_src
```

```c
#include <zephyr/mpipe/mpipe_src.h>
```

基础源元素（base source element）的属性。

基础源（Base Source）可配置属性的枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PROP_SRC_NUM_BUFS` | 源发送流结束（EOS）前输出的缓冲区数量。 |
| `MPIPE_PROP_SRC_LAST` | 最后一个源属性标记（Last Source Property Marker），用于校验／遍历。 |

<a id="ga1eed36753b4c3d29b2e8c94e74ee832c"></a>

### `mpipe_fake_src_init()`

```c
int mpipe_fake_src_init ( struct mpipe_fake_src * fsrc, uint8_t id )
```

```c
#include <zephyr/mpipe/mpipe_fake_src.h>
```

初始化伪源元素（Fake Source Element）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fsrc` | 指向待初始化的 `mpipe_fake_src` 的指针。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga53dfd90c1a3942949337f1d222317700"></a>

### `mpipe_src_change_state()`

```c
int mpipe_src_change_state ( struct mpipe_element * self, enum mpipe_state_change transition )
```

```c
#include <zephyr/mpipe/mpipe_src.h>
```

基础源元素的状态变更函数（change state function）。

从 PAUSED 转为 READY 时，将已协商的焊盘能力（Pad Caps）重置为 ANY，使下一次重新协商从全新状态开始。覆盖 `change_state` 的派生源必须继续调用此基类函数，才能继承该行为。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向 Elements 结构体的指针。 |
| `transition` | 转换状态（transition state），参见 `mpipe_state_change`。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga31c1f53bbb8ee29228766cf33f49f924"></a>

### `mpipe_src_get_property()`

```c
int mpipe_src_get_property ( struct mpipe_object * obj, uint32_t key, void * val )
```

```c
#include <zephyr/mpipe/mpipe_src.h>
```

获取源元素的属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` obj` | 指向 Objects 的指针，即源元素（Source Element）。 |
| ` key` | 属性键标识符（Property Key Identifier）。 |
| `[out] val` | 用于保存所取得属性值的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gab96ba2e8ce9cbe6bf2bb27587710bbf0"></a>

### `mpipe_src_init()`

```c
int mpipe_src_init ( struct mpipe_src * src, uint8_t id )
```

```c
#include <zephyr/mpipe/mpipe_src.h>
```

初始化源元素（source element）。

初始化基础源元素结构体（Base Source Element），包括源焊盘（Source Pad）和默认回调。具体源在自身初始化中首先以相同的标识（ID）调用本函数，然后按需覆盖相关内容。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 指向待初始化的 Sources 的指针。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga867c427e847edb78082607cbe9d5a87b"></a>

### `mpipe_src_set_property()`

```c
int mpipe_src_set_property ( struct mpipe_object * obj, uint32_t key, const void * val )
```

```c
#include <zephyr/mpipe/mpipe_src.h>
```

设置源元素的属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj` | 指向 Objects 的指针，即源元素（Source Element）。 |
| `key` | 属性键标识符（Property Key Identifier）。 |
| `val` | 指向待设置属性值的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。


## 9.6\_原页交叉引用（Cross References）

- [mpipe_fake_src.h](../api_file_configuration_reference/P056_zephyr__mpipe__mpipe_fake_src.h_文件参考.md)
- [mpipe_src.h](../api_file_interface_reference/P033_zephyr__mpipe__mpipe_src.h_文件参考.md)
- [mpipe_fake_src](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md)
- [mpipe_src](../audio_video_model_reference/P030_mpipe_src_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [元素（Elements）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html)
- [对象（Objects）](P008_对象（Objects）.md)
- [源（Sources）](P009_源（Sources）.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae7fdcd5a2bfe2bfb28fa5f430349355ea23225c0f2e18cb85fb0f054b5da50d0b"></a>
<a id="ggae7fdcd5a2bfe2bfb28fa5f430349355ea7607aa8978e84a6b6e89fb9a8bf59e8e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_对象（Objects）.md) · [返回大纲](大纲.md) · [下一章](P010_PAJ7620 API主题.md)
