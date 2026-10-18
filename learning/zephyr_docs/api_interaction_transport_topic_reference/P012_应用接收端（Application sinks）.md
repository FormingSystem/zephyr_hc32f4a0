---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-12
title: 应用接收端（Application sinks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_应用接收端（Application sinks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将管线缓冲区交给应用程序的元素。

<a id="details"></a>

将流水线缓冲区交给应用程序的元素（Element），构成消费侧的应用边界。到达接收端（Sink）的每个缓冲区都按片段交付一次：若注册了回调，就交给回调；否则进入队列，由应用程序通过 `mpipe_app_sink_pull` 取走。与其他接收端一样，流结束（End of Stream）通过流水线总线（Pipeline Bus）报告。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_mpipe_5Fapp_5Fsink_2Eh"></a>

```c
file mpipe_app_sink.h
```

相关声明：[mpipe_app_sink.h](../api_file_interface_reference/P032_zephyr__mpipe__base__mpipe_app_sink.h_文件参考.md)。

应用接收端元素（Application Sink Element）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fapp_5Fsink_5Fcb"></a>

```c
struct mpipe_app_sink_cb
```

相关声明：[mpipe_app_sink_cb](../audio_video_model_reference/P013_mpipe_app_sink_cb_结构体.md)。

MPIPE_PROP_BASE_APP_SINK_CB的回调注册。

<a id="r_mpipe_5Fapp_5Fsink"></a>

```c
struct mpipe_app_sink
```

相关声明：[mpipe_app_sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md)。

应用接收端元素（Application Sink Element）的结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.3\_类型定义（Typedefs）

<a id="r_ga8bd213256bc8867364864eff4e9b0d55"></a>

```c
typedef void(* mpipe_app_sink_cb_t) (const struct net_buf *buf, void *user_data)
```

相关声明：[mpipe_app_sink_cb_t](#ga8bd213256bc8867364864eff4e9b0d55)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

缓冲区回调（buffer callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.4\_枚举（Enumerations）

<a id="r_gab996263656e57f425230376ecdd838de"></a>

```c
enum { MPIPE_PROP_BASE_APP_SINK_CAPS = MPIPE_PROP_SINK_LAST , MPIPE_PROP_BASE_APP_SINK_CB }
```

相关声明：[MPIPE_PROP_BASE_APP_SINK_CAPS](#ggab996263656e57f425230376ecdd838deac9e61be01787df7e978c00c91e68583b)、[MPIPE_PROP_BASE_APP_SINK_CB](#ggab996263656e57f425230376ecdd838dea2dd7456ad7e1306258b259634c4d66a7)。

应用接收端（application sink）的属性标识符。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.5\_函数（Functions）

<a id="r_ga6ab7e49f03e81d49a32988f996760af1"></a>

```c
int mpipe_app_sink_init (struct mpipe_app_sink *app_sink, uint8_t id)
```

相关声明：[mpipe_app_sink_init](#ga6ab7e49f03e81d49a32988f996760af1)、[mpipe_app_sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化应用接收端元素。

<a id="r_ga2f62c9d0d779686aeb62ee6a393ed36b"></a>

```c
int mpipe_app_sink_pull (struct mpipe_app_sink *app_sink, struct net_buf **buf, k_timeout_t timeout)
```

相关声明：[mpipe_app_sink_pull](#ga2f62c9d0d779686aeb62ee6a393ed36b)、[mpipe_app_sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

拉取下一个缓冲区。

## 12.6\_详细说明（Detailed Documentation）

<a id="ga8bd213256bc8867364864eff4e9b0d55"></a>

### `mpipe_app_sink_cb_t`

```c
typedef void(* mpipe_app_sink_cb_t) (const struct net_buf *buf, void *user_data)
```

```c
#include <zephyr/mpipe/base/mpipe_app_sink.h>
```

缓冲区回调（buffer callback）。

在驱动接收端的线程中运行，应保持简短，并复制所需内容。缓冲区属于该元素，回调返回时即被释放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 到达接收端（Sink）的缓冲区。 |
| `user_data` | 注册回调时提供的指针。 |

<a id="gab996263656e57f425230376ecdd838de"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/mpipe/base/mpipe_app_sink.h>
```

应用接收端（application sink）的属性标识符。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PROP_BASE_APP_SINK_CAPS` | 接收端接受的能力（Capability），以 `const struct mpipe_structure` 指针传入并复制；设置之前接受任何内容。 |
| `MPIPE_PROP_BASE_APP_SINK_CB` | 缓冲区回调（Buffer Callback），以 `const struct mpipe_app_sink_cb` 指针传入并复制；设置后缓冲区不再排队供主动拉取（Pull）。 |

<a id="ga6ab7e49f03e81d49a32988f996760af1"></a>

### `mpipe_app_sink_init()`

```c
int mpipe_app_sink_init ( struct mpipe_app_sink * app_sink, uint8_t id )
```

```c
#include <zephyr/mpipe/base/mpipe_app_sink.h>
```

初始化应用接收端元素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_sink` | 指向待初始化元素（Element）的指针（Pointer）。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga2f62c9d0d779686aeb62ee6a393ed36b"></a>

### `mpipe_app_sink_pull()`

```c
int mpipe_app_sink_pull ( struct mpipe_app_sink * app_sink, struct net_buf ** buf, k_timeout_t timeout )
```

```c
#include <zephyr/mpipe/base/mpipe_app_sink.h>
```

拉取下一个缓冲区。

仅在未设置回调时有意义。调用者拥有返回缓冲区，必须通过 `net_buf_unref()` 释放。队列已满时到达的缓冲区会被丢弃，因此拉取过慢会丢失数据，而不会使流水线停顿（Stall）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_sink` | 应用接收端（Application Sink）。 |
| `buf` | 填入拉取得到的缓冲区。 |
| `timeout` | 等待缓冲区的时长。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EAGAIN` | 超时时限内没有缓冲区到达。 |


## 12.7\_原页交叉引用（Cross References）

- [mpipe_app_sink.h](../api_file_interface_reference/P032_zephyr__mpipe__base__mpipe_app_sink.h_文件参考.md)
- [mpipe_app_sink_cb](../audio_video_model_reference/P013_mpipe_app_sink_cb_结构体.md)
- [mpipe_app_sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [net_buf_unref()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab996263656e57f425230376ecdd838deac9e61be01787df7e978c00c91e68583b"></a>
<a id="ggab996263656e57f425230376ecdd838dea2dd7456ad7e1306258b259634c4d66a7"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_调制解调器串口复用（Modem CMUX）.md) · [返回大纲](大纲.md) · [下一章](P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md)
