---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-48
title: mspi_scramble_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__scramble__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_mspi\_scramble\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__scramble__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI控制器的扰码配置（Scramble Configuration）。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI控制器的扰码配置（Scramble Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_a362ce29f7748d28e818e2c809bd4cedd"></a>

```c
bool enable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable](#a362ce29f7748d28e818e2c809bd4cedd)。

是否启用扰码（Scrambling）。

<a id="r_adf56743768432f22f0a5090e1b823a67"></a>

```c
uint32_t address_offset
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[address_offset](#adf56743768432f22f0a5090e1b823a67)。

扰码区域起始地址 = 硬件默认地址 + 地址偏移量。

<a id="r_a8d6d5b47b3d777674b974a6c79337b43"></a>

```c
uint32_t size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[size](#a8d6d5b47b3d777674b974a6c79337b43)。

扰码区域大小。

## 48.2\_详细说明（Detailed Documentation）

<a id="adf56743768432f22f0a5090e1b823a67"></a>

### `address_offset`

```c
uint32_t mspi_scramble_cfg::address_offset
```

扰码区域起始地址 = 硬件默认地址 + 地址偏移量。

<a id="a362ce29f7748d28e818e2c809bd4cedd"></a>

### `enable`

```c
bool mspi_scramble_cfg::enable
```

是否启用扰码（Scrambling）。

<a id="a8d6d5b47b3d777674b974a6c79337b43"></a>

### `size`

```c
uint32_t mspi_scramble_cfg::size
```

扰码区域大小。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_mspi_memmap_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_mspi_timing_cfg_结构体.md)
