---
id: learning.zephyr-docs.kconfig-reference.page-143
title: "`drivers/pwm`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第143章\_`drivers/pwm`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/pwm` 的 92 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MCPWM_ESP32"></a>

## 143.1 `CONFIG_MCPWM_ESP32`

**提示（Prompt）**：ESP32 电机控制 PWM（MCPWM）驱动

**说明（Help）**

此选项启用 ESP32 系列处理器的 MCPWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_MCPWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.esp32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.esp32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM"></a>

## 143.2 `CONFIG_PWM`

**提示（Prompt）**：脉宽调制（Pulse Width Modulation，PWM）驱动

**说明（Help）**

启用 PWM 驱动的配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BUZZER_PWM
CONFIG_CLOCK_CONTROL_PWM
CONFIG_DALI_PWM
CONFIG_LED_PWM
CONFIG_TSIC_XX6
```

**定义位置（Location）**：[`drivers/pwm/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BUZZER_PWM`](P058_drivers_buzzer_配置项参考.md#CONFIG_BUZZER_PWM)、[`CONFIG_CLOCK_CONTROL_PWM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_PWM)、[`CONFIG_DALI_PWM`](P074_drivers_dali_配置项参考.md#CONFIG_DALI_PWM)、[`CONFIG_LED_PWM`](P114_drivers_led_配置项参考.md#CONFIG_LED_PWM)、[`CONFIG_TSIC_XX6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TSIC_XX6)。

<a id="CONFIG_PWM_ADI_AXI_PWMGEN"></a>

## 143.3 `CONFIG_PWM_ADI_AXI_PWMGEN`

**提示（Prompt）**：Analog Devices AXI PWM 发生器（Generator）驱动

**说明（Help）**

启用 Analog Devices AXI PWM Generator 核驱动，生成周期性触发脉冲，例如 ADC 转换 CNV 信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AXI_PWMGEN_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.adi_axi_pwmgen:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.adi_axi_pwmgen#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_AMBIQ_CTIMER"></a>

## 143.4 `CONFIG_PWM_AMBIQ_CTIMER`

**提示（Prompt）**：Ambiq CTimer PWM 驱动

**说明（Help）**

启用基于 CTimer 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_CTIMER_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_TIMER
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.ambiq_timer:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.ambiq_timer#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_TIMER)。

<a id="CONFIG_PWM_AMBIQ_TIMER"></a>

## 143.5 `CONFIG_PWM_AMBIQ_TIMER`

**提示（Prompt）**：Ambiq Timer PWM 驱动

**说明（Help）**

启用基于 Timer 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_TIMER_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_TIMER
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.ambiq_timer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.ambiq_timer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_TIMER)。

<a id="CONFIG_PWM_AMEBA"></a>

## 143.6 `CONFIG_PWM_AMEBA`

**提示（Prompt）**：AMEBA PWM 驱动

**说明（Help）**

启用 AMEBA 系列处理器的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.ameba:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.ameba#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_BBLED_XEC"></a>

## 143.7 `CONFIG_PWM_BBLED_XEC`

**提示（Prompt）**：Microchip XEC PWM-BBLED 驱动

**说明（Help）**

启用将 Microchip XEC 呼吸／闪烁 LED（Breathing-Blinking LED）用作 PWM 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_PWMBBLED_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.xec:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.xec#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_BEE"></a>

## 143.8 `CONFIG_PWM_BEE`

**提示（Prompt）**：Realtek Bee 系列 PWM 驱动

**说明（Help）**

此选项启用 Realtek Bee SoC 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_TIM if DT_HAS_REALTEK_BEE_BASIC_TIMER_ENABLED
CONFIG_HAL_REALTEK_BEE_ENHTIM if DT_HAS_REALTEK_BEE_ENHANCED_TIMER_ENABLED
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.bee:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.bee#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_HAL_REALTEK_BEE_TIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_TIM)、[`CONFIG_HAL_REALTEK_BEE_ENHTIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_ENHTIM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_TIM`、`CONFIG_HAL_REALTEK_BEE_ENHTIM`。

<a id="CONFIG_PWM_BFLB_1"></a>

## 143.9 `CONFIG_PWM_BFLB_1`

**提示（Prompt）**：BFLB PWM 1（BL60x、BL70x、BL70xL）驱动

**说明（Help）**

此选项启用 Bouffalolab BL60x、BL70x 和部分 BL70xL 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_PWM_1_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_BFLB_2"></a>

## 143.10 `CONFIG_PWM_BFLB_2`

**提示（Prompt）**：BFLB PWM 2（BL61x、BL70xL）驱动

**说明（Help）**

此选项启用 Bouffalolab BL61x 和部分 BL70xL 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_PWM_2_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.bflb:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.bflb#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_BITBANG"></a>

## 143.11 `CONFIG_PWM_BITBANG`

**提示（Prompt）**：位操作模拟（Bitbang）PWM 驱动

**说明（Help）**

使用硬件定时器中断的通用软件 PWM 驱动。仅在没有剩余专用硬件 PWM 引脚，并了解 CPU 开销影响时，将其用作备用方案。所有通道使用相同周期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_PWM_BITBANG_ENABLED && CONFIG_GPIO && CONFIG_COUNTER && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.bitbang:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.bitbang#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_BITBANG_INIT_PRIORITY"></a>

## 143.12 `CONFIG_PWM_BITBANG_INIT_PRIORITY`

**提示（Prompt）**：Bitbang PWM 初始化优先级

**说明（Help）**

位操作模拟 PWM 驱动的系统初始化优先级。必须大于或等于 `CONFIG_COUNTER_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM_BITBANG && CONFIG_PWM
```

**默认值（Defaults）**

```text
CONFIG_COUNTER_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.bitbang:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.bitbang#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → 位操作模拟（Bitbang）PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM_BITBANG`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_BITBANG)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_COUNTER_INIT_PRIORITY`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_INIT_PRIORITY)。

<a id="CONFIG_PWM_CAPTURE"></a>

## 143.13 `CONFIG_PWM_CAPTURE`

**提示（Prompt）**：提供 PWM 捕获（Capture）API

**说明（Help）**

此选项扩展 Zephyr PWM API，增加捕获 PWM 周期／脉冲宽度的能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM
```

**被选择（Selected by）**

```text
CONFIG_TSIC_XX6
```

**定义位置（Location）**：[`drivers/pwm/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_TSIC_XX6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TSIC_XX6)。

<a id="CONFIG_PWM_CAPTURE_MCUX_FTM_FILTER_VALUE"></a>

## 143.14 `CONFIG_PWM_CAPTURE_MCUX_FTM_FILTER_VALUE`

**提示（Prompt）**：MCUX FTM PWM 捕获滤波值（Capture Filter Value）

**说明（Help）**

通道 0 和 2 的 PWM 捕获滤波值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM_MCUX_FTM && CONFIG_PWM_CAPTURE && CONFIG_PWM
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_ftm:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_ftm#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → MCUX FTM PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM_MCUX_FTM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_MCUX_FTM)、[`CONFIG_PWM_CAPTURE`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_CAPTURE)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_CAPTURE_MCUX_QTMR_FILTER_COUNT"></a>

## 143.15 `CONFIG_PWM_CAPTURE_MCUX_QTMR_FILTER_COUNT`

**提示（Prompt）**：MCUX QMTR PWM 输入滤波采样计数（Input Filter Sample Count）

**说明（Help）**

输入滤波器接受一次输入跳变之前，必须连续一致的采样数量。实际采样数量为 `(value +3)`；例如值 `0x0` 表示 3 次采样。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM_MCUX_QTMR && CONFIG_PWM_CAPTURE && CONFIG_PWM
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_qtmr:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_qtmr#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → MCUX QMTR PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM_MCUX_QTMR`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_MCUX_QTMR)、[`CONFIG_PWM_CAPTURE`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_CAPTURE)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_CAPTURE_MCUX_QTMR_FILTER_PERIOD"></a>

## 143.16 `CONFIG_PWM_CAPTURE_MCUX_QTMR_FILTER_PERIOD`

**提示（Prompt）**：MCUX QMTR PWM 输入滤波采样周期（Sample Period）

**说明（Help）**

TMR 输入信号的采样周期，以 IP 总线时钟周期计。值为 `0x00`（默认）时，旁路输入滤波器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM_MCUX_QTMR && CONFIG_PWM_CAPTURE && CONFIG_PWM
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_qtmr:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_qtmr#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → MCUX QMTR PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM_MCUX_QTMR`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_MCUX_QTMR)、[`CONFIG_PWM_CAPTURE`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_CAPTURE)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_CAPTURE_MCUX_TPM_FILTER_VALUE"></a>

## 143.17 `CONFIG_PWM_CAPTURE_MCUX_TPM_FILTER_VALUE`

**提示（Prompt）**：MCUX TPM PWM 捕获滤波值

**说明（Help）**

各通道的 PWM 捕获滤波值。值为 0 时禁用滤波器，否则滤波器配置为 `(CHxFVAL * 4)` 个时钟周期。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM_MCUX_TPM && CONFIG_PWM_CAPTURE && CONFIG_PWM
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_tpm:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_tpm#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → MCUX TPM PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM_MCUX_TPM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_MCUX_TPM)、[`CONFIG_PWM_CAPTURE`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_CAPTURE)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_CC13XX_CC26XX_TIMER"></a>

## 143.18 `CONFIG_PWM_CC13XX_CC26XX_TIMER`

**提示（Prompt）**：TI SimpleLink CC13xx/CC26xx GPT 定时器 PWM 驱动

**说明（Help）**

启用 TI SimpleLink CC13xx/CC26xx GPT 定时器 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_TIMER_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.cc13xx_cc26xx_timer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.cc13xx_cc26xx_timer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_CC23X0_TIMER"></a>

## 143.19 `CONFIG_PWM_CC23X0_TIMER`

**提示（Prompt）**：TI SimpleLink CC23x0 LGPT PWM 驱动

**说明（Help）**

启用 TI SimpleLink CC23x0 LGPT PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_LGPT_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.cc23x0_timer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.cc23x0_timer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_ENE_KB106X"></a>

## 143.20 `CONFIG_PWM_ENE_KB106X`

**提示（Prompt）**：ENE KB106X PWM 驱动

**说明（Help）**

此选项启用 KB106X 处理器的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB106X_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.ene:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.ene#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_ENE_KB1200"></a>

## 143.21 `CONFIG_PWM_ENE_KB1200`

**提示（Prompt）**：ENE KB1200 PWM 驱动

**说明（Help）**

此选项启用 KB1200 处理器的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ENE_KB1200_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.ene:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.ene#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_EVENT"></a>

## 143.22 `CONFIG_PWM_EVENT`

**提示（Prompt）**：提供 PWM 事件（Event）API【实验性（EXPERIMENTAL）】

**说明（Help）**

此选项扩展 Zephyr PWM API，增加配置和接收 PWM 事件的能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_PWM_FAKE"></a>

## 143.23 `CONFIG_PWM_FAKE`

**提示（Prompt）**：模拟 PWM 驱动程序。

**说明（Help）**

启用基于伪函数框架（FFF）的模拟 PWM 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FAKE_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.fake:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.fake#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_GD32"></a>

## 143.24 `CONFIG_PWM_GD32`

**提示（Prompt）**：GigaDevice GD32 PWM 驱动

**说明（Help）**

启用 GigaDevice GD32 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_GECKO"></a>

## 143.25 `CONFIG_PWM_GECKO`

**提示（Prompt）**：GECKO MCU PWM 驱动

**说明（Help）**

此选项启用 EXX32 GECKO 系列处理器的 PWM 驱动。如需使用 EXX32 MCU 的 PWM 端口，请选 y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_TIMER
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.gecko:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.gecko#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_SILABS_GECKO_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_TIMER)。

<a id="CONFIG_PWM_IMX"></a>

## 143.26 `CONFIG_PWM_IMX`

**提示（Prompt）**：i.MX PWM 驱动

**说明（Help）**

启用 i.MX PWM 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FSL_IMX27_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.imx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.imx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_INFINEON_TCPWM"></a>

## 143.27 `CONFIG_PWM_INFINEON_TCPWM`

**提示（Prompt）**：Infineon TCPWM 驱动

**说明（Help）**

此选项启用 Infineon TCPWM 外设中的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_TCPWM_PWM_ENABLED && !CONFIG_SOC_FAMILY_INFINEON_PSOC4 && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_PWM
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.infineon_tcpwm:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.infineon_tcpwm#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_USE_INFINEON_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_PWM_INFINEON_TCPWM_PSOC4"></a>

## 143.28 `CONFIG_PWM_INFINEON_TCPWM_PSOC4`

**提示（Prompt）**：PSOC4 的 Infineon TCPWM 驱动

**说明（Help）**

此选项启用 PSOC4 系列 Infineon TCPWM 外设中的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_TCPWM_PWM_ENABLED && CONFIG_SOC_FAMILY_INFINEON_PSOC4 && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_PWM
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.infineon_tcpwm:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.infineon_tcpwm#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_USE_INFINEON_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_PWM_INIT_PRIORITY"></a>

## 143.29 `CONFIG_PWM_INIT_PRIORITY`

**提示（Prompt）**：PWM 初始化优先级

**说明（Help）**

PWM 驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/pwm/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_PWM_INTEL_BLINKY"></a>

## 143.30 `CONFIG_PWM_INTEL_BLINKY`

**提示（Prompt）**：Blinky PWM 驱动

**说明（Help）**

启用 Intel SoC 中的 Intel PCH PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_BLINKY_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.intel_blinky:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.intel_blinky#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_ITE_IT51XXX"></a>

## 143.31 `CONFIG_PWM_ITE_IT51XXX`

**提示（Prompt）**：ITE IT51XXX 嵌入式控制器（EC）PWM 驱动

**说明（Help）**

启用 IT51XXX 系列 SoC 的 PWM 驱动。支持三个 16 位预分频器（Prescaler），每个配有 10 位周期定时器；还支持八个 PWM 通道，每个具有 10 位占空比（Duty Cycle）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_ITE_IT8801"></a>

## 143.32 `CONFIG_PWM_ITE_IT8801`

**提示（Prompt）**：ITE IT8801 PWM 设备驱动

**说明（Help）**

启用 ITE IT8801 基于 I²C 的 PWM 驱动，支持 7 路开漏／推挽（Open-drain/Push-pull）输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8801_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.it8801:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.it8801#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_PWM_ITE_IT8XXX2"></a>

## 143.33 `CONFIG_PWM_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 嵌入式控制器（EC）PWM 驱动

**说明（Help）**

启用 it8xxx2_evb 的 PWM 驱动。支持三个 16 位预分频器，每个配有 8 位周期定时器；还支持八个 PWM 通道，每个具有 8 位占空比。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.it8xxx2:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.it8xxx2#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_LED_ESP32"></a>

## 143.34 `CONFIG_PWM_LED_ESP32`

**提示（Prompt）**：ESP32 PWM LED 驱动

**说明（Help）**

此选项启用 ESP32 系列处理器的 PWM LED 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_LEDC_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.esp32:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.esp32#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_LITEX"></a>

## 143.35 `CONFIG_PWM_LITEX`

**提示（Prompt）**：LiteX PWM 驱动

**说明（Help）**

启用 LiteX PWM 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.litex:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.litex#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_LITEX_INIT_PRIORITY"></a>

## 143.36 `CONFIG_PWM_LITEX_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

PWM 设备驱动初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM_LITEX && CONFIG_PWM
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.litex:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.litex#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → LiteX PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM_LITEX`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_LITEX)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_MAX2221X"></a>

## 143.37 `CONFIG_PWM_MAX2221X`

**提示（Prompt）**：Analog Devices MAX2221X 多功能设备驱动

**说明（Help）**

启用 MAX2221x PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX2221X_PWM_ENABLED && CONFIG_MFD && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.max2221x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.max2221x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_MAX2221X_INIT_PRIORITY"></a>

## 143.38 `CONFIG_PWM_MAX2221X_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

Analog Devices MAX22216/MAX22217 PWM 驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM_MAX2221X && CONFIG_PWM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.max2221x:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.max2221x#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → Analog Devices MAX2221X 多功能设备驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM_MAX2221X`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_MAX2221X)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_MAX31790"></a>

## 143.39 `CONFIG_PWM_MAX31790`

**提示（Prompt）**：MAX31790 六通道 I²C 总线 PWM 驱动

**说明（Help）**

启用 MAX31790 六通道 I²C 总线 PWM 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX31790_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.max31790:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.max31790#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_PWM_MAX32"></a>

## 143.40 `CONFIG_PWM_MAX32`

**提示（Prompt）**：MAX32 PWM 驱动

**说明（Help）**

启用 MAX32 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_MCHP_G1_TCC"></a>

## 143.41 `CONFIG_PWM_MCHP_G1_TCC`

**提示（Prompt）**：Microchip TCC G1 PWM 驱动

**说明（Help）**

启用 Microchip 脉宽调制（PWM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_TCC_G1_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mchp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mchp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → Microchip PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_MCHP_PWM_G1"></a>

## 143.42 `CONFIG_PWM_MCHP_PWM_G1`

**提示（Prompt）**：Microchip PWM G1 PWM 驱动

**说明（Help）**

启用 Microchip 脉宽调制（PWM）G1 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_PWM_G1_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mchp:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mchp#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → Microchip PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_MCHP_TC_G1"></a>

## 143.43 `CONFIG_PWM_MCHP_TC_G1`

**提示（Prompt）**：Microchip TC G1 PWM 驱动

**说明（Help）**

启用 Microchip 脉宽调制（PWM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_TC_G1_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mchp:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mchp#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → Microchip PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_MCUX"></a>

## 143.44 `CONFIG_PWM_MCUX`

**提示（Prompt）**：MCUX PWM 驱动

**说明（Help）**

启用 MCUX PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_MCUX_CTIMER"></a>

## 143.45 `CONFIG_PWM_MCUX_CTIMER`

**提示（Prompt）**：MCUX CTimer PWM 驱动

**说明（Help）**

启用基于 CTimer 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_CTIMER_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_MUX if CONFIG_PWM_CAPTURE
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_ctimer:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_ctimer#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)、[`CONFIG_PWM_CAPTURE`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_CAPTURE)。

<a id="CONFIG_PWM_MCUX_FTM"></a>

## 143.46 `CONFIG_PWM_MCUX_FTM`

**提示（Prompt）**：MCUX FTM PWM 驱动

**说明（Help）**

启用 MCUX FTM PWM 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FTM_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_ftm:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_ftm#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_MCUX_PWT"></a>

## 143.47 `CONFIG_PWM_MCUX_PWT`

**提示（Prompt）**：MCUX PWT PWM 捕获（Capture）驱动

**说明（Help）**

启用 MCUX 脉冲宽度定时器（Pulse Width Timer，PWT）PWM 捕获驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_PWT_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM_CAPTURE && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_pwt:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_pwt#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM_CAPTURE`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_CAPTURE)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_MCUX_QTMR"></a>

## 143.48 `CONFIG_PWM_MCUX_QTMR`

**提示（Prompt）**：MCUX QMTR PWM 驱动

**说明（Help）**

启用基于 QTMR 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_QTMR_PWM_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_qtmr:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_qtmr#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_MCUX_SCTIMER"></a>

## 143.49 `CONFIG_PWM_MCUX_SCTIMER`

**提示（Prompt）**：MCUX SCTimer PWM 驱动

**说明（Help）**

启用基于 SCTimer 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SCTIMER_PWM_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_MUX if CONFIG_PWM_CAPTURE
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_sctimer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_sctimer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)、[`CONFIG_PWM_CAPTURE`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_CAPTURE)。

<a id="CONFIG_PWM_MCUX_TPM"></a>

## 143.50 `CONFIG_PWM_MCUX_TPM`

**提示（Prompt）**：MCUX TPM PWM 驱动

**说明（Help）**

启用 MCUX TPM PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_TPM_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mcux_tpm:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mcux_tpm#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_MSPM0"></a>

## 143.51 `CONFIG_PWM_MSPM0`

**提示（Prompt）**：TI MSPM0 MCU 系列 PWM 驱动

**说明（Help）**

启用 TI MSPM0 MCU 系列 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_TIMER_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_USE_MSPM0_DL_TIMER
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.mspm0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.mspm0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_USE_MSPM0_DL_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_TIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_TIMER`。

<a id="CONFIG_PWM_NEORV32"></a>

## 143.52 `CONFIG_PWM_NEORV32`

**提示（Prompt）**：NEORV32 PWM 驱动

**说明（Help）**

启用 NEORV32 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NEORV32_PWM_ENABLED && CONFIG_SYSCON && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.neorv32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.neorv32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_NPCX"></a>

## 143.53 `CONFIG_PWM_NPCX`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（EC）PWM 驱动

**说明（Help）**

此选项启用 NPCX 系列处理器的 PWM 驱动。如需使用 NPCX MCU 的 PWM 端口，请选 y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_NRFX"></a>

## 143.54 `CONFIG_PWM_NRFX`

**提示（Prompt）**：nRF PWM nrfx 驱动

**说明（Help）**

启用 nRF52 MCU 系列的 nrfx 硬件 PWM 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PWM
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.nrfx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.nrfx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_NRFX_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_NRFX_NO_GLITCH_DUTY_100"></a>

## 143.55 `CONFIG_PWM_NRFX_NO_GLITCH_DUTY_100`

**提示（Prompt）**：100% 占空比时无毛刺（No Glitches）

**说明（Help）**

由于 PWM 的 `IDLEOUT` 功能工作方式，当所有其他通道切换到 0% 或 100% 占空比时，100% 占空比通道上可能出现毛刺（Glitch）。启用此项可保证无毛刺，但也意味着任何通道使用 100% 占空比时，PWM 外设都必须保持活动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.nrfx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.nrfx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

<a id="CONFIG_PWM_NRF_SW"></a>

## 143.56 `CONFIG_PWM_NRF_SW`

**提示（Prompt）**：Nordic Semiconductor nRF 系列软件（S/W）PWM 驱动

**说明（Help）**

启用在 Nordic Semiconductor nRF SoC 上使用 PWM 的驱动。使用高频（HF）定时器时，最多提供 5 个引脚，每个引脚使用一个 GPIOTE 通道和两个 PPI/DPPI 通道。使用 RTC 时，最多提供 3 个引脚，每个引脚使用一个 GPIOTE 通道和两个 PPI/DPPI 通道；无分叉（Fork）功能时则需要三个 PPI/DPPI 通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_SW_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPIOTE
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.nrf_sw:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.nrf_sw#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_NRFX_GPIOTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPIOTE)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

<a id="CONFIG_PWM_NUMAKER"></a>

## 143.57 `CONFIG_PWM_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker MCU PWM 驱动

**说明（Help）**

此选项启用 Nuvoton NuMaker 系列处理器的 PWM 驱动。如需启用 NuMaker PWM，请选 y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_NUMAKER_PWM
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_HAS_NUMAKER_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_NXP_EMIOS"></a>

## 143.58 `CONFIG_PWM_NXP_EMIOS`

**提示（Prompt）**：NXP PWM-eMIOS 驱动

**说明（Help）**

启用 NXP PWM-eMIOS 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_EMIOS_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.nxp_emios:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.nxp_emios#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_NXP_FLEXIO"></a>

## 143.59 `CONFIG_PWM_NXP_FLEXIO`

**提示（Prompt）**：NXP FlexIO PWM 驱动

**说明（Help）**

启用基于 FlexIO 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FLEXIO_ENABLED && CONFIG_CLOCK_CONTROL && DT_HAS_NXP_FLEXIO_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MCUX_FLEXIO
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.nxp_flexio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.nxp_flexio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_MCUX_FLEXIO`](P123_drivers_misc_配置项参考.md#CONFIG_MCUX_FLEXIO)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_NXP_IPWM"></a>

## 143.60 `CONFIG_PWM_NXP_IPWM`

**提示（Prompt）**：NXP i.MX PWM 驱动

**说明（Help）**

启用 i.MX8M 系列中 i.MX PWM 模块的驱动。它与 `PWM_MCUX` 覆盖的 FlexPWM 模块不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IPWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.nxp_ipwm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.nxp_ipwm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_NXP_S32_EMIOS"></a>

## 143.61 `CONFIG_PWM_NXP_S32_EMIOS`

**提示（Prompt）**：NXP S32 PWM-eMIOS 驱动

**说明（Help）**

启用 NXP S32 PWM-eMIOS 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_EMIOS_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NXP_S32_EMIOS
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.nxp_s32_emios:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.nxp_s32_emios#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_NXP_S32_EMIOS`](P123_drivers_misc_配置项参考.md#CONFIG_NXP_S32_EMIOS)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_PWM_PCA9685"></a>

## 143.62 `CONFIG_PWM_PCA9685`

**提示（Prompt）**：PCA9685 十六通道、12 位 PWM Fm+ I²C 总线 LED 控制器

**说明（Help）**

启用 PCA9685 十六通道、12 位 PWM 快速模式增强版（Fm+）I²C 总线 LED 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCA9685_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.pca9685:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.pca9685#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_PWM_PWMSWR_LOOP"></a>

## 143.63 `CONFIG_PWM_PWMSWR_LOOP`

**提示（Prompt）**：PWM 软件复位循环次数（Software Reset Loop Count）

**说明（Help）**

禁用 PWM 通道时，PWM 软件复位的循环次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM_IMX && CONFIG_PWM
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.imx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.imx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动 → i.MX PWM 驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM_IMX`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_IMX)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_RCAR"></a>

## 143.64 `CONFIG_PWM_RCAR`

**提示（Prompt）**：Renesas R-Car PWM 驱动

**说明（Help）**

启用 Renesas R-Car PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RCAR && DT_HAS_RENESAS_PWM_RCAR_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.rcar:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.rcar#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RCAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RCAR)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RCAR`。

<a id="CONFIG_PWM_REALTEK_RTS5912"></a>

## 143.65 `CONFIG_PWM_REALTEK_RTS5912`

**提示（Prompt）**：Realtek RTS5912 PWM 驱动

**说明（Help）**

启用 Realtek RTS5912 嵌入式控制器（EC）的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.rts5912:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.rts5912#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_RENESAS_RA"></a>

## 143.66 `CONFIG_PWM_RENESAS_RA`

**提示（Prompt）**：Renesas RA PWM 驱动

**说明（Help）**

启用 Renesas RA PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_GPT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_USE_RA_FSP_GPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_GPT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_RENESAS_RX_MTU"></a>

## 143.67 `CONFIG_PWM_RENESAS_RX_MTU`

**提示（Prompt）**：Renesas RX MTU PWM 驱动

**说明（Help）**

启用 Renesas RX PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_MTU_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.renesas_rx_mtu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.renesas_rx_mtu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_RENESAS_RZA2M_GPT"></a>

## 143.68 `CONFIG_PWM_RENESAS_RZA2M_GPT`

**提示（Prompt）**：Renesas RZA2M 通用 PWM 定时器（GPT）PWM 驱动

**说明（Help）**

启用 Renesas RZ/A2M 通用 PWM 定时器（General PWM Timer，GPT）的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_GPT_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.renesas_rz:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.renesas_rz#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_RENESAS_RZ_GPT"></a>

## 143.69 `CONFIG_PWM_RENESAS_RZ_GPT`

**提示（Prompt）**：Renesas RZ 通用 PWM 定时器（GPT）PWM 驱动

**说明（Help）**

启用 Renesas RZ 通用 PWM 定时器（GPT）的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_GPT_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_GPT
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_USE_RZ_FSP_GPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_GPT)。

<a id="CONFIG_PWM_RENESAS_RZ_MTU"></a>

## 143.70 `CONFIG_PWM_RENESAS_RZ_MTU`

**提示（Prompt）**：Renesas RZ 多功能定时脉冲单元（MTU）PWM 驱动

**说明（Help）**

启用 Renesas RZ 多功能定时脉冲单元（Multi-Function Timer Pulse，MTU）的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_MTU_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_MTU
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.renesas_rz:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.renesas_rz#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_USE_RZ_FSP_MTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_MTU)。

<a id="CONFIG_PWM_RPI_PICO"></a>

## 143.71 `CONFIG_PWM_RPI_PICO`

**提示（Prompt）**：RPi Pico PWM 驱动

**说明（Help）**

启用 RPi Pico MCU 系列的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_PWM_ENABLED && CONFIG_RESET && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_PWM
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PICOSDK_USE_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_RV32M1_TPM"></a>

## 143.72 `CONFIG_PWM_RV32M1_TPM`

**提示（Prompt）**：RV32M1 TPM PWM 驱动

**说明（Help）**

启用 RV32M1 TPM PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_TPM_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.rv32m1_tpm:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.rv32m1_tpm#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_SAM"></a>

## 143.73 `CONFIG_PWM_SAM`

**提示（Prompt）**：Atmel SAM MCU 系列 PWM 驱动

**说明（Help）**

启用 Atmel SAM MCU 的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.sam:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.sam#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_SAM0_TC"></a>

## 143.74 `CONFIG_PWM_SAM0_TC`

**提示（Prompt）**：Atmel SAM0 MCU 系列 TC PWM 驱动

**说明（Help）**

启用 Atmel SAM0 MCU 使用 TC 定时器／计数器（Timer/Counter）的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_TC_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.sam0_tc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.sam0_tc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_SAM0_TCC"></a>

## 143.75 `CONFIG_PWM_SAM0_TCC`

**提示（Prompt）**：Atmel SAM0 MCU 系列 TCC PWM 驱动

**说明（Help）**

启用 Atmel SAM0 MCU 使用 TCC 定时器／计数器的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_TCC_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.sam0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.sam0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_SF32LB_ATIM"></a>

## 143.76 `CONFIG_PWM_SF32LB_ATIM`

**提示（Prompt）**：SF32LB ATIM PWM 驱动

**说明（Help）**

启用 SF32LB MCU 系列的 PWM 驱动。此驱动使用高级定时器（Advanced Timer）外设实现 PWM 功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_ATIM_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.sf32lb:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.sf32lb#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_SF32LB_GPT"></a>

## 143.77 `CONFIG_PWM_SF32LB_GPT`

**提示（Prompt）**：SF32LB GPT PWM 驱动

**说明（Help）**

启用 SF32LB MCU 系列的 PWM 驱动。此驱动使用定时器外设实现 PWM 功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_GPT_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_SHELL"></a>

## 143.78 `CONFIG_PWM_SHELL`

**提示（Prompt）**：PWM 命令行（Shell）

**说明（Help）**

启用 PWM 相关 Shell 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_PWM
```

**定义位置（Location）**：[`drivers/pwm/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_SIFIVE"></a>

## 143.79 `CONFIG_PWM_SIFIVE`

**提示（Prompt）**：SiFive Freedom PWM 驱动

**说明（Help）**

启用 SiFive Freedom 平台的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFIVE_PWM0_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL if CONFIG_SOC_SERIES_FE300
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.sifive:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.sifive#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_FE300`。

<a id="CONFIG_PWM_SILABS_LETIMER"></a>

## 143.80 `CONFIG_PWM_SILABS_LETIMER`

**提示（Prompt）**：Silabs LETIMER PWM 驱动

**说明（Help）**

启用 Silabs Series 2 SoC 上 LETIMER 外设的 PWM 驱动。LETIMER 有两个通道，共享 PWM 周期配置；最后配置的周期适用于两个通道。更新 PWM 脉冲和周期时，由于新值立即生效，输出可能出现毛刺（Glitch）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_LETIMER_PWM_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_LETIMER
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_SILABS_SISDK_LETIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_LETIMER)。

<a id="CONFIG_PWM_SILABS_SIWX91X"></a>

## 143.81 `CONFIG_PWM_SILABS_SIWX91X`

**提示（Prompt）**：Silabs SiWx91x PWM 驱动

**说明（Help）**

启用 Silabs SiWx91x SoC 系列的 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_PWM_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_SILABS_TIMER"></a>

## 143.82 `CONFIG_PWM_SILABS_TIMER`

**提示（Prompt）**：Silabs TIMER PWM 驱动

**说明（Help）**

启用 Silabs Series 2 SoC 上 TIMER 外设的 PWM 驱动。TIMER 有三个或更多通道，共享 PWM 周期配置；最后配置的周期适用于所有通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_TIMER_PWM_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_TIMER
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.silabs:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.silabs#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_SILABS_SISDK_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_TIMER)。

<a id="CONFIG_PWM_STM32"></a>

## 143.83 `CONFIG_PWM_STM32`

**提示（Prompt）**：STM32 MCU PWM 驱动

**说明（Help）**

此选项启用 STM32 系列处理器的 PWM 驱动。如需使用 STM32 MCU 的 PWM 端口，请选 y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.stm32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.stm32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_TC_INIT_PRIORITY"></a>

## 143.84 `CONFIG_PWM_TC_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PWM
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.sam0_tc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.sam0_tc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_TELINK_B91"></a>

## 143.85 `CONFIG_PWM_TELINK_B91`

**提示（Prompt）**：Telink Semiconductor B91 PWM 驱动

**说明（Help）**

启用 Telink B91 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TELINK_B91_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.b91:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.b91#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_TI_AM3352_ECAP"></a>

## 143.86 `CONFIG_PWM_TI_AM3352_ECAP`

**提示（Prompt）**：TI ECAP PWM 驱动

**说明（Help）**

启用 TI SoC 的 ECAP 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_AM3352_ECAP_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.ti_am3352_ecap:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.ti_am3352_ecap#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_TI_AM3352_EHRPWM"></a>

## 143.87 `CONFIG_PWM_TI_AM3352_EHRPWM`

**提示（Prompt）**：TI EHRPWM PWM 驱动

**说明（Help）**

启用 TI SoC 的 EHRPWM 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_AM3352_EHRPWM_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SYSCON
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.ti_am3352_ehrpwm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.ti_am3352_ehrpwm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)。

<a id="CONFIG_PWM_WCH_GPTM"></a>

## 143.88 `CONFIG_PWM_WCH_GPTM`

**提示（Prompt）**：WCH 通用定时器（General-purpose Timer，GPTM）PWM 驱动

**说明（Help）**

WCH GPTM 的 PWM 驱动，例如 CH32V003 上的 TIM2。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_WCH_GPTM_PWM_ENABLED || DT_HAS_WCH_ADTM_PWM_ENABLED) && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_XEC"></a>

## 143.89 `CONFIG_PWM_XEC`

**提示（Prompt）**：Microchip XEC PWM 驱动

**说明（Help）**

启用在 Microchip XEC IP 模块上使用 PWM 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_XLNX_AXI_TIMER"></a>

## 143.90 `CONFIG_PWM_XLNX_AXI_TIMER`

**提示（Prompt）**：Xilinx AXI 定时器驱动（AXI Timer Driver）

**说明（Help）**

启用 Xilinx AXI Timer v2.0 IP 的 PWM 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_XPS_TIMER_1_00_A_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.xlnx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.xlnx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)。

<a id="CONFIG_PWM_XMC4XXX_CCU4"></a>

## 143.91 `CONFIG_PWM_XMC4XXX_CCU4`

**提示（Prompt）**：Infineon XMC4XXX CCU4 驱动

**说明（Help）**

启用 Infineon XMC4XXX CCU4 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_CCU4_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.xmc4xxx_ccu4:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.xmc4xxx_ccu4#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PWM_XMC4XXX_CCU8"></a>

## 143.92 `CONFIG_PWM_XMC4XXX_CCU8`

**提示（Prompt）**：Infineon XMC4XXX CCU8 驱动

**说明（Help）**

启用 Infineon XMC4XXX CCU8 PWM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_CCU8_PWM_ENABLED && CONFIG_PWM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/pwm/Kconfig.xmc4xxx_ccu8:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/Kconfig.xmc4xxx_ccu8#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 脉宽调制（Pulse Width Modulation，PWM）驱动

**配置项引用（Symbol References）**：[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<!-- kconfig-navigation -->

[上一章](P142_drivers_pulse_io_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P144_drivers_regulator_配置项参考.md)
