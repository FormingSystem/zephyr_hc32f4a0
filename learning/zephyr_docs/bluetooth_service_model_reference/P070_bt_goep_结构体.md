---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-70
title: bt_goep_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_bt\_goep\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用对象交换配置文件（Generic Object Exchange Profile，GOEP）结构体。

```c
#include <zephyr/bluetooth/classic/goep.h>
```

<a id="details"></a>

通用对象交换规范结构（GOEP structure）。注意（Note），传输版本选择与生命周期规则如下：活动会话中，`bt_goep::v1` 和 `bt_goep::v2` 必须恰有一个被设置为非 `NULL`。所指向的 `bt_goep_transport_v1`／`bt_goep_transport_v2` 实例，必须在传输连接的整个生命周期内保持有效且地址稳定；因为蓝牙主机协议栈会在异步回调中，对嵌入的 RFCOMM／L2CAP 对象使用 `CONTAINER_OF()`。调用任何 GOEP 传输连接或注册 API 之前，必须将版本专用对象的反向指针 `bt_goep_transport_v1::goep`／`bt_goep_transport_v2::goep` 初始化为指向父通用对象交换规范对象（Generic Object Exchange Profile，GOEP）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_a9820cd834fb77847110b0c0f490b637e"></a>

```c
struct bt_goep_transport_v1 * v1
```

相关声明：[bt_goep_transport_v1](P075_bt_goep_transport_v1_结构体.md)、[v1](#a9820cd834fb77847110b0c0f490b637e)。

用于传输版本 1（Transport v1）。

<a id="r_a6d341f018f6e7dc9187eab11cea9bc53"></a>

```c
struct bt_goep_transport_v2 * v2
```

相关声明：[bt_goep_transport_v2](P076_bt_goep_transport_v2_结构体.md)、[v2](#a6d341f018f6e7dc9187eab11cea9bc53)。

用于传输版本 2（Transport v2）。

<a id="r_abca52709a4b2535eccecb632a1a6f29d"></a>

```c
const struct bt_goep_transport_ops * transport_ops
```

相关声明：[bt_goep_transport_ops](P073_bt_goep_transport_ops_结构体.md)、[transport_ops](#abca52709a4b2535eccecb632a1a6f29d)。

通用对象交换规范传输操作（GOEP transport operations）。

<a id="r_a8ff09a1652dca4c9d10c6bbef7c73c5f"></a>

```c
struct bt_obex obex
```

相关声明：[bt_obex](P127_bt_obex_结构体.md)、[obex](#a8ff09a1652dca4c9d10c6bbef7c73c5f)。

对象交换对象（OBEX object）。

## 70.2\_详细说明（Detailed Documentation）

<a id="a8ff09a1652dca4c9d10c6bbef7c73c5f"></a>

### `obex`

```c
struct bt_obex bt_goep::obex
```

对象交换对象（OBEX object）。

<a id="abca52709a4b2535eccecb632a1a6f29d"></a>

### `transport_ops`

```c
const struct bt_goep_transport_ops* bt_goep::transport_ops
```

通用对象交换规范传输操作（GOEP transport operations）。

上层提供通用对象交换规范结构（GOEP structure）时，应将操作表传给 `transport_ops`。

<a id="a9820cd834fb77847110b0c0f490b637e"></a>

### `v1`

```c
struct bt_goep_transport_v1* bt_goep::v1
```

用于传输版本 1（Transport v1）。

使用传输版本 2（Transport v2）时必须为 `NULL`。

<a id="a6d341f018f6e7dc9187eab11cea9bc53"></a>

### `v2`

```c
struct bt_goep_transport_v2* bt_goep::v2
```

用于传输版本 2（Transport v2）。

使用传输版本 1（Transport v1）时必须为 `NULL`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/goep.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h_source.html)
- [bt_goep_transport_v1](P075_bt_goep_transport_v1_结构体.md)
- [bt_goep_transport_v2](P076_bt_goep_transport_v2_结构体.md)
- [bt_goep_transport_ops](P073_bt_goep_transport_ops_结构体.md)
- [bt_obex](P127_bt_obex_结构体.md)
- [CONTAINER_OF()](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)
- [bt_goep_transport_v1::goep](P075_bt_goep_transport_v1_结构体.md#a82ed6f11432432f051c705bddfd7a53b)
- [bt_goep_transport_v2::goep](P076_bt_goep_transport_v2_结构体.md#a5d3086e35bd244810e87d4bd0023e7bc)
- [通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_bt_gmap_feat_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_bt_goep_transport_结构体.md)
