---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-10
title: LSM6DSO16IS API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dso16is__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_LSM6DSO16IS API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dso16is__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LSM6DSO16IS 六轴惯性测量单元（IMU）。

<a id="details"></a>

STMicroelectronics LSM6DSO16IS 六轴惯性测量单元（IMU）。

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_lsm6dso16is_2Eh"></a>

```c
file lsm6dso16is.h
```

相关声明：[lsm6dso16is.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso16is_8h.html)。

the ST LSM6DSO16IS IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 10.2\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_gaef962f51d056b682499253d924efbebd"></a>

```c
#define LSM6DSO16IS_DT_FS_2G 0
```

相关声明：[LSM6DSO16IS_DT_FS_2G](#gaef962f51d056b682499253d924efbebd)。

量程（range）：±2 g。

<a id="r_gaa5a35dd0a780ef6bcc9e10d3649da6ea"></a>

```c
#define LSM6DSO16IS_DT_FS_16G 1
```

相关声明：[LSM6DSO16IS_DT_FS_16G](#gaa5a35dd0a780ef6bcc9e10d3649da6ea)。

量程（range）：±16 g。

<a id="r_ga4c001f612eeda1cbf4f90fc8b5d152de"></a>

```c
#define LSM6DSO16IS_DT_FS_4G 2
```

相关声明：[LSM6DSO16IS_DT_FS_4G](#ga4c001f612eeda1cbf4f90fc8b5d152de)。

量程（range）：±4 g。

<a id="r_gaaf35c79b724086e52bf23e770672dbfb"></a>

```c
#define LSM6DSO16IS_DT_FS_8G 3
```

相关声明：[LSM6DSO16IS_DT_FS_8G](#gaaf35c79b724086e52bf23e770672dbfb)。

量程（range）：±8 g。

## 10.3\_陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_ga1d0a9442346bae3d5b5a36ad1c3489e8"></a>

```c
#define LSM6DSO16IS_DT_FS_250DPS 0x0
```

相关声明：[LSM6DSO16IS_DT_FS_250DPS](#ga1d0a9442346bae3d5b5a36ad1c3489e8)。

角速度量程：±250 度／秒（dps）。

<a id="r_gaceffc85cca61d470130c161db5c96e07"></a>

```c
#define LSM6DSO16IS_DT_FS_500DPS 0x1
```

相关声明：[LSM6DSO16IS_DT_FS_500DPS](#gaceffc85cca61d470130c161db5c96e07)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga69b6df4545ebb41822bafaca1b874d17"></a>

```c
#define LSM6DSO16IS_DT_FS_1000DPS 0x2
```

相关声明：[LSM6DSO16IS_DT_FS_1000DPS](#ga69b6df4545ebb41822bafaca1b874d17)。

角速度量程：±1000 度／秒（dps）。

<a id="r_gac902aeef5746301643bbfd8cdaa4de58"></a>

```c
#define LSM6DSO16IS_DT_FS_2000DPS 0x3
```

相关声明：[LSM6DSO16IS_DT_FS_2000DPS](#gac902aeef5746301643bbfd8cdaa4de58)。

角速度量程：±2000 度／秒（dps）。

<a id="r_gada2187a79f7a1760cd51b9013db3116b"></a>

```c
#define LSM6DSO16IS_DT_FS_125DPS 0x10
```

相关声明：[LSM6DSO16IS_DT_FS_125DPS](#gada2187a79f7a1760cd51b9013db3116b)。

角速度量程：±125 度／秒（dps）。

## 10.4\_加速度计与陀螺仪输出数据率（Accelerometer and Gyroscope Output Data Rate）

设备树（Devicetree）属性 `accel-odr` 和 `gyro-odr` 的取值。

HP：高性能模式（High-performance）；LP：低功耗模式（Low-power）。

<a id="r_ga4ba627f0619a454d6ef51cd96bd16899"></a>

```c
#define LSM6DSO16IS_DT_ODR_OFF 0x0
```

相关声明：[LSM6DSO16IS_DT_ODR_OFF](#ga4ba627f0619a454d6ef51cd96bd16899)。

掉电（Power-down）。

<a id="r_gab8f3e866915d67db14c2542b0e0daf7a"></a>

```c
#define LSM6DSO16IS_DT_ODR_12Hz5_HP 0x1
```

相关声明：[LSM6DSO16IS_DT_ODR_12Hz5_HP](#gab8f3e866915d67db14c2542b0e0daf7a)。

12.5 Hz，高性能模式（HP, High-performance）。

<a id="r_ga0b207e36eccb0cd6925c892825b92b20"></a>

```c
#define LSM6DSO16IS_DT_ODR_26H_HP 0x2
```

相关声明：[LSM6DSO16IS_DT_ODR_26H_HP](#ga0b207e36eccb0cd6925c892825b92b20)。

26 Hz，高性能模式（HP, High-performance）。

<a id="r_gaf65d338ed7037873e8eeed06f13de32e"></a>

```c
#define LSM6DSO16IS_DT_ODR_52Hz_HP 0x3
```

相关声明：[LSM6DSO16IS_DT_ODR_52Hz_HP](#gaf65d338ed7037873e8eeed06f13de32e)。

52 Hz，高性能模式（HP, High-performance）。

<a id="r_ga9fc5dae1a461c33532eb9886408f826d"></a>

```c
#define LSM6DSO16IS_DT_ODR_104Hz_HP 0x4
```

相关声明：[LSM6DSO16IS_DT_ODR_104Hz_HP](#ga9fc5dae1a461c33532eb9886408f826d)。

104 Hz，高性能模式（HP, High-performance）。

<a id="r_gabf26a667b036d12df116892b61da4c21"></a>

```c
#define LSM6DSO16IS_DT_ODR_208Hz_HP 0x5
```

相关声明：[LSM6DSO16IS_DT_ODR_208Hz_HP](#gabf26a667b036d12df116892b61da4c21)。

208 Hz，高性能模式（HP, High-performance）。

<a id="r_ga3369d95d744f89867ec3bfc72657eabf"></a>

```c
#define LSM6DSO16IS_DT_ODR_416Hz_HP 0x6
```

相关声明：[LSM6DSO16IS_DT_ODR_416Hz_HP](#ga3369d95d744f89867ec3bfc72657eabf)。

416 Hz，高性能模式（HP, High-performance）。

<a id="r_ga4e8db7ad45aae2970ed6b5128054180a"></a>

```c
#define LSM6DSO16IS_DT_ODR_833Hz_HP 0x7
```

相关声明：[LSM6DSO16IS_DT_ODR_833Hz_HP](#ga4e8db7ad45aae2970ed6b5128054180a)。

833 Hz，高性能模式（HP, High-performance）。

<a id="r_gad25ff38e64749fc911d1981283546cd0"></a>

```c
#define LSM6DSO16IS_DT_ODR_1667Hz_HP 0x8
```

相关声明：[LSM6DSO16IS_DT_ODR_1667Hz_HP](#gad25ff38e64749fc911d1981283546cd0)。

1667 Hz，高性能模式（HP, High-performance）。

<a id="r_ga81004a456887572b9df7140e0e85b33c"></a>

```c
#define LSM6DSO16IS_DT_ODR_3333Hz_HP 0x9
```

相关声明：[LSM6DSO16IS_DT_ODR_3333Hz_HP](#ga81004a456887572b9df7140e0e85b33c)。

3333 Hz，高性能模式（HP, High-performance）。

<a id="r_gaf7c0b12cf6995c790a91d513a2046bd8"></a>

```c
#define LSM6DSO16IS_DT_ODR_6667Hz_HP 0xa
```

相关声明：[LSM6DSO16IS_DT_ODR_6667Hz_HP](#gaf7c0b12cf6995c790a91d513a2046bd8)。

6667 Hz，高性能模式（HP, High-performance）。

<a id="r_ga03f8cf22c6e912aa10767c316fb7e2a3"></a>

```c
#define LSM6DSO16IS_DT_ODR_12Hz5_LP 0x11
```

相关声明：[LSM6DSO16IS_DT_ODR_12Hz5_LP](#ga03f8cf22c6e912aa10767c316fb7e2a3)。

12.5 Hz，低功耗模式（LP, Low-power）。

<a id="r_ga752fea530e4977f942cd802299b8f04e"></a>

```c
#define LSM6DSO16IS_DT_ODR_26H_LP 0x12
```

相关声明：[LSM6DSO16IS_DT_ODR_26H_LP](#ga752fea530e4977f942cd802299b8f04e)。

26 Hz，低功耗模式（LP, Low-power）。

<a id="r_gaaa1feb747d3f4156194ad712b6790210"></a>

```c
#define LSM6DSO16IS_DT_ODR_52Hz_LP 0x13
```

相关声明：[LSM6DSO16IS_DT_ODR_52Hz_LP](#gaaa1feb747d3f4156194ad712b6790210)。

52 Hz，低功耗模式（LP, Low-power）。

<a id="r_ga2e827035678f213fc3dcc31f8c439eea"></a>

```c
#define LSM6DSO16IS_DT_ODR_104Hz_LP 0x14
```

相关声明：[LSM6DSO16IS_DT_ODR_104Hz_LP](#ga2e827035678f213fc3dcc31f8c439eea)。

104 Hz，低功耗模式（LP, Low-power）。

<a id="r_ga5b875ba646a4a94cba706f275e056fb8"></a>

```c
#define LSM6DSO16IS_DT_ODR_208Hz_LP 0x15
```

相关声明：[LSM6DSO16IS_DT_ODR_208Hz_LP](#ga5b875ba646a4a94cba706f275e056fb8)。

208 Hz，低功耗模式（LP, Low-power）。

<a id="r_gaa5c131c9bc27d864c19a7eaf3f815a0f"></a>

```c
#define LSM6DSO16IS_DT_ODR_416Hz_LP 0x16
```

相关声明：[LSM6DSO16IS_DT_ODR_416Hz_LP](#gaa5c131c9bc27d864c19a7eaf3f815a0f)。

416 Hz，低功耗模式（LP, Low-power）。

<a id="r_ga1402fda052ab8395909a3c825045fc73"></a>

```c
#define LSM6DSO16IS_DT_ODR_833Hz_LP 0x17
```

相关声明：[LSM6DSO16IS_DT_ODR_833Hz_LP](#ga1402fda052ab8395909a3c825045fc73)。

833 Hz，低功耗模式（LP, Low-power）。

<a id="r_ga6460d76877bad9037e704c262f703c1d"></a>

```c
#define LSM6DSO16IS_DT_ODR_1667Hz_LP 0x18
```

相关声明：[LSM6DSO16IS_DT_ODR_1667Hz_LP](#ga6460d76877bad9037e704c262f703c1d)。

1667 Hz，低功耗模式（LP, Low-power）。

<a id="r_gaf34646135c7fa8351ae55395e4d30b1c"></a>

```c
#define LSM6DSO16IS_DT_ODR_3333Hz_LP 0x19
```

相关声明：[LSM6DSO16IS_DT_ODR_3333Hz_LP](#gaf34646135c7fa8351ae55395e4d30b1c)。

3333 Hz，低功耗模式（LP, Low-power）。

<a id="r_ga36bdc86bb5f3a64db2120340bbd52587"></a>

```c
#define LSM6DSO16IS_DT_ODR_6667Hz_LP 0x1a
```

相关声明：[LSM6DSO16IS_DT_ODR_6667Hz_LP](#ga36bdc86bb5f3a64db2120340bbd52587)。

6667 Hz，低功耗模式（LP, Low-power）。

<a id="r_gab6e4b5abb44d1a0da80b9ce0f8a48169"></a>

```c
#define LSM6DSO16IS_DT_ODR_1Hz6_LP 0x1b
```

相关声明：[LSM6DSO16IS_DT_ODR_1Hz6_LP](#gab6e4b5abb44d1a0da80b9ce0f8a48169)。

1.6 Hz，低功耗模式（LP, Low-power）。

## 10.5\_详细说明（Detailed Documentation）

<a id="ga69b6df4545ebb41822bafaca1b874d17"></a>

### `LSM6DSO16IS_DT_FS_1000DPS`

```c
#define LSM6DSO16IS_DT_FS_1000DPS 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

角速度量程：±1000 度／秒（dps）。

<a id="gada2187a79f7a1760cd51b9013db3116b"></a>

### `LSM6DSO16IS_DT_FS_125DPS`

```c
#define LSM6DSO16IS_DT_FS_125DPS 0x10
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

角速度量程：±125 度／秒（dps）。

<a id="gaa5a35dd0a780ef6bcc9e10d3649da6ea"></a>

### `LSM6DSO16IS_DT_FS_16G`

```c
#define LSM6DSO16IS_DT_FS_16G 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

量程（range）：±16 g。

<a id="gac902aeef5746301643bbfd8cdaa4de58"></a>

### `LSM6DSO16IS_DT_FS_2000DPS`

```c
#define LSM6DSO16IS_DT_FS_2000DPS 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

角速度量程：±2000 度／秒（dps）。

<a id="ga1d0a9442346bae3d5b5a36ad1c3489e8"></a>

### `LSM6DSO16IS_DT_FS_250DPS`

```c
#define LSM6DSO16IS_DT_FS_250DPS 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

角速度量程：±250 度／秒（dps）。

<a id="gaef962f51d056b682499253d924efbebd"></a>

### `LSM6DSO16IS_DT_FS_2G`

```c
#define LSM6DSO16IS_DT_FS_2G 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

量程（range）：±2 g。

<a id="ga4c001f612eeda1cbf4f90fc8b5d152de"></a>

### `LSM6DSO16IS_DT_FS_4G`

```c
#define LSM6DSO16IS_DT_FS_4G 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

量程（range）：±4 g。

<a id="gaceffc85cca61d470130c161db5c96e07"></a>

### `LSM6DSO16IS_DT_FS_500DPS`

```c
#define LSM6DSO16IS_DT_FS_500DPS 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

角速度量程：±500 度／秒（dps）。

<a id="gaaf35c79b724086e52bf23e770672dbfb"></a>

### `LSM6DSO16IS_DT_FS_8G`

```c
#define LSM6DSO16IS_DT_FS_8G 3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

量程（range）：±8 g。

<a id="ga9fc5dae1a461c33532eb9886408f826d"></a>

### `LSM6DSO16IS_DT_ODR_104Hz_HP`

```c
#define LSM6DSO16IS_DT_ODR_104Hz_HP 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

104 Hz，高性能模式（HP, High-performance）。

<a id="ga2e827035678f213fc3dcc31f8c439eea"></a>

### `LSM6DSO16IS_DT_ODR_104Hz_LP`

```c
#define LSM6DSO16IS_DT_ODR_104Hz_LP 0x14
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

104 Hz，低功耗模式（LP, Low-power）。

<a id="gab8f3e866915d67db14c2542b0e0daf7a"></a>

### `LSM6DSO16IS_DT_ODR_12Hz5_HP`

```c
#define LSM6DSO16IS_DT_ODR_12Hz5_HP 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

12.5 Hz，高性能模式（HP, High-performance）。

<a id="ga03f8cf22c6e912aa10767c316fb7e2a3"></a>

### `LSM6DSO16IS_DT_ODR_12Hz5_LP`

```c
#define LSM6DSO16IS_DT_ODR_12Hz5_LP 0x11
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

12.5 Hz，低功耗模式（LP, Low-power）。

<a id="gad25ff38e64749fc911d1981283546cd0"></a>

### `LSM6DSO16IS_DT_ODR_1667Hz_HP`

```c
#define LSM6DSO16IS_DT_ODR_1667Hz_HP 0x8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

1667 Hz，高性能模式（HP, High-performance）。

<a id="ga6460d76877bad9037e704c262f703c1d"></a>

### `LSM6DSO16IS_DT_ODR_1667Hz_LP`

```c
#define LSM6DSO16IS_DT_ODR_1667Hz_LP 0x18
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

1667 Hz，低功耗模式（LP, Low-power）。

<a id="gab6e4b5abb44d1a0da80b9ce0f8a48169"></a>

### `LSM6DSO16IS_DT_ODR_1Hz6_LP`

```c
#define LSM6DSO16IS_DT_ODR_1Hz6_LP 0x1b
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

1.6 Hz，低功耗模式（LP, Low-power）。

<a id="gabf26a667b036d12df116892b61da4c21"></a>

### `LSM6DSO16IS_DT_ODR_208Hz_HP`

```c
#define LSM6DSO16IS_DT_ODR_208Hz_HP 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

208 Hz，高性能模式（HP, High-performance）。

<a id="ga5b875ba646a4a94cba706f275e056fb8"></a>

### `LSM6DSO16IS_DT_ODR_208Hz_LP`

```c
#define LSM6DSO16IS_DT_ODR_208Hz_LP 0x15
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

208 Hz，低功耗模式（LP, Low-power）。

<a id="ga0b207e36eccb0cd6925c892825b92b20"></a>

### `LSM6DSO16IS_DT_ODR_26H_HP`

```c
#define LSM6DSO16IS_DT_ODR_26H_HP 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

26 Hz，高性能模式（HP, High-performance）。

<a id="ga752fea530e4977f942cd802299b8f04e"></a>

### `LSM6DSO16IS_DT_ODR_26H_LP`

```c
#define LSM6DSO16IS_DT_ODR_26H_LP 0x12
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

26 Hz，低功耗模式（LP, Low-power）。

<a id="ga81004a456887572b9df7140e0e85b33c"></a>

### `LSM6DSO16IS_DT_ODR_3333Hz_HP`

```c
#define LSM6DSO16IS_DT_ODR_3333Hz_HP 0x9
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

3333 Hz，高性能模式（HP, High-performance）。

<a id="gaf34646135c7fa8351ae55395e4d30b1c"></a>

### `LSM6DSO16IS_DT_ODR_3333Hz_LP`

```c
#define LSM6DSO16IS_DT_ODR_3333Hz_LP 0x19
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

3333 Hz，低功耗模式（LP, Low-power）。

<a id="ga3369d95d744f89867ec3bfc72657eabf"></a>

### `LSM6DSO16IS_DT_ODR_416Hz_HP`

```c
#define LSM6DSO16IS_DT_ODR_416Hz_HP 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

416 Hz，高性能模式（HP, High-performance）。

<a id="gaa5c131c9bc27d864c19a7eaf3f815a0f"></a>

### `LSM6DSO16IS_DT_ODR_416Hz_LP`

```c
#define LSM6DSO16IS_DT_ODR_416Hz_LP 0x16
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

416 Hz，低功耗模式（LP, Low-power）。

<a id="gaf65d338ed7037873e8eeed06f13de32e"></a>

### `LSM6DSO16IS_DT_ODR_52Hz_HP`

```c
#define LSM6DSO16IS_DT_ODR_52Hz_HP 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

52 Hz，高性能模式（HP, High-performance）。

<a id="gaaa1feb747d3f4156194ad712b6790210"></a>

### `LSM6DSO16IS_DT_ODR_52Hz_LP`

```c
#define LSM6DSO16IS_DT_ODR_52Hz_LP 0x13
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

52 Hz，低功耗模式（LP, Low-power）。

<a id="gaf7c0b12cf6995c790a91d513a2046bd8"></a>

### `LSM6DSO16IS_DT_ODR_6667Hz_HP`

```c
#define LSM6DSO16IS_DT_ODR_6667Hz_HP 0xa
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

6667 Hz，高性能模式（HP, High-performance）。

<a id="ga36bdc86bb5f3a64db2120340bbd52587"></a>

### `LSM6DSO16IS_DT_ODR_6667Hz_LP`

```c
#define LSM6DSO16IS_DT_ODR_6667Hz_LP 0x1a
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

6667 Hz，低功耗模式（LP, Low-power）。

<a id="ga4e8db7ad45aae2970ed6b5128054180a"></a>

### `LSM6DSO16IS_DT_ODR_833Hz_HP`

```c
#define LSM6DSO16IS_DT_ODR_833Hz_HP 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

833 Hz，高性能模式（HP, High-performance）。

<a id="ga1402fda052ab8395909a3c825045fc73"></a>

### `LSM6DSO16IS_DT_ODR_833Hz_LP`

```c
#define LSM6DSO16IS_DT_ODR_833Hz_LP 0x17
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

833 Hz，低功耗模式（LP, Low-power）。

<a id="ga4ba627f0619a454d6ef51cd96bd16899"></a>

### `LSM6DSO16IS_DT_ODR_OFF`

```c
#define LSM6DSO16IS_DT_ODR_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso16is.h>
```

掉电（Power-down）。


## 10.6\_原页交叉引用（Cross References）

- [lsm6dso16is.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso16is_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P009_链路层发现协议（Link Layer Discovery Protocol）的定义与辅助工具。.md) · [返回大纲](大纲.md) · [下一章](P011_按需分页 API（Demand Paging APIs）.md)
