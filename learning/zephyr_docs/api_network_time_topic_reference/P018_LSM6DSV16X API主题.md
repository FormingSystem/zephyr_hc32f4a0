---
id: learning.zephyr-docs.api-network-time-topic-reference.page-18
title: LSM6DSV16X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv16x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_LSM6DSV16X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv16x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LSM6DSV16X 六轴惯性测量单元（IMU）。

<a id="details"></a>

STMicroelectronics LSM6DSV16X 六轴惯性测量单元（6-axis IMU）。整个系列共用输出数据率（ODR）及先进先出缓冲区（FIFO）设置；参见 `LSM6DSVXXX`。

<a id="header-files"></a>
<a id="files"></a>

## 18.1\_文件（Files）

<a id="r_lsm6dsv16x_2Eh"></a>

```c
file lsm6dsv16x.h
```

相关声明：[lsm6dsv16x.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv16x_8h.html)。

the ST LSM6DSV16X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 18.2\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga0062d4a16bf431f8429ae06c1926dd13"></a>

```c
#define LSM6DSV16X_DT_FS_2G 2
```

相关声明：[LSM6DSV16X_DT_FS_2G](#ga0062d4a16bf431f8429ae06c1926dd13)。

量程（range）：±2 g。

<a id="r_ga90b5d8955a2e8d4cfc1741f426433668"></a>

```c
#define LSM6DSV16X_DT_FS_4G 4
```

相关声明：[LSM6DSV16X_DT_FS_4G](#ga90b5d8955a2e8d4cfc1741f426433668)。

量程（range）：±4 g。

<a id="r_ga5416be4ee0699ccf0994c7decfd9637f"></a>

```c
#define LSM6DSV16X_DT_FS_8G 8
```

相关声明：[LSM6DSV16X_DT_FS_8G](#ga5416be4ee0699ccf0994c7decfd9637f)。

量程（range）：±8 g。

<a id="r_ga8106285e2a93c6dfc3b9c704166938e7"></a>

```c
#define LSM6DSV16X_DT_FS_16G 16
```

相关声明：[LSM6DSV16X_DT_FS_16G](#ga8106285e2a93c6dfc3b9c704166938e7)。

量程（range）：±16 g。

## 18.3\_陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_gaba0ad1e516dc73ce4f610474db2cf8f0"></a>

```c
#define LSM6DSV16X_DT_FS_125DPS 0x0
```

相关声明：[LSM6DSV16X_DT_FS_125DPS](#gaba0ad1e516dc73ce4f610474db2cf8f0)。

角速度量程：±125 度／秒（dps）。

<a id="r_ga4b908bb6e1684b69e3023a9b3056461d"></a>

```c
#define LSM6DSV16X_DT_FS_250DPS 0x1
```

相关声明：[LSM6DSV16X_DT_FS_250DPS](#ga4b908bb6e1684b69e3023a9b3056461d)。

角速度量程：±250 度／秒（dps）。

<a id="r_ga02d9fa7e2f077d98c4f6882555f74162"></a>

```c
#define LSM6DSV16X_DT_FS_500DPS 0x2
```

相关声明：[LSM6DSV16X_DT_FS_500DPS](#ga02d9fa7e2f077d98c4f6882555f74162)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga062069e117674a493a3100369c6bae0c"></a>

```c
#define LSM6DSV16X_DT_FS_1000DPS 0x3
```

相关声明：[LSM6DSV16X_DT_FS_1000DPS](#ga062069e117674a493a3100369c6bae0c)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga7568fcc223af82319d884138ff43fcaa"></a>

```c
#define LSM6DSV16X_DT_FS_2000DPS 0x4
```

相关声明：[LSM6DSV16X_DT_FS_2000DPS](#ga7568fcc223af82319d884138ff43fcaa)。

角速度量程：±2000 度／秒（dps）。

<a id="r_gaad0a2d26bab54aff65bcf922db56d5dd"></a>

```c
#define LSM6DSV16X_DT_FS_4000DPS 0xc
```

相关声明：[LSM6DSV16X_DT_FS_4000DPS](#gaad0a2d26bab54aff65bcf922db56d5dd)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。

## 18.4\_详细说明（Detailed Documentation）

<a id="ga062069e117674a493a3100369c6bae0c"></a>

### `LSM6DSV16X_DT_FS_1000DPS`

```c
#define LSM6DSV16X_DT_FS_1000DPS 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

角速度量程：±1000 度／秒（dps）。

<a id="gaba0ad1e516dc73ce4f610474db2cf8f0"></a>

### `LSM6DSV16X_DT_FS_125DPS`

```c
#define LSM6DSV16X_DT_FS_125DPS 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

角速度量程：±125 度／秒（dps）。

<a id="ga8106285e2a93c6dfc3b9c704166938e7"></a>

### `LSM6DSV16X_DT_FS_16G`

```c
#define LSM6DSV16X_DT_FS_16G 16
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

量程（range）：±16 g。

<a id="ga7568fcc223af82319d884138ff43fcaa"></a>

### `LSM6DSV16X_DT_FS_2000DPS`

```c
#define LSM6DSV16X_DT_FS_2000DPS 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

角速度量程：±2000 度／秒（dps）。

<a id="ga4b908bb6e1684b69e3023a9b3056461d"></a>

### `LSM6DSV16X_DT_FS_250DPS`

```c
#define LSM6DSV16X_DT_FS_250DPS 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

角速度量程：±250 度／秒（dps）。

<a id="ga0062d4a16bf431f8429ae06c1926dd13"></a>

### `LSM6DSV16X_DT_FS_2G`

```c
#define LSM6DSV16X_DT_FS_2G 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

量程（range）：±2 g。

<a id="gaad0a2d26bab54aff65bcf922db56d5dd"></a>

### `LSM6DSV16X_DT_FS_4000DPS`

```c
#define LSM6DSV16X_DT_FS_4000DPS 0xc
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

角速度量程（angular-rate range）：±4000 度／秒（dps）。

<a id="ga90b5d8955a2e8d4cfc1741f426433668"></a>

### `LSM6DSV16X_DT_FS_4G`

```c
#define LSM6DSV16X_DT_FS_4G 4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

量程（range）：±4 g。

<a id="ga02d9fa7e2f077d98c4f6882555f74162"></a>

### `LSM6DSV16X_DT_FS_500DPS`

```c
#define LSM6DSV16X_DT_FS_500DPS 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

角速度量程：±500 度／秒（dps）。

<a id="ga5416be4ee0699ccf0994c7decfd9637f"></a>

### `LSM6DSV16X_DT_FS_8G`

```c
#define LSM6DSV16X_DT_FS_8G 8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv16x.h>
```

量程（range）：±8 g。


## 18.5\_原页交叉引用（Cross References）

- [lsm6dsv16x.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv16x_8h.html)
- [LSM6DSVXXX](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P017_指令内存接口（Instruction Memory APIs）.md) · [返回大纲](大纲.md) · [下一章](P019_LSM6DSV32X API主题.md)
