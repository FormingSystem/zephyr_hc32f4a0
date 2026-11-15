---
id: learning.zephyr-docs.kconfig-reference.page-115
title: "`drivers/led_strip`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第115章\_`drivers/led_strip`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/led_strip` 的 22 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_APA102_STRIP"></a>

## 115.1 `CONFIG_APA102_STRIP`

**提示（Prompt）**：APA102 SPI LED 灯带驱动（Strip Driver）

**说明（Help）**

启用串接 APA102 RGB LED 的灯带驱动。这类产品由 Adafruit 以 DotStar 名称销售，其他厂商也以 Superled 名称销售。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_APA_APA102_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI if n
CONFIG_LED_STRIP_RGB_SCRATCH
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.apa102:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.apa102#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_LED_STRIP_RGB_SCRATCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_STRIP_RGB_SCRATCH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LED_STRIP_RGB_SCRATCH`。

<a id="CONFIG_DELAY_T0H"></a>

## 115.2 `CONFIG_DELAY_T0H`

**提示（Prompt）**：0 位高电平脉冲延迟（High Pulse Delay）

**说明（Help）**

产生 0 位高电平时段延迟所需的 NOP 汇编操作数量，默认时长为 350 ns。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WS2812_STRIP_GPIO && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
0 if n
0 if n
3
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → WS2812 LED 灯带 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_WS2812_STRIP_GPIO`](P115_drivers_led_strip_配置项参考.md#CONFIG_WS2812_STRIP_GPIO)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_DELAY_T0L"></a>

## 115.3 `CONFIG_DELAY_T0L`

**提示（Prompt）**：0 位低电平脉冲延迟（Low Pulse Delay）

**说明（Help）**

产生 0 位低电平时段延迟所需的 NOP 汇编操作数量，默认时长为 800 ns。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WS2812_STRIP_GPIO && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
0 if n
0 if n
8
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → WS2812 LED 灯带 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_WS2812_STRIP_GPIO`](P115_drivers_led_strip_配置项参考.md#CONFIG_WS2812_STRIP_GPIO)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_DELAY_T1H"></a>

## 115.4 `CONFIG_DELAY_T1H`

**提示（Prompt）**：1 位高电平脉冲延迟（High Pulse Delay）

**说明（Help）**

产生 1 位高电平时段延迟所需的 NOP 汇编操作数量，默认时长为 700 ns。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WS2812_STRIP_GPIO && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
0 if n
0 if n
7
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → WS2812 LED 灯带 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_WS2812_STRIP_GPIO`](P115_drivers_led_strip_配置项参考.md#CONFIG_WS2812_STRIP_GPIO)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_DELAY_T1L"></a>

## 115.5 `CONFIG_DELAY_T1L`

**提示（Prompt）**：1 位低电平脉冲延迟（Low Pulse Delay）

**说明（Help）**

产生 1 位低电平时段延迟所需的 NOP 汇编操作数量，默认时长为 600 ns。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WS2812_STRIP_GPIO && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
0 if n
0 if n
6
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → WS2812 LED 灯带 GPIO 驱动

**配置项引用（Symbol References）**：[`CONFIG_WS2812_STRIP_GPIO`](P115_drivers_led_strip_配置项参考.md#CONFIG_WS2812_STRIP_GPIO)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_LED_STRIP"></a>

## 115.6 `CONFIG_LED_STRIP`

**提示（Prompt）**：发光二极管（Light-Emitting Diode，LED）灯带驱动

**说明（Help）**

在系统配置中纳入 LED 灯带驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_LED_STRIP_MATRIX
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP_MATRIX`](P077_drivers_display_配置项参考_1.md#CONFIG_LED_STRIP_MATRIX)。

<a id="CONFIG_LED_STRIP_INIT_PRIORITY"></a>

## 115.7 `CONFIG_LED_STRIP_INIT_PRIORITY`

**提示（Prompt）**：LED 灯带初始化优先级（Initialization Priority）

**说明（Help）**

LED 灯带驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_LED_STRIP_SHELL"></a>

## 115.8 `CONFIG_LED_STRIP_SHELL`

**提示（Prompt）**：LED 灯带命令行（Shell）

**说明（Help）**

启用用于测试的 LED 灯带 Shell。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_LED_STRIP
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_LED_STRIP_SHELL_MAX_PIXELS"></a>

## 115.9 `CONFIG_LED_STRIP_SHELL_MAX_PIXELS`

**提示（Prompt）**：Shell 可访问的最大 LED 数量

**说明（Help）**

需要列出像素颜色（Pixel Color）的命令，接受的像素数不会超过此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LED_STRIP_SHELL && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → LED 灯带命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP_SHELL`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP_SHELL)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_LPD880X_STRIP"></a>

## 115.10 `CONFIG_LPD880X_STRIP`

**提示（Prompt）**：LPD880x SPI LED 灯带驱动

**说明（Help）**

启用菊花链（Daisy Chain）连接的 LPD880x（LPD8803、LPD8806 或兼容型号）设备的 LED 灯带驱动。每个 LPD880x LED 驱动芯片有若干输出通道，LPD8803 为 3 个，LPD8806 为 6 个；可通过简化 SPI 接口（仅 SDI 和 CLK 线）以 7 位分辨率设置 PWM 占空比（Duty Cycle）。每个芯片还提供数据和时钟输出引脚，用于菊花链连接灯带。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_GREELED_LPD8803_ENABLED || DT_HAS_GREELED_LPD8806_ENABLED) && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI if n || n
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.lpd880x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.lpd880x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_MODULINO_PIXELS"></a>

## 115.11 `CONFIG_MODULINO_PIXELS`

**提示（Prompt）**：Arduino Modulino Pixels

**说明（Help）**

启用 Arduino Modulino Pixels 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARDUINO_MODULINO_PIXELS_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.modulino:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.modulino#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TLC5971_STRIP"></a>

## 115.12 `CONFIG_TLC5971_STRIP`

**提示（Prompt）**：TLC5971 及兼容型号的 LED 灯带驱动

**说明（Help）**

启用菊花链（Daisy Chain）连接的 TLC5971 类设备的 LED 灯带驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI && DT_HAS_TI_TLC5971_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.tlc5971:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.tlc5971#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_TLC59731_STRIP"></a>

## 115.13 `CONFIG_TLC59731_STRIP`

**提示（Prompt）**：TLC59731 LED 控制器

**说明（Help）**

启用 Texas Instruments TLC59731 EasySet LED 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TLC59731_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.tlc59731:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.tlc59731#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_WS2812_STRIP_BFLB_WO"></a>

## 115.14 `CONFIG_WS2812_STRIP_BFLB_WO`

**提示（Prompt）**：通过 BFLB Wire Out 驱动 WS2812 LED 灯带

**说明（Help）**

启用使用 BouffaloLab GPIO FIFO / Wire Out 的 WS2812 及兼容型号 LED 灯带驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WORLDSEMI_WS2812_BFLB_WO_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_GPIO_BL61X_808_WO
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_GPIO_BL61X_808_WO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_BL61X_808_WO)。

<a id="CONFIG_WS2812_STRIP_BFLB_WO_ASYNC"></a>

## 115.15 `CONFIG_WS2812_STRIP_BFLB_WO_ASYNC`

**提示（Prompt）**：通过 BFLB Wire Out 异步驱动 WS2812 LED 灯带

**说明（Help）**

启用 BFLB GPIO FIFO / Wire Out WS2812 驱动的异步模式（Asynchronous Mode）。这可能使用大量 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WS2812_STRIP_BFLB_WO && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → 通过 BFLB Wire Out 驱动 WS2812 LED 灯带

**配置项引用（Symbol References）**：[`CONFIG_WS2812_STRIP_BFLB_WO`](P115_drivers_led_strip_配置项参考.md#CONFIG_WS2812_STRIP_BFLB_WO)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_WS2812_STRIP_GPIO"></a>

## 115.16 `CONFIG_WS2812_STRIP_GPIO`

**提示（Prompt）**：WS2812 LED 灯带 GPIO 驱动

**说明（Help）**

启用通过 GPIO 直接控制 WS2812 及兼容型号 LED 灯带的驱动。GPIO 驱动使用内联汇编（Inline Assembly）进行位操作模拟（Bit Banging），并非适用于所有 SoC。注意，此驱动不兼容 Everlight B1414 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WORLDSEMI_WS2812_GPIO_ENABLED && (CONFIG_SOC_SERIES_NRF91 || CONFIG_SOC_SERIES_NRF51 || CONFIG_SOC_SERIES_NRF52 || CONFIG_SOC_SERIES_NRF53) && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_SERIES_NRF51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)。

<a id="CONFIG_WS2812_STRIP_I2S"></a>

## 115.17 `CONFIG_WS2812_STRIP_I2S`

**提示（Prompt）**：WS2812 LED 灯带 I²S 驱动

**说明（Help）**

启用使用 I²S 的 WS2812 及兼容型号 LED 灯带驱动。它使用 I²S 外设，内存用量为每种颜色 4 字节乘以像素数量，另需少量内存处理起始和结束延迟。复位延迟（Reset Delay）的分辨率较粗，约为 20 μs。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WORLDSEMI_WS2812_I2S_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2S if n
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_I2S`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S)。

<a id="CONFIG_WS2812_STRIP_PULSE_IO"></a>

## 115.18 `CONFIG_WS2812_STRIP_PULSE_IO`

**提示（Prompt）**：WS2812 LED 灯带 pulse_io 驱动

**说明（Help）**

启用使用 CELL 模式下 `pulse_io` 控制器通道的 WS2812 及兼容型号 LED 灯带驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WORLDSEMI_WS2812_PULSE_IO_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PULSE_IO
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_PULSE_IO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PULSE_IO)。

<a id="CONFIG_WS2812_STRIP_RPI_PICO_PIO"></a>

## 115.19 `CONFIG_WS2812_STRIP_RPI_PICO_PIO`

**提示（Prompt）**：WS2812 LED 灯带 Raspberry Pi Pico PIO 驱动

**说明（Help）**

启用使用 Raspberry Pi Pico 可编程 I/O（PIO）的 WS2812 及兼容型号 LED 灯带驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WORLDSEMI_WS2812_RPI_PICO_PIO_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_PIO
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_PICOSDK_USE_PIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_PIO)。

<a id="CONFIG_WS2812_STRIP_SPI"></a>

## 115.20 `CONFIG_WS2812_STRIP_SPI`

**提示（Prompt）**：WS2812 LED 灯带 SPI 驱动

**说明（Help）**

启用使用 SPI 的 WS2812 及兼容型号 LED 灯带驱动。SPI 驱动具有可移植性，但需要显著更多内存：每一位像素数据需要 1 字节开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WORLDSEMI_WS2812_SPI_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI if n
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_WS2812_STRIP_SPI_FORCE_NOCACHE"></a>

## 115.21 `CONFIG_WS2812_STRIP_SPI_FORCE_NOCACHE`

**提示（Prompt）**：将 LED 缓冲区放入 `__nocache` 段（Section）

**说明（Help）**

使用 DMA 进行 SPI 通信时，将 WS2812 SPI 缓冲区放入 `__nocache` 段，确保其位于不可缓存内存（Uncached Memory）中，因为 DMA 通常要求访问不可缓存区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WS2812_STRIP_SPI && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y if CONFIG_DCACHE && CONFIG_DMA
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动 → WS2812 LED 灯带 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_WS2812_STRIP_SPI`](P115_drivers_led_strip_配置项参考.md#CONFIG_WS2812_STRIP_SPI)、[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_WS2812_STRIP_UART"></a>

## 115.22 `CONFIG_WS2812_STRIP_UART`

**提示（Prompt）**：WS2812 LED 灯带 UART 驱动

**说明（Help）**

启用使用 UART 的 WS2812 及兼容型号 LED 灯带驱动。此方法需要高速 UART，并需精心构造字节帧，以满足 WS2812 严格的时序协议（Timing Protocol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WORLDSEMI_WS2812_UART_ENABLED && CONFIG_LED_STRIP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL if n
CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`drivers/led_strip/Kconfig.ws2812:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/Kconfig.ws2812#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 发光二极管（Light-Emitting Diode，LED）灯带驱动

**配置项引用（Symbol References）**：[`CONFIG_LED_STRIP`](P115_drivers_led_strip_配置项参考.md#CONFIG_LED_STRIP)、[`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)。

<!-- kconfig-navigation -->

[上一章](P114_drivers_led_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P116_drivers_lin_配置项参考.md)
