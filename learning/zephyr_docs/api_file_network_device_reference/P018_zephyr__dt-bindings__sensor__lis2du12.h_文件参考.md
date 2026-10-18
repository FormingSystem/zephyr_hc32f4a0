---
id: learning.zephyr-docs.api-file-network-device-reference.page-18
title: zephyr__dt-bindings__sensor__lis2du12.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lis2du12_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_dt-bindings\_\_sensor\_\_lis2du12.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lis2du12_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LIS2DU12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST LIS2DU12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga2b42fd439750df2fb03d62a9c657fca1"></a>

```c
#define LIS2DU12_DT_FS_2G 0
```

相关声明：[LIS2DU12_DT_FS_2G](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga2b42fd439750df2fb03d62a9c657fca1)。

量程（range）：±2 g。

<a id="r_ga3465e147dab6ce4b85fbdf2709e39613"></a>

```c
#define LIS2DU12_DT_FS_4G 1
```

相关声明：[LIS2DU12_DT_FS_4G](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga3465e147dab6ce4b85fbdf2709e39613)。

量程（range）：±4 g。

<a id="r_gaf1b1956d5a808fca2dbaab01845bcf5e"></a>

```c
#define LIS2DU12_DT_FS_8G 2
```

相关声明：[LIS2DU12_DT_FS_8G](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gaf1b1956d5a808fca2dbaab01845bcf5e)。

量程（range）：±8 g。

<a id="r_ga07253b36548b1ae59171576a8e7e2115"></a>

```c
#define LIS2DU12_DT_FS_16G 3
```

相关声明：[LIS2DU12_DT_FS_16G](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga07253b36548b1ae59171576a8e7e2115)。

量程（range）：±16 g。

<a id="define-members-1"></a>

### 加速度计输出数据率（Accelerometer output data rate）

设备树（Devicetree）属性 `accel-odr` 的取值。

超低功耗模式（Ultra-low-power Mode，ULP）。

<a id="r_ga3a76a7b040855274d5e8b00ea522654d"></a>

```c
#define LIS2DU12_DT_ODR_OFF 0x00
```

相关声明：[LIS2DU12_DT_ODR_OFF](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga3a76a7b040855274d5e8b00ea522654d)。

掉电（Power-down）。

<a id="r_gac1c54a059fbfb427f975fc0961343e28"></a>

```c
#define LIS2DU12_DT_ODR_AT_1Hz6_ULP 0x01
```

相关声明：[LIS2DU12_DT_ODR_AT_1Hz6_ULP](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gac1c54a059fbfb427f975fc0961343e28)。

1.6 Hz，超低功耗（ULP）模式。

<a id="r_ga64606f40cd014eae9d89c929168c5e0f"></a>

```c
#define LIS2DU12_DT_ODR_AT_3Hz_ULP 0x02
```

相关声明：[LIS2DU12_DT_ODR_AT_3Hz_ULP](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga64606f40cd014eae9d89c929168c5e0f)。

3 Hz，超低功耗（ULP）模式。

<a id="r_gab54ebbbe8991aa268c0dbaae4427fcd8"></a>

```c
#define LIS2DU12_DT_ODR_AT_6Hz_ULP 0x03
```

相关声明：[LIS2DU12_DT_ODR_AT_6Hz_ULP](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gab54ebbbe8991aa268c0dbaae4427fcd8)。

6 Hz，超低功耗（ULP）模式。

<a id="r_gaf135c2f1fd176eef32ee45ec09010213"></a>

```c
#define LIS2DU12_DT_ODR_AT_6Hz 0x04
```

相关声明：[LIS2DU12_DT_ODR_AT_6Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gaf135c2f1fd176eef32ee45ec09010213)。

6 Hz，正常（Normal）模式。

<a id="r_ga421b54616308f44cd796b4553ccbd93d"></a>

```c
#define LIS2DU12_DT_ODR_AT_12Hz 0x05
```

相关声明：[LIS2DU12_DT_ODR_AT_12Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga421b54616308f44cd796b4553ccbd93d)。

12.5 Hz，正常（Normal）模式。

<a id="r_gad3aaa0a89d8e90cac5e67a52b63e2c7e"></a>

```c
#define LIS2DU12_DT_ODR_AT_25Hz 0x06
```

相关声明：[LIS2DU12_DT_ODR_AT_25Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gad3aaa0a89d8e90cac5e67a52b63e2c7e)。

25 Hz，正常（Normal）模式。

<a id="r_gac444fac795f58756c3d5dd469412bba1"></a>

```c
#define LIS2DU12_DT_ODR_AT_50Hz 0x07
```

相关声明：[LIS2DU12_DT_ODR_AT_50Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gac444fac795f58756c3d5dd469412bba1)。

50 Hz，正常（Normal）模式。

<a id="r_ga2f43a631e26e62246d9b198b48b3c10e"></a>

```c
#define LIS2DU12_DT_ODR_AT_100Hz 0x08
```

相关声明：[LIS2DU12_DT_ODR_AT_100Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga2f43a631e26e62246d9b198b48b3c10e)。

100 Hz，正常（Normal）模式。

<a id="r_ga11789548c0055a69e0899dcd8590df07"></a>

```c
#define LIS2DU12_DT_ODR_AT_200Hz 0x09
```

相关声明：[LIS2DU12_DT_ODR_AT_200Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga11789548c0055a69e0899dcd8590df07)。

200 Hz，正常（Normal）模式。

<a id="r_gaa728d2f438efffdcd6eb607efa5db714"></a>

```c
#define LIS2DU12_DT_ODR_AT_400Hz 0x0a
```

相关声明：[LIS2DU12_DT_ODR_AT_400Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gaa728d2f438efffdcd6eb607efa5db714)。

400 Hz，正常（Normal）模式。

<a id="r_ga1ab1a8891428768cbdfedf3f281ff9fb"></a>

```c
#define LIS2DU12_DT_ODR_AT_800Hz 0x0b
```

相关声明：[LIS2DU12_DT_ODR_AT_800Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga1ab1a8891428768cbdfedf3f281ff9fb)。

800 Hz，正常（Normal）模式。

<a id="r_ga5b1ec0132ce400ce9207b100a1926687"></a>

```c
#define LIS2DU12_DT_ODR_TRIG_PIN 0x0e
```

相关声明：[LIS2DU12_DT_ODR_TRIG_PIN](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga5b1ec0132ce400ce9207b100a1926687)。

通过 INT2 执行单次采样（Single-shot），高延迟（High Latency）。

<a id="r_gaf3389a81e1bc4ce6a9965ad6ba828963"></a>

```c
#define LIS2DU12_DT_ODR_TRIG_SW 0x0f
```

相关声明：[LIS2DU12_DT_ODR_TRIG_SW](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gaf3389a81e1bc4ce6a9965ad6ba828963)。

通过总线执行单次采样（Single-shot），高延迟（High Latency）。


## 18.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P443_lis2du12.h_源码浏览.md)
- [LIS2DU12_DT_FS_2G](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga2b42fd439750df2fb03d62a9c657fca1)
- [LIS2DU12_DT_FS_4G](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga3465e147dab6ce4b85fbdf2709e39613)
- [LIS2DU12_DT_FS_8G](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gaf1b1956d5a808fca2dbaab01845bcf5e)
- [LIS2DU12_DT_FS_16G](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga07253b36548b1ae59171576a8e7e2115)
- [LIS2DU12_DT_ODR_OFF](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga3a76a7b040855274d5e8b00ea522654d)
- [LIS2DU12_DT_ODR_AT_1Hz6_ULP](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gac1c54a059fbfb427f975fc0961343e28)
- [LIS2DU12_DT_ODR_AT_3Hz_ULP](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga64606f40cd014eae9d89c929168c5e0f)
- [LIS2DU12_DT_ODR_AT_6Hz_ULP](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gab54ebbbe8991aa268c0dbaae4427fcd8)
- [LIS2DU12_DT_ODR_AT_6Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gaf135c2f1fd176eef32ee45ec09010213)
- [LIS2DU12_DT_ODR_AT_12Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga421b54616308f44cd796b4553ccbd93d)
- [LIS2DU12_DT_ODR_AT_25Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gad3aaa0a89d8e90cac5e67a52b63e2c7e)
- [LIS2DU12_DT_ODR_AT_50Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gac444fac795f58756c3d5dd469412bba1)
- [LIS2DU12_DT_ODR_AT_100Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga2f43a631e26e62246d9b198b48b3c10e)
- [LIS2DU12_DT_ODR_AT_200Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga11789548c0055a69e0899dcd8590df07)
- [LIS2DU12_DT_ODR_AT_400Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gaa728d2f438efffdcd6eb607efa5db714)
- [LIS2DU12_DT_ODR_AT_800Hz](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga1ab1a8891428768cbdfedf3f281ff9fb)
- [LIS2DU12_DT_ODR_TRIG_PIN](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#ga5b1ec0132ce400ce9207b100a1926687)
- [LIS2DU12_DT_ODR_TRIG_SW](../api_update_memory_topic_reference/P007_LIS2DU12 API主题.md#gaf3389a81e1bc4ce6a9965ad6ba828963)

<a id="header-details"></a>

---

[上一章](P017_zephyr__net__ipv4_autoconf.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__mfd__m5pm1.h_文件参考.md)
