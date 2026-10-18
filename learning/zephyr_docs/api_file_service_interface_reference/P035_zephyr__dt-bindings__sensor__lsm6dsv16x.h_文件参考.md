---
id: learning.zephyr-docs.api-file-service-interface-reference.page-35
title: zephyr__dt-bindings__sensor__lsm6dsv16x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv16x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_dt-bindings\_\_sensor\_\_lsm6dsv16x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv16x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LSM6DSV16X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include "lsm6dsvxxx.h"
```

查看此文件的源码。

the ST LSM6DSV16X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 35.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga0062d4a16bf431f8429ae06c1926dd13"></a>

```c
#define LSM6DSV16X_DT_FS_2G 2
```

相关声明：[LSM6DSV16X_DT_FS_2G](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga0062d4a16bf431f8429ae06c1926dd13)。

量程（range）：±2 g。

<a id="r_ga90b5d8955a2e8d4cfc1741f426433668"></a>

```c
#define LSM6DSV16X_DT_FS_4G 4
```

相关声明：[LSM6DSV16X_DT_FS_4G](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga90b5d8955a2e8d4cfc1741f426433668)。

量程（range）：±4 g。

<a id="r_ga5416be4ee0699ccf0994c7decfd9637f"></a>

```c
#define LSM6DSV16X_DT_FS_8G 8
```

相关声明：[LSM6DSV16X_DT_FS_8G](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga5416be4ee0699ccf0994c7decfd9637f)。

量程（range）：±8 g。

<a id="r_ga8106285e2a93c6dfc3b9c704166938e7"></a>

```c
#define LSM6DSV16X_DT_FS_16G 16
```

相关声明：[LSM6DSV16X_DT_FS_16G](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga8106285e2a93c6dfc3b9c704166938e7)。

量程（range）：±16 g。

<a id="define-members-1"></a>

### 陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_gaba0ad1e516dc73ce4f610474db2cf8f0"></a>

```c
#define LSM6DSV16X_DT_FS_125DPS 0x0
```

相关声明：[LSM6DSV16X_DT_FS_125DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#gaba0ad1e516dc73ce4f610474db2cf8f0)。

角速度量程：±125 度／秒（dps）。

<a id="r_ga4b908bb6e1684b69e3023a9b3056461d"></a>

```c
#define LSM6DSV16X_DT_FS_250DPS 0x1
```

相关声明：[LSM6DSV16X_DT_FS_250DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga4b908bb6e1684b69e3023a9b3056461d)。

角速度量程：±250 度／秒（dps）。

<a id="r_ga02d9fa7e2f077d98c4f6882555f74162"></a>

```c
#define LSM6DSV16X_DT_FS_500DPS 0x2
```

相关声明：[LSM6DSV16X_DT_FS_500DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga02d9fa7e2f077d98c4f6882555f74162)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga062069e117674a493a3100369c6bae0c"></a>

```c
#define LSM6DSV16X_DT_FS_1000DPS 0x3
```

相关声明：[LSM6DSV16X_DT_FS_1000DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga062069e117674a493a3100369c6bae0c)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga7568fcc223af82319d884138ff43fcaa"></a>

```c
#define LSM6DSV16X_DT_FS_2000DPS 0x4
```

相关声明：[LSM6DSV16X_DT_FS_2000DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga7568fcc223af82319d884138ff43fcaa)。

角速度量程：±2000 度／秒（dps）。

<a id="r_gaad0a2d26bab54aff65bcf922db56d5dd"></a>

```c
#define LSM6DSV16X_DT_FS_4000DPS 0xc
```

相关声明：[LSM6DSV16X_DT_FS_4000DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#gaad0a2d26bab54aff65bcf922db56d5dd)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。


## 35.2\_原页交叉引用（Cross References）

- [lsm6dsvxxx.h](../api_source_reference/P207_lsm6dsvxxx.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P461_lsm6dsv16x.h_源码浏览.md)
- [LSM6DSV16X_DT_FS_2G](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga0062d4a16bf431f8429ae06c1926dd13)
- [LSM6DSV16X_DT_FS_4G](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga90b5d8955a2e8d4cfc1741f426433668)
- [LSM6DSV16X_DT_FS_8G](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga5416be4ee0699ccf0994c7decfd9637f)
- [LSM6DSV16X_DT_FS_16G](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga8106285e2a93c6dfc3b9c704166938e7)
- [LSM6DSV16X_DT_FS_125DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#gaba0ad1e516dc73ce4f610474db2cf8f0)
- [LSM6DSV16X_DT_FS_250DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga4b908bb6e1684b69e3023a9b3056461d)
- [LSM6DSV16X_DT_FS_500DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga02d9fa7e2f077d98c4f6882555f74162)
- [LSM6DSV16X_DT_FS_1000DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga062069e117674a493a3100369c6bae0c)
- [LSM6DSV16X_DT_FS_2000DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#ga7568fcc223af82319d884138ff43fcaa)
- [LSM6DSV16X_DT_FS_4000DPS](../api_network_time_topic_reference/P018_LSM6DSV16X API主题.md#gaad0a2d26bab54aff65bcf922db56d5dd)

<a id="header-details"></a>

---

[上一章](P034_zephyr__lorawan__emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__dt-bindings__sensor__lsm6dsv320x.h_文件参考.md)
