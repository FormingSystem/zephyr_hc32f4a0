---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-4
title: zephyr__dt-bindings__sensor__afbr_s50.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2afbr__s50_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_sensor\_\_afbr\_s50.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2afbr__s50_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Broadcom AFBR-S50 ToF sensor的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Broadcom AFBR-S50 ToF sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 双频模式选项（Dual-frequency Mode Options）

设备树属性（Devicetree Property）`dual-freq-mode` 的取值。

双频模式（Dual-frequency Mode）结合两个调制频率下的测量结果，扩展无模糊量程（Unambiguous Range）。

<a id="r_ga8876f0466109e96bdfea3fc533180539"></a>

```c
#define AFBR_S50_DT_DFM_MODE_OFF 0
```

相关声明：[AFBR_S50_DT_DFM_MODE_OFF](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga8876f0466109e96bdfea3fc533180539)。

禁用（Disabled）。

<a id="r_gad3b8e0c86fe0ef50ff8b134bb952b6ee"></a>

```c
#define AFBR_S50_DT_DFM_MODE_4X 1
```

相关声明：[AFBR_S50_DT_DFM_MODE_4X](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gad3b8e0c86fe0ef50ff8b134bb952b6ee)。

4 倍量程扩展（4x Range Extension）。

<a id="r_ga142b78ba68727d9c85dbe243503dff65"></a>

```c
#define AFBR_S50_DT_DFM_MODE_8X 2
```

相关声明：[AFBR_S50_DT_DFM_MODE_8X](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga142b78ba68727d9c85dbe243503dff65)。

8 倍量程扩展（8x Range Extension）。

<a id="define-members-1"></a>

### 测量模式（Measurement Modes）

设备树属性（Devicetree Property）`measurement-mode` 的取值。

带 `laser-class-2` 后缀的模式会提高光学输出功率（Optical Output Power）。

<a id="r_gadfe6cccf720230f57a84d366733fab31"></a>

```c
#define AFBR_S50_DT_MODE_SHORT_RANGE 1
```

相关声明：[AFBR_S50_DT_MODE_SHORT_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gadfe6cccf720230f57a84d366733fab31)。

短量程（Short Range）。

<a id="r_ga44f255c5f786d435a06a134ef6f1f767"></a>

```c
#define AFBR_S50_DT_MODE_LONG_RANGE 2
```

相关声明：[AFBR_S50_DT_MODE_LONG_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga44f255c5f786d435a06a134ef6f1f767)。

长量程（Long Range）。

<a id="r_gaee1514551ef77c017071231509c51f16"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE 5
```

相关声明：[AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gaee1514551ef77c017071231509c51f16)。

高速短量程（High-speed Short Range）。

<a id="r_gad28361ea69a29cc5c4e6a856a3fa59e4"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE 6
```

相关声明：[AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gad28361ea69a29cc5c4e6a856a3fa59e4)。

高速长量程（High-speed Long Range）。

<a id="r_ga7859e170d43d8b0741601abf10ce23bd"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE 9
```

相关声明：[AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga7859e170d43d8b0741601abf10ce23bd)。

高精度短量程（High-precision Short Range）。

<a id="r_ga0c7b3995f3df932279d03771f41f1fe1"></a>

```c
#define AFBR_S50_DT_MODE_SHORT_RANGE_LASER_CLASS_2 129
```

相关声明：[AFBR_S50_DT_MODE_SHORT_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga0c7b3995f3df932279d03771f41f1fe1)。

短量程（Short Range），2 类激光（Laser Class 2）。

<a id="r_gaa4f9e151e35ae38abf0e9488029a1258"></a>

```c
#define AFBR_S50_DT_MODE_LONG_RANGE_LASER_CLASS_2 130
```

相关声明：[AFBR_S50_DT_MODE_LONG_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gaa4f9e151e35ae38abf0e9488029a1258)。

长量程（Long Range），2 类激光（Laser Class 2）。

<a id="r_ga673e118c7fc92d0cb83f30f599f45209"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE_LASER_CLASS_2 133
```

相关声明：[AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga673e118c7fc92d0cb83f30f599f45209)。

高速短量程（High-speed Short Range），2 类激光（Laser Class 2）。

<a id="r_gad4b8aa14142578155e83adb7ee0e83b5"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE_LASER_CLASS_2 134
```

相关声明：[AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gad4b8aa14142578155e83adb7ee0e83b5)。

高速长量程（High-speed Long Range），2 类激光（Laser Class 2）。

<a id="r_ga2d7544987a12b451812e3fc259a851ef"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE_LASER_CLASS_2 137
```

相关声明：[AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga2d7544987a12b451812e3fc259a851ef)。

高精度短量程（High-precision Short Range），2 类激光（Laser Class 2）。


## 4.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P202_afbr_s50.h_源码浏览.md)
- [AFBR_S50_DT_DFM_MODE_OFF](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga8876f0466109e96bdfea3fc533180539)
- [AFBR_S50_DT_DFM_MODE_4X](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gad3b8e0c86fe0ef50ff8b134bb952b6ee)
- [AFBR_S50_DT_DFM_MODE_8X](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga142b78ba68727d9c85dbe243503dff65)
- [AFBR_S50_DT_MODE_SHORT_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gadfe6cccf720230f57a84d366733fab31)
- [AFBR_S50_DT_MODE_LONG_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga44f255c5f786d435a06a134ef6f1f767)
- [AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gaee1514551ef77c017071231509c51f16)
- [AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gad28361ea69a29cc5c4e6a856a3fa59e4)
- [AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga7859e170d43d8b0741601abf10ce23bd)
- [AFBR_S50_DT_MODE_SHORT_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga0c7b3995f3df932279d03771f41f1fe1)
- [AFBR_S50_DT_MODE_LONG_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gaa4f9e151e35ae38abf0e9488029a1258)
- [AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga673e118c7fc92d0cb83f30f599f45209)
- [AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#gad4b8aa14142578155e83adb7ee0e83b5)
- [AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE_LASER_CLASS_2](../api_input_runtime_topic_reference/P001_AFBR-S50 API主题.md#ga2d7544987a12b451812e3fc259a851ef)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__wuc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__sensor__icm45686.h_文件参考.md)
