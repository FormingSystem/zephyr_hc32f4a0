---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-168
title: bt_sdp_client_result_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__client__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第168章\_bt\_sdp\_client\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__client__result.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用SDP客户端查询结果（Client Query Result）的数据容器。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

通用SDP客户端查询结果（Client Query Result）的数据容器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 168.1\_数据成员（Data Fields）

<a id="r_aa223dc666cbeaaebea462362188c531d"></a>

```c
struct net_buf * resp_buf
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[resp_buf](#aa223dc666cbeaaebea462362188c531d)。

包含给定 UUID 对应的未解析 SDP 记录结果的缓冲区。

<a id="r_aa1d12c7e550773963691e3b40ec6dd8e"></a>

```c
bool next_record_hint
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[next_record_hint](#aa1d12c7e550773963691e3b40ec6dd8e)。

指示给定 UUID 是否还有更多结果块的标志。

## 168.2\_详细说明（Detailed Documentation）

<a id="aa1d12c7e550773963691e3b40ec6dd8e"></a>

### `next_record_hint`

```c
bool bt_sdp_client_result::next_record_hint
```

指示给定 UUID 是否还有更多结果块的标志。

<a id="aa223dc666cbeaaebea462362188c531d"></a>

### `resp_buf`

```c
struct net_buf* bt_sdp_client_result::resp_buf
```

包含给定 UUID 对应的未解析 SDP 记录结果的缓冲区。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 168.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P167_bt_sdp_attribute_id_range_结构体.md) · [返回大纲](大纲.md) · [下一章](P169_bt_sdp_data_elem_结构体.md)
