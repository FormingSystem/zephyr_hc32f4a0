---
id: learning.zephyr-docs.kconfig-reference.page-154
title: "`drivers/sensor`配置项参考（6/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第154章\_`drivers/sensor`配置项参考（6/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_GROW_R502A_GPIO_POWER"></a>

## 154.1 `CONFIG_GROW_R502A_GPIO_POWER`

**提示（Prompt）**：GROW_R502A 传感器 VCC 和 VT GPIO

**说明（Help）**

启用对 `vin-gpios` 和 `act-gpios` 的控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GROW_R502A && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/grow_r502a/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/grow_r502a/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → GROW_R502A 指纹传感器（Fingerprint Sensor）

**配置项引用（Symbol References）**：[`CONFIG_GROW_R502A`](P153_drivers_sensor_配置项参考_5.md#CONFIG_GROW_R502A)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_GROW_R502A_THREAD_PRIORITY"></a>

## 154.2 `CONFIG_GROW_R502A_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GROW_R502A_TRIGGER_OWN_THREAD && CONFIG_GROW_R502A_TRIGGER && CONFIG_GROW_R502A && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/grow_r502a/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/grow_r502a/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → GROW_R502A 指纹传感器（Fingerprint Sensor）

**配置项引用（Symbol References）**：[`CONFIG_GROW_R502A_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_GROW_R502A_TRIGGER_OWN_THREAD)、[`CONFIG_GROW_R502A_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GROW_R502A_TRIGGER)、[`CONFIG_GROW_R502A`](P153_drivers_sensor_配置项参考_5.md#CONFIG_GROW_R502A)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GROW_R502A_TRIGGER`。

<a id="CONFIG_GROW_R502A_THREAD_STACK_SIZE"></a>

## 154.3 `CONFIG_GROW_R502A_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GROW_R502A_TRIGGER_OWN_THREAD && CONFIG_GROW_R502A_TRIGGER && CONFIG_GROW_R502A && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/grow_r502a/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/grow_r502a/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → GROW_R502A 指纹传感器（Fingerprint Sensor）

**配置项引用（Symbol References）**：[`CONFIG_GROW_R502A_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_GROW_R502A_TRIGGER_OWN_THREAD)、[`CONFIG_GROW_R502A_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GROW_R502A_TRIGGER)、[`CONFIG_GROW_R502A`](P153_drivers_sensor_配置项参考_5.md#CONFIG_GROW_R502A)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GROW_R502A_TRIGGER`。

<a id="CONFIG_GROW_R502A_TRIGGER_GLOBAL_THREAD"></a>

## 154.4 `CONFIG_GROW_R502A_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice>
```

**主动选择（Selects）**

```text
CONFIG_GROW_R502A_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/grow_r502a/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/grow_r502a/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → GROW_R502A 指纹传感器（Fingerprint Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_GROW_R502A_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GROW_R502A_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GROW_R502A_TRIGGER`。

<a id="CONFIG_GROW_R502A_TRIGGER_NONE"></a>

## 154.5 `CONFIG_GROW_R502A_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/grow_r502a/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/grow_r502a/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → GROW_R502A 指纹传感器（Fingerprint Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_GROW_R502A_TRIGGER_OWN_THREAD"></a>

## 154.6 `CONFIG_GROW_R502A_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_GROW_R502A_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/grow_r502a/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/grow_r502a/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → GROW_R502A 指纹传感器（Fingerprint Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GROW_R502A_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GROW_R502A_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GROW_R502A_TRIGGER`。

<a id="CONFIG_HC_SR04"></a>

## 154.7 `CONFIG_HC_SR04`

**提示（Prompt）**：HC-SR04 超声波测距传感器（Ultrasound Distance Sensor）

**说明（Help）**

启用 HC-SR04 测距传感器（Distance Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HC_SR04_ENABLED && CONFIG_GPIO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/hc_sr04/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hc_sr04/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HM330X"></a>

## 154.8 `CONFIG_HM330X`

**提示（Prompt）**：HM330X 粉尘颗粒传感器（Dust Particle Sensor）

**说明（Help）**

启用 HM330X 粉尘颗粒传感器（Dust Particle Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SEEED_HM330X_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/seeed/hm330x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/seeed/hm330x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_HMC5883L"></a>

## 154.9 `CONFIG_HMC5883L`

**提示（Prompt）**：HMC5883L 磁力计（Magnetometer）

**说明（Help）**

启用基于 I2C 的 HMC5883L 磁力计（Magnetometer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HONEYWELL_HMC5883L_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/honeywell/hmc5883l/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/hmc5883l/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_HMC5883L_FS"></a>

## 154.10 `CONFIG_HMC5883L_FS`

**提示（Prompt）**：满量程范围（Full-scale Range）

**说明（Help）**

磁力计满量程范围（Magnetometer Full-scale Range）。配置值 X 表示范围为 ±X 高斯（Gauss）。有效值为 0.88、1.3、1.9、2.5、4、4.7、5.6 和 8.1。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HMC5883L && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
"1.3"
```

**定义位置（Location）**：[`drivers/sensor/honeywell/hmc5883l/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/hmc5883l/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HMC5883L 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_HMC5883L`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HMC5883L)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HMC5883L_ODR"></a>

## 154.11 `CONFIG_HMC5883L_ODR`

**提示（Prompt）**：输出数据速率（Output Data Rate，ODR）

**说明（Help）**

磁力计输出数据速率（Output Data Rate），以每秒采样数表示。芯片支持的数据速率为 0.75、1.5、3、7.5、15、30 和 75。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HMC5883L && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
"15"
```

**定义位置（Location）**：[`drivers/sensor/honeywell/hmc5883l/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/hmc5883l/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HMC5883L 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_HMC5883L`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HMC5883L)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HMC5883L_THREAD_PRIORITY"></a>

## 154.12 `CONFIG_HMC5883L_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HMC5883L_TRIGGER_OWN_THREAD && CONFIG_HMC5883L && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/honeywell/hmc5883l/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/hmc5883l/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HMC5883L 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_HMC5883L_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HMC5883L_TRIGGER_OWN_THREAD)、[`CONFIG_HMC5883L`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HMC5883L)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HMC5883L_THREAD_STACK_SIZE"></a>

## 154.13 `CONFIG_HMC5883L_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HMC5883L_TRIGGER_OWN_THREAD && CONFIG_HMC5883L && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/honeywell/hmc5883l/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/hmc5883l/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HMC5883L 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_HMC5883L_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HMC5883L_TRIGGER_OWN_THREAD)、[`CONFIG_HMC5883L`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HMC5883L)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HMC5883L_TRIGGER_GLOBAL_THREAD"></a>

## 154.14 `CONFIG_HMC5883L_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_HMC5883L_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/honeywell/hmc5883l/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/hmc5883l/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HMC5883L 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_HMC5883L_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HMC5883L_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HMC5883L_TRIGGER`。

<a id="CONFIG_HMC5883L_TRIGGER_NONE"></a>

## 154.15 `CONFIG_HMC5883L_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/hmc5883l/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/hmc5883l/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HMC5883L 磁力计（Magnetometer） → 触发模式（Trigger Mode）

<a id="CONFIG_HMC5883L_TRIGGER_OWN_THREAD"></a>

## 154.16 `CONFIG_HMC5883L_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_HMC5883L_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/honeywell/hmc5883l/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/hmc5883l/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HMC5883L 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_HMC5883L_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HMC5883L_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HMC5883L_TRIGGER`。

<a id="CONFIG_HP206C"></a>

## 154.17 `CONFIG_HP206C`

**提示（Prompt）**：HopeRF HP206C 精密气压计与高度计传感器（Precision Barometer and Altimeter Sensor）

**说明（Help）**

启用 HopeRF HP206C 气压计与高度计（Barometer and Altimeter）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HOPERF_HP206C_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/hp206c/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hp206c/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_HP206C_ALT_OFFSET"></a>

## 154.18 `CONFIG_HP206C_ALT_OFFSET`

**提示（Prompt）**：高度偏移量（Altitude Offset），单位为 cm

**说明（Help）**

用于补偿高度计算的数值，单位为厘米（cm）。有关如何选择此值的更多信息，请参阅数据手册第 6.1.1 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_HP206C_ALT_OFFSET_RUNTIME && CONFIG_HP206C && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/hp206c/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hp206c/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HopeRF HP206C 精密气压计与高度计传感器（Precision Barometer and Altimeter Sensor）

**配置项引用（Symbol References）**：[`CONFIG_HP206C_ALT_OFFSET_RUNTIME`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HP206C_ALT_OFFSET_RUNTIME)、[`CONFIG_HP206C`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HP206C)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HP206C_ALT_OFFSET_RUNTIME"></a>

## 154.19 `CONFIG_HP206C_ALT_OFFSET_RUNTIME`

**提示（Prompt）**：在运行时设置高度偏移量（Altitude Offset）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HP206C && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/hp206c/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hp206c/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HopeRF HP206C 精密气压计与高度计传感器（Precision Barometer and Altimeter Sensor）

**配置项引用（Symbol References）**：[`CONFIG_HP206C`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HP206C)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HP206C_OSR"></a>

## 154.20 `CONFIG_HP206C_OSR`

**提示（Prompt）**：过采样率（Oversampling Rate）

**说明（Help）**

允许的值：4096、2048、1024、512、256、128。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_HP206C_OSR_RUNTIME && CONFIG_HP206C && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/sensor/hp206c/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hp206c/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HopeRF HP206C 精密气压计与高度计传感器（Precision Barometer and Altimeter Sensor）

**配置项引用（Symbol References）**：[`CONFIG_HP206C_OSR_RUNTIME`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HP206C_OSR_RUNTIME)、[`CONFIG_HP206C`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HP206C)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HP206C_OSR_RUNTIME"></a>

## 154.21 `CONFIG_HP206C_OSR_RUNTIME`

**提示（Prompt）**：在运行时设置过采样率（Oversampling Rate）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HP206C && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/hp206c/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hp206c/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HopeRF HP206C 精密气压计与高度计传感器（Precision Barometer and Altimeter Sensor）

**配置项引用（Symbol References）**：[`CONFIG_HP206C`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HP206C)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HS300X"></a>

## 154.22 `CONFIG_HS300X`

**提示（Prompt）**：HS300x 温湿度传感器（Temperature and Humidity Sensor）

**说明（Help）**

启用 HS300x 温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_HS300X_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/renesas/hs300x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/hs300x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_HS400X"></a>

## 154.23 `CONFIG_HS400X`

**提示（Prompt）**：HS400x 传感器（Sensor）

**说明（Help）**

启用 HS400x 温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_HS400X_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/renesas/hs400x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/hs400x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HS400X_CRC"></a>

## 154.24 `CONFIG_HS400X_CRC`

**提示（Prompt）**：HS400X 循环冗余校验（CRC Check）

**说明（Help）**

验证测量数据中的校验和字节（Checksum Byte）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HS400X && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/sensor/renesas/hs400x/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/hs400x/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HS400x 传感器（Sensor）

**配置项引用（Symbol References）**：[`CONFIG_HS400X`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HS400X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_HTS221"></a>

## 154.25 `CONFIG_HTS221`

**提示（Prompt）**：HTS221 温湿度传感器（Temperature and Humidity Sensor）

**说明（Help）**

启用基于 I2C/SPI 的 HTS221 温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_HTS221_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_HTS221
```

**定义位置（Location）**：[`drivers/sensor/st/hts221/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/hts221/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_HTS221`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_HTS221)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_HTS221`。

<a id="CONFIG_HTS221_ODR"></a>

## 154.26 `CONFIG_HTS221_ODR`

**提示（Prompt）**：输出数据速率（Output Data Rate，ODR）

**说明（Help）**

传感器输出数据速率（Output Data Rate），以每秒采样数表示。芯片支持的数据速率为 1、7 和 12.5。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HTS221 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
"1"
```

**定义位置（Location）**：[`drivers/sensor/st/hts221/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/hts221/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HTS221 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_HTS221`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HTS221_THREAD_PRIORITY"></a>

## 154.27 `CONFIG_HTS221_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTS221_TRIGGER_OWN_THREAD && CONFIG_HTS221 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/hts221/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/hts221/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HTS221 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_HTS221_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221_TRIGGER_OWN_THREAD)、[`CONFIG_HTS221`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HTS221_THREAD_STACK_SIZE"></a>

## 154.28 `CONFIG_HTS221_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTS221_TRIGGER_OWN_THREAD && CONFIG_HTS221 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/hts221/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/hts221/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HTS221 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_HTS221_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221_TRIGGER_OWN_THREAD)、[`CONFIG_HTS221`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HTS221_TRIGGER_GLOBAL_THREAD"></a>

## 154.29 `CONFIG_HTS221_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_HTS221_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/hts221/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/hts221/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HTS221 温湿度传感器（Temperature and Humidity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_HTS221_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTS221_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HTS221_TRIGGER`。

<a id="CONFIG_HTS221_TRIGGER_MODE"></a>

## 154.30 `CONFIG_HTS221_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTS221 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_HTS221_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_HTS221_TRIGGER_NONE
CONFIG_HTS221_TRIGGER_GLOBAL_THREAD
CONFIG_HTS221_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/hts221/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/hts221/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HTS221 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_HTS221`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_HTS221_TRIGGER_GLOBAL_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221_TRIGGER_GLOBAL_THREAD)、[`CONFIG_HTS221_TRIGGER_NONE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221_TRIGGER_NONE)、[`CONFIG_HTS221_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221_TRIGGER_OWN_THREAD)。

<a id="CONFIG_HTS221_TRIGGER_NONE"></a>

## 154.31 `CONFIG_HTS221_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HTS221_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/hts221/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/hts221/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HTS221 温湿度传感器（Temperature and Humidity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_HTS221_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTS221_TRIGGER_MODE)。

<a id="CONFIG_HTS221_TRIGGER_OWN_THREAD"></a>

## 154.32 `CONFIG_HTS221_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_HTS221_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/hts221/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/hts221/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → HTS221 温湿度传感器（Temperature and Humidity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_HTS221_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTS221_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HTS221_TRIGGER`。

<a id="CONFIG_HTU31D"></a>

## 154.33 `CONFIG_HTU31D`

**提示（Prompt）**：HTU31D 温湿度传感器（Humidity and Temperature Sensor）

**说明（Help）**

启用通过 I2C 通信的 TE Connectivity HTU31D 数字温湿度传感器（Digital Humidity and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MEAS_HTU31D_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/sensor/meas/htu31d/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/htu31d/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_HX711_SPI"></a>

## 154.34 `CONFIG_HX711_SPI`

**提示（Prompt）**：Avia Semiconductor HX711：SPI 总线上用于称重传感器／应变计的专用 24 位 ADC

**说明（Help）**

启用 Avia Semiconductor HX711 驱动；原文将其描述为 SPI 总线上专用于称重传感器（Load Cell）／应变计（Strain Gauge）的 24 位模数转换器（ADC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AVIA_HX711_SPI_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/hx711_spi/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hx711_spi/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_HX711_SPI_THREAD_PRIORITY"></a>

## 154.35 `CONFIG_HX711_SPI_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HX711_SPI_TRIGGER_OWN_THREAD && CONFIG_HX711_SPI_TRIGGER && CONFIG_HX711_SPI && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/hx711_spi/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hx711_spi/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Avia Semiconductor HX711：SPI 总线上用于称重传感器／应变计的专用 24 位 ADC → 使用专用工作队列线程（Own Workqueue Thread）

**配置项引用（Symbol References）**：[`CONFIG_HX711_SPI_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI_TRIGGER_OWN_THREAD)、[`CONFIG_HX711_SPI_TRIGGER`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI_TRIGGER)、[`CONFIG_HX711_SPI`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HX711_SPI_THREAD_STACK_SIZE"></a>

## 154.36 `CONFIG_HX711_SPI_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HX711_SPI_TRIGGER_OWN_THREAD && CONFIG_HX711_SPI_TRIGGER && CONFIG_HX711_SPI && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/hx711_spi/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hx711_spi/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Avia Semiconductor HX711：SPI 总线上用于称重传感器／应变计的专用 24 位 ADC → 使用专用工作队列线程（Own Workqueue Thread）

**配置项引用（Symbol References）**：[`CONFIG_HX711_SPI_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI_TRIGGER_OWN_THREAD)、[`CONFIG_HX711_SPI_TRIGGER`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI_TRIGGER)、[`CONFIG_HX711_SPI`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_HX711_SPI_TRIGGER"></a>

## 154.37 `CONFIG_HX711_SPI_TRIGGER`

**提示（Prompt）**：使用数据就绪触发器（Data Ready Trigger）

**说明（Help）**

通过 DOUT 线下降沿中断，在数据就绪时触发数据传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_HX711_SPI && CONFIG_SENSOR
```

**被选择（Selected by）**

```text
CONFIG_HX711_SPI_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/hx711_spi/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hx711_spi/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Avia Semiconductor HX711：SPI 总线上用于称重传感器／应变计的专用 24 位 ADC

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HX711_SPI`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_HX711_SPI_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI_TRIGGER_OWN_THREAD)。

<a id="CONFIG_HX711_SPI_TRIGGER_OWN_THREAD"></a>

## 154.38 `CONFIG_HX711_SPI_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用工作队列线程（Own Workqueue Thread）

**说明（Help）**

中断发生时，中断处理程序提交一个工作项（Work），用于执行用户回调。默认提交到系统工作队列（System Workqueue）。启用此选项后，将工作项提交到驱动自身的工作队列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HX711_SPI && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_HX711_SPI_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/hx711_spi/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/hx711_spi/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Avia Semiconductor HX711：SPI 总线上用于称重传感器／应变计的专用 24 位 ADC

**配置项引用（Symbol References）**：[`CONFIG_HX711_SPI`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_HX711_SPI_TRIGGER`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HX711_SPI_TRIGGER)。

<a id="CONFIG_I3G4250D"></a>

## 154.39 `CONFIG_I3G4250D`

**提示（Prompt）**：I3G4250D 三轴数字输出陀螺仪（Three-axis Digital Output Gyroscope）

**说明（Help）**

启用基于 SPI 的 I3G4250D 三轴运动跟踪器件（Three-axis Motion Tracking Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_I3G4250D_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_I3G4250D
```

**定义位置（Location）**：[`drivers/sensor/st/i3g4250d/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/i3g4250d/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_I3G4250D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_I3G4250D)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_I3G4250D`。

<a id="CONFIG_IAQ_CORE_MAX_READ_RETRIES"></a>

## 154.40 `CONFIG_IAQ_CORE_MAX_READ_RETRIES`

**提示（Prompt）**：读取重试次数

**说明（Help）**

读取失败或设备尚未就绪时的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AMS_IAQ_CORE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/sensor/ams/ams_iAQcore/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ams_iAQcore/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → iAQ-core 数字挥发性有机物（VOC）传感器

**配置项引用（Symbol References）**：[`CONFIG_AMS_IAQ_CORE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AMS_IAQ_CORE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM40627"></a>

## 154.41 `CONFIG_ICM40627`

**提示（Prompt）**：ICM40627 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**说明（Help）**

启用基于 I2C 的 ICM40627 六轴运动跟踪器件（Six-axis Motion Tracking Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INVENSENSE_ICM40627_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm40627/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm40627/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_ICM40627_THREAD_PRIORITY"></a>

## 154.42 `CONFIG_ICM40627_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM40627_TRIGGER_OWN_THREAD && CONFIG_ICM40627_TRIGGER && CONFIG_ICM40627 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM40627 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM40627_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627_TRIGGER_OWN_THREAD)、[`CONFIG_ICM40627_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM40627_TRIGGER)、[`CONFIG_ICM40627`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM40627_TRIGGER`。

<a id="CONFIG_ICM40627_THREAD_STACK_SIZE"></a>

## 154.43 `CONFIG_ICM40627_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM40627_TRIGGER_OWN_THREAD && CONFIG_ICM40627_TRIGGER && CONFIG_ICM40627 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM40627 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM40627_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627_TRIGGER_OWN_THREAD)、[`CONFIG_ICM40627_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM40627_TRIGGER)、[`CONFIG_ICM40627`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM40627_TRIGGER`。

<a id="CONFIG_ICM40627_TRIGGER_GLOBAL_THREAD"></a>

## 154.44 `CONFIG_ICM40627_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ICM40627_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ICM40627_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM40627 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICM40627_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627_TRIGGER_MODE)、[`CONFIG_ICM40627_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM40627_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM40627_TRIGGER`。

<a id="CONFIG_ICM40627_TRIGGER_MODE"></a>

## 154.45 `CONFIG_ICM40627_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM40627 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ICM40627_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_ICM40627_TRIGGER_NONE
CONFIG_ICM40627_TRIGGER_GLOBAL_THREAD
CONFIG_ICM40627_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM40627 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM40627`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ICM40627_TRIGGER_NONE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627_TRIGGER_NONE)、[`CONFIG_ICM40627_TRIGGER_GLOBAL_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ICM40627_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ICM40627_TRIGGER_NONE"></a>

## 154.46 `CONFIG_ICM40627_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ICM40627_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM40627 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ICM40627_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627_TRIGGER_MODE)。

<a id="CONFIG_ICM40627_TRIGGER_OWN_THREAD"></a>

## 154.47 `CONFIG_ICM40627_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ICM40627_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ICM40627_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM40627 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICM40627_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM40627_TRIGGER_MODE)、[`CONFIG_ICM40627_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM40627_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM40627_TRIGGER`。

<a id="CONFIG_ICM42605"></a>

## 154.48 `CONFIG_ICM42605`

**提示（Prompt）**：ICM42605 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**说明（Help）**

启用基于 SPI 的 ICM42605 六轴运动跟踪器件（Six-axis Motion Tracking Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INVENSENSE_ICM42605_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42605/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42605/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ICM42605_THREAD_PRIORITY"></a>

## 154.49 `CONFIG_ICM42605_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD && CONFIG_ICM42605 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42605/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42605/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42605 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ICM42605`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42605)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM42605_THREAD_STACK_SIZE"></a>

## 154.50 `CONFIG_ICM42605_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD && CONFIG_ICM42605 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42605/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42605/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42605 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ICM42605`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42605)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD"></a>

## 154.51 `CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ICM42605_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42605/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42605/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42605 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ICM42605_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM42605_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM42605_TRIGGER`。

<a id="CONFIG_ICM42605_TRIGGER_MODE"></a>

## 154.52 `CONFIG_ICM42605_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM42605 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_ICM42605_TRIGGER_NONE
CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42605/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42605/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42605 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM42605`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42605)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42605_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ICM42605_TRIGGER_NONE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42605_TRIGGER_NONE)。

<a id="CONFIG_ICM42605_TRIGGER_NONE"></a>

## 154.53 `CONFIG_ICM42605_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ICM42605_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42605/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42605/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42605 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ICM42605_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42605_TRIGGER_MODE)。

<a id="CONFIG_ICM4268X"></a>

## 154.54 `CONFIG_ICM4268X`

**提示（Prompt）**：ICM4268X 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**说明（Help）**

启用基于 SPI 的 ICM4268X 六轴运动跟踪器件（Six-axis Motion Tracking Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INVENSENSE_ICM4268X_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/tdk/icm4268x/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm4268x/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_ICM4268X_DECODER"></a>

## 154.55 `CONFIG_ICM4268X_DECODER`

**提示（Prompt）**：ICM4268X 解码逻辑（Decoder Logic）

**说明（Help）**

编译 ICM4268X 解码器（Decoder）API，用于解码传感器返回的原始数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM4268X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm4268x/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm4268x/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM4268X 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM4268X`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM4268X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_ICM4268X_STREAM"></a>

## 154.56 `CONFIG_ICM4268X_STREAM`

**提示（Prompt）**：使用硬件先入先出队列（FIFO）流式传输数据

**说明（Help）**

使用此配置选项，启用通过实时 I/O（RTIO）子系统流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SENSOR_ASYNC_API && CONFIG_ICM4268X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ICM4268X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm4268x/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm4268x/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM4268X 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_ICM4268X`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM4268X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ICM4268X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM4268X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM4268X_TRIGGER`。

<a id="CONFIG_ICM4268X_THREAD_PRIORITY"></a>

## 154.57 `CONFIG_ICM4268X_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**

处理中断的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM4268X_TRIGGER_OWN_THREAD && CONFIG_ICM4268X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm4268x/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm4268x/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM4268X 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM4268X_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM4268X_TRIGGER_OWN_THREAD)、[`CONFIG_ICM4268X`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM4268X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM4268X_THREAD_STACK_SIZE"></a>

## 154.58 `CONFIG_ICM4268X_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**

线程栈（Thread Stack）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM4268X_TRIGGER_OWN_THREAD && CONFIG_ICM4268X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm4268x/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm4268x/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM4268X 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM4268X_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM4268X_TRIGGER_OWN_THREAD)、[`CONFIG_ICM4268X`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM4268X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM4268X_TRIGGER_GLOBAL_THREAD"></a>

## 154.59 `CONFIG_ICM4268X_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ICM4268X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm4268x/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm4268x/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM4268X 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ICM4268X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM4268X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM4268X_TRIGGER`。

<a id="CONFIG_ICM4268X_TRIGGER_NONE"></a>

## 154.60 `CONFIG_ICM4268X_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm4268x/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm4268x/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM4268X 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

<a id="CONFIG_ICM4268X_TRIGGER_OWN_THREAD"></a>

## 154.61 `CONFIG_ICM4268X_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ICM4268X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm4268x/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm4268x/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM4268X 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ICM4268X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM4268X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM4268X_TRIGGER`。

<a id="CONFIG_ICM42X70"></a>

## 154.62 `CONFIG_ICM42X70`

**提示（Prompt）**：ICM42670-P/-S 六轴或 ICM42370-P 三轴运动跟踪器件

**说明（Help）**

启用基于 SPI 或 I2C 的 ICM42x70 六轴或三轴运动跟踪器件（Motion Tracking Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_INVENSENSE_ICM42670P_ENABLED || DT_HAS_INVENSENSE_ICM42670S_ENABLED || DT_HAS_INVENSENSE_ICM42370P_ENABLED) && CONFIG_ZEPHYR_HAL_TDK_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI if n || n || n
CONFIG_I2C if n || n || n
CONFIG_TDK_APEX if n || n || n || n || n || n || n || n || n || n || n || n
CONFIG_USE_EMD_ICM42670 if DT_HAS_INVENSENSE_ICM42670P_ENABLED || DT_HAS_INVENSENSE_ICM42670S_ENABLED
CONFIG_USE_EMD_ICM42370 if DT_HAS_INVENSENSE_ICM42370P_ENABLED
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42x70/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42x70/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_TDK_APEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TDK_APEX)、[`CONFIG_USE_EMD_ICM42670`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM42670)、[`CONFIG_USE_EMD_ICM42370`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM42370)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`、`CONFIG_TDK_APEX`。

<a id="CONFIG_ICM42X70_THREAD_PRIORITY"></a>

## 154.63 `CONFIG_ICM42X70_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM42X70_TRIGGER_OWN_THREAD && CONFIG_ICM42X70 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42x70/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42x70/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42670-P/-S 六轴或 ICM42370-P 三轴运动跟踪器件

**配置项引用（Symbol References）**：[`CONFIG_ICM42X70_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70_TRIGGER_OWN_THREAD)、[`CONFIG_ICM42X70`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM42X70_THREAD_STACK_SIZE"></a>

## 154.64 `CONFIG_ICM42X70_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM42X70_TRIGGER_OWN_THREAD && CONFIG_ICM42X70 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42x70/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42x70/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42670-P/-S 六轴或 ICM42370-P 三轴运动跟踪器件

**配置项引用（Symbol References）**：[`CONFIG_ICM42X70_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70_TRIGGER_OWN_THREAD)、[`CONFIG_ICM42X70`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM42X70_TRIGGER_GLOBAL_THREAD"></a>

## 154.65 `CONFIG_ICM42X70_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n || n) && <choice CONFIG_ICM42X70_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ICM42X70_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42x70/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42x70/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42670-P/-S 六轴或 ICM42370-P 三轴运动跟踪器件 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICM42X70_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70_TRIGGER_MODE)、[`CONFIG_ICM42X70_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM42X70_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM42X70_TRIGGER`。

<a id="CONFIG_ICM42X70_TRIGGER_MODE"></a>

## 154.66 `CONFIG_ICM42X70_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM42X70 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ICM42X70_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_ICM42X70_TRIGGER_NONE
CONFIG_ICM42X70_TRIGGER_GLOBAL_THREAD
CONFIG_ICM42X70_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42x70/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42x70/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42670-P/-S 六轴或 ICM42370-P 三轴运动跟踪器件

**配置项引用（Symbol References）**：[`CONFIG_ICM42X70`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ICM42X70_TRIGGER_NONE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70_TRIGGER_NONE)、[`CONFIG_ICM42X70_TRIGGER_GLOBAL_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ICM42X70_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ICM42X70_TRIGGER_NONE"></a>

## 154.67 `CONFIG_ICM42X70_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ICM42X70_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42x70/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42x70/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42670-P/-S 六轴或 ICM42370-P 三轴运动跟踪器件 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ICM42X70_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70_TRIGGER_MODE)。

<a id="CONFIG_ICM42X70_TRIGGER_OWN_THREAD"></a>

## 154.68 `CONFIG_ICM42X70_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n || n) && <choice CONFIG_ICM42X70_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ICM42X70_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm42x70/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm42x70/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM42670-P/-S 六轴或 ICM42370-P 三轴运动跟踪器件 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICM42X70_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70_TRIGGER_MODE)、[`CONFIG_ICM42X70_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM42X70_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM42X70_TRIGGER`。

<a id="CONFIG_ICM45686"></a>

## 154.69 `CONFIG_ICM45686`

**提示（Prompt）**：ICM45686 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device）

**说明（Help）**

启用 ICM45686 高精度六轴运动跟踪器件（High-precision 6-axis Motion Tracking Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && (DT_HAS_INVENSENSE_ICM45605_ENABLED || DT_HAS_INVENSENSE_ICM45605S_ENABLED || DT_HAS_INVENSENSE_ICM45686_ENABLED || DT_HAS_INVENSENSE_ICM45686S_ENABLED || DT_HAS_INVENSENSE_ICM45688P_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI if n || n || n || n || n
CONFIG_SPI_RTIO if n || n || n || n || n
CONFIG_I2C if n || n || n || n || n
CONFIG_I2C_RTIO if n || n || n || n || n
CONFIG_I3C if n || n || n || n || n
CONFIG_I3C_RTIO if n || n || n || n || n
CONFIG_USE_EMD_ICM45605 if DT_HAS_INVENSENSE_ICM45605_ENABLED
CONFIG_USE_EMD_ICM45605S if DT_HAS_INVENSENSE_ICM45605S_ENABLED
CONFIG_USE_EMD_ICM45686 if DT_HAS_INVENSENSE_ICM45686_ENABLED
CONFIG_USE_EMD_ICM45686S if DT_HAS_INVENSENSE_ICM45686S_ENABLED
CONFIG_USE_EMD_ICM45688P if DT_HAS_INVENSENSE_ICM45688P_ENABLED
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm45686/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm45686/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_USE_EMD_ICM45605`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM45605)、[`CONFIG_USE_EMD_ICM45605S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM45605S)、[`CONFIG_USE_EMD_ICM45686`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM45686)、[`CONFIG_USE_EMD_ICM45686S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM45686S)、[`CONFIG_USE_EMD_ICM45688P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM45688P)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_ICM45686_STREAM"></a>

## 154.70 `CONFIG_ICM45686_STREAM`

**提示（Prompt）**：流式模式（Streaming Mode）

**说明（Help）**

启用传感器数据流式传输（Streaming）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_GPIO || n) && (n || n || n || n || n || n || n || n || n || n) && CONFIG_ICM45686 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm45686/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm45686/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM45686 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM45686_THREAD_PRIORITY"></a>

## 154.71 `CONFIG_ICM45686_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**

用于处理触发事件的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM45686_TRIGGER_OWN_THREAD && CONFIG_ICM45686 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm45686/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm45686/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM45686 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM45686_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686_TRIGGER_OWN_THREAD)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM45686_THREAD_STACK_SIZE"></a>

## 154.72 `CONFIG_ICM45686_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**

线程栈（Thread Stack）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM45686_TRIGGER_OWN_THREAD && CONFIG_ICM45686 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm45686/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm45686/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM45686 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM45686_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686_TRIGGER_OWN_THREAD)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM45686_TRIGGER_GLOBAL_THREAD"></a>

## 154.73 `CONFIG_ICM45686_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n || n || n || n) && !CONFIG_ICM45686_STREAM && <choice>
```

**主动选择（Selects）**

```text
CONFIG_ICM45686_TRIGGER
CONFIG_TDK_APEX
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm45686/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm45686/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM45686 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICM45686_STREAM`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686_STREAM)、[`CONFIG_ICM45686_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM45686_TRIGGER)、[`CONFIG_TDK_APEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TDK_APEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM45686_TRIGGER`、`CONFIG_TDK_APEX`。

<a id="CONFIG_ICM45686_TRIGGER_NONE"></a>

## 154.74 `CONFIG_ICM45686_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm45686/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm45686/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM45686 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

<a id="CONFIG_ICM45686_TRIGGER_OWN_THREAD"></a>

## 154.75 `CONFIG_ICM45686_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n || n || n || n) && !CONFIG_ICM45686_STREAM && <choice>
```

**主动选择（Selects）**

```text
CONFIG_ICM45686_TRIGGER
CONFIG_TDK_APEX
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm45686/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm45686/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM45686 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICM45686_STREAM`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686_STREAM)、[`CONFIG_ICM45686_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM45686_TRIGGER)、[`CONFIG_TDK_APEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TDK_APEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM45686_TRIGGER`、`CONFIG_TDK_APEX`。

<a id="CONFIG_ICM566XX"></a>

## 154.76 `CONFIG_ICM566XX`

**提示（Prompt）**：ICM566XX 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device）

**说明（Help）**

启用 ICM566XX 高精度六轴运动跟踪器件（High-precision 6-axis Motion Tracking Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_INVENSENSE_ICM56622_ENABLED || DT_HAS_INVENSENSE_ICM56686_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI if n || n
CONFIG_SPI_RTIO if n || n
CONFIG_I2C if n || n
CONFIG_I2C_RTIO if n || n
CONFIG_I3C if n || n
CONFIG_I3C_RTIO if n || n
CONFIG_USE_EMD_ICM56622 if DT_HAS_INVENSENSE_ICM56622_ENABLED
CONFIG_USE_EMD_ICM56686 if DT_HAS_INVENSENSE_ICM56686_ENABLED
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm566xx/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm566xx/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_USE_EMD_ICM56622`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM56622)、[`CONFIG_USE_EMD_ICM56686`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM56686)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_EMD_ICM56622`、`CONFIG_USE_EMD_ICM56686`。

<a id="CONFIG_ICM566XX_STREAM"></a>

## 154.77 `CONFIG_ICM566XX_STREAM`

**提示（Prompt）**：流式模式（Streaming Mode）

**说明（Help）**

启用传感器数据流式传输（Streaming）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || n || n || n) && CONFIG_ICM566XX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm566xx/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm566xx/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM566XX 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM566XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM566XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM566XX_THREAD_PRIORITY"></a>

## 154.78 `CONFIG_ICM566XX_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**

用于处理触发事件的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM566XX_TRIGGER_OWN_THREAD && CONFIG_ICM566XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm566xx/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm566xx/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM566XX 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM566XX_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM566XX_TRIGGER_OWN_THREAD)、[`CONFIG_ICM566XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM566XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM566XX_THREAD_STACK_SIZE"></a>

## 154.79 `CONFIG_ICM566XX_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**

线程栈（Thread Stack）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICM566XX_TRIGGER_OWN_THREAD && CONFIG_ICM566XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm566xx/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm566xx/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM566XX 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_ICM566XX_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM566XX_TRIGGER_OWN_THREAD)、[`CONFIG_ICM566XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM566XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ICM566XX_TRIGGER_GLOBAL_THREAD"></a>

## 154.80 `CONFIG_ICM566XX_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || n) && !CONFIG_ICM566XX_STREAM && <choice>
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_ICM566XX_TRIGGER
CONFIG_TDK_APEX
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm566xx/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm566xx/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM566XX 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ICM566XX_STREAM`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM566XX_STREAM)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICM566XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM566XX_TRIGGER)、[`CONFIG_TDK_APEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TDK_APEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM566XX_TRIGGER`、`CONFIG_TDK_APEX`。

<a id="CONFIG_ICM566XX_TRIGGER_NONE"></a>

## 154.81 `CONFIG_ICM566XX_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm566xx/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm566xx/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM566XX 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

<a id="CONFIG_ICM566XX_TRIGGER_OWN_THREAD"></a>

## 154.82 `CONFIG_ICM566XX_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || n) && !CONFIG_ICM566XX_STREAM && <choice>
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_ICM566XX_TRIGGER
CONFIG_TDK_APEX
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm566xx/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm566xx/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM566XX 高精度六轴运动跟踪器件（High-precision 6-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ICM566XX_STREAM`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM566XX_STREAM)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICM566XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM566XX_TRIGGER)、[`CONFIG_TDK_APEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TDK_APEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICM566XX_TRIGGER`、`CONFIG_TDK_APEX`。

<a id="CONFIG_ICP101XX"></a>

## 154.83 `CONFIG_ICP101XX`

**提示（Prompt）**：ICP101XX 大气压力与温度传感器（Barometric Pressure and Temperature Sensor）

**说明（Help）**

启用 ICP101XX 大气压力／温度传感器（Barometric Pressure/Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INVENSENSE_ICP101XX_ENABLED && CONFIG_ZEPHYR_HAL_TDK_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_USE_EMD_ICP101XX
```

**定义位置（Location）**：[`drivers/sensor/tdk/icp101xx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icp101xx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_EMD_ICP101XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICP101XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_ICP201XX"></a>

## 154.84 `CONFIG_ICP201XX`

**提示（Prompt）**：ICP201xx 大气压力与温度传感器（Barometric Pressure and Temperature Sensor）

**说明（Help）**

启用 ICP101xx 大气压力与温度传感器（Barometric Pressure and Temperature Sensor）驱动。

译注：本条帮助原文写作 ICP101xx，而对应选项标题写作 ICP201xx；此处保留该差异，具体器件支持应结合所链接的源代码核对。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INVENSENSE_ICP201XX_ENABLED && CONFIG_ZEPHYR_HAL_TDK_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_USE_EMD_ICP201XX
CONFIG_FPU if CONFIG_CPU_HAS_FPU
```

**定义位置（Location）**：[`drivers/sensor/tdk/icp201xx/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icp201xx/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_USE_EMD_ICP201XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICP201XX)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_ICP201XX_THREAD_PRIORITY"></a>

## 154.85 `CONFIG_ICP201XX_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICP201XX_TRIGGER_OWN_THREAD && CONFIG_ICP201XX_TRIGGER && CONFIG_ICP201XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICP201xx 大气压力与温度传感器（Barometric Pressure and Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ICP201XX_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX_TRIGGER_OWN_THREAD)、[`CONFIG_ICP201XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICP201XX_TRIGGER)、[`CONFIG_ICP201XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICP201XX_TRIGGER`。

<a id="CONFIG_ICP201XX_THREAD_STACK_SIZE"></a>

## 154.86 `CONFIG_ICP201XX_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ICP201XX_TRIGGER_OWN_THREAD && CONFIG_ICP201XX_TRIGGER && CONFIG_ICP201XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICP201xx 大气压力与温度传感器（Barometric Pressure and Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ICP201XX_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX_TRIGGER_OWN_THREAD)、[`CONFIG_ICP201XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICP201XX_TRIGGER)、[`CONFIG_ICP201XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICP201XX_TRIGGER`。

<a id="CONFIG_ICP201XX_TRIGGER_GLOBAL_THREAD"></a>

## 154.87 `CONFIG_ICP201XX_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ICP201XX_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ICP201XX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICP201xx 大气压力与温度传感器（Barometric Pressure and Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICP201XX_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX_TRIGGER_MODE)、[`CONFIG_ICP201XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICP201XX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICP201XX_TRIGGER`。

<a id="CONFIG_ICP201XX_TRIGGER_MODE"></a>

## 154.88 `CONFIG_ICP201XX_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ICP201XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ICP201XX_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_ICP201XX_TRIGGER_NONE
CONFIG_ICP201XX_TRIGGER_GLOBAL_THREAD
CONFIG_ICP201XX_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICP201xx 大气压力与温度传感器（Barometric Pressure and Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ICP201XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ICP201XX_TRIGGER_NONE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX_TRIGGER_NONE)、[`CONFIG_ICP201XX_TRIGGER_GLOBAL_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ICP201XX_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ICP201XX_TRIGGER_NONE"></a>

## 154.89 `CONFIG_ICP201XX_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ICP201XX_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICP201xx 大气压力与温度传感器（Barometric Pressure and Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ICP201XX_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX_TRIGGER_MODE)。

<a id="CONFIG_ICP201XX_TRIGGER_OWN_THREAD"></a>

## 154.90 `CONFIG_ICP201XX_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_ICP201XX_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_ICP201XX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICP201xx 大气压力与温度传感器（Barometric Pressure and Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_ICP201XX_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX_TRIGGER_MODE)、[`CONFIG_ICP201XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICP201XX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ICP201XX_TRIGGER`。

<a id="CONFIG_IIS2DH"></a>

## 154.91 `CONFIG_IIS2DH`

**提示（Prompt）**：IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**说明（Help）**

启用 IIS2DH 加速度传感器（Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_IIS2DH_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_IIS2DH
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_IIS2DH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_IIS2DH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_IIS2DH`。

<a id="CONFIG_IIS2DH_ODR"></a>

## 154.92 `CONFIG_IIS2DH_ODR`

**提示（Prompt）**：加速度计采样频率（输出数据速率，ODR）

**说明（Help）**

指定默认加速度计输出数据速率（ODR），以每秒采样数（Hz）表示。

- 0：在运行时选择 ODR。
- 1：1 Hz。
- 2：10 Hz。
- 3：25 Hz。
- 4：50 Hz。
- 5：100 Hz。
- 6：200 Hz。
- 7：400 Hz。
- 8：1620 Hz，仅适用于低功耗模式（LP）。
- 9：取决于模式；低功耗模式（LP）为 5376 Hz，正常模式（NORM）或高分辨率模式（HR）为 1344 Hz。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 9]
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DH`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2DH_POWER_MODE"></a>

## 154.93 `CONFIG_IIS2DH_POWER_MODE`

**提示（Prompt）**：传感器功耗模式（Sensor Power Modes）

**说明（Help）**

指定传感器功耗模式（Power Mode）：

- 0：高分辨率模式（High Resolution Mode）。
- 1：正常模式（Normal Mode）。
- 2：低功耗模式（Low Power Mode）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DH`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2DH_RANGE"></a>

## 154.94 `CONFIG_IIS2DH_RANGE`

**提示（Prompt）**：加速度计满量程范围（Full-scale Range）设置

**说明（Help）**

指定默认加速度计满量程范围（Full-scale Range）。有效值为：

- 0：在运行时选择满量程。
- 2：±2 g。
- 4：±4 g。
- 8：±8 g。
- 16：±16 g。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DH`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2DH_THREAD_PRIORITY"></a>

## 154.95 `CONFIG_IIS2DH_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DH_TRIGGER_OWN_THREAD && CONFIG_IIS2DH_TRIGGER && CONFIG_IIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DH_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH_TRIGGER_OWN_THREAD)、[`CONFIG_IIS2DH_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DH_TRIGGER)、[`CONFIG_IIS2DH`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DH_TRIGGER`。

<a id="CONFIG_IIS2DH_THREAD_STACK_SIZE"></a>

## 154.96 `CONFIG_IIS2DH_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DH_TRIGGER_OWN_THREAD && CONFIG_IIS2DH_TRIGGER && CONFIG_IIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DH_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH_TRIGGER_OWN_THREAD)、[`CONFIG_IIS2DH_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DH_TRIGGER)、[`CONFIG_IIS2DH`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DH_TRIGGER`。

<a id="CONFIG_IIS2DH_TRIGGER_GLOBAL_THREAD"></a>

## 154.97 `CONFIG_IIS2DH_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS2DH_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2DH_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DH_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DH_TRIGGER`。

<a id="CONFIG_IIS2DH_TRIGGER_MODE"></a>

## 154.98 `CONFIG_IIS2DH_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DH && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_IIS2DH_TRIGGER_NONE
CONFIG_IIS2DH_TRIGGER_GLOBAL_THREAD
CONFIG_IIS2DH_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DH`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_IIS2DH_TRIGGER_NONE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH_TRIGGER_NONE)、[`CONFIG_IIS2DH_TRIGGER_GLOBAL_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH_TRIGGER_GLOBAL_THREAD)、[`CONFIG_IIS2DH_TRIGGER_OWN_THREAD`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH_TRIGGER_OWN_THREAD)。

<a id="CONFIG_IIS2DH_TRIGGER_NONE"></a>

## 154.99 `CONFIG_IIS2DH_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IIS2DH_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2DH_TRIGGER_MODE`](P154_drivers_sensor_配置项参考_6.md#CONFIG_IIS2DH_TRIGGER_MODE)。

<a id="CONFIG_IIS2DH_TRIGGER_OWN_THREAD"></a>

## 154.100 `CONFIG_IIS2DH_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS2DH_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dh/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dh/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DH I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2DH_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DH_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DH_TRIGGER`。

<!-- kconfig-navigation -->

[上一章](P153_drivers_sensor_配置项参考_5.md) · [返回大纲](大纲.md) · [下一章](P155_drivers_sensor_配置项参考_7.md)
