---
id: learning.zephyr-docs.kconfig-reference.page-434
title: "`subsys/usb`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第434章\_`subsys/usb`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `subsys/usb` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BUILD_OUTPUT_VIF"></a>

## 434.1 `CONFIG_BUILD_OUTPUT_VIF`

**提示（Prompt）**：以 XML 格式生成 USB-C 供应商信息文件（VIF）策略

**说明（Help）**

在项目构建期间，生成包含供应商信息文件（Vendor Information File，VIF）策略的 XML 文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_USB_C_CONNECTOR_ENABLED && CONFIG_USBC_STACK
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)。

<a id="CONFIG_CDC_ACM_BULK_EP_MPS"></a>

## 434.2 `CONFIG_CDC_ACM_BULK_EP_MPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通信设备类抽象控制模型（CDC ACM）批量端点（Bulk endpoint）大小

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_CDC_ACM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
512 if CONFIG_USB_DC_HAS_HS_SUPPORT
64
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.cdc:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.cdc#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CDC_ACM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DC_HAS_HS_SUPPORT`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_HAS_HS_SUPPORT)。

<a id="CONFIG_CDC_ACM_DTE_RATE_CALLBACK_SUPPORT"></a>

## 434.3 `CONFIG_CDC_ACM_DTE_RATE_CALLBACK_SUPPORT`

**提示（Prompt）**：USB 主机修改虚拟波特率（Virtual baud rate）时支持回调

**说明（Help）**

启用后，远端主机修改虚拟波特率（Virtual baud rate）时调用回调（Callback）。Arduino 风格的编程工具使用它将设备复位到引导加载程序（Bootloader）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_CDC_ACM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
CONFIG_BOOTLOADER_BOSSA
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.cdc:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.cdc#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CDC_ACM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_BOOTLOADER_BOSSA`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BOOTLOADER_BOSSA)。

<a id="CONFIG_CDC_ACM_IAD"></a>

## 434.4 `CONFIG_CDC_ACM_IAD`

**提示（Prompt）**：强制使用接口关联描述符（Interface Association Descriptor，IAD）

**说明（Help）**

非复合的 CDC ACM 设备通常不需要接口关联描述符（IAD），但 Windows 7 缺少它时无法正确枚举（Enumeration）。需要让 CDC ACM 在 Windows 7 上工作时，应启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_CDC_ACM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.cdc:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.cdc#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CDC_ACM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_CDC_ACM_INTERRUPT_EP_MPS"></a>

## 434.5 `CONFIG_CDC_ACM_INTERRUPT_EP_MPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CDC ACM 类中断输入端点（Interrupt IN endpoint）大小

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_CDC_ACM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.cdc:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.cdc#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CDC_ACM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_CDC_ACM_SERIAL_ENABLE_AT_BOOT"></a>

## 434.6 `CONFIG_CDC_ACM_SERIAL_ENABLE_AT_BOOT`

**提示（Prompt）**：启动时启用 USB 设备（USB device）

**说明（Help）**

禁用时，应用负责启用和禁用 USB 设备（USB device）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/app/Kconfig.cdc_acm_serial:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/app/Kconfig.cdc_acm_serial#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 启动时初始化 USB 设备及 CDC ACM UART

**配置项引用（Symbol References）**：[`CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`](P434_subsys_usb_配置项参考_1.md#CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT"></a>

## 434.7 `CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`

**提示（Prompt）**：启动时初始化 USB 设备及 CDC ACM UART

**说明（Help）**

此功能用于配合 `cdc-acm-snippet`，或在完全不需要、未配置且未启用其他 USB 功能的应用中，作为默认串行后端（Serial backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_CDC_ACM_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/app/Kconfig.cdc_acm_serial:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/app/Kconfig.cdc_acm_serial#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_CDC_ACM_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_CDC_ACM_SERIAL_MANUFACTURER_STRING"></a>

## 434.8 `CONFIG_CDC_ACM_SERIAL_MANUFACTURER_STRING`

**提示（Prompt）**：USB 设备制造商字符串描述符（Manufacturer string descriptor）

**说明（Help）**

USB 设备制造商字符串描述符（Manufacturer string descriptor）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
"Zephyr Project"
```

**定义位置（Location）**：[`subsys/usb/device_next/app/Kconfig.cdc_acm_serial:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/app/Kconfig.cdc_acm_serial#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 启动时初始化 USB 设备及 CDC ACM UART

**配置项引用（Symbol References）**：[`CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`](P434_subsys_usb_配置项参考_1.md#CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_CDC_ACM_SERIAL_MAX_POWER"></a>

## 434.9 `CONFIG_CDC_ACM_SERIAL_MAX_POWER`

**提示（Prompt）**：USB 设备的 `bMaxPower` 值

**说明（Help）**

配置描述符中的 `bMaxPower` 值，单位为 2 mA。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
125
```

**取值范围（Ranges）**

```text
[0, 250]
```

**定义位置（Location）**：[`subsys/usb/device_next/app/Kconfig.cdc_acm_serial:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/app/Kconfig.cdc_acm_serial#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 启动时初始化 USB 设备及 CDC ACM UART

**配置项引用（Symbol References）**：[`CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`](P434_subsys_usb_配置项参考_1.md#CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_CDC_ACM_SERIAL_PID"></a>

## 434.10 `CONFIG_CDC_ACM_SERIAL_PID`

**提示（Prompt）**：USB 设备产品 ID（Product ID，PID）

**说明（Help）**

在 Zephyr 项目之外的示例和应用中，必须使用自己的产品 ID（PID）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
0x0004
```

**定义位置（Location）**：[`subsys/usb/device_next/app/Kconfig.cdc_acm_serial:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/app/Kconfig.cdc_acm_serial#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 启动时初始化 USB 设备及 CDC ACM UART

**配置项引用（Symbol References）**：[`CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`](P434_subsys_usb_配置项参考_1.md#CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_CDC_ACM_SERIAL_PRODUCT_STRING"></a>

## 434.11 `CONFIG_CDC_ACM_SERIAL_PRODUCT_STRING`

**提示（Prompt）**：USB 设备产品字符串描述符（Product string descriptor）

**说明（Help）**

USB 设备产品字符串描述符（Product string descriptor）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
"CDC ACM serial backend"
```

**定义位置（Location）**：[`subsys/usb/device_next/app/Kconfig.cdc_acm_serial:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/app/Kconfig.cdc_acm_serial#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 启动时初始化 USB 设备及 CDC ACM UART

**配置项引用（Symbol References）**：[`CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`](P434_subsys_usb_配置项参考_1.md#CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_CDC_ACM_SERIAL_SELF_POWERED"></a>

## 434.12 `CONFIG_CDC_ACM_SERIAL_SELF_POWERED`

**提示（Prompt）**：USB 设备自供电属性（Self-powered attribute）

**说明（Help）**

设置配置描述符中的自供电属性（Self-powered attribute）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT && CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/app/Kconfig.cdc_acm_serial:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/app/Kconfig.cdc_acm_serial#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 启动时初始化 USB 设备及 CDC ACM UART

**配置项引用（Symbol References）**：[`CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`](P434_subsys_usb_配置项参考_1.md#CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_CDC_ACM_SERIAL_VID"></a>

## 434.13 `CONFIG_CDC_ACM_SERIAL_VID`

**提示（Prompt）**：USB 设备供应商 ID（Vendor ID，VID）

**说明（Help）**

在 Zephyr 项目之外的示例和应用中，必须使用自己的供应商 ID（VID）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
0x2fe3
```

**定义位置（Location）**：[`subsys/usb/device_next/app/Kconfig.cdc_acm_serial:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/app/Kconfig.cdc_acm_serial#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 启动时初始化 USB 设备及 CDC ACM UART

**配置项引用（Symbol References）**：[`CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`](P434_subsys_usb_配置项参考_1.md#CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_CDC_ACM_TX_DELAY_MS"></a>

## 434.14 `CONFIG_CDC_ACM_TX_DELAY_MS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

向主机发送实际有效载荷（Payload）前等待的毫秒数，用于避免 Linux 上的终端回显（tty ECHO）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_CDC_ACM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.cdc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.cdc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CDC_ACM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_CDC_ECM_BULK_EP_MPS"></a>

## 434.15 `CONFIG_CDC_ECM_BULK_EP_MPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通信设备类以太网控制模型（CDC ECM）批量端点大小

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_NETWORK_ECM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
512 if CONFIG_USB_DC_HAS_HS_SUPPORT
64
```

**定义位置（Location）**：[`subsys/usb/device/class/netusb/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/netusb/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_ECM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_NETWORK_ECM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DC_HAS_HS_SUPPORT`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_HAS_HS_SUPPORT)。

<a id="CONFIG_CDC_ECM_INTERRUPT_EP_MPS"></a>

## 434.16 `CONFIG_CDC_ECM_INTERRUPT_EP_MPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CDC ECM 类中断端点（Interrupt endpoint）大小

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_NETWORK_ECM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/usb/device/class/netusb/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/netusb/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_ECM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_NETWORK_ECM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_ENABLE_HID_INT_OUT_EP"></a>

## 434.17 `CONFIG_ENABLE_HID_INT_OUT_EP`

**提示（Prompt）**：USB 人机接口设备（HID）的中断输出端点（Interrupt OUT Endpoint）

**说明（Help）**

启用 USB 人机接口设备（HID）的中断输出端点（Interrupt OUT Endpoint）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_HID && CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`subsys/usb/device/class/hid/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/hid/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_HID`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_HID)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_GENVIF_INPUT_VIF_XML_PATH"></a>

## 434.18 `CONFIG_GENVIF_INPUT_VIF_XML_PATH`

**提示（Prompt）**：输入供应商信息文件（VIF）的路径

**说明（Help）**

GenVIF 输入 VIF XML 文件的路径，可为绝对路径，或相对于应用源目录的相对路径（Relative path）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_OUTPUT_VIF && CONFIG_USBC_STACK
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → 以 XML 格式生成 USB-C 供应商信息文件（VIF）策略

**配置项引用（Symbol References）**：[`CONFIG_BUILD_OUTPUT_VIF`](P434_subsys_usb_配置项参考_1.md#CONFIG_BUILD_OUTPUT_VIF)、[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)。

<a id="CONFIG_HID_INTERRUPT_EP_MPS"></a>

## 434.19 `CONFIG_HID_INTERRUPT_EP_MPS`

**提示（Prompt）**：USB 人机接口设备（HID）的中断端点大小（Interrupt Endpoint size）

**说明（Help）**

USB 人机接口设备（HID）的中断端点大小（Interrupt endpoint size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_HID && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/usb/device/class/hid/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/hid/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_HID`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_HID)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_MASS_STORAGE_BULK_EP_MPS"></a>

## 434.20 `CONFIG_MASS_STORAGE_BULK_EP_MPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

大容量存储设备类（Mass Storage Class，MSC）的批量端点大小

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_MASS_STORAGE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
512 if CONFIG_USB_DC_HAS_HS_SUPPORT
64
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.msc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.msc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_MASS_STORAGE)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DC_HAS_HS_SUPPORT`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_HAS_HS_SUPPORT)。

<a id="CONFIG_MASS_STORAGE_DISK_NAME"></a>

## 434.21 `CONFIG_MASS_STORAGE_DISK_NAME`

**提示（Prompt）**：大容量存储磁盘或驱动器名称（Disk/drive name）

**说明（Help）**

大容量存储设备（Mass storage device）的磁盘或驱动器名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_MASS_STORAGE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"RAM"
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.msc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.msc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_MASS_STORAGE)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_MASS_STORAGE_INQ_PRODUCT_ID"></a>

## 434.22 `CONFIG_MASS_STORAGE_INQ_PRODUCT_ID`

**提示（Prompt）**：查询使用的产品 ID（Inquiry Product ID），必须为 16 个字符

**说明（Help）**

查询请求（Inquiry request）使用的产品 ID，必须补空格，使字符串达到 16 字节。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_MASS_STORAGE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"ZEPHYR USB DISK "
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.msc:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.msc#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_MASS_STORAGE)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_MASS_STORAGE_INQ_REVISION"></a>

## 434.23 `CONFIG_MASS_STORAGE_INQ_REVISION`

**提示（Prompt）**：查询使用的修订号（Inquiry revision），必须为 4 个字符

**说明（Help）**

查询请求（Inquiry request）使用的修订号，必须补空格，使字符串达到 4 字节。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_MASS_STORAGE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"0.01"
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.msc:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.msc#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_MASS_STORAGE)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_MASS_STORAGE_INQ_VENDOR_ID"></a>

## 434.24 `CONFIG_MASS_STORAGE_INQ_VENDOR_ID`

**提示（Prompt）**：查询使用的 T10 分配供应商 ID（Vendor ID），必须为 8 个字符

**说明（Help）**

查询请求（Inquiry request）使用的供应商 ID，必须补空格，使字符串达到 8 字节。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_MASS_STORAGE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"ZEPHYR  "
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.msc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.msc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_MASS_STORAGE)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_MASS_STORAGE_STACK_SIZE"></a>

## 434.25 `CONFIG_MASS_STORAGE_STACK_SIZE`

**提示（Prompt）**：设置大容量存储线程栈大小（Mass storage thread stack size）

**说明（Help）**

大容量存储磁盘操作线程（Disk operations thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_MASS_STORAGE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
786 if CONFIG_SD_STACK
512
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.msc:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.msc#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_MASS_STORAGE)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_SD_STACK`](P420_subsys_sd_配置项参考.md#CONFIG_SD_STACK)。

<a id="CONFIG_MCTP_USB_CLASS_INSTANCES_COUNT"></a>

## 434.26 `CONFIG_MCTP_USB_CLASS_INSTANCES_COUNT`

**提示（Prompt）**：`MCTP_USB_CLASS` 实例（Instance）数量

**说明（Help）**

此 USB 类实现的实例（Instance）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCTP_USB && CONFIG_MCTP
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/usb/common/Kconfig.template.instances_count:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/common/Kconfig.template.instances_count#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCTP_USB`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP_USB)、[`CONFIG_MCTP`](P412_subsys_pmci_配置项参考.md#CONFIG_MCTP)。

<a id="CONFIG_RNDIS_BULK_EP_MPS"></a>

## 434.27 `CONFIG_RNDIS_BULK_EP_MPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

远程网络驱动接口规范（RNDIS）批量端点大小

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_NETWORK_RNDIS && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
512 if CONFIG_USB_DC_HAS_HS_SUPPORT
64
```

**定义位置（Location）**：[`subsys/usb/device/class/netusb/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/netusb/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_RNDIS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_NETWORK_RNDIS)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DC_HAS_HS_SUPPORT`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DC_HAS_HS_SUPPORT)。

<a id="CONFIG_RNDIS_INTERRUPT_EP_MPS"></a>

## 434.28 `CONFIG_RNDIS_INTERRUPT_EP_MPS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

远程网络驱动接口规范（RNDIS）中断端点大小

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_NETWORK_RNDIS && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/usb/device/class/netusb/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/netusb/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_RNDIS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_NETWORK_RNDIS)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USBC_CSM_DRP"></a>

## 434.29 `CONFIG_USBC_CSM_DRP`

**提示（Prompt）**：双角色电源（Dual Role Power，DRP）USB-C 连接状态机

**说明（Help）**

让 USB-C 状态机作为双角色电源（Dual Role Power，DRP）运行。依据 USB Type-C 规范，未连接时，DRP 在供电端（Source，Rp）与受电端（Sink，Rd）角色间切换，从 `Unattached.SNK` 状态开始。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_CSM_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_USBC_CSM_SUPPORTS_SINK
CONFIG_USBC_CSM_SUPPORTS_SOURCE
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → USB-C 连接状态机（Connection State Machine）

**配置项引用（Symbol References）**：[`CONFIG_USBC_CSM_TYPE`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_TYPE)、[`CONFIG_USBC_CSM_SUPPORTS_SINK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_SUPPORTS_SINK)、[`CONFIG_USBC_CSM_SUPPORTS_SOURCE`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_SUPPORTS_SOURCE)。

<a id="CONFIG_USBC_CSM_SINK_ONLY"></a>

## 434.30 `CONFIG_USBC_CSM_SINK_ONLY`

**提示（Prompt）**：受电端（Sink）USB-C 连接状态机

**说明（Help）**

允许 USB-C 状态机作为受电端（Sink）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_CSM_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_USBC_CSM_SUPPORTS_SINK
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → USB-C 连接状态机（Connection State Machine）

**配置项引用（Symbol References）**：[`CONFIG_USBC_CSM_TYPE`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_TYPE)、[`CONFIG_USBC_CSM_SUPPORTS_SINK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_SUPPORTS_SINK)。

<a id="CONFIG_USBC_CSM_SOURCE_ONLY"></a>

## 434.31 `CONFIG_USBC_CSM_SOURCE_ONLY`

**提示（Prompt）**：供电端（Source）USB-C 连接状态机

**说明（Help）**

允许 USB-C 状态机作为供电端（Source）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_CSM_TYPE>
```

**主动选择（Selects）**

```text
CONFIG_USBC_CSM_SUPPORTS_SOURCE
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → USB-C 连接状态机（Connection State Machine）

**配置项引用（Symbol References）**：[`CONFIG_USBC_CSM_TYPE`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_TYPE)、[`CONFIG_USBC_CSM_SUPPORTS_SOURCE`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_SUPPORTS_SOURCE)。

<a id="CONFIG_USBC_CSM_SUPPORTS_SINK"></a>

## 434.32 `CONFIG_USBC_CSM_SUPPORTS_SINK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 USB-C 状态机支持受电端（Sink）操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_STACK
```

**被选择（Selected by）**

```text
CONFIG_USBC_CSM_SINK_ONLY
CONFIG_USBC_CSM_DRP
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)、[`CONFIG_USBC_CSM_SINK_ONLY`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_SINK_ONLY)、[`CONFIG_USBC_CSM_DRP`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_DRP)。

<a id="CONFIG_USBC_CSM_SUPPORTS_SOURCE"></a>

## 434.33 `CONFIG_USBC_CSM_SUPPORTS_SOURCE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 USB-C 状态机支持供电端（Source）操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_STACK
```

**被选择（Selected by）**

```text
CONFIG_USBC_CSM_SOURCE_ONLY
CONFIG_USBC_CSM_DRP
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)、[`CONFIG_USBC_CSM_SOURCE_ONLY`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_SOURCE_ONLY)、[`CONFIG_USBC_CSM_DRP`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_DRP)。

<a id="CONFIG_USBC_CSM_TYPE"></a>

## 434.34 `CONFIG_USBC_CSM_TYPE`

**提示（Prompt）**：USB-C 连接状态机（Connection State Machine）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_STACK
```

**默认值（Defaults）**

```text
CONFIG_USBC_CSM_SINK_ONLY
```

**可选项（Choices）**

```text
CONFIG_USBC_CSM_SINK_ONLY
CONFIG_USBC_CSM_SOURCE_ONLY
CONFIG_USBC_CSM_DRP
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)、[`CONFIG_USBC_CSM_SINK_ONLY`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_SINK_ONLY)、[`CONFIG_USBC_CSM_SOURCE_ONLY`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_SOURCE_ONLY)、[`CONFIG_USBC_CSM_DRP`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_DRP)。

<a id="CONFIG_USBC_DRP_DUTY_CYCLE"></a>

## 434.35 `CONFIG_USBC_DRP_DUTY_CYCLE`

**提示（Prompt）**：双角色电源（DRP）的供电端占空比（Source duty cycle，百分比）

**说明（Help）**

双角色电源（DRP）在一个 `tDRP` 周期内宣告供电端（Source，Rp）角色的时间百分比。USB Type-C 规范规定为 30%～70%。例如：

- 50%：供电端与受电端（Sink）时间相等，保持平衡。
- 30%：偏向受电端，70% 时间为受电端、30% 为供电端。
- 70%：偏向供电端，70% 时间为供电端、30% 为受电端。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_CSM_DRP && CONFIG_USBC_STACK
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[30, 70]
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_CSM_DRP`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_DRP)、[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)。

<a id="CONFIG_USBC_DRP_PERIOD_MS"></a>

## 434.36 `CONFIG_USBC_DRP_PERIOD_MS`

**提示（Prompt）**：双角色电源（DRP）切换周期 `tDRP`（毫秒）

**说明（Help）**

双角色电源（DRP）完成一次从供电端（Source）到受电端（Sink）再返回的角色宣告所用周期。USB Type-C 规范规定 `tDRP = 50-100ms`，表示一个完整切换周期的总时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_CSM_DRP && CONFIG_USBC_STACK
```

**默认值（Defaults）**

```text
75
```

**取值范围（Ranges）**

```text
[50, 100]
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_CSM_DRP`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_CSM_DRP)、[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)。

<a id="CONFIG_USBC_LOG_PD_MSG_NAMES"></a>

## 434.37 `CONFIG_USBC_LOG_PD_MSG_NAMES`

**提示（Prompt）**：记录 USB 电力传输（PD）消息名称

**说明（Help）**

在协议层（Protocol Layer）的 SEND 和 RECV 日志行中，除原始报头外，还记录便于阅读的 USB 电力传输（PD）消息名称，例如 `Source_Capabilities`。启用有助于调试，但消息名称表会增大代码体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_STACK
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)。

<a id="CONFIG_USBC_STACK"></a>

## 434.38 `CONFIG_USBC_STACK`

**提示（Prompt）**：USB-C 协议栈支持（Stack Support）

**说明（Help）**

启用 USB-C 协议栈（Stack）。注意，每个 USB-C 端口都有独立线程。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SMF
CONFIG_SMF_ANCESTOR_SUPPORT
CONFIG_USBC_TCPC_DRIVER
CONFIG_USBC_VBUS_DRIVER
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SMF`](P198_lib_配置项参考_2.md#CONFIG_SMF)、[`CONFIG_SMF_ANCESTOR_SUPPORT`](P198_lib_配置项参考_2.md#CONFIG_SMF_ANCESTOR_SUPPORT)、[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)、[`CONFIG_USBC_VBUS_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_VBUS_DRIVER)。

<a id="CONFIG_USBC_STACK_INIT_PRIORITY"></a>

## 434.39 `CONFIG_USBC_STACK_INIT_PRIORITY`

**提示（Prompt）**：USB-C 协议栈初始化优先级（Initialization priority）

**说明（Help）**

USB-C 连接器驱动在 POST_KERNEL 级别的初始化优先级。它必须在 USB-C 连接器引用的设备之后初始化，例如 VBUS 和 Type-C 端口控制器（TCPC）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_STACK
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)。

<a id="CONFIG_USBC_STACK_SIZE"></a>

## 434.40 `CONFIG_USBC_STACK_SIZE`

**提示（Prompt）**：USB-C 线程栈大小（Thread stack size）

**说明（Help）**

为每个实例创建的线程的栈大小（Stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_STACK
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)。

<a id="CONFIG_USBC_STATE_MACHINE_CYCLE_TIME"></a>

## 434.41 `CONFIG_USBC_STATE_MACHINE_CYCLE_TIME`

**提示（Prompt）**：USB-C 状态机循环时间（Cycle time，毫秒）

**说明（Help）**

USB-C 状态机（State machine）在循环中运行，此周期值表示开始下一轮循环前的延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_STACK
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)。

<a id="CONFIG_USBC_THREAD_PRIORITY"></a>

## 434.42 `CONFIG_USBC_THREAD_PRIORITY`

**提示（Prompt）**：USB-C 线程优先级（Thread priority）

**说明（Help）**

设置 USB-C 线程的优先级（Thread priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBC_STACK
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/usb/usb_c/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBC_STACK)。

<a id="CONFIG_USBD_AUDIO2_CLASS"></a>

## 434.43 `CONFIG_USBD_AUDIO2_CLASS`

**提示（Prompt）**：USB 音频类 2 支持（Audio 2 class）

**说明（Help）**

USB 音频 2.0 设备类（USB Audio 2 device class）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**主动选择（Selects）**

```text
CONFIG_UDC_ENABLE_SOF
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.uac2:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.uac2#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_UDC_ENABLE_SOF`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_ENABLE_SOF)。

<a id="CONFIG_USBD_BOS_SUPPORT"></a>

## 434.44 `CONFIG_USBD_BOS_SUPPORT`

**提示（Prompt）**：USB 设备二进制设备对象存储（BOS）支持

**说明（Help）**

如果应用不使用二进制设备对象存储（Binary device Object Store，BOS）描述符，可禁用 BOS 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_BT_HCI"></a>

## 434.45 `CONFIG_USBD_BT_HCI`

**提示（Prompt）**：蓝牙 HCI USB 传输层（Transport Layer）

**说明（Help）**

蓝牙 HCI USB 传输层（Transport Layer）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**主动选择（Selects）**

```text
CONFIG_BT
CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.bt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.bt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_RAW)。

<a id="CONFIG_USBD_BT_HCI_RX_THREAD_PRIORITY"></a>

## 434.46 `CONFIG_USBD_BT_HCI_RX_THREAD_PRIORITY`

**提示（Prompt）**：接收线程优先级（RX Thread Priority）

**说明（Help）**

蓝牙主机控制器接口（HCI）USB 传输层接收线程（RX thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_BT_HCI && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.bt:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.bt#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BT_HCI`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_BT_HCI)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_BT_HCI_TX_STACK_SIZE"></a>

## 434.47 `CONFIG_USBD_BT_HCI_TX_STACK_SIZE`

**提示（Prompt）**：发送线程栈大小（TX Thread Stack Size）

**说明（Help）**

蓝牙主机控制器接口（HCI）USB 传输层发送线程（TX thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_BT_HCI && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.bt:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.bt#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BT_HCI`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_BT_HCI)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_BT_HCI_TX_THREAD_PRIORITY"></a>

## 434.48 `CONFIG_USBD_BT_HCI_TX_THREAD_PRIORITY`

**提示（Prompt）**：发送线程优先级（TX Thread Priority）

**说明（Help）**

蓝牙主机控制器接口（HCI）USB 传输层发送线程（TX thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_BT_HCI && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.bt:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.bt#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BT_HCI`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_BT_HCI)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_CDC_ACM_CLASS"></a>

## 434.49 `CONFIG_USBD_CDC_ACM_CLASS`

**提示（Prompt）**：USB 通信设备类抽象控制模型实现（CDC ACM）

**说明（Help）**

USB 设备通信设备类抽象控制模型（CDC ACM）的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL && DT_HAS_ZEPHYR_CDC_ACM_UART_ENABLED && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.cdc_acm:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.cdc_acm#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_USBD_CDC_ACM_STACK_SIZE"></a>

## 434.50 `CONFIG_USBD_CDC_ACM_STACK_SIZE`

**提示（Prompt）**：USB CDC ACM 工作队列栈大小（Workqueue stack size）

**说明（Help）**

USB CDC ACM 工作队列（Workqueue）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_CDC_ACM_WORKQUEUE && CONFIG_USBD_CDC_ACM_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.cdc_acm:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.cdc_acm#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM） → CDC ACM 使用专用工作队列（Dedicated workqueue）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_WORKQUEUE`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_CDC_ACM_WORKQUEUE)、[`CONFIG_USBD_CDC_ACM_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_CDC_ACM_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_CDC_ACM_TX_DELAY_MS"></a>

## 434.51 `CONFIG_USBD_CDC_ACM_TX_DELAY_MS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

向主机发送实际有效载荷（Payload）前等待的毫秒数，用于避免 Linux 上的终端回显（tty ECHO）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_CDC_ACM_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.cdc_acm:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.cdc_acm#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_CDC_ACM_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_CDC_ACM_WORKQUEUE"></a>

## 434.52 `CONFIG_USBD_CDC_ACM_WORKQUEUE`

**提示（Prompt）**：CDC ACM 使用专用工作队列（Dedicated workqueue）

**说明（Help）**

因性能问题或其他冲突无法使用系统工作队列时，让 CDC ACM 实现使用专用工作队列（Dedicated workqueue）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_CDC_ACM_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.cdc_acm:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.cdc_acm#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_CDC_ACM_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_CDC_ECM_CLASS"></a>

## 434.53 `CONFIG_USBD_CDC_ECM_CLASS`

**提示（Prompt）**：USB 通信设备类以太网控制模型实现（CDC ECM）

**说明（Help）**

USB 通信设备类以太网控制模型（CDC Ethernet Control Model，ECM）的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && DT_HAS_ZEPHYR_CDC_ECM_ETHERNET_ENABLED && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.cdc_ecm:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.cdc_ecm#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_CDC_NCM_CLASS"></a>

## 434.54 `CONFIG_USBD_CDC_NCM_CLASS`

**提示（Prompt）**：USB 通信设备类网络控制模型实现（CDC NCM）

**说明（Help）**

USB 通信设备类网络控制模型（CDC Network Control Model，NCM）的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && DT_HAS_ZEPHYR_CDC_NCM_ETHERNET_ENABLED && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.cdc_ncm:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.cdc_ncm#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_CDC_NCM_MAX_DGRAM_PER_NTB"></a>

## 434.55 `CONFIG_USBD_CDC_NCM_MAX_DGRAM_PER_NTB`

**提示（Prompt）**：每个网络传输块（NTB）可接收的最大数据报数量

**说明（Help）**

每个网络传输块（Network Transfer Block，NTB）能够接收的数据报（Datagram）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_CDC_NCM_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.cdc_ncm:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.cdc_ncm#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类网络控制模型实现（CDC NCM）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_NCM_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_CDC_NCM_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_CDC_NCM_SUPPORT_NTB32"></a>

## 434.56 `CONFIG_USBD_CDC_NCM_SUPPORT_NTB32`

**提示（Prompt）**：支持 NTB32 格式

**说明（Help）**

启用 NTB32 格式支持，允许使用更大的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_CDC_NCM_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.cdc_ncm:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.cdc_ncm#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类网络控制模型实现（CDC NCM）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_NCM_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_CDC_NCM_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_DFU"></a>

## 434.57 `CONFIG_USBD_DFU`

**提示（Prompt）**：USB 设备固件更新类支持（DFU Class）

**说明（Help）**

USB 设备固件更新类支持（DFU Class）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.dfu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.dfu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_DFU_ENABLE_UPLOAD"></a>

## 434.58 `CONFIG_USBD_DFU_ENABLE_UPLOAD`

**提示（Prompt）**：允许将映像（Image）上传到主机

**说明（Help）**

设置设备固件升级（DFU）属性中的 `bitCanUpload` 标志，允许将映像（Image）上传到主机。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_DFU && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.dfu:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.dfu#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_DFU_FLASH"></a>

## 434.59 `CONFIG_USBD_DFU_FLASH`

**提示（Prompt）**：内置闪存后端（Built-in flash backend）

**说明（Help）**

启用内置闪存后端（Built-in flash backend），最多可服务两个映像槽位（Image slot），这是源码树内开发板的常见配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH && CONFIG_FLASH_MAP && CONFIG_STREAM_FLASH && CONFIG_IMG_MANAGER && CONFIG_IMG_ERASE_PROGRESSIVELY && CONFIG_USBD_DFU && CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.dfu:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.dfu#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_MAP`](P429_subsys_storage_配置项参考.md#CONFIG_FLASH_MAP)、[`CONFIG_STREAM_FLASH`](P429_subsys_storage_配置项参考.md#CONFIG_STREAM_FLASH)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_IMG_ERASE_PROGRESSIVELY`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_ERASE_PROGRESSIVELY)、[`CONFIG_USBD_DFU`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_DFU_FLASH_SLOT0"></a>

## 434.60 `CONFIG_USBD_DFU_FLASH_SLOT0`

**提示（Prompt）**：`slot-0` 分区的闪存后端（Flash backend）

**说明（Help）**

如果定义了 `slot-0` 分区，启用其下载或上传功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_DFU_FLASH && CONFIG_USBD_DFU && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.dfu:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.dfu#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class） → 内置闪存后端（Built-in flash backend）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU_FLASH`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU_FLASH)、[`CONFIG_USBD_DFU`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_DFU_FLASH_SLOT1"></a>

## 434.61 `CONFIG_USBD_DFU_FLASH_SLOT1`

**提示（Prompt）**：`slot-1` 分区的闪存后端（Flash backend）

**说明（Help）**

如果定义了 `slot-1` 分区，启用其下载或上传功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_DFU_FLASH && CONFIG_USBD_DFU && CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.dfu:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.dfu#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class） → 内置闪存后端（Built-in flash backend）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU_FLASH`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU_FLASH)、[`CONFIG_USBD_DFU`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_DFU_MANIFESTATION_TOLERANT"></a>

## 434.62 `CONFIG_USBD_DFU_MANIFESTATION_TOLERANT`

**提示（Prompt）**：设备支持固件生效后继续通信（Manifestation tolerant）

**说明（Help）**

设置设备固件升级（DFU）属性中的 `bitManifestationTolerant` 标志，表示设备在固件生效阶段（Manifestation phase）之后仍可通过 USB 通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_DFU && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.dfu:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.dfu#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_DFU_NUMOF_IMAGES"></a>

## 434.63 `CONFIG_USBD_DFU_NUMOF_IMAGES`

**提示（Prompt）**：可用的 DFU 映像（Image）数量

**说明（Help）**

可用的设备固件升级（DFU）映像数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_DFU && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.dfu:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.dfu#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_DFU_POLLTIMEOUT"></a>

## 434.64 `CONFIG_USBD_DFU_POLLTIMEOUT`

**提示（Prompt）**：`bwPollTimeout` 值（毫秒）

**说明（Help）**

设置 `DFU_GETSTATUS` 响应中的 `bwPollTimeout` 字段。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_DFU && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.dfu:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.dfu#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_DFU_TRANSFER_SIZE"></a>

## 434.65 `CONFIG_USBD_DFU_TRANSFER_SIZE`

**提示（Prompt）**：设备每次传输可接受的最大字节数

**说明（Help）**

设置设备固件升级（DFU）功能描述符（Functional descriptor）中的 `wTransferSize`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_DFU && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[64, 1024]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.dfu:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.dfu#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_DFU)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_HID_INIT_PRIORITY"></a>

## 434.66 `CONFIG_USBD_HID_INIT_PRIORITY`

**提示（Prompt）**：人机接口设备（HID）初始化优先级

**说明（Help）**

人机接口设备（HID）的初始化优先级（Initialization priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_HID_SUPPORT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.hid:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.hid#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_SUPPORT`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_HID_SUPPORT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_USBD_HID_IN_BUF_COUNT"></a>

## 434.67 `CONFIG_USBD_HID_IN_BUF_COUNT`

**提示（Prompt）**：输入缓冲池（IN pool）的缓冲区数量

**说明（Help）**

每个 HID 实例的输入缓冲池（IN pool）中的缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_HID_SUPPORT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.hid:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.hid#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_SUPPORT`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_HID_SUPPORT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_HID_OUT_BUF_COUNT"></a>

## 434.68 `CONFIG_USBD_HID_OUT_BUF_COUNT`

**提示（Prompt）**：输出缓冲池（OUT pool）的缓冲区数量

**说明（Help）**

每个 HID 实例的输出缓冲池（OUT pool）中的缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_HID_SUPPORT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.hid:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.hid#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_SUPPORT`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_HID_SUPPORT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_HID_SET_POLLING_PERIOD"></a>

## 434.69 `CONFIG_USBD_HID_SET_POLLING_PERIOD`

**提示（Prompt）**：允许运行时设置轮询周期（Polling period）

**说明（Help）**

允许运行时设置输入或输出报告（Input/output report）的轮询周期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_HID_SUPPORT && CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.hid:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.hid#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_SUPPORT`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_HID_SUPPORT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_HID_SUPPORT"></a>

## 434.70 `CONFIG_USBD_HID_SUPPORT`

**提示（Prompt）**：USB 人机接口设备支持（Human Interface Device）

**说明（Help）**

启用 USB 人机接口设备（Human Interface Device，HID）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_HID_DEVICE_ENABLED && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_FIDO2_TRANSPORT_USB_HID
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.hid:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.hid#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_FIDO2_TRANSPORT_USB_HID`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_USB_HID)。

<a id="CONFIG_USBD_HWINFO_DEVID_LENGTH"></a>

## 434.71 `CONFIG_USBD_HWINFO_DEVID_LENGTH`

**提示（Prompt）**：向硬件信息（HWINFO）请求的设备 ID 长度（字节）

**说明（Help）**

每个字节对应序列号字符串描述符（Serial number string descriptor）中的两个数字字符。本选项可限制从 HWINFO 请求的长度，使生成的数字位数适当。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[8, 128]
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_LOOPBACK_CLASS"></a>

## 434.72 `CONFIG_USBD_LOOPBACK_CLASS`

**提示（Prompt）**：USB 回环类（Loopback Class）

**说明（Help）**

USB 设备环回类（Loopback class），主要用于测试和开发。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.loopback:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.loopback#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_LOOPBACK_ENABLE_ISO"></a>

## 434.73 `CONFIG_USBD_LOOPBACK_ENABLE_ISO`

**提示（Prompt）**：等时传输处理（Isochronous transfer handling）

**说明（Help）**

在接口中包含等时端点描述符（Isochronous endpoint descriptor），并启用等时传输处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_ENABLE_SOF && CONFIG_USBD_LOOPBACK_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.loopback:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.loopback#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class）

**配置项引用（Symbol References）**：[`CONFIG_UDC_ENABLE_SOF`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_ENABLE_SOF)、[`CONFIG_USBD_LOOPBACK_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_LOOPBACK_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_LOOPBACK_HS_INT_IN_EP_TPL"></a>

## 434.74 `CONFIG_USBD_LOOPBACK_HS_INT_IN_EP_TPL`

**提示（Prompt）**：高速中断输入端点的 TPL（High-speed interrupt IN TPL）

**说明（Help）**

高速（High speed）配置下中断输入端点（Interrupt IN endpoint）的 TPL 值。较大的值要求调整 USB 设备控制器（UDC）缓冲池。全速（Full speed）配置下的 TPL 始终为 64。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_LOOPBACK_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[64, 3072]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.loopback:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.loopback#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_LOOPBACK_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_LOOPBACK_HS_INT_OUT_EP_TPL"></a>

## 434.75 `CONFIG_USBD_LOOPBACK_HS_INT_OUT_EP_TPL`

**提示（Prompt）**：高速中断输出端点的 TPL（High-speed interrupt OUT TPL）

**说明（Help）**

高速（High speed）配置下中断输出端点（Interrupt OUT endpoint）的 TPL 值。较大的值要求调整 USB 设备控制器（UDC）缓冲池。全速（Full speed）配置下的 TPL 始终为 64。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_LOOPBACK_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[64, 3072]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.loopback:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.loopback#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_LOOPBACK_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_LOOPBACK_HS_ISO_IN_EP_TPL"></a>

## 434.76 `CONFIG_USBD_LOOPBACK_HS_ISO_IN_EP_TPL`

**提示（Prompt）**：高速等时输入端点的 TPL（High-speed isochronous IN TPL）

**说明（Help）**

高速（High speed）配置下等时输入端点（Isochronous IN endpoint）的 TPL 值。较大的值要求调整 USB 设备控制器（UDC）缓冲池。全速（Full speed）配置下的 TPL 始终为 256。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_LOOPBACK_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[256, 3072]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.loopback:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.loopback#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class） → 等时传输处理（Isochronous transfer handling）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_LOOPBACK_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_LOOPBACK_HS_ISO_OUT_EP_TPL"></a>

## 434.77 `CONFIG_USBD_LOOPBACK_HS_ISO_OUT_EP_TPL`

**提示（Prompt）**：高速等时输出端点的 TPL（High-speed isochronous OUT TPL）

**说明（Help）**

高速（High speed）配置下等时输出端点（Isochronous OUT endpoint）的 TPL 值。较大的值要求调整 USB 设备控制器（UDC）缓冲池。全速（Full speed）配置下的 TPL 始终为 256。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_LOOPBACK_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[256, 3072]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.loopback:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.loopback#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class） → 等时传输处理（Isochronous transfer handling）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_LOOPBACK_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_LOOPBACK_INSTANCES_COUNT"></a>

## 434.78 `CONFIG_USBD_LOOPBACK_INSTANCES_COUNT`

**提示（Prompt）**：`USBD_LOOPBACK` 实例（Instance）数量

**说明（Help）**

此 USB 类实现的实例（Instance）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_LOOPBACK_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/usb/common/Kconfig.template.instances_count:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/common/Kconfig.template.instances_count#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_LOOPBACK_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MAX_SPEED_CHOICE"></a>

## 434.79 `CONFIG_USBD_MAX_SPEED_CHOICE`

**提示（Prompt）**：支持的最高连接速度（Maximum connection speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_MAX_SPEED_HIGH if CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
CONFIG_USBD_MAX_SPEED_FULL
```

**可选项（Choices）**

```text
CONFIG_USBD_MAX_SPEED_HIGH
CONFIG_USBD_MAX_SPEED_FULL
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_MAX_SPEED_HIGH`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_MAX_SPEED_HIGH)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)、[`CONFIG_USBD_MAX_SPEED_FULL`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_MAX_SPEED_FULL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_USBD_MAX_SPEED_FULL"></a>

## 434.80 `CONFIG_USBD_MAX_SPEED_FULL`

**提示（Prompt）**：全速（Full-Speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_UDC_DRIVER_HIGH_SPEED_SUPPORT_ENABLED && <choice CONFIG_USBD_MAX_SPEED_CHOICE>
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 支持的最高连接速度（Maximum connection speed）

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER_HIGH_SPEED_SUPPORT_ENABLED`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER_HIGH_SPEED_SUPPORT_ENABLED)、[`CONFIG_USBD_MAX_SPEED_CHOICE`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_MAX_SPEED_CHOICE)。

<a id="CONFIG_USBD_MAX_SPEED_HIGH"></a>

## 434.81 `CONFIG_USBD_MAX_SPEED_HIGH`

**提示（Prompt）**：高速（High-Speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT && <choice CONFIG_USBD_MAX_SPEED_CHOICE>
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 支持的最高连接速度（Maximum connection speed）

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)、[`CONFIG_USBD_MAX_SPEED_CHOICE`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_MAX_SPEED_CHOICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_USBD_MAX_UDC_MSG"></a>

## 434.82 `CONFIG_USBD_MAX_UDC_MSG`

**提示（Prompt）**：USB 设备控制器（UDC）事件的最大数量

**说明（Help）**

可排队的 USB 设备控制器（USB Device Controller，UDC）事件的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MIDI2_CLASS"></a>

## 434.83 `CONFIG_USBD_MIDI2_CLASS`

**提示（Prompt）**：USB MIDI 2.0 类支持【实验性 EXPERIMENTAL】

**说明（Help）**

启用 USB 乐器数字接口 2.0（MIDI 2.0）设备类支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.midi2:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.midi2#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MSC_CLASS"></a>

## 434.84 `CONFIG_USBD_MSC_CLASS`

**提示（Prompt）**：USB 大容量存储设备类支持（Mass Storage Device class）

**说明（Help）**

USB 大容量存储设备类（Mass Storage Class，MSC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**主动选择（Selects）**

```text
CONFIG_DISK_ACCESS
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.msc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.msc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_DISK_ACCESS`](P340_subsys_disk_配置项参考.md#CONFIG_DISK_ACCESS)。

<a id="CONFIG_USBD_MSC_DOUBLE_BUFFERING"></a>

## 434.85 `CONFIG_USBD_MSC_DOUBLE_BUFFERING`

**提示（Prompt）**：小型计算机系统接口（SCSI）双缓冲（Double buffering）

**说明（Help）**

分配两个 SCSI 缓冲区而非一个，让磁盘子系统和 USB 能够同时分别使用一个缓冲区，提高吞吐量（Throughput）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_MSC_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.msc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.msc#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_MSC_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MSC_INSTANCES_COUNT"></a>

## 434.86 `CONFIG_USBD_MSC_INSTANCES_COUNT`

**提示（Prompt）**：`USBD_MSC` 实例（Instance）数量

**说明（Help）**

此 USB 类实现的实例（Instance）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_MSC_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/usb/common/Kconfig.template.instances_count:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/common/Kconfig.template.instances_count#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_MSC_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MSC_LUNS_PER_INSTANCE"></a>

## 434.87 `CONFIG_USBD_MSC_LUNS_PER_INSTANCE`

**提示（Prompt）**：逻辑单元（LUN）的数量

**说明（Help）**

每个实例可注册的逻辑单元（Logical Unit）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_MSC_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.msc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.msc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_MSC_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MSC_SCSI_BUFFER_SIZE"></a>

## 434.88 `CONFIG_USBD_MSC_SCSI_BUFFER_SIZE`

**提示（Prompt）**：小型计算机系统接口（SCSI）缓冲区大小

**说明（Help）**

缓冲区必须至少能够容纳一个扇区（Sector）。同一实例的全部逻辑单元（LUN）共享 SCSI 缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_MSC_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.msc:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.msc#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_MSC_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MSC_STACK_SIZE"></a>

## 434.89 `CONFIG_USBD_MSC_STACK_SIZE`

**提示（Prompt）**：USB 大容量存储类（MSC）线程栈大小

**说明（Help）**

USB 大容量存储类（MSC）的线程栈大小（Thread stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_MSC_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.msc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.msc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_MSC_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MSG_DEFERRED_MODE"></a>

## 434.90 `CONFIG_USBD_MSG_DEFERRED_MODE`

**提示（Prompt）**：在系统工作队列（System workqueue）中执行消息回调

**说明（Help）**

在系统工作队列（System workqueue）中执行消息回调（Message callback）。禁用时，回调在 USB 设备协议栈上下文中执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MSG_SLAB_COUNT"></a>

## 434.91 `CONFIG_USBD_MSG_SLAB_COUNT`

**提示（Prompt）**：USB 设备通知消息（Notification message）的最大数量

**说明（Help）**

可排队的 USB 设备通知消息（Notification message）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[4, 64]
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 在系统工作队列（System workqueue）中执行消息回调

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_MSG_WORK_DELAY"></a>

## 434.92 `CONFIG_USBD_MSG_WORK_DELAY`

**提示（Prompt）**：USB 设备通知消息工作项延迟（Work delay）

**说明（Help）**

设备协议栈可能尚未准备好发布消息，因此可能需要延迟消息工作项（Message work）的执行，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 在系统工作队列（System workqueue）中执行消息回调

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_SHELL"></a>

## 434.93 `CONFIG_USBD_SHELL`

**提示（Prompt）**：USB 设备命令行（Device shell）

**说明（Help）**

启用 USB 设备命令行（Device shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_THREAD_INIT_PRIO"></a>

## 434.94 `CONFIG_USBD_THREAD_INIT_PRIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

USB 设备线程的初始化优先级（Initialization priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_THREAD_STACK_SIZE"></a>

## 434.95 `CONFIG_USBD_THREAD_STACK_SIZE`

**提示（Prompt）**：USB 设备协议栈线程栈大小（Thread stack size）

**说明（Help）**

USB 设备协议栈线程的栈大小（Stack size），单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_UAC2_FS_WINDOWS_WORKAROUND"></a>

## 434.96 `CONFIG_USBD_UAC2_FS_WINDOWS_WORKAROUND`

**提示（Prompt）**：规避 Windows 全速 USB 的 `wMaxPacketSize` 缺陷

**说明（Help）**

将全速 USB 链路上的 USB 音频类 2.0（UAC2）反馈端点（Feedback endpoint）大小设为 4 字节。USB 2.0 规范要求长度为 3，而原文所述不符合规范的 Windows UAC2 驱动要求为 4。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_AUDIO2_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.uac2:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.uac2#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 音频类 2 支持（Audio 2 class）

**配置项引用（Symbol References）**：[`CONFIG_USBD_AUDIO2_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_AUDIO2_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_VIDEO_CLASS"></a>

## 434.97 `CONFIG_USBD_VIDEO_CLASS`

**提示（Prompt）**：USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】

**说明（Help）**

USB 视频设备类（USB Video Class，UVC）的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_UVC_DEVICE_ENABLED && CONFIG_USB_DEVICE_STACK_NEXT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.uvc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.uvc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_USBD_VIDEO_MAX_FORMATS"></a>

## 434.98 `CONFIG_USBD_VIDEO_MAX_FORMATS`

**提示（Prompt）**：格式描述符（Format descriptor）的最大数量

**说明（Help）**

格式描述符（Format descriptor）表在运行时生成。本选项在构建时规划存储空间，以容纳足够数量的描述符。默认值在满足大多数设备需求和避免占用过多内存之间折中。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_VIDEO_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 254]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.uvc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.uvc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBD_VIDEO_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_VIDEO_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_VIDEO_MAX_FRMIVAL"></a>

## 434.99 `CONFIG_USBD_VIDEO_MAX_FRMIVAL`

**提示（Prompt）**：每个 USB 视频接口的最大视频输出流数（Video output streams）

**说明（Help）**

帧描述符（Frame descriptor）中列出的帧间隔（Frame Interval）的最大数量。默认值依据一般情况选取，尽量满足多数场景而不占用过多 RAM。

译注：原文标题写作“视频输出流数”，帮助正文则说明“帧间隔数量”；这里分别保留。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_VIDEO_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.uvc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.uvc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBD_VIDEO_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_VIDEO_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBD_VIDEO_NUM_BUFS"></a>

## 434.100 `CONFIG_USBD_VIDEO_NUM_BUFS`

**提示（Prompt）**：USB 视频类（UVC）可分配的最大缓冲区数量

**说明（Help）**

控制 USB 视频类（UVC）可同时分配的缓冲区数量。默认值在足够的并发缓冲区与适度内存占用之间折中。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBD_VIDEO_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/usb/device_next/class/Kconfig.uvc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/Kconfig.uvc#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBD_VIDEO_CLASS`](P434_subsys_usb_配置项参考_1.md#CONFIG_USBD_VIDEO_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<!-- kconfig-navigation -->

[上一章](P433_subsys_tracing_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P435_subsys_usb_配置项参考_2.md)
