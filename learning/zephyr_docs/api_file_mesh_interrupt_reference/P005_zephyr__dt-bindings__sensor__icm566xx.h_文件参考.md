---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-5
title: zephyr__dt-bindings__sensor__icm566xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2icm566xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_sensor\_\_icm566xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2icm566xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the TDK InvenSense ICM566xx IMU的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the TDK InvenSense ICM566xx IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计电源模式（Accelerometer Power Modes）

设备树属性（Devicetree Property）`accel-pwr-mode` 的取值。

<a id="r_gaf5d0235fd419733537fa4cd32821668a"></a>

```c
#define ICM566XX_DT_ACCEL_OFF 0
```

相关声明：[ICM566XX_DT_ACCEL_OFF](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaf5d0235fd419733537fa4cd32821668a)。

已断电（Powered Down）。

<a id="r_ga50279b4a7eeaec5d322943b50f53e878"></a>

```c
#define ICM566XX_DT_ACCEL_LP 2
```

相关声明：[ICM566XX_DT_ACCEL_LP](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga50279b4a7eeaec5d322943b50f53e878)。

低功耗模式（Low-power Mode）。

<a id="r_gad40b63ce1173c77ffc35727509efc392"></a>

```c
#define ICM566XX_DT_ACCEL_LN 3
```

相关声明：[ICM566XX_DT_ACCEL_LN](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad40b63ce1173c77ffc35727509efc392)。

低噪声模式（Low-noise Mode）。

<a id="define-members-1"></a>

### 陀螺仪电源模式（Gyroscope Power Modes）

设备树属性（Devicetree Property）`gyro-pwr-mode` 的取值。

<a id="r_gaf354f134ca8bf7334b5d684af51100b6"></a>

```c
#define ICM566XX_DT_GYRO_OFF 0
```

相关声明：[ICM566XX_DT_GYRO_OFF](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaf354f134ca8bf7334b5d684af51100b6)。

已断电（Powered Down）。

<a id="r_ga10f0cdd8f05e3ccd85871b312e870802"></a>

```c
#define ICM566XX_DT_GYRO_STANDBY 1
```

相关声明：[ICM566XX_DT_GYRO_STANDBY](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga10f0cdd8f05e3ccd85871b312e870802)。

待机（Standby）。

<a id="r_gad4496a59e2a10ad508501d4636a47b19"></a>

```c
#define ICM566XX_DT_GYRO_LP 2
```

相关声明：[ICM566XX_DT_GYRO_LP](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad4496a59e2a10ad508501d4636a47b19)。

低功耗模式（Low-power Mode）。

<a id="r_gabab45d06bfe9e25ac299c3216f75af0f"></a>

```c
#define ICM566XX_DT_GYRO_LN 3
```

相关声明：[ICM566XX_DT_GYRO_LN](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gabab45d06bfe9e25ac299c3216f75af0f)。

低噪声模式（Low-noise Mode）。

<a id="define-members-2"></a>

### 加速度计量程选项（Accelerometer Scale Options）

设备树属性（Devicetree Property）`accel-fs` 的取值。

<a id="r_ga437a0d53e9b7152a22b6b6b279223479"></a>

```c
#define ICM566XX_DT_ACCEL_FS_32 0
```

相关声明：[ICM566XX_DT_ACCEL_FS_32](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga437a0d53e9b7152a22b6b6b279223479)。

满量程（Full Scale）：32g。

<a id="r_ga66550f154521e76da491004eb7979451"></a>

```c
#define ICM566XX_DT_ACCEL_FS_16 1
```

相关声明：[ICM566XX_DT_ACCEL_FS_16](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga66550f154521e76da491004eb7979451)。

满量程（Full Scale）：16g。

<a id="r_ga79be3f79bd227c62e0b8f3e13804378e"></a>

```c
#define ICM566XX_DT_ACCEL_FS_8 2
```

相关声明：[ICM566XX_DT_ACCEL_FS_8](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga79be3f79bd227c62e0b8f3e13804378e)。

满量程（Full Scale）：8g。

<a id="r_ga4beb14180e50869297f633b004f892a6"></a>

```c
#define ICM566XX_DT_ACCEL_FS_4 3
```

相关声明：[ICM566XX_DT_ACCEL_FS_4](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga4beb14180e50869297f633b004f892a6)。

满量程（Full Scale）：4g。

<a id="r_ga4f1f08648397f6fd058e586f9f1ea0c9"></a>

```c
#define ICM566XX_DT_ACCEL_FS_2 4
```

相关声明：[ICM566XX_DT_ACCEL_FS_2](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga4f1f08648397f6fd058e586f9f1ea0c9)。

满量程（Full Scale）：2g。

<a id="define-members-3"></a>

### 陀螺仪量程选项（Gyroscope Scale Options）

设备树属性（Devicetree Property）`gyro-fs` 的取值。

<a id="r_ga4d34d95ee2463dd847bc8fbb848c9f73"></a>

```c
#define ICM566XX_DT_GYRO_FS_4000 0
```

相关声明：[ICM566XX_DT_GYRO_FS_4000](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga4d34d95ee2463dd847bc8fbb848c9f73)。

满量程（Full Scale）：4000 dps（度／秒）。

<a id="r_ga29836f13c0174d77fdcb725949425e1a"></a>

```c
#define ICM566XX_DT_GYRO_FS_2000 1
```

相关声明：[ICM566XX_DT_GYRO_FS_2000](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga29836f13c0174d77fdcb725949425e1a)。

满量程（Full Scale）：2000 dps（度／秒）。

<a id="r_ga2b3614b2be6aa85c0566d85781043134"></a>

```c
#define ICM566XX_DT_GYRO_FS_1000 2
```

相关声明：[ICM566XX_DT_GYRO_FS_1000](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga2b3614b2be6aa85c0566d85781043134)。

满量程（Full Scale）：1000 dps（度／秒）。

<a id="r_ga275d6bdae7765c7d4ffc7b5f0af9a311"></a>

```c
#define ICM566XX_DT_GYRO_FS_500 3
```

相关声明：[ICM566XX_DT_GYRO_FS_500](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga275d6bdae7765c7d4ffc7b5f0af9a311)。

满量程（Full Scale）：500 dps（度／秒）。

<a id="r_ga74d6dca05eca7c92f2fed67e4262c3a9"></a>

```c
#define ICM566XX_DT_GYRO_FS_250 4
```

相关声明：[ICM566XX_DT_GYRO_FS_250](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga74d6dca05eca7c92f2fed67e4262c3a9)。

满量程（Full Scale）：250 dps（度／秒）。

<a id="r_gaeb125d4a19491276bc0a45e3622abe0d"></a>

```c
#define ICM566XX_DT_GYRO_FS_125 5
```

相关声明：[ICM566XX_DT_GYRO_FS_125](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaeb125d4a19491276bc0a45e3622abe0d)。

满量程（Full Scale）：125 dps（度／秒）。

<a id="r_gac15ced8fda07377fbc3b2ad9087831e9"></a>

```c
#define ICM566XX_DT_GYRO_FS_62_5 6
```

相关声明：[ICM566XX_DT_GYRO_FS_62_5](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gac15ced8fda07377fbc3b2ad9087831e9)。

满量程（Full Scale）：62.5 dps（度／秒）。

<a id="r_ga3660b0393736f7b448158307c71b6048"></a>

```c
#define ICM566XX_DT_GYRO_FS_31_25 7
```

相关声明：[ICM566XX_DT_GYRO_FS_31_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga3660b0393736f7b448158307c71b6048)。

满量程（Full Scale）：31.25 dps（度／秒）。

<a id="r_ga3764916c304e3783cd4e00e8123f33f8"></a>

```c
#define ICM566XX_DT_GYRO_FS_15_625 8
```

相关声明：[ICM566XX_DT_GYRO_FS_15_625](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga3764916c304e3783cd4e00e8123f33f8)。

满量程（Full Scale）：15.625 dps（度／秒）。

<a id="define-members-4"></a>

### 加速度计数据速率选项（Accelerometer Data Rate Options）

设备树（Devicetree）属性 `accel-odr` 的取值。

<a id="r_ga6b7b33acf93a7070231640473e0b276e"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_6400 3
```

相关声明：[ICM566XX_DT_ACCEL_ODR_6400](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga6b7b33acf93a7070231640473e0b276e)。

6400 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga7b998728b193fa5f49551c3690e493b5"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_3200 4
```

相关声明：[ICM566XX_DT_ACCEL_ODR_3200](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga7b998728b193fa5f49551c3690e493b5)。

3200 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga0908a03f35c371a087f6615f43b843c0"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_1600 5
```

相关声明：[ICM566XX_DT_ACCEL_ODR_1600](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga0908a03f35c371a087f6615f43b843c0)。

1600 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gadf0a170ebe013b3fc9d30458e33aadad"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_800 6
```

相关声明：[ICM566XX_DT_ACCEL_ODR_800](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gadf0a170ebe013b3fc9d30458e33aadad)。

800 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gac1f4fa91d6dfa74c0b3dca304e937292"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_400 7
```

相关声明：[ICM566XX_DT_ACCEL_ODR_400](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gac1f4fa91d6dfa74c0b3dca304e937292)。

400 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga92674f1d54dccf72657f71611062fbc9"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_200 8
```

相关声明：[ICM566XX_DT_ACCEL_ODR_200](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga92674f1d54dccf72657f71611062fbc9)。

200 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gace9ce1ce1dd05c226f79890e3c7d5ae4"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_100 9
```

相关声明：[ICM566XX_DT_ACCEL_ODR_100](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gace9ce1ce1dd05c226f79890e3c7d5ae4)。

100 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga9d749134dc24267fd52f76538c853807"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_50 10
```

相关声明：[ICM566XX_DT_ACCEL_ODR_50](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga9d749134dc24267fd52f76538c853807)。

50 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga05185f0a0f72368d4cc16dcfafce0c96"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_25 11
```

相关声明：[ICM566XX_DT_ACCEL_ODR_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga05185f0a0f72368d4cc16dcfafce0c96)。

25 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gae37790bc7673e43408ecfd6e82ffd7e7"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_12_5 12
```

相关声明：[ICM566XX_DT_ACCEL_ODR_12_5](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gae37790bc7673e43408ecfd6e82ffd7e7)。

12.5 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gac74bb0ad1420cce3e0a9fd248b2ac051"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_6_25 13
```

相关声明：[ICM566XX_DT_ACCEL_ODR_6_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gac74bb0ad1420cce3e0a9fd248b2ac051)。

6.25 Hz（仅适用于低功耗（LP）模式）。

<a id="r_gaf07a780bbdaf741cd5f8ab6a7524b077"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_3_125 14
```

相关声明：[ICM566XX_DT_ACCEL_ODR_3_125](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaf07a780bbdaf741cd5f8ab6a7524b077)。

3.125 Hz（仅适用于低功耗（LP）模式）。

<a id="r_gabe60143ab3faee9d82c5f0a7cb3fde1e"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_1_5625 15
```

相关声明：[ICM566XX_DT_ACCEL_ODR_1_5625](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gabe60143ab3faee9d82c5f0a7cb3fde1e)。

1.5625 Hz（仅适用于低功耗（LP）模式）。

<a id="define-members-5"></a>

### 陀螺仪数据速率选项（Gyroscope Data Rate Options）

设备树属性（Devicetree Property）`gyro-odr` 的取值。

<a id="r_gacce1ecb914ab26bfb124092cd03256e2"></a>

```c
#define ICM566XX_DT_GYRO_ODR_6400 3
```

相关声明：[ICM566XX_DT_GYRO_ODR_6400](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gacce1ecb914ab26bfb124092cd03256e2)。

6400 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga72b736f6702a0bf43c49554da2ec8a85"></a>

```c
#define ICM566XX_DT_GYRO_ODR_3200 4
```

相关声明：[ICM566XX_DT_GYRO_ODR_3200](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga72b736f6702a0bf43c49554da2ec8a85)。

3200 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gaa41a39d63f171f74915b7c9be0597f5b"></a>

```c
#define ICM566XX_DT_GYRO_ODR_1600 5
```

相关声明：[ICM566XX_DT_GYRO_ODR_1600](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaa41a39d63f171f74915b7c9be0597f5b)。

1600 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gad4ce89d9ef3865bdb4a911a7e3e50972"></a>

```c
#define ICM566XX_DT_GYRO_ODR_800 6
```

相关声明：[ICM566XX_DT_GYRO_ODR_800](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad4ce89d9ef3865bdb4a911a7e3e50972)。

800 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga6192cac91455a1fcf42e56264da8242e"></a>

```c
#define ICM566XX_DT_GYRO_ODR_400 7
```

相关声明：[ICM566XX_DT_GYRO_ODR_400](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga6192cac91455a1fcf42e56264da8242e)。

400 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga461e51c57b053ed4e20d410feea6f5dc"></a>

```c
#define ICM566XX_DT_GYRO_ODR_200 8
```

相关声明：[ICM566XX_DT_GYRO_ODR_200](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga461e51c57b053ed4e20d410feea6f5dc)。

200 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga3513a51121482d74a36c87d1c0b11bcd"></a>

```c
#define ICM566XX_DT_GYRO_ODR_100 9
```

相关声明：[ICM566XX_DT_GYRO_ODR_100](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga3513a51121482d74a36c87d1c0b11bcd)。

100 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gae5fd553b7a0cd0caf01115d81def276f"></a>

```c
#define ICM566XX_DT_GYRO_ODR_50 10
```

相关声明：[ICM566XX_DT_GYRO_ODR_50](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gae5fd553b7a0cd0caf01115d81def276f)。

50 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gad6183a26c7063792b2309e6afde0d7c4"></a>

```c
#define ICM566XX_DT_GYRO_ODR_25 11
```

相关声明：[ICM566XX_DT_GYRO_ODR_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad6183a26c7063792b2309e6afde0d7c4)。

25 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gaf6e7d62c7bf1d70e24456ac695c2dcb7"></a>

```c
#define ICM566XX_DT_GYRO_ODR_12_5 12
```

相关声明：[ICM566XX_DT_GYRO_ODR_12_5](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaf6e7d62c7bf1d70e24456ac695c2dcb7)。

12.5 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gae2b1c4a2443d401f19672ca6094a31ed"></a>

```c
#define ICM566XX_DT_GYRO_ODR_6_25 13
```

相关声明：[ICM566XX_DT_GYRO_ODR_6_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gae2b1c4a2443d401f19672ca6094a31ed)。

6.25 Hz（仅适用于低功耗（LP）模式）。

<a id="r_gae9dcf2919e8451ad9043fb459bddc4f8"></a>

```c
#define ICM566XX_DT_GYRO_ODR_3_125 14
```

相关声明：[ICM566XX_DT_GYRO_ODR_3_125](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gae9dcf2919e8451ad9043fb459bddc4f8)。

3.125 Hz（仅适用于低功耗（LP）模式）。

<a id="r_ga72e142db33cb62da147b4e1bb1c4ea92"></a>

```c
#define ICM566XX_DT_GYRO_ODR_1_5625 15
```

相关声明：[ICM566XX_DT_GYRO_ODR_1_5625](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga72e142db33cb62da147b4e1bb1c4ea92)。

1.5625 Hz（仅适用于低功耗（LP）模式）。

<a id="define-members-6"></a>

### 陀螺仪低通滤波选项（Gyroscope Low-pass Filtering Options）

设备树属性（Devicetree Property）`gyro-lpf-bw` 的取值。

<a id="r_ga8a60df60c5ca01421b98b2b22c97eec2"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_OFF 0
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_OFF](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga8a60df60c5ca01421b98b2b22c97eec2)。

禁用滤波器（Filter Disabled）。

<a id="r_ga8615f0ddec208b4f7dd3d7c470259015"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_4 1
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_4](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga8615f0ddec208b4f7dd3d7c470259015)。

输出数据速率（ODR）的 1/4。

<a id="r_ga3dedfa654c08300592eedbc9da5110d8"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_8 2
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_8](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga3dedfa654c08300592eedbc9da5110d8)。

输出数据速率（ODR）的 1/8。

<a id="r_ga79fba6d40c25ef0f009fdd8c97ca9eb1"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_16 3
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_16](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga79fba6d40c25ef0f009fdd8c97ca9eb1)。

输出数据速率（ODR）的 1/16。

<a id="r_gac0bc2e1428081e330a7e997335ceafa8"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_32 4
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_32](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gac0bc2e1428081e330a7e997335ceafa8)。

输出数据速率（ODR）的 1/32。

<a id="r_gad4605e71889f0c72f354bdf9cc5f83ae"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_64 5
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_64](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad4605e71889f0c72f354bdf9cc5f83ae)。

输出数据速率（ODR）的 1/64。

<a id="r_ga0b7cf8c4ef1c3f9f9e1605d32d7373bf"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_128 6
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_128](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga0b7cf8c4ef1c3f9f9e1605d32d7373bf)。

输出数据速率（ODR）的 1/128。

<a id="define-members-7"></a>

### 加速度计低通滤波选项（Accelerometer Low-pass Filtering Options）

设备树属性（Devicetree Property）`accel-lpf-bw` 的取值。

<a id="r_ga5d0e59c91ba3c2515058ba0c9d3071a4"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_OFF 0
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_OFF](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga5d0e59c91ba3c2515058ba0c9d3071a4)。

禁用滤波器（Filter Disabled）。

<a id="r_ga7c52f3003c6c5a12f98cb8232e295b9b"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_4 1
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_4](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga7c52f3003c6c5a12f98cb8232e295b9b)。

输出数据速率（ODR）的 1/4。

<a id="r_ga61268eed123637b32837b7f7d8d2a689"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_8 2
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_8](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga61268eed123637b32837b7f7d8d2a689)。

输出数据速率（ODR）的 1/8。

<a id="r_ga78ec7bd9579ebdb72c8ef41497790a51"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_16 3
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_16](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga78ec7bd9579ebdb72c8ef41497790a51)。

输出数据速率（ODR）的 1/16。

<a id="r_ga5b8be207fd78dc659c42bb33984ff416"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_32 4
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_32](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga5b8be207fd78dc659c42bb33984ff416)。

输出数据速率（ODR）的 1/32。

<a id="r_ga72b0d7e543db3e8dea630fdc811a7417"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_64 5
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_64](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga72b0d7e543db3e8dea630fdc811a7417)。

输出数据速率（ODR）的 1/64。

<a id="r_gacfb42d7af5e385f9d29d854132b74924"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_128 6
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_128](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gacfb42d7af5e385f9d29d854132b74924)。

输出数据速率（ODR）的 1/128。


## 5.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P204_icm566xx.h_源码浏览.md)
- [ICM566XX_DT_ACCEL_OFF](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaf5d0235fd419733537fa4cd32821668a)
- [ICM566XX_DT_ACCEL_LP](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga50279b4a7eeaec5d322943b50f53e878)
- [ICM566XX_DT_ACCEL_LN](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad40b63ce1173c77ffc35727509efc392)
- [ICM566XX_DT_GYRO_OFF](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaf354f134ca8bf7334b5d684af51100b6)
- [ICM566XX_DT_GYRO_STANDBY](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga10f0cdd8f05e3ccd85871b312e870802)
- [ICM566XX_DT_GYRO_LP](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad4496a59e2a10ad508501d4636a47b19)
- [ICM566XX_DT_GYRO_LN](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gabab45d06bfe9e25ac299c3216f75af0f)
- [ICM566XX_DT_ACCEL_FS_32](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga437a0d53e9b7152a22b6b6b279223479)
- [ICM566XX_DT_ACCEL_FS_16](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga66550f154521e76da491004eb7979451)
- [ICM566XX_DT_ACCEL_FS_8](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga79be3f79bd227c62e0b8f3e13804378e)
- [ICM566XX_DT_ACCEL_FS_4](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga4beb14180e50869297f633b004f892a6)
- [ICM566XX_DT_ACCEL_FS_2](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga4f1f08648397f6fd058e586f9f1ea0c9)
- [ICM566XX_DT_GYRO_FS_4000](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga4d34d95ee2463dd847bc8fbb848c9f73)
- [ICM566XX_DT_GYRO_FS_2000](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga29836f13c0174d77fdcb725949425e1a)
- [ICM566XX_DT_GYRO_FS_1000](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga2b3614b2be6aa85c0566d85781043134)
- [ICM566XX_DT_GYRO_FS_500](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga275d6bdae7765c7d4ffc7b5f0af9a311)
- [ICM566XX_DT_GYRO_FS_250](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga74d6dca05eca7c92f2fed67e4262c3a9)
- [ICM566XX_DT_GYRO_FS_125](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaeb125d4a19491276bc0a45e3622abe0d)
- [ICM566XX_DT_GYRO_FS_62_5](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gac15ced8fda07377fbc3b2ad9087831e9)
- [ICM566XX_DT_GYRO_FS_31_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga3660b0393736f7b448158307c71b6048)
- [ICM566XX_DT_GYRO_FS_15_625](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga3764916c304e3783cd4e00e8123f33f8)
- [ICM566XX_DT_ACCEL_ODR_6400](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga6b7b33acf93a7070231640473e0b276e)
- [ICM566XX_DT_ACCEL_ODR_3200](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga7b998728b193fa5f49551c3690e493b5)
- [ICM566XX_DT_ACCEL_ODR_1600](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga0908a03f35c371a087f6615f43b843c0)
- [ICM566XX_DT_ACCEL_ODR_800](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gadf0a170ebe013b3fc9d30458e33aadad)
- [ICM566XX_DT_ACCEL_ODR_400](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gac1f4fa91d6dfa74c0b3dca304e937292)
- [ICM566XX_DT_ACCEL_ODR_200](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga92674f1d54dccf72657f71611062fbc9)
- [ICM566XX_DT_ACCEL_ODR_100](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gace9ce1ce1dd05c226f79890e3c7d5ae4)
- [ICM566XX_DT_ACCEL_ODR_50](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga9d749134dc24267fd52f76538c853807)
- [ICM566XX_DT_ACCEL_ODR_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga05185f0a0f72368d4cc16dcfafce0c96)
- [ICM566XX_DT_ACCEL_ODR_12_5](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gae37790bc7673e43408ecfd6e82ffd7e7)
- [ICM566XX_DT_ACCEL_ODR_6_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gac74bb0ad1420cce3e0a9fd248b2ac051)
- [ICM566XX_DT_ACCEL_ODR_3_125](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaf07a780bbdaf741cd5f8ab6a7524b077)
- [ICM566XX_DT_ACCEL_ODR_1_5625](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gabe60143ab3faee9d82c5f0a7cb3fde1e)
- [ICM566XX_DT_GYRO_ODR_6400](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gacce1ecb914ab26bfb124092cd03256e2)
- [ICM566XX_DT_GYRO_ODR_3200](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga72b736f6702a0bf43c49554da2ec8a85)
- [ICM566XX_DT_GYRO_ODR_1600](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaa41a39d63f171f74915b7c9be0597f5b)
- [ICM566XX_DT_GYRO_ODR_800](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad4ce89d9ef3865bdb4a911a7e3e50972)
- [ICM566XX_DT_GYRO_ODR_400](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga6192cac91455a1fcf42e56264da8242e)
- [ICM566XX_DT_GYRO_ODR_200](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga461e51c57b053ed4e20d410feea6f5dc)
- [ICM566XX_DT_GYRO_ODR_100](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga3513a51121482d74a36c87d1c0b11bcd)
- [ICM566XX_DT_GYRO_ODR_50](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gae5fd553b7a0cd0caf01115d81def276f)
- [ICM566XX_DT_GYRO_ODR_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad6183a26c7063792b2309e6afde0d7c4)
- [ICM566XX_DT_GYRO_ODR_12_5](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gaf6e7d62c7bf1d70e24456ac695c2dcb7)
- [ICM566XX_DT_GYRO_ODR_6_25](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gae2b1c4a2443d401f19672ca6094a31ed)
- [ICM566XX_DT_GYRO_ODR_3_125](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gae9dcf2919e8451ad9043fb459bddc4f8)
- [ICM566XX_DT_GYRO_ODR_1_5625](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga72e142db33cb62da147b4e1bb1c4ea92)
- [ICM566XX_DT_GYRO_LPF_BW_OFF](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga8a60df60c5ca01421b98b2b22c97eec2)
- [ICM566XX_DT_GYRO_LPF_BW_1_4](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga8615f0ddec208b4f7dd3d7c470259015)
- [ICM566XX_DT_GYRO_LPF_BW_1_8](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga3dedfa654c08300592eedbc9da5110d8)
- [ICM566XX_DT_GYRO_LPF_BW_1_16](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga79fba6d40c25ef0f009fdd8c97ca9eb1)
- [ICM566XX_DT_GYRO_LPF_BW_1_32](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gac0bc2e1428081e330a7e997335ceafa8)
- [ICM566XX_DT_GYRO_LPF_BW_1_64](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gad4605e71889f0c72f354bdf9cc5f83ae)
- [ICM566XX_DT_GYRO_LPF_BW_1_128](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga0b7cf8c4ef1c3f9f9e1605d32d7373bf)
- [ICM566XX_DT_ACCEL_LPF_BW_OFF](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga5d0e59c91ba3c2515058ba0c9d3071a4)
- [ICM566XX_DT_ACCEL_LPF_BW_1_4](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga7c52f3003c6c5a12f98cb8232e295b9b)
- [ICM566XX_DT_ACCEL_LPF_BW_1_8](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga61268eed123637b32837b7f7d8d2a689)
- [ICM566XX_DT_ACCEL_LPF_BW_1_16](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga78ec7bd9579ebdb72c8ef41497790a51)
- [ICM566XX_DT_ACCEL_LPF_BW_1_32](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga5b8be207fd78dc659c42bb33984ff416)
- [ICM566XX_DT_ACCEL_LPF_BW_1_64](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#ga72b0d7e543db3e8dea630fdc811a7417)
- [ICM566XX_DT_ACCEL_LPF_BW_1_128](../api_bridge_paging_topic_reference/P004_ICM566xx API主题.md#gacfb42d7af5e385f9d29d854132b74924)

<a id="header-details"></a>

---

[上一章](P004_zephyr__drivers__sensor__mcp9600.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__i3c__error_types.h_文件参考.md)
