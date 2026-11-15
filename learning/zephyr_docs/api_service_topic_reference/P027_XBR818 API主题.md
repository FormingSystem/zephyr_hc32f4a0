---
id: learning.zephyr-docs.api-service-topic-reference.page-27
title: XBR818 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_XBR818 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Phosense XBR818 10 GHz 雷达（Radar）。

<a id="details"></a>

Phosense XBR818 10 GHz 雷达（Radar）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 27.1\_枚举（Enumerations）

<a id="r_ga2f524848967d71fe6c7557355a064bec"></a>

```c
enum sensor_attribute_xbr818 { SENSOR_ATTR_XBR818_DELAY_TIME = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_XBR818_LOCK_TIME , SENSOR_ATTR_XBR818_NOISE_FLOOR , SENSOR_ATTR_XBR818_RF_POWER }
```

相关声明：[sensor_attribute_xbr818](#ga2f524848967d71fe6c7557355a064bec)、[SENSOR_ATTR_XBR818_DELAY_TIME](#gga2f524848967d71fe6c7557355a064becaa9f1b6389623e1f197b4e9d41ce784ed)、[SENSOR_ATTR_XBR818_LOCK_TIME](#gga2f524848967d71fe6c7557355a064beca69b529d03c9898dd1dad0907ea090434)、[SENSOR_ATTR_XBR818_NOISE_FLOOR](#gga2f524848967d71fe6c7557355a064beca7fdfc87ccda9cbf8c1dc5c5b3b093467)、[SENSOR_ATTR_XBR818_RF_POWER](#gga2f524848967d71fe6c7557355a064beca91dd8effcc638ecdf035ef5c051f75ad)。

XBR818 的自定义传感器属性（Custom Sensor Attributes）。

## 27.2\_详细说明（Detailed Documentation）

<a id="ga2f524848967d71fe6c7557355a064bec"></a>

### `sensor_attribute_xbr818`

```c
enum sensor_attribute_xbr818
```

```c
#include <zephyr/drivers/sensor/xbr818.h>
```

XBR818 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_XBR818_DELAY_TIME` | 触发输出前持续接收到活动（Activity）的时间，单位为秒（Seconds）。 |
| `SENSOR_ATTR_XBR818_LOCK_TIME` | 不再检测到活动（Activity）后，输出继续保持触发状态的时长，单位为秒（Seconds）。 |
| `SENSOR_ATTR_XBR818_NOISE_FLOOR` | 雷达噪声底阈值（Radar Noise Floor Threshold），使用整数部分的低 16 个有效位（LSBs）。 |
| `SENSOR_ATTR_XBR818_RF_POWER` | 雷达射频功率（RF Power），范围为 0～7，使用整数部分的最低有效位（LSB）。 |


## 27.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor/xbr818.h](../api_file_configuration_reference/P081_zephyr__drivers__sensor__xbr818.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga2f524848967d71fe6c7557355a064becaa9f1b6389623e1f197b4e9d41ce784ed"></a>
<a id="gga2f524848967d71fe6c7557355a064beca69b529d03c9898dd1dad0907ea090434"></a>
<a id="gga2f524848967d71fe6c7557355a064beca7fdfc87ccda9cbf8c1dc5c5b3b093467"></a>
<a id="gga2f524848967d71fe6c7557355a064beca91dd8effcc638ecdf035ef5c051f75ad"></a>

---

[上一章](P026_WSEN-PADS-2511020213301 API主题.md) · [返回大纲](大纲.md) · [下一章](P028_Xen硬件虚拟机（HVM）的操作。.md)
