---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-14
title: espi_request_packet_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__request__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_espi\_request\_packet\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__request__packet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

eSPI外设请求（Peripheral Request）数据包。

```c
#include <zephyr/drivers/espi.h>
```

<a id="details"></a>

eSPI 外设请求包（Peripheral request packet）。定义外设通道（CH0）事务的格式，该通道用于内存、I/O 和消息周期（Cycles）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a9b474155dfa0c74d0bd55e4b831b383a"></a>

```c
enum espi_cycle_type cycle_type
```

相关声明：[espi_cycle_type](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga3e52615f244d7fa8ccda495ab8ec8a5b)、[cycle_type](#a9b474155dfa0c74d0bd55e4b831b383a)。

正在执行的 eSPI 周期类型。

<a id="r_a22a0111e338827125eaf79ce8516b744"></a>

```c
uint8_t tag
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tag](#a22a0111e338827125eaf79ce8516b744)。

用于跟踪的事务标签（Transaction tag）。

<a id="r_ae8b7dc12b04f469b5689ad27cc4f0643"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#ae8b7dc12b04f469b5689ad27cc4f0643)。

数据载荷的字节数。

<a id="r_a4ac2d50786fdc4c4bd8da88bde28f77d"></a>

```c
uint32_t address
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[address](#a4ac2d50786fdc4c4bd8da88bde28f77d)。

事务的目标地址。

<a id="r_a6f808763faf949ff7ef83d68fb71e7ba"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a6f808763faf949ff7ef83d68fb71e7ba)。

供读写操作使用的数据缓冲区指针。

## 14.2\_详细说明（Detailed Documentation）

<a id="a4ac2d50786fdc4c4bd8da88bde28f77d"></a>

### `address`

```c
uint32_t espi_request_packet::address
```

事务的目标地址。

<a id="a9b474155dfa0c74d0bd55e4b831b383a"></a>

### `cycle_type`

```c
enum espi_cycle_type espi_request_packet::cycle_type
```

正在执行的 eSPI 周期类型。

<a id="a6f808763faf949ff7ef83d68fb71e7ba"></a>

### `data`

```c
uint8_t* espi_request_packet::data
```

供读写操作使用的数据缓冲区指针。

<a id="ae8b7dc12b04f469b5689ad27cc4f0643"></a>

### `len`

```c
uint16_t espi_request_packet::len
```

数据载荷的字节数。

<a id="a22a0111e338827125eaf79ce8516b744"></a>

### `tag`

```c
uint8_t espi_request_packet::tag
```

用于跟踪的事务标签（Transaction tag）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi.h](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)
- [espi_cycle_type](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga3e52615f244d7fa8ccda495ab8ec8a5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_espi_oob_packet_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_espi_saf_cfg_结构体.md)
