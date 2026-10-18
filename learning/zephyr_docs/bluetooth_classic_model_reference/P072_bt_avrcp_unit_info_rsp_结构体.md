---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-72
title: bt_avrcp_unit_info_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__unit__info__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_bt\_avrcp\_unit\_info\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__unit__info__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_a92b869b3200841ea1d10aca41cdd9f77"></a>

```c
bt_avrcp_subunit_type_t unit_type
```

相关声明：[bt_avrcp_subunit_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga78ba828636b731b2c43e088a581bfee9)、[unit_type](#a92b869b3200841ea1d10aca41cdd9f77)。

<a id="r_a0225755bf457bc6d4046d8172af49217"></a>

```c
uint32_t company_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[company_id](#a0225755bf457bc6d4046d8172af49217)。

## 72.2\_详细说明（Detailed Documentation）

<a id="a0225755bf457bc6d4046d8172af49217"></a>

### `company_id`

```c
uint32_t bt_avrcp_unit_info_rsp::company_id
```

<a id="a92b869b3200841ea1d10aca41cdd9f77"></a>

### `unit_type`

```c
bt_avrcp_subunit_type_t bt_avrcp_unit_info_rsp::unit_type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [bt_avrcp_subunit_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga78ba828636b731b2c43e088a581bfee9)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_bt_avrcp_tg_cb_结构体.md) · [返回大纲](大纲.md)
