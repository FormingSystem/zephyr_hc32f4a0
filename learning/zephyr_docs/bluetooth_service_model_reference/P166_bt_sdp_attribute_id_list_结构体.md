---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-166
title: bt_sdp_attribute_id_list_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attribute__id__list.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第166章\_bt\_sdp\_attribute\_id\_list\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attribute__id__list.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务属性及服务搜索属性事务（Service Attribute / Service Search Attribute）使用的SDP属性ID列表。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

服务属性及服务搜索属性事务（Service Attribute / Service Search Attribute）使用的SDP属性ID列表。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 166.1\_数据成员（Data Fields）

<a id="r_a3f0c472e904dd86bf95f8623b1d04d73"></a>

```c
size_t count
```

相关声明：[count](#a3f0c472e904dd86bf95f8623b1d04d73)。

SDP 属性 ID 范围的数量。

<a id="r_af38e30a77ad8b0a2e981d6a38caffa2d"></a>

```c
struct bt_sdp_attribute_id_range * ranges
```

相关声明：[bt_sdp_attribute_id_range](P167_bt_sdp_attribute_id_range_结构体.md)、[ranges](#af38e30a77ad8b0a2e981d6a38caffa2d)。

属性 ID 范围数组列表。

## 166.2\_详细说明（Detailed Documentation）

<a id="a3f0c472e904dd86bf95f8623b1d04d73"></a>

### `count`

```c
size_t bt_sdp_attribute_id_list::count
```

SDP 属性 ID 范围的数量。

编码后的列表必须能装入一个 SDP 请求 PDU：每个范围编码为 5 字节，单个属性 ID（起始值与结束值相等）编码为 3 字节；整个列表连同其 2 字节头部，总共不得超过 162 字节。`bt_sdp_discover()` 会拒绝更长的列表。

<a id="af38e30a77ad8b0a2e981d6a38caffa2d"></a>

### `ranges`

```c
struct bt_sdp_attribute_id_range* bt_sdp_attribute_id_list::ranges
```

属性 ID 范围数组列表。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 166.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [bt_sdp_attribute_id_range](P167_bt_sdp_attribute_id_range_结构体.md)
- [bt_sdp_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga44658df825a40f820a31e7adb4240d25)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P165_bt_sdp_attribute_结构体.md) · [返回大纲](大纲.md) · [下一章](P167_bt_sdp_attribute_id_range_结构体.md)
