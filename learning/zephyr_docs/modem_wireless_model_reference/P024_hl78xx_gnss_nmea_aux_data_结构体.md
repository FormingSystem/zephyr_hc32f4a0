---
id: learning.zephyr-docs.modem-wireless-model-reference.page-24
title: hl78xx_gnss_nmea_aux_data_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__gnss__nmea__aux__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_hl78xx\_gnss\_nmea\_aux\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__gnss__nmea__aux__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全部GNSS辅助NMEA数据的容器。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

容纳所有 GNSS 辅助 NMEA 数据的容器。汇集补充 NMEA 语句（GSA、GST、PEPU）的解析结果，这些语句提供质量和精度指标。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a529e929ce8878c329f0c370fd8155ce2"></a>

```c
struct nmea_match_gsa_data gsa
```

相关声明：[nmea_match_gsa_data](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md)、[gsa](#a529e929ce8878c329f0c370fd8155ce2)。

GSA 语句数据，包含精度因子（DOP）和定位类型。

<a id="r_a9d099e5d5baf20aa18dfd43e531aa202"></a>

```c
struct nmea_match_gst_data gst
```

相关声明：[nmea_match_gst_data](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md)、[gst](#a9d099e5d5baf20aa18dfd43e531aa202)。

GST 语句数据，包含伪距误差统计（pseudorange error statistics）。

<a id="r_a471784cde53ace4fda5ab532e428c6c8"></a>

```c
struct nmea_match_epu_data epu
```

相关声明：[nmea_match_epu_data](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md)、[epu](#a471784cde53ace4fda5ab532e428c6c8)。

EPU 语句数据，包含 HL78xx 专有的位置和速度误差。

## 24.2\_详细说明（Detailed Documentation）

<a id="a471784cde53ace4fda5ab532e428c6c8"></a>

### `epu`

```c
struct nmea_match_epu_data hl78xx_gnss_nmea_aux_data::epu
```

EPU 语句数据，包含 HL78xx 专有的位置和速度误差。

<a id="a529e929ce8878c329f0c370fd8155ce2"></a>

### `gsa`

```c
struct nmea_match_gsa_data hl78xx_gnss_nmea_aux_data::gsa
```

GSA 语句数据，包含精度因子（DOP）和定位类型。

<a id="a9d099e5d5baf20aa18dfd43e531aa202"></a>

### `gst`

```c
struct nmea_match_gst_data hl78xx_gnss_nmea_aux_data::gst
```

GST 语句数据，包含伪距误差统计（pseudorange error statistics）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [nmea_match_gsa_data](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md)
- [nmea_match_gst_data](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md)
- [nmea_match_epu_data](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_hl78xx_gnss_aux_data_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_hl78xx_network_结构体.md)
