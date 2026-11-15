---
id: learning.zephyr-docs.api-file-mesh-acpi-reference.page-7
title: zephyr__dt-bindings__sensor__lsm9ds1.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lsm9ds1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_dt-bindings\_\_sensor\_\_lsm9ds1.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lsm9ds1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LSM9DS1 IMU and magnetometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST LSM9DS1 IMU and magnetometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_gaa0f17393c9ff976e0ee0c110ecc72473"></a>

```c
#define LSM9DS1_DT_FS_2G 0
```

相关声明：[LSM9DS1_DT_FS_2G](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa0f17393c9ff976e0ee0c110ecc72473)。

量程（range）：±2 g。

<a id="r_ga2db5ff66fa97b7b4bb5915843b1bb6f6"></a>

```c
#define LSM9DS1_DT_FS_16G 1
```

相关声明：[LSM9DS1_DT_FS_16G](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga2db5ff66fa97b7b4bb5915843b1bb6f6)。

量程（range）：±16 g。

<a id="r_ga7535ca239218a5e9356c6246b938caaf"></a>

```c
#define LSM9DS1_DT_FS_4G 2
```

相关声明：[LSM9DS1_DT_FS_4G](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga7535ca239218a5e9356c6246b938caaf)。

量程（range）：±4 g。

<a id="r_ga6afa3768fd367db78b1e3f7deac5508e"></a>

```c
#define LSM9DS1_DT_FS_8G 3
```

相关声明：[LSM9DS1_DT_FS_8G](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga6afa3768fd367db78b1e3f7deac5508e)。

量程（range）：±8 g。

<a id="define-members-1"></a>

### 陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_ga088dba4db0ddde1687db351ed03b1538"></a>

```c
#define LSM9DS1_DT_FS_245DPS 0
```

相关声明：[LSM9DS1_DT_FS_245DPS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga088dba4db0ddde1687db351ed03b1538)。

±245 度／秒（Degrees per Second，dps）。

<a id="r_ga8e32311fa33f06c0003d41fac83d4121"></a>

```c
#define LSM9DS1_DT_FS_500DPS 1
```

相关声明：[LSM9DS1_DT_FS_500DPS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga8e32311fa33f06c0003d41fac83d4121)。

角速度量程：±500 度／秒（dps）。

<a id="r_gaa6a1e7e28d197dd28b2e13a40a521015"></a>

```c
#define LSM9DS1_DT_FS_2000DPS 3
```

相关声明：[LSM9DS1_DT_FS_2000DPS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa6a1e7e28d197dd28b2e13a40a521015)。

角速度量程：±2000 度／秒（dps）。

<a id="define-members-2"></a>

### 加速度计与陀螺仪输出数据率（Accelerometer and Gyroscope Output Data Rate）

设备树（Devicetree）属性 `imu-odr` 的取值。

每个值选择一种加速度计（XL）与陀螺仪（GY）的速率组合。后缀 `_LP` 选择陀螺仪低功耗模式（Low-Power Mode）。

<a id="r_gab7f0150bb6481d55f759f64f7c502edf"></a>

```c
#define LSM9DS1_IMU_OFF 0x00
```

相关声明：[LSM9DS1_IMU_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gab7f0150bb6481d55f759f64f7c502edf)。

加速度计（Accelerometer）和陀螺仪（Gyroscope）关闭。

<a id="r_gae897ff93c37f7254c016349cfc48466e"></a>

```c
#define LSM9DS1_GY_OFF_XL_10Hz 0x10
```

相关声明：[LSM9DS1_GY_OFF_XL_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gae897ff93c37f7254c016349cfc48466e)。

陀螺仪（GY）关闭，加速度计（XL）为 10 Hz。

<a id="r_ga055b320d6158932562f10ef2d2b96a97"></a>

```c
#define LSM9DS1_GY_OFF_XL_50Hz 0x20
```

相关声明：[LSM9DS1_GY_OFF_XL_50Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga055b320d6158932562f10ef2d2b96a97)。

陀螺仪（GY）关闭，加速度计（XL）为 50 Hz。

<a id="r_ga4d7b97ebeba2cb8007372755021a5de8"></a>

```c
#define LSM9DS1_GY_OFF_XL_119Hz 0x30
```

相关声明：[LSM9DS1_GY_OFF_XL_119Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga4d7b97ebeba2cb8007372755021a5de8)。

陀螺仪（GY）关闭，加速度计（XL）为 119 Hz。

<a id="r_gaa9db97ee52368cabd1c3ccd7cbd3f1a4"></a>

```c
#define LSM9DS1_GY_OFF_XL_238Hz 0x40
```

相关声明：[LSM9DS1_GY_OFF_XL_238Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa9db97ee52368cabd1c3ccd7cbd3f1a4)。

陀螺仪（GY）关闭，加速度计（XL）为 238 Hz。

<a id="r_gad3318f2c48533b3822d7c6fafe224373"></a>

```c
#define LSM9DS1_GY_OFF_XL_476Hz 0x50
```

相关声明：[LSM9DS1_GY_OFF_XL_476Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gad3318f2c48533b3822d7c6fafe224373)。

陀螺仪（GY）关闭，加速度计（XL）为 476 Hz。

<a id="r_ga086c4d1c8287d40be3437f05f3227db7"></a>

```c
#define LSM9DS1_GY_OFF_XL_952Hz 0x60
```

相关声明：[LSM9DS1_GY_OFF_XL_952Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga086c4d1c8287d40be3437f05f3227db7)。

陀螺仪（GY）关闭，加速度计（XL）为 952 Hz。

<a id="r_ga393366ba14c5db7ed1a5ff95a85adae7"></a>

```c
#define LSM9DS1_XL_OFF_GY_14Hz9 0x01
```

相关声明：[LSM9DS1_XL_OFF_GY_14Hz9](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga393366ba14c5db7ed1a5ff95a85adae7)。

加速度计（XL）关闭，陀螺仪（GY）为 14.9 Hz。

<a id="r_gaff981b33a86e8d93268ec9e144c1e761"></a>

```c
#define LSM9DS1_XL_OFF_GY_59Hz5 0x02
```

相关声明：[LSM9DS1_XL_OFF_GY_59Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaff981b33a86e8d93268ec9e144c1e761)。

加速度计（XL）关闭，陀螺仪（GY）为 59.5 Hz。

<a id="r_gafe2f271b51a0ea6cf5ce29f03f761054"></a>

```c
#define LSM9DS1_XL_OFF_GY_119Hz 0x03
```

相关声明：[LSM9DS1_XL_OFF_GY_119Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gafe2f271b51a0ea6cf5ce29f03f761054)。

加速度计（XL）关闭，陀螺仪（GY）为 119 Hz。

<a id="r_gaa9d2c6c89ef7bb5d1d543b8bcc39b392"></a>

```c
#define LSM9DS1_XL_OFF_GY_238Hz 0x04
```

相关声明：[LSM9DS1_XL_OFF_GY_238Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa9d2c6c89ef7bb5d1d543b8bcc39b392)。

加速度计（XL）关闭，陀螺仪（GY）为 238 Hz。

<a id="r_gaf7af84f2ee96d01fe3f031e5b09217ff"></a>

```c
#define LSM9DS1_XL_OFF_GY_476Hz 0x05
```

相关声明：[LSM9DS1_XL_OFF_GY_476Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaf7af84f2ee96d01fe3f031e5b09217ff)。

加速度计（XL）关闭，陀螺仪（GY）为 476 Hz。

<a id="r_gabcb55995e6b3de4aa23dc804b88eb409"></a>

```c
#define LSM9DS1_XL_OFF_GY_952Hz 0x06
```

相关声明：[LSM9DS1_XL_OFF_GY_952Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gabcb55995e6b3de4aa23dc804b88eb409)。

加速度计（XL）关闭，陀螺仪（GY）为 952 Hz。

<a id="r_gaf65ec4dc4c5075282380da389b68a77b"></a>

```c
#define LSM9DS1_IMU_14Hz9 0x11
```

相关声明：[LSM9DS1_IMU_14Hz9](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaf65ec4dc4c5075282380da389b68a77b)。

加速度计（XL）与陀螺仪（GY）均为 14.9 Hz。

<a id="r_ga571432113f63d003e7c3e242b6509093"></a>

```c
#define LSM9DS1_IMU_59Hz5 0x22
```

相关声明：[LSM9DS1_IMU_59Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga571432113f63d003e7c3e242b6509093)。

加速度计（XL）与陀螺仪（GY）均为 59.5 Hz。

<a id="r_ga71e8c41d54062e315ecd72f933160208"></a>

```c
#define LSM9DS1_IMU_119Hz 0x33
```

相关声明：[LSM9DS1_IMU_119Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga71e8c41d54062e315ecd72f933160208)。

加速度计（XL）与陀螺仪（GY）均为 119 Hz。

<a id="r_ga3a8b6d1a000a7d4e1fdb6bcc0a70243d"></a>

```c
#define LSM9DS1_IMU_238Hz 0x44
```

相关声明：[LSM9DS1_IMU_238Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga3a8b6d1a000a7d4e1fdb6bcc0a70243d)。

加速度计（XL）与陀螺仪（GY）均为 238 Hz。

<a id="r_ga5a09b132476058df9906e58d0755386c"></a>

```c
#define LSM9DS1_IMU_476Hz 0x55
```

相关声明：[LSM9DS1_IMU_476Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5a09b132476058df9906e58d0755386c)。

加速度计（XL）与陀螺仪（GY）均为 476 Hz。

<a id="r_ga5fe83cf26a6024edeb2ff759ee20d3c8"></a>

```c
#define LSM9DS1_IMU_952Hz 0x66
```

相关声明：[LSM9DS1_IMU_952Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5fe83cf26a6024edeb2ff759ee20d3c8)。

加速度计（XL）与陀螺仪（GY）均为 952 Hz。

<a id="r_ga6bbd0b822cc47491d6048f7d71478c9b"></a>

```c
#define LSM9DS1_XL_OFF_GY_14Hz9_LP 0x81
```

相关声明：[LSM9DS1_XL_OFF_GY_14Hz9_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga6bbd0b822cc47491d6048f7d71478c9b)。

加速度计（XL）关闭，陀螺仪（GY）为 14.9 Hz，低功耗（Low-Power）模式。

<a id="r_gaca3c0f2e322a39f56fa9a5fa70497df6"></a>

```c
#define LSM9DS1_XL_OFF_GY_59Hz5_LP 0x82
```

相关声明：[LSM9DS1_XL_OFF_GY_59Hz5_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaca3c0f2e322a39f56fa9a5fa70497df6)。

加速度计（XL）关闭，陀螺仪（GY）为 59.5 Hz，低功耗（Low-Power）模式。

<a id="r_ga98e7b9e3924622147f73be90f00bd1ba"></a>

```c
#define LSM9DS1_XL_OFF_GY_119Hz_LP 0x83
```

相关声明：[LSM9DS1_XL_OFF_GY_119Hz_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga98e7b9e3924622147f73be90f00bd1ba)。

加速度计（XL）关闭，陀螺仪（GY）为 119 Hz，低功耗（Low-Power）模式。

<a id="r_ga61e50f3183b7541a81fe2907752f7375"></a>

```c
#define LSM9DS1_IMU_14Hz9_LP 0x91
```

相关声明：[LSM9DS1_IMU_14Hz9_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga61e50f3183b7541a81fe2907752f7375)。

加速度计（XL）与陀螺仪（GY）均为 14.9 Hz，低功耗（Low-Power）模式。

<a id="r_ga5b991524e1cec97295c9a1bfdcf31708"></a>

```c
#define LSM9DS1_IMU_59Hz5_LP 0xA2
```

相关声明：[LSM9DS1_IMU_59Hz5_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5b991524e1cec97295c9a1bfdcf31708)。

加速度计（XL）与陀螺仪（GY）均为 59.5 Hz，低功耗（Low-Power）模式。

<a id="r_ga20088ff32a83f6a368d36ae138629452"></a>

```c
#define LSM9DS1_IMU_119Hz_LP 0xB3
```

相关声明：[LSM9DS1_IMU_119Hz_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga20088ff32a83f6a368d36ae138629452)。

加速度计（XL）与陀螺仪（GY）均为 119 Hz，低功耗（Low-Power）模式。

<a id="define-members-3"></a>

### 磁力计满量程范围（Magnetometer Full-Scale Range）

设备树（Devicetree）属性 `mag-range` 的取值。

<a id="r_gaa268b28f8b86b3cef6a82e38609160c9"></a>

```c
#define LSM9DS1_DT_FS_4Ga 0
```

相关声明：[LSM9DS1_DT_FS_4Ga](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa268b28f8b86b3cef6a82e38609160c9)。

±4 高斯（Gauss）。

<a id="r_ga3106e0cabbb21625faf2af9ae8250262"></a>

```c
#define LSM9DS1_DT_FS_8Ga 1
```

相关声明：[LSM9DS1_DT_FS_8Ga](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga3106e0cabbb21625faf2af9ae8250262)。

±8 高斯（Gauss）。

<a id="r_ga539af8febdf954010ef673afe2c5ee73"></a>

```c
#define LSM9DS1_DT_FS_12Ga 2
```

相关声明：[LSM9DS1_DT_FS_12Ga](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga539af8febdf954010ef673afe2c5ee73)。

±12 高斯（Gauss）。

<a id="r_gacf7c7ab63f7255bac3bebc1f4dc007f3"></a>

```c
#define LSM9DS1_DT_FS_16Ga 3
```

相关声明：[LSM9DS1_DT_FS_16Ga](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gacf7c7ab63f7255bac3bebc1f4dc007f3)。

±16 高斯（Gauss）。

<a id="define-members-4"></a>

### 磁力计输出数据速率（Magnetometer Output Data Rate）

设备树（Devicetree）属性 `mag-odr` 的取值。

LP：低功耗（Low-Power）；MP：中等性能（Medium-Performance）；HP：高性能（High-Performance）；UHP：超高性能（Ultra-High-Performance）模式。

<a id="r_ga7963c9a3003168a8a52dce50054bc96f"></a>

```c
#define LSM9DS1_MAG_POWER_DOWN 0xC0
```

相关声明：[LSM9DS1_MAG_POWER_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga7963c9a3003168a8a52dce50054bc96f)。

掉电（Power-down）。

<a id="r_ga002a92d8c6cf9ba80d80033e972645ef"></a>

```c
#define LSM9DS1_MAG_LP_0Hz625 0x00
```

相关声明：[LSM9DS1_MAG_LP_0Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga002a92d8c6cf9ba80d80033e972645ef)。

低功耗（Low-Power，LP）模式，0.625 Hz。

<a id="r_ga13f527ae76cb0677f94968496d530a13"></a>

```c
#define LSM9DS1_MAG_LP_1Hz25 0x01
```

相关声明：[LSM9DS1_MAG_LP_1Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga13f527ae76cb0677f94968496d530a13)。

低功耗（Low-Power，LP）模式，1.25 Hz。

<a id="r_ga758b8866ffcd4c654ab457e1f0521d09"></a>

```c
#define LSM9DS1_MAG_LP_2Hz5 0x02
```

相关声明：[LSM9DS1_MAG_LP_2Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga758b8866ffcd4c654ab457e1f0521d09)。

低功耗（Low-Power，LP）模式，2.5 Hz。

<a id="r_ga30dcf54cd4be8c55dac82932ad7a37b2"></a>

```c
#define LSM9DS1_MAG_LP_5Hz 0x03
```

相关声明：[LSM9DS1_MAG_LP_5Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga30dcf54cd4be8c55dac82932ad7a37b2)。

低功耗（Low-Power，LP）模式，5 Hz。

<a id="r_ga9ef4b743a50dfd2b1d5db86bc6495644"></a>

```c
#define LSM9DS1_MAG_LP_10Hz 0x04
```

相关声明：[LSM9DS1_MAG_LP_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga9ef4b743a50dfd2b1d5db86bc6495644)。

低功耗（Low-Power，LP）模式，10 Hz。

<a id="r_ga4e575f4fb5326777f50531556d1353a3"></a>

```c
#define LSM9DS1_MAG_LP_20Hz 0x05
```

相关声明：[LSM9DS1_MAG_LP_20Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga4e575f4fb5326777f50531556d1353a3)。

低功耗（Low-Power，LP）模式，20 Hz。

<a id="r_ga0b4eaacf63176e5231f137ab0ce56d99"></a>

```c
#define LSM9DS1_MAG_LP_40Hz 0x06
```

相关声明：[LSM9DS1_MAG_LP_40Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga0b4eaacf63176e5231f137ab0ce56d99)。

低功耗（Low-Power，LP）模式，40 Hz。

<a id="r_ga724fade6479c4f729dec15448df15e97"></a>

```c
#define LSM9DS1_MAG_LP_80Hz 0x07
```

相关声明：[LSM9DS1_MAG_LP_80Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga724fade6479c4f729dec15448df15e97)。

低功耗（Low-Power，LP）模式，80 Hz。

<a id="r_ga6d6e2f72b0dc4aa6bcd5d15842f65e7f"></a>

```c
#define LSM9DS1_MAG_MP_0Hz625 0x10
```

相关声明：[LSM9DS1_MAG_MP_0Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga6d6e2f72b0dc4aa6bcd5d15842f65e7f)。

中等性能（Medium-Performance，MP）模式，0.625 Hz。

<a id="r_gaafe3cfba4bc8cbc7e74e3410aefaea17"></a>

```c
#define LSM9DS1_MAG_MP_1Hz25 0x11
```

相关声明：[LSM9DS1_MAG_MP_1Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaafe3cfba4bc8cbc7e74e3410aefaea17)。

中等性能（Medium-Performance，MP）模式，1.25 Hz。

<a id="r_ga106068e9984c230a9044b5c1dca25fa5"></a>

```c
#define LSM9DS1_MAG_MP_2Hz5 0x12
```

相关声明：[LSM9DS1_MAG_MP_2Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga106068e9984c230a9044b5c1dca25fa5)。

中等性能（Medium-Performance，MP）模式，2.5 Hz。

<a id="r_ga6ba7628e2ee8564d8fab308eb2a3eef4"></a>

```c
#define LSM9DS1_MAG_MP_5Hz 0x13
```

相关声明：[LSM9DS1_MAG_MP_5Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga6ba7628e2ee8564d8fab308eb2a3eef4)。

中等性能（Medium-Performance，MP）模式，5 Hz。

<a id="r_gaab920f8d82ff7795dc155482d5c25814"></a>

```c
#define LSM9DS1_MAG_MP_10Hz 0x14
```

相关声明：[LSM9DS1_MAG_MP_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaab920f8d82ff7795dc155482d5c25814)。

中等性能（Medium-Performance，MP）模式，10 Hz。

<a id="r_ga2fefcffec0ca84714c22930bf571cb59"></a>

```c
#define LSM9DS1_MAG_MP_20Hz 0x15
```

相关声明：[LSM9DS1_MAG_MP_20Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga2fefcffec0ca84714c22930bf571cb59)。

中等性能（Medium-Performance，MP）模式，20 Hz。

<a id="r_ga64d18383987182bf4bf1e53f2b453eac"></a>

```c
#define LSM9DS1_MAG_MP_40Hz 0x16
```

相关声明：[LSM9DS1_MAG_MP_40Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga64d18383987182bf4bf1e53f2b453eac)。

中等性能（Medium-Performance，MP）模式，40 Hz。

<a id="r_ga3471c091bd2aa1e74806ecb346d6596f"></a>

```c
#define LSM9DS1_MAG_MP_80Hz 0x17
```

相关声明：[LSM9DS1_MAG_MP_80Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga3471c091bd2aa1e74806ecb346d6596f)。

中等性能（Medium-Performance，MP）模式，80 Hz。

<a id="r_ga8a2acdcf03dbf680d4a426ce40c8febd"></a>

```c
#define LSM9DS1_MAG_HP_0Hz625 0x20
```

相关声明：[LSM9DS1_MAG_HP_0Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga8a2acdcf03dbf680d4a426ce40c8febd)。

高性能（High-Performance，HP）模式，0.625 Hz。

<a id="r_ga45dd09f8821be6c22c566b849fdc8809"></a>

```c
#define LSM9DS1_MAG_HP_1Hz25 0x21
```

相关声明：[LSM9DS1_MAG_HP_1Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga45dd09f8821be6c22c566b849fdc8809)。

高性能（High-Performance，HP）模式，1.25 Hz。

<a id="r_ga453c9c2cd3c8c3cb06269ca4dd9618d5"></a>

```c
#define LSM9DS1_MAG_HP_2Hz5 0x22
```

相关声明：[LSM9DS1_MAG_HP_2Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga453c9c2cd3c8c3cb06269ca4dd9618d5)。

高性能（High-Performance，HP）模式，2.5 Hz。

<a id="r_gafcaa83b806529e561a6aa56c43e11fbf"></a>

```c
#define LSM9DS1_MAG_HP_5Hz 0x23
```

相关声明：[LSM9DS1_MAG_HP_5Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gafcaa83b806529e561a6aa56c43e11fbf)。

高性能（High-Performance，HP）模式，5 Hz。

<a id="r_gaf1b8bbaf138fb569f9940d9ce463ed8d"></a>

```c
#define LSM9DS1_MAG_HP_10Hz 0x24
```

相关声明：[LSM9DS1_MAG_HP_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaf1b8bbaf138fb569f9940d9ce463ed8d)。

高性能（High-Performance，HP）模式，10 Hz。

<a id="r_ga8a36029449d53745c049809e21277694"></a>

```c
#define LSM9DS1_MAG_HP_20Hz 0x25
```

相关声明：[LSM9DS1_MAG_HP_20Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga8a36029449d53745c049809e21277694)。

高性能（High-Performance，HP）模式，20 Hz。

<a id="r_ga31edee3a33e9a0b80b750db1c65e8b1b"></a>

```c
#define LSM9DS1_MAG_HP_40Hz 0x26
```

相关声明：[LSM9DS1_MAG_HP_40Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga31edee3a33e9a0b80b750db1c65e8b1b)。

高性能（High-Performance，HP）模式，40 Hz。

<a id="r_ga932221535b82f140d9d27c671b3a1dea"></a>

```c
#define LSM9DS1_MAG_HP_80Hz 0x27
```

相关声明：[LSM9DS1_MAG_HP_80Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga932221535b82f140d9d27c671b3a1dea)。

高性能（High-Performance，HP）模式，80 Hz。

<a id="r_ga32701c13ef1b3a1f0f7729559494a05e"></a>

```c
#define LSM9DS1_MAG_UHP_0Hz625 0x30
```

相关声明：[LSM9DS1_MAG_UHP_0Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga32701c13ef1b3a1f0f7729559494a05e)。

超高性能（Ultra-High-Performance，UHP）模式，0.625 Hz。

<a id="r_ga5fe24fb1f5d2a406988ed21a468a2c65"></a>

```c
#define LSM9DS1_MAG_UHP_1Hz25 0x31
```

相关声明：[LSM9DS1_MAG_UHP_1Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5fe24fb1f5d2a406988ed21a468a2c65)。

超高性能（Ultra-High-Performance，UHP）模式，1.25 Hz。

<a id="r_ga5ee91247f5ac37f1b7039e5f94d812b4"></a>

```c
#define LSM9DS1_MAG_UHP_2Hz5 0x32
```

相关声明：[LSM9DS1_MAG_UHP_2Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5ee91247f5ac37f1b7039e5f94d812b4)。

超高性能（Ultra-High-Performance，UHP）模式，2.5 Hz。

<a id="r_gadec6d523b553139aec1434b4f82f092b"></a>

```c
#define LSM9DS1_MAG_UHP_5Hz 0x33
```

相关声明：[LSM9DS1_MAG_UHP_5Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gadec6d523b553139aec1434b4f82f092b)。

超高性能（Ultra-High-Performance，UHP）模式，5 Hz。

<a id="r_gae984af176e83d363d81eac84fb3d110c"></a>

```c
#define LSM9DS1_MAG_UHP_10Hz 0x34
```

相关声明：[LSM9DS1_MAG_UHP_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gae984af176e83d363d81eac84fb3d110c)。

超高性能（Ultra-High-Performance，UHP）模式，10 Hz。

<a id="r_ga52a1f1cb2ec277d35efc15d69d291d7f"></a>

```c
#define LSM9DS1_MAG_UHP_20Hz 0x35
```

相关声明：[LSM9DS1_MAG_UHP_20Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga52a1f1cb2ec277d35efc15d69d291d7f)。

超高性能（Ultra-High-Performance，UHP）模式，20 Hz。

<a id="r_ga4831ab9b2168d875f3031894264a2628"></a>

```c
#define LSM9DS1_MAG_UHP_40Hz 0x36
```

相关声明：[LSM9DS1_MAG_UHP_40Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga4831ab9b2168d875f3031894264a2628)。

超高性能（Ultra-High-Performance，UHP）模式，40 Hz。

<a id="r_ga2da3adcf32e4a22b8663ee011317c907"></a>

```c
#define LSM9DS1_MAG_UHP_80Hz 0x37
```

相关声明：[LSM9DS1_MAG_UHP_80Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga2da3adcf32e4a22b8663ee011317c907)。

超高性能（Ultra-High-Performance，UHP）模式，80 Hz。

<a id="r_gaa0f179e3e3f3c65461e405329d723cec"></a>

```c
#define LSM9DS1_MAG_UHP_155Hz 0x38
```

相关声明：[LSM9DS1_MAG_UHP_155Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa0f179e3e3f3c65461e405329d723cec)。

超高性能（Ultra-High-Performance，UHP）模式，155 Hz。

<a id="r_gae7fb9f552e7a91943291b42e14883cfa"></a>

```c
#define LSM9DS1_MAG_HP_300Hz 0x28
```

相关声明：[LSM9DS1_MAG_HP_300Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gae7fb9f552e7a91943291b42e14883cfa)。

高性能（High-Performance，HP）模式，300 Hz。

<a id="r_ga94294a103d745a8967f28df3a9e0e8d6"></a>

```c
#define LSM9DS1_MAG_MP_560Hz 0x18
```

相关声明：[LSM9DS1_MAG_MP_560Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga94294a103d745a8967f28df3a9e0e8d6)。

中等性能（Medium-Performance，MP）模式，560 Hz。

<a id="r_ga2347bfea0c970effe93f8cc48bb9e567"></a>

```c
#define LSM9DS1_MAG_LP_1000Hz 0x08
```

相关声明：[LSM9DS1_MAG_LP_1000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga2347bfea0c970effe93f8cc48bb9e567)。

低功耗（Low-Power，LP）模式，1000 Hz。

<a id="r_ga0f5049091c9bf8123cd6bf110ae95a99"></a>

```c
#define LSM9DS1_MAG_ONE_SHOT 0x70
```

相关声明：[LSM9DS1_MAG_ONE_SHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga0f5049091c9bf8123cd6bf110ae95a99)。

单次转换（Single/One-Shot Conversion）。


## 7.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P465_lsm9ds1.h_源码浏览.md)
- [LSM9DS1_DT_FS_2G](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa0f17393c9ff976e0ee0c110ecc72473)
- [LSM9DS1_DT_FS_16G](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga2db5ff66fa97b7b4bb5915843b1bb6f6)
- [LSM9DS1_DT_FS_4G](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga7535ca239218a5e9356c6246b938caaf)
- [LSM9DS1_DT_FS_8G](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga6afa3768fd367db78b1e3f7deac5508e)
- [LSM9DS1_DT_FS_245DPS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga088dba4db0ddde1687db351ed03b1538)
- [LSM9DS1_DT_FS_500DPS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga8e32311fa33f06c0003d41fac83d4121)
- [LSM9DS1_DT_FS_2000DPS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa6a1e7e28d197dd28b2e13a40a521015)
- [LSM9DS1_IMU_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gab7f0150bb6481d55f759f64f7c502edf)
- [LSM9DS1_GY_OFF_XL_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gae897ff93c37f7254c016349cfc48466e)
- [LSM9DS1_GY_OFF_XL_50Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga055b320d6158932562f10ef2d2b96a97)
- [LSM9DS1_GY_OFF_XL_119Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga4d7b97ebeba2cb8007372755021a5de8)
- [LSM9DS1_GY_OFF_XL_238Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa9db97ee52368cabd1c3ccd7cbd3f1a4)
- [LSM9DS1_GY_OFF_XL_476Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gad3318f2c48533b3822d7c6fafe224373)
- [LSM9DS1_GY_OFF_XL_952Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga086c4d1c8287d40be3437f05f3227db7)
- [LSM9DS1_XL_OFF_GY_14Hz9](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga393366ba14c5db7ed1a5ff95a85adae7)
- [LSM9DS1_XL_OFF_GY_59Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaff981b33a86e8d93268ec9e144c1e761)
- [LSM9DS1_XL_OFF_GY_119Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gafe2f271b51a0ea6cf5ce29f03f761054)
- [LSM9DS1_XL_OFF_GY_238Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa9d2c6c89ef7bb5d1d543b8bcc39b392)
- [LSM9DS1_XL_OFF_GY_476Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaf7af84f2ee96d01fe3f031e5b09217ff)
- [LSM9DS1_XL_OFF_GY_952Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gabcb55995e6b3de4aa23dc804b88eb409)
- [LSM9DS1_IMU_14Hz9](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaf65ec4dc4c5075282380da389b68a77b)
- [LSM9DS1_IMU_59Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga571432113f63d003e7c3e242b6509093)
- [LSM9DS1_IMU_119Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga71e8c41d54062e315ecd72f933160208)
- [LSM9DS1_IMU_238Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga3a8b6d1a000a7d4e1fdb6bcc0a70243d)
- [LSM9DS1_IMU_476Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5a09b132476058df9906e58d0755386c)
- [LSM9DS1_IMU_952Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5fe83cf26a6024edeb2ff759ee20d3c8)
- [LSM9DS1_XL_OFF_GY_14Hz9_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga6bbd0b822cc47491d6048f7d71478c9b)
- [LSM9DS1_XL_OFF_GY_59Hz5_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaca3c0f2e322a39f56fa9a5fa70497df6)
- [LSM9DS1_XL_OFF_GY_119Hz_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga98e7b9e3924622147f73be90f00bd1ba)
- [LSM9DS1_IMU_14Hz9_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga61e50f3183b7541a81fe2907752f7375)
- [LSM9DS1_IMU_59Hz5_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5b991524e1cec97295c9a1bfdcf31708)
- [LSM9DS1_IMU_119Hz_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga20088ff32a83f6a368d36ae138629452)
- [LSM9DS1_DT_FS_4Ga](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa268b28f8b86b3cef6a82e38609160c9)
- [LSM9DS1_DT_FS_8Ga](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga3106e0cabbb21625faf2af9ae8250262)
- [LSM9DS1_DT_FS_12Ga](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga539af8febdf954010ef673afe2c5ee73)
- [LSM9DS1_DT_FS_16Ga](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gacf7c7ab63f7255bac3bebc1f4dc007f3)
- [LSM9DS1_MAG_POWER_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga7963c9a3003168a8a52dce50054bc96f)
- [LSM9DS1_MAG_LP_0Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga002a92d8c6cf9ba80d80033e972645ef)
- [LSM9DS1_MAG_LP_1Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga13f527ae76cb0677f94968496d530a13)
- [LSM9DS1_MAG_LP_2Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga758b8866ffcd4c654ab457e1f0521d09)
- [LSM9DS1_MAG_LP_5Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga30dcf54cd4be8c55dac82932ad7a37b2)
- [LSM9DS1_MAG_LP_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga9ef4b743a50dfd2b1d5db86bc6495644)
- [LSM9DS1_MAG_LP_20Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga4e575f4fb5326777f50531556d1353a3)
- [LSM9DS1_MAG_LP_40Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga0b4eaacf63176e5231f137ab0ce56d99)
- [LSM9DS1_MAG_LP_80Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga724fade6479c4f729dec15448df15e97)
- [LSM9DS1_MAG_MP_0Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga6d6e2f72b0dc4aa6bcd5d15842f65e7f)
- [LSM9DS1_MAG_MP_1Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaafe3cfba4bc8cbc7e74e3410aefaea17)
- [LSM9DS1_MAG_MP_2Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga106068e9984c230a9044b5c1dca25fa5)
- [LSM9DS1_MAG_MP_5Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga6ba7628e2ee8564d8fab308eb2a3eef4)
- [LSM9DS1_MAG_MP_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaab920f8d82ff7795dc155482d5c25814)
- [LSM9DS1_MAG_MP_20Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga2fefcffec0ca84714c22930bf571cb59)
- [LSM9DS1_MAG_MP_40Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga64d18383987182bf4bf1e53f2b453eac)
- [LSM9DS1_MAG_MP_80Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga3471c091bd2aa1e74806ecb346d6596f)
- [LSM9DS1_MAG_HP_0Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga8a2acdcf03dbf680d4a426ce40c8febd)
- [LSM9DS1_MAG_HP_1Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga45dd09f8821be6c22c566b849fdc8809)
- [LSM9DS1_MAG_HP_2Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga453c9c2cd3c8c3cb06269ca4dd9618d5)
- [LSM9DS1_MAG_HP_5Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gafcaa83b806529e561a6aa56c43e11fbf)
- [LSM9DS1_MAG_HP_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaf1b8bbaf138fb569f9940d9ce463ed8d)
- [LSM9DS1_MAG_HP_20Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga8a36029449d53745c049809e21277694)
- [LSM9DS1_MAG_HP_40Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga31edee3a33e9a0b80b750db1c65e8b1b)
- [LSM9DS1_MAG_HP_80Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga932221535b82f140d9d27c671b3a1dea)
- [LSM9DS1_MAG_UHP_0Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga32701c13ef1b3a1f0f7729559494a05e)
- [LSM9DS1_MAG_UHP_1Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5fe24fb1f5d2a406988ed21a468a2c65)
- [LSM9DS1_MAG_UHP_2Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga5ee91247f5ac37f1b7039e5f94d812b4)
- [LSM9DS1_MAG_UHP_5Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gadec6d523b553139aec1434b4f82f092b)
- [LSM9DS1_MAG_UHP_10Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gae984af176e83d363d81eac84fb3d110c)
- [LSM9DS1_MAG_UHP_20Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga52a1f1cb2ec277d35efc15d69d291d7f)
- [LSM9DS1_MAG_UHP_40Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga4831ab9b2168d875f3031894264a2628)
- [LSM9DS1_MAG_UHP_80Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga2da3adcf32e4a22b8663ee011317c907)
- [LSM9DS1_MAG_UHP_155Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gaa0f179e3e3f3c65461e405329d723cec)
- [LSM9DS1_MAG_HP_300Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#gae7fb9f552e7a91943291b42e14883cfa)
- [LSM9DS1_MAG_MP_560Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga94294a103d745a8967f28df3a9e0e8d6)
- [LSM9DS1_MAG_LP_1000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga2347bfea0c970effe93f8cc48bb9e567)
- [LSM9DS1_MAG_ONE_SHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html#ga0f5049091c9bf8123cd6bf110ae95a99)

<a id="header-details"></a>

---

[上一章](P006_zephyr__bluetooth__iso.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__dt-bindings__sensor__qdec_nxp_s32.h_文件参考.md)
