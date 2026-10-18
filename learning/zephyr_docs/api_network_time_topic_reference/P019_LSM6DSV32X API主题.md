---
id: learning.zephyr-docs.api-network-time-topic-reference.page-19
title: LSM6DSV32X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv32x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_LSM6DSV32X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv32x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LSM6DSV32X 六轴惯性测量单元（IMU）。

<a id="details"></a>

STMicroelectronics LSM6DSV32X 六轴惯性测量单元（6-axis IMU）。整个系列共用输出数据率（ODR）及先进先出缓冲区（FIFO）设置；参见 `LSM6DSVXXX`。

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_lsm6dsv32x_2Eh"></a>

```c
file lsm6dsv32x.h
```

相关声明：[lsm6dsv32x.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv32x_8h.html)。

the ST LSM6DSV32X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 19.2\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga63c4f983f8993c3a4eed919d4776ad4f"></a>

```c
#define LSM6DSV32X_DT_FS_4G 4
```

相关声明：[LSM6DSV32X_DT_FS_4G](#ga63c4f983f8993c3a4eed919d4776ad4f)。

量程（range）：±4 g。

<a id="r_ga8827172289d9777ab552bd8223a918cf"></a>

```c
#define LSM6DSV32X_DT_FS_8G 8
```

相关声明：[LSM6DSV32X_DT_FS_8G](#ga8827172289d9777ab552bd8223a918cf)。

量程（range）：±8 g。

<a id="r_ga5c44eece6a3cf2edbf5c176247420d79"></a>

```c
#define LSM6DSV32X_DT_FS_16G 16
```

相关声明：[LSM6DSV32X_DT_FS_16G](#ga5c44eece6a3cf2edbf5c176247420d79)。

量程（range）：±16 g。

<a id="r_ga9f92f49cb9d467499bf5819961513c61"></a>

```c
#define LSM6DSV32X_DT_FS_32G 32
```

相关声明：[LSM6DSV32X_DT_FS_32G](#ga9f92f49cb9d467499bf5819961513c61)。

量程（range）：±32 g。

## 19.3\_陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_ga9b05b356a0ce126863e5f6caac17b2e3"></a>

```c
#define LSM6DSV32X_DT_FS_125DPS 0x0
```

相关声明：[LSM6DSV32X_DT_FS_125DPS](#ga9b05b356a0ce126863e5f6caac17b2e3)。

角速度量程：±125 度／秒（dps）。

<a id="r_ga407ec932b970a2331e7ff1021913966b"></a>

```c
#define LSM6DSV32X_DT_FS_250DPS 0x1
```

相关声明：[LSM6DSV32X_DT_FS_250DPS](#ga407ec932b970a2331e7ff1021913966b)。

角速度量程：±250 度／秒（dps）。

<a id="r_gaf025cfb25f7d1dcfc39c53aeffc29386"></a>

```c
#define LSM6DSV32X_DT_FS_500DPS 0x2
```

相关声明：[LSM6DSV32X_DT_FS_500DPS](#gaf025cfb25f7d1dcfc39c53aeffc29386)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga2e199c568a50a01f18430bcd3de7a5e4"></a>

```c
#define LSM6DSV32X_DT_FS_1000DPS 0x3
```

相关声明：[LSM6DSV32X_DT_FS_1000DPS](#ga2e199c568a50a01f18430bcd3de7a5e4)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga9de191ba9bf3b8182ae5fbd92cae7232"></a>

```c
#define LSM6DSV32X_DT_FS_2000DPS 0x4
```

相关声明：[LSM6DSV32X_DT_FS_2000DPS](#ga9de191ba9bf3b8182ae5fbd92cae7232)。

角速度量程：±2000 度／秒（dps）。

<a id="r_ga904634042980879843517445bccebea8"></a>

```c
#define LSM6DSV32X_DT_FS_4000DPS 0xc
```

相关声明：[LSM6DSV32X_DT_FS_4000DPS](#ga904634042980879843517445bccebea8)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。

## 19.4\_详细说明（Detailed Documentation）

<a id="ga2e199c568a50a01f18430bcd3de7a5e4"></a>

### `LSM6DSV32X_DT_FS_1000DPS`

```c
#define LSM6DSV32X_DT_FS_1000DPS 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

角速度量程：±1000 度／秒（dps）。

<a id="ga9b05b356a0ce126863e5f6caac17b2e3"></a>

### `LSM6DSV32X_DT_FS_125DPS`

```c
#define LSM6DSV32X_DT_FS_125DPS 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

角速度量程：±125 度／秒（dps）。

<a id="ga5c44eece6a3cf2edbf5c176247420d79"></a>

### `LSM6DSV32X_DT_FS_16G`

```c
#define LSM6DSV32X_DT_FS_16G 16
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

量程（range）：±16 g。

<a id="ga9de191ba9bf3b8182ae5fbd92cae7232"></a>

### `LSM6DSV32X_DT_FS_2000DPS`

```c
#define LSM6DSV32X_DT_FS_2000DPS 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

角速度量程：±2000 度／秒（dps）。

<a id="ga407ec932b970a2331e7ff1021913966b"></a>

### `LSM6DSV32X_DT_FS_250DPS`

```c
#define LSM6DSV32X_DT_FS_250DPS 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

角速度量程：±250 度／秒（dps）。

<a id="ga9f92f49cb9d467499bf5819961513c61"></a>

### `LSM6DSV32X_DT_FS_32G`

```c
#define LSM6DSV32X_DT_FS_32G 32
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

量程（range）：±32 g。

<a id="ga904634042980879843517445bccebea8"></a>

### `LSM6DSV32X_DT_FS_4000DPS`

```c
#define LSM6DSV32X_DT_FS_4000DPS 0xc
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

角速度量程（angular-rate range）：±4000 度／秒（dps）。

<a id="ga63c4f983f8993c3a4eed919d4776ad4f"></a>

### `LSM6DSV32X_DT_FS_4G`

```c
#define LSM6DSV32X_DT_FS_4G 4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

量程（range）：±4 g。

<a id="gaf025cfb25f7d1dcfc39c53aeffc29386"></a>

### `LSM6DSV32X_DT_FS_500DPS`

```c
#define LSM6DSV32X_DT_FS_500DPS 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

角速度量程：±500 度／秒（dps）。

<a id="ga8827172289d9777ab552bd8223a918cf"></a>

### `LSM6DSV32X_DT_FS_8G`

```c
#define LSM6DSV32X_DT_FS_8G 8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv32x.h>
```

量程（range）：±8 g。


## 19.5\_原页交叉引用（Cross References）

- [lsm6dsv32x.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv32x_8h.html)
- [LSM6DSVXXX](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P018_LSM6DSV16X API主题.md) · [返回大纲](大纲.md) · [下一章](P020_向量绝对值（Vector Absolute Value）.md)
