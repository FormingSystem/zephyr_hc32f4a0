---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-10
title: zephyr__dt-bindings__sensor__iis2dlpc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/iis2dlpc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_sensor\_\_iis2dlpc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/iis2dlpc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST IIS2DLPC accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST IIS2DLPC accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 电源模式（Power Modes）

设备树属性（Devicetree Property）`power-mode` 的取值。

<a id="r_ga1e1c2a12612d55d0d1a60e6df5cc3050"></a>

```c
#define IIS2DLPC_DT_LP_M1 0
```

相关声明：[IIS2DLPC_DT_LP_M1](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga1e1c2a12612d55d0d1a60e6df5cc3050)。

低功耗模式（Low-power Mode）1，12 位。

<a id="r_ga52571a5d3d8e7a042a442f8d8b55029e"></a>

```c
#define IIS2DLPC_DT_LP_M2 1
```

相关声明：[IIS2DLPC_DT_LP_M2](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga52571a5d3d8e7a042a442f8d8b55029e)。

低功耗模式（Low-power Mode）2，14 位。

<a id="r_gada77b7def23ffce8089c4773204a5ed0"></a>

```c
#define IIS2DLPC_DT_LP_M3 2
```

相关声明：[IIS2DLPC_DT_LP_M3](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gada77b7def23ffce8089c4773204a5ed0)。

低功耗模式（Low-power Mode）3，14 位。

<a id="r_gaa39b8641e427747eb81ab276b30447f9"></a>

```c
#define IIS2DLPC_DT_LP_M4 3
```

相关声明：[IIS2DLPC_DT_LP_M4](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gaa39b8641e427747eb81ab276b30447f9)。

低功耗模式（Low-power Mode）4，14 位。

<a id="r_ga623fd5c18feaac196c33265ea84aa0e8"></a>

```c
#define IIS2DLPC_DT_HP_MODE 4
```

相关声明：[IIS2DLPC_DT_HP_MODE](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga623fd5c18feaac196c33265ea84aa0e8)。

高性能模式（High-performance Mode），14 位。

<a id="define-members-1"></a>

### 滤波器带宽选项（Filter Bandwidth Options）

抗混叠滤波器（Anti-aliasing Filter）的带宽，用输出数据速率（ODR）的比例表示。

<a id="r_gabf53338af02c9036850d61f4942123fe"></a>

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_2 0
```

相关声明：[IIS2DLPC_DT_FILTER_BW_ODR_DIV_2](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gabf53338af02c9036850d61f4942123fe)。

输出数据速率（ODR）除以 2。

<a id="r_ga24ba2864f9a1c76f73636ab40ce977cc"></a>

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_4 1
```

相关声明：[IIS2DLPC_DT_FILTER_BW_ODR_DIV_4](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga24ba2864f9a1c76f73636ab40ce977cc)。

输出数据速率（ODR）除以 4。

<a id="r_gae701e403e5b068c4188bf6ecebc5e088"></a>

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_10 2
```

相关声明：[IIS2DLPC_DT_FILTER_BW_ODR_DIV_10](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gae701e403e5b068c4188bf6ecebc5e088)。

输出数据速率（ODR）除以 10。

<a id="r_gab453a45f6561c03f6c2657b025fb8280"></a>

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_20 3
```

相关声明：[IIS2DLPC_DT_FILTER_BW_ODR_DIV_20](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gab453a45f6561c03f6c2657b025fb8280)。

输出数据速率（ODR）除以 20。

<a id="define-members-2"></a>

### 敲击检测模式（Tap Detection Mode）

设备树属性（Devicetree Property）`tap-mode` 的取值。

<a id="r_ga52c4b179f307100adfbe341dcc8756b1"></a>

```c
#define IIS2DLPC_DT_SINGLE_TAP 0
```

相关声明：[IIS2DLPC_DT_SINGLE_TAP](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga52c4b179f307100adfbe341dcc8756b1)。

仅单击（Single-tap Only）。

<a id="r_gae49fca709c40c78ae3001454d2277761"></a>

```c
#define IIS2DLPC_DT_SINGLE_DOUBLE_TAP 1
```

相关声明：[IIS2DLPC_DT_SINGLE_DOUBLE_TAP](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gae49fca709c40c78ae3001454d2277761)。

单击与双击（Single and Double Tap）。

<a id="define-members-3"></a>

### 自由落体阈值选项（Free-fall Threshold Options）

自由落体检测阈值（Free-fall Detection Threshold）。

<a id="r_ga31b120d2c9f9271f6d6c0e6270d6869c"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_156_mg 0
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_156_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga31b120d2c9f9271f6d6c0e6270d6869c)。

156 mg（千分之一标准重力加速度）。

<a id="r_gaa03f24ea0546d41d75b7b27980ec4a03"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_219_mg 1
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_219_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gaa03f24ea0546d41d75b7b27980ec4a03)。

219 mg（千分之一标准重力加速度）。

<a id="r_gaa97f60a94b60643bf8fd53ba93a213b5"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_250_mg 2
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_250_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gaa97f60a94b60643bf8fd53ba93a213b5)。

250 mg（千分之一标准重力加速度）。

<a id="r_ga6958c72e3b6a4202c2e393802f44c045"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_312_mg 3
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_312_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga6958c72e3b6a4202c2e393802f44c045)。

312 mg（千分之一标准重力加速度）。

<a id="r_ga368134487e769d5b6a9a8c43caf75fb4"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_344_mg 4
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_344_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga368134487e769d5b6a9a8c43caf75fb4)。

344 mg（千分之一标准重力加速度）。

<a id="r_ga189b31dc699c5c7698289502d1d4a2c2"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_406_mg 5
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_406_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga189b31dc699c5c7698289502d1d4a2c2)。

406 mg（千分之一标准重力加速度）。

<a id="r_gabb23c1eaaa0b82d566e3c6fb24b4bf75"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_469_mg 6
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_469_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gabb23c1eaaa0b82d566e3c6fb24b4bf75)。

469 mg（千分之一标准重力加速度）。

<a id="r_ga84b6e0ed1a646f349e7e166e18ef3b5d"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_500_mg 7
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_500_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga84b6e0ed1a646f349e7e166e18ef3b5d)。

500 mg（千分之一标准重力加速度）。

<a id="define-members-4"></a>

### 唤醒持续时间选项（Wake-up Duration Options）

唤醒事件持续时间（Wake-up Event Duration），以输出数据速率周期（ODR Periods）为单位。

<a id="r_gad369d4265e7542856d5ccd052fcb3025"></a>

```c
#define IIS2DLPC_DT_WAKEUP_1_ODR 0
```

相关声明：[IIS2DLPC_DT_WAKEUP_1_ODR](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gad369d4265e7542856d5ccd052fcb3025)。

1 个输出数据速率周期（ODR Period）。

<a id="r_gad7f6fb74463c30e726dc34ef9462993c"></a>

```c
#define IIS2DLPC_DT_WAKEUP_2_ODR 1
```

相关声明：[IIS2DLPC_DT_WAKEUP_2_ODR](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gad7f6fb74463c30e726dc34ef9462993c)。

2 个输出数据速率周期（ODR Period）。

<a id="r_gad3f89e84420074c53fc9e13a30f116a8"></a>

```c
#define IIS2DLPC_DT_WAKEUP_3_ODR 2
```

相关声明：[IIS2DLPC_DT_WAKEUP_3_ODR](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gad3f89e84420074c53fc9e13a30f116a8)。

3 个输出数据速率周期（ODR Period）。

<a id="r_ga651cadb8f638381169876dbd5291714a"></a>

```c
#define IIS2DLPC_DT_WAKEUP_4_ODR 3
```

相关声明：[IIS2DLPC_DT_WAKEUP_4_ODR](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga651cadb8f638381169876dbd5291714a)。

4 个输出数据速率周期（ODR Period）。


## 10.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P345_iis2dlpc.h_源码浏览.md)
- [IIS2DLPC_DT_LP_M1](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga1e1c2a12612d55d0d1a60e6df5cc3050)
- [IIS2DLPC_DT_LP_M2](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga52571a5d3d8e7a042a442f8d8b55029e)
- [IIS2DLPC_DT_LP_M3](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gada77b7def23ffce8089c4773204a5ed0)
- [IIS2DLPC_DT_LP_M4](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gaa39b8641e427747eb81ab276b30447f9)
- [IIS2DLPC_DT_HP_MODE](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga623fd5c18feaac196c33265ea84aa0e8)
- [IIS2DLPC_DT_FILTER_BW_ODR_DIV_2](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gabf53338af02c9036850d61f4942123fe)
- [IIS2DLPC_DT_FILTER_BW_ODR_DIV_4](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga24ba2864f9a1c76f73636ab40ce977cc)
- [IIS2DLPC_DT_FILTER_BW_ODR_DIV_10](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gae701e403e5b068c4188bf6ecebc5e088)
- [IIS2DLPC_DT_FILTER_BW_ODR_DIV_20](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gab453a45f6561c03f6c2657b025fb8280)
- [IIS2DLPC_DT_SINGLE_TAP](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga52c4b179f307100adfbe341dcc8756b1)
- [IIS2DLPC_DT_SINGLE_DOUBLE_TAP](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gae49fca709c40c78ae3001454d2277761)
- [IIS2DLPC_DT_FF_THRESHOLD_156_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga31b120d2c9f9271f6d6c0e6270d6869c)
- [IIS2DLPC_DT_FF_THRESHOLD_219_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gaa03f24ea0546d41d75b7b27980ec4a03)
- [IIS2DLPC_DT_FF_THRESHOLD_250_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gaa97f60a94b60643bf8fd53ba93a213b5)
- [IIS2DLPC_DT_FF_THRESHOLD_312_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga6958c72e3b6a4202c2e393802f44c045)
- [IIS2DLPC_DT_FF_THRESHOLD_344_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga368134487e769d5b6a9a8c43caf75fb4)
- [IIS2DLPC_DT_FF_THRESHOLD_406_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga189b31dc699c5c7698289502d1d4a2c2)
- [IIS2DLPC_DT_FF_THRESHOLD_469_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gabb23c1eaaa0b82d566e3c6fb24b4bf75)
- [IIS2DLPC_DT_FF_THRESHOLD_500_mg](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga84b6e0ed1a646f349e7e166e18ef3b5d)
- [IIS2DLPC_DT_WAKEUP_1_ODR](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gad369d4265e7542856d5ccd052fcb3025)
- [IIS2DLPC_DT_WAKEUP_2_ODR](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gad7f6fb74463c30e726dc34ef9462993c)
- [IIS2DLPC_DT_WAKEUP_3_ODR](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#gad3f89e84420074c53fc9e13a30f116a8)
- [IIS2DLPC_DT_WAKEUP_4_ODR](../api_bridge_paging_topic_reference/P005_IIS2DLPC API主题.md#ga651cadb8f638381169876dbd5291714a)

<a id="header-details"></a>

---

[上一章](P009_zephyr__drivers__haptics.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__dt-bindings__power__imx952_power.h_文件参考.md)
