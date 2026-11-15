---
id: learning.zephyr-docs.api-fota-storage-topic-reference.page-5
title: LSM6DSVXXX API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_LSM6DSVXXX API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ST Microelectronics LSM6DSVXXX 三轴惯性测量单元（3-axis IMU）系列。

<a id="details"></a>

ST Microelectronics LSM6DSVXXX 三轴惯性测量单元（3-axis IMU）系列。

<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_lsm6dsvxxx_2Eh"></a>

```c
file lsm6dsvxxx.h
```

相关声明：[lsm6dsvxxx.h](../api_file_configuration_reference/P019_zephyr__drivers__sensor__lsm6dsvxxx.h_文件参考.md)。

LSM6DSVXXX传感器的扩展API头文件（Extended Sensor API Header）。

```c
file lsm6dsvxxx.h
```

相关声明：[lsm6dsvxxx.h](../api_file_network_pcie_reference/P002_zephyr__dt-bindings__sensor__lsm6dsvxxx.h_文件参考.md)。

ST LSM6DSVxxx六轴惯性测量单元（6-Axis IMUs）共享的设备树绑定常量。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.2\_枚举（Enumerations）

<a id="r_gaa40abf78652db54d4b43b41c7750b558"></a>

```c
enum sensor_attribute_lsm6dsvxxx { SENSOR_ATTR_GET_SELF_TEST_RESULT = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_lsm6dsvxxx](#gaa40abf78652db54d4b43b41c7750b558)、[SENSOR_ATTR_GET_SELF_TEST_RESULT](#ggaa40abf78652db54d4b43b41c7750b558a3b1d8afe96e306670568008d1f8b5a5d)。

LSM6DSVXXX 的自定义传感器属性（Custom Sensor Attributes）。

<a id="r_ga0e2d73310764e4ad782f20f9e2b2da46"></a>

```c
enum lsm6dsvxxx_self_test_result { LSM6DSVXXX_ST_OK = 0 , LSM6DSVXXX_ST_FAIL = 1 }
```

相关声明：[lsm6dsvxxx_self_test_result](#ga0e2d73310764e4ad782f20f9e2b2da46)、[LSM6DSVXXX_ST_OK](#gga0e2d73310764e4ad782f20f9e2b2da46a01c6e9bb517b46bd18e2d69b1eb02349)、[LSM6DSVXXX_ST_FAIL](#gga0e2d73310764e4ad782f20f9e2b2da46a18d5155644c60de23dde8bf2ca3f5a36)。

LSM6DSVXXX 的自检结果（Self-Test Result）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 5.3\_加速度计和陀螺仪数据速率（Accelerometer and gyroscope data rates）

设备树（Devicetree）属性 `accel-odr` 和 `gyro-odr` 的取值。

HA01 和 HA02 分别选择第一组和第二组高精度输出数据率（High-accuracy ODR）设置。

<a id="r_gaa2f3a91a76a073c7ab7ed54766191bfc"></a>

```c
#define LSM6DSVXXX_DT_ODR_OFF 0x0
```

相关声明：[LSM6DSVXXX_DT_ODR_OFF](#gaa2f3a91a76a073c7ab7ed54766191bfc)。

已断电（Powered Down）。

<a id="r_ga3be748256792c3a92a53860ba35ec37e"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_1Hz875 0x1
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_1Hz875](#ga3be748256792c3a92a53860ba35ec37e)。

1.875 Hz

<a id="r_gabc401ff628f557d26e4b563c59a5a1fd"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_7Hz5 0x2
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_7Hz5](#gabc401ff628f557d26e4b563c59a5a1fd)。

7.5 Hz

<a id="r_ga3f4f72d9ba0886cabd2b8c2b722fb4a4"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_15Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_15Hz](#ga3f4f72d9ba0886cabd2b8c2b722fb4a4)。

15 Hz

<a id="r_ga11812be3986cb32212fed1cbe633bb02"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_30Hz 0x4
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_30Hz](#ga11812be3986cb32212fed1cbe633bb02)。

30 Hz

<a id="r_ga9844e2a752e351ad60b9ba33fe115a5d"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_60Hz 0x5
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_60Hz](#ga9844e2a752e351ad60b9ba33fe115a5d)。

60 Hz

<a id="r_gadd4d620ed3e4bf2d1634038fa562d125"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_120Hz 0x6
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_120Hz](#gadd4d620ed3e4bf2d1634038fa562d125)。

120 Hz

<a id="r_ga89e9deb98803378fe536f8be047ba163"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_240Hz 0x7
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_240Hz](#ga89e9deb98803378fe536f8be047ba163)。

240 Hz

<a id="r_gabaa02a50ecf88a84ba1936e05b9cda64"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_480Hz 0x8
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_480Hz](#gabaa02a50ecf88a84ba1936e05b9cda64)。

480 Hz（赫兹）。

<a id="r_ga1b6fdb03a0aa1afb1b1dd4b9b17480f8"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_960Hz 0x9
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_960Hz](#ga1b6fdb03a0aa1afb1b1dd4b9b17480f8)。

960 Hz（赫兹）。

<a id="r_ga6fb1ef88249f73a0f77d41f80cae9b92"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_1920Hz 0xA
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_1920Hz](#ga6fb1ef88249f73a0f77d41f80cae9b92)。

1920 Hz（赫兹）。

<a id="r_ga755a4e96058319aff0cc1dfc9d83b543"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_3840Hz 0xB
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_3840Hz](#ga755a4e96058319aff0cc1dfc9d83b543)。

3840 Hz（赫兹）。

<a id="r_ga47178c61455a339ac1f488cfeca5df36"></a>

```c
#define LSM6DSVXXX_DT_ODR_AT_7680Hz 0xC
```

相关声明：[LSM6DSVXXX_DT_ODR_AT_7680Hz](#ga47178c61455a339ac1f488cfeca5df36)。

7680 Hz（赫兹）。

<a id="r_gac2e60f249f1ef4a78959e65580f74452"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625 0x13
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625](#gac2e60f249f1ef4a78959e65580f74452)。

高精度 1（High-accuracy 1），15.625 Hz。

<a id="r_gafaf3d1f73b95285b7e0eb9daa26b71ce"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25 0x14
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25](#gafaf3d1f73b95285b7e0eb9daa26b71ce)。

高精度 1（High-accuracy 1），31.25 Hz。

<a id="r_gaf90fd3e38738689eefacff410e1806fc"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5 0x15
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5](#gaf90fd3e38738689eefacff410e1806fc)。

高精度 1（High-accuracy 1），62.5 Hz。

<a id="r_gacf3aa8af4d68646513cdcdd924567e9c"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_125Hz 0x16
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_125Hz](#gacf3aa8af4d68646513cdcdd924567e9c)。

高精度 1（High-accuracy 1），125 Hz。

<a id="r_ga2022940241f4c0fdf19fb98c0e1cc1b1"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_250Hz 0x17
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_250Hz](#ga2022940241f4c0fdf19fb98c0e1cc1b1)。

高精度 1（High-accuracy 1），250 Hz。

<a id="r_ga5723fb099f01688aeb21439419484ca8"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_500Hz 0x18
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_500Hz](#ga5723fb099f01688aeb21439419484ca8)。

高精度 1（High-accuracy 1），500 Hz。

<a id="r_ga65d87ec8c3178d759633adf4e31decda"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz 0x19
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz](#ga65d87ec8c3178d759633adf4e31decda)。

高精度 1（High-accuracy 1），1000 Hz。

<a id="r_ga150d749dc27d494a17620b9a88fb91e9"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz 0x1A
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz](#ga150d749dc27d494a17620b9a88fb91e9)。

高精度 1（High-accuracy 1），2000 Hz。

<a id="r_ga175f2f879cf54c6d056c14b4e8ac6492"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz 0x1B
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz](#ga175f2f879cf54c6d056c14b4e8ac6492)。

高精度 1（High-accuracy 1），4000 Hz。

<a id="r_gaa4a3e31a309fe54777323a71231f61e2"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz 0x1C
```

相关声明：[LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz](#gaa4a3e31a309fe54777323a71231f61e2)。

高精度 1（High-accuracy 1），8000 Hz。

<a id="r_gab1553739349be4c090b648a8f6ce7b21"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5 0x23
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5](#gab1553739349be4c090b648a8f6ce7b21)。

高精度 2（High-accuracy 2），12.5 Hz。

<a id="r_gafdc624740a59409cc921a6883237d4bf"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_25Hz 0x24
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_25Hz](#gafdc624740a59409cc921a6883237d4bf)。

高精度 2（High-accuracy 2），25 Hz。

<a id="r_gad630053a419a49eb0aaa0068b552cf2c"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_50Hz 0x25
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_50Hz](#gad630053a419a49eb0aaa0068b552cf2c)。

高精度 2（High-accuracy 2），50 Hz。

<a id="r_gab8c0b7c9847d33260ed82a569f09ee7d"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_100Hz 0x26
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_100Hz](#gab8c0b7c9847d33260ed82a569f09ee7d)。

高精度 2（High-accuracy 2），100 Hz。

<a id="r_ga10f700875a21fa4a163446acb97035d5"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_200Hz 0x27
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_200Hz](#ga10f700875a21fa4a163446acb97035d5)。

高精度 2（High-accuracy 2），200 Hz。

<a id="r_ga96e0ab14e77c9b39757ceecdd6184388"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_400Hz 0x28
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_400Hz](#ga96e0ab14e77c9b39757ceecdd6184388)。

高精度 2（High-accuracy 2），400 Hz。

<a id="r_ga95521c6f18519bead2be0d35ec3cf127"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_800Hz 0x29
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_800Hz](#ga95521c6f18519bead2be0d35ec3cf127)。

高精度 2（High-accuracy 2），800 Hz。

<a id="r_gaa7df01142e7bf1227e1bd833f4b21fd8"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz 0x2A
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz](#gaa7df01142e7bf1227e1bd833f4b21fd8)。

高精度 2（High-accuracy 2），1600 Hz。

<a id="r_ga8e18d124dd79ed9b654dd0b6b4f602b4"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz 0x2B
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz](#ga8e18d124dd79ed9b654dd0b6b4f602b4)。

高精度 2（High-accuracy 2），3200 Hz。

<a id="r_gae9c7edb6bf740c8b6e630e8bed92ce78"></a>

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz 0x2C
```

相关声明：[LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz](#gae9c7edb6bf740c8b6e630e8bed92ce78)。

高精度 2（High-accuracy 2），6400 Hz。

## 5.4\_加速度计 FIFO 批量采集速率（Accelerometer FIFO batching rates）

设备树 accel-fifo-batch-rate 属性（Property）的值。

<a id="r_ga2d5a1021d7aae23240f7d2b9daba868d"></a>

```c
#define LSM6DSVXXX_DT_XL_NOT_BATCHED 0x0
```

相关声明：[LSM6DSVXXX_DT_XL_NOT_BATCHED](#ga2d5a1021d7aae23240f7d2b9daba868d)。

不批量入队（Not Batched）。

<a id="r_gafda071feff90a5a8870e4f4e4922fc56"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_1Hz875 0x1
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_1Hz875](#gafda071feff90a5a8870e4f4e4922fc56)。

1.875 Hz

<a id="r_ga5d43c2750c55ece3dded6a61f5c3d78b"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_7Hz5 0x2
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_7Hz5](#ga5d43c2750c55ece3dded6a61f5c3d78b)。

7.5 Hz

<a id="r_ga60c9cd315c0df0df8675ea9075ff5f60"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_15Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_15Hz](#ga60c9cd315c0df0df8675ea9075ff5f60)。

15 Hz

<a id="r_gaab1720de9852174953ab3db6b61ed9f7"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_30Hz 0x4
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_30Hz](#gaab1720de9852174953ab3db6b61ed9f7)。

30 Hz

<a id="r_ga8425ee828bab319ccd97a35591a86802"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_60Hz 0x5
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_60Hz](#ga8425ee828bab319ccd97a35591a86802)。

60 Hz

<a id="r_gac7c6daed24a500629ab3c4455363cf12"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_120Hz 0x6
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_120Hz](#gac7c6daed24a500629ab3c4455363cf12)。

120 Hz

<a id="r_gab1eab92c52d5e83aa8f1bb8fc586e5a0"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_240Hz 0x7
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_240Hz](#gab1eab92c52d5e83aa8f1bb8fc586e5a0)。

240 Hz

<a id="r_gae6f80d519366c78ee9b25c368def7fe2"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_480Hz 0x8
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_480Hz](#gae6f80d519366c78ee9b25c368def7fe2)。

480 Hz（赫兹）。

<a id="r_gaea7a895fd766ffdddefff82b9dc9b2f8"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_960Hz 0x9
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_960Hz](#gaea7a895fd766ffdddefff82b9dc9b2f8)。

960 Hz（赫兹）。

<a id="r_ga73d83e5c025af1a3ba7c11b8c98594a0"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_1920Hz 0xa
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_1920Hz](#ga73d83e5c025af1a3ba7c11b8c98594a0)。

1920 Hz（赫兹）。

<a id="r_gabe653b1f4634c8db6dd0abb98eeaf993"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_3840Hz 0xb
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_3840Hz](#gabe653b1f4634c8db6dd0abb98eeaf993)。

3840 Hz（赫兹）。

<a id="r_ga2c57246c8035e01914d63bf497241bd5"></a>

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_7680Hz 0xc
```

相关声明：[LSM6DSVXXX_DT_XL_BATCHED_AT_7680Hz](#ga2c57246c8035e01914d63bf497241bd5)。

7680 Hz（赫兹）。

## 5.5\_陀螺仪 FIFO 批量采集速率（Gyroscope FIFO batching rates）

设备树属性（Devicetree Property）`gyro-fifo-batch-rate` 的取值。

<a id="r_ga21074319549fe782f14885b8cf4e598e"></a>

```c
#define LSM6DSVXXX_DT_GY_NOT_BATCHED 0x0
```

相关声明：[LSM6DSVXXX_DT_GY_NOT_BATCHED](#ga21074319549fe782f14885b8cf4e598e)。

不批量入队（Not Batched）。

<a id="r_ga6701e54d1bdc9cc38b78869d422b4a24"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_1Hz875 0x1
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_1Hz875](#ga6701e54d1bdc9cc38b78869d422b4a24)。

1.875 Hz

<a id="r_ga1d71dcadbdb735c1ed67d33f64dcc377"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_7Hz5 0x2
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_7Hz5](#ga1d71dcadbdb735c1ed67d33f64dcc377)。

7.5 Hz

<a id="r_ga74cf3363ef11b6f309d187e15511da0f"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_15Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_15Hz](#ga74cf3363ef11b6f309d187e15511da0f)。

15 Hz

<a id="r_ga1f90e6eb1041d2adaa5b3904bc7c3ec5"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_30Hz 0x4
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_30Hz](#ga1f90e6eb1041d2adaa5b3904bc7c3ec5)。

30 Hz

<a id="r_ga04b59445efcaba20b9de75f118621036"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_60Hz 0x5
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_60Hz](#ga04b59445efcaba20b9de75f118621036)。

60 Hz

<a id="r_gad54fb498d1ac9a79e933fef1b3135b44"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_120Hz 0x6
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_120Hz](#gad54fb498d1ac9a79e933fef1b3135b44)。

120 Hz

<a id="r_ga379a95a050085645c6b667be959917f1"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_240Hz 0x7
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_240Hz](#ga379a95a050085645c6b667be959917f1)。

240 Hz

<a id="r_gab8e2d1c1e5fbbc94c5205bd36a18c698"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_480Hz 0x8
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_480Hz](#gab8e2d1c1e5fbbc94c5205bd36a18c698)。

480 Hz（赫兹）。

<a id="r_gae827fd454d5fd6621dcaded3cde58dce"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_960Hz 0x9
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_960Hz](#gae827fd454d5fd6621dcaded3cde58dce)。

960 Hz（赫兹）。

<a id="r_ga0d9391fcf25e211e74b96b0567690e8c"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_1920Hz 0xa
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_1920Hz](#ga0d9391fcf25e211e74b96b0567690e8c)。

1920 Hz（赫兹）。

<a id="r_gaa618e22a3ee6a5cd08512d75a2f8ba23"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_3840Hz 0xb
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_3840Hz](#gaa618e22a3ee6a5cd08512d75a2f8ba23)。

3840 Hz（赫兹）。

<a id="r_ga1433bcac6731056771402543cb52b05d"></a>

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_7680Hz 0xc
```

相关声明：[LSM6DSVXXX_DT_GY_BATCHED_AT_7680Hz](#ga1433bcac6731056771402543cb52b05d)。

7680 Hz（赫兹）。

## 5.6\_温度 FIFO 批量采集速率（Temperature FIFO batching rates）

设备树 temp-fifo-batch-rate 属性（Property）的值。

<a id="r_ga5b0ec9d5af96cba4f214f9cc18725d4a"></a>

```c
#define LSM6DSVXXX_DT_TEMP_NOT_BATCHED 0x0
```

相关声明：[LSM6DSVXXX_DT_TEMP_NOT_BATCHED](#ga5b0ec9d5af96cba4f214f9cc18725d4a)。

不批量入队（Not Batched）。

<a id="r_gaa4f00b050752fcd61a8b374ffc3e53e2"></a>

```c
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_1Hz875 0x1
```

相关声明：[LSM6DSVXXX_DT_TEMP_BATCHED_AT_1Hz875](#gaa4f00b050752fcd61a8b374ffc3e53e2)。

1.875 Hz

<a id="r_ga959ed5facb6f55bb105766fed641fb3b"></a>

```c
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_15Hz 0x2
```

相关声明：[LSM6DSVXXX_DT_TEMP_BATCHED_AT_15Hz](#ga959ed5facb6f55bb105766fed641fb3b)。

15 Hz

<a id="r_ga5fd9d7951f7e13eae7240dceba715a0d"></a>

```c
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_60Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_TEMP_BATCHED_AT_60Hz](#ga5fd9d7951f7e13eae7240dceba715a0d)。

60 Hz

## 5.7\_低功耗传感器融合数据速率（Sensor-fusion low-power data rates）

设备树属性（Devicetree Property）`sflp-odr` 的取值。

<a id="r_gadfe3e073293cc1f28dd35fdcbcb64504"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_15Hz 0x0
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_15Hz](#gadfe3e073293cc1f28dd35fdcbcb64504)。

15 Hz

<a id="r_ga0728a6554ed8585a5eaf705ad0ab8b84"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_30Hz 0x1
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_30Hz](#ga0728a6554ed8585a5eaf705ad0ab8b84)。

30 Hz

<a id="r_ga293ecc01f316565790cf1de00511f7e5"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_60Hz 0x2
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_60Hz](#ga293ecc01f316565790cf1de00511f7e5)。

60 Hz

<a id="r_ga5bd64654e4cba2e05d4c686a6008673b"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_120Hz 0x3
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_120Hz](#ga5bd64654e4cba2e05d4c686a6008673b)。

120 Hz

<a id="r_ga001956d8e537d42ec356240be93caff5"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_240Hz 0x4
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_240Hz](#ga001956d8e537d42ec356240be93caff5)。

240 Hz

<a id="r_ga2a25517fc9b890b150e5ca8d1b88990c"></a>

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_480Hz 0x5
```

相关声明：[LSM6DSVXXX_DT_SFLP_ODR_AT_480Hz](#ga2a25517fc9b890b150e5ca8d1b88990c)。

480 Hz（赫兹）。

## 5.8\_低功耗传感器融合 FIFO 输出（Sensor-fusion low-power FIFO outputs）

设备树属性（Devicetree Property）`sflp-fifo-enable` 的取值。

<a id="r_gae2e528f1f3eb49e1f3098c624b76441a"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_OFF 0x0
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_OFF](#gae2e528f1f3eb49e1f3098c624b76441a)。

无 SFLP 输出（No SFLP Output）。

<a id="r_gaeff5ded37cf0bdbdb1dcaac49a19fd75"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION 0x1
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION](#gaeff5ded37cf0bdbdb1dcaac49a19fd75)。

游戏旋转向量（Game-rotation Vector）。

<a id="r_ga57ad9deaa73162e5350e171c79cd87ec"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY 0x2
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY](#ga57ad9deaa73162e5350e171c79cd87ec)。

重力向量（Gravity Vector）。

<a id="r_ga37dcd41d788f62ca71fb4edc392e8c70"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY 0x3
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY](#ga37dcd41d788f62ca71fb4edc392e8c70)。

旋转与重力（Rotation and Gravity）。

<a id="r_ga767e76d5e63f6c23c078b574e48cb445"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GBIAS 0x4
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GBIAS](#ga767e76d5e63f6c23c078b574e48cb445)。

陀螺仪偏置（Gyroscope Bias）。

<a id="r_ga5a2e8191ce4daf332c818629b071bb91"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GBIAS 0x5
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GBIAS](#ga5a2e8191ce4daf332c818629b071bb91)。

旋转与陀螺仪偏置（Rotation and Gyro Bias）。

<a id="r_ga0f26c813d590aac8d94522144ea6b9a1"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY_GBIAS 0x6
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY_GBIAS](#ga0f26c813d590aac8d94522144ea6b9a1)。

重力与陀螺仪偏置（Gravity and Gyro Bias）。

<a id="r_ga4e6154f4150417d3240bdb88caf578ff"></a>

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY_GBIAS 0x7
```

相关声明：[LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY_GBIAS](#ga4e6154f4150417d3240bdb88caf578ff)。

旋转、重力与偏置（Rotation, Gravity, Bias）。

## 5.9\_FIFO 记录标签（FIFO Record Tags）

FIFO 数据流中报告的记录标签值（Record Tag Values）。

<a id="r_ga471b55f70fc3375571160acb78ad2617"></a>

```c
#define LSM6DSVXXX_FIFO_EMPTY 0x0
```

相关声明：[LSM6DSVXXX_FIFO_EMPTY](#ga471b55f70fc3375571160acb78ad2617)。

先进先出缓冲区（FIFO）为空。

<a id="r_ga7cca9213d67413e009dbb2fa74bf7bb3"></a>

```c
#define LSM6DSVXXX_GY_NC_TAG 0x1
```

相关声明：[LSM6DSVXXX_GY_NC_TAG](#ga7cca9213d67413e009dbb2fa74bf7bb3)。

陀螺仪（Gyroscope），不压缩。

<a id="r_ga320efe292f3c5121031d0d8f5436a5e7"></a>

```c
#define LSM6DSVXXX_XL_NC_TAG 0x2
```

相关声明：[LSM6DSVXXX_XL_NC_TAG](#ga320efe292f3c5121031d0d8f5436a5e7)。

加速度计（Accelerometer），不压缩。

<a id="r_ga49900f3a225fad10e3eff3c251de3ef9"></a>

```c
#define LSM6DSVXXX_TEMPERATURE_TAG 0x3
```

相关声明：[LSM6DSVXXX_TEMPERATURE_TAG](#ga49900f3a225fad10e3eff3c251de3ef9)。

温度（Temperature）。

<a id="r_gae8e6953df547162248da27a53a6d8ddf"></a>

```c
#define LSM6DSVXXX_TIMESTAMP_TAG 0x4
```

相关声明：[LSM6DSVXXX_TIMESTAMP_TAG](#gae8e6953df547162248da27a53a6d8ddf)。

时间戳（Timestamp）。

<a id="r_gac63cd2760ac68a57ab916e6a7ab41e01"></a>

```c
#define LSM6DSVXXX_CFG_CHANGE_TAG 0x5
```

相关声明：[LSM6DSVXXX_CFG_CHANGE_TAG](#gac63cd2760ac68a57ab916e6a7ab41e01)。

配置变化（Configuration Change）。

<a id="r_gabbd301aa0313208a3df654b587e41b09"></a>

```c
#define LSM6DSVXXX_XL_NC_T_2_TAG 0x6
```

相关声明：[LSM6DSVXXX_XL_NC_T_2_TAG](#gabbd301aa0313208a3df654b587e41b09)。

加速度计（Accelerometer），T-2 样本（Sample）。

<a id="r_gab375a7fe25056957f5dc100b24185d37"></a>

```c
#define LSM6DSVXXX_XL_NC_T_1_TAG 0x7
```

相关声明：[LSM6DSVXXX_XL_NC_T_1_TAG](#gab375a7fe25056957f5dc100b24185d37)。

加速度计（Accelerometer），T-1 样本（Sample）。

<a id="r_gad74ab246e526843a3a9c0b51aff23bf3"></a>

```c
#define LSM6DSVXXX_XL_2XC_TAG 0x8
```

相关声明：[LSM6DSVXXX_XL_2XC_TAG](#gad74ab246e526843a3a9c0b51aff23bf3)。

加速度计（Accelerometer），2 倍压缩（2x Compressed）。

<a id="r_gad17ba982da4ff778dd789adc597267d8"></a>

```c
#define LSM6DSVXXX_XL_3XC_TAG 0x9
```

相关声明：[LSM6DSVXXX_XL_3XC_TAG](#gad17ba982da4ff778dd789adc597267d8)。

加速度计（Accelerometer），3 倍压缩（3x Compressed）。

<a id="r_ga2e3cdeecf56735b7261d1ff4220e7031"></a>

```c
#define LSM6DSVXXX_GY_NC_T_2_TAG 0xA
```

相关声明：[LSM6DSVXXX_GY_NC_T_2_TAG](#ga2e3cdeecf56735b7261d1ff4220e7031)。

陀螺仪（Gyroscope），T-2 样本（Sample）。

<a id="r_gaa17a548bc43898f64a7106fa9c6a7df5"></a>

```c
#define LSM6DSVXXX_GY_NC_T_1_TAG 0xB
```

相关声明：[LSM6DSVXXX_GY_NC_T_1_TAG](#gaa17a548bc43898f64a7106fa9c6a7df5)。

陀螺仪（Gyroscope），T-1 样本（Sample）。

<a id="r_gaca3fdec6fd30386a9c0393331da4c57f"></a>

```c
#define LSM6DSVXXX_GY_2XC_TAG 0xC
```

相关声明：[LSM6DSVXXX_GY_2XC_TAG](#gaca3fdec6fd30386a9c0393331da4c57f)。

陀螺仪（Gyroscope），2 倍压缩（2x Compressed）。

<a id="r_ga050b458172c45ae15319ae397a046c50"></a>

```c
#define LSM6DSVXXX_GY_3XC_TAG 0xD
```

相关声明：[LSM6DSVXXX_GY_3XC_TAG](#ga050b458172c45ae15319ae397a046c50)。

陀螺仪（Gyroscope），3 倍压缩（3x Compressed）。

<a id="r_ga087907d682457fe1b4fec7a19f781910"></a>

```c
#define LSM6DSVXXX_SENSORHUB_TARGET0_TAG 0xE
```

相关声明：[LSM6DSVXXX_SENSORHUB_TARGET0_TAG](#ga087907d682457fe1b4fec7a19f781910)。

传感器集线器目标（Sensor-hub Target）0。

<a id="r_gaf27c820db6fe6b17ab480ef85cf393b7"></a>

```c
#define LSM6DSVXXX_SENSORHUB_TARGET1_TAG 0xF
```

相关声明：[LSM6DSVXXX_SENSORHUB_TARGET1_TAG](#gaf27c820db6fe6b17ab480ef85cf393b7)。

传感器集线器目标（Sensor-hub Target）1。

<a id="r_ga4bf7e0ad77c3d15db6903fa1dff8fa87"></a>

```c
#define LSM6DSVXXX_SENSORHUB_TARGET2_TAG 0x10
```

相关声明：[LSM6DSVXXX_SENSORHUB_TARGET2_TAG](#ga4bf7e0ad77c3d15db6903fa1dff8fa87)。

传感器集线器目标（Sensor-hub Target）2。

<a id="r_gafeb7c36af782d046f24b74292f4ace83"></a>

```c
#define LSM6DSVXXX_SENSORHUB_TARGET3_TAG 0x11
```

相关声明：[LSM6DSVXXX_SENSORHUB_TARGET3_TAG](#gafeb7c36af782d046f24b74292f4ace83)。

传感器集线器目标（Sensor-hub Target）3。

<a id="r_gae256607af0954b035571be6c0a6348e1"></a>

```c
#define LSM6DSVXXX_STEP_COUNTER_TAG 0x12
```

相关声明：[LSM6DSVXXX_STEP_COUNTER_TAG](#gae256607af0954b035571be6c0a6348e1)。

步数计数器（Step Counter）。

<a id="r_ga6fe39933ed4405ddc6e234f533215327"></a>

```c
#define LSM6DSVXXX_SFLP_GAME_ROTATION_VECTOR_TAG 0x13
```

相关声明：[LSM6DSVXXX_SFLP_GAME_ROTATION_VECTOR_TAG](#ga6fe39933ed4405ddc6e234f533215327)。

SFLP 游戏旋转向量（Game-rotation Vector）。

<a id="r_ga213228f246738c27b2f59b6bfd7d8f02"></a>

```c
#define LSM6DSVXXX_SFLP_GYROSCOPE_BIAS_TAG 0x16
```

相关声明：[LSM6DSVXXX_SFLP_GYROSCOPE_BIAS_TAG](#ga213228f246738c27b2f59b6bfd7d8f02)。

SFLP 陀螺仪偏置（Gyroscope Bias）。

<a id="r_ga5e919c257bd092142cf1830266d98031"></a>

```c
#define LSM6DSVXXX_SFLP_GRAVITY_VECTOR_TAG 0x17
```

相关声明：[LSM6DSVXXX_SFLP_GRAVITY_VECTOR_TAG](#ga5e919c257bd092142cf1830266d98031)。

SFLP 重力向量（Gravity Vector）。

<a id="r_ga2f00d0a884eadf2c1c73e49d9e06e62e"></a>

```c
#define LSM6DSVXXX_HG_XL_PEAK_TAG 0x18
```

相关声明：[LSM6DSVXXX_HG_XL_PEAK_TAG](#ga2f00d0a884eadf2c1c73e49d9e06e62e)。

高 g 加速度计峰值（High-g Accelerometer Peak）。

<a id="r_ga7fb42233e1c2cbed5e6bda21393788da"></a>

```c
#define LSM6DSVXXX_SENSORHUB_NACK_TAG 0x19
```

相关声明：[LSM6DSVXXX_SENSORHUB_NACK_TAG](#ga7fb42233e1c2cbed5e6bda21393788da)。

传感器集线器否定应答（Sensor-hub NACK）。

<a id="r_ga82ca6346bc78a1ba4d928a3605a2447c"></a>

```c
#define LSM6DSVXXX_MLC_RESULT_TAG 0x1A
```

相关声明：[LSM6DSVXXX_MLC_RESULT_TAG](#ga82ca6346bc78a1ba4d928a3605a2447c)。

机器学习核心结果（Machine-learning Core Result）。

<a id="r_ga3b8cdba38288aa6da8e2636e9bfd011f"></a>

```c
#define LSM6DSVXXX_MLC_FILTER 0x1B
```

相关声明：[LSM6DSVXXX_MLC_FILTER](#ga3b8cdba38288aa6da8e2636e9bfd011f)。

机器学习核心滤波器（Machine-learning Core Filter）。

<a id="r_ga4c6e247b7f1deb8ae05b661d0490907f"></a>

```c
#define LSM6DSVXXX_MLC_FEATURE 0x1C
```

相关声明：[LSM6DSVXXX_MLC_FEATURE](#ga4c6e247b7f1deb8ae05b661d0490907f)。

机器学习核心特征（Machine-learning Core Feature）。

<a id="r_ga44578392f8501ba6ac317746b9083bd8"></a>

```c
#define LSM6DSVXXX_XL_HG_TAG 0x1D
```

相关声明：[LSM6DSVXXX_XL_HG_TAG](#ga44578392f8501ba6ac317746b9083bd8)。

高 g 加速度计（High-g Accelerometer）。

<a id="r_ga30b4ae439b3705d2c3a245f6794237e4"></a>

```c
#define LSM6DSVXXX_GY_ENHANCED_EIS 0x1E
```

相关声明：[LSM6DSVXXX_GY_ENHANCED_EIS](#ga30b4ae439b3705d2c3a245f6794237e4)。

陀螺仪增强电子防抖（Gyroscope Enhanced EIS）。

## 5.10\_状态与输出寄存器地址（Status and output register addresses）

驱动使用的状态寄存器和输出寄存器地址（Status and Output Register Addresses）。

<a id="r_ga0e8060623183b30ed20b434bee4c3418"></a>

```c
#define LSM6DSVXXX_STATUS_REG 0x1EU
```

相关声明：[LSM6DSVXXX_STATUS_REG](#ga0e8060623183b30ed20b434bee4c3418)。

`STATUS_REG` 寄存器（Register）。

<a id="r_ga9eec9a8f38708f0fef6c23ccd98a49d9"></a>

```c
#define LSM6DSVXXX_OUTX_L_A 0x28U
```

相关声明：[LSM6DSVXXX_OUTX_L_A](#ga9eec9a8f38708f0fef6c23ccd98a49d9)。

`OUTX_L_A` 加速度计输出（Accelerometer Output）。

<a id="r_ga68dc130a24d8670e943edb4a8a0677b8"></a>

```c
#define LSM6DSVXXX_FIFO_STATUS1 0x1BU
```

相关声明：[LSM6DSVXXX_FIFO_STATUS1](#ga68dc130a24d8670e943edb4a8a0677b8)。

FIFO_STATUS1 寄存器（Register）。

<a id="r_ga4ddcf2c91859da3e4c9738432eaced59"></a>

```c
#define LSM6DSVXXX_FIFO_DATA_OUT_TAG 0x78U
```

相关声明：[LSM6DSVXXX_FIFO_DATA_OUT_TAG](#ga4ddcf2c91859da3e4c9738432eaced59)。

FIFO_DATA_OUT_TAG 寄存器（Register）。

## 5.11\_FIFO 控制寄存器地址与模式（FIFO control register addresses and modes）

驱动使用的 FIFO 控制寄存器地址及模式值（FIFO Control Register Addresses and Mode Values）。

<a id="r_ga499e5dfd705abdb9e1d06660da62c80b"></a>

```c
#define LSM6DSVXXX_BYPASS_MODE 0x00U
```

相关声明：[LSM6DSVXXX_BYPASS_MODE](#ga499e5dfd705abdb9e1d06660da62c80b)。

FIFO 旁路模式（Bypass Mode），即禁用。

<a id="r_ga54bcb9e05b7a0297ecc150676f4d9060"></a>

```c
#define LSM6DSVXXX_FIFO_CTRL4 0x0AU
```

相关声明：[LSM6DSVXXX_FIFO_CTRL4](#ga54bcb9e05b7a0297ecc150676f4d9060)。

`FIFO_CTRL4` 寄存器（Register）。

## 5.12\_GPIO 中断配置（Interrupt Configuration）

设备树属性（Devicetree Property）`int-gpio-config` 的取值。

<a id="r_ga12502cd7c50cfbce5bd5953278e9541a"></a>

```c
#define LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE 0
```

相关声明：[LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE](#ga12502cd7c50cfbce5bd5953278e9541a)。

边沿触发中断（Edge-Triggered Interrupt）。

<a id="r_ga8ebdca143d57f1d3d3c894c9afdf5be8"></a>

```c
#define LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE 1
```

相关声明：[LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE](#ga8ebdca143d57f1d3d3c894c9afdf5be8)。

电平触发中断（Level-Triggered Interrupt）。

## 5.13\_详细说明（Detailed Documentation）

<a id="ga499e5dfd705abdb9e1d06660da62c80b"></a>

### `LSM6DSVXXX_BYPASS_MODE`

```c
#define LSM6DSVXXX_BYPASS_MODE 0x00U
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

FIFO 旁路模式（Bypass Mode），即禁用。

<a id="gac63cd2760ac68a57ab916e6a7ab41e01"></a>

### `LSM6DSVXXX_CFG_CHANGE_TAG`

```c
#define LSM6DSVXXX_CFG_CHANGE_TAG 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

配置变化（Configuration Change）。

<a id="ga12502cd7c50cfbce5bd5953278e9541a"></a>

### `LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE`

```c
#define LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

边沿触发中断（Edge-Triggered Interrupt）。

<a id="ga8ebdca143d57f1d3d3c894c9afdf5be8"></a>

### `LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE`

```c
#define LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

电平触发中断（Level-Triggered Interrupt）。

<a id="gad54fb498d1ac9a79e933fef1b3135b44"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_120Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_120Hz 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

120 Hz

<a id="ga74cf3363ef11b6f309d187e15511da0f"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_15Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_15Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

15 Hz

<a id="ga0d9391fcf25e211e74b96b0567690e8c"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_1920Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_1920Hz 0xa
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

1920 Hz（赫兹）。

<a id="ga6701e54d1bdc9cc38b78869d422b4a24"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_1Hz875`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_1Hz875 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

1.875 Hz

<a id="ga379a95a050085645c6b667be959917f1"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_240Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_240Hz 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

240 Hz

<a id="ga1f90e6eb1041d2adaa5b3904bc7c3ec5"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_30Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_30Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

30 Hz

<a id="gaa618e22a3ee6a5cd08512d75a2f8ba23"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_3840Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_3840Hz 0xb
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

3840 Hz（赫兹）。

<a id="gab8e2d1c1e5fbbc94c5205bd36a18c698"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_480Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_480Hz 0x8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

480 Hz（赫兹）。

<a id="ga04b59445efcaba20b9de75f118621036"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_60Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_60Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

60 Hz

<a id="ga1433bcac6731056771402543cb52b05d"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_7680Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_7680Hz 0xc
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

7680 Hz（赫兹）。

<a id="ga1d71dcadbdb735c1ed67d33f64dcc377"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_7Hz5`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_7Hz5 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

7.5 Hz

<a id="gae827fd454d5fd6621dcaded3cde58dce"></a>

### `LSM6DSVXXX_DT_GY_BATCHED_AT_960Hz`

```c
#define LSM6DSVXXX_DT_GY_BATCHED_AT_960Hz 0x9
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

960 Hz（赫兹）。

<a id="ga21074319549fe782f14885b8cf4e598e"></a>

### `LSM6DSVXXX_DT_GY_NOT_BATCHED`

```c
#define LSM6DSVXXX_DT_GY_NOT_BATCHED 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

不批量入队（Not Batched）。

<a id="gadd4d620ed3e4bf2d1634038fa562d125"></a>

### `LSM6DSVXXX_DT_ODR_AT_120Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_120Hz 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

120 Hz

<a id="ga3f4f72d9ba0886cabd2b8c2b722fb4a4"></a>

### `LSM6DSVXXX_DT_ODR_AT_15Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_15Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

15 Hz

<a id="ga6fb1ef88249f73a0f77d41f80cae9b92"></a>

### `LSM6DSVXXX_DT_ODR_AT_1920Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_1920Hz 0xA
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

1920 Hz（赫兹）。

<a id="ga3be748256792c3a92a53860ba35ec37e"></a>

### `LSM6DSVXXX_DT_ODR_AT_1Hz875`

```c
#define LSM6DSVXXX_DT_ODR_AT_1Hz875 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

1.875 Hz

<a id="ga89e9deb98803378fe536f8be047ba163"></a>

### `LSM6DSVXXX_DT_ODR_AT_240Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_240Hz 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

240 Hz

<a id="ga11812be3986cb32212fed1cbe633bb02"></a>

### `LSM6DSVXXX_DT_ODR_AT_30Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_30Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

30 Hz

<a id="ga755a4e96058319aff0cc1dfc9d83b543"></a>

### `LSM6DSVXXX_DT_ODR_AT_3840Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_3840Hz 0xB
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

3840 Hz（赫兹）。

<a id="gabaa02a50ecf88a84ba1936e05b9cda64"></a>

### `LSM6DSVXXX_DT_ODR_AT_480Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_480Hz 0x8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

480 Hz（赫兹）。

<a id="ga9844e2a752e351ad60b9ba33fe115a5d"></a>

### `LSM6DSVXXX_DT_ODR_AT_60Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_60Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

60 Hz

<a id="ga47178c61455a339ac1f488cfeca5df36"></a>

### `LSM6DSVXXX_DT_ODR_AT_7680Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_7680Hz 0xC
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

7680 Hz（赫兹）。

<a id="gabc401ff628f557d26e4b563c59a5a1fd"></a>

### `LSM6DSVXXX_DT_ODR_AT_7Hz5`

```c
#define LSM6DSVXXX_DT_ODR_AT_7Hz5 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

7.5 Hz

<a id="ga1b6fdb03a0aa1afb1b1dd4b9b17480f8"></a>

### `LSM6DSVXXX_DT_ODR_AT_960Hz`

```c
#define LSM6DSVXXX_DT_ODR_AT_960Hz 0x9
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

960 Hz（赫兹）。

<a id="ga65d87ec8c3178d759633adf4e31decda"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz 0x19
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），1000 Hz。

<a id="gacf3aa8af4d68646513cdcdd924567e9c"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_125Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_125Hz 0x16
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），125 Hz。

<a id="gac2e60f249f1ef4a78959e65580f74452"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625 0x13
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），15.625 Hz。

<a id="ga150d749dc27d494a17620b9a88fb91e9"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz 0x1A
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），2000 Hz。

<a id="ga2022940241f4c0fdf19fb98c0e1cc1b1"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_250Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_250Hz 0x17
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），250 Hz。

<a id="gafaf3d1f73b95285b7e0eb9daa26b71ce"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25 0x14
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），31.25 Hz。

<a id="ga175f2f879cf54c6d056c14b4e8ac6492"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz 0x1B
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），4000 Hz。

<a id="ga5723fb099f01688aeb21439419484ca8"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_500Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_500Hz 0x18
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），500 Hz。

<a id="gaf90fd3e38738689eefacff410e1806fc"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5 0x15
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），62.5 Hz。

<a id="gaa4a3e31a309fe54777323a71231f61e2"></a>

### `LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz 0x1C
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 1（High-accuracy 1），8000 Hz。

<a id="gab8c0b7c9847d33260ed82a569f09ee7d"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_100Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_100Hz 0x26
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），100 Hz。

<a id="gab1553739349be4c090b648a8f6ce7b21"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5 0x23
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），12.5 Hz。

<a id="gaa7df01142e7bf1227e1bd833f4b21fd8"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz 0x2A
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），1600 Hz。

<a id="ga10f700875a21fa4a163446acb97035d5"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_200Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_200Hz 0x27
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），200 Hz。

<a id="gafdc624740a59409cc921a6883237d4bf"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_25Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_25Hz 0x24
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），25 Hz。

<a id="ga8e18d124dd79ed9b654dd0b6b4f602b4"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz 0x2B
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），3200 Hz。

<a id="ga96e0ab14e77c9b39757ceecdd6184388"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_400Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_400Hz 0x28
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），400 Hz。

<a id="gad630053a419a49eb0aaa0068b552cf2c"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_50Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_50Hz 0x25
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），50 Hz。

<a id="gae9c7edb6bf740c8b6e630e8bed92ce78"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz 0x2C
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），6400 Hz。

<a id="ga95521c6f18519bead2be0d35ec3cf127"></a>

### `LSM6DSVXXX_DT_ODR_HA02_AT_800Hz`

```c
#define LSM6DSVXXX_DT_ODR_HA02_AT_800Hz 0x29
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高精度 2（High-accuracy 2），800 Hz。

<a id="gaa2f3a91a76a073c7ab7ed54766191bfc"></a>

### `LSM6DSVXXX_DT_ODR_OFF`

```c
#define LSM6DSVXXX_DT_ODR_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

已断电（Powered Down）。

<a id="gaeff5ded37cf0bdbdb1dcaac49a19fd75"></a>

### `LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION`

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

游戏旋转向量（Game-rotation Vector）。

<a id="ga5a2e8191ce4daf332c818629b071bb91"></a>

### `LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GBIAS`

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GBIAS 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

旋转与陀螺仪偏置（Rotation and Gyro Bias）。

<a id="ga37dcd41d788f62ca71fb4edc392e8c70"></a>

### `LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY`

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

旋转与重力（Rotation and Gravity）。

<a id="ga4e6154f4150417d3240bdb88caf578ff"></a>

### `LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY_GBIAS`

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY_GBIAS 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

旋转、重力与偏置（Rotation, Gravity, Bias）。

<a id="ga767e76d5e63f6c23c078b574e48cb445"></a>

### `LSM6DSVXXX_DT_SFLP_FIFO_GBIAS`

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GBIAS 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

陀螺仪偏置（Gyroscope Bias）。

<a id="ga57ad9deaa73162e5350e171c79cd87ec"></a>

### `LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY`

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

重力向量（Gravity Vector）。

<a id="ga0f26c813d590aac8d94522144ea6b9a1"></a>

### `LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY_GBIAS`

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY_GBIAS 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

重力与陀螺仪偏置（Gravity and Gyro Bias）。

<a id="gae2e528f1f3eb49e1f3098c624b76441a"></a>

### `LSM6DSVXXX_DT_SFLP_FIFO_OFF`

```c
#define LSM6DSVXXX_DT_SFLP_FIFO_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

无 SFLP 输出（No SFLP Output）。

<a id="ga5bd64654e4cba2e05d4c686a6008673b"></a>

### `LSM6DSVXXX_DT_SFLP_ODR_AT_120Hz`

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_120Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

120 Hz

<a id="gadfe3e073293cc1f28dd35fdcbcb64504"></a>

### `LSM6DSVXXX_DT_SFLP_ODR_AT_15Hz`

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_15Hz 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

15 Hz

<a id="ga001956d8e537d42ec356240be93caff5"></a>

### `LSM6DSVXXX_DT_SFLP_ODR_AT_240Hz`

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_240Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

240 Hz

<a id="ga0728a6554ed8585a5eaf705ad0ab8b84"></a>

### `LSM6DSVXXX_DT_SFLP_ODR_AT_30Hz`

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_30Hz 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

30 Hz

<a id="ga2a25517fc9b890b150e5ca8d1b88990c"></a>

### `LSM6DSVXXX_DT_SFLP_ODR_AT_480Hz`

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_480Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

480 Hz（赫兹）。

<a id="ga293ecc01f316565790cf1de00511f7e5"></a>

### `LSM6DSVXXX_DT_SFLP_ODR_AT_60Hz`

```c
#define LSM6DSVXXX_DT_SFLP_ODR_AT_60Hz 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

60 Hz

<a id="ga959ed5facb6f55bb105766fed641fb3b"></a>

### `LSM6DSVXXX_DT_TEMP_BATCHED_AT_15Hz`

```c
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_15Hz 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

15 Hz

<a id="gaa4f00b050752fcd61a8b374ffc3e53e2"></a>

### `LSM6DSVXXX_DT_TEMP_BATCHED_AT_1Hz875`

```c
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_1Hz875 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

1.875 Hz

<a id="ga5fd9d7951f7e13eae7240dceba715a0d"></a>

### `LSM6DSVXXX_DT_TEMP_BATCHED_AT_60Hz`

```c
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_60Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

60 Hz

<a id="ga5b0ec9d5af96cba4f214f9cc18725d4a"></a>

### `LSM6DSVXXX_DT_TEMP_NOT_BATCHED`

```c
#define LSM6DSVXXX_DT_TEMP_NOT_BATCHED 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

不批量入队（Not Batched）。

<a id="gac7c6daed24a500629ab3c4455363cf12"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_120Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_120Hz 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

120 Hz

<a id="ga60c9cd315c0df0df8675ea9075ff5f60"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_15Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_15Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

15 Hz

<a id="ga73d83e5c025af1a3ba7c11b8c98594a0"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_1920Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_1920Hz 0xa
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

1920 Hz（赫兹）。

<a id="gafda071feff90a5a8870e4f4e4922fc56"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_1Hz875`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_1Hz875 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

1.875 Hz

<a id="gab1eab92c52d5e83aa8f1bb8fc586e5a0"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_240Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_240Hz 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

240 Hz

<a id="gaab1720de9852174953ab3db6b61ed9f7"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_30Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_30Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

30 Hz

<a id="gabe653b1f4634c8db6dd0abb98eeaf993"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_3840Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_3840Hz 0xb
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

3840 Hz（赫兹）。

<a id="gae6f80d519366c78ee9b25c368def7fe2"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_480Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_480Hz 0x8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

480 Hz（赫兹）。

<a id="ga8425ee828bab319ccd97a35591a86802"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_60Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_60Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

60 Hz

<a id="ga2c57246c8035e01914d63bf497241bd5"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_7680Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_7680Hz 0xc
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

7680 Hz（赫兹）。

<a id="ga5d43c2750c55ece3dded6a61f5c3d78b"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_7Hz5`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_7Hz5 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

7.5 Hz

<a id="gaea7a895fd766ffdddefff82b9dc9b2f8"></a>

### `LSM6DSVXXX_DT_XL_BATCHED_AT_960Hz`

```c
#define LSM6DSVXXX_DT_XL_BATCHED_AT_960Hz 0x9
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

960 Hz（赫兹）。

<a id="ga2d5a1021d7aae23240f7d2b9daba868d"></a>

### `LSM6DSVXXX_DT_XL_NOT_BATCHED`

```c
#define LSM6DSVXXX_DT_XL_NOT_BATCHED 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

不批量入队（Not Batched）。

<a id="ga54bcb9e05b7a0297ecc150676f4d9060"></a>

### `LSM6DSVXXX_FIFO_CTRL4`

```c
#define LSM6DSVXXX_FIFO_CTRL4 0x0AU
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

`FIFO_CTRL4` 寄存器（Register）。

<a id="ga4ddcf2c91859da3e4c9738432eaced59"></a>

### `LSM6DSVXXX_FIFO_DATA_OUT_TAG`

```c
#define LSM6DSVXXX_FIFO_DATA_OUT_TAG 0x78U
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

FIFO_DATA_OUT_TAG 寄存器（Register）。

<a id="ga471b55f70fc3375571160acb78ad2617"></a>

### `LSM6DSVXXX_FIFO_EMPTY`

```c
#define LSM6DSVXXX_FIFO_EMPTY 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

先进先出缓冲区（FIFO）为空。

<a id="ga68dc130a24d8670e943edb4a8a0677b8"></a>

### `LSM6DSVXXX_FIFO_STATUS1`

```c
#define LSM6DSVXXX_FIFO_STATUS1 0x1BU
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

FIFO_STATUS1 寄存器（Register）。

<a id="gaca3fdec6fd30386a9c0393331da4c57f"></a>

### `LSM6DSVXXX_GY_2XC_TAG`

```c
#define LSM6DSVXXX_GY_2XC_TAG 0xC
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

陀螺仪（Gyroscope），2 倍压缩（2x Compressed）。

<a id="ga050b458172c45ae15319ae397a046c50"></a>

### `LSM6DSVXXX_GY_3XC_TAG`

```c
#define LSM6DSVXXX_GY_3XC_TAG 0xD
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

陀螺仪（Gyroscope），3 倍压缩（3x Compressed）。

<a id="ga30b4ae439b3705d2c3a245f6794237e4"></a>

### `LSM6DSVXXX_GY_ENHANCED_EIS`

```c
#define LSM6DSVXXX_GY_ENHANCED_EIS 0x1E
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

陀螺仪增强电子防抖（Gyroscope Enhanced EIS）。

<a id="gaa17a548bc43898f64a7106fa9c6a7df5"></a>

### `LSM6DSVXXX_GY_NC_T_1_TAG`

```c
#define LSM6DSVXXX_GY_NC_T_1_TAG 0xB
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

陀螺仪（Gyroscope），T-1 样本（Sample）。

<a id="ga2e3cdeecf56735b7261d1ff4220e7031"></a>

### `LSM6DSVXXX_GY_NC_T_2_TAG`

```c
#define LSM6DSVXXX_GY_NC_T_2_TAG 0xA
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

陀螺仪（Gyroscope），T-2 样本（Sample）。

<a id="ga7cca9213d67413e009dbb2fa74bf7bb3"></a>

### `LSM6DSVXXX_GY_NC_TAG`

```c
#define LSM6DSVXXX_GY_NC_TAG 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

陀螺仪（Gyroscope），不压缩。

<a id="ga2f00d0a884eadf2c1c73e49d9e06e62e"></a>

### `LSM6DSVXXX_HG_XL_PEAK_TAG`

```c
#define LSM6DSVXXX_HG_XL_PEAK_TAG 0x18
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高 g 加速度计峰值（High-g Accelerometer Peak）。

<a id="ga4c6e247b7f1deb8ae05b661d0490907f"></a>

### `LSM6DSVXXX_MLC_FEATURE`

```c
#define LSM6DSVXXX_MLC_FEATURE 0x1C
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

机器学习核心特征（Machine-learning Core Feature）。

<a id="ga3b8cdba38288aa6da8e2636e9bfd011f"></a>

### `LSM6DSVXXX_MLC_FILTER`

```c
#define LSM6DSVXXX_MLC_FILTER 0x1B
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

机器学习核心滤波器（Machine-learning Core Filter）。

<a id="ga82ca6346bc78a1ba4d928a3605a2447c"></a>

### `LSM6DSVXXX_MLC_RESULT_TAG`

```c
#define LSM6DSVXXX_MLC_RESULT_TAG 0x1A
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

机器学习核心结果（Machine-learning Core Result）。

<a id="ga9eec9a8f38708f0fef6c23ccd98a49d9"></a>

### `LSM6DSVXXX_OUTX_L_A`

```c
#define LSM6DSVXXX_OUTX_L_A 0x28U
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

`OUTX_L_A` 加速度计输出（Accelerometer Output）。

<a id="ga7fb42233e1c2cbed5e6bda21393788da"></a>

### `LSM6DSVXXX_SENSORHUB_NACK_TAG`

```c
#define LSM6DSVXXX_SENSORHUB_NACK_TAG 0x19
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

传感器集线器否定应答（Sensor-hub NACK）。

<a id="ga087907d682457fe1b4fec7a19f781910"></a>

### `LSM6DSVXXX_SENSORHUB_TARGET0_TAG`

```c
#define LSM6DSVXXX_SENSORHUB_TARGET0_TAG 0xE
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

传感器集线器目标（Sensor-hub Target）0。

<a id="gaf27c820db6fe6b17ab480ef85cf393b7"></a>

### `LSM6DSVXXX_SENSORHUB_TARGET1_TAG`

```c
#define LSM6DSVXXX_SENSORHUB_TARGET1_TAG 0xF
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

传感器集线器目标（Sensor-hub Target）1。

<a id="ga4bf7e0ad77c3d15db6903fa1dff8fa87"></a>

### `LSM6DSVXXX_SENSORHUB_TARGET2_TAG`

```c
#define LSM6DSVXXX_SENSORHUB_TARGET2_TAG 0x10
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

传感器集线器目标（Sensor-hub Target）2。

<a id="gafeb7c36af782d046f24b74292f4ace83"></a>

### `LSM6DSVXXX_SENSORHUB_TARGET3_TAG`

```c
#define LSM6DSVXXX_SENSORHUB_TARGET3_TAG 0x11
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

传感器集线器目标（Sensor-hub Target）3。

<a id="ga6fe39933ed4405ddc6e234f533215327"></a>

### `LSM6DSVXXX_SFLP_GAME_ROTATION_VECTOR_TAG`

```c
#define LSM6DSVXXX_SFLP_GAME_ROTATION_VECTOR_TAG 0x13
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

SFLP 游戏旋转向量（Game-rotation Vector）。

<a id="ga5e919c257bd092142cf1830266d98031"></a>

### `LSM6DSVXXX_SFLP_GRAVITY_VECTOR_TAG`

```c
#define LSM6DSVXXX_SFLP_GRAVITY_VECTOR_TAG 0x17
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

SFLP 重力向量（Gravity Vector）。

<a id="ga213228f246738c27b2f59b6bfd7d8f02"></a>

### `LSM6DSVXXX_SFLP_GYROSCOPE_BIAS_TAG`

```c
#define LSM6DSVXXX_SFLP_GYROSCOPE_BIAS_TAG 0x16
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

SFLP 陀螺仪偏置（Gyroscope Bias）。

<a id="ga0e8060623183b30ed20b434bee4c3418"></a>

### `LSM6DSVXXX_STATUS_REG`

```c
#define LSM6DSVXXX_STATUS_REG 0x1EU
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

`STATUS_REG` 寄存器（Register）。

<a id="gae256607af0954b035571be6c0a6348e1"></a>

### `LSM6DSVXXX_STEP_COUNTER_TAG`

```c
#define LSM6DSVXXX_STEP_COUNTER_TAG 0x12
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

步数计数器（Step Counter）。

<a id="ga49900f3a225fad10e3eff3c251de3ef9"></a>

### `LSM6DSVXXX_TEMPERATURE_TAG`

```c
#define LSM6DSVXXX_TEMPERATURE_TAG 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

温度（Temperature）。

<a id="gae8e6953df547162248da27a53a6d8ddf"></a>

### `LSM6DSVXXX_TIMESTAMP_TAG`

```c
#define LSM6DSVXXX_TIMESTAMP_TAG 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

时间戳（Timestamp）。

<a id="gad74ab246e526843a3a9c0b51aff23bf3"></a>

### `LSM6DSVXXX_XL_2XC_TAG`

```c
#define LSM6DSVXXX_XL_2XC_TAG 0x8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

加速度计（Accelerometer），2 倍压缩（2x Compressed）。

<a id="gad17ba982da4ff778dd789adc597267d8"></a>

### `LSM6DSVXXX_XL_3XC_TAG`

```c
#define LSM6DSVXXX_XL_3XC_TAG 0x9
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

加速度计（Accelerometer），3 倍压缩（3x Compressed）。

<a id="ga44578392f8501ba6ac317746b9083bd8"></a>

### `LSM6DSVXXX_XL_HG_TAG`

```c
#define LSM6DSVXXX_XL_HG_TAG 0x1D
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

高 g 加速度计（High-g Accelerometer）。

<a id="gab375a7fe25056957f5dc100b24185d37"></a>

### `LSM6DSVXXX_XL_NC_T_1_TAG`

```c
#define LSM6DSVXXX_XL_NC_T_1_TAG 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

加速度计（Accelerometer），T-1 样本（Sample）。

<a id="gabbd301aa0313208a3df654b587e41b09"></a>

### `LSM6DSVXXX_XL_NC_T_2_TAG`

```c
#define LSM6DSVXXX_XL_NC_T_2_TAG 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

加速度计（Accelerometer），T-2 样本（Sample）。

<a id="ga320efe292f3c5121031d0d8f5436a5e7"></a>

### `LSM6DSVXXX_XL_NC_TAG`

```c
#define LSM6DSVXXX_XL_NC_TAG 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsvxxx.h>
```

加速度计（Accelerometer），不压缩。

<a id="ga0e2d73310764e4ad782f20f9e2b2da46"></a>

### `lsm6dsvxxx_self_test_result`

```c
enum lsm6dsvxxx_self_test_result
```

```c
#include <zephyr/drivers/sensor/lsm6dsvxxx.h>
```

LSM6DSVXXX 的自检结果（Self-Test Result）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LSM6DSVXXX_ST_OK` | 自检通过（Self-Test Passed）。 |
| `LSM6DSVXXX_ST_FAIL` | 自检失败（Self-Test Failed）。 |

<a id="gaa40abf78652db54d4b43b41c7750b558"></a>

### `sensor_attribute_lsm6dsvxxx`

```c
enum sensor_attribute_lsm6dsvxxx
```

```c
#include <zephyr/drivers/sensor/lsm6dsvxxx.h>
```

LSM6DSVXXX 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_GET_SELF_TEST_RESULT` | 获取自检模式结果（Self-Test Mode Result）。结果存储在 `sensor_value.val1` 字段中；可能的取值参见 `lsm6dsvxxx_self_test_result`。 |


## 5.14\_原页交叉引用（Cross References）

- [lsm6dsvxxx.h](../api_file_configuration_reference/P019_zephyr__drivers__sensor__lsm6dsvxxx.h_文件参考.md)
- [lsm6dsvxxx.h](../api_file_network_pcie_reference/P002_zephyr__dt-bindings__sensor__lsm6dsvxxx.h_文件参考.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0e2d73310764e4ad782f20f9e2b2da46a01c6e9bb517b46bd18e2d69b1eb02349"></a>
<a id="gga0e2d73310764e4ad782f20f9e2b2da46a18d5155644c60de23dde8bf2ca3f5a36"></a>
<a id="ggaa40abf78652db54d4b43b41c7750b558a3b1d8afe96e306670568008d1f8b5a5d"></a>

---

[上一章](P004_HTTP响应状态码（Response Status Codes）。.md) · [返回大纲](大纲.md) · [下一章](P006_PCIe能力（Capabilities）。.md)
