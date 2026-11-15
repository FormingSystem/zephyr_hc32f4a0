---
id: learning.zephyr-docs.kconfig-reference.page-147
title: "`drivers/rtc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第147章\_`drivers/rtc`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/rtc` 的 70 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_RTC"></a>

## 147.1 `CONFIG_RTC`

**提示（Prompt）**：实时时钟（Real-Time Clock，RTC）驱动

**说明（Help）**

启用 RTC 驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/rtc/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_RTC_ALARM"></a>

## 147.2 `CONFIG_RTC_ALARM`

**提示（Prompt）**：RTC 驱动闹钟（Alarm）支持

**说明（Help）**

此选项启用 RTC 闹钟的驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_AM1805"></a>

## 147.3 `CONFIG_RTC_AM1805`

**提示（Prompt）**：AMBIQ AM1805 RTC 驱动

**说明（Help）**

启用 AMBIQ AM1805 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_AM1805_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.am1805:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.am1805#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_AM1805_THREAD_PRIO"></a>

## 147.4 `CONFIG_RTC_AM1805_THREAD_PRIO`

**提示（Prompt）**：AM1805 中断线程优先级

**说明（Help）**

处理中断并分发回调（Callback）的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC_AM1805 && CONFIG_RTC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.am1805:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.am1805#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → AMBIQ AM1805 RTC 驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC_AM1805`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_AM1805)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_AM1805_THREAD_STACK_SIZE"></a>

## 147.5 `CONFIG_RTC_AM1805_THREAD_STACK_SIZE`

**提示（Prompt）**：AM1805 中断线程栈大小

**说明（Help）**

处理中断并分发回调（Callback）的线程所用栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC_AM1805 && CONFIG_RTC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.am1805:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.am1805#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → AMBIQ AM1805 RTC 驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC_AM1805`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_AM1805)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_AMBIQ"></a>

## 147.6 `CONFIG_RTC_AMBIQ`

**提示（Prompt）**：AMBIQ RTC 驱动

**说明（Help）**

启用 AMBIQ RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.ambiq:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.ambiq#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)。

<a id="CONFIG_RTC_AMEBA"></a>

## 147.7 `CONFIG_RTC_AMEBA`

**提示（Prompt）**：AMEBA RTC 驱动

**说明（Help）**

构建 AMEBA SoC 的实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.ameba:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.ameba#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_ATMEL_SAM"></a>

## 147.8 `CONFIG_RTC_ATMEL_SAM`

**提示（Prompt）**：Atmel SAM RTC 驱动

**说明（Help）**

用于 SAM SoC 系列的 Atmel 实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.sam:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.sam#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_ATMEL_SAM0"></a>

## 147.9 `CONFIG_RTC_ATMEL_SAM0`

**提示（Prompt）**：Atmel SAM RTC 驱动

**说明（Help）**

用于 SAM0 SoC 系列的 Atmel 实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_RTC_ENABLED && !n && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.sam0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.sam0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_BQ32002"></a>

## 147.10 `CONFIG_RTC_BQ32002`

**提示（Prompt）**：Texas Instruments BQ32002 实时时钟驱动

**说明（Help）**

启用 Texas Instruments BQ32002 I²C RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_BQ32002_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.bq32002:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.bq32002#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_CALIBRATION"></a>

## 147.11 `CONFIG_RTC_CALIBRATION`

**提示（Prompt）**：RTC 驱动时钟校准（Clock Calibration）支持

**说明（Help）**

此选项启用 RTC 时钟校准的驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_COUNTER"></a>

## 147.12 `CONFIG_RTC_COUNTER`

**提示（Prompt）**：使用计数器 API（Counter API）的实时时钟驱动

**说明（Help）**

适用于没有分解时间（Broken-down Time）寄存器的 RTC 设备。通过封装计数器 API 提供 RTC 功能，使用 Unix 时间戳在分解时间和计数器滴答（Ticks）之间转换。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_RTC_COUNTER_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER
CONFIG_COUNTER_CALIBRATION if CONFIG_RTC_CALIBRATION
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.counter:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.counter#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_COUNTER_CALIBRATION`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_CALIBRATION)、[`CONFIG_RTC_CALIBRATION`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_CALIBRATION)。

<a id="CONFIG_RTC_COUNTER_INIT_PRIORITY"></a>

## 147.13 `CONFIG_RTC_COUNTER_INIT_PRIORITY`

**提示（Prompt）**：rtc_counter 初始化优先级

**说明（Help）**

以计数器为后端的 RTC 驱动初始化优先级。通常应设置为使封装层在底层计数器设备之后初始化；驱动还会在初始化时通过 `device_is_ready()` 检查计数器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC_COUNTER && CONFIG_RTC
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.counter:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.counter#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 使用计数器 API（Counter API）的实时时钟驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC_COUNTER`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_COUNTER)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_COUNTER_NVMEM"></a>

## 147.14 `CONFIG_RTC_COUNTER_NVMEM`

**提示（Prompt）**：NVMEM 中的纪元偏移（Epoch Offset）

**说明（Help）**

调用 `rtc_set_time` 时，将纪元偏移写入非易失性存储单元（NVMEM Cell），并在初始化时读取。只有具有名为 `epoch-offset` 的 NVMEM 单元的兼容节点才保存数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NVMEM
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.counter:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.counter#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)。

<a id="CONFIG_RTC_DS1302"></a>

## 147.15 `CONFIG_RTC_DS1302`

**提示（Prompt）**：MAXIM DS1302 RTC 驱动

**说明（Help）**

启用 MAXIM DS1302 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_DS1302_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.ds1302:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.ds1302#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_RTC_DS1307"></a>

## 147.16 `CONFIG_RTC_DS1307`

**提示（Prompt）**：MAXIM DS1307 RTC 驱动

**说明（Help）**

启用 MAXIM DS1307 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_DS1307_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.ds1307:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.ds1307#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_DS1337"></a>

## 147.17 `CONFIG_RTC_DS1337`

**提示（Prompt）**：Maxim DS1337 RTC 驱动

**说明（Help）**

启用 Maxim DS1337 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_DS1337_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.ds1337:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.ds1337#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_DS3231"></a>

## 147.18 `CONFIG_RTC_DS3231`

**提示（Prompt）**：Maxim DS3231 RTC／温度补偿晶体振荡器（TCXO）

**说明（Help）**

启用基于 Maxim DS3231 I²C 设备的 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_DS3231_MFD_ENABLED && DT_HAS_MAXIM_DS3231_RTC_ENABLED && CONFIG_RTC
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

**定义位置（Location）**：[`drivers/rtc/Kconfig.ds3231:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.ds3231#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_RTC_DS3231_INIT_PRIORITY"></a>

## 147.19 `CONFIG_RTC_DS3231_INIT_PRIORITY`

**提示（Prompt）**：DS3231 RTC 驱动初始化优先级

**说明（Help）**

DS3231 RTC 驱动的初始化优先级，必须大于 I²C 控制器和 MFD 驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC_DS3231 && CONFIG_RTC
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.ds3231:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.ds3231#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → Maxim DS3231 RTC／温度补偿晶体振荡器（TCXO）

**配置项引用（Symbol References）**：[`CONFIG_RTC_DS3231`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_DS3231)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_EMUL"></a>

## 147.20 `CONFIG_RTC_EMUL`

**提示（Prompt）**：仿真 RTC 驱动（Emulated RTC Driver）

**说明（Help）**

启用仿真实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_RTC_EMUL_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_EMUL_INIT_DATETIME"></a>

## 147.21 `CONFIG_RTC_EMUL_INIT_DATETIME`

**提示（Prompt）**：使用主机墙上时钟（Wall-clock）初始化仿真 RTC 时间

**说明（Help）**

以主机当前墙上时钟时间设置仿真 RTC 的初始时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && CONFIG_RTC_EMUL && CONFIG_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.emul:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.emul#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 仿真 RTC 驱动（Emulated RTC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_RTC_EMUL`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_EMUL)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_FAKE"></a>

## 147.22 `CONFIG_RTC_FAKE`

**提示（Prompt）**：模拟 RTC 驱动程序。

**说明（Help）**

启用基于伪函数框架（FFF）的模拟 RTC 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FAKE_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.fake:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.fake#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_INFINEON_CAT1"></a>

## 147.23 `CONFIG_RTC_INFINEON_CAT1`

**提示（Prompt）**：Infineon CAT1 RTC 驱动

**说明（Help）**

此选项启用 Infineon CAT1 系列的 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.infineon:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.infineon#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_USE_INFINEON_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_RTC)。

<a id="CONFIG_RTC_INIT_PRIORITY"></a>

## 147.24 `CONFIG_RTC_INIT_PRIORITY`

**提示（Prompt）**：RTC 初始化优先级

**说明（Help）**

RTC 设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/rtc/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_RTC_ITE_IT8XXX2"></a>

## 147.25 `CONFIG_RTC_ITE_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 RTC 驱动

**说明（Help）**

此选项启用 IT8XXX2 的 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_MAX31331"></a>

## 147.26 `CONFIG_RTC_MAX31331`

**提示（Prompt）**：MAX31331 超低功耗（Ultra Low-power）RTC

**说明（Help）**

启用 Analog Devices MAX31331 RTC 多功能设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX31331_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.max31331:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.max31331#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_MAX31331_INTERRUPT"></a>

## 147.27 `CONFIG_RTC_MAX31331_INTERRUPT`

**提示（Prompt）**：中断支持（Interrupt Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.max31331:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.max31331#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_MAX31331_INTERRUPT_GLOBAL_THREAD"></a>

## 147.28 `CONFIG_RTC_MAX31331_INTERRUPT_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**

使用全局线程（Global Thread）处理中断

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_RTC_MAX31331_INTERRUPT
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.max31331:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.max31331#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 设置中断处理选项（Interrupt Handling）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_RTC_MAX31331_INTERRUPT`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_MAX31331_INTERRUPT)。

<a id="CONFIG_RTC_MAX31331_INTERRUPT_MODE"></a>

## 147.29 `CONFIG_RTC_MAX31331_INTERRUPT_MODE`

**提示（Prompt）**：设置中断处理选项（Interrupt Handling）

**说明（Help）**

选择 MAX31331 RTC 驱动实现中断处理的方式，可根据应用需求选择不同的中断处理机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX31331_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
CONFIG_RTC_MAX31331_INTERRUPT_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_RTC_MAX31331_INTERRUPT_GLOBAL_THREAD
CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.max31331:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.max31331#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_RTC_MAX31331_INTERRUPT_GLOBAL_THREAD`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_MAX31331_INTERRUPT_GLOBAL_THREAD)、[`CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD)。

<a id="CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD"></a>

## 147.30 `CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**

使用专用线程（Own Thread）处理中断

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_RTC_MAX31331_INTERRUPT
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.max31331:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.max31331#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → 设置中断处理选项（Interrupt Handling）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_RTC_MAX31331_INTERRUPT`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_MAX31331_INTERRUPT)。

<a id="CONFIG_RTC_MAX31331_THREAD_PRIORITY"></a>

## 147.31 `CONFIG_RTC_MAX31331_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

选择“使用专用线程”（Use Own Thread）时，设置处理中断的线程优先级。数值越小，优先级越高。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD && CONFIG_RTC
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.max31331:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.max31331#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_MAX31331_THREAD_STACK_SIZE"></a>

## 147.32 `CONFIG_RTC_MAX31331_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小（Thread Stack Size）

**说明（Help）**

选择“使用专用线程”（Use Own Thread）时，指定处理中断所用线程的栈大小，单位为字节。应确保栈足以容纳中断处理逻辑，避免栈溢出（Stack Overflow）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD && CONFIG_RTC
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.max31331:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.max31331#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_MAX31331_INTERRUPT_OWN_THREAD)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_MAX31331_TIMESTAMPING"></a>

## 147.33 `CONFIG_RTC_MAX31331_TIMESTAMPING`

**提示（Prompt）**：时间戳（Timestamping）支持，TS0～TS3

**说明（Help）**

启用通过 TS0～TS3 寄存器实现的时间戳功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX31331_ENABLED && CONFIG_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.max31331:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.max31331#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_MCHP_G1"></a>

## 147.34 `CONFIG_RTC_MCHP_G1`

**提示（Prompt）**：Microchip RTC G1 驱动

**说明（Help）**

启用 Microchip G1 的 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_RTC_G1_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_MCHP_G2"></a>

## 147.35 `CONFIG_RTC_MCHP_G2`

**提示（Prompt）**：Microchip RTC G2 驱动

**说明（Help）**

用于 SAM SoC 系列的 Microchip 实时时钟（RTC）G2 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_RTC_G2_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYSCON
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.mchp:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.mchp#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)。

<a id="CONFIG_RTC_MCHP_MSS"></a>

## 147.36 `CONFIG_RTC_MCHP_MSS`

**提示（Prompt）**：Microchip RTC MSS 驱动

**说明（Help）**

启用 Microchip MSS 的 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_RTC_MSS_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.mchp:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.mchp#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_MCHP_SUPPORTS_DUAL_ALARM"></a>

## 147.37 `CONFIG_RTC_MCHP_SUPPORTS_DUAL_ALARM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RTC 支持两个闹钟（Alarm）；PIC32CM JH 仅支持一个。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC_MCHP_G1 && !CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.mchp:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.mchp#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC_MCHP_G1`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_MCHP_G1)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`。

<a id="CONFIG_RTC_MOTOROLA_MC146818"></a>

## 147.38 `CONFIG_RTC_MOTOROLA_MC146818`

**提示（Prompt）**：x86 CMOS/RTC 时钟的 RTC 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MOTOROLA_MC146818_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y if !CONFIG_COUNTER
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.mc146818:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.mc146818#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_RTC_NUMAKER"></a>

## 147.39 `CONFIG_RTC_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker MCU RTC 驱动

**说明（Help）**

此选项启用 Nuvoton NuMaker 系列处理器的 RTC 驱动。如需启用 NuMaker RTC，请选 y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_NUMAKER_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_HAS_NUMAKER_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_RTC)。

<a id="CONFIG_RTC_NXP_IRTC"></a>

## 147.40 `CONFIG_RTC_NXP_IRTC`

**提示（Prompt）**：NXP 独立实时时钟（Independent Real Time Clock）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IRTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.nxp_irtc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.nxp_irtc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_NXP_RTC_ANALOG"></a>

## 147.41 `CONFIG_RTC_NXP_RTC_ANALOG`

**提示（Prompt）**：NXP RTC Analog 驱动

**说明（Help）**

启用 NXP RTC Analog 驱动。此 RTC 模块支持三个独立闹钟、二进制编码十进制（BCD）时间／日期模式，以及百分之一秒分辨率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_RTC_ANALOG_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.nxp_rtc_analog:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.nxp_rtc_analog#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_PCF2123"></a>

## 147.42 `CONFIG_RTC_PCF2123`

**提示（Prompt）**：NXP PCF2123 实时时钟驱动

**说明（Help）**

启用 NXP PCF2123 SPI RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCF2123_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.pcf2123:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.pcf2123#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_RTC_PCF85063A"></a>

## 147.43 `CONFIG_RTC_PCF85063A`

**提示（Prompt）**：NXP PCF85063A 实时时钟驱动

**说明（Help）**

启用 NXP PCF85063A I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCF85063A_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.pcf85063a:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.pcf85063a#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_PCF8523"></a>

## 147.44 `CONFIG_RTC_PCF8523`

**提示（Prompt）**：NXP PCF8523 RTC 驱动

**说明（Help）**

启用 NXP PCF8523 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCF8523_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.pcf8523:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.pcf8523#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_PCF8523_OFFSET_MODE"></a>

## 147.45 `CONFIG_RTC_PCF8523_OFFSET_MODE`

**提示（Prompt）**：偏移模式（Offset Mode）

**说明（Help）**

偏移寄存器模式选择（Offset Register Mode Selection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC_CALIBRATION && CONFIG_RTC_PCF8523 && CONFIG_RTC
```

**默认值（Defaults）**

```text
CONFIG_RTC_PCF8523_OFFSET_MODE_SLOW
```

**可选项（Choices）**

```text
CONFIG_RTC_PCF8523_OFFSET_MODE_SLOW
CONFIG_RTC_PCF8523_OFFSET_MODE_FAST
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.pcf8523:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.pcf8523#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → NXP PCF8523 RTC 驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC_CALIBRATION`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_CALIBRATION)、[`CONFIG_RTC_PCF8523`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_PCF8523)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_RTC_PCF8523_OFFSET_MODE_SLOW`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_PCF8523_OFFSET_MODE_SLOW)、[`CONFIG_RTC_PCF8523_OFFSET_MODE_FAST`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_PCF8523_OFFSET_MODE_FAST)。

<a id="CONFIG_RTC_PCF8523_OFFSET_MODE_FAST"></a>

## 147.46 `CONFIG_RTC_PCF8523_OFFSET_MODE_FAST`

**提示（Prompt）**：快速模式（Fast）

**说明（Help）**

每分钟进行一次偏移校正（Offset Correction），然后每秒施加一次校正脉冲，最多 60 个脉冲。校正值超过 60 个脉冲时，在第 59 秒施加额外校正脉冲（`MODE = 1`）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTC_PCF8523_OFFSET_MODE>
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.pcf8523:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.pcf8523#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → NXP PCF8523 RTC 驱动 → 偏移模式（Offset Mode）

**配置项引用（Symbol References）**：[`CONFIG_RTC_PCF8523_OFFSET_MODE`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_PCF8523_OFFSET_MODE)。

<a id="CONFIG_RTC_PCF8523_OFFSET_MODE_SLOW"></a>

## 147.47 `CONFIG_RTC_PCF8523_OFFSET_MODE_SLOW`

**提示（Prompt）**：慢速（Slow）

**说明（Help）**

每两小时进行一次偏移校正，然后每分钟施加一次校正脉冲，直到完成编程指定的校正量（`MODE = 0`）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTC_PCF8523_OFFSET_MODE>
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.pcf8523:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.pcf8523#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → NXP PCF8523 RTC 驱动 → 偏移模式（Offset Mode）

**配置项引用（Symbol References）**：[`CONFIG_RTC_PCF8523_OFFSET_MODE`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_PCF8523_OFFSET_MODE)。

<a id="CONFIG_RTC_PCF8523_THREAD_PRIO"></a>

## 147.48 `CONFIG_RTC_PCF8523_THREAD_PRIO`

**提示（Prompt）**：PCF8523 中断线程优先级

**说明（Help）**

处理中断并分发回调（Callback）的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_RTC_ALARM || CONFIG_RTC_UPDATE) && CONFIG_RTC_PCF8523 && CONFIG_RTC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.pcf8523:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.pcf8523#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → NXP PCF8523 RTC 驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC_ALARM`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_ALARM)、[`CONFIG_RTC_UPDATE`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_UPDATE)、[`CONFIG_RTC_PCF8523`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_PCF8523)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_PCF8523_THREAD_STACK_SIZE"></a>

## 147.49 `CONFIG_RTC_PCF8523_THREAD_STACK_SIZE`

**提示（Prompt）**：PCF8523 中断线程栈大小

**说明（Help）**

处理中断并分发回调（Callback）的线程所用栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_RTC_ALARM || CONFIG_RTC_UPDATE) && CONFIG_RTC_PCF8523 && CONFIG_RTC
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.pcf8523:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.pcf8523#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → NXP PCF8523 RTC 驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC_ALARM`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_ALARM)、[`CONFIG_RTC_UPDATE`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_UPDATE)、[`CONFIG_RTC_PCF8523`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_PCF8523)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_PCF8563"></a>

## 147.50 `CONFIG_RTC_PCF8563`

**提示（Prompt）**：NXP PCF8563 RTC 驱动

**说明（Help）**

启用 NXP PCF8563 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCF8563_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.pcf8563:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.pcf8563#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_RENESAS_RA"></a>

## 147.51 `CONFIG_RTC_RENESAS_RA`

**提示（Prompt）**：Renesas RA RTC

**说明（Help）**

启用 Renesas RA RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_USE_RA_FSP_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_RTC)。

<a id="CONFIG_RTC_RENESAS_RA_ALWAYS_SET_CLOCK_SOURCE"></a>

## 147.52 `CONFIG_RTC_RENESAS_RA_ALWAYS_SET_CLOCK_SOURCE`

**提示（Prompt）**：初始化期间强制设置 RTC 时钟源（Clock Source）

**说明（Help）**

无论复位类型如何，初始化期间始终配置 RTC 时钟源。此项仅用于暖启动（Warm-start）检测不可靠时的测试。生产环境中不要使用，因为它可能不必要地重新初始化 RTC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC_RENESAS_RA && CONFIG_RTC
```

**默认值（Defaults）**

```text
y if CONFIG_TEST
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.renesas_ra:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.renesas_ra#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动 → Renesas RA RTC

**配置项引用（Symbol References）**：[`CONFIG_RTC_RENESAS_RA`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_RENESAS_RA)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST)。

<a id="CONFIG_RTC_RPI_PICO"></a>

## 147.53 `CONFIG_RTC_RPI_PICO`

**提示（Prompt）**：Raspberry Pi Pico RTC 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_RTC_ENABLED && CONFIG_RESET && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_PICOSDK_USE_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_RTC)。

<a id="CONFIG_RTC_RTS5912"></a>

## 147.54 `CONFIG_RTC_RTS5912`

**提示（Prompt）**：Realtek RTS5912 RTC 驱动

**说明（Help）**

启用 Realtek RTC 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL && DT_HAS_REALTEK_RTS5912_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.rts5912:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.rts5912#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_RV3028"></a>

## 147.55 `CONFIG_RTC_RV3028`

**提示（Prompt）**：Micro Crystal RV3028 I²C 极低功耗（Extreme Low Power）RTC 驱动

**说明（Help）**

启用 Micro Crystal RV3028 I²C RTC 驱动。根据启用的 RTC API 选项，通过 RTC API 提供时间、闹钟、更新事件和校准支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV3028_RTC_ENABLED && DT_HAS_MICROCRYSTAL_RV3028_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.rv3028:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.rv3028#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_RTC_RV3032"></a>

## 147.56 `CONFIG_RTC_RV3032`

**提示（Prompt）**：Micro Crystal RV3032 实时时钟模块

**说明（Help）**

启用 Micro Crystal RV3032 I²C RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV3032_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD_RV3032
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.rv3032:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.rv3032#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_MFD_RV3032`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_RV3032)。

<a id="CONFIG_RTC_RV8263"></a>

## 147.57 `CONFIG_RTC_RV8263`

**提示（Prompt）**：Micro Crystal RV-8263-C8 RTC 驱动

**说明（Help）**

Micro Crystal RV-8263-C8 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV_8263_C8_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.rv8263:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.rv8263#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_RV8803"></a>

## 147.58 `CONFIG_RTC_RV8803`

**提示（Prompt）**：Micro Crystal RV8803 极低功耗实时时钟模块驱动

**说明（Help）**

启用 Micro Crystal RV8803 I²C RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV8803_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.rv8803:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.rv8803#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_RX8130CE"></a>

## 147.59 `CONFIG_RTC_RX8130CE`

**提示（Prompt）**：EPSON RX8130CE RTC 驱动

**说明（Help）**

启用 Epson RX8130CE RTC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_EPSON_RX8130CE_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.rx8130ce:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.rx8130ce#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_RTC_SF32LB"></a>

## 147.60 `CONFIG_RTC_SF32LB`

**提示（Prompt）**：SF32LB MCU 系列 RTC 驱动

**说明（Help）**

启用 SF32LB MCU 系列的 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_SHELL"></a>

## 147.61 `CONFIG_RTC_SHELL`

**提示（Prompt）**：RTC Shell 命令

**说明（Help）**

RTC Shell 命令

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_SILABS_SIWX91X"></a>

## 147.62 `CONFIG_RTC_SILABS_SIWX91X`

**提示（Prompt）**：Silabs SiWx91x RTC 驱动

**说明（Help）**

构建 Silabs SiWx91x SoC 的 RTC 驱动，对应参考手册所述日历（Calendar）硬件模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_RTC_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_SMARTBOND"></a>

## 147.63 `CONFIG_RTC_SMARTBOND`

**提示（Prompt）**：SmartBond RTC 驱动

**说明（Help）**

构建 SmartBond SoC 的 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.smartbond:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.smartbond#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_STM32"></a>

## 147.64 `CONFIG_RTC_STM32`

**提示（Prompt）**：STM32 RTC 驱动

**说明（Help）**

构建 STM32 SoC 的 RTC 驱动，不包括 STM32F1 系列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_RTC_ENABLED && !CONFIG_SOC_SERIES_STM32F1X && CONFIG_RTC
```

**默认值（Defaults）**

```text
y if !CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F1X`。

<a id="CONFIG_RTC_TI_MSPM0"></a>

## 147.65 `CONFIG_RTC_TI_MSPM0`

**提示（Prompt）**：Texas Instruments MSPM0 RTC 驱动

**说明（Help）**

用于 MSPM0 SoC 系列的 Texas Instruments 实时时钟（RTC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.ti_mspm0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.ti_mspm0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_UPDATE"></a>

## 147.66 `CONFIG_RTC_UPDATE`

**提示（Prompt）**：RTC 驱动更新事件回调（Update Event Callback）支持

**说明（Help）**

此选项启用 RTC 更新事件回调的驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTC
```

**定义位置（Location）**：[`drivers/rtc/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_XEC"></a>

## 147.67 `CONFIG_RTC_XEC`

**提示（Prompt）**：Microchip XEC RTC

**说明（Help）**

启用在 Microchip XEC IP 模块上使用 RTC 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.mchp_xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.mchp_xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_XEC_DATA_MODE_BCD"></a>

## 147.68 `CONFIG_RTC_XEC_DATA_MODE_BCD`

**提示（Prompt）**：选择数据模式（Data Mode）

**说明（Help）**

选择时间的二进制或二进制编码十进制（BCD）表示。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.mchp_xec:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.mchp_xec#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_XEC_HOUR_FORMAT_24"></a>

## 147.69 `CONFIG_RTC_XEC_HOUR_FORMAT_24`

**提示（Prompt）**：选择小时格式（Hour Format）

**说明（Help）**

选择时间的 24 小时制／12 小时制表示。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.mchp_xec:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.mchp_xec#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<a id="CONFIG_RTC_XMC4XXX"></a>

## 147.70 `CONFIG_RTC_XMC4XXX`

**提示（Prompt）**：XMC4XXX RTC 驱动

**说明（Help）**

构建 XMC4XXX SoC 的 RTC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_RTC_ENABLED && CONFIG_RTC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/rtc/Kconfig.xmc4xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/Kconfig.xmc4xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 实时时钟（Real-Time Clock，RTC）驱动

**配置项引用（Symbol References）**：[`CONFIG_RTC`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC)。

<!-- kconfig-navigation -->

[上一章](P146_drivers_retained_mem_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P148_drivers_sdhc_配置项参考.md)
