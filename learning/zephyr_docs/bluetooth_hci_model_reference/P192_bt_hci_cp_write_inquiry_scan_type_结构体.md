---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-192
title: bt_hci_cp_write_inquiry_scan_type_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__inquiry__scan__type.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第192章\_bt\_hci\_cp\_write\_inquiry\_scan\_type\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__inquiry__scan__type.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

写入查询扫描类型（Write Inquiry Scan Type）的 HCI 命令参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

写入查询扫描类型（Write Inquiry Scan Type）的 HCI 命令参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 192.1\_数据成员（Data Fields）

<a id="r_a6342e77d0c83c1b7c8fd3bd1eeddf8b4"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a6342e77d0c83c1b7c8fd3bd1eeddf8b4)。

查询扫描类型（Inquiry Scan Type）。

## 192.2\_详细说明（Detailed Documentation）

<a id="a6342e77d0c83c1b7c8fd3bd1eeddf8b4"></a>

### `type`

```c
uint8_t bt_hci_cp_write_inquiry_scan_type::type
```

查询扫描类型（Inquiry Scan Type）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 192.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P191_bt_hci_cp_write_inquiry_scan_activity_结构体.md) · [返回大纲](大纲.md) · [下一章](P193_bt_hci_cp_write_le_host_supp_结构体.md)
