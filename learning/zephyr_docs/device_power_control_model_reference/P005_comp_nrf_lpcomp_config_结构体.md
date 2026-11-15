---
id: learning.zephyr-docs.device-power-control-model-reference.page-5
title: comp_nrf_lpcomp_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcomp__nrf__lpcomp__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_comp\_nrf\_lpcomp\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcomp__nrf__lpcomp__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配置结构（Configuration Structure）。

```c
#include <zephyr/drivers/comparator/nrf_lpcomp.h>
```

<a id="details"></a>

配置结构体（Configuration structure）。注意：只有 `refsel == COMP_NRF_LPCOMP_REFSEL_AREF` 时才使用 `extrefsel`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a6145079376220c7fc3914e208bee819f"></a>

```c
uint8_t psel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[psel](#a6145079376220c7fc3914e208bee819f)。

正输入选择，由 `NRF_COMP_AIN` 定义。

<a id="r_a21b862cc82704353d269cb81b0c71a42"></a>

```c
uint8_t extrefsel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[extrefsel](#a21b862cc82704353d269cb81b0c71a42)。

外部参考输入选择，由 `NRF_COMP_AIN` 定义。

<a id="r_ad1022de6c772909a4f8c3d90e0748fe7"></a>

```c
enum comp_nrf_lpcomp_refsel refsel
```

相关声明：[comp_nrf_lpcomp_refsel](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04)、[refsel](#ad1022de6c772909a4f8c3d90e0748fe7)。

参考源选择（Reference selection）。

<a id="r_ac561f00056c9faabb61a4a67b628f963"></a>

```c
bool enable_hyst
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable_hyst](#ac561f00056c9faabb61a4a67b628f963)。

迟滞（Hysteresis）配置。

## 5.2\_详细说明（Detailed Documentation）

<a id="ac561f00056c9faabb61a4a67b628f963"></a>

### `enable_hyst`

```c
bool comp_nrf_lpcomp_config::enable_hyst
```

迟滞（Hysteresis）配置。

<a id="a21b862cc82704353d269cb81b0c71a42"></a>

### `extrefsel`

```c
uint8_t comp_nrf_lpcomp_config::extrefsel
```

外部参考输入选择，由 `NRF_COMP_AIN` 定义。

<a id="a6145079376220c7fc3914e208bee819f"></a>

### `psel`

```c
uint8_t comp_nrf_lpcomp_config::psel
```

正输入选择，由 `NRF_COMP_AIN` 定义。

<a id="ad1022de6c772909a4f8c3d90e0748fe7"></a>

### `refsel`

```c
enum comp_nrf_lpcomp_refsel comp_nrf_lpcomp_config::refsel
```

参考源选择（Reference selection）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/comparator/nrf_lpcomp.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/drivers/comparator/nrf_lpcomp.h](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [comp_nrf_lpcomp_refsel](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_comp_nrf_comp_se_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_dtc_transfer_status_结构体.md)
