---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-21
title: nmea_match_gst_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnmea__match__gst__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_nmea\_match\_gst\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnmea__match__gst__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已解析的GST语句数据，即GNSS伪距误差统计（Pseudorange Error Statistics）。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

解析后的 GST 语句数据，表示 GNSS 伪距误差统计（Pseudorange Error Statistics）。包含从 GST NMEA 语句取得的位置误差估计。误差值以米为单位，并以定点整数存储。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_af7061a41e30e58c5cc58bebbd1663f9c"></a>

```c
int32_t i32
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[i32](#af7061a41e30e58c5cc58bebbd1663f9c)。

保留供内部使用。

<a id="r_a932c670f5a642ad7449806f69910328f"></a>

```c
uint32_t gst_utc
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[gst_utc](#a932c670f5a642ad7449806f69910328f)。

对应定位结果的 UTC 时间，格式为 HHMMSS。

<a id="r_a7ba102be3748cdad0d9a44bd68d6c70f"></a>

```c
int64_t rms
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[rms](#a7ba102be3748cdad0d9a44bd68d6c70f)。

测距输入标准差的均方根（RMS）值。

<a id="r_a5bc62b0b55f62c0922fc00d13ff2f364"></a>

```c
int64_t sd_major
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[sd_major](#a5bc62b0b55f62c0922fc00d13ff2f364)。

误差椭圆半长轴（semi-major axis）的标准差，单位为米。

<a id="r_aab1c6e9433619af20da9182d693ed692"></a>

```c
int64_t sd_minor
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[sd_minor](#aab1c6e9433619af20da9182d693ed692)。

误差椭圆半短轴（semi-minor axis）的标准差，单位为米。

<a id="r_a8032be26aa57b4feb55dd119183b3d47"></a>

```c
int64_t orient
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[orient](#a8032be26aa57b4feb55dd119183b3d47)。

误差椭圆半长轴的方向，以相对于真北的角度表示。

<a id="r_a4fdfb99f5c451ac7360613579a68416a"></a>

```c
int64_t lat_err
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[lat_err](#a4fdfb99f5c451ac7360613579a68416a)。

纬度误差标准差，单位为米。

<a id="r_a667027ebf56ecdd29be0321e982cb72f"></a>

```c
int64_t lon_err
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[lon_err](#a667027ebf56ecdd29be0321e982cb72f)。

经度误差标准差，单位为米。

<a id="r_a590ae7d7df7a4c78da267f0dc9f451f2"></a>

```c
int64_t alt_err
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[alt_err](#a590ae7d7df7a4c78da267f0dc9f451f2)。

高度误差标准差，单位为米。

## 21.2\_详细说明（Detailed Documentation）

<a id="a590ae7d7df7a4c78da267f0dc9f451f2"></a>

### `alt_err`

```c
int64_t nmea_match_gst_data::alt_err
```

高度误差标准差，单位为米。

<a id="a932c670f5a642ad7449806f69910328f"></a>

### `gst_utc`

```c
uint32_t nmea_match_gst_data::gst_utc
```

对应定位结果的 UTC 时间，格式为 HHMMSS。

<a id="af7061a41e30e58c5cc58bebbd1663f9c"></a>

### `i32`

```c
int32_t nmea_match_gst_data::i32
```

保留供内部使用。

<a id="a4fdfb99f5c451ac7360613579a68416a"></a>

### `lat_err`

```c
int64_t nmea_match_gst_data::lat_err
```

纬度误差标准差，单位为米。

<a id="a667027ebf56ecdd29be0321e982cb72f"></a>

### `lon_err`

```c
int64_t nmea_match_gst_data::lon_err
```

经度误差标准差，单位为米。

<a id="a8032be26aa57b4feb55dd119183b3d47"></a>

### `orient`

```c
int64_t nmea_match_gst_data::orient
```

误差椭圆半长轴的方向，以相对于真北的角度表示。

<a id="a7ba102be3748cdad0d9a44bd68d6c70f"></a>

### `rms`

```c
int64_t nmea_match_gst_data::rms
```

测距输入标准差的均方根（RMS）值。

<a id="a5bc62b0b55f62c0922fc00d13ff2f364"></a>

### `sd_major`

```c
int64_t nmea_match_gst_data::sd_major
```

误差椭圆半长轴（semi-major axis）的标准差，单位为米。

<a id="aab1c6e9433619af20da9182d693ed692"></a>

### `sd_minor`

```c
int64_t nmea_match_gst_data::sd_minor
```

误差椭圆半短轴（semi-minor axis）的标准差，单位为米。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_nmea_match_gsa_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_r502a_sys_param_结构体.md)
