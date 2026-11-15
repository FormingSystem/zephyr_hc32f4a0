---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-14
title: LIS2DUX12 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dux12__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_LIS2DUX12 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dux12__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LIS2DUX12 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

STMicroelectronics LIS2DUX12 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_lis2dux12_2Eh"></a>

```c
file lis2dux12.h
```

相关声明：[lis2dux12.h](https://docs.zephyrproject.org/latest/doxygen/html/lis2dux12_8h.html)。

the ST LIS2DUX12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 14.2\_工作模式（Operating mode）

设备树属性（Devicetree Property）`power-mode` 的取值。

<a id="r_ga2319e5357a3b3933e46e0e445d8bb868"></a>

```c
#define LIS2DUX12_OPER_MODE_POWER_DOWN 0
```

相关声明：[LIS2DUX12_OPER_MODE_POWER_DOWN](#ga2319e5357a3b3933e46e0e445d8bb868)。

掉电（Power-down）。

<a id="r_ga03d276c97b5ee65f80ce301f78d8d620"></a>

```c
#define LIS2DUX12_OPER_MODE_LOW_POWER 1
```

相关声明：[LIS2DUX12_OPER_MODE_LOW_POWER](#ga03d276c97b5ee65f80ce301f78d8d620)。

低功耗模式（Low-power Mode）。

<a id="r_gae08239e9d97ce581865d441faf13861b"></a>

```c
#define LIS2DUX12_OPER_MODE_HIGH_PERFORMANCE 2
```

相关声明：[LIS2DUX12_OPER_MODE_HIGH_PERFORMANCE](#gae08239e9d97ce581865d441faf13861b)。

高性能模式（High-performance Mode）。

<a id="r_ga1a6e9387e8b30d1c6ffcf0f02ca61000"></a>

```c
#define LIS2DUX12_OPER_MODE_SINGLE_SHOT 3
```

相关声明：[LIS2DUX12_OPER_MODE_SINGLE_SHOT](#ga1a6e9387e8b30d1c6ffcf0f02ca61000)。

单次模式（Single-shot Mode）。

## 14.3\_输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

ULP：超低功耗模式（Ultra-low-power）；LP：低功耗模式（Low-power）；HP：高性能模式（High-performance）。

<a id="r_ga94ab30f7ef8aec193a84188ccf63a21d"></a>

```c
#define LIS2DUX12_DT_ODR_OFF 0
```

相关声明：[LIS2DUX12_DT_ODR_OFF](#ga94ab30f7ef8aec193a84188ccf63a21d)。

掉电（Power-down）。

<a id="r_gae8f5f4224653c75ba0343d13d0588910"></a>

```c
#define LIS2DUX12_DT_ODR_1Hz_ULP 1
```

相关声明：[LIS2DUX12_DT_ODR_1Hz_ULP](#gae8f5f4224653c75ba0343d13d0588910)。

1 Hz，仅适用于超低功耗模式（ULP Mode）。

<a id="r_ga4a85ef36d5836a6c216a36272c645cfb"></a>

```c
#define LIS2DUX12_DT_ODR_3Hz_ULP 2
```

相关声明：[LIS2DUX12_DT_ODR_3Hz_ULP](#ga4a85ef36d5836a6c216a36272c645cfb)。

3 Hz，仅适用于超低功耗模式（ULP Mode）。

<a id="r_gaf649bb985c44d6631e6fd1a0a91fbf85"></a>

```c
#define LIS2DUX12_DT_ODR_25Hz_ULP 3
```

相关声明：[LIS2DUX12_DT_ODR_25Hz_ULP](#gaf649bb985c44d6631e6fd1a0a91fbf85)。

25 Hz，仅适用于超低功耗模式（ULP Mode）。

<a id="r_ga7c83ff001a3ff25aaab5cbac32a56df0"></a>

```c
#define LIS2DUX12_DT_ODR_6Hz 4
```

相关声明：[LIS2DUX12_DT_ODR_6Hz](#ga7c83ff001a3ff25aaab5cbac32a56df0)。

6 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="r_ga01ab37065a2bb53366adc7740af37d62"></a>

```c
#define LIS2DUX12_DT_ODR_12Hz5 5
```

相关声明：[LIS2DUX12_DT_ODR_12Hz5](#ga01ab37065a2bb53366adc7740af37d62)。

12.5 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="r_ga1daa6448cea439025041b74f5dc3e58f"></a>

```c
#define LIS2DUX12_DT_ODR_25Hz 6
```

相关声明：[LIS2DUX12_DT_ODR_25Hz](#ga1daa6448cea439025041b74f5dc3e58f)。

25 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="r_gaea1f056b715ed59a38ddb4c8aac48804"></a>

```c
#define LIS2DUX12_DT_ODR_50Hz 7
```

相关声明：[LIS2DUX12_DT_ODR_50Hz](#gaea1f056b715ed59a38ddb4c8aac48804)。

50 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="r_ga3b40a334bea0de6546b783ab65e9f4dd"></a>

```c
#define LIS2DUX12_DT_ODR_100Hz 8
```

相关声明：[LIS2DUX12_DT_ODR_100Hz](#ga3b40a334bea0de6546b783ab65e9f4dd)。

100 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="r_ga230b18cdf50c202d1bced583914332e1"></a>

```c
#define LIS2DUX12_DT_ODR_200Hz 9
```

相关声明：[LIS2DUX12_DT_ODR_200Hz](#ga230b18cdf50c202d1bced583914332e1)。

200 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="r_gae3dc67b51572e8f0c5d5ec3394d5d750"></a>

```c
#define LIS2DUX12_DT_ODR_400Hz 10
```

相关声明：[LIS2DUX12_DT_ODR_400Hz](#gae3dc67b51572e8f0c5d5ec3394d5d750)。

400 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="r_ga6a8105006b18fe6632fbce06c77bed52"></a>

```c
#define LIS2DUX12_DT_ODR_800Hz 11
```

相关声明：[LIS2DUX12_DT_ODR_800Hz](#ga6a8105006b18fe6632fbce06c77bed52)。

800 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="r_ga68214dc2825057ef3fa3e87a7ae1fcc1"></a>

```c
#define LIS2DUX12_DT_ODR_END 12
```

相关声明：[LIS2DUX12_DT_ODR_END](#ga68214dc2825057ef3fa3e87a7ae1fcc1)。

哨兵值（Sentinel），位于最后一个输出数据率（ODR）值之后。

## 14.4\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `range` 属性的取值。

<a id="r_ga9793fcda818ea10e61e844a3b94cda62"></a>

```c
#define LIS2DUX12_DT_FS_2G 0
```

相关声明：[LIS2DUX12_DT_FS_2G](#ga9793fcda818ea10e61e844a3b94cda62)。

量程（Range）：±2 g；灵敏度（Sensitivity）：0.061 mg/LSB。

<a id="r_gab50eb77d0d2bac9eb493ec0490f2b4f7"></a>

```c
#define LIS2DUX12_DT_FS_4G 1
```

相关声明：[LIS2DUX12_DT_FS_4G](#gab50eb77d0d2bac9eb493ec0490f2b4f7)。

量程（Range）：±4 g；灵敏度（Sensitivity）：0.122 mg/LSB。

<a id="r_gad0119b9353cec4ff57ad4e6fe1c7c055"></a>

```c
#define LIS2DUX12_DT_FS_8G 2
```

相关声明：[LIS2DUX12_DT_FS_8G](#gad0119b9353cec4ff57ad4e6fe1c7c055)。

量程（Range）：±8 g；灵敏度（Sensitivity）：0.244 mg/LSB。

<a id="r_ga6e29f5351f4eebe482648629024af77e"></a>

```c
#define LIS2DUX12_DT_FS_16G 3
```

相关声明：[LIS2DUX12_DT_FS_16G](#ga6e29f5351f4eebe482648629024af77e)。

量程（Range）：±16 g；灵敏度（Sensitivity）：0.488 mg/LSB。

## 14.5\_加速度计 FIFO 批量采集数据率（Accelerometer FIFO Batching Data Rate）

设备树 accel-fifo-batch-rate 属性（Property）的值。

<a id="r_ga3d4281053ce07bf0e2871180affd246a"></a>

```c
#define LIS2DUX12_DT_BDR_XL_ODR 0x0
```

相关声明：[LIS2DUX12_DT_BDR_XL_ODR](#ga3d4281053ce07bf0e2871180affd246a)。

按输出数据率（ODR）批量采集。

<a id="r_ga658039a66e163c5950d80eebd1b67f4a"></a>

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_2 0x1
```

相关声明：[LIS2DUX12_DT_BDR_XL_ODR_DIV_2](#ga658039a66e163c5950d80eebd1b67f4a)。

按 ODR / 2 批量采集（Batched）。

<a id="r_ga0b27bbf1af06f586a9f901d8603629b7"></a>

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_4 0x2
```

相关声明：[LIS2DUX12_DT_BDR_XL_ODR_DIV_4](#ga0b27bbf1af06f586a9f901d8603629b7)。

按 ODR / 4 批量采集（Batched）。

<a id="r_gadf324739868e1fe7bc4b1128699e2223"></a>

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_8 0x3
```

相关声明：[LIS2DUX12_DT_BDR_XL_ODR_DIV_8](#gadf324739868e1fe7bc4b1128699e2223)。

按 ODR / 8 批量采集（Batched）。

<a id="r_ga9560e4c28c1d4b50f273aab0c3274274"></a>

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_16 0x4
```

相关声明：[LIS2DUX12_DT_BDR_XL_ODR_DIV_16](#ga9560e4c28c1d4b50f273aab0c3274274)。

按 ODR / 16 批量采集（Batched）。

<a id="r_ga03ef61baf524a38730341b3344cdc046"></a>

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_32 0x5
```

相关声明：[LIS2DUX12_DT_BDR_XL_ODR_DIV_32](#ga03ef61baf524a38730341b3344cdc046)。

按 ODR / 32 批量采集（Batched）。

<a id="r_ga73e547d7a3fd0436ee3c308d6f7c20f2"></a>

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_64 0x6
```

相关声明：[LIS2DUX12_DT_BDR_XL_ODR_DIV_64](#ga73e547d7a3fd0436ee3c308d6f7c20f2)。

按 ODR / 64 批量采集（Batched）。

<a id="r_gafbbb48285a89128d313eeea2b7a1bbb1"></a>

```c
#define LIS2DUX12_DT_BDR_XL_ODR_OFF 0x7
```

相关声明：[LIS2DUX12_DT_BDR_XL_ODR_OFF](#gafbbb48285a89128d313eeea2b7a1bbb1)。

不批量入队（Not Batched）。

## 14.6\_加速度计 FIFO 时间戳抽取（Accelerometer FIFO Timestamp Decimation）

设备树 timestamp-fifo-batch-rate 属性（Property）的值。

<a id="r_ga058e573325b65dde80dd3813984ac38a"></a>

```c
#define LIS2DUX12_DT_DEC_TS_OFF 0x0
```

相关声明：[LIS2DUX12_DT_DEC_TS_OFF](#ga058e573325b65dde80dd3813984ac38a)。

时间戳不批量入队（Timestamp Not Batched）。

<a id="r_ga7520bcd1eae2b91bf068cdc1f6ae4487"></a>

```c
#define LIS2DUX12_DT_DEC_TS_1 0x1
```

相关声明：[LIS2DUX12_DT_DEC_TS_1](#ga7520bcd1eae2b91bf068cdc1f6ae4487)。

1 倍抽取（Decimation）。

<a id="r_ga209de2a2bd10240767aa01c9d2f4d73d"></a>

```c
#define LIS2DUX12_DT_DEC_TS_8 0x2
```

相关声明：[LIS2DUX12_DT_DEC_TS_8](#ga209de2a2bd10240767aa01c9d2f4d73d)。

8 倍抽取（Decimation）。

<a id="r_ga12c2234e04c51383868576fb82f8cecc"></a>

```c
#define LIS2DUX12_DT_DEC_TS_32 0x3
```

相关声明：[LIS2DUX12_DT_DEC_TS_32](#ga12c2234e04c51383868576fb82f8cecc)。

32 倍抽取（Decimation）。

## 14.7\_FIFO 记录标签（FIFO Record Tags）

FIFO 数据流中报告的记录标签值（Record Tag Values）。

<a id="r_gab0f9df25d43e17fc210c63581a3abc0f"></a>

```c
#define LIS2DUXXX_FIFO_EMPTY 0x0
```

相关声明：[LIS2DUXXX_FIFO_EMPTY](#gab0f9df25d43e17fc210c63581a3abc0f)。

先进先出缓冲区（FIFO）为空。

<a id="r_ga26fc2cb8dbefd4995f47b0dd4b7d0652"></a>

```c
#define LIS2DUXXX_XL_TEMP_TAG 0x2
```

相关声明：[LIS2DUXXX_XL_TEMP_TAG](#ga26fc2cb8dbefd4995f47b0dd4b7d0652)。

加速度计和温度（Accelerometer and Temperature）。

<a id="r_ga6540e92e3d71a254fbb5c6d13e0e707c"></a>

```c
#define LIS2DUXXX_XL_ONLY_2X_TAG 0x3
```

相关声明：[LIS2DUXXX_XL_ONLY_2X_TAG](#ga6540e92e3d71a254fbb5c6d13e0e707c)。

仅加速度计（Accelerometer Only），采用 2 倍压缩。

<a id="r_ga4eb99cf7057a0688bc7289c3fbb05020"></a>

```c
#define LIS2DUXXX_TIMESTAMP_TAG 0x4
```

相关声明：[LIS2DUXXX_TIMESTAMP_TAG](#ga4eb99cf7057a0688bc7289c3fbb05020)。

时间戳（Timestamp）。

<a id="r_gad2648a4dd63e75dc6ec07fc7f5307ed8"></a>

```c
#define LIS2DUXXX_STEP_COUNTER_TAG 0x12
```

相关声明：[LIS2DUXXX_STEP_COUNTER_TAG](#gad2648a4dd63e75dc6ec07fc7f5307ed8)。

步数计数器（Step Counter）。

<a id="r_gab6e05aec8aec334546ef581b88f85741"></a>

```c
#define LIS2DUXXX_MLC_RESULT_TAG 0x1A
```

相关声明：[LIS2DUXXX_MLC_RESULT_TAG](#gab6e05aec8aec334546ef581b88f85741)。

机器学习核心结果（Machine-learning Core Result）。

<a id="r_ga9063c5ef1b246d7e859945aaa2832dd3"></a>

```c
#define LIS2DUXXX_MLC_FILTER_TAG 0x1B
```

相关声明：[LIS2DUXXX_MLC_FILTER_TAG](#ga9063c5ef1b246d7e859945aaa2832dd3)。

机器学习核心滤波器（Machine-learning Core Filter）。

<a id="r_ga9ca64efe26ab1956ccffd4a921c0352c"></a>

```c
#define LIS2DUXXX_MLC_FEATURE 0x1C
```

相关声明：[LIS2DUXXX_MLC_FEATURE](#ga9ca64efe26ab1956ccffd4a921c0352c)。

机器学习核心特征（Machine-learning Core Feature）。

<a id="r_gaa0b27f7c2bca8115c3026482aeaea324"></a>

```c
#define LIS2DUXXX_FSM_RESULT_TAG 0x1D
```

相关声明：[LIS2DUXXX_FSM_RESULT_TAG](#gaa0b27f7c2bca8115c3026482aeaea324)。

有限状态机结果（Finite-state-machine Result）。

## 14.8\_FIFO 模式（FIFO Modes）

驱动使用的 FIFO 工作模式（Operating Modes）。

<a id="r_gacc96a742af72f029a4b05ef67f99bb6d"></a>

```c
#define LIS2DUXXX_DT_BYPASS_MODE 0x0
```

相关声明：[LIS2DUXXX_DT_BYPASS_MODE](#gacc96a742af72f029a4b05ef67f99bb6d)。

旁路（Bypass），禁用 FIFO。

<a id="r_ga64c29d5624aac1eb64d5d38f3aa77f2b"></a>

```c
#define LIS2DUXXX_DT_FIFO_MODE 0x1
```

相关声明：[LIS2DUXXX_DT_FIFO_MODE](#ga64c29d5624aac1eb64d5d38f3aa77f2b)。

FIFO 模式（FIFO Mode）。

<a id="r_gad0846e36da27873da048c8c44689f59e"></a>

```c
#define LIS2DUXXX_DT_STREAM_TO_FIFO_MODE 0x3
```

相关声明：[LIS2DUXXX_DT_STREAM_TO_FIFO_MODE](#gad0846e36da27873da048c8c44689f59e)。

流转 FIFO 模式（Stream-to-FIFO Mode）。

<a id="r_ga2d1b9368d9bfcc55b93334fb13208b21"></a>

```c
#define LIS2DUXXX_DT_BYPASS_TO_STREAM_MODE 0x4
```

相关声明：[LIS2DUXXX_DT_BYPASS_TO_STREAM_MODE](#ga2d1b9368d9bfcc55b93334fb13208b21)。

旁路转流模式（Bypass-to-stream Mode）。

<a id="r_ga62f6c22b8c4bdeb587a5262a727e4368"></a>

```c
#define LIS2DUXXX_DT_STREAM_MODE 0x6
```

相关声明：[LIS2DUXXX_DT_STREAM_MODE](#ga62f6c22b8c4bdeb587a5262a727e4368)。

连续流模式（Continuous Stream Mode）。

<a id="r_ga2ad4e4ad6c41d804db6a502f7863726a"></a>

```c
#define LIS2DUXXX_DT_BYPASS_TO_FIFO_MODE 0x7
```

相关声明：[LIS2DUXXX_DT_BYPASS_TO_FIFO_MODE](#ga2ad4e4ad6c41d804db6a502f7863726a)。

旁路转 FIFO 模式（Bypass-to-FIFO Mode）。

<a id="r_ga952127a0b7199066e7f3f0fa58fa2f95"></a>

```c
#define LIS2DUXXX_DT_FIFO_OFF 0x8
```

相关声明：[LIS2DUXXX_DT_FIFO_OFF](#ga952127a0b7199066e7f3f0fa58fa2f95)。

关闭 FIFO（FIFO Off）。

## 14.9\_寄存器地址（Register Addresses）

驱动使用的寄存器地址（Register Addresses）。

<a id="r_gaffa56c1d9471f5afbada2c14261f36a3"></a>

```c
#define LIS2DUXXX_DT_FIFO_CTRL 0x15U
```

相关声明：[LIS2DUXXX_DT_FIFO_CTRL](#gaffa56c1d9471f5afbada2c14261f36a3)。

FIFO_CTRL 寄存器（Register）。

<a id="r_gac4d1357af5ab51679f04a03a5396f76e"></a>

```c
#define LIS2DUXXX_DT_STATUS 0x25U
```

相关声明：[LIS2DUXXX_DT_STATUS](#gac4d1357af5ab51679f04a03a5396f76e)。

STATUS 寄存器（Register）。

<a id="r_gaeb7afe0eb54defa45b66a5726d51dec7"></a>

```c
#define LIS2DUXXX_DT_FIFO_STATUS1 0x26U
```

相关声明：[LIS2DUXXX_DT_FIFO_STATUS1](#gaeb7afe0eb54defa45b66a5726d51dec7)。

FIFO_STATUS1 寄存器（Register）。

<a id="r_ga7fd3f10740da5a54fdf18f37c9282f29"></a>

```c
#define LIS2DUXXX_DT_OUTX_L 0x28U
```

相关声明：[LIS2DUXXX_DT_OUTX_L](#ga7fd3f10740da5a54fdf18f37c9282f29)。

OUTX_L 输出寄存器（Output Register）。

<a id="r_gad773a65749a20dd28e4e7b37cf8db62d"></a>

```c
#define LIS2DUXXX_DT_FIFO_DATA_OUT_TAG 0x40U
```

相关声明：[LIS2DUXXX_DT_FIFO_DATA_OUT_TAG](#gad773a65749a20dd28e4e7b37cf8db62d)。

FIFO_DATA_OUT_TAG 寄存器（Register）。

## 14.10\_详细说明（Detailed Documentation）

<a id="ga3d4281053ce07bf0e2871180affd246a"></a>

### `LIS2DUX12_DT_BDR_XL_ODR`

```c
#define LIS2DUX12_DT_BDR_XL_ODR 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

按输出数据率（ODR）批量采集。

<a id="ga9560e4c28c1d4b50f273aab0c3274274"></a>

### `LIS2DUX12_DT_BDR_XL_ODR_DIV_16`

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_16 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

按 ODR / 16 批量采集（Batched）。

<a id="ga658039a66e163c5950d80eebd1b67f4a"></a>

### `LIS2DUX12_DT_BDR_XL_ODR_DIV_2`

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_2 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

按 ODR / 2 批量采集（Batched）。

<a id="ga03ef61baf524a38730341b3344cdc046"></a>

### `LIS2DUX12_DT_BDR_XL_ODR_DIV_32`

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_32 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

按 ODR / 32 批量采集（Batched）。

<a id="ga0b27bbf1af06f586a9f901d8603629b7"></a>

### `LIS2DUX12_DT_BDR_XL_ODR_DIV_4`

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_4 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

按 ODR / 4 批量采集（Batched）。

<a id="ga73e547d7a3fd0436ee3c308d6f7c20f2"></a>

### `LIS2DUX12_DT_BDR_XL_ODR_DIV_64`

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_64 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

按 ODR / 64 批量采集（Batched）。

<a id="gadf324739868e1fe7bc4b1128699e2223"></a>

### `LIS2DUX12_DT_BDR_XL_ODR_DIV_8`

```c
#define LIS2DUX12_DT_BDR_XL_ODR_DIV_8 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

按 ODR / 8 批量采集（Batched）。

<a id="gafbbb48285a89128d313eeea2b7a1bbb1"></a>

### `LIS2DUX12_DT_BDR_XL_ODR_OFF`

```c
#define LIS2DUX12_DT_BDR_XL_ODR_OFF 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

不批量入队（Not Batched）。

<a id="ga7520bcd1eae2b91bf068cdc1f6ae4487"></a>

### `LIS2DUX12_DT_DEC_TS_1`

```c
#define LIS2DUX12_DT_DEC_TS_1 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

1 倍抽取（Decimation）。

<a id="ga12c2234e04c51383868576fb82f8cecc"></a>

### `LIS2DUX12_DT_DEC_TS_32`

```c
#define LIS2DUX12_DT_DEC_TS_32 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

32 倍抽取（Decimation）。

<a id="ga209de2a2bd10240767aa01c9d2f4d73d"></a>

### `LIS2DUX12_DT_DEC_TS_8`

```c
#define LIS2DUX12_DT_DEC_TS_8 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

8 倍抽取（Decimation）。

<a id="ga058e573325b65dde80dd3813984ac38a"></a>

### `LIS2DUX12_DT_DEC_TS_OFF`

```c
#define LIS2DUX12_DT_DEC_TS_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

时间戳不批量入队（Timestamp Not Batched）。

<a id="ga6e29f5351f4eebe482648629024af77e"></a>

### `LIS2DUX12_DT_FS_16G`

```c
#define LIS2DUX12_DT_FS_16G 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

量程（Range）：±16 g；灵敏度（Sensitivity）：0.488 mg/LSB。

<a id="ga9793fcda818ea10e61e844a3b94cda62"></a>

### `LIS2DUX12_DT_FS_2G`

```c
#define LIS2DUX12_DT_FS_2G 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

量程（Range）：±2 g；灵敏度（Sensitivity）：0.061 mg/LSB。

<a id="gab50eb77d0d2bac9eb493ec0490f2b4f7"></a>

### `LIS2DUX12_DT_FS_4G`

```c
#define LIS2DUX12_DT_FS_4G 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

量程（Range）：±4 g；灵敏度（Sensitivity）：0.122 mg/LSB。

<a id="gad0119b9353cec4ff57ad4e6fe1c7c055"></a>

### `LIS2DUX12_DT_FS_8G`

```c
#define LIS2DUX12_DT_FS_8G 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

量程（Range）：±8 g；灵敏度（Sensitivity）：0.244 mg/LSB。

<a id="ga3b40a334bea0de6546b783ab65e9f4dd"></a>

### `LIS2DUX12_DT_ODR_100Hz`

```c
#define LIS2DUX12_DT_ODR_100Hz 8
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

100 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="ga01ab37065a2bb53366adc7740af37d62"></a>

### `LIS2DUX12_DT_ODR_12Hz5`

```c
#define LIS2DUX12_DT_ODR_12Hz5 5
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

12.5 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="gae8f5f4224653c75ba0343d13d0588910"></a>

### `LIS2DUX12_DT_ODR_1Hz_ULP`

```c
#define LIS2DUX12_DT_ODR_1Hz_ULP 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

1 Hz，仅适用于超低功耗模式（ULP Mode）。

<a id="ga230b18cdf50c202d1bced583914332e1"></a>

### `LIS2DUX12_DT_ODR_200Hz`

```c
#define LIS2DUX12_DT_ODR_200Hz 9
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

200 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="ga1daa6448cea439025041b74f5dc3e58f"></a>

### `LIS2DUX12_DT_ODR_25Hz`

```c
#define LIS2DUX12_DT_ODR_25Hz 6
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

25 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="gaf649bb985c44d6631e6fd1a0a91fbf85"></a>

### `LIS2DUX12_DT_ODR_25Hz_ULP`

```c
#define LIS2DUX12_DT_ODR_25Hz_ULP 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

25 Hz，仅适用于超低功耗模式（ULP Mode）。

<a id="ga4a85ef36d5836a6c216a36272c645cfb"></a>

### `LIS2DUX12_DT_ODR_3Hz_ULP`

```c
#define LIS2DUX12_DT_ODR_3Hz_ULP 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

3 Hz，仅适用于超低功耗模式（ULP Mode）。

<a id="gae3dc67b51572e8f0c5d5ec3394d5d750"></a>

### `LIS2DUX12_DT_ODR_400Hz`

```c
#define LIS2DUX12_DT_ODR_400Hz 10
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

400 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="gaea1f056b715ed59a38ddb4c8aac48804"></a>

### `LIS2DUX12_DT_ODR_50Hz`

```c
#define LIS2DUX12_DT_ODR_50Hz 7
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

50 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="ga7c83ff001a3ff25aaab5cbac32a56df0"></a>

### `LIS2DUX12_DT_ODR_6Hz`

```c
#define LIS2DUX12_DT_ODR_6Hz 4
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

6 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="ga6a8105006b18fe6632fbce06c77bed52"></a>

### `LIS2DUX12_DT_ODR_800Hz`

```c
#define LIS2DUX12_DT_ODR_800Hz 11
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

800 Hz，适用于低功耗（LP）或高性能（HP）模式。

<a id="ga68214dc2825057ef3fa3e87a7ae1fcc1"></a>

### `LIS2DUX12_DT_ODR_END`

```c
#define LIS2DUX12_DT_ODR_END 12
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

哨兵值（Sentinel），位于最后一个输出数据率（ODR）值之后。

<a id="ga94ab30f7ef8aec193a84188ccf63a21d"></a>

### `LIS2DUX12_DT_ODR_OFF`

```c
#define LIS2DUX12_DT_ODR_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

掉电（Power-down）。

<a id="gae08239e9d97ce581865d441faf13861b"></a>

### `LIS2DUX12_OPER_MODE_HIGH_PERFORMANCE`

```c
#define LIS2DUX12_OPER_MODE_HIGH_PERFORMANCE 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

高性能模式（High-performance Mode）。

<a id="ga03d276c97b5ee65f80ce301f78d8d620"></a>

### `LIS2DUX12_OPER_MODE_LOW_POWER`

```c
#define LIS2DUX12_OPER_MODE_LOW_POWER 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

低功耗模式（Low-power Mode）。

<a id="ga2319e5357a3b3933e46e0e445d8bb868"></a>

### `LIS2DUX12_OPER_MODE_POWER_DOWN`

```c
#define LIS2DUX12_OPER_MODE_POWER_DOWN 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

掉电（Power-down）。

<a id="ga1a6e9387e8b30d1c6ffcf0f02ca61000"></a>

### `LIS2DUX12_OPER_MODE_SINGLE_SHOT`

```c
#define LIS2DUX12_OPER_MODE_SINGLE_SHOT 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

单次模式（Single-shot Mode）。

<a id="gacc96a742af72f029a4b05ef67f99bb6d"></a>

### `LIS2DUXXX_DT_BYPASS_MODE`

```c
#define LIS2DUXXX_DT_BYPASS_MODE 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

旁路（Bypass），禁用 FIFO。

<a id="ga2ad4e4ad6c41d804db6a502f7863726a"></a>

### `LIS2DUXXX_DT_BYPASS_TO_FIFO_MODE`

```c
#define LIS2DUXXX_DT_BYPASS_TO_FIFO_MODE 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

旁路转 FIFO 模式（Bypass-to-FIFO Mode）。

<a id="ga2d1b9368d9bfcc55b93334fb13208b21"></a>

### `LIS2DUXXX_DT_BYPASS_TO_STREAM_MODE`

```c
#define LIS2DUXXX_DT_BYPASS_TO_STREAM_MODE 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

旁路转流模式（Bypass-to-stream Mode）。

<a id="gaffa56c1d9471f5afbada2c14261f36a3"></a>

### `LIS2DUXXX_DT_FIFO_CTRL`

```c
#define LIS2DUXXX_DT_FIFO_CTRL 0x15U
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

FIFO_CTRL 寄存器（Register）。

<a id="gad773a65749a20dd28e4e7b37cf8db62d"></a>

### `LIS2DUXXX_DT_FIFO_DATA_OUT_TAG`

```c
#define LIS2DUXXX_DT_FIFO_DATA_OUT_TAG 0x40U
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

FIFO_DATA_OUT_TAG 寄存器（Register）。

<a id="ga64c29d5624aac1eb64d5d38f3aa77f2b"></a>

### `LIS2DUXXX_DT_FIFO_MODE`

```c
#define LIS2DUXXX_DT_FIFO_MODE 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

FIFO 模式（FIFO Mode）。

<a id="ga952127a0b7199066e7f3f0fa58fa2f95"></a>

### `LIS2DUXXX_DT_FIFO_OFF`

```c
#define LIS2DUXXX_DT_FIFO_OFF 0x8
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

关闭 FIFO（FIFO Off）。

<a id="gaeb7afe0eb54defa45b66a5726d51dec7"></a>

### `LIS2DUXXX_DT_FIFO_STATUS1`

```c
#define LIS2DUXXX_DT_FIFO_STATUS1 0x26U
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

FIFO_STATUS1 寄存器（Register）。

<a id="ga7fd3f10740da5a54fdf18f37c9282f29"></a>

### `LIS2DUXXX_DT_OUTX_L`

```c
#define LIS2DUXXX_DT_OUTX_L 0x28U
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

OUTX_L 输出寄存器（Output Register）。

<a id="gac4d1357af5ab51679f04a03a5396f76e"></a>

### `LIS2DUXXX_DT_STATUS`

```c
#define LIS2DUXXX_DT_STATUS 0x25U
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

STATUS 寄存器（Register）。

<a id="ga62f6c22b8c4bdeb587a5262a727e4368"></a>

### `LIS2DUXXX_DT_STREAM_MODE`

```c
#define LIS2DUXXX_DT_STREAM_MODE 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

连续流模式（Continuous Stream Mode）。

<a id="gad0846e36da27873da048c8c44689f59e"></a>

### `LIS2DUXXX_DT_STREAM_TO_FIFO_MODE`

```c
#define LIS2DUXXX_DT_STREAM_TO_FIFO_MODE 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

流转 FIFO 模式（Stream-to-FIFO Mode）。

<a id="gab0f9df25d43e17fc210c63581a3abc0f"></a>

### `LIS2DUXXX_FIFO_EMPTY`

```c
#define LIS2DUXXX_FIFO_EMPTY 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

先进先出缓冲区（FIFO）为空。

<a id="gaa0b27f7c2bca8115c3026482aeaea324"></a>

### `LIS2DUXXX_FSM_RESULT_TAG`

```c
#define LIS2DUXXX_FSM_RESULT_TAG 0x1D
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

有限状态机结果（Finite-state-machine Result）。

<a id="ga9ca64efe26ab1956ccffd4a921c0352c"></a>

### `LIS2DUXXX_MLC_FEATURE`

```c
#define LIS2DUXXX_MLC_FEATURE 0x1C
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

机器学习核心特征（Machine-learning Core Feature）。

<a id="ga9063c5ef1b246d7e859945aaa2832dd3"></a>

### `LIS2DUXXX_MLC_FILTER_TAG`

```c
#define LIS2DUXXX_MLC_FILTER_TAG 0x1B
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

机器学习核心滤波器（Machine-learning Core Filter）。

<a id="gab6e05aec8aec334546ef581b88f85741"></a>

### `LIS2DUXXX_MLC_RESULT_TAG`

```c
#define LIS2DUXXX_MLC_RESULT_TAG 0x1A
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

机器学习核心结果（Machine-learning Core Result）。

<a id="gad2648a4dd63e75dc6ec07fc7f5307ed8"></a>

### `LIS2DUXXX_STEP_COUNTER_TAG`

```c
#define LIS2DUXXX_STEP_COUNTER_TAG 0x12
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

步数计数器（Step Counter）。

<a id="ga4eb99cf7057a0688bc7289c3fbb05020"></a>

### `LIS2DUXXX_TIMESTAMP_TAG`

```c
#define LIS2DUXXX_TIMESTAMP_TAG 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

时间戳（Timestamp）。

<a id="ga6540e92e3d71a254fbb5c6d13e0e707c"></a>

### `LIS2DUXXX_XL_ONLY_2X_TAG`

```c
#define LIS2DUXXX_XL_ONLY_2X_TAG 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

仅加速度计（Accelerometer Only），采用 2 倍压缩。

<a id="ga26fc2cb8dbefd4995f47b0dd4b7d0652"></a>

### `LIS2DUXXX_XL_TEMP_TAG`

```c
#define LIS2DUXXX_XL_TEMP_TAG 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dux12.h>
```

加速度计和温度（Accelerometer and Temperature）。


## 14.11\_原页交叉引用（Cross References）

- [lis2dux12.h](https://docs.zephyrproject.org/latest/doxygen/html/lis2dux12_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P013_Grow R502A API主题.md) · [返回大纲](大纲.md) · [下一章](P015_MFD M5PM1 接口.md)
