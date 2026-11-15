---
id: learning.zephyr-docs.kconfig-reference.page-181
title: "`drivers/usb_c`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第181章\_`drivers/usb_c`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/usb_c` 的 27 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_USBC_PPC_DRIVER"></a>

## 181.1 `CONFIG_USBC_PPC_DRIVER`

**提示（Prompt）**：USB-C 电源路径控制器（PPC）驱动

**说明（Help）**

启用 USB-C 电源路径控制器（Power Path Controller，PPC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/usb_c/ppc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/ppc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_USBC_PPC_INIT_PRIORITY"></a>

## 181.2 `CONFIG_USBC_PPC_INIT_PRIORITY`

**提示（Prompt）**：USB-C PPC 驱动初始化优先级

**说明（Help）**

USB-C 电源路径控制器（PPC）驱动在 `POST_KERNEL` 阶段的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_PPC_DRIVER
```

**默认值（Defaults）**

```text
82
```

**定义位置（Location）**：[`drivers/usb_c/ppc/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/ppc/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_PPC_DRIVER)。

<a id="CONFIG_USBC_PPC_NUMAKER"></a>

## 181.3 `CONFIG_USBC_PPC_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker USB-C 电源路径控制器（PPC）

**说明（Help）**

为带 UTCPD 的 Nuvoton NuMaker 芯片启用 USB-C 电源路径控制器（PPC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_PPC_ENABLED && CONFIG_USBC_TCPC_NUMAKER && CONFIG_USBC_PPC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb_c/ppc/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/ppc/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_NUMAKER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_NUMAKER)、[`CONFIG_USBC_PPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_PPC_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USBC_PPC_NX20P3483"></a>

## 181.4 `CONFIG_USBC_PPC_NX20P3483`

**提示（Prompt）**：NXP NX20P3483 支持

**说明（Help）**

为 NXP NX20P3483 芯片启用 USB-C 电源路径控制器（PPC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_NX20P3483_ENABLED && CONFIG_USBC_PPC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb_c/ppc/Kconfig.nxp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/ppc/Kconfig.nxp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_PPC_DRIVER)。

<a id="CONFIG_USBC_PPC_NX20P3483_DUMP_FULL_REG_NAMES"></a>

## 181.5 `CONFIG_USBC_PPC_NX20P3483_DUMP_FULL_REG_NAMES`

**提示（Prompt）**：转储完整寄存器名称

**说明（Help）**

转储便于阅读的寄存器名称，而非寄存器偏移量（Offset）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_PPC_NX20P3483 && CONFIG_USBC_PPC_DRIVER
```

**定义位置（Location）**：[`drivers/usb_c/ppc/Kconfig.nxp:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/ppc/Kconfig.nxp#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动 → NXP NX20P3483 支持

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_NX20P3483`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_PPC_NX20P3483)、[`CONFIG_USBC_PPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_PPC_DRIVER)。

<a id="CONFIG_USBC_PPC_SHELL"></a>

## 181.6 `CONFIG_USBC_PPC_SHELL`

**提示（Prompt）**：电源路径控制器（PPC）的命令行命令

**说明（Help）**

添加用于操作和调试电源路径控制器（PPC）的实用命令行命令（Shell Commands）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_PPC_DRIVER
```

**定义位置（Location）**：[`drivers/usb_c/ppc/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/ppc/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_PPC_DRIVER)。

<a id="CONFIG_USBC_TCPC_DRIVER"></a>

## 181.7 `CONFIG_USBC_TCPC_DRIVER`

**提示（Prompt）**：USB-C Type-C 端口控制器（TCPC）驱动

**说明（Help）**

启用 USB Type-C 端口控制器（Type-C Port Controller，TCPC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_USBC_STACK
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_STACK)。

<a id="CONFIG_USBC_TCPC_FUSB307"></a>

## 181.8 `CONFIG_USBC_TCPC_FUSB307`

**提示（Prompt）**：USB-C TCPC 设备控制器驱动

**说明（Help）**

启用 FUSB307 的 Type-C 端口控制器（TCPC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ONNN_FUSB307_TCPC_ENABLED && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USBC_TCPC_TCPCI
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_fusb307:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_fusb307#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)、[`CONFIG_USBC_TCPC_TCPCI`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_TCPCI)。

<a id="CONFIG_USBC_TCPC_FUSB307_INIT_DELAY"></a>

## 181.9 `CONFIG_USBC_TCPC_FUSB307_INIT_DELAY`

**提示（Prompt）**：FUSB307 初始化延迟

**说明（Help）**

TCPC 每次初始化尝试之间的延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_FUSB307 && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_fusb307:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_fusb307#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB-C TCPC 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_FUSB307`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_FUSB307)、[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)。

<a id="CONFIG_USBC_TCPC_FUSB307_INIT_RETRIES"></a>

## 181.10 `CONFIG_USBC_TCPC_FUSB307_INIT_RETRIES`

**提示（Prompt）**：FUSB307 初始化重试次数

**说明（Help）**

将执行的初始化尝试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_FUSB307 && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_fusb307:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_fusb307#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB-C TCPC 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_FUSB307`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_FUSB307)、[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)。

<a id="CONFIG_USBC_TCPC_INIT_PRIORITY"></a>

## 181.11 `CONFIG_USBC_TCPC_INIT_PRIORITY`

**提示（Prompt）**：USB-C TCPC 驱动初始化优先级

**说明（Help）**

USB-C 设备驱动的初始化优先级。除非清楚其影响，否则不要随意修改。此处优先级数值必须小于 USB-C 协议栈的初始化优先级，使驱动能够在 USB-C 子系统之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)。

<a id="CONFIG_USBC_TCPC_NUMAKER"></a>

## 181.12 `CONFIG_USBC_TCPC_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker USB-C TCPC 设备控制器驱动

**说明（Help）**

为带 UTCPD 的 Nuvoton NuMaker 芯片启用 USB-C Type-C 端口控制器（TCPC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_TCPC_ENABLED && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_NUMAKER_ADC
CONFIG_HAS_NUMAKER_TMR
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)、[`CONFIG_HAS_NUMAKER_ADC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_ADC)、[`CONFIG_HAS_NUMAKER_TMR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NUMAKER_TMR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USBC_TCPC_PS8XXX"></a>

## 181.13 `CONFIG_USBC_TCPC_PS8XXX`

**提示（Prompt）**：USB-C TCPC 设备控制器驱动

**说明（Help）**

为 Parade PS8xxx 芯片系列启用 USB-C Type-C 端口控制器（TCPC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PARADE_PS8XXX_ENABLED && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USBC_TCPC_TCPCI
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_ps8xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_ps8xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)、[`CONFIG_USBC_TCPC_TCPCI`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_TCPCI)。

<a id="CONFIG_USBC_TCPC_PS8XXX_INIT_DELAY"></a>

## 181.14 `CONFIG_USBC_TCPC_PS8XXX_INIT_DELAY`

**提示（Prompt）**：PS8xxx 初始化延迟

**说明（Help）**

TCPC 每次初始化尝试之间的延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_PS8XXX && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
25
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_ps8xxx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_ps8xxx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB-C TCPC 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_PS8XXX`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_PS8XXX)、[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)。

<a id="CONFIG_USBC_TCPC_PS8XXX_INIT_RETRIES"></a>

## 181.15 `CONFIG_USBC_TCPC_PS8XXX_INIT_RETRIES`

**提示（Prompt）**：PS8xxx 初始化重试次数

**说明（Help）**

将执行的初始化尝试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_PS8XXX && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_ps8xxx:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_ps8xxx#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB-C TCPC 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_PS8XXX`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_PS8XXX)、[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)。

<a id="CONFIG_USBC_TCPC_RT1715"></a>

## 181.16 `CONFIG_USBC_TCPC_RT1715`

**提示（Prompt）**：USB-C TCPC 设备控制器驱动

**说明（Help）**

为 Richtek RT1715 启用 USB-C Type-C 端口控制器（TCPC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RICHTEK_RT1715_ENABLED && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USBC_TCPC_TCPCI
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_rt1715:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_rt1715#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)、[`CONFIG_USBC_TCPC_TCPCI`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_TCPCI)。

<a id="CONFIG_USBC_TCPC_RT1715_INIT_DELAY"></a>

## 181.17 `CONFIG_USBC_TCPC_RT1715_INIT_DELAY`

**提示（Prompt）**：RT1715 初始化延迟

**说明（Help）**

TCPC 每次初始化尝试之间的延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_RT1715 && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_rt1715:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_rt1715#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB-C TCPC 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_RT1715`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_RT1715)、[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)。

<a id="CONFIG_USBC_TCPC_RT1715_INIT_RETRIES"></a>

## 181.18 `CONFIG_USBC_TCPC_RT1715_INIT_RETRIES`

**提示（Prompt）**：RT1715 初始化重试次数

**说明（Help）**

将执行的初始化尝试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_RT1715 && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_rt1715:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_rt1715#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB-C TCPC 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_RT1715`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_RT1715)、[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)。

<a id="CONFIG_USBC_TCPC_SHELL"></a>

## 181.19 `CONFIG_USBC_TCPC_SHELL`

**提示（Prompt）**：TCPC 子系统的命令行命令（Shell Commands）

**说明（Help）**

启用有助于 USB-C 诊断的 TCPC 命令行命令，例如打印 VBUS、芯片信息和转储寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_DRIVER
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)。

<a id="CONFIG_USBC_TCPC_STM32"></a>

## 181.20 `CONFIG_USBC_TCPC_STM32`

**提示（Prompt）**：USB-C TCPC 设备控制器驱动

**说明（Help）**

在 STM32 G0、G4、L5 和 U5 系列处理器上启用 USB-C Type-C 端口控制器（TCPC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_UCPD_ENABLED && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_stm32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_stm32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USBC_TCPC_TCPCI"></a>

## 181.21 `CONFIG_USBC_TCPC_TCPCI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Type-C 端口控制器接口（Type-C Port Controller Interface，TCPCI）支持。符合 TCPCI 的驱动应选择此符号，以使用通用 TCPCI 寄存器操作函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_DRIVER
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**被选择（Selected by）**

```text
CONFIG_USBC_TCPC_PS8XXX
CONFIG_USBC_TCPC_RT1715
CONFIG_USBC_TCPC_FUSB307
CONFIG_USBC_VBUS_TCPCI
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_tcpci:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_tcpci#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_USBC_TCPC_PS8XXX`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_PS8XXX)、[`CONFIG_USBC_TCPC_RT1715`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_RT1715)、[`CONFIG_USBC_TCPC_FUSB307`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_FUSB307)、[`CONFIG_USBC_VBUS_TCPCI`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_VBUS_TCPCI)。

<a id="CONFIG_USBC_TCPC_TCPCI_I2C_RETRIES"></a>

## 181.22 `CONFIG_USBC_TCPC_TCPCI_I2C_RETRIES`

**提示（Prompt）**：I2C 通信重试次数

**说明（Help）**

每个请求执行的 I2C 事务尝试次数。部分 Type-C 端口控制器（TCPC）在未连接充电器时进入深度睡眠模式（Deep Sleep Mode），不会立即响应 I2C 地址。如果重试后设备仍不响应，表示设备无响应或未连接。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_TCPC_TCPCI && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/usb_c/tcpc/Kconfig.tcpc_tcpci:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/tcpc/Kconfig.tcpc_tcpci#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_TCPCI`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_TCPCI)、[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)。

<a id="CONFIG_USBC_VBUS_ADC"></a>

## 181.23 `CONFIG_USBC_VBUS_ADC`

**提示（Prompt）**：USB-C VBUS 模数转换器（ADC）

**说明（Help）**

通过分压器（Voltage Divider），使用模数转换器（ADC）测量 VBUS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_USB_C_VBUS_ADC_ENABLED && CONFIG_USBC_VBUS_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/usb_c/vbus/Kconfig.usbc_vbus_adc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/vbus/Kconfig.usbc_vbus_adc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C VBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_VBUS_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_VBUS_DRIVER)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_USBC_VBUS_DRIVER"></a>

## 181.24 `CONFIG_USBC_VBUS_DRIVER`

**提示（Prompt）**：USB-C VBUS 驱动

**说明（Help）**

启用 USB-C 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_USBC_STACK
```

**定义位置（Location）**：[`drivers/usb_c/vbus/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/vbus/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_STACK)。

<a id="CONFIG_USBC_VBUS_INIT_PRIORITY"></a>

## 181.25 `CONFIG_USBC_VBUS_INIT_PRIORITY`

**提示（Prompt）**：USB-C VBUS 驱动初始化优先级

**说明（Help）**

USB-C VBUS 测量驱动在 `POST_KERNEL` 阶段的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_VBUS_DRIVER
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/usb_c/vbus/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/vbus/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C VBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_VBUS_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_VBUS_DRIVER)。

<a id="CONFIG_USBC_VBUS_NUMAKER"></a>

## 181.26 `CONFIG_USBC_VBUS_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker USB-C VBUS

**说明（Help）**

为带 UTCPD 的 Nuvoton NuMaker 芯片启用 USB-C VBUS 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_VBUS_ENABLED && CONFIG_USBC_TCPC_NUMAKER && CONFIG_USBC_VBUS_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb_c/vbus/Kconfig.numaker:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/vbus/Kconfig.numaker#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C VBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_TCPC_NUMAKER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_NUMAKER)、[`CONFIG_USBC_VBUS_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_VBUS_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_USBC_VBUS_TCPCI"></a>

## 181.27 `CONFIG_USBC_VBUS_TCPCI`

**提示（Prompt）**：USB-C VBUS TCPCI

**说明（Help）**

使用符合 Type-C 端口控制器接口（TCPCI）的 TCPC 芯片测量 VBUS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_USB_C_VBUS_TCPCI_ENABLED && CONFIG_USBC_VBUS_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USBC_TCPC_TCPCI
```

**定义位置（Location）**：[`drivers/usb_c/vbus/Kconfig.usbc_vbus_tcpci:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb_c/vbus/Kconfig.usbc_vbus_tcpci#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C VBUS 驱动

**配置项引用（Symbol References）**：[`CONFIG_USBC_VBUS_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_VBUS_DRIVER)、[`CONFIG_USBC_TCPC_TCPCI`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_TCPCI)。

<!-- kconfig-navigation -->

[上一章](P180_drivers_usb_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P182_drivers_video_配置项参考.md)
