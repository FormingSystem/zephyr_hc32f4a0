---
id: learning.zephyr-docs.audio-video-model-reference.page-16
title: mpipe_buffer_meta_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__buffer__meta.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_mpipe\_buffer\_meta\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__buffer__meta.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

存储在net_buf user_data中的通用缓冲区元数据（Buffer Metadata）。

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

<a id="details"></a>

存储在net_buf user_data中的通用缓冲区元数据（Buffer Metadata）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a9c1c2114a0f15f52f4c134bd6bb0bf1b"></a>

```c
struct mpipe_buffer_pool * pool
```

相关声明：[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[pool](#a9c1c2114a0f15f52f4c134bd6bb0bf1b)。

此缓冲区所属的缓冲池。

<a id="r_aaac565e0d6f8a80a7d4a3b1e0e756198"></a>

```c
uint32_t bytes_used
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bytes_used](#aaac565e0d6f8a80a7d4a3b1e0e756198)。

有效载荷长度，以字节为单位。

<a id="r_a030b6e1f0c2b88c0e7bc5cdc86bb7740"></a>

```c
uint32_t timestamp
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp](#a030b6e1f0c2b88c0e7bc5cdc86bb7740)。

时间戳，单位为毫秒。

<a id="r_af9725c46e3959c7c9821537851c2a17f"></a>

```c
void * driver_buf
```

相关声明：[driver_buf](#af9725c46e3959c7c9821537851c2a17f)。

指向驱动实际拥有的缓冲区的指针。

<a id="r_a61f7a290475f471058ddd477a32206ea"></a>

```c
void * priv
```

相关声明：[priv](#a61f7a290475f471058ddd477a32206ea)。

供插件专用的不透明指针（opaque pointer）。

## 16.2\_详细说明（Detailed Documentation）

<a id="aaac565e0d6f8a80a7d4a3b1e0e756198"></a>

### `bytes_used`

```c
uint32_t mpipe_buffer_meta::bytes_used
```

有效载荷长度，以字节为单位。

对应 `net_buf` 的 `len` 字段，但该字段只有 16 位，无法容纳视频帧长度：读取方使用本字段，写入方同时设置两者。

<a id="af9725c46e3959c7c9821537851c2a17f"></a>

### `driver_buf`

```c
void* mpipe_buffer_meta::driver_buf
```

指向驱动实际拥有的缓冲区的指针。

<a id="a9c1c2114a0f15f52f4c134bd6bb0bf1b"></a>

### `pool`

```c
struct mpipe_buffer_pool* mpipe_buffer_meta::pool
```

此缓冲区所属的缓冲池。

<a id="a61f7a290475f471058ddd477a32206ea"></a>

### `priv`

```c
void* mpipe_buffer_meta::priv
```

供插件专用的不透明指针（opaque pointer）。

<a id="a030b6e1f0c2b88c0e7bc5cdc86bb7740"></a>

### `timestamp`

```c
uint32_t mpipe_buffer_meta::timestamp
```

时间戳，单位为毫秒。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_buffer.h`

## 16.3\_原页交叉引用（Cross References）

- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h_source.html)
- [mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_mpipe_bin_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_mpipe_buffer_pool_结构体.md)
