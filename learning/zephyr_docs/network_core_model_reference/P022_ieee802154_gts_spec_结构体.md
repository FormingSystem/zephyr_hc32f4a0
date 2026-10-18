---
id: learning.zephyr-docs.network-core-model-reference.page-22
title: ieee802154_gts_spec_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__gts__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_ieee802154\_gts\_spec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__gts__spec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

信标载荷中的保证时隙规范（GTS Specification）字段。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

信标载荷的保证时隙规范（GTS Specification）字段。见第7.3.1.5节及图7-9。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a5cea7b714d7f8ab2afe1261d96593491"></a>

```c
uint8_t permit: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[permit](#a5cea7b714d7f8ab2afe1261d96593491)。

保证时隙许可子字段（GTS Permit Subfield）。

<a id="r_a37d0ae20cb6da8ed68848d06b92013f5"></a>

```c
uint8_t reserved: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#a37d0ae20cb6da8ed68848d06b92013f5)。

保留字段（Reserved），应为0。

<a id="r_a81f217f576b60b71c84cb62d307400df"></a>

```c
uint8_t desc_count: 3
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[desc_count](#a81f217f576b60b71c84cb62d307400df)。

保证时隙描述符数量子字段（GTS Descriptor Count Subfield）。

## 22.2\_详细说明（Detailed Documentation）

<a id="a81f217f576b60b71c84cb62d307400df"></a>

### `desc_count`

```c
uint8_t ieee802154_gts_spec::desc_count
```

保证时隙描述符数量子字段（GTS Descriptor Count Subfield）。

<a id="a5cea7b714d7f8ab2afe1261d96593491"></a>

### `permit`

```c
uint8_t ieee802154_gts_spec::permit
```

保证时隙许可子字段（GTS Permit Subfield）。

<a id="a37d0ae20cb6da8ed68848d06b92013f5"></a>

### `reserved`

```c
uint8_t ieee802154_gts_spec::reserved
```

保留字段（Reserved），应为0。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_ieee802154_gts_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_ieee802154_header_ie_csl_结构体.md)
