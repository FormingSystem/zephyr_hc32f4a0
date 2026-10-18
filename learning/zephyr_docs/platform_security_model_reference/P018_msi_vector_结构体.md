---
id: learning.zephyr-docs.platform-security-model-reference.page-18
title: msi_vector_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsi__vector.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_msi\_vector\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsi__vector.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a643d712565f3464874efaab81b25b68a"></a>

```c
pcie_bdf_t bdf
```

相关声明：[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bdf](#a643d712565f3464874efaab81b25b68a)。

<a id="r_aec3f368bdbe75d9e53d6bc9b0f6a18a7"></a>

```c
arch_msi_vector_t arch
```

相关声明：[arch](#aec3f368bdbe75d9e53d6bc9b0f6a18a7)。

## 18.2\_详细说明（Detailed Documentation）

<a id="aec3f368bdbe75d9e53d6bc9b0f6a18a7"></a>

### `arch`

```c
arch_msi_vector_t msi_vector::arch
```

<a id="a643d712565f3464874efaab81b25b68a"></a>

### `bdf`

```c
pcie_bdf_t msi_vector::bdf
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/pcie/msi.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/msi.h](https://docs.zephyrproject.org/latest/doxygen/html/msi_8h_source.html)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_mcontext_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_msix_vector_结构体.md)
