---
id: learning.zephyr-docs.kconfig-reference.page-127
title: "`drivers/modem`配置项参考（3/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第127章\_`drivers/modem`配置项参考（3/4）

本章翻译官方 Kconfig 数据库中 `drivers/modem` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MODEM_HL78XX_BAND_3"></a>

## 127.1 `CONFIG_MODEM_HL78XX_BAND_3`

**提示（Prompt）**：频段 3：1800 MHz

**说明（Help）**

启用频段 3：1800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:881`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L881)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_31"></a>

## 127.2 `CONFIG_MODEM_HL78XX_BAND_31`

**提示（Prompt）**：频段（Band）31：450 MHz

**说明（Help）**

启用频段 31：450 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:979`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L979)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_4"></a>

## 127.3 `CONFIG_MODEM_HL78XX_BAND_4`

**提示（Prompt）**：频段 4：1700 MHz

**说明（Help）**

启用频段 4：1700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:887`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L887)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_5"></a>

## 127.4 `CONFIG_MODEM_HL78XX_BAND_5`

**提示（Prompt）**：频段 5：850 MHz

**说明（Help）**

启用频段 5：850 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:893`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L893)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_66"></a>

## 127.5 `CONFIG_MODEM_HL78XX_BAND_66`

**提示（Prompt）**：频段 66：1800 MHz

**说明（Help）**

启用频段 66：1800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:984`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L984)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_72"></a>

## 127.6 `CONFIG_MODEM_HL78XX_BAND_72`

**提示（Prompt）**：频段 72：450 MHz

**说明（Help）**

启用频段 72：450 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:989`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L989)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_73"></a>

## 127.7 `CONFIG_MODEM_HL78XX_BAND_73`

**提示（Prompt）**：频段 73：450 MHz

**说明（Help）**

启用频段 73：450 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:994`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L994)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_8"></a>

## 127.8 `CONFIG_MODEM_HL78XX_BAND_8`

**提示（Prompt）**：频段 8：900 MHz

**说明（Help）**

启用频段 8：900 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:899`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L899)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_85"></a>

## 127.9 `CONFIG_MODEM_HL78XX_BAND_85`

**提示（Prompt）**：频段 85：700 MHz

**说明（Help）**

启用频段 85：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:999`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L999)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_87"></a>

## 127.10 `CONFIG_MODEM_HL78XX_BAND_87`

**提示（Prompt）**：频段 87：410 MHz

**说明（Help）**

启用频段 87：410 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1004`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1004)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_88"></a>

## 127.11 `CONFIG_MODEM_HL78XX_BAND_88`

**提示（Prompt）**：频段 88：410 MHz

**说明（Help）**

启用频段 88：410 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1009`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1009)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_9"></a>

## 127.12 `CONFIG_MODEM_HL78XX_BAND_9`

**提示（Prompt）**：频段 9：1900 MHz

**说明（Help）**

启用频段 9：1900 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:905`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L905)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BOOT_IN_AIRPLANE_MODE"></a>

## 127.13 `CONFIG_MODEM_HL78XX_BOOT_IN_AIRPLANE_MODE`

**提示（Prompt）**：飞行模式（Airplane Mode）

**说明（Help）**

- 使用 `AT+CFUN = 4,0`。
- 禁用无线电发送和接收，SIM 保持供电，即飞行模式。
- 设置时还需考虑复位条件，即 CFUN 的第二个参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_BOOT_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:565`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L565)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 调制解调器启动类型（Modem Boot Type）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_BOOT_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_BOOT_MODE)。

<a id="CONFIG_MODEM_HL78XX_BOOT_IN_FULLY_FUNCTIONAL_MODE"></a>

## 127.14 `CONFIG_MODEM_HL78XX_BOOT_IN_FULLY_FUNCTIONAL_MODE`

**提示（Prompt）**：完整功能模式（Full Functional Mode）

**说明（Help）**

- 使用 `AT+CFUN = 1,0`。
- 启用完整功能，开始搜索蜂窝网络。
- 设置时还需考虑复位条件，即 CFUN 的第二个参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_BOOT_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:558`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L558)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 调制解调器启动类型（Modem Boot Type）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_BOOT_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_BOOT_MODE)。

<a id="CONFIG_MODEM_HL78XX_BOOT_IN_MINIMUM_FUNCTIONAL_MODE"></a>

## 127.15 `CONFIG_MODEM_HL78XX_BOOT_IN_MINIMUM_FUNCTIONAL_MODE`

**提示（Prompt）**：最小功能模式（Minimum Functional Mode）

**说明（Help）**

- 使用 `AT+CFUN = 0,0`，启用最小功能并关闭 SIM 电源。
- 还需考虑复位条件，即 CFUN 的第二个参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_BOOT_MODE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:551`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L551)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 调制解调器启动类型（Modem Boot Type）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_BOOT_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_BOOT_MODE)。

<a id="CONFIG_MODEM_HL78XX_BOOT_MODE"></a>

## 127.16 `CONFIG_MODEM_HL78XX_BOOT_MODE`

**提示（Prompt）**：调制解调器启动类型（Modem Boot Type）

**说明（Help）**

设置调制解调器功能，参见 `AT+CFUN`。设置时还需考虑 CFUN 第二个参数所表示的复位条件：

- 0：设置为 `<fun>` 功耗级别之前，不复位移动终端（MT）。
- 1：设置为 `<fun>` 功耗级别之前，先复位移动终端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_BOOT_IN_FULLY_FUNCTIONAL_MODE
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_BOOT_IN_MINIMUM_FUNCTIONAL_MODE
CONFIG_MODEM_HL78XX_BOOT_IN_FULLY_FUNCTIONAL_MODE
CONFIG_MODEM_HL78XX_BOOT_IN_AIRPLANE_MODE
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:542`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L542)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_BOOT_IN_FULLY_FUNCTIONAL_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_BOOT_IN_FULLY_FUNCTIONAL_MODE)、[`CONFIG_MODEM_HL78XX_BOOT_IN_MINIMUM_FUNCTIONAL_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_BOOT_IN_MINIMUM_FUNCTIONAL_MODE)、[`CONFIG_MODEM_HL78XX_BOOT_IN_AIRPLANE_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_BOOT_IN_AIRPLANE_MODE)。

<a id="CONFIG_MODEM_HL78XX_CHAT_BUFFER_SIZES"></a>

## 127.17 `CONFIG_MODEM_HL78XX_CHAT_BUFFER_SIZES`

**提示（Prompt）**：会话脚本（Chat Script）使用的缓冲区大小，单位为字节。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1572`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1572)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_COMMAND_BUFFER_SIZE"></a>

## 127.18 `CONFIG_MODEM_HL78XX_COMMAND_BUFFER_SIZE`

**提示（Prompt）**：AT 命令缓冲区大小，单位为字节。

**说明（Help）**

此设置定义保存与 HL78XX 调制解调器交换的 AT 命令及响应的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1561`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1561)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_CONFIGURE_BANDS"></a>

## 127.19 `CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`

**提示（Prompt）**：配置调制解调器频段（Modem Bands）

**说明（Help）**

选择此设置，以配置 HL78XX 调制解调器在启动时使用哪些 LTE 频段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_AUTORAT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if !CONFIG_MODEM_HL78XX_AUTORAT
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:858`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L858)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTORAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTORAT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_DESIRED_FW_VERSION"></a>

## 127.20 `CONFIG_MODEM_HL78XX_DESIRED_FW_VERSION`

**提示（Prompt）**：期望的固件版本（Desired Firmware Version）

**说明（Help）**

指定期望的 HL78xx 调制解调器固件版本。驱动会检查当前版本；若与期望版本不符，则记录警告。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_DEV_INIT_PRIORITY"></a>

## 127.21 `CONFIG_MODEM_HL78XX_DEV_INIT_PRIORITY`

**提示（Prompt）**：Sierra Wireless HL78XX 设备驱动初始化优先级

**说明（Help）**

Sierra Wireless HL78XX 设备驱动的初始化优先级。除非清楚其影响，否则不要随意更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1631`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1631)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_DEV_POWER_PULSE_DURATION_MS"></a>

## 127.22 `CONFIG_MODEM_HL78XX_DEV_POWER_PULSE_DURATION_MS`

**提示（Prompt）**：上电脉冲持续时间（Power-on Pulse Duration），单位为毫秒

**说明（Help）**

将上电 GPIO 引脚保持高电平指定时长，以触发上电序列（Power-on Sequence）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1596`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1596)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_DEV_RESET_PULSE_DURATION_MS"></a>

## 127.23 `CONFIG_MODEM_HL78XX_DEV_RESET_PULSE_DURATION_MS`

**提示（Prompt）**：电源复位脉冲持续时间（Power-reset Pulse Duration），单位为毫秒

**说明（Help）**

将复位 GPIO 引脚保持高电平指定时长，以触发电源复位序列。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1603`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1603)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_DEV_SHUTDOWN_TIME_MS"></a>

## 127.24 `CONFIG_MODEM_HL78XX_DEV_SHUTDOWN_TIME_MS`

**提示（Prompt）**：认定设备完全关闭之前的等待时间。

**说明（Help）**

系统应等待调制解调器完全关机的时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
120
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1624`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1624)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_DEV_STARTUP_TIME_MS"></a>

## 127.25 `CONFIG_MODEM_HL78XX_DEV_STARTUP_TIME_MS`

**提示（Prompt）**：认定设备就绪之前的等待时间。

**说明（Help）**

预期调制解调器完全上电并可运行所需的延迟时间，单位为毫秒。该延迟发生在驱动打开 UART 管道并附接会话层（Chat Layer）之前。此值必须足够长，让驱动启动代码完成初始化；又必须足够短，确保调制解调器在启动期间发出首批主动结果码（URC）前，管道已经准备好。但如果启用了启动时自动检测波特率，原文建议延长此延迟，让调制解调器完成启动序列。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2000 if CONFIG_MODEM_HL78XX_AUTOBAUD_AT_BOOT
120 if !CONFIG_MODEM_HL78XX_AUTOBAUD_AT_BOOT
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1610`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1610)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_AUTOBAUD_AT_BOOT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTOBAUD_AT_BOOT)。

<a id="CONFIG_MODEM_HL78XX_DISABLE_NETWORK_STATUS_URC_REPORT"></a>

## 127.26 `CONFIG_MODEM_HL78XX_DISABLE_NETWORK_STATUS_URC_REPORT`

**提示（Prompt）**：禁用网络状态主动结果码（URC）报告

**说明（Help）**

禁用网络注册主动结果码（Unsolicited Result Code）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1351)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 网络注册状态报告配置（Network Registration Status Report Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG)。

<a id="CONFIG_MODEM_HL78XX_EDRX"></a>

## 127.27 `CONFIG_MODEM_HL78XX_EDRX`

**提示（Prompt）**：扩展非连续接收（eDRX）

**说明（Help）**

启用 LTE 扩展非连续接收（eDRX）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1154)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes） → 低功耗策略（Low Power Strategy）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION)。

<a id="CONFIG_MODEM_HL78XX_EDRX_IDLE_TIMEOUT"></a>

## 127.28 `CONFIG_MODEM_HL78XX_EDRX_IDLE_TIMEOUT`

**提示（Prompt）**：允许睡眠前的 eDRX 空闲超时，单位为秒

**说明（Help）**

与发送 `+PSMEV` URC 的 PSM 不同，eDRX 不会显式通知调制解调器已经可以睡眠。此超时用作无活动检测：每条 AT 命令都会重置定时器。定时器到期、没有 AT 活动时，将 WAKE 引脚拉低，允许调制解调器进入 eDRX 低功耗睡眠。此值应长于寻呼时间窗口（Paging Time Window，PTW），避免调制解调器仍处于寻呼周期时拉低 WAKE。默认值为 10 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_EDRX && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[2, 120]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1191)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_EDRX`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_EDRX)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_EDRX_VALUE"></a>

## 127.29 `CONFIG_MODEM_HL78XX_EDRX_VALUE`

**提示（Prompt）**：请求的 eDRX 定时器（Requested eDRX Timer）

**说明（Help）**

以 4 位格式表示的半个字节。eDRX 值对应扩展 DRX 参数信息元素第 3 个八位组（Octet）的位 4 至位 1。原文默认值写作“5（81.92）秒”，参见 `Requested_eDRX_value`。译注：保留原文的编码／时长并列表述。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_EDRX && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"0101"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1173)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_EDRX`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_EDRX)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT"></a>

## 127.30 `CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT`

**提示（Prompt）**：网络状态主动结果码（URC）报告

**说明（Help）**

启用网络注册主动结果码：

```text
+CEREG: <stat>
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1356`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1356)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 网络注册状态报告配置（Network Registration Status Report Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG)。

<a id="CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION"></a>

## 127.31 `CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION`

**提示（Prompt）**：包含位置信息的网络状态 URC 报告

**说明（Help）**

启用包含网络注册与位置信息的主动结果：

```text
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>]]
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1361`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1361)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 网络注册状态报告配置（Network Registration Status Report Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG)。

<a id="CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION_AND_CAUSE"></a>

## 127.32 `CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION_AND_CAUSE`

**提示（Prompt）**：包含位置与原因的网络状态 URC 报告

**说明（Help）**

启用包含网络注册、位置信息和 EPS 移动性管理（EMM）原因值的主动结果码：

```text
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,<cause_type>, <reject_cause>]]
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1367)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 网络注册状态报告配置（Network Registration Status Report Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG)。

<a id="CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM"></a>

## 127.33 `CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM`

**提示（Prompt）**：包含省电模式（PSM）信息的网络状态 URC 报告

**说明（Help）**

对于希望采用 PSM 的用户设备（UE），启用包含网络注册与位置信息的主动结果码：

```text
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,,[,[<Active- Time>],[<PeriodicTAU>]]]]
```

译注：占位符中的空格与标点按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1374)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 网络注册状态报告配置（Network Registration Status Report Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG)。

<a id="CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM_AND_CAUSE"></a>

## 127.34 `CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM_AND_CAUSE`

**提示（Prompt）**：包含 PSM 与原因的网络状态 URC 报告

**说明（Help）**

对于希望采用 PSM 的用户设备（UE），启用包含网络注册、位置信息和 EMM 原因值的主动结果码：

```text
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,[<cause_type>],[<reject_-
cause>][,[<Active-Time>] [<Periodic-TAU>]]]]
```

译注：占位符的拼写、换行、空格与标点均按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1381`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1381)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 网络注册状态报告配置（Network Registration Status Report Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG)。

<a id="CONFIG_MODEM_HL78XX_HAS_CTZEU_URC"></a>

## 127.35 `CONFIG_MODEM_HL78XX_HAS_CTZEU_URC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏能力符号（Hidden Capability Symbol）：所选变体支持 `+CTZEU` 主动结果码（URC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if CONFIG_MODEM_HL78XX_12
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_12`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12)。

<a id="CONFIG_MODEM_HL78XX_HAS_KPSMEV_URC"></a>

## 127.36 `CONFIG_MODEM_HL78XX_HAS_KPSMEV_URC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏能力符号：所选变体支持 `+KPSMEV` 主动结果码（URC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if CONFIG_MODEM_HL78XX_12
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_12`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12)。

<a id="CONFIG_MODEM_HL78XX_HAS_KSTATEV_URC"></a>

## 127.37 `CONFIG_MODEM_HL78XX_HAS_KSTATEV_URC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏能力符号：所选变体会发出 `+KSTATEV` 主动结果码（URC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if CONFIG_MODEM_HL78XX_12
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_12`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG"></a>

## 127.38 `CONFIG_MODEM_HL78XX_KNWSCANCFG`

**提示（Prompt）**：配置网络扫描时序（Network Scan Timing）

**说明（Help）**

在调制解调器初始化脚本中发送 `AT+KNWSCANCFG`。禁用此选项，可保留调制解调器默认的网络扫描时序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:583`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L583)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN"></a>

## 127.39 `CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN`

**提示（Prompt）**：配置初始扫描（Initial Scan）

**说明（Help）**

在调制解调器初始化脚本中发送 `AT+KNWSCANCFG=1,...`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:646`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L646)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_MAX"></a>

## 127.40 `CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_MAX`

**提示（Prompt）**：初始扫描最大间隔，单位为秒

**说明（Help）**

两次初始扫描之间的最大间隔，单位为秒。必须保持大于或等于最小间隔。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 65535]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:682`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L682)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置初始扫描（Initial Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_MIN"></a>

## 127.41 `CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_MIN`

**提示（Prompt）**：初始扫描最小间隔，单位为秒

**说明（Help）**

两次初始扫描之间的最小间隔，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 65535]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:675`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L675)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置初始扫描（Initial Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME"></a>

## 127.42 `CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME`

**提示（Prompt）**：初始扫描退避方案（Backoff Scheme）

**说明（Help）**

选择 `AT+KNWSCANCFG=1` 使用的重试间隔方案。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR
CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_EXPONENTIAL
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:654`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L654)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置初始扫描（Initial Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_EXPONENTIAL`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_EXPONENTIAL)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_EXPONENTIAL"></a>

## 127.43 `CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_EXPONENTIAL`

**提示（Prompt）**：指数（Exponential）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:663`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L663)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置初始扫描（Initial Scan） → 初始扫描退避方案（Backoff Scheme）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR"></a>

## 127.44 `CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR`

**提示（Prompt）**：线性（Linear）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:660`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L660)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置初始扫描（Initial Scan） → 初始扫描退避方案（Backoff Scheme）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_VALUE"></a>

## 127.45 `CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_VALUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于 `AT+KNWSCANCFG=1` 的 `<scheme>` 参数的隐藏辅助值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
0 if CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR
1 if CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_EXPONENTIAL
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:668`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L668)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置初始扫描（Initial Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_EXPONENTIAL`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_EXPONENTIAL)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_STEP"></a>

## 127.46 `CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_STEP`

**提示（Prompt）**：初始扫描线性间隔步长，单位为秒

**说明（Help）**

选择线性模式时，相邻扫描之间增加的秒数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR && CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 32767]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:690`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L690)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置初始扫描（Initial Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN_SCHEME_LINEAR)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_INITIAL_SCAN)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC"></a>

## 127.47 `CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC`

**提示（Prompt）**：配置覆盖范围外扫描（Out-of-coverage Scan）

**说明（Help）**

在调制解调器初始化脚本中发送 `AT+KNWSCANCFG=0,...`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:592`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L592)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_MAX"></a>

## 127.48 `CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_MAX`

**提示（Prompt）**：覆盖范围外扫描的最大间隔，单位为秒

**说明（Help）**

两次覆盖范围外扫描之间的最大间隔，单位为秒。必须保持大于或等于最小间隔。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 65535]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:628`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L628)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置覆盖范围外扫描（Out-of-coverage Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_MIN"></a>

## 127.49 `CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_MIN`

**提示（Prompt）**：覆盖范围外扫描的最小间隔，单位为秒

**说明（Help）**

两次覆盖范围外扫描之间的最小间隔，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 65535]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:621`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L621)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置覆盖范围外扫描（Out-of-coverage Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME"></a>

## 127.50 `CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME`

**提示（Prompt）**：覆盖范围外扫描退避方案（Backoff Scheme）

**说明（Help）**

选择 `AT+KNWSCANCFG=0` 使用的重试间隔方案。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR
CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_EXPONENTIAL
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:600`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L600)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置覆盖范围外扫描（Out-of-coverage Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_EXPONENTIAL`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_EXPONENTIAL)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_EXPONENTIAL"></a>

## 127.51 `CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_EXPONENTIAL`

**提示（Prompt）**：指数（Exponential）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:609`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L609)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置覆盖范围外扫描（Out-of-coverage Scan） → 覆盖范围外扫描退避方案（Backoff Scheme）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR"></a>

## 127.52 `CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR`

**提示（Prompt）**：线性（Linear）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:606`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L606)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置覆盖范围外扫描（Out-of-coverage Scan） → 覆盖范围外扫描退避方案（Backoff Scheme）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_VALUE"></a>

## 127.53 `CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_VALUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于 `AT+KNWSCANCFG=0` 的 `<scheme>` 参数的隐藏辅助值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
0 if CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR
1 if CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_EXPONENTIAL
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:614`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L614)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置覆盖范围外扫描（Out-of-coverage Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_EXPONENTIAL`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_EXPONENTIAL)。

<a id="CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_STEP"></a>

## 127.54 `CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_STEP`

**提示（Prompt）**：覆盖范围外线性扫描间隔步长，单位为秒

**说明（Help）**

选择线性模式时，相邻扫描之间增加的秒数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR && CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC && CONFIG_MODEM_HL78XX_KNWSCANCFG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 32767]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:636`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L636)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置网络扫描时序（Network Scan Timing） → 配置覆盖范围外扫描（Out-of-coverage Scan）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC_SCHEME_LINEAR)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG_OOC)、[`CONFIG_MODEM_HL78XX_KNWSCANCFG`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_KNWSCANCFG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_LOG_CONTEXT_VERBOSE_DEBUG"></a>

## 127.55 `CONFIG_MODEM_HL78XX_LOG_CONTEXT_VERBOSE_DEBUG`

**提示（Prompt）**：HL78xx 详细调试输出（Verbose Debug Output）

**说明（Help）**

启用后，调制解调器会产生极其大量的调试输出。生产环境中不得保持开启。此设置依赖全局日志级别为 Debug。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_MODULES_LOG_LEVEL_DBG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1646`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1646)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES_LOG_LEVEL_DBG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_LOW_POWER_MODE"></a>

## 127.56 `CONFIG_MODEM_HL78XX_LOW_POWER_MODE`

**提示（Prompt）**：低功耗模式（Low Power Modes）

**说明（Help）**

选择此设置，以启用 HL78XX 调制解调器的低功耗模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1139)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION"></a>

## 127.57 `CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION`

**提示（Prompt）**：低功耗策略（Low Power Strategy）

**说明（Help）**

只选择一种低功耗策略（Low-power Strategy）。在完成全面验证之前，有意禁用并行组合，例如 PSM + eDRX。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_PSM
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_EDRX
CONFIG_MODEM_HL78XX_PSM
CONFIG_MODEM_HL78XX_POWER_DOWN
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1146)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_PSM`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_PSM)、[`CONFIG_MODEM_HL78XX_EDRX`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_EDRX)、[`CONFIG_MODEM_HL78XX_POWER_DOWN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_POWER_DOWN)。

<a id="CONFIG_MODEM_HL78XX_MAX_PDP_CONTEXTS"></a>

## 127.58 `CONFIG_MODEM_HL78XX_MAX_PDP_CONTEXTS`

**提示（Prompt）**：PDP 上下文最大数量（Maximum PDP Contexts）

**说明（Help）**

可以同时定义的 PDP 上下文最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 1] if !CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG
[1, 2] if CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1546`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1546)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG)。

<a id="CONFIG_MODEM_HL78XX_NBNTN_POSITIONING"></a>

## 127.59 `CONFIG_MODEM_HL78XX_NBNTN_POSITIONING`

**提示（Prompt）**：NB-IoT 非地面网络（NTN）位置配置

**说明（Help）**

选择此设置，以配置 NB-IoT NTN 定位参数。当 NB-NTN 可能成为活动无线接入技术（RAT）时适用：可以是专用 NB-NTN 模式（`MODEM_HL78XX_RAT_NBNTN`），也可以是回退流程能在运行时将调制解调器转到 NTN 的自动 RAT 构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_NTN_SUPPORT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1043`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1043)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_NTN_SUPPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_NTN_SUPPORT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG"></a>

## 127.60 `CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG`

**提示（Prompt）**：网络注册状态报告配置（Network Registration Status Report Configuration）

**说明（Help）**

网络注册报告配置代码含义如下。命令格式保留原文占位符、空格、标点与换行。

0：禁用网络注册主动结果码。

1：启用网络注册主动结果码：

```text
+CEREG: <stat>
```

2：启用包含网络注册与位置信息的主动结果码：

```text
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>]]
```

3：启用包含网络注册、位置信息和 EMM 原因值的主动结果码：

```text
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,<cause_type>, <reject_cause>]]
```

4：对希望采用 PSM 的用户设备（UE），启用包含网络注册与位置信息的主动结果码：

```text
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,,[,[<Active- Time>],[<PeriodicTAU>]]]]
```

5：对希望采用 PSM 的用户设备（UE），启用包含网络注册、位置信息和 EMM 原因值的主动结果码：

```text
+CEREG: <stat>[,[<tac>],[<ci>],[<AcT>][,[<cause_type>],[<reject_-
cause>][,[<Active-Time>] [<Periodic-TAU>]]]]
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM_AND_CAUSE
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_DISABLE_NETWORK_STATUS_URC_REPORT
CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT
CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION
CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION_AND_CAUSE
CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM
CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM_AND_CAUSE
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1331`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1331)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM_AND_CAUSE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM_AND_CAUSE)、[`CONFIG_MODEM_HL78XX_DISABLE_NETWORK_STATUS_URC_REPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_DISABLE_NETWORK_STATUS_URC_REPORT)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION_AND_CAUSE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION_AND_CAUSE)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM)。

<a id="CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG_CODE"></a>

## 127.61 `CONFIG_MODEM_HL78XX_NETWORK_REG_STATUS_REPORT_CFG_CODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此设置用于配置网络注册状态报告代码，供 `AT+CREG`/`CEREG` 命令设置网络注册状态报告方式。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"5" if CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM_AND_CAUSE
"4" if CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM
"3" if CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION_AND_CAUSE
"2" if CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION
"1" if CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT
"0" if CONFIG_MODEM_HL78XX_DISABLE_NETWORK_STATUS_URC_REPORT
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1391`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1391)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM_AND_CAUSE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM_AND_CAUSE)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_PSM)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION_AND_CAUSE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION_AND_CAUSE)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT_WITH_LOCATION)、[`CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_ENABLE_NETWORK_STATUS_URC_REPORT)、[`CONFIG_MODEM_HL78XX_DISABLE_NETWORK_STATUS_URC_REPORT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_DISABLE_NETWORK_STATUS_URC_REPORT)。

<a id="CONFIG_MODEM_HL78XX_NTN_SUPPORT"></a>

## 127.62 `CONFIG_MODEM_HL78XX_NTN_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏能力符号：NB-NTN 可在运行时成为活动无线接入技术（RAT），既可来自专用 Kconfig RAT（`MODEM_HL78XX_RAT_NBNTN`），也可来自自动 RAT 从地面网络回退到 NTN 的流程，将 `AT+KSRAT=3` 保持为当前选择。此项编译进 NTN 配置辅助函数，包括 `+KNTNCFG` 定位配置，使两条路径应用相同的 NTN 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_RAT_NBNTN || (CONFIG_MODEM_HL78XX_AUTORAT && CONFIG_MODEM_HL78XX_12_FW_R6)
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:849`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L849)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_AUTORAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTORAT)、[`CONFIG_MODEM_HL78XX_12_FW_R6`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12_FW_R6)。

<a id="CONFIG_MODEM_HL78XX_NUM_SOCKETS"></a>

## 127.63 `CONFIG_MODEM_HL78XX_NUM_SOCKETS`

**提示（Prompt）**：套接字最大数量（Maximum Sockets）

**说明（Help）**

可以同时打开的套接字最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[6, 6] if !CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG
[1, 6] if CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1538`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1538)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG)。

<a id="CONFIG_MODEM_HL78XX_OFFLOAD_INIT_PRIORITY"></a>

## 127.64 `CONFIG_MODEM_HL78XX_OFFLOAD_INIT_PRIORITY`

**提示（Prompt）**：Sierra Wireless HL78XX 卸载驱动（Offload Driver）初始化优先级

**说明（Help）**

Sierra Wireless HL78XX 驱动的设备驱动初始化优先级。除非清楚其影响，否则不要随意更改。确保卸载驱动的初始化优先级数值高于设备初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
81
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1638`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1638)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_PERIODIC_SCRIPT_MS"></a>

## 127.65 `CONFIG_MODEM_HL78XX_PERIODIC_SCRIPT_MS`

**提示（Prompt）**：周期性脚本间隔（Periodic Script Interval），单位为毫秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:702`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L702)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_POWER_DOWN"></a>

## 127.66 `CONFIG_MODEM_HL78XX_POWER_DOWN`

**提示（Prompt）**：关闭（Turn OFF）

**说明（Help）**

关闭调制解调器电源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1164)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes） → 低功耗策略（Low Power Strategy）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION)。

<a id="CONFIG_MODEM_HL78XX_POWER_DOWN_ACTIVE_TIME"></a>

## 127.67 `CONFIG_MODEM_HL78XX_POWER_DOWN_ACTIVE_TIME`

**提示（Prompt）**：断电前调制解调器活动时间（Active Time）

**说明（Help）**

调制解调器断电前分配给用户设备（UE）的活动时间值，以 8 位格式表示的一个字节。默认值为 30 秒。此设置用于在关闭电源前，让调制解调器再保持活动一小段时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_USE_ACTIVE_TIME_BASED_POWER_DOWN && CONFIG_MODEM_HL78XX_POWER_DOWN && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[20, 600]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1265)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_USE_ACTIVE_TIME_BASED_POWER_DOWN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_USE_ACTIVE_TIME_BASED_POWER_DOWN)、[`CONFIG_MODEM_HL78XX_POWER_DOWN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_POWER_DOWN)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_POWER_DOWN_CONFIRM_TIMEOUT_S"></a>

## 127.68 `CONFIG_MODEM_HL78XX_POWER_DOWN_CONFIRM_TIMEOUT_S`

**提示（Prompt）**：正常关机确认超时（Graceful Shutdown Confirmation Timeout），单位为秒

**说明（Help）**

以 `POWER_DOWN_EVENT_ENTER` 分发 `HL78XX_POWER_DOWN_UPDATE` 后，驱动等待应用调用 `hl78xx_power_down_respond()` 的时间，单位为秒。调用方可使用立即响应（Immediate Response）马上继续关机，或使用重新调度响应（Reschedule Response）从当前时刻延长宽限期。若应用未在此窗口内响应，驱动将无条件继续关闭调制解调器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_POWER_DOWN && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[5, 60]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1278`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1278)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_POWER_DOWN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_POWER_DOWN)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_POWER_DOWN_DELAY"></a>

## 127.69 `CONFIG_MODEM_HL78XX_POWER_DOWN_DELAY`

**提示（Prompt）**：断电前延迟，单位为秒

**说明（Help）**

最后一次数据传输后、关闭调制解调器电源前的延迟，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_USE_DELAY_BASED_POWER_DOWN && CONFIG_MODEM_HL78XX_POWER_DOWN && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[10, 600]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1253)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_USE_DELAY_BASED_POWER_DOWN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_USE_DELAY_BASED_POWER_DOWN)、[`CONFIG_MODEM_HL78XX_POWER_DOWN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_POWER_DOWN)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_POWER_DOWN_MODE"></a>

## 127.70 `CONFIG_MODEM_HL78XX_POWER_DOWN_MODE`

**提示（Prompt）**：断电模式（Power Down Mode）

**说明（Help）**

选择决定 HL78XX 调制解调器何时断电的逻辑，只能选择一种：

- 使用最后一次数据活动之后的延迟（Use Delay after Last Data Activity）。
- 使用 RRC 连接之后的活动时间（Use Active Time after RRC Connection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_POWER_DOWN && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_USE_DELAY_BASED_POWER_DOWN
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_USE_DELAY_BASED_POWER_DOWN
CONFIG_MODEM_HL78XX_USE_ACTIVE_TIME_BASED_POWER_DOWN
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1227)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_POWER_DOWN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_POWER_DOWN)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_USE_DELAY_BASED_POWER_DOWN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_USE_DELAY_BASED_POWER_DOWN)、[`CONFIG_MODEM_HL78XX_USE_ACTIVE_TIME_BASED_POWER_DOWN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_USE_ACTIVE_TIME_BASED_POWER_DOWN)。

<a id="CONFIG_MODEM_HL78XX_PSM"></a>

## 127.71 `CONFIG_MODEM_HL78XX_PSM`

**提示（Prompt）**：省电模式（PSM）

**说明（Help）**

启用省电模式（Power Save Mode，PSM）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1159)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes） → 低功耗策略（Low Power Strategy）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_SELECTION)。

<a id="CONFIG_MODEM_HL78XX_PSM_ACTIVE_TIME"></a>

## 127.72 `CONFIG_MODEM_HL78XX_PSM_ACTIVE_TIME`

**提示（Prompt）**：请求的活动时间（Requested Active Time）

**说明（Help）**

请求分配给用户设备（UE）的活动时间值（T3324），以 8 位格式表示的一个字节。默认值为 30 秒。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_PSM && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"00001111"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1217)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_PSM`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_PSM)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_PSM_PERIODIC_TAU"></a>

## 127.73 `CONFIG_MODEM_HL78XX_PSM_PERIODIC_TAU`

**提示（Prompt）**：请求的扩展周期性 TAU 定时器

**说明（Help）**

请求在 E-UTRAN 中分配给用户设备（UE）的扩展周期性跟踪区更新（Tracking Area Update，TAU）值（T3412），以 8 位格式表示的一个字节。默认值为 15 分钟。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_PSM && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"10000010"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1209)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_PSM`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_PSM)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_PTW_VALUE"></a>

## 127.74 `CONFIG_MODEM_HL78XX_PTW_VALUE`

**提示（Prompt）**：请求的 eDRX 寻呼时间窗口（Paging Time Window，PTW）定时器

**说明（Help）**

PTW 值对应扩展 DRX 参数信息元素第 3 个八位组的位 8 至位 5。实际寻呼时间窗口长度按原文公式计算：

- CAT-M1：

```text
actual PTW length = 1.28 sec x (1 + PTW)
```

- NB-IoT：

```text
actual PTW length = 2.56 sec x (1 + PTW)
```

其中 `actual PTW length` 为实际 PTW 长度，`sec` 为秒，`x` 表示乘法。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_EDRX && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1182)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_EDRX`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_EDRX)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_RAT"></a>

## 127.75 `CONFIG_MODEM_HL78XX_RAT`

**提示（Prompt）**：无线接入技术模式（Radio Access Technology Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_AUTORAT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_RAT_M1
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_RAT_M1
CONFIG_MODEM_HL78XX_RAT_NB1
CONFIG_MODEM_HL78XX_RAT_GSM
CONFIG_MODEM_HL78XX_RAT_NBNTN
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:816`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L816)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTORAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTORAT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_RAT_M1`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_M1)、[`CONFIG_MODEM_HL78XX_RAT_NB1`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NB1)、[`CONFIG_MODEM_HL78XX_RAT_GSM`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_GSM)、[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)。

<a id="CONFIG_MODEM_HL78XX_RAT_GSM"></a>

## 127.76 `CONFIG_MODEM_HL78XX_RAT_GSM`

**提示（Prompt）**：全球移动通信系统（GSM）

**说明（Help）**

调制解调器初始化期间启用 GSM 模式。2 表示 GSM，仅适用于 HL7802/HL7812。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_12 && <choice CONFIG_MODEM_HL78XX_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:833`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L833)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_12`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12)、[`CONFIG_MODEM_HL78XX_RAT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT)。

<a id="CONFIG_MODEM_HL78XX_RAT_M1"></a>

## 127.77 `CONFIG_MODEM_HL78XX_RAT_M1`

**提示（Prompt）**：LTE-M1

**说明（Help）**

调制解调器初始化期间启用 LTE Cat-M1 模式。在读取响应（Read Response）中，0 表示 CAT-M1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:821`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L821)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT)。

<a id="CONFIG_MODEM_HL78XX_RAT_NB1"></a>

## 127.78 `CONFIG_MODEM_HL78XX_RAT_NB1`

**提示（Prompt）**：窄带物联网（NB-IoT）

**说明（Help）**

调制解调器初始化期间启用 LTE Cat-NB1 模式。1 表示 NB-IoT，仅适用于 HL78XX/HL7802/HL7810/HL7845/HL7812。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:827`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L827)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT)。

<a id="CONFIG_MODEM_HL78XX_RAT_NBNTN"></a>

## 127.79 `CONFIG_MODEM_HL78XX_RAT_NBNTN`

**提示（Prompt）**：窄带非地面网络（NB-NTN）

**说明（Help）**

调制解调器初始化期间启用 NBNTN 模式。3 表示 NBNTN，仅适用于 HL7810/HL7812。不支持 `<reboot> = 1`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_12_FW_R6 && <choice CONFIG_MODEM_HL78XX_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:840`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L840)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_12_FW_R6`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12_FW_R6)、[`CONFIG_MODEM_HL78XX_RAT`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT)。

<a id="CONFIG_MODEM_HL78XX_RECV_BUF_CNT"></a>

## 127.80 `CONFIG_MODEM_HL78XX_RECV_BUF_CNT`

**提示（Prompt）**：分配的网络缓冲区数量（Network Buffer Count）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1580`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1580)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_RECV_BUF_SIZE"></a>

## 127.81 `CONFIG_MODEM_HL78XX_RECV_BUF_SIZE`

**提示（Prompt）**：网络缓冲区大小，单位为字节

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1584`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1584)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_RSSI_WORK"></a>

## 127.82 `CONFIG_MODEM_HL78XX_RSSI_WORK`

**提示（Prompt）**：RSSI 轮询工作项（Polling Work）

**说明（Help）**

将 Sierra Wireless HL78XX 驱动设备配置为轮询接收信号强度指示（RSSI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:765`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L765)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_RSSI_WORK_PERIOD"></a>

## 127.83 `CONFIG_MODEM_HL78XX_RSSI_WORK_PERIOD`

**提示（Prompt）**：配置 RSSI 工作项轮询频率（Polling Frequency）

**说明（Help）**

此设置用于配置 RSSI 轮询周期。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_RSSI_WORK && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:771`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L771)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → RSSI 轮询工作项（Polling Work）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RSSI_WORK`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RSSI_WORK)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_RX_WORKQ_STACK_SIZE"></a>

## 127.84 `CONFIG_MODEM_HL78XX_RX_WORKQ_STACK_SIZE`

**提示（Prompt）**：Sierra Wireless HL78XX 调制解调器驱动工作队列栈大小

**说明（Help）**

工作队列（Work Queue）使用此栈，将 `net_pkt` 数据交给网络协议栈的其他部分，使接收线程能继续处理数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1588`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1588)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_SLEEP_DELAY_AFTER_REBOOT"></a>

## 127.85 `CONFIG_MODEM_HL78XX_SLEEP_DELAY_AFTER_REBOOT`

**提示（Prompt）**：重启后进入睡眠前的延迟，单位为秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_POWER_DOWN && CONFIG_MODEM_HL78XX_LOW_POWER_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1324`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1324)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_POWER_DOWN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_POWER_DOWN)、[`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_LOW_POWER_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_SLEEP_LEVEL_HIBERNATE"></a>

## 127.86 `CONFIG_MODEM_HL78XX_SLEEP_LEVEL_HIBERNATE`

**提示（Prompt）**：休眠（Hibernate）

**说明（Help）**

功耗最低；不保留 I/O 状态；应用子系统关闭（OFF）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_DEFAULT_SLEEP_LEVEL>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1301`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1301)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes） → 默认睡眠级别（Default Sleep Level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_DEFAULT_SLEEP_LEVEL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_DEFAULT_SLEEP_LEVEL)。

<a id="CONFIG_MODEM_HL78XX_SLEEP_LEVEL_LITE_HIBERNATE"></a>

## 127.87 `CONFIG_MODEM_HL78XX_SLEEP_LEVEL_LITE_HIBERNATE`

**提示（Prompt）**：轻度休眠（Lite Hibernate）

**说明（Help）**

保留 I/O 状态；应用子系统关闭（OFF）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_DEFAULT_SLEEP_LEVEL>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1308`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1308)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes） → 默认睡眠级别（Default Sleep Level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_DEFAULT_SLEEP_LEVEL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_DEFAULT_SLEEP_LEVEL)。

<a id="CONFIG_MODEM_HL78XX_SLEEP_LEVEL_SLEEP"></a>

## 127.88 `CONFIG_MODEM_HL78XX_SLEEP_LEVEL_SLEEP`

**提示（Prompt）**：睡眠（Sleep）

**说明（Help）**

在调制解调器各睡眠状态中功耗最高；保留 I/O 状态；应用子系统开启（ON）；允许套接字（Socket）保持打开。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_DEFAULT_SLEEP_LEVEL>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1314)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 低功耗模式（Low Power Modes） → 默认睡眠级别（Default Sleep Level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_DEFAULT_SLEEP_LEVEL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_DEFAULT_SLEEP_LEVEL)。

<a id="CONFIG_MODEM_HL78XX_SOCKETS_SOCKOPT_TLS"></a>

## 127.89 `CONFIG_MODEM_HL78XX_SOCKETS_SOCKOPT_TLS`

**提示（Prompt）**：套接字的传输层安全（TLS）支持

**说明（Help）**

此选项为 HL78xx 调制解调器上的套接字启用传输层安全（Transport Layer Security，TLS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1554`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1554)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_SOCKET_RESTORE_ON_BOOT"></a>

## 127.90 `CONFIG_MODEM_HL78XX_SOCKET_RESTORE_ON_BOOT`

**提示（Prompt）**：启动时恢复套接字（Restore Sockets on Boot）

**说明（Help）**

只恢复第一个会话（Session）。

- 对 HL780x，要在 eDRX/PSM 休眠周期或复位之后恢复第一个会话，必须启用 `restore_on_boot`。
- 对 HL781x/45，所有会话都会跨 eDRX/PSM 休眠周期保留，与此配置无关；仅在复位场景需要此选项。
- 对恢复后的客户端会话，例如复位或退出休眠之后，必须先用 `+KTCPCNX` 建立连接，才能发送／接收任何数据。

0 表示启动时不恢复套接字；1 表示启动时恢复套接字。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1523`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1523)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 高级套接字配置（Advanced Socket Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_SOCKET_UDP_DISPLAY_DATA_URC"></a>

## 127.91 `CONFIG_MODEM_HL78XX_SOCKET_UDP_DISPLAY_DATA_URC`

**提示（Prompt）**：在主动结果码（URC）中显示数据

**说明（Help）**

- 0：不在 URC 中显示数据。
- 1：自动在 URC 中显示数据。
- 2：不在 URC 中显示数据，必须使用 `KUDPRCV` 命令转储数据。如果在 `rcv_timeout` 之后仍未收到 `KUDPRCV` 命令，则丢弃原始数据，并重新启用 URC。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1513`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1513)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 高级套接字配置（Advanced Socket Configuration）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_STAY_IN_BOOT_MODE_FOR_ROAMING"></a>

## 127.92 `CONFIG_MODEM_HL78XX_STAY_IN_BOOT_MODE_FOR_ROAMING`

**提示（Prompt）**：等待漫游（Wait for Roaming）

**说明（Help）**

保持设备处于启动模式，直到收到 `+CREG`/`+CEREG` 状态 1（正常，Normal）或 5（漫游，Roaming）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_BOOT_IN_FULLY_FUNCTIONAL_MODE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:576`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L576)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_BOOT_IN_FULLY_FUNCTIONAL_MODE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_BOOT_IN_FULLY_FUNCTIONAL_MODE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE"></a>

## 127.93 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`

**提示（Prompt）**：目标 UART 波特率（Target Baud Rate）

**说明（Help）**

选择与调制解调器通信的目标波特率。检测完成后，驱动会将调制解调器配置为使用此波特率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_115200
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_9600
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_19200
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_38400
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_57600
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_115200
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_230400
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_460800
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_3000000
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTO_BAUDRATE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_115200`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_115200)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_9600`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_9600)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_19200`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_19200)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_38400`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_38400)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_57600`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_57600)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_230400`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_230400)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_460800`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_460800)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_3000000`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_3000000)。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_115200"></a>

## 127.94 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_115200`

**提示（Prompt）**：115200

**说明（Help）**

将调制解调器波特率设为 115200 bps，默认值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_TARGET_BAUDRATE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching） → 目标 UART 波特率（Target Baud Rate）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE)。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_19200"></a>

## 127.95 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_19200`

**提示（Prompt）**：19200

**说明（Help）**

将调制解调器波特率设为 19200 bps。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_TARGET_BAUDRATE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching） → 目标 UART 波特率（Target Baud Rate）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE)。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_230400"></a>

## 127.96 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_230400`

**提示（Prompt）**：230400

**说明（Help）**

将调制解调器波特率设为 230400 bps。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_TARGET_BAUDRATE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching） → 目标 UART 波特率（Target Baud Rate）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE)。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_3000000"></a>

## 127.97 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_3000000`

**提示（Prompt）**：3000000

**说明（Help）**

将调制解调器波特率设为 3000000 bps。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_12 && <choice CONFIG_MODEM_HL78XX_TARGET_BAUDRATE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching） → 目标 UART 波特率（Target Baud Rate）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_12`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12)、[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE)。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_38400"></a>

## 127.98 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_38400`

**提示（Prompt）**：38400

**说明（Help）**

将调制解调器波特率设为 38400 bps。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_TARGET_BAUDRATE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching） → 目标 UART 波特率（Target Baud Rate）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE)。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_460800"></a>

## 127.99 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_460800`

**提示（Prompt）**：460800

**说明（Help）**

将调制解调器波特率设为 460800 bps。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_TARGET_BAUDRATE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching） → 目标 UART 波特率（Target Baud Rate）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE)。

<a id="CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_57600"></a>

## 127.100 `CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_57600`

**提示（Prompt）**：57600

**说明（Help）**

将调制解调器波特率设为 57600 bps。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_TARGET_BAUDRATE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching） → 目标 UART 波特率（Target Baud Rate）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_TARGET_BAUDRATE`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_TARGET_BAUDRATE)。

<!-- kconfig-navigation -->

[上一章](P126_drivers_modem_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P128_drivers_modem_配置项参考_4.md)
