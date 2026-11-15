---
id: learning.zephyr-docs.api-file-clock-network-reference.page-13
title: zephyr__dt-bindings__sensor__iis3dwb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/iis3dwb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_dt-bindings\_\_sensor\_\_iis3dwb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/iis3dwb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST IIS3DWB accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

the ST IIS3DWB accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_ga6ec4af1218c207cda346c077a58ba5fa"></a>

```c
#define IIS3DWB_DT_ODR_OFF 0
```

相关声明：[IIS3DWB_DT_ODR_OFF](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga6ec4af1218c207cda346c077a58ba5fa)。

掉电（Power-down）。

<a id="r_ga13f02278734157c50fac51a8f09084d9"></a>

```c
#define IIS3DWB_DT_ODR_26k7Hz 5
```

相关声明：[IIS3DWB_DT_ODR_26k7Hz](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga13f02278734157c50fac51a8f09084d9)。

频率（Frequency）：26.7 kHz。

<a id="define-members-1"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `range` 属性的取值。

<a id="r_ga4dfd677fa0b1e29c9bc40b463f976233"></a>

```c
#define IIS3DWB_DT_FS_2G 0
```

相关声明：[IIS3DWB_DT_FS_2G](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga4dfd677fa0b1e29c9bc40b463f976233)。

量程（Range）：±2 g；灵敏度（Sensitivity）：0.061 mg/LSB。

<a id="r_ga506726fa2f5b4c185f9f0cb2eddbb056"></a>

```c
#define IIS3DWB_DT_FS_16G 1
```

相关声明：[IIS3DWB_DT_FS_16G](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga506726fa2f5b4c185f9f0cb2eddbb056)。

量程（Range）：±16 g；灵敏度（Sensitivity）：0.488 mg/LSB。

<a id="r_ga4a46a69f72d1c6aef0661f391828af25"></a>

```c
#define IIS3DWB_DT_FS_4G 2
```

相关声明：[IIS3DWB_DT_FS_4G](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga4a46a69f72d1c6aef0661f391828af25)。

量程（Range）：±4 g；灵敏度（Sensitivity）：0.122 mg/LSB。

<a id="r_gadc45970b6e6a32be222a0b528e867b91"></a>

```c
#define IIS3DWB_DT_FS_8G 3
```

相关声明：[IIS3DWB_DT_FS_8G](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gadc45970b6e6a32be222a0b528e867b91)。

量程（Range）：±8 g；灵敏度（Sensitivity）：0.244 mg/LSB。

<a id="define-members-2"></a>

### 滤波路径选项（Filter Path Options）

设备树 filter 属性（Property）的值。

选择应用于加速度计输出的数字滤波器（Digital Filter）：斜率（Slope）、高通（HP）或低通（LP），截止频率表示为输出数据率（Output Data Rate，ODR）的某个分数。

<a id="r_gac557e77437f2d658b75005db34e715b3"></a>

```c
#define IIS3DWB_DT_SLOPE_ODR_DIV_4 0x10
```

相关声明：[IIS3DWB_DT_SLOPE_ODR_DIV_4](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gac557e77437f2d658b75005db34e715b3)。

斜率滤波器（Slope Filter），ODR / 4。

<a id="r_ga3411119d55b85413516b88b91782bd28"></a>

```c
#define IIS3DWB_DT_HP_REF_MODE 0x37
```

相关声明：[IIS3DWB_DT_HP_REF_MODE](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga3411119d55b85413516b88b91782bd28)。

高通参考模式（High-pass Reference Mode）。

<a id="r_ga85e76be4aecff12115c17ceaa53e75ec"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_10 0x11
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_10](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga85e76be4aecff12115c17ceaa53e75ec)。

高通（High-pass），ODR / 10。

<a id="r_gaeb389c22f7835affe3e5b7211bd2adc2"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_20 0x12
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_20](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gaeb389c22f7835affe3e5b7211bd2adc2)。

高通（High-pass），ODR / 20。

<a id="r_ga654c694464c036e6bf5b25a5711e029d"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_45 0x13
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_45](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga654c694464c036e6bf5b25a5711e029d)。

高通（High-pass），ODR / 45。

<a id="r_ga8926ea05a80c76e2a6058540807aae0a"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_100 0x14
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_100](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga8926ea05a80c76e2a6058540807aae0a)。

高通（High-pass），ODR / 100。

<a id="r_ga5a426c62af407a029b60206d74fed226"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_200 0x15
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_200](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga5a426c62af407a029b60206d74fed226)。

高通（High-pass），ODR / 200。

<a id="r_ga57114b2257380a1b54a8a8b20538bde7"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_400 0x16
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_400](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga57114b2257380a1b54a8a8b20538bde7)。

高通（High-pass），ODR / 400。

<a id="r_gafce0a98570166feb29c769f2ffe56a08"></a>

```c
#define IIS3DWB_DT_HP_ODR_DIV_800 0x17
```

相关声明：[IIS3DWB_DT_HP_ODR_DIV_800](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gafce0a98570166feb29c769f2ffe56a08)。

高通（High-pass），ODR / 800。

<a id="r_ga33e3ab3cf214aa2190767527ff961a74"></a>

```c
#define IIS3DWB_DT_LP_6k3Hz 0x00
```

相关声明：[IIS3DWB_DT_LP_6k3Hz](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga33e3ab3cf214aa2190767527ff961a74)。

低通（Low-pass），6.3 kHz。

<a id="r_gad25472470cb5211e1a6cfe26a432a1e9"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_4 0x80
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_4](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gad25472470cb5211e1a6cfe26a432a1e9)。

低通（Low-pass），ODR / 4。

<a id="r_ga12881256d83269256cd812077969b3b5"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_10 0x81
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_10](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga12881256d83269256cd812077969b3b5)。

低通（Low-pass），ODR / 10。

<a id="r_ga7747705f6e2777d22651d040bb0adebe"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_20 0x82
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_20](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga7747705f6e2777d22651d040bb0adebe)。

低通（Low-pass），ODR / 20。

<a id="r_ga28dde4ed628eb1e19b766c5bc6dd8a87"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_45 0x83
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_45](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga28dde4ed628eb1e19b766c5bc6dd8a87)。

低通（Low-pass），ODR / 45。

<a id="r_gaf395ae5e9869141e96b9cfb3b7b29b2e"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_100 0x84
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_100](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gaf395ae5e9869141e96b9cfb3b7b29b2e)。

低通（Low-pass），ODR / 100。

<a id="r_ga1c25888dd9cd34b3daff073c6bfe2ea0"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_200 0x85
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_200](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga1c25888dd9cd34b3daff073c6bfe2ea0)。

低通（Low-pass），ODR / 200。

<a id="r_gac1de555dff858c1640179ae2058621e8"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_400 0x86
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_400](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gac1de555dff858c1640179ae2058621e8)。

低通（Low-pass），ODR / 400。

<a id="r_gab3623fb19fc3121fb58a1dd529e770eb"></a>

```c
#define IIS3DWB_DT_LP_ODR_DIV_800 0x87
```

相关声明：[IIS3DWB_DT_LP_ODR_DIV_800](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gab3623fb19fc3121fb58a1dd529e770eb)。

低通（Low-pass），ODR / 800。

<a id="define-members-3"></a>

### 加速度计 FIFO 批量入队速率（Accelerometer FIFO Batching Rate）

设备树 accel-fifo-batch-rate 属性（Property）的值。

<a id="r_ga8a172c5be99ce84cc8c77abfe8fb9578"></a>

```c
#define IIS3DWB_DT_XL_NOT_BATCHED 0x0
```

相关声明：[IIS3DWB_DT_XL_NOT_BATCHED](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga8a172c5be99ce84cc8c77abfe8fb9578)。

不批量入队（Not Batched）。

<a id="r_ga0bc4148870c0f462189807d0b03d335e"></a>

```c
#define IIS3DWB_DT_XL_BATCHED_AT_26k7Hz 0xA
```

相关声明：[IIS3DWB_DT_XL_BATCHED_AT_26k7Hz](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga0bc4148870c0f462189807d0b03d335e)。

频率（Frequency）：26.7 kHz。

<a id="define-members-4"></a>

### 温度 FIFO 批量入队速率（Temperature FIFO Batching Rate）

设备树 temp-fifo-batch-rate 属性（Property）的值。

<a id="r_ga5027e4b865594e7bb26665c74baacca8"></a>

```c
#define IIS3DWB_DT_TEMP_NOT_BATCHED 0
```

相关声明：[IIS3DWB_DT_TEMP_NOT_BATCHED](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga5027e4b865594e7bb26665c74baacca8)。

不批量入队（Not Batched）。

<a id="r_ga20caf830abe63a7e5196b561d7c716ad"></a>

```c
#define IIS3DWB_DT_TEMP_BATCHED_AT_104Hz 3
```

相关声明：[IIS3DWB_DT_TEMP_BATCHED_AT_104Hz](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga20caf830abe63a7e5196b561d7c716ad)。

频率：104 Hz。

<a id="define-members-5"></a>

### FIFO 时间戳抽取（Timestamp Decimation）

设备树 timestamp-fifo-batch-rate 属性（Property）的值。

<a id="r_ga8a7fb4ebabfdc8a27acb89b5ecb21f62"></a>

```c
#define IIS3DWB_DT_TS_NOT_BATCHED 0x0
```

相关声明：[IIS3DWB_DT_TS_NOT_BATCHED](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga8a7fb4ebabfdc8a27acb89b5ecb21f62)。

时间戳不批量入队（Timestamp Not Batched）。

<a id="r_ga9fd77bdd0ee73b255ab4c81fa5989a61"></a>

```c
#define IIS3DWB_DT_DEC_TS_1 0x1
```

相关声明：[IIS3DWB_DT_DEC_TS_1](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga9fd77bdd0ee73b255ab4c81fa5989a61)。

1 倍抽取（Decimation）。

<a id="r_ga51426db564b97a6219e55e91cf32c7a1"></a>

```c
#define IIS3DWB_DT_DEC_TS_8 0x2
```

相关声明：[IIS3DWB_DT_DEC_TS_8](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga51426db564b97a6219e55e91cf32c7a1)。

8 倍抽取（Decimation）。

<a id="r_ga3a8bd2b92d89719836eac5cb7d6f0103"></a>

```c
#define IIS3DWB_DT_DEC_TS_32 0x3
```

相关声明：[IIS3DWB_DT_DEC_TS_32](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga3a8bd2b92d89719836eac5cb7d6f0103)。

32 倍抽取（Decimation）。


## 13.2\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P347_iis3dwb.h_源码浏览.md)
- [IIS3DWB_DT_ODR_OFF](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga6ec4af1218c207cda346c077a58ba5fa)
- [IIS3DWB_DT_ODR_26k7Hz](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga13f02278734157c50fac51a8f09084d9)
- [IIS3DWB_DT_FS_2G](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga4dfd677fa0b1e29c9bc40b463f976233)
- [IIS3DWB_DT_FS_16G](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga506726fa2f5b4c185f9f0cb2eddbb056)
- [IIS3DWB_DT_FS_4G](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga4a46a69f72d1c6aef0661f391828af25)
- [IIS3DWB_DT_FS_8G](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gadc45970b6e6a32be222a0b528e867b91)
- [IIS3DWB_DT_SLOPE_ODR_DIV_4](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gac557e77437f2d658b75005db34e715b3)
- [IIS3DWB_DT_HP_REF_MODE](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga3411119d55b85413516b88b91782bd28)
- [IIS3DWB_DT_HP_ODR_DIV_10](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga85e76be4aecff12115c17ceaa53e75ec)
- [IIS3DWB_DT_HP_ODR_DIV_20](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gaeb389c22f7835affe3e5b7211bd2adc2)
- [IIS3DWB_DT_HP_ODR_DIV_45](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga654c694464c036e6bf5b25a5711e029d)
- [IIS3DWB_DT_HP_ODR_DIV_100](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga8926ea05a80c76e2a6058540807aae0a)
- [IIS3DWB_DT_HP_ODR_DIV_200](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga5a426c62af407a029b60206d74fed226)
- [IIS3DWB_DT_HP_ODR_DIV_400](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga57114b2257380a1b54a8a8b20538bde7)
- [IIS3DWB_DT_HP_ODR_DIV_800](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gafce0a98570166feb29c769f2ffe56a08)
- [IIS3DWB_DT_LP_6k3Hz](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga33e3ab3cf214aa2190767527ff961a74)
- [IIS3DWB_DT_LP_ODR_DIV_4](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gad25472470cb5211e1a6cfe26a432a1e9)
- [IIS3DWB_DT_LP_ODR_DIV_10](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga12881256d83269256cd812077969b3b5)
- [IIS3DWB_DT_LP_ODR_DIV_20](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga7747705f6e2777d22651d040bb0adebe)
- [IIS3DWB_DT_LP_ODR_DIV_45](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga28dde4ed628eb1e19b766c5bc6dd8a87)
- [IIS3DWB_DT_LP_ODR_DIV_100](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gaf395ae5e9869141e96b9cfb3b7b29b2e)
- [IIS3DWB_DT_LP_ODR_DIV_200](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga1c25888dd9cd34b3daff073c6bfe2ea0)
- [IIS3DWB_DT_LP_ODR_DIV_400](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gac1de555dff858c1640179ae2058621e8)
- [IIS3DWB_DT_LP_ODR_DIV_800](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#gab3623fb19fc3121fb58a1dd529e770eb)
- [IIS3DWB_DT_XL_NOT_BATCHED](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga8a172c5be99ce84cc8c77abfe8fb9578)
- [IIS3DWB_DT_XL_BATCHED_AT_26k7Hz](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga0bc4148870c0f462189807d0b03d335e)
- [IIS3DWB_DT_TEMP_NOT_BATCHED](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga5027e4b865594e7bb26665c74baacca8)
- [IIS3DWB_DT_TEMP_BATCHED_AT_104Hz](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga20caf830abe63a7e5196b561d7c716ad)
- [IIS3DWB_DT_TS_NOT_BATCHED](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga8a7fb4ebabfdc8a27acb89b5ecb21f62)
- [IIS3DWB_DT_DEC_TS_1](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga9fd77bdd0ee73b255ab4c81fa5989a61)
- [IIS3DWB_DT_DEC_TS_8](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga51426db564b97a6219e55e91cf32c7a1)
- [IIS3DWB_DT_DEC_TS_32](../api_radio_permission_topic_reference/P012_IIS3DWB API主题.md#ga3a8bd2b92d89719836eac5cb7d6f0103)

<a id="header-details"></a>

---

[上一章](P012_zephyr__bluetooth__classic__hfp_ag.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__dt-bindings__sensor__ina237.h_文件参考.md)
