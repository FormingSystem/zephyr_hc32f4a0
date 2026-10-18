---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-86
title: sdio_func_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsdio__func.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_sdio\_func\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsdio__func.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SDIO功能（Function）的定义。

```c
#include <zephyr/sd/sd.h>
```

<a id="details"></a>

SDIO 功能定义（Function definition）。用于分别存储每个 SDIO 功能的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 86.1\_数据成员（Data Fields）

<a id="r_a3bc320f1ca7268344b848a998ace615c"></a>

```c
enum sdio_func_num num
```

相关声明：[sdio_func_num](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a3a542344967c5c1912bde216559e7cd6)、[num](#a3bc320f1ca7268344b848a998ace615c)。

功能编号（Function number）。

<a id="r_a7387979362ba892c013a7a69e004d96b"></a>

```c
struct sd_card * card
```

相关声明：[sd_card](P074_sd_card_结构体.md)、[card](#a7387979362ba892c013a7a69e004d96b)。

此功能所在的卡。

<a id="r_af83e71e628841b8acf70130261a97060"></a>

```c
struct sdio_cis cis
```

相关声明：[sdio_cis](P085_sdio_cis_结构体.md)、[cis](#af83e71e628841b8acf70130261a97060)。

此功能的 CIS 元组数据。

<a id="r_aa4ad13eb77f656020b38f6cf165e2965"></a>

```c
uint16_t block_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[block_size](#aa4ad13eb77f656020b38f6cf165e2965)。

此功能当前的块大小。

## 86.2\_详细说明（Detailed Documentation）

<a id="aa4ad13eb77f656020b38f6cf165e2965"></a>

### `block_size`

```c
uint16_t sdio_func::block_size
```

此功能当前的块大小。

<a id="a7387979362ba892c013a7a69e004d96b"></a>

### `card`

```c
struct sd_card* sdio_func::card
```

此功能所在的卡。

<a id="af83e71e628841b8acf70130261a97060"></a>

### `cis`

```c
struct sdio_cis sdio_func::cis
```

此功能的 CIS 元组数据。

<a id="a3bc320f1ca7268344b848a998ace615c"></a>

### `num`

```c
enum sdio_func_num sdio_func::num
```

功能编号（Function number）。

本数据类型文档由以下文件生成：

- `zephyr/sd/sd.h`

## 86.3\_原页交叉引用（Cross References）

- [zephyr/sd/sd.h](https://docs.zephyrproject.org/latest/doxygen/html/sd_8h_source.html)
- [sdio_func_num](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a3a542344967c5c1912bde216559e7cd6)
- [sd_card](P074_sd_card_结构体.md)
- [sdio_cis](P085_sdio_cis_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P085_sdio_cis_结构体.md) · [返回大纲](大纲.md) · [下一章](P087_sent_driver_api_结构体.md)
