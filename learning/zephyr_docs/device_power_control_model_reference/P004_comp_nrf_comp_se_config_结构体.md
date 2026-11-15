---
id: learning.zephyr-docs.device-power-control-model-reference.page-4
title: comp_nrf_comp_se_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcomp__nrf__comp__se__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_comp\_nrf\_comp\_se\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcomp__nrf__comp__se__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单端模式（Single-Ended Mode）的配置结构。

```c
#include <zephyr/drivers/comparator/nrf_comp.h>
```

<a id="details"></a>

单端模式（Single-ended mode）配置结构体。注意：只有 `refsel == COMP_NRF_COMP_REFSEL_AREF` 时才使用 `extrefsel`。迟滞下阈值（伏）`= ((th_down + 1) / 64) * ref`；迟滞上阈值（伏）`= ((th_up + 1) / 64) * ref`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a7faaf85605587ce3b3d1b9a7a3d062d6"></a>

```c
uint8_t psel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[psel](#a7faaf85605587ce3b3d1b9a7a3d062d6)。

正输入选择，由 `NRF_COMP_AIN` 定义。

<a id="r_a484cc2b4c38c7b5a8c05e87e560c7b5e"></a>

```c
enum comp_nrf_comp_sp_mode sp_mode
```

相关声明：[comp_nrf_comp_sp_mode](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#ad13baf7c262d5fb2321ea5140180b3b1)、[sp_mode](#a484cc2b4c38c7b5a8c05e87e560c7b5e)。

速度模式选择。

<a id="r_a3ffb95afd621727dedbc617e3072cfd9"></a>

```c
enum comp_nrf_comp_isource isource
```

相关声明：[comp_nrf_comp_isource](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a74444aeafb5a2bf633ffd706cc6b9010)、[isource](#a3ffb95afd621727dedbc617e3072cfd9)。

电流源（Current source）配置。

<a id="r_a486c261d0d13cc1feb4a2a60c5ea54f5"></a>

```c
uint8_t extrefsel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[extrefsel](#a486c261d0d13cc1feb4a2a60c5ea54f5)。

外部参考输入选择，由 `NRF_COMP_AIN` 定义。

<a id="r_a3a7c4e624cb7e34624732dbe4b5ab4f8"></a>

```c
enum comp_nrf_comp_refsel refsel
```

相关声明：[comp_nrf_comp_refsel](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a661d2e37c4acd5551b77e5bf2437b553)、[refsel](#a3a7c4e624cb7e34624732dbe4b5ab4f8)。

参考源选择（Reference selection）。

<a id="r_ad4c0e1711565c3bd05c08a6eaf593aad"></a>

```c
uint8_t th_down
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[th_down](#ad4c0e1711565c3bd05c08a6eaf593aad)。

迟滞下阈值配置。

<a id="r_a72dcaac8a0508b8859397b7926238112"></a>

```c
uint8_t th_up
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[th_up](#a72dcaac8a0508b8859397b7926238112)。

迟滞上阈值配置。

## 4.2\_详细说明（Detailed Documentation）

<a id="a486c261d0d13cc1feb4a2a60c5ea54f5"></a>

### `extrefsel`

```c
uint8_t comp_nrf_comp_se_config::extrefsel
```

外部参考输入选择，由 `NRF_COMP_AIN` 定义。

<a id="a3ffb95afd621727dedbc617e3072cfd9"></a>

### `isource`

```c
enum comp_nrf_comp_isource comp_nrf_comp_se_config::isource
```

电流源（Current source）配置。

<a id="a7faaf85605587ce3b3d1b9a7a3d062d6"></a>

### `psel`

```c
uint8_t comp_nrf_comp_se_config::psel
```

正输入选择，由 `NRF_COMP_AIN` 定义。

<a id="a3a7c4e624cb7e34624732dbe4b5ab4f8"></a>

### `refsel`

```c
enum comp_nrf_comp_refsel comp_nrf_comp_se_config::refsel
```

参考源选择（Reference selection）。

<a id="a484cc2b4c38c7b5a8c05e87e560c7b5e"></a>

### `sp_mode`

```c
enum comp_nrf_comp_sp_mode comp_nrf_comp_se_config::sp_mode
```

速度模式选择。

<a id="ad4c0e1711565c3bd05c08a6eaf593aad"></a>

### `th_down`

```c
uint8_t comp_nrf_comp_se_config::th_down
```

迟滞下阈值配置。

<a id="a72dcaac8a0508b8859397b7926238112"></a>

### `th_up`

```c
uint8_t comp_nrf_comp_se_config::th_up
```

迟滞上阈值配置。

本数据类型文档由以下文件生成：

- `zephyr/drivers/comparator/nrf_comp.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/drivers/comparator/nrf_comp.h](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [comp_nrf_comp_sp_mode](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#ad13baf7c262d5fb2321ea5140180b3b1)
- [comp_nrf_comp_isource](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a74444aeafb5a2bf633ffd706cc6b9010)
- [comp_nrf_comp_refsel](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a661d2e37c4acd5551b77e5bf2437b553)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_comp_nrf_comp_diff_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_comp_nrf_lpcomp_config_结构体.md)
