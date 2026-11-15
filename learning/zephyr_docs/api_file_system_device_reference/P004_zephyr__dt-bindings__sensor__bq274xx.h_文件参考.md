---
id: learning.zephyr-docs.api-file-system-device-reference.page-4
title: zephyr__dt-bindings__sensor__bq274xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bq274xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_sensor\_\_bq274xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bq274xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the TI BQ274xx fuel gauges的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the TI BQ274xx fuel gauges的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="define-members-0"></a>

### BQ27427 化学特性标识符（chemistry IDs）

设备树 `chemistry-id` 属性的取值。

<a id="r_gafd885c85ac533a7640f93e97fec8ccb9"></a>

```c
#define BQ27427_CHEM_ID_A 0x3230
```

相关声明：[BQ27427_CHEM_ID_A](../api_device_topic_reference/P003_BQ274XX API主题.md#gafd885c85ac533a7640f93e97fec8ccb9)。

电池化学特性配置 A（Chemistry profile A），4.35 V。

<a id="r_gaafd294ad5ecf988c816ed258e61fa781"></a>

```c
#define BQ27427_CHEM_ID_B 0x1202
```

相关声明：[BQ27427_CHEM_ID_B](../api_device_topic_reference/P003_BQ274XX API主题.md#gaafd294ad5ecf988c816ed258e61fa781)。

电池化学特性配置 B（Chemistry profile B），4.2 V，默认配置。

<a id="r_gac932a2d227876901d5a001a46b0aba07"></a>

```c
#define BQ27427_CHEM_ID_C 0x3142
```

相关声明：[BQ27427_CHEM_ID_C](../api_device_topic_reference/P003_BQ274XX API主题.md#gac932a2d227876901d5a001a46b0aba07)。

电池化学特性配置 C（Chemistry profile C），4.4 V。

<a id="define-members-1"></a>

### BQ27421 化学特性标识符（chemistry IDs）

设备树 `chemistry-id` 属性的取值。

<a id="r_ga8f812e864a406e7ac743bedeecc9ddf3"></a>

```c
#define BQ27421_G1A_CHEM_ID 0x0128
```

相关声明：[BQ27421_G1A_CHEM_ID](../api_device_topic_reference/P003_BQ274XX API主题.md#ga8f812e864a406e7ac743bedeecc9ddf3)。

BQ27421-G1A 的化学特性标识符（chemistry ID）。

<a id="r_gaf337b60f20d3c986c353293596d7c2f6"></a>

```c
#define BQ27421_G1B_CHEM_ID 0x0312
```

相关声明：[BQ27421_G1B_CHEM_ID](../api_device_topic_reference/P003_BQ274XX API主题.md#gaf337b60f20d3c986c353293596d7c2f6)。

BQ27421-G1B 的化学特性标识符（chemistry ID）。

<a id="r_ga3f58b290a4556f6a74da8b4759262fc0"></a>

```c
#define BQ27421_G1D_CHEM_ID 0x3142
```

相关声明：[BQ27421_G1D_CHEM_ID](../api_device_topic_reference/P003_BQ274XX API主题.md#ga3f58b290a4556f6a74da8b4759262fc0)。

BQ27421-G1D 的化学特性标识符（chemistry ID）。


## 4.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P021_bq274xx.h_源码浏览.md)
- [BQ27427_CHEM_ID_A](../api_device_topic_reference/P003_BQ274XX API主题.md#gafd885c85ac533a7640f93e97fec8ccb9)
- [BQ27427_CHEM_ID_B](../api_device_topic_reference/P003_BQ274XX API主题.md#gaafd294ad5ecf988c816ed258e61fa781)
- [BQ27427_CHEM_ID_C](../api_device_topic_reference/P003_BQ274XX API主题.md#gac932a2d227876901d5a001a46b0aba07)
- [BQ27421_G1A_CHEM_ID](../api_device_topic_reference/P003_BQ274XX API主题.md#ga8f812e864a406e7ac743bedeecc9ddf3)
- [BQ27421_G1B_CHEM_ID](../api_device_topic_reference/P003_BQ274XX API主题.md#gaf337b60f20d3c986c353293596d7c2f6)
- [BQ27421_G1D_CHEM_ID](../api_device_topic_reference/P003_BQ274XX API主题.md#ga3f58b290a4556f6a74da8b4759262fc0)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__firmware__scmi__base.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__drivers__clock_control__clock_control_bflb_common.h_文件参考.md)
