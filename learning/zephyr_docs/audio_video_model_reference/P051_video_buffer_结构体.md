---
id: learning.zephyr-docs.audio-video-model-reference.page-51
title: video_buffer_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__buffer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_video\_buffer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__buffer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频缓冲区（Video Buffer）结构。

```c
#include <zephyr/video/types.h>
```

<a id="details"></a>

视频缓冲区（Video buffer）结构体，表示一个视频帧。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_ab184d528487042650af105eb7d37381e"></a>

```c
void * driver_data
```

相关声明：[driver_data](#ab184d528487042650af105eb7d37381e)。

指向驱动专用数据的指针。

<a id="r_a46dd9bd9398ff74e4f9859a07b9c48af"></a>

```c
enum video_buf_type type
```

相关声明：[video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)、[type](#a46dd9bd9398ff74e4f9859a07b9c48af)。

缓冲区类型。

<a id="r_a687f782126d32b36b3b07aaa976a83a4"></a>

```c
uint8_t memory
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[memory](#a687f782126d32b36b3b07aaa976a83a4)。

缓冲区内存类型，参见 `video_buf_memory`。

<a id="r_a6a62d7a50c717dc6bc85e2d8f6ae95e3"></a>

```c
uint8_t * buffer
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buffer](#a6a62d7a50c717dc6bc85e2d8f6ae95e3)。

指向缓冲区起始位置的指针。

<a id="r_a84550afc674ad543c8c709d55ececda2"></a>

```c
uint16_t index
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[index](#a84550afc674ad543c8c709d55ececda2)。

缓冲区在视频缓冲池中的索引。

<a id="r_a3f040775c683c91740c8bda5c96e621b"></a>

```c
uint32_t size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[size](#a3f040775c683c91740c8bda5c96e621b)。

缓冲区大小，单位为字节。

<a id="r_a17505a283ab5ef65047b798cb49aa9e1"></a>

```c
uint32_t bytesused
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bytesused](#a17505a283ab5ef65047b798cb49aa9e1)。

缓冲区中有效数据占用的字节数。

<a id="r_af5c1abf09e0047334e03afbc64226eba"></a>

```c
uint32_t timestamp
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp](#af5c1abf09e0047334e03afbc64226eba)。

以毫秒表示的时间参考：对于输入端点，表示最后一个数据字节实际接收的时刻；对于输出端点，表示最后一个数据字节应被消费的时刻。

<a id="r_abe25963ea5e42d6fe42de1f21b554b87"></a>

```c
uint16_t line_offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[line_offset](#abe25963ea5e42d6fe42de1f21b554b87)。

此缓冲区所表示的数据在帧内的行偏移量（line offset），相对于帧起始位置。

## 51.2\_详细说明（Detailed Documentation）

<a id="a6a62d7a50c717dc6bc85e2d8f6ae95e3"></a>

### `buffer`

```c
uint8_t* video_buffer::buffer
```

指向缓冲区起始位置的指针。

<a id="a17505a283ab5ef65047b798cb49aa9e1"></a>

### `bytesused`

```c
uint32_t video_buffer::bytesused
```

缓冲区中有效数据占用的字节数。

<a id="ab184d528487042650af105eb7d37381e"></a>

### `driver_data`

```c
void* video_buffer::driver_data
```

指向驱动专用数据的指针。

<a id="a84550afc674ad543c8c709d55ececda2"></a>

### `index`

```c
uint16_t video_buffer::index
```

缓冲区在视频缓冲池中的索引。

<a id="abe25963ea5e42d6fe42de1f21b554b87"></a>

### `line_offset`

```c
uint16_t video_buffer::line_offset
```

此缓冲区所表示的数据在帧内的行偏移量（line offset），相对于帧起始位置。

此偏移量以像素为单位，因此 `line_offset * pitch` 给出从帧起始位置计算的字节偏移量。

<a id="a687f782126d32b36b3b07aaa976a83a4"></a>

### `memory`

```c
uint8_t video_buffer::memory
```

缓冲区内存类型，参见 `video_buf_memory`。

<a id="a3f040775c683c91740c8bda5c96e621b"></a>

### `size`

```c
uint32_t video_buffer::size
```

缓冲区大小，单位为字节。

<a id="af5c1abf09e0047334e03afbc64226eba"></a>

### `timestamp`

```c
uint32_t video_buffer::timestamp
```

以毫秒表示的时间参考：对于输入端点，表示最后一个数据字节实际接收的时刻；对于输出端点，表示最后一个数据字节应被消费的时刻。

<a id="a46dd9bd9398ff74e4f9859a07b9c48af"></a>

### `type`

```c
enum video_buf_type video_buffer::type
```

缓冲区类型。

本数据类型文档由以下文件生成：

- `zephyr/video/types.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/video/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2video_2types_8h_source.html)
- [video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [video_buf_memory](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ga43aa9bdc7283175df8165332a29c3f6c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_uaol_ep_table_entry_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_video_caps_结构体.md)
