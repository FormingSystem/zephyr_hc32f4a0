---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-47
title: mspi_memmap_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__memmap__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_mspi\_memmap\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__memmap__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI控制器的内存映射配置（Memory Map Configuration）。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI控制器的内存映射配置（Memory Map Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_ac7ded0cfb89863d88672c112a32fa136"></a>

```c
bool enable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable](#ac7ded0cfb89863d88672c112a32fa136)。

是否启用内存映射（Memory map）。

<a id="r_a7736a88d44b6fa3b30373b12ebad4100"></a>

```c
uint32_t address_offset
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[address_offset](#a7736a88d44b6fa3b30373b12ebad4100)。

内存映射区域起始地址 = 硬件默认地址 + 地址偏移量。

<a id="r_a3ac0e8a0ee3ee9936f25c3a1a2fdfa19"></a>

```c
uint32_t size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[size](#a3ac0e8a0ee3ee9936f25c3a1a2fdfa19)。

内存映射区域大小。

<a id="r_a9a1309b447dbc47473436df6b66f9ef3"></a>

```c
enum mspi_memmap_permit permission
```

相关声明：[mspi_memmap_permit](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gac127ef78c7b66c7eebe03782abf08c40)、[permission](#a9a1309b447dbc47473436df6b66f9ef3)。

内存映射访问权限。

## 47.2\_详细说明（Detailed Documentation）

<a id="a7736a88d44b6fa3b30373b12ebad4100"></a>

### `address_offset`

```c
uint32_t mspi_memmap_cfg::address_offset
```

内存映射区域起始地址 = 硬件默认地址 + 地址偏移量。

<a id="ac7ded0cfb89863d88672c112a32fa136"></a>

### `enable`

```c
bool mspi_memmap_cfg::enable
```

是否启用内存映射（Memory map）。

<a id="a9a1309b447dbc47473436df6b66f9ef3"></a>

### `permission`

```c
enum mspi_memmap_permit mspi_memmap_cfg::permission
```

内存映射访问权限。

<a id="a3ac0e8a0ee3ee9936f25c3a1a2fdfa19"></a>

### `size`

```c
uint32_t mspi_memmap_cfg::size
```

内存映射区域大小。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mspi_memmap_permit](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gac127ef78c7b66c7eebe03782abf08c40)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_mspi_event_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_mspi_scramble_cfg_结构体.md)
