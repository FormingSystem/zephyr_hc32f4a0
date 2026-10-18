---
id: learning.zephyr-docs.system-service-model-reference.page-29
title: flash_img_context_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__img__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_flash\_img\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__img__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dfu/flash_img.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_a80fb0afaa391d3242c7de9ffe0f10675"></a>

```c
uint8_t buf [CONFIG_IMG_BLOCK_BUF_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#a80fb0afaa391d3242c7de9ffe0f10675)。

<a id="r_ae98e6408fe707543f30094f89ae43bdd"></a>

```c
const struct flash_area * flash_area
```

相关声明：[flash_area](P027_flash_area_结构体.md)、[flash_area](#ae98e6408fe707543f30094f89ae43bdd)。

<a id="r_a9bdb531f92f32957ab78e6cfcced6a3b"></a>

```c
struct stream_flash_ctx stream
```

相关声明：[stream_flash_ctx](../stream_flash_reference/P003_流式Flash上下文.md)、[stream](#a9bdb531f92f32957ab78e6cfcced6a3b)。

## 29.2\_详细说明（Detailed Documentation）

<a id="a80fb0afaa391d3242c7de9ffe0f10675"></a>

### `buf`

```c
uint8_t flash_img_context::buf[CONFIG_IMG_BLOCK_BUF_SIZE]
```

<a id="ae98e6408fe707543f30094f89ae43bdd"></a>

### `flash_area`

```c
const struct flash_area* flash_img_context::flash_area
```

<a id="a9bdb531f92f32957ab78e6cfcced6a3b"></a>

### `stream`

```c
struct stream_flash_ctx flash_img_context::stream
```

本数据类型文档由以下文件生成：

- `zephyr/dfu/flash_img.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/dfu/flash_img.h](https://docs.zephyrproject.org/latest/doxygen/html/flash__img_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flash_area](P027_flash_area_结构体.md)
- [stream_flash_ctx](../stream_flash_reference/P003_流式Flash上下文.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_flash_img_check_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_flash_it51xxx_ex_op_addr_protection_结构体.md)
