---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-7
title: zephyr__drivers__pwm__max31790.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwm_2max31790_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_pwm\_\_max31790.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pwm_2max31790_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAX31790脉宽调制（PWM）驱动的头文件。

查看此文件的源码。

<a id="details"></a>

MAX31790脉宽调制（PWM）驱动的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_ga2b7c056ec08e8add71a422d9cc610c98"></a>

```c
#define PWM_MAX31790_FLAG_SPIN_UP (1 << PWM_MAX31790_FLAG_SPIN_UP_POS)
```

相关声明：[PWM_MAX31790_FLAG_SPIN_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga2b7c056ec08e8add71a422d9cc610c98)。

启用风扇启动加速（Spin Up）。

<a id="define-members-0"></a>

### MAX31790 自定义 PWM 标志（Custom PWM Flags）

这些标志可与 PWM API 一起使用，放在 `pwm_flags_t` 的高 8 位中。它们允许使用每分钟转数模式（RPM Mode），使 MAX31790 测量风扇实际转速，并自动控制至所需转速。

<a id="r_ga49d4bcb7f5c77aa1489e54957f32433a"></a>

```c
#define PWM_MAX31790_FLAG_RPM_MODE (1 << PWM_MAX31790_FLAG_RPM_MODE_POS)
```

相关声明：[PWM_MAX31790_FLAG_RPM_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga49d4bcb7f5c77aa1489e54957f32433a)。

每分钟转数模式（RPM Mode）。

<a id="define-members-1"></a>

### 风扇转速范围（Speed Range of Fan）

表示转速检测（TACH）计数的倍乘因子，应根据风扇的标称每分钟转数（Nominal RPM）选择。

如何选择适当值的详细表格可在 MAX31790 数据手册（Datasheet）中找到。

<a id="r_ga98b4a27f06adbc3f7011f8e22c29d28f"></a>

```c
#define PWM_MAX31790_FLAG_SPEED_RANGE_1 (0 << PWM_MAX31790_FLAG_SPEED_RANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_SPEED_RANGE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga98b4a27f06adbc3f7011f8e22c29d28f)。

1 个转速检测周期（TACH Period），最适合低速风扇。

<a id="r_ga98f86024db6a17a04def84bafd87f5b9"></a>

```c
#define PWM_MAX31790_FLAG_SPEED_RANGE_2 (1 << PWM_MAX31790_FLAG_SPEED_RANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_SPEED_RANGE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga98f86024db6a17a04def84bafd87f5b9)。

2 个转速检测周期（TACH Periods）。

<a id="r_ga77105f041235cc0189c43ddece06f220"></a>

```c
#define PWM_MAX31790_FLAG_SPEED_RANGE_4 (2 << PWM_MAX31790_FLAG_SPEED_RANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_SPEED_RANGE_4](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga77105f041235cc0189c43ddece06f220)。

4 个转速检测周期（TACH Periods）。

<a id="r_ga0fb4a86a4cd1ed5582f025d35f82c148"></a>

```c
#define PWM_MAX31790_FLAG_SPEED_RANGE_8 (3 << PWM_MAX31790_FLAG_SPEED_RANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_SPEED_RANGE_8](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga0fb4a86a4cd1ed5582f025d35f82c148)。

8 个转速检测周期（TACH Periods）。

<a id="r_ga28bc19a81c2ea6b910a84cd622bcea05"></a>

```c
#define PWM_MAX31790_FLAG_SPEED_RANGE_16 (4 << PWM_MAX31790_FLAG_SPEED_RANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_SPEED_RANGE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga28bc19a81c2ea6b910a84cd622bcea05)。

16 个转速检测周期（TACH Periods）。

<a id="r_ga79d0de4ba831f2b1df823550bc813578"></a>

```c
#define PWM_MAX31790_FLAG_SPEED_RANGE_32 (5 << PWM_MAX31790_FLAG_SPEED_RANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_SPEED_RANGE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga79d0de4ba831f2b1df823550bc813578)。

32 个转速检测周期（TACH Periods），最适合高速风扇。

<a id="define-members-2"></a>

### PWM 变化速率（Rate of Change）

配置风扇的内部控制回路（Internal Control Loop）。

这些值的详细信息可在 MAX31790 数据手册（Datasheet）中找到。

<a id="r_ga9030b924200302e3b03295d540e71df1"></a>

```c
#define PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_0 (0 << PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_0](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga9030b924200302e3b03295d540e71df1)。

最快变化速率（Fastest Rate of Change），PWM 模式中每步 0 ms。

<a id="r_gad0cf273c9627e5491438ce4827184e2d"></a>

```c
#define PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_1 (1 << PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#gad0cf273c9627e5491438ce4827184e2d)。

快速变化速率（Fast Rate of Change），每步 1.953125 ms。

<a id="r_gab49c21cba041885bc5e2c67f5decf994"></a>

```c
#define PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_2 (2 << PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#gab49c21cba041885bc5e2c67f5decf994)。

中快速变化速率（Medium-fast Rate of Change），每步 3.90625 ms。

<a id="r_ga4e3772d1a9d1a4b79b66fa016d681106"></a>

```c
#define PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_3 (3 << PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga4e3772d1a9d1a4b79b66fa016d681106)。

中等变化速率（Medium Rate of Change），每步 7.8125 ms。

<a id="r_ga04e3d5b3adcefb3152090707a1affcf0"></a>

```c
#define PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_4 (4 << PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_4](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga04e3d5b3adcefb3152090707a1affcf0)。

中慢速变化速率（Medium-slow Rate of Change），每步 15.625 ms。

<a id="r_ga8bd18ed522d33db5d7a3b0f02b8b9e39"></a>

```c
#define PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_5 (5 << PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_5](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga8bd18ed522d33db5d7a3b0f02b8b9e39)。

慢速变化速率（Slow Rate of Change），每步 31.25 ms。

<a id="r_ga83447dea9e822dae8f9838ace497fc55"></a>

```c
#define PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_6 (6 << PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_6](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga83447dea9e822dae8f9838ace497fc55)。

很慢的变化速率（Very Slow Rate of Change），每步 62.5 ms。

<a id="r_ga40371ed8f761964573be18c33db2c759"></a>

```c
#define PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_7 (7 << PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_POS)
```

相关声明：[PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_7](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga40371ed8f761964573be18c33db2c759)。

极慢的变化速率（Ultra-slow Rate of Change），每步 125 ms。


## 7.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P683_max31790.h_源码浏览.md)
- [PWM_MAX31790_FLAG_SPIN_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga2b7c056ec08e8add71a422d9cc610c98)
- [pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)
- [PWM_MAX31790_FLAG_RPM_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga49d4bcb7f5c77aa1489e54957f32433a)
- [PWM_MAX31790_FLAG_SPEED_RANGE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga98b4a27f06adbc3f7011f8e22c29d28f)
- [PWM_MAX31790_FLAG_SPEED_RANGE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga98f86024db6a17a04def84bafd87f5b9)
- [PWM_MAX31790_FLAG_SPEED_RANGE_4](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga77105f041235cc0189c43ddece06f220)
- [PWM_MAX31790_FLAG_SPEED_RANGE_8](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga0fb4a86a4cd1ed5582f025d35f82c148)
- [PWM_MAX31790_FLAG_SPEED_RANGE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga28bc19a81c2ea6b910a84cd622bcea05)
- [PWM_MAX31790_FLAG_SPEED_RANGE_32](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga79d0de4ba831f2b1df823550bc813578)
- [PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_0](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga9030b924200302e3b03295d540e71df1)
- [PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#gad0cf273c9627e5491438ce4827184e2d)
- [PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#gab49c21cba041885bc5e2c67f5decf994)
- [PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga4e3772d1a9d1a4b79b66fa016d681106)
- [PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_4](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga04e3d5b3adcefb3152090707a1affcf0)
- [PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_5](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga8bd18ed522d33db5d7a3b0f02b8b9e39)
- [PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_6](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga83447dea9e822dae8f9838ace497fc55)
- [PWM_MAX31790_FLAG_PWM_RATE_OF_CHANGE_7](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max31790__interface.html#ga40371ed8f761964573be18c33db2c759)

<a id="header-details"></a>

---

[上一章](P006_zephyr__drivers__sensor__mcux_lpcmp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__stepper__stepper_ctrl.h_文件参考.md)
