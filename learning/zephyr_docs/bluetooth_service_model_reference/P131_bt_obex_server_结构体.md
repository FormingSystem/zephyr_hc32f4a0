---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-131
title: bt_obex_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第131章\_bt\_obex\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象交换协议（OBEX）的服务器结构。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="details"></a>

对象交换协议（OBEX）的服务器结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 131.1\_数据成员（Data Fields）

<a id="r_ac96bcf45b1753cacb8a797c5f7c29eed"></a>

```c
struct bt_obex * obex
```

相关声明：[bt_obex](P127_bt_obex_结构体.md)、[obex](#ac96bcf45b1753cacb8a797c5f7c29eed)。

对象交换（OBEX）对象。

<a id="r_ac3acbf06e1dfa787507bba076be85e14"></a>

```c
const struct bt_uuid_128 * uuid
```

相关声明：[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](#ac3acbf06e1dfa787507bba076be85e14)。

服务的 UUID。

<a id="r_aefe5b0dbed43308a4881643b5705f033"></a>

```c
const struct bt_obex_server_ops * ops
```

相关声明：[bt_obex_server_ops](P132_bt_obex_server_ops_结构体.md)、[ops](#aefe5b0dbed43308a4881643b5705f033)。

OBEX 服务器操作（Server operations）。

```c
struct {
```

<a id="r_a59f03ddb130ff3f5d359033c69d9252a"></a>

```c
uint16_t mopl
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mopl](#a3aa4c23ecfea67698b6739b670a77aae)。

最大 OBEX 数据包长度（Maximum OBEX Packet Length，MOPL）。

<a id="r_a03527bd1e6f2907658756c08e342c283"></a>

```c
} rx
```

相关声明：[rx](#a03527bd1e6f2907658756c08e342c283)。

接收配置（Receiving configurations）。

```c
struct {
```

<a id="r_a79eb6770d217e18689a4d849cca85551"></a>

```c
uint16_t mopl
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mopl](#a3aa4c23ecfea67698b6739b670a77aae)。

最大 OBEX 数据包长度（Maximum OBEX Packet Length，MOPL）。

<a id="r_a3ea81fb07df98a2dd9b9bfdb0acfdf62"></a>

```c
} tx
```

相关声明：[tx](#a3ea81fb07df98a2dd9b9bfdb0acfdf62)。

发送配置（Transmission configurations）。

## 131.2\_详细说明（Detailed Documentation）

<a id="a3aa4c23ecfea67698b6739b670a77aae"></a>

### `mopl`

```c
uint16_t bt_obex_server::mopl
```

最大 OBEX 数据包长度（Maximum OBEX Packet Length，MOPL）。

<a id="ac96bcf45b1753cacb8a797c5f7c29eed"></a>

### `obex`

```c
struct bt_obex* bt_obex_server::obex
```

对象交换（OBEX）对象。

<a id="aefe5b0dbed43308a4881643b5705f033"></a>

### `ops`

```c
const struct bt_obex_server_ops* bt_obex_server::ops
```

OBEX 服务器操作（Server operations）。

如果这是 OBEX 服务器，上层在提供 OBEX 服务器结构体时，应通过 `server_ops` 传入服务器操作。

<a id="a03527bd1e6f2907658756c08e342c283"></a>

### `[struct]`

```c
struct { ... } bt_obex_server::rx
```

接收配置（Receiving configurations）。

<a id="a3ea81fb07df98a2dd9b9bfdb0acfdf62"></a>

### `[struct]`

```c
struct { ... } bt_obex_server::tx
```

发送配置（Transmission configurations）。

<a id="ac3acbf06e1dfa787507bba076be85e14"></a>

### `uuid`

```c
const struct bt_uuid_128* bt_obex_server::uuid
```

服务的 UUID。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/obex.h`

## 131.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html)
- [bt_obex](P127_bt_obex_结构体.md)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [bt_obex_server_ops](P132_bt_obex_server_ops_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P130_bt_obex_hdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P132_bt_obex_server_ops_结构体.md)
