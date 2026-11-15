---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-17
title: espi_saf_packet_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__saf__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_espi\_saf\_packet\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__saf__packet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

eSPI从设备附属闪存（SAF）事务的数据包格式。

```c
#include <zephyr/drivers/espi_saf.h>
```

<a id="details"></a>

eSPI从设备附属闪存（SAF）事务的数据包格式。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a8ee8a45b3490746f893f6b17fb96b815"></a>

```c
uint32_t flash_addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flash_addr](#a8ee8a45b3490746f893f6b17fb96b815)。

<a id="r_a00bfcab9fe2b928be3ea3485c5e91401"></a>

```c
uint8_t * buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#a00bfcab9fe2b928be3ea3485c5e91401)。

<a id="r_af88017b76b64b77c95d9684981f48482"></a>

```c
uint32_t len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[len](#af88017b76b64b77c95d9684981f48482)。

## 17.2\_详细说明（Detailed Documentation）

<a id="a00bfcab9fe2b928be3ea3485c5e91401"></a>

### `buf`

```c
uint8_t* espi_saf_packet::buf
```

<a id="a8ee8a45b3490746f893f6b17fb96b815"></a>

### `flash_addr`

```c
uint32_t espi_saf_packet::flash_addr
```

<a id="af88017b76b64b77c95d9684981f48482"></a>

### `len`

```c
uint32_t espi_saf_packet::len
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi_saf.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi_saf.h](https://docs.zephyrproject.org/latest/doxygen/html/espi__saf_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_espi_saf_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_fpga_driver_api_结构体.md)
