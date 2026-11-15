---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-58
title: bt_avrcp_passthrough_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__passthrough__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_bt\_avrcp\_passthrough\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__passthrough__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a91aaa705b91cc9ca0954645a9a43c504"></a>

```c
uint8_t opid_state
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[opid_state](#a91aaa705b91cc9ca0954645a9a43c504)。

第 7 位为 `state_flag`，第 6–0 位为 `opid`。

<a id="r_a16c0388be437f140c5aaa1364cdfb3fe"></a>

```c
uint8_t data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_len](#a16c0388be437f140c5aaa1364cdfb3fe)。

<a id="r_a735fca5cd5e5d85e987af9748f9d0ab0"></a>

```c
struct bt_avrcp_passthrough_opvu_data data [0]
```

相关声明：[bt_avrcp_passthrough_opvu_data](P057_bt_avrcp_passthrough_opvu_data_结构体.md)、[data](#a735fca5cd5e5d85e987af9748f9d0ab0)。

`opvu` 数据。

## 58.2\_详细说明（Detailed Documentation）

<a id="a735fca5cd5e5d85e987af9748f9d0ab0"></a>

### `data`

```c
struct bt_avrcp_passthrough_opvu_data bt_avrcp_passthrough_rsp::data[0]
```

`opvu` 数据。

<a id="a16c0388be437f140c5aaa1364cdfb3fe"></a>

### `data_len`

```c
uint8_t bt_avrcp_passthrough_rsp::data_len
```

<a id="a91aaa705b91cc9ca0954645a9a43c504"></a>

### `opid_state`

```c
uint8_t bt_avrcp_passthrough_rsp::opid_state
```

第 7 位为 `state_flag`，第 6–0 位为 `opid`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_passthrough_opvu_data](P057_bt_avrcp_passthrough_opvu_data_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_bt_avrcp_passthrough_opvu_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_bt_avrcp_play_item_cmd_结构体.md)
