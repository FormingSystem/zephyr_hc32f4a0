---
id: learning.zephyr-docs.api-file-storage-event-reference.page-13
title: zephyr__dt-bindings__sensor__lps2xdf.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lps2xdf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_dt-bindings\_\_sensor\_\_lps2xdf.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lps2xdf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LPS2xDF pressure sensors的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST LPS2xDF pressure sensors的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_gaba5086849d797518ce64484c3f7c40c2"></a>

```c
#define LPS2xDF_DT_ODR_POWER_DOWN 0
```

相关声明：[LPS2xDF_DT_ODR_POWER_DOWN](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gaba5086849d797518ce64484c3f7c40c2)。

掉电（Power-down）。

<a id="r_ga4ace0b4fcaa9251e69c934564c116634"></a>

```c
#define LPS2xDF_DT_ODR_1HZ 1
```

相关声明：[LPS2xDF_DT_ODR_1HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga4ace0b4fcaa9251e69c934564c116634)。

频率：1 Hz。

<a id="r_ga30282e0a4f090bb3106ccb21f577de64"></a>

```c
#define LPS2xDF_DT_ODR_4HZ 2
```

相关声明：[LPS2xDF_DT_ODR_4HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga30282e0a4f090bb3106ccb21f577de64)。

频率（Frequency）：4 Hz。

<a id="r_ga9bfb85c1e7e6a5f176e6e52447112ba1"></a>

```c
#define LPS2xDF_DT_ODR_10HZ 3
```

相关声明：[LPS2xDF_DT_ODR_10HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga9bfb85c1e7e6a5f176e6e52447112ba1)。

频率：10 Hz。

<a id="r_ga7ff9cde8d5f782008fd302962e61f62e"></a>

```c
#define LPS2xDF_DT_ODR_25HZ 4
```

相关声明：[LPS2xDF_DT_ODR_25HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga7ff9cde8d5f782008fd302962e61f62e)。

频率：25 Hz。

<a id="r_ga5f767d66c25ee9d30b292f451fe898e9"></a>

```c
#define LPS2xDF_DT_ODR_50HZ 5
```

相关声明：[LPS2xDF_DT_ODR_50HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga5f767d66c25ee9d30b292f451fe898e9)。

频率：50 Hz。

<a id="r_gaead62a263aae03b5a4b0d4aa4832c921"></a>

```c
#define LPS2xDF_DT_ODR_75HZ 6
```

相关声明：[LPS2xDF_DT_ODR_75HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gaead62a263aae03b5a4b0d4aa4832c921)。

频率：75 Hz。

<a id="r_ga014ee98e7252de3f16d5cc95d602a575"></a>

```c
#define LPS2xDF_DT_ODR_100HZ 7
```

相关声明：[LPS2xDF_DT_ODR_100HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga014ee98e7252de3f16d5cc95d602a575)。

频率：100 Hz。

<a id="r_ga75287fb5fe773719de936e3c35b38935"></a>

```c
#define LPS2xDF_DT_ODR_200HZ 8
```

相关声明：[LPS2xDF_DT_ODR_200HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga75287fb5fe773719de936e3c35b38935)。

频率：200 Hz。

<a id="define-members-1"></a>

### 低通滤波器选项（Low-pass Filter Options）

设备树属性（Devicetree Property）`lpf` 的取值。

<a id="r_gae76b2b2a597dfc2f15dbf310a49846dd"></a>

```c
#define LPS2xDF_DT_LP_FILTER_OFF 0
```

相关声明：[LPS2xDF_DT_LP_FILTER_OFF](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gae76b2b2a597dfc2f15dbf310a49846dd)。

禁用滤波器（Filter Disabled）。

<a id="r_ga73930a4a4a834b102cacfcc262b47b05"></a>

```c
#define LPS2xDF_DT_LP_FILTER_ODR_4 1
```

相关声明：[LPS2xDF_DT_LP_FILTER_ODR_4](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga73930a4a4a834b102cacfcc262b47b05)。

输出数据速率（ODR）除以 4。

<a id="r_ga3dbce218e79cfb34de7cacb216cf9e12"></a>

```c
#define LPS2xDF_DT_LP_FILTER_ODR_9 3
```

相关声明：[LPS2xDF_DT_LP_FILTER_ODR_9](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga3dbce218e79cfb34de7cacb216cf9e12)。

输出数据速率（ODR）除以 9。

<a id="define-members-2"></a>

### 平均采样数量选项（Averaging Number of Samples Options）

设备树属性（Devicetree Property）`avg` 的取值。

<a id="r_gaa2a9f4859187ec438fbf0caf8e97d2d1"></a>

```c
#define LPS2xDF_DT_AVG_4_SAMPLES 0
```

相关声明：[LPS2xDF_DT_AVG_4_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gaa2a9f4859187ec438fbf0caf8e97d2d1)。

4 个样本（Samples）。

<a id="r_gab8401d04498cbc2db82f653fe43bd9c6"></a>

```c
#define LPS2xDF_DT_AVG_8_SAMPLES 1
```

相关声明：[LPS2xDF_DT_AVG_8_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gab8401d04498cbc2db82f653fe43bd9c6)。

8 个样本（Samples）。

<a id="r_gaa78c0c206a4313eeb53607d2f1541a8d"></a>

```c
#define LPS2xDF_DT_AVG_16_SAMPLES 2
```

相关声明：[LPS2xDF_DT_AVG_16_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gaa78c0c206a4313eeb53607d2f1541a8d)。

16 个样本（Samples）。

<a id="r_ga0aa8b28e50ad119bec6082bd152fa6cc"></a>

```c
#define LPS2xDF_DT_AVG_32_SAMPLES 3
```

相关声明：[LPS2xDF_DT_AVG_32_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga0aa8b28e50ad119bec6082bd152fa6cc)。

32 个样本（Samples）。

<a id="r_ga5859a72559cf5121f284eaf3c2acf50f"></a>

```c
#define LPS2xDF_DT_AVG_64_SAMPLES 4
```

相关声明：[LPS2xDF_DT_AVG_64_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga5859a72559cf5121f284eaf3c2acf50f)。

64 个样本（Samples）。

<a id="r_ga17b064199992bae3a44fbe34f068f042"></a>

```c
#define LPS2xDF_DT_AVG_128_SAMPLES 5
```

相关声明：[LPS2xDF_DT_AVG_128_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga17b064199992bae3a44fbe34f068f042)。

128 个样本（Samples）。

<a id="r_ga5695d812598ee97cf07a0f13a229c08c"></a>

```c
#define LPS2xDF_DT_AVG_256_SAMPLES 6
```

相关声明：[LPS2xDF_DT_AVG_256_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga5695d812598ee97cf07a0f13a229c08c)。

256 个样本（Samples）。

<a id="r_gac656a90e3be782d9df47c4bb893843c1"></a>

```c
#define LPS2xDF_DT_AVG_512_SAMPLES 7
```

相关声明：[LPS2xDF_DT_AVG_512_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gac656a90e3be782d9df47c4bb893843c1)。

512 个样本（Samples）。

<a id="define-members-3"></a>

### 满量程压力模式选项（Full-scale Pressure Mode Options）

设备树属性（Devicetree Property）`fs` 的取值。

<a id="r_ga77848469494ffd8912bdc79f65e6fe86"></a>

```c
#define LPS28DFW_DT_FS_MODE_1_1260 0
```

相关声明：[LPS28DFW_DT_FS_MODE_1_1260](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga77848469494ffd8912bdc79f65e6fe86)。

LPS28DFW 模式（Mode）1，1260 hPa。

<a id="r_ga924ab5b02a02c3b28626a87f860c0055"></a>

```c
#define LPS28DFW_DT_FS_MODE_2_4060 1
```

相关声明：[LPS28DFW_DT_FS_MODE_2_4060](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga924ab5b02a02c3b28626a87f860c0055)。

LPS28DFW 模式（Mode）2，4060 hPa。

<a id="r_gabcff3a9fb4a7b883b75bc59c5bd547f3"></a>

```c
#define ILPS22QS_DT_FS_MODE_1_1260 0
```

相关声明：[ILPS22QS_DT_FS_MODE_1_1260](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gabcff3a9fb4a7b883b75bc59c5bd547f3)。

ILPS22QS 模式（Mode）1，1260 hPa。

<a id="r_ga896769c2a9611c670d3e04e554c35ea0"></a>

```c
#define ILPS22QS_DT_FS_MODE_2_4060 1
```

相关声明：[ILPS22QS_DT_FS_MODE_2_4060](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga896769c2a9611c670d3e04e554c35ea0)。

ILPS22QS 模式（Mode）2，4060 hPa。


## 13.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P458_lps2xdf.h_源码浏览.md)
- [LPS2xDF_DT_ODR_POWER_DOWN](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gaba5086849d797518ce64484c3f7c40c2)
- [LPS2xDF_DT_ODR_1HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga4ace0b4fcaa9251e69c934564c116634)
- [LPS2xDF_DT_ODR_4HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga30282e0a4f090bb3106ccb21f577de64)
- [LPS2xDF_DT_ODR_10HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga9bfb85c1e7e6a5f176e6e52447112ba1)
- [LPS2xDF_DT_ODR_25HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga7ff9cde8d5f782008fd302962e61f62e)
- [LPS2xDF_DT_ODR_50HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga5f767d66c25ee9d30b292f451fe898e9)
- [LPS2xDF_DT_ODR_75HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gaead62a263aae03b5a4b0d4aa4832c921)
- [LPS2xDF_DT_ODR_100HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga014ee98e7252de3f16d5cc95d602a575)
- [LPS2xDF_DT_ODR_200HZ](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga75287fb5fe773719de936e3c35b38935)
- [LPS2xDF_DT_LP_FILTER_OFF](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gae76b2b2a597dfc2f15dbf310a49846dd)
- [LPS2xDF_DT_LP_FILTER_ODR_4](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga73930a4a4a834b102cacfcc262b47b05)
- [LPS2xDF_DT_LP_FILTER_ODR_9](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga3dbce218e79cfb34de7cacb216cf9e12)
- [LPS2xDF_DT_AVG_4_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gaa2a9f4859187ec438fbf0caf8e97d2d1)
- [LPS2xDF_DT_AVG_8_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gab8401d04498cbc2db82f653fe43bd9c6)
- [LPS2xDF_DT_AVG_16_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gaa78c0c206a4313eeb53607d2f1541a8d)
- [LPS2xDF_DT_AVG_32_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga0aa8b28e50ad119bec6082bd152fa6cc)
- [LPS2xDF_DT_AVG_64_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga5859a72559cf5121f284eaf3c2acf50f)
- [LPS2xDF_DT_AVG_128_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga17b064199992bae3a44fbe34f068f042)
- [LPS2xDF_DT_AVG_256_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga5695d812598ee97cf07a0f13a229c08c)
- [LPS2xDF_DT_AVG_512_SAMPLES](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gac656a90e3be782d9df47c4bb893843c1)
- [LPS28DFW_DT_FS_MODE_1_1260](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga77848469494ffd8912bdc79f65e6fe86)
- [LPS28DFW_DT_FS_MODE_2_4060](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga924ab5b02a02c3b28626a87f860c0055)
- [ILPS22QS_DT_FS_MODE_1_1260](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#gabcff3a9fb4a7b883b75bc59c5bd547f3)
- [ILPS22QS_DT_FS_MODE_2_4060](../api_power_policy_topic_reference/P007_LPS2xDF API主题.md#ga896769c2a9611c670d3e04e554c35ea0)

<a id="header-details"></a>

---

[上一章](P012_zephyr__net__ieee802154.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__net__mdns_responder.h_文件参考.md)
