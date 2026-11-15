---
id: learning.zephyr-docs.api-video-event-topic-reference.page-8
title: 视频缓冲区（Video Buffers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_视频缓冲区（Video Buffers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于分配和交换视频缓冲区的函数。

<a id="details"></a>

用于分配和交换视频缓冲区的函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.1\_函数（Functions）

<a id="r_ga036c42c1e7dbaa97eb2789dfc3a3c1d7"></a>

```c
int video_enqueue (const struct device *dev, struct video_buffer *buf)
```

相关声明：[video_enqueue](#ga036c42c1e7dbaa97eb2789dfc3a3c1d7)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)。

将视频缓冲区（Video Buffer）交给视频设备。

<a id="r_gaba208d8f4747952acbec5b84f474e31b"></a>

```c
int video_dequeue (const struct device *dev, struct video_buffer **vbuf, k_timeout_t timeout)
```

相关声明：[video_dequeue](#gaba208d8f4747952acbec5b84f474e31b)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从视频设备获取视频缓冲区（Video Buffer）。

<a id="r_ga195914c7f03f2241702c77d41d1ab750"></a>

```c
struct video_buffer * video_buffer_aligned_alloc (size_t size, size_t align, k_timeout_t timeout)
```

相关声明：[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[video_buffer_aligned_alloc](#ga195914c7f03f2241702c77d41d1ab750)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

分配对齐的视频缓冲区（Aligned Video Buffer）。

<a id="r_gaee6eb26310a40d3f18161b3567f9e0a9"></a>

```c
struct video_buffer * video_buffer_alloc (size_t size, k_timeout_t timeout)
```

相关声明：[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[video_buffer_alloc](#gaee6eb26310a40d3f18161b3567f9e0a9)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

分配视频缓冲区（Video Buffer）。

<a id="r_gaa65b69cdc4271a07ad26c4850ff96e45"></a>

```c
struct video_buffer * video_import_buffer (uint8_t *mem, size_t sz)
```

相关声明：[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[video_import_buffer](#gaa65b69cdc4271a07ad26c4850ff96e45)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将外部内存（External Memory）导入视频缓冲池（Video Buffer Pool）。

<a id="r_gaae3a7eee506e77dd130fae74107f6533"></a>

```c
int video_buffer_release (struct video_buffer *buf)
```

相关声明：[video_buffer_release](#gaae3a7eee506e77dd130fae74107f6533)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)。

释放视频缓冲区（Video Buffer）。

<a id="r_ga4d3c1458b8c30cff9ac5e6a62d6391c9"></a>

```c
int video_transfer_buffer (const struct device *src, const struct device *sink, enum video_buf_type src_type, enum video_buf_type sink_type, k_timeout_t timeout)
```

相关声明：[video_transfer_buffer](#ga4d3c1458b8c30cff9ac5e6a62d6391c9)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

在两个视频设备之间转移缓冲区（Transfer a Buffer）。

<a id="r_ga8ec3f0b83ba64947570dfe06ad5e2cbd"></a>

```c
int video_set_signal (const struct device *dev, struct k_poll_signal *sig)
```

相关声明：[video_set_signal](#ga8ec3f0b83ba64947570dfe06ad5e2cbd)、[device](../device_reference/P002_设备对象结构.md)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

为视频端点（Video Endpoint）注册／注销 `k_poll` 信号。

## 8.2\_详细说明（Detailed Documentation）

<a id="ga195914c7f03f2241702c77d41d1ab750"></a>

### `video_buffer_aligned_alloc()`

```c
struct video_buffer * video_buffer_aligned_alloc ( size_t size, size_t align, k_timeout_t timeout )
```

```c
#include <zephyr/video/video.h>
```

分配对齐的视频缓冲区（Aligned Video Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `size` | 视频缓冲区大小（Video Buffer Size），单位为字节。 |
| `align` | 请求内存的对齐（Alignment），必须为 2 的幂。 |
| `timeout` | 超时时长（Timeout Duration）或 `K_NO_WAIT`。 |

**返回（Returns）**：返回值：指向已分配视频缓冲区（Video Buffer）的指针。

<a id="gaee6eb26310a40d3f18161b3567f9e0a9"></a>

### `video_buffer_alloc()`

```c
struct video_buffer * video_buffer_alloc ( size_t size, k_timeout_t timeout )
```

```c
#include <zephyr/video/video.h>
```

分配视频缓冲区（Video Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `size` | 视频缓冲区大小（Video Buffer Size），单位为字节。 |
| `timeout` | 超时时长（Timeout Duration）或 `K_NO_WAIT`。 |

**返回（Returns）**：返回值：指向已分配视频缓冲区（Video Buffer）的指针。

<a id="gaae3a7eee506e77dd130fae74107f6533"></a>

### `video_buffer_release()`

```c
int video_buffer_release ( struct video_buffer * buf)
```

```c
#include <zephyr/video/video.h>
```

释放视频缓冲区（Video Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向要释放的视频缓冲区（Video Buffer）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时，或失败时返回负 errno 值。 |

<a id="gaba208d8f4747952acbec5b84f474e31b"></a>

### `video_dequeue()`

```c
int video_dequeue ( const struct device * dev, struct video_buffer ** vbuf, k_timeout_t timeout )
```

```c
#include <zephyr/video/video.h>
```

从视频设备获取视频缓冲区（Video Buffer）。

从驱动端点的出站队列（Outgoing Queue）取出空的视频缓冲区（输出模式）或已填充的视频缓冲区（采集模式）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `vbuf` | 视频设备返回的缓冲区（Buffer）。 |
| `timeout` | 超时时长（Timeout Duration）或 `K_NO_WAIT`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时（Successful）。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga036c42c1e7dbaa97eb2789dfc3a3c1d7"></a>

### `video_enqueue()`

```c
int video_enqueue ( const struct device * dev, struct video_buffer * buf )
```

```c
#include <zephyr/video/video.h>
```

将视频缓冲区（Video Buffer）交给视频设备。

向驱动端点的入站队列（Incoming Queue）加入空的视频缓冲区（采集模式）或已填充的视频缓冲区（输出模式）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `buf` | 指向视频缓冲区（Video Buffer）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时（Successful）。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="gaa65b69cdc4271a07ad26c4850ff96e45"></a>

### `video_import_buffer()`

```c
struct video_buffer * video_import_buffer ( uint8_t * mem, size_t sz )
```

```c
#include <zephyr/video/video.h>
```

将外部内存（External Memory）导入视频缓冲池（Video Buffer Pool）。

将外部分配的内存作为 `video_buffer` 导入视频缓冲池（Video Buffer Pool）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mem` | 指向外部内存（External Memory）的指针。 |
| `sz` | 外部内存大小（External Memory Size）。 |

**返回（Returns）**：返回值：成功返回持有所述外部内存的已导入 `video_buffer` 指针；失败返回 `NULL`。

<a id="ga8ec3f0b83ba64947570dfe06ad5e2cbd"></a>

### `video_set_signal()`

```c
int video_set_signal ( const struct device * dev, struct k_poll_signal * sig )
```

```c
#include <zephyr/video/video.h>
```

为视频端点（Video Endpoint）注册／注销 `k_poll` 信号。

为端点注册轮询信号（Poll Signal），帧完成时会触发信号，包括正常完成、中止及错误。注册 `NULL` 轮询信号会注销先前注册的任何信号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `sig` | 指向 `k_poll_signal` 的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；否则返回 `-ERRNO` 错误码。 |

<a id="ga4d3c1458b8c30cff9ac5e6a62d6391c9"></a>

### `video_transfer_buffer()`

```c
int video_transfer_buffer ( const struct device * src, const struct device * sink, enum video_buf_type src_type, enum video_buf_type sink_type, k_timeout_t timeout )
```

```c
#include <zephyr/video/video.h>
```

在两个视频设备之间转移缓冲区（Transfer a Buffer）。

辅助函数，从源设备（Source Device）取出缓冲区，再将其加入接收设备（Sink Device）的队列，并在两者之间转换缓冲区类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 从中取出缓冲区的视频设备，即源设备（Source）。 |
| `sink` | 要将缓冲区加入其队列的视频设备，即接收设备（Sink）。 |
| `src_type` | 源设备上的视频缓冲区类型（Video Buffer Type）。 |
| `sink_type` | 接收设备上的视频缓冲区类型（Video Buffer Type）。 |
| `timeout` | 取出缓冲区时使用的超时（Dequeue Timeout）。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负 errno 错误码。


## 8.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [zephyr/video/video.h](../api_file_host_video_reference/P012_zephyr__video__video.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_消息（Messages）.md) · [返回大纲](大纲.md) · [下一章](P009_视频格式（Video Format）.md)
