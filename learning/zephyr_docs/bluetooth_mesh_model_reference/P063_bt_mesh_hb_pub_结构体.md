---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-63
title: bt_mesh_hb_pub_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__hb__pub.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_bt\_mesh\_hb\_pub\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__hb__pub.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

心跳发布（Heartbeat Publication）的参数。

```c
#include <zephyr/bluetooth/mesh/heartbeat.h>
```

<a id="details"></a>

心跳发布（Heartbeat Publication）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_aaeb4c9000088418d8688b4f2f964335a"></a>

```c
uint16_t dst
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst](#aaeb4c9000088418d8688b4f2f964335a)。

目的地址（Destination Address）。

<a id="r_a7161896dd5e337b2b0ee671f59a2444a"></a>

```c
uint16_t count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[count](#a7161896dd5e337b2b0ee671f59a2444a)。

剩余发布次数（Remaining publish count）。

<a id="r_a82dd3457291cc4a939883590e27fdbfb"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#a82dd3457291cc4a939883590e27fdbfb)。

生存时间值（Time To Live，TTL）。

<a id="r_a08f32f66fb5c7c0011651633ad212bc9"></a>

```c
uint16_t feat
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[feat](#a08f32f66fb5c7c0011651633ad212bc9)。

特性位图（Feature bitmap）；其中的特性变化时触发心跳发布（Heartbeat publication）。

<a id="r_af8ed3029b088c7b45be4912eb0d9024d"></a>

```c
uint16_t net_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#af8ed3029b088c7b45be4912eb0d9024d)。

发布所用的网络索引（Network index）。

<a id="r_a0bf6205724b157fe374e24c024f240c9"></a>

```c
uint32_t period
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[period](#a0bf6205724b157fe374e24c024f240c9)。

发布周期（Publication period），单位为秒。

## 63.2\_详细说明（Detailed Documentation）

<a id="a7161896dd5e337b2b0ee671f59a2444a"></a>

### `count`

```c
uint16_t bt_mesh_hb_pub::count
```

剩余发布次数（Remaining publish count）。

<a id="aaeb4c9000088418d8688b4f2f964335a"></a>

### `dst`

```c
uint16_t bt_mesh_hb_pub::dst
```

目的地址（Destination Address）。

<a id="a08f32f66fb5c7c0011651633ad212bc9"></a>

### `feat`

```c
uint16_t bt_mesh_hb_pub::feat
```

特性位图（Feature bitmap）；其中的特性变化时触发心跳发布（Heartbeat publication）。

合法值为 `BT_MESH_FEAT_RELAY`、`BT_MESH_FEAT_PROXY`、`BT_MESH_FEAT_FRIEND` 和 `BT_MESH_FEAT_LOW_POWER`。

<a id="af8ed3029b088c7b45be4912eb0d9024d"></a>

### `net_idx`

```c
uint16_t bt_mesh_hb_pub::net_idx
```

发布所用的网络索引（Network index）。

<a id="a0bf6205724b157fe374e24c024f240c9"></a>

### `period`

```c
uint32_t bt_mesh_hb_pub::period
```

发布周期（Publication period），单位为秒。

<a id="a82dd3457291cc4a939883590e27fdbfb"></a>

### `ttl`

```c
uint8_t bt_mesh_hb_pub::ttl
```

生存时间值（Time To Live，TTL）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/heartbeat.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/heartbeat.h](https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [BT_MESH_FEAT_RELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gac588eefe83db94784a420ce063f02b55)
- [BT_MESH_FEAT_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gaee648ce202316c56d4d588cb0ad5aeb4)
- [BT_MESH_FEAT_FRIEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga8f27086b3bc3c4a6e14621836f9f8e80)
- [BT_MESH_FEAT_LOW_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gaad71a36c82b4e4d3fa334ecff5cc0171)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_bt_mesh_hb_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_bt_mesh_hb_sub_结构体.md)
