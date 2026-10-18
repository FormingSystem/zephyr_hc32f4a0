---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-17
title: gnss_time_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgnss__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_gnss\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgnss__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全球导航卫星系统（GNSS）的时间数据结构。

```c
#include <zephyr/drivers/gnss.h>
```

<a id="details"></a>

全球导航卫星系统（GNSS）的时间数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a5c8a280736741d8d07dacba30d48ed6f"></a>

```c
uint8_t hour
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hour](#a5c8a280736741d8d07dacba30d48ed6f)。

小时，范围为 `[0, 23]`。

<a id="r_a3e8b96861e45cc2a6222961e92ab62f5"></a>

```c
uint8_t minute
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[minute](#a3e8b96861e45cc2a6222961e92ab62f5)。

分钟，范围为 `[0, 59]`。

<a id="r_a2ab6b41452491ec34966fda0ddbdd9da"></a>

```c
uint16_t millisecond
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[millisecond](#a2ab6b41452491ec34966fda0ddbdd9da)。

毫秒，范围为 `[0, 60999]`。

<a id="r_a766744149009588f83cca930ef53ff10"></a>

```c
uint8_t month_day
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[month_day](#a766744149009588f83cca930ef53ff10)。

月内日期，范围为 `[1, 31]`。

<a id="r_a1c6730dc08cd3dfb48aee08154f5f2de"></a>

```c
uint8_t month
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[month](#a1c6730dc08cd3dfb48aee08154f5f2de)。

月份，范围为 `[1, 12]`。

<a id="r_a4daa514f38a7b7d88bf49cb5d664b2ac"></a>

```c
uint8_t century_year
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[century_year](#a4daa514f38a7b7d88bf49cb5d664b2ac)。

年份，范围为 `[0, 99]`。

## 17.2\_详细说明（Detailed Documentation）

<a id="a4daa514f38a7b7d88bf49cb5d664b2ac"></a>

### `century_year`

```c
uint8_t gnss_time::century_year
```

年份，范围为 `[0, 99]`。

<a id="a5c8a280736741d8d07dacba30d48ed6f"></a>

### `hour`

```c
uint8_t gnss_time::hour
```

小时，范围为 `[0, 23]`。

<a id="a2ab6b41452491ec34966fda0ddbdd9da"></a>

### `millisecond`

```c
uint16_t gnss_time::millisecond
```

毫秒，范围为 `[0, 60999]`。

<a id="a3e8b96861e45cc2a6222961e92ab62f5"></a>

### `minute`

```c
uint8_t gnss_time::minute
```

分钟，范围为 `[0, 59]`。

<a id="a1c6730dc08cd3dfb48aee08154f5f2de"></a>

### `month`

```c
uint8_t gnss_time::month
```

月份，范围为 `[1, 12]`。

<a id="a766744149009588f83cca930ef53ff10"></a>

### `month_day`

```c
uint8_t gnss_time::month_day
```

月内日期，范围为 `[1, 31]`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/gnss.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/drivers/gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_gnss_satellites_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_navigation_data_结构体.md)
