---
id: learning.zephyr-docs.kconfig-reference.page-61
title: "`drivers/charger`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第61章\_`drivers/charger`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/charger` 的 21 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CHARGER"></a>

## 61.1 `CONFIG_CHARGER`

**提示（Prompt）**：电池充电器驱动（Battery Charger Drivers）

**说明（Help）**

启用电池充电器（Battery Charger）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/charger/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_CHARGER_ADP5360"></a>

## 61.2 `CONFIG_CHARGER_ADP5360`

**提示（Prompt）**：ADI ADP5360 电池充电器驱动（Battery Charger Driver）

**说明（Help）**

启用 ADI ADP5360 电池充电器（Battery Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADP5360_CHARGER_ENABLED && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/charger/Kconfig.adp5360:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.adp5360#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_CHARGER_ADP5360_INIT_PRIORITY"></a>

## 61.3 `CONFIG_CHARGER_ADP5360_INIT_PRIORITY`

**提示（Prompt）**：ADP5360 充电器初始化优先级（Charger Init Priority）

**说明（Help）**

亚德诺（Analog Devices）ADP5360 充电器子系统（Charger Subsystem）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CHARGER_ADP5360 && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
89
```

**定义位置（Location）**：[`drivers/charger/Kconfig.adp5360:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.adp5360#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → ADI ADP5360 电池充电器驱动（Battery Charger Driver）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER_ADP5360`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_ADP5360)、[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)。

<a id="CONFIG_CHARGER_AXP2101"></a>

## 61.4 `CONFIG_CHARGER_AXP2101`

**提示（Prompt）**：芯智汇 AXP2101 PMIC 充电器驱动（X-Powers Charger Driver）

**说明（Help）**

启用 AXP2101 电源管理集成电路（PMIC）的充电器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_X_POWERS_AXP2101_CHARGER_ENABLED && DT_HAS_X_POWERS_AXP2101_ENABLED && CONFIG_CHARGER
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

**定义位置（Location）**：[`drivers/charger/Kconfig.axp2101:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.axp2101#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_CHARGER_BQ24190"></a>

## 61.5 `CONFIG_CHARGER_BQ24190`

**提示（Prompt）**：BQ24190 电池充电器（Battery Charger）

**说明（Help）**

启用基于 I2C 的 TI BQ24190 电池充电器（Battery Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_BQ24190_ENABLED && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/charger/Kconfig.bq24190:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.bq24190#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_CHARGER_BQ2429X"></a>

## 61.6 `CONFIG_CHARGER_BQ2429X`

**提示（Prompt）**：BQ2429X 电池充电器（Battery Charger）

**说明（Help）**

启用 TI BQ2429X 电池充电器（Battery Charger）驱动。支持的器件包括 BQ24295、BQ24296、BQ24296M、BQ24297 和 BQ24298。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_BQ24295_ENABLED || DT_HAS_TI_BQ24296_ENABLED || DT_HAS_TI_BQ24296M_ENABLED || DT_HAS_TI_BQ24297_ENABLED || DT_HAS_TI_BQ24298_ENABLED) && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/charger/Kconfig.bq2429x:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.bq2429x#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_CHARGER_BQ2518X"></a>

## 61.7 `CONFIG_CHARGER_BQ2518X`

**提示（Prompt）**：BQ2518x 电池充电器（Battery Charger）

**说明（Help）**

启用 BQ2518x 电池充电器（Battery Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_BQ25180_ENABLED || DT_HAS_TI_BQ25186_ENABLED || DT_HAS_TI_BQ25188_ENABLED) && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/charger/Kconfig.bq2518x:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.bq2518x#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_CHARGER_BQ25713"></a>

## 61.8 `CONFIG_CHARGER_BQ25713`

**提示（Prompt）**：BQ25713 电池充电器（Battery Charger）

**说明（Help）**

启用 BQ25713 电池充电器（Battery Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_BQ25713_ENABLED && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/charger/Kconfig.bq25713:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.bq25713#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_CHARGER_DISCHARGE_CURRENT_NOTIFICATIONS"></a>

## 61.9 `CONFIG_CHARGER_DISCHARGE_CURRENT_NOTIFICATIONS`

**提示（Prompt）**：放电电流通知支持（Discharge Current Notifications）

**说明（Help）**

启用放电电流通知（Discharge Current Notification）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CHARGER_HAS_DISCHARGE_CURRENT_NOTIFICATIONS && CONFIG_CHARGER
```

**定义位置（Location）**：[`drivers/charger/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → 放电电流通知（Discharge Current Notifications）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER_HAS_DISCHARGE_CURRENT_NOTIFICATIONS`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_HAS_DISCHARGE_CURRENT_NOTIFICATIONS)、[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)。

<a id="CONFIG_CHARGER_GPIO"></a>

## 61.10 `CONFIG_CHARGER_GPIO`

**提示（Prompt）**：GPIO 控制的电池充电器（Battery Charger）

**说明（Help）**

启用 GPIO 电池充电器（Battery Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_CHARGER_GPIO_ENABLED && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/charger/Kconfig.gpio:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.gpio#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_CHARGER_HAS_DISCHARGE_CURRENT_NOTIFICATIONS"></a>

## 61.11 `CONFIG_CHARGER_HAS_DISCHARGE_CURRENT_NOTIFICATIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果充电器支持放电电流通知（Discharge Current Notifications），此符号为 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CHARGER
```

**定义位置（Location）**：[`drivers/charger/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)。

<a id="CONFIG_CHARGER_HAS_SYSTEM_VOLTAGE_NOTIFICATIONS"></a>

## 61.12 `CONFIG_CHARGER_HAS_SYSTEM_VOLTAGE_NOTIFICATIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果充电器支持系统电压通知（System Voltage Notifications），此符号为 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CHARGER
```

**定义位置（Location）**：[`drivers/charger/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)。

<a id="CONFIG_CHARGER_INIT_PRIORITY"></a>

## 61.13 `CONFIG_CHARGER_INIT_PRIORITY`

**提示（Prompt）**：电池充电器初始化优先级（Battery Charger Init Priority）

**说明（Help）**

电池充电器（Battery Charger）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CHARGER
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/charger/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)。

<a id="CONFIG_CHARGER_MAX20335"></a>

## 61.14 `CONFIG_CHARGER_MAX20335`

**提示（Prompt）**：MAX20335 电池充电器驱动（Battery Charger Driver）

**说明（Help）**

启用 MAX20335 电池充电器（Battery Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX20335_CHARGER_ENABLED && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_I2C
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/charger/Kconfig.max20335:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.max20335#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_CHARGER_NPM10XX"></a>

## 61.15 `CONFIG_CHARGER_NPM10XX`

**提示（Prompt）**：nPM10xx 电池充电器驱动（Battery Charger Driver）

**说明（Help）**

启用 nPM10xx 充电器（Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM10XX_CHARGER_ENABLED && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/charger/Kconfig.npm10xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.npm10xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_CHARGER_PCA9422"></a>

## 61.16 `CONFIG_CHARGER_PCA9422`

**提示（Prompt）**：PCA9422 电池充电器驱动（Battery Charger Driver）

**说明（Help）**

启用 PCA9422 电池充电器（Battery Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PCA9422_CHARGER_ENABLED && CONFIG_CHARGER
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

**定义位置（Location）**：[`drivers/charger/Kconfig.pca9422:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.pca9422#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_CHARGER_PF1550"></a>

## 61.17 `CONFIG_CHARGER_PF1550`

**提示（Prompt）**：恩智浦 PF1550 电池充电器驱动（NXP Battery Charger Driver）

**说明（Help）**

启用恩智浦（NXP）PF1550 电池充电器（Battery Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PF1550_CHARGER_ENABLED && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_I2C
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/charger/Kconfig.pf1550:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.pf1550#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_CHARGER_SY6974B"></a>

## 61.18 `CONFIG_CHARGER_SY6974B`

**提示（Prompt）**：矽力杰 SY6974B 电池充电器（Silergy Battery Charger）

**说明（Help）**

启用矽力杰（Silergy）SY6974B 的 I2C 驱动。该器件是 3A 单节锂离子开关式电池充电器（Single-Cell Li-Ion Switching Battery Charger）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILERGY_SY6974B_ENABLED && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/charger/Kconfig.sy6974b:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.sy6974b#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_CHARGER_SYSTEM_VOLTAGE_NOTIFICATIONS"></a>

## 61.19 `CONFIG_CHARGER_SYSTEM_VOLTAGE_NOTIFICATIONS`

**提示（Prompt）**：系统电压通知支持（System Voltage Notifications）

**说明（Help）**

启用系统电压通知（System Voltage Notifications）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CHARGER_HAS_SYSTEM_VOLTAGE_NOTIFICATIONS && CONFIG_CHARGER
```

**定义位置（Location）**：[`drivers/charger/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → 系统电压通知（System Voltage Notification）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER_HAS_SYSTEM_VOLTAGE_NOTIFICATIONS`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER_HAS_SYSTEM_VOLTAGE_NOTIFICATIONS)、[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)。

<a id="CONFIG_EMUL_SBS_CHARGER"></a>

## 61.20 `CONFIG_EMUL_SBS_CHARGER`

**提示（Prompt）**：仿真符合 SBS 1.1 的智能电池充电器（Smart Battery Charger）

**说明（Help）**

提供遵循简单序列的读数（Readings），使测试代码能够检查功能是否按预期工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_SBS_CHARGER && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/charger/Kconfig.sbs_charger:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.sbs_charger#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers） → 智能电池充电器（Smart Battery Charger）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SBS_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_SBS_CHARGER)、[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)。

<a id="CONFIG_SBS_CHARGER"></a>

## 61.21 `CONFIG_SBS_CHARGER`

**提示（Prompt）**：智能电池充电器（Smart Battery Charger）

**说明（Help）**

启用基于 I2C／系统管理总线（SMBus）的智能电池充电器（Smart Battery Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SBS_SBS_CHARGER_ENABLED && CONFIG_CHARGER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/charger/Kconfig.sbs_charger:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/Kconfig.sbs_charger#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池充电器驱动（Battery Charger Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CHARGER`](P061_drivers_charger_配置项参考.md#CONFIG_CHARGER)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<!-- kconfig-navigation -->

[上一章](P060_drivers_can_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P062_drivers_clock_control_配置项参考_1.md)
