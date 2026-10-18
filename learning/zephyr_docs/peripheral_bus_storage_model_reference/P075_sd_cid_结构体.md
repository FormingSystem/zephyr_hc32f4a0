---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-75
title: sd_cid_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsd__cid.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_sd\_cid\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsd__cid.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD卡标识寄存器（Card Identification Register）。

```c
#include <zephyr/sd/sd_spec.h>
```

<a id="details"></a>

SD 卡标识寄存器（Card Identification register，CID）。描述 SD 卡标识寄存器的布局。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 75.1\_数据成员（Data Fields）

<a id="r_a7d97bc0f58c766abd2501d923e163d40"></a>

```c
uint8_t manufacturer
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[manufacturer](#a7d97bc0f58c766abd2501d923e163d40)。

制造商 ID（Manufacturer ID）`[127:120]`。

<a id="r_a11ec5fa23ae13ee084c093b27c1d381a"></a>

```c
uint16_t application
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[application](#a11ec5fa23ae13ee084c093b27c1d381a)。

OEM/应用 ID（OEM/Application ID）`[119:104]`。

<a id="r_a46f36abc3c2b1f3e9aa34c199d2bfcf3"></a>

```c
uint8_t name [5]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[name](#a46f36abc3c2b1f3e9aa34c199d2bfcf3)。

产品名称（Product name）`[103:64]`。

<a id="r_aba79f6a5bdf963772ac3c77ac209faf2"></a>

```c
uint8_t version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[version](#aba79f6a5bdf963772ac3c77ac209faf2)。

产品修订版本（Product revision）`[63:56]`。

<a id="r_ace04f0f28cb7e058e69fbbc643f66052"></a>

```c
uint32_t ser_num
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ser_num](#ace04f0f28cb7e058e69fbbc643f66052)。

产品序列号（Product serial number）`[55:24]`。

<a id="r_a50fbbc6844a1fde29a25a803ed9d0df7"></a>

```c
uint16_t date
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[date](#a50fbbc6844a1fde29a25a803ed9d0df7)。

制造日期（Manufacturing date）`[19:8]`。

## 75.2\_详细说明（Detailed Documentation）

<a id="a11ec5fa23ae13ee084c093b27c1d381a"></a>

### `application`

```c
uint16_t sd_cid::application
```

OEM/应用 ID（OEM/Application ID）`[119:104]`。

<a id="a50fbbc6844a1fde29a25a803ed9d0df7"></a>

### `date`

```c
uint16_t sd_cid::date
```

制造日期（Manufacturing date）`[19:8]`。

<a id="a7d97bc0f58c766abd2501d923e163d40"></a>

### `manufacturer`

```c
uint8_t sd_cid::manufacturer
```

制造商 ID（Manufacturer ID）`[127:120]`。

<a id="a46f36abc3c2b1f3e9aa34c199d2bfcf3"></a>

### `name`

```c
uint8_t sd_cid::name[5]
```

产品名称（Product name）`[103:64]`。

<a id="ace04f0f28cb7e058e69fbbc643f66052"></a>

### `ser_num`

```c
uint32_t sd_cid::ser_num
```

产品序列号（Product serial number）`[55:24]`。

<a id="aba79f6a5bdf963772ac3c77ac209faf2"></a>

### `version`

```c
uint8_t sd_cid::version
```

产品修订版本（Product revision）`[63:56]`。

本数据类型文档由以下文件生成：

- `zephyr/sd/sd_spec.h`

## 75.3\_原页交叉引用（Cross References）

- [zephyr/sd/sd_spec.h](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P074_sd_card_结构体.md) · [返回大纲](大纲.md) · [下一章](P076_sd_csd_结构体.md)
