---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-12
title: 应用源（Application sources）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_应用源（Application sources）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将应用数据注入管线的元素。

<a id="details"></a>

将应用数据注入管线（Pipeline）的元素（Element），是生产端的应用边界。有效载荷（Payload）可以通过 `mpipe_app_src_push` 复制传递，也可以原位传递：`mpipe_app_src_alloc` 从元素的缓冲池分配缓冲区供应用填充，`mpipe_app_src_push_buf` 再将其入队。管线至少进入 `PAUSED` 状态后再推送；在 `READY` 状态期间排队的所有数据，都会在管线启动时丢弃。可使用 `mpipe_app_src_eos` 声明流结束（EOS）；也可通过 `MPIPE_PROP_SRC_NUM_BUFS` 让流在产生指定数量的缓冲区后结束。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_mpipe_5Fapp_5Fsrc_2Eh"></a>

```c
file mpipe_app_src.h
```

相关声明：[mpipe_app_src.h](../api_file_system_device_reference/P028_zephyr__mpipe__base__mpipe_app_src.h_文件参考.md)。

应用源元素（Application Source Element）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fapp_5Fsrc"></a>

```c
struct mpipe_app_src
```

相关声明：[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)。

应用源元素（Application Source Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.3\_枚举（Enumerations）

<a id="r_gaee1930383745bc07d8734dfeac317f89"></a>

```c
enum { MPIPE_PROP_BASE_APP_SRC_CAPS = MPIPE_PROP_SRC_LAST }
```

相关声明：[MPIPE_PROP_BASE_APP_SRC_CAPS](#ggaee1930383745bc07d8734dfeac317f89ab1e24989a31b21a248e4ff49bb04bcef)。

应用源（application source）的属性标识符。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.4\_函数（Functions）

<a id="r_ga36d2f33b184a21b4bc81c3851da09231"></a>

```c
int mpipe_app_src_init (struct mpipe_app_src *app_src, uint8_t id)
```

相关声明：[mpipe_app_src_init](#ga36d2f33b184a21b4bc81c3851da09231)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化应用源元素。

<a id="r_ga38b11181f864200dc78a742e1627367a"></a>

```c
int mpipe_app_src_alloc (struct mpipe_app_src *app_src, uint32_t size, k_timeout_t timeout, struct net_buf **buf)
```

相关声明：[mpipe_app_src_alloc](#ga38b11181f864200dc78a742e1627367a)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从元素的缓冲池获取一个缓冲区，以便就地填充。

<a id="r_ga6b367eef2ce6e91ca66ceb9040a71d1f"></a>

```c
int mpipe_app_src_push_buf (struct mpipe_app_src *app_src, struct net_buf *buf, uint32_t size, k_timeout_t timeout)
```

相关声明：[mpipe_app_src_push_buf](#ga6b367eef2ce6e91ca66ceb9040a71d1f)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

将已填充的缓冲区加入管线队列。

<a id="r_ga3b30d456b8b1812f98a753012618906b"></a>

```c
int mpipe_app_src_push (struct mpipe_app_src *app_src, const void *data, uint32_t size, k_timeout_t timeout)
```

相关声明：[mpipe_app_src_push](#ga3b30d456b8b1812f98a753012618906b)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

通过复制方式向管线推送一份有效载荷（payload）。

<a id="r_ga7e0d167ba0017e1952b455c9e269ca37"></a>

```c
int mpipe_app_src_eos (struct mpipe_app_src *app_src, k_timeout_t timeout)
```

相关声明：[mpipe_app_src_eos](#ga7e0d167ba0017e1952b455c9e269ca37)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

声明流结束（end of stream）。

## 12.5\_详细说明（Detailed Documentation）

<a id="gaee1930383745bc07d8734dfeac317f89"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/mpipe/base/mpipe_app_src.h>
```

应用源（application source）的属性标识符。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PROP_BASE_APP_SRC_CAPS` | 输出流的能力（Capability），以 `const struct mpipe_structure` 指针传入，内容会被复制。这是协商（Negotiation）时向下游提供的能力；应用推送的数据必须与其匹配，元素自身无法检查。在设置之前，元素提供的能力不施加任何约束。 |

<a id="ga38b11181f864200dc78a742e1627367a"></a>

### `mpipe_app_src_alloc()`

```c
int mpipe_app_src_alloc ( struct mpipe_app_src * app_src, uint32_t size, k_timeout_t timeout, struct net_buf ** buf )
```

```c
#include <zephyr/mpipe/base/mpipe_app_src.h>
```

从元素的缓冲池获取一个缓冲区，以便就地填充。

缓冲区最多容纳 `CONFIG_MPIPE_BASE_APP_SRC_BUF_SZ` 字节。应用将有效载荷（Payload）写入缓冲区数据区，再将缓冲区交给 `mpipe_app_src_push_buf`；若改变主意，则通过 `net_buf_unref()` 释放它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_src` | 应用数据源（Application Source）。 |
| `size` | 缓冲区必须容纳的有效载荷字节数（Payload Bytes）。 |
| `timeout` | 等待空闲缓冲区（Free Buffer）的时长。 |
| `buf` | 用于填入所获得的缓冲区（Buffer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `size` 为 0，或超过缓冲区大小。 |
| `-ENOBUFS` | 在超时（Timeout）期限内，没有缓冲区变为空闲。 |

<a id="ga7e0d167ba0017e1952b455c9e269ca37"></a>

### `mpipe_app_src_eos()`

```c
int mpipe_app_src_eos ( struct mpipe_app_src * app_src, k_timeout_t timeout )
```

```c
#include <zephyr/mpipe/base/mpipe_app_src.h>
```

声明流结束（end of stream）。

此次调用之前推送的缓冲区仍会被交付；随后管线会收到流结束（EOS）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_src` | 应用数据源（Application Source）。 |
| `timeout` | 等待队列空位（Queue Slot）的时长。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EAGAIN` | 在超时（Timeout）期限内，队列一直处于满状态。 |

<a id="ga36d2f33b184a21b4bc81c3851da09231"></a>

### `mpipe_app_src_init()`

```c
int mpipe_app_src_init ( struct mpipe_app_src * app_src, uint8_t id )
```

```c
#include <zephyr/mpipe/base/mpipe_app_src.h>
```

初始化应用源元素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_src` | 指向待初始化元素（Element）的指针（Pointer）。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga3b30d456b8b1812f98a753012618906b"></a>

### `mpipe_app_src_push()`

```c
int mpipe_app_src_push ( struct mpipe_app_src * app_src, const void * data, uint32_t size, k_timeout_t timeout )
```

```c
#include <zephyr/mpipe/base/mpipe_app_src.h>
```

通过复制方式向管线推送一份有效载荷（payload）。

获取一个缓冲区，将 `size` 字节复制进去并入队：两次等待各自最多可持续 `timeout` 时长。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_src` | 应用数据源（Application Source）。 |
| `data` | 有效载荷字节（Payload Bytes）。 |
| `size` | 字节数，上限为 `CONFIG_MPIPE_BASE_APP_SRC_BUF_SZ`。 |
| `timeout` | 等待空闲缓冲区，以及等待队列空位（Queue Slot）的时长。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `size` 为 0，或超过缓冲区大小。 |
| `-ENOBUFS` | 在超时（Timeout）期限内，没有缓冲区变为空闲。 |
| `-EAGAIN` | 在超时（Timeout）期限内，队列一直处于满状态。 |

<a id="ga6b367eef2ce6e91ca66ceb9040a71d1f"></a>

### `mpipe_app_src_push_buf()`

```c
int mpipe_app_src_push_buf ( struct mpipe_app_src * app_src, struct net_buf * buf, uint32_t size, k_timeout_t timeout )
```

```c
#include <zephyr/mpipe/base/mpipe_app_src.h>
```

将已填充的缓冲区加入管线队列。

缓冲区来自 `mpipe_app_src_alloc`。成功时，管线取得其所有权（Ownership）；失败时，所有权仍属于调用方，可重试或释放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_src` | 应用数据源（Application Source）。 |
| `buf` | 要入队的缓冲区（Buffer）。 |
| `size` | 缓冲区中有效的载荷字节数（Payload Bytes）。 |
| `timeout` | 等待队列空位（Queue Slot）的时长。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `size` 为 0，或超过缓冲区所容纳的大小。 |
| `-EAGAIN` | 在超时（Timeout）期限内，队列一直处于满状态。 |


## 12.6\_原页交叉引用（Cross References）

- [mpipe_app_src.h](../api_file_system_device_reference/P028_zephyr__mpipe__base__mpipe_app_src.h_文件参考.md)
- [mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [CONFIG_MPIPE_BASE_APP_SRC_BUF_SZ](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_BASE_APP_SRC_BUF_SZ)
- [net_buf_unref()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaee1930383745bc07d8734dfeac317f89ab1e24989a31b21a248e4ff49bb04bcef"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_按需分页 API（Demand Paging APIs）.md) · [返回大纲](大纲.md) · [下一章](P013_MSPI 配置 API（MSPI Configure API）.md)
