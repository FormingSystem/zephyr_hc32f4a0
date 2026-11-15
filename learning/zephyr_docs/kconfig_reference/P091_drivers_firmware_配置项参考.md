---
id: learning.zephyr-docs.kconfig-reference.page-91
title: "`drivers/firmware`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第91章\_`drivers/firmware`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/firmware` 的 27 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARM_SCMI"></a>

## 91.1 `CONFIG_ARM_SCMI`

**提示（Prompt）**：ARM 系统配置与管理接口（SCMI）支持

**说明（Help）**

启用 ARM 系统配置与管理接口（System Configuration and Management Interface，SCMI）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM || CONFIG_ARM64
```

**定义位置（Location）**：[`drivers/firmware/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)。

<a id="CONFIG_ARM_SCMI_BASE_HELPERS"></a>

## 91.2 `CONFIG_ARM_SCMI_BASE_HELPERS`

**提示（Prompt）**：SCMI 基础协议辅助函数（Base Protocol Helper Functions）

**说明（Help）**

启用 SCMI 基础协议（Base Protocol）辅助函数支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_CHAN_SEM_TIMEOUT_USEC"></a>

## 91.3 `CONFIG_ARM_SCMI_CHAN_SEM_TIMEOUT_USEC`

**提示（Prompt）**：ARM SCMI 通道信号量超时（Channel Semaphore Timeout）

**说明（Help）**

等待 SCMI 平台回复的最大微秒数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_CLK_HELPERS"></a>

## 91.4 `CONFIG_ARM_SCMI_CLK_HELPERS`

**提示（Prompt）**：SCMI 时钟协议辅助函数（Clock Protocol Helper Functions）

**说明（Help）**

启用 SCMI 时钟协议（Clock Protocol）辅助函数支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_SCMI_CLOCK_ENABLED && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_MAILBOX_TRANSPORT"></a>

## 91.5 `CONFIG_ARM_SCMI_MAILBOX_TRANSPORT`

**提示（Prompt）**：基于共享内存与门铃的 SCMI 传输（Shared Memory and Doorbells）

**说明（Help）**

启用基于共享内存（Shared Memory）与门铃（Doorbell）的 SCMI 传输支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_SCMI_ENABLED && CONFIG_ARM_SCMI_SHMEM && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI_SHMEM`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_SHMEM)、[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)、[`CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS)。

<a id="CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS"></a>

## 91.6 `CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS`

**提示（Prompt）**：允许 NXP 专用 SCMI 功能（NXP-Specific Features）

**说明（Help）**

启用后，可使用 NXP 专用的额外 SCMI 功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/firmware/scmi/nxp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/nxp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_ARM_SCMI_PINCTRL_HELPERS"></a>

## 91.7 `CONFIG_ARM_SCMI_PINCTRL_HELPERS`

**提示（Prompt）**：SCMI 引脚控制协议辅助函数（Pinctrl Protocol Helper Functions）

**说明（Help）**

启用 SCMI 引脚控制协议（Pinctrl Protocol）辅助函数支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_SCMI_PINCTRL_ENABLED && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ARM_SCMI_POLLING_ONLY"></a>

## 91.8 `CONFIG_ARM_SCMI_POLLING_ONLY`

**提示（Prompt）**：ARM SCMI 仅使用轮询的通信流程（Polling-Only Communication Flow）

**说明（Help）**

强制使用基于轮询（Polling）的通信流程。如果 SCMI 平台不支持中断驱动（Interrupt-Driven）的通信流程，可能需要此项。轮询不是首选模式，因此仅在这种情况下才应启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_POWER_DOMAIN_HELPERS"></a>

## 91.9 `CONFIG_ARM_SCMI_POWER_DOMAIN_HELPERS`

**提示（Prompt）**：SCMI 电源域协议辅助函数（Power Domain Protocol Helper Functions）

**说明（Help）**

启用 SCMI 电源域协议（Power Domain Protocol）辅助函数支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_SCMI_POWER_ENABLED && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_REBOOT"></a>

## 91.10 `CONFIG_ARM_SCMI_REBOOT`

**提示（Prompt）**：SCMI 系统重启支持（System Reboot Support）

**说明（Help）**

启用通过 SCMI 系统电源协议（System Power Protocol）执行系统重启（System Reboot）的功能，为具有 SCMI 的平台提供 `sys_arch_reboot()` 实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI_SYSTEM && CONFIG_REBOOT && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI_SYSTEM`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_SYSTEM)、[`CONFIG_REBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REBOOT)、[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_RESET_HELPERS"></a>

## 91.11 `CONFIG_ARM_SCMI_RESET_HELPERS`

**提示（Prompt）**：SCMI 复位协议辅助函数（Reset Protocol Helper Functions）

**说明（Help）**

启用 SCMI 复位协议（Reset Protocol）辅助函数支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_SCMI_RESET_ENABLED && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_SHELL"></a>

## 91.12 `CONFIG_ARM_SCMI_SHELL`

**提示（Prompt）**：ARM SCMI 命令行命令（Shell Commands）

**说明（Help）**

启用 ARM SCMI 命令行命令（Shell Commands）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI
```

**主动选择（Selects）**

```text
CONFIG_SHELL
```

**定义位置（Location）**：[`drivers/firmware/scmi/shell/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/shell/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_ARM_SCMI_SHMEM"></a>

## 91.13 `CONFIG_ARM_SCMI_SHMEM`

**提示（Prompt）**：SCMI 共享内存驱动（Shared Memory，SHMEM）

**说明（Help）**

启用 SCMI 共享内存（Shared Memory，SHMEM）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_SCMI_SHMEM_ENABLED && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_SHMEM_INIT_PRIORITY"></a>

## 91.14 `CONFIG_ARM_SCMI_SHMEM_INIT_PRIORITY`

**提示（Prompt）**：SCMI 共享内存（SHMEM）初始化优先级（Initialization Priority）

**说明（Help）**

SCMI 共享内存（SHMEM）驱动设备的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_SMC_TRANSPORT"></a>

## 91.15 `CONFIG_ARM_SCMI_SMC_TRANSPORT`

**提示（Prompt）**：基于共享内存与 SMC 的 SCMI 传输（Transport）

**说明（Help）**

启用以共享内存（Shared Memory）传递数据、以 ARM 安全监控调用（SMC）充当门铃（Doorbell）的 SCMI 传输支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_SCMI_SMC_ENABLED && CONFIG_ARM_SCMI_SHMEM && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI_SHMEM`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_SHMEM)、[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)、[`CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS)。

<a id="CONFIG_ARM_SCMI_SYSTEM"></a>

## 91.16 `CONFIG_ARM_SCMI_SYSTEM`

**提示（Prompt）**：SCMI 系统电源协议（System Power Protocol）

**说明（Help）**

启用 SCMI 系统协议（System Protocol）函数支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_SCMI_SYSTEM_ENABLED && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS"></a>

## 91.17 `CONFIG_ARM_SCMI_TRANSPORT_HAS_STATIC_CHANNELS`

**提示（Prompt）**：传输层具有静态通道（Static Channels）

**说明（Help）**

如果 SCMI 传输层（Transport Layer）使用静态通道（Static Channel），则启用此项。这意味着各协议的通道在编译时（Compile Time）分配。对于可以使用默认通道分配方案的传输层驱动，建议启用此项：如果存在协议专用通道，则使用它们；否则使用基础协议（Base Protocol）的通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI
```

**被选择（Selected by）**

```text
CONFIG_ARM_SCMI_MAILBOX_TRANSPORT
CONFIG_ARM_SCMI_SMC_TRANSPORT
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)、[`CONFIG_ARM_SCMI_MAILBOX_TRANSPORT`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_MAILBOX_TRANSPORT)、[`CONFIG_ARM_SCMI_SMC_TRANSPORT`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_SMC_TRANSPORT)。

<a id="CONFIG_ARM_SCMI_TRANSPORT_INIT_PRIORITY"></a>

## 91.18 `CONFIG_ARM_SCMI_TRANSPORT_INIT_PRIORITY`

**提示（Prompt）**：SCMI 传输层初始化优先级（Transport Layer Initialization Priority）

**说明（Help）**

SCMI 传输驱动（Transport Driver）设备的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/firmware/scmi/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_NXP_SCMI_CPU_DOMAIN_HELPERS"></a>

## 91.19 `CONFIG_NXP_SCMI_CPU_DOMAIN_HELPERS`

**提示（Prompt）**：SCMI CPU 域协议辅助函数（CPU Domain Protocol Helper Functions）

**说明（Help）**

启用 SCMI CPU 域协议（CPU Domain Protocol）辅助函数支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SCMI_CPU_ENABLED && CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS && CONFIG_ARM_SCMI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/firmware/scmi/nxp/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi/nxp/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers） → 允许 NXP 专用 SCMI 功能（NXP-Specific Features）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS)、[`CONFIG_ARM_SCMI`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI)。

<a id="CONFIG_QEMU_FWCFG"></a>

## 91.20 `CONFIG_QEMU_FWCFG`

**提示（Prompt）**：QEMU 固件配置（fwcfg）支持

**说明（Help）**

启用 QEMU 固件配置设备（Firmware Configuration Device）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_QEMU_FW_CFG_MMIO_ENABLED || DT_HAS_QEMU_FW_CFG_IOPORT_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_QEMU_RAMFB_DISPLAY
```

**定义位置（Location）**：[`drivers/firmware/qemu_fwcfg/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/qemu_fwcfg/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_RAMFB_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_QEMU_RAMFB_DISPLAY)。

<a id="CONFIG_QEMU_FWCFG_DMA_BOUNCE_SIZE"></a>

## 91.21 `CONFIG_QEMU_FWCFG_DMA_BOUNCE_SIZE`

**提示（Prompt）**：QEMU fwcfg DMA 中转缓冲区大小（Bounce Buffer Size）

**说明（Help）**

QEMU fwcfg 驱动为每个设备使用的内部 DMA 中转缓冲区（Bounce Buffer）大小，以字节为单位。较大的值可减少大数据传输所需的 DMA 事务（Transaction）数量；较小的值可减少 RAM 用量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_FWCFG
```

**默认值（Defaults）**

```text
4096
```

**取值范围（Ranges）**

```text
[16, 65536]
```

**定义位置（Location）**：[`drivers/firmware/qemu_fwcfg/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/qemu_fwcfg/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers） → QEMU 固件配置（fwcfg）支持

**配置项引用（Symbol References）**：[`CONFIG_QEMU_FWCFG`](P091_drivers_firmware_配置项参考.md#CONFIG_QEMU_FWCFG)。

<a id="CONFIG_QEMU_FWCFG_IOPORT"></a>

## 91.22 `CONFIG_QEMU_FWCFG_IOPORT`

**提示（Prompt）**：QEMU fwcfg I/O 端口传输（I/O Port Transport）

**说明（Help）**

启用 QEMU fwcfg 的 I/O 端口传输（I/O Port Transport）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86 && DT_HAS_QEMU_FW_CFG_IOPORT_ENABLED && CONFIG_QEMU_FWCFG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/firmware/qemu_fwcfg/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/qemu_fwcfg/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers） → QEMU 固件配置（fwcfg）支持

**配置项引用（Symbol References）**：[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_QEMU_FWCFG`](P091_drivers_firmware_配置项参考.md#CONFIG_QEMU_FWCFG)。

<a id="CONFIG_QEMU_FWCFG_MMIO"></a>

## 91.23 `CONFIG_QEMU_FWCFG_MMIO`

**提示（Prompt）**：QEMU fwcfg 内存映射 I/O 传输（MMIO Transport）

**说明（Help）**

启用 QEMU fwcfg 的内存映射 I/O（Memory-Mapped I/O，MMIO）传输支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_QEMU_FW_CFG_MMIO_ENABLED && CONFIG_QEMU_FWCFG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/firmware/qemu_fwcfg/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/qemu_fwcfg/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers） → QEMU 固件配置（fwcfg）支持

**配置项引用（Symbol References）**：[`CONFIG_QEMU_FWCFG`](P091_drivers_firmware_配置项参考.md#CONFIG_QEMU_FWCFG)。

<a id="CONFIG_RASPBERRYPI_FIRMWARE"></a>

## 91.24 `CONFIG_RASPBERRYPI_FIRMWARE`

**提示（Prompt）**：树莓派（Raspberry Pi）VideoCore 固件（Firmware）

**说明（Help）**

树莓派（Raspberry Pi）VideoCore 固件通过 VideoCore 邮箱（Mailbox）提供前端接口（Frontend Interface）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_BCM283X_FIRMWARE_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MBOX
```

**被选择（Selected by）**

```text
CONFIG_RASPBERRYPI_BCM2711_FRAMEBUFFER
CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X
CONFIG_RASPBERRYPI_BCM283X_VC_THERMAL
```

**定义位置（Location）**：[`drivers/firmware/rpi_fw/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/rpi_fw/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBOX)、[`CONFIG_RASPBERRYPI_BCM2711_FRAMEBUFFER`](P077_drivers_display_配置项参考_1.md#CONFIG_RASPBERRYPI_BCM2711_FRAMEBUFFER)、[`CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWER_DOMAIN_RASPBERRYPI_BCM283X)、[`CONFIG_RASPBERRYPI_BCM283X_VC_THERMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RASPBERRYPI_BCM283X_VC_THERMAL)。

<a id="CONFIG_RASPBERRYPI_FIRMWARE_INIT_PRIORITY"></a>

## 91.25 `CONFIG_RASPBERRYPI_FIRMWARE_INIT_PRIORITY`

**提示（Prompt）**：树莓派（Raspberry Pi）VideoCore 固件初始化优先级（Init Priority）

**说明（Help）**

数值必须大于 `CONFIG_MBOX_INIT_PRIORITY`，也就是更晚初始化，以确保本驱动初始化之前邮箱设备（Mailbox Device）已经就绪。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RASPBERRYPI_FIRMWARE
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/firmware/rpi_fw/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/rpi_fw/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers） → 树莓派（Raspberry Pi）VideoCore 固件（Firmware）

**配置项引用（Symbol References）**：[`CONFIG_RASPBERRYPI_FIRMWARE`](P091_drivers_firmware_配置项参考.md#CONFIG_RASPBERRYPI_FIRMWARE)。

<a id="CONFIG_TISCI"></a>

## 91.26 `CONFIG_TISCI`

**提示（Prompt）**：TI 系统控制器接口（TISCI）固件驱动（Firmware Driver）

**说明（Help）**

TISCI 固件驱动通过 `secureproxy` 邮箱（Mailbox），为 TI 系统控制器接口固件（TI System Controller Interface Firmware）提供前端接口（Frontend Interface）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_K2G_SCI_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MBOX
```

**定义位置（Location）**：[`drivers/firmware/tisci/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/tisci/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBOX)。

<a id="CONFIG_TISCI_INIT_PRIORITY"></a>

## 91.27 `CONFIG_TISCI_INIT_PRIORITY`

**提示（Prompt）**：TISCI 初始化优先级（Init Priority）

**说明（Help）**

TISCI 驱动的初始化优先级（Init Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TISCI
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/firmware/tisci/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/tisci/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 固件驱动（Firmware Drivers） → TI 系统控制器接口（TISCI）固件驱动（Firmware Driver）

**配置项引用（Symbol References）**：[`CONFIG_TISCI`](P091_drivers_firmware_配置项参考.md#CONFIG_TISCI)、[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<!-- kconfig-navigation -->

[上一章](P090_drivers_ethernet_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P092_drivers_flash_配置项参考_1.md)
