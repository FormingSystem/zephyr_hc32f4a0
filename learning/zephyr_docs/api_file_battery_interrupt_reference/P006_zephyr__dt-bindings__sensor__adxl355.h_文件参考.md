---
id: learning.zephyr-docs.api-file-battery-interrupt-reference.page-6
title: zephyr__dt-bindings__sensor__adxl355.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2adxl355_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_dt-bindings\_\_sensor\_\_adxl355.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2adxl355_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Analog Devices ADXL355 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Analog Devices ADXL355 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输出速率选项（Output Rate Options）

设备树 `odr` 属性的取值。

<a id="r_gab60be1cb5989008043c4c768c4bb67a5"></a>

```c
#define ADXL355_DT_ODR_4000 0
```

相关声明：[ADXL355_DT_ODR_4000](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gab60be1cb5989008043c4c768c4bb67a5)。

输出数据速率（Output Data Rate）：4000 Hz。

<a id="r_gaae25fe8c25742fb0358dff1c4aa95eef"></a>

```c
#define ADXL355_DT_ODR_2000 1
```

相关声明：[ADXL355_DT_ODR_2000](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gaae25fe8c25742fb0358dff1c4aa95eef)。

输出数据速率（Output Data Rate）：2000 Hz。

<a id="r_ga5aabb32d884ee322d8744408e507aee8"></a>

```c
#define ADXL355_DT_ODR_1000 2
```

相关声明：[ADXL355_DT_ODR_1000](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga5aabb32d884ee322d8744408e507aee8)。

输出数据速率（Output Data Rate）：1000 Hz。

<a id="r_ga8c19b7c5d1a57c33a0ae3a5edc114768"></a>

```c
#define ADXL355_DT_ODR_500 3
```

相关声明：[ADXL355_DT_ODR_500](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga8c19b7c5d1a57c33a0ae3a5edc114768)。

输出数据速率（Output Data Rate）：500 Hz。

<a id="r_ga71a30b4c271eabcf11ca501acfb05ff3"></a>

```c
#define ADXL355_DT_ODR_250 4
```

相关声明：[ADXL355_DT_ODR_250](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga71a30b4c271eabcf11ca501acfb05ff3)。

输出数据速率（Output Data Rate）：250 Hz。

<a id="r_gab411f93d442413e4ca21061115c1399c"></a>

```c
#define ADXL355_DT_ODR_125 5
```

相关声明：[ADXL355_DT_ODR_125](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gab411f93d442413e4ca21061115c1399c)。

输出数据速率（Output Data Rate）：125 Hz。

<a id="r_gad0bf8e8272a0db9be1452c21a122cd98"></a>

```c
#define ADXL355_DT_ODR_62_5 6
```

相关声明：[ADXL355_DT_ODR_62_5](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gad0bf8e8272a0db9be1452c21a122cd98)。

输出数据速率（Output Data Rate）：62.5 Hz。

<a id="r_ga4f85d789f9b184ac8a96c75590a93719"></a>

```c
#define ADXL355_DT_ODR_31_25 7
```

相关声明：[ADXL355_DT_ODR_31_25](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga4f85d789f9b184ac8a96c75590a93719)。

输出数据速率（Output Data Rate）：31.25 Hz。

<a id="r_ga61378797ab5e9e8d373908efce4df39e"></a>

```c
#define ADXL355_DT_ODR_15_625 8
```

相关声明：[ADXL355_DT_ODR_15_625](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga61378797ab5e9e8d373908efce4df39e)。

输出数据速率（Output Data Rate）：15.625 Hz。

<a id="r_ga92cb10f98315e05768a90fd9397eccff"></a>

```c
#define ADXL355_DT_ODR_7_813 9
```

相关声明：[ADXL355_DT_ODR_7_813](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga92cb10f98315e05768a90fd9397eccff)。

输出数据速率（Output Data Rate）：7.813 Hz。

<a id="r_ga0d6025b885cc0b21174b96f8fa2dced6"></a>

```c
#define ADXL355_DT_ODR_3_906 10
```

相关声明：[ADXL355_DT_ODR_3_906](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga0d6025b885cc0b21174b96f8fa2dced6)。

输出数据速率（Output Data Rate）：3.906 Hz。

<a id="define-members-1"></a>

### 测量范围选择选项（Select Range Options）

设备树 `range` 属性的取值。

<a id="r_gac0296485c3d583e12c9d4a73ee532f33"></a>

```c
#define ADXL355_DT_RANGE_2G 1
```

相关声明：[ADXL355_DT_RANGE_2G](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gac0296485c3d583e12c9d4a73ee532f33)。

选择 ±2 g 测量范围（Measurement Range）。

<a id="r_gaff43fe8c86158d46b826df053a6fa530"></a>

```c
#define ADXL355_DT_RANGE_4G 2
```

相关声明：[ADXL355_DT_RANGE_4G](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gaff43fe8c86158d46b826df053a6fa530)。

选择 ±4 g 测量范围（Measurement Range）。

<a id="r_ga083df135be18fe7bcdd1f6681d434197"></a>

```c
#define ADXL355_DT_RANGE_8G 3
```

相关声明：[ADXL355_DT_RANGE_8G](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga083df135be18fe7bcdd1f6681d434197)。

选择 ±8 g 测量范围（Measurement Range）。

<a id="define-members-2"></a>

### 高通滤波器截止频率选项（High Pass Filter Corner Options）

设备树属性（Devicetree Property）`hpf-corner` 的取值。

<a id="r_ga15cb598fda2032fea4f74df2dd586c43"></a>

```c
#define ADXL355_DT_HPF_OFF 0
```

相关声明：[ADXL355_DT_HPF_OFF](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga15cb598fda2032fea4f74df2dd586c43)。

高通滤波器（High-pass Filter）禁用。

<a id="r_ga2bb6fc7a0f5db2d41d1b7ab41408e5cf"></a>

```c
#define ADXL355_DT_HPF_24_7e_4 1
```

相关声明：[ADXL355_DT_HPF_24_7e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga2bb6fc7a0f5db2d41d1b7ab41408e5cf)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 24.7e-4 倍。

<a id="r_gad88ed912cd272948bf6cc1d99786d190"></a>

```c
#define ADXL355_DT_HPF_6_208e_4 2
```

相关声明：[ADXL355_DT_HPF_6_208e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gad88ed912cd272948bf6cc1d99786d190)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 6.208e-4 倍。

<a id="r_ga73f0b16ce376b02d42f0f93ff6ccc97c"></a>

```c
#define ADXL355_DT_HPF_1_5545e_4 3
```

相关声明：[ADXL355_DT_HPF_1_5545e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga73f0b16ce376b02d42f0f93ff6ccc97c)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 1.5545e-4 倍。

<a id="r_ga8eeaac80b071b9d0921e00d085cc0e0a"></a>

```c
#define ADXL355_DT_HPF_0_3862e_4 4
```

相关声明：[ADXL355_DT_HPF_0_3862e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga8eeaac80b071b9d0921e00d085cc0e0a)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.3862e-4 倍。

<a id="r_ga34c4fe4b7bbea96d3f6153746dc6228c"></a>

```c
#define ADXL355_DT_HPF_0_0954e_4 5
```

相关声明：[ADXL355_DT_HPF_0_0954e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga34c4fe4b7bbea96d3f6153746dc6228c)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.0954e-4 倍。

<a id="r_ga665874864fa75fef549936a93ae61b52"></a>

```c
#define ADXL355_DT_HPF_0_0238e_4 6
```

相关声明：[ADXL355_DT_HPF_0_0238e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga665874864fa75fef549936a93ae61b52)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.0238e-4 倍。

<a id="define-members-3"></a>

### 外部时钟选项（External Clock Options）

设备树属性（Devicetree Property）`ext-clk` 的取值。

<a id="r_ga218ea74d36be97682a38b860b58b717f"></a>

```c
#define ADXL355_DT_EXTCLK_DISABLED 0
```

相关声明：[ADXL355_DT_EXTCLK_DISABLED](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga218ea74d36be97682a38b860b58b717f)。

外部时钟（External Clock）禁用。

<a id="r_gaa9bed643f472c8c4f9056465be1fe1c6"></a>

```c
#define ADXL355_DT_EXTCLK_ENABLED 1
```

相关声明：[ADXL355_DT_EXTCLK_ENABLED](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gaa9bed643f472c8c4f9056465be1fe1c6)。

外部时钟（External Clock）启用。

<a id="define-members-4"></a>

### 外部同步选项（External Sync Options）

设备树属性（Devicetree Property）`ext-sync` 的取值。

<a id="r_gafb59af517b95dcd49521605624ccd0f2"></a>

```c
#define ADXL355_DT_INTERNAL_SYNC 0
```

相关声明：[ADXL355_DT_INTERNAL_SYNC](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gafb59af517b95dcd49521605624ccd0f2)。

内部同步（Internal Synchronization）。

<a id="r_gab54040571fbb582ab22f60b878861db6"></a>

```c
#define ADXL355_DT_EXTERNAL_SYNC_NO_INTERPOLATION 1
```

相关声明：[ADXL355_DT_EXTERNAL_SYNC_NO_INTERPOLATION](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gab54040571fbb582ab22f60b878861db6)。

不带插值的外部同步（External Synchronization without Interpolation）。

<a id="r_ga0a8992af010d9c33e3874a3f88f8c5b9"></a>

```c
#define ADXL355_DT_EXTERNAL_SYNC_WITH_INTERPOLATION 2
```

相关声明：[ADXL355_DT_EXTERNAL_SYNC_WITH_INTERPOLATION](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga0a8992af010d9c33e3874a3f88f8c5b9)。

带插值的外部同步（External Synchronization with Interpolation）。


## 6.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P201_adxl355.h_源码浏览.md)
- [ADXL355_DT_ODR_4000](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gab60be1cb5989008043c4c768c4bb67a5)
- [ADXL355_DT_ODR_2000](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gaae25fe8c25742fb0358dff1c4aa95eef)
- [ADXL355_DT_ODR_1000](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga5aabb32d884ee322d8744408e507aee8)
- [ADXL355_DT_ODR_500](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga8c19b7c5d1a57c33a0ae3a5edc114768)
- [ADXL355_DT_ODR_250](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga71a30b4c271eabcf11ca501acfb05ff3)
- [ADXL355_DT_ODR_125](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gab411f93d442413e4ca21061115c1399c)
- [ADXL355_DT_ODR_62_5](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gad0bf8e8272a0db9be1452c21a122cd98)
- [ADXL355_DT_ODR_31_25](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga4f85d789f9b184ac8a96c75590a93719)
- [ADXL355_DT_ODR_15_625](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga61378797ab5e9e8d373908efce4df39e)
- [ADXL355_DT_ODR_7_813](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga92cb10f98315e05768a90fd9397eccff)
- [ADXL355_DT_ODR_3_906](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga0d6025b885cc0b21174b96f8fa2dced6)
- [ADXL355_DT_RANGE_2G](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gac0296485c3d583e12c9d4a73ee532f33)
- [ADXL355_DT_RANGE_4G](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gaff43fe8c86158d46b826df053a6fa530)
- [ADXL355_DT_RANGE_8G](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga083df135be18fe7bcdd1f6681d434197)
- [ADXL355_DT_HPF_OFF](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga15cb598fda2032fea4f74df2dd586c43)
- [ADXL355_DT_HPF_24_7e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga2bb6fc7a0f5db2d41d1b7ab41408e5cf)
- [ADXL355_DT_HPF_6_208e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gad88ed912cd272948bf6cc1d99786d190)
- [ADXL355_DT_HPF_1_5545e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga73f0b16ce376b02d42f0f93ff6ccc97c)
- [ADXL355_DT_HPF_0_3862e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga8eeaac80b071b9d0921e00d085cc0e0a)
- [ADXL355_DT_HPF_0_0954e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga34c4fe4b7bbea96d3f6153746dc6228c)
- [ADXL355_DT_HPF_0_0238e_4](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga665874864fa75fef549936a93ae61b52)
- [ADXL355_DT_EXTCLK_DISABLED](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga218ea74d36be97682a38b860b58b717f)
- [ADXL355_DT_EXTCLK_ENABLED](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gaa9bed643f472c8c4f9056465be1fe1c6)
- [ADXL355_DT_INTERNAL_SYNC](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gafb59af517b95dcd49521605624ccd0f2)
- [ADXL355_DT_EXTERNAL_SYNC_NO_INTERPOLATION](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#gab54040571fbb582ab22f60b878861db6)
- [ADXL355_DT_EXTERNAL_SYNC_WITH_INTERPOLATION](../api_flash_backend_topic_reference/P001_ADXL355 API主题.md#ga0a8992af010d9c33e3874a3f88f8c5b9)

<a id="header-details"></a>

---

[上一章](P005_zephyr__drivers__biometrics.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__interrupt_controller__intc_nxp_gint.h_文件参考.md)
