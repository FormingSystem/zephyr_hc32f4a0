---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-12
title: gnss_info_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgnss__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_gnss\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgnss__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全球导航卫星系统（GNSS）的信息数据结构。

```c
#include <zephyr/drivers/gnss.h>
```

<a id="details"></a>

全球导航卫星系统（GNSS）的信息数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a81160955c4b9d3a746280d88a74f07eb"></a>

```c
uint16_t satellites_cnt
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[satellites_cnt](#a81160955c4b9d3a746280d88a74f07eb)。

正在跟踪的卫星数量。

<a id="r_a5de15dd2a9843c05b8805d4519b49a73"></a>

```c
uint32_t hdop
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[hdop](#a5de15dd2a9843c05b8805d4519b49a73)。

水平精度因子（Horizontal Dilution of Precision，HDOP），单位为 1/1000。

<a id="r_a5f87d86da1ea290fb3951fab1f95459d"></a>

```c
int32_t geoid_separation
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[geoid_separation](#a5f87d86da1ea290fb3951fab1f95459d)。

大地水准面分离高度（Geoid separation），单位为毫米。

<a id="r_a718e95833c4d07ad530669035ca21f8c"></a>

```c
enum gnss_fix_status fix_status
```

相关声明：[gnss_fix_status](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga15536308e2229a45493d06e8b61e63d9)、[fix_status](#a718e95833c4d07ad530669035ca21f8c)。

定位状态（fix status）。

<a id="r_a54396dd23fd05185bcb1104ee529984e"></a>

```c
enum gnss_fix_quality fix_quality
```

相关声明：[gnss_fix_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gacf5a3464c487ae7609d526c73ccc758a)、[fix_quality](#a54396dd23fd05185bcb1104ee529984e)。

定位质量（fix quality）。

## 12.2\_详细说明（Detailed Documentation）

<a id="a54396dd23fd05185bcb1104ee529984e"></a>

### `fix_quality`

```c
enum gnss_fix_quality gnss_info::fix_quality
```

定位质量（fix quality）。

<a id="a718e95833c4d07ad530669035ca21f8c"></a>

### `fix_status`

```c
enum gnss_fix_status gnss_info::fix_status
```

定位状态（fix status）。

<a id="a5f87d86da1ea290fb3951fab1f95459d"></a>

### `geoid_separation`

```c
int32_t gnss_info::geoid_separation
```

大地水准面分离高度（Geoid separation），单位为毫米。

<a id="a5de15dd2a9843c05b8805d4519b49a73"></a>

### `hdop`

```c
uint32_t gnss_info::hdop
```

水平精度因子（Horizontal Dilution of Precision，HDOP），单位为 1/1000。

<a id="a81160955c4b9d3a746280d88a74f07eb"></a>

### `satellites_cnt`

```c
uint16_t gnss_info::satellites_cnt
```

正在跟踪的卫星数量。

本数据类型文档由以下文件生成：

- `zephyr/drivers/gnss.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/drivers/gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [gnss_fix_status](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga15536308e2229a45493d06e8b61e63d9)
- [gnss_fix_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gacf5a3464c487ae7609d526c73ccc758a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_gnss_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_gnss_rtk_data_结构体.md)
