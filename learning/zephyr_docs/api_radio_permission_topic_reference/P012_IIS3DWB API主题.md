---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-12
title: IIS3DWB API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__iis3dwb__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_IIS3DWB API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__iis3dwb__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics IIS3DWB 三轴振动加速度计（3-axis vibration accelerometer）。

<a id="details"></a>

STMicroelectronics IIS3DWB 三轴振动加速度计（3-axis vibration accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_iis3dwb_2Eh"></a>

```c
file iis3dwb.h
```

相关声明：[iis3dwb.h](https://docs.zephyrproject.org/latest/doxygen/html/iis3dwb_8h.html)。

the ST IIS3DWB accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 12.2\_输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_ga6ec4af1218c207cda346c077a58ba5fa"></a>

```c
#define IIS3DWB_DT_ODR_OFF 0
```

相关声明：[IIS3DWB_DT_ODR_OFF](#ga6ec4af1218c207cda346c077a58ba5fa)。

掉电（Power-down）。

<a id="r_ga13f02278734157c50fac51a8f09084d9"></a>

```c
#define IIS3DWB_DT_ODR_26k7Hz 5
```

相关声明：[IIS3DWB_DT_ODR_26k7Hz](#ga13f02278734157c50fac51a8f09084d9)。

频率（Frequency）：26.7 kHz。

## 12.3\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `range` 属性的取值。

<a id="r_ga4dfd677fa0b1e29c9bc40b463f976233"></a>

```c
#define IIS3DWB_DT_FS_2G 0
```

相关声明：[IIS3DWB_DT_FS_2G](#ga4dfd677fa0b1e29c9bc40b463f976233)。

量程（Range）：±2 g；灵敏度（Sensitivity）：0.061 mg/LSB。

<a id="r_ga506726fa2f5b4c185f9f0cb2eddbb056"></a>

```c
#define IIS3DWB_DT_FS_16G 1
```

相关声明：[IIS3DWB_DT_FS_16G](#ga506726fa2f5b4c185f9f0cb2eddbb056)。

量程（Range）：±16 g；灵敏度（Sensitivity）：0.488 mg/LSB。

<a id="r_ga4a46a69f72d1c6aef0661f391828af25"></a>

```c
#define IIS3DWB_DT_FS_4G 2
```

相关声明：[IIS3DWB_DT_FS_4G](#ga4a46a69f72d1c6aef0661f391828af25)。

量程（Range）：±4 g；灵敏度（Sensitivity）：0.122 mg/LSB。

<a id="r_gadc45970b6e6a32be222a0b528e867b91"></a>

```c
#define IIS3DWB_DT_FS_8G 3
```

相关声明：[IIS3DWB_DT_FS_8G](#gadc45970b6e6a32be222a0b528e867b91)。

量程（Range）：±8 g；灵敏度（Sensitivity）：0.244 mg/LSB。

## 12.4\_滤波路径选项（Filter Path Options）

设备树 filter 属性（Property）的值。

选择应用于加速度计输出的数字滤波器（Digital Filter）：斜率（Slope）、高通（HP）或低通（LP），截止频率表示为输出数据率（Output Data Rate，ODR）的某个分数。

<a id="r_gac557e77437f2d658b75005db34e715b3"></a>

```c
#define IIS3DWB_DT_SLOPE_ODR_DIV_4 0x10
```

相关声明：[IIS3DWB_DT_SLOPE_ODR_DIV_4](#gac557e77437f2d658b75005db34e715b3)。

斜率滤波器（Slope Filter），ODR / 4。

<a id="r_ga3411119d55b85413516b88b91782bd28"></a>

```c
#define IIS3DWB_DT_HP_REF_MODE 0x37
```

相关声明：[IIS3DWB_DT_HP_REF_MODE](#ga3411119d55b85413516b88b91782bd28)。

高通参考模式（High-pass Reference Mode）。

<a id="r_ga85e76be4aecff12115c17ceaa53e75ec"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_10 0x11
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_10](#ga85e76be4aecff12115c17ceaa53e75ec)。

高通（High-pass），ODR / 10。

<a id="r_gaeb389c22f7835affe3e5b7211bd2adc2"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_20 0x12
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_20](#gaeb389c22f7835affe3e5b7211bd2adc2)。

高通（High-pass），ODR / 20。

<a id="r_ga654c694464c036e6bf5b25a5711e029d"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_45 0x13
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_45](#ga654c694464c036e6bf5b25a5711e029d)。

高通（High-pass），ODR / 45。

<a id="r_ga8926ea05a80c76e2a6058540807aae0a"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_100 0x14
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_100](#ga8926ea05a80c76e2a6058540807aae0a)。

高通（High-pass），ODR / 100。

<a id="r_ga5a426c62af407a029b60206d74fed226"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_200 0x15
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_200](#ga5a426c62af407a029b60206d74fed226)。

高通（High-pass），ODR / 200。

<a id="r_ga57114b2257380a1b54a8a8b20538bde7"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_400 0x16
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_400](#ga57114b2257380a1b54a8a8b20538bde7)。

高通（High-pass），ODR / 400。

<a id="r_gafce0a98570166feb29c769f2ffe56a08"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_800 0x17
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_800](#gafce0a98570166feb29c769f2ffe56a08)。

高通（High-pass），ODR / 800。

<a id="r_ga33e3ab3cf214aa2190767527ff961a74"></a>

```c
#define IIS3DWB_DT_LP_6k3Hz 0x00
```

相关声明：[IIS3DWB_DT_LP_6k3Hz](#ga33e3ab3cf214aa2190767527ff961a74)。

低通（Low-pass），6.3 kHz。

<a id="r_gad25472470cb5211e1a6cfe26a432a1e9"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_4 0x80
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_4](#gad25472470cb5211e1a6cfe26a432a1e9)。

低通（Low-pass），ODR / 4。

<a id="r_ga12881256d83269256cd812077969b3b5"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_10 0x81
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_10](#ga12881256d83269256cd812077969b3b5)。

低通（Low-pass），ODR / 10。

<a id="r_ga7747705f6e2777d22651d040bb0adebe"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_20 0x82
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_20](#ga7747705f6e2777d22651d040bb0adebe)。

低通（Low-pass），ODR / 20。

<a id="r_ga28dde4ed628eb1e19b766c5bc6dd8a87"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_45 0x83
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_45](#ga28dde4ed628eb1e19b766c5bc6dd8a87)。

低通（Low-pass），ODR / 45。

<a id="r_gaf395ae5e9869141e96b9cfb3b7b29b2e"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_100 0x84
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_100](#gaf395ae5e9869141e96b9cfb3b7b29b2e)。

低通（Low-pass），ODR / 100。

<a id="r_ga1c25888dd9cd34b3daff073c6bfe2ea0"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_200 0x85
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_200](#ga1c25888dd9cd34b3daff073c6bfe2ea0)。

低通（Low-pass），ODR / 200。

<a id="r_gac1de555dff858c1640179ae2058621e8"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_400 0x86
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_400](#gac1de555dff858c1640179ae2058621e8)。

低通（Low-pass），ODR / 400。

<a id="r_gab3623fb19fc3121fb58a1dd529e770eb"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_800 0x87
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_800](#gab3623fb19fc3121fb58a1dd529e770eb)。

低通（Low-pass），ODR / 800。

## 12.5\_加速度计 FIFO 批量入队速率（Accelerometer FIFO Batching Rate）

设备树 accel-fifo-batch-rate 属性（Property）的值。

<a id="r_ga8a172c5be99ce84cc8c77abfe8fb9578"></a>

```c
#define IIS3DWB_DT_XL_NOT_BATCHED 0x0
```

相关声明：[IIS3DWB_DT_XL_NOT_BATCHED](#ga8a172c5be99ce84cc8c77abfe8fb9578)。

不批量入队（Not Batched）。

<a id="r_ga0bc4148870c0f462189807d0b03d335e"></a>

```c
#define IIS3DWB_DT_XL_BATCHED_AT_26k7Hz 0xA
```

相关声明：[IIS3DWB_DT_XL_BATCHED_AT_26k7Hz](#ga0bc4148870c0f462189807d0b03d335e)。

频率（Frequency）：26.7 kHz。

## 12.6\_温度 FIFO 批量入队速率（Temperature FIFO Batching Rate）

设备树 temp-fifo-batch-rate 属性（Property）的值。

<a id="r_ga5027e4b865594e7bb26665c74baacca8"></a>

```c
#define IIS3DWB_DT_TEMP_NOT_BATCHED 0
```

相关声明：[IIS3DWB_DT_TEMP_NOT_BATCHED](#ga5027e4b865594e7bb26665c74baacca8)。

不批量入队（Not Batched）。

<a id="r_ga20caf830abe63a7e5196b561d7c716ad"></a>

```c
#define IIS3DWB_DT_TEMP_BATCHED_AT_104Hz 3
```

相关声明：[IIS3DWB_DT_TEMP_BATCHED_AT_104Hz](#ga20caf830abe63a7e5196b561d7c716ad)。

频率：104 Hz。

## 12.7\_FIFO 时间戳抽取（Timestamp Decimation）

设备树 timestamp-fifo-batch-rate 属性（Property）的值。

<a id="r_ga8a7fb4ebabfdc8a27acb89b5ecb21f62"></a>

```c
#define IIS3DWB_DT_TS_NOT_BATCHED 0x0
```

相关声明：[IIS3DWB_DT_TS_NOT_BATCHED](#ga8a7fb4ebabfdc8a27acb89b5ecb21f62)。

时间戳不批量入队（Timestamp Not Batched）。

<a id="r_ga9fd77bdd0ee73b255ab4c81fa5989a61"></a>

```c
#define IIS3DWB_DT_DEC_TS_1 0x1
```

相关声明：[IIS3DWB_DT_DEC_TS_1](#ga9fd77bdd0ee73b255ab4c81fa5989a61)。

1 倍抽取（Decimation）。

<a id="r_ga51426db564b97a6219e55e91cf32c7a1"></a>

```c
#define IIS3DWB_DT_DEC_TS_8 0x2
```

相关声明：[IIS3DWB_DT_DEC_TS_8](#ga51426db564b97a6219e55e91cf32c7a1)。

8 倍抽取（Decimation）。

<a id="r_ga3a8bd2b92d89719836eac5cb7d6f0103"></a>

```c
#define IIS3DWB_DT_DEC_TS_32 0x3
```

相关声明：[IIS3DWB_DT_DEC_TS_32](#ga3a8bd2b92d89719836eac5cb7d6f0103)。

32 倍抽取（Decimation）。

## 12.8\_详细说明（Detailed Documentation）

<a id="ga9fd77bdd0ee73b255ab4c81fa5989a61"></a>

### `IIS3DWB_DT_DEC_TS_1`

```c
#define IIS3DWB_DT_DEC_TS_1 0x1
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

1 倍抽取（Decimation）。

<a id="ga3a8bd2b92d89719836eac5cb7d6f0103"></a>

### `IIS3DWB_DT_DEC_TS_32`

```c
#define IIS3DWB_DT_DEC_TS_32 0x3
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

32 倍抽取（Decimation）。

<a id="ga51426db564b97a6219e55e91cf32c7a1"></a>

### `IIS3DWB_DT_DEC_TS_8`

```c
#define IIS3DWB_DT_DEC_TS_8 0x2
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

8 倍抽取（Decimation）。

<a id="ga506726fa2f5b4c185f9f0cb2eddbb056"></a>

### `IIS3DWB_DT_FS_16G`

```c
#define IIS3DWB_DT_FS_16G 1
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

量程（Range）：±16 g；灵敏度（Sensitivity）：0.488 mg/LSB。

<a id="ga4dfd677fa0b1e29c9bc40b463f976233"></a>

### `IIS3DWB_DT_FS_2G`

```c
#define IIS3DWB_DT_FS_2G 0
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

量程（Range）：±2 g；灵敏度（Sensitivity）：0.061 mg/LSB。

<a id="ga4a46a69f72d1c6aef0661f391828af25"></a>

### `IIS3DWB_DT_FS_4G`

```c
#define IIS3DWB_DT_FS_4G 2
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

量程（Range）：±4 g；灵敏度（Sensitivity）：0.122 mg/LSB。

<a id="gadc45970b6e6a32be222a0b528e867b91"></a>

### `IIS3DWB_DT_FS_8G`

```c
#define IIS3DWB_DT_FS_8G 3
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

量程（Range）：±8 g；灵敏度（Sensitivity）：0.244 mg/LSB。

<a id="ga85e76be4aecff12115c17ceaa53e75ec"></a>

### `IIS3DWB_DT_HP_ODR_DIV_10`

```c
#define IIS3DWB_DT_HP_ODR_DIV_10 0x11
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

高通（High-pass），ODR / 10。

<a id="ga8926ea05a80c76e2a6058540807aae0a"></a>

### `IIS3DWB_DT_HP_ODR_DIV_100`

```c
#define IIS3DWB_DT_HP_ODR_DIV_100 0x14
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

高通（High-pass），ODR / 100。

<a id="gaeb389c22f7835affe3e5b7211bd2adc2"></a>

### `IIS3DWB_DT_HP_ODR_DIV_20`

```c
#define IIS3DWB_DT_HP_ODR_DIV_20 0x12
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

高通（High-pass），ODR / 20。

<a id="ga5a426c62af407a029b60206d74fed226"></a>

### `IIS3DWB_DT_HP_ODR_DIV_200`

```c
#define IIS3DWB_DT_HP_ODR_DIV_200 0x15
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

高通（High-pass），ODR / 200。

<a id="ga57114b2257380a1b54a8a8b20538bde7"></a>

### `IIS3DWB_DT_HP_ODR_DIV_400`

```c
#define IIS3DWB_DT_HP_ODR_DIV_400 0x16
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

高通（High-pass），ODR / 400。

<a id="ga654c694464c036e6bf5b25a5711e029d"></a>

### `IIS3DWB_DT_HP_ODR_DIV_45`

```c
#define IIS3DWB_DT_HP_ODR_DIV_45 0x13
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

高通（High-pass），ODR / 45。

<a id="gafce0a98570166feb29c769f2ffe56a08"></a>

### `IIS3DWB_DT_HP_ODR_DIV_800`

```c
#define IIS3DWB_DT_HP_ODR_DIV_800 0x17
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

高通（High-pass），ODR / 800。

<a id="ga3411119d55b85413516b88b91782bd28"></a>

### `IIS3DWB_DT_HP_REF_MODE`

```c
#define IIS3DWB_DT_HP_REF_MODE 0x37
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

高通参考模式（High-pass Reference Mode）。

<a id="ga33e3ab3cf214aa2190767527ff961a74"></a>

### `IIS3DWB_DT_LP_6k3Hz`

```c
#define IIS3DWB_DT_LP_6k3Hz 0x00
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

低通（Low-pass），6.3 kHz。

<a id="ga12881256d83269256cd812077969b3b5"></a>

### `IIS3DWB_DT_LP_ODR_DIV_10`

```c
#define IIS3DWB_DT_LP_ODR_DIV_10 0x81
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

低通（Low-pass），ODR / 10。

<a id="gaf395ae5e9869141e96b9cfb3b7b29b2e"></a>

### `IIS3DWB_DT_LP_ODR_DIV_100`

```c
#define IIS3DWB_DT_LP_ODR_DIV_100 0x84
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

低通（Low-pass），ODR / 100。

<a id="ga7747705f6e2777d22651d040bb0adebe"></a>

### `IIS3DWB_DT_LP_ODR_DIV_20`

```c
#define IIS3DWB_DT_LP_ODR_DIV_20 0x82
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

低通（Low-pass），ODR / 20。

<a id="ga1c25888dd9cd34b3daff073c6bfe2ea0"></a>

### `IIS3DWB_DT_LP_ODR_DIV_200`

```c
#define IIS3DWB_DT_LP_ODR_DIV_200 0x85
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

低通（Low-pass），ODR / 200。

<a id="gad25472470cb5211e1a6cfe26a432a1e9"></a>

### `IIS3DWB_DT_LP_ODR_DIV_4`

```c
#define IIS3DWB_DT_LP_ODR_DIV_4 0x80
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

低通（Low-pass），ODR / 4。

<a id="gac1de555dff858c1640179ae2058621e8"></a>

### `IIS3DWB_DT_LP_ODR_DIV_400`

```c
#define IIS3DWB_DT_LP_ODR_DIV_400 0x86
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

低通（Low-pass），ODR / 400。

<a id="ga28dde4ed628eb1e19b766c5bc6dd8a87"></a>

### `IIS3DWB_DT_LP_ODR_DIV_45`

```c
#define IIS3DWB_DT_LP_ODR_DIV_45 0x83
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

低通（Low-pass），ODR / 45。

<a id="gab3623fb19fc3121fb58a1dd529e770eb"></a>

### `IIS3DWB_DT_LP_ODR_DIV_800`

```c
#define IIS3DWB_DT_LP_ODR_DIV_800 0x87
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

低通（Low-pass），ODR / 800。

<a id="ga13f02278734157c50fac51a8f09084d9"></a>

### `IIS3DWB_DT_ODR_26k7Hz`

```c
#define IIS3DWB_DT_ODR_26k7Hz 5
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

频率（Frequency）：26.7 kHz。

<a id="ga6ec4af1218c207cda346c077a58ba5fa"></a>

### `IIS3DWB_DT_ODR_OFF`

```c
#define IIS3DWB_DT_ODR_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

掉电（Power-down）。

<a id="gac557e77437f2d658b75005db34e715b3"></a>

### `IIS3DWB_DT_SLOPE_ODR_DIV_4`

```c
#define IIS3DWB_DT_SLOPE_ODR_DIV_4 0x10
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

斜率滤波器（Slope Filter），ODR / 4。

<a id="ga20caf830abe63a7e5196b561d7c716ad"></a>

### `IIS3DWB_DT_TEMP_BATCHED_AT_104Hz`

```c
#define IIS3DWB_DT_TEMP_BATCHED_AT_104Hz 3
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

频率：104 Hz。

<a id="ga5027e4b865594e7bb26665c74baacca8"></a>

### `IIS3DWB_DT_TEMP_NOT_BATCHED`

```c
#define IIS3DWB_DT_TEMP_NOT_BATCHED 0
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

不批量入队（Not Batched）。

<a id="ga8a7fb4ebabfdc8a27acb89b5ecb21f62"></a>

### `IIS3DWB_DT_TS_NOT_BATCHED`

```c
#define IIS3DWB_DT_TS_NOT_BATCHED 0x0
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

时间戳不批量入队（Timestamp Not Batched）。

<a id="ga0bc4148870c0f462189807d0b03d335e"></a>

### `IIS3DWB_DT_XL_BATCHED_AT_26k7Hz`

```c
#define IIS3DWB_DT_XL_BATCHED_AT_26k7Hz 0xA
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

频率（Frequency）：26.7 kHz。

<a id="ga8a172c5be99ce84cc8c77abfe8fb9578"></a>

### `IIS3DWB_DT_XL_NOT_BATCHED`

```c
#define IIS3DWB_DT_XL_NOT_BATCHED 0x0
```

```c
#include <zephyr/dt-bindings/sensor/iis3dwb.h>
```

不批量入队（Not Batched）。


## 12.9\_原页交叉引用（Cross References）

- [iis3dwb.h](https://docs.zephyrproject.org/latest/doxygen/html/iis3dwb_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P011_HTTP请求方法（Request Methods）。.md) · [返回大纲](大纲.md) · [下一章](P013_线性范围（Linear Range）.md)
