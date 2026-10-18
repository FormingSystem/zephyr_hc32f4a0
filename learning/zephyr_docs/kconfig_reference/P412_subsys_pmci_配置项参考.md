---
id: learning.zephyr-docs.kconfig-reference.page-412
title: "`subsys/pmci`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第412章\_`subsys/pmci`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/pmci` 的 16 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LIBMCTP_CONTROL_HANDLER_ENABLED"></a>

## 412.1 `CONFIG_LIBMCTP_CONTROL_HANDLER_ENABLED`

**提示（Prompt）**：libmctp 控制处理程序（Control Handler）

**说明（Help）**

启用 libmctp 控制处理程序（Control handler），处理管理组件传输协议（MCTP）的控制消息。如果应用不希望自行处理 MCTP 控制消息，或希望在 libmctp 控制处理程序之前拦截这些消息，可启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTP
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_MCTP"></a>

## 412.2 `CONFIG_MCTP`

**提示（Prompt）**：管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**说明（Help）**

启用管理组件传输协议（MCTP）子系统与模块使用

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_MCTP_HEAP_SIZE"></a>

## 412.3 `CONFIG_MCTP_HEAP_SIZE`

**提示（Prompt）**：MCTP 堆大小（Heap size）

**说明（Help）**

MCTP 需要堆（Heap）来分配数据包缓冲区。启动时向 MCTP 提供专用堆，因此无需指定 libmctp 的分配操作。本选项以字节为单位定义专用 MCTP 堆大小。对于小数据包，默认值为 1 KB。需要多数据包消息重组（Reassembly）时，堆至少应能容纳一个 MCTP 上下文结构，以及每个活动端点各一个 `CONFIG_MCTP_MAX_MESSAGE_SIZE` 字节的重组缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTP
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_MCTP_I2C_GPIO_CONTROLLER"></a>

## 412.4 `CONFIG_MCTP_I2C_GPIO_CONTROLLER`

**提示（Prompt）**：MCTP I2C 与 GPIO 控制器绑定（Controller binding）

**说明（Help）**

构建 MCTP I2C 与 GPIO 控制器绑定（Controller binding），通过 Zephyr 的 I2C 实时 I/O（RTIO）接口传输 MCTP，并使用目标设备发出的 GPIO 中断表示其写入请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C && CONFIG_I2C_RTIO && CONFIG_GPIO && CONFIG_MCTP
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_MCTP_I2C_GPIO_TARGET"></a>

## 412.5 `CONFIG_MCTP_I2C_GPIO_TARGET`

**提示（Prompt）**：MCTP I2C 与 GPIO 目标设备绑定（Target binding）

**说明（Help）**

构建 MCTP I2C 与 GPIO 目标设备绑定（Target binding），通过 Zephyr 的 I2C 目标接口传输 MCTP，并使用 GPIO 向总线控制器表示写入请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I2C && CONFIG_GPIO && CONFIG_MCTP
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_MCTP_I3C_CONTROLLER"></a>

## 412.6 `CONFIG_MCTP_I3C_CONTROLLER`

**提示（Prompt）**：MCTP I3C 控制器绑定（Controller binding）

**说明（Help）**

构建 MCTP I3C 控制器绑定（Controller binding），通过 Zephyr 的 I3C 接口传输 MCTP。此绑定可使用带内中断（IBI）信号或轮询模式接收目标设备通知。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_CONTROLLER && CONFIG_MCTP
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_I3C_CONTROLLER`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_CONTROLLER)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_MCTP_I3C_CONTROLLER_DATA_PATH"></a>

## 412.7 `CONFIG_MCTP_I3C_CONTROLLER_DATA_PATH`

**提示（Prompt）**：MCTP I3C 控制器的数据接收方式（Data reception method）

**说明（Help）**

选择 MCTP I3C 控制器从目标设备接收数据的方式，必须且只能选择一种。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTP_I3C_CONTROLLER && CONFIG_MCTP
```

**可选项（Choices）**

```text
CONFIG_MCTP_I3C_CONTROLLER_IBI_MODE
CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → MCTP I3C 控制器绑定（Controller binding）

**配置项引用（Symbol References）**：[`CONFIG_MCTP_I3C_CONTROLLER`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP_I3C_CONTROLLER)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)、[`CONFIG_MCTP_I3C_CONTROLLER_IBI_MODE`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP_I3C_CONTROLLER_IBI_MODE)、[`CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE)。

<a id="CONFIG_MCTP_I3C_CONTROLLER_IBI_MODE"></a>

## 412.8 `CONFIG_MCTP_I3C_CONTROLLER_IBI_MODE`

**提示（Prompt）**：使用带内中断（In-Band Interrupt，IBI）

**说明（Help）**

使用带内中断（In-Band Interrupt，IBI）信号通知数据可用，硬件支持时优先采用此方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_USE_IBI && <choice CONFIG_MCTP_I3C_CONTROLLER_DATA_PATH>
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → MCTP I3C 控制器绑定（Controller binding） → MCTP I3C 控制器的数据接收方式（Data reception method）

**配置项引用（Symbol References）**：[`CONFIG_I3C_USE_IBI`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_USE_IBI)、[`CONFIG_MCTP_I3C_CONTROLLER_DATA_PATH`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP_I3C_CONTROLLER_DATA_PATH)。

<a id="CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE"></a>

## 412.9 `CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE`

**提示（Prompt）**：使用轮询模式（Polling mode）

**说明（Help）**

周期性轮询 I3C 目标设备，检查是否有待处理数据。在带内中断（IBI）不可用或不受支持时使用此方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTP_I3C_CONTROLLER_DATA_PATH>
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → MCTP I3C 控制器绑定（Controller binding） → MCTP I3C 控制器的数据接收方式（Data reception method）

**配置项引用（Symbol References）**：[`CONFIG_MCTP_I3C_CONTROLLER_DATA_PATH`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP_I3C_CONTROLLER_DATA_PATH)。

<a id="CONFIG_MCTP_I3C_CONTROLLER_POLL_INTERVAL_MS"></a>

## 412.10 `CONFIG_MCTP_I3C_CONTROLLER_POLL_INTERVAL_MS`

**提示（Prompt）**：MCTP I3C 轮询间隔（Polling interval，毫秒）

**说明（Help）**

检查每个已配置 I3C 端点（Endpoint）是否有待处理数据的轮询间隔，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE && CONFIG_MCTP_I3C_CONTROLLER && CONFIG_MCTP
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 60000]
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → MCTP I3C 控制器绑定（Controller binding）

**配置项引用（Symbol References）**：[`CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP_I3C_CONTROLLER_POLLING_MODE)、[`CONFIG_MCTP_I3C_CONTROLLER`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP_I3C_CONTROLLER)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_MCTP_I3C_TARGET"></a>

## 412.11 `CONFIG_MCTP_I3C_TARGET`

**提示（Prompt）**：MCTP I3C 目标设备绑定（Target binding）

**说明（Help）**

构建 MCTP I3C 目标设备绑定（Target binding），通过 Zephyr 的 I3C 目标接口传输 MCTP，并可选择使用带内中断（IBI）向总线控制器发出发送消息的请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_I3C_TARGET && CONFIG_MCTP
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_I3C_TARGET`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_TARGET)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_MCTP_LOG_CUSTOM_ZEPHYR"></a>

## 412.12 `CONFIG_MCTP_LOG_CUSTOM_ZEPHYR`

**提示（Prompt）**：将 libmctp 日志接入 Zephyr 日志系统（Logging）

**说明（Help）**

编译相应支持，使用配置的 MCTP 日志级别，将 libmctp 日志转交给 Zephyr 日志子系统（Logging subsystem）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCTP
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_MCTP_MAX_MESSAGE_SIZE"></a>

## 412.13 `CONFIG_MCTP_MAX_MESSAGE_SIZE`

**提示（Prompt）**：MCTP 重组消息（Reassembled message）的最大大小

**说明（Help）**

可由多个 MCTP 数据包重组出的单条 MCTP 消息的最大大小，单位为字节。每当多数据包消息开始到达时，libmctp 从 MCTP 堆（Heap）分配一个此大小的缓冲区。因此，`CONFIG_MCTP_HEAP_SIZE` 至少应足以为每个同时活动的重组上下文（Reassembly context）容纳一个这样的缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTP
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_MCTP_UART"></a>

## 412.14 `CONFIG_MCTP_UART`

**提示（Prompt）**：MCTP 通用异步收发器（UART）绑定

**说明（Help）**

构建 MCTP UART 绑定（Binding），通过 Zephyr 的异步 UART 接口传输 MCTP。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_MCTP
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_MCTP_USB"></a>

## 412.15 `CONFIG_MCTP_USB`

**提示（Prompt）**：MCTP USB 绑定（Binding）

**说明（Help）**

构建 MCTP USB 绑定（Binding），通过 Zephyr 的 USB 设备接口传输 MCTP。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT && CONFIG_MCTP
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_MCTP_USB_TX_TIMEOUT"></a>

## 412.16 `CONFIG_MCTP_USB_TX_TIMEOUT`

**提示（Prompt）**：MCTP USB 发送超时（Transmit timeout，毫秒）

**说明（Help）**

设置 MCTP USB 发送超时（Transmit timeout），单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTP_USB && CONFIG_MCTP
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/pmci/mctp/Kconfig.usb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/pmci/mctp/Kconfig.usb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCTP_USB`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP_USB)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<!-- kconfig-navigation -->

[上一章](P411_subsys_pm_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P413_subsys_portability_配置项参考_1.md)
