---
id: learning.zephyr-docs.kconfig-reference.page-63
title: "`drivers/clock_control`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第63章\_`drivers/clock_control`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/clock_control` 的 88 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL"></a>

## 63.1 `CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL`

**提示（Prompt）**：全局高速锁频环时钟控制（Global HSFLL Clock Control）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_HSFLL_GLOBAL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFS
CONFIG_NRFS_GDFS_SERVICE_ENABLED
CONFIG_CLOCK_CONTROL_NRF_COMMON
CONFIG_CLOCK_CONTROL_NRF_ONOFF
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L298)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS)、[`CONFIG_NRFS_GDFS_SERVICE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_GDFS_SERVICE_ENABLED)、[`CONFIG_CLOCK_CONTROL_NRF_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_COMMON)、[`CONFIG_CLOCK_CONTROL_NRF_ONOFF`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_ONOFF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_COMMON`。

<a id="CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL_INIT_PRIORITY"></a>

## 63.2 `CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL_INIT_PRIORITY`

**提示（Prompt）**：全局 HSFLL 设备驱动初始化优先级（Init Priority）

**说明（Help）**

必须高于 NRFS 后端（Backend）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
52
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:327`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L327)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 全局高速锁频环时钟控制（Global HSFLL Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL_REQ_LOW_FREQ"></a>

## 63.3 `CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL_REQ_LOW_FREQ`

**提示（Prompt）**：初始化时请求低频（LOW Frequency）

**说明（Help）**

全局动态频率调整（GDFS）服务在收到较低频率请求之前，默认使用高频（HIGH）。NRF2 时钟控制器驱动预期时钟初始化为其最低频率，因此需要在初始化时发送请求，使 GDFS 与 NRF2 驱动的预期一致。

如果某个模块在初始化时无论如何都会请求高频，可禁用此初始请求，避免可能不必要的 `HIGH -> LOW -> HIGH` 切换。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 全局高速锁频环时钟控制（Global HSFLL Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL_TIMEOUT_MS"></a>

## 63.4 `CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL_TIMEOUT_MS`

**提示（Prompt）**：频率请求超时，单位为毫秒（Frequency Request Timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L309)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 全局高速锁频环时钟控制（Global HSFLL Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL"></a>

## 63.5 `CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL`

**提示（Prompt）**：nRF 本地高速锁频环驱动支持（HSFLL LOCAL Driver Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_HSFLL_LOCAL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFS
CONFIG_NRFS_DVFS_LOCAL_DOMAIN
CONFIG_CLOCK_CONTROL_NRF_COMMON
CONFIG_CLOCK_CONTROL_NRF_ONOFF
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:358`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L358)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS)、[`CONFIG_NRFS_DVFS_LOCAL_DOMAIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_DVFS_LOCAL_DOMAIN)、[`CONFIG_CLOCK_CONTROL_NRF_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_COMMON)、[`CONFIG_CLOCK_CONTROL_NRF_ONOFF`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_ONOFF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_COMMON`。

<a id="CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL_NRFS_DVFS_TIMEOUT_MS"></a>

## 63.6 `CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL_NRFS_DVFS_TIMEOUT_MS`

**提示（Prompt）**：等待 NRFS 动态电压与频率调整服务回调的超时，单位为毫秒（DVFS Service Callback Timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L374)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 本地高速锁频环驱动支持（HSFLL LOCAL Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL_REQ_LOW_FREQ"></a>

## 63.7 `CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL_REQ_LOW_FREQ`

**提示（Prompt）**：初始化后降低本地域运行档位（Local Domain Scale Down）

**说明（Help）**

动态电压与频率调整（DVFS）初始化完成后，请求最低运行点（Operating Point）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:369`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L369)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 本地高速锁频环驱动支持（HSFLL LOCAL Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL"></a>

## 63.8 `CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL`

**提示（Prompt）**：nRF IronSide 本地高速锁频环驱动支持（HSFLL LOCAL Driver Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_IRON_HSFLL_LOCAL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_IRONSIDE_SE_DVFS
CONFIG_CLOCK_CONTROL_NRF_COMMON
CONFIG_CLOCK_CONTROL_NRF_ONOFF
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:380`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L380)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_IRONSIDE_SE_DVFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IRONSIDE_SE_DVFS)、[`CONFIG_CLOCK_CONTROL_NRF_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_COMMON)、[`CONFIG_CLOCK_CONTROL_NRF_ONOFF`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_ONOFF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_COMMON`。

<a id="CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL_DVFS_TIMEOUT_MS"></a>

## 63.9 `CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL_DVFS_TIMEOUT_MS`

**提示（Prompt）**：等待动态电压与频率调整请求完成的超时（DVFS Request Timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:395`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L395)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF IronSide 本地高速锁频环驱动支持（HSFLL LOCAL Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL_REQ_LOW_FREQ"></a>

## 63.10 `CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL_REQ_LOW_FREQ`

**提示（Prompt）**：初始化后降低本地域运行档位（Local Domain Scale Down）

**说明（Help）**

动态电压与频率调整（DVFS）初始化完成后，请求最低运行点（Operating Point）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:390`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L390)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF IronSide 本地高速锁频环驱动支持（HSFLL LOCAL Driver Support）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_100PPM"></a>

## 63.11 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_100PPM`

**提示（Prompt）**：76 ppm 到 100 ppm，ppm 表示百万分之一（Parts Per Million）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟精度（Clock Accuracy）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_150PPM"></a>

## 63.12 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_150PPM`

**提示（Prompt）**：101 ppm 到 150 ppm，ppm 表示百万分之一（Parts Per Million）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟精度（Clock Accuracy）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_20PPM"></a>

## 63.13 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_20PPM`

**提示（Prompt）**：0 ppm 到 20 ppm，ppm 表示百万分之一（Parts Per Million）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟精度（Clock Accuracy）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_250PPM"></a>

## 63.14 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_250PPM`

**提示（Prompt）**：151 ppm 到 250 ppm，ppm 表示百万分之一（Parts Per Million）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟精度（Clock Accuracy）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_30PPM"></a>

## 63.15 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_30PPM`

**提示（Prompt）**：21 ppm 到 30 ppm，ppm 表示百万分之一（Parts Per Million）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟精度（Clock Accuracy）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_500PPM"></a>

## 63.16 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_500PPM`

**提示（Prompt）**：251 ppm 到 500 ppm，ppm 表示百万分之一（Parts Per Million）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟精度（Clock Accuracy）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_50PPM"></a>

## 63.17 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_50PPM`

**提示（Prompt）**：31 ppm 到 50 ppm，ppm 表示百万分之一（Parts Per Million）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟精度（Clock Accuracy）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_75PPM"></a>

## 63.18 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_75PPM`

**提示（Prompt）**：51 ppm 到 75 ppm，ppm 表示百万分之一（Parts Per Million）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM>
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟精度（Clock Accuracy）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING"></a>

## 63.19 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING`

**提示（Prompt）**：外部全摆幅（External Full Swing）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF52 && <choice CONFIG_CLOCK_CONTROL_NRF_SOURCE>
```

**主动选择（Selects）**

```text
CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_LF_SRC_FULL_SWING if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟源（Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_CLOCK_CONTROL_NRF_SOURCE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_SOURCE)、[`CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED)、[`CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT)、[`CONFIG_NRFX_CLOCK_LF_SRC_FULL_SWING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_FULL_SWING)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING"></a>

## 63.20 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING`

**提示（Prompt）**：外部低摆幅（External Low Swing）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF52 && <choice CONFIG_CLOCK_CONTROL_NRF_SOURCE>
```

**主动选择（Selects）**

```text
CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_LF_SRC_LOW_SWING if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟源（Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_CLOCK_CONTROL_NRF_SOURCE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_SOURCE)、[`CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED)、[`CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT)、[`CONFIG_NRFX_CLOCK_LF_SRC_LOW_SWING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_LOW_SWING)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_FREQUENCY"></a>

## 63.21 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_FREQUENCY`

**提示（Prompt）**：32k 源时钟频率（Source Clock Frequency）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
32768
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC"></a>

## 63.22 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC`

**提示（Prompt）**：RC 振荡器（RC Oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_SOURCE>
```

**主动选择（Selects）**

```text
CONFIG_NRFX_CLOCK_LF_SRC_RC if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟源（Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_SOURCE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_SOURCE)、[`CONFIG_NRFX_CLOCK_LF_SRC_RC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_RC)、[`CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION"></a>

## 63.23 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION`

**提示（Prompt）**：低频时钟校准（LF Clock Calibration）

**说明（Help）**

使用 RC 作为低频时钟（Low-Frequency Clock）时，如果禁用校准（Calibration），时钟精度会下降。禁用后需自行承担精度下降的后果。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_SYNTH"></a>

## 63.24 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_SYNTH`

**提示（Prompt）**：由高频时钟合成（Synthesized from HFCLK）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_NRF91 && <choice CONFIG_CLOCK_CONTROL_NRF_SOURCE>
```

**主动选择（Selects）**

```text
CONFIG_NRFX_CLOCK_LF_SRC_SYNTH if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟源（Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_CLOCK_CONTROL_NRF_SOURCE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_SOURCE)、[`CONFIG_NRFX_CLOCK_LF_SRC_SYNTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_SYNTH)、[`CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT)。

<a id="CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL"></a>

## 63.25 `CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL`

**提示（Prompt）**：晶体振荡器（Crystal Oscillator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CLOCK_CONTROL_NRF_SOURCE>
```

**主动选择（Selects）**

```text
CONFIG_NRFX_CLOCK_LF_SRC_XTAL if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED if !SOC_SERIES_BSIM_NRFXX && !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］ → 32kHz 时钟源（Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF_SOURCE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_SOURCE)、[`CONFIG_NRFX_CLOCK_LF_SRC_XTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_XTAL)、[`CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT)、[`CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED)。

<a id="CONFIG_CLOCK_CONTROL_NRF_LFRC"></a>

## 63.26 `CONFIG_CLOCK_CONTROL_NRF_LFRC`

**提示（Prompt）**：nRF 低频 RC 振荡器驱动支持（LFRC Driver Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_LFRC_ENABLED && !CONFIG_CLOCK_CONTROL_NRF && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_NRF_COMMON
CONFIG_NRFX_CLOCK_LFRC if !CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_NRF_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_COMMON)、[`CONFIG_NRFX_CLOCK_LFRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LFRC)、[`CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_FORCE_ALT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_COMMON`。

<a id="CONFIG_CLOCK_CONTROL_NRF_ONOFF"></a>

## 63.27 `CONFIG_CLOCK_CONTROL_NRF_ONOFF`

**提示（Prompt）**：开关管理器相关功能（On-Off Manager Functionality）

**说明（Help）**

为 nRF 时钟控制（Clock Control）启用开关管理器（On-Off Manager）相关功能。如果应用不使用该管理器，可以禁用此配置以减小镜像体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ONOFF
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION
CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL
CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL
CONFIG_CLOCK_CONTROL_NRF_FLL16M
CONFIG_CLOCK_CONTROL_NRF54H_HFXO
CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL
CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL
CONFIG_CLOCK_CONTROL_NRFS_LFCLK
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_ONOFF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ONOFF)、[`CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION)、[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL)、[`CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL)、[`CONFIG_CLOCK_CONTROL_NRF_FLL16M`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF_FLL16M)、[`CONFIG_CLOCK_CONTROL_NRF54H_HFXO`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF54H_HFXO)、[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL)、[`CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL)、[`CONFIG_CLOCK_CONTROL_NRFS_LFCLK`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRFS_LFCLK)。

<a id="CONFIG_CLOCK_CONTROL_NRF_SHELL"></a>

## 63.28 `CONFIG_CLOCK_CONTROL_NRF_SHELL`

**提示（Prompt）**：命令行命令（Shell Commands）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_CLOCK_CONTROL_NRF && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NRF_SOURCE"></a>

## 63.29 `CONFIG_CLOCK_CONTROL_NRF_SOURCE`

**提示（Prompt）**：32kHz 时钟源（Clock Source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL
```

**可选项（Choices）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC
CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL
CONFIG_CLOCK_CONTROL_NRF_K32SRC_SYNTH
CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING
CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nrf:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nrf#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → nRF 时钟控制器支持（Clock Controller Support）［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_SYNTH`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_SYNTH)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING)。

<a id="CONFIG_CLOCK_CONTROL_NUMAKER_SCC"></a>

## 63.30 `CONFIG_CLOCK_CONTROL_NUMAKER_SCC`

**提示（Prompt）**：NuMaker 系统时钟控制器驱动（System Clock Controller Driver）

**说明（Help）**

启用 NuMaker 系统时钟控制器（System Clock Controller）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_SCC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NUMICRO_M4_SCC"></a>

## 63.31 `CONFIG_CLOCK_CONTROL_NUMICRO_M4_SCC`

**提示（Prompt）**：NuMicro 系统时钟控制器驱动（System Clock Controller Driver）

**说明（Help）**

启用 NuMicro M4 系列的系统时钟控制器（System Clock Controller）子系统驱动，目前已在 M487 上测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NUMICRO && DT_HAS_NUVOTON_NUMICRO_M4_SCC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.numaker:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.numaker#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NUMICRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMICRO)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NUMICRO`。

<a id="CONFIG_CLOCK_CONTROL_NXP_MCXW7X"></a>

## 63.32 `CONFIG_CLOCK_CONTROL_NXP_MCXW7X`

**提示（Prompt）**：恩智浦 MCXW7X 时钟控制驱动（NXP Clock Control Driver）

**说明（Help）**

启用恩智浦（NXP）MCXW7X 时钟控制（Clock Control）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCXW7X_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NXP_MC_CGM"></a>

## 63.33 `CONFIG_CLOCK_CONTROL_NXP_MC_CGM`

**提示（Prompt）**：恩智浦 MC_CGM 时钟驱动（NXP Clock Driver）

**说明（Help）**

启用恩智浦（NXP）MC_CGM 时钟（Clock）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MC_CGM_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NXP_S32"></a>

## 63.34 `CONFIG_CLOCK_CONTROL_NXP_S32`

**提示（Prompt）**：恩智浦 S32 时钟控制驱动（NXP Clock Control Driver）

**说明（Help）**

启用恩智浦（NXP）S32 时钟控制（Clock Control）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_NXP_S32_CLOCK_CONFIG_IDX"></a>

## 63.35 `CONFIG_CLOCK_CONTROL_NXP_S32_CLOCK_CONFIG_IDX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

指定初始化片上系统（SoC）时钟时使用的时钟配置（Clock Configuration）索引，从 0 开始编号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NXP_S32 && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.nxp:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.nxp#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 恩智浦 S32 时钟控制驱动（NXP Clock Control Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NXP_S32`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NXP_S32)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_PWM"></a>

## 63.36 `CONFIG_CLOCK_CONTROL_PWM`

**提示（Prompt）**：通用 PWM 时钟（Generic PWM Clock）

**说明（Help）**

启用通用脉宽调制（PWM）时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PWM_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PWM
```

**被选择（Selected by）**

```text
CONFIG_VIDEO_RENESAS_RA_CEU
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.pwm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.pwm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PWM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM)、[`CONFIG_VIDEO_RENESAS_RA_CEU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_RENESAS_RA_CEU)。

<a id="CONFIG_CLOCK_CONTROL_PWM_INIT_PRIORITY"></a>

## 63.37 `CONFIG_CLOCK_CONTROL_PWM_INIT_PRIORITY`

**提示（Prompt）**：PWM 时钟设备初始化优先级（Initialization Priority）

**说明（Help）**

脉宽调制（PWM）时钟设备的初始化优先级，必须低于 PWM 的实际初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_PWM && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.pwm:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.pwm#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 通用 PWM 时钟（Generic PWM Clock）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_PWM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_PWM)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RCAR_CPG_MSSR"></a>

## 63.38 `CONFIG_CLOCK_CONTROL_RCAR_CPG_MSSR`

**提示（Prompt）**：R-Car CPG MSSR 驱动（Driver）

**说明（Help）**

启用瑞萨（Renesas）R-Car CPG MSSR 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RCAR && !CONFIG_SOC_SERIES_RCAR_GEN5 && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RCAR_GEN3
CONFIG_SOC_R8A779F0_R52
CONFIG_SOC_R8A779F0_A55
CONFIG_SOC_R8A779G0_R52
CONFIG_SOC_R8A779G0_A76
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.rcar:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.rcar#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RCAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RCAR)、[`CONFIG_SOC_SERIES_RCAR_GEN5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RCAR_GEN5)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_SERIES_RCAR_GEN3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RCAR_GEN3)、[`CONFIG_SOC_R8A779F0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779F0_R52)、[`CONFIG_SOC_R8A779F0_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779F0_A55)、[`CONFIG_SOC_R8A779G0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779G0_R52)、[`CONFIG_SOC_R8A779G0_A76`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779G0_A76)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RCAR`、`CONFIG_SOC_SERIES_RCAR_GEN3`、`CONFIG_SOC_R8A779G0_R52`、`CONFIG_SOC_R8A779G0_A76`。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RA_CGC"></a>

## 63.39 `CONFIG_CLOCK_CONTROL_RENESAS_RA_CGC`

**提示（Prompt）**：RA 时钟发生电路驱动（CGC Driver）

**说明（Help）**

启用瑞萨（Renesas）RA 时钟发生电路（CGC）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA && CONFIG_HAS_RENESAS_RA_FSP && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RA2L1
CONFIG_SOC_SERIES_RA4C1
CONFIG_SOC_SERIES_RA4E1
CONFIG_SOC_SERIES_RA4E2
CONFIG_SOC_SERIES_RA4L1
CONFIG_SOC_SERIES_RA4M1
CONFIG_SOC_SERIES_RA4M2
CONFIG_SOC_SERIES_RA4M3
CONFIG_SOC_SERIES_RA4T1
CONFIG_SOC_SERIES_RA4W1
CONFIG_SOC_SERIES_RA6E1
CONFIG_SOC_SERIES_RA6E2
CONFIG_SOC_SERIES_RA6M1
CONFIG_SOC_SERIES_RA6M2
CONFIG_SOC_SERIES_RA6M3
CONFIG_SOC_SERIES_RA6M4
CONFIG_SOC_SERIES_RA6M5
CONFIG_SOC_SERIES_RA8D1
CONFIG_SOC_SERIES_RA8D2
CONFIG_SOC_SERIES_RA8E1
CONFIG_SOC_SERIES_RA8M1
CONFIG_SOC_SERIES_RA8M2
CONFIG_SOC_SERIES_RA8P1
CONFIG_SOC_SERIES_RA8T1
CONFIG_SOC_SERIES_RA8T2
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_ra_cgc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_ra_cgc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_HAS_RENESAS_RA_FSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_RENESAS_RA_FSP)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_SERIES_RA4C1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4C1)、[`CONFIG_SOC_SERIES_RA4E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E1)、[`CONFIG_SOC_SERIES_RA4E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4E2)、[`CONFIG_SOC_SERIES_RA4L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SOC_SERIES_RA4M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M2)、[`CONFIG_SOC_SERIES_RA4M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M3)、[`CONFIG_SOC_SERIES_RA4T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4T1)、[`CONFIG_SOC_SERIES_RA4W1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4W1)、[`CONFIG_SOC_SERIES_RA6E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E1)、[`CONFIG_SOC_SERIES_RA6E2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6E2)、[`CONFIG_SOC_SERIES_RA6M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M1)、[`CONFIG_SOC_SERIES_RA6M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M2)、[`CONFIG_SOC_SERIES_RA6M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M3)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA8D1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D1)、[`CONFIG_SOC_SERIES_RA8D2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8D2)、[`CONFIG_SOC_SERIES_RA8E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8E1)、[`CONFIG_SOC_SERIES_RA8M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M1)、[`CONFIG_SOC_SERIES_RA8M2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8M2)、[`CONFIG_SOC_SERIES_RA8P1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8P1)、[`CONFIG_SOC_SERIES_RA8T1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T1)、[`CONFIG_SOC_SERIES_RA8T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA8T2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_SERIES_RA2L1`。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RA_SUBCLK"></a>

## 63.40 `CONFIG_CLOCK_CONTROL_RENESAS_RA_SUBCLK`

**提示（Prompt）**：瑞萨 RA 子时钟源（Renesas Sub Clock Source）

**说明（Help）**

启用瑞萨（Renesas）RA 子时钟（Sub Clock）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_CGC_SUBCLK_ENABLED && CONFIG_CLOCK_CONTROL_RENESAS_RA_CGC && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_ra_cgc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_ra_cgc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → RA 时钟发生电路驱动（CGC Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_RENESAS_RA_CGC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RENESAS_RA_CGC)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC"></a>

## 63.41 `CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC`

**提示（Prompt）**：RX 时钟发生电路驱动（CGC Driver）

**说明（Help）**

启用瑞萨（Renesas）RX 时钟发生电路（CGC）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RX130
CONFIG_SOC_SERIES_RX140
CONFIG_SOC_SERIES_RX14T
CONFIG_SOC_SERIES_RX261
CONFIG_SOC_SERIES_RX26T
CONFIG_SOC_SERIES_RX74M
CONFIG_SOC_SERIES_RX74N
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_rx_cgc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_rx_cgc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_SERIES_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_SERIES_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX140)、[`CONFIG_SOC_SERIES_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX14T)、[`CONFIG_SOC_SERIES_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX261)、[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)、[`CONFIG_SOC_SERIES_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74M)、[`CONFIG_SOC_SERIES_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74N)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RX_PCLK"></a>

## 63.42 `CONFIG_CLOCK_CONTROL_RENESAS_RX_PCLK`

**提示（Prompt）**：瑞萨 RX 根时钟源（Renesas Root Clock Source）

**说明（Help）**

启用瑞萨（Renesas）RX 外设时钟（PCLK）源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_rx_cgc:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_rx_cgc#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → RX 时钟发生电路驱动（CGC Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RX_PLL"></a>

## 63.43 `CONFIG_CLOCK_CONTROL_RENESAS_RX_PLL`

**提示（Prompt）**：瑞萨 RX 锁相环时钟源（Renesas PLL Clock Source）

**说明（Help）**

启用瑞萨（Renesas）RX 锁相环（PLL），仅适用于只有一个 PLL 电路的 RX 微控制器（MCU）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_CGC_PLL_ENABLED && CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_rx_cgc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_rx_cgc#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → RX 时钟发生电路驱动（CGC Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RX_PLLCCR_TYPE"></a>

## 63.44 `CONFIG_CLOCK_CONTROL_RENESAS_RX_PLLCCR_TYPE`

**提示（Prompt）**：使用 FSP 的瑞萨 RX 锁相环时钟源（Renesas PLL Clock Source）

**说明（Help）**

为 PLL 倍频设置使用 `PLLCCR` 索引值（Indexed Values）表示的 RX 微控制器（MCU）启用锁相环（PLL）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_CGC_PLLCCR_TYPE_ENABLED && CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_rx_cgc:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_rx_cgc#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → RX 时钟发生电路驱动（CGC Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RX_ROOT"></a>

## 63.45 `CONFIG_CLOCK_CONTROL_RENESAS_RX_ROOT`

**提示（Prompt）**：瑞萨 RX 根时钟源（Renesas Root Clock Source）

**说明（Help）**

启用瑞萨（Renesas）RX 根时钟（Root Clock）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_CGC_ROOT_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_rx_cgc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_rx_cgc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → RX 时钟发生电路驱动（CGC Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RENESAS_RX_CGC)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RZA2M_CPG"></a>

## 63.46 `CONFIG_CLOCK_CONTROL_RENESAS_RZA2M_CPG`

**提示（Prompt）**：瑞萨 RZ/A2M 时钟控制驱动（Renesas Clock Control Driver）

**说明（Help）**

启用瑞萨（Renesas）RZ/A2M 时钟脉冲发生器（Clock Pulse Generator，CPG）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_CPG_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_rz_cpg:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_rz_cpg#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RZ_CGC"></a>

## 63.47 `CONFIG_CLOCK_CONTROL_RENESAS_RZ_CGC`

**提示（Prompt）**：瑞萨 RZ 时钟控制驱动（Renesas Clock Control Driver）

**说明（Help）**

启用瑞萨（Renesas）RZ 时钟发生电路（Clock Generator Circuit，CGC）驱动支持。CGC 驱动仅支持模块时钟（Module Clocks），不配置锁相环（PLL）和内核时钟（Core Clocks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_CGC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_CGC
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_rz_cgc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_rz_cgc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_USE_RZ_FSP_CGC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_CGC)。

<a id="CONFIG_CLOCK_CONTROL_RENESAS_RZ_CPG"></a>

## 63.48 `CONFIG_CLOCK_CONTROL_RENESAS_RZ_CPG`

**提示（Prompt）**：瑞萨 RZ/G 时钟控制驱动（Renesas Clock Control Driver）

**说明（Help）**

启用瑞萨（Renesas）RZ 时钟脉冲发生器（Clock Pulse Generator，CPG）驱动支持。CPG 驱动仅支持模块时钟（Module Clocks），不配置锁相环（PLL）和内核时钟（Core Clocks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_CPG_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_CPG
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.renesas_rz_cpg:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.renesas_rz_cpg#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_USE_RZ_FSP_CPG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_CPG)。

<a id="CONFIG_CLOCK_CONTROL_ROCKCHIP_RK3588"></a>

## 63.49 `CONFIG_CLOCK_CONTROL_ROCKCHIP_RK3588`

**提示（Prompt）**：瑞芯微 RK3588 CRU 时钟控制器（Rockchip Clock Controller）

**说明（Help）**

启用瑞芯微（Rockchip）RK3588 CRU 的时钟门控（Clock Gate）控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ROCKCHIP_RK3588_CRU_CLK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.rockchip:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.rockchip#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RPI_PICO"></a>

## 63.50 `CONFIG_CLOCK_CONTROL_RPI_PICO`

**提示（Prompt）**：树莓派 Pico 时钟控制器驱动（Raspberry Pi Pico Clock Controller Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_CLOCK_CONTROLLER_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RP2350
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.rpi_pico:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.rpi_pico#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RP2350`。

<a id="CONFIG_CLOCK_CONTROL_RTS5817"></a>

## 63.51 `CONFIG_CLOCK_CONTROL_RTS5817`

**提示（Prompt）**：RTS5817 时钟控制（Clock Control）

**说明（Help）**

启用 RTS5817 时钟控制（Clock Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5817_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.rts5817:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.rts5817#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RTS5912_SCCON"></a>

## 63.52 `CONFIG_CLOCK_CONTROL_RTS5912_SCCON`

**提示（Prompt）**：瑞昱 RTS5912 系统时钟控制器驱动（Realtek System Clock Controller Driver）

**说明（Help）**

启用 RTS5912 系统时钟控制器（System Clock Controller）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RTS5912 && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y if DT_HAS_REALTEK_RTS5912_SCCON_ENABLED
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.rts5912:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.rts5912#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_RV32M1_PCC"></a>

## 63.53 `CONFIG_CLOCK_CONTROL_RV32M1_PCC`

**提示（Prompt）**：RV32M1 PCC 驱动（Driver）

**说明（Help）**

启用 RV32M1 PCC 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_PCC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.rv32m1:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.rv32m1#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SAM"></a>

## 63.54 `CONFIG_CLOCK_CONTROL_SAM`

**提示（Prompt）**：Atmel SAM 时钟控制（Clock Control）

**说明（Help）**

启用 Atmel SAM 时钟控制（Clock Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_PMC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.sam:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.sam#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SAMA7G5"></a>

## 63.55 `CONFIG_CLOCK_CONTROL_SAMA7G5`

**提示（Prompt）**：Microchip SAMA7G5 电源管理控制器（Power Management Controller，PMC）

**说明（Help）**

启用 Microchip SAMA7G5 电源管理控制器（Power Management Controller，PMC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SAM_PMC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.sam:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.sam#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SAMA7G5_SCKC"></a>

## 63.56 `CONFIG_CLOCK_CONTROL_SAMA7G5_SCKC`

**提示（Prompt）**：Microchip SAMA7G5 低速时钟控制器（Slow Clock Controller，SCKC）

**说明（Help）**

启用 Microchip SAMA7G5 低速时钟控制器（Slow Clock Controller，SCKC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SAMA7G5_SCKC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.sam:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.sam#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SF32LB_HXT48"></a>

## 63.57 `CONFIG_CLOCK_CONTROL_SF32LB_HXT48`

**提示（Prompt）**：SF32LB HXT48 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用思澈（SiFli）SF32LB HXT48 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_HXT48_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.sf32lb_hxt48:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.sf32lb_hxt48#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SF32LB_RCC"></a>

## 63.58 `CONFIG_CLOCK_CONTROL_SF32LB_RCC`

**提示（Prompt）**：SF32LB RCC 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用思澈（SiFli）SF32LB 复位与时钟控制（RCC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_RCC_CLK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.sf32lb_rcc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.sf32lb_rcc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SHELL"></a>

## 63.59 `CONFIG_CLOCK_CONTROL_SHELL`

**提示（Prompt）**：时钟控制命令行（Clock Control Shell）

**说明（Help）**

启用时钟控制命令行（Clock Control Shell），支持调用时钟控制 API 操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SI32_AHB"></a>

## 63.60 `CONFIG_CLOCK_CONTROL_SI32_AHB`

**提示（Prompt）**：SI32 AHB 时钟控制（Clock Control）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI32_AHB_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.si32:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.si32#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SI32_APB"></a>

## 63.61 `CONFIG_CLOCK_CONTROL_SI32_APB`

**提示（Prompt）**：SI32 APB 时钟控制（Clock Control）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI32_APB_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.si32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.si32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SI32_PLL"></a>

## 63.62 `CONFIG_CLOCK_CONTROL_SI32_PLL`

**提示（Prompt）**：SI32 锁相环时钟控制（PLL Clock Control）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI32_PLL_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.si32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.si32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_SILABS_SERIES"></a>

## 63.63 `CONFIG_CLOCK_CONTROL_SILABS_SERIES`

**提示（Prompt）**：Silicon Labs Series 2+ 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用 Silicon Labs Series 2+ 时钟管理单元（Clock Management Unit）的时钟控制驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SERIES_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_CLOCK_MANAGER
```

**被选择（Selected by）**

```text
CONFIG_SPI_SILABS_USART
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SILABS_SISDK_CLOCK_MANAGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_CLOCK_MANAGER)、[`CONFIG_SPI_SILABS_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_SILABS_USART)。

<a id="CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT"></a>

## 63.64 `CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT`

**提示（Prompt）**：Silicon Labs Series 2+ 时钟输出驱动（Clock Output Driver）

**说明（Help）**

启用 Silicon Labs Series 2+ 时钟管理单元（Clock Management Unit）的时钟输出驱动。驱动支持 `on`、`off`、`get_rate` 和 `get_status` 操作，将设备树（Devicetree）配置的时钟输出到引脚。时钟 API 的 `subsys` 参数表示所操作的时钟输出（Clock Output）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SERIES_CLOCK_OUTPUT_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_CLOCK_MANAGER
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.silabs:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.silabs#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SILABS_SISDK_CLOCK_MANAGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_CLOCK_MANAGER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT_INIT_PRIORITY"></a>

## 63.65 `CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT_INIT_PRIORITY`

**提示（Prompt）**：Silicon Labs Series 2+ 时钟输出初始化优先级（Init Priority）

**说明（Help）**

时钟输出（Clock Output）的初始化优先级。其数值必须大于引脚控制（Pinctrl）／GPIO 初始化的数值，并小于任何时钟使用者（Clock Consumer）的数值，使时钟输出在前者之后、后者之前初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.silabs:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.silabs#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → Silicon Labs Series 2+ 时钟输出驱动（Clock Output Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_SILABS_SERIES_OUTPUT)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<a id="CONFIG_CLOCK_CONTROL_SILABS_SIWX91X"></a>

## 63.66 `CONFIG_CLOCK_CONTROL_SILABS_SIWX91X`

**提示（Prompt）**：Silicon Labs SiWx91x 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用 Silicon Labs SiWx91x 芯片的时钟管理（Clock Management），支持高性能（High Performance，HP）、超低功耗（Ultra Low Power，ULP）和常开（Always-On，AON）时钟。

AON／ULP／HP 的初始化顺序通过设备树（Devicetree）中各时钟管理单元（CMU）节点之间的 `clocks` 引用句柄（Phandle）表达。三个管理器都使用 `CLOCK_CONTROL_INIT_PRIORITY`，由设备树依赖序号（DT Dependency Ordinals）决定顺序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_CMU_HP_ENABLED && DT_HAS_SILABS_SIWX91X_CMU_ULP_ENABLED && DT_HAS_SILABS_SIWX91X_CMU_AON_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_CLOCK_CONTROL_SMARTBOND"></a>

## 63.67 `CONFIG_CLOCK_CONTROL_SMARTBOND`

**提示（Prompt）**：SmartBond 时钟控制（Clock Control）

**说明（Help）**

启用 SmartBond 中的时钟控制（Clock Control）子系统驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_SMARTBOND && CONFIG_CLOCK_CONTROL
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_DA1469X
CONFIG_COUNTER_SMARTBOND_TIMER
CONFIG_USB_DC_SMARTBOND
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.smartbond:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.smartbond#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_SMARTBOND)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_COUNTER_SMARTBOND_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_SMARTBOND_TIMER)、[`CONFIG_USB_DC_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DC_SMARTBOND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`。

<a id="CONFIG_CLOCK_CONTROL_STM32_CUBE"></a>

## 63.68 `CONFIG_CLOCK_CONTROL_STM32_CUBE`

**提示（Prompt）**：STM32 复位与时钟控制（Reset & Clock Control）

**说明（Help）**

启用 STM32 微控制器（MCU）系列中的复位与时钟控制（Reset & Clock Control）子系统驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32 && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_LL_UTILS
CONFIG_USE_STM32_LL_RCC if CONFIG_SOC_SERIES_STM32MP1X || CONFIG_SOC_SERIES_STM32MP13X || CONFIG_SOC_SERIES_STM32MP2X || CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H7RSX || CONFIG_SOC_SERIES_STM32F4X || CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32N6X
CONFIG_RUNTIME_NMI if n && n
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.stm32:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.stm32#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_USE_STM32_LL_UTILS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_UTILS)、[`CONFIG_USE_STM32_LL_RCC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_RCC)、[`CONFIG_SOC_SERIES_STM32MP1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP1X)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_SOC_SERIES_STM32MP2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP2X)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_RUNTIME_NMI`](P030_arch_arm_配置项参考_2.md#CONFIG_RUNTIME_NMI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`、`CONFIG_SOC_SERIES_STM32MP1X`、`CONFIG_SOC_SERIES_STM32MP13X`、`CONFIG_SOC_SERIES_STM32MP2X`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32N6X`。

<a id="CONFIG_CLOCK_CONTROL_SYNA_SR100"></a>

## 63.69 `CONFIG_CLOCK_CONTROL_SYNA_SR100`

**提示（Prompt）**：Synaptics SR100 时钟控制驱动（Clock Control Driver）

**说明（Help）**

启用 Synaptics SR100 片上系统（SoC）系列的时钟控制（Clock Control）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SYNA_SR100_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.syna_sr100:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.syna_sr100#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_TISCI"></a>

## 63.70 `CONFIG_CLOCK_CONTROL_TISCI`

**提示（Prompt）**：TI SCI 时钟控制驱动（Clock Control Driver）

**说明（Help）**

基于 TI 系统控制接口（TISCI）的时钟控制（Clock Control）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_K2G_SCI_CLK_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.tisci:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.tisci#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_TISCI_PRIORITY"></a>

## 63.71 `CONFIG_CLOCK_CONTROL_TISCI_PRIORITY`

**提示（Prompt）**：TISCI 时钟控制器优先级（Clock Controller Priority）

**说明（Help）**

TISCI 时钟控制器的优先级数值应始终等于或大于 TISCI 的优先级数值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_TISCI && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.tisci:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.tisci#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → TI SCI 时钟控制驱动（Clock Control Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_TISCI`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_TISCI)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<a id="CONFIG_CLOCK_CONTROL_TI_CDCE9XX"></a>

## 63.72 `CONFIG_CLOCK_CONTROL_TI_CDCE9XX`

**提示（Prompt）**：TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator）

**说明（Help）**

TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_CDCE913_ENABLED || DT_HAS_TI_CDCE925_ENABLED || DT_HAS_TI_CDCE937_ENABLED || DT_HAS_TI_CDCE949_ENABLED) && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.ti_cdce9xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.ti_cdce9xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_CLOCK_CONTROL_TI_CDCE9XX_PRIORITY"></a>

## 63.73 `CONFIG_CLOCK_CONTROL_TI_CDCE9XX_PRIORITY`

**提示（Prompt）**：TI CDCE9xx 低功耗时钟发生器初始化优先级（Init Priority）

**说明（Help）**

TI CDCE9xx 低功耗时钟发生器（Low Power Clock Generator）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_TI_CDCE9XX && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.ti_cdce9xx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.ti_cdce9xx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → TI 低功耗时钟发生器 CDCE9xx（Low Power Clock Generator）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_TI_CDCE9XX`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_TI_CDCE9XX)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_WCH_RCC"></a>

## 63.74 `CONFIG_CLOCK_CONTROL_WCH_RCC`

**提示（Prompt）**：沁恒 CH32V00x 复位与时钟控制驱动（WCH RCC Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_RCC_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.wch_rcc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.wch_rcc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_CONTROL_XCLK_WIZ"></a>

## 63.75 `CONFIG_CLOCK_CONTROL_XCLK_WIZ`

**提示（Prompt）**：Xilinx 时钟向导驱动（Clock Wizard Driver）

**说明（Help）**

为 AMD Versal2 平台启用 Xilinx Clocking Wizard，即 `clkx5-wiz-1.0`，的时钟控制驱动。支持以下功能：

- 设置时钟输出频率（Clock Output Rate Set），通过动态重新配置混合模式时钟管理器（MMCM）实现。
- 获取时钟输出频率（Clock Output Rate Get），读取当前 M／D／O 分频系数。
- 启用／禁用时钟输出，通过各输出独立的时钟门控（Per-Output Clock Gating）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_CLKX5_WIZ_1_0_ENABLED && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.xclk_wiz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.xclk_wiz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_STM32_HSE_CLOCK"></a>

## 63.76 `CONFIG_CLOCK_STM32_HSE_CLOCK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

外部高速时钟（High-Speed External Clock，HSE）的频率。

此符号的值用于设置预处理器定义（Preprocessor Definition）`HSE_VALUE`，硬件抽象层（HAL）等代码会使用它。

此符号不能从外部设置；其值直接取自已启用的设备树节点（Devicetree Node）`clk_hse` 的 `clock-frequency` 属性。该节点通常如下：

```dts
  &clk_hse {
    clock-frequency = <DT_FREQ_M(25)>;
    status = "okay";
  };
```

如果 `clk_hse` 节点不存在，或未启用，即 `status != "okay"`，则不定义此符号，也不存在 `HSE_VALUE` 预处理器定义。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.stm32:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.stm32#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → STM32 复位与时钟控制（Reset & Clock Control）

<a id="CONFIG_CLOCK_STM32_MCO"></a>

## 63.77 `CONFIG_CLOCK_STM32_MCO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

允许通过可配置的预分频器（Prescaler），将不同的时钟源输出到微控制器时钟输出（MCO）引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_CLOCK_MCO_ENABLED || DT_HAS_ST_STM32F1_CLOCK_MCO_ENABLED) && CONFIG_CLOCK_CONTROL_STM32_CUBE && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.stm32:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.stm32#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → STM32 复位与时钟控制（Reset & Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_STM32_CUBE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_STM32_CUBE)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_CLOCK_STM32_MCO_HAS_ENABLE_BIT"></a>

## 63.78 `CONFIG_CLOCK_STM32_MCO_HAS_ENABLE_BIT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，表示该系列具有用于启用微控制器时钟输出（MCO）的专用位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_CLOCK_MCO_ENABLED && (CONFIG_SOC_SERIES_STM32N6X || CONFIG_SOC_SERIES_STM32MP13X) && CONFIG_CLOCK_CONTROL_STM32_CUBE && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.stm32:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.stm32#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → STM32 复位与时钟控制（Reset & Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_CLOCK_CONTROL_STM32_CUBE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_STM32_CUBE)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32MP13X`。

<a id="CONFIG_CLOCK_STM32_MUX"></a>

## 63.79 `CONFIG_CLOCK_STM32_MUX`

**提示（Prompt）**：STM32 时钟多路选择器驱动（Clock Mux Driver）

**说明（Help）**

启用 STM32 时钟多路选择器（Clock Mux）驱动。该选择器不对应现有的时钟硬件模块，但允许为特定时钟域（Domain）选择时钟，例如 STM32H7 的 `per_ck` 或 `CLK48` 时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_CLOCK_MUX_ENABLED && CONFIG_CLOCK_CONTROL_STM32_CUBE && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.stm32:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.stm32#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → STM32 复位与时钟控制（Reset & Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_STM32_CUBE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_STM32_CUBE)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_CLOCK_STM32_N6_PRESERVE_BOOT_CONFIG"></a>

## 63.80 `CONFIG_CLOCK_STM32_N6_PRESERVE_BOOT_CONFIG`

**提示（Prompt）**：保留 STM32N6 启动时钟配置（Boot Clock Configuration）

**说明（Help）**

对于由 MCUboot 链式加载（Chain-Loaded）的 STM32N6 应用，保留已有时钟配置。应用可能从引导加载程序（Bootloader）初始化的外部 XSPI NOR 或伪静态 RAM（PSRAM）执行。

预期引导加载程序已初始化需要保留的时钟树（Clock Tree）及外部内存控制器（External-Memory Controller）。应用域的振荡器（Oscillator）、锁相环（PLL）、互连（Interconnect）、预分频器（Prescaler）、IC 和系统时钟（SYSCLK）配置有意不再重复。应用的设备树（Devicetree）必须描述这些保留下来的时钟与外部内存硬件状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_STM32N6X && CONFIG_BOOTLOADER_MCUBOOT && (DT_HAS_ST_STM32_XSPI_NOR_ENABLED || DT_HAS_ST_STM32_XSPI_PSRAM_ENABLED) && CONFIG_CLOCK_CONTROL_STM32_CUBE && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.stm32:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.stm32#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → STM32 复位与时钟控制（Reset & Clock Control）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_BOOTLOADER_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_CLOCK_CONTROL_STM32_CUBE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_STM32_CUBE)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`。

<a id="CONFIG_EM32_DELAY_SWITCH_PRIORITY"></a>

## 63.81 `CONFIG_EM32_DELAY_SWITCH_PRIORITY`

**提示（Prompt）**：延迟后端切换初始化优先级（Delay Switch Init Priority）

**说明（Help）**

将延迟后端（Delay Backend）切换到 `k_busy_wait()` 的初始化优先级。其数值必须大于 `CONFIG_SYSTEM_CLOCK_INIT_PRIORITY`，因为系统定时器（System Timer）在 `PRE_KERNEL_2` 阶段初始化。默认值为 1，在此片上系统（SoC）中即 `CONFIG_SYSTEM_CLOCK_INIT_PRIORITY + 1`。`BUILD_ASSERT` 会强制检查顺序；如果系统时钟初始化优先级发生变化，导致顺序不符，构建将失败。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_CLOCK_CONTROL_EM32_AHB || CONFIG_CLOCK_CONTROL_EM32_APB) && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.em32:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.em32#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_EM32_AHB`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_EM32_AHB)、[`CONFIG_CLOCK_CONTROL_EM32_APB`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_EM32_APB)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_INFINEON_SYSCLK_HAS_CLK_PUMP"></a>

## 63.82 `CONFIG_INFINEON_SYSCLK_HAS_CLK_PUMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，由具有 `clk_pump` 电荷泵（Charge Pump）IP 模块的片上系统（SoC）系列启用。并非所有英飞凌（Infineon）CAT1 SoC 都有此能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
n if CONFIG_SOC_SERIES_PSOC4000T
y if CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.infineon:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.infineon#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_INFINEON_SYSCLK_LOCK_NONE"></a>

## 63.83 `CONFIG_INFINEON_SYSCLK_LOCK_NONE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，由以下片上系统（SoC）系列启用：其内部主振荡器（IMO）时钟重新配置后，必须显式解除与`WCO` 时钟的锁定，即调用 `Cy_SysClk_ImoLock(CY_SYSCLK_IMO_LOCK_NONE)`。并非所有英飞凌（Infineon）CAT1 SoC 都有此能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
n if CONFIG_SOC_SERIES_PSOC4000T
y if CONFIG_SOC_FAMILY_INFINEON_PSOC4
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.infineon:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.infineon#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_FAMILY_INFINEON_PSOC4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_PSOC4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_PSOC4`。

<a id="CONFIG_IT51XXX_USB_SOF_CALIBRATION"></a>

## 63.84 `CONFIG_IT51XXX_USB_SOF_CALIBRATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用帧起始（SOF）校准，以提高 USB 时钟精度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_IT51XXX && CONFIG_CLOCK_CONTROL
```

**被选择（Selected by）**

```text
CONFIG_UDC_IT51XXX
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.it51xxx:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.it51xxx#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → ITE IT51XXX 时钟控制器驱动（Clock Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_IT51XXX`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_IT51XXX)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_UDC_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_IT51XXX)。

<a id="CONFIG_RPI_PICO_ROSC_USE_MEASURED_FREQ"></a>

## 63.85 `CONFIG_RPI_PICO_ROSC_USE_MEASURED_FREQ`

**提示（Prompt）**：使用环形振荡器的测得频率（Measured Ring Oscillator Frequency）

**说明（Help）**

使用频率计数器（Frequency Counter）测得的值作为环形振荡器（ROSC）频率，而不是使用设备树源码（DTS）中的值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_RPI_PICO && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.rpi_pico:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.rpi_pico#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 树莓派 Pico 时钟控制器驱动（Raspberry Pi Pico Clock Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_RPI_PICO`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RPI_PICO)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_RPI_PICO_SKIP_CLOCK_INIT"></a>

## 63.86 `CONFIG_RPI_PICO_SKIP_CLOCK_INIT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

跳过时钟初始化（Clock Initialisation）；在第二个 CPU 内核上运行 Zephyr 时需要这样做。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_RPI_PICO && CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.rpi_pico:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.rpi_pico#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → 树莓派 Pico 时钟控制器驱动（Raspberry Pi Pico Clock Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_RPI_PICO`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RPI_PICO)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_STM32WB0_LSI_MEASUREMENT_WINDOW"></a>

## 63.87 `CONFIG_STM32WB0_LSI_MEASUREMENT_WINDOW`

**提示（Prompt）**：LSI 测量窗口大小，以周期数计（Measurement Window Size）

**说明（Help）**

低速内部振荡器（LSI）测量窗口的大小，即 LSI 周期数量。测量过程等待一定数量的 LSI 周期发生，以精确确定 LSI 周期及其频率。此属性控制每次测量需要多少个 LSI 周期。

窗口越大，测量精度越高，但完成测量所需的时间也越长。由于 `fLSI >= 24kHz`，测量窗口每增加一个周期，最坏情况下每次测量会增加约 42µs。最小值采用 RM0505 Rev.1 第 25.8.2 节的建议，最大值受硬件限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32WB0_LSI_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL_STM32_CUBE && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[23, 256]
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.stm32:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.stm32#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → STM32 复位与时钟控制（Reset & Clock Control） → STM32WB0 LSI 选项（LSI Options）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_STM32_CUBE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_STM32_CUBE)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_STM32WB0_LSI_RUNTIME_MEASUREMENT_INTERVAL"></a>

## 63.88 `CONFIG_STM32WB0_LSI_RUNTIME_MEASUREMENT_INTERVAL`

**提示（Prompt）**：LSI 运行时测量间隔，单位为毫秒（Runtime Measurement Interval）

**说明（Help）**

运行时测量（Runtime Measurement）的执行间隔，单位为毫秒。由于低速内部 RC 振荡器（LSI）的频率受温度影响，而温度随时间变化，建议定期测量 LSI 频率以获得更高精度。

存在此属性时会启用运行时 LSI 测量，创建一个后台线程执行测量，并在相邻测量之间休眠此属性指定的时长。该线程还与外设驱动配合，更新受低速时钟漂移（Slow Clock Drift）影响的外设控制寄存器，例如实时时钟（RTC）和独立看门狗（IWDG）的寄存器。

注意，这会增加时钟控制驱动的内存占用，也可能增加功耗。将此选项设为默认值 0，可禁用运行时频率测量；启动时单次测量的结果将被视为应用整个生命周期内的 LSI 频率。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32WB0_LSI_CLOCK_ENABLED && CONFIG_CLOCK_CONTROL_STM32_CUBE && CONFIG_CLOCK_CONTROL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/clock_control/Kconfig.stm32:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/Kconfig.stm32#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟控制器驱动（Clock Controller Drivers） → STM32 复位与时钟控制（Reset & Clock Control） → STM32WB0 LSI 选项（LSI Options）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_STM32_CUBE`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_STM32_CUBE)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<!-- kconfig-navigation -->

[上一章](P062_drivers_clock_control_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P064_drivers_clock_monitor_配置项参考.md)
