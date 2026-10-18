---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-167
title: bt_sdp_attribute_id_range_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attribute__id__range.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第167章\_bt\_sdp\_attribute\_id\_range\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attribute__id__range.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）的属性ID范围。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

SDP 属性 ID 范围。如果起始属性 ID 与结束属性 ID 相同，此范围就表示单个属性 ID。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 167.1\_数据成员（Data Fields）

<a id="r_a30a7eca0679107ef24154998bba35b78"></a>

```c
uint16_t beginning
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[beginning](#a30a7eca0679107ef24154998bba35b78)。

此范围的起始属性 ID。

<a id="r_a2d5deb3e68536e0d7c90bc25e2bc1fbe"></a>

```c
uint16_t ending
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ending](#a2d5deb3e68536e0d7c90bc25e2bc1fbe)。

此范围的结束属性 ID。

## 167.2\_详细说明（Detailed Documentation）

<a id="a30a7eca0679107ef24154998bba35b78"></a>

### `beginning`

```c
uint16_t bt_sdp_attribute_id_range::beginning
```

此范围的起始属性 ID。

<a id="a2d5deb3e68536e0d7c90bc25e2bc1fbe"></a>

### `ending`

```c
uint16_t bt_sdp_attribute_id_range::ending
```

此范围的结束属性 ID。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 167.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P166_bt_sdp_attribute_id_list_结构体.md) · [返回大纲](大纲.md) · [下一章](P168_bt_sdp_client_result_结构体.md)
