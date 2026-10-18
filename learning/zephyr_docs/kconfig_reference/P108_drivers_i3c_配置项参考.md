---
id: learning.zephyr-docs.kconfig-reference.page-108
title: "`drivers/i3c`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第108章\_`drivers/i3c`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/i3c` 的 58 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_I3C"></a>

## 108.1 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_I3C`

**提示（Prompt）**：I³C 堆内存池大小（Heap Memory Pool Size）

**说明（Help）**

I³C 使用的内存池大小。仅用于 DEFTGTS（定义目标设备列表，Define List of Targets）通用命令码（Common Command Code，CCC）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_CONTROLLER && CONFIG_I3C_TARGET && CONFIG_I3C
```

**默认值（Defaults）**

```text
48
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_I3C_TARGET`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_TARGET)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C"></a>

## 108.2 `CONFIG_I3C`

**提示（Prompt）**：改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**说明（Help）**

启用 I³C 驱动配置（Driver Configuration）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_LPS2XDF
CONFIG_LSM6DSV16X
CONFIG_LSM6DSVXXX
CONFIG_ICM45686
CONFIG_ICM566XX
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LPS2XDF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPS2XDF)、[`CONFIG_LSM6DSV16X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X)、[`CONFIG_LSM6DSVXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSVXXX)、[`CONFIG_ICM45686`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM45686)、[`CONFIG_ICM566XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM566XX)。

<a id="CONFIG_I3CM_IT51XXX"></a>

## 108.3 `CONFIG_I3CM_IT51XXX`

**提示（Prompt）**：it51xxx i3cm 驱动

**说明（Help）**

启用 it51xxx I³C 控制器（Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_I3CM_ENABLED && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I3C_IBI_WORKQUEUE if CONFIG_I3C_USE_IBI
CONFIG_SOC_IT51XXX_CPU_IDLE_GATING
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_SOC_IT51XXX_CPU_IDLE_GATING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX_CPU_IDLE_GATING)。

<a id="CONFIG_I3CM_IT51XXX_DLM_SIZE"></a>

## 108.4 `CONFIG_I3CM_IT51XXX_DLM_SIZE`

**提示（Prompt）**：it51xxx i3cm DLM 数据大小

**说明（Help）**

设置 i3cm 数据局部存储器（Data-local-memory，DLM）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3CM_IT51XXX && CONFIG_I3CM_IT51XXX && CONFIG_I3C
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cm 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3CM_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CM_IT51XXX)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3CM_IT51XXX_TRANSFER_TIMEOUT_MS"></a>

## 108.5 `CONFIG_I3CM_IT51XXX_TRANSFER_TIMEOUT_MS`

**提示（Prompt）**：设置传输超时，单位为毫秒。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3CM_IT51XXX && CONFIG_I3C
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cm 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3CM_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CM_IT51XXX)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3CS_IT51XXX"></a>

## 108.6 `CONFIG_I3CS_IT51XXX`

**提示（Prompt）**：it51xxx i3cs 驱动

**说明（Help）**

启用 it51xxx I³C 目标设备（Target）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_I3CS_ENABLED && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I3C_TARGET_BUFFER_MODE
CONFIG_SOC_IT51XXX_CPU_IDLE_GATING
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I3C_TARGET_BUFFER_MODE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_TARGET_BUFFER_MODE)、[`CONFIG_SOC_IT51XXX_CPU_IDLE_GATING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX_CPU_IDLE_GATING)。

<a id="CONFIG_I3CS_IT51XXX_IBI_TIMEOUT_MS"></a>

## 108.7 `CONFIG_I3CS_IT51XXX_IBI_TIMEOUT_MS`

**提示（Prompt）**：设置带内中断（IBI）超时时间，单位为毫秒。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3CS_IT51XXX && CONFIG_I3C
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3CS_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_IT51XXX)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3CS_IT51XXX_RX_FIFO_SIZE"></a>

## 108.8 `CONFIG_I3CS_IT51XXX_RX_FIFO_SIZE`

**提示（Prompt）**：it51xxx i3cs 接收 FIFO 大小

**说明（Help）**

设置 i3cs 接收（RX）先入先出队列（FIFO）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3CS_IT51XXX && CONFIG_I3C
```

**默认值（Defaults）**

```text
16 if CONFIG_I3CS_RX_FIFO_16_BYTE
32 if CONFIG_I3CS_RX_FIFO_32_BYTE
64 if CONFIG_I3CS_RX_FIFO_64_BYTE
128 if CONFIG_I3CS_RX_FIFO_128_BYTE
4096 if CONFIG_I3CS_RX_FIFO_4096_BYTE
16
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3CS_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_IT51XXX)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3CS_RX_FIFO_16_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_RX_FIFO_16_BYTE)、[`CONFIG_I3CS_RX_FIFO_32_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_RX_FIFO_32_BYTE)、[`CONFIG_I3CS_RX_FIFO_64_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_RX_FIFO_64_BYTE)、[`CONFIG_I3CS_RX_FIFO_128_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_RX_FIFO_128_BYTE)、[`CONFIG_I3CS_RX_FIFO_4096_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_RX_FIFO_4096_BYTE)。

<a id="CONFIG_I3CS_IT51XXX_TX_FIFO_SIZE"></a>

## 108.9 `CONFIG_I3CS_IT51XXX_TX_FIFO_SIZE`

**提示（Prompt）**：it51xxx i3cs 发送 FIFO 大小

**说明（Help）**

设置 i3cs 发送（TX）先入先出队列（FIFO）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3CS_IT51XXX && CONFIG_I3C
```

**默认值（Defaults）**

```text
16 if CONFIG_I3CS_TX_FIFO_16_BYTE
32 if CONFIG_I3CS_TX_FIFO_32_BYTE
64 if CONFIG_I3CS_TX_FIFO_64_BYTE
128 if CONFIG_I3CS_TX_FIFO_128_BYTE
4096 if CONFIG_I3CS_TX_FIFO_4096_BYTE
16
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3CS_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_IT51XXX)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3CS_TX_FIFO_16_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_TX_FIFO_16_BYTE)、[`CONFIG_I3CS_TX_FIFO_32_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_TX_FIFO_32_BYTE)、[`CONFIG_I3CS_TX_FIFO_64_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_TX_FIFO_64_BYTE)、[`CONFIG_I3CS_TX_FIFO_128_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_TX_FIFO_128_BYTE)、[`CONFIG_I3CS_TX_FIFO_4096_BYTE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_TX_FIFO_4096_BYTE)。

<a id="CONFIG_I3CS_RX_FIFO_128_BYTE"></a>

## 108.10 `CONFIG_I3CS_RX_FIFO_128_BYTE`

**提示（Prompt）**：128

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 接收 FIFO 大小

<a id="CONFIG_I3CS_RX_FIFO_16_BYTE"></a>

## 108.11 `CONFIG_I3CS_RX_FIFO_16_BYTE`

**提示（Prompt）**：16

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 接收 FIFO 大小

<a id="CONFIG_I3CS_RX_FIFO_32_BYTE"></a>

## 108.12 `CONFIG_I3CS_RX_FIFO_32_BYTE`

**提示（Prompt）**：32

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 接收 FIFO 大小

<a id="CONFIG_I3CS_RX_FIFO_4096_BYTE"></a>

## 108.13 `CONFIG_I3CS_RX_FIFO_4096_BYTE`

**提示（Prompt）**：4096

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 接收 FIFO 大小

<a id="CONFIG_I3CS_RX_FIFO_64_BYTE"></a>

## 108.14 `CONFIG_I3CS_RX_FIFO_64_BYTE`

**提示（Prompt）**：64

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 接收 FIFO 大小

<a id="CONFIG_I3CS_TX_FIFO_128_BYTE"></a>

## 108.15 `CONFIG_I3CS_TX_FIFO_128_BYTE`

**提示（Prompt）**：128

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 发送 FIFO 大小

<a id="CONFIG_I3CS_TX_FIFO_16_BYTE"></a>

## 108.16 `CONFIG_I3CS_TX_FIFO_16_BYTE`

**提示（Prompt）**：16

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 发送 FIFO 大小

<a id="CONFIG_I3CS_TX_FIFO_32_BYTE"></a>

## 108.17 `CONFIG_I3CS_TX_FIFO_32_BYTE`

**提示（Prompt）**：32

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 发送 FIFO 大小

<a id="CONFIG_I3CS_TX_FIFO_4096_BYTE"></a>

## 108.18 `CONFIG_I3CS_TX_FIFO_4096_BYTE`

**提示（Prompt）**：4096

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 发送 FIFO 大小

<a id="CONFIG_I3CS_TX_FIFO_64_BYTE"></a>

## 108.19 `CONFIG_I3CS_TX_FIFO_64_BYTE`

**提示（Prompt）**：64

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cs 驱动 → 选择 i3cs 发送 FIFO 大小

<a id="CONFIG_I3C_CADENCE"></a>

## 108.20 `CONFIG_I3C_CADENCE`

**提示（Prompt）**：Cadence I³C 驱动

**说明（Help）**

启用 Cadence I³C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDNS_I3C_ENABLED && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I3C_IBI_WORKQUEUE if CONFIG_I3C_USE_IBI && CONFIG_I3C_CONTROLLER
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.cdns:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.cdns#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)。

<a id="CONFIG_I3C_CADENCE_IDLE_TIMEOUT_US"></a>

## 108.21 `CONFIG_I3C_CADENCE_IDLE_TIMEOUT_US`

**提示（Prompt）**：I³C 空闲超时（Idle Timeout，微秒）

**说明（Help）**

等待进入 I³C 空闲状态的超时时间。I³C 外设的状态机（State Machine）比较特殊：传输结束后，可能暂时还未进入空闲状态，并在进入空闲之前又进行一次传输。必须等待它回到空闲状态，才能开始另一次传输。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_CADENCE && CONFIG_I3C
```

**默认值（Defaults）**

```text
250
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.cdns:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.cdns#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → Cadence I³C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_CADENCE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CADENCE)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_CADENCE_TRANSFER_TIMEOUT_MARGIN_US"></a>

## 108.22 `CONFIG_I3C_CADENCE_TRANSFER_TIMEOUT_MARGIN_US`

**提示（Prompt）**：I³C 传输超时余量（Transfer Timeout Margin，微秒）

**说明（Help）**

计算传输完成超时时，在算出的传输时间基础上增加的额外余量，单位为微秒。基础超时时间由待传输位数和 SCL 频率推导。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_CADENCE && CONFIG_I3C
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.cdns:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.cdns#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → Cadence I³C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_CADENCE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CADENCE)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_CALLBACK"></a>

## 108.23 `CONFIG_I3C_CALLBACK`

**提示（Prompt）**：I³C 异步回调（Asynchronous Callback）API

**说明（Help）**

`i3c_transfer_cb` 和 `i3c_do_ccc_cb` 的 API 及实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_CONTROLLER && CONFIG_I3C
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_CONTROLLER"></a>

## 108.24 `CONFIG_I3C_CONTROLLER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示已启用作为 I³C 控制器（Controller）的支持。此内部选项根据 I³C 模式选择（`I3C_CONTROLLER_ROLE_ONLY` 或 `I3C_DUAL_ROLE`）自动推导，不应直接设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C
```

**默认值（Defaults）**

```text
y if CONFIG_I3C_DUAL_ROLE || CONFIG_I3C_CONTROLLER_ROLE_ONLY
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_DUAL_ROLE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_DUAL_ROLE)、[`CONFIG_I3C_CONTROLLER_ROLE_ONLY`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER_ROLE_ONLY)。

<a id="CONFIG_I3C_CONTROLLER_INIT_PRIORITY"></a>

## 108.25 `CONFIG_I3C_CONTROLLER_INIT_PRIORITY`

**提示（Prompt）**：I³C 控制器初始化优先级（Initialization Priority）

**说明（Help）**

用于建立 I³C 控制器设备驱动实例，并执行总线初始化，例如动态地址分配（Dynamic Address Assignment）。注意，必须先完成这些操作，然后连接到总线的 I²C 和 I³C 设备驱动实例才能开始初始化各自设备，因为某些设备在控制器分配地址之前可能无法寻址。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_CONTROLLER_ROLE_ONLY"></a>

## 108.26 `CONFIG_I3C_CONTROLLER_ROLE_ONLY`

**提示（Prompt）**：仅 I³C 控制器（Controller）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MODE>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I³C 模式选择（Mode Selection）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MODE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_MODE)。

<a id="CONFIG_I3C_DUAL_ROLE"></a>

## 108.27 `CONFIG_I3C_DUAL_ROLE`

**提示（Prompt）**：同时支持 I³C 控制器（Controller）与目标设备（Target）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MODE>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I³C 模式选择（Mode Selection）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MODE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_MODE)。

<a id="CONFIG_I3C_DW"></a>

## 108.28 `CONFIG_I3C_DW`

**提示（Prompt）**：DW I³C 支持

**说明（Help）**

启用 Synopsys DesignWare I³C 驱动。支持上游 `snps,designware-i3c` 兼容项，以及 Microchip XEC 变体 `microchip,xec-i3c`。后者是在相同 IP 外增加 XEC 包装层（Wrapper），提供 ECIA 中断路由和 `HOST_CFG` 端口选择寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SNPS_DESIGNWARE_I3C_ENABLED || DT_HAS_MICROCHIP_XEC_I3C_ENABLED) && CONFIG_CLOCK_CONTROL && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I3C_IBI_WORKQUEUE if CONFIG_I3C_USE_IBI && CONFIG_I3C_CONTROLLER
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.dw:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.dw#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)。

<a id="CONFIG_I3C_DW_RW_TIMEOUT_MS"></a>

## 108.29 `CONFIG_I3C_DW_RW_TIMEOUT_MS`

**提示（Prompt）**：设置读写超时（Read/Write Timeout），单位为毫秒。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_DW && CONFIG_I3C
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.dw:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.dw#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → DW I³C 支持

**配置项引用（Symbol References）**：[`CONFIG_I3C_DW`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_DW)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_I2C_NUM_OF_DESC_MEM_SLABS"></a>

## 108.30 `CONFIG_I3C_I2C_NUM_OF_DESC_MEM_SLABS`

**提示（Prompt）**：I²C 设备描述符内存块（Mem Slab）数量

**说明（Help）**

通过 DEFTGTS 发现不在已知 I²C 设备列表中的设备时，用于分配描述符的固定大小内存块（Memory Slab）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_CONTROLLER && CONFIG_I3C_TARGET && CONFIG_I3C
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_I3C_TARGET`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_TARGET)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE"></a>

## 108.31 `CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE`

**提示（Prompt）**：最大带内中断有效载荷大小（Maximum IBI Payload Size）

**说明（Help）**

最大带内中断（IBI）有效载荷大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_USE_IBI && CONFIG_I3C
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → 使用带内中断（In-Band Interrupt，IBI）

**配置项引用（Symbol References）**：[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_IBI_WORKQUEUE"></a>

## 108.32 `CONFIG_I3C_IBI_WORKQUEUE`

**提示（Prompt）**：使用 IBI 工作队列（Workqueue）

**说明（Help）**

使用全局工作队列处理带内中断（IBI）。需要时由驱动启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_USE_IBI && CONFIG_I3C
```

**被选择（Selected by）**

```text
CONFIG_I3C_CADENCE
CONFIG_I3C_DW
CONFIG_I3CM_IT51XXX
CONFIG_I3C_MAX32
CONFIG_I3C_NPCX
CONFIG_I3C_MCUX
CONFIG_I3C_STM32
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → 使用带内中断（In-Band Interrupt，IBI）

**配置项引用（Symbol References）**：[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_CADENCE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CADENCE)、[`CONFIG_I3C_DW`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_DW)、[`CONFIG_I3CM_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CM_IT51XXX)、[`CONFIG_I3C_MAX32`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_MAX32)、[`CONFIG_I3C_NPCX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_NPCX)、[`CONFIG_I3C_MCUX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_MCUX)、[`CONFIG_I3C_STM32`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_STM32)。

<a id="CONFIG_I3C_IBI_WORKQUEUE_LENGTH"></a>

## 108.33 `CONFIG_I3C_IBI_WORKQUEUE_LENGTH`

**提示（Prompt）**：IBI 工作队列长度（Queue Length）

**说明（Help）**

定义工作队列中可排队的带内中断（IBI）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_IBI_WORKQUEUE && CONFIG_I3C_USE_IBI && CONFIG_I3C
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → 使用带内中断（In-Band Interrupt，IBI） → 使用 IBI 工作队列（Workqueue）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_IBI_WORKQUEUE_PRIORITY"></a>

## 108.34 `CONFIG_I3C_IBI_WORKQUEUE_PRIORITY`

**提示（Prompt）**：IBI 工作队列线程优先级（Thread Priority）

**说明（Help）**

IBI 全局工作队列的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_IBI_WORKQUEUE && CONFIG_I3C_USE_IBI && CONFIG_I3C
```

**默认值（Defaults）**

```text
-1
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → 使用带内中断（In-Band Interrupt，IBI） → 使用 IBI 工作队列（Workqueue）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_IBI_WORKQUEUE_STACK_SIZE"></a>

## 108.35 `CONFIG_I3C_IBI_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：IBI 工作队列栈大小（Stack Size）

**说明（Help）**

IBI 全局工作队列的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_IBI_WORKQUEUE && CONFIG_I3C_USE_IBI && CONFIG_I3C
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → 使用带内中断（In-Band Interrupt，IBI） → 使用 IBI 工作队列（Workqueue）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_IBI_WORKQUEUE_VERBOSE_DEBUG"></a>

## 108.36 `CONFIG_I3C_IBI_WORKQUEUE_VERBOSE_DEBUG`

**提示（Prompt）**：IBI 工作队列的详细调试消息（Verbose Debug Messages）

**说明（Help）**

日志级别设为 DEBUG 时，此选项启用 IBI 工作队列的详细调试输出，并打印 IBI 有效载荷（Payload）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_IBI_WORKQUEUE && CONFIG_I3C_USE_IBI && CONFIG_I3C
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → 使用带内中断（In-Band Interrupt，IBI） → 使用 IBI 工作队列（Workqueue）

**配置项引用（Symbol References）**：[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_INIT_RSTACT"></a>

## 108.37 `CONFIG_I3C_INIT_RSTACT`

**提示（Prompt）**：在总线初始化期间执行复位操作（Reset Action）

**说明（Help）**

此选项决定总线初始化例程是否向 I³C 目标设备发送复位操作命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_MAX32"></a>

## 108.38 `CONFIG_I3C_MAX32`

**提示（Prompt）**：Analog Devices MAX32 I³C 驱动

**说明（Help）**

MAX32 SoC 系列的 I³C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_I3C_ENABLED && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I3C_IBI_WORKQUEUE if CONFIG_I3C_USE_IBI
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.max32:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.max32#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)。

<a id="CONFIG_I3C_MCUX"></a>

## 108.39 `CONFIG_I3C_MCUX`

**提示（Prompt）**：MCUX I³C 驱动

**说明（Help）**

启用 MCUX I³C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX && DT_HAS_NXP_MCUX_I3C_ENABLED && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I3C_IBI_WORKQUEUE if CONFIG_I3C_USE_IBI
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.nxp:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.nxp#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_I3C_MODE"></a>

## 108.40 `CONFIG_I3C_MODE`

**提示（Prompt）**：I³C 模式选择（Mode Selection）

**说明（Help）**

选择 I³C 启用的角色。必须至少启用控制器（Controller）或目标设备（Target）之一。仅选择一种角色可减少代码占用（Code Footprint）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C
```

**默认值（Defaults）**

```text
CONFIG_I3C_DUAL_ROLE
```

**可选项（Choices）**

```text
CONFIG_I3C_CONTROLLER_ROLE_ONLY
CONFIG_I3C_TARGET_ROLE_ONLY
CONFIG_I3C_DUAL_ROLE
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_DUAL_ROLE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_DUAL_ROLE)、[`CONFIG_I3C_CONTROLLER_ROLE_ONLY`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER_ROLE_ONLY)、[`CONFIG_I3C_TARGET_ROLE_ONLY`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_TARGET_ROLE_ONLY)。

<a id="CONFIG_I3C_NPCX"></a>

## 108.41 `CONFIG_I3C_NPCX`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（Embedded Controller，EC）I³C 驱动

**说明（Help）**

此选项启用 NPCX 系列处理器的 I³C 驱动。如需使用 NPCX MCU 上的 I³C 通道，请选 y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_I3C_ENABLED && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
CONFIG_I3C_IBI_WORKQUEUE if CONFIG_I3C_USE_IBI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.npcx:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.npcx#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I3C_NPCX_DMA"></a>

## 108.42 `CONFIG_I3C_NPCX_DMA`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（EC）串行驱动 DMA 支持

**说明（Help）**

启用 NPCX I³C DMA 模式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_NPCX && "0x0" != 0 && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I3C_TARGET_BUFFER_MODE
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.npcx:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.npcx#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → Nuvoton NPCX 嵌入式控制器（Embedded Controller，EC）I³C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_NPCX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_NPCX)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_TARGET_BUFFER_MODE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_TARGET_BUFFER_MODE)。

<a id="CONFIG_I3C_NUM_OF_DESC_MEM_SLABS"></a>

## 108.43 `CONFIG_I3C_NUM_OF_DESC_MEM_SLABS`

**提示（Prompt）**：I³C 设备描述符内存块（Mem Slab）数量

**说明（Help）**

通过 ENTDAA 或 DEFTGTS 发现不在已知 I³C 设备列表中的设备时，用于分配描述符的固定大小内存块（Memory Slab）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_CONTROLLER && CONFIG_I3C
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_NXP_TRANSFER_TIMEOUT"></a>

## 108.44 `CONFIG_I3C_NXP_TRANSFER_TIMEOUT`

**提示（Prompt）**：传输超时（Transfer Timeout，毫秒）

**说明（Help）**

每次 I³C 传输的超时时间，单位为毫秒。0 表示驱动应使用 `K_FOREVER`，即一直等待，直到操作能够完成。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_MCUX && CONFIG_I3C
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.nxp:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.nxp#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → MCUX I³C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_MCUX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_MCUX)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_RENESAS_RA"></a>

## 108.45 `CONFIG_I3C_RENESAS_RA`

**提示（Prompt）**：Renesas RA I³C 驱动支持

**说明（Help）**

启用 Renesas RA 微控制器的 I³C 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_I3C_ENABLED && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_I3C
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.renesas:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.renesas#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_USE_RA_FSP_I3C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_I3C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I3C_RTIO"></a>

## 108.46 `CONFIG_I3C_RTIO`

**提示（Prompt）**：I³C 实时 I/O（RTIO）API【实验性（EXPERIMENTAL）】

**说明（Help）**

用于实时 I/O（RTIO）的 I³C API 及实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_CONTROLLER && CONFIG_I3C
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_RTIO
CONFIG_RTIO_WORKQ
```

**被选择（Selected by）**

```text
CONFIG_LSM6DSV16X
CONFIG_LSM6DSVXXX
CONFIG_ICM45686
CONFIG_ICM566XX
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_LSM6DSV16X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X)、[`CONFIG_LSM6DSVXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSVXXX)、[`CONFIG_ICM45686`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM45686)、[`CONFIG_ICM566XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM566XX)。

<a id="CONFIG_I3C_RTIO_CQ_SIZE"></a>

## 108.47 `CONFIG_I3C_RTIO_CQ_SIZE`

**提示（Prompt）**：阻塞调用的完成队列（Completion Queue）大小

**说明（Help）**

启用 `I3C_RTIO` 时，阻塞式 I³C 调用会复制到每个驱动各自的提交队列（Submission Queue）中。队列深度决定传给 `i3c_transfer` 的数组中最多可含多少个 `i3c_msg` 结构体。考虑到设备地址、寄存器地址以及要读写的值，4 是合理的默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_RTIO && CONFIG_I3C_CONTROLLER && CONFIG_I3C
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I³C 实时 I/O（RTIO）API【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_RTIO_FALLBACK_MSGS"></a>

## 108.48 `CONFIG_I3C_RTIO_FALLBACK_MSGS`

**提示（Prompt）**：可供默认处理程序使用的 `i3c_msg` 结构体数量

**说明（Help）**

将 RTIO 用于尚未原生实现提交（Submit）API 的驱动时，提交项会转换回 `struct i3c_msg` 值，再交给 `i3c_transfer`。这要求栈上有一定数量的消息对象，用来承接提交项的转换结果。MISRA 规则要求提前知道这一数量。4 很可能适用于所有使用者；但如果使用 RTIO，驱动未原生实现 submit，……译注：所用官方数据库中的帮助正文到此处逗号结束；没有补写缺失的后半句。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_RTIO && CONFIG_I3C_CONTROLLER && CONFIG_I3C
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I³C 实时 I/O（RTIO）API【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_RTIO_SQ_SIZE"></a>

## 108.49 `CONFIG_I3C_RTIO_SQ_SIZE`

**提示（Prompt）**：阻塞调用的提交队列（Submission Queue）大小

**说明（Help）**

启用 `I3C_RTIO` 时，阻塞式 I³C 调用会复制到每个驱动各自的提交队列（Submission Queue）中。队列深度决定传给 `i3c_transfer` 的数组中最多可含多少个 `i3c_msg` 结构体。考虑到设备地址、寄存器地址以及要读写的值，4 是合理的默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_RTIO && CONFIG_I3C_CONTROLLER && CONFIG_I3C
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I³C 实时 I/O（RTIO）API【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_SHELL"></a>

## 108.50 `CONFIG_I3C_SHELL`

**提示（Prompt）**：I³C 命令行（Shell）

**说明（Help）**

启用 I³C 命令行（Shell）。它支持信息查询、总线恢复、通用命令码（CCC）以及 I³C 读写操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_I3C
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_STM32"></a>

## 108.51 `CONFIG_I3C_STM32`

**提示（Prompt）**：STM32 I³C 驱动支持

**说明（Help）**

启用 STM32 微控制器的 I³C 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_I3C_ENABLED && CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I3C_IBI_WORKQUEUE if CONFIG_I3C_USE_IBI && CONFIG_I3C_CONTROLLER
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.stm32:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.stm32#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_IBI_WORKQUEUE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_IBI_WORKQUEUE)、[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I3C_STM32_DMA"></a>

## 108.52 `CONFIG_I3C_STM32_DMA`

**提示（Prompt）**：STM32 I³C DMA 驱动支持

**说明（Help）**

启用 STM32 微控制器的 I³C DMA 模式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_STM32 && CONFIG_I3C
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.stm32:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.stm32#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → STM32 I³C 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_I3C_STM32`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_STM32)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_I3C_STM32_DMA_FIFO_HEAP_SIZE"></a>

## 108.53 `CONFIG_I3C_STM32_DMA_FIFO_HEAP_SIZE`

**提示（Prompt）**：状态 FIFO 与控制 FIFO 的堆（Heap）

**说明（Help）**

配置堆大小，用于动态分配存放状态 FIFO 和控制 FIFO 字（Word）的区域，供 DMA 使用。此值取决于单次传输将发送的最大消息数量。2 KB 可保证有足够的堆空间在单次传输中发送 256 条消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_STM32_DMA && CONFIG_I3C_STM32 && CONFIG_I3C
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.stm32:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.stm32#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → STM32 I³C 驱动支持 → STM32 I³C DMA 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_I3C_STM32_DMA`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_STM32_DMA)、[`CONFIG_I3C_STM32`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_STM32)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_I3C_TARGET"></a>

## 108.54 `CONFIG_I3C_TARGET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示已启用作为 I³C 目标设备（Target）的支持。此内部选项根据 I³C 模式选择（`I3C_TARGET_ROLE_ONLY` 或 `I3C_DUAL_ROLE`）自动推导，不应直接设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C
```

**默认值（Defaults）**

```text
y if CONFIG_I3C_DUAL_ROLE || CONFIG_I3C_TARGET_ROLE_ONLY
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_DUAL_ROLE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_DUAL_ROLE)、[`CONFIG_I3C_TARGET_ROLE_ONLY`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_TARGET_ROLE_ONLY)。

<a id="CONFIG_I3C_TARGET_BUFFER_MODE"></a>

## 108.55 `CONFIG_I3C_TARGET_BUFFER_MODE`

**提示（Prompt）**：I³C 目标设备驱动缓冲模式（Buffer Mode）

**说明（Help）**

此选项用于启用缓冲模式（Buffer Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_TARGET && CONFIG_I3C
```

**被选择（Selected by）**

```text
CONFIG_I3CS_IT51XXX
CONFIG_I3C_NPCX_DMA
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_TARGET`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_TARGET)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3CS_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CS_IT51XXX)、[`CONFIG_I3C_NPCX_DMA`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_NPCX_DMA)。

<a id="CONFIG_I3C_TARGET_ROLE_ONLY"></a>

## 108.56 `CONFIG_I3C_TARGET_ROLE_ONLY`

**提示（Prompt）**：仅 I³C 目标设备（Target）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_I3C_MODE>
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → I³C 模式选择（Mode Selection）

**配置项引用（Symbol References）**：[`CONFIG_I3C_MODE`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_MODE)。

<a id="CONFIG_I3C_USE_IBI"></a>

## 108.57 `CONFIG_I3C_USE_IBI`

**提示（Prompt）**：使用带内中断（In-Band Interrupt，IBI）

**说明（Help）**

启用此选项以使用带内中断（In-Band Interrupt，IBI）。不确定时请选择 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i3c/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<a id="CONFIG_IT51XXX_AUTO_IBI_MAX_TARGETS"></a>

## 108.58 `CONFIG_IT51XXX_AUTO_IBI_MAX_TARGETS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

it51xxx 自动 IBI 响应机制支持的最大目标设备（Target）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_USE_IBI && CONFIG_I3CM_IT51XXX && CONFIG_I3C
```

**默认值（Defaults）**

```text
0 if CONFIG_SOC_IT51526AW || CONFIG_SOC_IT51526BW
3
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`drivers/i3c/Kconfig.it51xxx:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/Kconfig.it51xxx#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 改进型集成电路互连（Improved Inter-Integrated Circuit，I³C）总线驱动 → it51xxx i3cm 驱动

**配置项引用（Symbol References）**：[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_I3CM_IT51XXX`](P108_drivers_i3c_配置项参考.md#CONFIG_I3CM_IT51XXX)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_SOC_IT51526AW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51526AW)、[`CONFIG_SOC_IT51526BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51526BW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_IT51526AW`、`CONFIG_SOC_IT51526BW`。

<!-- kconfig-navigation -->

[上一章](P107_drivers_i2s_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P109_drivers_ieee802154_配置项参考_1.md)
