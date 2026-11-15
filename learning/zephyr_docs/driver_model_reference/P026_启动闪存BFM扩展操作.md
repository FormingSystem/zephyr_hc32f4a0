---
id: learning.zephyr-docs.driver-model-reference.page-26
title: 启动闪存BFM扩展操作
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbfm__exop.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_启动闪存BFM扩展操作

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbfm__exop.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

启动闪存（Boot Flash Memory，BFM）扩展操作参数。

```c
#include <zephyr/drivers/flash/mchp_nvmctrl_g3.h>
```

<a id="details"></a>

启动闪存（Boot Flash Memory，BFM）扩展操作参数。此结构体包含对启动闪存执行扩展操作所需的参数，例如配置写保护和选择启动存储体（Boot Bank）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_a2c16d2c160205b3eaba14b9f0ecb8c37"></a>

```c
enum boot_flash_bank boot_bank
```

相关声明：[boot_flash_bank](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gae4ce42c1991f6edf715e4aa2b294234b)、[boot_bank](#a2c16d2c160205b3eaba14b9f0ecb8c37)。

启动闪存存储体／分区（Bank/Panel）选择。

<a id="r_a2b390a2ae33a5690850b95df7b5f8e7d"></a>

```c
uint32_t wp_page
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[wp_page](#a2b390a2ae33a5690850b95df7b5f8e7d)。

写保护页配置（Write Protection Page Configuration）。

## 26.2\_详细说明（Detailed Documentation）

<a id="a2c16d2c160205b3eaba14b9f0ecb8c37"></a>

### `boot_bank`

```c
enum boot_flash_bank bfm_exop::boot_bank
```

启动闪存存储体／分区（Bank/Panel）选择。

<a id="a2b390a2ae33a5690850b95df7b5f8e7d"></a>

### `wp_page`

```c
uint32_t bfm_exop::wp_page
```

写保护页配置（Write Protection Page Configuration）。

本结构体文档由以下文件生成：

- `zephyr/drivers/flash/mchp_nvmctrl_g3.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/drivers/flash/mchp_nvmctrl_g3.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g3_8h_source.html)
- [boot_flash_bank](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gae4ce42c1991f6edf715e4aa2b294234b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_BC12伙伴状态.md) · [返回大纲](大纲.md) · [下一章](P027_生物识别能力.md)
