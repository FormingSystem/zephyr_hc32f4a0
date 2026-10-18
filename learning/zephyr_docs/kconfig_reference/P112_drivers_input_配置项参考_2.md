---
id: learning.zephyr-docs.kconfig-reference.page-112
title: "`drivers/input`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第112章\_`drivers/input`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/input` 的 28 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_INPUT_SBUS_SEND_SYNC"></a>

## 112.1 `CONFIG_INPUT_SBUS_SEND_SYNC`

**提示（Prompt）**：每个 SBUS 帧都向输入子系统发送同步（Sync）

**说明（Help）**

向输入子系统发送带同步位（Sync Bit）的同步消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_SBUS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.sbus:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.sbus#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → SBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_SBUS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_SBUS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_SBUS_THREAD_PRIORITY"></a>

## 112.2 `CONFIG_INPUT_SBUS_THREAD_PRIORITY`

**提示（Prompt）**：SBUS 线程优先级（Thread Priority）

**说明（Help）**

SBUS 线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_SBUS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/input/Kconfig.sbus:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.sbus#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → SBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_SBUS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_SBUS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_SBUS_THREAD_STACK_SIZE"></a>

## 112.3 `CONFIG_INPUT_SBUS_THREAD_STACK_SIZE`

**提示（Prompt）**：SBUS 线程栈大小（Stack Size）

**说明（Help）**

SBUS 线程所用栈的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_SBUS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/input/Kconfig.sbus:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.sbus#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → SBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_SBUS`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_SBUS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_SDL_TOUCH"></a>

## 112.4 `CONFIG_INPUT_SDL_TOUCH`

**提示（Prompt）**：用于触摸面板仿真的 SDL 事件过滤器（Event Filter）

**说明（Help）**

启用 SDL 鼠标事件过滤器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_INPUT_SDL_TOUCH_ENABLED && HAS_SDL && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.sdl:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.sdl#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_SHELL_KBD_MATRIX_STATE"></a>

## 112.5 `CONFIG_INPUT_SHELL_KBD_MATRIX_STATE`

**提示（Prompt）**：输入子系统 `kbd_matrix_state` Shell 命令

**说明（Help）**

启用输入子系统的 `kbd_matrix_state` Shell 命令，用于记录键盘矩阵设备的状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_SHELL && CONFIG_INPUT_KBD_MATRIX && CONFIG_INPUT
```

**定义位置（Location）**：[`drivers/input/Kconfig.kbd_matrix:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.kbd_matrix#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_SHELL)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_SHELL_KBD_MATRIX_STATE_MAX_COLS"></a>

## 112.6 `CONFIG_INPUT_SHELL_KBD_MATRIX_STATE_MAX_COLS`

**提示（Prompt）**：`kbd_matrix_state` 命令支持的最大列数（Maximum Column Count）

**说明（Help）**

输入子系统 `kbd_matrix_state` Shell 命令可处理的设备最大列数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_SHELL_KBD_MATRIX_STATE && CONFIG_INPUT_KBD_MATRIX && CONFIG_INPUT
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/input/Kconfig.kbd_matrix:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.kbd_matrix#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → 输入子系统 `kbd_matrix_state` Shell 命令

**配置项引用（Symbol References）**：[`CONFIG_INPUT_SHELL_KBD_MATRIX_STATE`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_SHELL_KBD_MATRIX_STATE)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_STM32_TSC_KEYS"></a>

## 112.7 `CONFIG_INPUT_STM32_TSC_KEYS`

**提示（Prompt）**：STM32 TSC 触摸库（Touch Library）

**说明（Help）**

启用 STM32 TSC 触摸库支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_TSC_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.tsc_keys:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.tsc_keys#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_STM32_TSC_KEYS_BUFFER_WORD_SIZE"></a>

## 112.8 `CONFIG_INPUT_STM32_TSC_KEYS_BUFFER_WORD_SIZE`

**提示（Prompt）**：STM32 TSC 触摸缓冲区大小，单位为字（Word）

**说明（Help）**

STM32 TSC 触摸库的环形缓冲区（Ring Buffer）大小。此大小与 `tsc-keys` 设备树节点中的 `sampling-interval` 属性共同决定关注的时间窗口。通过计算缓冲区中最旧值与最新值之间的斜率，生成按下或释放输入事件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_STM32_TSC_KEYS && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.tsc_keys:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.tsc_keys#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → STM32 TSC 触摸库（Touch Library）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_STM32_TSC_KEYS`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_STM32_TSC_KEYS)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_STMPE811"></a>

## 112.9 `CONFIG_INPUT_STMPE811`

**提示（Prompt）**：STMPE811 触摸驱动

**说明（Help）**

启用 STMPE811 触摸面板驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STMPE811_ENABLED && CONFIG_INPUT
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

**定义位置（Location）**：[`drivers/input/Kconfig.stmpe811:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.stmpe811#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_TMA525B"></a>

## 112.10 `CONFIG_INPUT_TMA525B`

**提示（Prompt）**：TMA525B 电容式触摸控制器（Capacitive Touch Controller）

**说明（Help）**

启用 Parade Tech TMA525B 电容式触摸控制器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PARADE_TMA525B_ENABLED && CONFIG_INPUT
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

**定义位置（Location）**：[`drivers/input/Kconfig.tma525b:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.tma525b#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_INPUT_TMA525B_INTERRUPT"></a>

## 112.11 `CONFIG_INPUT_TMA525B_INTERRUPT`

**提示（Prompt）**：中断模式（Interrupt Mode）

**说明（Help）**

为 TMA525B 触摸控制器启用中断模式。禁用时，驱动使用轮询模式（Polling Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_TMA525B && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`drivers/input/Kconfig.tma525b:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.tma525b#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → TMA525B 电容式触摸控制器（Capacitive Touch Controller）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_TMA525B`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TMA525B)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_TMA525B_MAX_TOUCH_POINTS"></a>

## 112.12 `CONFIG_INPUT_TMA525B_MAX_TOUCH_POINTS`

**提示（Prompt）**：最大触摸点数（Maximum Touch Points）

**说明（Help）**

控制器支持的最大触摸点数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_TMA525B && CONFIG_INPUT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`drivers/input/Kconfig.tma525b:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.tma525b#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → TMA525B 电容式触摸控制器（Capacitive Touch Controller）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_TMA525B`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TMA525B)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_TMA525B_PERIOD_MS"></a>

## 112.13 `CONFIG_INPUT_TMA525B_PERIOD_MS`

**提示（Prompt）**：轮询周期（Polling Period，毫秒）

**说明（Help）**

控制器处于轮询模式时的轮询周期，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_INPUT_TMA525B_INTERRUPT && CONFIG_INPUT_TMA525B && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.tma525b:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.tma525b#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → TMA525B 电容式触摸控制器（Capacitive Touch Controller）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_TMA525B_INTERRUPT`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TMA525B_INTERRUPT)、[`CONFIG_INPUT_TMA525B`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TMA525B)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_TMA525B_RETRY_TIMES"></a>

## 112.14 `CONFIG_INPUT_TMA525B_RETRY_TIMES`

**提示（Prompt）**：控制器进入应用模式（Application Mode）的重试次数

**说明（Help）**

上电后控制器进入应用模式的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_TMA525B && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.tma525b:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.tma525b#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → TMA525B 电容式触摸控制器（Capacitive Touch Controller）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_TMA525B`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TMA525B)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_TOUCH"></a>

## 112.15 `CONFIG_INPUT_TOUCH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用触摸屏（Touchscreen）驱动使用的库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT
```

**被选择（Selected by）**

```text
CONFIG_INPUT_CF1133
CONFIG_INPUT_CHSC5X
CONFIG_INPUT_CHSC6X
CONFIG_INPUT_CST8XX
CONFIG_INPUT_FT5336
CONFIG_INPUT_FT6146
CONFIG_INPUT_GT911
CONFIG_INPUT_ILI2132A
CONFIG_INPUT_STMPE811
CONFIG_INPUT_TMA525B
CONFIG_INPUT_XPT2046
```

**定义位置（Location）**：[`drivers/input/Kconfig.touch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.touch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_CF1133`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CF1133)、[`CONFIG_INPUT_CHSC5X`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CHSC5X)、[`CONFIG_INPUT_CHSC6X`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CHSC6X)、[`CONFIG_INPUT_CST8XX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CST8XX)、[`CONFIG_INPUT_FT5336`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT5336)、[`CONFIG_INPUT_FT6146`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_FT6146)、[`CONFIG_INPUT_GT911`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_GT911)、[`CONFIG_INPUT_ILI2132A`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_ILI2132A)、[`CONFIG_INPUT_STMPE811`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_STMPE811)、[`CONFIG_INPUT_TMA525B`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TMA525B)、[`CONFIG_INPUT_XPT2046`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_XPT2046)。

<a id="CONFIG_INPUT_TSM12"></a>

## 112.16 `CONFIG_INPUT_TSM12`

**提示（Prompt）**：TSM12 电容式触摸传感器

**说明（Help）**

启用 AD Semiconductor TSM12 12 通道电容式触摸传感器及 Si12T 等寄存器兼容器件的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADSEMI_TSM12_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/input/Kconfig.tsm12:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.tsm12#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INPUT_TSM12_PERIOD_MS"></a>

## 112.17 `CONFIG_INPUT_TSM12_PERIOD_MS`

**提示（Prompt）**：采样周期（Sample Period）

**说明（Help）**

采样周期，单位为毫秒。未配置 `int-gpios` 的实例会持续轮询；配置了 `int-gpios` 的实例仅在某个通道被触摸时轮询，以检测释放。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_TSM12 && CONFIG_INPUT
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/input/Kconfig.tsm12:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.tsm12#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → TSM12 电容式触摸传感器

**配置项引用（Symbol References）**：[`CONFIG_INPUT_TSM12`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TSM12)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_VIRTIO"></a>

## 112.18 `CONFIG_INPUT_VIRTIO`

**提示（Prompt）**：VIRTIO 输入设备（Input Device）驱动

**说明（Help）**

启用 VIRTIO 输入设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_INPUT_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_VIRTIO
```

**定义位置（Location）**：[`drivers/input/Kconfig.virtio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.virtio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_VIRTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO)。

<a id="CONFIG_INPUT_VIRTIO_DEVICE_TYPE"></a>

## 112.19 `CONFIG_INPUT_VIRTIO_DEVICE_TYPE`

**提示（Prompt）**：VIRTIO 输入设备类型（Device Type）

**说明（Help）**

要仿真／探测（Emulate/Probe）的 VIRTIO 输入设备类型。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_VIRTIO && CONFIG_INPUT
```

**默认值（Defaults）**

```text
CONFIG_INPUT_VIRTIO_DEVICE_TYPE_TABLET
```

**可选项（Choices）**

```text
CONFIG_INPUT_VIRTIO_DEVICE_TYPE_TABLET
CONFIG_INPUT_VIRTIO_DEVICE_TYPE_KEYBOARD
```

**定义位置（Location）**：[`drivers/input/Kconfig.virtio:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.virtio#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → VIRTIO 输入设备（Input Device）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_VIRTIO`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_VIRTIO)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_VIRTIO_DEVICE_TYPE_TABLET`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_VIRTIO_DEVICE_TYPE_TABLET)、[`CONFIG_INPUT_VIRTIO_DEVICE_TYPE_KEYBOARD`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_VIRTIO_DEVICE_TYPE_KEYBOARD)。

<a id="CONFIG_INPUT_VIRTIO_DEVICE_TYPE_KEYBOARD"></a>

## 112.20 `CONFIG_INPUT_VIRTIO_DEVICE_TYPE_KEYBOARD`

**提示（Prompt）**：键盘（Keyboard）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_VIRTIO_DEVICE_TYPE>
```

**定义位置（Location）**：[`drivers/input/Kconfig.virtio:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.virtio#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → VIRTIO 输入设备（Input Device）驱动 → VIRTIO 输入设备类型（Device Type）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_VIRTIO_DEVICE_TYPE`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_VIRTIO_DEVICE_TYPE)。

<a id="CONFIG_INPUT_VIRTIO_DEVICE_TYPE_TABLET"></a>

## 112.21 `CONFIG_INPUT_VIRTIO_DEVICE_TYPE_TABLET`

**提示（Prompt）**：数位板（Tablet）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_INPUT_VIRTIO_DEVICE_TYPE>
```

**定义位置（Location）**：[`drivers/input/Kconfig.virtio:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.virtio#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → VIRTIO 输入设备（Input Device）驱动 → VIRTIO 输入设备类型（Device Type）

**配置项引用（Symbol References）**：[`CONFIG_INPUT_VIRTIO_DEVICE_TYPE`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_VIRTIO_DEVICE_TYPE)。

<a id="CONFIG_INPUT_VIRTIO_EVENT_BUF_COUNT"></a>

## 112.22 `CONFIG_INPUT_VIRTIO_EVENT_BUF_COUNT`

**提示（Prompt）**：排队事件缓冲区数量（Queued Event Buffers）

**说明（Help）**

事件 virtqueue 上排队的事件缓冲区数量。每个缓冲区保存一个输入事件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT_VIRTIO && CONFIG_INPUT
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`drivers/input/Kconfig.virtio:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.virtio#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → VIRTIO 输入设备（Input Device）驱动

**配置项引用（Symbol References）**：[`CONFIG_INPUT_VIRTIO`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_VIRTIO)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_INPUT_VS1838B"></a>

## 112.23 `CONFIG_INPUT_VS1838B`

**提示（Prompt）**：Vishay VS1838B 红外接收器（Infrared Receiver）

**说明（Help）**

此选项启用 VS1838B 红外接收器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VISHAY_VS1838B_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/input/Kconfig.vs1838b:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.vs1838b#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_INPUT_XEC_KBD"></a>

## 112.24 `CONFIG_INPUT_XEC_KBD`

**提示（Prompt）**：Microchip XEC 系列键盘矩阵（Keyboard Matrix）驱动

**说明（Help）**

启用 Microchip XEC Kscan IO 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_KBD_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INPUT_KBD_MATRIX
CONFIG_MULTITHREADING
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/input/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_INPUT_KBD_MATRIX`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_KBD_MATRIX)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_INPUT_XPT2046"></a>

## 112.25 `CONFIG_INPUT_XPT2046`

**提示（Prompt）**：XPT2046 电阻式触摸面板（Resistive Touch Panel）驱动

**说明（Help）**

启用 Xptek XPT2046 电阻式触摸面板驱动。此驱动与 ADS7843 非常相似，但通道编号不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XPTEK_XPT2046_ENABLED && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_INPUT_TOUCH
```

**定义位置（Location）**：[`drivers/input/Kconfig.xpt2046:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.xpt2046#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_INPUT_TOUCH`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_TOUCH)。

<a id="CONFIG_NATIVE_LINUX_EVDEV"></a>

## 112.26 `CONFIG_NATIVE_LINUX_EVDEV`

**提示（Prompt）**：基于原生 Linux evdev 的输入设备

**说明（Help）**

启用从 Linux evdev 设备读取输入；需要通过 `--evdev` 命令行参数指定 evdev 设备路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_LINUX_EVDEV_ENABLED && CONFIG_ARCH_POSIX && CONFIG_MULTITHREADING && CONFIG_INPUT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/input/Kconfig.evdev:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.evdev#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_NATIVE_LINUX_EVDEV_THREAD_PRIORITY"></a>

## 112.27 `CONFIG_NATIVE_LINUX_EVDEV_THREAD_PRIORITY`

**提示（Prompt）**：Linux evdev 线程优先级（Thread Priority）

**说明（Help）**

处理 Linux 输入事件的内部线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NATIVE_LINUX_EVDEV && CONFIG_INPUT
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/input/Kconfig.evdev:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.evdev#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → 基于原生 Linux evdev 的输入设备

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_LINUX_EVDEV`](P112_drivers_input_配置项参考_2.md#CONFIG_NATIVE_LINUX_EVDEV)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<a id="CONFIG_NATIVE_LINUX_THREAD_SLEEP_MS"></a>

## 112.28 `CONFIG_NATIVE_LINUX_THREAD_SLEEP_MS`

**提示（Prompt）**：Linux evdev 线程睡眠间隔（Sleep Period）

**说明（Help）**

Linux 输入事件线程两次检查新事件之间的睡眠时长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NATIVE_LINUX_EVDEV && CONFIG_INPUT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/input/Kconfig.evdev:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/Kconfig.evdev#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 输入驱动（Input Drivers） → 基于原生 Linux evdev 的输入设备

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_LINUX_EVDEV`](P112_drivers_input_配置项参考_2.md#CONFIG_NATIVE_LINUX_EVDEV)、[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)。

<!-- kconfig-navigation -->

[上一章](P111_drivers_input_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P113_drivers_ipm_配置项参考.md)
