---
id: learning.zephyr-docs.kconfig-reference.page-106
title: "`drivers/i2c`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第106章\_`drivers/i2c`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/i2c` 的 65 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_I2C_RENESAS_RX_CALLBACK"></a>

## 106.1 `CONFIG_I2C_RENESAS_RX_CALLBACK`

**提示（Prompt）**：Renesas RX I²C 回调（Callback）支持

**说明（Help）**

为 I²C 驱动启用回调支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_CALLBACK && CONFIG_I2C_RENESAS_RX_RIIC && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_rx:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_rx#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Renesas RX I²C 控制器（Controller）

**配置项引用（Symbol References）**：[`CONFIG_I2C_CALLBACK`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_CALLBACK)、[`CONFIG_I2C_RENESAS_RX_RIIC`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RENESAS_RX_RIIC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_RENESAS_RX_RIIC"></a>

## 106.2 `CONFIG_I2C_RENESAS_RX_RIIC`

**提示（Prompt）**：Renesas RX I²C 控制器（Controller）

**说明（Help）**

启用 Renesas RX I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RX_RDP_I2C
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_rx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_rx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_RX_RDP_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RX_RDP_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_RENESAS_RZA2M_RIIC"></a>

## 106.3 `CONFIG_I2C_RENESAS_RZA2M_RIIC`

**提示（Prompt）**：用于 RZ/A2M 的 Renesas I²C 驱动

**说明（Help）**

启用用于 RZ/A2M 的 Renesas I²C 驱动（RIIC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_RIIC_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_rz:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_rz#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_RENESAS_RZ_IIC"></a>

## 106.4 `CONFIG_I2C_RENESAS_RZ_IIC`

**提示（Prompt）**：Renesas RZ I²C IIC 控制器（Controller）

**说明（Help）**

启用 Renesas RZ I²C IIC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_IIC_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_IIC_MASTER
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_rz:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_rz#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_RZ_FSP_IIC_MASTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_IIC_MASTER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_RENESAS_RZ_RIIC"></a>

## 106.5 `CONFIG_I2C_RENESAS_RZ_RIIC`

**提示（Prompt）**：Renesas RZ I²C RIIC 控制器（Controller）

**说明（Help）**

启用 Renesas RZ I²C RIIC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_RIIC_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_RIIC_MASTER
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USE_RZ_FSP_RIIC_MASTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_RIIC_MASTER)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_RTIO"></a>

## 106.6 `CONFIG_I2C_RTIO`

**提示（Prompt）**：I²C 实时 I/O（RTIO）API【实验性（EXPERIMENTAL）】

**说明（Help）**

用于实时 I/O（RTIO）的 I²C API 及实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_RTIO
CONFIG_RTIO_WORKQ
```

**被选择（Selected by）**

```text
CONFIG_ENS210
CONFIG_AKM09918C
CONFIG_BMA4XX
CONFIG_BMI08X
CONFIG_MS5637
CONFIG_LIS2DUX12
CONFIG_LSM6DSV16X
CONFIG_LSM6DSVXXX
CONFIG_ICM45686
CONFIG_ICM566XX
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_ENS210`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENS210)、[`CONFIG_AKM09918C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AKM09918C)、[`CONFIG_BMA4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMA4XX)、[`CONFIG_BMI08X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI08X)、[`CONFIG_MS5637`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MS5637)、[`CONFIG_LIS2DUX12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DUX12)、[`CONFIG_LSM6DSV16X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X)、[`CONFIG_LSM6DSVXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSVXXX)、[`CONFIG_ICM45686`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM45686)、[`CONFIG_ICM566XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM566XX)。

<a id="CONFIG_I2C_RTIO_CQ_SIZE"></a>

## 106.7 `CONFIG_I2C_RTIO_CQ_SIZE`

**提示（Prompt）**：阻塞调用的完成队列（Completion Queue）大小

**说明（Help）**

启用 `I2C_RTIO` 时，阻塞式 I²C 调用会复制到每个驱动各自的提交队列（Submission Queue）中。队列深度决定传给 `i2c_transfer` 的数组中最多可含多少个 `i2c_msg` 结构体。考虑到设备地址、寄存器地址以及要读写的值，4 是合理的默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_RTIO && CONFIG_I2C
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I²C 实时 I/O（RTIO）API【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_RTIO_FALLBACK_MSGS"></a>

## 106.8 `CONFIG_I2C_RTIO_FALLBACK_MSGS`

**提示（Prompt）**：可供默认处理程序使用的 `i2c_msg` 结构体数量

**说明（Help）**

将 RTIO 用于尚未原生实现提交（Submit）API 的驱动时，提交项会转换回 `struct i2c_msg` 值，再交给 `i2c_transfer`。这要求栈上有一定数量的消息对象，用来承接提交项的转换结果。MISRA 规则要求提前知道这一数量。4 很可能适用于所有使用者；但如果使用 RTIO、驱动未原生实现 submit，且遇到 I²C 消息对象不足的错误，就应调整此 Kconfig 选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_RTIO && CONFIG_I2C
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I²C 实时 I/O（RTIO）API【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_RTIO_SQ_SIZE"></a>

## 106.9 `CONFIG_I2C_RTIO_SQ_SIZE`

**提示（Prompt）**：阻塞调用的提交队列（Submission Queue）大小

**说明（Help）**

启用 `I2C_RTIO` 时，阻塞式 I²C 调用会复制到每个驱动各自的提交队列（Submission Queue）中。队列深度决定传给 `i2c_transfer` 的数组中最多可含多少个 `i2c_msg` 结构体。考虑到设备地址、寄存器地址以及要读写的值，4 是合理的默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_RTIO && CONFIG_I2C
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I²C 实时 I/O（RTIO）API【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_RTS5912"></a>

## 106.10 `CONFIG_I2C_RTS5912`

**提示（Prompt）**：Realtek RTS5912 I²C 支持

**说明（Help）**

启用 Realtek RTS5912 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C_ALLOW_NO_STOP_TRANSACTIONS
CONFIG_I2C_DW_EXTENDED_SUPPORT
CONFIG_I2C_DW_PM_POLICY_STATE_LOCK
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.rts5912:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.rts5912#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_ALLOW_NO_STOP_TRANSACTIONS`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ALLOW_NO_STOP_TRANSACTIONS)、[`CONFIG_I2C_DW_EXTENDED_SUPPORT`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DW_EXTENDED_SUPPORT)、[`CONFIG_I2C_DW_PM_POLICY_STATE_LOCK`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DW_PM_POLICY_STATE_LOCK)。

<a id="CONFIG_I2C_RTS5912_INIT_PRIORITY"></a>

## 106.11 `CONFIG_I2C_RTS5912_INIT_PRIORITY`

**提示（Prompt）**：RTS5912 初始化优先级（Initialization Priority）

**说明（Help）**

I²C 设备驱动初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_RTS5912 && CONFIG_I2C
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.rts5912:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.rts5912#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Realtek RTS5912 I²C 支持

**配置项引用（Symbol References）**：[`CONFIG_I2C_RTS5912`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTS5912)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_RV32M1_LPI2C"></a>

## 106.12 `CONFIG_I2C_RV32M1_LPI2C`

**提示（Prompt）**：RV32M1 LPI2C 驱动

**说明（Help）**

启用 RV32M1 LPI2C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_LPI2C_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:297`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L297)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_SAM0"></a>

## 106.13 `CONFIG_I2C_SAM0`

**提示（Prompt）**：SAM0 系列 I²C SERCOM 驱动

**说明（Help）**

启用 SAM0 系列 SERCOM I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sam0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sam0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_SAM0_DMA_DRIVEN"></a>

## 106.14 `CONFIG_I2C_SAM0_DMA_DRIVEN`

**提示（Prompt）**：SAM0 I²C 设备的 DMA 支持

**说明（Help）**

启用 I²C 外设的 DMA 驱动事务。DMA 模式处理事务所需的中断更少，并能确保高速模式不会因重新装载数据而延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_SAM0 && CONFIG_I2C
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sam0:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sam0#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → SAM0 系列 I²C SERCOM 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_SAM0`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SAM0)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_I2C_SAM0_TRANSFER_TIMEOUT"></a>

## 106.15 `CONFIG_I2C_SAM0_TRANSFER_TIMEOUT`

**提示（Prompt）**：传输超时（Transfer Timeout，毫秒）

**说明（Help）**

每次 I²C 传输的超时时间，单位为毫秒。0 表示驱动应使用 `K_FOREVER`，即一直等待，直到操作能够完成。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_SAM0 && CONFIG_I2C
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sam0:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sam0#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → SAM0 系列 I²C SERCOM 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_SAM0`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SAM0)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SAM_TWI"></a>

## 106.16 `CONFIG_I2C_SAM_TWI`

**提示（Prompt）**：Atmel SAM（TWI）I²C 驱动

**说明（Help）**

启用 Atmel SAM MCU 系列（TWI）I²C 总线驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_I2C_TWI_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_SAM_TWIHS"></a>

## 106.17 `CONFIG_I2C_SAM_TWIHS`

**提示（Prompt）**：Atmel SAM（TWIHS）I²C 驱动

**说明（Help）**

启用 Atmel SAM MCU 系列（TWIHS）I²C 总线驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_I2C_TWIHS_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sam_twihs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sam_twihs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_SAM_TWIM"></a>

## 106.18 `CONFIG_I2C_SAM_TWIM`

**提示（Prompt）**：Atmel SAM（TWIM）I²C 驱动

**说明（Help）**

启用 Atmel SAM MCU 系列（TWIM）I²C 总线驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_I2C_TWIM_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_SBCON"></a>

## 106.19 `CONFIG_I2C_SBCON`

**提示（Prompt）**：ARM SBCon 双线串行总线接口（Two-wire Serial Bus Interface）的 I²C 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_VERSATILE_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sbcon:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sbcon#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_SC18IM704"></a>

## 106.20 `CONFIG_I2C_SC18IM704`

**提示（Prompt）**：NXP SC18IM704 I²C 控制器驱动

**说明（Help）**

启用 NXP SC18IM704 I²C 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SC18IM704_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sc18im704:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sc18im704#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_I2C_SC18IM704_INIT_PRIORITY"></a>

## 106.21 `CONFIG_I2C_SC18IM704_INIT_PRIORITY`

**提示（Prompt）**：SC18IM704 I²C 初始化优先级（Initialization Priority）

**说明（Help）**

SC18IM704 I²C 控制器的初始化优先级。注意：数值必须大于 UART 总线的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_SC18IM704 && CONFIG_I2C
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sc18im704:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sc18im704#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → NXP SC18IM704 I²C 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_SC18IM704`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SC18IM704)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SC18IM704_VERIFY"></a>

## 106.22 `CONFIG_I2C_SC18IM704_VERIFY`

**提示（Prompt）**：验证 SC18IM704 I²C 传输

**说明（Help）**

在 I²C 传输后检查 I²C 状态寄存器（State Register），以检测错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_SC18IM704 && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sc18im704:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sc18im704#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → NXP SC18IM704 I²C 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_SC18IM704`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SC18IM704)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SEDI"></a>

## 106.23 `CONFIG_I2C_SEDI`

**提示（Prompt）**：Intel SEDI I²C 驱动

**说明（Help）**

此选项启用 Intel SEDI I²C 驱动。该驱动只是构建在 `hal-intel` 模块中 SEDI 裸机（Bare Metal）I²C 驱动之上的适配层驱动（Shim Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_SEDI_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sedi:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sedi#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SF32LB"></a>

## 106.24 `CONFIG_I2C_SF32LB`

**提示（Prompt）**：SiFli SF32LB I²C 驱动

**说明（Help）**

启用 SiFli SF32LB 的 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA if n
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_I2C_SHELL"></a>

## 106.25 `CONFIG_I2C_SHELL`

**提示（Prompt）**：I²C 命令行（Shell）

**说明（Help）**

启用 I²C 命令行（Shell）。I²C Shell 支持扫描、总线恢复以及 I²C 读写操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SHELL_BUFFER_SIZE"></a>

## 106.26 `CONFIG_I2C_SHELL_BUFFER_SIZE`

**提示（Prompt）**：I²C Shell 缓冲区大小（Buffer Size）

**说明（Help）**

部分 I²C 命令使用的缓冲区大小，决定读写操作的最大长度。注意，此缓冲区分配在栈（Stack）上。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SIFIVE"></a>

## 106.27 `CONFIG_I2C_SIFIVE`

**提示（Prompt）**：SiFive I²C 驱动

**说明（Help）**

启用 SiFive Freedom 的 I²C 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFIVE_I2C0_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sifive:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sifive#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SILABS"></a>

## 106.28 `CONFIG_I2C_SILABS`

**提示（Prompt）**：Silabs I2C_S2 驱动

**说明（Help）**

为 Silabs Gecko SoC 系列启用 I²C Series 2 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_I2C_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SILABS_SISDK_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_I2C)。

<a id="CONFIG_I2C_SILABS_DMA"></a>

## 106.29 `CONFIG_I2C_SILABS_DMA`

**提示（Prompt）**：I²C 操作的 DMA 支持

**说明（Help）**

启用用于 I²C DMA 传输的 DMA 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA && CONFIG_I2C_SILABS && CONFIG_I2C
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.silabs:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.silabs#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Silabs I2C_S2 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_I2C_SILABS`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SILABS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SILABS_TIMEOUT"></a>

## 106.30 `CONFIG_I2C_SILABS_TIMEOUT`

**提示（Prompt）**：I²C 操作超时（Operation Timeout，毫秒）

**说明（Help）**

指定 I²C 传输的超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_SILABS && CONFIG_I2C
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.silabs:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.silabs#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Silabs I2C_S2 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_SILABS`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SILABS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SMARTBOND"></a>

## 106.31 `CONFIG_I2C_SMARTBOND`

**提示（Prompt）**：Renesas SmartBond™ I²C 驱动

**说明（Help）**

启用 Renesas SmartBond™ DA1469x 系列 MCU 的 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.smartbond:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.smartbond#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_STATS"></a>

## 106.32 `CONFIG_I2C_STATS`

**提示（Prompt）**：I²C 设备统计（Stats）

**说明（Help）**

启用 I²C 统计（Stats）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STATS && CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_STM32"></a>

## 106.33 `CONFIG_I2C_STM32`

**提示（Prompt）**：STM32 I²C 驱动

**说明（Help）**

启用 STM32 系统级芯片（SoC）的 I²C 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_I2C_V1_ENABLED || DT_HAS_ST_STM32_I2C_V2_ENABLED) && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED)。

<a id="CONFIG_I2C_STM32_BUS_RECOVERY"></a>

## 106.34 `CONFIG_I2C_STM32_BUS_RECOVERY`

**提示（Prompt）**：总线恢复（Bus Recovery）支持

**说明（Help）**

启用 STM32 驱动通过 GPIO 位操作模拟（Bit Banging）实现的总线恢复支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_I2C_STM32 && CONFIG_I2C
```

**默认值（Defaults）**

```text
y if CONFIG_I2C_BUS_RECOVERY
```

**主动选择（Selects）**

```text
CONFIG_I2C_BITBANG
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.stm32:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.stm32#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → STM32 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_BUS_RECOVERY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BUS_RECOVERY)、[`CONFIG_I2C_BITBANG`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_BITBANG)。

<a id="CONFIG_I2C_STM32_INTERRUPT"></a>

## 106.35 `CONFIG_I2C_STM32_INTERRUPT`

**提示（Prompt）**：STM32 MCU I²C 中断（Interrupt）支持

**说明（Help）**

为 I²C 驱动启用中断（Interrupt）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_I2C_STM32_V1 || CONFIG_I2C_STM32_V2) && CONFIG_I2C_STM32 && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_I2C_STM32_V1
CONFIG_I2C_STM32_V2
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.stm32:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.stm32#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → STM32 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_STM32_V1`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32_V1)、[`CONFIG_I2C_STM32_V2`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32_V2)、[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_STM32_V1"></a>

## 106.36 `CONFIG_I2C_STM32_V1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

匹配 `st,stm32-i2c-v1` 兼容字符串（Compatible）的驱动变体。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_I2C_V1_ENABLED && CONFIG_I2C_STM32 && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C_STM32_INTERRUPT if CONFIG_I2C_TARGET || CONFIG_I2C_RTIO
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.stm32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.stm32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → STM32 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_STM32_INTERRUPT`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32_INTERRUPT)、[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)。

<a id="CONFIG_I2C_STM32_V2"></a>

## 106.37 `CONFIG_I2C_STM32_V2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

匹配 `st,stm32-i2c-v2` 兼容字符串（Compatible）的驱动变体。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_I2C_V2_ENABLED && CONFIG_I2C_STM32 && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C_STM32_INTERRUPT if CONFIG_I2C_TARGET || CONFIG_I2C_RTIO
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.stm32:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.stm32#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → STM32 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_STM32_INTERRUPT`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32_INTERRUPT)、[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)。

<a id="CONFIG_I2C_STM32_V2_DMA"></a>

## 106.38 `CONFIG_I2C_STM32_V2_DMA`

**提示（Prompt）**：直接内存访问支持（DMA Support）

**说明（Help）**

启用 STM32 I²C 驱动的 DMA 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_STM32_V2 && CONFIG_I2C_STM32 && CONFIG_I2C
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.stm32:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.stm32#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → STM32 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_STM32_V2`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32_V2)、[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_I2C_STM32_V2_TIMING"></a>

## 106.39 `CONFIG_I2C_STM32_V2_TIMING`

**提示（Prompt）**：计算 I²C V2 总线时序（Bus Timing）

**说明（Help）**

启用 STM32 驱动总线时序计算。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_STM32_V2 && CONFIG_I2C_STM32 && CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.stm32:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.stm32#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → STM32 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_STM32_V2`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32_V2)、[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_STM32_WAIT_BUS_IDLE_TIMEOUT_USEC"></a>

## 106.40 `CONFIG_I2C_STM32_WAIT_BUS_IDLE_TIMEOUT_USEC`

**提示（Prompt）**：STM32 I²C 总线等待超时（微秒）

**说明（Help）**

附接了目标设备（Target）模式时，在启动新的控制器会话（Controller Session）之前等待总线空闲的时间，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_STM32 && CONFIG_I2C
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[1, 4294967295]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.stm32:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.stm32#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → STM32 I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SY1XX"></a>

## 106.41 `CONFIG_I2C_SY1XX`

**提示（Prompt）**：Sensry SY1XX I²C 驱动

**说明（Help）**

启用 Sensry SY1xx SoC 系列 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSRY_SY1XX_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sy1xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sy1xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_SY1XX_BUFFER_SIZE"></a>

## 106.42 `CONFIG_I2C_SY1XX_BUFFER_SIZE`

**提示（Prompt）**：SY1XX I²C 缓冲区大小（Buffer Size）

**说明（Help）**

SY1XX I²C 驱动用于分块传输（Chunked Transfer）的默认缓冲区大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_SY1XX && CONFIG_I2C
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.sy1xx:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.sy1xx#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Sensry SY1XX I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_SY1XX`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_SY1XX)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_TARGET"></a>

## 106.43 `CONFIG_I2C_TARGET`

**提示（Prompt）**：I²C 目标设备（Target）驱动

**说明（Help）**

启用 I²C 目标设备（Target）驱动配置

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/i2c/target/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/target/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_TARGET_ALLOW_POWER_SAVING"></a>

## 106.44 `CONFIG_I2C_TARGET_ALLOW_POWER_SAVING`

**提示（Prompt）**：允许 I²C 目标设备进入节能模式（Power-saving Mode）【实验性】

**说明（Help）**

启用后，I²C 目标设备可在总线空闲时进入打盹／深度打盹（Doze/Deep Doze）状态。正在进行的传输会阻止进入低功耗状态，直到传输完成，从而在降低总体功耗的同时确保通信正确。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_ITE_ENHANCE && !CONFIG_SOC_IT8XXX2_REG_SET_V1 && CONFIG_I2C_TARGET && CONFIG_I2C
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it8xxx2:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it8xxx2#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_ITE_ENHANCE`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_ENHANCE)、[`CONFIG_SOC_IT8XXX2_REG_SET_V1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2_REG_SET_V1)、[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_I2C_TARGET_BUFFER_MODE"></a>

## 106.45 `CONFIG_I2C_TARGET_BUFFER_MODE`

**提示（Prompt）**：I²C 目标设备驱动缓冲模式（Buffer Mode）【实验性】

**说明（Help）**

此选项用于启用缓冲模式（Buffer Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_TARGET && CONFIG_I2C
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/i2c/target/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/target/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I²C 目标设备（Target）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_I2C_TARGET_INIT_PRIORITY"></a>

## 106.46 `CONFIG_I2C_TARGET_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

I²C 目标设备驱动初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_TARGET && CONFIG_I2C
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`drivers/i2c/target/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/target/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I²C 目标设备（Target）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_TARGET_IT51XXX_MAX_BUF_SIZE"></a>

## 106.47 `CONFIG_I2C_TARGET_IT51XXX_MAX_BUF_SIZE`

**提示（Prompt）**：I²C 目标设备驱动缓冲区大小（Buffer Size）

**说明（Help）**

I²C 目标设备驱动使用的缓冲区大小，用于累积多次 FIFO 传输的数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_TARGET && CONFIG_I2C_ITE_IT51XXX && CONFIG_I2C
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[32, 2048]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it51xxx:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it51xxx#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → ITE IT51XXX I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C_ITE_IT51XXX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_IT51XXX)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_TARGET_IT8XXX2_MAX_BUF_SIZE"></a>

## 106.48 `CONFIG_I2C_TARGET_IT8XXX2_MAX_BUF_SIZE`

**提示（Prompt）**：允许配置的大小上限为 2044 字节。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_ITE_ENHANCE && CONFIG_I2C_TARGET && CONFIG_I2C
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[4, 2044]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.it8xxx2:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.it8xxx2#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_ITE_ENHANCE`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_ENHANCE)、[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_TARGET_REGSET_LIB"></a>

## 106.49 `CONFIG_I2C_TARGET_REGSET_LIB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

I²C 目标设备寄存器集（Regset）库支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_TARGET && CONFIG_I2C
```

**被选择（Selected by）**

```text
CONFIG_I2C_EEPROM_TARGET
CONFIG_I2C_TMP103_TARGET
```

**定义位置（Location）**：[`drivers/i2c/target/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/target/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I²C 目标设备（Target）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_EEPROM_TARGET`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_EEPROM_TARGET)、[`CONFIG_I2C_TMP103_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TMP103_TARGET)。

<a id="CONFIG_I2C_TARGET_RENESAS_RA_IIC_BUFFER_SIZE"></a>

## 106.50 `CONFIG_I2C_TARGET_RENESAS_RA_IIC_BUFFER_SIZE`

**提示（Prompt）**：I²C 目标设备数据缓冲区长度（Buffer Length）

**说明（Help）**

指定 Renesas RA I²C IIC 目标设备驱动所用数据缓冲区的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_RENESAS_RA_IIC && CONFIG_I2C_TARGET && CONFIG_I2C_TARGET_BUFFER_MODE && CONFIG_I2C
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_ra:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_ra#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Renesas RA I²C IIC 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_RENESAS_RA_IIC`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_RENESAS_RA_IIC)、[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C_TARGET_BUFFER_MODE`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET_BUFFER_MODE)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_TCA954X"></a>

## 106.51 `CONFIG_I2C_TCA954X`

**提示（Prompt）**：可由 I²C 寻址的开关（I²C Addressable Switch）

**说明（Help）**

启用 TCA954x 系列 I²C 总线开关。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_TCA9546A_ENABLED || DT_HAS_TI_TCA9548A_ENABLED || DT_HAS_TI_TCA9544A_ENABLED) && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.tca954x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.tca954x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_TCA954X_CHANNEL_INIT_PRIO"></a>

## 106.52 `CONFIG_I2C_TCA954X_CHANNEL_INIT_PRIO`

**提示（Prompt）**：TCA954x 通道驱动初始化优先级（Initialization Priority）

**说明（Help）**

应高于 `I2C_TCA954X_ROOT_INIT_PRIO`。译注：原文为 higher than；同一快照中通道与根驱动均默认取 `I2C_INIT_PRIORITY`，此处保留帮助文字与默认值之间的差异，不擅改配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_TCA954X && CONFIG_I2C
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.tca954x:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.tca954x#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → 可由 I²C 寻址的开关（I²C Addressable Switch）

**配置项引用（Symbol References）**：[`CONFIG_I2C_TCA954X`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TCA954X)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_INIT_PRIORITY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_I2C_TCA954X_ROOT_INIT_PRIO"></a>

## 106.53 `CONFIG_I2C_TCA954X_ROOT_INIT_PRIO`

**提示（Prompt）**：TCA954x 根驱动初始化优先级（Initialization Priority）

**说明（Help）**

应低于 `I2C_TCA954X_CHANNEL_INIT_PRIO`。译注：原文为 lower than；同一快照中根驱动与通道均默认取 `I2C_INIT_PRIORITY`，此处保留帮助文字与默认值之间的差异，不擅改配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_TCA954X && CONFIG_I2C
```

**默认值（Defaults）**

```text
CONFIG_I2C_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.tca954x:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.tca954x#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → 可由 I²C 寻址的开关（I²C Addressable Switch）

**配置项引用（Symbol References）**：[`CONFIG_I2C_TCA954X`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TCA954X)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_INIT_PRIORITY`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_INIT_PRIORITY)。

<a id="CONFIG_I2C_TELINK_B91"></a>

## 106.54 `CONFIG_I2C_TELINK_B91`

**提示（Prompt）**：Telink Semiconductor B91 I²C 驱动

**说明（Help）**

启用 Telink B91 I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TELINK_B91_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.b91:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.b91#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_TMP103_TARGET"></a>

## 106.55 `CONFIG_I2C_TMP103_TARGET`

**提示（Prompt）**：I²C 目标设备（Target）TMP103 驱动

**说明（Help）**

启用虚拟 I²C 目标设备 TMP103 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_I2C_TARGET_TMP103_ENABLED && CONFIG_I2C_TARGET && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C_TARGET_REGSET_LIB
```

**定义位置（Location）**：[`drivers/i2c/target/Kconfig.tmp103:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/target/Kconfig.tmp103#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → I²C 目标设备（Target）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_TARGET`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_TARGET_REGSET_LIB`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TARGET_REGSET_LIB)。

<a id="CONFIG_I2C_TRANSFER_TIMEOUT_MS"></a>

## 106.56 `CONFIG_I2C_TRANSFER_TIMEOUT_MS`

**提示（Prompt）**：传输超时（Transfer Timeout），单位为毫秒

**说明（Help）**

每次 I²C 传输的超时时间，单位为毫秒。某些驱动中，0 表示应使用 `K_FOREVER`，即一直等待，直到操作能够完成。将超时值直接写入寄存器的 I²C 控制器不支持把此选项设为 0，并使用 `BUILD_ASSERT_INVALID_I2C_TRANSFER_TIMEOUT()` 检查来防止无限超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED && CONFIG_I2C
```

**默认值（Defaults）**

```text
500
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig)。

```text
1000 if CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED"></a>

## 106.57 `CONFIG_I2C_TRANSFER_TIMEOUT_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由支持通过 `I2C_TRANSFER_TIMEOUT_MS` Kconfig 选项设置 I²C 事务超时的驱动选中（Select）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C
```

**被选择（Selected by）**

```text
CONFIG_I2C_DW
CONFIG_I2C_INFINEON_CAT1_PDL
CONFIG_I2C_ITE_IT51XXX
CONFIG_I2C_ITE_IT8XXX2
CONFIG_I2C_ITE_ENHANCE
CONFIG_I2C_NPCX
CONFIG_I2C_NRFX
CONFIG_I2C_STM32
```

**定义位置（Location）**：[`drivers/i2c/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_DW`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_DW)、[`CONFIG_I2C_INFINEON_CAT1_PDL`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_INFINEON_CAT1_PDL)、[`CONFIG_I2C_ITE_IT51XXX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_IT51XXX)、[`CONFIG_I2C_ITE_IT8XXX2`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_IT8XXX2)、[`CONFIG_I2C_ITE_ENHANCE`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_ITE_ENHANCE)、[`CONFIG_I2C_NPCX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_NPCX)、[`CONFIG_I2C_NRFX`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C_NRFX)、[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)。

<a id="CONFIG_I2C_VIRTIO"></a>

## 106.58 `CONFIG_I2C_VIRTIO`

**提示（Prompt）**：VIRTIO I²C 适配器（Adapter）驱动

**说明（Help）**

启用 VIRTIO I²C 适配器设备的驱动。每次传输都需要与 virtio 设备进行一次往返（Round Trip），因此 I²C API 只能从线程（Thread）中使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_VIRTIO
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.virtio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.virtio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_VIRTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO)。

<a id="CONFIG_I2C_VIRTIO_MAX_MSGS"></a>

## 106.59 `CONFIG_I2C_VIRTIO_MAX_MSGS`

**提示（Prompt）**：每批提交的消息数量（Messages per Batch）

**说明（Help）**

一次 `i2c_transfer` 中，驱动在通知设备之前排入队列的消息数量。超过此数量的传输会拆分为多个批次；这样做在功能上正确，但每个额外批次都增加一次往返，因此默认值设得远高于寄存器读取所需的两条消息。每个槽位消耗少量 RAM，并使请求 virtqueue 按每条消息三个描述符（Descriptor）确定大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_VIRTIO && CONFIG_I2C
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.virtio:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.virtio#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → VIRTIO I²C 适配器（Adapter）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_VIRTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_VIRTIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_WCH"></a>

## 106.60 `CONFIG_I2C_WCH`

**提示（Prompt）**：WCH I²C 驱动

**说明（Help）**

启用 WCH 平台的 I²C 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_WCH_XFER_TIMEOUT_MS"></a>

## 106.61 `CONFIG_I2C_WCH_XFER_TIMEOUT_MS`

**提示（Prompt）**：设置传输超时，单位为毫秒。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C_WCH && CONFIG_I2C
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.wch:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.wch#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → WCH I²C 驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_WCH`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_WCH)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_I2C_XEC"></a>

## 106.62 `CONFIG_I2C_XEC`

**提示（Prompt）**：XEC Microchip I²C 驱动

**说明（Help）**

启用 Microchip XEC I²C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_I2C_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mchp_xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mchp_xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_XEC_V2"></a>

## 106.63 `CONFIG_I2C_XEC_V2`

**提示（Prompt）**：XEC Microchip I²C 驱动

**说明（Help）**

启用 Microchip XEC I²C V2 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_I2C_V2_ENABLED && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.mchp_xec:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.mchp_xec#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_I2C_XILINX_AXI"></a>

## 106.64 `CONFIG_I2C_XILINX_AXI`

**提示（Prompt）**：Xilinx AXI I²C 驱动

**说明（Help）**

启用 Xilinx AXI IIC 总线接口（Bus Interface）驱动。这是 Xilinx 文档 PG090 所述的 FPGA 逻辑核（Logic Core）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_XLNX_XPS_IIC_2_00_A_ENABLED || DT_HAS_XLNX_XPS_IIC_2_1_ENABLED) && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.xilinx_axi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.xilinx_axi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_RENESAS_RX_I2C_DTC"></a>

## 106.65 `CONFIG_RENESAS_RX_I2C_DTC`

**提示（Prompt）**：Renesas RX I²C 通过 DTC 传输

**说明（Help）**

启用使用 DTC 模块传输数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_DTC_ENABLED && CONFIG_I2C_RENESAS_RX_RIIC && CONFIG_I2C
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RENESAS_RX_DTC
```

**定义位置（Location）**：[`drivers/i2c/Kconfig.renesas_rx:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/Kconfig.renesas_rx#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 集成电路互连（Inter-Integrated Circuit，I²C）总线驱动 → Renesas RX I²C 控制器（Controller）

**配置项引用（Symbol References）**：[`CONFIG_I2C_RENESAS_RX_RIIC`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RENESAS_RX_RIIC)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_RENESAS_RX_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RENESAS_RX_DTC)。

<!-- kconfig-navigation -->

[上一章](P105_drivers_i2c_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P107_drivers_i2s_配置项参考.md)
