---
id: learning.zephyr-docs.kconfig-reference.page-149
title: "`drivers/sensor`配置项参考（1/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第149章\_`drivers/sensor`配置项参考（1/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_2SMPB_02E"></a>

## 149.1 `CONFIG_2SMPB_02E`

**提示（Prompt）**：OMRON 2SMPB_02E 数字气压传感器（Digital Barometric Pressure Sensor）

**说明（Help）**

启用 OMRON O2SMPB_02E 数字气压传感器驱动。译注：帮助中的型号比标题多一个字母 O，按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OMRON_2SMPB_02E_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_FPU if CONFIG_CPU_HAS_FPU
```

**定义位置（Location）**：[`drivers/sensor/omron/2smpb_02e/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/omron/2smpb_02e/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)。

<a id="CONFIG_A01NYUB"></a>

## 149.2 `CONFIG_A01NYUB`

**提示（Prompt）**：DFRobot A01NYUB 距离传感器（Distance Sensor）

**说明（Help）**

启用 DFRobot A01NYUB 距离传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_DFROBOT_A01NYUB_ENABLED && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`drivers/sensor/a01nyub/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/a01nyub/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_AD2S1210"></a>

## 149.3 `CONFIG_AD2S1210`

**提示（Prompt）**：AD2S1210 10～16 位分辨率跟踪式旋转变压器数字转换器（Resolver-to-digital Converter）

**说明（Help）**

启用 AD2S1210 10～16 位分辨率跟踪式旋转变压器数字转换器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AD2S1210_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/adi/ad2s1210/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ad2s1210/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADC_CMP_NPCX"></a>

## 149.4 `CONFIG_ADC_CMP_NPCX`

**提示（Prompt）**：Nuvoton NPCX ADC 阈值检测中断（Threshold Detection Interrupt）

**说明（Help）**

此选项通过传感器触发（Sensor Trigger）API 启用阈值中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_ADC_CMP_ENABLED && CONFIG_ADC_NPCX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/nuvoton/nuvoton_adc_cmp_npcx/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nuvoton/nuvoton_adc_cmp_npcx/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ADC_NPCX`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NPCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADC_CMP_NPCX_WORKQUEUE"></a>

## 149.5 `CONFIG_ADC_CMP_NPCX_WORKQUEUE`

**提示（Prompt）**：NPCX ADC 阈值检测使用内部工作队列（Internal Work Queue）

**说明（Help）**

阈值检测中断服务例程（ISR）利用系统工作队列调用触发处理程序；设置此选项可改用专用工作队列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_CMP_NPCX && CONFIG_ADC_NPCX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nuvoton/nuvoton_adc_cmp_npcx/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nuvoton/nuvoton_adc_cmp_npcx/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Nuvoton NPCX ADC 阈值检测中断（Threshold Detection Interrupt）

**配置项引用（Symbol References）**：[`CONFIG_ADC_CMP_NPCX`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADC_CMP_NPCX)、[`CONFIG_ADC_NPCX`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NPCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADC_CMP_NPCX_WORKQUEUE_PRIORITY"></a>

## 149.6 `CONFIG_ADC_CMP_NPCX_WORKQUEUE_PRIORITY`

**提示（Prompt）**：Nuvoton NPCX ADC 阈值检测工作队列优先级

**说明（Help）**

此选项设置内部 NPCX ADC 阈值检测工作队列的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_CMP_NPCX_WORKQUEUE && CONFIG_ADC_CMP_NPCX && CONFIG_ADC_NPCX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SYSTEM_WORKQUEUE_PRIORITY
```

**定义位置（Location）**：[`drivers/sensor/nuvoton/nuvoton_adc_cmp_npcx/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nuvoton/nuvoton_adc_cmp_npcx/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Nuvoton NPCX ADC 阈值检测中断（Threshold Detection Interrupt） → NPCX ADC 阈值检测使用内部工作队列（Internal Work Queue）

**配置项引用（Symbol References）**：[`CONFIG_ADC_CMP_NPCX_WORKQUEUE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADC_CMP_NPCX_WORKQUEUE)、[`CONFIG_ADC_CMP_NPCX`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADC_CMP_NPCX)、[`CONFIG_ADC_NPCX`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NPCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SYSTEM_WORKQUEUE_PRIORITY`](P002_kernel_配置项参考_2.md#CONFIG_SYSTEM_WORKQUEUE_PRIORITY)。

<a id="CONFIG_ADC_CMP_NPCX_WORKQUEUE_STACK_SIZE"></a>

## 149.7 `CONFIG_ADC_CMP_NPCX_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：Nuvoton NPCX ADC 阈值检测工作队列栈大小

**说明（Help）**

此选项设置内部 NPCX ADC 阈值检测工作队列的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_CMP_NPCX_WORKQUEUE && CONFIG_ADC_CMP_NPCX && CONFIG_ADC_NPCX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
768
```

**定义位置（Location）**：[`drivers/sensor/nuvoton/nuvoton_adc_cmp_npcx/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nuvoton/nuvoton_adc_cmp_npcx/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Nuvoton NPCX ADC 阈值检测中断（Threshold Detection Interrupt） → NPCX ADC 阈值检测使用内部工作队列（Internal Work Queue）

**配置项引用（Symbol References）**：[`CONFIG_ADC_CMP_NPCX_WORKQUEUE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADC_CMP_NPCX_WORKQUEUE)、[`CONFIG_ADC_CMP_NPCX`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADC_CMP_NPCX)、[`CONFIG_ADC_NPCX`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NPCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADC_V2T_NPCX"></a>

## 149.8 `CONFIG_ADC_V2T_NPCX`

**提示（Prompt）**：启用 Nuvoton NPCX ADC V2T

**说明（Help）**

此选项启用 ADC 电压转温度（Voltage to Temperature，V2T）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/nuvoton/nuvoton_adc_v2t_npcx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nuvoton/nuvoton_adc_v2t_npcx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

<a id="CONFIG_ADE7978"></a>

## 149.9 `CONFIG_ADE7978`

**提示（Prompt）**：ADE7978 用于多相分流式电表的隔离式电能计量芯片组（Isolated Energy Metering Chipset）

**说明（Help）**

启用 Analog Devices ADE7978 隔离式电能计量芯片组驱动，用于多相分流式电表（Polyphase Shunt Meter）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADE7978_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/adi/ade7978/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ade7978/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADE7978_SHUNT_RESISTOR"></a>

## 149.10 `CONFIG_ADE7978_SHUNT_RESISTOR`

**提示（Prompt）**：分流电阻值（Shunt Resistor Value）

**说明（Help）**

分流电阻的阻值，单位为微欧（μΩ）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`drivers/sensor/adi/ade7978/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ade7978/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADE7978_VOLTAGE_DIVIDER"></a>

## 149.11 `CONFIG_ADE7978_VOLTAGE_DIVIDER`

**提示（Prompt）**：分压比（Voltage Divider Ratio）

**说明（Help）**

电压分压系数（Voltage Divider Factor）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1131
```

**定义位置（Location）**：[`drivers/sensor/adi/ade7978/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ade7978/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADIS1647X"></a>

## 149.12 `CONFIG_ADIS1647X`

**提示（Prompt）**：ADIS1647x 六自由度（6-DoF）MEMS 惯性测量单元（IMU）

**说明（Help）**

启用 ADIS1647x 六自由度 MEMS 惯性测量单元驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADIS1647X_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_SPI_RTIO if CONFIG_SENSOR_ASYNC_API
CONFIG_RTIO if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/adi/adis1647x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adis1647x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO)。

<a id="CONFIG_ADIS1647X_STREAM"></a>

## 149.13 `CONFIG_ADIS1647X_STREAM`

**提示（Prompt）**：通过实时 I/O（RTIO）流式传输 IMU 数据

**说明（Help）**

使用此配置选项，在数据就绪（DRDY）中断时通过 RTIO 流式传输传感器数据。需要 `SPI_RTIO`、设备树中的 `drdy-gpios` 引脚，并选择一种触发线程模式（Trigger Thread Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADIS1647X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adis1647x/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adis1647x/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADIS1647x 六自由度（6-DoF）MEMS 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_ADIS1647X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADIS1647X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADIS1647X_TRIGGER`。

<a id="CONFIG_ADIS1647X_THREAD_PRIORITY"></a>

## 149.14 `CONFIG_ADIS1647X_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADIS1647X_TRIGGER_OWN_THREAD && CONFIG_ADIS1647X_TRIGGER && CONFIG_ADIS1647X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/adis1647x/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adis1647x/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADIS1647x 六自由度（6-DoF）MEMS 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_ADIS1647X_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X_TRIGGER_OWN_THREAD)、[`CONFIG_ADIS1647X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADIS1647X_TRIGGER)、[`CONFIG_ADIS1647X`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADIS1647X_TRIGGER`。

<a id="CONFIG_ADIS1647X_THREAD_STACK_SIZE"></a>

## 149.15 `CONFIG_ADIS1647X_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADIS1647X_TRIGGER_OWN_THREAD && CONFIG_ADIS1647X_TRIGGER && CONFIG_ADIS1647X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/adis1647x/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adis1647x/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADIS1647x 六自由度（6-DoF）MEMS 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_ADIS1647X_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X_TRIGGER_OWN_THREAD)、[`CONFIG_ADIS1647X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADIS1647X_TRIGGER)、[`CONFIG_ADIS1647X`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADIS1647X_TRIGGER`。

<a id="CONFIG_ADIS1647X_TRIGGER_GLOBAL_THREAD"></a>

## 149.16 `CONFIG_ADIS1647X_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADIS1647X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adis1647x/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adis1647x/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADIS1647x 六自由度（6-DoF）MEMS 惯性测量单元（IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADIS1647X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADIS1647X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADIS1647X_TRIGGER`。

<a id="CONFIG_ADIS1647X_TRIGGER_MODE"></a>

## 149.17 `CONFIG_ADIS1647X_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADIS1647X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ADIS1647X_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_ADIS1647X_TRIGGER_NONE
CONFIG_ADIS1647X_TRIGGER_GLOBAL_THREAD
CONFIG_ADIS1647X_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/adi/adis1647x/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adis1647x/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADIS1647x 六自由度（6-DoF）MEMS 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_ADIS1647X`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADIS1647X_TRIGGER_NONE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X_TRIGGER_NONE)、[`CONFIG_ADIS1647X_TRIGGER_GLOBAL_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ADIS1647X_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ADIS1647X_TRIGGER_NONE"></a>

## 149.18 `CONFIG_ADIS1647X_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADIS1647X_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/adis1647x/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adis1647x/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADIS1647x 六自由度（6-DoF）MEMS 惯性测量单元（IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADIS1647X_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X_TRIGGER_MODE)。

<a id="CONFIG_ADIS1647X_TRIGGER_OWN_THREAD"></a>

## 149.19 `CONFIG_ADIS1647X_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADIS1647X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adis1647x/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adis1647x/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADIS1647x 六自由度（6-DoF）MEMS 惯性测量单元（IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADIS1647X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADIS1647X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADIS1647X_TRIGGER`。

<a id="CONFIG_ADLTC2990"></a>

## 149.20 `CONFIG_ADLTC2990`

**提示（Prompt）**：ADLTC2990 四通道 I²C 电压、电流和温度监视器（Monitor）

**说明（Help）**

启用 Analog Devices LTC2990 四通道 I²C 电压、电流和温度监视器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADLTC2990_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/adi/adltc2990/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adltc2990/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_ADT7310"></a>

## 149.21 `CONFIG_ADT7310`

**提示（Prompt）**：ADT7310 温度传感器（Temperature Sensor）

**说明（Help）**

启用 Analog Devices ADT7310 高精度 16 位数字 SPI 温度传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADT7310_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7310/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7310/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADT7310_THREAD_PRIORITY"></a>

## 149.22 `CONFIG_ADT7310_THREAD_PRIORITY`

**提示（Prompt）**：中断处理程序的线程优先级（Thread Priority）

**说明（Help）**

中断处理线程（Interrupt Handler Thread）的优先级。原文说明数字越大，优先级越高。该线程是协作式（Cooperative）线程，在主动让出执行权之前，不会被另一个线程打断。

译注：这里保留上游对数值方向的说明；实际使用应对照驱动的优先级换算，不应将此句视为所有 Zephyr 线程优先级的通用规则。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADT7310_TRIGGER_OWN_THREAD && CONFIG_ADT7310 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7310/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7310/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7310 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ADT7310_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7310_TRIGGER_OWN_THREAD)、[`CONFIG_ADT7310`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7310)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADT7310_THREAD_STACK_SIZE"></a>

## 149.23 `CONFIG_ADT7310_THREAD_STACK_SIZE`

**提示（Prompt）**：中断处理线程栈大小（Stack Size）

**说明（Help）**

中断处理线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADT7310_TRIGGER_OWN_THREAD && CONFIG_ADT7310 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7310/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7310/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7310 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ADT7310_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7310_TRIGGER_OWN_THREAD)、[`CONFIG_ADT7310`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7310)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADT7310_TRIGGER_GLOBAL_THREAD"></a>

## 149.24 `CONFIG_ADT7310_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**

使用全局线程（Global Thread）处理中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADT7310_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7310/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7310/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7310 温度传感器（Temperature Sensor） → 设置触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADT7310_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADT7310_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADT7310_TRIGGER`。

<a id="CONFIG_ADT7310_TRIGGER_NONE"></a>

## 149.25 `CONFIG_ADT7310_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7310/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7310/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7310 温度传感器（Temperature Sensor） → 设置触发模式（Trigger Mode）

<a id="CONFIG_ADT7310_TRIGGER_OWN_THREAD"></a>

## 149.26 `CONFIG_ADT7310_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**

使用独立线程（Separate Thread）处理中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADT7310_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7310/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7310/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7310 温度传感器（Temperature Sensor） → 设置触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADT7310_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADT7310_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADT7310_TRIGGER`。

<a id="CONFIG_ADT7420"></a>

## 149.27 `CONFIG_ADT7420`

**提示（Prompt）**：ADT7420 温度传感器

**说明（Help）**

启用 Analog Devices ADT7420 高精度 16 位数字 I²C 温度传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_ADT7420_ENABLED || DT_HAS_ADI_ADT7410_ENABLED || DT_HAS_ADI_ADT7422_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7420/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7420/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_ADT7420_TEMP_CRIT"></a>

## 149.28 `CONFIG_ADT7420_TEMP_CRIT`

**提示（Prompt）**：临界过温阈值（Critical Overtemperature），单位为摄氏度

**说明（Help）**

温度超过此值时，临界过温引脚置为有效状态。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADT7420 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
147 if n || n
125 if n
```

**取值范围（Ranges）**

```text
[-40, 150] if n
[-55, 150] if n
[-40, 125] if n
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7420/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7420/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7420 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_ADT7420`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7420)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADT7420_TEMP_HYST"></a>

## 149.29 `CONFIG_ADT7420_TEMP_HYST`

**提示（Prompt）**：温度迟滞（Temperature Hysteresis），单位为摄氏度

**说明（Help）**

指定 THIGH、TLOW 和 TCRIT 温度限值的温度迟滞，单位为摄氏度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADT7420 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7420/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7420/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7420 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_ADT7420`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7420)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADT7420_THREAD_PRIORITY"></a>

## 149.30 `CONFIG_ADT7420_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADT7420_TRIGGER_OWN_THREAD && CONFIG_ADT7420_TRIGGER && CONFIG_ADT7420 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7420/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7420/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7420 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_ADT7420_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7420_TRIGGER_OWN_THREAD)、[`CONFIG_ADT7420_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADT7420_TRIGGER)、[`CONFIG_ADT7420`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7420)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADT7420_TRIGGER`。

<a id="CONFIG_ADT7420_THREAD_STACK_SIZE"></a>

## 149.31 `CONFIG_ADT7420_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADT7420_TRIGGER_OWN_THREAD && CONFIG_ADT7420_TRIGGER && CONFIG_ADT7420 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7420/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7420/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7420 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_ADT7420_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7420_TRIGGER_OWN_THREAD)、[`CONFIG_ADT7420_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADT7420_TRIGGER)、[`CONFIG_ADT7420`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADT7420)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADT7420_TRIGGER`。

<a id="CONFIG_ADT7420_TRIGGER_GLOBAL_THREAD"></a>

## 149.32 `CONFIG_ADT7420_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADT7420_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7420/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7420/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7420 温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADT7420_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADT7420_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADT7420_TRIGGER`。

<a id="CONFIG_ADT7420_TRIGGER_NONE"></a>

## 149.33 `CONFIG_ADT7420_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7420/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7420/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7420 温度传感器 → 触发模式（Trigger Mode）

<a id="CONFIG_ADT7420_TRIGGER_OWN_THREAD"></a>

## 149.34 `CONFIG_ADT7420_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADT7420_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adt7420/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adt7420/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADT7420 温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADT7420_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADT7420_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADT7420_TRIGGER`。

<a id="CONFIG_ADXL313"></a>

## 149.35 `CONFIG_ADXL313`

**提示（Prompt）**：ADXL313 三轴加速度计（Three-Axis Accelerometer）

**说明（Help）**

启用 Analog Devices ADXL313 三轴数字加速度计驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADXL313_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl313/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl313/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_ADXL345"></a>

## 149.36 `CONFIG_ADXL345`

**提示（Prompt）**：ADXL345 三轴加速度计

**说明（Help）**

启用 ADXL345 三轴数字加速度计驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADXL345_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl345/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl345/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_ADXL345_ACCEL_RANGE_RUNTIME"></a>

## 149.37 `CONFIG_ADXL345_ACCEL_RANGE_RUNTIME`

**提示（Prompt）**：运行时选择量程（Range）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL345 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl345/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl345/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL345 三轴加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL345`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL345_STREAM"></a>

## 149.38 `CONFIG_ADXL345_STREAM`

**提示（Prompt）**：使用先进先出队列传输数据流（FIFO Streaming）

**说明（Help）**

使用此配置选项启用通过 RTIO 流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SPI_RTIO || CONFIG_I2C_RTIO) && CONFIG_SENSOR_ASYNC_API && CONFIG_ADXL345 && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_ADXL345_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl345/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl345/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL345 三轴加速度计

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_ADXL345`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL345_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL345_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL345_TRIGGER`。

<a id="CONFIG_ADXL345_THREAD_PRIORITY"></a>

## 149.39 `CONFIG_ADXL345_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL345_TRIGGER_OWN_THREAD && CONFIG_ADXL345_TRIGGER && CONFIG_ADXL345 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl345/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl345/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL345 三轴加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL345_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL345_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL345_TRIGGER)、[`CONFIG_ADXL345`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL345_TRIGGER`。

<a id="CONFIG_ADXL345_THREAD_STACK_SIZE"></a>

## 149.40 `CONFIG_ADXL345_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL345_TRIGGER_OWN_THREAD && CONFIG_ADXL345_TRIGGER && CONFIG_ADXL345 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl345/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl345/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL345 三轴加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL345_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL345_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL345_TRIGGER)、[`CONFIG_ADXL345`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL345_TRIGGER`。

<a id="CONFIG_ADXL345_TRIGGER_GLOBAL_THREAD"></a>

## 149.41 `CONFIG_ADXL345_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ADXL345_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ADXL345_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl345/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl345/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL345 三轴加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ADXL345_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345_TRIGGER_MODE)、[`CONFIG_ADXL345_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL345_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL345_TRIGGER`。

<a id="CONFIG_ADXL345_TRIGGER_MODE"></a>

## 149.42 `CONFIG_ADXL345_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL345 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ADXL345_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_ADXL345_TRIGGER_NONE
CONFIG_ADXL345_TRIGGER_GLOBAL_THREAD
CONFIG_ADXL345_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl345/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl345/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL345 三轴加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL345`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL345_TRIGGER_NONE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345_TRIGGER_NONE)、[`CONFIG_ADXL345_TRIGGER_GLOBAL_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ADXL345_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ADXL345_TRIGGER_NONE"></a>

## 149.43 `CONFIG_ADXL345_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADXL345_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl345/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl345/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL345 三轴加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL345_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345_TRIGGER_MODE)。

<a id="CONFIG_ADXL345_TRIGGER_OWN_THREAD"></a>

## 149.44 `CONFIG_ADXL345_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ADXL345_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ADXL345_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl345/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl345/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL345 三轴加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ADXL345_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL345_TRIGGER_MODE)、[`CONFIG_ADXL345_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL345_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL345_TRIGGER`。

<a id="CONFIG_ADXL355"></a>

## 149.45 `CONFIG_ADXL355`

**提示（Prompt）**：ADXL355 三轴数字加速度计

**说明（Help）**

启用 ADXL355 三轴数字加速度计驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADXL355_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_ADXL355_INIT_PRIORITY"></a>

## 149.46 `CONFIG_ADXL355_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

ADXL355 设备初始化优先级。数值越小，启动期间越早初始化；数值越大，初始化越晚。默认为 `CONFIG_SENSOR_INIT_PRIORITY`。启用自检（Self-test）时可增大此值，例如设为 90，推迟初始化，避免延迟关键启动任务。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL355 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SENSOR_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL355`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SENSOR_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_INIT_PRIORITY)。

<a id="CONFIG_ADXL355_MEASUREMENT_MODE"></a>

## 149.47 `CONFIG_ADXL355_MEASUREMENT_MODE`

**提示（Prompt）**：测量模式（Measurement Mode）

**说明（Help）**

此模式下，按输出数据速率（Output Data Rate，ODR）持续提供加速度数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADXL355_OP_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计 → 工作模式（Operating Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL355_OP_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_OP_MODE)。

<a id="CONFIG_ADXL355_OP_MODE"></a>

## 149.48 `CONFIG_ADXL355_OP_MODE`

**提示（Prompt）**：工作模式（Operating Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL355 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ADXL355_MEASUREMENT_MODE
```

**可选项（Choices）**

```text
CONFIG_ADXL355_MEASUREMENT_MODE
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL355`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL355_MEASUREMENT_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_MEASUREMENT_MODE)。

<a id="CONFIG_ADXL355_STREAM"></a>

## 149.49 `CONFIG_ADXL355_STREAM`

**提示（Prompt）**：使用先进先出队列传输数据流（FIFO Streaming）

**说明（Help）**

使用此配置选项启用通过 RTIO 流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SPI_RTIO || CONFIG_I2C_RTIO) && CONFIG_SENSOR_ASYNC_API && CONFIG_ADXL355 && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_ADXL355_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_ADXL355`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL355_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL355_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL355_TRIGGER`。

<a id="CONFIG_ADXL355_THREAD_PRIORITY"></a>

## 149.50 `CONFIG_ADXL355_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL355_TRIGGER_OWN_THREAD && CONFIG_ADXL355_TRIGGER && CONFIG_ADXL355 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL355_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL355_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL355_TRIGGER)、[`CONFIG_ADXL355`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL355_TRIGGER`。

<a id="CONFIG_ADXL355_THREAD_STACK_SIZE"></a>

## 149.51 `CONFIG_ADXL355_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL355_TRIGGER_OWN_THREAD && CONFIG_ADXL355_TRIGGER && CONFIG_ADXL355 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL355_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL355_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL355_TRIGGER)、[`CONFIG_ADXL355`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL355_TRIGGER`。

<a id="CONFIG_ADXL355_TRIGGER_GLOBAL_THREAD"></a>

## 149.52 `CONFIG_ADXL355_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ADXL355_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ADXL355_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ADXL355_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_TRIGGER_MODE)、[`CONFIG_ADXL355_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL355_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL355_TRIGGER`。

<a id="CONFIG_ADXL355_TRIGGER_MODE"></a>

## 149.53 `CONFIG_ADXL355_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL355 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ADXL355_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_ADXL355_TRIGGER_NONE
CONFIG_ADXL355_TRIGGER_GLOBAL_THREAD
CONFIG_ADXL355_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL355`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL355_TRIGGER_NONE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_TRIGGER_NONE)、[`CONFIG_ADXL355_TRIGGER_GLOBAL_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ADXL355_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ADXL355_TRIGGER_NONE"></a>

## 149.54 `CONFIG_ADXL355_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADXL355_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL355_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_TRIGGER_MODE)。

<a id="CONFIG_ADXL355_TRIGGER_OWN_THREAD"></a>

## 149.55 `CONFIG_ADXL355_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ADXL355_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ADXL355_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl355/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl355/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL355 三轴数字加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ADXL355_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL355_TRIGGER_MODE)、[`CONFIG_ADXL355_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL355_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL355_TRIGGER`。

<a id="CONFIG_ADXL362"></a>

## 149.56 `CONFIG_ADXL362`

**提示（Prompt）**：ADXL362 传感器

**说明（Help）**

启用 ADXL362 三轴数字加速度计驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADXL362_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_ADXL362_ABS_REF_MODE"></a>

## 149.57 `CONFIG_ADXL362_ABS_REF_MODE`

**提示（Prompt）**：绝对／参考中断（Absolute/Referenced Interrupt）

**说明（Help）**

无符号值，将 ADXL362 中断模式设为绝对或参考模式：

- 0：绝对模式（Absolute Mode）。
- 1：参考模式（Referenced Mode）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL362 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL362_ACCEL_ODR_100"></a>

## 149.58 `CONFIG_ADXL362_ACCEL_ODR_100`

**提示（Prompt）**：频率：100 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_ADXL362_ACCEL_ODR_12_5"></a>

## 149.59 `CONFIG_ADXL362_ACCEL_ODR_12_5`

**提示（Prompt）**：频率：12.5 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_ADXL362_ACCEL_ODR_200"></a>

## 149.60 `CONFIG_ADXL362_ACCEL_ODR_200`

**提示（Prompt）**：频率：200 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_ADXL362_ACCEL_ODR_25"></a>

## 149.61 `CONFIG_ADXL362_ACCEL_ODR_25`

**提示（Prompt）**：频率：25 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_ADXL362_ACCEL_ODR_400"></a>

## 149.62 `CONFIG_ADXL362_ACCEL_ODR_400`

**提示（Prompt）**：频率：400 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_ADXL362_ACCEL_ODR_50"></a>

## 149.63 `CONFIG_ADXL362_ACCEL_ODR_50`

**提示（Prompt）**：频率：50 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_ADXL362_ACCEL_ODR_RUNTIME"></a>

## 149.64 `CONFIG_ADXL362_ACCEL_ODR_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_ADXL362_ACCEL_RANGE_2G"></a>

## 149.65 `CONFIG_ADXL362_ACCEL_RANGE_2G`

**提示（Prompt）**：第二代移动通信（2G）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计量程设置（Range Setting）

<a id="CONFIG_ADXL362_ACCEL_RANGE_4G"></a>

## 149.66 `CONFIG_ADXL362_ACCEL_RANGE_4G`

**提示（Prompt）**：第四代移动通信（4G）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计量程设置（Range Setting）

<a id="CONFIG_ADXL362_ACCEL_RANGE_8G"></a>

## 149.67 `CONFIG_ADXL362_ACCEL_RANGE_8G`

**提示（Prompt）**：8G

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计量程设置（Range Setting）

<a id="CONFIG_ADXL362_ACCEL_RANGE_RUNTIME"></a>

## 149.68 `CONFIG_ADXL362_ACCEL_RANGE_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 加速度计量程设置（Range Setting）

<a id="CONFIG_ADXL362_ACTIVITY_THRESHOLD"></a>

## 149.69 `CONFIG_ADXL362_ACTIVITY_THRESHOLD`

**提示（Prompt）**：上阈值（Upper Threshold Value）

**说明（Help）**

无符号值，在活动触发（Activity Trigger）模式下与 ADXL362 采样值比较。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL362 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL362_ACTIVITY_TIME"></a>

## 149.70 `CONFIG_ADXL362_ACTIVITY_TIME`

**提示（Prompt）**：上阈值时间（Upper Threshold Time）

**说明（Help）**

写入活动定时器寄存器的 8 位值，范围为 0～254。时间秒数等于此值除以输出数据速率（ODR）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL362 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL362_INACTIVITY_THRESHOLD"></a>

## 149.71 `CONFIG_ADXL362_INACTIVITY_THRESHOLD`

**提示（Prompt）**：下阈值（Lower Threshold Value）

**说明（Help）**

无符号值，在非活动触发（Inactivity Trigger）模式下与 ADXL362 采样值比较。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL362 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL362_INACTIVITY_TIME"></a>

## 149.72 `CONFIG_ADXL362_INACTIVITY_TIME`

**提示（Prompt）**：下阈值时间（Lower Threshold Time）

**说明（Help）**

写入活动定时器寄存器的 16 位值，范围为 0～65535。时间秒数等于此值除以输出数据速率（ODR）。译注：此处原文使用 activity timer，按原文保留。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL362 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL362_INTERRUPT_MODE"></a>

## 149.73 `CONFIG_ADXL362_INTERRUPT_MODE`

**提示（Prompt）**：活动与非活动中断模式（Activity/Inactivity Interrupt Mode）

**说明（Help）**

无符号值，将 ADXL362 设为不同中断模式：

- 0：默认模式（Default Mode）。
- 1：联动模式（Linked Mode）。
- 3：循环模式（Loop Mode）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL362 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL362_STREAM"></a>

## 149.74 `CONFIG_ADXL362_STREAM`

**提示（Prompt）**：使用先进先出队列传输数据流（FIFO Streaming）

**说明（Help）**

使用此配置选项启用通过 RTIO 流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SENSOR_ASYNC_API && CONFIG_ADXL362 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADXL362_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL362_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL362_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL362_TRIGGER`。

<a id="CONFIG_ADXL362_THREAD_PRIORITY"></a>

## 149.75 `CONFIG_ADXL362_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL362_TRIGGER_OWN_THREAD && CONFIG_ADXL362_TRIGGER && CONFIG_ADXL362 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADXL362_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL362_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL362_TRIGGER)、[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL362_TRIGGER`。

<a id="CONFIG_ADXL362_THREAD_STACK_SIZE"></a>

## 149.76 `CONFIG_ADXL362_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL362_TRIGGER_OWN_THREAD && CONFIG_ADXL362_TRIGGER && CONFIG_ADXL362 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器

**配置项引用（Symbol References）**：[`CONFIG_ADXL362_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL362_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL362_TRIGGER)、[`CONFIG_ADXL362`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL362)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL362_TRIGGER`。

<a id="CONFIG_ADXL362_TRIGGER_GLOBAL_THREAD"></a>

## 149.77 `CONFIG_ADXL362_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADXL362_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL362_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL362_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL362_TRIGGER`。

<a id="CONFIG_ADXL362_TRIGGER_NONE"></a>

## 149.78 `CONFIG_ADXL362_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 触发模式（Trigger Mode）

<a id="CONFIG_ADXL362_TRIGGER_OWN_THREAD"></a>

## 149.79 `CONFIG_ADXL362_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADXL362_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl362/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl362/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL362 传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL362_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL362_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL362_TRIGGER`。

<a id="CONFIG_ADXL367"></a>

## 149.80 `CONFIG_ADXL367`

**提示（Prompt）**：ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**说明（Help）**

启用 ADXL367 三轴数字加速度计驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_ADXL367_ENABLED || DT_HAS_ADI_ADXL366_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n || n
CONFIG_SPI if n || n
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ADXL367_ACTIVITY_DETECTION_MODE"></a>

## 149.81 `CONFIG_ADXL367_ACTIVITY_DETECTION_MODE`

**提示（Prompt）**：使用活动检测（Activity Detection）

**说明（Help）**

启用活动检测。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL367_ACTIVITY_THRESHOLD"></a>

## 149.82 `CONFIG_ADXL367_ACTIVITY_THRESHOLD`

**提示（Prompt）**：以原始值表示的活动阈值（Activity Threshold）

**说明（Help）**

活动检测阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 8191]
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL367_ACTIVITY_TIME"></a>

## 149.83 `CONFIG_ADXL367_ACTIVITY_TIME`

**提示（Prompt）**：活动时间（Activity Time）

**说明（Help）**

活动定时器提供稳健的活动检测，尽量减少误触发运动事件。使用定时器后，只有持续运动才能触发活动检测。此值表示采样数量；例如 ODR 为 100 Hz 时，值 100 对应 1 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL367_INACTIVITY_DETECTION_MODE"></a>

## 149.84 `CONFIG_ADXL367_INACTIVITY_DETECTION_MODE`

**提示（Prompt）**：使用非活动检测（Inactivity Detection）

**说明（Help）**

启用非活动检测。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL367_INACTIVITY_THRESHOLD"></a>

## 149.85 `CONFIG_ADXL367_INACTIVITY_THRESHOLD`

**提示（Prompt）**：以原始值表示的非活动阈值（Inactivity Threshold）

**说明（Help）**

非活动检测阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 8191]
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL367_INACTIVITY_TIME"></a>

## 149.86 `CONFIG_ADXL367_INACTIVITY_TIME`

**提示（Prompt）**：非活动时间（Inactivity Time）

**说明（Help）**

检测到非活动事件之前，所有启用轴必须持续低于非活动阈值的时间。此值表示采样数量；例如 ODR 为 100 Hz 时，值 100 对应 1 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL367_MEASUREMENT_MODE"></a>

## 149.87 `CONFIG_ADXL367_MEASUREMENT_MODE`

**提示（Prompt）**：测量模式（Measurement Mode）

**说明（Help）**

此模式下，按输出数据速率（Output Data Rate，ODR）持续提供加速度数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADXL367_OP_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计 → 工作模式（Operating Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL367_OP_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_OP_MODE)。

<a id="CONFIG_ADXL367_OP_MODE"></a>

## 149.88 `CONFIG_ADXL367_OP_MODE`

**提示（Prompt）**：工作模式（Operating Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ADXL367_MEASUREMENT_MODE
```

**可选项（Choices）**

```text
CONFIG_ADXL367_MEASUREMENT_MODE
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL367_MEASUREMENT_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_MEASUREMENT_MODE)。

<a id="CONFIG_ADXL367_REFERENCED_ACTIVITY_DETECTION_MODE"></a>

## 149.89 `CONFIG_ADXL367_REFERENCED_ACTIVITY_DETECTION_MODE`

**提示（Prompt）**：使用参考式活动检测（Referenced Activity Detection）

**说明（Help）**

活动检测可配置为参考式或绝对式。使用绝对式活动检测时，加速度采样值直接与用户设定的阈值比较，以判断是否存在运动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL367_REFERENCED_INACTIVITY_DETECTION_MODE"></a>

## 149.90 `CONFIG_ADXL367_REFERENCED_INACTIVITY_DETECTION_MODE`

**提示（Prompt）**：使用参考式非活动检测（Referenced Inactivity Detection）

**说明（Help）**

非活动检测可配置为参考式或绝对式。使用绝对式非活动检测时，加速度采样值直接与用户设定的阈值比较，以判断是否存在运动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL367_STREAM"></a>

## 149.91 `CONFIG_ADXL367_STREAM`

**提示（Prompt）**：使用先进先出队列传输数据流（FIFO Streaming）

**说明（Help）**

使用此配置选项启用通过 RTIO 流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SENSOR_ASYNC_API && CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADXL367_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL367_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL367_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL367_TRIGGER`。

<a id="CONFIG_ADXL367_THREAD_PRIORITY"></a>

## 149.92 `CONFIG_ADXL367_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367_TRIGGER_OWN_THREAD && CONFIG_ADXL367_TRIGGER && CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL367_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL367_TRIGGER)、[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL367_TRIGGER`。

<a id="CONFIG_ADXL367_THREAD_STACK_SIZE"></a>

## 149.93 `CONFIG_ADXL367_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367_TRIGGER_OWN_THREAD && CONFIG_ADXL367_TRIGGER && CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL367_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL367_TRIGGER)、[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL367_TRIGGER`。

<a id="CONFIG_ADXL367_TRIGGER_GLOBAL_THREAD"></a>

## 149.94 `CONFIG_ADXL367_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n) && <choice CONFIG_ADXL367_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ADXL367_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ADXL367_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_TRIGGER_MODE)、[`CONFIG_ADXL367_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL367_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL367_TRIGGER`。

<a id="CONFIG_ADXL367_TRIGGER_MODE"></a>

## 149.95 `CONFIG_ADXL367_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL367 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ADXL367_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_ADXL367_TRIGGER_NONE
CONFIG_ADXL367_TRIGGER_GLOBAL_THREAD
CONFIG_ADXL367_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL367`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL367_TRIGGER_NONE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_TRIGGER_NONE)、[`CONFIG_ADXL367_TRIGGER_GLOBAL_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ADXL367_TRIGGER_OWN_THREAD`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ADXL367_TRIGGER_NONE"></a>

## 149.96 `CONFIG_ADXL367_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADXL367_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL367_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_TRIGGER_MODE)。

<a id="CONFIG_ADXL367_TRIGGER_OWN_THREAD"></a>

## 149.97 `CONFIG_ADXL367_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n) && <choice CONFIG_ADXL367_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ADXL367_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl367/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl367/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL367 三轴高加速度（High-g）I²C/SPI 加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ADXL367_TRIGGER_MODE`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL367_TRIGGER_MODE)、[`CONFIG_ADXL367_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL367_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL367_TRIGGER`。

<a id="CONFIG_ADXL372"></a>

## 149.98 `CONFIG_ADXL372`

**提示（Prompt）**：ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**说明（Help）**

启用 ADXL372 三轴数字加速度计驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADXL372_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_ADXL372_ACTIVITY_THRESHOLD"></a>

## 149.99 `CONFIG_ADXL372_ACTIVITY_THRESHOLD`

**提示（Prompt）**：活动阈值，单位为毫重力加速度（mg）

**说明（Help）**

活动检测阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[0, 200000]
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL372_ACTIVITY_TIME"></a>

## 149.100 `CONFIG_ADXL372_ACTIVITY_TIME`

**提示（Prompt）**：活动时间（Activity Time）

**说明（Help）**

活动定时器提供稳健的活动检测，尽量减少误触发运动事件。使用定时器后，只有持续运动才能触发活动检测。此值表示加速度必须持续高于阈值的活动定时器单位数量，原文以 3.3 ms 的倍数描述。ODR 为 6400 Hz 时，每个编码单位为 3.3 ms；ODR 为 3200 Hz 及以下时，每个编码单位为 6.6 ms。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<!-- kconfig-navigation -->

[上一章](P148_drivers_sdhc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P150_drivers_sensor_配置项参考_2.md)
