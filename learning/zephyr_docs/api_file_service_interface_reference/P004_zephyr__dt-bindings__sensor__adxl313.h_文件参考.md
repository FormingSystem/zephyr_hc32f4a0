---
id: learning.zephyr-docs.api-file-service-interface-reference.page-4
title: zephyr__dt-bindings__sensor__adxl313.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adxl313_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_sensor\_\_adxl313.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adxl313_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Analog Devices ADXL313 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Analog Devices ADXL313 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值，对应 `BW_RATE` 寄存器。

<a id="r_ga02a7095f521f5e696800cfc5fce72217"></a>

```c
#define ADXL313_DT_ODR_6_25 6
```

相关声明：[ADXL313_DT_ODR_6_25](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga02a7095f521f5e696800cfc5fce72217)。

频率：6.25 Hz。

<a id="r_ga4807d03edd4da963773d99a24b805f12"></a>

```c
#define ADXL313_DT_ODR_12_5 7
```

相关声明：[ADXL313_DT_ODR_12_5](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga4807d03edd4da963773d99a24b805f12)。

频率：12.5 Hz。

<a id="r_gae74ffdddc1787b97e561785f6b8ad202"></a>

```c
#define ADXL313_DT_ODR_25 8
```

相关声明：[ADXL313_DT_ODR_25](../api_network_time_topic_reference/P001_ADXL313 API主题.md#gae74ffdddc1787b97e561785f6b8ad202)。

频率：25 Hz。

<a id="r_ga1d20b1876f2c6ca49d974f374bdef464"></a>

```c
#define ADXL313_DT_ODR_50 9
```

相关声明：[ADXL313_DT_ODR_50](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga1d20b1876f2c6ca49d974f374bdef464)。

频率：50 Hz。

<a id="r_gaece105aeb621ef3f73ce67f434d76771"></a>

```c
#define ADXL313_DT_ODR_100 10
```

相关声明：[ADXL313_DT_ODR_100](../api_network_time_topic_reference/P001_ADXL313 API主题.md#gaece105aeb621ef3f73ce67f434d76771)。

频率：100 Hz。

<a id="r_gab4fa8769a7c3d8b97513da312be8c188"></a>

```c
#define ADXL313_DT_ODR_200 11
```

相关声明：[ADXL313_DT_ODR_200](../api_network_time_topic_reference/P001_ADXL313 API主题.md#gab4fa8769a7c3d8b97513da312be8c188)。

频率：200 Hz。

<a id="r_ga087d90450b45bb0bb75e895610ce4665"></a>

```c
#define ADXL313_DT_ODR_400 12
```

相关声明：[ADXL313_DT_ODR_400](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga087d90450b45bb0bb75e895610ce4665)。

频率：400 Hz。

<a id="r_ga3e44a470a8849b99688352afefa7e1de"></a>

```c
#define ADXL313_DT_ODR_800 13
```

相关声明：[ADXL313_DT_ODR_800](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga3e44a470a8849b99688352afefa7e1de)。

频率：800 Hz。

<a id="r_ga730220c782b951050dd16a248bf978ad"></a>

```c
#define ADXL313_DT_ODR_1600 14
```

相关声明：[ADXL313_DT_ODR_1600](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga730220c782b951050dd16a248bf978ad)。

频率：1600 Hz。

<a id="r_gaec20668bace20c1d9342b0d79468ed5c"></a>

```c
#define ADXL313_DT_ODR_3200 15
```

相关声明：[ADXL313_DT_ODR_3200](../api_network_time_topic_reference/P001_ADXL313 API主题.md#gaec20668bace20c1d9342b0d79468ed5c)。

频率：3200 Hz。

<a id="define-members-1"></a>

### 测量量程选项（Measurement range options）

设备树 `range` 属性的取值，对应 `DATA_FORMAT` 寄存器。

<a id="r_ga01d6676b81a52cafc326940abe8c3dcd"></a>

```c
#define ADXL313_DT_RANGE_0_5G 0
```

相关声明：[ADXL313_DT_RANGE_0_5G](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga01d6676b81a52cafc326940abe8c3dcd)。

量程（range）：±0.5 g。

<a id="r_ga876a5a51a12688ed335d78a75d362dce"></a>

```c
#define ADXL313_DT_RANGE_1G 1
```

相关声明：[ADXL313_DT_RANGE_1G](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga876a5a51a12688ed335d78a75d362dce)。

量程（range）：±1 g。

<a id="r_ga576838117e35f1f086da223d1ca29639"></a>

```c
#define ADXL313_DT_RANGE_2G 2
```

相关声明：[ADXL313_DT_RANGE_2G](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga576838117e35f1f086da223d1ca29639)。

量程（range）：±2 g。

<a id="r_ga49806e46c1570f30498e2d672738e6f6"></a>

```c
#define ADXL313_DT_RANGE_4G 3
```

相关声明：[ADXL313_DT_RANGE_4G](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga49806e46c1570f30498e2d672738e6f6)。

量程（range）：±4 g。


## 4.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P011_adxl313.h_源码浏览.md)
- [ADXL313_DT_ODR_6_25](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga02a7095f521f5e696800cfc5fce72217)
- [ADXL313_DT_ODR_12_5](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga4807d03edd4da963773d99a24b805f12)
- [ADXL313_DT_ODR_25](../api_network_time_topic_reference/P001_ADXL313 API主题.md#gae74ffdddc1787b97e561785f6b8ad202)
- [ADXL313_DT_ODR_50](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga1d20b1876f2c6ca49d974f374bdef464)
- [ADXL313_DT_ODR_100](../api_network_time_topic_reference/P001_ADXL313 API主题.md#gaece105aeb621ef3f73ce67f434d76771)
- [ADXL313_DT_ODR_200](../api_network_time_topic_reference/P001_ADXL313 API主题.md#gab4fa8769a7c3d8b97513da312be8c188)
- [ADXL313_DT_ODR_400](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga087d90450b45bb0bb75e895610ce4665)
- [ADXL313_DT_ODR_800](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga3e44a470a8849b99688352afefa7e1de)
- [ADXL313_DT_ODR_1600](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga730220c782b951050dd16a248bf978ad)
- [ADXL313_DT_ODR_3200](../api_network_time_topic_reference/P001_ADXL313 API主题.md#gaec20668bace20c1d9342b0d79468ed5c)
- [ADXL313_DT_RANGE_0_5G](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga01d6676b81a52cafc326940abe8c3dcd)
- [ADXL313_DT_RANGE_1G](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga876a5a51a12688ed335d78a75d362dce)
- [ADXL313_DT_RANGE_2G](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga576838117e35f1f086da223d1ca29639)
- [ADXL313_DT_RANGE_4G](../api_network_time_topic_reference/P001_ADXL313 API主题.md#ga49806e46c1570f30498e2d672738e6f6)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__clock_control__adi_max32_clock_control.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__interrupt-controller__arm-gic.h_文件参考.md)
