---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-127
title: bt_obex_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第127章\_bt\_obex\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象交换协议（OBEX）结构。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="details"></a>

对象交换协议（OBEX）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 127.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a0ce1e889e58b6187e4ab0cf3205c6cac"></a>

```c
uint16_t mtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu](#aa22aa60d3dc3308865508717a4b9c398)。

对象交换（OBEX）传输的最大传输单元（MTU）。

<a id="r_ac2bc4ebc3b440c1be71c033b7c051c98"></a>

```c
} rx
```

相关声明：[rx](#ac2bc4ebc3b440c1be71c033b7c051c98)。

接收配置（Receiving configurations）。

```c
struct {
```

<a id="r_a3b9c937d9f1fe9da5a2705f7748e6801"></a>

```c
uint16_t mtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu](#aa22aa60d3dc3308865508717a4b9c398)。

对象交换（OBEX）传输的最大传输单元（MTU）。

<a id="r_a9aa32991272416015a9746e7cf8e9027"></a>

```c
} tx
```

相关声明：[tx](#a9aa32991272416015a9746e7cf8e9027)。

发送配置（Transmission configurations）。

## 127.2\_详细说明（Detailed Documentation）

<a id="aa22aa60d3dc3308865508717a4b9c398"></a>

### `mtu`

```c
uint16_t bt_obex::mtu
```

对象交换（OBEX）传输的最大传输单元（MTU）。

<a id="ac2bc4ebc3b440c1be71c033b7c051c98"></a>

### `[struct]`

```c
struct { ... } bt_obex::rx
```

接收配置（Receiving configurations）。

<a id="a9aa32991272416015a9746e7cf8e9027"></a>

### `[struct]`

```c
struct { ... } bt_obex::tx
```

发送配置（Transmission configurations）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/obex.h`

## 127.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P126_bt_nus_inst_结构体.md) · [返回大纲](大纲.md) · [下一章](P128_bt_obex_client_结构体.md)
