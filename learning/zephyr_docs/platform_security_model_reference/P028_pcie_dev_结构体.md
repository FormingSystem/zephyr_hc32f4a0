---
id: learning.zephyr-docs.platform-security-model-reference.page-28
title: pcie_dev_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpcie__dev.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_pcie\_dev\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpcie__dev.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a7cc2f61e85b1d9c4985115b91fc6e832"></a>

```c
pcie_bdf_t bdf
```

相关声明：[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bdf](#a7cc2f61e85b1d9c4985115b91fc6e832)。

<a id="r_a5709ef678d9e81d4d3a61f6c26371076"></a>

```c
pcie_id_t id
```

相关声明：[pcie_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga30840d0e312e35f00790660193fd4c04)、[id](#a5709ef678d9e81d4d3a61f6c26371076)。

<a id="r_abedf281cdce4961dd02abba849747f45"></a>

```c
uint32_t class_rev
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[class_rev](#abedf281cdce4961dd02abba849747f45)。

<a id="r_a798e25696997a74ed01f8df6cec64489"></a>

```c
uint32_t class_rev_mask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[class_rev_mask](#a798e25696997a74ed01f8df6cec64489)。

## 28.2\_详细说明（Detailed Documentation）

<a id="a7cc2f61e85b1d9c4985115b91fc6e832"></a>

### `bdf`

```c
pcie_bdf_t pcie_dev::bdf
```

<a id="abedf281cdce4961dd02abba849747f45"></a>

### `class_rev`

```c
uint32_t pcie_dev::class_rev
```

<a id="a798e25696997a74ed01f8df6cec64489"></a>

### `class_rev_mask`

```c
uint32_t pcie_dev::class_rev_mask
```

<a id="a5709ef678d9e81d4d3a61f6c26371076"></a>

### `id`

```c
pcie_id_t pcie_dev::id
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/pcie/pcie.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h_source.html)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [pcie_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga30840d0e312e35f00790660193fd4c04)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_pcie_ctrl_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_pcie_ep_driver_api_结构体.md)
