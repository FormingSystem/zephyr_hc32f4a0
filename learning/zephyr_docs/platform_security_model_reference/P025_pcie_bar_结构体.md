---
id: learning.zephyr-docs.platform-security-model-reference.page-25
title: pcie_bar_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpcie__bar.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_pcie\_bar\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpcie__bar.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a75ed340a7d80a6825f3c60469194dae8"></a>

```c
uintptr_t phys_addr
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[phys_addr](#a75ed340a7d80a6825f3c60469194dae8)。

<a id="r_ab68c921f2993c94d2ae65684568bf770"></a>

```c
size_t size
```

相关声明：[size](#ab68c921f2993c94d2ae65684568bf770)。

## 25.2\_详细说明（Detailed Documentation）

<a id="a75ed340a7d80a6825f3c60469194dae8"></a>

### `phys_addr`

```c
uintptr_t pcie_bar::phys_addr
```

<a id="ab68c921f2993c94d2ae65684568bf770"></a>

### `size`

```c
size_t pcie_bar::size
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/pcie/pcie.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h_source.html)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_otp_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_pcie_ctrl_config_结构体.md)
