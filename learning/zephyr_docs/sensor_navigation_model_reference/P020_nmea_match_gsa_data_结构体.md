---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-20
title: nmea_match_gsa_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnmea__match__gsa__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_nmea\_match\_gsa\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnmea__match__gsa__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已解析的GSA语句数据，即GNSS精度衰减因子（DOP）及活动卫星数据。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

解析后的 GSA 语句数据，表示 GNSS 精度因子及参与定位的卫星（DOP and Active Satellites）。包含从 GSA NMEA 语句取得的精度因子值。值以定点整数存储，即乘以适当比例因子后保存。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_aed176a2bc4f981221c69e1b08099df67"></a>

```c
int32_t fix_type
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[fix_type](#aed176a2bc4f981221c69e1b08099df67)。

定位类型（Fix type）：1 表示未定位，2 表示二维定位，3 表示三维定位。

<a id="r_aa4caab02bb1ab3a0c3014c4a3f993eae"></a>

```c
int64_t pdop
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[pdop](#aa4caab02bb1ab3a0c3014c4a3f993eae)。

位置精度因子（Position Dilution of Precision，PDOP），已按比例缩放。

<a id="r_a9a785ec7d4c1ef2727e202927fd67440"></a>

```c
int64_t hdop
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[hdop](#a9a785ec7d4c1ef2727e202927fd67440)。

水平精度因子（Horizontal Dilution of Precision，HDOP），已按比例缩放。

<a id="r_a872c2e3cbcd0dcf5b0fff194f794622f"></a>

```c
int64_t vdop
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[vdop](#a872c2e3cbcd0dcf5b0fff194f794622f)。

垂直精度因子（Vertical Dilution of Precision，VDOP），已按比例缩放。

## 20.2\_详细说明（Detailed Documentation）

<a id="aed176a2bc4f981221c69e1b08099df67"></a>

### `fix_type`

```c
int32_t nmea_match_gsa_data::fix_type
```

定位类型（Fix type）：1 表示未定位，2 表示二维定位，3 表示三维定位。

<a id="a9a785ec7d4c1ef2727e202927fd67440"></a>

### `hdop`

```c
int64_t nmea_match_gsa_data::hdop
```

水平精度因子（Horizontal Dilution of Precision，HDOP），已按比例缩放。

<a id="aa4caab02bb1ab3a0c3014c4a3f993eae"></a>

### `pdop`

```c
int64_t nmea_match_gsa_data::pdop
```

位置精度因子（Position Dilution of Precision，PDOP），已按比例缩放。

<a id="a872c2e3cbcd0dcf5b0fff194f794622f"></a>

### `vdop`

```c
int64_t nmea_match_gsa_data::vdop
```

垂直精度因子（Vertical Dilution of Precision，VDOP），已按比例缩放。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_nmea_match_epu_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_nmea_match_gst_data_结构体.md)
