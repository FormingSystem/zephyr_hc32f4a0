---
id: learning.zephyr-docs.kconfig-reference.page-126
title: "`drivers/modem`配置项参考（2/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第126章\_`drivers/modem`配置项参考（2/4）

本章翻译官方 Kconfig 数据库中 `drivers/modem` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MODEM_HL7800_BAND_2"></a>

## 126.1 `CONFIG_MODEM_HL7800_BAND_2`

**提示（Prompt）**：频段（Band）2：1900 MHz

**说明（Help）**

启用频段 2：1900 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_20"></a>

## 126.2 `CONFIG_MODEM_HL7800_BAND_20`

**提示（Prompt）**：频段 20：800 MHz

**说明（Help）**

启用频段 20：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_25"></a>

## 126.3 `CONFIG_MODEM_HL7800_BAND_25`

**提示（Prompt）**：频段 25：1900 MHz

**说明（Help）**

启用频段 25：1900 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_26"></a>

## 126.4 `CONFIG_MODEM_HL7800_BAND_26`

**提示（Prompt）**：频段 26：800 MHz

**说明（Help）**

启用频段 26：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_27"></a>

## 126.5 `CONFIG_MODEM_HL7800_BAND_27`

**提示（Prompt）**：频段 27：800 MHz

**说明（Help）**

启用频段 27：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_28"></a>

## 126.6 `CONFIG_MODEM_HL7800_BAND_28`

**提示（Prompt）**：频段 28：700 MHz

**说明（Help）**

启用频段 28：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_3"></a>

## 126.7 `CONFIG_MODEM_HL7800_BAND_3`

**提示（Prompt）**：频段 3：1800 MHz

**说明（Help）**

启用频段 3：1800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_4"></a>

## 126.8 `CONFIG_MODEM_HL7800_BAND_4`

**提示（Prompt）**：频段 4：1700 MHz

**说明（Help）**

启用频段 4：1700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_5"></a>

## 126.9 `CONFIG_MODEM_HL7800_BAND_5`

**提示（Prompt）**：频段 5：850 MHz

**说明（Help）**

启用频段 5：850 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_66"></a>

## 126.10 `CONFIG_MODEM_HL7800_BAND_66`

**提示（Prompt）**：频段 66：1800 MHz

**说明（Help）**

启用频段 66：1800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L183)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_8"></a>

## 126.11 `CONFIG_MODEM_HL7800_BAND_8`

**提示（Prompt）**：频段 8：900 MHz

**说明（Help）**

启用频段 8：900 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BAND_9"></a>

## 126.12 `CONFIG_MODEM_HL7800_BAND_9`

**提示（Prompt）**：频段 9：1900 MHz

**说明（Help）**

启用频段 9：1900 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_CONFIGURE_BANDS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_CONFIGURE_BANDS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_BOOT_DELAY"></a>

## 126.13 `CONFIG_MODEM_HL7800_BOOT_DELAY`

**提示（Prompt）**：延后驱动的第二阶段初始化和网络附着（Network Attach）

**说明（Help）**

此项为 true 时，应用必须调用 `mdm_hl7800_reset`。此模式会推迟调制解调器信息变为有效的时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 调制解调器启动类型（Modem Boot Type）

<a id="CONFIG_MODEM_HL7800_BOOT_IN_AIRPLANE_MODE"></a>

## 126.14 `CONFIG_MODEM_HL7800_BOOT_IN_AIRPLANE_MODE`

**提示（Prompt）**：初始化期间进入飞行模式（Airplane Mode）

**说明（Help）**

应用必须使用 `mdm_hl7800_set_functionality` 退出飞行模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:319`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L319)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 调制解调器启动类型（Modem Boot Type）

<a id="CONFIG_MODEM_HL7800_BOOT_NORMAL"></a>

## 126.15 `CONFIG_MODEM_HL7800_BOOT_NORMAL`

**提示（Prompt）**：无延迟（No Delay）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:310`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L310)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 调制解调器启动类型（Modem Boot Type）

<a id="CONFIG_MODEM_HL7800_CONFIGURE_BANDS"></a>

## 126.16 `CONFIG_MODEM_HL7800_CONFIGURE_BANDS`

**提示（Prompt）**：配置调制解调器频段（Modem Bands）

**说明（Help）**

选择此设置，以配置 HL7800 调制解调器在启动时应使用哪些 LTE 频段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_CTS_FILTER_US"></a>

## 126.17 `CONFIG_MODEM_HL7800_CTS_FILTER_US`

**提示（Prompt）**：允许发送（Clear to Send，CTS）信号滤波时间，单位为微秒

**说明（Help）**

此值用于过滤调制解调器的 CTS 信号。短于此时长的 CTS 脉冲将被忽略。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L367)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_EDRX"></a>

## 126.18 `CONFIG_MODEM_HL7800_EDRX`

**提示（Prompt）**：扩展非连续接收（eDRX）

**说明（Help）**

启用 LTE 扩展非连续接收（eDRX）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 低功耗模式（Low Power Modes） → 低功耗模式（Low Power Mode）

<a id="CONFIG_MODEM_HL7800_EDRX_VALUE"></a>

## 126.19 `CONFIG_MODEM_HL7800_EDRX_VALUE`

**提示（Prompt）**：请求的 eDRX 定时器（Requested eDRX Timer）

**说明（Help）**

以 4 位格式表示的半个字节。eDRX 值对应扩展 DRX 参数信息元素（Extended DRX Parameters Information Element）第 3 个八位组（Octet）的位 4 至位 1。默认值为 81.92 秒。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_EDRX && CONFIG_MODEM_HL7800_LOW_POWER_MODE && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"0101"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_EDRX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_EDRX)、[`CONFIG_MODEM_HL7800_LOW_POWER_MODE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_LOW_POWER_MODE)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_FW_UPDATE"></a>

## 126.20 `CONFIG_MODEM_HL7800_FW_UPDATE`

**提示（Prompt）**：固件更新（Firmware Update）

**说明（Help）**

启用通过 XMODEM 更新 HL7800 的能力，方法是向更新 API 提供更新文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_FILE_SYSTEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_FILE_SYSTEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_MODEM_HL7800_GET_IP_ADDR_INFO_ATTEMPTS"></a>

## 126.21 `CONFIG_MODEM_HL7800_GET_IP_ADDR_INFO_ATTEMPTS`

**提示（Prompt）**：初始化期间尝试获取 IP 地址信息的次数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:302`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L302)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_GPS"></a>

## 126.22 `CONFIG_MODEM_HL7800_GPS`

**提示（Prompt）**：GPS 命令与处理程序（Commands and Handlers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:327`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L327)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_INIT_PRIORITY"></a>

## 126.23 `CONFIG_MODEM_HL7800_INIT_PRIORITY`

**提示（Prompt）**：HL7800 驱动初始化优先级

**说明（Help）**

HL7800 设备驱动的初始化优先级。除非清楚其影响，否则不要随意更改。注意，数值需要低于网络协议栈的初始化优先级，使它能在网络子系统之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:293`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L293)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_LOW_POWER_MODE"></a>

## 126.24 `CONFIG_MODEM_HL7800_LOW_POWER_MODE`

**提示（Prompt）**：低功耗模式（Low Power Modes）

**说明（Help）**

选择此设置，以启用 HL7800 调制解调器的低功耗模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_POLTE"></a>

## 126.25 `CONFIG_MODEM_HL7800_POLTE`

**提示（Prompt）**：PoLTE 命令与处理程序（Commands and Handlers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L334)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_PSM"></a>

## 126.26 `CONFIG_MODEM_HL7800_PSM`

**提示（Prompt）**：省电模式（PSM）

**说明（Help）**

启用省电模式（Power Save Mode，PSM）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 低功耗模式（Low Power Modes） → 低功耗模式（Low Power Mode）

<a id="CONFIG_MODEM_HL7800_PSM_ACTIVE_TIME"></a>

## 126.27 `CONFIG_MODEM_HL7800_PSM_ACTIVE_TIME`

**提示（Prompt）**：请求的活动时间（Requested Active Time）

**说明（Help）**

请求分配给用户设备（UE）的活动时间值（T3324），以 8 位格式表示的一个字节。默认值为 30 秒。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_PSM && CONFIG_MODEM_HL7800_LOW_POWER_MODE && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"00001111"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_PSM`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_PSM)、[`CONFIG_MODEM_HL7800_LOW_POWER_MODE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_LOW_POWER_MODE)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_PSM_PERIODIC_TAU"></a>

## 126.28 `CONFIG_MODEM_HL7800_PSM_PERIODIC_TAU`

**提示（Prompt）**：请求的扩展周期性 TAU 定时器

**说明（Help）**

请求在演进型通用陆地无线接入网（E-UTRAN）中分配给用户设备（UE）的扩展周期性跟踪区更新（Tracking Area Update，TAU）值（T3412），以 8 位格式表示的一个字节。默认值为 1 分钟。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_PSM && CONFIG_MODEM_HL7800_LOW_POWER_MODE && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"10000010"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L226)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_PSM`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_PSM)、[`CONFIG_MODEM_HL7800_LOW_POWER_MODE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_LOW_POWER_MODE)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_RAT"></a>

## 126.29 `CONFIG_MODEM_HL7800_RAT`

**提示（Prompt）**：无线接入技术模式（Radio Access Technology Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL7800_RAT_NO_CHANGE
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL7800_RAT_NO_CHANGE
CONFIG_MODEM_HL7800_RAT_M1
CONFIG_MODEM_HL7800_RAT_NB1
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL7800_RAT_NO_CHANGE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_RAT_NO_CHANGE)、[`CONFIG_MODEM_HL7800_RAT_M1`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_RAT_M1)、[`CONFIG_MODEM_HL7800_RAT_NB1`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_RAT_NB1)。

<a id="CONFIG_MODEM_HL7800_RAT_M1"></a>

## 126.30 `CONFIG_MODEM_HL7800_RAT_M1`

**提示（Prompt）**：LTE-M1

**说明（Help）**

调制解调器初始化期间启用 LTE Cat-M1 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL7800_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_RAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_RAT)。

<a id="CONFIG_MODEM_HL7800_RAT_NB1"></a>

## 126.31 `CONFIG_MODEM_HL7800_RAT_NB1`

**提示（Prompt）**：窄带物联网（NB-IoT）

**说明（Help）**

调制解调器初始化期间启用 LTE Cat-NB1 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL7800_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_RAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_RAT)。

<a id="CONFIG_MODEM_HL7800_RAT_NO_CHANGE"></a>

## 126.32 `CONFIG_MODEM_HL7800_RAT_NO_CHANGE`

**提示（Prompt）**：不更改无线接入技术（RAT）

**说明（Help）**

调制解调器初始化期间保持 HL7800 的 RAT 不变。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL7800_RAT>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 无线接入技术模式（Radio Access Technology Mode）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_RAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_RAT)。

<a id="CONFIG_MODEM_HL7800_RECV_BUF_CNT"></a>

## 126.33 `CONFIG_MODEM_HL7800_RECV_BUF_CNT`

**提示（Prompt）**：分配的网络缓冲区数量（Network Buffer Count）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_RECV_BUF_SIZE"></a>

## 126.34 `CONFIG_MODEM_HL7800_RECV_BUF_SIZE`

**提示（Prompt）**：网络缓冲区大小，单位为字节

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_RSSI_RATE_SECONDS"></a>

## 126.35 `CONFIG_MODEM_HL7800_RSSI_RATE_SECONDS`

**提示（Prompt）**：自动查询接收信号强度指示（RSSI）的频率

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
0 if CONFIG_MODEM_HL7800_LOW_POWER_MODE
30
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:362`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L362)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL7800_LOW_POWER_MODE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_LOW_POWER_MODE)。

<a id="CONFIG_MODEM_HL7800_RX_STACK_SIZE"></a>

## 126.36 `CONFIG_MODEM_HL7800_RX_STACK_SIZE`

**提示（Prompt）**：HL7800 调制解调器驱动接收线程栈大小

**说明（Help）**

此栈由 HL7800 接收（RX）线程使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
1536 if CONFIG_MODEM_HL7800_POLTE
1280
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:278`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L278)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL7800_POLTE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_POLTE)。

<a id="CONFIG_MODEM_HL7800_RX_WORKQ_STACK_SIZE"></a>

## 126.37 `CONFIG_MODEM_HL7800_RX_WORKQ_STACK_SIZE`

**提示（Prompt）**：HL7800 调制解调器驱动工作队列栈大小

**说明（Help）**

工作队列（Work Queue）使用此栈，将 `net_pkt` 数据交给网络协议栈的其他部分，使接收线程能继续处理数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_SET_APN_NAME_ON_STARTUP"></a>

## 126.38 `CONFIG_MODEM_HL7800_SET_APN_NAME_ON_STARTUP`

**提示（Prompt）**：在驱动初始化期间设置 APN 名称

**说明（Help）**

启动时，如果 APN 与 `MODEM_HL7800_APN_NAME` 不匹配，则将其设为该配置值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_SLEEP_DELAY_AFTER_REBOOT"></a>

## 126.39 `CONFIG_MODEM_HL7800_SLEEP_DELAY_AFTER_REBOOT`

**提示（Prompt）**：重启后进入睡眠前的延迟，单位为秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_LOW_POWER_MODE && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:272`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L272)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 低功耗模式（Low Power Modes）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_LOW_POWER_MODE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_LOW_POWER_MODE)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL7800_SLEEP_LEVEL_HIBERNATE"></a>

## 126.40 `CONFIG_MODEM_HL7800_SLEEP_LEVEL_HIBERNATE`

**提示（Prompt）**：休眠（Hibernate）

**说明（Help）**

功耗最低；不保留 I/O 状态；应用子系统关闭（OFF）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 低功耗模式（Low Power Modes） → 默认睡眠级别（Default Sleep Level）

<a id="CONFIG_MODEM_HL7800_SLEEP_LEVEL_LITE_HIBERNATE"></a>

## 126.41 `CONFIG_MODEM_HL7800_SLEEP_LEVEL_LITE_HIBERNATE`

**提示（Prompt）**：轻度休眠（Lite Hibernate）

**说明（Help）**

保留 I/O 状态；应用子系统关闭（OFF）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 低功耗模式（Low Power Modes） → 默认睡眠级别（Default Sleep Level）

<a id="CONFIG_MODEM_HL7800_SLEEP_LEVEL_SLEEP"></a>

## 126.42 `CONFIG_MODEM_HL7800_SLEEP_LEVEL_SLEEP`

**提示（Prompt）**：睡眠（Sleep）

**说明（Help）**

在调制解调器各睡眠状态中功耗最高；保留 I/O 状态；应用子系统开启（ON）；允许套接字（Socket）保持打开。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → 低功耗模式（Low Power Modes） → 默认睡眠级别（Default Sleep Level）

<a id="CONFIG_MODEM_HL7800_USE_GLONASS"></a>

## 126.43 `CONFIG_MODEM_HL7800_USE_GLONASS`

**提示（Prompt）**：除 GPS 外还使用 GLONASS

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL7800_GPS && CONFIG_MODEM_HL7800 && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800:330`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl7800-legacy/Kconfig.hl7800#L330)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Sierra Wireless HL7800 调制解调器驱动 → GPS 命令与处理程序（Commands and Handlers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL7800_GPS`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_GPS)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX"></a>

## 126.44 `CONFIG_MODEM_HL78XX`

**提示（Prompt）**：HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**说明（Help）**

选择此设置，以启用 Sierra Wireless HL78XX LTE-CatM1/NB-IoT 调制解调器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_CELLULAR && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_MODEM_MODULES
CONFIG_MODEM_CHAT
CONFIG_MODEM_PIPE
CONFIG_MODEM_PIPELINK
CONFIG_MODEM_BACKEND_UART
CONFIG_MODEM_SOCKET
CONFIG_NET_OFFLOAD
CONFIG_MODEM_CONTEXT
CONFIG_EXPERIMENTAL
```

**弱选择（Implies）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_CHAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_PIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PIPE)、[`CONFIG_MODEM_PIPELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PIPELINK)、[`CONFIG_MODEM_BACKEND_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_SOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_SOCKET)、[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MODEM_HL78XX_00"></a>

## 126.45 `CONFIG_MODEM_HL78XX_00`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

存在匹配设备树节点时，启用 Sierra Wireless HL7800 调制解调器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if DT_HAS_SWIR_HL7800_ENABLED
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_12"></a>

## 126.46 `CONFIG_MODEM_HL78XX_12`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

存在匹配设备树节点时，启用 Sierra Wireless HL7812 调制解调器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if DT_HAS_SWIR_HL7812_ENABLED
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_12_FW_R6"></a>

## 126.47 `CONFIG_MODEM_HL78XX_12_FW_R6`

**提示（Prompt）**：调制解调器固件 R6

**说明（Help）**

仅适用于 HL7812。启用此设置以使用窄带非地面网络（NBNTN）无线接入技术，这是 NBNTN 模式的必需设置。R6 固件支持 NBNTN 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_12 && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_12`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_ADDRESS_FAMILY"></a>

## 126.48 `CONFIG_MODEM_HL78XX_ADDRESS_FAMILY`

**提示（Prompt）**：IP 地址族（Address Family）

**说明（Help）**

IP 连接使用的地址族（Address Family）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IP if CONFIG_MODEM_HL78XX_RAT_NBNTN
CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4V6 if !CONFIG_MODEM_HL78XX_RAT_NBNTN
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IP
CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4
CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV6
CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4V6
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:523`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L523)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IP`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IP)、[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4V6`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4V6)、[`CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4)、[`CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV6`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV6)。

<a id="CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IP"></a>

## 126.49 `CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IP`

**提示（Prompt）**：互联网协议（IP）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_ADDRESS_FAMILY>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:529`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L529)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → IP 地址族（Address Family）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_ADDRESS_FAMILY`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADDRESS_FAMILY)。

<a id="CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4"></a>

## 126.50 `CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4`

**提示（Prompt）**：IPv4（互联网协议第 4 版）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_ADDRESS_FAMILY>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:531`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L531)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → IP 地址族（Address Family）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_ADDRESS_FAMILY`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADDRESS_FAMILY)。

<a id="CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4V6"></a>

## 126.51 `CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV4V6`

**提示（Prompt）**：IPv4v6（IPv4／IPv6 双栈）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_ADDRESS_FAMILY>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:537`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L537)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → IP 地址族（Address Family）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_ADDRESS_FAMILY`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADDRESS_FAMILY)。

<a id="CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV6"></a>

## 126.52 `CONFIG_MODEM_HL78XX_ADDRESS_FAMILY_IPV6`

**提示（Prompt）**：IPv6（互联网协议第 6 版）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_ADDRESS_FAMILY>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:534`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L534)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → IP 地址族（Address Family）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_ADDRESS_FAMILY`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_ADDRESS_FAMILY)。

<a id="CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG"></a>

## 126.53 `CONFIG_MODEM_HL78XX_ADVANCED_SOCKET_CONFIG`

**提示（Prompt）**：高级套接字配置（Advanced Socket Configuration）

**说明（Help）**

启用高级套接字配置选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1506`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1506)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AIRVANTAGE"></a>

## 126.54 `CONFIG_MODEM_HL78XX_AIRVANTAGE`

**提示（Prompt）**：AirVantage

**说明（Help）**

启用 HL78xx 模块通过 OMA 连接 AirVantage 设备管理（DM）服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1453`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1453)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AIRVANTAGE_HOST_INITIATED"></a>

## 126.55 `CONFIG_MODEM_HL78XX_AIRVANTAGE_HOST_INITIATED`

**提示（Prompt）**：主机发起（Host Initiated）

**说明（Help）**

由主机应用负责发起与 AirVantage 服务器的连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_AIRVANTAGE_SESSION_INITIATION>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1466`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1466)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AirVantage → AirVantage 初始化（Initialization）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AIRVANTAGE_SESSION_INITIATION`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE_SESSION_INITIATION)。

<a id="CONFIG_MODEM_HL78XX_AIRVANTAGE_MODULE_INITIATED"></a>

## 126.56 `CONFIG_MODEM_HL78XX_AIRVANTAGE_MODULE_INITIATED`

**提示（Prompt）**：模块发起（Module Initiated）

**说明（Help）**

由 HL78xx 模块负责发起与 AirVantage 服务器的连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_AIRVANTAGE_SESSION_INITIATION>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1471`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1471)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AirVantage → AirVantage 初始化（Initialization）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AIRVANTAGE_SESSION_INITIATION`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE_SESSION_INITIATION)。

<a id="CONFIG_MODEM_HL78XX_AIRVANTAGE_SESSION_INITIATION"></a>

## 126.57 `CONFIG_MODEM_HL78XX_AIRVANTAGE_SESSION_INITIATION`

**提示（Prompt）**：AirVantage 初始化（Initialization）

**说明（Help）**

选择此设置，以允许 HL78xx 模块连接 AirVantage 设备管理（DM）服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AIRVANTAGE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_AIRVANTAGE_HOST_INITIATED
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_AIRVANTAGE_HOST_INITIATED
CONFIG_MODEM_HL78XX_AIRVANTAGE_MODULE_INITIATED
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1460`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1460)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AirVantage

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AIRVANTAGE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_AIRVANTAGE_HOST_INITIATED`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE_HOST_INITIATED)、[`CONFIG_MODEM_HL78XX_AIRVANTAGE_MODULE_INITIATED`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE_MODULE_INITIATED)。

<a id="CONFIG_MODEM_HL78XX_AIRVANTAGE_UA_CONNECT_AIRVANTAGE"></a>

## 126.58 `CONFIG_MODEM_HL78XX_AIRVANTAGE_UA_CONNECT_AIRVANTAGE`

**提示（Prompt）**：连接 AirVantage

**说明（Help）**

模块请求用户／应用连接 AirVantage。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT && CONFIG_MODEM_HL78XX_AIRVANTAGE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1488`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1488)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AirVantage → 用户同意机制启用（User Agreement Activation）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT)、[`CONFIG_MODEM_HL78XX_AIRVANTAGE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AIRVANTAGE_UA_DOWNLOAD_FIRMWARE"></a>

## 126.59 `CONFIG_MODEM_HL78XX_AIRVANTAGE_UA_DOWNLOAD_FIRMWARE`

**提示（Prompt）**：下载固件（Download Firmware）

**说明（Help）**

AirVantage 请求设备下载固件包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT && CONFIG_MODEM_HL78XX_AIRVANTAGE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1493`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1493)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AirVantage → 用户同意机制启用（User Agreement Activation）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT)、[`CONFIG_MODEM_HL78XX_AIRVANTAGE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AIRVANTAGE_UA_INSTALL_FIRMWARE"></a>

## 126.60 `CONFIG_MODEM_HL78XX_AIRVANTAGE_UA_INSTALL_FIRMWARE`

**提示（Prompt）**：安装固件（Install Firmware）

**说明（Help）**

AirVantage 请求设备安装已下载的固件包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT && CONFIG_MODEM_HL78XX_AIRVANTAGE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1498`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1498)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AirVantage → 用户同意机制启用（User Agreement Activation）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT)、[`CONFIG_MODEM_HL78XX_AIRVANTAGE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT"></a>

## 126.61 `CONFIG_MODEM_HL78XX_AIRVANTAGE_USER_AGREEMENT`

**提示（Prompt）**：用户同意机制启用（User Agreement Activation）

**说明（Help）**

启用用户同意机制（User Agreements）后，主机处理器应用可控制固件空中升级（FOTA）流程。例如，主机正在执行服务，如车辆运行或支付交易进行中时，可决定推迟固件下载或安装，因为接受固件安装会导致嵌入式模块在 FOTA 完成后重启。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AIRVANTAGE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1478`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1478)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → AirVantage

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AIRVANTAGE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AIRVANTAGE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_APN"></a>

## 126.62 `CONFIG_MODEM_HL78XX_APN`

**提示（Prompt）**：用于建立网络连接的接入点名称（APN）

**说明（Help）**

此设置用于 `AT+CGDCONT` 命令，为网络连接上下文设置 APN 名称。此值取决于网络提供商，必须相应更改。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_APN_SOURCE_KCONFIG && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"xxxxxxxx"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:743`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L743)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_APN_SOURCE_KCONFIG`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE_KCONFIG)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_APN_PROFILES"></a>

## 126.63 `CONFIG_MODEM_HL78XX_APN_PROFILES`

**提示（Prompt）**：自动检测 APN 时搜索的配置文件列表（Profiles）

**说明（Help）**

设置以逗号分隔的配置文件列表，每项包含以下形式之一：

```text
<apn>=<IMSI_1> ... <IMSI_n>
<apn>=<ICCID_1> ... <ICCID_n>
```

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
(CONFIG_MODEM_HL78XX_APN_SOURCE_ICCID || CONFIG_MODEM_HL78XX_APN_SOURCE_IMSI) && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"hologram=23450, wm=20601, int=29505"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:755`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L755)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_APN_SOURCE_ICCID`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE_ICCID)、[`CONFIG_MODEM_HL78XX_APN_SOURCE_IMSI`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE_IMSI)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_APN_SOURCE"></a>

## 126.64 `CONFIG_MODEM_HL78XX_APN_SOURCE`

**提示（Prompt）**：APN 来源（Source）

**说明（Help）**

选择自动检测 APN 的来源。可选择国际移动用户识别码（International Mobile Subscriber Identity，IMSI）或集成电路卡标识符（Integrated Circuit Card Identifier，ICCID）作为关联 APN 的依据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_HL78XX_APN_SOURCE_NETWORK
```

**可选项（Choices）**

```text
CONFIG_MODEM_HL78XX_APN_SOURCE_ICCID
CONFIG_MODEM_HL78XX_APN_SOURCE_IMSI
CONFIG_MODEM_HL78XX_APN_SOURCE_KCONFIG
CONFIG_MODEM_HL78XX_APN_SOURCE_NETWORK
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:706`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L706)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_APN_SOURCE_NETWORK`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE_NETWORK)、[`CONFIG_MODEM_HL78XX_APN_SOURCE_ICCID`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE_ICCID)、[`CONFIG_MODEM_HL78XX_APN_SOURCE_IMSI`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE_IMSI)、[`CONFIG_MODEM_HL78XX_APN_SOURCE_KCONFIG`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE_KCONFIG)。

<a id="CONFIG_MODEM_HL78XX_APN_SOURCE_ICCID"></a>

## 126.65 `CONFIG_MODEM_HL78XX_APN_SOURCE_ICCID`

**提示（Prompt）**：CCID 关联的 APN

**说明（Help）**

- 使用 `AT+CCID`。
- 可在 APN PROFILE 配置中保存多组 ICCID 与 APN 组合，参见 `MODEM_HL78XX_APN_PROFILES`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_APN_SOURCE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:714`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L714)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → APN 来源（Source）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_APN_SOURCE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE)。

<a id="CONFIG_MODEM_HL78XX_APN_SOURCE_IMSI"></a>

## 126.66 `CONFIG_MODEM_HL78XX_APN_SOURCE_IMSI`

**提示（Prompt）**：CIMI 关联的 APN

**说明（Help）**

- 使用 `AT+CIMI`。
- 可在 APN PROFILE 配置中保存多组 CIMI 与 APN 组合，参见 `MODEM_HL78XX_APN_PROFILES`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_APN_SOURCE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:721`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L721)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → APN 来源（Source）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_APN_SOURCE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE)。

<a id="CONFIG_MODEM_HL78XX_APN_SOURCE_KCONFIG"></a>

## 126.67 `CONFIG_MODEM_HL78XX_APN_SOURCE_KCONFIG`

**提示（Prompt）**：用户定义的单个 APN

**说明（Help）**

- 使用 `MODEM_HL78XX_APN` 中定义的 APN。
- 仅支持一个 APN。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_APN_SOURCE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:728`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L728)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → APN 来源（Source）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_APN_SOURCE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE)。

<a id="CONFIG_MODEM_HL78XX_APN_SOURCE_NETWORK"></a>

## 126.68 `CONFIG_MODEM_HL78XX_APN_SOURCE_NETWORK`

**提示（Prompt）**：网络提供的 APN

**说明（Help）**

- 使用 `AT+CGCONTRDP=1`。
- 使用网络提供的 APN。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_HL78XX_APN_SOURCE>
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:734`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L734)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → APN 来源（Source）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_APN_SOURCE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_APN_SOURCE)。

<a id="CONFIG_MODEM_HL78XX_AT_SHELL"></a>

## 126.69 `CONFIG_MODEM_HL78XX_AT_SHELL`

**提示（Prompt）**：AT 命令行（AT Command Shell）

**说明（Help）**

为调制解调器启用 AT 命令 Shell。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTOBAUD_AT_BOOT"></a>

## 126.70 `CONFIG_MODEM_HL78XX_AUTOBAUD_AT_BOOT`

**提示（Prompt）**：启动时自动检测波特率（Auto Baud Rate Detection），跳过 KSUP 等待

**说明（Help）**

启用后，驱动在调制解调器上电后立即自动检测波特率，不等待 KSUP 主动结果码（URC，即启动就绪指示）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTO_BAUDRATE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTOBAUD_CHANGE_PERSISTENT"></a>

## 126.71 `CONFIG_MODEM_HL78XX_AUTOBAUD_CHANGE_PERSISTENT`

**提示（Prompt）**：持久保存检测到的波特率（Persistently Save）

**说明（Help）**

启用此选项，将配置保存到调制解调器非易失性存储器（Non-volatile Memory）；否则断电重启后会恢复之前的设置。原文强烈建议启用，以检测意外的调制解调器重启并快速恢复。波特率更改会跨电源周期永久保留。注意：更改电话功能（`AT+CFUN`）会将波特率重置为默认值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTO_BAUDRATE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTOBAUD_DETECTION_BAUDRATES"></a>

## 126.72 `CONFIG_MODEM_HL78XX_AUTOBAUD_DETECTION_BAUDRATES`

**提示（Prompt）**：自动检测时尝试的波特率，以逗号分隔

**说明（Help）**

自动检测调制解调器当前波特率时，要依次尝试的波特率列表，以逗号分隔。驱动按顺序尝试，直到成功通信。常见波特率为 9600、19200、38400、57600 和 115200。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"115200,9600,57600,38400,19200"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L183)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTO_BAUDRATE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL"></a>

## 126.73 `CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL`

**提示（Prompt）**：仅在通信失败时自动检测波特率

**说明（Help）**

启用后，仅当最初以配置的目标波特率与调制解调器进行 UART 通信失败时，才自动检测波特率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTO_BAUDRATE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTOBAUD_RETRY_COUNT"></a>

## 126.74 `CONFIG_MODEM_HL78XX_AUTOBAUD_RETRY_COUNT`

**提示（Prompt）**：波特率检测重试次数（Retries）

**说明（Help）**

放弃前重试波特率检测的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTO_BAUDRATE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE"></a>

## 126.75 `CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE`

**提示（Prompt）**：从目标波特率开始自动检测

**说明（Help）**

启用后，自动波特率检测首先尝试以配置的目标波特率通信。若调制解调器已设为该波特率，可加快检测。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTO_BAUDRATE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTOBAUD_TIMEOUT"></a>

## 126.76 `CONFIG_MODEM_HL78XX_AUTOBAUD_TIMEOUT`

**提示（Prompt）**：每次波特率检测尝试的超时，单位为秒

**说明（Help）**

自动检测时，尝试某个特定波特率后等待调制解调器响应的最长时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 120]
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动波特率检测与切换（Detection and Switching）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTO_BAUDRATE)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTORAT"></a>

## 126.77 `CONFIG_MODEM_HL78XX_AUTORAT`

**提示（Prompt）**：自动切换无线接入技术（RAT）并设置首选列表（PRL）配置

**说明（Help）**

`AT+KSRAT` 仅为向后兼容而提供。原文建议使用 `AT+KSELACQ` 切换 RAT，详情参见 RAT Switching Application Note（文档号 2174296）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:778`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L778)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTORAT_M1_BAND_CFG"></a>

## 126.78 `CONFIG_MODEM_HL78XX_AUTORAT_M1_BAND_CFG`

**提示（Prompt）**：Cat-M1 频段配置，以逗号分隔的列表

**说明（Help）**

使用自动 RAT 时，指定 Cat-M1 使用的 LTE 频段，例如 `3,5,12`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTORAT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"1,2,3,4,5,8,12,13,20,28"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:808`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L808)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动切换无线接入技术（RAT）并设置首选列表（PRL）配置

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTORAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTORAT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTORAT_NB_BAND_CFG"></a>

## 126.79 `CONFIG_MODEM_HL78XX_AUTORAT_NB_BAND_CFG`

**提示（Prompt）**：NB-IoT 频段配置，以逗号分隔的列表

**说明（Help）**

使用自动 RAT 时，指定 NB-IoT 使用的 LTE 频段，例如 `8,20,28`。此字符串在运行时或构建时解析。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTORAT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"1,2,3,4,5,8,12,13,20,28"
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:801`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L801)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动切换无线接入技术（RAT）并设置首选列表（PRL）配置

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTORAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTORAT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTORAT_OVER_WRITE_PRL"></a>

## 126.80 `CONFIG_MODEM_HL78XX_AUTORAT_OVER_WRITE_PRL`

**提示（Prompt）**：每次启动始终覆盖 PRL 配置

**说明（Help）**

启用后，应用每次启动都会用自己的 PRL 配置值覆盖调制解调器中的 PRL 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTORAT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:787`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L787)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动切换无线接入技术（RAT）并设置首选列表（PRL）配置

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTORAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTORAT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_AUTORAT_PRL_PROFILES"></a>

## 126.81 `CONFIG_MODEM_HL78XX_AUTORAT_PRL_PROFILES`

**提示（Prompt）**：配置首选无线接入技术列表（Preferred Radio Access Technology List）

**说明（Help）**

以下为原文给出的型号与接入技术顺序：

```text
AT+KSELACQ=0,1,2,3 , MODEM HL7812,CAT-M1, NB-IoT, GSM
AT+KSELACQ=0,1,2,1 , MODEM HL7800,CAT-M1, NB-IoT, CAT-M1
```

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_AUTORAT && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
"1,2,3" if CONFIG_MODEM_HL78XX_12
"1,2,1" if CONFIG_MODEM_HL78XX_00
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:793`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L793)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 自动切换无线接入技术（RAT）并设置首选列表（PRL）配置

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_AUTORAT`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_AUTORAT)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_12`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_12)、[`CONFIG_MODEM_HL78XX_00`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX_00)。

<a id="CONFIG_MODEM_HL78XX_AUTO_BAUDRATE"></a>

## 126.82 `CONFIG_MODEM_HL78XX_AUTO_BAUDRATE`

**提示（Prompt）**：自动波特率检测与切换（Detection and Switching）

**说明（Help）**

启用 HL78xx 调制解调器的自动波特率检测与切换。驱动会尝试检测当前波特率，然后通过 `AT+IPR` 命令切换到配置的目标波特率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**主动选择（Selects）**

```text
CONFIG_UART_USE_RUNTIME_CONFIGURE if CONFIG_SOC_SERIES_NRF52
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)。

<a id="CONFIG_MODEM_HL78XX_BAND_1"></a>

## 126.83 `CONFIG_MODEM_HL78XX_BAND_1`

**提示（Prompt）**：频段（Band）1：2000 MHz

**说明（Help）**

启用频段 1：2000 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:869`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L869)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_10"></a>

## 126.84 `CONFIG_MODEM_HL78XX_BAND_10`

**提示（Prompt）**：频段 10：2100 MHz

**说明（Help）**

启用频段 10：2100 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:910`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L910)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_106"></a>

## 126.85 `CONFIG_MODEM_HL78XX_BAND_106`

**提示（Prompt）**：频段 106：900 MHz

**说明（Help）**

启用频段 106：900 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1014`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1014)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_107"></a>

## 126.86 `CONFIG_MODEM_HL78XX_BAND_107`

**提示（Prompt）**：频段 107：1800 MHz

**说明（Help）**

启用频段 107：1800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1019`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1019)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_12"></a>

## 126.87 `CONFIG_MODEM_HL78XX_BAND_12`

**提示（Prompt）**：频段 12：700 MHz

**说明（Help）**

启用频段 12：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:915`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L915)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_13"></a>

## 126.88 `CONFIG_MODEM_HL78XX_BAND_13`

**提示（Prompt）**：频段 13：700 MHz

**说明（Help）**

启用频段 13：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:921`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L921)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_17"></a>

## 126.89 `CONFIG_MODEM_HL78XX_BAND_17`

**提示（Prompt）**：频段 17：700 MHz

**说明（Help）**

启用频段 17：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:927`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L927)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_18"></a>

## 126.90 `CONFIG_MODEM_HL78XX_BAND_18`

**提示（Prompt）**：频段 18：800 MHz

**说明（Help）**

启用频段 18：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:932`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L932)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_19"></a>

## 126.91 `CONFIG_MODEM_HL78XX_BAND_19`

**提示（Prompt）**：频段 19：800 MHz

**说明（Help）**

启用频段 19：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:937`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L937)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_2"></a>

## 126.92 `CONFIG_MODEM_HL78XX_BAND_2`

**提示（Prompt）**：频段（Band）2：1900 MHz

**说明（Help）**

启用频段 2：1900 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:875`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L875)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_20"></a>

## 126.93 `CONFIG_MODEM_HL78XX_BAND_20`

**提示（Prompt）**：频段 20：800 MHz

**说明（Help）**

启用频段 20：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:942`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L942)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_23"></a>

## 126.94 `CONFIG_MODEM_HL78XX_BAND_23`

**提示（Prompt）**：频段 23：2000 MHz

**说明（Help）**

启用频段 23：2000 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if CONFIG_MODEM_HL78XX_RAT_NBNTN
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:950`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L950)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)。

<a id="CONFIG_MODEM_HL78XX_BAND_25"></a>

## 126.95 `CONFIG_MODEM_HL78XX_BAND_25`

**提示（Prompt）**：频段 25：1900 MHz

**说明（Help）**

启用频段 25：1900 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:958`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L958)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_255"></a>

## 126.96 `CONFIG_MODEM_HL78XX_BAND_255`

**提示（Prompt）**：频段 255：1500 MHz

**说明（Help）**

启用频段 255：1500 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if CONFIG_MODEM_HL78XX_RAT_NBNTN
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1026`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1026)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)。

<a id="CONFIG_MODEM_HL78XX_BAND_256"></a>

## 126.97 `CONFIG_MODEM_HL78XX_BAND_256`

**提示（Prompt）**：频段 256：2000 MHz

**说明（Help）**

启用频段 256：2000 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y if CONFIG_MODEM_HL78XX_RAT_NBNTN
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:1032`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L1032)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)。

<a id="CONFIG_MODEM_HL78XX_BAND_26"></a>

## 126.98 `CONFIG_MODEM_HL78XX_BAND_26`

**提示（Prompt）**：频段 26：800 MHz

**说明（Help）**

启用频段 26：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:963`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L963)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_27"></a>

## 126.99 `CONFIG_MODEM_HL78XX_BAND_27`

**提示（Prompt）**：频段 27：800 MHz

**说明（Help）**

启用频段 27：800 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:968`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L968)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<a id="CONFIG_MODEM_HL78XX_BAND_28"></a>

## 126.100 `CONFIG_MODEM_HL78XX_BAND_28`

**提示（Prompt）**：频段 28：700 MHz

**说明（Help）**

启用频段 28：700 MHz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MODEM_HL78XX_RAT_NBNTN && CONFIG_MODEM_HL78XX_CONFIGURE_BANDS && CONFIG_MODEM_HL78XX && CONFIG_MODEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx:973`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/vendor_standalone/hl78xx/Kconfig.hl78xx#L973)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → HL78XX 调制解调器驱动【实验性（EXPERIMENTAL）】 → 配置调制解调器频段（Modem Bands）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_HL78XX_RAT_NBNTN`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_RAT_NBNTN)、[`CONFIG_MODEM_HL78XX_CONFIGURE_BANDS`](P127_drivers_modem_配置项参考_3.md#CONFIG_MODEM_HL78XX_CONFIGURE_BANDS)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)。

<!-- kconfig-navigation -->

[上一章](P125_drivers_modem_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P127_drivers_modem_配置项参考_3.md)
