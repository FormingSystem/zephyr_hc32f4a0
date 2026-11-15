---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-2
title: zephyr__dt-bindings__sensor__lsm6dsvxxx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lsm6dsvxxx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_sensor\_\_lsm6dsvxxx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lsm6dsvxxx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ST LSM6DSVxxx六轴惯性测量单元（6-Axis IMUs）共享的设备树绑定常量。

查看此文件的源码。

<a id="details"></a>

ST LSM6DSVxxx六轴惯性测量单元（6-Axis IMUs）共享的设备树绑定常量。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计和陀螺仪数据速率（Accelerometer and gyroscope data rates）

设备树（Devicetree）属性 `accel-odr` 和 `gyro-odr` 的取值。

HA01 和 HA02 分别选择第一组和第二组高精度输出数据率（High-accuracy ODR）设置。

<a id="r_gaa2f3a91a76a073c7ab7ed54766191bfc"></a>

```c
#define LSM6DSVXXX_DT_ODR_OFF 0x0
```

相关声明：[LSM6DSVXXX_DT_ODR_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa2f3a91a76a073c7ab7ed54766191bfc)。

已断电（Powered Down）。

<a id="r_ga3be748256792c3a92a53860ba35ec37e"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_1Hz875 0x1
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_1Hz875](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga3be748256792c3a92a53860ba35ec37e)。

1.875 Hz

<a id="r_gabc401ff628f557d26e4b563c59a5a1fd"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_7Hz5 0x2
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_7Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gabc401ff628f557d26e4b563c59a5a1fd)。

7.5 Hz

<a id="r_ga3f4f72d9ba0886cabd2b8c2b722fb4a4"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_15Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga3f4f72d9ba0886cabd2b8c2b722fb4a4)。

15 Hz

<a id="r_ga11812be3986cb32212fed1cbe633bb02"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_30Hz 0x4
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_30Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga11812be3986cb32212fed1cbe633bb02)。

30 Hz

<a id="r_ga9844e2a752e351ad60b9ba33fe115a5d"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_60Hz 0x5
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga9844e2a752e351ad60b9ba33fe115a5d)。

60 Hz

<a id="r_gadd4d620ed3e4bf2d1634038fa562d125"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_120Hz 0x6
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_120Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gadd4d620ed3e4bf2d1634038fa562d125)。

120 Hz

<a id="r_ga89e9deb98803378fe536f8be047ba163"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_240Hz 0x7
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_240Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga89e9deb98803378fe536f8be047ba163)。

240 Hz

<a id="r_gabaa02a50ecf88a84ba1936e05b9cda64"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_480Hz 0x8
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_480Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gabaa02a50ecf88a84ba1936e05b9cda64)。

480 Hz（赫兹）。

<a id="r_ga1b6fdb03a0aa1afb1b1dd4b9b17480f8"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_960Hz 0x9
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_960Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga1b6fdb03a0aa1afb1b1dd4b9b17480f8)。

960 Hz（赫兹）。

<a id="r_ga6fb1ef88249f73a0f77d41f80cae9b92"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_1920Hz 0xA
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_1920Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga6fb1ef88249f73a0f77d41f80cae9b92)。

1920 Hz（赫兹）。

<a id="r_ga755a4e96058319aff0cc1dfc9d83b543"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_3840Hz 0xB
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_3840Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga755a4e96058319aff0cc1dfc9d83b543)。

3840 Hz（赫兹）。

<a id="r_ga47178c61455a339ac1f488cfeca5df36"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_7680Hz 0xC
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_7680Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga47178c61455a339ac1f488cfeca5df36)。

7680 Hz（赫兹）。

<a id="r_gac2e60f249f1ef4a78959e65580f74452"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625 0x13
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gac2e60f249f1ef4a78959e65580f74452)。

高精度 1（High-accuracy 1），15.625 Hz。

<a id="r_gafaf3d1f73b95285b7e0eb9daa26b71ce"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25 0x14
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gafaf3d1f73b95285b7e0eb9daa26b71ce)。

高精度 1（High-accuracy 1），31.25 Hz。

<a id="r_gaf90fd3e38738689eefacff410e1806fc"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5 0x15
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaf90fd3e38738689eefacff410e1806fc)。

高精度 1（High-accuracy 1），62.5 Hz。

<a id="r_gacf3aa8af4d68646513cdcdd924567e9c"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_125Hz 0x16
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_125Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gacf3aa8af4d68646513cdcdd924567e9c)。

高精度 1（High-accuracy 1），125 Hz。

<a id="r_ga2022940241f4c0fdf19fb98c0e1cc1b1"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_250Hz 0x17
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_250Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2022940241f4c0fdf19fb98c0e1cc1b1)。

高精度 1（High-accuracy 1），250 Hz。

<a id="r_ga5723fb099f01688aeb21439419484ca8"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_500Hz 0x18
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_500Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5723fb099f01688aeb21439419484ca8)。

高精度 1（High-accuracy 1），500 Hz。

<a id="r_ga65d87ec8c3178d759633adf4e31decda"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz 0x19
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga65d87ec8c3178d759633adf4e31decda)。

高精度 1（High-accuracy 1），1000 Hz。

<a id="r_ga150d749dc27d494a17620b9a88fb91e9"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz 0x1A
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga150d749dc27d494a17620b9a88fb91e9)。

高精度 1（High-accuracy 1），2000 Hz。

<a id="r_ga175f2f879cf54c6d056c14b4e8ac6492"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz 0x1B
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga175f2f879cf54c6d056c14b4e8ac6492)。

高精度 1（High-accuracy 1），4000 Hz。

<a id="r_gaa4a3e31a309fe54777323a71231f61e2"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz 0x1C
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa4a3e31a309fe54777323a71231f61e2)。

高精度 1（High-accuracy 1），8000 Hz。

<a id="r_gab1553739349be4c090b648a8f6ce7b21"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5 0x23
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab1553739349be4c090b648a8f6ce7b21)。

高精度 2（High-accuracy 2），12.5 Hz。

<a id="r_gafdc624740a59409cc921a6883237d4bf"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_25Hz 0x24
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_25Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gafdc624740a59409cc921a6883237d4bf)。

高精度 2（High-accuracy 2），25 Hz。

<a id="r_gad630053a419a49eb0aaa0068b552cf2c"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_50Hz 0x25
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_50Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gad630053a419a49eb0aaa0068b552cf2c)。

高精度 2（High-accuracy 2），50 Hz。

<a id="r_gab8c0b7c9847d33260ed82a569f09ee7d"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_100Hz 0x26
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_100Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab8c0b7c9847d33260ed82a569f09ee7d)。

高精度 2（High-accuracy 2），100 Hz。

<a id="r_ga10f700875a21fa4a163446acb97035d5"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_200Hz 0x27
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_200Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga10f700875a21fa4a163446acb97035d5)。

高精度 2（High-accuracy 2），200 Hz。

<a id="r_ga96e0ab14e77c9b39757ceecdd6184388"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_400Hz 0x28
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_400Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga96e0ab14e77c9b39757ceecdd6184388)。

高精度 2（High-accuracy 2），400 Hz。

<a id="r_ga95521c6f18519bead2be0d35ec3cf127"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_800Hz 0x29
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_800Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga95521c6f18519bead2be0d35ec3cf127)。

高精度 2（High-accuracy 2），800 Hz。

<a id="r_gaa7df01142e7bf1227e1bd833f4b21fd8"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz 0x2A
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa7df01142e7bf1227e1bd833f4b21fd8)。

高精度 2（High-accuracy 2），1600 Hz。

<a id="r_ga8e18d124dd79ed9b654dd0b6b4f602b4"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz 0x2B
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga8e18d124dd79ed9b654dd0b6b4f602b4)。

高精度 2（High-accuracy 2），3200 Hz。

<a id="r_gae9c7edb6bf740c8b6e630e8bed92ce78"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz 0x2C
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae9c7edb6bf740c8b6e630e8bed92ce78)。

高精度 2（High-accuracy 2），6400 Hz。

<a id="define-members-1"></a>

### 加速度计 FIFO 批量采集速率（Accelerometer FIFO batching rates）

设备树 accel-fifo-batch-rate 属性（Property）的值。

<a id="r_ga2d5a1021d7aae23240f7d2b9daba868d"></a>

```c
#define LSM6DSVXXX_DT_XL_NOT_BATCHED 0x0
```

相关声明：[LSM6DSVXXX_DT_XL_NOT_BATCHED](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2d5a1021d7aae23240f7d2b9daba868d)。

不批量入队（Not Batched）。

<a id="r_gafda071feff90a5a8870e4f4e4922fc56"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_1Hz875 0x1
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_1Hz875](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gafda071feff90a5a8870e4f4e4922fc56)。

1.875 Hz

<a id="r_ga5d43c2750c55ece3dded6a61f5c3d78b"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_7Hz5 0x2
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_7Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5d43c2750c55ece3dded6a61f5c3d78b)。

7.5 Hz

<a id="r_ga60c9cd315c0df0df8675ea9075ff5f60"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_15Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga60c9cd315c0df0df8675ea9075ff5f60)。

15 Hz

<a id="r_gaab1720de9852174953ab3db6b61ed9f7"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_30Hz 0x4
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_30Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaab1720de9852174953ab3db6b61ed9f7)。

30 Hz

<a id="r_ga8425ee828bab319ccd97a35591a86802"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_60Hz 0x5
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga8425ee828bab319ccd97a35591a86802)。

60 Hz

<a id="r_gac7c6daed24a500629ab3c4455363cf12"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_120Hz 0x6
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_120Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gac7c6daed24a500629ab3c4455363cf12)。

120 Hz

<a id="r_gab1eab92c52d5e83aa8f1bb8fc586e5a0"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_240Hz 0x7
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_240Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab1eab92c52d5e83aa8f1bb8fc586e5a0)。

240 Hz

<a id="r_gae6f80d519366c78ee9b25c368def7fe2"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_480Hz 0x8
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_480Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae6f80d519366c78ee9b25c368def7fe2)。

480 Hz（赫兹）。

<a id="r_gaea7a895fd766ffdddefff82b9dc9b2f8"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_960Hz 0x9
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_960Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaea7a895fd766ffdddefff82b9dc9b2f8)。

960 Hz（赫兹）。

<a id="r_ga73d83e5c025af1a3ba7c11b8c98594a0"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_1920Hz 0xa
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_1920Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga73d83e5c025af1a3ba7c11b8c98594a0)。

1920 Hz（赫兹）。

<a id="r_gabe653b1f4634c8db6dd0abb98eeaf993"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_3840Hz 0xb
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_3840Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gabe653b1f4634c8db6dd0abb98eeaf993)。

3840 Hz（赫兹）。

<a id="r_ga2c57246c8035e01914d63bf497241bd5"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_7680Hz 0xc
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_7680Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2c57246c8035e01914d63bf497241bd5)。

7680 Hz（赫兹）。

<a id="define-members-2"></a>

### 陀螺仪 FIFO 批量采集速率（Gyroscope FIFO batching rates）

设备树属性（Devicetree Property）`gyro-fifo-batch-rate` 的取值。

<a id="r_ga21074319549fe782f14885b8cf4e598e"></a>

```c
#define LSM6DSVXXX_DT_GY_NOT_BATCHED 0x0
```

相关声明：[LSM6DSVXXX_DT_GY_NOT_BATCHED](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga21074319549fe782f14885b8cf4e598e)。

不批量入队（Not Batched）。

<a id="r_ga6701e54d1bdc9cc38b78869d422b4a24"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_1Hz875 0x1
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_1Hz875](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga6701e54d1bdc9cc38b78869d422b4a24)。

1.875 Hz

<a id="r_ga1d71dcadbdb735c1ed67d33f64dcc377"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_7Hz5 0x2
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_7Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga1d71dcadbdb735c1ed67d33f64dcc377)。

7.5 Hz

<a id="r_ga74cf3363ef11b6f309d187e15511da0f"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_15Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga74cf3363ef11b6f309d187e15511da0f)。

15 Hz

<a id="r_ga1f90e6eb1041d2adaa5b3904bc7c3ec5"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_30Hz 0x4
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_30Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga1f90e6eb1041d2adaa5b3904bc7c3ec5)。

30 Hz

<a id="r_ga04b59445efcaba20b9de75f118621036"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_60Hz 0x5
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga04b59445efcaba20b9de75f118621036)。

60 Hz

<a id="r_gad54fb498d1ac9a79e933fef1b3135b44"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_120Hz 0x6
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_120Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gad54fb498d1ac9a79e933fef1b3135b44)。

120 Hz

<a id="r_ga379a95a050085645c6b667be959917f1"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_240Hz 0x7
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_240Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga379a95a050085645c6b667be959917f1)。

240 Hz

<a id="r_gab8e2d1c1e5fbbc94c5205bd36a18c698"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_480Hz 0x8
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_480Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab8e2d1c1e5fbbc94c5205bd36a18c698)。

480 Hz（赫兹）。

<a id="r_gae827fd454d5fd6621dcaded3cde58dce"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_960Hz 0x9
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_960Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae827fd454d5fd6621dcaded3cde58dce)。

960 Hz（赫兹）。

<a id="r_ga0d9391fcf25e211e74b96b0567690e8c"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_1920Hz 0xa
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_1920Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0d9391fcf25e211e74b96b0567690e8c)。

1920 Hz（赫兹）。

<a id="r_gaa618e22a3ee6a5cd08512d75a2f8ba23"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_3840Hz 0xb
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_3840Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa618e22a3ee6a5cd08512d75a2f8ba23)。

3840 Hz（赫兹）。

<a id="r_ga1433bcac6731056771402543cb52b05d"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_7680Hz 0xc
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_7680Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga1433bcac6731056771402543cb52b05d)。

7680 Hz（赫兹）。

<a id="define-members-3"></a>

### 温度 FIFO 批量采集速率（Temperature FIFO batching rates）

设备树 temp-fifo-batch-rate 属性（Property）的值。

<a id="r_ga5b0ec9d5af96cba4f214f9cc18725d4a"></a>

```c
#define LSM6DSVXXX_DT_TEMP_NOT_BATCHED 0x0
```

相关声明：[LSM6DSVXXX_DT_TEMP_NOT_BATCHED](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5b0ec9d5af96cba4f214f9cc18725d4a)。

不批量入队（Not Batched）。

<a id="r_gaa4f00b050752fcd61a8b374ffc3e53e2"></a>

```c
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_1Hz875 0x1
```

相关声明：[LSM6DSVXXX_DT_TEMP_BATCHED_AT_1Hz875](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa4f00b050752fcd61a8b374ffc3e53e2)。

1.875 Hz

<a id="r_ga959ed5facb6f55bb105766fed641fb3b"></a>

```c
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_15Hz 0x2
```

相关声明：[LSM6DSVXXX_DT_TEMP_BATCHED_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga959ed5facb6f55bb105766fed641fb3b)。

15 Hz

<a id="r_ga5fd9d7951f7e13eae7240dceba715a0d"></a>

```c
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_60Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_TEMP_BATCHED_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5fd9d7951f7e13eae7240dceba715a0d)。

60 Hz

<a id="define-members-4"></a>

### 低功耗传感器融合数据速率（Sensor-fusion low-power data rates）

设备树属性（Devicetree Property）`sflp-odr` 的取值。

<a id="r_gadfe3e073293cc1f28dd35fdcbcb64504"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_15Hz 0x0
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gadfe3e073293cc1f28dd35fdcbcb64504)。

15 Hz

<a id="r_ga0728a6554ed8585a5eaf705ad0ab8b84"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_30Hz 0x1
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_30Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0728a6554ed8585a5eaf705ad0ab8b84)。

30 Hz

<a id="r_ga293ecc01f316565790cf1de00511f7e5"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_60Hz 0x2
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga293ecc01f316565790cf1de00511f7e5)。

60 Hz

<a id="r_ga5bd64654e4cba2e05d4c686a6008673b"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_120Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_120Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5bd64654e4cba2e05d4c686a6008673b)。

120 Hz

<a id="r_ga001956d8e537d42ec356240be93caff5"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_240Hz 0x4
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_240Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga001956d8e537d42ec356240be93caff5)。

240 Hz

<a id="r_ga2a25517fc9b890b150e5ca8d1b88990c"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_480Hz 0x5
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_480Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2a25517fc9b890b150e5ca8d1b88990c)。

480 Hz（赫兹）。

<a id="define-members-5"></a>

### 低功耗传感器融合 FIFO 输出（Sensor-fusion low-power FIFO outputs）

设备树属性（Devicetree Property）`sflp-fifo-enable` 的取值。

<a id="r_gae2e528f1f3eb49e1f3098c624b76441a"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_OFF 0x0
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae2e528f1f3eb49e1f3098c624b76441a)。

无 SFLP 输出（No SFLP Output）。

<a id="r_gaeff5ded37cf0bdbdb1dcaac49a19fd75"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION 0x1
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaeff5ded37cf0bdbdb1dcaac49a19fd75)。

游戏旋转向量（Game-rotation Vector）。

<a id="r_ga57ad9deaa73162e5350e171c79cd87ec"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY 0x2
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga57ad9deaa73162e5350e171c79cd87ec)。

重力向量（Gravity Vector）。

<a id="r_ga37dcd41d788f62ca71fb4edc392e8c70"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY 0x3
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga37dcd41d788f62ca71fb4edc392e8c70)。

旋转与重力（Rotation and Gravity）。

<a id="r_ga767e76d5e63f6c23c078b574e48cb445"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GBIAS 0x4
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GBIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga767e76d5e63f6c23c078b574e48cb445)。

陀螺仪偏置（Gyroscope Bias）。

<a id="r_ga5a2e8191ce4daf332c818629b071bb91"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GBIAS 0x5
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GBIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5a2e8191ce4daf332c818629b071bb91)。

旋转与陀螺仪偏置（Rotation and Gyro Bias）。

<a id="r_ga0f26c813d590aac8d94522144ea6b9a1"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY_GBIAS 0x6
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY_GBIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0f26c813d590aac8d94522144ea6b9a1)。

重力与陀螺仪偏置（Gravity and Gyro Bias）。

<a id="r_ga4e6154f4150417d3240bdb88caf578ff"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY_GBIAS 0x7
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY_GBIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga4e6154f4150417d3240bdb88caf578ff)。

旋转、重力与偏置（Rotation, Gravity, Bias）。

<a id="define-members-6"></a>

### FIFO 记录标签（FIFO Record Tags）

FIFO 数据流中报告的记录标签值（Record Tag Values）。

<a id="r_ga471b55f70fc3375571160acb78ad2617"></a>

```c
#define LSM6DSVXXX_FIFO_EMPTY 0x0
```

相关声明：[LSM6DSVXXX_FIFO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga471b55f70fc3375571160acb78ad2617)。

先进先出缓冲区（FIFO）为空。

<a id="r_ga7cca9213d67413e009dbb2fa74bf7bb3"></a>

```c
#define LSM6DSVXXX_GY_NC_TAG 0x1
```

相关声明：[LSM6DSVXXX_GY_NC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga7cca9213d67413e009dbb2fa74bf7bb3)。

陀螺仪（Gyroscope），不压缩。

<a id="r_ga320efe292f3c5121031d0d8f5436a5e7"></a>

```c
#define LSM6DSVXXX_XL_NC_TAG 0x2
```

相关声明：[LSM6DSVXXX_XL_NC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga320efe292f3c5121031d0d8f5436a5e7)。

加速度计（Accelerometer），不压缩。

<a id="r_ga49900f3a225fad10e3eff3c251de3ef9"></a>

```c
#define LSM6DSVXXX_TEMPERATURE_TAG 0x3
```

相关声明：[LSM6DSVXXX_TEMPERATURE_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga49900f3a225fad10e3eff3c251de3ef9)。

温度（Temperature）。

<a id="r_gae8e6953df547162248da27a53a6d8ddf"></a>

```c
#define LSM6DSVXXX_TIMESTAMP_TAG 0x4
```

相关声明：[LSM6DSVXXX_TIMESTAMP_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae8e6953df547162248da27a53a6d8ddf)。

时间戳（Timestamp）。

<a id="r_gac63cd2760ac68a57ab916e6a7ab41e01"></a>

```c
#define LSM6DSVXXX_CFG_CHANGE_TAG 0x5
```

相关声明：[LSM6DSVXXX_CFG_CHANGE_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gac63cd2760ac68a57ab916e6a7ab41e01)。

配置变化（Configuration Change）。

<a id="r_gabbd301aa0313208a3df654b587e41b09"></a>

```c
#define LSM6DSVXXX_XL_NC_T_2_TAG 0x6
```

相关声明：[LSM6DSVXXX_XL_NC_T_2_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gabbd301aa0313208a3df654b587e41b09)。

加速度计（Accelerometer），T-2 样本（Sample）。

<a id="r_gab375a7fe25056957f5dc100b24185d37"></a>

```c
#define LSM6DSVXXX_XL_NC_T_1_TAG 0x7
```

相关声明：[LSM6DSVXXX_XL_NC_T_1_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab375a7fe25056957f5dc100b24185d37)。

加速度计（Accelerometer），T-1 样本（Sample）。

<a id="r_gad74ab246e526843a3a9c0b51aff23bf3"></a>

```c
#define LSM6DSVXXX_XL_2XC_TAG 0x8
```

相关声明：[LSM6DSVXXX_XL_2XC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gad74ab246e526843a3a9c0b51aff23bf3)。

加速度计（Accelerometer），2 倍压缩（2x Compressed）。

<a id="r_gad17ba982da4ff778dd789adc597267d8"></a>

```c
#define LSM6DSVXXX_XL_3XC_TAG 0x9
```

相关声明：[LSM6DSVXXX_XL_3XC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gad17ba982da4ff778dd789adc597267d8)。

加速度计（Accelerometer），3 倍压缩（3x Compressed）。

<a id="r_ga2e3cdeecf56735b7261d1ff4220e7031"></a>

```c
#define LSM6DSVXXX_GY_NC_T_2_TAG 0xA
```

相关声明：[LSM6DSVXXX_GY_NC_T_2_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2e3cdeecf56735b7261d1ff4220e7031)。

陀螺仪（Gyroscope），T-2 样本（Sample）。

<a id="r_gaa17a548bc43898f64a7106fa9c6a7df5"></a>

```c
#define LSM6DSVXXX_GY_NC_T_1_TAG 0xB
```

相关声明：[LSM6DSVXXX_GY_NC_T_1_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa17a548bc43898f64a7106fa9c6a7df5)。

陀螺仪（Gyroscope），T-1 样本（Sample）。

<a id="r_gaca3fdec6fd30386a9c0393331da4c57f"></a>

```c
#define LSM6DSVXXX_GY_2XC_TAG 0xC
```

相关声明：[LSM6DSVXXX_GY_2XC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaca3fdec6fd30386a9c0393331da4c57f)。

陀螺仪（Gyroscope），2 倍压缩（2x Compressed）。

<a id="r_ga050b458172c45ae15319ae397a046c50"></a>

```c
#define LSM6DSVXXX_GY_3XC_TAG 0xD
```

相关声明：[LSM6DSVXXX_GY_3XC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga050b458172c45ae15319ae397a046c50)。

陀螺仪（Gyroscope），3 倍压缩（3x Compressed）。

<a id="r_ga087907d682457fe1b4fec7a19f781910"></a>

```c
#define LSM6DSVXXX_SENSORHUB_TARGET0_TAG 0xE
```

相关声明：[LSM6DSVXXX_SENSORHUB_TARGET0_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga087907d682457fe1b4fec7a19f781910)。

传感器集线器目标（Sensor-hub Target）0。

<a id="r_gaf27c820db6fe6b17ab480ef85cf393b7"></a>

```c
#define LSM6DSVXXX_SENSORHUB_TARGET1_TAG 0xF
```

相关声明：[LSM6DSVXXX_SENSORHUB_TARGET1_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaf27c820db6fe6b17ab480ef85cf393b7)。

传感器集线器目标（Sensor-hub Target）1。

<a id="r_ga4bf7e0ad77c3d15db6903fa1dff8fa87"></a>

```c
#define LSM6DSVXXX_SENSORHUB_TARGET2_TAG 0x10
```

相关声明：[LSM6DSVXXX_SENSORHUB_TARGET2_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga4bf7e0ad77c3d15db6903fa1dff8fa87)。

传感器集线器目标（Sensor-hub Target）2。

<a id="r_gafeb7c36af782d046f24b74292f4ace83"></a>

```c
#define LSM6DSVXXX_SENSORHUB_TARGET3_TAG 0x11
```

相关声明：[LSM6DSVXXX_SENSORHUB_TARGET3_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gafeb7c36af782d046f24b74292f4ace83)。

传感器集线器目标（Sensor-hub Target）3。

<a id="r_gae256607af0954b035571be6c0a6348e1"></a>

```c
#define LSM6DSVXXX_STEP_COUNTER_TAG 0x12
```

相关声明：[LSM6DSVXXX_STEP_COUNTER_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae256607af0954b035571be6c0a6348e1)。

步数计数器（Step Counter）。

<a id="r_ga6fe39933ed4405ddc6e234f533215327"></a>

```c
#define LSM6DSVXXX_SFLP_GAME_ROTATION_VECTOR_TAG 0x13
```

相关声明：[LSM6DSVXXX_SFLP_GAME_ROTATION_VECTOR_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga6fe39933ed4405ddc6e234f533215327)。

SFLP 游戏旋转向量（Game-rotation Vector）。

<a id="r_ga213228f246738c27b2f59b6bfd7d8f02"></a>

```c
#define LSM6DSVXXX_SFLP_GYROSCOPE_BIAS_TAG 0x16
```

相关声明：[LSM6DSVXXX_SFLP_GYROSCOPE_BIAS_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga213228f246738c27b2f59b6bfd7d8f02)。

SFLP 陀螺仪偏置（Gyroscope Bias）。

<a id="r_ga5e919c257bd092142cf1830266d98031"></a>

```c
#define LSM6DSVXXX_SFLP_GRAVITY_VECTOR_TAG 0x17
```

相关声明：[LSM6DSVXXX_SFLP_GRAVITY_VECTOR_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5e919c257bd092142cf1830266d98031)。

SFLP 重力向量（Gravity Vector）。

<a id="r_ga2f00d0a884eadf2c1c73e49d9e06e62e"></a>

```c
#define LSM6DSVXXX_HG_XL_PEAK_TAG 0x18
```

相关声明：[LSM6DSVXXX_HG_XL_PEAK_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2f00d0a884eadf2c1c73e49d9e06e62e)。

高 g 加速度计峰值（High-g Accelerometer Peak）。

<a id="r_ga7fb42233e1c2cbed5e6bda21393788da"></a>

```c
#define LSM6DSVXXX_SENSORHUB_NACK_TAG 0x19
```

相关声明：[LSM6DSVXXX_SENSORHUB_NACK_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga7fb42233e1c2cbed5e6bda21393788da)。

传感器集线器否定应答（Sensor-hub NACK）。

<a id="r_ga82ca6346bc78a1ba4d928a3605a2447c"></a>

```c
#define LSM6DSVXXX_MLC_RESULT_TAG 0x1A
```

相关声明：[LSM6DSVXXX_MLC_RESULT_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga82ca6346bc78a1ba4d928a3605a2447c)。

机器学习核心结果（Machine-learning Core Result）。

<a id="r_ga3b8cdba38288aa6da8e2636e9bfd011f"></a>

```c
#define LSM6DSVXXX_MLC_FILTER 0x1B
```

相关声明：[LSM6DSVXXX_MLC_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga3b8cdba38288aa6da8e2636e9bfd011f)。

机器学习核心滤波器（Machine-learning Core Filter）。

<a id="r_ga4c6e247b7f1deb8ae05b661d0490907f"></a>

```c
#define LSM6DSVXXX_MLC_FEATURE 0x1C
```

相关声明：[LSM6DSVXXX_MLC_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga4c6e247b7f1deb8ae05b661d0490907f)。

机器学习核心特征（Machine-learning Core Feature）。

<a id="r_ga44578392f8501ba6ac317746b9083bd8"></a>

```c
#define LSM6DSVXXX_XL_HG_TAG 0x1D
```

相关声明：[LSM6DSVXXX_XL_HG_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga44578392f8501ba6ac317746b9083bd8)。

高 g 加速度计（High-g Accelerometer）。

<a id="r_ga30b4ae439b3705d2c3a245f6794237e4"></a>

```c
#define LSM6DSVXXX_GY_ENHANCED_EIS 0x1E
```

相关声明：[LSM6DSVXXX_GY_ENHANCED_EIS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga30b4ae439b3705d2c3a245f6794237e4)。

陀螺仪增强电子防抖（Gyroscope Enhanced EIS）。

<a id="define-members-7"></a>

### 状态与输出寄存器地址（Status and output register addresses）

驱动使用的状态寄存器和输出寄存器地址（Status and Output Register Addresses）。

<a id="r_ga0e8060623183b30ed20b434bee4c3418"></a>

```c
#define LSM6DSVXXX_STATUS_REG 0x1EU
```

相关声明：[LSM6DSVXXX_STATUS_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0e8060623183b30ed20b434bee4c3418)。

`STATUS_REG` 寄存器（Register）。

<a id="r_ga9eec9a8f38708f0fef6c23ccd98a49d9"></a>

```c
#define LSM6DSVXXX_OUTX_L_A 0x28U
```

相关声明：[LSM6DSVXXX_OUTX_L_A](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga9eec9a8f38708f0fef6c23ccd98a49d9)。

`OUTX_L_A` 加速度计输出（Accelerometer Output）。

<a id="r_ga68dc130a24d8670e943edb4a8a0677b8"></a>

```c
#define LSM6DSVXXX_FIFO_STATUS1 0x1BU
```

相关声明：[LSM6DSVXXX_FIFO_STATUS1](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga68dc130a24d8670e943edb4a8a0677b8)。

FIFO_STATUS1 寄存器（Register）。

<a id="r_ga4ddcf2c91859da3e4c9738432eaced59"></a>

```c
#define LSM6DSVXXX_FIFO_DATA_OUT_TAG 0x78U
```

相关声明：[LSM6DSVXXX_FIFO_DATA_OUT_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga4ddcf2c91859da3e4c9738432eaced59)。

FIFO_DATA_OUT_TAG 寄存器（Register）。

<a id="define-members-8"></a>

### FIFO 控制寄存器地址与模式（FIFO control register addresses and modes）

驱动使用的 FIFO 控制寄存器地址及模式值（FIFO Control Register Addresses and Mode Values）。

<a id="r_ga499e5dfd705abdb9e1d06660da62c80b"></a>

```c
#define LSM6DSVXXX_BYPASS_MODE 0x00U
```

相关声明：[LSM6DSVXXX_BYPASS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga499e5dfd705abdb9e1d06660da62c80b)。

FIFO 旁路模式（Bypass Mode），即禁用。

<a id="r_ga54bcb9e05b7a0297ecc150676f4d9060"></a>

```c
#define LSM6DSVXXX_FIFO_CTRL4 0x0AU
```

相关声明：[LSM6DSVXXX_FIFO_CTRL4](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga54bcb9e05b7a0297ecc150676f4d9060)。

`FIFO_CTRL4` 寄存器（Register）。

<a id="define-members-9"></a>

### GPIO 中断配置（Interrupt Configuration）

设备树属性（Devicetree Property）`int-gpio-config` 的取值。

<a id="r_ga12502cd7c50cfbce5bd5953278e9541a"></a>

```c
#define LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE 0
```

相关声明：[LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga12502cd7c50cfbce5bd5953278e9541a)。

边沿触发中断（Edge-Triggered Interrupt）。

<a id="r_ga8ebdca143d57f1d3d3c894c9afdf5be8"></a>

```c
#define LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE 1
```

相关声明：[LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga8ebdca143d57f1d3d3c894c9afdf5be8)。

电平触发中断（Level-Triggered Interrupt）。


## 2.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P207_lsm6dsvxxx.h_源码浏览.md)
- [LSM6DSVXXX_DT_ODR_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa2f3a91a76a073c7ab7ed54766191bfc)
- [LSM6DSVXXX_DT_ODR_AT_1Hz875](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga3be748256792c3a92a53860ba35ec37e)
- [LSM6DSVXXX_DT_ODR_AT_7Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gabc401ff628f557d26e4b563c59a5a1fd)
- [LSM6DSVXXX_DT_ODR_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga3f4f72d9ba0886cabd2b8c2b722fb4a4)
- [LSM6DSVXXX_DT_ODR_AT_30Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga11812be3986cb32212fed1cbe633bb02)
- [LSM6DSVXXX_DT_ODR_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga9844e2a752e351ad60b9ba33fe115a5d)
- [LSM6DSVXXX_DT_ODR_AT_120Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gadd4d620ed3e4bf2d1634038fa562d125)
- [LSM6DSVXXX_DT_ODR_AT_240Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga89e9deb98803378fe536f8be047ba163)
- [LSM6DSVXXX_DT_ODR_AT_480Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gabaa02a50ecf88a84ba1936e05b9cda64)
- [LSM6DSVXXX_DT_ODR_AT_960Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga1b6fdb03a0aa1afb1b1dd4b9b17480f8)
- [LSM6DSVXXX_DT_ODR_AT_1920Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga6fb1ef88249f73a0f77d41f80cae9b92)
- [LSM6DSVXXX_DT_ODR_AT_3840Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga755a4e96058319aff0cc1dfc9d83b543)
- [LSM6DSVXXX_DT_ODR_AT_7680Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga47178c61455a339ac1f488cfeca5df36)
- [LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gac2e60f249f1ef4a78959e65580f74452)
- [LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gafaf3d1f73b95285b7e0eb9daa26b71ce)
- [LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaf90fd3e38738689eefacff410e1806fc)
- [LSM6DSVXXX_DT_ODR_HA01_AT_125Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gacf3aa8af4d68646513cdcdd924567e9c)
- [LSM6DSVXXX_DT_ODR_HA01_AT_250Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2022940241f4c0fdf19fb98c0e1cc1b1)
- [LSM6DSVXXX_DT_ODR_HA01_AT_500Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5723fb099f01688aeb21439419484ca8)
- [LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga65d87ec8c3178d759633adf4e31decda)
- [LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga150d749dc27d494a17620b9a88fb91e9)
- [LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga175f2f879cf54c6d056c14b4e8ac6492)
- [LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa4a3e31a309fe54777323a71231f61e2)
- [LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab1553739349be4c090b648a8f6ce7b21)
- [LSM6DSVXXX_DT_ODR_HA02_AT_25Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gafdc624740a59409cc921a6883237d4bf)
- [LSM6DSVXXX_DT_ODR_HA02_AT_50Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gad630053a419a49eb0aaa0068b552cf2c)
- [LSM6DSVXXX_DT_ODR_HA02_AT_100Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab8c0b7c9847d33260ed82a569f09ee7d)
- [LSM6DSVXXX_DT_ODR_HA02_AT_200Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga10f700875a21fa4a163446acb97035d5)
- [LSM6DSVXXX_DT_ODR_HA02_AT_400Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga96e0ab14e77c9b39757ceecdd6184388)
- [LSM6DSVXXX_DT_ODR_HA02_AT_800Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga95521c6f18519bead2be0d35ec3cf127)
- [LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa7df01142e7bf1227e1bd833f4b21fd8)
- [LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga8e18d124dd79ed9b654dd0b6b4f602b4)
- [LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae9c7edb6bf740c8b6e630e8bed92ce78)
- [LSM6DSVXXX_DT_XL_NOT_BATCHED](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2d5a1021d7aae23240f7d2b9daba868d)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_1Hz875](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gafda071feff90a5a8870e4f4e4922fc56)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_7Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5d43c2750c55ece3dded6a61f5c3d78b)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga60c9cd315c0df0df8675ea9075ff5f60)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_30Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaab1720de9852174953ab3db6b61ed9f7)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga8425ee828bab319ccd97a35591a86802)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_120Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gac7c6daed24a500629ab3c4455363cf12)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_240Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab1eab92c52d5e83aa8f1bb8fc586e5a0)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_480Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae6f80d519366c78ee9b25c368def7fe2)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_960Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaea7a895fd766ffdddefff82b9dc9b2f8)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_1920Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga73d83e5c025af1a3ba7c11b8c98594a0)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_3840Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gabe653b1f4634c8db6dd0abb98eeaf993)
- [LSM6DSVXXX_DT_XL_BATCHED_AT_7680Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2c57246c8035e01914d63bf497241bd5)
- [LSM6DSVXXX_DT_GY_NOT_BATCHED](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga21074319549fe782f14885b8cf4e598e)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_1Hz875](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga6701e54d1bdc9cc38b78869d422b4a24)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_7Hz5](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga1d71dcadbdb735c1ed67d33f64dcc377)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga74cf3363ef11b6f309d187e15511da0f)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_30Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga1f90e6eb1041d2adaa5b3904bc7c3ec5)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga04b59445efcaba20b9de75f118621036)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_120Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gad54fb498d1ac9a79e933fef1b3135b44)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_240Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga379a95a050085645c6b667be959917f1)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_480Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab8e2d1c1e5fbbc94c5205bd36a18c698)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_960Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae827fd454d5fd6621dcaded3cde58dce)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_1920Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0d9391fcf25e211e74b96b0567690e8c)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_3840Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa618e22a3ee6a5cd08512d75a2f8ba23)
- [LSM6DSVXXX_DT_GY_BATCHED_AT_7680Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga1433bcac6731056771402543cb52b05d)
- [LSM6DSVXXX_DT_TEMP_NOT_BATCHED](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5b0ec9d5af96cba4f214f9cc18725d4a)
- [LSM6DSVXXX_DT_TEMP_BATCHED_AT_1Hz875](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa4f00b050752fcd61a8b374ffc3e53e2)
- [LSM6DSVXXX_DT_TEMP_BATCHED_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga959ed5facb6f55bb105766fed641fb3b)
- [LSM6DSVXXX_DT_TEMP_BATCHED_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5fd9d7951f7e13eae7240dceba715a0d)
- [LSM6DSVXXX_DT_SFLP_ODR_AT_15Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gadfe3e073293cc1f28dd35fdcbcb64504)
- [LSM6DSVXXX_DT_SFLP_ODR_AT_30Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0728a6554ed8585a5eaf705ad0ab8b84)
- [LSM6DSVXXX_DT_SFLP_ODR_AT_60Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga293ecc01f316565790cf1de00511f7e5)
- [LSM6DSVXXX_DT_SFLP_ODR_AT_120Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5bd64654e4cba2e05d4c686a6008673b)
- [LSM6DSVXXX_DT_SFLP_ODR_AT_240Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga001956d8e537d42ec356240be93caff5)
- [LSM6DSVXXX_DT_SFLP_ODR_AT_480Hz](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2a25517fc9b890b150e5ca8d1b88990c)
- [LSM6DSVXXX_DT_SFLP_FIFO_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae2e528f1f3eb49e1f3098c624b76441a)
- [LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaeff5ded37cf0bdbdb1dcaac49a19fd75)
- [LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga57ad9deaa73162e5350e171c79cd87ec)
- [LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga37dcd41d788f62ca71fb4edc392e8c70)
- [LSM6DSVXXX_DT_SFLP_FIFO_GBIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga767e76d5e63f6c23c078b574e48cb445)
- [LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GBIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5a2e8191ce4daf332c818629b071bb91)
- [LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY_GBIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0f26c813d590aac8d94522144ea6b9a1)
- [LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY_GBIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga4e6154f4150417d3240bdb88caf578ff)
- [LSM6DSVXXX_FIFO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga471b55f70fc3375571160acb78ad2617)
- [LSM6DSVXXX_GY_NC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga7cca9213d67413e009dbb2fa74bf7bb3)
- [LSM6DSVXXX_XL_NC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga320efe292f3c5121031d0d8f5436a5e7)
- [LSM6DSVXXX_TEMPERATURE_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga49900f3a225fad10e3eff3c251de3ef9)
- [LSM6DSVXXX_TIMESTAMP_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae8e6953df547162248da27a53a6d8ddf)
- [LSM6DSVXXX_CFG_CHANGE_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gac63cd2760ac68a57ab916e6a7ab41e01)
- [LSM6DSVXXX_XL_NC_T_2_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gabbd301aa0313208a3df654b587e41b09)
- [LSM6DSVXXX_XL_NC_T_1_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gab375a7fe25056957f5dc100b24185d37)
- [LSM6DSVXXX_XL_2XC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gad74ab246e526843a3a9c0b51aff23bf3)
- [LSM6DSVXXX_XL_3XC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gad17ba982da4ff778dd789adc597267d8)
- [LSM6DSVXXX_GY_NC_T_2_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2e3cdeecf56735b7261d1ff4220e7031)
- [LSM6DSVXXX_GY_NC_T_1_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa17a548bc43898f64a7106fa9c6a7df5)
- [LSM6DSVXXX_GY_2XC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaca3fdec6fd30386a9c0393331da4c57f)
- [LSM6DSVXXX_GY_3XC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga050b458172c45ae15319ae397a046c50)
- [LSM6DSVXXX_SENSORHUB_TARGET0_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga087907d682457fe1b4fec7a19f781910)
- [LSM6DSVXXX_SENSORHUB_TARGET1_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaf27c820db6fe6b17ab480ef85cf393b7)
- [LSM6DSVXXX_SENSORHUB_TARGET2_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga4bf7e0ad77c3d15db6903fa1dff8fa87)
- [LSM6DSVXXX_SENSORHUB_TARGET3_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gafeb7c36af782d046f24b74292f4ace83)
- [LSM6DSVXXX_STEP_COUNTER_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gae256607af0954b035571be6c0a6348e1)
- [LSM6DSVXXX_SFLP_GAME_ROTATION_VECTOR_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga6fe39933ed4405ddc6e234f533215327)
- [LSM6DSVXXX_SFLP_GYROSCOPE_BIAS_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga213228f246738c27b2f59b6bfd7d8f02)
- [LSM6DSVXXX_SFLP_GRAVITY_VECTOR_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga5e919c257bd092142cf1830266d98031)
- [LSM6DSVXXX_HG_XL_PEAK_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga2f00d0a884eadf2c1c73e49d9e06e62e)
- [LSM6DSVXXX_SENSORHUB_NACK_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga7fb42233e1c2cbed5e6bda21393788da)
- [LSM6DSVXXX_MLC_RESULT_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga82ca6346bc78a1ba4d928a3605a2447c)
- [LSM6DSVXXX_MLC_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga3b8cdba38288aa6da8e2636e9bfd011f)
- [LSM6DSVXXX_MLC_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga4c6e247b7f1deb8ae05b661d0490907f)
- [LSM6DSVXXX_XL_HG_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga44578392f8501ba6ac317746b9083bd8)
- [LSM6DSVXXX_GY_ENHANCED_EIS](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga30b4ae439b3705d2c3a245f6794237e4)
- [LSM6DSVXXX_STATUS_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0e8060623183b30ed20b434bee4c3418)
- [LSM6DSVXXX_OUTX_L_A](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga9eec9a8f38708f0fef6c23ccd98a49d9)
- [LSM6DSVXXX_FIFO_STATUS1](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga68dc130a24d8670e943edb4a8a0677b8)
- [LSM6DSVXXX_FIFO_DATA_OUT_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga4ddcf2c91859da3e4c9738432eaced59)
- [LSM6DSVXXX_BYPASS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga499e5dfd705abdb9e1d06660da62c80b)
- [LSM6DSVXXX_FIFO_CTRL4](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga54bcb9e05b7a0297ecc150676f4d9060)
- [LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga12502cd7c50cfbce5bd5953278e9541a)
- [LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga8ebdca143d57f1d3d3c894c9afdf5be8)

<a id="header-details"></a>

---

[上一章](P001_zephyr__drivers__pcie__cap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__llext__elf.h_文件参考.md)
