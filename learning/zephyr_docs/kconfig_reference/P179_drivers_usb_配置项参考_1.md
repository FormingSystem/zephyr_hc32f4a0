---
id: learning.zephyr-docs.kconfig-reference.page-179
title: "`drivers/usb`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第179章\_`drivers/usb`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/usb` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_EMUL_BC12_PI3USB9201"></a>

## 179.1 `CONFIG_EMUL_BC12_PI3USB9201`

**提示（Prompt）**：仿真 Pericom PI3USB9201 USB 充电检测器（Charging Detector）

**说明（Help）**

这是 Pericom PI3USB9201 USB 充电检测器（Charging Detector）的仿真器。后端 API 允许测试代码强制指定连接的充电对端设备类型。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST && DT_HAS_DIODES_PI3USB9201_ENABLED && CONFIG_USB_BC12
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/bc12/Kconfig.pi3usb9201:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/bc12/Kconfig.pi3usb9201#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)、[`CONFIG_USB_BC12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_BC12)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_UHC_MCUX"></a>

## 179.2 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_UHC_MCUX`

**提示（Prompt）**：NXP HAL USB 主机控制器驱动所需的堆（Heap）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.mcux:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.mcux#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_DRIVER)。

<a id="CONFIG_MAX3421E_OSC_WAIT_RETRIES"></a>

## 179.3 `CONFIG_MAX3421E_OSC_WAIT_RETRIES`

**提示（Prompt）**：振荡器就绪事件（Oscillator Ready Event）的最大重试次数

**说明（Help）**

指定振荡器就绪事件（Oscillator Ready Event）的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_MAX3421E && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.max3421e:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.max3421e#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → MAX3421E 驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_MAX3421E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_MAX3421E)、[`CONFIG_UHC_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_DRIVER)。

<a id="CONFIG_MAX3421E_THREAD_STACK_SIZE"></a>

## 179.4 `CONFIG_MAX3421E_THREAD_STACK_SIZE`

**提示（Prompt）**：驱动内部线程栈大小

**说明（Help）**

驱动使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UHC_MAX3421E && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/uhc/Kconfig.max3421e:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/uhc/Kconfig.max3421e#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → MAX3421E 驱动

**配置项引用（Symbol References）**：[`CONFIG_UHC_MAX3421E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_MAX3421E)、[`CONFIG_UHC_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_DRIVER)。

<a id="CONFIG_NRF_USBD_COMMON"></a>

## 179.5 `CONFIG_NRF_USBD_COMMON`

**提示（Prompt）**：USB 设备（USBD）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_UDC_NRF
CONFIG_USB_NRFX
```

**定义位置（Location）**：[`drivers/usb/common/nrf_usbd_common/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/common/nrf_usbd_common/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common）

**配置项引用（Symbol References）**：[`CONFIG_UDC_NRF`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NRF)、[`CONFIG_USB_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_NRFX)。

<a id="CONFIG_NRF_USBD_ISO_IN_ZLP"></a>

## 179.6 `CONFIG_NRF_USBD_ISO_IN_ZLP`

**提示（Prompt）**：未就绪时在等时 IN（ISO IN）端点上发送零长度包（ZLP）

**说明（Help）**

控制没有数据可发送时，等时 IN（ISO IN）端点对 IN 令牌（IN Token）的响应。启用时，在无数据就绪的情况下发送零长度包（Zero-Length Packet，ZLP）；禁用时，不发送响应，因而发生总线超时。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_USBD_COMMON
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/common/nrf_usbd_common/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/common/nrf_usbd_common/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → USB 设备（USBD）驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF_USBD_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_NRF_USBD_COMMON)。

<a id="CONFIG_NRF_USBHS_WRAPPER"></a>

## 179.7 `CONFIG_NRF_USBHS_WRAPPER`

**提示（Prompt）**：Nordic USBHS 封装（Wrapper）

**说明（Help）**

Nordic USBHS 封装（Wrapper）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_USBHS_WRAPPER_ENABLED && CONFIG_REGULATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**被选择（Selected by）**

```text
CONFIG_USB_BC12_NRF_USBHS
CONFIG_UDC_DWC2
```

**定义位置（Location）**：[`drivers/usb/common/nordic/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/common/nordic/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common）

**配置项引用（Symbol References）**：[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_USB_BC12_NRF_USBHS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_BC12_NRF_USBHS)、[`CONFIG_UDC_DWC2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DWC2)。

<a id="CONFIG_STM32_HAS_EMBEDDED_FS_ULPI_OFF_QUIRK"></a>

## 179.8 `CONFIG_STM32_HAS_EMBEDDED_FS_ULPI_OFF_QUIRK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，用于存在以下特殊要求的系列：使用内置全速物理层（Embedded Full-Speed PHY）时，必须禁用 ULPI 时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_STM32F4X || CONFIG_SOC_SERIES_STM32H7X) && CONFIG_STM32_USB_COMMON && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/common/stm32/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/common/stm32/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_STM32_USB_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_STM32_USB_COMMON)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_PHY_EXTERNAL_ULPI"></a>

## 179.9 `CONFIG_STM32_PHY_EXTERNAL_ULPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32 ULPI PHY 接口的伪 PHY 驱动（Pseudo-PHY Driver），使用外部 ULPI PHY 时需要此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_USB_ULPI_PHY_ENABLED && (CONFIG_SOC_SERIES_STM32F2X || CONFIG_SOC_SERIES_STM32F4X || CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32H7X) && CONFIG_STM32_USB_COMMON && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/common/stm32/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/common/stm32/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_STM32_USB_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_STM32_USB_COMMON)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_PHY_U5OTGHSPHY"></a>

## 179.10 `CONFIG_STM32_PHY_U5OTGHSPHY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32 U5OTGHS 内置高速物理层（Embedded High-Speed PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32U5_OTGHS_PHY_ENABLED && CONFIG_STM32_USB_COMMON && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/common/stm32/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/common/stm32/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common）

**配置项引用（Symbol References）**：[`CONFIG_STM32_USB_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_STM32_USB_COMMON)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_PHY_USBPHYC"></a>

## 179.11 `CONFIG_STM32_PHY_USBPHYC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32 USBPHYC 内置高速物理层（Embedded High-Speed PHY）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_USBPHYC_ENABLED || DT_HAS_ST_STM32F7_USBPHYC_ENABLED || DT_HAS_ST_STM32N6_USBPHYC_ENABLED) && CONFIG_STM32_USB_COMMON && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/common/stm32/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/common/stm32/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common）

**配置项引用（Symbol References）**：[`CONFIG_STM32_USB_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_STM32_USB_COMMON)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_USB_COMMON"></a>

## 179.12 `CONFIG_STM32_USB_COMMON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32 USB 公共代码的编译。USB 驱动会在适用时选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**被选择（Selected by）**

```text
CONFIG_UDC_STM32
```

**定义位置（Location）**：[`drivers/usb/common/stm32/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/common/stm32/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_UDC_AMBIQ"></a>

## 179.13 `CONFIG_UDC_AMBIQ`

**提示（Prompt）**：Ambiq 器件的 USB 设备控制器（Device Controller）驱动

**说明（Help）**

启用 USB 设备控制器（Device Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_USB_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_USB
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.ambiq:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.ambiq#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_USB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_USB)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_AMBIQ_DEB_ENABLE"></a>

## 179.14 `CONFIG_UDC_AMBIQ_DEB_ENABLE`

**提示（Prompt）**：启用端点双缓冲（EP Double Buffer）

**说明（Help）**

端点双缓冲加速（Double Endpoint Buffer Acceleration，DEB）将端点（EP）的 FIFO 大小加倍，使 USB 传输在等待 DMA／CPU 向端点 FIFO 装入数据或从中取出数据时仍可继续。此十六进制值是指定哪些端点启用 DEB 的位图：位 0 至 4 表示 OUT_EP 1 至 5，位 16 至 20 表示 IN_EP 1 至 5。

注意，此功能受端点 FIFO 总容量限制。启用 DEB 前，应正确计算所有端点的 FIFO 总用量，确保不超过片上系统（SoC）提供的容量。原文列出的 SoC 及其 FIFO 容量如下，其中包含控制端点所需的 128 字节：

- Apollo510：4096 字节 FIFO。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_APOLLO5X && CONFIG_UDC_AMBIQ && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
0x0000
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.ambiq:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.ambiq#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Ambiq 器件的 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_UDC_AMBIQ`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_AMBIQ_DMA0_MODE"></a>

## 179.15 `CONFIG_UDC_AMBIQ_DMA0_MODE`

**提示（Prompt）**：DMA0 传输模式（Transfer Mode）

**说明（Help）**

使用同步端点（Synchronous Endpoint）时，选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UDC_AMBIQ_DMA_MODE>
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.ambiq:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.ambiq#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Ambiq 器件的 USB 设备控制器（Device Controller）驱动 → 非控制 USB 端点的 DMA 模式

**配置项引用（Symbol References）**：[`CONFIG_UDC_AMBIQ_DMA_MODE`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ_DMA_MODE)。

<a id="CONFIG_UDC_AMBIQ_DMA1_MODE"></a>

## 179.16 `CONFIG_UDC_AMBIQ_DMA1_MODE`

**提示（Prompt）**：DMA1 传输模式（Transfer Mode）

**说明（Help）**

端点缓冲区大于最大包大小（Max Packet Size）时，此选项提供最佳吞吐量。不过，使用同步端点（Synchronous Endpoint）时不能选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UDC_AMBIQ_DMA_MODE>
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.ambiq:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.ambiq#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Ambiq 器件的 USB 设备控制器（Device Controller）驱动 → 非控制 USB 端点的 DMA 模式

**配置项引用（Symbol References）**：[`CONFIG_UDC_AMBIQ_DMA_MODE`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ_DMA_MODE)。

<a id="CONFIG_UDC_AMBIQ_DMA_MODE"></a>

## 179.17 `CONFIG_UDC_AMBIQ_DMA_MODE`

**提示（Prompt）**：非控制 USB 端点的 DMA 模式

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_APOLLO5X && CONFIG_UDC_AMBIQ && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_UDC_AMBIQ_DMA0_MODE
```

**可选项（Choices）**

```text
CONFIG_UDC_AMBIQ_DMA0_MODE
CONFIG_UDC_AMBIQ_DMA1_MODE
CONFIG_UDC_AMBIQ_PIO_MODE
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.ambiq:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.ambiq#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Ambiq 器件的 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_UDC_AMBIQ`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UDC_AMBIQ_DMA0_MODE`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ_DMA0_MODE)、[`CONFIG_UDC_AMBIQ_DMA1_MODE`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ_DMA1_MODE)、[`CONFIG_UDC_AMBIQ_PIO_MODE`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ_PIO_MODE)。

<a id="CONFIG_UDC_AMBIQ_MAX_QMESSAGES"></a>

## 179.18 `CONFIG_UDC_AMBIQ_MAX_QMESSAGES`

**提示（Prompt）**：UDC AMBIQ 中断服务程序（ISR）事件消息的最大数量

**说明（Help）**

AMBIQ 中断服务程序（ISR）事件消息的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_AMBIQ && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[4, 64]
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.ambiq:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.ambiq#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Ambiq 器件的 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_AMBIQ`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_AMBIQ_PIO_MODE"></a>

## 179.19 `CONFIG_UDC_AMBIQ_PIO_MODE`

**提示（Prompt）**：程序控制输入输出（PIO）传输模式

**说明（Help）**

需要避免处理缓存一致性（Cache Coherency）时，选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UDC_AMBIQ_DMA_MODE>
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.ambiq:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.ambiq#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Ambiq 器件的 USB 设备控制器（Device Controller）驱动 → 非控制 USB 端点的 DMA 模式

**配置项引用（Symbol References）**：[`CONFIG_UDC_AMBIQ_DMA_MODE`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ_DMA_MODE)。

<a id="CONFIG_UDC_AMBIQ_STACK_SIZE"></a>

## 179.20 `CONFIG_UDC_AMBIQ_STACK_SIZE`

**提示（Prompt）**：UDC AMBIQ 驱动内部线程栈大小

**说明（Help）**

AMBIQ 驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_AMBIQ && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.ambiq:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.ambiq#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Ambiq 器件的 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_AMBIQ`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_AMBIQ_THREAD_PRIORITY"></a>

## 179.21 `CONFIG_UDC_AMBIQ_THREAD_PRIORITY`

**提示（Prompt）**：UDC AMBIQ 驱动线程优先级

**说明（Help）**

AMBIQ 驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_AMBIQ && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.ambiq:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.ambiq#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Ambiq 器件的 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_AMBIQ`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_AMBIQ)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_BFLB_V1"></a>

## 179.22 `CONFIG_UDC_BFLB_V1`

**提示（Prompt）**：Bouffalo Lab USB 设备控制器驱动（USB v1 模块）

**说明（Help）**

适用于采用 v1 USB 模块的 Bouffalo Lab 片上系统（SoC，BL702/BL706）的 USB 设备控制器驱动。支持 USB 1.1 全速（Full-Speed），具有 8 个端点，每个端点均支持 IN 和 OUT。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_UDC_1_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.bflb_v1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.bflb_v1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UDC_BFLB_V1_STACK_SIZE"></a>

## 179.23 `CONFIG_UDC_BFLB_V1_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

Bouffalo Lab USB 设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_BFLB_V1 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.bflb_v1:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.bflb_v1#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Bouffalo Lab USB 设备控制器驱动（USB v1 模块）

**配置项引用（Symbol References）**：[`CONFIG_UDC_BFLB_V1`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_BFLB_V1)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_BFLB_V1_THREAD_PRIORITY"></a>

## 179.24 `CONFIG_UDC_BFLB_V1_THREAD_PRIORITY`

**提示（Prompt）**：USB 设备控制器（UDC）驱动线程优先级

**说明（Help）**

Bouffalo Lab USB 设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_BFLB_V1 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.bflb_v1:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.bflb_v1#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Bouffalo Lab USB 设备控制器驱动（USB v1 模块）

**配置项引用（Symbol References）**：[`CONFIG_UDC_BFLB_V1`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_BFLB_V1)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_BUF_COUNT"></a>

## 179.25 `CONFIG_UDC_BUF_COUNT`

**提示（Prompt）**：池中的缓冲区数量

**说明（Help）**

池中的 USB 设备控制器（UDC）请求缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[16, 256]
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_BUF_FORCE_NOCACHE"></a>

## 179.26 `CONFIG_UDC_BUF_FORCE_NOCACHE`

**提示（Prompt）**：将缓冲区池放在非缓存内存区域（Nocache Memory Region）

**说明（Help）**

如果驱动无法处理缓存内存中的缓冲区，则将缓冲区池放在非缓存内存区域（Nocache Memory Region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NOCACHE_MEMORY && CONFIG_DCACHE && CONFIG_UDC_DRIVER
```

**被弱选择（Implied by）**

```text
CONFIG_UDC_NXP_EHCI
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UDC_NXP_EHCI`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NXP_EHCI)。

<a id="CONFIG_UDC_BUF_POOL_SIZE"></a>

## 179.27 `CONFIG_UDC_BUF_POOL_SIZE`

**提示（Prompt）**：可用于请求的内存

**说明（Help）**

可用于 USB 设备控制器（UDC）请求的内存总量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[64, 32768]
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_DRIVER"></a>

## 179.28 `CONFIG_UDC_DRIVER`

**提示（Prompt）**：USB 设备控制器（Device Controller）驱动

**说明（Help）**

USB 设备控制器（Device Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NET_BUF
```

**被选择（Selected by）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_UDC_DRIVER_HIGH_SPEED_SUPPORT_ENABLED"></a>

## 179.29 `CONFIG_UDC_DRIVER_HIGH_SPEED_SUPPORT_ENABLED`

**提示（Prompt）**：允许高速握手啁啾信号（High-Speed Chirp）

**说明（Help）**

允许支持高速（High-Speed）的设备以高速运行。禁用此选项可强制设备仅以全速（Full-Speed）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_DWC2"></a>

## 179.30 `CONFIG_UDC_DWC2`

**提示（Prompt）**：DWC2 USB 设备控制器（Device Controller）驱动

**说明（Help）**

DWC2 USB 设备控制器（Device Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DWC2_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
CONFIG_NRFS if CONFIG_NRFS_HAS_VBUS_DETECTOR_SERVICE
CONFIG_NRFS_VBUS_DETECTOR_SERVICE_ENABLED if CONFIG_NRFS_HAS_VBUS_DETECTOR_SERVICE
CONFIG_EVENTS
CONFIG_REGULATOR if CONFIG_SOC_SERIES_NRF54L || CONFIG_SOC_SERIES_NRF71 || CONFIG_SOC_SERIES_NRF92X
CONFIG_NRF_USBHS_WRAPPER if CONFIG_SOC_SERIES_NRF54L || CONFIG_SOC_SERIES_NRF71 || CONFIG_SOC_SERIES_NRF92X
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.dwc2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.dwc2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)、[`CONFIG_NRFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS)、[`CONFIG_NRFS_HAS_VBUS_DETECTOR_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_HAS_VBUS_DETECTOR_SERVICE)、[`CONFIG_NRFS_VBUS_DETECTOR_SERVICE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFS_VBUS_DETECTOR_SERVICE_ENABLED)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_SOC_SERIES_NRF54L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_SERIES_NRF71`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_SERIES_NRF92X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92X)、[`CONFIG_NRF_USBHS_WRAPPER`](P179_drivers_usb_配置项参考_1.md#CONFIG_NRF_USBHS_WRAPPER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`、`CONFIG_NRFS_HAS_VBUS_DETECTOR_SERVICE`。

<a id="CONFIG_UDC_DWC2_DMA"></a>

## 179.31 `CONFIG_UDC_DWC2_DMA`

**提示（Prompt）**：DWC2 USB 直接内存访问（DMA）支持

**说明（Help）**

如果 DWC2 USB 控制器支持内部 DMA（Internal DMA），则启用缓冲区 DMA（Buffer DMA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DWC2 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_SERIES_XMC4XXX
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.dwc2:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.dwc2#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → DWC2 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DWC2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DWC2)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_SOC_SERIES_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC4XXX)。

<a id="CONFIG_UDC_DWC2_HIBERNATION"></a>

## 179.32 `CONFIG_UDC_DWC2_HIBERNATION`

**提示（Prompt）**：DWC2 USB 休眠（Hibernation）支持

**说明（Help）**

如果 DWC2 USB 控制器支持休眠（Hibernation），则启用休眠功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DWC2 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.dwc2:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.dwc2#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → DWC2 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DWC2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DWC2)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_DWC2_PTI"></a>

## 179.33 `CONFIG_UDC_DWC2_PTI`

**提示（Prompt）**：DWC2 USB 周期传输中断（Periodic Transfer Interrupt）

**说明（Help）**

调度等时端点（Isochronous Endpoint）时忽略帧号。当等时传输应仅在收到主机 IN 或 OUT 令牌（Token）后结束时，使用此选项。在周期传输中断（Periodic Transfer Interrupt）模式下，如果主机在某个微帧（Microframe）内未发出令牌，DWC2 驱动不会自动结束该传输。启用可减少等时端点的 CPU 开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DWC2 && CONFIG_UDC_DRIVER
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.dwc2:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.dwc2#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → DWC2 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DWC2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DWC2)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_DWC2_STACK_SIZE"></a>

## 179.34 `CONFIG_UDC_DWC2_STACK_SIZE`

**提示（Prompt）**：UDC DWC2 驱动内部线程栈大小

**说明（Help）**

DWC2 驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DWC2 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1024 if CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.dwc2:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.dwc2#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → DWC2 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DWC2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DWC2)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_UDC_DWC2_THREAD_PRIORITY"></a>

## 179.35 `CONFIG_UDC_DWC2_THREAD_PRIORITY`

**提示（Prompt）**：UDC DWC2 驱动线程优先级

**说明（Help）**

DWC2 驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DWC2 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.dwc2:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.dwc2#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → DWC2 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DWC2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DWC2)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_DWC2_USBHS_VBUS_READY_TIMEOUT"></a>

## 179.36 `CONFIG_UDC_DWC2_USBHS_VBUS_READY_TIMEOUT`

**提示（Prompt）**：UDC DWC2 USBHS VBUS 就绪事件超时，单位为毫秒

**说明（Help）**

UDC DWC2 USBHS VBUS 就绪事件的超时时间。使用 Nordic USBHS 控制器且 VBUS 尚未就绪时，`udc_enable()` 将阻塞此处指定的时长。设为 0 表示无限等待。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_NRF54H || CONFIG_SOC_SERIES_NRF54L || CONFIG_SOC_SERIES_NRF71 || CONFIG_SOC_SERIES_NRF92) && CONFIG_UDC_DWC2 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.dwc2:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.dwc2#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → DWC2 USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_SERIES_NRF54L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_SERIES_NRF71`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_SERIES_NRF92`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92)、[`CONFIG_UDC_DWC2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DWC2)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_ENABLE_SOF"></a>

## 179.37 `CONFIG_UDC_ENABLE_SOF`

**提示（Prompt）**：帧起始（SOF）中断处理

**说明（Help）**

在高速控制器上启用帧起始（SOF）中断可能造成很高的 CPU 负载，因为中断间隔为 125 µs。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_USBD_AUDIO2_CLASS
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_USBD_AUDIO2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_AUDIO2_CLASS)。

<a id="CONFIG_UDC_IT51XXX"></a>

## 179.38 `CONFIG_UDC_IT51XXX`

**提示（Prompt）**：IT51XXX USB 设备控制器驱动

**说明（Help）**

IT51XXX USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_USB_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_IT51XXX_USB_SOF_CALIBRATION
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_IT51XXX_USB_SOF_CALIBRATION`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_IT51XXX_USB_SOF_CALIBRATION)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_UDC_IT51XXX_CLEAR_READY_BIT_SUPPORTED"></a>

## 179.39 `CONFIG_UDC_IT51XXX_CLEAR_READY_BIT_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 IT51XXX USB 设备控制器（UDC）IP 是否支持固件清除就绪位（Ready Bit）。如果不支持，驱动在禁用端点或将端点出队时，改为清除使能位（Enable Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_IT51XXX && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_IT51526AW && !CONFIG_SOC_IT51526BW
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.it51xxx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.it51xxx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → IT51XXX USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_IT51XXX`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_IT51XXX)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_SOC_IT51526AW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51526AW)、[`CONFIG_SOC_IT51526BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51526BW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_IT51526AW`、`CONFIG_SOC_IT51526BW`。

<a id="CONFIG_UDC_IT51XXX_STACK_SIZE"></a>

## 179.40 `CONFIG_UDC_IT51XXX_STACK_SIZE`

**提示（Prompt）**：IT51XXX UDC 驱动内部线程栈大小

**说明（Help）**

驱动中用于处理 IT51XXX USBD 中断服务程序（ISR）事件的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_IT51XXX && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.it51xxx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.it51xxx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → IT51XXX USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_IT51XXX`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_IT51XXX)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_IT51XXX_THREAD_PRIORITY"></a>

## 179.41 `CONFIG_UDC_IT51XXX_THREAD_PRIORITY`

**提示（Prompt）**：IT51XXX UDC 驱动内部线程优先级

**说明（Help）**

IT51XXX UDC 驱动内部线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_IT51XXX && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.it51xxx:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.it51xxx#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → IT51XXX USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_IT51XXX`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_IT51XXX)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_IT82XX2"></a>

## 179.42 `CONFIG_UDC_IT82XX2`

**提示（Prompt）**：IT82XX2 USB 设备控制器驱动

**说明（Help）**

IT82xx2 USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT82XX2_USB_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.it82xx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.it82xx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UDC_IT82xx2_EVENT_COUNT"></a>

## 179.43 `CONFIG_UDC_IT82xx2_EVENT_COUNT`

**提示（Prompt）**：UDC IT82xx2 事件数量

**说明（Help）**

IT82xx2 事件数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_IT82XX2 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[4, 64]
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.it82xx2:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.it82xx2#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → IT82XX2 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_IT82XX2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_IT82XX2)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_IT82xx2_STACK_SIZE"></a>

## 179.44 `CONFIG_UDC_IT82xx2_STACK_SIZE`

**提示（Prompt）**：IT82xx2 UDC 驱动内部线程栈大小

**说明（Help）**

驱动中用于处理 IT82xx2 USBD 中断服务程序（ISR）事件的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_IT82XX2 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.it82xx2:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.it82xx2#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → IT82XX2 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_IT82XX2`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_IT82XX2)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_KINETIS"></a>

## 179.45 `CONFIG_UDC_KINETIS`

**提示（Prompt）**：Kinetis USB 设备控制器驱动

**说明（Help）**

Kinetis USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_USBD_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DYNAMIC_INTERRUPTS if CONFIG_UHC_NXP_KHCI
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.kinetis:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.kinetis#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_UHC_NXP_KHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_NXP_KHCI)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_UDC_KINETIS_STACK_SIZE"></a>

## 179.46 `CONFIG_UDC_KINETIS_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_KINETIS && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.kinetis:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.kinetis#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Kinetis USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_KINETIS`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_KINETIS)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_KINETIS_THREAD_PRIORITY"></a>

## 179.47 `CONFIG_UDC_KINETIS_THREAD_PRIORITY`

**提示（Prompt）**：USB 设备控制器（UDC）驱动线程优先级

**说明（Help）**

设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_KINETIS && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.kinetis:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.kinetis#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Kinetis USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_KINETIS`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_KINETIS)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_MAX32"></a>

## 179.48 `CONFIG_UDC_MAX32`

**提示（Prompt）**：MAX32 USB 设备控制器驱动

**说明（Help）**

MAX32 USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_USBHS_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_MAX32_MAX_QMESSAGES"></a>

## 179.49 `CONFIG_UDC_MAX32_MAX_QMESSAGES`

**提示（Prompt）**：MAX32 UDC 驱动中断服务程序（ISR）事件消息的最大数量

**说明（Help）**

用于处理 MAX32 USBD 中断服务程序（ISR）事件的消息最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_MAX32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[4, 64]
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.max32:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.max32#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → MAX32 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_MAX32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_MAX32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_MAX32_THREAD_PRIORITY"></a>

## 179.50 `CONFIG_UDC_MAX32_THREAD_PRIORITY`

**提示（Prompt）**：MAX32 USB 设备控制器驱动线程优先级

**说明（Help）**

MAX32 USB 设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_MAX32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.max32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.max32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → MAX32 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_MAX32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_MAX32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_MAX32_THREAD_STACK_SIZE"></a>

## 179.51 `CONFIG_UDC_MAX32_THREAD_STACK_SIZE`

**提示（Prompt）**：MAX32 UDC 驱动内部线程栈大小

**说明（Help）**

驱动内部线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_MAX32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.max32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.max32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → MAX32 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_MAX32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_MAX32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_MCHP_UDPHS_G1"></a>

## 179.52 `CONFIG_UDC_MCHP_UDPHS_G1`

**提示（Prompt）**：Microchip USB 设备高速端口（USB Device High Speed Port，UDPHS）G1

**说明（Help）**

启用 Microchip UDPHS G1 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_UDPHS_G1_UDC_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_GPIO
CONFIG_SYS_MEM_BLOCKS
CONFIG_EVENTS
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_MCHP_UDPHS_G1_BURST_LOCK"></a>

## 179.53 `CONFIG_UDC_MCHP_UDPHS_G1_BURST_LOCK`

**提示（Prompt）**：锁定总线访问以获得最大带宽

**说明（Help）**

锁定 USB 包的系统数据突发传输（System Data Bursts），以最大程度优化总线带宽利用率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_MCHP_UDPHS_G1 && CONFIG_UDC_DRIVER
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mchp:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mchp#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Microchip USB 设备高速端口（USB Device High Speed Port，UDPHS）G1

**配置项引用（Symbol References）**：[`CONFIG_UDC_MCHP_UDPHS_G1`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_MCHP_UDPHS_G1)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_MCHP_UDPHS_G1_DMA"></a>

## 179.54 `CONFIG_UDC_MCHP_UDPHS_G1_DMA`

**提示（Prompt）**：直接内存访问支持（DMA Support）

**说明（Help）**

启用直接内存访问（DMA）传输；否则，通过 FIFO 传输数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_MCHP_UDPHS_G1 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mchp:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mchp#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Microchip USB 设备高速端口（USB Device High Speed Port，UDPHS）G1

**配置项引用（Symbol References）**：[`CONFIG_UDC_MCHP_UDPHS_G1`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_MCHP_UDPHS_G1)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_MCHP_UDPHS_G1_STACK_SIZE"></a>

## 179.55 `CONFIG_UDC_MCHP_UDPHS_G1_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_MCHP_UDPHS_G1 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mchp:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mchp#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Microchip USB 设备高速端口（USB Device High Speed Port，UDPHS）G1

**配置项引用（Symbol References）**：[`CONFIG_UDC_MCHP_UDPHS_G1`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_MCHP_UDPHS_G1)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_MCHP_UDPHS_G1_THREAD_PRI"></a>

## 179.56 `CONFIG_UDC_MCHP_UDPHS_G1_THREAD_PRI`

**提示（Prompt）**：USB 设备控制器（UDC）驱动线程优先级

**说明（Help）**

设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_MCHP_UDPHS_G1 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mchp:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mchp#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Microchip USB 设备高速端口（USB Device High Speed Port，UDPHS）G1

**配置项引用（Symbol References）**：[`CONFIG_UDC_MCHP_UDPHS_G1`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_MCHP_UDPHS_G1)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NRF"></a>

## 179.57 `CONFIG_UDC_NRF`

**提示（Prompt）**：Nordic Semiconductor USB 设备控制器驱动

**说明（Help）**

nRF USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_USBD_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRF_USBD_COMMON
CONFIG_NRFX_POWER
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.nrf:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.nrf#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_NRF_USBD_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_NRF_USBD_COMMON)、[`CONFIG_NRFX_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_POWER)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_UDC_NRF_THREAD_STACK_SIZE"></a>

## 179.58 `CONFIG_UDC_NRF_THREAD_STACK_SIZE`

**提示（Prompt）**：nRF UDC 驱动内部线程栈大小

**说明（Help）**

驱动中用于处理 nRF USBD 中断服务程序（ISR）事件的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_NRF && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.nrf:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.nrf#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nordic Semiconductor USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_NRF`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NRF)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NUMAKER"></a>

## 179.59 `CONFIG_UDC_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker USB 设备控制器

**说明（Help）**

启用 Nuvoton NuMaker USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NUVOTON_NUMAKER_USBD_ENABLED || DT_HAS_NUVOTON_NUMAKER_HSUSBD_ENABLED) && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT if DT_HAS_NUVOTON_NUMAKER_HSUSBD_ENABLED
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.numaker:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.numaker#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_NUMAKER_DMA"></a>

## 179.60 `CONFIG_UDC_NUMAKER_DMA`

**提示（Prompt）**：UDC NuMaker 直接内存访问（DMA）支持

**说明（Help）**

启用用户缓冲区与 USB 缓冲区之间的直接内存访问（DMA）传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_HSUSBD_ENABLED && CONFIG_UDC_NUMAKER && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.numaker:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.numaker#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nuvoton NuMaker USB 设备控制器

**配置项引用（Symbol References）**：[`CONFIG_UDC_NUMAKER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NUMAKER)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NUMAKER_DMA_TIMEOUT_MS"></a>

## 179.61 `CONFIG_UDC_NUMAKER_DMA_TIMEOUT_MS`

**提示（Prompt）**：UDC NuMaker DMA 超时时间

**说明（Help）**

配置 DMA 传输的超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_NUMAKER_DMA && CONFIG_UDC_NUMAKER && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.numaker:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.numaker#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nuvoton NuMaker USB 设备控制器 → UDC NuMaker 直接内存访问（DMA）支持

**配置项引用（Symbol References）**：[`CONFIG_UDC_NUMAKER_DMA`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NUMAKER_DMA)、[`CONFIG_UDC_NUMAKER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NUMAKER)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NUMAKER_MSG_QUEUE_SIZE"></a>

## 179.62 `CONFIG_UDC_NUMAKER_MSG_QUEUE_SIZE`

**提示（Prompt）**：UDC NuMaker 消息队列（Message Queue）大小

**说明（Help）**

驱动能够排入队列、用于中断下半部（Interrupt Bottom Half）处理的消息最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_NUMAKER && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.numaker:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.numaker#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nuvoton NuMaker USB 设备控制器

**配置项引用（Symbol References）**：[`CONFIG_UDC_NUMAKER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NUMAKER)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NUMAKER_THREAD_PRIORITY"></a>

## 179.63 `CONFIG_UDC_NUMAKER_THREAD_PRIORITY`

**提示（Prompt）**：UDC NuMaker 驱动内部线程优先级

**说明（Help）**

驱动内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_NUMAKER && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.numaker:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.numaker#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nuvoton NuMaker USB 设备控制器

**配置项引用（Symbol References）**：[`CONFIG_UDC_NUMAKER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NUMAKER)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NUMAKER_THREAD_STACK_SIZE"></a>

## 179.64 `CONFIG_UDC_NUMAKER_THREAD_STACK_SIZE`

**提示（Prompt）**：UDC NuMaker 驱动内部线程栈大小

**说明（Help）**

驱动内部线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_NUMAKER && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1536
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.numaker:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.numaker#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Nuvoton NuMaker USB 设备控制器

**配置项引用（Symbol References）**：[`CONFIG_UDC_NUMAKER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NUMAKER)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NXP_EHCI"></a>

## 179.65 `CONFIG_UDC_NXP_EHCI`

**提示（Prompt）**：NXP MCUX USB EHCI 设备控制器驱动

**说明（Help）**

用于 EHCI 的 NXP MCUX USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_EHCI_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
CONFIG_PINCTRL
CONFIG_NOCACHE_MEMORY if CONFIG_CPU_HAS_DCACHE
CONFIG_DYNAMIC_INTERRUPTS if CONFIG_UHC_NXP_EHCI
CONFIG_EVENTS
```

**弱选择（Implies）**

```text
CONFIG_UDC_BUF_FORCE_NOCACHE
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mcux:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mcux#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_UHC_NXP_EHCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_NXP_EHCI)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_UDC_BUF_FORCE_NOCACHE`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_BUF_FORCE_NOCACHE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_NXP_EHCI_THREAD_PRIORITY"></a>

## 179.66 `CONFIG_UDC_NXP_EHCI_THREAD_PRIORITY`

**提示（Prompt）**：NXP EHCI UDC 驱动内部线程优先级

**说明（Help）**

处理控制器事件的内部线程的协作式优先级（Cooperative Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_NXP_EHCI && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mcux:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mcux#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → NXP MCUX USB EHCI 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_NXP_EHCI`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NXP_EHCI)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NXP_EHCI_THREAD_STACK_SIZE"></a>

## 179.67 `CONFIG_UDC_NXP_EHCI_THREAD_STACK_SIZE`

**提示（Prompt）**：NXP EHCI UDC 驱动内部线程栈大小

**说明（Help）**

处理控制器事件的内部线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_NXP_EHCI && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mcux:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mcux#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → NXP MCUX USB EHCI 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_NXP_EHCI`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NXP_EHCI)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NXP_IP3511"></a>

## 179.68 `CONFIG_UDC_NXP_IP3511`

**提示（Prompt）**：NXP MCUX USB IP3511 设备控制器驱动

**说明（Help）**

用于 IP3511 的 NXP MCUX USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPCIP3511_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
CONFIG_PINCTRL
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mcux:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mcux#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_NXP_IP3511_THREAD_PRIORITY"></a>

## 179.69 `CONFIG_UDC_NXP_IP3511_THREAD_PRIORITY`

**提示（Prompt）**：NXP IP3511 UDC 驱动内部线程优先级

**说明（Help）**

处理控制器事件的内部线程的协作式优先级（Cooperative Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_NXP_IP3511 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mcux:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mcux#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → NXP MCUX USB IP3511 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_NXP_IP3511`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NXP_IP3511)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_NXP_IP3511_THREAD_STACK_SIZE"></a>

## 179.70 `CONFIG_UDC_NXP_IP3511_THREAD_STACK_SIZE`

**提示（Prompt）**：NXP IP3511 UDC 驱动内部线程栈大小

**说明（Help）**

处理控制器事件的内部线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_NXP_IP3511 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.mcux:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.mcux#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → NXP MCUX USB IP3511 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_NXP_IP3511`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_NXP_IP3511)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_RENESAS_RA"></a>

## 179.71 `CONFIG_UDC_RENESAS_RA`

**提示（Prompt）**：Renesas RA 系列 USB 设备控制器（UDC）驱动

**说明（Help）**

启用 Renesas RA 系列 USB 设备控制器（UDC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_UDC_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_USB_DEVICE
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_USE_RA_FSP_USB_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_USB_DEVICE)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_RENESAS_RA_MAX_QMESSAGES"></a>

## 179.72 `CONFIG_UDC_RENESAS_RA_MAX_QMESSAGES`

**提示（Prompt）**：Renesas RA 系列 UDC 驱动中断服务程序（ISR）事件消息的最大数量

**说明（Help）**

用于处理 Renesas RA USBD 中断服务程序（ISR）事件的消息最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_RENESAS_RA && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[4, 64]
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.renesas_ra:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.renesas_ra#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Renesas RA 系列 USB 设备控制器（UDC）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_RENESAS_RA`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_RENESAS_RA)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_RENESAS_RA_STACK_SIZE"></a>

## 179.73 `CONFIG_UDC_RENESAS_RA_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

Renesas RA 设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_RENESAS_RA && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.renesas_ra:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.renesas_ra#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Renesas RA 系列 USB 设备控制器（UDC）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_RENESAS_RA`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_RENESAS_RA)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_RENESAS_RA_THREAD_PRIORITY"></a>

## 179.74 `CONFIG_UDC_RENESAS_RA_THREAD_PRIORITY`

**提示（Prompt）**：Renesas RA 系列 UDC 驱动线程优先级

**说明（Help）**

Renesas RA 设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_RENESAS_RA && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.renesas_ra:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.renesas_ra#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Renesas RA 系列 USB 设备控制器（UDC）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_RENESAS_RA`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_RENESAS_RA)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_RPI_PICO"></a>

## 179.75 `CONFIG_UDC_RPI_PICO`

**提示（Prompt）**：Raspberry Pi Pico USB 设备控制器驱动

**说明（Help）**

Raspberry Pi Pico USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_USBD_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYS_MEM_BLOCKS
CONFIG_EVENTS
```

**弱选择（Implies）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_UDC_RPI_PICO_STACK_SIZE"></a>

## 179.76 `CONFIG_UDC_RPI_PICO_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_RPI_PICO && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.rpi_pico:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.rpi_pico#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Raspberry Pi Pico USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_RPI_PICO`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_RPI_PICO)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_RPI_PICO_THREAD_PRIORITY"></a>

## 179.77 `CONFIG_UDC_RPI_PICO_THREAD_PRIORITY`

**提示（Prompt）**：USB 设备控制器（UDC）驱动线程优先级

**说明（Help）**

设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_RPI_PICO && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.rpi_pico:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.rpi_pico#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Raspberry Pi Pico USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_RPI_PICO`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_RPI_PICO)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SAM0"></a>

## 179.78 `CONFIG_UDC_SAM0`

**提示（Prompt）**：SAM0 系列 USB 设备控制器驱动

**说明（Help）**

SAM0 系列 USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_USB_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_UDC_SAM0_STACK_SIZE"></a>

## 179.79 `CONFIG_UDC_SAM0_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SAM0 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam0:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam0#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → SAM0 系列 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_SAM0`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SAM0)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SAM0_THREAD_PRIORITY"></a>

## 179.80 `CONFIG_UDC_SAM0_THREAD_PRIORITY`

**提示（Prompt）**：USB 设备控制器（UDC）驱动线程优先级

**说明（Help）**

设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SAM0 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam0:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam0#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → SAM0 系列 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_SAM0`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SAM0)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SAM_UDP"></a>

## 179.81 `CONFIG_UDC_SAM_UDP`

**提示（Prompt）**：Atmel SAM USB 设备端口（USB Device Port，UDP）控制器

**说明（Help）**

启用 Atmel SAM USB 设备端口（UDP）控制器驱动。此控制器支持 USB 2.0 全速（Full-speed）设备模式，具有 8 个端点。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_UDP_ENABLED && CONFIG_SOC_FAMILY_ATMEL_SAM && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam_udp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam_udp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_UDC_SAM_UDP_THREAD_PRIORITY"></a>

## 179.82 `CONFIG_UDC_SAM_UDP_THREAD_PRIORITY`

**提示（Prompt）**：USB 设备控制器驱动线程优先级

**说明（Help）**

USB 设备控制器驱动线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SAM_UDP && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam_udp:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam_udp#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Atmel SAM USB 设备端口（USB Device Port，UDP）控制器

**配置项引用（Symbol References）**：[`CONFIG_UDC_SAM_UDP`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SAM_UDP)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SAM_UDP_THREAD_STACK_SIZE"></a>

## 179.83 `CONFIG_UDC_SAM_UDP_THREAD_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器驱动线程栈大小

**说明（Help）**

USB 设备控制器驱动线程的栈大小。该线程处理 USB 事件，包括 OUT 数据接收。为处理从 `udc_submit_ep_event()` 发起、可能调用 USB 类驱动（Class Driver）的回调链，需要较大的栈。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SAM_UDP && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam_udp:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam_udp#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → Atmel SAM USB 设备端口（USB Device Port，UDP）控制器

**配置项引用（Symbol References）**：[`CONFIG_UDC_SAM_UDP`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SAM_UDP)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SAM_USBC"></a>

## 179.84 `CONFIG_UDC_SAM_USBC`

**提示（Prompt）**：SAM USBC 系列 USB 设备控制器驱动

**说明（Help）**

SAM USBC 系列 USB 设备控制器（SAM4L 系列）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_USBC_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam_usbc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam_usbc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_UDC_SAM_USBC_STACK_SIZE"></a>

## 179.85 `CONFIG_UDC_SAM_USBC_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SAM_USBC && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam_usbc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam_usbc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → SAM USBC 系列 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_SAM_USBC`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SAM_USBC)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SAM_USBC_THREAD_PRIORITY"></a>

## 179.86 `CONFIG_UDC_SAM_USBC_THREAD_PRIORITY`

**提示（Prompt）**：USB 设备控制器（UDC）驱动线程优先级

**说明（Help）**

设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SAM_USBC && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam_usbc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam_usbc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → SAM USBC 系列 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_SAM_USBC`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SAM_USBC)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SAM_USBHS"></a>

## 179.87 `CONFIG_UDC_SAM_USBHS`

**提示（Prompt）**：SAM USBHS USB 设备控制器驱动

**说明（Help）**

SAM E70/S70/V70/V71 系列 USBHS 设备控制器驱动。支持高速（High-Speed，480 Mbps）和全速（Full-Speed，12 Mbps）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_USBHS_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_EVENTS
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT if n
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam_usbhs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam_usbhs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_SAM_USBHS_STACK_SIZE"></a>

## 179.88 `CONFIG_UDC_SAM_USBHS_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SAM_USBHS && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam_usbhs:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam_usbhs#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → SAM USBHS USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_SAM_USBHS`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SAM_USBHS)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SAM_USBHS_THREAD_PRIORITY"></a>

## 179.89 `CONFIG_UDC_SAM_USBHS_THREAD_PRIORITY`

**提示（Prompt）**：USB 设备控制器（UDC）驱动线程优先级

**说明（Help）**

设备控制器驱动线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SAM_USBHS && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.sam_usbhs:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.sam_usbhs#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → SAM USBHS USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_SAM_USBHS`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SAM_USBHS)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SKELETON"></a>

## 179.90 `CONFIG_UDC_SKELETON`

**提示（Prompt）**：USB 设备控制器驱动骨架（Skeleton）

**说明（Help）**

USB 设备控制器驱动骨架（Skeleton）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_UDC_SKELETON_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.skeleton:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.skeleton#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_SKELETON_STACK_SIZE"></a>

## 179.91 `CONFIG_UDC_SKELETON_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

设备控制器驱动骨架的内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SKELETON && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.skeleton:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.skeleton#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 设备控制器驱动骨架（Skeleton）

**配置项引用（Symbol References）**：[`CONFIG_UDC_SKELETON`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SKELETON)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SKELETON_THREAD_PRIORITY"></a>

## 179.92 `CONFIG_UDC_SKELETON_THREAD_PRIORITY`

**提示（Prompt）**：控制器驱动骨架的线程优先级

**说明（Help）**

设备控制器驱动骨架的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_SKELETON && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.skeleton:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.skeleton#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 设备控制器驱动骨架（Skeleton）

**配置项引用（Symbol References）**：[`CONFIG_UDC_SKELETON`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_SKELETON)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_SMARTBOND"></a>

## 179.93 `CONFIG_UDC_SMARTBOND`

**提示（Prompt）**：Smartbond USB 设备控制器驱动

**说明（Help）**

Smartbond USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_USBD_ENABLED && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.smartbond:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.smartbond#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_UDC_STM32"></a>

## 179.94 `CONFIG_UDC_STM32`

**提示（Prompt）**：STM32 USB 设备控制器驱动

**说明（Help）**

STM32 USB 设备控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_OTGFS_ENABLED || DT_HAS_ST_STM32_OTGHS_ENABLED || DT_HAS_ST_STM32_USB_ENABLED) && CONFIG_UDC_DRIVER
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
CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT
CONFIG_STM32_USB_COMMON
CONFIG_PINCTRL
CONFIG_GPIO if n
```

**弱选择（Implies）**

```text
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_USE_STM32_LL_USB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_USB)、[`CONFIG_USE_STM32_HAL_PCD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PCD)、[`CONFIG_USE_STM32_HAL_PCD_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PCD_EX)、[`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT)、[`CONFIG_STM32_USB_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_STM32_USB_COMMON)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_UDC_DRIVER_HAS_HIGH_SPEED_SUPPORT`。

<a id="CONFIG_UDC_STM32_CLOCK_CHECK"></a>

## 179.95 `CONFIG_UDC_STM32_CLOCK_CHECK`

**提示（Prompt）**：运行时 USB 48 MHz 时钟检查

**说明（Help）**

启用运行时 USB 48 MHz 时钟配置检查。某些特定情况下，此检查可能给出错误判定，应禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_STM32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
n if CONFIG_SOC_SERIES_STM32F1X || CONFIG_SOC_SERIES_STM32F3X || CONFIG_SOC_SERIES_STM32L1X || CONFIG_SOC_SERIES_STM32U5X || CONFIG_SOC_SERIES_STM32WBAX
y
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.stm32:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.stm32#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → STM32 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F3X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F3X`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WBAX`。

<a id="CONFIG_UDC_STM32_MAX_QMESSAGES"></a>

## 179.96 `CONFIG_UDC_STM32_MAX_QMESSAGES`

**提示（Prompt）**：STM32 UDC 驱动中断服务程序（ISR）事件消息的最大数量

**说明（Help）**

用于处理 STM32 USBD 中断服务程序（ISR）事件的消息最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_STM32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[4, 64]
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.stm32:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.stm32#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → STM32 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_STM32_OTG_RXFIFO_BASELINE_SIZE"></a>

## 179.97 `CONFIG_UDC_STM32_OTG_RXFIFO_BASELINE_SIZE`

**提示（Prompt）**：接收 FIFO 基准大小（Baseline RxFIFO Size），单位为字节

**说明（Help）**

计算接收 FIFO（RxFIFO）大小时的基准值。OTG_FS 和 OTG_HS USB 控制器使用单个 RxFIFO 保存所有 OUT 端点接收的数据。RxFIFO 大小受多种参数影响；最佳值取决于实际使用的 USB 配置，但驱动在必须配置 RxFIFO 大小时尚不知道这些信息。

RxFIFO 总大小等于此选项的值，加上驱动可根据硬件配置推导出的固定开销，例如已实现的端点数量。有关 RxFIFO 的更多信息，请参阅 STM32 参考手册。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_OTGFS_ENABLED || DT_HAS_ST_STM32_OTGHS_ENABLED) && CONFIG_UDC_STM32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
600
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.stm32:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.stm32#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → STM32 USB 设备控制器驱动 → OTGHS/OTGFS 选项

**配置项引用（Symbol References）**：[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_STM32_STACK_SIZE"></a>

## 179.98 `CONFIG_UDC_STM32_STACK_SIZE`

**提示（Prompt）**：USB 设备控制器（UDC）驱动内部线程栈大小

**说明（Help）**

STM32 USB 设备控制器驱动内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UDC_STM32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.stm32:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.stm32#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → STM32 USB 设备控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_STM32_STUSB_ISO_IN_EP_NUM"></a>

## 179.99 `CONFIG_UDC_STM32_STUSB_ISO_IN_EP_NUM`

**提示（Prompt）**：为等时 IN（Isochronous IN）预留的端点数量

**说明（Help）**

为 IN 等时模式（Isochronous Mode）操作预留的端点数量。此选项设为 0 时，不能将任何端点配置为等时 IN 模式。更多信息请参阅 `CONFIG_UDC_STM32_STUSB_ISO_OUT_EP_NUM`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_USB_ENABLED && CONFIG_UDC_STM32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.stm32:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.stm32#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → STM32 USB 设备控制器驱动 → ST USB 选项

**配置项引用（Symbol References）**：[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<a id="CONFIG_UDC_STM32_STUSB_ISO_OUT_EP_NUM"></a>

## 179.100 `CONFIG_UDC_STM32_STUSB_ISO_OUT_EP_NUM`

**提示（Prompt）**：为等时 OUT（Isochronous OUT）预留的端点数量

**说明（Help）**

为 OUT 等时模式（Isochronous Mode）操作预留的端点数量。等时模式需要特殊处理，当前协议栈设计不易直接完成，因此通过此选项预留用于等时模式的端点。

此选项与 `CONFIG_UDC_STM32_STUSB_ISO_IN_EP_NUM` 配合使用。最先的 `CONFIG_UDC_STM32_STUSB_ISO_OUT_EP_NUM` 个端点被预留，只能配置为等时 OUT；接下来的 `UDC_STM32_STUSB_ISO_IN_EP_NUM` 个端点被预留，只能配置为等时 IN。其余端点可在任意方向配置为批量／中断（Bulk/Interrupt）端点。预留从 EP1 开始，EP0 保留为控制端点（Control Endpoint）。

例如，`CONFIG_UDC_STM32_STUSB_ISO_OUT_EP_NUM` 和 `CONFIG_UDC_STM32_STUSB_ISO_IN_EP_NUM` 均设为 1 时：

- EP0 OUT/IN：保留为控制端点。
- EP1 OUT：预留给等时模式。
- EP1 IN：被预留，不能使用。
- EP2 OUT：被预留，不能使用。
- EP2 IN：预留给等时模式。
- EP3 至 EPn OUT/IN：可自由用于批量／中断模式。

此选项设为 0 时，不能将任何端点配置为等时 OUT。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_USB_ENABLED && CONFIG_UDC_STM32 && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/usb/udc/Kconfig.stm32:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/Kconfig.stm32#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → STM32 USB 设备控制器驱动 → ST USB 选项

**配置项引用（Symbol References）**：[`CONFIG_UDC_STM32`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_STM32)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)。

<!-- kconfig-navigation -->

[上一章](P178_drivers_uaol_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P180_drivers_usb_配置项参考_2.md)
