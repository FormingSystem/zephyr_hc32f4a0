---
id: learning.zephyr-docs.device-power-control-model-reference.page-3
title: comp_nrf_comp_diff_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcomp__nrf__comp__diff__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_comp\_nrf\_comp\_diff\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcomp__nrf__comp__diff__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

差分模式（Differential Mode）的配置结构。

```c
#include <zephyr/drivers/comparator/nrf_comp.h>
```

<a id="details"></a>

差分模式（Differential Mode）的配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a32e78a6a82b1baba4d77c2737c2db069"></a>

```c
uint8_t psel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[psel](#a32e78a6a82b1baba4d77c2737c2db069)。

正输入选择，由 `NRF_COMP_AIN` 定义。

<a id="r_a9a9b95f993a1a193292eb940c0550e1f"></a>

```c
enum comp_nrf_comp_sp_mode sp_mode
```

相关声明：[comp_nrf_comp_sp_mode](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#ad13baf7c262d5fb2321ea5140180b3b1)、[sp_mode](#a9a9b95f993a1a193292eb940c0550e1f)。

速度模式选择。

<a id="r_ac1aada8c9bceab130cd6ffdf294ce52f"></a>

```c
enum comp_nrf_comp_isource isource
```

相关声明：[comp_nrf_comp_isource](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a74444aeafb5a2bf633ffd706cc6b9010)、[isource](#ac1aada8c9bceab130cd6ffdf294ce52f)。

电流源（Current source）配置。

<a id="r_ac80eeeca2f685ddb2f2a97af18f9515b"></a>

```c
uint8_t extrefsel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[extrefsel](#ac80eeeca2f685ddb2f2a97af18f9515b)。

负输入选择，由 `NRF_COMP_AIN` 定义。

<a id="r_ae597d46f83c77923541e73cf254bc4ee"></a>

```c
bool enable_hyst
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable_hyst](#ae597d46f83c77923541e73cf254bc4ee)。

迟滞（Hysteresis）配置。

## 3.2\_详细说明（Detailed Documentation）

<a id="ae597d46f83c77923541e73cf254bc4ee"></a>

### `enable_hyst`

```c
bool comp_nrf_comp_diff_config::enable_hyst
```

迟滞（Hysteresis）配置。

<a id="ac80eeeca2f685ddb2f2a97af18f9515b"></a>

### `extrefsel`

```c
uint8_t comp_nrf_comp_diff_config::extrefsel
```

负输入选择，由 `NRF_COMP_AIN` 定义。

<a id="ac1aada8c9bceab130cd6ffdf294ce52f"></a>

### `isource`

```c
enum comp_nrf_comp_isource comp_nrf_comp_diff_config::isource
```

电流源（Current source）配置。

<a id="a32e78a6a82b1baba4d77c2737c2db069"></a>

### `psel`

```c
uint8_t comp_nrf_comp_diff_config::psel
```

正输入选择，由 `NRF_COMP_AIN` 定义。

<a id="a9a9b95f993a1a193292eb940c0550e1f"></a>

### `sp_mode`

```c
enum comp_nrf_comp_sp_mode comp_nrf_comp_diff_config::sp_mode
```

速度模式选择。

本数据类型文档由以下文件生成：

- `zephyr/drivers/comparator/nrf_comp.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/drivers/comparator/nrf_comp.h](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [comp_nrf_comp_sp_mode](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#ad13baf7c262d5fb2321ea5140180b3b1)
- [comp_nrf_comp_isource](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a74444aeafb5a2bf633ffd706cc6b9010)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_charger_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_comp_nrf_comp_se_config_结构体.md)
