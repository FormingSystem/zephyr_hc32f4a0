---
id: learning.zephyr-docs.system-service-model-reference.page-30
title: flash_it51xxx_ex_op_addr_protection_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__it51xxx__ex__op__addr__protection.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_flash\_it51xxx\_ex\_op\_addr\_protection\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__it51xxx__ex__op__addr__protection.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

闪存地址保护（Flash Address Protection）的请求/结果。

```c
#include <zephyr/drivers/flash/it51xxx_flash_api_ex.h>
```

<a id="details"></a>

闪存地址保护（Flash Address Protection）的请求/结果。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a05615f4f616b2d03d8218311faf9b57c"></a>

```c
uint32_t addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[addr](#a05615f4f616b2d03d8218311faf9b57c)。

保护区域的起始地址。

<a id="r_aeb261e12e2276ab42fe76d4a7803a3bb"></a>

```c
size_t size
```

相关声明：[size](#aeb261e12e2276ab42fe76d4a7803a3bb)。

保护区域大小，单位为字节。

<a id="r_ac74e0e265856f6da0c8c76cae1e195aa"></a>

```c
uint8_t path
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[path](#ac74e0e265856f6da0c8c76cae1e195aa)。

保护路径位图（protection path bitmap），参见 `PROTECT_PATH_*`。

<a id="r_af5f3e6d03547d30e1f0b922319803b06"></a>

```c
bool is_protected
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_protected](#af5f3e6d03547d30e1f0b922319803b06)。

指定区域的保护状态。

## 30.2\_详细说明（Detailed Documentation）

<a id="a05615f4f616b2d03d8218311faf9b57c"></a>

### `addr`

```c
uint32_t flash_it51xxx_ex_op_addr_protection::addr
```

保护区域的起始地址。

<a id="af5f3e6d03547d30e1f0b922319803b06"></a>

### `is_protected`

```c
bool flash_it51xxx_ex_op_addr_protection::is_protected
```

指定区域的保护状态。

<a id="ac74e0e265856f6da0c8c76cae1e195aa"></a>

### `path`

```c
uint8_t flash_it51xxx_ex_op_addr_protection::path
```

保护路径位图（protection path bitmap），参见 `PROTECT_PATH_*`。

<a id="aeb261e12e2276ab42fe76d4a7803a3bb"></a>

### `size`

```c
size_t flash_it51xxx_ex_op_addr_protection::size
```

保护区域大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/it51xxx_flash_api_ex.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/drivers/flash/it51xxx_flash_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__flash__api__ex_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_flash_img_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md)
