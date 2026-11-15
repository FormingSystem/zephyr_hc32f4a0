---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-128
title: bt_obex_client_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第128章\_bt\_obex\_client\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象交换协议（OBEX）的客户端结构。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="details"></a>

对象交换协议（OBEX）的客户端结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 128.1\_数据成员（Data Fields）

<a id="r_a271142fde25a5622e25404e3a1f469ad"></a>

```c
struct bt_obex * obex
```

相关声明：[bt_obex](P127_bt_obex_结构体.md)、[obex](#a271142fde25a5622e25404e3a1f469ad)。

对象交换（OBEX）对象。

<a id="r_a4b9a3f84253936e7babbfc0077da994a"></a>

```c
const struct bt_obex_client_ops * ops
```

相关声明：[bt_obex_client_ops](P129_bt_obex_client_ops_结构体.md)、[ops](#a4b9a3f84253936e7babbfc0077da994a)。

OBEX 客户端操作（Client operations）。

```c
struct {
```

<a id="r_a17ccffd3d72ee116c15b914d97f4e732"></a>

```c
uint16_t mopl
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mopl](#adb6891c7c9682987c12021280e18c8d4)。

最大 OBEX 数据包长度（Maximum OBEX Packet Length，MOPL）。

<a id="r_add9c1c75137848fbfbaf65b63ed01e3b"></a>

```c
} rx
```

相关声明：[rx](#add9c1c75137848fbfbaf65b63ed01e3b)。

接收配置（Receiving configurations）。

```c
struct {
```

<a id="r_acfea5e688fbf6a005b110434e423110d"></a>

```c
uint16_t mopl
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mopl](#adb6891c7c9682987c12021280e18c8d4)。

最大 OBEX 数据包长度（Maximum OBEX Packet Length，MOPL）。

<a id="r_ac66119d12d329310a666a1b2d7175fce"></a>

```c
} tx
```

相关声明：[tx](#ac66119d12d329310a666a1b2d7175fce)。

发送配置（Transmission configurations）。

## 128.2\_详细说明（Detailed Documentation）

<a id="adb6891c7c9682987c12021280e18c8d4"></a>

### `mopl`

```c
uint16_t bt_obex_client::mopl
```

最大 OBEX 数据包长度（Maximum OBEX Packet Length，MOPL）。

<a id="a271142fde25a5622e25404e3a1f469ad"></a>

### `obex`

```c
struct bt_obex* bt_obex_client::obex
```

对象交换（OBEX）对象。

<a id="a4b9a3f84253936e7babbfc0077da994a"></a>

### `ops`

```c
const struct bt_obex_client_ops* bt_obex_client::ops
```

OBEX 客户端操作（Client operations）。

如果这是 OBEX 客户端，上层在提供 OBEX 客户端结构体时，应通过 `client_ops` 传入客户端操作。

<a id="add9c1c75137848fbfbaf65b63ed01e3b"></a>

### `[struct]`

```c
struct { ... } bt_obex_client::rx
```

接收配置（Receiving configurations）。

<a id="ac66119d12d329310a666a1b2d7175fce"></a>

### `[struct]`

```c
struct { ... } bt_obex_client::tx
```

发送配置（Transmission configurations）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/obex.h`

## 128.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html)
- [bt_obex](P127_bt_obex_结构体.md)
- [bt_obex_client_ops](P129_bt_obex_client_ops_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P127_bt_obex_结构体.md) · [返回大纲](大纲.md) · [下一章](P129_bt_obex_client_ops_结构体.md)
