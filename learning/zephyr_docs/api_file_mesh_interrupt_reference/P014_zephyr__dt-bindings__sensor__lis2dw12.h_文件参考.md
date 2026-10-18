---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-14
title: zephyr__dt-bindings__sensor__lis2dw12.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lis2dw12_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_dt-bindings\_\_sensor\_\_lis2dw12.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lis2dw12_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LIS2DW12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST LIS2DW12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 电源模式（Power Modes）

设备树属性（Devicetree Property）`power-mode` 的取值。

<a id="r_ga0c03f55d1b6ebbf1d48e0c34d9122a74"></a>

```c
#define LIS2DW12_DT_LP_M1 0
```

相关声明：[LIS2DW12_DT_LP_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga0c03f55d1b6ebbf1d48e0c34d9122a74)。

低功耗模式（Low-power Mode）1，12 位。

<a id="r_gaeb6d34d3c11a1f3e7dc2cfe5f7405aae"></a>

```c
#define LIS2DW12_DT_LP_M2 1
```

相关声明：[LIS2DW12_DT_LP_M2](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaeb6d34d3c11a1f3e7dc2cfe5f7405aae)。

低功耗模式（Low-power Mode）2，14 位。

<a id="r_gab9ab746af6c8dfa384671ee313c7eea4"></a>

```c
#define LIS2DW12_DT_LP_M3 2
```

相关声明：[LIS2DW12_DT_LP_M3](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gab9ab746af6c8dfa384671ee313c7eea4)。

低功耗模式（Low-power Mode）3，14 位。

<a id="r_gada20bc2633adb3ae955c2f709d727154"></a>

```c
#define LIS2DW12_DT_LP_M4 3
```

相关声明：[LIS2DW12_DT_LP_M4](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gada20bc2633adb3ae955c2f709d727154)。

低功耗模式（Low-power Mode）4，14 位。

<a id="r_ga0307502b4dee186f1945636c713eee4d"></a>

```c
#define LIS2DW12_DT_HP_MODE 4
```

相关声明：[LIS2DW12_DT_HP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga0307502b4dee186f1945636c713eee4d)。

高性能模式（High-performance Mode），14 位。

<a id="define-members-1"></a>

### 滤波器带宽选项（Filter Bandwidth Options）

设备树属性（Devicetree Property）`bw-filt` 的取值。

<a id="r_ga88efe563d0f4d704773886d7670bea31"></a>

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_2 0
```

相关声明：[LIS2DW12_DT_FILTER_BW_ODR_DIV_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga88efe563d0f4d704773886d7670bea31)。

输出数据速率（ODR）除以 2。

<a id="r_ga4433ccc00389f58d30b9998b11915848"></a>

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_4 1
```

相关声明：[LIS2DW12_DT_FILTER_BW_ODR_DIV_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga4433ccc00389f58d30b9998b11915848)。

输出数据速率（ODR）除以 4。

<a id="r_gaad4197948abbd4587f6c9810f34e0c49"></a>

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_10 2
```

相关声明：[LIS2DW12_DT_FILTER_BW_ODR_DIV_10](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaad4197948abbd4587f6c9810f34e0c49)。

输出数据速率（ODR）除以 10。

<a id="r_ga9972d8b7618f39c9ddff273ecd80616a"></a>

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_20 3
```

相关声明：[LIS2DW12_DT_FILTER_BW_ODR_DIV_20](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga9972d8b7618f39c9ddff273ecd80616a)。

输出数据速率（ODR）除以 20。

<a id="define-members-2"></a>

### 敲击检测模式（Tap Detection Mode）

设备树属性（Devicetree Property）`tap-mode` 的取值。

<a id="r_ga71fc2ff7108bd85a86fd82c0ff002c18"></a>

```c
#define LIS2DW12_DT_SINGLE_TAP 0
```

相关声明：[LIS2DW12_DT_SINGLE_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga71fc2ff7108bd85a86fd82c0ff002c18)。

仅单击（Single-tap Only）。

<a id="r_ga4011203a9d243f9650cecab3d9ecf34d"></a>

```c
#define LIS2DW12_DT_SINGLE_DOUBLE_TAP 1
```

相关声明：[LIS2DW12_DT_SINGLE_DOUBLE_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga4011203a9d243f9650cecab3d9ecf34d)。

单击与双击（Single and Double Tap）。

<a id="define-members-3"></a>

### 自由落体阈值选项（Free-fall Threshold Options）

设备树属性（Devicetree Property）`ff-threshold` 的取值。

<a id="r_gac0420687b2a5ef0b886534b183d9b2f7"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_156_mg 0
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_156_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gac0420687b2a5ef0b886534b183d9b2f7)。

156 mg（千分之一标准重力加速度）。

<a id="r_ga6afc0cf0328630c3bcdaf4cc579d8988"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_219_mg 1
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_219_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga6afc0cf0328630c3bcdaf4cc579d8988)。

219 mg（千分之一标准重力加速度）。

<a id="r_ga25b0e004ef448952083e417b0c77f97d"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_250_mg 2
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_250_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga25b0e004ef448952083e417b0c77f97d)。

250 mg（千分之一标准重力加速度）。

<a id="r_ga5ab3d56ad2ab84179316f3706780d716"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_312_mg 3
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_312_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga5ab3d56ad2ab84179316f3706780d716)。

312 mg（千分之一标准重力加速度）。

<a id="r_ga429524e40340eb36610b7c0b4a449298"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_344_mg 4
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_344_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga429524e40340eb36610b7c0b4a449298)。

344 mg（千分之一标准重力加速度）。

<a id="r_ga9a7a1520051a5b6107e6e0adbfb1d837"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_406_mg 5
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_406_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga9a7a1520051a5b6107e6e0adbfb1d837)。

406 mg（千分之一标准重力加速度）。

<a id="r_gac336d6955333fc41ce21b9d68dfde4e5"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_469_mg 6
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_469_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gac336d6955333fc41ce21b9d68dfde4e5)。

469 mg（千分之一标准重力加速度）。

<a id="r_ga7de449940954836ff3c48ef192662760"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_500_mg 7
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_500_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga7de449940954836ff3c48ef192662760)。

500 mg（千分之一标准重力加速度）。

<a id="define-members-4"></a>

### 唤醒持续时间选项（Wake-up Duration Options）

设备树属性（Devicetree Property）`wakeup-duration` 的取值。

<a id="r_ga1bcffaa1b8439f626164b736be17f9db"></a>

```c
#define LIS2DW12_DT_WAKEUP_1_ODR 0
```

相关声明：[LIS2DW12_DT_WAKEUP_1_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga1bcffaa1b8439f626164b736be17f9db)。

1 个输出数据速率周期（ODR Period）。

<a id="r_ga53457e3a0d24bf3599ff779f3a559fb4"></a>

```c
#define LIS2DW12_DT_WAKEUP_2_ODR 1
```

相关声明：[LIS2DW12_DT_WAKEUP_2_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga53457e3a0d24bf3599ff779f3a559fb4)。

2 个输出数据速率周期（ODR Period）。

<a id="r_ga580dd3e03a377fce36db7916c254b52a"></a>

```c
#define LIS2DW12_DT_WAKEUP_3_ODR 2
```

相关声明：[LIS2DW12_DT_WAKEUP_3_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga580dd3e03a377fce36db7916c254b52a)。

3 个输出数据速率周期（ODR Period）。

<a id="r_gaae58921652443e8f7757b38ade589c49"></a>

```c
#define LIS2DW12_DT_WAKEUP_4_ODR 3
```

相关声明：[LIS2DW12_DT_WAKEUP_4_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaae58921652443e8f7757b38ade589c49)。

4 个输出数据速率周期（ODR Period）。

<a id="define-members-5"></a>

### 休眠持续时间选项（Sleep Duration Options）

设备树属性（Devicetree Property）`sleep-duration` 的取值。

<a id="r_gaa9df8cef65e33e117a8de9eb2df745c3"></a>

```c
#define LIS2DW12_DT_SLEEP_0_ODR 0
```

相关声明：[LIS2DW12_DT_SLEEP_0_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaa9df8cef65e33e117a8de9eb2df745c3)。

0 个输出数据速率周期（ODR Period）。

<a id="r_gaf43f42617789c1482e1ddf1d9abd7c3d"></a>

```c
#define LIS2DW12_DT_SLEEP_1_ODR 1
```

相关声明：[LIS2DW12_DT_SLEEP_1_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaf43f42617789c1482e1ddf1d9abd7c3d)。

1 个输出数据速率周期（ODR Period）。

<a id="r_ga6c76600bf9baff0483d5865ba98aa75e"></a>

```c
#define LIS2DW12_DT_SLEEP_2_ODR 2
```

相关声明：[LIS2DW12_DT_SLEEP_2_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga6c76600bf9baff0483d5865ba98aa75e)。

2 个输出数据速率周期（ODR Period）。

<a id="r_gaf294baab225caba1e4931abfee9660b8"></a>

```c
#define LIS2DW12_DT_SLEEP_3_ODR 3
```

相关声明：[LIS2DW12_DT_SLEEP_3_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaf294baab225caba1e4931abfee9660b8)。

3 个输出数据速率周期（ODR Period）。

<a id="r_gac45de707e5c1ee485b5cdd95ce3332af"></a>

```c
#define LIS2DW12_DT_SLEEP_4_ODR 4
```

相关声明：[LIS2DW12_DT_SLEEP_4_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gac45de707e5c1ee485b5cdd95ce3332af)。

4 个输出数据速率周期（ODR Period）。

<a id="r_ga904ec47239d01ac05218bee5fa2f4235"></a>

```c
#define LIS2DW12_DT_SLEEP_5_ODR 5
```

相关声明：[LIS2DW12_DT_SLEEP_5_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga904ec47239d01ac05218bee5fa2f4235)。

5 个输出数据速率周期（ODR Period）。

<a id="r_ga552a71243df2cfe6dcc6f9ca5a4208c9"></a>

```c
#define LIS2DW12_DT_SLEEP_6_ODR 6
```

相关声明：[LIS2DW12_DT_SLEEP_6_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga552a71243df2cfe6dcc6f9ca5a4208c9)。

6 个输出数据速率周期（ODR Period）。

<a id="r_ga72ced204873bfce192b6bcfc9d823ffc"></a>

```c
#define LIS2DW12_DT_SLEEP_7_ODR 7
```

相关声明：[LIS2DW12_DT_SLEEP_7_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga72ced204873bfce192b6bcfc9d823ffc)。

7 个输出数据速率周期（ODR Period）。

<a id="r_ga9078b4d1fa77dd53871ddbc7715b3f0c"></a>

```c
#define LIS2DW12_DT_SLEEP_8_ODR 8
```

相关声明：[LIS2DW12_DT_SLEEP_8_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga9078b4d1fa77dd53871ddbc7715b3f0c)。

8 个输出数据速率周期（ODR Period）。

<a id="r_ga979e47f3dda9c72b92d87bb3fc5b3e4f"></a>

```c
#define LIS2DW12_DT_SLEEP_9_ODR 9
```

相关声明：[LIS2DW12_DT_SLEEP_9_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga979e47f3dda9c72b92d87bb3fc5b3e4f)。

9 个输出数据速率周期（ODR Period）。

<a id="r_ga15982beb9fce8268a056fb2f088f6724"></a>

```c
#define LIS2DW12_DT_SLEEP_10_ODR 10
```

相关声明：[LIS2DW12_DT_SLEEP_10_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga15982beb9fce8268a056fb2f088f6724)。

10 个输出数据速率周期（ODR Period）。

<a id="r_gad3546f54d5eee5d7d9cb9318a6104a9c"></a>

```c
#define LIS2DW12_DT_SLEEP_11_ODR 11
```

相关声明：[LIS2DW12_DT_SLEEP_11_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gad3546f54d5eee5d7d9cb9318a6104a9c)。

11 个输出数据速率周期（ODR Period）。

<a id="r_ga97614b907ca69fd13f0e8a9b61e15904"></a>

```c
#define LIS2DW12_DT_SLEEP_12_ODR 12
```

相关声明：[LIS2DW12_DT_SLEEP_12_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga97614b907ca69fd13f0e8a9b61e15904)。

12 个输出数据速率周期（ODR Period）。

<a id="r_gabff45bcd009134ee4da471e9e915584a"></a>

```c
#define LIS2DW12_DT_SLEEP_13_ODR 13
```

相关声明：[LIS2DW12_DT_SLEEP_13_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gabff45bcd009134ee4da471e9e915584a)。

13 个输出数据速率周期（ODR Period）。

<a id="r_ga8ba46d92426bf168d6b9da5acee6668f"></a>

```c
#define LIS2DW12_DT_SLEEP_14_ODR 14
```

相关声明：[LIS2DW12_DT_SLEEP_14_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga8ba46d92426bf168d6b9da5acee6668f)。

14 个输出数据速率周期（ODR Period）。

<a id="r_ga39ddac85ed26346de4272157ce2533a8"></a>

```c
#define LIS2DW12_DT_SLEEP_15_ODR 15
```

相关声明：[LIS2DW12_DT_SLEEP_15_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga39ddac85ed26346de4272157ce2533a8)。

15 个输出数据速率周期（ODR Period）。


## 14.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P445_lis2dw12.h_源码浏览.md)
- [LIS2DW12_DT_LP_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga0c03f55d1b6ebbf1d48e0c34d9122a74)
- [LIS2DW12_DT_LP_M2](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaeb6d34d3c11a1f3e7dc2cfe5f7405aae)
- [LIS2DW12_DT_LP_M3](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gab9ab746af6c8dfa384671ee313c7eea4)
- [LIS2DW12_DT_LP_M4](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gada20bc2633adb3ae955c2f709d727154)
- [LIS2DW12_DT_HP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga0307502b4dee186f1945636c713eee4d)
- [LIS2DW12_DT_FILTER_BW_ODR_DIV_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga88efe563d0f4d704773886d7670bea31)
- [LIS2DW12_DT_FILTER_BW_ODR_DIV_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga4433ccc00389f58d30b9998b11915848)
- [LIS2DW12_DT_FILTER_BW_ODR_DIV_10](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaad4197948abbd4587f6c9810f34e0c49)
- [LIS2DW12_DT_FILTER_BW_ODR_DIV_20](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga9972d8b7618f39c9ddff273ecd80616a)
- [LIS2DW12_DT_SINGLE_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga71fc2ff7108bd85a86fd82c0ff002c18)
- [LIS2DW12_DT_SINGLE_DOUBLE_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga4011203a9d243f9650cecab3d9ecf34d)
- [LIS2DW12_DT_FF_THRESHOLD_156_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gac0420687b2a5ef0b886534b183d9b2f7)
- [LIS2DW12_DT_FF_THRESHOLD_219_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga6afc0cf0328630c3bcdaf4cc579d8988)
- [LIS2DW12_DT_FF_THRESHOLD_250_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga25b0e004ef448952083e417b0c77f97d)
- [LIS2DW12_DT_FF_THRESHOLD_312_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga5ab3d56ad2ab84179316f3706780d716)
- [LIS2DW12_DT_FF_THRESHOLD_344_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga429524e40340eb36610b7c0b4a449298)
- [LIS2DW12_DT_FF_THRESHOLD_406_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga9a7a1520051a5b6107e6e0adbfb1d837)
- [LIS2DW12_DT_FF_THRESHOLD_469_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gac336d6955333fc41ce21b9d68dfde4e5)
- [LIS2DW12_DT_FF_THRESHOLD_500_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga7de449940954836ff3c48ef192662760)
- [LIS2DW12_DT_WAKEUP_1_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga1bcffaa1b8439f626164b736be17f9db)
- [LIS2DW12_DT_WAKEUP_2_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga53457e3a0d24bf3599ff779f3a559fb4)
- [LIS2DW12_DT_WAKEUP_3_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga580dd3e03a377fce36db7916c254b52a)
- [LIS2DW12_DT_WAKEUP_4_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaae58921652443e8f7757b38ade589c49)
- [LIS2DW12_DT_SLEEP_0_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaa9df8cef65e33e117a8de9eb2df745c3)
- [LIS2DW12_DT_SLEEP_1_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaf43f42617789c1482e1ddf1d9abd7c3d)
- [LIS2DW12_DT_SLEEP_2_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga6c76600bf9baff0483d5865ba98aa75e)
- [LIS2DW12_DT_SLEEP_3_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gaf294baab225caba1e4931abfee9660b8)
- [LIS2DW12_DT_SLEEP_4_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gac45de707e5c1ee485b5cdd95ce3332af)
- [LIS2DW12_DT_SLEEP_5_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga904ec47239d01ac05218bee5fa2f4235)
- [LIS2DW12_DT_SLEEP_6_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga552a71243df2cfe6dcc6f9ca5a4208c9)
- [LIS2DW12_DT_SLEEP_7_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga72ced204873bfce192b6bcfc9d823ffc)
- [LIS2DW12_DT_SLEEP_8_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga9078b4d1fa77dd53871ddbc7715b3f0c)
- [LIS2DW12_DT_SLEEP_9_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga979e47f3dda9c72b92d87bb3fc5b3e4f)
- [LIS2DW12_DT_SLEEP_10_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga15982beb9fce8268a056fb2f088f6724)
- [LIS2DW12_DT_SLEEP_11_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gad3546f54d5eee5d7d9cb9318a6104a9c)
- [LIS2DW12_DT_SLEEP_12_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga97614b907ca69fd13f0e8a9b61e15904)
- [LIS2DW12_DT_SLEEP_13_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#gabff45bcd009134ee4da471e9e915584a)
- [LIS2DW12_DT_SLEEP_14_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga8ba46d92426bf168d6b9da5acee6668f)
- [LIS2DW12_DT_SLEEP_15_ODR](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html#ga39ddac85ed26346de4272157ce2533a8)

<a id="header-details"></a>

---

[上一章](P013_zephyr__dt-bindings__sensor__ina230.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__dt-bindings__sensor__lsm6dso16is.h_文件参考.md)
