---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-171
title: bt_sdp_record_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__record.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第171章\_bt\_sdp\_record\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__record.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）的服务记录值（Service Record Value）。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

服务发现协议（SDP）的服务记录值（Service Record Value）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 171.1\_数据成员（Data Fields）

<a id="r_ae94becbbce55a43661ef0c563e314b6b"></a>

```c
uint32_t handle
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[handle](#ae94becbbce55a43661ef0c563e314b6b)。

冗余字段，用于快速引用。

<a id="r_ad8ee5b17c45ca32696a492bc9c62d4fd"></a>

```c
struct bt_sdp_attribute * attrs
```

相关声明：[bt_sdp_attribute](P165_bt_sdp_attribute_结构体.md)、[attrs](#ad8ee5b17c45ca32696a492bc9c62d4fd)。

属性数组的基地址。

<a id="r_a2bbcb54c385f88d512c1ccd4cf5e05ff"></a>

```c
size_t attr_count
```

相关声明：[attr_count](#a2bbcb54c385f88d512c1ccd4cf5e05ff)。

属性数量。

<a id="r_ad54ca76a96964df3a6ac909eb54274df"></a>

```c
uint8_t index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[index](#ad54ca76a96964df3a6ac909eb54274df)。

记录在链表（LL）中的索引。

<a id="r_a07caa07efa3c4bea065db4f39a72d70b"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a07caa07efa3c4bea065db4f39a72d70b)。

## 171.2\_详细说明（Detailed Documentation）

<a id="a2bbcb54c385f88d512c1ccd4cf5e05ff"></a>

### `attr_count`

```c
size_t bt_sdp_record::attr_count
```

属性数量。

<a id="ad8ee5b17c45ca32696a492bc9c62d4fd"></a>

### `attrs`

```c
struct bt_sdp_attribute* bt_sdp_record::attrs
```

属性数组的基地址。

<a id="ae94becbbce55a43661ef0c563e314b6b"></a>

### `handle`

```c
uint32_t bt_sdp_record::handle
```

冗余字段，用于快速引用。

<a id="ad54ca76a96964df3a6ac909eb54274df"></a>

### `index`

```c
uint8_t bt_sdp_record::index
```

记录在链表（LL）中的索引。

<a id="a07caa07efa3c4bea065db4f39a72d70b"></a>

### `node`

```c
sys_snode_t bt_sdp_record::node
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 171.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_sdp_attribute](P165_bt_sdp_attribute_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P170_bt_sdp_discover_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P172_bt_tbs_cb_结构体.md)
