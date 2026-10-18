---
id: learning.zephyr-docs.api-file-host-video-reference.page-9
title: zephyr__dt-bindings__sensor__mc3419.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mc3419_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_sensor\_\_mc3419.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mc3419_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the MEMSIC MC3419 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the MEMSIC MC3419 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 低通滤波器选项（Low-pass Filter Options）

设备树属性（Devicetree Property）`lpf-fc-sel` 的取值。

启用的选项将滤波器截止频率（Corner Frequency，Fc）设置为内部数据速率（Internal Data Rate，IDR）的某个比例。

<a id="r_ga11cd920edd9483d882366beeb728b518"></a>

```c
#define MC3419_LPF_DISABLE 0
```

相关声明：[MC3419_LPF_DISABLE](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga11cd920edd9483d882366beeb728b518)。

禁用滤波器（Filter Disabled）。

<a id="r_ga0123fd43d398d82350a3291222eb2bbc"></a>

```c
#define MC3419_LPF_EN_WITH_IDR_BY_4p255_FC 9
```

相关声明：[MC3419_LPF_EN_WITH_IDR_BY_4p255_FC](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga0123fd43d398d82350a3291222eb2bbc)。

截止频率（Fc）等于内部数据速率（IDR）除以 4.255。

<a id="r_ga5daff5558d967eab297821d0ce3d701d"></a>

```c
#define MC3419_LPF_EN_WITH_IDR_BY_6_FC 10
```

相关声明：[MC3419_LPF_EN_WITH_IDR_BY_6_FC](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga5daff5558d967eab297821d0ce3d701d)。

截止频率（Fc）等于内部数据速率（IDR）除以 6。

<a id="r_ga9b38fa6d4a2a0d61c85dd36304518caa"></a>

```c
#define MC3419_LPF_EN_WITH_IDR_BY_12_FC 11
```

相关声明：[MC3419_LPF_EN_WITH_IDR_BY_12_FC](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga9b38fa6d4a2a0d61c85dd36304518caa)。

截止频率（Fc）等于内部数据速率（IDR）除以 12。

<a id="r_gaeaaf8bb96a00e0b3424f6cda73418ee7"></a>

```c
#define MC3419_LPF_EN_WITH_IDR_BY_16_FC 13
```

相关声明：[MC3419_LPF_EN_WITH_IDR_BY_16_FC](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gaeaaf8bb96a00e0b3424f6cda73418ee7)。

截止频率（Fc）等于内部数据速率（IDR）除以 16。

<a id="define-members-1"></a>

### 抽取率选项（Decimation Rate Options）

设备树属性（Devicetree Property）`decimation-rate` 的取值。

将内部数据速率（IDR）除以所选因子（Factor）。

<a id="r_ga2f3efa22b849c6d4671e86018be4979a"></a>

```c
#define MC3419_DECIMATE_IDR_BY_1 0
```

相关声明：[MC3419_DECIMATE_IDR_BY_1](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga2f3efa22b849c6d4671e86018be4979a)。

内部数据速率（IDR）除以 1。

<a id="r_gab6f9750f1f2769a92cac010d4a5e12b7"></a>

```c
#define MC3419_DECIMATE_IDR_BY_2 1
```

相关声明：[MC3419_DECIMATE_IDR_BY_2](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gab6f9750f1f2769a92cac010d4a5e12b7)。

内部数据速率（IDR）除以 2。

<a id="r_ga541ce2fe5ed9df3104b4dcfb54a3c307"></a>

```c
#define MC3419_DECIMATE_IDR_BY_4 2
```

相关声明：[MC3419_DECIMATE_IDR_BY_4](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga541ce2fe5ed9df3104b4dcfb54a3c307)。

内部数据速率（IDR）除以 4。

<a id="r_ga352782642aad37ae5ee68786e40c13b3"></a>

```c
#define MC3419_DECIMATE_IDR_BY_5 3
```

相关声明：[MC3419_DECIMATE_IDR_BY_5](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga352782642aad37ae5ee68786e40c13b3)。

内部数据速率（IDR）除以 5。

<a id="r_gafe04e51c2f5fbe81dbe1694a1612b644"></a>

```c
#define MC3419_DECIMATE_IDR_BY_8 4
```

相关声明：[MC3419_DECIMATE_IDR_BY_8](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gafe04e51c2f5fbe81dbe1694a1612b644)。

内部数据速率（IDR）除以 8。

<a id="r_gaa60312616dfd56a204e62be699b27c90"></a>

```c
#define MC3419_DECIMATE_IDR_BY_10 5
```

相关声明：[MC3419_DECIMATE_IDR_BY_10](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gaa60312616dfd56a204e62be699b27c90)。

内部数据速率（IDR）除以 10。

<a id="r_gae64d9aa76f76a4cea593e0945a41bb0b"></a>

```c
#define MC3419_DECIMATE_IDR_BY_16 6
```

相关声明：[MC3419_DECIMATE_IDR_BY_16](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gae64d9aa76f76a4cea593e0945a41bb0b)。

内部数据速率（IDR）除以 16。

<a id="r_gab9e66b4d2e02787bdc40e39a4cc481d3"></a>

```c
#define MC3419_DECIMATE_IDR_BY_20 7
```

相关声明：[MC3419_DECIMATE_IDR_BY_20](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gab9e66b4d2e02787bdc40e39a4cc481d3)。

内部数据速率（IDR）除以 20。

<a id="r_ga1a0c0568aa9f2faed334638a8412d88d"></a>

```c
#define MC3419_DECIMATE_IDR_BY_40 8
```

相关声明：[MC3419_DECIMATE_IDR_BY_40](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga1a0c0568aa9f2faed334638a8412d88d)。

内部数据速率（IDR）除以 40。

<a id="r_gaf8974281d52d9d0657835850d79bb4c1"></a>

```c
#define MC3419_DECIMATE_IDR_BY_67 9
```

相关声明：[MC3419_DECIMATE_IDR_BY_67](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gaf8974281d52d9d0657835850d79bb4c1)。

内部数据速率（IDR）除以 67。

<a id="r_gac778f60735b0f2c14e53a6a835bbbd75"></a>

```c
#define MC3419_DECIMATE_IDR_BY_80 10
```

相关声明：[MC3419_DECIMATE_IDR_BY_80](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gac778f60735b0f2c14e53a6a835bbbd75)。

内部数据速率（IDR）除以 80。

<a id="r_ga2f0fd6a142da25d9e4bf2a95281cfa7d"></a>

```c
#define MC3419_DECIMATE_IDR_BY_100 11
```

相关声明：[MC3419_DECIMATE_IDR_BY_100](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga2f0fd6a142da25d9e4bf2a95281cfa7d)。

内部数据速率（IDR）除以 100。

<a id="r_ga8793b433099272dec442a9a9d485e587"></a>

```c
#define MC3419_DECIMATE_IDR_BY_200 12
```

相关声明：[MC3419_DECIMATE_IDR_BY_200](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga8793b433099272dec442a9a9d485e587)。

内部数据速率（IDR）除以 200。

<a id="r_ga00f5b28b6d6ef247e283799820cfebe2"></a>

```c
#define MC3419_DECIMATE_IDR_BY_250 13
```

相关声明：[MC3419_DECIMATE_IDR_BY_250](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga00f5b28b6d6ef247e283799820cfebe2)。

内部数据速率（IDR）除以 250。

<a id="r_gaef90dffe184d84c8ee86e0f303541edc"></a>

```c
#define MC3419_DECIMATE_IDR_BY_500 14
```

相关声明：[MC3419_DECIMATE_IDR_BY_500](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gaef90dffe184d84c8ee86e0f303541edc)。

内部数据速率（IDR）除以 500。

<a id="r_ga001fd7fd72fd5844d8bd614864d0e210"></a>

```c
#define MC3419_DECIMATE_IDR_BY_1000 15
```

相关声明：[MC3419_DECIMATE_IDR_BY_1000](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga001fd7fd72fd5844d8bd614864d0e210)。

内部数据速率（IDR）除以 1000。


## 9.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P489_mc3419.h_源码浏览.md)
- [MC3419_LPF_DISABLE](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga11cd920edd9483d882366beeb728b518)
- [MC3419_LPF_EN_WITH_IDR_BY_4p255_FC](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga0123fd43d398d82350a3291222eb2bbc)
- [MC3419_LPF_EN_WITH_IDR_BY_6_FC](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga5daff5558d967eab297821d0ce3d701d)
- [MC3419_LPF_EN_WITH_IDR_BY_12_FC](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga9b38fa6d4a2a0d61c85dd36304518caa)
- [MC3419_LPF_EN_WITH_IDR_BY_16_FC](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gaeaaf8bb96a00e0b3424f6cda73418ee7)
- [MC3419_DECIMATE_IDR_BY_1](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga2f3efa22b849c6d4671e86018be4979a)
- [MC3419_DECIMATE_IDR_BY_2](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gab6f9750f1f2769a92cac010d4a5e12b7)
- [MC3419_DECIMATE_IDR_BY_4](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga541ce2fe5ed9df3104b4dcfb54a3c307)
- [MC3419_DECIMATE_IDR_BY_5](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga352782642aad37ae5ee68786e40c13b3)
- [MC3419_DECIMATE_IDR_BY_8](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gafe04e51c2f5fbe81dbe1694a1612b644)
- [MC3419_DECIMATE_IDR_BY_10](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gaa60312616dfd56a204e62be699b27c90)
- [MC3419_DECIMATE_IDR_BY_16](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gae64d9aa76f76a4cea593e0945a41bb0b)
- [MC3419_DECIMATE_IDR_BY_20](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gab9e66b4d2e02787bdc40e39a4cc481d3)
- [MC3419_DECIMATE_IDR_BY_40](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga1a0c0568aa9f2faed334638a8412d88d)
- [MC3419_DECIMATE_IDR_BY_67](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gaf8974281d52d9d0657835850d79bb4c1)
- [MC3419_DECIMATE_IDR_BY_80](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gac778f60735b0f2c14e53a6a835bbbd75)
- [MC3419_DECIMATE_IDR_BY_100](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga2f0fd6a142da25d9e4bf2a95281cfa7d)
- [MC3419_DECIMATE_IDR_BY_200](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga8793b433099272dec442a9a9d485e587)
- [MC3419_DECIMATE_IDR_BY_250](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga00f5b28b6d6ef247e283799820cfebe2)
- [MC3419_DECIMATE_IDR_BY_500](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#gaef90dffe184d84c8ee86e0f303541edc)
- [MC3419_DECIMATE_IDR_BY_1000](../api_hid_pipeline_topic_reference/P006_MC3419 API主题.md#ga001fd7fd72fd5844d8bd614864d0e210)

<a id="header-details"></a>

---

[上一章](P008_zephyr__drivers__interrupt_controller__intel_vtd.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__drivers__clock_control__nrf_clock_control.h_文件参考.md)
