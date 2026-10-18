---
id: learning.zephyr-docs.network-core-model-reference.page-10
title: ieee802154_cmd_assoc_res_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__cmd__assoc__res.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_ieee802154\_cmd\_assoc\_res\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__cmd__assoc__res.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

关联响应（Association Response）命令的载荷。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

关联响应（Association Response）命令的载荷。见第7.5.3节及图7-23。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a0aec016dd92112254d9d162734a9f2d6"></a>

```c
uint16_t short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[short_addr](#a0aec016dd92112254d9d162734a9f2d6)。

协调器分配的短地址（Short Address）；未分配时为特殊值。

<a id="r_a372c5c7bee963eb890ccddcab9526fc4"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a372c5c7bee963eb890ccddcab9526fc4)。

关联状态（Association Status），见ieee802154_association_status_field。

## 10.2\_详细说明（Detailed Documentation）

<a id="a0aec016dd92112254d9d162734a9f2d6"></a>

### `short_addr`

```c
uint16_t ieee802154_cmd_assoc_res::short_addr
```

协调器分配的短地址（Short Address）；未分配时为特殊值。

<a id="a372c5c7bee963eb890ccddcab9526fc4"></a>

### `status`

```c
uint8_t ieee802154_cmd_assoc_res::status
```

关联状态（Association Status），见ieee802154_association_status_field。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ieee802154_association_status_field](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa2c9cb8ba5b7c397c695a9a591649b91)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_ieee802154_cmd_assoc_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_ieee802154_cmd_coord_realign_结构体.md)
