---
id: learning.zephyr-docs.kconfig-reference.page-96
title: "`drivers/fuel_gauge`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第96章\_`drivers/fuel_gauge`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/fuel_gauge` 的 22 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BQ27Z746"></a>

## 96.1 `CONFIG_BQ27Z746`

**提示（Prompt）**：BQ27Z746 电量计（Fuel Gauge）

**说明（Help）**

启用基于 I2C 的 BQ27Z746 电量计（Fuel Gauge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_BQ27Z746_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/fuel_gauge/bq27z746/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/bq27z746/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_BQ40Z50"></a>

## 96.2 `CONFIG_BQ40Z50`

**提示（Prompt）**：BQ40Z50 电量计（Fuel Gauge）

**说明（Help）**

启用基于 I2C 的 BQ40Z50 电量计（Fuel Gauge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_BQ40Z50_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/fuel_gauge/bq40z50/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/bq40z50/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_EMUL_BQ27Z746"></a>

## 96.3 `CONFIG_EMUL_BQ27Z746`

**提示（Prompt）**：仿真 BQ27Z746 电量计（Emulate Fuel Gauge）

**说明（Help）**

按简单序列提供读数（Readings），使测试代码能够检查行为是否符合预期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_BQ27Z746 && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/fuel_gauge/bq27z746/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/bq27z746/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → BQ27Z746 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_BQ27Z746`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_BQ27Z746)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_EMUL_BQ40Z50"></a>

## 96.4 `CONFIG_EMUL_BQ40Z50`

**提示（Prompt）**：仿真 BQ40Z50 电量计（Emulate Fuel Gauge）

**说明（Help）**

按简单序列提供读数（Readings），使测试代码能够检查行为是否符合预期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_BQ40Z50 && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/fuel_gauge/bq40z50/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/bq40z50/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → BQ40Z50 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_BQ40Z50`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_BQ40Z50)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_EMUL_LC709203F"></a>

## 96.5 `CONFIG_EMUL_LC709203F`

**提示（Prompt）**：仿真 LC709203F 电量计（Emulate Fuel Gauge）

**说明（Help）**

按简单序列提供读数（Readings），使测试代码能够检查行为是否符合预期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_LC709203F && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/fuel_gauge/lc709203f/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/lc709203f/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → LC709203F 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_LC709203F`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_LC709203F)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_EMUL_LTC2959"></a>

## 96.6 `CONFIG_EMUL_LTC2959`

**提示（Prompt）**：仿真 LTC2959 电量计（Emulate Fuel Gauge）

**说明（Help）**

按简单序列提供读数（Readings），使测试代码能够检查行为是否符合预期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_FUEL_GAUGE_LTC2959 && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/fuel_gauge/ltc2959/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/ltc2959/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → LTC2959 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_FUEL_GAUGE_LTC2959`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE_LTC2959)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_EMUL_MAX17048"></a>

## 96.7 `CONFIG_EMUL_MAX17048`

**提示（Prompt）**：仿真 MAX17048 电量计（Emulate Fuel Gauge）

**说明（Help）**

按简单序列提供读数（Readings），使测试代码能够检查行为是否符合预期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_MAX17048 && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/fuel_gauge/max17048/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/max17048/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → MAX17048 锂聚合物电池电量计（Li-Po Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_MAX17048`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_MAX17048)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_EMUL_SBS_GAUGE"></a>

## 96.8 `CONFIG_EMUL_SBS_GAUGE`

**提示（Prompt）**：仿真符合 SBS 1.1 的智能电池电量计（Smart Battery Fuel Gauge）

**说明（Help）**

按简单序列提供读数（Readings），使测试代码能够检查行为是否符合预期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && (CONFIG_SBS_GAUGE_NEW_API || CONFIG_SBS_GAUGE) && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/fuel_gauge/sbs_gauge/Kconfig.emul_sbs_gauge:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/sbs_gauge/Kconfig.emul_sbs_gauge#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SBS_GAUGE_NEW_API`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_SBS_GAUGE_NEW_API)、[`CONFIG_SBS_GAUGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SBS_GAUGE)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_EMUL_SY24561"></a>

## 96.9 `CONFIG_EMUL_SY24561`

**提示（Prompt）**：仿真 SY24561 电量计（Emulate Fuel Gauge）

**说明（Help）**

按简单序列提供读数（Readings），使测试代码能够检查行为是否符合预期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_SY24561 && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/fuel_gauge/sy24561/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/sy24561/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → 矽力杰（Silergy）SY24561 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SY24561`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_SY24561)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_FUEL_GAUGE"></a>

## 96.10 `CONFIG_FUEL_GAUGE`

**提示（Prompt）**：电池电量计驱动（Battery Fuel Gauge Drivers）

**说明（Help）**

启用电池电量计（Battery Fuel Gauge）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/fuel_gauge/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_FUEL_GAUGE_ADP5360"></a>

## 96.11 `CONFIG_FUEL_GAUGE_ADP5360`

**提示（Prompt）**：ADP5360 电量计（Fuel Gauge）

**说明（Help）**

启用基于 I2C 的 ADP5360 电量计（Fuel Gauge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADP5360_FUEL_GAUGE_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/fuel_gauge/adp5360/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/adp5360/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_FUEL_GAUGE_ADP5360_INIT_PRIORITY"></a>

## 96.12 `CONFIG_FUEL_GAUGE_ADP5360_INIT_PRIORITY`

**提示（Prompt）**：ADP5360 电量计初始化优先级（Fuel Gauge Init Priority）

**说明（Help）**

Analog Devices ADP5360 电量计子系统（Fuel Gauge Subsystem）的初始化优先级（Init Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FUEL_GAUGE_ADP5360 && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/fuel_gauge/adp5360/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/adp5360/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → ADP5360 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE_ADP5360`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE_ADP5360)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_FUEL_GAUGE_AXP2101"></a>

## 96.13 `CONFIG_FUEL_GAUGE_AXP2101`

**提示（Prompt）**：X-Powers AXP2101 电量计（Fuel Gauge）

**说明（Help）**

启用 X-Powers AXP2101 电量计设备（Fuel Gauge Device）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_X_POWERS_AXP2101_FUEL_GAUGE_ENABLED && DT_HAS_X_POWERS_AXP2101_ENABLED && CONFIG_FUEL_GAUGE
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

**定义位置（Location）**：[`drivers/fuel_gauge/axp2101/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/axp2101/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_FUEL_GAUGE_COMPOSITE"></a>

## 96.14 `CONFIG_FUEL_GAUGE_COMPOSITE`

**提示（Prompt）**：Zephyr 组合电量计（Composite Fuel Gauge）

**说明（Help）**

启用 Zephyr 组合电量计设备（Composite Fuel Gauge Device）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FUEL_GAUGE_COMPOSITE_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/fuel_gauge/composite/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/composite/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_FUEL_GAUGE_COMPOSITE_DATA_VALIDITY_MS"></a>

## 96.15 `CONFIG_FUEL_GAUGE_COMPOSITE_DATA_VALIDITY_MS`

**提示（Prompt）**：`sensor_fetch` 数据的缓存时长（Cache Duration）

**说明（Help）**

为确保多次 `fuel_gauge_get_prop` 调用之间的数据一致性，只有距上一次 `sensor_fetch` 调用至少经过此时长后，才再次调用 `sensor_fetch`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FUEL_GAUGE_COMPOSITE && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
150
```

**定义位置（Location）**：[`drivers/fuel_gauge/composite/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/composite/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → Zephyr 组合电量计（Composite Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE_COMPOSITE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE_COMPOSITE)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_FUEL_GAUGE_INIT_PRIORITY"></a>

## 96.16 `CONFIG_FUEL_GAUGE_INIT_PRIORITY`

**提示（Prompt）**：电池电量计初始化优先级（Battery Fuel Gauge Init Priority）

**说明（Help）**

电池电量计（Battery Fuel Gauge）的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/fuel_gauge/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)。

<a id="CONFIG_FUEL_GAUGE_LTC2959"></a>

## 96.17 `CONFIG_FUEL_GAUGE_LTC2959`

**提示（Prompt）**：LTC2959 电量计（Fuel Gauge）

**说明（Help）**

启用 Analog Devices 的 LTC2959 电量计（Fuel Gauge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_LTC2959_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/fuel_gauge/ltc2959/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/ltc2959/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_HY4245"></a>

## 96.18 `CONFIG_HY4245`

**提示（Prompt）**：HY4245 电量计（Fuel Gauge）

**说明（Help）**

启用基于 I2C 的 HY4245 电量计（Fuel Gauge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HYCON_HY4245_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/fuel_gauge/hy4245/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/hy4245/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_LC709203F"></a>

## 96.19 `CONFIG_LC709203F`

**提示（Prompt）**：LC709203F 电量计（Fuel Gauge）

**说明（Help）**

启用基于 I2C 的 LC709203F 电量计（Fuel Gauge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ONNN_LC709203F_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/fuel_gauge/lc709203f/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/lc709203f/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_MAX17048"></a>

## 96.20 `CONFIG_MAX17048`

**提示（Prompt）**：MAX17048 锂聚合物电池电量计（Li-Po Fuel Gauge）

**说明（Help）**

启用 MAX17048 电量计设备（Fuel Gauge Device）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX17048_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/fuel_gauge/max17048/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/max17048/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_SBS_GAUGE_NEW_API"></a>

## 96.21 `CONFIG_SBS_GAUGE_NEW_API`

**提示（Prompt）**：智能电池电量计（Smart Battery Fuel Gauge）

**说明（Help）**

启用基于 I2C/SMBus 的智能电池电量计（Smart Battery Fuel Gauge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SBS_SBS_GAUGE_NEW_API_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/fuel_gauge/sbs_gauge/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/sbs_gauge/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_SY24561"></a>

## 96.22 `CONFIG_SY24561`

**提示（Prompt）**：矽力杰（Silergy）SY24561 电量计（Fuel Gauge）

**说明（Help）**

启用矽力杰（Silergy）SY24561 电量计设备（Fuel Gauge Device）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILERGY_SY24561_ENABLED && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/fuel_gauge/sy24561/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/fuel_gauge/sy24561/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<!-- kconfig-navigation -->

[上一章](P095_drivers_fpga_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P097_drivers_gnss_配置项参考.md)
