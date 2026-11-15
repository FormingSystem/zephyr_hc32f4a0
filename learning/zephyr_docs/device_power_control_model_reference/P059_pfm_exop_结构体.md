---
id: learning.zephyr-docs.device-power-control-model-reference.page-59
title: pfm_exop_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpfm__exop.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_pfm\_exop\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpfm__exop.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

程序闪存（Program Flash Memory，PFM）的扩展操作参数。

```c
#include <zephyr/drivers/flash/mchp_nvmctrl_g3.h>
```

<a id="details"></a>

程序 Flash 存储器（Program Flash Memory，PFM）的扩展操作参数。此结构体包含对 PFM 区域执行扩展操作所需的参数，例如配置写保护区域。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_ae724956923f6d97a5c1bc7064dd94de1"></a>

```c
enum pfm_wp_region region
```

相关声明：[pfm_wp_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ga68310865b2b4ef28fe8259b0d625bc56)、[region](#ae724956923f6d97a5c1bc7064dd94de1)。

写保护区域选择器（Write protection region selector）。

<a id="r_aaf55812dbc58f2f97b97122efc8390dd"></a>

```c
uint32_t base_addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[base_addr](#aaf55812dbc58f2f97b97122efc8390dd)。

写保护区域的基地址。

<a id="r_af86d62884866a07344bf0a1e11022d06"></a>

```c
uint32_t region_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[region_size](#af86d62884866a07344bf0a1e11022d06)。

写保护区域的大小，单位为字节。

<a id="r_af498df4d30381eb4ee74380e9c2f2639"></a>

```c
bool mirror_enable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[mirror_enable](#af498df4d30381eb4ee74380e9c2f2639)。

为此区域启用镜像（Mirroring）。

## 59.2\_详细说明（Detailed Documentation）

<a id="aaf55812dbc58f2f97b97122efc8390dd"></a>

### `base_addr`

```c
uint32_t pfm_exop::base_addr
```

写保护区域的基地址。

<a id="af498df4d30381eb4ee74380e9c2f2639"></a>

### `mirror_enable`

```c
bool pfm_exop::mirror_enable
```

为此区域启用镜像（Mirroring）。

<a id="ae724956923f6d97a5c1bc7064dd94de1"></a>

### `region`

```c
enum pfm_wp_region pfm_exop::region
```

写保护区域选择器（Write protection region selector）。

<a id="af86d62884866a07344bf0a1e11022d06"></a>

### `region_size`

```c
uint32_t pfm_exop::region_size
```

写保护区域的大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/mchp_nvmctrl_g3.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/drivers/flash/mchp_nvmctrl_g3.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g3_8h_source.html)
- [pfm_wp_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ga68310865b2b4ef28fe8259b0d625bc56)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_pfc_drive_reg_field_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_pinctrl_soc_pin_结构体.md)
