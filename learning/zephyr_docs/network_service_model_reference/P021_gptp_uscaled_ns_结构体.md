---
id: learning.zephyr-docs.network-service-model-reference.page-21
title: gptp_uscaled_ns_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgptp__uscaled__ns.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_gptp\_uscaled\_ns\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgptp__uscaled__ns.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

无符号缩放纳秒（UScaled Nanoseconds）。

```c
#include <zephyr/net/gptp.h>
```

<a id="details"></a>

无符号缩放纳秒（UScaled Nanoseconds）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_a11cd4f2cc15731ba91dab742fcea248f"></a>

```c
uint32_t high
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[high](#a11cd4f2cc15731ba91dab742fcea248f)。

高半部分（High half）。

<a id="r_ae374e99c81753ecd26ff9a7cac35dfa4"></a>

```c
uint64_t low
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[low](#ae374e99c81753ecd26ff9a7cac35dfa4)。

低半部分（Low half）。

## 21.2\_详细说明（Detailed Documentation）

<a id="a11cd4f2cc15731ba91dab742fcea248f"></a>

### `high`

```c
uint32_t gptp_uscaled_ns::high
```

高半部分（High half）。

<a id="ae374e99c81753ecd26ff9a7cac35dfa4"></a>

### `low`

```c
uint64_t gptp_uscaled_ns::low
```

低半部分（Low half）。

本数据类型文档由以下文件生成：

- `zephyr/net/gptp.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/net/gptp.h](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_gptp_scaled_ns_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_hci_cp_le_conn_update_结构体.md)
