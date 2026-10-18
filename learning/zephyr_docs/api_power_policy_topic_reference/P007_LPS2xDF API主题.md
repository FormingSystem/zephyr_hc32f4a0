---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-7
title: LPS2xDF API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lps2xdf__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_LPS2xDF API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lps2xdf__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LPS2xDF 压力和温度传感器。

<a id="details"></a>

STMicroelectronics LPS2xDF 压力和温度传感器。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_lps2xdf_2Eh"></a>

```c
file lps2xdf.h
```

相关声明：[lps2xdf.h](https://docs.zephyrproject.org/latest/doxygen/html/lps2xdf_8h.html)。

the ST LPS2xDF pressure sensors的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.2\_输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_gaba5086849d797518ce64484c3f7c40c2"></a>

```c
#define LPS2xDF_DT_ODR_POWER_DOWN 0
```

相关声明：[LPS2xDF_DT_ODR_POWER_DOWN](#gaba5086849d797518ce64484c3f7c40c2)。

掉电（Power-down）。

<a id="r_ga4ace0b4fcaa9251e69c934564c116634"></a>

```c
#define LPS2xDF_DT_ODR_1HZ 1
```

相关声明：[LPS2xDF_DT_ODR_1HZ](#ga4ace0b4fcaa9251e69c934564c116634)。

频率：1 Hz。

<a id="r_ga30282e0a4f090bb3106ccb21f577de64"></a>

```c
#define LPS2xDF_DT_ODR_4HZ 2
```

相关声明：[LPS2xDF_DT_ODR_4HZ](#ga30282e0a4f090bb3106ccb21f577de64)。

频率（Frequency）：4 Hz。

<a id="r_ga9bfb85c1e7e6a5f176e6e52447112ba1"></a>

```c
#define LPS2xDF_DT_ODR_10HZ 3
```

相关声明：[LPS2xDF_DT_ODR_10HZ](#ga9bfb85c1e7e6a5f176e6e52447112ba1)。

频率：10 Hz。

<a id="r_ga7ff9cde8d5f782008fd302962e61f62e"></a>

```c
#define LPS2xDF_DT_ODR_25HZ 4
```

相关声明：[LPS2xDF_DT_ODR_25HZ](#ga7ff9cde8d5f782008fd302962e61f62e)。

频率：25 Hz。

<a id="r_ga5f767d66c25ee9d30b292f451fe898e9"></a>

```c
#define LPS2xDF_DT_ODR_50HZ 5
```

相关声明：[LPS2xDF_DT_ODR_50HZ](#ga5f767d66c25ee9d30b292f451fe898e9)。

频率：50 Hz。

<a id="r_gaead62a263aae03b5a4b0d4aa4832c921"></a>

```c
#define LPS2xDF_DT_ODR_75HZ 6
```

相关声明：[LPS2xDF_DT_ODR_75HZ](#gaead62a263aae03b5a4b0d4aa4832c921)。

频率：75 Hz。

<a id="r_ga014ee98e7252de3f16d5cc95d602a575"></a>

```c
#define LPS2xDF_DT_ODR_100HZ 7
```

相关声明：[LPS2xDF_DT_ODR_100HZ](#ga014ee98e7252de3f16d5cc95d602a575)。

频率：100 Hz。

<a id="r_ga75287fb5fe773719de936e3c35b38935"></a>

```c
#define LPS2xDF_DT_ODR_200HZ 8
```

相关声明：[LPS2xDF_DT_ODR_200HZ](#ga75287fb5fe773719de936e3c35b38935)。

频率：200 Hz。

## 7.3\_低通滤波器选项（Low-pass Filter Options）

设备树属性（Devicetree Property）`lpf` 的取值。

<a id="r_gae76b2b2a597dfc2f15dbf310a49846dd"></a>

```c
#define LPS2xDF_DT_LP_FILTER_OFF 0
```

相关声明：[LPS2xDF_DT_LP_FILTER_OFF](#gae76b2b2a597dfc2f15dbf310a49846dd)。

禁用滤波器（Filter Disabled）。

<a id="r_ga73930a4a4a834b102cacfcc262b47b05"></a>

```c
#define LPS2xDF_DT_LP_FILTER_ODR_4 1
```

相关声明：[LPS2xDF_DT_LP_FILTER_ODR_4](#ga73930a4a4a834b102cacfcc262b47b05)。

输出数据速率（ODR）除以 4。

<a id="r_ga3dbce218e79cfb34de7cacb216cf9e12"></a>

```c
#define LPS2xDF_DT_LP_FILTER_ODR_9 3
```

相关声明：[LPS2xDF_DT_LP_FILTER_ODR_9](#ga3dbce218e79cfb34de7cacb216cf9e12)。

输出数据速率（ODR）除以 9。

## 7.4\_平均采样数量选项（Averaging Number of Samples Options）

设备树属性（Devicetree Property）`avg` 的取值。

<a id="r_gaa2a9f4859187ec438fbf0caf8e97d2d1"></a>

```c
#define LPS2xDF_DT_AVG_4_SAMPLES 0
```

相关声明：[LPS2xDF_DT_AVG_4_SAMPLES](#gaa2a9f4859187ec438fbf0caf8e97d2d1)。

4 个样本（Samples）。

<a id="r_gab8401d04498cbc2db82f653fe43bd9c6"></a>

```c
#define LPS2xDF_DT_AVG_8_SAMPLES 1
```

相关声明：[LPS2xDF_DT_AVG_8_SAMPLES](#gab8401d04498cbc2db82f653fe43bd9c6)。

8 个样本（Samples）。

<a id="r_gaa78c0c206a4313eeb53607d2f1541a8d"></a>

```c
#define LPS2xDF_DT_AVG_16_SAMPLES 2
```

相关声明：[LPS2xDF_DT_AVG_16_SAMPLES](#gaa78c0c206a4313eeb53607d2f1541a8d)。

16 个样本（Samples）。

<a id="r_ga0aa8b28e50ad119bec6082bd152fa6cc"></a>

```c
#define LPS2xDF_DT_AVG_32_SAMPLES 3
```

相关声明：[LPS2xDF_DT_AVG_32_SAMPLES](#ga0aa8b28e50ad119bec6082bd152fa6cc)。

32 个样本（Samples）。

<a id="r_ga5859a72559cf5121f284eaf3c2acf50f"></a>

```c
#define LPS2xDF_DT_AVG_64_SAMPLES 4
```

相关声明：[LPS2xDF_DT_AVG_64_SAMPLES](#ga5859a72559cf5121f284eaf3c2acf50f)。

64 个样本（Samples）。

<a id="r_ga17b064199992bae3a44fbe34f068f042"></a>

```c
#define LPS2xDF_DT_AVG_128_SAMPLES 5
```

相关声明：[LPS2xDF_DT_AVG_128_SAMPLES](#ga17b064199992bae3a44fbe34f068f042)。

128 个样本（Samples）。

<a id="r_ga5695d812598ee97cf07a0f13a229c08c"></a>

```c
#define LPS2xDF_DT_AVG_256_SAMPLES 6
```

相关声明：[LPS2xDF_DT_AVG_256_SAMPLES](#ga5695d812598ee97cf07a0f13a229c08c)。

256 个样本（Samples）。

<a id="r_gac656a90e3be782d9df47c4bb893843c1"></a>

```c
#define LPS2xDF_DT_AVG_512_SAMPLES 7
```

相关声明：[LPS2xDF_DT_AVG_512_SAMPLES](#gac656a90e3be782d9df47c4bb893843c1)。

512 个样本（Samples）。

## 7.5\_满量程压力模式选项（Full-scale Pressure Mode Options）

设备树属性（Devicetree Property）`fs` 的取值。

<a id="r_ga77848469494ffd8912bdc79f65e6fe86"></a>

```c
#define LPS28DFW_DT_FS_MODE_1_1260 0
```

相关声明：[LPS28DFW_DT_FS_MODE_1_1260](#ga77848469494ffd8912bdc79f65e6fe86)。

LPS28DFW 模式（Mode）1，1260 hPa。

<a id="r_ga924ab5b02a02c3b28626a87f860c0055"></a>

```c
#define LPS28DFW_DT_FS_MODE_2_4060 1
```

相关声明：[LPS28DFW_DT_FS_MODE_2_4060](#ga924ab5b02a02c3b28626a87f860c0055)。

LPS28DFW 模式（Mode）2，4060 hPa。

<a id="r_gabcff3a9fb4a7b883b75bc59c5bd547f3"></a>

```c
#define ILPS22QS_DT_FS_MODE_1_1260 0
```

相关声明：[ILPS22QS_DT_FS_MODE_1_1260](#gabcff3a9fb4a7b883b75bc59c5bd547f3)。

ILPS22QS 模式（Mode）1，1260 hPa。

<a id="r_ga896769c2a9611c670d3e04e554c35ea0"></a>

```c
#define ILPS22QS_DT_FS_MODE_2_4060 1
```

相关声明：[ILPS22QS_DT_FS_MODE_2_4060](#ga896769c2a9611c670d3e04e554c35ea0)。

ILPS22QS 模式（Mode）2，4060 hPa。

## 7.6\_详细说明（Detailed Documentation）

<a id="gabcff3a9fb4a7b883b75bc59c5bd547f3"></a>

### `ILPS22QS_DT_FS_MODE_1_1260`

```c
#define ILPS22QS_DT_FS_MODE_1_1260 0
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

ILPS22QS 模式（Mode）1，1260 hPa。

<a id="ga896769c2a9611c670d3e04e554c35ea0"></a>

### `ILPS22QS_DT_FS_MODE_2_4060`

```c
#define ILPS22QS_DT_FS_MODE_2_4060 1
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

ILPS22QS 模式（Mode）2，4060 hPa。

<a id="ga77848469494ffd8912bdc79f65e6fe86"></a>

### `LPS28DFW_DT_FS_MODE_1_1260`

```c
#define LPS28DFW_DT_FS_MODE_1_1260 0
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

LPS28DFW 模式（Mode）1，1260 hPa。

<a id="ga924ab5b02a02c3b28626a87f860c0055"></a>

### `LPS28DFW_DT_FS_MODE_2_4060`

```c
#define LPS28DFW_DT_FS_MODE_2_4060 1
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

LPS28DFW 模式（Mode）2，4060 hPa。

<a id="ga17b064199992bae3a44fbe34f068f042"></a>

### `LPS2xDF_DT_AVG_128_SAMPLES`

```c
#define LPS2xDF_DT_AVG_128_SAMPLES 5
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

128 个样本（Samples）。

<a id="gaa78c0c206a4313eeb53607d2f1541a8d"></a>

### `LPS2xDF_DT_AVG_16_SAMPLES`

```c
#define LPS2xDF_DT_AVG_16_SAMPLES 2
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

16 个样本（Samples）。

<a id="ga5695d812598ee97cf07a0f13a229c08c"></a>

### `LPS2xDF_DT_AVG_256_SAMPLES`

```c
#define LPS2xDF_DT_AVG_256_SAMPLES 6
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

256 个样本（Samples）。

<a id="ga0aa8b28e50ad119bec6082bd152fa6cc"></a>

### `LPS2xDF_DT_AVG_32_SAMPLES`

```c
#define LPS2xDF_DT_AVG_32_SAMPLES 3
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

32 个样本（Samples）。

<a id="gaa2a9f4859187ec438fbf0caf8e97d2d1"></a>

### `LPS2xDF_DT_AVG_4_SAMPLES`

```c
#define LPS2xDF_DT_AVG_4_SAMPLES 0
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

4 个样本（Samples）。

<a id="gac656a90e3be782d9df47c4bb893843c1"></a>

### `LPS2xDF_DT_AVG_512_SAMPLES`

```c
#define LPS2xDF_DT_AVG_512_SAMPLES 7
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

512 个样本（Samples）。

<a id="ga5859a72559cf5121f284eaf3c2acf50f"></a>

### `LPS2xDF_DT_AVG_64_SAMPLES`

```c
#define LPS2xDF_DT_AVG_64_SAMPLES 4
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

64 个样本（Samples）。

<a id="gab8401d04498cbc2db82f653fe43bd9c6"></a>

### `LPS2xDF_DT_AVG_8_SAMPLES`

```c
#define LPS2xDF_DT_AVG_8_SAMPLES 1
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

8 个样本（Samples）。

<a id="ga73930a4a4a834b102cacfcc262b47b05"></a>

### `LPS2xDF_DT_LP_FILTER_ODR_4`

```c
#define LPS2xDF_DT_LP_FILTER_ODR_4 1
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

输出数据速率（ODR）除以 4。

<a id="ga3dbce218e79cfb34de7cacb216cf9e12"></a>

### `LPS2xDF_DT_LP_FILTER_ODR_9`

```c
#define LPS2xDF_DT_LP_FILTER_ODR_9 3
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

输出数据速率（ODR）除以 9。

<a id="gae76b2b2a597dfc2f15dbf310a49846dd"></a>

### `LPS2xDF_DT_LP_FILTER_OFF`

```c
#define LPS2xDF_DT_LP_FILTER_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

禁用滤波器（Filter Disabled）。

<a id="ga014ee98e7252de3f16d5cc95d602a575"></a>

### `LPS2xDF_DT_ODR_100HZ`

```c
#define LPS2xDF_DT_ODR_100HZ 7
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

频率：100 Hz。

<a id="ga9bfb85c1e7e6a5f176e6e52447112ba1"></a>

### `LPS2xDF_DT_ODR_10HZ`

```c
#define LPS2xDF_DT_ODR_10HZ 3
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

频率：10 Hz。

<a id="ga4ace0b4fcaa9251e69c934564c116634"></a>

### `LPS2xDF_DT_ODR_1HZ`

```c
#define LPS2xDF_DT_ODR_1HZ 1
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

频率：1 Hz。

<a id="ga75287fb5fe773719de936e3c35b38935"></a>

### `LPS2xDF_DT_ODR_200HZ`

```c
#define LPS2xDF_DT_ODR_200HZ 8
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

频率：200 Hz。

<a id="ga7ff9cde8d5f782008fd302962e61f62e"></a>

### `LPS2xDF_DT_ODR_25HZ`

```c
#define LPS2xDF_DT_ODR_25HZ 4
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

频率：25 Hz。

<a id="ga30282e0a4f090bb3106ccb21f577de64"></a>

### `LPS2xDF_DT_ODR_4HZ`

```c
#define LPS2xDF_DT_ODR_4HZ 2
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

频率（Frequency）：4 Hz。

<a id="ga5f767d66c25ee9d30b292f451fe898e9"></a>

### `LPS2xDF_DT_ODR_50HZ`

```c
#define LPS2xDF_DT_ODR_50HZ 5
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

频率：50 Hz。

<a id="gaead62a263aae03b5a4b0d4aa4832c921"></a>

### `LPS2xDF_DT_ODR_75HZ`

```c
#define LPS2xDF_DT_ODR_75HZ 6
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

频率：75 Hz。

<a id="gaba5086849d797518ce64484c3f7c40c2"></a>

### `LPS2xDF_DT_ODR_POWER_DOWN`

```c
#define LPS2xDF_DT_ODR_POWER_DOWN 0
```

```c
#include <zephyr/dt-bindings/sensor/lps2xdf.h>
```

掉电（Power-down）。


## 7.7\_原页交叉引用（Cross References）

- [lps2xdf.h](https://docs.zephyrproject.org/latest/doxygen/html/lps2xdf_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_IT51XXX API主题.md) · [返回大纲](大纲.md) · [下一章](P008_MFD AXP192 接口.md)
