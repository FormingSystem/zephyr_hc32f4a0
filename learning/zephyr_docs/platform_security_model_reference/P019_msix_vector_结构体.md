---
id: learning.zephyr-docs.platform-security-model-reference.page-19
title: msix_vector_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsix__vector.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_msix\_vector\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsix__vector.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a2c09a989a9ed99536d85c0e800283743"></a>

```c
uint32_t msg_addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[msg_addr](#a2c09a989a9ed99536d85c0e800283743)。

<a id="r_a908e2d095b43713f0b9682716cd4ae85"></a>

```c
uint32_t msg_up_addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[msg_up_addr](#a908e2d095b43713f0b9682716cd4ae85)。

<a id="r_acd899f1dc388ef49f38d593083e0042d"></a>

```c
uint32_t msg_data
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[msg_data](#acd899f1dc388ef49f38d593083e0042d)。

<a id="r_ac4d0f7192cc8bcaffd4fac75589ca298"></a>

```c
uint32_t vector_ctrl
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[vector_ctrl](#ac4d0f7192cc8bcaffd4fac75589ca298)。

## 19.2\_详细说明（Detailed Documentation）

<a id="a2c09a989a9ed99536d85c0e800283743"></a>

### `msg_addr`

```c
uint32_t msix_vector::msg_addr
```

<a id="acd899f1dc388ef49f38d593083e0042d"></a>

### `msg_data`

```c
uint32_t msix_vector::msg_data
```

<a id="a908e2d095b43713f0b9682716cd4ae85"></a>

### `msg_up_addr`

```c
uint32_t msix_vector::msg_up_addr
```

<a id="ac4d0f7192cc8bcaffd4fac75589ca298"></a>

### `vector_ctrl`

```c
uint32_t msix_vector::vector_ctrl
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/pcie/msi.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/msi.h](https://docs.zephyrproject.org/latest/doxygen/html/msi_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_msi_vector_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_nxp_flexio_child_结构体.md)
