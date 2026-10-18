---
id: learning.zephyr-docs.kconfig-reference.page-180
title: "`drivers/usb`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第180章\_`drivers/usb`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/usb` 的 67 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_UDC_STM32_THREAD_PRIORITY"></a>

## 180.1 `CONFIG_UDC_STM32_THREAD_PRIORITY`

**提示（Prompt）**：STM32 USB 控制器驱动线程优先级

**说明（Help）**

STM32 USB 设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_STM32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.stm32:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.stm32#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → STM32 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_VIRTUAL"></a>

## 180.2 `CONFIG_UDC_VIRTUAL`

**提示（Prompt）**：虚拟 USB 设备控制器（Virtual USB Device Controller）驱动

**说明（Help）**

虚拟 USB 设备控制器（Virtual USB Device Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_UDC_VIRTUAL_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UVB
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.virtual:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.virtual#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UVB`](P180_drivers_usb_配置项参考_2.md#CONFIG_UVB)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_VIRTUAL_STACK_SIZE"></a>

## 180.3 `CONFIG_UDC_VIRTUAL_STACK_SIZE`

**提示（Prompt）**：虚拟控制器驱动内部线程栈大小

**说明（Help）**

虚拟设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_VIRTUAL && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.virtual:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.virtual#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → 虚拟 USB 设备控制器（Virtual USB Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_VIRTUAL`](P180_drivers_usb_配置项参考_2.md#CONFIG_UDC_VIRTUAL)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_VIRTUAL_THREAD_PRIORITY"></a>

## 180.4 `CONFIG_UDC_VIRTUAL_THREAD_PRIORITY`

**提示（Prompt）**：虚拟控制器驱动线程优先级

**说明（Help）**

虚拟设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_VIRTUAL && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.virtual:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.virtual#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → 虚拟 USB 设备控制器（Virtual USB Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_VIRTUAL`](P180_drivers_usb_配置项参考_2.md#CONFIG_UDC_VIRTUAL)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_WORKQUEUE"></a>

## 180.5 `CONFIG_UDC_WORKQUEUE`

**提示（Prompt）**：为 USB 设备控制器（UDC）驱动使用专用工作队列

**说明（Help）**

此选项为 USB 设备控制器（UDC）驱动提供专用工作队列（Dedicated Work Queue）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DRIVER
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_WORKQUEUE_PRIORITY"></a>

## 180.6 `CONFIG_UDC_WORKQUEUE_PRIORITY`

**提示（Prompt）**：UDC 工作队列优先级（Workqueue Priority）

**说明（Help）**

默认情况下，UDC 工作队列优先级与系统工作队列（System Workqueue）优先级相同。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_WORKQUEUE && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_SYSTEM_WORKQUEUE_PRIORITY
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → 为 USB 设备控制器（UDC）驱动使用专用工作队列

**配置项引用（Symbol References）**：[`CONFIG_UDC_WORKQUEUE`](P180_drivers_usb_配置项参考_2.md#CONFIG_UDC_WORKQUEUE)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_SYSTEM_WORKQUEUE_PRIORITY`](P002_kernel_配置项参考_2.md#CONFIG_SYSTEM_WORKQUEUE_PRIORITY)。

<a id="CONFIG_UDC_WORKQUEUE_STACK_SIZE"></a>

## 180.7 `CONFIG_UDC_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：UDC 工作队列栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_WORKQUEUE && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → 为 USB 设备控制器（UDC）驱动使用专用工作队列

**配置项引用（Symbol References）**：[`CONFIG_UDC_WORKQUEUE`](P180_drivers_usb_配置项参考_2.md#CONFIG_UDC_WORKQUEUE)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UHC_BUF_COUNT"></a>

## 180.8 `CONFIG_UHC_BUF_COUNT`

**提示（Prompt）**：池中的缓冲区数量

**说明（Help）**

池中的 USB 主机控制器（UHC）请求缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[16, 256]
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_BUF_FORCE_NOCACHE"></a>

## 180.9 `CONFIG_UHC_BUF_FORCE_NOCACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果驱动无法处理缓存内存中的缓冲区，则将缓冲区池放在非缓存内存区域（Nocache Memory Region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NOCACHE_MEMORY && CONFIG_DCACHE && CONFIG_UHC_DRIVER
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_BUF_POOL_SIZE"></a>

## 180.10 `CONFIG_UHC_BUF_POOL_SIZE`

**提示（Prompt）**：可用于缓冲区的内存

**说明（Help）**

可用于 USB 主机控制器（UHC）缓冲区的内存总量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[64, 32768]
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_DRIVER"></a>

## 180.11 `CONFIG_UHC_DRIVER`

**提示（Prompt）**：USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**说明（Help）**

USB 主机控制器（Host Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_NET_BUF
```

**被选择（Selected by）**

```text
CONFIG_USB_HOST_STACK
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_NET_BUF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF)、[`CONFIG_USB_HOST_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_UHC_DWC2"></a>

## 180.12 `CONFIG_UHC_DWC2`

**提示（Prompt）**：DWC2 USB 主机控制器驱动

**说明（Help）**

DWC2 USB 主机控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DWC2_ENABLED && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
CONFIG_REGULATOR if CONFIG_SOC_SERIES_NRF54L || CONFIG_SOC_SERIES_NRF71
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.dwc2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.dwc2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_SOC_SERIES_NRF54L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_SERIES_NRF71`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF71)。

<a id="CONFIG_UHC_DWC2_DEBOUNCE_DELAY_MS"></a>

## 180.13 `CONFIG_UHC_DWC2_DEBOUNCE_DELAY_MS`

**提示（Prompt）**：去抖延迟（Debounce Delay），单位为毫秒

**说明（Help）**

连接 USB 设备时，USB 2.0 规范要求去抖间隔（Debounce Interval）至少持续 100 ms，以使连接稳定；更多信息见 USB 2.0 第 7.1.7.3 节。去抖期间，不登记新的连接／断开事件。为留出余量，默认值设为 250 ms。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DWC2 && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
250
```

**取值范围（Ranges）**

```text
[100, 250]
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.dwc2:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.dwc2#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → DWC2 USB 主机控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_DWC2`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DWC2)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_DWC2_RESET_HOLD_MS"></a>

## 180.14 `CONFIG_UHC_DWC2_RESET_HOLD_MS`

**提示（Prompt）**：复位保持时间（Reset Hold），单位为毫秒

**说明（Help）**

根端口（Root Port）的复位保持时间，单位为毫秒。USB 2.0 要求普通复位信号至少保持有效 10 ms，但由根端口发出的复位必须至少持续 50 ms。默认值为 50 ms。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DWC2 && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[10, 50]
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.dwc2:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.dwc2#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → DWC2 USB 主机控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_DWC2`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DWC2)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_DWC2_RESET_RECOVERY_MS"></a>

## 180.15 `CONFIG_UHC_DWC2_RESET_RECOVERY_MS`

**提示（Prompt）**：复位恢复延迟（Reset Recovery Delay），单位为毫秒

**说明（Help）**

复位后的恢复延迟，单位为毫秒。USB 2.0 要求端口停止驱动复位后，系统软件至少留出 10 ms 供设备恢复，再要求连接的设备响应数据传输。在此恢复间隔内，设备可以忽略数据传输。默认值为 30 ms。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DWC2 && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[10, 30]
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.dwc2:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.dwc2#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → DWC2 USB 主机控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_DWC2`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DWC2)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_DWC2_RESUME_DURATION_MS"></a>

## 180.16 `CONFIG_UHC_DWC2_RESUME_DURATION_MS`

**提示（Prompt）**：恢复信号持续时间（Resume Duration），单位为毫秒

**说明（Help）**

向根端口（Root Port）驱动恢复信号（Resume）的持续时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DWC2 && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[20, 4294967295]
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.dwc2:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.dwc2#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → DWC2 USB 主机控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_DWC2`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DWC2)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_DWC2_SET_ADDR_DELAY_MS"></a>

## 180.17 `CONFIG_UHC_DWC2_SET_ADDR_DELAY_MS`

**提示（Prompt）**：设置设备地址后的延迟

**说明（Help）**

原文引用 USB 2.0 第 9.2.6.3 节的要求：状态阶段（Status Stage）成功完成后，设备允许有 2 ms 的 `SetAddress()` 恢复间隔。此间隔结束时，设备必须能够接收发送到新地址的设置包（Setup Packet），并且不得再响应发送到旧地址的令牌（Token），除非新旧地址相同。为留出余量，默认值设为 10 ms。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DWC2 && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[2, 30]
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.dwc2:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.dwc2#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → DWC2 USB 主机控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_DWC2`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DWC2)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_DWC2_STACK_SIZE"></a>

## 180.18 `CONFIG_UHC_DWC2_STACK_SIZE`

**提示（Prompt）**：UHC DWC2 驱动线程栈大小

**说明（Help）**

DWC2 驱动线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DWC2 && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.dwc2:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.dwc2#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → DWC2 USB 主机控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_DWC2`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DWC2)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_DWC2_THREAD_PRIORITY"></a>

## 180.19 `CONFIG_UHC_DWC2_THREAD_PRIORITY`

**提示（Prompt）**：UHC DWC2 驱动线程优先级

**说明（Help）**

DWC2 驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DWC2 && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.dwc2:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.dwc2#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → DWC2 USB 主机控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_DWC2`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DWC2)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_DWC2_USBHS_VBUS_READY_TIMEOUT"></a>

## 180.20 `CONFIG_UHC_DWC2_USBHS_VBUS_READY_TIMEOUT`

**提示（Prompt）**：USBHS VBUS 就绪事件超时，单位为毫秒

**说明（Help）**

用于 nRF 微控制器（MCU）上 DWC2 USBHS 变体的 VBUS 就绪事件超时时间。使用 Nordic USBHS 控制器且 VBUS 尚未就绪时，`uhc_enable()` 将阻塞此处指定的时长。设为 0 表示无限等待。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_NRF54L || CONFIG_SOC_SERIES_NRF71) && CONFIG_UHC_DWC2 && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.dwc2:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.dwc2#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → DWC2 USB 主机控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_SERIES_NRF71`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_UHC_DWC2`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DWC2)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_MAX3421E"></a>

## 180.21 `CONFIG_UHC_MAX3421E`

**提示（Prompt）**：MAX3421E 驱动

**说明（Help）**

此选项启用带 SPI 接口的 MAX3421E USB 外设／主机控制器（Peripheral/Host Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX3421E_SPI_ENABLED && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.max3421e:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.max3421e#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_UHC_NXP_EHCI"></a>

## 180.22 `CONFIG_UHC_NXP_EHCI`

**提示（Prompt）**：NXP MCUX USB EHCI 主机控制器驱动

**说明（Help）**

用于 EHCI 的 NXP MCUX USB 主机控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_UHC_EHCI_ENABLED && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
CONFIG_NOCACHE_MEMORY if CONFIG_CPU_HAS_DCACHE
CONFIG_DYNAMIC_INTERRUPTS if CONFIG_UDC_NXP_EHCI
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.mcux:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.mcux#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_UDC_NXP_EHCI`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NXP_EHCI)。

<a id="CONFIG_UHC_NXP_IP3516HS"></a>

## 180.23 `CONFIG_UHC_NXP_IP3516HS`

**提示（Prompt）**：NXP MCUX USB IP3516HS 主机控制器驱动

**说明（Help）**

用于 IP3516HS 的 NXP MCUX USB 主机控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_UHC_IP3516HS_ENABLED && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.mcux:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.mcux#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_UHC_NXP_KHCI"></a>

## 180.24 `CONFIG_UHC_NXP_KHCI`

**提示（Prompt）**：NXP MCUX USB KHCI 主机控制器驱动

**说明（Help）**

用于 KHCI 的 NXP MCUX USB 主机控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_UHC_KHCI_ENABLED && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
CONFIG_DYNAMIC_INTERRUPTS if CONFIG_UDC_KINETIS
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.mcux:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.mcux#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_UDC_KINETIS`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_KINETIS)。

<a id="CONFIG_UHC_NXP_OHCI"></a>

## 180.25 `CONFIG_UHC_NXP_OHCI`

**提示（Prompt）**：NXP MCUX USB IP3516HS 主机控制器驱动

**说明（Help）**

用于 OHCI 的 NXP MCUX USB 主机控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_UHC_OHCI_ENABLED && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.mcux:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.mcux#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_UHC_NXP_THREAD_STACK_SIZE"></a>

## 180.26 `CONFIG_UHC_NXP_THREAD_STACK_SIZE`

**提示（Prompt）**：MCUX UHC 驱动内部线程栈大小

**说明（Help）**

驱动使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.mcux:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.mcux#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_RENESAS_RA"></a>

## 180.27 `CONFIG_UHC_RENESAS_RA`

**提示（Prompt）**：Renesas RA 系列 USB 主机控制器（UHC）驱动

**说明（Help）**

启用 Renesas RA 系列 USB 主机控制器（UHC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_UHC_ENABLED && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_USB_HOST
CONFIG_DYNAMIC_INTERRUPTS
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)、[`CONFIG_USE_RA_FSP_USB_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_USB_HOST)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)。

<a id="CONFIG_UHC_RENESAS_RA_MAX_MSGQ"></a>

## 180.28 `CONFIG_UHC_RENESAS_RA_MAX_MSGQ`

**提示（Prompt）**：Renesas RA 系列 UHC 驱动内部消息队列（Msgq）大小

**说明（Help）**

Renesas RA 设备控制器驱动内部消息队列（Msgq）的大小。

译注：标题为主机控制器（UHC），帮助原文写作设备控制器（Device Controller）；此处保留该差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_RENESAS_RA && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.renesas_ra:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.renesas_ra#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → Renesas RA 系列 USB 主机控制器（UHC）驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_RENESAS_RA`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_RENESAS_RA)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_RENESAS_RA_OSC_WAIT_RETRIES"></a>

## 180.29 `CONFIG_UHC_RENESAS_RA_OSC_WAIT_RETRIES`

**提示（Prompt）**：振荡器就绪事件（Oscillator Ready Event）的最大重试次数

**说明（Help）**

指定振荡器就绪事件（Oscillator Ready Event）的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_RENESAS_RA && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.renesas_ra:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.renesas_ra#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → Renesas RA 系列 USB 主机控制器（UHC）驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_RENESAS_RA`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_RENESAS_RA)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_RENESAS_RA_STACK_SIZE"></a>

## 180.30 `CONFIG_UHC_RENESAS_RA_STACK_SIZE`

**提示（Prompt）**：USB 主机控制器（UHC）驱动内部线程栈大小

**说明（Help）**

Renesas RA 设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_RENESAS_RA && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.renesas_ra:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.renesas_ra#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → Renesas RA 系列 USB 主机控制器（UHC）驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_RENESAS_RA`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_RENESAS_RA)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_RENESAS_RA_THREAD_PRIORITY"></a>

## 180.31 `CONFIG_UHC_RENESAS_RA_THREAD_PRIORITY`

**提示（Prompt）**：Renesas RA 系列 UHC 驱动线程优先级

**说明（Help）**

Renesas RA 设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_RENESAS_RA && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.renesas_ra:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.renesas_ra#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → Renesas RA 系列 USB 主机控制器（UHC）驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_RENESAS_RA`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_RENESAS_RA)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_UHC_VIRTUAL"></a>

## 180.32 `CONFIG_UHC_VIRTUAL`

**提示（Prompt）**：虚拟 USB 主机控制器（Virtual USB Host Controller）驱动

**说明（Help）**

虚拟 USB 主机控制器（Virtual USB Host Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_UHC_VIRTUAL_ENABLED && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UVB
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.virtual:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.virtual#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)、[`CONFIG_UVB`](P180_drivers_usb_配置项参考_2.md#CONFIG_UVB)。

<a id="CONFIG_UHC_XFER_COUNT"></a>

## 180.33 `CONFIG_UHC_XFER_COUNT`

**提示（Prompt）**：池中的传输数量

**说明（Help）**

可用的 USB 主机控制器（UHC）传输数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[2, 256]
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_USB_BC12"></a>

## 180.34 `CONFIG_USB_BC12`

**提示（Prompt）**：USB 电池充电规范 BC1.2 驱动

**说明（Help）**

启用 USB BC1.2 电池充电检测（Battery Charging Detection）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/usb/bc12/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/bc12/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_USB_BC12_NRF_USBHS"></a>

## 180.35 `CONFIG_USB_BC12_NRF_USBHS`

**提示（Prompt）**：Nordic USBHS 便携设备（PD）充电类型检测器

**说明（Help）**

Nordic 便携设备模式（Portable Device Mode）的 USB 充电类型检测器（Charging-Type Detector）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_USBHS_BC12_ENABLED && CONFIG_USB_BC12
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRF_USBHS_WRAPPER
CONFIG_REGULATOR
```

**定义位置（Location）**：[`drivers/usb/bc12/Kconfig.nrf54l:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/bc12/Kconfig.nrf54l#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_BC12`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_BC12)、[`CONFIG_NRF_USBHS_WRAPPER`](P179_drivers_usb_配置项参考_1.md#CONFIG_NRF_USBHS_WRAPPER)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_USB_BC12_PI3USB9201"></a>

## 180.36 `CONFIG_USB_BC12_PI3USB9201`

**提示（Prompt）**：Diodes PI3USB9201

**说明（Help）**

这是一种双角色 USB 充电类型检测器（Dual-Role USB Charging-Type Detector），可工作于主机模式或客户端模式（Host/Client Mode）。它支持电池充电规范修订版 1.2（Battery Charging Specification，BC1.2）：在主机模式下，可声明标准下行端口（SDP）、充电下行端口（CDP）或专用充电端口（DCP）类型。在便携设备或客户端模式下，它启动 BC1.2 检测以判断所连接的主机类型，并通过 I2C 接口报告检测结果。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_DIODES_PI3USB9201_ENABLED && CONFIG_USB_BC12
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/bc12/Kconfig.pi3usb9201:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/bc12/Kconfig.pi3usb9201#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_BC12`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_BC12)。

<a id="CONFIG_USB_BC12_PI3USB9201_CDP_ERRATA"></a>

## 180.37 `CONFIG_USB_BC12_PI3USB9201_CDP_ERRATA`

**提示（Prompt）**：PI3USB9201 CDP 勘误（Errata）

**说明（Help）**

启用此选项且充电模式配置为充电下行端口（Charging Downstream Port，CDP）时，成功完成 CDP 检测后，驱动会自动将充电模式设为标准下行端口（Standard Downstream Port，SDP）。这是针对 CDP 模式下 USB 数据线上出现毛刺（Glitch）的变通方案。注意，BC1.2 协商在切换至 SDP 模式前已完成，因此连接的便携设备仍可继续汲取最高 1.5 A 电流。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_BC12_PI3USB9201 && CONFIG_USB_BC12
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/bc12/Kconfig.pi3usb9201:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/bc12/Kconfig.pi3usb9201#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_BC12_PI3USB9201`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_BC12_PI3USB9201)、[`CONFIG_USB_BC12`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_BC12)。

<a id="CONFIG_USB_DC_HAS_HS_SUPPORT"></a>

## 180.38 `CONFIG_USB_DC_HAS_HS_SUPPORT`

**提示（Prompt）**：USB 设备控制器支持高速（High Speed）

**说明（Help）**

USB 设备控制器支持高速（High Speed）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_USB_DC_NXP_EHCI
CONFIG_USB_NATIVE_POSIX_HS
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_USB_DC_NXP_EHCI`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_NXP_EHCI)、[`CONFIG_USB_NATIVE_POSIX_HS`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_NATIVE_POSIX_HS)。

<a id="CONFIG_USB_DC_IT82XX2"></a>

## 180.39 `CONFIG_USB_DC_IT82XX2`

**提示（Prompt）**：ITE IT82XX2 USB 设备控制器驱动

**说明（Help）**

ITE IT82XX2 USB 设备控制器驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT82XX2_USB_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USB_DC_MSG_QUEUE_LEN"></a>

## 180.40 `CONFIG_USB_DC_MSG_QUEUE_LEN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

USB 设备控制器中断可为回调线程排入队列的消息最大数量

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_MCUX && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → NXP MCUX USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_MCUX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_MCUX)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)。

<a id="CONFIG_USB_DC_NUMAKER"></a>

## 180.41 `CONFIG_USB_DC_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker USB 1.1 设备控制器

**说明（Help）**

启用 Nuvoton NuMaker USB 1.1 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_USBD_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USB_DC_NUMAKER_MSG_HANDLER_THREAD_STACK_SIZE"></a>

## 180.42 `CONFIG_USB_DC_NUMAKER_MSG_HANDLER_THREAD_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（DC）消息处理线程栈大小

**说明（Help）**

消息处理线程的栈大小。驱动使用该线程处理来自 USB 设备控制器中断服务程序（USB DC ISR）的消息，即执行中断下半部（Interrupt Bottom Half）处理，包括对 USB 设备协议栈的回调。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DC_NUMAKER && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
1536
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nuvoton NuMaker USB 1.1 设备控制器

**配置项引用（Symbol References）**：[`CONFIG_USB_DC_NUMAKER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_NUMAKER)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)。

<a id="CONFIG_USB_DC_NUMAKER_MSG_QUEUE_SIZE"></a>

## 180.43 `CONFIG_USB_DC_NUMAKER_MSG_QUEUE_SIZE`

**提示（Prompt）**：USB 设备控制器（DC）消息队列大小

**说明（Help）**

驱动可排入队列、用于中断下半部（Interrupt Bottom Half）处理的消息最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DC_NUMAKER && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nuvoton NuMaker USB 1.1 设备控制器

**配置项引用（Symbol References）**：[`CONFIG_USB_DC_NUMAKER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_NUMAKER)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)。

<a id="CONFIG_USB_DC_NXP_EHCI"></a>

## 180.44 `CONFIG_USB_DC_NXP_EHCI`

**提示（Prompt）**：MXRT EHCI USB 设备控制器

**说明（Help）**

Kinetis 和 RT EHCI USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_EHCI_ENABLED && CONFIG_USB_MCUX && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_USB_DC_HAS_HS_SUPPORT
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → NXP MCUX USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_MCUX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_MCUX)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_USB_DC_HAS_HS_SUPPORT`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_HAS_HS_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_USB_DC_NXP_LPCIP3511"></a>

## 180.45 `CONFIG_USB_DC_NXP_LPCIP3511`

**提示（Prompt）**：LPC USB 设备控制器

**说明（Help）**

LPC USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPCIP3511_ENABLED && CONFIG_USB_MCUX && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USB_DC_HAS_HS_SUPPORT if n
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → NXP MCUX USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_MCUX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_MCUX)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_USB_DC_HAS_HS_SUPPORT`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_HAS_HS_SUPPORT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USB_DC_RPI_PICO"></a>

## 180.46 `CONFIG_USB_DC_RPI_PICO`

**提示（Prompt）**：Raspberry Pi Pico 器件的 USB 设备控制器驱动

**说明（Help）**

为 RP2 系列处理器启用 USB 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_USBD_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USB_DC_SAM0"></a>

## 180.47 `CONFIG_USB_DC_SAM0`

**提示（Prompt）**：SAM0 系列 USB 设备控制器驱动

**说明（Help）**

SAM0 系列 USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_USB_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USB_DC_SAM_USBC"></a>

## 180.48 `CONFIG_USB_DC_SAM_USBC`

**提示（Prompt）**：SAM4L USBC 设备控制器驱动

**说明（Help）**

SAM4L 系列 USBC 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_USBC_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USB_DC_SAM_USBHS"></a>

## 180.49 `CONFIG_USB_DC_SAM_USBHS`

**提示（Prompt）**：SAM 系列 USB 高速（HS）设备控制器驱动

**说明（Help）**

SAM 系列 USB 高速（HS）设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_USBHS_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_USB_DC_HAS_HS_SUPPORT if n
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_USB_DC_HAS_HS_SUPPORT`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_HAS_HS_SUPPORT)。

<a id="CONFIG_USB_DC_SMARTBOND"></a>

## 180.50 `CONFIG_USB_DC_SMARTBOND`

**提示（Prompt）**：SmartBond 系列 USB 设备控制器驱动

**说明（Help）**

SmartBond 系列 USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_USBD_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL_SMARTBOND
CONFIG_CLOCK_CONTROL
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_CLOCK_CONTROL_SMARTBOND`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_SMARTBOND)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_USB_DC_STM32"></a>

## 180.51 `CONFIG_USB_DC_STM32`

**提示（Prompt）**：STM32 器件的 USB 设备控制器驱动

**说明（Help）**

启用 STM32 系列 USB 设备控制器适配驱动（Shim Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_OTGFS_ENABLED || DT_HAS_ST_STM32_OTGHS_ENABLED || DT_HAS_ST_STM32_USB_ENABLED) && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_LL_USB
CONFIG_USE_STM32_HAL_PCD
CONFIG_USE_STM32_HAL_PCD_EX
CONFIG_USB_DC_HAS_HS_SUPPORT if n
CONFIG_PINCTRL
```

**弱选择（Implies）**

```text
CONFIG_USB_DEVICE_REMOTE_WAKEUP
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_USE_STM32_LL_USB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_USB)、[`CONFIG_USE_STM32_HAL_PCD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PCD)、[`CONFIG_USE_STM32_HAL_PCD_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PCD_EX)、[`CONFIG_USB_DC_HAS_HS_SUPPORT`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_HAS_HS_SUPPORT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_USB_DEVICE_REMOTE_WAKEUP`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_REMOTE_WAKEUP)。

<a id="CONFIG_USB_DC_STM32_CLOCK_CHECK"></a>

## 180.52 `CONFIG_USB_DC_STM32_CLOCK_CHECK`

**提示（Prompt）**：运行时 USB 48 MHz 时钟检查

**说明（Help）**

启用运行时 USB 48 MHz 时钟配置检查。某些特定情况下，此检查可能给出错误判定，应禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DC_STM32 && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y if !(CONFIG_SOC_SERIES_STM32F1X || CONFIG_SOC_SERIES_STM32F3X || CONFIG_SOC_SERIES_STM32U5X)
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → STM32 器件的 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DC_STM32`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_STM32)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F3X`、`CONFIG_SOC_SERIES_STM32U5X`。

<a id="CONFIG_USB_DEVICE_DRIVER"></a>

## 180.53 `CONFIG_USB_DEVICE_DRIVER`

**提示（Prompt）**：USB 设备控制器（Device Controller）驱动

**说明（Help）**

启用 USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**被选择（Selected by）**

```text
CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_REMOTE_WAKEUP"></a>

## 180.54 `CONFIG_USB_DEVICE_REMOTE_WAKEUP`

**提示（Prompt）**：远程唤醒支持（Remote Wakeup Support）

**说明（Help）**

USB 设备控制器支持远程唤醒（Remote Wakeup）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_DRIVER
```

**被弱选择（Implied by）**

```text
CONFIG_USB_DC_STM32
CONFIG_USB_NRFX
CONFIG_USB_MCUX
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_USB_DC_STM32`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_STM32)、[`CONFIG_USB_NRFX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_NRFX)、[`CONFIG_USB_MCUX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_MCUX)。

<a id="CONFIG_USB_DW"></a>

## 180.55 `CONFIG_USB_DW`

**提示（Prompt）**：DesignWare USB 设备控制器驱动

**说明（Help）**

DesignWare USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DWC2_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)。

<a id="CONFIG_USB_DW_USB_2_0"></a>

## 180.56 `CONFIG_USB_DW_USB_2_0`

**提示（Prompt）**：DesignWare 控制器和物理层（PHY）的 USB 2.0 规范支持

**说明（Help）**

表示是否支持 USB 2.0 版规范。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DW && CONFIG_USB_DEVICE_DRIVER
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → DesignWare USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DW`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DW)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)。

<a id="CONFIG_USB_KINETIS"></a>

## 180.57 `CONFIG_USB_KINETIS`

**提示（Prompt）**：Kinetis USB 设备控制器驱动

**说明（Help）**

Kinetis USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_USBD_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)。

<a id="CONFIG_USB_MCUX"></a>

## 180.58 `CONFIG_USB_MCUX`

**提示（Prompt）**：NXP MCUX USB 设备控制器驱动

**说明（Help）**

适用于 MXRT 和 LPC 片上系统（SoC）的 NXP MCUX USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NXP_EHCI_ENABLED || DT_HAS_NXP_LPCIP3511_ENABLED) && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**弱选择（Implies）**

```text
CONFIG_USB_DEVICE_REMOTE_WAKEUP
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_USB_DEVICE_REMOTE_WAKEUP`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_REMOTE_WAKEUP)。

<a id="CONFIG_USB_MCUX_THREAD_STACK_SIZE"></a>

## 180.59 `CONFIG_USB_MCUX_THREAD_STACK_SIZE`

**提示（Prompt）**：USB 驱动栈大小

**说明（Help）**

内部 USB 线程使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_MCUX && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
2048 if CONFIG_USB_DEVICE_LOG_LEVEL_DBG
1024
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → NXP MCUX USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_MCUX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_MCUX)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_USB_DEVICE_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_LOG_LEVEL_DBG)。

<a id="CONFIG_USB_NATIVE_POSIX"></a>

## 180.60 `CONFIG_USB_NATIVE_POSIX`

**提示（Prompt）**：原生 POSIX USB 设备控制器驱动

**说明（Help）**

原生 POSIX USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && CONFIG_EXTERNAL_LIBC && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_BOARD_NATIVE_SIM
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L232)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_EXTERNAL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXTERNAL_LIBC)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_BOARD_NATIVE_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NATIVE_SIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NATIVE_SIM`。

<a id="CONFIG_USB_NATIVE_POSIX_HS"></a>

## 180.61 `CONFIG_USB_NATIVE_POSIX_HS`

**提示（Prompt）**：高速支持（High Speed Support）

**说明（Help）**

在原生 POSIX USB 设备控制器驱动中启用高速（High Speed）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_NATIVE_POSIX && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_USB_DC_HAS_HS_SUPPORT
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L242)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → 原生 POSIX USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_NATIVE_POSIX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_NATIVE_POSIX)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_USB_DC_HAS_HS_SUPPORT`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_HAS_HS_SUPPORT)。

<a id="CONFIG_USB_NRFX"></a>

## 180.62 `CONFIG_USB_NRFX`

**提示（Prompt）**：Nordic Semiconductor USB 设备控制器驱动

**说明（Help）**

nRF USB 设备控制器驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_USBD_ENABLED && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRF_USBD_COMMON
CONFIG_NRFX_POWER
```

**弱选择（Implies）**

```text
CONFIG_USB_DEVICE_REMOTE_WAKEUP
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_NRF_USBD_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_NRF_USBD_COMMON)、[`CONFIG_NRFX_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_POWER)、[`CONFIG_USB_DEVICE_REMOTE_WAKEUP`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_REMOTE_WAKEUP)。

<a id="CONFIG_USB_NRFX_ATTACHED_EVENT_DELAY"></a>

## 180.63 `CONFIG_USB_NRFX_ATTACHED_EVENT_DELAY`

**提示（Prompt）**：USBD 连接事件延迟（Attached Event Delay）

**说明（Help）**

可配置的连接事件（Attached Event）延迟，单位为毫秒。此延迟可为 USB 充电控制器（Charging Controller）的初始化留出时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_NRFX && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nordic Semiconductor USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_NRFX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_NRFX)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)。

<a id="CONFIG_USB_NRFX_EVT_QUEUE_SIZE"></a>

## 180.64 `CONFIG_USB_NRFX_EVT_QUEUE_SIZE`

**提示（Prompt）**：USBD 事件队列（Event Queue）大小

**说明（Help）**

驱动内部事件队列（Event Queue）的大小。所需大小取决于正在使用的端点数量，即类实例（Class Instances）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_NRFX && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[4, 64]
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nordic Semiconductor USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_NRFX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_NRFX)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)。

<a id="CONFIG_USB_NRFX_WORK_QUEUE_STACK_SIZE"></a>

## 180.65 `CONFIG_USB_NRFX_WORK_QUEUE_STACK_SIZE`

**提示（Prompt）**：USBD 工作队列栈大小

**说明（Help）**

工作队列线程的栈大小。驱动使用该线程处理来自 USBD 中断服务程序（ISR）的事件，即执行端点回调并向 USB 设备协议栈发送适当通知。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_NRFX && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/usb/device/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/device/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nordic Semiconductor USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USB_NRFX`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_NRFX)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)。

<a id="CONFIG_UVB"></a>

## 180.66 `CONFIG_UVB`

**提示（Prompt）**：USB 虚拟总线（Virtual Bus）

**说明（Help）**

供虚拟 USB 设备控制器（UDC）和 USB 主机控制器（UHC）使用的 USB 虚拟总线服务。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_UDC_VIRTUAL
CONFIG_UHC_VIRTUAL
```

**定义位置（Location）**：[`drivers/usb/uvb/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uvb/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UDC_VIRTUAL`](P180_drivers_usb_配置项参考_2.md#CONFIG_UDC_VIRTUAL)、[`CONFIG_UHC_VIRTUAL`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_VIRTUAL)。

<a id="CONFIG_UVB_MAX_MESSAGES"></a>

## 180.67 `CONFIG_UVB_MAX_MESSAGES`

**提示（Prompt）**：可分配消息的最大数量

**说明（Help）**

可分配消息的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UVB
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[4, 256]
```

**定义位置（Location）**：[`drivers/usb/uvb/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uvb/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 虚拟总线（Virtual Bus）

**配置项引用（Symbol References）**：[`CONFIG_UVB`](P180_drivers_usb_配置项参考_2.md#CONFIG_UVB)。

<!-- kconfig-navigation -->

[上一章](P179_drivers_usb_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P181_drivers_usb_c_配置项参考.md)
