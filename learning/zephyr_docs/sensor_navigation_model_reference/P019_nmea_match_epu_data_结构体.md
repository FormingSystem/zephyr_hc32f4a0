---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-19
title: nmea_match_epu_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnmea__match__epu__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_nmea\_match\_epu\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnmea__match__epu__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已解析的EPU语句数据，即HL78xx专有的位置误差（Position Error）数据。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

解析后的 EPU 语句数据，表示 HL78xx 专有的位置误差信息。包含从 HL78xx 专有的 PEPU NMEA 语句中获得的估计位置及速度不确定度。所有值的单位为米或米/秒，均以定点整数（fixed-point integer）存储。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a869278cfd8e19efd76ab25c620d98972"></a>

```c
int64_t pos_3d
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[pos_3d](#a869278cfd8e19efd76ab25c620d98972)。

三维（3D）位置误差估计，单位为米。

<a id="r_a1824d2be73ef8309c000e71fc28d685e"></a>

```c
int64_t pos_2d
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[pos_2d](#a1824d2be73ef8309c000e71fc28d685e)。

二维（水平）位置误差估计，单位为米。

<a id="r_af001cd72af6d3f37d37b94e9c1c3f16b"></a>

```c
int64_t pos_lat
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[pos_lat](#af001cd72af6d3f37d37b94e9c1c3f16b)。

纬度位置误差估计，单位为米。

<a id="r_a4441cc16e1cb15ab6d631d6f2408ffd8"></a>

```c
int64_t pos_lon
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[pos_lon](#a4441cc16e1cb15ab6d631d6f2408ffd8)。

经度位置误差估计，单位为米。

<a id="r_a1545c6fbe045b9770b0701ba89b76353"></a>

```c
int64_t pos_alt
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[pos_alt](#a1545c6fbe045b9770b0701ba89b76353)。

高度位置误差估计，单位为米。

<a id="r_a854b002cd40b9803e8767136a9b100a5"></a>

```c
int64_t vel_3d
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[vel_3d](#a854b002cd40b9803e8767136a9b100a5)。

三维（3D）速度误差估计，单位为 m/s。

<a id="r_a2bebe6e0c3b502cddb46ded81339c96d"></a>

```c
int64_t vel_2d
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[vel_2d](#a2bebe6e0c3b502cddb46ded81339c96d)。

二维（水平）速度误差估计，单位为 m/s。

<a id="r_a0b6709964409e68bfc1ec6053599c4d3"></a>

```c
int64_t vel_hdg
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[vel_hdg](#a0b6709964409e68bfc1ec6053599c4d3)。

航向速度误差估计，单位为 m/s。

<a id="r_a00bc50a051125d483ecc0372939d3366"></a>

```c
int64_t vel_east
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[vel_east](#a00bc50a051125d483ecc0372939d3366)。

东向速度误差估计，单位为 m/s。

<a id="r_a342a008ff997d77e50be985807e09e39"></a>

```c
int64_t vel_north
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[vel_north](#a342a008ff997d77e50be985807e09e39)。

北向速度误差估计，单位为 m/s。

<a id="r_a5fd2bd27efde367b4b8cee37a6f73cfe"></a>

```c
int64_t vel_up
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[vel_up](#a5fd2bd27efde367b4b8cee37a6f73cfe)。

向上（垂直）速度误差估计，单位为 m/s。

## 19.2\_详细说明（Detailed Documentation）

<a id="a1824d2be73ef8309c000e71fc28d685e"></a>

### `pos_2d`

```c
int64_t nmea_match_epu_data::pos_2d
```

二维（水平）位置误差估计，单位为米。

<a id="a869278cfd8e19efd76ab25c620d98972"></a>

### `pos_3d`

```c
int64_t nmea_match_epu_data::pos_3d
```

三维（3D）位置误差估计，单位为米。

<a id="a1545c6fbe045b9770b0701ba89b76353"></a>

### `pos_alt`

```c
int64_t nmea_match_epu_data::pos_alt
```

高度位置误差估计，单位为米。

<a id="af001cd72af6d3f37d37b94e9c1c3f16b"></a>

### `pos_lat`

```c
int64_t nmea_match_epu_data::pos_lat
```

纬度位置误差估计，单位为米。

<a id="a4441cc16e1cb15ab6d631d6f2408ffd8"></a>

### `pos_lon`

```c
int64_t nmea_match_epu_data::pos_lon
```

经度位置误差估计，单位为米。

<a id="a2bebe6e0c3b502cddb46ded81339c96d"></a>

### `vel_2d`

```c
int64_t nmea_match_epu_data::vel_2d
```

二维（水平）速度误差估计，单位为 m/s。

<a id="a854b002cd40b9803e8767136a9b100a5"></a>

### `vel_3d`

```c
int64_t nmea_match_epu_data::vel_3d
```

三维（3D）速度误差估计，单位为 m/s。

<a id="a00bc50a051125d483ecc0372939d3366"></a>

### `vel_east`

```c
int64_t nmea_match_epu_data::vel_east
```

东向速度误差估计，单位为 m/s。

<a id="a0b6709964409e68bfc1ec6053599c4d3"></a>

### `vel_hdg`

```c
int64_t nmea_match_epu_data::vel_hdg
```

航向速度误差估计，单位为 m/s。

<a id="a342a008ff997d77e50be985807e09e39"></a>

### `vel_north`

```c
int64_t nmea_match_epu_data::vel_north
```

北向速度误差估计，单位为 m/s。

<a id="a5fd2bd27efde367b4b8cee37a6f73cfe"></a>

### `vel_up`

```c
int64_t nmea_match_epu_data::vel_up
```

向上（垂直）速度误差估计，单位为 m/s。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_navigation_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_nmea_match_gsa_data_结构体.md)
