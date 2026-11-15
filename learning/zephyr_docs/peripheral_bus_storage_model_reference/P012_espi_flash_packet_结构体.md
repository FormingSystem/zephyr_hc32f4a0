---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-12
title: espi_flash_packet_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__flash__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_espi\_flash\_packet\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__flash__packet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

eSPI闪存事务（Flash Transaction）的数据包格式。

```c
#include <zephyr/drivers/espi.h>
```

<a id="details"></a>

eSPI闪存事务（Flash Transaction）的数据包格式。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a22244bc4063618707eea571f170bdfde"></a>

```c
uint8_t * buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#a22244bc4063618707eea571f170bdfde)。

指向数据缓冲区的指针。

<a id="r_ac638c0b5d0d98e15ab66850afc394cec"></a>

```c
uint32_t flash_addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flash_addr](#ac638c0b5d0d98e15ab66850afc394cec)。

要访问的 Flash 地址。

<a id="r_adade51336ae37a519c06b12bf19fc86d"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#adade51336ae37a519c06b12bf19fc86d)。

对于读写操作，表示数据的字节数；对于擦除操作，表示扇区/块的大小。

## 12.2\_详细说明（Detailed Documentation）

<a id="a22244bc4063618707eea571f170bdfde"></a>

### `buf`

```c
uint8_t* espi_flash_packet::buf
```

指向数据缓冲区的指针。

<a id="ac638c0b5d0d98e15ab66850afc394cec"></a>

### `flash_addr`

```c
uint32_t espi_flash_packet::flash_addr
```

要访问的 Flash 地址。

<a id="adade51336ae37a519c06b12bf19fc86d"></a>

### `len`

```c
uint16_t espi_flash_packet::len
```

对于读写操作，表示数据的字节数；对于擦除操作，表示扇区/块的大小。

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi.h](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_espi_evt_data_pvt_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_espi_oob_packet_结构体.md)
