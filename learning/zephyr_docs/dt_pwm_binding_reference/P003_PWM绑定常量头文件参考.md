---
id: learning.zephyr-docs.dt-pwm-binding-reference.page-3
title: PWM绑定常量头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pwm_2pwm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_PWM绑定常量头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pwm_2pwm_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)选择PWM设备树访问或PWM、I2C绑定常量头文件，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="define-members-0"></a>

### PWM周期设置辅助宏（PWM Period Set Helpers）

PWM 说明符中的 `period` 参数单元必须以纳秒提供。

但在某些应用中，使用其他时间尺度更方便。

<a id="r_ga17f20d628bcc81d5023c39e4cdfad405"></a>

```c
#define PWM_NSEC(x)
```

相关声明：[PWM_NSEC](../hardware/P255_PWM公共接口.md#ga17f20d628bcc81d5023c39e4cdfad405)。

以纳秒（Nanoseconds）指定 PWM 周期。

<a id="r_ga368f28c8daaee25e546484bd908e675e"></a>

```c
#define PWM_USEC(x)
```

相关声明：[PWM_USEC](../hardware/P255_PWM公共接口.md#ga368f28c8daaee25e546484bd908e675e)。

以微秒（Microseconds）指定 PWM 周期。

<a id="r_ga1cccc226a23866dd2dcac9467ff3af0e"></a>

```c
#define PWM_MSEC(x)
```

相关声明：[PWM_MSEC](../hardware/P255_PWM公共接口.md#ga1cccc226a23866dd2dcac9467ff3af0e)。

以毫秒（Milliseconds）指定 PWM 周期。

<a id="r_ga4da4565d4dbded0efb640bd538cba3c2"></a>

```c
#define PWM_SEC(x)
```

相关声明：[PWM_SEC](../hardware/P255_PWM公共接口.md#ga4da4565d4dbded0efb640bd538cba3c2)。

以秒（Seconds）指定 PWM 周期。

<a id="r_ga4a5edbee48c4a5706cf75524aef2364a"></a>

```c
#define PWM_HZ(x)
```

相关声明：[PWM_HZ](../hardware/P255_PWM公共接口.md#ga4a5edbee48c4a5706cf75524aef2364a)。

以赫兹（Hertz）指定 PWM 频率。

<a id="r_gaf846cf23d31d14296e0cbc1f82a530f4"></a>

```c
#define PWM_KHZ(x)
```

相关声明：[PWM_KHZ](../hardware/P255_PWM公共接口.md#gaf846cf23d31d14296e0cbc1f82a530f4)。

以千赫兹（Kilohertz）指定 PWM 频率。

<a id="define-members-1"></a>

### PWM极性标志（PWM Polarity Flags）

`PWM_POLARITY_*` 标志与 `pwm_set_cycles()`、`pwm_set()` 或 `pwm_configure_capture()` 配合，用于指定 PWM 通道的极性（Polarity）。

这些标志位于 `pwm_flags_t` 的低 8 位。

<a id="r_ga2c706bbada711f383d7b42f09dace861"></a>

```c
#define PWM_POLARITY_NORMAL (0 << 0)
```

相关声明：[PWM_POLARITY_NORMAL](../hardware/P255_PWM公共接口.md#ga2c706bbada711f383d7b42f09dace861)。

PWM 引脚采用正常极性（Normal Polarity），脉冲为高电平有效（Active High）。

<a id="r_ga930c0ab50f81aeb571af9747947d7fae"></a>

```c
#define PWM_POLARITY_INVERTED (1 << 0)
```

相关声明：[PWM_POLARITY_INVERTED](../hardware/P255_PWM公共接口.md#ga930c0ab50f81aeb571af9747947d7fae)。

PWM 引脚采用反向极性（Inverted Polarity），脉冲为低电平有效（Active Low）。

## 3.2\_源码定位与版本边界

相对源码定位：[PWM设备树宏](../../../include/zephyr/devicetree/pwms.h)、[PWM绑定常量](../../../include/zephyr/dt-bindings/pwm/pwm.h)、[I2C绑定常量](../../../include/zephyr/dt-bindings/i2c/i2c.h)、[PWM公共绑定](../../../dts/bindings/pwm/pwm-controller.yaml)和[I2C公共绑定](../../../dts/bindings/i2c/i2c-controller.yaml)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：周期换算：PWM_NSEC原样返回参数，USEC／MSEC／SEC逐级乘1000UL；PWM_HZ通过1000000000UL除以频率生成纳秒周期，PWM_KHZ先把千赫兹换算为赫兹。因此频率辅助宏的结果仍是周期，不是频率值。常见整数常量输入会执行整数除法，不能保证无截断；零频率、乘法溢出和实际定时器分辨率均不由这些宏检查。

> 译注——源码核对：极性标志：正常极性（Normal Polarity）为高电平有效脉冲，反向极性（Inverted Polarity）为低电平有效脉冲；常量分别为0与1，内部PWM_POLARITY_MASK为0x1。原文所说低8位是标志布局说明，不表示该头文件定义了八种极性，也不表示所有驱动都支持所有标志。头文件引用运行时API只是说明使用位置，不会自行配置硬件。

> 译注——源码核对：版本边界：本批核对三份官方头文件及PWM、I2C控制器公共绑定并记录摘要；三个源码浏览页的非注释代码与读取的官方原始头文件一致。latest、滚动main与仓库参照版本不自动相同。仓库源码链接仅用于定位；本次没有生成设备树、构建固件或操作硬件。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的源码](P004_PWM绑定常量头文件源码.md)
- [PWM_NSEC](../hardware/P255_PWM公共接口.md#ga17f20d628bcc81d5023c39e4cdfad405)
- [PWM_USEC](../hardware/P255_PWM公共接口.md#ga368f28c8daaee25e546484bd908e675e)
- [PWM_MSEC](../hardware/P255_PWM公共接口.md#ga1cccc226a23866dd2dcac9467ff3af0e)
- [PWM_SEC](../hardware/P255_PWM公共接口.md#ga4da4565d4dbded0efb640bd538cba3c2)
- [PWM_HZ](../hardware/P255_PWM公共接口.md#ga4a5edbee48c4a5706cf75524aef2364a)
- [PWM_KHZ](../hardware/P255_PWM公共接口.md#gaf846cf23d31d14296e0cbc1f82a530f4)
- [pwm_set_cycles()](../hardware/P255_PWM公共接口.md#gaff280789f7b45fdefc354b3f841fe3ef)
- [pwm_set()](../hardware/P255_PWM公共接口.md#gadd9049c9a56cd9419736b3514e42dc01)
- [pwm_configure_capture()](../hardware/P255_PWM公共接口.md#ga9603146d7f9c2690c1e1983113d6c6bb)
- [pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)
- [PWM_POLARITY_NORMAL](../hardware/P255_PWM公共接口.md#ga2c706bbada711f383d7b42f09dace861)
- [PWM_POLARITY_INVERTED](../hardware/P255_PWM公共接口.md#ga930c0ab50f81aeb571af9747947d7fae)

---

[上一章](P002_PWM设备树头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_PWM绑定常量头文件源码.md)
