---
id: learning.zephyr-docs.analog_reference.analogheader-3
title: MCUX模拟比较器扩展头文件参考
kind: reference
status: maintained
domains: [zephyr, analog_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/comparator_2mcux__acmp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第3章\_MCUX模拟比较器扩展头文件参考

原文：[comparator_2mcux__acmp_8h](https://docs.zephyrproject.org/latest/doxygen/html/comparator_2mcux__acmp_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/comparator/mcux_acmp.h`为MCUX模拟比较器（Analog Comparator，ACMP）提供配置扩展。文件包含公共比较器（Comparator）头文件：

```c
#include <zephyr/drivers/comparator.h>
```

原参考页列出五个结构体、八个枚举和六个函数，多数条目没有附加说明。以下中文释义依据标识符；离散模式（Discrete Mode，DM）的名称与[对应设备树绑定](../hardware/P745_NXPKinetis模拟比较器绑定.md)中的`discrete-mode-*`配置相对应，属于交叉阅读说明。

## 3.1\_配置结构体入口

五种配置分别用于工作模式、输入选择、滤波器、数模转换器（Digital-to-Analog Converter，DAC）和离散模式。

| 结构体 | 对应字段说明 |
| --- | --- |
| `comp_mcux_acmp_mode_config` | [工作模式配置](P013_MCUX比较器工作模式配置结构.md) |
| `comp_mcux_acmp_input_config` | [输入配置](P012_MCUX比较器输入配置结构.md) |
| `comp_mcux_acmp_filter_config` | [滤波配置](P011_MCUX比较器滤波配置结构.md) |
| `comp_mcux_acmp_dac_config` | [DAC配置](P009_MCUX比较器DAC配置结构.md) |
| `comp_mcux_acmp_dm_config` | [DM配置](P010_MCUX比较器DM模式配置结构.md) |

## 3.2\_全部枚举

每个枚举的首项均显式赋值为0，其余项保持原顺序递增。选项名称中的数字不等同于枚举的整数编码。

**偏置模式（Offset Mode）**：`comp_mcux_acmp_offset_mode`。两种级别（Level）为LEVEL0和LEVEL1。

```c
enum comp_mcux_acmp_offset_mode {
        COMP_MCUX_ACMP_OFFSET_MODE_LEVEL0 = 0,
        COMP_MCUX_ACMP_OFFSET_MODE_LEVEL1,
};
```

**迟滞模式（Hysteresis Mode）**：`comp_mcux_acmp_hysteresis_mode`。四种级别为LEVEL0至LEVEL3。原页未给出各级对应的电压。

```c
enum comp_mcux_acmp_hysteresis_mode {
        COMP_MCUX_ACMP_HYSTERESIS_MODE_LEVEL0 = 0,
        COMP_MCUX_ACMP_HYSTERESIS_MODE_LEVEL1,
        COMP_MCUX_ACMP_HYSTERESIS_MODE_LEVEL2,
        COMP_MCUX_ACMP_HYSTERESIS_MODE_LEVEL3,
};
```

**多路复用器输入（Multiplexer Input，MUX Input）**：`comp_mcux_acmp_mux_input`。输入选项为IN0至IN7。

```c
enum comp_mcux_acmp_mux_input {
        COMP_MCUX_ACMP_MUX_INPUT_IN0 = 0,
        COMP_MCUX_ACMP_MUX_INPUT_IN1,
        COMP_MCUX_ACMP_MUX_INPUT_IN2,
        COMP_MCUX_ACMP_MUX_INPUT_IN3,
        COMP_MCUX_ACMP_MUX_INPUT_IN4,
        COMP_MCUX_ACMP_MUX_INPUT_IN5,
        COMP_MCUX_ACMP_MUX_INPUT_IN6,
        COMP_MCUX_ACMP_MUX_INPUT_IN7,
};
```

**端口输入（Port Input）**：`comp_mcux_acmp_port_input`。DAC表示数模转换器（Digital-to-Analog Converter），MUX表示多路复用器。

```c
enum comp_mcux_acmp_port_input {
        COMP_MCUX_ACMP_PORT_INPUT_DAC = 0,
        COMP_MCUX_ACMP_PORT_INPUT_MUX,
};
```

**DAC参考电压源（Reference Voltage Source）**：`comp_mcux_acmp_dac_vref_source`。原选项为VIN1和VIN2；原页未提供电压数值。

```c
enum comp_mcux_acmp_dac_vref_source {
        COMP_MCUX_ACMP_DAC_VREF_SOURCE_VIN1 = 0,
        COMP_MCUX_ACMP_DAC_VREF_SOURCE_VIN2,
};
```

**离散模式时钟（Discrete Mode Clock，DM Clock）**：`comp_mcux_acmp_dm_clock`。两种选项为慢速（Slow）与快速（Fast）。

```c
enum comp_mcux_acmp_dm_clock {
        COMP_MCUX_ACMP_DM_CLOCK_SLOW = 0,
        COMP_MCUX_ACMP_DM_CLOCK_FAST,
};
```

**离散模式采样时间（Sample Time）**：`comp_mcux_acmp_dm_sample_time`。保留T1、T2、T4、T8、T16、T32、T64、T256选项；T64之后直接为T256，没有T128。

```c
enum comp_mcux_acmp_dm_sample_time {
        COMP_MCUX_ACMP_DM_SAMPLE_TIME_T1 = 0,
        COMP_MCUX_ACMP_DM_SAMPLE_TIME_T2,
        COMP_MCUX_ACMP_DM_SAMPLE_TIME_T4,
        COMP_MCUX_ACMP_DM_SAMPLE_TIME_T8,
        COMP_MCUX_ACMP_DM_SAMPLE_TIME_T16,
        COMP_MCUX_ACMP_DM_SAMPLE_TIME_T32,
        COMP_MCUX_ACMP_DM_SAMPLE_TIME_T64,
        COMP_MCUX_ACMP_DM_SAMPLE_TIME_T256,
};
```

**离散模式阶段时间（Phase Time）**：`comp_mcux_acmp_dm_phase_time`。保留ALT0至ALT7选项；本页不为这些选项补造纳秒或微秒数值。

```c
enum comp_mcux_acmp_dm_phase_time {
        COMP_MCUX_ACMP_DM_PHASE_TIME_ALT0 = 0,
        COMP_MCUX_ACMP_DM_PHASE_TIME_ALT1,
        COMP_MCUX_ACMP_DM_PHASE_TIME_ALT2,
        COMP_MCUX_ACMP_DM_PHASE_TIME_ALT3,
        COMP_MCUX_ACMP_DM_PHASE_TIME_ALT4,
        COMP_MCUX_ACMP_DM_PHASE_TIME_ALT5,
        COMP_MCUX_ACMP_DM_PHASE_TIME_ALT6,
        COMP_MCUX_ACMP_DM_PHASE_TIME_ALT7,
};
```

## 3.3\_设置配置与窗口模式

前五个函数分别设置工作模式、输入、滤波器、DAC和离散模式配置，均接收设备指针`dev`与只读配置指针`config`。最后一个函数通过布尔值`enable`控制窗口模式（Window Mode）。

```c
int comp_mcux_acmp_set_mode_config(const struct device *dev,
                                   const struct comp_mcux_acmp_mode_config *config);
int comp_mcux_acmp_set_input_config(const struct device *dev,
                                    const struct comp_mcux_acmp_input_config *config);
int comp_mcux_acmp_set_filter_config(const struct device *dev,
                                     const struct comp_mcux_acmp_filter_config *config);
int comp_mcux_acmp_set_dac_config(const struct device *dev,
                                  const struct comp_mcux_acmp_dac_config *config);
int comp_mcux_acmp_set_dm_config(const struct device *dev,
                                 const struct comp_mcux_acmp_dm_config *config);
int comp_mcux_acmp_set_window_mode(const struct device *dev, bool enable);
```

原页未说明返回码、字段有效范围、时钟频率或具体芯片差异，因此本页不补写这些保证。完整声明见[源码页](P004_MCUX模拟比较器扩展头文件源码.md)。

---

[上一章：比较器公共头文件源码](P002_比较器公共头文件源码.md) · [下一章：MCUX模拟比较器扩展头文件源码](P004_MCUX模拟比较器扩展头文件源码.md) · [返回大纲](大纲.md)
