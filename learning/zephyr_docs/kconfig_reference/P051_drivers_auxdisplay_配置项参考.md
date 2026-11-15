---
id: learning.zephyr-docs.kconfig-reference.page-51
title: "`drivers/auxdisplay`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第51章\_`drivers/auxdisplay`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/auxdisplay` 的 10 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AUXDISPLAY"></a>

## 51.1 `CONFIG_AUXDISPLAY`

**提示（Prompt）**：辅助文字显示驱动（Auxiliary Textual Display Drivers）

**说明（Help）**

启用辅助／文字显示驱动（Auxiliary / Textual Display Drivers），例如字母数字显示器（Alphanumerical Display）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_AUXDISPLAY_GPIO_7SEG"></a>

## 51.2 `CONFIG_AUXDISPLAY_GPIO_7SEG`

**提示（Prompt）**：通用 GPIO 驱动的七段数码管（7-Segment Display）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_7_SEGMENT_ENABLED && CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig.gpio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig.gpio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_AUXDISPLAY_HD44780"></a>

## 51.3 `CONFIG_AUXDISPLAY_HD44780`

**提示（Prompt）**：日立 HD44780 液晶显示驱动（Hitachi LCD Driver）

**说明（Help）**

启用日立（Hitachi）HD44780 及兼容液晶显示器（LCD）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HIT_HD44780_ENABLED && CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig.hd44780:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig.hd44780#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_AUXDISPLAY_INIT_PRIORITY"></a>

## 51.4 `CONFIG_AUXDISPLAY_INIT_PRIORITY`

**提示（Prompt）**：辅助显示设备初始化优先级（Auxiliary Display Init Priority）

**说明（Help）**

辅助文字显示设备（Auxiliary Textual Display Device）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)。

<a id="CONFIG_AUXDISPLAY_ITRON"></a>

## 51.5 `CONFIG_AUXDISPLAY_ITRON`

**提示（Prompt）**：Noritake Itron 真空荧光显示驱动（VFD Driver）

**说明（Help）**

启用 Noritake Itron 真空荧光显示器（VFD）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORITAKE_ITRON_ENABLED && CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig.itron:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig.itron#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)。

<a id="CONFIG_AUXDISPLAY_JHD1313"></a>

## 51.6 `CONFIG_AUXDISPLAY_JHD1313`

**提示（Prompt）**：精华显示 JHD1313 驱动（Jinghua Display Driver）

**说明（Help）**

启用精华显示（Jinghua Display）JHD1313 显示器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_JHD_JHD1313_ENABLED && CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig.jhd1313:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig.jhd1313#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUXDISPLAY_NXP_SLCD"></a>

## 51.7 `CONFIG_AUXDISPLAY_NXP_SLCD`

**提示（Prompt）**：恩智浦 MCUX SLCD 显示驱动（NXP Display Driver）

**说明（Help）**

启用恩智浦（NXP）MCUX 段式液晶显示器（Segmented LCD，SLCD）的辅助显示（auxdisplay）驱动。为 NXP MCX SLCD 硬件提供标准 auxdisplay API，在同一个驱动中统一处理硬件初始化和显示面板层（Display Panel Layer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SLCD_ENABLED && CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SHIELD_OD_6010
```

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig.nxp_slcd:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig.nxp_slcd#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)、[`CONFIG_SHIELD_OD_6010`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_OD_6010)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_OD_6010`。

<a id="CONFIG_AUXDISPLAY_PT6314"></a>

## 51.8 `CONFIG_AUXDISPLAY_PT6314`

**提示（Prompt）**：普诚 PT6314 点阵字符 VFD 驱动（PTC Dot Character VFD Driver）

**说明（Help）**

启用普诚（PTC）PT6314 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PTC_PT6314_ENABLED && CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig.pt6314:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig.pt6314#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_AUXDISPLAY_SERLCD"></a>

## 51.9 `CONFIG_AUXDISPLAY_SERLCD`

**提示（Prompt）**：SparkFun SerLCD 点阵字符液晶驱动（Dot Character LCD Driver）

**说明（Help）**

启用 SparkFun SerLCD 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SPARKFUN_SERLCD_ENABLED && CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig.serlcd:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig.serlcd#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUXDISPLAY_TM1637"></a>

## 51.10 `CONFIG_AUXDISPLAY_TM1637`

**提示（Prompt）**：天微 TM1637 七段显示支持（Titan Micro 7-Segment Display Support）

**说明（Help）**

启用天微（TM，Shenzhen Titan Micro Elec）TM1637 七段 LED 显示器驱动。该驱动支持时钟模块和简单数字显示器中常见的四位七段数码管（4-Digit 7-Segment Display）。TM1637 使用 `CLK` 和 `DIO` 两线串行接口（Two-Wire Serial Interface），最多控制 4 位数字，并支持亮度控制（Brightness Control）。此驱动实现辅助显示（auxdisplay）API，可用于通用显示场景；同时提供直接显示数字的辅助 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TITANMEC_TM1637_ENABLED && CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/auxdisplay/Kconfig.tm1637:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/auxdisplay/Kconfig.tm1637#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<!-- kconfig-navigation -->

[上一章](P050_drivers_audio_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P052_drivers_bbram_配置项参考.md)
