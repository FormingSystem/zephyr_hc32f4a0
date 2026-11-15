---
id: learning.zephyr-docs.api-biometric-mesh-topic-reference.page-3
title: LSM9DS1 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_LSM9DS1 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm9ds1__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LSM9DS1 九轴惯性测量单元（IMU），包含加速度计、陀螺仪和磁力计。

<a id="details"></a>

STMicroelectronics LSM9DS1 九轴惯性测量单元（IMU），包含加速度计、陀螺仪和磁力计。

<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_lsm9ds1_2Eh"></a>

```c
file lsm9ds1.h
```

相关声明：[lsm9ds1.h](../api_file_mesh_acpi_reference/P007_zephyr__dt-bindings__sensor__lsm9ds1.h_文件参考.md)。

the ST LSM9DS1 IMU and magnetometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 3.2\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_gaa0f17393c9ff976e0ee0c110ecc72473"></a>

```c
#define LSM9DS1_DT_FS_2G 0
```

相关声明：[LSM9DS1_DT_FS_2G](#gaa0f17393c9ff976e0ee0c110ecc72473)。

量程（range）：±2 g。

<a id="r_ga2db5ff66fa97b7b4bb5915843b1bb6f6"></a>

```c
#define LSM9DS1_DT_FS_16G 1
```

相关声明：[LSM9DS1_DT_FS_16G](#ga2db5ff66fa97b7b4bb5915843b1bb6f6)。

量程（range）：±16 g。

<a id="r_ga7535ca239218a5e9356c6246b938caaf"></a>

```c
#define LSM9DS1_DT_FS_4G 2
```

相关声明：[LSM9DS1_DT_FS_4G](#ga7535ca239218a5e9356c6246b938caaf)。

量程（range）：±4 g。

<a id="r_ga6afa3768fd367db78b1e3f7deac5508e"></a>

```c
#define LSM9DS1_DT_FS_8G 3
```

相关声明：[LSM9DS1_DT_FS_8G](#ga6afa3768fd367db78b1e3f7deac5508e)。

量程（range）：±8 g。

## 3.3\_陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_ga088dba4db0ddde1687db351ed03b1538"></a>

```c
#define LSM9DS1_DT_FS_245DPS 0
```

相关声明：[LSM9DS1_DT_FS_245DPS](#ga088dba4db0ddde1687db351ed03b1538)。

±245 度／秒（Degrees per Second，dps）。

<a id="r_ga8e32311fa33f06c0003d41fac83d4121"></a>

```c
#define LSM9DS1_DT_FS_500DPS 1
```

相关声明：[LSM9DS1_DT_FS_500DPS](#ga8e32311fa33f06c0003d41fac83d4121)。

角速度量程：±500 度／秒（dps）。

<a id="r_gaa6a1e7e28d197dd28b2e13a40a521015"></a>

```c
#define LSM9DS1_DT_FS_2000DPS 3
```

相关声明：[LSM9DS1_DT_FS_2000DPS](#gaa6a1e7e28d197dd28b2e13a40a521015)。

角速度量程：±2000 度／秒（dps）。

## 3.4\_加速度计与陀螺仪输出数据率（Accelerometer and Gyroscope Output Data Rate）

设备树（Devicetree）属性 `imu-odr` 的取值。

每个值选择一种加速度计（XL）与陀螺仪（GY）的速率组合。后缀 `_LP` 选择陀螺仪低功耗模式（Low-Power Mode）。

<a id="r_gab7f0150bb6481d55f759f64f7c502edf"></a>

```c
#define LSM9DS1_IMU_OFF 0x00
```

相关声明：[LSM9DS1_IMU_OFF](#gab7f0150bb6481d55f759f64f7c502edf)。

加速度计（Accelerometer）和陀螺仪（Gyroscope）关闭。

<a id="r_gae897ff93c37f7254c016349cfc48466e"></a>

```c
#define LSM9DS1_GY_OFF_XL_10Hz 0x10
```

相关声明：[LSM9DS1_GY_OFF_XL_10Hz](#gae897ff93c37f7254c016349cfc48466e)。

陀螺仪（GY）关闭，加速度计（XL）为 10 Hz。

<a id="r_ga055b320d6158932562f10ef2d2b96a97"></a>

```c
#define LSM9DS1_GY_OFF_XL_50Hz 0x20
```

相关声明：[LSM9DS1_GY_OFF_XL_50Hz](#ga055b320d6158932562f10ef2d2b96a97)。

陀螺仪（GY）关闭，加速度计（XL）为 50 Hz。

<a id="r_ga4d7b97ebeba2cb8007372755021a5de8"></a>

```c
#define LSM9DS1_GY_OFF_XL_119Hz 0x30
```

相关声明：[LSM9DS1_GY_OFF_XL_119Hz](#ga4d7b97ebeba2cb8007372755021a5de8)。

陀螺仪（GY）关闭，加速度计（XL）为 119 Hz。

<a id="r_gaa9db97ee52368cabd1c3ccd7cbd3f1a4"></a>

```c
#define LSM9DS1_GY_OFF_XL_238Hz 0x40
```

相关声明：[LSM9DS1_GY_OFF_XL_238Hz](#gaa9db97ee52368cabd1c3ccd7cbd3f1a4)。

陀螺仪（GY）关闭，加速度计（XL）为 238 Hz。

<a id="r_gad3318f2c48533b3822d7c6fafe224373"></a>

```c
#define LSM9DS1_GY_OFF_XL_476Hz 0x50
```

相关声明：[LSM9DS1_GY_OFF_XL_476Hz](#gad3318f2c48533b3822d7c6fafe224373)。

陀螺仪（GY）关闭，加速度计（XL）为 476 Hz。

<a id="r_ga086c4d1c8287d40be3437f05f3227db7"></a>

```c
#define LSM9DS1_GY_OFF_XL_952Hz 0x60
```

相关声明：[LSM9DS1_GY_OFF_XL_952Hz](#ga086c4d1c8287d40be3437f05f3227db7)。

陀螺仪（GY）关闭，加速度计（XL）为 952 Hz。

<a id="r_ga393366ba14c5db7ed1a5ff95a85adae7"></a>

```c
#define LSM9DS1_XL_OFF_GY_14Hz9 0x01
```

相关声明：[LSM9DS1_XL_OFF_GY_14Hz9](#ga393366ba14c5db7ed1a5ff95a85adae7)。

加速度计（XL）关闭，陀螺仪（GY）为 14.9 Hz。

<a id="r_gaff981b33a86e8d93268ec9e144c1e761"></a>

```c
#define LSM9DS1_XL_OFF_GY_59Hz5 0x02
```

相关声明：[LSM9DS1_XL_OFF_GY_59Hz5](#gaff981b33a86e8d93268ec9e144c1e761)。

加速度计（XL）关闭，陀螺仪（GY）为 59.5 Hz。

<a id="r_gafe2f271b51a0ea6cf5ce29f03f761054"></a>

```c
#define LSM9DS1_XL_OFF_GY_119Hz 0x03
```

相关声明：[LSM9DS1_XL_OFF_GY_119Hz](#gafe2f271b51a0ea6cf5ce29f03f761054)。

加速度计（XL）关闭，陀螺仪（GY）为 119 Hz。

<a id="r_gaa9d2c6c89ef7bb5d1d543b8bcc39b392"></a>

```c
#define LSM9DS1_XL_OFF_GY_238Hz 0x04
```

相关声明：[LSM9DS1_XL_OFF_GY_238Hz](#gaa9d2c6c89ef7bb5d1d543b8bcc39b392)。

加速度计（XL）关闭，陀螺仪（GY）为 238 Hz。

<a id="r_gaf7af84f2ee96d01fe3f031e5b09217ff"></a>

```c
#define LSM9DS1_XL_OFF_GY_476Hz 0x05
```

相关声明：[LSM9DS1_XL_OFF_GY_476Hz](#gaf7af84f2ee96d01fe3f031e5b09217ff)。

加速度计（XL）关闭，陀螺仪（GY）为 476 Hz。

<a id="r_gabcb55995e6b3de4aa23dc804b88eb409"></a>

```c
#define LSM9DS1_XL_OFF_GY_952Hz 0x06
```

相关声明：[LSM9DS1_XL_OFF_GY_952Hz](#gabcb55995e6b3de4aa23dc804b88eb409)。

加速度计（XL）关闭，陀螺仪（GY）为 952 Hz。

<a id="r_gaf65ec4dc4c5075282380da389b68a77b"></a>

```c
#define LSM9DS1_IMU_14Hz9 0x11
```

相关声明：[LSM9DS1_IMU_14Hz9](#gaf65ec4dc4c5075282380da389b68a77b)。

加速度计（XL）与陀螺仪（GY）均为 14.9 Hz。

<a id="r_ga571432113f63d003e7c3e242b6509093"></a>

```c
#define LSM9DS1_IMU_59Hz5 0x22
```

相关声明：[LSM9DS1_IMU_59Hz5](#ga571432113f63d003e7c3e242b6509093)。

加速度计（XL）与陀螺仪（GY）均为 59.5 Hz。

<a id="r_ga71e8c41d54062e315ecd72f933160208"></a>

```c
#define LSM9DS1_IMU_119Hz 0x33
```

相关声明：[LSM9DS1_IMU_119Hz](#ga71e8c41d54062e315ecd72f933160208)。

加速度计（XL）与陀螺仪（GY）均为 119 Hz。

<a id="r_ga3a8b6d1a000a7d4e1fdb6bcc0a70243d"></a>

```c
#define LSM9DS1_IMU_238Hz 0x44
```

相关声明：[LSM9DS1_IMU_238Hz](#ga3a8b6d1a000a7d4e1fdb6bcc0a70243d)。

加速度计（XL）与陀螺仪（GY）均为 238 Hz。

<a id="r_ga5a09b132476058df9906e58d0755386c"></a>

```c
#define LSM9DS1_IMU_476Hz 0x55
```

相关声明：[LSM9DS1_IMU_476Hz](#ga5a09b132476058df9906e58d0755386c)。

加速度计（XL）与陀螺仪（GY）均为 476 Hz。

<a id="r_ga5fe83cf26a6024edeb2ff759ee20d3c8"></a>

```c
#define LSM9DS1_IMU_952Hz 0x66
```

相关声明：[LSM9DS1_IMU_952Hz](#ga5fe83cf26a6024edeb2ff759ee20d3c8)。

加速度计（XL）与陀螺仪（GY）均为 952 Hz。

<a id="r_ga6bbd0b822cc47491d6048f7d71478c9b"></a>

```c
#define LSM9DS1_XL_OFF_GY_14Hz9_LP 0x81
```

相关声明：[LSM9DS1_XL_OFF_GY_14Hz9_LP](#ga6bbd0b822cc47491d6048f7d71478c9b)。

加速度计（XL）关闭，陀螺仪（GY）为 14.9 Hz，低功耗（Low-Power）模式。

<a id="r_gaca3c0f2e322a39f56fa9a5fa70497df6"></a>

```c
#define LSM9DS1_XL_OFF_GY_59Hz5_LP 0x82
```

相关声明：[LSM9DS1_XL_OFF_GY_59Hz5_LP](#gaca3c0f2e322a39f56fa9a5fa70497df6)。

加速度计（XL）关闭，陀螺仪（GY）为 59.5 Hz，低功耗（Low-Power）模式。

<a id="r_ga98e7b9e3924622147f73be90f00bd1ba"></a>

```c
#define LSM9DS1_XL_OFF_GY_119Hz_LP 0x83
```

相关声明：[LSM9DS1_XL_OFF_GY_119Hz_LP](#ga98e7b9e3924622147f73be90f00bd1ba)。

加速度计（XL）关闭，陀螺仪（GY）为 119 Hz，低功耗（Low-Power）模式。

<a id="r_ga61e50f3183b7541a81fe2907752f7375"></a>

```c
#define LSM9DS1_IMU_14Hz9_LP 0x91
```

相关声明：[LSM9DS1_IMU_14Hz9_LP](#ga61e50f3183b7541a81fe2907752f7375)。

加速度计（XL）与陀螺仪（GY）均为 14.9 Hz，低功耗（Low-Power）模式。

<a id="r_ga5b991524e1cec97295c9a1bfdcf31708"></a>

```c
#define LSM9DS1_IMU_59Hz5_LP 0xA2
```

相关声明：[LSM9DS1_IMU_59Hz5_LP](#ga5b991524e1cec97295c9a1bfdcf31708)。

加速度计（XL）与陀螺仪（GY）均为 59.5 Hz，低功耗（Low-Power）模式。

<a id="r_ga20088ff32a83f6a368d36ae138629452"></a>

```c
#define LSM9DS1_IMU_119Hz_LP 0xB3
```

相关声明：[LSM9DS1_IMU_119Hz_LP](#ga20088ff32a83f6a368d36ae138629452)。

加速度计（XL）与陀螺仪（GY）均为 119 Hz，低功耗（Low-Power）模式。

## 3.5\_磁力计满量程范围（Magnetometer Full-Scale Range）

设备树（Devicetree）属性 `mag-range` 的取值。

<a id="r_gaa268b28f8b86b3cef6a82e38609160c9"></a>

```c
#define LSM9DS1_DT_FS_4Ga 0
```

相关声明：[LSM9DS1_DT_FS_4Ga](#gaa268b28f8b86b3cef6a82e38609160c9)。

±4 高斯（Gauss）。

<a id="r_ga3106e0cabbb21625faf2af9ae8250262"></a>

```c
#define LSM9DS1_DT_FS_8Ga 1
```

相关声明：[LSM9DS1_DT_FS_8Ga](#ga3106e0cabbb21625faf2af9ae8250262)。

±8 高斯（Gauss）。

<a id="r_ga539af8febdf954010ef673afe2c5ee73"></a>

```c
#define LSM9DS1_DT_FS_12Ga 2
```

相关声明：[LSM9DS1_DT_FS_12Ga](#ga539af8febdf954010ef673afe2c5ee73)。

±12 高斯（Gauss）。

<a id="r_gacf7c7ab63f7255bac3bebc1f4dc007f3"></a>

```c
#define LSM9DS1_DT_FS_16Ga 3
```

相关声明：[LSM9DS1_DT_FS_16Ga](#gacf7c7ab63f7255bac3bebc1f4dc007f3)。

±16 高斯（Gauss）。

## 3.6\_磁力计输出数据速率（Magnetometer Output Data Rate）

设备树（Devicetree）属性 `mag-odr` 的取值。

LP：低功耗（Low-Power）；MP：中等性能（Medium-Performance）；HP：高性能（High-Performance）；UHP：超高性能（Ultra-High-Performance）模式。

<a id="r_ga7963c9a3003168a8a52dce50054bc96f"></a>

```c
#define LSM9DS1_MAG_POWER_DOWN 0xC0
```

相关声明：[LSM9DS1_MAG_POWER_DOWN](#ga7963c9a3003168a8a52dce50054bc96f)。

掉电（Power-down）。

<a id="r_ga002a92d8c6cf9ba80d80033e972645ef"></a>

```c
#define LSM9DS1_MAG_LP_0Hz625 0x00
```

相关声明：[LSM9DS1_MAG_LP_0Hz625](#ga002a92d8c6cf9ba80d80033e972645ef)。

低功耗（Low-Power，LP）模式，0.625 Hz。

<a id="r_ga13f527ae76cb0677f94968496d530a13"></a>

```c
#define LSM9DS1_MAG_LP_1Hz25 0x01
```

相关声明：[LSM9DS1_MAG_LP_1Hz25](#ga13f527ae76cb0677f94968496d530a13)。

低功耗（Low-Power，LP）模式，1.25 Hz。

<a id="r_ga758b8866ffcd4c654ab457e1f0521d09"></a>

```c
#define LSM9DS1_MAG_LP_2Hz5 0x02
```

相关声明：[LSM9DS1_MAG_LP_2Hz5](#ga758b8866ffcd4c654ab457e1f0521d09)。

低功耗（Low-Power，LP）模式，2.5 Hz。

<a id="r_ga30dcf54cd4be8c55dac82932ad7a37b2"></a>

```c
#define LSM9DS1_MAG_LP_5Hz 0x03
```

相关声明：[LSM9DS1_MAG_LP_5Hz](#ga30dcf54cd4be8c55dac82932ad7a37b2)。

低功耗（Low-Power，LP）模式，5 Hz。

<a id="r_ga9ef4b743a50dfd2b1d5db86bc6495644"></a>

```c
#define LSM9DS1_MAG_LP_10Hz 0x04
```

相关声明：[LSM9DS1_MAG_LP_10Hz](#ga9ef4b743a50dfd2b1d5db86bc6495644)。

低功耗（Low-Power，LP）模式，10 Hz。

<a id="r_ga4e575f4fb5326777f50531556d1353a3"></a>

```c
#define LSM9DS1_MAG_LP_20Hz 0x05
```

相关声明：[LSM9DS1_MAG_LP_20Hz](#ga4e575f4fb5326777f50531556d1353a3)。

低功耗（Low-Power，LP）模式，20 Hz。

<a id="r_ga0b4eaacf63176e5231f137ab0ce56d99"></a>

```c
#define LSM9DS1_MAG_LP_40Hz 0x06
```

相关声明：[LSM9DS1_MAG_LP_40Hz](#ga0b4eaacf63176e5231f137ab0ce56d99)。

低功耗（Low-Power，LP）模式，40 Hz。

<a id="r_ga724fade6479c4f729dec15448df15e97"></a>

```c
#define LSM9DS1_MAG_LP_80Hz 0x07
```

相关声明：[LSM9DS1_MAG_LP_80Hz](#ga724fade6479c4f729dec15448df15e97)。

低功耗（Low-Power，LP）模式，80 Hz。

<a id="r_ga6d6e2f72b0dc4aa6bcd5d15842f65e7f"></a>

```c
#define LSM9DS1_MAG_MP_0Hz625 0x10
```

相关声明：[LSM9DS1_MAG_MP_0Hz625](#ga6d6e2f72b0dc4aa6bcd5d15842f65e7f)。

中等性能（Medium-Performance，MP）模式，0.625 Hz。

<a id="r_gaafe3cfba4bc8cbc7e74e3410aefaea17"></a>

```c
#define LSM9DS1_MAG_MP_1Hz25 0x11
```

相关声明：[LSM9DS1_MAG_MP_1Hz25](#gaafe3cfba4bc8cbc7e74e3410aefaea17)。

中等性能（Medium-Performance，MP）模式，1.25 Hz。

<a id="r_ga106068e9984c230a9044b5c1dca25fa5"></a>

```c
#define LSM9DS1_MAG_MP_2Hz5 0x12
```

相关声明：[LSM9DS1_MAG_MP_2Hz5](#ga106068e9984c230a9044b5c1dca25fa5)。

中等性能（Medium-Performance，MP）模式，2.5 Hz。

<a id="r_ga6ba7628e2ee8564d8fab308eb2a3eef4"></a>

```c
#define LSM9DS1_MAG_MP_5Hz 0x13
```

相关声明：[LSM9DS1_MAG_MP_5Hz](#ga6ba7628e2ee8564d8fab308eb2a3eef4)。

中等性能（Medium-Performance，MP）模式，5 Hz。

<a id="r_gaab920f8d82ff7795dc155482d5c25814"></a>

```c
#define LSM9DS1_MAG_MP_10Hz 0x14
```

相关声明：[LSM9DS1_MAG_MP_10Hz](#gaab920f8d82ff7795dc155482d5c25814)。

中等性能（Medium-Performance，MP）模式，10 Hz。

<a id="r_ga2fefcffec0ca84714c22930bf571cb59"></a>

```c
#define LSM9DS1_MAG_MP_20Hz 0x15
```

相关声明：[LSM9DS1_MAG_MP_20Hz](#ga2fefcffec0ca84714c22930bf571cb59)。

中等性能（Medium-Performance，MP）模式，20 Hz。

<a id="r_ga64d18383987182bf4bf1e53f2b453eac"></a>

```c
#define LSM9DS1_MAG_MP_40Hz 0x16
```

相关声明：[LSM9DS1_MAG_MP_40Hz](#ga64d18383987182bf4bf1e53f2b453eac)。

中等性能（Medium-Performance，MP）模式，40 Hz。

<a id="r_ga3471c091bd2aa1e74806ecb346d6596f"></a>

```c
#define LSM9DS1_MAG_MP_80Hz 0x17
```

相关声明：[LSM9DS1_MAG_MP_80Hz](#ga3471c091bd2aa1e74806ecb346d6596f)。

中等性能（Medium-Performance，MP）模式，80 Hz。

<a id="r_ga8a2acdcf03dbf680d4a426ce40c8febd"></a>

```c
#define LSM9DS1_MAG_HP_0Hz625 0x20
```

相关声明：[LSM9DS1_MAG_HP_0Hz625](#ga8a2acdcf03dbf680d4a426ce40c8febd)。

高性能（High-Performance，HP）模式，0.625 Hz。

<a id="r_ga45dd09f8821be6c22c566b849fdc8809"></a>

```c
#define LSM9DS1_MAG_HP_1Hz25 0x21
```

相关声明：[LSM9DS1_MAG_HP_1Hz25](#ga45dd09f8821be6c22c566b849fdc8809)。

高性能（High-Performance，HP）模式，1.25 Hz。

<a id="r_ga453c9c2cd3c8c3cb06269ca4dd9618d5"></a>

```c
#define LSM9DS1_MAG_HP_2Hz5 0x22
```

相关声明：[LSM9DS1_MAG_HP_2Hz5](#ga453c9c2cd3c8c3cb06269ca4dd9618d5)。

高性能（High-Performance，HP）模式，2.5 Hz。

<a id="r_gafcaa83b806529e561a6aa56c43e11fbf"></a>

```c
#define LSM9DS1_MAG_HP_5Hz 0x23
```

相关声明：[LSM9DS1_MAG_HP_5Hz](#gafcaa83b806529e561a6aa56c43e11fbf)。

高性能（High-Performance，HP）模式，5 Hz。

<a id="r_gaf1b8bbaf138fb569f9940d9ce463ed8d"></a>

```c
#define LSM9DS1_MAG_HP_10Hz 0x24
```

相关声明：[LSM9DS1_MAG_HP_10Hz](#gaf1b8bbaf138fb569f9940d9ce463ed8d)。

高性能（High-Performance，HP）模式，10 Hz。

<a id="r_ga8a36029449d53745c049809e21277694"></a>

```c
#define LSM9DS1_MAG_HP_20Hz 0x25
```

相关声明：[LSM9DS1_MAG_HP_20Hz](#ga8a36029449d53745c049809e21277694)。

高性能（High-Performance，HP）模式，20 Hz。

<a id="r_ga31edee3a33e9a0b80b750db1c65e8b1b"></a>

```c
#define LSM9DS1_MAG_HP_40Hz 0x26
```

相关声明：[LSM9DS1_MAG_HP_40Hz](#ga31edee3a33e9a0b80b750db1c65e8b1b)。

高性能（High-Performance，HP）模式，40 Hz。

<a id="r_ga932221535b82f140d9d27c671b3a1dea"></a>

```c
#define LSM9DS1_MAG_HP_80Hz 0x27
```

相关声明：[LSM9DS1_MAG_HP_80Hz](#ga932221535b82f140d9d27c671b3a1dea)。

高性能（High-Performance，HP）模式，80 Hz。

<a id="r_ga32701c13ef1b3a1f0f7729559494a05e"></a>

```c
#define LSM9DS1_MAG_UHP_0Hz625 0x30
```

相关声明：[LSM9DS1_MAG_UHP_0Hz625](#ga32701c13ef1b3a1f0f7729559494a05e)。

超高性能（Ultra-High-Performance，UHP）模式，0.625 Hz。

<a id="r_ga5fe24fb1f5d2a406988ed21a468a2c65"></a>

```c
#define LSM9DS1_MAG_UHP_1Hz25 0x31
```

相关声明：[LSM9DS1_MAG_UHP_1Hz25](#ga5fe24fb1f5d2a406988ed21a468a2c65)。

超高性能（Ultra-High-Performance，UHP）模式，1.25 Hz。

<a id="r_ga5ee91247f5ac37f1b7039e5f94d812b4"></a>

```c
#define LSM9DS1_MAG_UHP_2Hz5 0x32
```

相关声明：[LSM9DS1_MAG_UHP_2Hz5](#ga5ee91247f5ac37f1b7039e5f94d812b4)。

超高性能（Ultra-High-Performance，UHP）模式，2.5 Hz。

<a id="r_gadec6d523b553139aec1434b4f82f092b"></a>

```c
#define LSM9DS1_MAG_UHP_5Hz 0x33
```

相关声明：[LSM9DS1_MAG_UHP_5Hz](#gadec6d523b553139aec1434b4f82f092b)。

超高性能（Ultra-High-Performance，UHP）模式，5 Hz。

<a id="r_gae984af176e83d363d81eac84fb3d110c"></a>

```c
#define LSM9DS1_MAG_UHP_10Hz 0x34
```

相关声明：[LSM9DS1_MAG_UHP_10Hz](#gae984af176e83d363d81eac84fb3d110c)。

超高性能（Ultra-High-Performance，UHP）模式，10 Hz。

<a id="r_ga52a1f1cb2ec277d35efc15d69d291d7f"></a>

```c
#define LSM9DS1_MAG_UHP_20Hz 0x35
```

相关声明：[LSM9DS1_MAG_UHP_20Hz](#ga52a1f1cb2ec277d35efc15d69d291d7f)。

超高性能（Ultra-High-Performance，UHP）模式，20 Hz。

<a id="r_ga4831ab9b2168d875f3031894264a2628"></a>

```c
#define LSM9DS1_MAG_UHP_40Hz 0x36
```

相关声明：[LSM9DS1_MAG_UHP_40Hz](#ga4831ab9b2168d875f3031894264a2628)。

超高性能（Ultra-High-Performance，UHP）模式，40 Hz。

<a id="r_ga2da3adcf32e4a22b8663ee011317c907"></a>

```c
#define LSM9DS1_MAG_UHP_80Hz 0x37
```

相关声明：[LSM9DS1_MAG_UHP_80Hz](#ga2da3adcf32e4a22b8663ee011317c907)。

超高性能（Ultra-High-Performance，UHP）模式，80 Hz。

<a id="r_gaa0f179e3e3f3c65461e405329d723cec"></a>

```c
#define LSM9DS1_MAG_UHP_155Hz 0x38
```

相关声明：[LSM9DS1_MAG_UHP_155Hz](#gaa0f179e3e3f3c65461e405329d723cec)。

超高性能（Ultra-High-Performance，UHP）模式，155 Hz。

<a id="r_gae7fb9f552e7a91943291b42e14883cfa"></a>

```c
#define LSM9DS1_MAG_HP_300Hz 0x28
```

相关声明：[LSM9DS1_MAG_HP_300Hz](#gae7fb9f552e7a91943291b42e14883cfa)。

高性能（High-Performance，HP）模式，300 Hz。

<a id="r_ga94294a103d745a8967f28df3a9e0e8d6"></a>

```c
#define LSM9DS1_MAG_MP_560Hz 0x18
```

相关声明：[LSM9DS1_MAG_MP_560Hz](#ga94294a103d745a8967f28df3a9e0e8d6)。

中等性能（Medium-Performance，MP）模式，560 Hz。

<a id="r_ga2347bfea0c970effe93f8cc48bb9e567"></a>

```c
#define LSM9DS1_MAG_LP_1000Hz 0x08
```

相关声明：[LSM9DS1_MAG_LP_1000Hz](#ga2347bfea0c970effe93f8cc48bb9e567)。

低功耗（Low-Power，LP）模式，1000 Hz。

<a id="r_ga0f5049091c9bf8123cd6bf110ae95a99"></a>

```c
#define LSM9DS1_MAG_ONE_SHOT 0x70
```

相关声明：[LSM9DS1_MAG_ONE_SHOT](#ga0f5049091c9bf8123cd6bf110ae95a99)。

单次转换（Single/One-Shot Conversion）。

## 3.7\_详细说明（Detailed Documentation）

<a id="ga539af8febdf954010ef673afe2c5ee73"></a>

### `LSM9DS1_DT_FS_12Ga`

```c
#define LSM9DS1_DT_FS_12Ga 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

±12 高斯（Gauss）。

<a id="ga2db5ff66fa97b7b4bb5915843b1bb6f6"></a>

### `LSM9DS1_DT_FS_16G`

```c
#define LSM9DS1_DT_FS_16G 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

量程（range）：±16 g。

<a id="gacf7c7ab63f7255bac3bebc1f4dc007f3"></a>

### `LSM9DS1_DT_FS_16Ga`

```c
#define LSM9DS1_DT_FS_16Ga 3
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

±16 高斯（Gauss）。

<a id="gaa6a1e7e28d197dd28b2e13a40a521015"></a>

### `LSM9DS1_DT_FS_2000DPS`

```c
#define LSM9DS1_DT_FS_2000DPS 3
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

角速度量程：±2000 度／秒（dps）。

<a id="ga088dba4db0ddde1687db351ed03b1538"></a>

### `LSM9DS1_DT_FS_245DPS`

```c
#define LSM9DS1_DT_FS_245DPS 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

±245 度／秒（Degrees per Second，dps）。

<a id="gaa0f17393c9ff976e0ee0c110ecc72473"></a>

### `LSM9DS1_DT_FS_2G`

```c
#define LSM9DS1_DT_FS_2G 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

量程（range）：±2 g。

<a id="ga7535ca239218a5e9356c6246b938caaf"></a>

### `LSM9DS1_DT_FS_4G`

```c
#define LSM9DS1_DT_FS_4G 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

量程（range）：±4 g。

<a id="gaa268b28f8b86b3cef6a82e38609160c9"></a>

### `LSM9DS1_DT_FS_4Ga`

```c
#define LSM9DS1_DT_FS_4Ga 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

±4 高斯（Gauss）。

<a id="ga8e32311fa33f06c0003d41fac83d4121"></a>

### `LSM9DS1_DT_FS_500DPS`

```c
#define LSM9DS1_DT_FS_500DPS 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

角速度量程：±500 度／秒（dps）。

<a id="ga6afa3768fd367db78b1e3f7deac5508e"></a>

### `LSM9DS1_DT_FS_8G`

```c
#define LSM9DS1_DT_FS_8G 3
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

量程（range）：±8 g。

<a id="ga3106e0cabbb21625faf2af9ae8250262"></a>

### `LSM9DS1_DT_FS_8Ga`

```c
#define LSM9DS1_DT_FS_8Ga 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

±8 高斯（Gauss）。

<a id="gae897ff93c37f7254c016349cfc48466e"></a>

### `LSM9DS1_GY_OFF_XL_10Hz`

```c
#define LSM9DS1_GY_OFF_XL_10Hz 0x10
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

陀螺仪（GY）关闭，加速度计（XL）为 10 Hz。

<a id="ga4d7b97ebeba2cb8007372755021a5de8"></a>

### `LSM9DS1_GY_OFF_XL_119Hz`

```c
#define LSM9DS1_GY_OFF_XL_119Hz 0x30
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

陀螺仪（GY）关闭，加速度计（XL）为 119 Hz。

<a id="gaa9db97ee52368cabd1c3ccd7cbd3f1a4"></a>

### `LSM9DS1_GY_OFF_XL_238Hz`

```c
#define LSM9DS1_GY_OFF_XL_238Hz 0x40
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

陀螺仪（GY）关闭，加速度计（XL）为 238 Hz。

<a id="gad3318f2c48533b3822d7c6fafe224373"></a>

### `LSM9DS1_GY_OFF_XL_476Hz`

```c
#define LSM9DS1_GY_OFF_XL_476Hz 0x50
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

陀螺仪（GY）关闭，加速度计（XL）为 476 Hz。

<a id="ga055b320d6158932562f10ef2d2b96a97"></a>

### `LSM9DS1_GY_OFF_XL_50Hz`

```c
#define LSM9DS1_GY_OFF_XL_50Hz 0x20
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

陀螺仪（GY）关闭，加速度计（XL）为 50 Hz。

<a id="ga086c4d1c8287d40be3437f05f3227db7"></a>

### `LSM9DS1_GY_OFF_XL_952Hz`

```c
#define LSM9DS1_GY_OFF_XL_952Hz 0x60
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

陀螺仪（GY）关闭，加速度计（XL）为 952 Hz。

<a id="ga71e8c41d54062e315ecd72f933160208"></a>

### `LSM9DS1_IMU_119Hz`

```c
#define LSM9DS1_IMU_119Hz 0x33
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）与陀螺仪（GY）均为 119 Hz。

<a id="ga20088ff32a83f6a368d36ae138629452"></a>

### `LSM9DS1_IMU_119Hz_LP`

```c
#define LSM9DS1_IMU_119Hz_LP 0xB3
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）与陀螺仪（GY）均为 119 Hz，低功耗（Low-Power）模式。

<a id="gaf65ec4dc4c5075282380da389b68a77b"></a>

### `LSM9DS1_IMU_14Hz9`

```c
#define LSM9DS1_IMU_14Hz9 0x11
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）与陀螺仪（GY）均为 14.9 Hz。

<a id="ga61e50f3183b7541a81fe2907752f7375"></a>

### `LSM9DS1_IMU_14Hz9_LP`

```c
#define LSM9DS1_IMU_14Hz9_LP 0x91
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）与陀螺仪（GY）均为 14.9 Hz，低功耗（Low-Power）模式。

<a id="ga3a8b6d1a000a7d4e1fdb6bcc0a70243d"></a>

### `LSM9DS1_IMU_238Hz`

```c
#define LSM9DS1_IMU_238Hz 0x44
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）与陀螺仪（GY）均为 238 Hz。

<a id="ga5a09b132476058df9906e58d0755386c"></a>

### `LSM9DS1_IMU_476Hz`

```c
#define LSM9DS1_IMU_476Hz 0x55
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）与陀螺仪（GY）均为 476 Hz。

<a id="ga571432113f63d003e7c3e242b6509093"></a>

### `LSM9DS1_IMU_59Hz5`

```c
#define LSM9DS1_IMU_59Hz5 0x22
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）与陀螺仪（GY）均为 59.5 Hz。

<a id="ga5b991524e1cec97295c9a1bfdcf31708"></a>

### `LSM9DS1_IMU_59Hz5_LP`

```c
#define LSM9DS1_IMU_59Hz5_LP 0xA2
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）与陀螺仪（GY）均为 59.5 Hz，低功耗（Low-Power）模式。

<a id="ga5fe83cf26a6024edeb2ff759ee20d3c8"></a>

### `LSM9DS1_IMU_952Hz`

```c
#define LSM9DS1_IMU_952Hz 0x66
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）与陀螺仪（GY）均为 952 Hz。

<a id="gab7f0150bb6481d55f759f64f7c502edf"></a>

### `LSM9DS1_IMU_OFF`

```c
#define LSM9DS1_IMU_OFF 0x00
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（Accelerometer）和陀螺仪（Gyroscope）关闭。

<a id="ga8a2acdcf03dbf680d4a426ce40c8febd"></a>

### `LSM9DS1_MAG_HP_0Hz625`

```c
#define LSM9DS1_MAG_HP_0Hz625 0x20
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

高性能（High-Performance，HP）模式，0.625 Hz。

<a id="gaf1b8bbaf138fb569f9940d9ce463ed8d"></a>

### `LSM9DS1_MAG_HP_10Hz`

```c
#define LSM9DS1_MAG_HP_10Hz 0x24
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

高性能（High-Performance，HP）模式，10 Hz。

<a id="ga45dd09f8821be6c22c566b849fdc8809"></a>

### `LSM9DS1_MAG_HP_1Hz25`

```c
#define LSM9DS1_MAG_HP_1Hz25 0x21
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

高性能（High-Performance，HP）模式，1.25 Hz。

<a id="ga8a36029449d53745c049809e21277694"></a>

### `LSM9DS1_MAG_HP_20Hz`

```c
#define LSM9DS1_MAG_HP_20Hz 0x25
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

高性能（High-Performance，HP）模式，20 Hz。

<a id="ga453c9c2cd3c8c3cb06269ca4dd9618d5"></a>

### `LSM9DS1_MAG_HP_2Hz5`

```c
#define LSM9DS1_MAG_HP_2Hz5 0x22
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

高性能（High-Performance，HP）模式，2.5 Hz。

<a id="gae7fb9f552e7a91943291b42e14883cfa"></a>

### `LSM9DS1_MAG_HP_300Hz`

```c
#define LSM9DS1_MAG_HP_300Hz 0x28
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

高性能（High-Performance，HP）模式，300 Hz。

<a id="ga31edee3a33e9a0b80b750db1c65e8b1b"></a>

### `LSM9DS1_MAG_HP_40Hz`

```c
#define LSM9DS1_MAG_HP_40Hz 0x26
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

高性能（High-Performance，HP）模式，40 Hz。

<a id="gafcaa83b806529e561a6aa56c43e11fbf"></a>

### `LSM9DS1_MAG_HP_5Hz`

```c
#define LSM9DS1_MAG_HP_5Hz 0x23
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

高性能（High-Performance，HP）模式，5 Hz。

<a id="ga932221535b82f140d9d27c671b3a1dea"></a>

### `LSM9DS1_MAG_HP_80Hz`

```c
#define LSM9DS1_MAG_HP_80Hz 0x27
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

高性能（High-Performance，HP）模式，80 Hz。

<a id="ga002a92d8c6cf9ba80d80033e972645ef"></a>

### `LSM9DS1_MAG_LP_0Hz625`

```c
#define LSM9DS1_MAG_LP_0Hz625 0x00
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

低功耗（Low-Power，LP）模式，0.625 Hz。

<a id="ga2347bfea0c970effe93f8cc48bb9e567"></a>

### `LSM9DS1_MAG_LP_1000Hz`

```c
#define LSM9DS1_MAG_LP_1000Hz 0x08
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

低功耗（Low-Power，LP）模式，1000 Hz。

<a id="ga9ef4b743a50dfd2b1d5db86bc6495644"></a>

### `LSM9DS1_MAG_LP_10Hz`

```c
#define LSM9DS1_MAG_LP_10Hz 0x04
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

低功耗（Low-Power，LP）模式，10 Hz。

<a id="ga13f527ae76cb0677f94968496d530a13"></a>

### `LSM9DS1_MAG_LP_1Hz25`

```c
#define LSM9DS1_MAG_LP_1Hz25 0x01
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

低功耗（Low-Power，LP）模式，1.25 Hz。

<a id="ga4e575f4fb5326777f50531556d1353a3"></a>

### `LSM9DS1_MAG_LP_20Hz`

```c
#define LSM9DS1_MAG_LP_20Hz 0x05
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

低功耗（Low-Power，LP）模式，20 Hz。

<a id="ga758b8866ffcd4c654ab457e1f0521d09"></a>

### `LSM9DS1_MAG_LP_2Hz5`

```c
#define LSM9DS1_MAG_LP_2Hz5 0x02
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

低功耗（Low-Power，LP）模式，2.5 Hz。

<a id="ga0b4eaacf63176e5231f137ab0ce56d99"></a>

### `LSM9DS1_MAG_LP_40Hz`

```c
#define LSM9DS1_MAG_LP_40Hz 0x06
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

低功耗（Low-Power，LP）模式，40 Hz。

<a id="ga30dcf54cd4be8c55dac82932ad7a37b2"></a>

### `LSM9DS1_MAG_LP_5Hz`

```c
#define LSM9DS1_MAG_LP_5Hz 0x03
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

低功耗（Low-Power，LP）模式，5 Hz。

<a id="ga724fade6479c4f729dec15448df15e97"></a>

### `LSM9DS1_MAG_LP_80Hz`

```c
#define LSM9DS1_MAG_LP_80Hz 0x07
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

低功耗（Low-Power，LP）模式，80 Hz。

<a id="ga6d6e2f72b0dc4aa6bcd5d15842f65e7f"></a>

### `LSM9DS1_MAG_MP_0Hz625`

```c
#define LSM9DS1_MAG_MP_0Hz625 0x10
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

中等性能（Medium-Performance，MP）模式，0.625 Hz。

<a id="gaab920f8d82ff7795dc155482d5c25814"></a>

### `LSM9DS1_MAG_MP_10Hz`

```c
#define LSM9DS1_MAG_MP_10Hz 0x14
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

中等性能（Medium-Performance，MP）模式，10 Hz。

<a id="gaafe3cfba4bc8cbc7e74e3410aefaea17"></a>

### `LSM9DS1_MAG_MP_1Hz25`

```c
#define LSM9DS1_MAG_MP_1Hz25 0x11
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

中等性能（Medium-Performance，MP）模式，1.25 Hz。

<a id="ga2fefcffec0ca84714c22930bf571cb59"></a>

### `LSM9DS1_MAG_MP_20Hz`

```c
#define LSM9DS1_MAG_MP_20Hz 0x15
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

中等性能（Medium-Performance，MP）模式，20 Hz。

<a id="ga106068e9984c230a9044b5c1dca25fa5"></a>

### `LSM9DS1_MAG_MP_2Hz5`

```c
#define LSM9DS1_MAG_MP_2Hz5 0x12
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

中等性能（Medium-Performance，MP）模式，2.5 Hz。

<a id="ga64d18383987182bf4bf1e53f2b453eac"></a>

### `LSM9DS1_MAG_MP_40Hz`

```c
#define LSM9DS1_MAG_MP_40Hz 0x16
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

中等性能（Medium-Performance，MP）模式，40 Hz。

<a id="ga94294a103d745a8967f28df3a9e0e8d6"></a>

### `LSM9DS1_MAG_MP_560Hz`

```c
#define LSM9DS1_MAG_MP_560Hz 0x18
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

中等性能（Medium-Performance，MP）模式，560 Hz。

<a id="ga6ba7628e2ee8564d8fab308eb2a3eef4"></a>

### `LSM9DS1_MAG_MP_5Hz`

```c
#define LSM9DS1_MAG_MP_5Hz 0x13
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

中等性能（Medium-Performance，MP）模式，5 Hz。

<a id="ga3471c091bd2aa1e74806ecb346d6596f"></a>

### `LSM9DS1_MAG_MP_80Hz`

```c
#define LSM9DS1_MAG_MP_80Hz 0x17
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

中等性能（Medium-Performance，MP）模式，80 Hz。

<a id="ga0f5049091c9bf8123cd6bf110ae95a99"></a>

### `LSM9DS1_MAG_ONE_SHOT`

```c
#define LSM9DS1_MAG_ONE_SHOT 0x70
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

单次转换（Single/One-Shot Conversion）。

<a id="ga7963c9a3003168a8a52dce50054bc96f"></a>

### `LSM9DS1_MAG_POWER_DOWN`

```c
#define LSM9DS1_MAG_POWER_DOWN 0xC0
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

掉电（Power-down）。

<a id="ga32701c13ef1b3a1f0f7729559494a05e"></a>

### `LSM9DS1_MAG_UHP_0Hz625`

```c
#define LSM9DS1_MAG_UHP_0Hz625 0x30
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

超高性能（Ultra-High-Performance，UHP）模式，0.625 Hz。

<a id="gae984af176e83d363d81eac84fb3d110c"></a>

### `LSM9DS1_MAG_UHP_10Hz`

```c
#define LSM9DS1_MAG_UHP_10Hz 0x34
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

超高性能（Ultra-High-Performance，UHP）模式，10 Hz。

<a id="gaa0f179e3e3f3c65461e405329d723cec"></a>

### `LSM9DS1_MAG_UHP_155Hz`

```c
#define LSM9DS1_MAG_UHP_155Hz 0x38
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

超高性能（Ultra-High-Performance，UHP）模式，155 Hz。

<a id="ga5fe24fb1f5d2a406988ed21a468a2c65"></a>

### `LSM9DS1_MAG_UHP_1Hz25`

```c
#define LSM9DS1_MAG_UHP_1Hz25 0x31
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

超高性能（Ultra-High-Performance，UHP）模式，1.25 Hz。

<a id="ga52a1f1cb2ec277d35efc15d69d291d7f"></a>

### `LSM9DS1_MAG_UHP_20Hz`

```c
#define LSM9DS1_MAG_UHP_20Hz 0x35
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

超高性能（Ultra-High-Performance，UHP）模式，20 Hz。

<a id="ga5ee91247f5ac37f1b7039e5f94d812b4"></a>

### `LSM9DS1_MAG_UHP_2Hz5`

```c
#define LSM9DS1_MAG_UHP_2Hz5 0x32
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

超高性能（Ultra-High-Performance，UHP）模式，2.5 Hz。

<a id="ga4831ab9b2168d875f3031894264a2628"></a>

### `LSM9DS1_MAG_UHP_40Hz`

```c
#define LSM9DS1_MAG_UHP_40Hz 0x36
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

超高性能（Ultra-High-Performance，UHP）模式，40 Hz。

<a id="gadec6d523b553139aec1434b4f82f092b"></a>

### `LSM9DS1_MAG_UHP_5Hz`

```c
#define LSM9DS1_MAG_UHP_5Hz 0x33
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

超高性能（Ultra-High-Performance，UHP）模式，5 Hz。

<a id="ga2da3adcf32e4a22b8663ee011317c907"></a>

### `LSM9DS1_MAG_UHP_80Hz`

```c
#define LSM9DS1_MAG_UHP_80Hz 0x37
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

超高性能（Ultra-High-Performance，UHP）模式，80 Hz。

<a id="gafe2f271b51a0ea6cf5ce29f03f761054"></a>

### `LSM9DS1_XL_OFF_GY_119Hz`

```c
#define LSM9DS1_XL_OFF_GY_119Hz 0x03
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）关闭，陀螺仪（GY）为 119 Hz。

<a id="ga98e7b9e3924622147f73be90f00bd1ba"></a>

### `LSM9DS1_XL_OFF_GY_119Hz_LP`

```c
#define LSM9DS1_XL_OFF_GY_119Hz_LP 0x83
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）关闭，陀螺仪（GY）为 119 Hz，低功耗（Low-Power）模式。

<a id="ga393366ba14c5db7ed1a5ff95a85adae7"></a>

### `LSM9DS1_XL_OFF_GY_14Hz9`

```c
#define LSM9DS1_XL_OFF_GY_14Hz9 0x01
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）关闭，陀螺仪（GY）为 14.9 Hz。

<a id="ga6bbd0b822cc47491d6048f7d71478c9b"></a>

### `LSM9DS1_XL_OFF_GY_14Hz9_LP`

```c
#define LSM9DS1_XL_OFF_GY_14Hz9_LP 0x81
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）关闭，陀螺仪（GY）为 14.9 Hz，低功耗（Low-Power）模式。

<a id="gaa9d2c6c89ef7bb5d1d543b8bcc39b392"></a>

### `LSM9DS1_XL_OFF_GY_238Hz`

```c
#define LSM9DS1_XL_OFF_GY_238Hz 0x04
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）关闭，陀螺仪（GY）为 238 Hz。

<a id="gaf7af84f2ee96d01fe3f031e5b09217ff"></a>

### `LSM9DS1_XL_OFF_GY_476Hz`

```c
#define LSM9DS1_XL_OFF_GY_476Hz 0x05
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）关闭，陀螺仪（GY）为 476 Hz。

<a id="gaff981b33a86e8d93268ec9e144c1e761"></a>

### `LSM9DS1_XL_OFF_GY_59Hz5`

```c
#define LSM9DS1_XL_OFF_GY_59Hz5 0x02
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）关闭，陀螺仪（GY）为 59.5 Hz。

<a id="gaca3c0f2e322a39f56fa9a5fa70497df6"></a>

### `LSM9DS1_XL_OFF_GY_59Hz5_LP`

```c
#define LSM9DS1_XL_OFF_GY_59Hz5_LP 0x82
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）关闭，陀螺仪（GY）为 59.5 Hz，低功耗（Low-Power）模式。

<a id="gabcb55995e6b3de4aa23dc804b88eb409"></a>

### `LSM9DS1_XL_OFF_GY_952Hz`

```c
#define LSM9DS1_XL_OFF_GY_952Hz 0x06
```

```c
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>
```

加速度计（XL）关闭，陀螺仪（GY）为 952 Hz。


## 3.8\_原页交叉引用（Cross References）

- [lsm9ds1.h](../api_file_mesh_acpi_reference/P007_zephyr__dt-bindings__sensor__lsm9ds1.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_访问层（Access layer）.md) · [返回大纲](大纲.md) · [下一章](P004_NXP S32 正交解码器（QDEC NXP S32）.md)
