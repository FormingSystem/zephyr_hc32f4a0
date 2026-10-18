---
id: learning.zephyr-docs.kconfig-reference.page-227
title: "`modules/hal_nordic`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第227章\_`modules/hal_nordic`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `modules/hal_nordic` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_IRONSIDE_SE_CALL"></a>

## 227.1 `CONFIG_IRONSIDE_SE_CALL`

**提示（Prompt）**：IronSide 调用（calls）

**说明（Help）**

支持 IronSide 调用 API（call APIs）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_IRONSIDE_SE_CALL && CONFIG_HAS_IRONSIDE_SE
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF54H20_CPURAD_ENABLE
CONFIG_DEBUG_CORESIGHT_NRF
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE

**配置项引用（Symbol References）**：[`CONFIG_HAS_IRONSIDE_SE_CALL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE_CALL)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)、[`CONFIG_SOC_NRF54H20_CPURAD_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_ENABLE)、[`CONFIG_DEBUG_CORESIGHT_NRF`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_CORESIGHT_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE_CALL`、`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_IRONSIDE_SE_CALL_DRIVER"></a>

## 227.2 `CONFIG_IRONSIDE_SE_CALL_DRIVER`

**提示（Prompt）**：IronSide 调用的驱动实现（driver implementation）

**说明（Help）**

IronSide 调用（calls）使用的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IRONSIDE_SE_CALL && CONFIG_HAS_IRONSIDE_SE
```

**默认值（Defaults）**

```text
CONFIG_IRONSIDE_SE_CALL_ZEPHYR if DT_HAS_NORDIC_IRONSIDE_CALL_ENABLED
CONFIG_IRONSIDE_SE_CALL_MINIMAL
```

**可选项（Choices）**

```text
CONFIG_IRONSIDE_SE_CALL_ZEPHYR
CONFIG_IRONSIDE_SE_CALL_MINIMAL
CONFIG_IRONSIDE_SE_CALL_ZEPHYR
CONFIG_IRONSIDE_SE_CALL_MINIMAL
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE → IronSide 调用（calls）

**配置项引用（Symbol References）**：[`CONFIG_IRONSIDE_SE_CALL`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)、[`CONFIG_IRONSIDE_SE_CALL_ZEPHYR`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL_ZEPHYR)、[`CONFIG_IRONSIDE_SE_CALL_MINIMAL`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL_MINIMAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_IRONSIDE_SE_CALL_INIT_PRIORITY"></a>

## 227.3 `CONFIG_IRONSIDE_SE_CALL_INIT_PRIORITY`

**提示（Prompt）**：IronSide 调用驱动的初始化优先级（initialization priority）

**说明（Help）**

IronSide 调用协议驱动（call protocol driver）的初始化优先级。初始化顺序必须晚于 `MBOX_INIT_PRIORITY` 对应的邮箱驱动，但早于任何依赖 `IRONSIDE_SE_CALL` 的功能。

译注：原文使用“below MBOX_INIT_PRIORITY, but higher than ...”描述优先级。当前快照中此项默认为 `41`，`MBOX_INIT_PRIORITY` 默认为 `40`；这里按初始化先后解释，不将 below 误译为数值小于 40。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IRONSIDE_SE_CALL_ZEPHYR && CONFIG_IRONSIDE_SE_CALL && CONFIG_HAS_IRONSIDE_SE
```

**默认值（Defaults）**

```text
41
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE → IronSide 调用（calls）

**配置项引用（Symbol References）**：[`CONFIG_IRONSIDE_SE_CALL_ZEPHYR`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL_ZEPHYR)、[`CONFIG_IRONSIDE_SE_CALL`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_IRONSIDE_SE_CALL_MINIMAL"></a>

## 227.4 `CONFIG_IRONSIDE_SE_CALL_MINIMAL`

**提示（Prompt）**：最小驱动（Minimal driver）

**说明（Help）**

使用 IronSide API 随附的最小 IronSide 调用驱动（minimal driver）。它不支持不同线程并发调用，等待 IronSide SE 回复时使用忙等待（busy waiting）而不是中断。它也不处理 IPC 缓冲区的数据缓存，而是假设该缓冲区区域不经过缓存。主要用于引导加载程序（bootloaders）等受限应用，不推荐用于通用场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IRONSIDE_SE_CALL_DRIVER>
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE → IronSide 调用（calls） → IronSide 调用的驱动实现（driver implementation）

**配置项引用（Symbol References）**：[`CONFIG_IRONSIDE_SE_CALL_DRIVER`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL_DRIVER)。

<a id="CONFIG_IRONSIDE_SE_CALL_ZEPHYR"></a>

## 227.5 `CONFIG_IRONSIDE_SE_CALL_ZEPHYR`

**提示（Prompt）**：Zephyr 驱动（driver）

**说明（Help）**

使用支持不同线程并发发起 IronSide 调用的默认驱动。这是推荐实现，大多数应用应使用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_IRONSIDE_CALL_ENABLED && CONFIG_MULTITHREADING && <choice CONFIG_IRONSIDE_SE_CALL_DRIVER>
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
CONFIG_MBOX
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE → IronSide 调用（calls） → IronSide 调用的驱动实现（driver implementation）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_IRONSIDE_SE_CALL_DRIVER`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL_DRIVER)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_IRONSIDE_SE_DVFS"></a>

## 227.6 `CONFIG_IRONSIDE_SE_DVFS`

**提示（Prompt）**：动态电压频率调整（DVFS）支持

**说明（Help）**

支持更改动态电压频率调整（DVFS）的工作点（operating point）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF54H20_CPUAPP && CONFIG_IRONSIDE_SE_CALL && CONFIG_HAS_IRONSIDE_SE
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE → IronSide 调用（calls）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54H20_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP)、[`CONFIG_IRONSIDE_SE_CALL`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)、[`CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_IRON_HSFLL_LOCAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_IRONSIDE_SE_DVFS_ABB_STATUSANA_CHECK_MAX_ATTEMPTS"></a>

## 227.7 `CONFIG_IRONSIDE_SE_DVFS_ABB_STATUSANA_CHECK_MAX_ATTEMPTS`

**提示（Prompt）**：ABB 模拟状态检查（analog status check）的最大尝试次数

**说明（Help）**

以 10 μs 为间隔尝试的最大次数；达到该次数仍未就绪时，报告忙状态（busy status）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IRONSIDE_SE_DVFS && CONFIG_HAS_IRONSIDE_SE
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`modules/hal_nordic/ironside/se/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/ironside/se/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → IronSide SE → IronSide 调用（calls） → 动态电压频率调整（DVFS）支持

**配置项引用（Symbol References）**：[`CONFIG_IRONSIDE_SE_DVFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_DVFS)、[`CONFIG_HAS_IRONSIDE_SE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_IRONSIDE_SE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_IRONSIDE_SE`。

<a id="CONFIG_NRFS"></a>

## 227.8 `CONFIG_NRFS`

**提示（Prompt）**：nRF 服务支持（Services Support）

**说明（Help）**

启用 nRF 服务库（Services library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFS && CONFIG_HAS_NRFS
```

**主动选择（Selects）**

```text
CONFIG_NRFS_LOCAL_DOMAIN if CONFIG_SOC_NRF54H20_CPUAPP || CONFIG_SOC_NRF54H20_CPURAD || CONFIG_SOC_NRF9280_CPUAPP || CONFIG_SOC_NRF9280_CPURAD
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL
CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL
CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL
CONFIG_CLOCK_CONTROL_NRFS_LFCLK
CONFIG_POWER_DOMAIN_NRFS_GDPWR
CONFIG_POWER_DOMAIN_NRFS_SWEXT
CONFIG_UDC_DWC2
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_FLASH_NRF_MRAM
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_NRFS_LOCAL_DOMAIN`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_LOCAL_DOMAIN)、[`CONFIG_SOC_NRF54H20_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP)、[`CONFIG_SOC_NRF54H20_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD)、[`CONFIG_SOC_NRF9280_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9280_CPUAPP)、[`CONFIG_SOC_NRF9280_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9280_CPURAD)、[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL)、[`CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL)、[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL)、[`CONFIG_CLOCK_CONTROL_NRFS_LFCLK`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRFS_LFCLK)、[`CONFIG_POWER_DOMAIN_NRFS_GDPWR`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_NRFS_GDPWR)、[`CONFIG_POWER_DOMAIN_NRFS_SWEXT`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_NRFS_SWEXT)、[`CONFIG_UDC_DWC2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DWC2)、[`CONFIG_SOC_FLASH_NRF_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_AUDIOPLL_SERVICE_ENABLED"></a>

## 227.9 `CONFIG_NRFS_AUDIOPLL_SERVICE_ENABLED`

**提示（Prompt）**：音频锁相环服务（Audio PLL service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_AUDIOPLL_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_NRF54H20_CPUAPP
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_AUDIOPLL_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_AUDIOPLL_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_SOC_NRF54H20_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP)、[`CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRFS_AUDIOPLL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_AUDIOPLL_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_BACKEND_IPC_SERVICE_INIT_PRIO"></a>

## 227.10 `CONFIG_NRFS_BACKEND_IPC_SERVICE_INIT_PRIO`

**提示（Prompt）**：NRFS IPC 后端初始化优先级（Initialization priority）

**说明（Help）**

此优先级数值应大于 NRFS 后端所使用的其他驱动／子系统的优先级数值。原文举例为值为 `50` 的 `MBOX_INIT_PRIORITY`。

译注：此项默认值为 `51`；当前完整快照中 `MBOX_INIT_PRIORITY` 的默认值实际为 `40`。原文示例 `50` 保留为来源表述，不据此改写邮箱驱动的实际默认值。数值较大对应较晚初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/backends/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/backends/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings）

**配置项引用（Symbol References）**：[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_BACKEND_TX_MSG_QUEUE_SIZE"></a>

## 227.11 `CONFIG_NRFS_BACKEND_TX_MSG_QUEUE_SIZE`

**提示（Prompt）**：发送缓冲区消息队列大小（TX buffer message queue size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/backends/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/backends/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings）

**配置项引用（Symbol References）**：[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_CLOCK_SERVICE_ENABLED"></a>

## 227.12 `CONFIG_NRFS_CLOCK_SERVICE_ENABLED`

**提示（Prompt）**：时钟服务（Clock service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_CLOCK_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRFS_LFCLK
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_CLOCK_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_CLOCK_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_CLOCK_CONTROL_NRFS_LFCLK`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRFS_LFCLK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_CLOCK_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_CONST_LATENCY_SERVICE_ENABLED"></a>

## 227.13 `CONFIG_NRFS_CONST_LATENCY_SERVICE_ENABLED`

**提示（Prompt）**：分布式可编程外设互连恒定延迟服务（DPPI constant latency service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_CONST_LATENCY_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_CONST_LATENCY_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_CONST_LATENCY_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_CONST_LATENCY_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_DIAG_SERVICE_ENABLED"></a>

## 227.14 `CONFIG_NRFS_DIAG_SERVICE_ENABLED`

**提示（Prompt）**：系统诊断服务（System Diagnostics service），仅用于开发

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_DIAG_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_DIAG_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_DIAG_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_DIAG_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_DVFS_LOCAL_DOMAIN"></a>

## 227.15 `CONFIG_NRFS_DVFS_LOCAL_DOMAIN`

**提示（Prompt）**：支持动态电压频率调整（DVFS）的本地域（Local domain）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_LOCAL_DOMAIN && CONFIG_NRFS_DVFS_SERVICE_ENABLED && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y if CONFIG_NRFS_DVFS_SERVICE_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → nRF 服务本地域支持（Services Local Domain Support）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_LOCAL_DOMAIN`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_LOCAL_DOMAIN)、[`CONFIG_NRFS_DVFS_SERVICE_ENABLED`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_DVFS_SERVICE_ENABLED)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_DVFS_SERVICE_ENABLED"></a>

## 227.16 `CONFIG_NRFS_DVFS_SERVICE_ENABLED`

**提示（Prompt）**：动态电压频率调整服务（DVFS service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_DVFS_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_NRF54H20_CPUAPP || CONFIG_SOC_NRF9280_CPUAPP
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_DVFS_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_DVFS_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_SOC_NRF54H20_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP)、[`CONFIG_SOC_NRF9280_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9280_CPUAPP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_DVFS_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_GDFS_SERVICE_ENABLED"></a>

## 227.17 `CONFIG_NRFS_GDFS_SERVICE_ENABLED`

**提示（Prompt）**：全局域频率调整服务（Global domain frequency scaling service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_GDFS_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_GDFS_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_GDFS_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_HSFLL_GLOBAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_GDFS_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_GDPWR_SERVICE_ENABLED"></a>

## 227.18 `CONFIG_NRFS_GDPWR_SERVICE_ENABLED`

**提示（Prompt）**：全局域电源请求服务（Global domain power request service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_GDPWR_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_POWER_DOMAIN_NRFS_GDPWR
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_GDPWR_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_GDPWR_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_POWER_DOMAIN_NRFS_GDPWR`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_NRFS_GDPWR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_GDPWR_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_GSWDT_SERVICE_ENABLED"></a>

## 227.19 `CONFIG_NRFS_GSWDT_SERVICE_ENABLED`

**提示（Prompt）**：全局软件看门狗服务（Global Software Watchdog service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_GSWDT_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_GSWDT_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_GSWDT_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_GSWDT_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_LOCAL_DOMAIN"></a>

## 227.20 `CONFIG_NRFS_LOCAL_DOMAIN`

**提示（Prompt）**：nRF 服务本地域支持（Services Local Domain Support）

**说明（Help）**

启用 nRF 服务本地域库（Services Local Domain libraries）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IPC_SERVICE
CONFIG_MBOX
CONFIG_EVENTS
CONFIG_REBOOT
```

**被选择（Selected by）**

```text
CONFIG_NRFS
CONFIG_NRFS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)。

<a id="CONFIG_NRFS_LOCAL_DOMAIN_DOWNSCALE_FINISH_DELAY_TIMEOUT_US"></a>

## 227.21 `CONFIG_NRFS_LOCAL_DOMAIN_DOWNSCALE_FINISH_DELAY_TIMEOUT_US`

**提示（Prompt）**：等待 secdom 完成降档过程（downscale procedure）的额外延迟，单位为 μs

**说明（Help）**

此值取决于 secdom 核心的性能，用户不应修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_DVFS_LOCAL_DOMAIN && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[1, 10000000]
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/dvfs/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/dvfs/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_DVFS_LOCAL_DOMAIN`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_DVFS_LOCAL_DOMAIN)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_LOCAL_DOMAIN_DOWNSCALE_SAFETY_TIMEOUT_US"></a>

## 227.22 `CONFIG_NRFS_LOCAL_DOMAIN_DOWNSCALE_SAFETY_TIMEOUT_US`

**提示（Prompt）**：电压下调过程安全超时（Voltage downscale procedure safety timeout），单位为 μs

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_DVFS_LOCAL_DOMAIN && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
1000000 if CONFIG_NRFS_LOCAL_DOMAIN_DVFS_TEST || CONFIG_LOG
1500
```

**取值范围（Ranges）**

```text
[1, 10000000]
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/dvfs/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/dvfs/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_DVFS_LOCAL_DOMAIN`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_DVFS_LOCAL_DOMAIN)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_NRFS_LOCAL_DOMAIN_DVFS_TEST`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_LOCAL_DOMAIN_DVFS_TEST)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_LOCAL_DOMAIN_DVFS_HANDLER_TASK_PRIORITY"></a>

## 227.23 `CONFIG_NRFS_LOCAL_DOMAIN_DVFS_HANDLER_TASK_PRIORITY`

**提示（Prompt）**：动态电压频率调整处理任务（DVFS handling task）优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_DVFS_LOCAL_DOMAIN && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[-16, CONFIG_NUM_PREEMPT_PRIORITIES]
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/dvfs/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/dvfs/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_DVFS_LOCAL_DOMAIN`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_DVFS_LOCAL_DOMAIN)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_LOCAL_DOMAIN_DVFS_HANDLER_TASK_STACK_SIZE"></a>

## 227.24 `CONFIG_NRFS_LOCAL_DOMAIN_DVFS_HANDLER_TASK_STACK_SIZE`

**提示（Prompt）**：动态电压频率调整处理任务（DVFS handling task）栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_DVFS_LOCAL_DOMAIN && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
1024 if CONFIG_LOG
512
```

**取值范围（Ranges）**

```text
[256, 2048]
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/dvfs/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/dvfs/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_DVFS_LOCAL_DOMAIN`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_DVFS_LOCAL_DOMAIN)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_LOCAL_DOMAIN_DVFS_TEST"></a>

## 227.25 `CONFIG_NRFS_LOCAL_DOMAIN_DVFS_TEST`

**提示（Prompt）**：本地域动态电压频率调整测试（Local domain DVFS test）

**说明（Help）**

为测试禁用与硬件寄存器（hardware registers）的交互。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_DVFS_LOCAL_DOMAIN && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/dvfs/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/dvfs/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_DVFS_LOCAL_DOMAIN`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS_DVFS_LOCAL_DOMAIN)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_MAX_BACKEND_PACKET_SIZE"></a>

## 227.26 `CONFIG_NRFS_MAX_BACKEND_PACKET_SIZE`

**提示（Prompt）**：最大进程间通信数据包大小（IPC data packet size），单位为字节

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[8, 128]
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/backends/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/backends/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings）

**配置项引用（Symbol References）**：[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_MRAM_SERVICE_ENABLED"></a>

## 227.27 `CONFIG_NRFS_MRAM_SERVICE_ENABLED`

**提示（Prompt）**：磁阻随机存取存储器延迟服务（MRAM latency service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_MRAM_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**被选择（Selected by）**

```text
CONFIG_MRAM_LATENCY
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_MRAM_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_MRAM_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_MRAM_LATENCY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MRAM_LATENCY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_MRAM_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_PMIC_SERVICE_ENABLED"></a>

## 227.28 `CONFIG_NRFS_PMIC_SERVICE_ENABLED`

**提示（Prompt）**：电源管理集成电路服务（PMIC service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_PMIC_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_PMIC_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_PMIC_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_PMIC_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_RESET_SERVICE_ENABLED"></a>

## 227.29 `CONFIG_NRFS_RESET_SERVICE_ENABLED`

**提示（Prompt）**：复位服务（Reset service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_RESET_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_RESET_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_RESET_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_RESET_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_SEND_RETRY_DELAY"></a>

## 227.30 `CONFIG_NRFS_SEND_RETRY_DELAY`

**提示（Prompt）**：延迟（Delay），单位为 μs

**说明（Help）**

发送出错后，等待下一次消息发送重试（message send retry）之前的延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/backends/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/backends/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings）

**配置项引用（Symbol References）**：[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_SEND_RETRY_MAX_COUNT"></a>

## 227.31 `CONFIG_NRFS_SEND_RETRY_MAX_COUNT`

**提示（Prompt）**：最大发送重试次数（send retries）

**说明（Help）**

nrfs 通过 IPC 服务发送消息时，在报告错误前最多尝试重发的次数，例如共享 IPC 内存已满时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 100]
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/backends/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/backends/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → NRFS 后端设置（backend settings）

**配置项引用（Symbol References）**：[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_SWEXT_SERVICE_ENABLED"></a>

## 227.32 `CONFIG_NRFS_SWEXT_SERVICE_ENABLED`

**提示（Prompt）**：SWEXT 外设控制服务（peripheral control service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_SWEXT_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_POWER_DOMAIN_NRFS_SWEXT
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_SWEXT_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_SWEXT_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_POWER_DOMAIN_NRFS_SWEXT`](P138_drivers_power_domain_配置项参考.md#CONFIG_POWER_DOMAIN_NRFS_SWEXT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_SWEXT_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_TEMP_SERVICE_ENABLED"></a>

## 227.33 `CONFIG_NRFS_TEMP_SERVICE_ENABLED`

**提示（Prompt）**：温度服务（Temperature service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_TEMP_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_TEMP_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_TEMP_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_TEMP_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED"></a>

## 227.34 `CONFIG_NRFS_TEMP_SERVICE_SUBSCRIPTION_ENABLED`

**提示（Prompt）**：温度服务的订阅功能（Subscription feature）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_TEMP_SERVICE_HAS_SUBSCRIPTION_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_TEMP_SERVICE_HAS_SUBSCRIPTION_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_TEMP_SERVICE_HAS_SUBSCRIPTION_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_TEMP_SERVICE_HAS_SUBSCRIPTION_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFS_VBUS_DETECTOR_SERVICE_ENABLED"></a>

## 227.35 `CONFIG_NRFS_VBUS_DETECTOR_SERVICE_ENABLED`

**提示（Prompt）**：USB 外设的 VBUS 检测器（detector）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFS_HAS_VBUS_DETECTOR_SERVICE && CONFIG_NRFS && CONFIG_HAS_NRFS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_UDC_DWC2
```

**定义位置（Location）**：[`modules/hal_nordic/nrfs/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfs/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 已启用服务（Enabled Services）

**配置项引用（Symbol References）**：[`CONFIG_NRFS_HAS_VBUS_DETECTOR_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_VBUS_DETECTOR_SERVICE)、[`CONFIG_NRFS`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFS)、[`CONFIG_HAS_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFS)、[`CONFIG_UDC_DWC2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DWC2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFS_HAS_VBUS_DETECTOR_SERVICE`、`CONFIG_HAS_NRFS`。

<a id="CONFIG_NRFX_ADC"></a>

## 227.36 `CONFIG_NRFX_ADC`

**提示（Prompt）**：模数转换器（ADC）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n && CONFIG_SOC_SERIES_NRF51 && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_ADC_NRFX_ADC
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_ADC_NRFX_ADC`](P048_drivers_adc_配置项参考_2.md#CONFIG_ADC_NRFX_ADC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_ADC_LOG"></a>

## 227.37 `CONFIG_NRFX_ADC_LOG`

**提示（Prompt）**：模数转换器（ADC）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_ADC && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_ADC`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_ADC)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_BELLBOARD"></a>

## 227.38 `CONFIG_NRFX_BELLBOARD`

**提示（Prompt）**：BELLBOARD 驱动（driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK"></a>

## 227.39 `CONFIG_NRFX_CLOCK`

**提示（Prompt）**：时钟（CLOCK）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || n || n || n || n || n || n || n) && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_HFCLK"></a>

## 227.40 `CONFIG_NRFX_CLOCK_HFCLK`

**提示（Prompt）**：高频时钟（HFCLK）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF
CONFIG_CLOCK_CONTROL_NRF_HFCLK
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_CLOCK_CONTROL_NRF_HFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_HFCLK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_CLOCK_CONTROL_NRF_HFCLK`。

<a id="CONFIG_NRFX_CLOCK_HFCLK192M"></a>

## 227.41 `CONFIG_NRFX_CLOCK_HFCLK192M`

**提示（Prompt）**：192 MHz 高频时钟（HFCLK192M）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF
CONFIG_CLOCK_CONTROL_NRF_HFCLK192M
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_CLOCK_CONTROL_NRF_HFCLK192M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_HFCLK192M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_CLOCK_CONTROL_NRF_HFCLK192M`。

<a id="CONFIG_NRFX_CLOCK_HFCLKAUDIO"></a>

## 227.42 `CONFIG_NRFX_CLOCK_HFCLKAUDIO`

**提示（Prompt）**：音频高频时钟（HFCLKAUDIO）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF
CONFIG_CLOCK_CONTROL_NRF_HFCLKAUDIO
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_CLOCK_CONTROL_NRF_HFCLKAUDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_HFCLKAUDIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_CLOCK_CONTROL_NRF_HFCLKAUDIO`。

<a id="CONFIG_NRFX_CLOCK_LFCLK"></a>

## 227.43 `CONFIG_NRFX_CLOCK_LFCLK`

**提示（Prompt）**：低频时钟（LFCLK）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF
CONFIG_CLOCK_CONTROL_NRF_LFCLK
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<a id="CONFIG_NRFX_CLOCK_LFRC"></a>

## 227.44 `CONFIG_NRFX_CLOCK_LFRC`

**提示（Prompt）**：低频 RC 时钟（LFRC）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF
CONFIG_CLOCK_CONTROL_NRF_LFRC
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_CLOCK_CONTROL_NRF_LFRC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_LFRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED"></a>

## 227.45 `CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED`

**提示（Prompt）**：低频时钟两阶段启动序列（Two stage start sequence）［已弃用，DEPRECATED］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF && CONFIG_NRFX_CLOCK_LFCLK && CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL
CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING
CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_NRFX_CLOCK_LFCLK`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_CLOCK_LFCLK)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_LF_CAL_ENABLED"></a>

## 227.46 `CONFIG_NRFX_CLOCK_LF_CAL_ENABLED`

**提示（Prompt）**：低频 RC 时钟校准（LFRC Calibration）［已弃用，DEPRECATED］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF && CONFIG_NRFX_CLOCK_LFCLK && CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_NRFX_CLOCK_LFCLK`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_CLOCK_LFCLK)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_LF_SRC_FULL_SWING"></a>

## 227.47 `CONFIG_NRFX_CLOCK_LF_SRC_FULL_SWING`

**提示（Prompt）**：外部全摆幅（External full swing）［已弃用，DEPRECATED］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF52X && CONFIG_CLOCK_CONTROL_NRF && CONFIG_NRFX_CLOCK_LFCLK && CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52X)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_NRFX_CLOCK_LFCLK`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_CLOCK_LFCLK)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_LF_SRC_LOW_SWING"></a>

## 227.48 `CONFIG_NRFX_CLOCK_LF_SRC_LOW_SWING`

**提示（Prompt）**：外部低摆幅（External low swing）［已弃用，DEPRECATED］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_NRF52X && CONFIG_CLOCK_CONTROL_NRF && CONFIG_NRFX_CLOCK_LFCLK && CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52X)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_NRFX_CLOCK_LFCLK`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_CLOCK_LFCLK)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_LF_SRC_RC"></a>

## 227.49 `CONFIG_NRFX_CLOCK_LF_SRC_RC`

**提示（Prompt）**：RC 振荡器（RC Oscillator）［已弃用，DEPRECATED］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF && CONFIG_NRFX_CLOCK_LFCLK && CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_NRFX_CLOCK_LFCLK`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_CLOCK_LFCLK)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_LF_SRC_SYNTH"></a>

## 227.50 `CONFIG_NRFX_CLOCK_LF_SRC_SYNTH`

**提示（Prompt）**：由高频时钟合成（Synthesized from HFCLK）［已弃用，DEPRECATED］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_NRF91X && CONFIG_CLOCK_CONTROL_NRF && CONFIG_NRFX_CLOCK_LFCLK && CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_SYNTH
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91X)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_NRFX_CLOCK_LFCLK`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_CLOCK_LFCLK)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_SYNTH`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_SYNTH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_LF_SRC_XTAL"></a>

## 227.51 `CONFIG_NRFX_CLOCK_LF_SRC_XTAL`

**提示（Prompt）**：晶体振荡器（Crystal Oscillator）［已弃用，DEPRECATED］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_NRF && CONFIG_NRFX_CLOCK_LFCLK && CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_NRFX_CLOCK_LFCLK`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_CLOCK_LFCLK)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_LOG"></a>

## 227.52 `CONFIG_NRFX_CLOCK_LOG`

**提示（Prompt）**：时钟（CLOCK）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_CLOCK && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_CLOCK`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_CLOCK)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CLOCK_XO"></a>

## 227.53 `CONFIG_NRFX_CLOCK_XO`

**提示（Prompt）**：晶体振荡器（XO）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF
CONFIG_CLOCK_CONTROL_NRF_XO
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_CLOCK_CONTROL_NRF_XO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_XO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_CLOCK_CONTROL_NRF_XO`。

<a id="CONFIG_NRFX_CLOCK_XO24M"></a>

## 227.54 `CONFIG_NRFX_CLOCK_XO24M`

**提示（Prompt）**：24 MHz 晶体振荡器（XO24M）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || CONFIG_CLOCK_CONTROL_NRF) && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_CONTROL_NRF
CONFIG_CLOCK_CONTROL_NRF_XO24M
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_CLOCK_CONTROL_NRF_XO24M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_XO24M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_CLOCK_CONTROL_NRF_XO24M`。

<a id="CONFIG_NRFX_COMP"></a>

## 227.55 `CONFIG_NRFX_COMP`

**提示（Prompt）**：比较器（COMP）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_COMPARATOR_NRF_COMP
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_NRF_COMP`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_NRF_COMP)。

<a id="CONFIG_NRFX_COMP_LOG"></a>

## 227.56 `CONFIG_NRFX_COMP_LOG`

**提示（Prompt）**：比较器（COMP）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_COMP && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_COMP`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_COMP)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_CRACEN"></a>

## 227.57 `CONFIG_NRFX_CRACEN`

**提示（Prompt）**：CRACEN 驱动（drivers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_COMPATIBLE_NRF54LX || CONFIG_SOC_COMPATIBLE_NRF71) && CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_CRACEN_BSIM_SUPPORT if SOC_SERIES_BSIM_NRFXX
```

**被选择（Selected by）**

```text
CONFIG_ENTROPY_NRF_CRACEN_CTR_DRBG
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_COMPATIBLE_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF54LX)、[`CONFIG_SOC_COMPATIBLE_NRF71`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF71)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_CRACEN_BSIM_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CRACEN_BSIM_SUPPORT)、[`CONFIG_ENTROPY_NRF_CRACEN_CTR_DRBG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NRF_CRACEN_CTR_DRBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF54LX`、`CONFIG_SOC_COMPATIBLE_NRF71`、`CONFIG_HAS_NRFX`、`CONFIG_NRFX_CRACEN_BSIM_SUPPORT`。

<a id="CONFIG_NRFX_EGU"></a>

## 227.58 `CONFIG_NRFX_EGU`

**提示（Prompt）**：事件生成单元（EGU）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_EGU_LOG"></a>

## 227.59 `CONFIG_NRFX_EGU_LOG`

**提示（Prompt）**：事件生成单元（EGU）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_EGU && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_EGU`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_EGU)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_GPIOTE"></a>

## 227.60 `CONFIG_NRFX_GPIOTE`

**提示（Prompt）**：GPIO 任务与事件（GPIOTE）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_DISPLAY_NRF_LED_MATRIX
CONFIG_GPIO_NRFX_INTERRUPT
CONFIG_PWM_NRF_SW
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_DISPLAY_NRF_LED_MATRIX`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_NRF_LED_MATRIX)、[`CONFIG_GPIO_NRFX_INTERRUPT`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_NRFX_INTERRUPT)、[`CONFIG_PWM_NRF_SW`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_NRF_SW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_GPIOTE_LOG"></a>

## 227.61 `CONFIG_NRFX_GPIOTE_LOG`

**提示（Prompt）**：GPIO 任务与事件（GPIOTE）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_GPIOTE && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_GPIOTE`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_GPIOTE)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_GPIOTE_NUM_OF_EVT_HANDLERS"></a>

## 227.62 `CONFIG_NRFX_GPIOTE_NUM_OF_EVT_HANDLERS`

**提示（Prompt）**：事件处理程序数量（event handlers）

**说明（Help）**

指定用户可向 `nrfx_gpiote` 驱动注册的处理程序（handlers）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_GPIOTE && CONFIG_HAS_NRFX
```

**取值范围（Ranges）**

```text
[1, 15]
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_GPIOTE`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_GPIOTE)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_GPPI"></a>

## 227.63 `CONFIG_NRFX_GPPI`

**提示（Prompt）**：通用可编程外设互连层（Generic PPI layer）

**说明（Help）**

启用 `nrfx_gppi` 实用工具，提供跨 SoC 系列创建可编程外设互连（PPI）连接的统一 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_NRF_SYS_EVENT_USE_GPPI
CONFIG_SOC_NRF53_RTC_PRETICK
CONFIG_NRF53_SYNC_RTC
CONFIG_COUNTER_RTC_WITH_PPI_WRAP
CONFIG_DISPLAY_NRF_LED_MATRIX
CONFIG_PWM_NRF_SW
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_0_ENHANCED_POLL_OUT
CONFIG_UART_1_ENHANCED_POLL_OUT
CONFIG_UART_2_ENHANCED_POLL_OUT
CONFIG_UART_3_ENHANCED_POLL_OUT
CONFIG_UART_00_ENHANCED_POLL_OUT
CONFIG_UART_20_ENHANCED_POLL_OUT
CONFIG_UART_21_ENHANCED_POLL_OUT
CONFIG_UART_22_ENHANCED_POLL_OUT
CONFIG_UART_23_ENHANCED_POLL_OUT
CONFIG_UART_24_ENHANCED_POLL_OUT
CONFIG_UART_30_ENHANCED_POLL_OUT
CONFIG_UART_120_ENHANCED_POLL_OUT
CONFIG_UART_130_ENHANCED_POLL_OUT
CONFIG_UART_131_ENHANCED_POLL_OUT
CONFIG_UART_132_ENHANCED_POLL_OUT
CONFIG_UART_133_ENHANCED_POLL_OUT
CONFIG_UART_134_ENHANCED_POLL_OUT
CONFIG_UART_135_ENHANCED_POLL_OUT
CONFIG_UART_136_ENHANCED_POLL_OUT
CONFIG_UART_137_ENHANCED_POLL_OUT
CONFIG_NRF_RTC_TIMER
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRF_SYS_EVENT_USE_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_SYS_EVENT_USE_GPPI)、[`CONFIG_SOC_NRF53_RTC_PRETICK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF53_RTC_PRETICK)、[`CONFIG_NRF53_SYNC_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF53_SYNC_RTC)、[`CONFIG_COUNTER_RTC_WITH_PPI_WRAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_RTC_WITH_PPI_WRAP)、[`CONFIG_DISPLAY_NRF_LED_MATRIX`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_NRF_LED_MATRIX)、[`CONFIG_PWM_NRF_SW`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_NRF_SW)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_0_ENHANCED_POLL_OUT`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_0_ENHANCED_POLL_OUT)、[`CONFIG_UART_1_ENHANCED_POLL_OUT`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_1_ENHANCED_POLL_OUT)、[`CONFIG_UART_2_ENHANCED_POLL_OUT`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_2_ENHANCED_POLL_OUT)、[`CONFIG_UART_3_ENHANCED_POLL_OUT`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_3_ENHANCED_POLL_OUT)、[`CONFIG_UART_00_ENHANCED_POLL_OUT`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_00_ENHANCED_POLL_OUT)、[`CONFIG_UART_20_ENHANCED_POLL_OUT`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_20_ENHANCED_POLL_OUT)、[`CONFIG_UART_21_ENHANCED_POLL_OUT`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_21_ENHANCED_POLL_OUT)、[`CONFIG_UART_22_ENHANCED_POLL_OUT`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_22_ENHANCED_POLL_OUT)、[`CONFIG_UART_23_ENHANCED_POLL_OUT`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_23_ENHANCED_POLL_OUT)、[`CONFIG_UART_24_ENHANCED_POLL_OUT`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_24_ENHANCED_POLL_OUT)、[`CONFIG_UART_30_ENHANCED_POLL_OUT`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_30_ENHANCED_POLL_OUT)、[`CONFIG_UART_120_ENHANCED_POLL_OUT`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_120_ENHANCED_POLL_OUT)、[`CONFIG_UART_130_ENHANCED_POLL_OUT`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_130_ENHANCED_POLL_OUT)、[`CONFIG_UART_131_ENHANCED_POLL_OUT`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_131_ENHANCED_POLL_OUT)、[`CONFIG_UART_132_ENHANCED_POLL_OUT`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_132_ENHANCED_POLL_OUT)、[`CONFIG_UART_133_ENHANCED_POLL_OUT`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_133_ENHANCED_POLL_OUT)、[`CONFIG_UART_134_ENHANCED_POLL_OUT`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_134_ENHANCED_POLL_OUT)、[`CONFIG_UART_135_ENHANCED_POLL_OUT`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_135_ENHANCED_POLL_OUT)、[`CONFIG_UART_136_ENHANCED_POLL_OUT`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_136_ENHANCED_POLL_OUT)、[`CONFIG_UART_137_ENHANCED_POLL_OUT`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_137_ENHANCED_POLL_OUT)、[`CONFIG_NRF_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_RTC_TIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRF_SYS_EVENT_USE_GPPI`、`CONFIG_COUNTER_RTC_WITH_PPI_WRAP`。

<a id="CONFIG_NRFX_GPPI_EXT_ALLOCATOR"></a>

## 227.64 `CONFIG_NRFX_GPPI_EXT_ALLOCATOR`

**提示（Prompt）**：外部 GPPI 分配器（allocator）

**说明（Help）**

表示已提供 GPPI 分配与释放函数（allocation and freeing functions）的外部实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_GPPI_EXT_ALLOCATOR_CLI
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_GPPI_EXT_ALLOCATOR_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPPI_EXT_ALLOCATOR_CLI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_GPPI_SD2PPI_GLOBAL"></a>

## 227.65 `CONFIG_NRFX_GPPI_SD2PPI_GLOBAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示用于安全多域 DPPI（Secure multi-Domain DPPI，`SD^2PPI`）架构的 GPPI 实现。`SD^2PPI` 架构使用多个 DPPI 控制器实例和 IronSide 服务，配置 PPI 资源的安全性与所有权（security and ownership）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_GPPI && CONFIG_HAS_NRFX
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPUPPR
CONFIG_SOC_NRF54H20_CPUFLPR
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 通用可编程外设互连层（Generic PPI layer）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_GPPI`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_GPPI)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPUPPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUPPR)、[`CONFIG_SOC_NRF54H20_CPUFLPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUFLPR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`。

<a id="CONFIG_NRFX_GRTC"></a>

## 227.66 `CONFIG_NRFX_GRTC`

**提示（Prompt）**：全局实时时钟（GRTC）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_NRF_GRTC_TIMER
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)。

<a id="CONFIG_NRFX_GRTC_LOG"></a>

## 227.67 `CONFIG_NRFX_GRTC_LOG`

**提示（Prompt）**：全局实时时钟（GRTC）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_GRTC && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_GRTC`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_GRTC)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_I2S"></a>

## 227.68 `CONFIG_NRFX_I2S`

**提示（Prompt）**：芯片间音频接口（I2S）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_I2S_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_I2S_NRFX`](P107_drivers_i2s_配置项参考.md#CONFIG_I2S_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_I2S_LOG"></a>

## 227.69 `CONFIG_NRFX_I2S_LOG`

**提示（Prompt）**：芯片间音频接口（I2S）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_I2S && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_I2S`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_I2S)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_IPC"></a>

## 227.70 `CONFIG_NRFX_IPC`

**提示（Prompt）**：进程间通信（IPC）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_IPM_NRFX
CONFIG_MBOX_NRFX_IPC
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_MBOX_NRFX_IPC`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_NRFX_IPC)。

<a id="CONFIG_NRFX_IPC_LOG"></a>

## 227.71 `CONFIG_NRFX_IPC_LOG`

**提示（Prompt）**：进程间通信（IPC）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_IPC && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_IPC`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_IPC)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_KMU"></a>

## 227.72 `CONFIG_NRFX_KMU`

**提示（Prompt）**：密钥管理单元（Key Management Unit）驱动

**说明（Help）**

启用 `nrfx_kmu` 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_LPCOMP"></a>

## 227.73 `CONFIG_NRFX_LPCOMP`

**提示（Prompt）**：低功耗比较器（LPCOMP）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n && !CONFIG_SOC_NRF52810 && !CONFIG_SOC_NRF52811 && !CONFIG_SOC_NRF52820 && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_COMPARATOR_NRF_LPCOMP
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF52810`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52810)、[`CONFIG_SOC_NRF52811`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52811)、[`CONFIG_SOC_NRF52820`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52820)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_COMPARATOR_NRF_LPCOMP`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_NRF_LPCOMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF52810`、`CONFIG_SOC_NRF52811`、`CONFIG_SOC_NRF52820`、`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_LPCOMP_LOG"></a>

## 227.74 `CONFIG_NRFX_LPCOMP_LOG`

**提示（Prompt）**：低功耗比较器（LPCOMP）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_LPCOMP && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_LPCOMP`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_LPCOMP)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_MRAMC"></a>

## 227.75 `CONFIG_NRFX_MRAMC`

**提示（Prompt）**：MRAMC 驱动（driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || n) && CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF7120_WICR_SETUP
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_FLASH_NRF_MRAMC
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_SOC_NRF7120_WICR_SETUP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_WICR_SETUP)、[`CONFIG_SOC_FLASH_NRF_MRAMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAMC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_MRAMC_LOG"></a>

## 227.76 `CONFIG_NRFX_MRAMC_LOG`

**提示（Prompt）**：MRAMC 驱动日志（driver logging）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_MRAMC && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_MRAMC`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_MRAMC)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_NFCT"></a>

## 227.77 `CONFIG_NRFX_NFCT`

**提示（Prompt）**：近场通信标签（NFCT）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_NRFX_TIMER
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_TIMER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_TIMER)。

<a id="CONFIG_NRFX_NFCT_LOG"></a>

## 227.78 `CONFIG_NRFX_NFCT_LOG`

**提示（Prompt）**：近场通信标签（NFCT）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_NFCT && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_NFCT`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_NFCT)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_NVMC"></a>

## 227.79 `CONFIG_NRFX_NVMC`

**提示（Prompt）**：非易失性存储控制器（NVMC）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_NRF
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)。

<a id="CONFIG_NRFX_NVMC_LOG"></a>

## 227.80 `CONFIG_NRFX_NVMC_LOG`

**提示（Prompt）**：非易失性存储控制器（NVMC）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_NVMC && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_NVMC`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_NVMC)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_PDM"></a>

## 227.81 `CONFIG_NRFX_PDM`

**提示（Prompt）**：脉冲密度调制（PDM）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_AUDIO_DMIC_NRFX_PDM
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:183`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L183)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_AUDIO_DMIC_NRFX_PDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_NRFX_PDM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_PDM_LOG"></a>

## 227.82 `CONFIG_NRFX_PDM_LOG`

**提示（Prompt）**：脉冲密度调制（PDM）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_PDM && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_PDM`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_PDM)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_POWER"></a>

## 227.83 `CONFIG_NRFX_POWER`

**提示（Prompt）**：电源（POWER）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_NRFX_USBREG
```

**被选择（Selected by）**

```text
CONFIG_NRF_SYS_EVENT
CONFIG_UDC_NRF
CONFIG_USB_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_USBREG`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRFX_USBREG)、[`CONFIG_NRF_SYS_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_SYS_EVENT)、[`CONFIG_UDC_NRF`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NRF)、[`CONFIG_USB_NRFX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_NRFX)。

<a id="CONFIG_NRFX_POWER_LOG"></a>

## 227.84 `CONFIG_NRFX_POWER_LOG`

**提示（Prompt）**：电源（POWER）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_POWER && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_POWER`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_POWER)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_PRS_BOX_0"></a>

## 227.85 `CONFIG_NRFX_PRS_BOX_0`

**提示（Prompt）**：外设资源共享（PRS）盒 0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:294`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L294)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_BOX_1"></a>

## 227.86 `CONFIG_NRFX_PRS_BOX_1`

**提示（Prompt）**：外设资源共享（PRS）盒 1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L298)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_BOX_2"></a>

## 227.87 `CONFIG_NRFX_PRS_BOX_2`

**提示（Prompt）**：外设资源共享（PRS）盒 2

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:302`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L302)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_BOX_3"></a>

## 227.88 `CONFIG_NRFX_PRS_BOX_3`

**提示（Prompt）**：外设资源共享（PRS）盒 3

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:306`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L306)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_BOX_4"></a>

## 227.89 `CONFIG_NRFX_PRS_BOX_4`

**提示（Prompt）**：外设资源共享（PRS）盒 4

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:310`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L310)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_BOX_5"></a>

## 227.90 `CONFIG_NRFX_PRS_BOX_5`

**提示（Prompt）**：外设资源共享（PRS）盒 5

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L314)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_BOX_6"></a>

## 227.91 `CONFIG_NRFX_PRS_BOX_6`

**提示（Prompt）**：外设资源共享（PRS）盒 6

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:318`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L318)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_BOX_7"></a>

## 227.92 `CONFIG_NRFX_PRS_BOX_7`

**提示（Prompt）**：外设资源共享（PRS）盒 7

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:322`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L322)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_BOX_8"></a>

## 227.93 `CONFIG_NRFX_PRS_BOX_8`

**提示（Prompt）**：外设资源共享（PRS）盒 8

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:326`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L326)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_BOX_9"></a>

## 227.94 `CONFIG_NRFX_PRS_BOX_9`

**提示（Prompt）**：外设资源共享（PRS）盒 9

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PRS
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:330`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L330)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → 外设资源共享模块（Peripheral Resource Sharing module）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_NRFX_PRS`。

<a id="CONFIG_NRFX_PRS_LOG"></a>

## 227.95 `CONFIG_NRFX_PRS_LOG`

**提示（Prompt）**：外设资源共享（PRS）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_PRS && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_PRS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PRS)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRFX_PRS`、`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_PWM"></a>

## 227.96 `CONFIG_NRFX_PWM`

**提示（Prompt）**：脉宽调制（PWM）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_PWM_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_PWM_NRFX`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_PWM_LOG"></a>

## 227.97 `CONFIG_NRFX_PWM_LOG`

**提示（Prompt）**：脉宽调制（PWM）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_PWM && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_PWM`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_PWM)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_QDEC"></a>

## 227.98 `CONFIG_NRFX_QDEC`

**提示（Prompt）**：正交解码器（QDEC）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX
```

**被选择（Selected by）**

```text
CONFIG_QDEC_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_QDEC_NRFX`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QDEC_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_QDEC_LOG"></a>

## 227.99 `CONFIG_NRFX_QDEC_LOG`

**提示（Prompt）**：正交解码器（QDEC）驱动日志

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRFX_QDEC && CONFIG_LOG && CONFIG_HAS_NRFX
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig.logging:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig.logging#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers） → nrfx 驱动日志（drivers logging）

**配置项引用（Symbol References）**：[`CONFIG_NRFX_QDEC`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_NRFX_QDEC)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`。

<a id="CONFIG_NRFX_QSPI"></a>

## 227.100 `CONFIG_NRFX_QSPI`

**提示（Prompt）**：四线串行外设接口（QSPI）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_NRF70_ON_QSPI
CONFIG_NRF70_ON_QSPI
CONFIG_NORDIC_QSPI_NOR
```

**定义位置（Location）**：[`modules/hal_nordic/nrfx/Kconfig:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_nordic/nrfx/Kconfig#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nrfx 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_ON_QSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_ON_QSPI)、[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRF70_ON_QSPI`。

<!-- kconfig-navigation -->

[上一章](P226_modules_hal_infineon_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P228_modules_hal_nordic_配置项参考_2.md)
