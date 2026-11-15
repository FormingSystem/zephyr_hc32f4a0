---
id: learning.zephyr-docs.kconfig-reference.page-388
title: "`subsys/modbus`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第388章\_`subsys/modbus`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/modbus` 的 15 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MODBUS"></a>

## 388.1 `CONFIG_MODBUS`

**提示（Prompt）**：Modbus 支持（support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_MODBUS_ASCII_MODE"></a>

## 388.2 `CONFIG_MODBUS_ASCII_MODE`

**提示（Prompt）**：Modbus ASCII 传输模式（transmission mode）

**说明（Help）**

启用 ASCII 传输模式（transmission mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS_SERIAL && CONFIG_MODBUS
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → 串行线路上的 Modbus 支持（Modbus over serial line）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_SERIAL`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS_SERIAL)、[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)。

<a id="CONFIG_MODBUS_BUFFER_SIZE"></a>

## 388.3 `CONFIG_MODBUS_BUFFER_SIZE`

**提示（Prompt）**：Modbus 缓冲区大小（buffer size）

**说明（Help）**

Modbus 缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[64, 256]
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)。

<a id="CONFIG_MODBUS_FC08_DIAGNOSTIC"></a>

## 388.4 `CONFIG_MODBUS_FC08_DIAGNOSTIC`

**提示（Prompt）**：功能码 08 诊断支持（FC08 Diagnostic）

**说明（Help）**

启用功能码 `08` 的诊断支持（Diagnostic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS_SERVER && CONFIG_MODBUS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODBUS_SERVER)、[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MODBUS_SERVER`。

<a id="CONFIG_MODBUS_FP_EXTENSIONS"></a>

## 388.5 `CONFIG_MODBUS_FP_EXTENSIONS`

**提示（Prompt）**：浮点扩展（Floating-Point extensions）

**说明（Help）**

启用浮点扩展（Floating-Point extensions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)。

<a id="CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE"></a>

## 388.6 `CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE`

**提示（Prompt）**：不符合规范的串行模式（Non-compliant serial mode）

**说明（Help）**

允许不符合规范的停止位（stop bits）和奇偶校验位（parity bits）设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS_SERIAL && CONFIG_MODBUS
```

**被选择（Selected by）**

```text
CONFIG_PZEM004T
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_SERIAL`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS_SERIAL)、[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)、[`CONFIG_PZEM004T`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PZEM004T)。

<a id="CONFIG_MODBUS_NUMOF_RAW_ADU"></a>

## 388.7 `CONFIG_MODBUS_NUMOF_RAW_ADU`

**提示（Prompt）**：原始应用数据单元（ADU）实例数量

**说明（Help）**

原始应用数据单元（raw ADU）实例的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS_RAW_ADU && CONFIG_MODBUS
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → Modbus 原始应用数据单元支持（raw ADU）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_RAW_ADU`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS_RAW_ADU)、[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)。

<a id="CONFIG_MODBUS_RAW_ADU"></a>

## 388.8 `CONFIG_MODBUS_RAW_ADU`

**提示（Prompt）**：Modbus 原始应用数据单元支持（raw ADU）

**说明（Help）**

启用 Modbus 原始应用数据单元（raw ADU）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)。

<a id="CONFIG_MODBUS_ROLE_CLIENT"></a>

## 388.9 `CONFIG_MODBUS_ROLE_CLIENT`

**提示（Prompt）**：客户端支持（Client support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → 支持的节点角色（Supported node roles）

<a id="CONFIG_MODBUS_ROLE_CLIENT_SERVER"></a>

## 388.10 `CONFIG_MODBUS_ROLE_CLIENT_SERVER`

**提示（Prompt）**：客户端和服务器支持（Client and server support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → 支持的节点角色（Supported node roles）

<a id="CONFIG_MODBUS_ROLE_SERVER"></a>

## 388.11 `CONFIG_MODBUS_ROLE_SERVER`

**提示（Prompt）**：服务器支持（Server support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → 支持的节点角色（Supported node roles）

<a id="CONFIG_MODBUS_SERIAL"></a>

## 388.12 `CONFIG_MODBUS_SERIAL`

**提示（Prompt）**：串行线路上的 Modbus 支持（Modbus over serial line）

**说明（Help）**

启用串行线路上的 Modbus（Modbus over serial line）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL && CONFIG_SERIAL_HAS_DRIVER && DT_HAS_ZEPHYR_MODBUS_SERIAL_ENABLED && CONFIG_MODBUS
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_MODBUS_SERIAL_ASYNC_API"></a>

## 388.13 `CONFIG_MODBUS_SERIAL_ASYNC_API`

**提示（Prompt）**：串行 Modbus 的 UART 异步 API 支持（ASYNC API）

**说明（Help）**

串行 Modbus 使用 UART 异步 API（ASYNC API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS_SERIAL && CONFIG_UART_ASYNC_API && CONFIG_MODBUS
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → 串行线路上的 Modbus 支持（Modbus over serial line）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_SERIAL`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS_SERIAL)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)。

<a id="CONFIG_MODBUS_STACK_SIZE"></a>

## 388.14 `CONFIG_MODBUS_STACK_SIZE`

**提示（Prompt）**：Modbus 工作队列栈大小（workqueue stack size）

**说明（Help）**

Modbus 工作队列（workqueue）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS_WORKQUEUE && CONFIG_MODBUS
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → Modbus 使用专用工作队列（dedicated workqueue）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_WORKQUEUE`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS_WORKQUEUE)、[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)。

<a id="CONFIG_MODBUS_WORKQUEUE"></a>

## 388.15 `CONFIG_MODBUS_WORKQUEUE`

**提示（Prompt）**：Modbus 使用专用工作队列（dedicated workqueue）

**说明（Help）**

系统工作队列因性能问题或其他冲突而无法使用时，通过专用队列处理收到的应用数据单元（ADUs）。例如，系统工作队列繁忙，或调用者自身就在该队列上下文中时，客户端事务可能超时，因为响应处理也共享同一个队列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODBUS
```

**定义位置（Location）**：[`subsys/modbus/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS`](P388_subsys_modbus_配置项参考.md#CONFIG_MODBUS)。

<!-- kconfig-navigation -->

[上一章](P387_subsys_mgmt_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P389_subsys_modem_配置项参考.md)
