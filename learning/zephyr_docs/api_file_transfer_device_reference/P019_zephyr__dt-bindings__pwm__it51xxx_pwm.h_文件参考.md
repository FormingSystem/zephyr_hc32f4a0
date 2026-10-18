---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-19
title: zephyr__dt-bindings__pwm__it51xxx_pwm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__pwm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_dt-bindings\_\_pwm\_\_it51xxx\_pwm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__pwm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.1\_宏定义（Macros）

<a id="r_a98aaba2e733ce20cd59eeadc33663965"></a>

```c
#define PWM_PRESCALER_C4 1
```

相关声明：[PWM_PRESCALER_C4](#a98aaba2e733ce20cd59eeadc33663965)。

<a id="r_a15fa229af614107078c43d887c985520"></a>

```c
#define PWM_PRESCALER_C6 2
```

相关声明：[PWM_PRESCALER_C6](#a15fa229af614107078c43d887c985520)。

<a id="r_a784a4aa1339416ac435615ec74742ca9"></a>

```c
#define PWM_PRESCALER_C7 3
```

相关声明：[PWM_PRESCALER_C7](#a784a4aa1339416ac435615ec74742ca9)。

<a id="r_a9b43cbcd1d148602c21fa850bebefbdc"></a>

```c
#define PWM_CHANNEL_0 0
```

相关声明：[PWM_CHANNEL_0](#a9b43cbcd1d148602c21fa850bebefbdc)。

<a id="r_a1da821e350e2e57c46bb73d60256e537"></a>

```c
#define PWM_CHANNEL_1 1
```

相关声明：[PWM_CHANNEL_1](#a1da821e350e2e57c46bb73d60256e537)。

<a id="r_a90a3351d5ed724d6970eb50970e12df3"></a>

```c
#define PWM_CHANNEL_2 2
```

相关声明：[PWM_CHANNEL_2](#a90a3351d5ed724d6970eb50970e12df3)。

<a id="r_ad7ecaad6ade54bca69bac60bb39b3d23"></a>

```c
#define PWM_CHANNEL_3 3
```

相关声明：[PWM_CHANNEL_3](#ad7ecaad6ade54bca69bac60bb39b3d23)。

<a id="r_a7695e0811561c98657a24fb828b7dd80"></a>

```c
#define PWM_CHANNEL_4 4
```

相关声明：[PWM_CHANNEL_4](#a7695e0811561c98657a24fb828b7dd80)。

<a id="r_a45c3365cad7dbd63b7db5881a287ca78"></a>

```c
#define PWM_CHANNEL_5 5
```

相关声明：[PWM_CHANNEL_5](#a45c3365cad7dbd63b7db5881a287ca78)。

<a id="r_abbce1e1eeae1747443dcea1259f99384"></a>

```c
#define PWM_CHANNEL_6 6
```

相关声明：[PWM_CHANNEL_6](#abbce1e1eeae1747443dcea1259f99384)。

<a id="r_aefd382e2874b5ecac051e5f0129199b0"></a>

```c
#define PWM_CHANNEL_7 7
```

相关声明：[PWM_CHANNEL_7](#aefd382e2874b5ecac051e5f0129199b0)。

<a id="define-members-0"></a>

### PWM 调光占空比值（Dimming Duty Cycle Values）

<a id="r_a807fcbd32a6fdd783133b54a9d339fba"></a>

```c
#define PWM_DIMMING_DC_40H 0
```

相关声明：[PWM_DIMMING_DC_40H](#a807fcbd32a6fdd783133b54a9d339fba)。

PWM 调光（Dimming）的最大占空比（Duty Cycle）为 25%。

<a id="r_a3d5f83d2a6bbb03caf09d0d0a70a2a0f"></a>

```c
#define PWM_DIMMING_DC_80H 1
```

相关声明：[PWM_DIMMING_DC_80H](#a3d5f83d2a6bbb03caf09d0d0a70a2a0f)。

PWM 调光（Dimming）的最大占空比（Duty Cycle）为 50%。

<a id="r_af34787cfc3cc7000520feb54011b9c7e"></a>

```c
#define PWM_DIMMING_DC_C0H 2
```

相关声明：[PWM_DIMMING_DC_C0H](#af34787cfc3cc7000520feb54011b9c7e)。

PWM 调光（Dimming）的最大占空比（Duty Cycle）为 75%。

<a id="r_ad1e43af52ec0d2ce671baeb15ac15dfd"></a>

```c
#define PWM_DIMMING_DC_FFH 3
```

相关声明：[PWM_DIMMING_DC_FFH](#ad1e43af52ec0d2ce671baeb15ac15dfd)。

PWM 调光（Dimming）的最大占空比（Duty Cycle）为 100%。

<a id="define-members-1"></a>

### PWM 调光占空比增减步长（Dimming Duty Increase/Decrease Step Values）

<a id="r_a13ed73b14adc660c05b76358de48eb91"></a>

```c
#define PWM_DIMMING_DC_STEP_1H 0
```

相关声明：[PWM_DIMMING_DC_STEP_1H](#a13ed73b14adc660c05b76358de48eb91)。

PWM 调光占空比（Dimming Duty）变化步长为 `1`。

<a id="r_a72c3214f1983fb526b4c7de7686c309a"></a>

```c
#define PWM_DIMMING_DC_STEP_2H 1
```

相关声明：[PWM_DIMMING_DC_STEP_2H](#a72c3214f1983fb526b4c7de7686c309a)。

PWM 调光占空比（Dimming Duty）变化步长为 `2`。

<a id="r_a9345ad68ed9a175606c9292dbd834e60"></a>

```c
#define PWM_DIMMING_DC_STEP_4H 2
```

相关声明：[PWM_DIMMING_DC_STEP_4H](#a9345ad68ed9a175606c9292dbd834e60)。

PWM 调光占空比（Dimming Duty）变化步长为 `4`。

<a id="r_aac9d28a7de97d7c891f33cd1e9537d4e"></a>

```c
#define PWM_DIMMING_DC_STEP_8H 3
```

相关声明：[PWM_DIMMING_DC_STEP_8H](#aac9d28a7de97d7c891f33cd1e9537d4e)。

PWM 调光占空比（Dimming Duty）变化步长为 `8`。

<a id="define-members-2"></a>

<a id="r_a7250e9763907d112155feca0f89f107f"></a>

```c
#define PWM_IT51XXX_OPEN_DRAIN BIT(8)
```

相关声明：[PWM_IT51XXX_OPEN_DRAIN](#a7250e9763907d112155feca0f89f107f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

提供保存 PWM 配置标志的类型。

<a id="r_adebae3783d02bd0839e1e861f41cf4e1"></a>

```c
#define PWM_IT51XXX_DIMMING_MODE BIT(9)
```

相关声明：[PWM_IT51XXX_DIMMING_MODE](#adebae3783d02bd0839e1e861f41cf4e1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启用 PWM 调光模式（Dimming Mode）的标志。

## 19.2\_详细说明（Detailed Documentation）

<a id="a9b43cbcd1d148602c21fa850bebefbdc"></a>

### `PWM_CHANNEL_0`

```c
#define PWM_CHANNEL_0 0
```

<a id="a1da821e350e2e57c46bb73d60256e537"></a>

### `PWM_CHANNEL_1`

```c
#define PWM_CHANNEL_1 1
```

<a id="a90a3351d5ed724d6970eb50970e12df3"></a>

### `PWM_CHANNEL_2`

```c
#define PWM_CHANNEL_2 2
```

<a id="ad7ecaad6ade54bca69bac60bb39b3d23"></a>

### `PWM_CHANNEL_3`

```c
#define PWM_CHANNEL_3 3
```

<a id="a7695e0811561c98657a24fb828b7dd80"></a>

### `PWM_CHANNEL_4`

```c
#define PWM_CHANNEL_4 4
```

<a id="a45c3365cad7dbd63b7db5881a287ca78"></a>

### `PWM_CHANNEL_5`

```c
#define PWM_CHANNEL_5 5
```

<a id="abbce1e1eeae1747443dcea1259f99384"></a>

### `PWM_CHANNEL_6`

```c
#define PWM_CHANNEL_6 6
```

<a id="aefd382e2874b5ecac051e5f0129199b0"></a>

### `PWM_CHANNEL_7`

```c
#define PWM_CHANNEL_7 7
```

<a id="a807fcbd32a6fdd783133b54a9d339fba"></a>

### `PWM_DIMMING_DC_40H`

```c
#define PWM_DIMMING_DC_40H 0
```

PWM 调光（Dimming）的最大占空比（Duty Cycle）为 25%。

<a id="a3d5f83d2a6bbb03caf09d0d0a70a2a0f"></a>

### `PWM_DIMMING_DC_80H`

```c
#define PWM_DIMMING_DC_80H 1
```

PWM 调光（Dimming）的最大占空比（Duty Cycle）为 50%。

<a id="af34787cfc3cc7000520feb54011b9c7e"></a>

### `PWM_DIMMING_DC_C0H`

```c
#define PWM_DIMMING_DC_C0H 2
```

PWM 调光（Dimming）的最大占空比（Duty Cycle）为 75%。

<a id="ad1e43af52ec0d2ce671baeb15ac15dfd"></a>

### `PWM_DIMMING_DC_FFH`

```c
#define PWM_DIMMING_DC_FFH 3
```

PWM 调光（Dimming）的最大占空比（Duty Cycle）为 100%。

<a id="a13ed73b14adc660c05b76358de48eb91"></a>

### `PWM_DIMMING_DC_STEP_1H`

```c
#define PWM_DIMMING_DC_STEP_1H 0
```

PWM 调光占空比（Dimming Duty）变化步长为 `1`。

<a id="a72c3214f1983fb526b4c7de7686c309a"></a>

### `PWM_DIMMING_DC_STEP_2H`

```c
#define PWM_DIMMING_DC_STEP_2H 1
```

PWM 调光占空比（Dimming Duty）变化步长为 `2`。

<a id="a9345ad68ed9a175606c9292dbd834e60"></a>

### `PWM_DIMMING_DC_STEP_4H`

```c
#define PWM_DIMMING_DC_STEP_4H 2
```

PWM 调光占空比（Dimming Duty）变化步长为 `4`。

<a id="aac9d28a7de97d7c891f33cd1e9537d4e"></a>

### `PWM_DIMMING_DC_STEP_8H`

```c
#define PWM_DIMMING_DC_STEP_8H 3
```

PWM 调光占空比（Dimming Duty）变化步长为 `8`。

<a id="adebae3783d02bd0839e1e861f41cf4e1"></a>

### `PWM_IT51XXX_DIMMING_MODE`

```c
#define PWM_IT51XXX_DIMMING_MODE BIT(9)
```

启用 PWM 调光模式（Dimming Mode）的标志。

<a id="a7250e9763907d112155feca0f89f107f"></a>

### `PWM_IT51XXX_OPEN_DRAIN`

```c
#define PWM_IT51XXX_OPEN_DRAIN BIT(8)
```

提供保存 PWM 配置标志的类型。

高 8 位保留给 SoC 专用标志（SoC-specific Flags）。输出开漏标志（Output Open-drain Flag）位于 `[8]`；输出调光模式标志（Output Dimming Mode Flag）位于 `[9]`；PWM 开漏标志（Open Drain Flag）。

<a id="a98aaba2e733ce20cd59eeadc33663965"></a>

### `PWM_PRESCALER_C4`

```c
#define PWM_PRESCALER_C4 1
```

<a id="a15fa229af614107078c43d887c985520"></a>

### `PWM_PRESCALER_C6`

```c
#define PWM_PRESCALER_C6 2
```

<a id="a784a4aa1339416ac435615ec74742ca9"></a>

### `PWM_PRESCALER_C7`

```c
#define PWM_PRESCALER_C7 3
```


## 19.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P043_it51xxx_pwm.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P018_zephyr__dt-bindings__interrupt-controller__intel-ioapic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__dt-bindings__clock__kinetis_sim.h_文件参考.md)
