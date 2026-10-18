---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-18
title: navigation_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnavigation__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_navigation\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnavigation__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

导航数据结构（Navigation Data Structure）。

```c
#include <zephyr/data/navigation.h>
```

<a id="details"></a>

导航数据（Navigation data）结构体，描述一个点相对于某个球体（通常为地球）的瞬时导航信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a02d9f8cea5fe68810123bb2bf554d59c"></a>

```c
int64_t latitude
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[latitude](#a02d9f8cea5fe68810123bb2bf554d59c)。

纬度位置（Latitudinal position），单位为纳度（nanodegree），原文范围为 `0 to +-180E9`。

译注：官方原文对纬度也给出了上述范围；这里保留该表述，不将其视为常规地理纬度范围的更改。

<a id="r_a530eb9c4e3750bbb03b26256794d0914"></a>

```c
int64_t longitude
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[longitude](#a530eb9c4e3750bbb03b26256794d0914)。

经度位置（Longitudinal position），单位为纳度（nanodegree），范围按原文为 `0 to +-180E9`。

<a id="r_af9887a29823fc3e083dbd14d1f6cfce1"></a>

```c
uint32_t bearing
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bearing](#af9887a29823fc3e083dbd14d1f6cfce1)。

方位角（Bearing angle），单位为毫度（millidegree），范围为 0 至 `360E3`。

<a id="r_a5fd501c07c21e66217a7634d7d607d1d"></a>

```c
uint32_t speed
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[speed](#a5fd501c07c21e66217a7634d7d607d1d)。

速度，单位为毫米/秒。

<a id="r_addd80254be4619c4ea7707f9c9bc434e"></a>

```c
int32_t altitude
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[altitude](#addd80254be4619c4ea7707f9c9bc434e)。

相对于平均海平面（MSL）的高度，单位为毫米。

## 18.2\_详细说明（Detailed Documentation）

<a id="addd80254be4619c4ea7707f9c9bc434e"></a>

### `altitude`

```c
int32_t navigation_data::altitude
```

相对于平均海平面（MSL）的高度，单位为毫米。

<a id="af9887a29823fc3e083dbd14d1f6cfce1"></a>

### `bearing`

```c
uint32_t navigation_data::bearing
```

方位角（Bearing angle），单位为毫度（millidegree），范围为 0 至 `360E3`。

<a id="a02d9f8cea5fe68810123bb2bf554d59c"></a>

### `latitude`

```c
int64_t navigation_data::latitude
```

纬度位置（Latitudinal position），单位为纳度（nanodegree），原文范围为 `0 to +-180E9`。

译注：官方原文对纬度也给出了上述范围；这里保留该表述，不将其视为常规地理纬度范围的更改。

<a id="a530eb9c4e3750bbb03b26256794d0914"></a>

### `longitude`

```c
int64_t navigation_data::longitude
```

经度位置（Longitudinal position），单位为纳度（nanodegree），范围按原文为 `0 to +-180E9`。

<a id="a5fd501c07c21e66217a7634d7d607d1d"></a>

### `speed`

```c
uint32_t navigation_data::speed
```

速度，单位为毫米/秒。

本数据类型文档由以下文件生成：

- `zephyr/data/navigation.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/data/navigation.h](https://docs.zephyrproject.org/latest/doxygen/html/navigation_8h_source.html)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_gnss_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_nmea_match_epu_data_结构体.md)
