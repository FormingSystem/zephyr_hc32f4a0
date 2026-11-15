---
id: learning.zephyr-docs.kconfig-reference.page-111
title: "`drivers/input`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第111章\_`drivers/input`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/input` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BEE_INPUT_KEYSCAN_AUTOSCAN_MODE"></a>

## 111.1 `CONFIG_BEE_INPUT_KEYSCAN_AUTOSCAN_MODE`

**提示（Prompt）**：配置 Bee 按键扫描模式（Keyscan Scan Mode）

**说明（Help）**

自动模式（Auto Mode）由硬件触发扫描，扫描间隔更短、更精确，适用于需要更高扫描速度、对延迟敏感的场景。手动模式（Manual Mode）下，启用电源管理（PM）功能后，系统可在两次扫描之间进入睡眠模式，适用于以能效为先、对功耗敏感的场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_BEE_KEYSCAN && CONFIG_INPUT
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/input/Kconfig.bee_keyscan:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.bee_keyscan#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Realtek Bee 系列输入按键扫描（Keyscan）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_BEE_KEYSCAN`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_BEE_KEYSCAN)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_ADAFRUIT_SEESAW_GAMEPAD"></a>

## 111.2 `CONFIG_INPUT_ADAFRUIT_SEESAW_GAMEPAD`

**提示（Prompt）**：带 seesaw 的 Adafruit Mini I²C Gamepad

**说明（Help）**

启用带 seesaw 的 Adafruit Mini I²C Gamepad（产品 5743）驱动。通过 Zephyr 输入子系统（Input Subsystem）报告双轴摇杆（`ABS_X`/`ABS_Y`）及六个按键（A、B、X、Y、Start、Select）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADAFRUIT_SEESAW_GAMEPAD_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/input/Kconfig.adafruit_seesaw_gamepad:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.adafruit_seesaw_gamepad#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INPUT_ADC_KEYS"></a>

## 111.3 `CONFIG_INPUT_ADC_KEYS`

**提示（Prompt）**：连接到 ADC 的电阻梯形网络按键（Resistor Ladder Buttons）

**说明（Help）**

启用连接到 ADC 的电阻梯形网络按键支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADC_KEYS_ENABLED && CONFIG_ADC && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.adc_keys:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.adc_keys#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_ANALOG_AXIS"></a>

## 111.4 `CONFIG_INPUT_ANALOG_AXIS`

**提示（Prompt）**：基于 ADC 的模拟轴输入（Analog Axis Input）驱动

**说明（Help）**

基于 ADC 的模拟轴输入（Analog Axis Input）驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANALOG_AXIS_ENABLED && CONFIG_MULTITHREADING && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/input/Kconfig.analog_axis:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.analog_axis#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_INPUT_ANALOG_AXIS_SETTINGS"></a>

## 111.5 `CONFIG_INPUT_ANALOG_AXIS_SETTINGS`

**提示（Prompt）**：模拟轴设置（Analog Axis Settings）支持

**说明（Help）**

模拟轴驱动的设置（Settings）支持，提供 `analog_axis_calibration_save()` 函数，将校准值保存到设置中，并在启动时自动加载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_INPUT_ANALOG_AXIS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.analog_axis:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.analog_axis#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → 基于 ADC 的模拟轴输入（Analog Axis Input）驱动

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_INPUT_ANALOG_AXIS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_ANALOG_AXIS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_ANALOG_AXIS_SETTINGS_MAX_AXES"></a>

## 111.6 `CONFIG_INPUT_ANALOG_AXIS_SETTINGS_MAX_AXES`

**提示（Prompt）**：设置中支持的最大轴数（Maximum Axes）。

**说明（Help）**

可在设置中保存校准值（Calibration Value）的最大轴数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_ANALOG_AXIS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/input/Kconfig.analog_axis:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.analog_axis#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → 基于 ADC 的模拟轴输入（Analog Axis Input）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_ANALOG_AXIS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_ANALOG_AXIS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_ANALOG_AXIS_THREAD_PRIORITY"></a>

## 111.7 `CONFIG_INPUT_ANALOG_AXIS_THREAD_PRIORITY`

**提示（Prompt）**：模拟轴线程优先级（Thread Priority）

**说明（Help）**

模拟轴线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_ANALOG_AXIS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/input/Kconfig.analog_axis:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.analog_axis#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → 基于 ADC 的模拟轴输入（Analog Axis Input）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_ANALOG_AXIS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_ANALOG_AXIS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_ANALOG_AXIS_THREAD_STACK_SIZE"></a>

## 111.8 `CONFIG_INPUT_ANALOG_AXIS_THREAD_STACK_SIZE`

**提示（Prompt）**：模拟轴线程栈大小（Stack Size）

**说明（Help）**

模拟轴线程所用栈的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_ANALOG_AXIS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
762
```

**定义位置（Location）**：[`drivers/input/Kconfig.analog_axis:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.analog_axis#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → 基于 ADC 的模拟轴输入（Analog Axis Input）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_ANALOG_AXIS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_ANALOG_AXIS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_BEE_KEYSCAN"></a>

## 111.9 `CONFIG_INPUT_BEE_KEYSCAN`

**提示（Prompt）**：Realtek Bee 系列输入按键扫描（Keyscan）驱动

**说明（Help）**

此选项启用 Realtek Bee 系统级芯片（SoC）的输入按键扫描驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_KEYSCAN_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INPUT_KBD_MATRIX
CONFIG_HAL_REALTEK_BEE_KEYSCAN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/input/Kconfig.bee_keyscan:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.bee_keyscan#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_HAL_REALTEK_BEE_KEYSCAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_KEYSCAN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_KEYSCAN`。

<a id="CONFIG_INPUT_BFLB_IRX"></a>

## 111.10 `CONFIG_INPUT_BFLB_IRX`

**提示（Prompt）**：Bouffalolab 红外接收器（Infrared Receiver）

**说明（Help）**

此选项启用 Bouffalolab 红外接收器外设的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_IRX_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/input/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_INPUT_CAP12XX"></a>

## 111.11 `CONFIG_INPUT_CAP12XX`

**提示（Prompt）**：Microchip CAP12xx 多通道电容式触摸传感器（Capacitive Touch Sensor）驱动

**说明（Help）**

启用 Microchip CAP12xx 多通道电容式触摸传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_CAP12XX_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/input/Kconfig.cap12xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.cap12xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INPUT_CF1133"></a>

## 111.12 `CONFIG_INPUT_CF1133`

**提示（Prompt）**：CF1133 电容式触摸面板（Capacitive Touch Panel）驱动

**说明（Help）**

启用 Sitronix 电容式触摸面板控制器驱动。此驱动应支持 CF1133。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SITRONIX_CF1133_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_INPUT_TOUCH
```

**定义位置（Location）**：[`drivers/input/Kconfig.cf1133:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.cf1133#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_CF1133_INTERRUPT"></a>

## 111.13 `CONFIG_INPUT_CF1133_INTERRUPT`

**提示（Prompt）**：中断（Interrupt）

**说明（Help）**

启用中断支持，要求所有 CF1133 实例都连接 INT GPIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CF1133 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.cf1133:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.cf1133#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CF1133 电容式触摸面板（Capacitive Touch Panel）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CF1133`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CF1133)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CF1133_PERIOD_MS"></a>

## 111.14 `CONFIG_INPUT_CF1133_PERIOD_MS`

**提示（Prompt）**：采样周期（Sample Period）

**说明（Help）**

轮询模式（Polling Mode）下的采样周期，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_CF1133_INTERRUPT && CONFIG_INPUT_CF1133 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.cf1133:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.cf1133#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CF1133 电容式触摸面板（Capacitive Touch Panel）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CF1133_INTERRUPT`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CF1133_INTERRUPT)、[`CONFIG_INPUT_CF1133`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CF1133)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CH9350L"></a>

## 111.15 `CONFIG_INPUT_CH9350L`

**提示（Prompt）**：WinChipHead CH9350L USB HID 转 UART 控制芯片

**说明（Help）**

此选项启用 WinChipHead CH9350L USB 人机接口设备（HID）转 UART 控制芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_CH9350L_ENABLED && CONFIG_SERIAL_SUPPORT_INTERRUPT && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`drivers/input/Kconfig.ch9350l:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ch9350l#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_INPUT_CH9350L_FRAME_COUNT"></a>

## 111.16 `CONFIG_INPUT_CH9350L_FRAME_COUNT`

**提示（Prompt）**：可分配帧数（Allocatable Frames）

**说明（Help）**

一次可以排队的输入帧（Input Frame）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CH9350L && CONFIG_INPUT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`drivers/input/Kconfig.ch9350l:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ch9350l#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → WinChipHead CH9350L USB HID 转 UART 控制芯片

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CH9350L`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CH9350L)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CHSC5X"></a>

## 111.17 `CONFIG_INPUT_CHSC5X`

**提示（Prompt）**：CHSC5X 电容式触摸面板（Capacitive Touch Panel）驱动

**说明（Help）**

启用 Chipsemi 电容式触摸面板控制器的 CHSC5X 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CHIPSEMI_CHSC5X_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_I2C
CONFIG_INPUT_TOUCH
```

**定义位置（Location）**：[`drivers/input/Kconfig.chsc5x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.chsc5x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_CHSC5X_VERIFY_IC_TYPE"></a>

## 111.18 `CONFIG_INPUT_CHSC5X_VERIFY_IC_TYPE`

**提示（Prompt）**：芯片类型验证（IC Type Verification）

**说明（Help）**

此选项启用芯片类型验证，会在初始化期间额外引入 100 ms 延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CHSC5X && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.chsc5x:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.chsc5x#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CHSC5X 电容式触摸面板（Capacitive Touch Panel）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CHSC5X`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CHSC5X)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CHSC6X"></a>

## 111.19 `CONFIG_INPUT_CHSC6X`

**提示（Prompt）**：使用 CHSC6X 电容式触摸面板驱动

**说明（Help）**

启用 CHSC6X 触摸面板的树外驱动（Out-of-tree Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_CHIPSEMI_CHSC6X_ENABLED || DT_HAS_CHIPSEMI_CHSC6540_ENABLED) && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_I2C
CONFIG_INPUT_TOUCH
```

**定义位置（Location）**：[`drivers/input/Kconfig.chsc6x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.chsc6x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_CRSF"></a>

## 111.20 `CONFIG_INPUT_CRSF`

**提示（Prompt）**：CRSF 驱动

**说明（Help）**

启用 CRSF 遥控器（Remote Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TBS_CRSF_ENABLED && CONFIG_UART_ASYNC_API && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`drivers/input/Kconfig.crsf:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.crsf#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_INPUT_CRSF_CHANNEL_VALUE_ONE"></a>

## 111.21 `CONFIG_INPUT_CRSF_CHANNEL_VALUE_ONE`

**提示（Prompt）**：判定 `INPUT_EV_KEY` 值为 1 的大于阈值（>）

**说明（Help）**

CRSF 为数字开关发送模拟值。此配置值设置将模拟值解释为逻辑 1 的阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CRSF && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1800
```

**定义位置（Location）**：[`drivers/input/Kconfig.crsf:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.crsf#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CRSF 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CRSF`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CRSF)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CRSF_CHANNEL_VALUE_ZERO"></a>

## 111.22 `CONFIG_INPUT_CRSF_CHANNEL_VALUE_ZERO`

**提示（Prompt）**：判定 `INPUT_EV_KEY` 值为 0 的小于阈值（<）

**说明（Help）**

CRSF 为数字开关发送模拟值。此配置值设置将模拟值解释为逻辑 0 的阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CRSF && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1200
```

**定义位置（Location）**：[`drivers/input/Kconfig.crsf:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.crsf#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CRSF 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CRSF`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CRSF)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CRSF_REPORT_FILTER"></a>

## 111.23 `CONFIG_INPUT_CRSF_REPORT_FILTER`

**提示（Prompt）**：触发报告的最小信号变化（Minimal Signal Change）

**说明（Help）**

CRSF 信号往往有些噪声，可以增大阈值以减少输入事件的数量。设为 0 表示不进行过滤。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CRSF && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/input/Kconfig.crsf:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.crsf#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CRSF 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CRSF`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CRSF)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CRSF_SEND_SYNC"></a>

## 111.24 `CONFIG_INPUT_CRSF_SEND_SYNC`

**提示（Prompt）**：每个 CRSF 帧都向输入子系统发送同步（Sync）

**说明（Help）**

向输入子系统发送带同步位（Sync Bit）的同步消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CRSF && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.crsf:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.crsf#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CRSF 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CRSF`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CRSF)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CRSF_THREAD_PRIORITY"></a>

## 111.25 `CONFIG_INPUT_CRSF_THREAD_PRIORITY`

**提示（Prompt）**：CRSF 线程优先级（Thread Priority）

**说明（Help）**

CRSF 线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CRSF && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/input/Kconfig.crsf:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.crsf#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CRSF 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CRSF`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CRSF)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CRSF_THREAD_STACK_SIZE"></a>

## 111.26 `CONFIG_INPUT_CRSF_THREAD_STACK_SIZE`

**提示（Prompt）**：CRSF 线程栈大小（Stack Size）

**说明（Help）**

CRSF 线程所用栈的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CRSF && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/input/Kconfig.crsf:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.crsf#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CRSF 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CRSF`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CRSF)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CRSF_USE_DTCM_FOR_DMA_BUFFER"></a>

## 111.27 `CONFIG_INPUT_CRSF_USE_DTCM_FOR_DMA_BUFFER`

**提示（Prompt）**：使用 DTCM 存放硬件 DMA 缓冲区（Hardware DMA Buffers）

**说明（Help）**

将硬件 DMA 缓冲区放入数据紧耦合存储器（DTCM），以降低延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/input/Kconfig.crsf:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.crsf#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CRSF 驱动

<a id="CONFIG_INPUT_CST8XX"></a>

## 111.28 `CONFIG_INPUT_CST8XX`

**提示（Prompt）**：CST8XX 电容式触摸面板驱动

**说明（Help）**

启用 Hynitron CST8XX 触摸面板驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HYNITRON_CST8XX_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_INPUT_TOUCH
```

**定义位置（Location）**：[`drivers/input/Kconfig.cst8xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.cst8xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_CST8XX_EV_DEVICE"></a>

## 111.29 `CONFIG_INPUT_CST8XX_EV_DEVICE`

**提示（Prompt）**：设备特定事件（Device-specific Event）支持

**说明（Help）**

启用设备特定事件支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_CST8XX && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.cst8xx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.cst8xx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CST8XX 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CST8XX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CST8XX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CST8XX_INTERRUPT"></a>

## 111.30 `CONFIG_INPUT_CST8XX_INTERRUPT`

**提示（Prompt）**：中断支持（Interrupt Support）

**说明（Help）**

启用中断支持，需要 GPIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_INPUT_CST8XX && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`drivers/input/Kconfig.cst8xx:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.cst8xx#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CST8XX 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_INPUT_CST8XX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CST8XX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CST8XX_PERIOD_MS"></a>

## 111.31 `CONFIG_INPUT_CST8XX_PERIOD_MS`

**提示（Prompt）**：采样周期（Sample Period）

**说明（Help）**

轮询模式（Polling Mode）下的采样周期，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_CST8XX_INTERRUPT && CONFIG_INPUT_CST8XX && CONFIG_INPUT
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/input/Kconfig.cst8xx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.cst8xx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → CST8XX 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_CST8XX_INTERRUPT`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CST8XX_INTERRUPT)、[`CONFIG_INPUT_CST8XX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CST8XX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_CY8CMBR3XXX"></a>

## 111.32 `CONFIG_INPUT_CY8CMBR3XXX`

**提示（Prompt）**：CY8CMBR3XXX 电容式触摸传感器驱动

**说明（Help）**

启用 Cypress CY8CMBR3XXX 电容式触摸传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CYPRESS_CY8CMBR3XXX_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/input/Kconfig.cy8cmbr3xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.cy8cmbr3xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INPUT_ESP32_TOUCH_SENSOR"></a>

## 111.33 `CONFIG_INPUT_ESP32_TOUCH_SENSOR`

**提示（Prompt）**：Espressif 触摸传感器输入（Touch Sensor Input）驱动

**说明（Help）**

启用 Espressif 触摸传感器输入驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_TOUCH_ENABLED && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_FT5336"></a>

## 111.34 `CONFIG_INPUT_FT5336`

**提示（Prompt）**：FT3267/FT5XX6/FT6XX6 电容式触摸面板驱动

**说明（Help）**

启用多种 Focaltech 电容式触摸面板控制器驱动。此驱动应支持 FT5x06、FT5606、FT5x16、FT6x06、Ft6x36、FT5x06i、FT5336、FT3316、FT5436i、FT3267、FT5336i 和 FT5x46。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FOCALTECH_FT5336_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_INPUT_TOUCH
```

**定义位置（Location）**：[`drivers/input/Kconfig.ft5336:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ft5336#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_FT5336_INIT_DELAY_MS"></a>

## 111.35 `CONFIG_INPUT_FT5336_INIT_DELAY_MS`

**提示（Prompt）**：初始化延迟（Initialization Delay）

**说明（Help）**

开始轮询触摸采样之前等待的时间，单位为毫秒。触摸控制器上电或初始化耗时较长时，此选项可能有用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_FT5336_INTERRUPT && CONFIG_INPUT_FT5336 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.ft5336:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ft5336#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → FT3267/FT5XX6/FT6XX6 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_FT5336_INTERRUPT`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT5336_INTERRUPT)、[`CONFIG_INPUT_FT5336`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT5336)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_FT5336_INTERRUPT"></a>

## 111.36 `CONFIG_INPUT_FT5336_INTERRUPT`

**提示（Prompt）**：中断（Interrupt）

**说明（Help）**

启用中断支持，需要 GPIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_FT5336 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`drivers/input/Kconfig.ft5336:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ft5336#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → FT3267/FT5XX6/FT6XX6 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_FT5336`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT5336)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_FT5336_MAX_TOUCH_POINTS"></a>

## 111.37 `CONFIG_INPUT_FT5336_MAX_TOUCH_POINTS`

**提示（Prompt）**：最大触摸点数（Maximum Touch Points）

**说明（Help）**

要处理的最大触摸点数。设为 1 时，不报告多点触控槽位事件（Multitouch Slot Event）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_FT5336 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`drivers/input/Kconfig.ft5336:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ft5336#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → FT3267/FT5XX6/FT6XX6 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_FT5336`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT5336)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_FT5336_PERIOD_MS"></a>

## 111.38 `CONFIG_INPUT_FT5336_PERIOD_MS`

**提示（Prompt）**：采样周期（Sample Period）

**说明（Help）**

轮询模式（Polling Mode）下的采样周期，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_FT5336_INTERRUPT && CONFIG_INPUT_FT5336 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.ft5336:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ft5336#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → FT3267/FT5XX6/FT6XX6 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_FT5336_INTERRUPT`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT5336_INTERRUPT)、[`CONFIG_INPUT_FT5336`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT5336)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_FT5336_PM_MODE_MONITOR"></a>

## 111.39 `CONFIG_INPUT_FT5336_PM_MODE_MONITOR`

**提示（Prompt）**：在电源管理挂起（PM Suspend）时使用监测模式（Monitor Mode）

**说明（Help）**

在 PM 挂起时使用监测模式。该模式将扫描速率降至 25 fps，并在检测到触摸时自动唤醒。禁用后使用休眠模式（Hibernate Mode），需要硬件复位才能唤醒，因此必须定义 `reset-gpios`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE && CONFIG_INPUT_FT5336 && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.ft5336:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ft5336#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → FT3267/FT5XX6/FT6XX6 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)、[`CONFIG_INPUT_FT5336`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT5336)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_FT6146"></a>

## 111.40 `CONFIG_INPUT_FT6146`

**提示（Prompt）**：FT6146 触摸控制器（Touch Controller）

**说明（Help）**

启用 FT6146 电容式触摸控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FOCALTECH_FT6146_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_INPUT_TOUCH
```

**定义位置（Location）**：[`drivers/input/Kconfig.ft6146:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ft6146#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_FT6146_INTERRUPT"></a>

## 111.41 `CONFIG_INPUT_FT6146_INTERRUPT`

**提示（Prompt）**：FT6146 中断（Interrupt）支持

**说明（Help）**

启用 FT6146 触摸控制器的中断支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_FT6146 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`drivers/input/Kconfig.ft6146:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ft6146#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → FT6146 触摸控制器（Touch Controller）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_FT6146`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT6146)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_FT6146_PERIOD_MS"></a>

## 111.42 `CONFIG_INPUT_FT6146_PERIOD_MS`

**提示（Prompt）**：采样周期（Sample Period）

**说明（Help）**

轮询模式（Polling Mode）下的采样周期，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_FT6146_INTERRUPT && CONFIG_INPUT_FT6146 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.ft6146:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ft6146#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → FT6146 触摸控制器（Touch Controller）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_FT6146_INTERRUPT`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT6146_INTERRUPT)、[`CONFIG_INPUT_FT6146`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT6146)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_GPIO_KBD_MATRIX"></a>

## 111.43 `CONFIG_INPUT_GPIO_KBD_MATRIX`

**提示（Prompt）**：基于 GPIO 的键盘矩阵输入（Keyboard Matrix Input）驱动

**说明（Help）**

GPIO 键盘矩阵输入驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_KBD_MATRIX_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INPUT_KBD_MATRIX
```

**定义位置（Location）**：[`drivers/input/Kconfig.gpio_kbd_matrix:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.gpio_kbd_matrix#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)。

<a id="CONFIG_INPUT_GPIO_KEYS"></a>

## 111.44 `CONFIG_INPUT_GPIO_KEYS`

**提示（Prompt）**：GPIO 按键输入（Keys Input）驱动

**说明（Help）**

启用 GPIO 按键输入驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_KEYS_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/input/Kconfig.gpio_keys:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.gpio_keys#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_INPUT_GPIO_QDEC"></a>

## 111.45 `CONFIG_INPUT_GPIO_QDEC`

**提示（Prompt）**：基于 GPIO 的正交解码器（QDEC）输入驱动

**说明（Help）**

GPIO 正交解码器（Quadrature Decoder）输入驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_QDEC_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.gpio_qdec:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.gpio_qdec#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_GT911"></a>

## 111.46 `CONFIG_INPUT_GT911`

**提示（Prompt）**：GT9xx / GT9xxx 电容式触摸面板驱动

**说明（Help）**

启用多种 Goodix 电容式触摸面板控制器驱动。此驱动应支持 gt9110、gt912、gt927、gt9271、gt928 和 gt967。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GOODIX_GT911_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_INPUT_TOUCH
```

**定义位置（Location）**：[`drivers/input/Kconfig.gt911:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.gt911#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_GT911_INTERRUPT"></a>

## 111.47 `CONFIG_INPUT_GT911_INTERRUPT`

**提示（Prompt）**：中断（Interrupt）

**说明（Help）**

启用中断支持；否则驱动会轮询（Poll）控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/lcd_par_s035/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lcd_par_s035/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk043fn66hs_ctg/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn66hs_ctg/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk055hdmipi4m/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4m/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk055hdmipi4ma0/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/aik_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/aik_ra8d1.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.gt911:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.gt911#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → GT9xx / GT9xxx 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_INPUT_GT911_MAX_TOUCH_POINTS"></a>

## 111.48 `CONFIG_INPUT_GT911_MAX_TOUCH_POINTS`

**提示（Prompt）**：触摸点数（Touch Number）

**说明（Help）**

要处理的最大触摸点数。等于 1 时，忽略多点触控（Multitouch）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_GT911 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`drivers/input/Kconfig.gt911:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.gt911#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → GT9xx / GT9xxx 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_GT911`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_GT911)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_GT911_PERIOD_MS"></a>

## 111.49 `CONFIG_INPUT_GT911_PERIOD_MS`

**提示（Prompt）**：采样周期（Sample Period）

**说明（Help）**

轮询模式（Polling Mode）下的采样周期，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_GT911_INTERRUPT && CONFIG_INPUT_GT911 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.gt911:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.gt911#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → GT9xx / GT9xxx 电容式触摸面板驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_GT911_INTERRUPT`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_GT911_INTERRUPT)、[`CONFIG_INPUT_GT911`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_GT911)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_ILI2132A"></a>

## 111.50 `CONFIG_INPUT_ILI2132A`

**提示（Prompt）**：ILI2132A 电容式触摸控制器驱动

**说明（Help）**

启用 Ilitek ILI2132A 触摸控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ILITEK_ILI2132A_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_INPUT_TOUCH
```

**定义位置（Location）**：[`drivers/input/Kconfig.ili2132a:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.ili2132a#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_ITE_IT51XXX_KBD"></a>

## 111.51 `CONFIG_INPUT_ITE_IT51XXX_KBD`

**提示（Prompt）**：ITE 键盘扫描（Keyboard Scanning）驱动

**说明（Help）**

此选项启用 ITE 键盘扫描驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_KBD_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INPUT_KBD_MATRIX
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/input/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_INPUT_ITE_IT8801_KBD"></a>

## 111.52 `CONFIG_INPUT_ITE_IT8801_KBD`

**提示（Prompt）**：ITE IT8801 键盘矩阵扫描控制器（Keyboard Matrix Scan Controller）

**说明（Help）**

启用 ITE IT8801 基于 I²C 的键盘矩阵扫描驱动。IT8801 支持 8 个 KSI 引脚和 19 个 KSO 引脚（[22:11]、[6:0]），其中 `KSO[22:18]` 可配置为 GPIO 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8801_KBD_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_INPUT_KBD_MATRIX
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/input/Kconfig.it8801:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.it8801#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_INPUT_ITE_IT8XXX2_KBD"></a>

## 111.53 `CONFIG_INPUT_ITE_IT8XXX2_KBD`

**提示（Prompt）**：ITE 键盘扫描（Keyboard Scanning）驱动

**说明（Help）**

此选项启用 ITE 键盘扫描驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_KBD_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INPUT_KBD_MATRIX
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/input/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC"></a>

## 111.54 `CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC`

**提示（Prompt）**：允许在运行时修改实际按键掩码（Actual Key Mask）

**说明（Help）**

启用后，设备树属性 `actual-key-mask` 的数据保存在 RAM 中，并提供 `input_kbd_matrix_actual_key_mask_set()` 函数在运行时修改其内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_KBD_MATRIX && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.kbd_matrix:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.kbd_matrix#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK"></a>

## 111.55 `CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在驱动特定的 `drive_column` 实现执行后，调用应用特定的钩子（Hook）。应用必须实现 `input_kbd_matrix_drive_column_hook` 函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_KBD_MATRIX && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.kbd_matrix:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.kbd_matrix#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_KBD_MATRIX"></a>

## 111.56 `CONFIG_INPUT_KBD_MATRIX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用键盘矩阵驱动使用的库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_INPUT
```

**被选择（Selected by）**

```text
CONFIG_INPUT_BEE_KEYSCAN
CONFIG_INPUT_GPIO_KBD_MATRIX
CONFIG_INPUT_ITE_IT51XXX_KBD
CONFIG_INPUT_ITE_IT8801_KBD
CONFIG_INPUT_ITE_IT8XXX2_KBD
CONFIG_INPUT_NPCX_KBD
CONFIG_INPUT_REALTEK_RTS5912_KBD
CONFIG_INPUT_XEC_KBD
```

**定义位置（Location）**：[`drivers/input/Kconfig.kbd_matrix:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.kbd_matrix#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_BEE_KEYSCAN`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_BEE_KEYSCAN)、[`CONFIG_INPUT_GPIO_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_GPIO_KBD_MATRIX)、[`CONFIG_INPUT_ITE_IT51XXX_KBD`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_ITE_IT51XXX_KBD)、[`CONFIG_INPUT_ITE_IT8801_KBD`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_ITE_IT8801_KBD)、[`CONFIG_INPUT_ITE_IT8XXX2_KBD`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_ITE_IT8XXX2_KBD)、[`CONFIG_INPUT_NPCX_KBD`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_NPCX_KBD)、[`CONFIG_INPUT_REALTEK_RTS5912_KBD`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_REALTEK_RTS5912_KBD)、[`CONFIG_INPUT_XEC_KBD`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_XEC_KBD)。

<a id="CONFIG_INPUT_KBD_MATRIX_16_BIT_ROW"></a>

## 111.57 `CONFIG_INPUT_KBD_MATRIX_16_BIT_ROW`

**提示（Prompt）**：16 位行大小（Row Size）支持

**说明（Help）**

内部结构使用 16 位类型；如果驱动支持，可使用最多 16 行的矩阵。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_KBD_MATRIX && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.kbd_matrix:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.kbd_matrix#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_KBD_MATRIX_THREAD_PRIORITY"></a>

## 111.58 `CONFIG_INPUT_KBD_MATRIX_THREAD_PRIORITY`

**提示（Prompt）**：键盘矩阵线程优先级（Thread Priority）

**说明（Help）**

键盘矩阵线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_KBD_MATRIX && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/input/Kconfig.kbd_matrix:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.kbd_matrix#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_KBD_MATRIX_THREAD_STACK_SIZE"></a>

## 111.59 `CONFIG_INPUT_KBD_MATRIX_THREAD_STACK_SIZE`

**提示（Prompt）**：键盘矩阵线程栈大小（Stack Size）

**说明（Help）**

键盘矩阵线程所用栈的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_KBD_MATRIX && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/input/Kconfig.kbd_matrix:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.kbd_matrix#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_KPP_PERIOD_MS"></a>

## 111.60 `CONFIG_INPUT_KPP_PERIOD_MS`

**提示（Prompt）**：采样周期（Sample Period）

**说明（Help）**

按键按下时的采样周期（Sample Period），单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_MCUX_KPP && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.mcux_kpp:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.mcux_kpp#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → 键盘端口（KPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_MCUX_KPP`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_MCUX_KPP)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_MCUX_KPP"></a>

## 111.61 `CONFIG_INPUT_MCUX_KPP`

**提示（Prompt）**：键盘端口（KPP）驱动

**说明（Help）**

启用键盘端口（Keypad Port）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCUX_KPP_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.mcux_kpp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.mcux_kpp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_MCUX_TSI"></a>

## 111.62 `CONFIG_INPUT_MCUX_TSI`

**提示（Prompt）**：NXP MCUX TSI 输入驱动

**说明（Help）**

启用 NXP MCUX 触摸感应输入（Touch Sensing Input，TSI）的输入驱动。此驱动通过输入子系统报告触摸事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TSI_INPUT_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.mcux_tsi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.mcux_tsi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_MODULINO_BUTTONS"></a>

## 111.63 `CONFIG_INPUT_MODULINO_BUTTONS`

**提示（Prompt）**：Arduino Modulino 按键（Buttons）

**说明（Help）**

启用 Arduino Modulino Buttons 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARDUINO_MODULINO_BUTTONS_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/input/Kconfig.modulino:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.modulino#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INPUT_NPCX_KBD"></a>

## 111.64 `CONFIG_INPUT_NPCX_KBD`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（EC）键盘扫描驱动

**说明（Help）**

此选项启用 NPCX 系列处理器的键盘扫描驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_KBD_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INPUT_KBD_MATRIX
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/input/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_INPUT_NPCX_KBD_KSO_HIGH_DRIVE"></a>

## 111.65 `CONFIG_INPUT_NPCX_KBD_KSO_HIGH_DRIVE`

**提示（Prompt）**：为 KSO 引脚选择准双向缓冲器（Quasi-bidirectional Buffer）

**说明（Help）**

为 KSO 引脚选择准双向缓冲器，以缩短低电平到高电平的转换时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_NPCX_KBD && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.npcx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.npcx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Nuvoton NPCX 嵌入式控制器（EC）键盘扫描驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_NPCX_KBD`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_NPCX_KBD)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_NUNCHUK"></a>

## 111.66 `CONFIG_INPUT_NUNCHUK`

**提示（Prompt）**：任天堂 Nunchuk 操纵杆（Nintendo Nunchuk joystick）。

**说明（Help）**

此选项启用 Nintendo Nunchuk 摇杆（Joystick）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NINTENDO_NUNCHUK_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/input/Kconfig.nunchuk:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.nunchuk#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INPUT_NUNCHUK_ACCELERATION"></a>

## 111.67 `CONFIG_INPUT_NUNCHUK_ACCELERATION`

**提示（Prompt）**：Nintendo Nunchuk 摇杆加速度传感器数据（Acceleration Sensor Data）

**说明（Help）**

此选项启用读取 Nintendo Nunchuk 摇杆的加速度数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_NUNCHUK && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.nunchuk:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.nunchuk#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → 任天堂 Nunchuk 操纵杆（Nintendo Nunchuk joystick）。

**配置项引用（Symbol References）**：[`CONFIG_INPUT_NUNCHUK`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_NUNCHUK)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_PAT912X"></a>

## 111.68 `CONFIG_INPUT_PAT912X`

**提示（Prompt）**：PAT912X 微型光学导航芯片（Miniature Optical Navigation Chip）输入驱动

**说明（Help）**

PAT912X 微型光学导航芯片（Miniature Optical Navigation Chip）输入驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PIXART_PAT912X_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/input/Kconfig.pat912x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.pat912x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INPUT_PAW32XX"></a>

## 111.69 `CONFIG_INPUT_PAW32XX`

**提示（Prompt）**：PAW32xx 超低功耗无线鼠标芯片（Ultra low power wireless mouse chip）。

**说明（Help）**

PAW32XX 低功耗激光鼠标传感器（Low-power Laser Mouse Sensor）输入驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PIXART_PAW32XX_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/input/Kconfig.paw32xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.paw32xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_INPUT_PINNACLE"></a>

## 111.70 `CONFIG_INPUT_PINNACLE`

**提示（Prompt）**：基于 Cirque Pinnacle 1CA027 触摸控制器的设备

**说明（Help）**

启用 Cirque Pinnacle 1CA027 轨迹输入设备（Tracked Input Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CIRQUE_PINNACLE_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_I2C if n
CONFIG_SPI if n
```

**定义位置（Location）**：[`drivers/input/Kconfig.pinnacle:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.pinnacle#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_INPUT_PMW3610"></a>

## 111.71 `CONFIG_INPUT_PMW3610`

**提示（Prompt）**：PMW3610 低功耗激光鼠标传感器输入驱动

**说明（Help）**

PMW3610 低功耗激光鼠标传感器输入驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PIXART_PMW3610_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/input/Kconfig.pmw3610:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.pmw3610#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_INPUT_REALTEK_RTS5912_KBD"></a>

## 111.72 `CONFIG_INPUT_REALTEK_RTS5912_KBD`

**提示（Prompt）**：Realtek RTS5912 键盘扫描（Keyboard Scanning）驱动

**说明（Help）**

此选项启用 Realtek 键盘扫描驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_KBD_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INPUT_KBD_MATRIX
```

**定义位置（Location）**：[`drivers/input/Kconfig.rts5912:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.rts5912#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU"></a>

## 111.73 `CONFIG_INPUT_RENESAS_RA_CTSU`

**提示（Prompt）**：Renesas RA 电容式触摸（Capacitive Touch）驱动

**说明（Help）**

启用 Renesas RA 触摸感应（Touch Sensing）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_CTSU_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_CTSU
CONFIG_USE_RA_FSP_TOUCH
CONFIG_SYS_MEM_BLOCKS
CONFIG_GPIO
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_USE_RA_FSP_CTSU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_CTSU)、[`CONFIG_USE_RA_FSP_TOUCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_TOUCH)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE"></a>

## 111.74 `CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE`

**提示（Prompt）**：抖动抑制类型（Chattering Suppression Type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_A
```

**可选项（Choices）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_A
CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_B
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_A`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_A)、[`CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_B`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_B)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_A"></a>

## 111.75 `CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_A`

**提示（Prompt）**：在迟滞范围（Hysteresis Range）内保持超阈值计数

**说明（Help）**

在迟滞范围（Hysteresis Range）内保持超出阈值的计数器值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE>
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动 → 抖动抑制类型（Chattering Suppression Type）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_B"></a>

## 111.76 `CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE_B`

**提示（Prompt）**：在迟滞范围（Hysteresis Range）内复位超阈值计数

**说明（Help）**

在迟滞范围（Hysteresis Range）内复位超出阈值的计数器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE>
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动 → 抖动抑制类型（Chattering Suppression Type）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU_CHATTERING_SUPPRESSION_TYPE)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_DRV_PRIORITY"></a>

## 111.77 `CONFIG_INPUT_RENESAS_RA_CTSU_DRV_PRIORITY`

**提示（Prompt）**：CTSU 内部线程优先级（Thread Priority）

**说明（Help）**

CTSU 驱动内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_DRV_STACK_SIZE"></a>

## 111.78 `CONFIG_INPUT_RENESAS_RA_CTSU_DRV_STACK_SIZE`

**提示（Prompt）**：CTSU 内部线程栈大小（Stack Size）

**说明（Help）**

CTSU 驱动内部线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_MSG_MEM_BLOCK_SIZE"></a>

## 111.79 `CONFIG_INPUT_RENESAS_RA_CTSU_MSG_MEM_BLOCK_SIZE`

**提示（Prompt）**：CTSU 内部 `sys_mem_blocks` 分配器大小（Allocator Size）

**说明（Help）**

CTSU 驱动内部 `sys_mem_blocks` 分配器的最大块数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_NUM_MUTUAL_ELEMENTS"></a>

## 111.80 `CONFIG_INPUT_RENESAS_RA_CTSU_NUM_MUTUAL_ELEMENTS`

**提示（Prompt）**：互电容元件数量（Mutual-capacitance Elements）

**说明（Help）**

CTSU 中互电容元件的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_NUM_SELF_ELEMENTS"></a>

## 111.81 `CONFIG_INPUT_RENESAS_RA_CTSU_NUM_SELF_ELEMENTS`

**提示（Prompt）**：自电容元件数量（Self-capacitance Elements）

**说明（Help）**

CTSU 中自电容元件的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/rtk0eg0019b01002bj/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk0eg0019b01002bj/Kconfig.defconfig)。

```text
12
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_POLLING_INTERVAL_MS"></a>

## 111.82 `CONFIG_INPUT_RENESAS_RA_CTSU_POLLING_INTERVAL_MS`

**提示（Prompt）**：CTSU 去抖间隔（Debounce Interval）

**说明（Help）**

去抖间隔时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[20, 500]
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RA_CTSU_STABILIZATION_TIME_US"></a>

## 111.83 `CONFIG_INPUT_RENESAS_RA_CTSU_STABILIZATION_TIME_US`

**提示（Prompt）**：CTSU 稳定时间（Stabilization Time）

**说明（Help）**

两次扫描之间需要等待的稳定时间，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RA_DEVICE_VCC"></a>

## 111.84 `CONFIG_INPUT_RENESAS_RA_DEVICE_VCC`

**提示（Prompt）**：SoC VCC 输入，单位为毫伏（mV）

**说明（Help）**

SoC VCC 输入，单位为毫伏（mV）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
3300
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG"></a>

## 111.85 `CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG`

**提示（Prompt）**：使用 QE Touch 工作流（Workflow）配置此驱动

**说明（Help）**

启用此配置后，CTSU 和电容式触摸（Cap Touch）驱动的设置将反映 QE Touch 工作流生成的设置。请将生成的 C 源文件加入应用的 `CMakeLists`，使驱动能够使用它们。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_RENESAS_RA_CTSU && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_ra:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_ra#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas RA 电容式触摸（Capacitive Touch）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RA_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RA_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU"></a>

## 111.86 `CONFIG_INPUT_RENESAS_RX_CTSU`

**提示（Prompt）**：Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**说明（Help）**

启用 RX 系列 CTSU 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_CTSU_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RX_RDP_CTSU
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_USE_RX_RDP_CTSU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RX_RDP_CTSU)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU_CANCEL_FREQ"></a>

## 111.87 `CONFIG_INPUT_RENESAS_RX_CTSU_CANCEL_FREQ`

**提示（Prompt）**：CTSU 取消频率（Cancel Frequency）

**说明（Help）**

连续触摸取消计数（Continuous Touch Cancel Count），0 表示不使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU_DRIFT_FREQ"></a>

## 111.88 `CONFIG_INPUT_RENESAS_RX_CTSU_DRIFT_FREQ`

**提示（Prompt）**：CTSU 漂移频率（Drift Frequency）

**说明（Help）**

用于漂移校正（Drift Correction）的采样计数，0 表示不使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
255
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU_NUM_MOVING_AVERAGE"></a>

## 111.89 `CONFIG_INPUT_RENESAS_RX_CTSU_NUM_MOVING_AVERAGE`

**提示（Prompt）**：CTSU 移动平均（Moving Average）

**说明（Help）**

测量数据的移动平均次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU_OFF_FREQ"></a>

## 111.90 `CONFIG_INPUT_RENESAS_RX_CTSU_OFF_FREQ`

**提示（Prompt）**：CTSU 关闭频率（Off Frequency）

**说明（Help）**

触摸释放（Touch-off）过滤的去抖计数次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU_ON_FREQ"></a>

## 111.91 `CONFIG_INPUT_RENESAS_RX_CTSU_ON_FREQ`

**提示（Prompt）**：CTSU 开启频率（On Frequency）

**说明（Help）**

触摸按下（Touch-on）过滤的去抖计数次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU_PCLK_DIVISION"></a>

## 111.92 `CONFIG_INPUT_RENESAS_RX_CTSU_PCLK_DIVISION`

**提示（Prompt）**：CTSU：PCLK 分频（Division）

**说明（Help）**

PCLK 分频：

- 0：`PCLK/1`。
- 1：`PCLK/2`。
- 2：`PCLK/4`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU_POWER_SUPPLY_CAPACITY"></a>

## 111.93 `CONFIG_INPUT_RENESAS_RX_CTSU_POWER_SUPPLY_CAPACITY`

**提示（Prompt）**：CTSU 电源供电能力（Power Supply Capacity）

**说明（Help）**

电源供电能力调整：

- 0：正常（Normal），40 μA。
- 1：大电流输出（High-current Output），80 μA。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 1]
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU_SCAN_INTERVAL_MS"></a>

## 111.94 `CONFIG_INPUT_RENESAS_RX_CTSU_SCAN_INTERVAL_MS`

**提示（Prompt）**：CTSU 通道扫描间隔（Scan Interval）

**说明（Help）**

两次扫描之间的间隔时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_CTSU_TRANSMISSION_POWER_SUPPLY"></a>

## 111.95 `CONFIG_INPUT_RENESAS_RX_CTSU_TRANSMISSION_POWER_SUPPLY`

**提示（Prompt）**：CTSU 发送电源（Transmission Power Supply）

**说明（Help）**

发送电源选择：

- 0：选择 VCC。
- 1：选择内部逻辑电源（Internal Logic Power Supply）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG && CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 1]
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG)、[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG"></a>

## 111.96 `CONFIG_INPUT_RENESAS_RX_QE_TOUCH_CFG`

**提示（Prompt）**：使用 QE Touch 工作流（Workflow）配置此驱动

**说明（Help）**

启用此配置后，CTSU 和电容式触摸（Cap Touch）驱动的设置将反映 QE Touch 工作流生成的设置。请将生成的 C 源文件加入应用的 `CMakeLists`，使驱动能够使用它们。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_RENESAS_RX_CTSU && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.renesas_rx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.renesas_rx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → Renesas 电容式触摸感应单元（Capacitive Touch Sensing Unit，CTSU）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_RENESAS_RX_CTSU`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_RENESAS_RX_CTSU)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_SBUS"></a>

## 111.97 `CONFIG_INPUT_SBUS`

**提示（Prompt）**：SBUS 驱动

**说明（Help）**

启用 SBUS 遥控器（Remote Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FUTABA_SBUS_ENABLED && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`drivers/input/Kconfig.sbus:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.sbus#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_INPUT_SBUS_CHANNEL_VALUE_ONE"></a>

## 111.98 `CONFIG_INPUT_SBUS_CHANNEL_VALUE_ONE`

**提示（Prompt）**：判定 `INPUT_EV_KEY` 值为 1 的大于阈值（>）

**说明（Help）**

SBUS 为数字开关发送模拟值。此配置值设置将模拟值解释为逻辑 1 的阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_SBUS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1800
```

**定义位置（Location）**：[`drivers/input/Kconfig.sbus:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.sbus#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → SBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_SBUS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_SBUS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_SBUS_CHANNEL_VALUE_ZERO"></a>

## 111.99 `CONFIG_INPUT_SBUS_CHANNEL_VALUE_ZERO`

**提示（Prompt）**：判定 `INPUT_EV_KEY` 值为 0 的小于阈值（<）

**说明（Help）**

SBUS 为数字开关发送模拟值。此配置值设置将模拟值解释为逻辑 0 的阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_SBUS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1200
```

**定义位置（Location）**：[`drivers/input/Kconfig.sbus:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.sbus#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → SBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_SBUS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_SBUS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_SBUS_REPORT_FILTER"></a>

## 111.100 `CONFIG_INPUT_SBUS_REPORT_FILTER`

**提示（Prompt）**：触发报告的最小信号变化（Minimal Signal Change）

**说明（Help）**

SBUS 信号往往有些噪声，可以增大阈值以减少输入事件的数量。设为 0 表示不进行过滤。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_SBUS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/input/Kconfig.sbus:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.sbus#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → SBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_SBUS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_SBUS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<!-- kconfig-navigation -->

[上一章](P110_drivers_ieee802154_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P112_drivers_input_配置项参考_2.md)
