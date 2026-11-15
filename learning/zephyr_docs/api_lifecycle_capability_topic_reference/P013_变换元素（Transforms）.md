---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-13
title: 变换元素（Transforms）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_变换元素（Transforms）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

同时具有输入与输出、处于协商过程中间环节的元素。

<a id="details"></a>

具有输入和输出、位于协商过程（Negotiation）中间的元素。转换元素（Transform）有一个接收端衬垫（Sink Pad）和一个发送端衬垫（Source Pad）：缓冲区从一侧进入，另一侧输出内容。输出什么由元素决定，`mpipe_transform_mode` 定义三种形式：从输出池分配新缓冲区、原地改写输入缓冲区，或保持原样透传。

转换元素在两种协商中都需要特别处理，因为它是唯一必须协调两侧的基类。

**跨越能力（Crossing a Capability）**

`transform_caps` 将一侧的能力（Capability）映射为另一侧可能具备的能力。接受某种压缩格式的解码器可能输出多种原始格式，因此这是一对多关系。由于协商中不允许分配内存，这些备选能力通过索引提供，而不返回集合：每个索引对应一种转换，逐个遍历直到元素报告没有更多结果。

因此，回答能力查询（Capability Query）需要嵌套遍历：对本侧支持的每一种能力，再遍历其每一种转换，询问另一侧的对端（Peer）。首个被对端接受的组合胜出；对端答复会保存在远侧衬垫（Far Pad）上，因为后续事件传递需要据此重新收窄范围。

稍后格式事件（Format Event）到达时，转换元素以相同方式跨侧转换，并先转发事件，再应用到自身衬垫，因为 `set_caps` 钩子（Hook）可能重新连接处理图（Graph）。

**缓冲池（Buffer Pools）**

收到缓冲池查询时，转换元素先向下游转发，再作决定，因此总能在选择之前看到下游提议；然后用自己的提议回复上游。两侧各自的责任参见下文 `propose_buffer_pool` 和 `decide_buffer_pool`。

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_mpipe_5Ftransform_2Eh"></a>

```c
file mpipe_transform.h
```

相关声明：[mpipe_transform.h](../api_file_interface_reference/P035_zephyr__mpipe__mpipe_transform.h_文件参考.md)。

变换（Transform）：将输入缓冲区转换为输出缓冲区的元素。

<a id="r_mpipe_5Ftransform_5Fclient_2Eh"></a>

```c
file mpipe_transform_client.h
```

相关声明：[mpipe_transform_client.h](../api_file_supplement_reference/P074_zephyr__mpipe__mpipe_transform_client.h_文件参考.md)。

变换客户端（Transform Client）：工作在另一内核上运行的变换。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.2\_数据结构（Data Structures）

<a id="r_mpipe_5Ftransform"></a>

```c
struct mpipe_transform
```

相关声明：[mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)。

变换元素（Transform Element）的结构。

<a id="r_mpipe_5Ftransform_5Fclient"></a>

```c
struct mpipe_transform_client
```

相关声明：[mpipe_transform_client](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md)。

变换客户端元素（Transform Client Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.3\_枚举（Enumerations）

<a id="r_ga1710f61119b47e057d957b56ab690dfe"></a>

```c
enum mpipe_prop_transform { MPIPE_PROP_TRANSFORM_LAST }
```

相关声明：[mpipe_prop_transform](#ga1710f61119b47e057d957b56ab690dfe)、[MPIPE_PROP_TRANSFORM_LAST](#gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7)。

变换元素（transform element）的属性。

<a id="r_ga53de93e6bf6ca6cc2e4a7be14ff76652"></a>

```c
enum mpipe_transform_mode { MPIPE_TRANSFORM_MODE_PASSTHROUGH = 0 , MPIPE_TRANSFORM_MODE_INPLACE = 1 , MPIPE_TRANSFORM_MODE_NORMAL = 2 }
```

相关声明：[mpipe_transform_mode](#ga53de93e6bf6ca6cc2e4a7be14ff76652)、[MPIPE_TRANSFORM_MODE_PASSTHROUGH](#gga53de93e6bf6ca6cc2e4a7be14ff76652aca06f29cd96b7d8e8de6424f4a7d4d7b)、[MPIPE_TRANSFORM_MODE_INPLACE](#gga53de93e6bf6ca6cc2e4a7be14ff76652a0472bf057ab05107d7dfd38c996dedea)、[MPIPE_TRANSFORM_MODE_NORMAL](#gga53de93e6bf6ca6cc2e4a7be14ff76652a204d168b2efe7c3779194eab1ff2ee0c)。

变换元素的运行模式（operating modes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_gaecc6d5f2c8fb0d033977ecb1d5edeb5a"></a>

```c
int mpipe_transform_init (struct mpipe_transform *transform, uint8_t id)
```

相关声明：[mpipe_transform_init](#gaecc6d5f2c8fb0d033977ecb1d5edeb5a)、[mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化变换元素。

<a id="r_ga24c1be1b0231360f5f192d142975efd9"></a>

```c
int mpipe_transform_set_caps (struct mpipe_transform *transform, enum mpipe_pad_direction direction, const struct mpipe_structure *caps)
```

相关声明：[mpipe_transform_set_caps](#ga24c1be1b0231360f5f192d142975efd9)、[mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)、[mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

在变换元素的连接端（pad）上设置一项能力（capability）。

<a id="r_ga4a80bc07f3cab770a42bf73a510e1aad"></a>

```c
int mpipe_transform_change_state (struct mpipe_element *self, enum mpipe_state_change transition)
```

相关声明：[mpipe_transform_change_state](#ga4a80bc07f3cab770a42bf73a510e1aad)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

基础变换元素（base transform element）的状态变更函数。

<a id="r_ga2b1ea237f62a4cf9731a90e3b5d0eea4"></a>

```c
int mpipe_transform_client_init (struct mpipe_transform_client *transform_client, uint8_t id)
```

相关声明：[mpipe_transform_client_init](#ga2b1ea237f62a4cf9731a90e3b5d0eea4)、[mpipe_transform_client](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化变换客户端元素（Transform Client Element）。

## 13.5\_详细说明（Detailed Documentation）

<a id="ga1710f61119b47e057d957b56ab690dfe"></a>

### `mpipe_prop_transform`

```c
enum mpipe_prop_transform
```

```c
#include <zephyr/mpipe/mpipe_transform.h>
```

变换元素（transform element）的属性。

可为基础转换元素（Base Transform）配置的属性枚举（Properties Enumeration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PROP_TRANSFORM_LAST` | 最后一个转换属性标记（Last Transform Property Marker），用于验证／遍历。 |

<a id="ga53de93e6bf6ca6cc2e4a7be14ff76652"></a>

### `mpipe_transform_mode`

```c
enum mpipe_transform_mode
```

```c
#include <zephyr/mpipe/mpipe_transform.h>
```

变换元素的运行模式（operating modes）。

此模式指定输入和输出缓冲区（Input and Output Buffers）的处理方式。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_TRANSFORM_MODE_PASSTHROUGH` | 缓冲区保持完整不变（Intact）。 |
| `MPIPE_TRANSFORM_MODE_INPLACE` | 直接修改输入缓冲区；输入和输出使用同一缓冲区（Same Buffer）。 |
| `MPIPE_TRANSFORM_MODE_NORMAL` | 分配输出缓冲区（Output Buffer），它与输入缓冲区不同。 |

<a id="ga4a80bc07f3cab770a42bf73a510e1aad"></a>

### `mpipe_transform_change_state()`

```c
int mpipe_transform_change_state ( struct mpipe_element * self, enum mpipe_state_change transition )
```

```c
#include <zephyr/mpipe/mpipe_transform.h>
```

基础变换元素（base transform element）的状态变更函数。

在从 `PAUSED` 到 `READY` 的状态转换时，将协商后的衬垫能力（Negotiated Pad Caps）重置为 `ANY`，使后续重新协商从初始状态开始。覆盖 `change_state` 的派生转换元素必须链式调用本基类函数，才能继承此行为。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向元素（Elements）的指针。 |
| `transition` | 转换状态（transition state），参见 `mpipe_state_change`。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga2b1ea237f62a4cf9731a90e3b5d0eea4"></a>

### `mpipe_transform_client_init()`

```c
int mpipe_transform_client_init ( struct mpipe_transform_client * transform_client, uint8_t id )
```

```c
#include <zephyr/mpipe/mpipe_transform_client.h>
```

初始化变换客户端元素（Transform Client Element）。

初始化基础转换元素（Base Transform Element），并安装处理函数；该函数通过传输通道转发缓冲区，而不是在本地处理。

调用时必须已设置 `init_rpc`。它在基础元素初始化之前运行，因此传输通道无法启动时会通过返回值报告，且不会留下半初始化对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transform_client` | 指向要初始化的 `mpipe_transform_client` 的指针。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gaecc6d5f2c8fb0d033977ecb1d5edeb5a"></a>

### `mpipe_transform_init()`

```c
int mpipe_transform_init ( struct mpipe_transform * transform, uint8_t id )
```

```c
#include <zephyr/mpipe/mpipe_transform.h>
```

初始化变换元素。

本函数初始化基础转换元素结构体（Base Transform Element Structure），设置接收端和发送端衬垫（Sink and Source Pads），并为元素操作配置默认函数指针。具体转换元素应在自身初始化函数中首先以相同 `id` 调用本函数，再按需覆盖操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transform` | 指向要初始化的转换元素（Transforms）的指针。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga24c1be1b0231360f5f192d142975efd9"></a>

### `mpipe_transform_set_caps()`

```c
int mpipe_transform_set_caps ( struct mpipe_transform * transform, enum mpipe_pad_direction direction, const struct mpipe_structure * caps )
```

```c
#include <zephyr/mpipe/mpipe_transform.h>
```

在变换元素的连接端（pad）上设置一项能力（capability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transform` | 指向变换元素的指针。 |
| `direction` | 要设置能力的衬垫方向（Pad Direction），即 `mpipe_pad_direction`。 |
| `caps` | 指向要设置的能力（Capability）的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。


## 13.6\_原页交叉引用（Cross References）

- [mpipe_transform.h](../api_file_interface_reference/P035_zephyr__mpipe__mpipe_transform.h_文件参考.md)
- [mpipe_transform_client.h](../api_file_supplement_reference/P074_zephyr__mpipe__mpipe_transform_client.h_文件参考.md)
- [mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)
- [mpipe_transform_client](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [元素（Elements）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html)
- [变换元素（Transforms）](P013_变换元素（Transforms）.md)

<a id="header-details"></a>
<a id="mpipe_transform_caps"></a>
<a id="mpipe_transform_pool"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7"></a>
<a id="gga53de93e6bf6ca6cc2e4a7be14ff76652aca06f29cd96b7d8e8de6424f4a7d4d7b"></a>
<a id="gga53de93e6bf6ca6cc2e4a7be14ff76652a0472bf057ab05107d7dfd38c996dedea"></a>
<a id="gga53de93e6bf6ca6cc2e4a7be14ff76652a204d168b2efe7c3779194eab1ff2ee0c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_播放器（Player）.md) · [返回大纲](大纲.md) · [下一章](P014_NPCX API主题.md)
