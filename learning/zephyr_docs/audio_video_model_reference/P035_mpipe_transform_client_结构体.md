---
id: learning.zephyr-docs.audio-video-model-reference.page-35
title: mpipe_transform_client_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__transform__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_mpipe\_transform\_client\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__transform__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

变换客户端元素（Transform Client Element）的结构。

```c
#include <zephyr/mpipe/mpipe_transform_client.h>
```

<a id="details"></a>

变换客户端元素（Transform client element）结构体，是多核管线客户端侧所有变换元素的基础结构。这些元素通过向服务器侧发起远程过程调用（RPC），将处理工作转移到服务器侧。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a8e406cdc0e2c448faf5c6e286779739e"></a>

```c
struct mpipe_transform transform
```

相关声明：[mpipe_transform](P034_mpipe_transform_结构体.md)、[transform](#a8e406cdc0e2c448faf5c6e286779739e)。

基础变换结构体。

<a id="r_a9d6edb742acdfe64509d0c3fb6567a36"></a>

```c
int(* init_rpc )(void)
```

相关声明：[init_rpc](#a9d6edb742acdfe64509d0c3fb6567a36)。

初始化客户端侧的 RPC 通信。

<a id="r_a65c1ee88e4255222e7b1ed93f4c56a58"></a>

```c
int(* process_fn_rpc )(uint32_t in_buf, uint32_t in_sz, uint32_t out_buf, uint32_t *out_sz)
```

相关声明：[process_fn_rpc](#a65c1ee88e4255222e7b1ed93f4c56a58)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

在服务器侧处理缓冲区的 RPC 处理函数。

## 35.2\_详细说明（Detailed Documentation）

<a id="a9d6edb742acdfe64509d0c3fb6567a36"></a>

### `init_rpc`

```c
int(* mpipe_transform_client::init_rpc) (void)
```

初始化客户端侧的 RPC 通信。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a65c1ee88e4255222e7b1ed93f4c56a58"></a>

### `process_fn_rpc`

```c
int(* mpipe_transform_client::process_fn_rpc) (uint32_t in_buf, uint32_t in_sz, uint32_t out_buf, uint32_t *out_sz)
```

在服务器侧处理缓冲区的 RPC 处理函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` in_buf` | 待处理输入缓冲区的地址。 |
| ` in_sz` | 输入缓冲区中有效字节的数量。 |
| ` out_buf` | 待填充的输出缓冲区地址。 |
| `[out] out_sz` | 写入输出缓冲区的字节数。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a8e406cdc0e2c448faf5c6e286779739e"></a>

### `transform`

```c
struct mpipe_transform mpipe_transform_client::transform
```

基础变换结构体。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_transform_client.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_transform_client.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform__client_8h_source.html)
- [mpipe_transform](P034_mpipe_transform_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_mpipe_transform_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_mpipe_value_结构体.md)
