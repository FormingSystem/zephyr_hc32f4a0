---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-8
title: zephyr__dt-bindings__sensor__lsm6dso.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_dt-bindings\_\_sensor\_\_lsm6dso.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LSM6DSO IMU的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST LSM6DSO IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计电源模式（Accelerometer Power Modes）

设备树属性（Devicetree Property）`accel-pm` 的取值。

<a id="r_gaa62e5d2a5529d005f4d622ecdf97f8f0"></a>

```c
#define LSM6DSO_DT_XL_HP_MODE 0
```

相关声明：[LSM6DSO_DT_XL_HP_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaa62e5d2a5529d005f4d622ecdf97f8f0)。

高性能模式（High-performance Mode）。

<a id="r_ga031783c6119db7de6138f368c65c0e49"></a>

```c
#define LSM6DSO_DT_XL_LP_NORMAL_MODE 1
```

相关声明：[LSM6DSO_DT_XL_LP_NORMAL_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga031783c6119db7de6138f368c65c0e49)。

低功耗／正常模式（Low-power/Normal Mode）。

<a id="r_gae1fc1b3317d8dac484cc8f094ff453c6"></a>

```c
#define LSM6DSO_DT_XL_ULP_MODE 2
```

相关声明：[LSM6DSO_DT_XL_ULP_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gae1fc1b3317d8dac484cc8f094ff453c6)。

超低功耗模式（Ultra-low-power Mode）。

<a id="define-members-1"></a>

### 陀螺仪电源模式（Gyroscope Power Modes）

设备树属性（Devicetree Property）`gyro-pm` 的取值。

<a id="r_gac6810407924f44016f0f27c44aca22de"></a>

```c
#define LSM6DSO_DT_GY_HP_MODE 0
```

相关声明：[LSM6DSO_DT_GY_HP_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gac6810407924f44016f0f27c44aca22de)。

高性能模式（High-performance Mode）。

<a id="r_gaae6bf6b52db6321cba323a06af6afe4c"></a>

```c
#define LSM6DSO_DT_GY_NORMAL_MODE 1
```

相关声明：[LSM6DSO_DT_GY_NORMAL_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaae6bf6b52db6321cba323a06af6afe4c)。

正常模式（Normal Mode）。

<a id="define-members-2"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga4b6fd691c9843fdce021c027a6c1d38f"></a>

```c
#define LSM6DSO_DT_FS_2G 0
```

相关声明：[LSM6DSO_DT_FS_2G](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga4b6fd691c9843fdce021c027a6c1d38f)。

量程（range）：±2 g。

<a id="r_gaab163b8d605a6433aff9af2c4fb31764"></a>

```c
#define LSM6DSO_DT_FS_16G 1
```

相关声明：[LSM6DSO_DT_FS_16G](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaab163b8d605a6433aff9af2c4fb31764)。

量程（range）：±16 g。

<a id="r_gac6b3e663efb2aa9340480a0a955b97d7"></a>

```c
#define LSM6DSO_DT_FS_4G 2
```

相关声明：[LSM6DSO_DT_FS_4G](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gac6b3e663efb2aa9340480a0a955b97d7)。

量程（range）：±4 g。

<a id="r_gad2f86d00fa1665c011296fa27b4a235c"></a>

```c
#define LSM6DSO_DT_FS_8G 3
```

相关声明：[LSM6DSO_DT_FS_8G](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gad2f86d00fa1665c011296fa27b4a235c)。

量程（range）：±8 g。

<a id="define-members-3"></a>

### 陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_ga3754f6339351a7d1be2b98fab8b88102"></a>

```c
#define LSM6DSO_DT_FS_250DPS 0
```

相关声明：[LSM6DSO_DT_FS_250DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga3754f6339351a7d1be2b98fab8b88102)。

角速度量程：±250 度／秒（dps）。

<a id="r_gae427e045d161c9f90eff4c6e5dee4efe"></a>

```c
#define LSM6DSO_DT_FS_125DPS 1
```

相关声明：[LSM6DSO_DT_FS_125DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gae427e045d161c9f90eff4c6e5dee4efe)。

角速度量程：±125 度／秒（dps）。

<a id="r_ga0edc66177f1cb810257fe8e3460586a4"></a>

```c
#define LSM6DSO_DT_FS_500DPS 2
```

相关声明：[LSM6DSO_DT_FS_500DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga0edc66177f1cb810257fe8e3460586a4)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga862e3383ea2a6db7fea154fe7b5e5f58"></a>

```c
#define LSM6DSO_DT_FS_1000DPS 4
```

相关声明：[LSM6DSO_DT_FS_1000DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga862e3383ea2a6db7fea154fe7b5e5f58)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga5f007e2d998b5eda7c5fd08145665e4e"></a>

```c
#define LSM6DSO_DT_FS_2000DPS 6
```

相关声明：[LSM6DSO_DT_FS_2000DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga5f007e2d998b5eda7c5fd08145665e4e)。

角速度量程：±2000 度／秒（dps）。

<a id="define-members-4"></a>

### 加速度计与陀螺仪输出数据率（Accelerometer and Gyroscope Output Data Rate）

设备树（Devicetree）属性 `accel-odr` 和 `gyro-odr` 的取值。

<a id="r_ga8969b4f07c618f652bf4b15de9d0b5f7"></a>

```c
#define LSM6DSO_DT_ODR_OFF 0x0
```

相关声明：[LSM6DSO_DT_ODR_OFF](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga8969b4f07c618f652bf4b15de9d0b5f7)。

掉电（Power-down）。

<a id="r_ga9f0952fa1854848632b30b59e8145f08"></a>

```c
#define LSM6DSO_DT_ODR_12Hz5 0x1
```

相关声明：[LSM6DSO_DT_ODR_12Hz5](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga9f0952fa1854848632b30b59e8145f08)。

频率：12.5 Hz。

<a id="r_gab8cc4ee8854e45071720c6e97cb9a133"></a>

```c
#define LSM6DSO_DT_ODR_26H 0x2
```

相关声明：[LSM6DSO_DT_ODR_26H](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab8cc4ee8854e45071720c6e97cb9a133)。

频率：26 Hz。

<a id="r_gab172e908c0810d7a57cad2ccd70626b1"></a>

```c
#define LSM6DSO_DT_ODR_52Hz 0x3
```

相关声明：[LSM6DSO_DT_ODR_52Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab172e908c0810d7a57cad2ccd70626b1)。

频率：52 Hz。

<a id="r_ga59b98b9f338fd9cf2d568b14ac5a5410"></a>

```c
#define LSM6DSO_DT_ODR_104Hz 0x4
```

相关声明：[LSM6DSO_DT_ODR_104Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga59b98b9f338fd9cf2d568b14ac5a5410)。

频率：104 Hz。

<a id="r_gaf57d5e0ecb4fba8230d4a69390a4857c"></a>

```c
#define LSM6DSO_DT_ODR_208Hz 0x5
```

相关声明：[LSM6DSO_DT_ODR_208Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaf57d5e0ecb4fba8230d4a69390a4857c)。

频率：208 Hz。

<a id="r_gaeb374d527698dc50af30a2469957da6f"></a>

```c
#define LSM6DSO_DT_ODR_417Hz 0x6
```

相关声明：[LSM6DSO_DT_ODR_417Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaeb374d527698dc50af30a2469957da6f)。

频率（Frequency）：417 Hz。

<a id="r_ga2cb2a2d726eee22c6e5457700a966c9a"></a>

```c
#define LSM6DSO_DT_ODR_833Hz 0x7
```

相关声明：[LSM6DSO_DT_ODR_833Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga2cb2a2d726eee22c6e5457700a966c9a)。

频率：833 Hz。

<a id="r_ga41f7e1ee6c74cd37b707382ccda3474b"></a>

```c
#define LSM6DSO_DT_ODR_1667Hz 0x8
```

相关声明：[LSM6DSO_DT_ODR_1667Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga41f7e1ee6c74cd37b707382ccda3474b)。

频率（Frequency）：1667 Hz。

<a id="r_gab66ab364d747f4b95f68c596effeb143"></a>

```c
#define LSM6DSO_DT_ODR_3333Hz 0x9
```

相关声明：[LSM6DSO_DT_ODR_3333Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab66ab364d747f4b95f68c596effeb143)。

频率（Frequency）：3333 Hz。

<a id="r_ga73b782f5504622e185d60d635397620a"></a>

```c
#define LSM6DSO_DT_ODR_6667Hz 0xa
```

相关声明：[LSM6DSO_DT_ODR_6667Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga73b782f5504622e185d60d635397620a)。

6667 Hz（赫兹）。

<a id="r_ga14963a4bd7e78ba44eb33da3eaa950af"></a>

```c
#define LSM6DSO_DT_ODR_1Hz6 0xb
```

相关声明：[LSM6DSO_DT_ODR_1Hz6](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga14963a4bd7e78ba44eb33da3eaa950af)。

1.6 Hz，低功耗（Low-power）模式。

<a id="define-members-5"></a>

### 低通滤波器分频选项（Low-pass Filter Divider Options）

设备树属性（Devicetree Property）`accel-lp-filter` 的取值。

<a id="r_ga4981c36e44bf1aa45bf05ab9b356117e"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_2 0
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_2](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga4981c36e44bf1aa45bf05ab9b356117e)。

输出数据速率（ODR）除以 2。

<a id="r_gab17d663d64d484ce04ac5c934e6d269a"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_10 1
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_10](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab17d663d64d484ce04ac5c934e6d269a)。

输出数据速率（ODR）除以 10。

<a id="r_gab57ddcf22ff9ae72a92b245c0fecc025"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_20 2
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_20](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab57ddcf22ff9ae72a92b245c0fecc025)。

输出数据速率（ODR）除以 20。

<a id="r_gaecd1f9c4b8e9ef0f98169f275b8ee98c"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_45 3
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_45](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaecd1f9c4b8e9ef0f98169f275b8ee98c)。

输出数据速率（ODR）除以 45。

<a id="r_ga8cffd21429574fa53f5817affb3620a6"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_100 4
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_100](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga8cffd21429574fa53f5817affb3620a6)。

输出数据速率（ODR）除以 100。

<a id="r_gaa200437c6db2aba3f4385bca36d2107c"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_200 5
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_200](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaa200437c6db2aba3f4385bca36d2107c)。

输出数据速率（ODR）除以 200。

<a id="r_ga33f69cb9156a657b46a88d5b34dfbd52"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_400 6
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_400](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga33f69cb9156a657b46a88d5b34dfbd52)。

输出数据速率（ODR）除以 400。

<a id="r_ga6799d36f05d459ebdb2fc51fa368bdb2"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_800 7
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_800](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga6799d36f05d459ebdb2fc51fa368bdb2)。

输出数据速率（ODR）除以 800。

<a id="define-members-6"></a>

### 敲击检测模式（Tap Detection Mode）

设备树属性（Devicetree Property）`tap-mode` 的取值。

<a id="r_gade7b8d0e5cf3f46ccee6133919af35df"></a>

```c
#define LSM6DSO_DT_SINGLE_TAP 0
```

相关声明：[LSM6DSO_DT_SINGLE_TAP](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gade7b8d0e5cf3f46ccee6133919af35df)。

仅单击（Single-tap Only）。

<a id="r_ga7ad4099bd82ffa09ce63eeaa79490941"></a>

```c
#define LSM6DSO_DT_SINGLE_DOUBLE_TAP 1
```

相关声明：[LSM6DSO_DT_SINGLE_DOUBLE_TAP](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga7ad4099bd82ffa09ce63eeaa79490941)。

单击与双击（Single and Double Tap）。


## 8.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P460_lsm6dso.h_源码浏览.md)
- [LSM6DSO_DT_XL_HP_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaa62e5d2a5529d005f4d622ecdf97f8f0)
- [LSM6DSO_DT_XL_LP_NORMAL_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga031783c6119db7de6138f368c65c0e49)
- [LSM6DSO_DT_XL_ULP_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gae1fc1b3317d8dac484cc8f094ff453c6)
- [LSM6DSO_DT_GY_HP_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gac6810407924f44016f0f27c44aca22de)
- [LSM6DSO_DT_GY_NORMAL_MODE](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaae6bf6b52db6321cba323a06af6afe4c)
- [LSM6DSO_DT_FS_2G](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga4b6fd691c9843fdce021c027a6c1d38f)
- [LSM6DSO_DT_FS_16G](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaab163b8d605a6433aff9af2c4fb31764)
- [LSM6DSO_DT_FS_4G](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gac6b3e663efb2aa9340480a0a955b97d7)
- [LSM6DSO_DT_FS_8G](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gad2f86d00fa1665c011296fa27b4a235c)
- [LSM6DSO_DT_FS_250DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga3754f6339351a7d1be2b98fab8b88102)
- [LSM6DSO_DT_FS_125DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gae427e045d161c9f90eff4c6e5dee4efe)
- [LSM6DSO_DT_FS_500DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga0edc66177f1cb810257fe8e3460586a4)
- [LSM6DSO_DT_FS_1000DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga862e3383ea2a6db7fea154fe7b5e5f58)
- [LSM6DSO_DT_FS_2000DPS](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga5f007e2d998b5eda7c5fd08145665e4e)
- [LSM6DSO_DT_ODR_OFF](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga8969b4f07c618f652bf4b15de9d0b5f7)
- [LSM6DSO_DT_ODR_12Hz5](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga9f0952fa1854848632b30b59e8145f08)
- [LSM6DSO_DT_ODR_26H](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab8cc4ee8854e45071720c6e97cb9a133)
- [LSM6DSO_DT_ODR_52Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab172e908c0810d7a57cad2ccd70626b1)
- [LSM6DSO_DT_ODR_104Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga59b98b9f338fd9cf2d568b14ac5a5410)
- [LSM6DSO_DT_ODR_208Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaf57d5e0ecb4fba8230d4a69390a4857c)
- [LSM6DSO_DT_ODR_417Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaeb374d527698dc50af30a2469957da6f)
- [LSM6DSO_DT_ODR_833Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga2cb2a2d726eee22c6e5457700a966c9a)
- [LSM6DSO_DT_ODR_1667Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga41f7e1ee6c74cd37b707382ccda3474b)
- [LSM6DSO_DT_ODR_3333Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab66ab364d747f4b95f68c596effeb143)
- [LSM6DSO_DT_ODR_6667Hz](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga73b782f5504622e185d60d635397620a)
- [LSM6DSO_DT_ODR_1Hz6](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga14963a4bd7e78ba44eb33da3eaa950af)
- [LSM6DSO_DT_LP_ODR_DIV_2](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga4981c36e44bf1aa45bf05ab9b356117e)
- [LSM6DSO_DT_LP_ODR_DIV_10](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab17d663d64d484ce04ac5c934e6d269a)
- [LSM6DSO_DT_LP_ODR_DIV_20](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gab57ddcf22ff9ae72a92b245c0fecc025)
- [LSM6DSO_DT_LP_ODR_DIV_45](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaecd1f9c4b8e9ef0f98169f275b8ee98c)
- [LSM6DSO_DT_LP_ODR_DIV_100](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga8cffd21429574fa53f5817affb3620a6)
- [LSM6DSO_DT_LP_ODR_DIV_200](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gaa200437c6db2aba3f4385bca36d2107c)
- [LSM6DSO_DT_LP_ODR_DIV_400](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga33f69cb9156a657b46a88d5b34dfbd52)
- [LSM6DSO_DT_LP_ODR_DIV_800](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga6799d36f05d459ebdb2fc51fa368bdb2)
- [LSM6DSO_DT_SINGLE_TAP](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#gade7b8d0e5cf3f46ccee6133919af35df)
- [LSM6DSO_DT_SINGLE_DOUBLE_TAP](../api_input_runtime_topic_reference/P011_LSM6DSO API主题.md#ga7ad4099bd82ffa09ce63eeaa79490941)

<a id="header-details"></a>

---

[上一章](P007_zephyr__drivers__interrupt_controller__intc_wkpu_nxp_s32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__gpio__stmod-plus-connector.h_文件参考.md)
