---
id: learning.zephyr-docs.api-source-reference.page-207
title: lsm6dsvxxx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lsm6dsvxxx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第207章\_lsm6dsvxxx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lsm6dsvxxx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lsm6dsvxxx_8h.html)。

## 207.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00020"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>

```c
/*
 * Copyright (c) 2025 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSVXXX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSVXXX_H_


#define LSM6DSVXXX_DT_ODR_OFF                   0x0
#define LSM6DSVXXX_DT_ODR_AT_1Hz875             0x1
#define LSM6DSVXXX_DT_ODR_AT_7Hz5               0x2
#define LSM6DSVXXX_DT_ODR_AT_15Hz               0x3
#define LSM6DSVXXX_DT_ODR_AT_30Hz               0x4
#define LSM6DSVXXX_DT_ODR_AT_60Hz               0x5
#define LSM6DSVXXX_DT_ODR_AT_120Hz              0x6
#define LSM6DSVXXX_DT_ODR_AT_240Hz              0x7
#define LSM6DSVXXX_DT_ODR_AT_480Hz              0x8
#define LSM6DSVXXX_DT_ODR_AT_960Hz              0x9
#define LSM6DSVXXX_DT_ODR_AT_1920Hz             0xA
#define LSM6DSVXXX_DT_ODR_AT_3840Hz             0xB
#define LSM6DSVXXX_DT_ODR_AT_7680Hz             0xC
#define LSM6DSVXXX_DT_ODR_HA01_AT_15Hz625       0x13
#define LSM6DSVXXX_DT_ODR_HA01_AT_31Hz25        0x14
#define LSM6DSVXXX_DT_ODR_HA01_AT_62Hz5         0x15
#define LSM6DSVXXX_DT_ODR_HA01_AT_125Hz         0x16
#define LSM6DSVXXX_DT_ODR_HA01_AT_250Hz         0x17
#define LSM6DSVXXX_DT_ODR_HA01_AT_500Hz         0x18
#define LSM6DSVXXX_DT_ODR_HA01_AT_1000Hz        0x19
#define LSM6DSVXXX_DT_ODR_HA01_AT_2000Hz        0x1A
#define LSM6DSVXXX_DT_ODR_HA01_AT_4000Hz        0x1B
#define LSM6DSVXXX_DT_ODR_HA01_AT_8000Hz        0x1C
#define LSM6DSVXXX_DT_ODR_HA02_AT_12Hz5         0x23
#define LSM6DSVXXX_DT_ODR_HA02_AT_25Hz          0x24
#define LSM6DSVXXX_DT_ODR_HA02_AT_50Hz          0x25
#define LSM6DSVXXX_DT_ODR_HA02_AT_100Hz         0x26
#define LSM6DSVXXX_DT_ODR_HA02_AT_200Hz         0x27
#define LSM6DSVXXX_DT_ODR_HA02_AT_400Hz         0x28
#define LSM6DSVXXX_DT_ODR_HA02_AT_800Hz         0x29
#define LSM6DSVXXX_DT_ODR_HA02_AT_1600Hz        0x2A
#define LSM6DSVXXX_DT_ODR_HA02_AT_3200Hz        0x2B
#define LSM6DSVXXX_DT_ODR_HA02_AT_6400Hz        0x2C

#define LSM6DSVXXX_DT_XL_NOT_BATCHED            0x0
#define LSM6DSVXXX_DT_XL_BATCHED_AT_1Hz875      0x1
#define LSM6DSVXXX_DT_XL_BATCHED_AT_7Hz5        0x2
#define LSM6DSVXXX_DT_XL_BATCHED_AT_15Hz        0x3
#define LSM6DSVXXX_DT_XL_BATCHED_AT_30Hz        0x4
#define LSM6DSVXXX_DT_XL_BATCHED_AT_60Hz        0x5
#define LSM6DSVXXX_DT_XL_BATCHED_AT_120Hz       0x6
#define LSM6DSVXXX_DT_XL_BATCHED_AT_240Hz       0x7
#define LSM6DSVXXX_DT_XL_BATCHED_AT_480Hz       0x8
#define LSM6DSVXXX_DT_XL_BATCHED_AT_960Hz       0x9
#define LSM6DSVXXX_DT_XL_BATCHED_AT_1920Hz      0xa
#define LSM6DSVXXX_DT_XL_BATCHED_AT_3840Hz      0xb
#define LSM6DSVXXX_DT_XL_BATCHED_AT_7680Hz      0xc

#define LSM6DSVXXX_DT_GY_NOT_BATCHED            0x0
#define LSM6DSVXXX_DT_GY_BATCHED_AT_1Hz875      0x1
#define LSM6DSVXXX_DT_GY_BATCHED_AT_7Hz5        0x2
#define LSM6DSVXXX_DT_GY_BATCHED_AT_15Hz        0x3
#define LSM6DSVXXX_DT_GY_BATCHED_AT_30Hz        0x4
#define LSM6DSVXXX_DT_GY_BATCHED_AT_60Hz        0x5
#define LSM6DSVXXX_DT_GY_BATCHED_AT_120Hz       0x6
#define LSM6DSVXXX_DT_GY_BATCHED_AT_240Hz       0x7
#define LSM6DSVXXX_DT_GY_BATCHED_AT_480Hz       0x8
#define LSM6DSVXXX_DT_GY_BATCHED_AT_960Hz       0x9
#define LSM6DSVXXX_DT_GY_BATCHED_AT_1920Hz      0xa
#define LSM6DSVXXX_DT_GY_BATCHED_AT_3840Hz      0xb
#define LSM6DSVXXX_DT_GY_BATCHED_AT_7680Hz      0xc

#define LSM6DSVXXX_DT_TEMP_NOT_BATCHED          0x0
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_1Hz875    0x1
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_15Hz      0x2
#define LSM6DSVXXX_DT_TEMP_BATCHED_AT_60Hz      0x3

#define LSM6DSVXXX_DT_SFLP_ODR_AT_15Hz          0x0
#define LSM6DSVXXX_DT_SFLP_ODR_AT_30Hz          0x1
#define LSM6DSVXXX_DT_SFLP_ODR_AT_60Hz          0x2
#define LSM6DSVXXX_DT_SFLP_ODR_AT_120Hz         0x3
#define LSM6DSVXXX_DT_SFLP_ODR_AT_240Hz         0x4
#define LSM6DSVXXX_DT_SFLP_ODR_AT_480Hz         0x5

#define LSM6DSVXXX_DT_SFLP_FIFO_OFF                             0x0
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION                   0x1
#define LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY                         0x2
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY           0x3
#define LSM6DSVXXX_DT_SFLP_FIFO_GBIAS                           0x4
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GBIAS             0x5
#define LSM6DSVXXX_DT_SFLP_FIFO_GRAVITY_GBIAS                   0x6
#define LSM6DSVXXX_DT_SFLP_FIFO_GAME_ROTATION_GRAVITY_GBIAS     0x7

#define LSM6DSVXXX_FIFO_EMPTY                    0x0
#define LSM6DSVXXX_GY_NC_TAG                     0x1
#define LSM6DSVXXX_XL_NC_TAG                     0x2
#define LSM6DSVXXX_TEMPERATURE_TAG               0x3
#define LSM6DSVXXX_TIMESTAMP_TAG                 0x4
#define LSM6DSVXXX_CFG_CHANGE_TAG                0x5
#define LSM6DSVXXX_XL_NC_T_2_TAG                 0x6
#define LSM6DSVXXX_XL_NC_T_1_TAG                 0x7
#define LSM6DSVXXX_XL_2XC_TAG                    0x8
#define LSM6DSVXXX_XL_3XC_TAG                    0x9
#define LSM6DSVXXX_GY_NC_T_2_TAG                 0xA
#define LSM6DSVXXX_GY_NC_T_1_TAG                 0xB
#define LSM6DSVXXX_GY_2XC_TAG                    0xC
#define LSM6DSVXXX_GY_3XC_TAG                    0xD
#define LSM6DSVXXX_SENSORHUB_TARGET0_TAG         0xE
#define LSM6DSVXXX_SENSORHUB_TARGET1_TAG         0xF
#define LSM6DSVXXX_SENSORHUB_TARGET2_TAG         0x10
#define LSM6DSVXXX_SENSORHUB_TARGET3_TAG         0x11
#define LSM6DSVXXX_STEP_COUNTER_TAG              0x12
#define LSM6DSVXXX_SFLP_GAME_ROTATION_VECTOR_TAG 0x13
#define LSM6DSVXXX_SFLP_GYROSCOPE_BIAS_TAG       0x16
#define LSM6DSVXXX_SFLP_GRAVITY_VECTOR_TAG       0x17
#define LSM6DSVXXX_HG_XL_PEAK_TAG                0x18
#define LSM6DSVXXX_SENSORHUB_NACK_TAG            0x19
#define LSM6DSVXXX_MLC_RESULT_TAG                0x1A
#define LSM6DSVXXX_MLC_FILTER                    0x1B
#define LSM6DSVXXX_MLC_FEATURE                   0x1C
#define LSM6DSVXXX_XL_HG_TAG                     0x1D
#define LSM6DSVXXX_GY_ENHANCED_EIS               0x1E

#define LSM6DSVXXX_STATUS_REG                   0x1EU
#define LSM6DSVXXX_OUTX_L_A                     0x28U
#define LSM6DSVXXX_FIFO_STATUS1                 0x1BU
#define LSM6DSVXXX_FIFO_DATA_OUT_TAG            0x78U

#define LSM6DSVXXX_BYPASS_MODE                  0x00U
#define LSM6DSVXXX_FIFO_CTRL4                   0x0AU

#define LSM6DSVXXX_DT_GPIO_INT_EDGE_TO_ACTIVE   0
#define LSM6DSVXXX_DT_GPIO_INT_LEVEL_ACTIVE     1


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSVXXX_H_ */
```

## 207.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 219 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM6DSVXXX_H_`。

## 207.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2lsm6dsvxxx_8h.html)

---

[上一章](P206_lis2dh.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P208_max30009.h_源码浏览.md)
