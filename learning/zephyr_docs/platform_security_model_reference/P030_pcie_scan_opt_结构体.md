---
id: learning.zephyr-docs.platform-security-model-reference.page-30
title: pcie_scan_opt_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpcie__scan__opt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_pcie\_scan\_opt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpcie__scan__opt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

扫描PCI设备（PCI Devices）的选项。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="details"></a>

扫描PCI设备（PCI Devices）的选项。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a036225c7a5730ba2040e03cab491b9da"></a>

```c
uint8_t bus
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bus](#a036225c7a5730ba2040e03cab491b9da)。

开始扫描的总线编号。

<a id="r_a28ad6c4993eed7bdf08ce682692bf306"></a>

```c
pcie_scan_cb_t cb
```

相关声明：[pcie_scan_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga922580e4fb6200ef75425bb54801ceda)、[cb](#a28ad6c4993eed7bdf08ce682692bf306)。

每找到一个端点就调用的函数。

<a id="r_a11b39138d2a2b6b1e8e1bd80216a8da6"></a>

```c
void * cb_data
```

相关声明：[cb_data](#a11b39138d2a2b6b1e8e1bd80216a8da6)。

传给扫描回调的自定义数据。

<a id="r_a7e485fb824dea16f9d5fdcb7079ebb7e"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a7e485fb824dea16f9d5fdcb7079ebb7e)。

扫描标志。

<a id="r_af3b4de1e2cb9263ddcdc2849f5773be8"></a>

```c
bool(* scan_masking_fn )(pcie_bdf_t bdf)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[scan_masking_fn](#af3b4de1e2cb9263ddcdc2849f5773be8)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

用于判断总线/设备/功能号（BDF）是否被屏蔽的函数。

## 30.2\_详细说明（Detailed Documentation）

<a id="a036225c7a5730ba2040e03cab491b9da"></a>

### `bus`

```c
uint8_t pcie_scan_opt::bus
```

开始扫描的总线编号。

<a id="a28ad6c4993eed7bdf08ce682692bf306"></a>

### `cb`

```c
pcie_scan_cb_t pcie_scan_opt::cb
```

每找到一个端点就调用的函数。

<a id="a11b39138d2a2b6b1e8e1bd80216a8da6"></a>

### `cb_data`

```c
void* pcie_scan_opt::cb_data
```

传给扫描回调的自定义数据。

<a id="a7e485fb824dea16f9d5fdcb7079ebb7e"></a>

### `flags`

```c
uint32_t pcie_scan_opt::flags
```

扫描标志。

<a id="af3b4de1e2cb9263ddcdc2849f5773be8"></a>

### `scan_masking_fn`

```c
bool(* pcie_scan_opt::scan_masking_fn) (pcie_bdf_t bdf)
```

用于判断总线/设备/功能号（BDF）是否被屏蔽的函数。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pcie/pcie.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pcie_scan_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga922580e4fb6200ef75425bb54801ceda)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_pcie_ep_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_pcie_vctc_map_结构体.md)
