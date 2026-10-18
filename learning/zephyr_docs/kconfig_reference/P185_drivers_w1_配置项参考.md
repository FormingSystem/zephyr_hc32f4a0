---
id: learning.zephyr-docs.kconfig-reference.page-185
title: "`drivers/w1`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第185章\_`drivers/w1`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/w1` 的 15 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_W1"></a>

## 185.1 `CONFIG_W1`

**提示（Prompt）**：单总线（1-Wire）驱动

**说明（Help）**

启用单总线（1-Wire）驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/w1/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_W1_DS2477_85_COMMON"></a>

## 185.2 `CONFIG_W1_DS2477_85_COMMON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用共享的 DS2477/85 单总线（1-Wire）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_W1
```

**被选择（Selected by）**

```text
CONFIG_W1_DS2485
```

**定义位置（Location）**：[`drivers/w1/Kconfig.ds2477_85:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig.ds2477_85#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)、[`CONFIG_W1_DS2485`](P185_drivers_w1_配置项参考.md#CONFIG_W1_DS2485)。

<a id="CONFIG_W1_DS2482_800"></a>

## 185.3 `CONFIG_W1_DS2482_800`

**提示（Prompt）**：DS2482-800，八通道单总线主控制器（8-Channel 1-Wire Master）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_DS2482_800_ENABLED && CONFIG_W1
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/w1/Kconfig.ds2482-800:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig.ds2482-800#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_W1_DS2484"></a>

## 185.4 `CONFIG_W1_DS2484`

**提示（Prompt）**：DS2484 单通道单总线主控制器（Single-Channel 1-Wire Master）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_DS2484_ENABLED && CONFIG_W1
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/w1/Kconfig.ds2484:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig.ds2484#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_W1_DS2485"></a>

## 185.5 `CONFIG_W1_DS2485`

**提示（Prompt）**：DS2485 单总线主控制器（1-Wire Master）驱动

**说明（Help）**

启用 DS2485 单总线主控制器（W1 Master）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_DS2485_ENABLED && CONFIG_W1
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_W1_DS2477_85_COMMON
```

**定义位置（Location）**：[`drivers/w1/Kconfig.ds2485:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig.ds2485#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_W1_DS2477_85_COMMON`](P185_drivers_w1_配置项参考.md#CONFIG_W1_DS2477_85_COMMON)。

<a id="CONFIG_W1_INIT_PRIORITY"></a>

## 185.6 `CONFIG_W1_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

单总线（1-Wire）设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_W1
```

**默认值（Defaults）**

```text
65
```

**定义位置（Location）**：[`drivers/w1/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)。

<a id="CONFIG_W1_MAX32"></a>

## 185.7 `CONFIG_W1_MAX32`

**提示（Prompt）**：MAX32xxx MCU 单总线主控制器（1-Wire Master）驱动

**说明（Help）**

此选项为 MAX32xxx 微控制器（MCU）启用单总线主控制器（1-Wire Master）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_W1_ENABLED && CONFIG_W1
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/w1/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_W1_NET"></a>

## 185.8 `CONFIG_W1_NET`

**提示（Prompt）**：1-Wire 网络层（Network layer）

**说明（Help）**

启用单总线网络层（1-Wire Network Layer）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_W1
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/w1/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)。

<a id="CONFIG_W1_NET_FORCE_MULTIDROP_ADDRESSING"></a>

## 185.9 `CONFIG_W1_NET_FORCE_MULTIDROP_ADDRESSING`

**提示（Prompt）**：强制单总线多点寻址（1-Wire Multidrop Addressing）

**说明（Help）**

此选项忽略设备树源文件（DTS）中定义的单总线从设备（1-Wire Slave Device）数量。具体而言，它避免使用 `SKIP ROM` 命令；通常总线上只有一个单总线从设备时，会使用此命令。多数情况下无需启用此选项，但如果连接了多个未在 DTS 中指定的单总线设备，则必须启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_W1_NET && CONFIG_W1
```

**定义位置（Location）**：[`drivers/w1/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → 1-Wire 网络层（Network layer）

**配置项引用（Symbol References）**：[`CONFIG_W1_NET`](P185_drivers_w1_配置项参考.md#CONFIG_W1_NET)、[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)。

<a id="CONFIG_W1_SHELL"></a>

## 185.10 `CONFIG_W1_SHELL`

**提示（Prompt）**：单总线命令行（1-Wire Shell）

**说明（Help）**

启用用于测试的单总线命令行（1-Wire Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_W1
```

**定义位置（Location）**：[`drivers/w1/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)。

<a id="CONFIG_W1_SHELL_BUFFER_SIZE"></a>

## 185.11 `CONFIG_W1_SHELL_BUFFER_SIZE`

**提示（Prompt）**：单总线命令行缓冲区大小

**说明（Help）**

发送和接收缓冲区的大小，单位为字节。需要写入超过 8 字节时，还应相应增大 `SHELL_ARGC_MAX`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_W1_SHELL && CONFIG_W1
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/w1/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → 单总线命令行（1-Wire Shell）

**配置项引用（Symbol References）**：[`CONFIG_W1_SHELL`](P185_drivers_w1_配置项参考.md#CONFIG_W1_SHELL)、[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)。

<a id="CONFIG_W1_ZEPHYR_GPIO"></a>

## 185.12 `CONFIG_W1_ZEPHYR_GPIO`

**提示（Prompt）**：GPIO 单总线（1-Wire GPIO）

**说明（Help）**

此选项启用 Zephyr GPIO 单总线主控制器（1-Wire Master）驱动。按照原文描述，总线复位及位读写操作，通过 Zephyr GPIO 驱动接口之上的字节读写操作执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_W1_GPIO_ENABLED && CONFIG_W1
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/w1/Kconfig.zephyr_gpio:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig.zephyr_gpio#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)。

<a id="CONFIG_W1_ZEPHYR_GPIO_TIME_CRITICAL"></a>

## 185.13 `CONFIG_W1_ZEPHYR_GPIO_TIME_CRITICAL`

**提示（Prompt）**：强制使用时间关键操作（Time-critical Operations）

**说明（Help）**

此选项强制单总线（1-Wire）GPIO 驱动对总线复位及位读写使用时间关键操作（Time-critical Operations）。生成这些通信操作期间，不允许中断打断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_W1_ZEPHYR_GPIO && CONFIG_W1
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/w1/Kconfig.zephyr_gpio:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig.zephyr_gpio#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → GPIO 单总线（1-Wire GPIO）

**配置项引用（Symbol References）**：[`CONFIG_W1_ZEPHYR_GPIO`](P185_drivers_w1_配置项参考.md#CONFIG_W1_ZEPHYR_GPIO)、[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)。

<a id="CONFIG_W1_ZEPHYR_SERIAL"></a>

## 185.14 `CONFIG_W1_ZEPHYR_SERIAL`

**提示（Prompt）**：串行单总线（1-Wire Serial）

**说明（Help）**

此选项启用 Zephyr 串行单总线主控制器（1-Wire Master）驱动。总线复位及位读写操作，通过 Zephyr 串行驱动接口之上的字节读写操作执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_W1_SERIAL_ENABLED && CONFIG_W1
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`drivers/w1/Kconfig.zephyr_serial:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig.zephyr_serial#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_W1_ZEPHYR_SERIAL_BIT_TIMEOUT"></a>

## 185.15 `CONFIG_W1_ZEPHYR_SERIAL_BIT_TIMEOUT`

**提示（Prompt）**：位读取超时（Bit Read Timeout），单位为微秒

**说明（Help）**

位读取超时（Bit Read Timeout）指定驱动尝试读取 UART 字节的最长时间，该字节对应一个单总线标准速率数据位。对于 `poll_out` 不会阻塞到传输完成的串行驱动，此值至少必须大于 87 µs，即 `10bits / 115.2 kBd` 所对应的时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_W1_ZEPHYR_SERIAL && CONFIG_W1
```

**默认值（Defaults）**

```text
380
```

**定义位置（Location）**：[`drivers/w1/Kconfig.zephyr_serial:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/w1/Kconfig.zephyr_serial#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → 串行单总线（1-Wire Serial）

**配置项引用（Symbol References）**：[`CONFIG_W1_ZEPHYR_SERIAL`](P185_drivers_w1_配置项参考.md#CONFIG_W1_ZEPHYR_SERIAL)、[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)。

<!-- kconfig-navigation -->

[上一章](P184_drivers_virtualization_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P186_drivers_watchdog_配置项参考_1.md)
