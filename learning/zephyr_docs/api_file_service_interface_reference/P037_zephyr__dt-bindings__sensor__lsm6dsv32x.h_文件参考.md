---
id: learning.zephyr-docs.api-file-service-interface-reference.page-37
title: zephyr__dt-bindings__sensor__lsm6dsv32x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv32x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_dt-bindings\_\_sensor\_\_lsm6dsv32x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv32x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LSM6DSV32X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include "lsm6dsvxxx.h"
```

查看此文件的源码。

the ST LSM6DSV32X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 37.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga63c4f983f8993c3a4eed919d4776ad4f"></a>

```c
#define LSM6DSV32X_DT_FS_4G 4
```

相关声明：[LSM6DSV32X_DT_FS_4G](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga63c4f983f8993c3a4eed919d4776ad4f)。

量程（range）：±4 g。

<a id="r_ga8827172289d9777ab552bd8223a918cf"></a>

```c
#define LSM6DSV32X_DT_FS_8G 8
```

相关声明：[LSM6DSV32X_DT_FS_8G](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga8827172289d9777ab552bd8223a918cf)。

量程（range）：±8 g。

<a id="r_ga5c44eece6a3cf2edbf5c176247420d79"></a>

```c
#define LSM6DSV32X_DT_FS_16G 16
```

相关声明：[LSM6DSV32X_DT_FS_16G](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga5c44eece6a3cf2edbf5c176247420d79)。

量程（range）：±16 g。

<a id="r_ga9f92f49cb9d467499bf5819961513c61"></a>

```c
#define LSM6DSV32X_DT_FS_32G 32
```

相关声明：[LSM6DSV32X_DT_FS_32G](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga9f92f49cb9d467499bf5819961513c61)。

量程（range）：±32 g。

<a id="define-members-1"></a>

### 陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_ga9b05b356a0ce126863e5f6caac17b2e3"></a>

```c
#define LSM6DSV32X_DT_FS_125DPS 0x0
```

相关声明：[LSM6DSV32X_DT_FS_125DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga9b05b356a0ce126863e5f6caac17b2e3)。

角速度量程：±125 度／秒（dps）。

<a id="r_ga407ec932b970a2331e7ff1021913966b"></a>

```c
#define LSM6DSV32X_DT_FS_250DPS 0x1
```

相关声明：[LSM6DSV32X_DT_FS_250DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga407ec932b970a2331e7ff1021913966b)。

角速度量程：±250 度／秒（dps）。

<a id="r_gaf025cfb25f7d1dcfc39c53aeffc29386"></a>

```c
#define LSM6DSV32X_DT_FS_500DPS 0x2
```

相关声明：[LSM6DSV32X_DT_FS_500DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#gaf025cfb25f7d1dcfc39c53aeffc29386)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga2e199c568a50a01f18430bcd3de7a5e4"></a>

```c
#define LSM6DSV32X_DT_FS_1000DPS 0x3
```

相关声明：[LSM6DSV32X_DT_FS_1000DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga2e199c568a50a01f18430bcd3de7a5e4)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga9de191ba9bf3b8182ae5fbd92cae7232"></a>

```c
#define LSM6DSV32X_DT_FS_2000DPS 0x4
```

相关声明：[LSM6DSV32X_DT_FS_2000DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga9de191ba9bf3b8182ae5fbd92cae7232)。

角速度量程：±2000 度／秒（dps）。

<a id="r_ga904634042980879843517445bccebea8"></a>

```c
#define LSM6DSV32X_DT_FS_4000DPS 0xc
```

相关声明：[LSM6DSV32X_DT_FS_4000DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga904634042980879843517445bccebea8)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。


## 37.2\_原页交叉引用（Cross References）

- [lsm6dsvxxx.h](../api_source_reference/P207_lsm6dsvxxx.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P463_lsm6dsv32x.h_源码浏览.md)
- [LSM6DSV32X_DT_FS_4G](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga63c4f983f8993c3a4eed919d4776ad4f)
- [LSM6DSV32X_DT_FS_8G](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga8827172289d9777ab552bd8223a918cf)
- [LSM6DSV32X_DT_FS_16G](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga5c44eece6a3cf2edbf5c176247420d79)
- [LSM6DSV32X_DT_FS_32G](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga9f92f49cb9d467499bf5819961513c61)
- [LSM6DSV32X_DT_FS_125DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga9b05b356a0ce126863e5f6caac17b2e3)
- [LSM6DSV32X_DT_FS_250DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga407ec932b970a2331e7ff1021913966b)
- [LSM6DSV32X_DT_FS_500DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#gaf025cfb25f7d1dcfc39c53aeffc29386)
- [LSM6DSV32X_DT_FS_1000DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga2e199c568a50a01f18430bcd3de7a5e4)
- [LSM6DSV32X_DT_FS_2000DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga9de191ba9bf3b8182ae5fbd92cae7232)
- [LSM6DSV32X_DT_FS_4000DPS](../api_network_time_topic_reference/P019_LSM6DSV32X API主题.md#ga904634042980879843517445bccebea8)

<a id="header-details"></a>

---

[上一章](P036_zephyr__dt-bindings__sensor__lsm6dsv320x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__dt-bindings__sensor__lsm6dsv80x.h_文件参考.md)
