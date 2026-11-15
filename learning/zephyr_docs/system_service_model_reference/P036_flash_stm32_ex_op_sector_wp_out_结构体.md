---
id: learning.zephyr-docs.system-service-model-reference.page-36
title: flash_stm32_ex_op_sector_wp_out_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__stm32__ex__op__sector__wp__out.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_flash\_stm32\_ex\_op\_sector\_wp\_out\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__stm32__ex__op__sector__wp__out.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FLASH_STM32_EX_OP_SECTOR_WP操作的输出结构。

```c
#include <zephyr/drivers/flash/stm32_flash_api_extensions.h>
```

<a id="details"></a>

FLASH_STM32_EX_OP_SECTOR_WP操作的输出结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_a5260c9c8f92f88563845e863365b4ae2"></a>

```c
uint64_t protected_mask
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[protected_mask](#a5260c9c8f92f88563845e863365b4ae2)。

已受保护扇区的掩码。

## 36.2\_详细说明（Detailed Documentation）

<a id="a5260c9c8f92f88563845e863365b4ae2"></a>

### `protected_mask`

```c
uint64_t flash_stm32_ex_op_sector_wp_out::protected_mask
```

已受保护扇区的掩码。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/stm32_flash_api_extensions.h`

## 36.3\_原页交叉引用（Cross References）

- [FLASH_STM32_EX_OP_SECTOR_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe)
- [zephyr/drivers/flash/stm32_flash_api_extensions.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__flash__api__extensions_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_flash_stm32_ex_op_sector_wp_in_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_fota_http_download_params_结构体.md)
