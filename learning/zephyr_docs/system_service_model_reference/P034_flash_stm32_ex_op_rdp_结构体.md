---
id: learning.zephyr-docs.system-service-model-reference.page-34
title: flash_stm32_ex_op_rdp_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__stm32__ex__op__rdp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_flash\_stm32\_ex\_op\_rdp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__stm32__ex__op__rdp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FLASH_STM32_EX_OP_RDP操作的输入结构。

```c
#include <zephyr/drivers/flash/stm32_flash_api_extensions.h>
```

<a id="details"></a>

FLASH_STM32_EX_OP_RDP操作的输入结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a45454dfb14c59310c2549aca1e7b31b2"></a>

```c
bool enable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable](#a45454dfb14c59310c2549aca1e7b31b2)。

启用还是禁用读出保护（readout protection）。

<a id="r_aab59e61f810e1e33bd96261fb7f9668b"></a>

```c
bool permanent
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[permanent](#aab59e61f810e1e33bd96261fb7f9668b)。

是否将读出保护设为永久保护。

## 34.2\_详细说明（Detailed Documentation）

<a id="a45454dfb14c59310c2549aca1e7b31b2"></a>

### `enable`

```c
bool flash_stm32_ex_op_rdp::enable
```

启用还是禁用读出保护（readout protection）。

<a id="aab59e61f810e1e33bd96261fb7f9668b"></a>

### `permanent`

```c
bool flash_stm32_ex_op_rdp::permanent
```

是否将读出保护设为永久保护。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/stm32_flash_api_extensions.h`

## 34.3\_原页交叉引用（Cross References）

- [FLASH_STM32_EX_OP_RDP](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0)
- [zephyr/drivers/flash/stm32_flash_api_extensions.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__flash__api__extensions_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_flash_sector_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_flash_stm32_ex_op_sector_wp_in_结构体.md)
