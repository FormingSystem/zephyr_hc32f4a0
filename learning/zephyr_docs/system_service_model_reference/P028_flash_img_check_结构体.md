---
id: learning.zephyr-docs.system-service-model-reference.page-28
title: flash_img_check_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__img__check.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_flash\_img\_check\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__img__check.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于验证闪存区域完整性（Flash Region Integrity）的结构。

```c
#include <zephyr/dfu/flash_img.h>
```

<a id="details"></a>

用于验证 Flash 区域完整性（integrity）的结构体。匹配向量（match vector）的长度固定，取决于用于验证 Flash 完整性的哈希算法输出大小。目前可用的算法为 SHA-256。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a6c4aebe9974ddebf0ceafe7f61af8ae9"></a>

```c
const uint8_t * match
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[match](#a6c4aebe9974ddebf0ceafe7f61af8ae9)。

<a id="r_abac05d254f5fc46093808083c86be379"></a>

```c
size_t clen
```

相关声明：[clen](#abac05d254f5fc46093808083c86be379)。

匹配向量数据。

## 28.2\_详细说明（Detailed Documentation）

<a id="abac05d254f5fc46093808083c86be379"></a>

### `clen`

```c
size_t flash_img_check::clen
```

匹配向量数据。

<a id="a6c4aebe9974ddebf0ceafe7f61af8ae9"></a>

### `match`

```c
const uint8_t* flash_img_check::match
```

本数据类型文档由以下文件生成：

- `zephyr/dfu/flash_img.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/dfu/flash_img.h](https://docs.zephyrproject.org/latest/doxygen/html/flash__img_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_flash_area_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_flash_img_context_结构体.md)
