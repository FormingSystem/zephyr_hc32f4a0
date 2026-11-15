---
id: learning.zephyr-docs.kconfig-reference.page-66
title: "`drivers/console`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第66章\_`drivers/console`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/console` 的 38 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CONSOLE"></a>

## 66.1 `CONFIG_CONSOLE`

**提示（Prompt）**：控制台驱动（Console Drivers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SHELL_BACKEND_RTT
```

**定义位置（Location）**：[`drivers/console/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_RTT)。

<a id="CONFIG_CONSOLE_HANDLER"></a>

## 66.2 `CONFIG_CONSOLE_HANDLER`

**提示（Prompt）**：控制台输入处理程序（Console Input Handler）

**说明（Help）**

启用控制台输入处理程序（Console Input Handler），以便编写串口控制台（Serial Console）与操作系统之间的简单交互。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_CONSOLE && CONFIG_SERIAL_SUPPORT_INTERRUPT && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
```

**被选择（Selected by）**

```text
CONFIG_CONSOLE_GETLINE
```

**定义位置（Location）**：[`drivers/console/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_CONSOLE_GETLINE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CONSOLE_GETLINE)。

<a id="CONFIG_CONSOLE_HAS_DRIVER"></a>

## 66.3 `CONFIG_CONSOLE_HAS_DRIVER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由控制台（Console）驱动启用的选项，表示系统存在某种控制台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE
```

**被选择（Selected by）**

```text
CONFIG_UART_CONSOLE
CONFIG_JAILHOUSE_DEBUG_CONSOLE
CONFIG_RAM_CONSOLE
CONFIG_RTT_CONSOLE
CONFIG_IPM_CONSOLE_SENDER
CONFIG_IPM_CONSOLE
CONFIG_XTENSA_SIM_CONSOLE
CONFIG_POSIX_ARCH_CONSOLE
CONFIG_SEMIHOST_CONSOLE
CONFIG_EFI_CONSOLE
CONFIG_WINSTREAM_CONSOLE
CONFIG_WHISPER_CONSOLE
CONFIG_WCH_SDI_CONSOLE
CONFIG_BT_DEBUG_MONITOR_UART
CONFIG_BT_DEBUG_MONITOR_RTT
```

**定义位置（Location）**：[`drivers/console/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)、[`CONFIG_JAILHOUSE_DEBUG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_JAILHOUSE_DEBUG_CONSOLE)、[`CONFIG_RAM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_RAM_CONSOLE)、[`CONFIG_RTT_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_RTT_CONSOLE)、[`CONFIG_IPM_CONSOLE_SENDER`](P066_drivers_console_配置项参考.md#CONFIG_IPM_CONSOLE_SENDER)、[`CONFIG_IPM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_IPM_CONSOLE)、[`CONFIG_XTENSA_SIM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_XTENSA_SIM_CONSOLE)、[`CONFIG_POSIX_ARCH_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_POSIX_ARCH_CONSOLE)、[`CONFIG_SEMIHOST_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_SEMIHOST_CONSOLE)、[`CONFIG_EFI_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_EFI_CONSOLE)、[`CONFIG_WINSTREAM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_WINSTREAM_CONSOLE)、[`CONFIG_WHISPER_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_WHISPER_CONSOLE)、[`CONFIG_WCH_SDI_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_WCH_SDI_CONSOLE)、[`CONFIG_BT_DEBUG_MONITOR_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEBUG_MONITOR_UART)、[`CONFIG_BT_DEBUG_MONITOR_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEBUG_MONITOR_RTT)。

<a id="CONFIG_CONSOLE_INIT_PRIORITY"></a>

## 66.4 `CONFIG_CONSOLE_INIT_PRIORITY`

**提示（Prompt）**：控制台初始化优先级（Console Init Priority）

**说明（Help）**

控制台（Console）驱动设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
60 if CONFIG_UART_CONSOLE || CONFIG_XTENSA_SIM_CONSOLE
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/console/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)、[`CONFIG_XTENSA_SIM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_XTENSA_SIM_CONSOLE)、[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<a id="CONFIG_CONSOLE_INPUT_MAX_LINE_LEN"></a>

## 66.5 `CONFIG_CONSOLE_INPUT_MAX_LINE_LEN`

**提示（Prompt）**：控制台输入行最大长度（Maximum Input Line Length）

**说明（Help）**

用于修改控制台输入（Console Input）允许的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/console/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_EFI_CONSOLE"></a>

## 66.6 `CONFIG_EFI_CONSOLE`

**提示（Prompt）**：使用 EFI 控制台输出（EFI Console Output）

**说明（Help）**

启用后，使用可扩展固件接口（EFI）的控制台输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_X86_EFI_CONSOLE
```

**定义位置（Location）**：[`drivers/console/Kconfig:290`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L290)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)、[`CONFIG_X86_EFI_CONSOLE`](P039_arch_x86_配置项参考.md#CONFIG_X86_EFI_CONSOLE)。

<a id="CONFIG_IPM_CONSOLE"></a>

## 66.7 `CONFIG_IPM_CONSOLE`

**提示（Prompt）**：处理器间邮箱控制台（Inter-Processor Mailbox Console）

**说明（Help）**

启用通过处理器间邮箱（Inter-Processor Mailbox，IPM）通信的控制台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/console/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_IPM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPM)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)。

<a id="CONFIG_IPM_CONSOLE_LINE_BUF_LEN"></a>

## 66.8 `CONFIG_IPM_CONSOLE_LINE_BUF_LEN`

**提示（Prompt）**：IPM 控制台行缓冲区长度（Line Buffer Length）

**说明（Help）**

处理器间邮箱（IPM）控制台的行缓冲区（Line Buffer）长度，指定整行发送之前用于存放字符的缓冲区容量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_CONSOLE && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/console/Kconfig:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 处理器间邮箱控制台（Inter-Processor Mailbox Console）

**配置项引用（Symbol References）**：[`CONFIG_IPM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_IPM_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_IPM_CONSOLE_RECEIVER"></a>

## 66.9 `CONFIG_IPM_CONSOLE_RECEIVER`

**提示（Prompt）**：处理器间邮箱控制台接收方（IPM Console Receiver）

**说明（Help）**

启用处理器间邮箱（IPM）控制台的接收侧。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE
```

**定义位置（Location）**：[`drivers/console/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_IPM_CONSOLE_SENDER"></a>

## 66.10 `CONFIG_IPM_CONSOLE_SENDER`

**提示（Prompt）**：处理器间邮箱控制台发送方（IPM Console Sender）

**说明（Help）**

启用处理器间邮箱（IPM）控制台的发送侧。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/console/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)。

<a id="CONFIG_IPM_CONSOLE_STACK_SIZE"></a>

## 66.11 `CONFIG_IPM_CONSOLE_STACK_SIZE`

**提示（Prompt）**：IPM 控制台接收线程栈大小（Receiver Thread Stack Size）

**说明（Help）**

每个处理器间邮箱（IPM）控制台接收驱动实例都会创建一个工作线程（Worker Thread），打印来自远端 CPU 的消息。此处指定这些线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_CONSOLE_RECEIVER && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
2048 if CONFIG_COVERAGE_GCOV
512
```

**定义位置（Location）**：[`drivers/console/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 处理器间邮箱控制台接收方（IPM Console Receiver）

**配置项引用（Symbol References）**：[`CONFIG_IPM_CONSOLE_RECEIVER`](P066_drivers_console_配置项参考.md#CONFIG_IPM_CONSOLE_RECEIVER)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)。

<a id="CONFIG_JAILHOUSE_DEBUG_CONSOLE"></a>

## 66.12 `CONFIG_JAILHOUSE_DEBUG_CONSOLE`

**提示（Prompt）**：使用 JAILHOUSE_DEBUG 控制台（Console）

**说明（Help）**

将控制台消息输出到 Jailhouse 虚拟机监控器（Hypervisor）的调试控制台。如果还没有可工作的串口驱动，这对开发板启动调试（Board Bring-Up）很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64 && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/console/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)。

<a id="CONFIG_POSIX_ARCH_CONSOLE"></a>

## 66.13 `CONFIG_POSIX_ARCH_CONSOLE`

**提示（Prompt）**：使用主机终端作为控制台（Host Terminal Console）

**说明（Help）**

Zephyr 的 `printk` 消息将输出到主机终端的标准输出（stdout）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/console/Kconfig:255`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L255)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)。

<a id="CONFIG_POSIX_ARCH_CONSOLE_INIT_PRIORITY"></a>

## 66.14 `CONFIG_POSIX_ARCH_CONSOLE_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_ARCH_CONSOLE && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`drivers/console/Kconfig:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用主机终端作为控制台（Host Terminal Console）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_ARCH_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_POSIX_ARCH_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_POSIX_ARCH_CONSOLE_STDOUT_BUF_SIZE"></a>

## 66.15 `CONFIG_POSIX_ARCH_CONSOLE_STDOUT_BUF_SIZE`

**提示（Prompt）**：标准输出缓冲区大小（Standard Output Buffer Size）

**说明（Help）**

刷新到主机终端（Host Terminal）之前，暂存 `printk` 消息的缓冲区大小。遇到换行符或缓冲区满时刷新消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_ARCH_CONSOLE && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/console/Kconfig:269`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L269)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用主机终端作为控制台（Host Terminal Console）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_ARCH_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_POSIX_ARCH_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_RAM_CONSOLE"></a>

## 66.16 `CONFIG_RAM_CONSOLE`

**提示（Prompt）**：使用 RAM 控制台（RAM Console）

**说明（Help）**

将控制台消息输出到 RAM 缓冲区 `ram_console`，运行时可通过调试器（Debugger）查看。如果还没有可工作的串口驱动，这对开发板启动调试（Board Bring-Up）很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
CONFIG_RAM_CONSOLE_BUFFER_SECTION if n
```

**定义位置（Location）**：[`drivers/console/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)、[`CONFIG_RAM_CONSOLE_BUFFER_SECTION`](P066_drivers_console_配置项参考.md#CONFIG_RAM_CONSOLE_BUFFER_SECTION)。

<a id="CONFIG_RAM_CONSOLE_BUFFER_SECTION"></a>

## 66.17 `CONFIG_RAM_CONSOLE_BUFFER_SECTION`

**提示（Prompt）**：使用专用节作为 RAM 控制台缓冲区（Dedicated Section）

**说明（Help）**

使用专用节（Dedicated Section）作为 RAM 控制台缓冲区，其地址在构建前已知，便于调试器（Debugger）或并行运行的操作系统中的软件工具查看控制台输出消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RAM_CONSOLE && n && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_DIRECT_MAP if CONFIG_MMU
```

**定义位置（Location）**：[`drivers/console/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用 RAM 控制台（RAM Console）

**配置项引用（Symbol References）**：[`CONFIG_RAM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_RAM_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_KERNEL_DIRECT_MAP`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_DIRECT_MAP)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_RAM_CONSOLE_BUFFER_SIZE"></a>

## 66.18 `CONFIG_RAM_CONSOLE_BUFFER_SIZE`

**提示（Prompt）**：RAM 控制台缓冲区大小（RAM Console Buffer Size）

**说明（Help）**

RAM 控制台缓冲区的总大小。为确保始终以空字符（NULL）结尾，会保留一个字节不用，因此实际可用长度少一个字节。超过实际可用长度后，消息会回绕（Wrap Around）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RAM_CONSOLE && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
0 if CONFIG_RAM_CONSOLE_BUFFER_SECTION
1024
```

**定义位置（Location）**：[`drivers/console/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用 RAM 控制台（RAM Console）

**配置项引用（Symbol References）**：[`CONFIG_RAM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_RAM_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_RAM_CONSOLE_BUFFER_SECTION`](P066_drivers_console_配置项参考.md#CONFIG_RAM_CONSOLE_BUFFER_SECTION)。

<a id="CONFIG_RTT_CONSOLE"></a>

## 66.19 `CONFIG_RTT_CONSOLE`

**提示（Prompt）**：使用实时传输控制台（RTT Console）

**说明（Help）**

将控制台消息输出到 RAM 缓冲区，再由 SEGGER J-Link 软件读取并实时显示在计算机上。要求板上配套集成电路（Companion IC）支持 SEGGER J-Link。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_SHELL_BACKEND_RTT
```

**定义位置（Location）**：[`drivers/console/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_SEGGER_RTT)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)、[`CONFIG_SHELL_BACKEND_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_RTT)。

<a id="CONFIG_RTT_TX_RETRY_CNT"></a>

## 66.20 `CONFIG_RTT_TX_RETRY_CNT`

**提示（Prompt）**：发送重试次数（Number of TX Retries）

**说明（Help）**

丢弃当前字节并认定实时传输（RTT）会话不活动之前，允许的发送重试（TX Retry）次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTT_CONSOLE && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/console/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用实时传输控制台（RTT Console）

**配置项引用（Symbol References）**：[`CONFIG_RTT_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_RTT_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_RTT_TX_RETRY_DELAY_MS"></a>

## 66.21 `CONFIG_RTT_TX_RETRY_DELAY_MS`

**提示（Prompt）**：发送重试间隔，单位为毫秒（TX Retry Delay）

**说明（Help）**

两次发送重试（TX Retry）之间的休眠时间。实时传输（RTT）会话期间，主机定期拉取数据，周期从 1–2 毫秒起；RTT 流量增加时，包括主机到设备的流量，该周期可能增加。流量较大时可能丢失数据，需要增大延迟或重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTT_CONSOLE && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/console/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用实时传输控制台（RTT Console）

**配置项引用（Symbol References）**：[`CONFIG_RTT_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_RTT_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_RTT_TX_RETRY_IN_INTERRUPT"></a>

## 66.22 `CONFIG_RTT_TX_RETRY_IN_INTERRUPT`

**提示（Prompt）**：中断上下文中忙等待发送重试（Busy Wait for TX Retry）

**说明（Help）**

启用后，当实时传输（RTT）控制台认为会话处于活动状态时，会在发送重试之间忙等待（Busy Wait）。流量较大时可能丢失数据，需要增大延迟或重试次数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTT_CONSOLE && CONFIG_CONSOLE
```

**定义位置（Location）**：[`drivers/console/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用实时传输控制台（RTT Console）

**配置项引用（Symbol References）**：[`CONFIG_RTT_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_RTT_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_SEMIHOST_CONSOLE"></a>

## 66.23 `CONFIG_SEMIHOST_CONSOLE`

**提示（Prompt）**：使用半主机控制台（Semihosting Console）

**说明（Help）**

启用后，使用半主机（Semihosting）作为控制台。更完整的半主机说明参阅 `SEMIHOST`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEMIHOST && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/console/Kconfig:278`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L278)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SEMIHOST`](P032_arch_common_配置项参考.md#CONFIG_SEMIHOST)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)。

<a id="CONFIG_UART_CONSOLE"></a>

## 66.24 `CONFIG_UART_CONSOLE`

**提示（Prompt）**：使用 UART 控制台（UART Console）

**说明（Help）**

启用后，使用一个通用异步收发器（UART）作为控制台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL && CONFIG_SERIAL_HAS_DRIVER && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_INSTRUMENTATION
```

**被弱选择（Implied by）**

```text
CONFIG_MPIPE_PLAYER
```

**定义位置（Location）**：[`drivers/console/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)、[`CONFIG_INSTRUMENTATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION)、[`CONFIG_MPIPE_PLAYER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_PLAYER)。

<a id="CONFIG_UART_CONSOLE_DEBUG_SERVER_HOOKS"></a>

## 66.25 `CONFIG_UART_CONSOLE_DEBUG_SERVER_HOOKS`

**提示（Prompt）**：调试控制台中的调试服务器钩子（Debug Server Hooks）

**说明（Help）**

允许 GDB 等调试服务器代理（Debug Server Agent）接管经过控制台逻辑的数据。调试服务器检查收到的字符：如果是某类控制字符（Control Character），则自行处理；如果没有特殊含义，则交由常规控制台代码处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_CONSOLE && CONFIG_CONSOLE
```

**定义位置（Location）**：[`drivers/console/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用 UART 控制台（UART Console）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_UART_CONSOLE_INPUT_EXPIRED"></a>

## 66.26 `CONFIG_UART_CONSOLE_INPUT_EXPIRED`

**提示（Prompt）**：支持 UART 控制台输入过期机制（Input Expired Mechanism）

**说明（Help）**

允许通知电源管理（Power Management）模块，UART 控制台模块当前正在使用。如果控制台未收到任何输入消息的时长超过过期超时（Expired Timeout），例如 `UART_CONSOLE_INPUT_EXPIRED_TIMEOUT`，则允许电源管理模块进入休眠／深度休眠（Sleep / Deep Sleep），并关闭 UART 控制台模块的时钟。

启用 `CONFIG_PM` 时，此机制为用户组织输入消息留出一个时间窗口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_CONSOLE && CONFIG_PM && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/console/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用 UART 控制台（UART Console）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_UART_CONSOLE_INPUT_EXPIRED_TIMEOUT"></a>

## 66.27 `CONFIG_UART_CONSOLE_INPUT_EXPIRED_TIMEOUT`

**提示（Prompt）**：UART 控制台使用中标志保持为真的固定时间（In-Use Flag Duration）

**说明（Help）**

让 UART 控制台使用中标志（In-Use Flag）保持为真的固定时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_CONSOLE_INPUT_EXPIRED && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
15000
```

**定义位置（Location）**：[`drivers/console/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用 UART 控制台（UART Console） → 支持 UART 控制台输入过期机制（Input Expired Mechanism）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE_INPUT_EXPIRED`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE_INPUT_EXPIRED)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_UART_CONSOLE_MCUMGR"></a>

## 66.28 `CONFIG_UART_CONSOLE_MCUMGR`

**提示（Prompt）**：UART 控制台 MCUmgr 透传（MCUmgr Passthrough）

**说明（Help）**

允许 UART 控制台接收用于镜像升级（Image Upgrade）和设备管理（Device Management）的 MCUmgr 帧。启用后，UART 控制台不处理这些帧，而是将其交给命令行（Shell）等上层模块。未设置时，传入的 MCUmgr 帧会被丢弃。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_CONSOLE && CONFIG_CONSOLE
```

**定义位置（Location）**：[`drivers/console/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用 UART 控制台（UART Console）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_UART_MCUMGR"></a>

## 66.29 `CONFIG_UART_MCUMGR`

**提示（Prompt）**：MCUmgr UART 驱动（Driver）

**说明（Help）**

启用 MCUmgr UART 驱动，使应用能够通过 UART 使用基于控制台的 MCUmgr 协议进行镜像升级（Image Upgrade）和设备管理（Device Management）。与控制台 UART 驱动不同，此驱动不检查收到的数据；接收协议数据的所有处理均由应用提供的回调（Callback）完成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`drivers/console/Kconfig:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_UART_MCUMGR_RAW_PROTOCOL"></a>

## 66.30 `CONFIG_UART_MCUMGR_RAW_PROTOCOL`

**提示（Prompt）**：原始协议，不使用基于控制台的 SMP（Raw Protocol）

**说明（Help）**

发送给设备或由设备发出的命令采用原始 MCUmgr 格式（Raw MCUmgr Format），而不是基于控制台的简单管理协议（SMP over Console）格式，即不进行 Base64 编码，也不添加额外的控制台专用部分。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MCUMGR && CONFIG_CONSOLE
```

**定义位置（Location）**：[`drivers/console/Kconfig:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → MCUmgr UART 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_MCUMGR`](P066_drivers_console_配置项参考.md#CONFIG_UART_MCUMGR)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_UART_MCUMGR_RX_BUF_COUNT"></a>

## 66.31 `CONFIG_UART_MCUMGR_RX_BUF_COUNT`

**提示（Prompt）**：UART 接收 MCUmgr 分片的缓冲区数量（Receive Buffer Count）

**说明（Help）**

指定 MCUmgr UART 接收缓冲区（Receive Buffer）数量。这些缓冲区在重组（Reassembly）之前保存收到的 MCUmgr 分片（Fragment）。

使用基于控制台的简单管理协议（SMP over Console）时，每个缓冲区保存一行接收数据，直到该行被解码到 SMP 数据包缓冲区中。因此，此值限制可以排队等待处理的分片数量，不限制 SMP 数据包大小；后者由 `MCUMGR_TRANSPORT_NETBUF_SIZE` 设置。

对于原始 UART 模式，即不使用 SMP over Console，原文将此值描述为传给 SMP 处理代码的缓冲区大小，该缓冲区会直接放入 `netbuf`；因此，与 SMP over Console 不同，此值应无需改变默认设置。

译注：本项标题与前半段描述缓冲区“数量”，原文最后一段却称其为“大小”；这里保留上游两种表述，不自行合并为同一含义。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MCUMGR && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/console/Kconfig:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → MCUmgr UART 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_MCUMGR`](P066_drivers_console_配置项参考.md#CONFIG_UART_MCUMGR)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_UART_MCUMGR_RX_BUF_SIZE"></a>

## 66.32 `CONFIG_UART_MCUMGR_RX_BUF_SIZE`

**提示（Prompt）**：UART 接收 MCUmgr 分片的缓冲区大小，单位为字节（Receive Buffer Size）

**说明（Help）**

指定 MCUmgr UART 接收缓冲区（Receive Buffer）的大小，单位为字节。必须足够容纳 MCUmgr 客户端发送的任意一行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_MCUMGR && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/console/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → MCUmgr UART 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_UART_MCUMGR`](P066_drivers_console_配置项参考.md#CONFIG_UART_MCUMGR)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_WCH_SDI_CONSOLE"></a>

## 66.33 `CONFIG_WCH_SDI_CONSOLE`

**提示（Prompt）**：沁恒 SDI 控制台（WCH SDI Console）

**说明（Help）**

通过 SDI 调试模块向主机发送控制台消息，可由 `minichlink` 等兼容 SDI 的调试器（Debugger）显示。注意，此控制台是阻塞式（Blocking）的，尤其在没有连接调试器时，可能拖慢运行。发布构建（Release Build）中可考虑禁用控制台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_SDI_CONSOLE_ENABLED && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/console/Kconfig:332`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L332)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)。

<a id="CONFIG_WHISPER_CONSOLE"></a>

## 66.34 `CONFIG_WHISPER_CONSOLE`

**提示（Prompt）**：Whisper 控制台（Console）

**说明（Help）**

使用 RISC-V Whisper 指令集模拟器（Instruction Set Simulator，ISS）提供的控制台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WHISPER_TARGET && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/console/Kconfig:325`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L325)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WHISPER_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_WHISPER_TARGET)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)。

<a id="CONFIG_WINSTREAM_CONSOLE"></a>

## 66.35 `CONFIG_WINSTREAM_CONSOLE`

**提示（Prompt）**：使用 Winstream 控制台（Console）

**说明（Help）**

将 Winstream 用作控制台。更多信息参阅 `WINSTREAM` 的 Kconfig 帮助。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WINSTREAM && CONFIG_CONSOLE
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/console/Kconfig:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WINSTREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WINSTREAM)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)。

<a id="CONFIG_WINSTREAM_CONSOLE_STATIC"></a>

## 66.36 `CONFIG_WINSTREAM_CONSOLE_STATIC`

**提示（Prompt）**：Winstream 控制台使用静态／可链接内存（Static / Linkable Memory）

**说明（Help）**

Winstream 控制台可配置为使用简单的链接器分配内存（Linker Memory），以帮助避免平台层手动管理内存。该内存应由 `_winstream_console_buf` 符号指向，大小通过 `CONFIG_WINSTREAM_CONSOLE_SIZE` 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WINSTREAM_CONSOLE && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_FAMILY_INTEL_ADSP
```

**定义位置（Location）**：[`drivers/console/Kconfig:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用 Winstream 控制台（Console）

**配置项引用（Symbol References）**：[`CONFIG_WINSTREAM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_WINSTREAM_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_WINSTREAM_CONSOLE_STATIC_SIZE"></a>

## 66.37 `CONFIG_WINSTREAM_CONSOLE_STATIC_SIZE`

**提示（Prompt）**：Winstream 控制台缓冲区大小（Console Buffer Size）

**说明（Help）**

Winstream 控制台缓冲区（Console Buffer）的大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WINSTREAM_CONSOLE && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
32768
```

**定义位置（Location）**：[`drivers/console/Kconfig:317`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L317)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → 使用 Winstream 控制台（Console）

**配置项引用（Symbol References）**：[`CONFIG_WINSTREAM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_WINSTREAM_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)。

<a id="CONFIG_XTENSA_SIM_CONSOLE"></a>

## 66.38 `CONFIG_XTENSA_SIM_CONSOLE`

**提示（Prompt）**：使用 Xtensa 模拟器控制台（Simulator Console）

**说明（Help）**

使用模拟器控制台（Simulator Console）打印消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SIMULATOR_XTENSA && !CONFIG_WINSTREAM_CONSOLE && !CONFIG_SEMIHOST_CONSOLE && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/console/Kconfig:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/console/Kconfig#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SIMULATOR_XTENSA`](P040_arch_xtensa_配置项参考.md#CONFIG_SIMULATOR_XTENSA)、[`CONFIG_WINSTREAM_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_WINSTREAM_CONSOLE)、[`CONFIG_SEMIHOST_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_SEMIHOST_CONSOLE)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_CONSOLE_HAS_DRIVER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HAS_DRIVER)。

<!-- kconfig-navigation -->

[上一章](P065_drivers_comparator_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P067_drivers_coredump_配置项参考.md)
