---
id: learning.zephyr-docs.kconfig-reference.page-114
title: "`drivers/led`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第114章\_`drivers/led`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/led` 的 34 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HT16K33"></a>

## 114.1 `CONFIG_HT16K33`

**提示（Prompt）**：HT16K33 LED 驱动

**说明（Help）**

启用 HT16K33 的 LED 驱动。HT16K33 是采用内存映射（Memory Mapping）的多功能 LED 控制驱动器，最多支持 128 个 LED，最多 16 行和 8 个公共端（Common）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HOLTEK_HT16K33_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.ht16k33:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.ht16k33#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_HT16K33_KEYSCAN"></a>

## 114.2 `CONFIG_HT16K33_KEYSCAN`

**提示（Prompt）**：按键扫描（Keyscan）支持

**说明（Help）**

在 HT16K33 LED 驱动中启用按键扫描子设备支持。按键扫描功能本身由 HT16K33 按键扫描驱动处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HT16K33 && CONFIG_INPUT && CONFIG_LED
```

**定义位置（Location）**：[`drivers/led/Kconfig.ht16k33:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.ht16k33#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → HT16K33 LED 驱动

**配置项引用（Symbol References）**：[`CONFIG_HT16K33`](P114_drivers_led_配置项参考.md#CONFIG_HT16K33)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)。

<a id="CONFIG_HT16K33_KEYSCAN_DEBOUNCE_MSEC"></a>

## 114.3 `CONFIG_HT16K33_KEYSCAN_DEBOUNCE_MSEC`

**提示（Prompt）**：按键扫描去抖间隔（Debounce Interval），单位为毫秒

**说明（Help）**

按键扫描去抖间隔，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HT16K33_KEYSCAN && CONFIG_LED
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[20, 1000]
```

**定义位置（Location）**：[`drivers/led/Kconfig.ht16k33:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.ht16k33#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → HT16K33 LED 驱动 → 按键扫描（Keyscan）支持

**配置项引用（Symbol References）**：[`CONFIG_HT16K33_KEYSCAN`](P114_drivers_led_配置项参考.md#CONFIG_HT16K33_KEYSCAN)、[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)。

<a id="CONFIG_HT16K33_KEYSCAN_IRQ_THREAD_PRIO"></a>

## 114.4 `CONFIG_HT16K33_KEYSCAN_IRQ_THREAD_PRIO`

**提示（Prompt）**：按键扫描中断请求处理线程的优先级（Thread Priority）

**说明（Help）**

处理按键扫描中断的内部线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HT16K33_KEYSCAN && CONFIG_LED
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/led/Kconfig.ht16k33:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.ht16k33#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → HT16K33 LED 驱动 → 按键扫描（Keyscan）支持

**配置项引用（Symbol References）**：[`CONFIG_HT16K33_KEYSCAN`](P114_drivers_led_配置项参考.md#CONFIG_HT16K33_KEYSCAN)、[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)。

<a id="CONFIG_HT16K33_KEYSCAN_IRQ_THREAD_STACK_SIZE"></a>

## 114.5 `CONFIG_HT16K33_KEYSCAN_IRQ_THREAD_STACK_SIZE`

**提示（Prompt）**：按键扫描中断请求处理线程的栈大小（Stack Size）

**说明（Help）**

处理按键扫描中断的内部线程所用栈的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HT16K33_KEYSCAN && CONFIG_LED
```

**默认值（Defaults）**

```text
400
```

**定义位置（Location）**：[`drivers/led/Kconfig.ht16k33:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.ht16k33#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → HT16K33 LED 驱动 → 按键扫描（Keyscan）支持

**配置项引用（Symbol References）**：[`CONFIG_HT16K33_KEYSCAN`](P114_drivers_led_配置项参考.md#CONFIG_HT16K33_KEYSCAN)、[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)。

<a id="CONFIG_HT16K33_KEYSCAN_POLL_MSEC"></a>

## 114.6 `CONFIG_HT16K33_KEYSCAN_POLL_MSEC`

**提示（Prompt）**：按键扫描轮询间隔（Poll Interval），单位为毫秒

**说明（Help）**

按键扫描轮询间隔，单位为毫秒。仅在没有中断线时使用轮询。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HT16K33_KEYSCAN && CONFIG_LED
```

**默认值（Defaults）**

```text
200
```

**取值范围（Ranges）**

```text
[20, 10000]
```

**定义位置（Location）**：[`drivers/led/Kconfig.ht16k33:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.ht16k33#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动 → HT16K33 LED 驱动 → 按键扫描（Keyscan）支持

**配置项引用（Symbol References）**：[`CONFIG_HT16K33_KEYSCAN`](P114_drivers_led_配置项参考.md#CONFIG_HT16K33_KEYSCAN)、[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)。

<a id="CONFIG_IS31FL319X"></a>

## 114.7 `CONFIG_IS31FL319X`

**提示（Prompt）**：IS31FL319x LED 驱动

**说明（Help）**

启用 Lumissil Microsystems（ISSI 的一个部门）的 LED 驱动。支持多色（例如 RGB、RGBW）和单色（即单通道）LED，也支持混合配置。支持型号：

- IS31FL3193：3 个通道。
- IS31FL3194：3 个通道。
- IS31FL3197：4 个通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ISSI_IS31FL3193_ENABLED || DT_HAS_ISSI_IS31FL3194_ENABLED || DT_HAS_ISSI_IS31FL3197_ENABLED) && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.is31fl319x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.is31fl319x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_IS31FL3216A"></a>

## 114.8 `CONFIG_IS31FL3216A`

**提示（Prompt）**：IS31FL3216A LED 驱动

**说明（Help）**

启用 Lumissil Microsystems（ISSI 的一个部门）IS31FL3216A 的 LED 驱动。此芯片最多支持 16 个由脉宽调制（PWM）控制的 LED。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ISSI_IS31FL3216A_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.is31fl3216a:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.is31fl3216a#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_IS31FL3733"></a>

## 114.9 `CONFIG_IS31FL3733`

**提示（Prompt）**：IS31FL3733 LED 驱动

**说明（Help）**

启用 IS31FL3733 的 LED 驱动。IS31FL3733 是矩阵 LED 驱动器，每个 LED 最大电流为 3.29 mA，或整个 12×16 点阵中所有 LED 的总电流最大为 42 mA。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ISSI_IS31FL3733_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.is31fl3733:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.is31fl3733#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LED"></a>

## 114.10 `CONFIG_LED`

**提示（Prompt）**：发光二极管（Light-Emitting Diode，LED）驱动

**说明（Help）**

在系统配置中纳入 LED 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/led/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_LEDS_GROUP_MULTICOLOR"></a>

## 114.11 `CONFIG_LEDS_GROUP_MULTICOLOR`

**提示（Prompt）**：LED 组多色驱动（Group Multi-color Driver）

**说明（Help）**

启用此驱动，以支持由多个单色 LED 组成的多色 LED。详情参见 `leds-group-multicolor` 设备树绑定（DT Binding）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LEDS_GROUP_MULTICOLOR_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/led/Kconfig.leds-group-multicolor:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.leds-group-multicolor#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)。

<a id="CONFIG_LED_AW9523B"></a>

## 114.12 `CONFIG_LED_AW9523B`

**提示（Prompt）**：AW9523B LED 驱动

**说明（Help）**

启用 AW9523B LED 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AWINIC_AW9523B_LED_ENABLED && CONFIG_LED
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

**定义位置（Location）**：[`drivers/led/Kconfig.aw9523b:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.aw9523b#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_LED_AXP192_AXP2101"></a>

## 114.13 `CONFIG_LED_AXP192_AXP2101`

**提示（Prompt）**：X-Powers AXP192/AXP2101 LED 驱动

**说明（Help）**

启用 AXP192/AXP2101 LED 驱动。AXP192 和 AXP2101 是多功能集成电源管理芯片（PMIC），此驱动用于其 LED 控制器功能。该控制器可通过寄存器控制点亮，也可以响应充电状态点亮。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_X_POWERS_AXP192_LED_ENABLED || DT_HAS_X_POWERS_AXP2101_LED_ENABLED) && (DT_HAS_X_POWERS_AXP192_ENABLED || DT_HAS_X_POWERS_AXP2101_ENABLED) && CONFIG_LED
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

**定义位置（Location）**：[`drivers/led/Kconfig.axp192:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.axp192#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_LED_DAC"></a>

## 114.14 `CONFIG_LED_DAC`

**提示（Prompt）**：DAC LED 驱动

**说明（Help）**

启用数模转换器（DAC）LED 驱动。通常在 DAC 与 LED 之间接入压控电流源（Voltage Controlled Current Source，VCCS）。也可能用此驱动从 DAC 直接为 LED 供电，但 `LED_PWM` 很可能更适合这一用途。若不使用 VCCS，应仔细检查 DAC 的能力，并启用输出缓冲器（Output Buffer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_DAC_LEDS_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DAC
```

**定义位置（Location）**：[`drivers/led/Kconfig.dac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.dac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)。

<a id="CONFIG_LED_FAKE"></a>

## 114.15 `CONFIG_LED_FAKE`

**提示（Prompt）**：模拟 LED 控制器驱动程序。

**说明（Help）**

启用基于伪函数框架（FFF）的模拟 LED 控制器驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FAKE_LEDS_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/led/Kconfig.fake:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.fake#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)。

<a id="CONFIG_LED_GPIO"></a>

## 114.16 `CONFIG_LED_GPIO`

**提示（Prompt）**：GPIO LED 驱动

**说明（Help）**

启用 GPIO LED 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_LEDS_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/led/Kconfig.gpio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.gpio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LED_INIT_PRIORITY"></a>

## 114.17 `CONFIG_LED_INIT_PRIORITY`

**提示（Prompt）**：LED 初始化优先级（Initialization Priority）

**说明（Help）**

LED 驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LED
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/led/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)。

<a id="CONFIG_LED_NPM10XX"></a>

## 114.18 `CONFIG_LED_NPM10XX`

**提示（Prompt）**：nPM10xx LED 驱动

**说明（Help）**

启用 nPM10xx LED 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM10XX_LED_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.npm10xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.npm10xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LED_NPM13XX"></a>

## 114.19 `CONFIG_LED_NPM13XX`

**提示（Prompt）**：nPM13xx LED 驱动

**说明（Help）**

启用 nPM13xx LED 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NORDIC_NPM1300_LED_ENABLED || DT_HAS_NORDIC_NPM1304_LED_ENABLED) && CONFIG_LED
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

**定义位置（Location）**：[`drivers/led/Kconfig.npm13xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.npm13xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_LED_PWM"></a>

## 114.20 `CONFIG_LED_PWM`

**提示（Prompt）**：PWM LED 驱动

**说明（Help）**

启用脉宽调制（PWM）LED 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PWM_LEDS_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PWM
```

**定义位置（Location）**：[`drivers/led/Kconfig.pwm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.pwm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM)。

<a id="CONFIG_LED_SCT2024"></a>

## 114.21 `CONFIG_LED_SCT2024`

**提示（Prompt）**：SCT2024 LED 控制器支持

**说明（Help）**

此选项启用 SCT2024 LED 控制器驱动支持。SCT2024 是通过 SPI 通信的 16 通道恒流（Constant Current）LED 驱动器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SCT_SCT2024_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/led/Kconfig.sct2024:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.sct2024#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_LED_SHELL"></a>

## 114.22 `CONFIG_LED_SHELL`

**提示（Prompt）**：LED 命令行（Shell）

**说明（Help）**

启用用于测试的 LED Shell。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_LED
```

**定义位置（Location）**：[`drivers/led/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)。

<a id="CONFIG_LED_XEC"></a>

## 114.23 `CONFIG_LED_XEC`

**提示（Prompt）**：Microchip XEC BB-LED 驱动

**说明（Help）**

启用 MEC15xx 和 MEC172x 的 Microchip XEC 呼吸／闪烁（Breathing-Blinking）LED 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_BBLED_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/led/Kconfig.xec:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.xec#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_LP3943"></a>

## 114.24 `CONFIG_LP3943`

**提示（Prompt）**：LP3943 LED 驱动

**说明（Help）**

启用 LP3943 LED 驱动。LP3943 有 16 个通道，每个通道都具有按指定速率工作的多种可编程状态。每个通道可为每个 LED 提供最大 25 mA 的驱动电流。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_LP3943_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.lp3943:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.lp3943#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LP50XX"></a>

## 114.25 `CONFIG_LP50XX`

**提示（Prompt）**：LP50XX LED 控制器

**说明（Help）**

启用 Texas Instruments LP50XX I²C LED 控制器驱动。支持 LP5009、LP5012、LP5018、LP5024、LP5030 和 LP5036。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_LP5009_ENABLED || DT_HAS_TI_LP5012_ENABLED || DT_HAS_TI_LP5018_ENABLED || DT_HAS_TI_LP5024_ENABLED || DT_HAS_TI_LP5030_ENABLED || DT_HAS_TI_LP5036_ENABLED) && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.lp50xx:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.lp50xx#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LP5562"></a>

## 114.26 `CONFIG_LP5562`

**提示（Prompt）**：LP5562 LED 驱动

**说明（Help）**

启用 LP5562 LED 驱动。LP5562 有 4 个通道（RGBW），每个通道可为每个 LED 提供最大 25.5 mA 的驱动电流。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_LP5562_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.lp5562:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.lp5562#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LP5569"></a>

## 114.27 `CONFIG_LP5569`

**提示（Prompt）**：LP5569 LED 驱动

**说明（Help）**

启用 LP5569 LED 驱动。LP5569 有 9 个通道，每个通道可为每个 LED 提供最大 25.5 mA 的驱动电流。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_LP5569_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.lp5569:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.lp5569#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LP586X"></a>

## 114.28 `CONFIG_LP586X`

**提示（Prompt）**：LP586X LED 矩阵控制器（Matrix Controller）

**说明（Help）**

启用 Texas Instruments LP586X I²C LED 矩阵控制器驱动。支持 LP5860、LP5861、LP5862、LP5864、LP5866 和 LP5868。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_LP5860_ENABLED || DT_HAS_TI_LP5861_ENABLED || DT_HAS_TI_LP5862_ENABLED || DT_HAS_TI_LP5864_ENABLED || DT_HAS_TI_LP5866_ENABLED || DT_HAS_TI_LP5868_ENABLED) && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.lp586x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.lp586x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MODULINO_BUTTONS_LEDS"></a>

## 114.29 `CONFIG_MODULINO_BUTTONS_LEDS`

**提示（Prompt）**：Arduino Modulino Buttons 的 LED

**说明（Help）**

启用 Arduino Modulino Buttons 的 LED 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARDUINO_MODULINO_BUTTONS_LEDS_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.modulino:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.modulino#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_NATIVE_LINUX_LEDS"></a>

## 114.30 `CONFIG_NATIVE_LINUX_LEDS`

**提示（Prompt）**：基于原生 Linux LED 的 LED 设备

**说明（Help）**

启用以 Linux sysfs LED 为后端的 native_sim LED 驱动。每个设备树 `native-linux-leds` 子节点通过 `path` 属性提供 Linux LED 名称，即 `/sys/class/leds` 下的名称；Zephyr LED 亮度请求映射到 `/sys/class/leds/<path>/brightness`。译注：这里是原文中的 Linux 系统接口路径，并非本仓库所在位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_LINUX_LEDS_ENABLED && CONFIG_ARCH_POSIX && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NATIVE_USE_NSI_ERRNO
```

**定义位置（Location）**：[`drivers/led/Kconfig.linux-leds:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.linux-leds#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)。

<a id="CONFIG_NCP5623"></a>

## 114.31 `CONFIG_NCP5623`

**提示（Prompt）**：NCP5623 LED 驱动

**说明（Help）**

启用 Onsemi NCP5623 I²C LED 控制器驱动。控制器和驱动支持两种硬件配置：

- 一个三通道（RGB）LED。
- 三个单通道 LED。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ONNN_NCP5623_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.ncp5623:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.ncp5623#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_PCA953X"></a>

## 114.32 `CONFIG_PCA953X`

**提示（Prompt）**：PCA953x LED 驱动

**说明（Help）**

启用 NXP PCA953x LED 调光器（Dimmer）系列的驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NXP_PCA9530_ENABLED || DT_HAS_NXP_PCA9531_ENABLED || DT_HAS_NXP_PCA9532_ENABLED || DT_HAS_NXP_PCA9533_ENABLED) && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.pca953x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.pca953x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_PCA9633"></a>

## 114.33 `CONFIG_PCA9633`

**提示（Prompt）**：PCA9633 LED 驱动

**说明（Help）**

启用 PCA9633 LED 驱动。PCA9633 有 4 个通道，每个通道具有多种可编程状态，并可为每个 LED 提供最大 25 mA 的驱动电流。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCA9633_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.pca9633:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.pca9633#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TLC59108"></a>

## 114.34 `CONFIG_TLC59108`

**提示（Prompt）**：TLC59108 LED 驱动

**说明（Help）**

启用 TLC59108 LED 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TLC59108_ENABLED && CONFIG_LED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led/Kconfig.tlc59108:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/Kconfig.tlc59108#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）驱动

**配置项引用（Symbol References）**：[`CONFIG_LED`](P114_drivers_led_配置项参考.md#CONFIG_LED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<!-- kconfig-navigation -->

[上一章](P113_drivers_ipm_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P115_drivers_led_strip_配置项参考.md)
