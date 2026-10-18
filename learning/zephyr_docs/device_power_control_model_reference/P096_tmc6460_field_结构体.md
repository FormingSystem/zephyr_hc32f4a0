---
id: learning.zephyr-docs.device-power-control-model-reference.page-96
title: tmc6460_field_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtmc6460__field.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_tmc6460\_field\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtmc6460__field.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述TMC6460寄存器中的位域（Bitfield）。

```c
#include <zephyr/drivers/misc/tmc6460/tmc6460.h>
```

<a id="details"></a>

描述TMC6460寄存器中的位域（Bitfield）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 96.1\_数据成员（Data Fields）

<a id="r_a45409216cb19a1a671d3b9a856882cba"></a>

```c
uint32_t mask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mask](#a45409216cb19a1a671d3b9a856882cba)。

选择寄存器内字段的位掩码。

<a id="r_a8018f232a7005ad27f05975bfee3ebcc"></a>

```c
uint8_t shift
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[shift](#a8018f232a7005ad27f05975bfee3ebcc)。

字段最低有效位（LSB）的位位置。

<a id="r_a929160c1ccba4518e27ea796184a4927"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#a929160c1ccba4518e27ea796184a4927)。

包含此字段的 16 位寄存器地址。

<a id="r_a052e6d4dd7c574b732e0370dc22d420d"></a>

```c
bool is_signed
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_signed](#a052e6d4dd7c574b732e0370dc22d420d)。

若字段保存二进制补码（Two's-complement）有符号值，则为 `true`。

## 96.2\_详细说明（Detailed Documentation）

<a id="a929160c1ccba4518e27ea796184a4927"></a>

### `addr`

```c
uint16_t tmc6460_field::addr
```

包含此字段的 16 位寄存器地址。

<a id="a052e6d4dd7c574b732e0370dc22d420d"></a>

### `is_signed`

```c
bool tmc6460_field::is_signed
```

若字段保存二进制补码（Two's-complement）有符号值，则为 `true`。

<a id="a45409216cb19a1a671d3b9a856882cba"></a>

### `mask`

```c
uint32_t tmc6460_field::mask
```

选择寄存器内字段的位掩码。

<a id="a8018f232a7005ad27f05975bfee3ebcc"></a>

### `shift`

```c
uint8_t tmc6460_field::shift
```

字段最低有效位（LSB）的位位置。

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/tmc6460/tmc6460.h`

## 96.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/tmc6460/tmc6460.h](https://docs.zephyrproject.org/latest/doxygen/html/tmc6460_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P095_tcpci_reg_dump_map_结构体.md) · [返回大纲](大纲.md) · [下一章](P097_usb_hub_descriptor_结构体.md)
