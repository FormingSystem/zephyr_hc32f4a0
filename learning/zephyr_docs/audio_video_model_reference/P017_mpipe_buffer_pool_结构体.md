---
id: learning.zephyr-docs.audio-video-model-reference.page-17
title: mpipe_buffer_pool_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__buffer__pool.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_mpipe\_buffer\_pool\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__buffer__pool.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

缓冲池（Buffer Pool）结构。

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

<a id="details"></a>

缓冲池（Buffer Pool）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a4e4dd42ddcf7b0a76fc8db650940ade3"></a>

```c
struct mpipe_buffer_pool_config req_config
```

相关声明：[mpipe_buffer_pool_config](P018_mpipe_buffer_pool_config_结构体.md)、[req_config](#a4e4dd42ddcf7b0a76fc8db650940ade3)。

协商之前，此缓冲池自身的要求，包括所有者硬件的最低要求和应用的请求。

<a id="r_a2d3b29d91616908739e3d1e61628f8ec"></a>

```c
struct mpipe_buffer_pool_config config
```

相关声明：[mpipe_buffer_pool_config](P018_mpipe_buffer_pool_config_结构体.md)、[config](#a2d3b29d91616908739e3d1e61628f8ec)。

协商最终确定的配置，`mpipe_buffer_pool::start` 按此配置分配资源。

<a id="r_a2b300e70d25c4001552966a1a1861644"></a>

```c
struct net_buf_pool * nb_pool
```

相关声明：[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[nb_pool](#a2b300e70d25c4001552966a1a1861644)。

与此缓冲池关联的 `net_buf` 池。

<a id="r_a9f4030e94a053a1f4c8c3a019d8e4bd3"></a>

```c
int(* configure )(struct mpipe_buffer_pool *pool, const struct mpipe_structure *caps)
```

相关声明：[configure](#a9f4030e94a053a1f4c8c3a019d8e4bd3)、[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[mpipe_structure](P031_mpipe_structure_结构体.md)。

格式确定后，按照能力（capability）设置池中缓冲区的大小。

<a id="r_a0393683ad4c617362d302e43697f7bbe"></a>

```c
int(* set_config )(struct mpipe_buffer_pool *pool, const struct mpipe_buffer_pool_config *cfg)
```

相关声明：[set_config](#a0393683ad4c617362d302e43697f7bbe)、[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[mpipe_buffer_pool_config](P018_mpipe_buffer_pool_config_结构体.md)。

应用已协商的缓冲池配置。

<a id="r_af8560f9a89aef97ff0a8fbce3f182c6b"></a>

```c
int(* start )(struct mpipe_buffer_pool *pool)
```

相关声明：[start](#af8560f9a89aef97ff0a8fbce3f182c6b)、[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)。

启动缓冲池并分配资源。

<a id="r_a958bf985bcd2f6afcdefacc5c869a33b"></a>

```c
int(* stop )(struct mpipe_buffer_pool *pool)
```

相关声明：[stop](#a958bf985bcd2f6afcdefacc5c869a33b)、[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)。

停止缓冲池并释放资源。

<a id="r_af31bdf5dd0aa881fd9d4394bb1020045"></a>

```c
int(* acquire_buffer )(struct mpipe_buffer_pool *pool, struct net_buf **buf)
```

相关声明：[acquire_buffer](#af31bdf5dd0aa881fd9d4394bb1020045)、[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从池中获取缓冲区。

<a id="r_af542398f20b82e4f611fe31c8140ceaa"></a>

```c
int(* release_buffer )(struct mpipe_buffer_pool *pool, struct net_buf *buf)
```

相关声明：[release_buffer](#af542398f20b82e4f611fe31c8140ceaa)、[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将缓冲区释放回池中；缓冲区引用计数降为 0 时自动调用。

<a id="r_a80a7f1817444a353765fd82634631812"></a>

```c
bool started
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[started](#a80a7f1817444a353765fd82634631812)。

指示缓冲池是否已启动的标志。

## 17.2\_详细说明（Detailed Documentation）

<a id="af31bdf5dd0aa881fd9d4394bb1020045"></a>

### `acquire_buffer`

```c
int(* mpipe_buffer_pool::acquire_buffer) (struct mpipe_buffer_pool *pool, struct net_buf **buf)
```

从池中获取缓冲区。

<a id="a2d3b29d91616908739e3d1e61628f8ec"></a>

### `config`

```c
struct mpipe_buffer_pool_config mpipe_buffer_pool::config
```

协商最终确定的配置，`mpipe_buffer_pool::start` 按此配置分配资源。

每次运行开始时，此配置都是 `req_config` 的副本；`mpipe_buffer_pool_stop` 会将其恢复。因此，一次运行不会继承上一次运行的要求。

<a id="a9f4030e94a053a1f4c8c3a019d8e4bd3"></a>

### `configure`

```c
int(* mpipe_buffer_pool::configure) (struct mpipe_buffer_pool *pool, const struct mpipe_structure *caps)
```

格式确定后，按照能力（capability）设置池中缓冲区的大小。

<a id="a2b300e70d25c4001552966a1a1861644"></a>

### `nb_pool`

```c
struct net_buf_pool* mpipe_buffer_pool::nb_pool
```

与此缓冲池关联的 `net_buf` 池。

<a id="af542398f20b82e4f611fe31c8140ceaa"></a>

### `release_buffer`

```c
int(* mpipe_buffer_pool::release_buffer) (struct mpipe_buffer_pool *pool, struct net_buf *buf)
```

将缓冲区释放回池中；缓冲区引用计数降为 0 时自动调用。

<a id="a4e4dd42ddcf7b0a76fc8db650940ade3"></a>

### `req_config`

```c
struct mpipe_buffer_pool_config mpipe_buffer_pool::req_config
```

协商之前，此缓冲池自身的要求，包括所有者硬件的最低要求和应用的请求。

在设置阶段，通过 `mpipe_buffer_pool_set_req_config` 写入一次，协商过程绝不会改写，因此它始终是每次运行开始时的最低要求。

<a id="a0393683ad4c617362d302e43697f7bbe"></a>

### `set_config`

```c
int(* mpipe_buffer_pool::set_config) (struct mpipe_buffer_pool *pool, const struct mpipe_buffer_pool_config *cfg)
```

应用已协商的缓冲池配置。

实现会根据缓冲池能提供的资源验证 `cfg`，自行将接受的值写入 `mpipe_buffer_pool::config`，并通过返回负值 `errno` 表示拒绝。例如，后备分配器无法满足所需对齐时返回 `-ENOTSUP`；缓冲区数量超出池容量时返回 `-ENOSPC`。

<a id="af8560f9a89aef97ff0a8fbce3f182c6b"></a>

### `start`

```c
int(* mpipe_buffer_pool::start) (struct mpipe_buffer_pool *pool)
```

启动缓冲池并分配资源。

<a id="a80a7f1817444a353765fd82634631812"></a>

### `started`

```c
bool mpipe_buffer_pool::started
```

指示缓冲池是否已启动的标志。

<a id="a958bf985bcd2f6afcdefacc5c869a33b"></a>

### `stop`

```c
int(* mpipe_buffer_pool::stop) (struct mpipe_buffer_pool *pool)
```

停止缓冲池并释放资源。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_buffer.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h_source.html)
- [mpipe_buffer_pool_config](P018_mpipe_buffer_pool_config_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)
- [mpipe_structure](P031_mpipe_structure_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mpipe_buffer_pool_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga7ed6b0b1108097583138a61402c077ff)
- [mpipe_buffer_pool_set_req_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga8a80231824e6cbb7748e80df8d504e93)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_mpipe_buffer_meta_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_mpipe_buffer_pool_config_结构体.md)
