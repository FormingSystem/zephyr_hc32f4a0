---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-57
title: bt_avrcp_passthrough_opvu_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__passthrough__opvu__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_bt\_avrcp\_passthrough\_opvu\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__passthrough__opvu__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_a17f6d3c32417102c04502336235f94fa"></a>

```c
uint8_t company_id [(3)]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[company_id](#a17f6d3c32417102c04502336235f94fa)。

<a id="r_a13db1521501ab7c24643b2d1fd6e956a"></a>

```c
uint16_t opid_vu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[opid_vu](#a13db1521501ab7c24643b2d1fd6e956a)。

## 57.2\_详细说明（Detailed Documentation）

<a id="a17f6d3c32417102c04502336235f94fa"></a>

### `company_id`

```c
uint8_t bt_avrcp_passthrough_opvu_data::company_id[(3)]
```

<a id="a13db1521501ab7c24643b2d1fd6e956a"></a>

### `opid_vu`

```c
uint16_t bt_avrcp_passthrough_opvu_data::opid_vu
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_bt_avrcp_passthrough_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_bt_avrcp_passthrough_rsp_结构体.md)
