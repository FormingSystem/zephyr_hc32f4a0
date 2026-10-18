---
id: learning.zephyr-docs.kconfig-reference.page-85
title: "`drivers/espi`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第85章\_`drivers/espi`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/espi` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESPI"></a>

## 85.1 `CONFIG_ESPI`

**提示（Prompt）**：增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**说明（Help）**

启用 eSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/espi/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_ESPI_AUTOMATIC_BOOT_DONE_ACKNOWLEDGE"></a>

## 85.2 `CONFIG_ESPI_AUTOMATIC_BOOT_DONE_ACKNOWLEDGE`

**提示（Prompt）**：自动确认目标启动状态（Automatically Acknowledge Target Boot Status）

**说明（Help）**

启用自动确认（Automatic Acknowledgment）：目标设备完成基本配置后，向 eSPI 主设备（Master）发送虚拟线消息（Virtual Wire Message）进行确认。确认时机取决于 SPI 启动配置；可能在流程较早阶段、虚拟线（VW）通道配置完成后进行，也可能等到闪存通道（Flash Channel）配置完成后再进行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_VWIRE_CHANNEL && CONFIG_ESPI_TARGET && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → eSPI 虚拟线通道（Virtual Wire Channel）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_VWIRE_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_VWIRE_CHANNEL)、[`CONFIG_ESPI_TARGET`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TARGET)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_AUTOMATIC_WARNING_ACKNOWLEDGE"></a>

## 85.3 `CONFIG_ESPI_AUTOMATIC_WARNING_ACKNOWLEDGE`

**提示（Prompt）**：自动确认 eSPI 主机警告（HOST Warnings）

**说明（Help）**

启用自动确认（Automatic Acknowledgment）：eSPI 目标设备（Target）每次收到挂起或复位警告（Suspend or Reset Warning）时，向 eSPI 控制器（Controller）确认。禁用此项意味着应用程序希望获得为主机挂起或复位做准备的机会。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_VWIRE_CHANNEL && CONFIG_ESPI_TARGET && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → eSPI 虚拟线通道（Virtual Wire Channel）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_VWIRE_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_VWIRE_CHANNEL)、[`CONFIG_ESPI_TARGET`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TARGET)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_EMUL"></a>

## 85.4 `CONFIG_ESPI_EMUL`

**提示（Prompt）**：eSPI 仿真器（Emulator）

**说明（Help）**

启用 eSPI 仿真器驱动（Emulator Driver）。这是一个伪驱动（Fake Driver），不与实际硬件通信，而是与仿真驱动通信；这些仿真驱动模拟仿真 eSPI 总线上的设备。它用于测试 eSPI 设备驱动。

eSPI 是使用 SPI 线路的接口，主要目的是减少所需引脚数量。它包含 LPC、SMB、SPI 本身的闪存访问（Flash Access），以及 GPIO 虚拟线（Virtual Wires）等功能。更多详情可参见 [Intel eSPI 基础规范 Rev 1.0（原文引用）](https://www.intel.com/content/dam/support/us/en/documents/software/chipset-software/327432-004_espi_base_specification_rev1.0_cb.pdf)，该规范也适合作为入门资料。

> 译注：2026-10-17 核验时，此旧版 PDF 地址实际返回重定向后的 Intel 文档入口 HTML，未取得 Rev 1.0 PDF 正文。保留 Zephyr 原始引用，不将可打开的替代入口计为旧版 PDF 已验证；本条译文依据已保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_ESPI_EMUL_CONTROLLER_ENABLED && CONFIG_EMUL && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.espi_emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.espi_emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_FLASH_BUFFER_SIZE"></a>

## 85.5 `CONFIG_ESPI_FLASH_BUFFER_SIZE`

**提示（Prompt）**：eSPI 闪存通道缓冲区大小（Flash Channel Buffer Size），以字节为单位

**说明（Help）**

使用规范定义的最大 RAM 缓冲区（Buffer）大小；如果 eSPI 主机不支持此大小，允许应用程序覆盖该值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_FLASH_CHANNEL && (CONFIG_ESPI_XEC || CONFIG_ESPI_XEC_V2) && CONFIG_ESPI
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_FLASH_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_FLASH_CHANNEL)、[`CONFIG_ESPI_XEC`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_FLASH_CHANNEL"></a>

## 85.6 `CONFIG_ESPI_FLASH_CHANNEL`

**提示（Prompt）**：eSPI 闪存通道（Flash Channel）

**说明（Help）**

eSPI 控制器（Controller）支持闪存通道（Flash Channel）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_INIT_PRIORITY"></a>

## 85.7 `CONFIG_ESPI_INIT_PRIORITY`

**提示（Prompt）**：eSPI 控制器驱动初始化优先级（Initialization Priority）

**说明（Help）**

eSPI 驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/espi/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_IT8XXX2"></a>

## 85.8 `CONFIG_ESPI_IT8XXX2`

**提示（Prompt）**：ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动

**说明（Help）**

启用 ITE IT8XXX2 eSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_ESPI_ENABLED && (CONFIG_SOC_IT8XXX2 || CONFIG_SOC_IT51XXX) && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2)、[`CONFIG_SOC_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51XXX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_IT8XXX2`、`CONFIG_SOC_IT51XXX`。

<a id="CONFIG_ESPI_IT8XXX2_H2RAM_SHARED"></a>

## 85.9 `CONFIG_ESPI_IT8XXX2_H2RAM_SHARED`

**提示（Prompt）**：共享访问 `h2ram_pool`（Shared Access）

**说明（Help）**

启用此选项会将 eSPI 驱动的 `h2ram_pool` 作为全局符号（Global Symbol，非 `static`）公开，使其他模块可复用这段内存。`CONFIG_ESPI_PERIPHERAL_HOST_CMD_PARAM_PORT_NUM` 与 `CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION_PORT_NUM` 配置对应的 RAM 空间之间存在空隙。启用 `CONFIG_ESPI_IT8XXX2_H2RAM_SHARED` 后，其他模块可复用这段未使用的空隙，减少整体 RAM 用量。

**注意**：必须通过构建时断言（Build-Time Assertion）确保共享区域大小不超过 `CONFIG_ESPI_PERIPHERAL_HOST_CMD_PARAM_PORT_NUM` 和 `CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION_PORT_NUM` 所限定的可用空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_IT8XXX2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_IT8XXX2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_IT8XXX2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_IT8XXX2_PNPCFG_DEVICE_KBC_MOUSE"></a>

## 85.10 `CONFIG_ESPI_IT8XXX2_PNPCFG_DEVICE_KBC_MOUSE`

**提示（Prompt）**：ITE IT8XXX2 KBC 鼠标设备（Mouse Device）

**说明（Help）**

启用此选项后，键盘控制器（KBC）的鼠标输出缓冲区（Output Buffer）满时，嵌入式控制器（EC）向主机发送 IRQ12 信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_IT8XXX2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_IT8XXX2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_IT8XXX2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_IT8XXX2_PORT_81_CYCLE"></a>

## 85.11 `CONFIG_ESPI_IT8XXX2_PORT_81_CYCLE`

**提示（Prompt）**：EC 接受 eSPI 事务中的 `0x81` I/O 周期（I/O Cycle）

**说明（Help）**

启用此选项后，嵌入式控制器（EC）接受来自主机的 `0x81` I/O 周期（I/O Cycle），从而可接受主机写入的 2 字节端口 80 数据。例如，使用 `iotools`：

```sh
iotools io_write16 0x80 0x1234
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80 && CONFIG_ESPI_IT8XXX2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80)、[`CONFIG_ESPI_IT8XXX2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_IT8XXX2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_NPCX"></a>

## 85.12 `CONFIG_ESPI_NPCX`

**提示（Prompt）**：新唐（Nuvoton）NPCX 嵌入式控制器（Embedded Controller，EC）eSPI 驱动

**说明（Help）**

此选项为 NPCX 系列处理器启用 Intel 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NPCX && DT_HAS_NUVOTON_NPCX_ESPI_ENABLED && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`。

<a id="CONFIG_ESPI_NPCX_BYPASS_CH_ENABLE_FATAL_ERROR"></a>

## 85.13 `CONFIG_ESPI_NPCX_BYPASS_CH_ENABLE_FATAL_ERROR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

规避 NPCX99nF 勘误（Errata）rev1_2 第 3.10 项记录的问题。在 eSPI 事务（Transaction）期间启用 eSPI 通道，可能以较低概率使 `eSPI_SIF` 模块转入错误状态，进而对传入事务返回 `FATAL_ERROR`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESPI_NPCX_NPCXN_V1 || CONFIG_ESPI_NPCX_NPCXN_V2) && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NPCX_NPCXN_V1`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_NPCXN_V1)、[`CONFIG_ESPI_NPCX_NPCXN_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_NPCXN_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_NPCX_CAF_GLOBAL_RESET_WORKAROUND"></a>

## 85.14 `CONFIG_ESPI_NPCX_CAF_GLOBAL_RESET_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

规避 NPCX4 SoC 勘误（Errata）中的“全局复位（Global Reset）”问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_NPCX && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y if CONFIG_ESPI_NPCX_NPCXN_V3 && CONFIG_ESPI_FLASH_CHANNEL
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NPCX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_ESPI_NPCX_NPCXN_V3`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_NPCXN_V3)、[`CONFIG_ESPI_FLASH_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_FLASH_CHANNEL)。

<a id="CONFIG_ESPI_NPCX_NPCKN_V1"></a>

## 85.15 `CONFIG_ESPI_NPCX_NPCKN_V1`

**提示（Prompt）**：新唐（Nuvoton）NPCX eSPI 第 1 版（Version 1）支持

**说明（Help）**

此选项为 NPCKn 变体（Variant）启用 eSPI 第 1 版（Version 1）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

<a id="CONFIG_ESPI_NPCX_NPCXN_V1"></a>

## 85.16 `CONFIG_ESPI_NPCX_NPCXN_V1`

**提示（Prompt）**：新唐（Nuvoton）NPCX eSPI 第 1 版（Version 1）支持

**说明（Help）**

此选项为 NPCXn 变体（Variant）启用 eSPI 第 1 版（Version 1）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

<a id="CONFIG_ESPI_NPCX_NPCXN_V2"></a>

## 85.17 `CONFIG_ESPI_NPCX_NPCXN_V2`

**提示（Prompt）**：新唐（Nuvoton）NPCX eSPI 第 2 版（Version 2）支持

**说明（Help）**

此选项为 NPCXn 变体（Variant）启用 eSPI 第 2 版（Version 2）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

<a id="CONFIG_ESPI_NPCX_NPCXN_V3"></a>

## 85.18 `CONFIG_ESPI_NPCX_NPCXN_V3`

**提示（Prompt）**：新唐（Nuvoton）NPCX eSPI 第 3 版（Version 3）支持

**说明（Help）**

此选项为 NPCXn 变体（Variant）启用 eSPI 第 3 版（Version 3）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

<a id="CONFIG_ESPI_NPCX_PERIPHERAL_ACPI_SHD_MEM_SIZE"></a>

## 85.19 `CONFIG_ESPI_NPCX_PERIPHERAL_ACPI_SHD_MEM_SIZE`

**提示（Prompt）**：NPCX 系列共享内存的主机 I/O 外设端口大小（Host I/O Peripheral Port Size）

**说明（Help）**

主机与嵌入式控制器（EC）通过共享内存区域（Shared Memory Region）通信、返回 ACPI 响应数据时使用的端口大小。NPCX EC 系列中，此选项的有效值为 `8`、`16`、`32`、`64`、`128`、`256`、`512`、`1024`、`2048` 或 `4096` 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESPI_NPCX || CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION) && CONFIG_ESPI
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NPCX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX)、[`CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_NPCX_PERIPHERAL_DEBUG_PORT_80_MULTI_BYTE"></a>

## 85.20 `CONFIG_ESPI_NPCX_PERIPHERAL_DEBUG_PORT_80_MULTI_BYTE`

**提示（Prompt）**：主机可在一次 eSPI 事务中写入 1/2/4 字节的端口 80（Port80）数据

**说明（Help）**

嵌入式控制器（EC）可接受主机在一次 eSPI 事务（Transaction）中写入的 1、2 或 4 字节端口 80（Port 80）数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESPI_NPCX_NPCXN_V2 || CONFIG_ESPI_NPCX_NPCXN_V3) && CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NPCX_NPCXN_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_NPCXN_V2)、[`CONFIG_ESPI_NPCX_NPCXN_V3`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_NPCXN_V3)、[`CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_NPCX_PERIPHERAL_DEBUG_PORT_80_RING_BUF_SIZE"></a>

## 85.21 `CONFIG_ESPI_NPCX_PERIPHERAL_DEBUG_PORT_80_RING_BUF_SIZE`

**提示（Prompt）**：调试端口 80 环形缓冲区大小（Debug Port80 Ring Buffer Size）

**说明（Help）**

端口 80 中断服务程序（ISR）用于存储主机自检码（POST Code）的环形缓冲区（Ring Buffer）大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_NPCX_PERIPHERAL_DEBUG_PORT_80_MULTI_BYTE && CONFIG_ESPI
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 主机可在一次 eSPI 事务中写入 1/2/4 字节的端口 80（Port80）数据

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NPCX_PERIPHERAL_DEBUG_PORT_80_MULTI_BYTE`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_PERIPHERAL_DEBUG_PORT_80_MULTI_BYTE)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_NPCX_PERIPHERAL_HOST_CMD_PARAM_SIZE"></a>

## 85.22 `CONFIG_ESPI_NPCX_PERIPHERAL_HOST_CMD_PARAM_SIZE`

**提示（Prompt）**：NPCX 系列 EC 主机命令的主机 I/O 外设端口大小（Host I/O Peripheral Port Size）

**说明（Help）**

主机与嵌入式控制器（EC）通过共享内存区域（Shared Memory Region）通信、返回主机命令参数数据时使用的端口大小。NPCX EC 系列中，此选项的有效值为 `8`、`16`、`32`、`64`、`128`、`256`、`512`、`1024`、`2048` 或 `4096` 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESPI_NPCX || CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD) && CONFIG_ESPI
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NPCX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX)、[`CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_NPCX_RESET_SLP_SX_VW_ON_ESPI_RST"></a>

## 85.23 `CONFIG_ESPI_NPCX_RESET_SLP_SX_VW_ON_ESPI_RST`

**提示（Prompt）**：`eSPI_RST` 置位时复位 `SLP_Sx` 虚拟线（Virtual Wires）

**说明（Help）**

全局复位（Global Reset）使 `eSPI_Reset` 生效时，会自动复位 `SLP_S3`、`SLP_S4` 和 `SLP_S5` 虚拟线（Virtual Wires）。如果平台实现了进入 Deep-Sx 的流程，则不要启用此配置，因为嵌入式控制器（EC）需要按请求保持这些引脚的状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_NPCX && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NPCX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_NPCX_SUPP_VW_GPIO"></a>

## 85.24 `CONFIG_ESPI_NPCX_SUPP_VW_GPIO`

**提示（Prompt）**：指示 eSPI 硬件支持虚拟线 GPIO（Virtual Wire GPIOs）

**说明（Help）**

当 NPCX 系列的 eSPI 模块支持虚拟线 GPIO（Virtual Wire GPIOs）时，选中此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_NPCX && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y if CONFIG_ESPI_NPCX_NPCXN_V2 || CONFIG_ESPI_NPCX_NPCXN_V3
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NPCX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_ESPI_NPCX_NPCXN_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_NPCXN_V2)、[`CONFIG_ESPI_NPCX_NPCXN_V3`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_NPCXN_V3)。

<a id="CONFIG_ESPI_NPCX_VWIRE_ENABLE_SEND_CHECK"></a>

## 85.25 `CONFIG_ESPI_NPCX_VWIRE_ENABLE_SEND_CHECK`

**提示（Prompt）**：在线路位改变后检查主机是否已读取该值

**说明（Help）**

此选项启用一项功能：虚拟线（Virtual Wire）数据变化后，检查主机是否已读取该值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_NPCX_WIRE_SEND_TIMEOUT_US"></a>

## 85.26 `CONFIG_ESPI_NPCX_WIRE_SEND_TIMEOUT_US`

**提示（Prompt）**：eSPI 虚拟线发送超时计数（Virtual Wire Send Timeout Count）

**说明（Help）**

发送 eSPI 虚拟线（Virtual Wire）信号后检查状态的时间，单位为微秒（µs）。

> 译注：原提示使用“count”，帮助正文使用“times”，但同时明确单位为微秒；配置标识符也以 `_TIMEOUT_US` 结尾。此处保留该时间单位，不将其解释为无单位的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_NPCX_i8042_KBC_AUX_VWIRE_IRQ_WORKAROUND"></a>

## 85.27 `CONFIG_ESPI_NPCX_i8042_KBC_AUX_VWIRE_IRQ_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项启用一种规避措施（Workaround）：当固件检测到输出缓冲区（Output Buffer）为空后立即写入数据时，防止丢失 IRQ1/IRQ12。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_NPCX9M7FB
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_SOC_NPCX9M7FB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NPCX9M7FB)。

<a id="CONFIG_ESPI_NXP"></a>

## 85.28 `CONFIG_ESPI_NXP`

**提示（Prompt）**：NXP eSPI 目标驱动（Target Driver）

**说明（Help）**

启用 NXP SoC 的 eSPI 目标驱动（Target Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ESPI_ENABLED && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ESPI_TARGET
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/espi/Kconfig.nxp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.nxp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_ESPI_TARGET`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TARGET)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ESPI_NXP_TIMEOUT_MS"></a>

## 85.29 `CONFIG_ESPI_NXP_TIMEOUT_MS`

**提示（Prompt）**：eSPI 操作超时时间（Operation Timeout），以毫秒为单位

**说明（Help）**

带外接收（OOB Receive）等同步 eSPI 操作（Synchronous Operation）的超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_NXP && CONFIG_ESPI
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`drivers/espi/Kconfig.nxp:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.nxp#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → NXP eSPI 目标驱动（Target Driver）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NXP`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NXP)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_OOB_BUFFER_SIZE"></a>

## 85.30 `CONFIG_ESPI_OOB_BUFFER_SIZE`

**提示（Prompt）**：eSPI 带外通道缓冲区大小（OOB Channel Buffer Size），以字节为单位

**说明（Help）**

默认使用最小 RAM 缓冲区（Buffer）大小，但允许应用程序覆盖该值。带外传输（OOB）的最大有效载荷（Payload）为 73 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_OOB_CHANNEL && (CONFIG_ESPI_XEC || CONFIG_ESPI_XEC_V2) && CONFIG_ESPI
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_OOB_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_OOB_CHANNEL)、[`CONFIG_ESPI_XEC`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_OOB_CHANNEL"></a>

## 85.31 `CONFIG_ESPI_OOB_CHANNEL`

**提示（Prompt）**：eSPI 带外通道（Out-of-Band Channel，OOB）

**说明（Help）**

eSPI 控制器（Controller）支持带外通道（OOB Channel）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_OOB_CHANNEL_RX_ASYNC"></a>

## 85.32 `CONFIG_ESPI_OOB_CHANNEL_RX_ASYNC`

**提示（Prompt）**：处理主机发起的带外通信（Host-Initiated OOB Traffic）

**说明（Help）**

启用对主机发起的带外通信（Host-Initiated OOB Traffic）的异步处理（Asynchronous Handling）。否则，假定 OOB 通信始终由客户端（Client）发起。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_OOB_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_OOB_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_OOB_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_8042_FAST_KBC_PORT92"></a>

## 85.33 `CONFIG_ESPI_PERIPHERAL_8042_FAST_KBC_PORT92`

**提示（Prompt）**：主机 I/O 92h 上的 8042 键盘快速替代 GATE A20 控制支持

**说明（Help）**

8042 键盘支持通过 I/O 端口 `92h` 执行快速、替代的 GATE A20 控制（Fast Alternate GATE A20 Control）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_8042_KBC"></a>

## 85.34 `CONFIG_ESPI_PERIPHERAL_8042_KBC`

**提示（Prompt）**：8042 键盘控制器（KBC）外设

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel）启用 8042 键盘控制器（Keyboard Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_ACPI_EC_IBF_EVT_DATA"></a>

## 85.35 `CONFIG_ESPI_PERIPHERAL_ACPI_EC_IBF_EVT_DATA`

**提示（Prompt）**：在输入缓冲区满中断服务程序（IBF ISR）中读取 ACPI EC 事件数据

**说明（Help）**

启用在 ACPI EC 输入缓冲区满中断服务程序（IBF ISR）中读取事件数据（Event Data）的功能。这适用于应用程序期望 IBF ISR 读取数据并传递给回调（Callback）的操作系统（OS）环境。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION"></a>

## 85.36 `CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`

**提示（Prompt）**：主机外设支持共享内存区域（Shared Memory Region）

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel）启用共享内存区域（Shared Memory Region），用于访问 ACPI 响应数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION_PORT_NUM"></a>

## 85.37 `CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION_PORT_NUM`

**提示（Prompt）**：共享内存区域的主机 I/O 外设端口号（Host I/O Peripheral Port Number）

**说明（Help）**

主机与嵌入式控制器（EC）通过共享内存区域（Shared Memory Region）通信、访问 ACPI 响应数据时使用的端口号。请确保主机代码配置为使用该端口访问 ACPI 响应数据，并确保所选端口号不与现有端口冲突。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION && CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**默认值（Defaults）**

```text
0x0900
```

**定义位置（Location）**：[`drivers/espi/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 主机外设支持共享内存区域（Shared Memory Region）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION)、[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_CHANNEL"></a>

## 85.38 `CONFIG_ESPI_PERIPHERAL_CHANNEL`

**提示（Prompt）**：eSPI 外设通道（Peripheral Channel）

**说明（Help）**

eSPI 控制器（Controller）支持外设通道（Peripheral Channel）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE"></a>

## 85.39 `CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE`

**提示（Prompt）**：主机外设支持自定义操作码（Customized Opcode）

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel），启用为 Chromebook 等特定平台定制的操作码（Opcode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80"></a>

## 85.40 `CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80`

**提示（Prompt）**：调试端口 80 外设（Debug Port 80 Peripheral）

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel）启用调试端口 80（Debug Port 80）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD"></a>

## 85.41 `CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD`

**提示（Prompt）**：主机外设支持 EC 主机命令子系统（EC Host Command Subsystem）

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel）启用嵌入式控制器（Embedded Controller，EC）主机命令子系统（Host Command Subsystem）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_HOST_CMD_DATA_PORT_NUM"></a>

## 85.42 `CONFIG_ESPI_PERIPHERAL_HOST_CMD_DATA_PORT_NUM`

**提示（Prompt）**：EC 主机命令数据的主机 I/O 外设端口号（Host I/O Peripheral Port Number）

**说明（Help）**

主机与嵌入式控制器（EC）通过 eSPI 外设通道（Peripheral Channel）通信、发送 EC 主机命令数据及其结果时使用的端口号。请确保主机代码配置为使用该端口访问主机命令数据和结果，并确保所选端口号不与现有端口冲突。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD && CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**默认值（Defaults）**

```text
0x0200
```

**定义位置（Location）**：[`drivers/espi/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD)、[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_HOST_CMD_PARAM_PORT_NUM"></a>

## 85.43 `CONFIG_ESPI_PERIPHERAL_HOST_CMD_PARAM_PORT_NUM`

**提示（Prompt）**：EC 主机命令参数的主机 I/O 外设端口号（Host I/O Peripheral Port Number）

**说明（Help）**

主机与嵌入式控制器（EC）通过 eSPI 外设通道（Peripheral Channel）通信、访问主机命令请求和响应数据时使用的端口号。请确保主机代码配置为使用该端口访问这些数据包，并确保所选端口号不与现有端口冲突。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD && CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**默认值（Defaults）**

```text
0x0800
```

**定义位置（Location）**：[`drivers/espi/Kconfig:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD)、[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_HOST_IO"></a>

## 85.44 `CONFIG_ESPI_PERIPHERAL_HOST_IO`

**提示（Prompt）**：主机 I/O 外设（Host I/O Peripheral）

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel）启用 ACPI 主机 I/O（Host I/O）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT"></a>

## 85.45 `CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT`

**提示（Prompt）**：主机 I/O 外设私有通道（Private Channel）

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel），为私有通道（Private Channel）启用 ACPI 主机 I/O。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT2"></a>

## 85.46 `CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT2`

**提示（Prompt）**：主机 I/O 外设私有通道 2（Private Channel 2）

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel），为私有通道 2（Private Channel 2）启用 ACPI 主机 I/O。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT2_PORT_NUM"></a>

## 85.47 `CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT2_PORT_NUM`

**提示（Prompt）**：主机 I/O 外设私有通道 2（Private Channel 2）

**说明（Help）**

主机与嵌入式控制器（EC）通过私有通道 2（Private Channel 2）通信时使用的端口号。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT2 && CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**默认值（Defaults）**

```text
0x0068
```

**定义位置（Location）**：[`drivers/espi/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT2)、[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT3"></a>

## 85.48 `CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT3`

**提示（Prompt）**：主机 I/O 外设私有通道 3（Private Channel 3）

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel），为私有通道 3（Private Channel 3）启用 ACPI 主机 I/O。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT3_PORT_NUM"></a>

## 85.49 `CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT3_PORT_NUM`

**提示（Prompt）**：主机 I/O 外设私有通道 3（Private Channel 3）

**说明（Help）**

主机与嵌入式控制器（EC）通过私有通道 3（Private Channel 3）通信时使用的端口号。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT3 && CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**默认值（Defaults）**

```text
0x0070
```

**定义位置（Location）**：[`drivers/espi/Kconfig:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT3`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT3)、[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT_PORT_NUM"></a>

## 85.50 `CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT_PORT_NUM`

**提示（Prompt）**：主机 I/O 外设私有通道（Private Channel）

**说明（Help）**

主机与嵌入式控制器（EC）通过私有通道（Private Channel）通信时使用的端口号。请确保主机代码配置为使用同一端口，并确保所选端口号不与现有端口（例如 80、92、62）冲突。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT && CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**默认值（Defaults）**

```text
0x06A00000
```

**定义位置（Location）**：[`drivers/espi/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_HOST_IO_PVT)、[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_KBC_IBF_EVT_DATA"></a>

## 85.51 `CONFIG_ESPI_PERIPHERAL_KBC_IBF_EVT_DATA`

**提示（Prompt）**：输入缓冲区满（IBF）情况下的 KBC 事件数据格式（Event Data Format）

**说明（Help）**

启用 `espi_evt_data_kbc` 格式，用于编码 KBC 输入缓冲区满中断服务程序（IBF ISR）中的事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_XEC_V2 && CONFIG_ESPI_PERIPHERAL_8042_KBC && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI_PERIPHERAL_8042_KBC`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_8042_KBC)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_KBC_OBE_CBK"></a>

## 85.52 `CONFIG_ESPI_PERIPHERAL_KBC_OBE_CBK`

**提示（Prompt）**：KBC 输出缓冲区空回调（OBE Callback）

**说明（Help）**

启用从输出缓冲区空中断服务程序（OBE ISR）调用 KBC OBE 回调（Callback）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_XEC_V2 && CONFIG_ESPI_PERIPHERAL_8042_KBC && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI_PERIPHERAL_8042_KBC`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_8042_KBC)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_UART"></a>

## 85.53 `CONFIG_ESPI_PERIPHERAL_UART`

**提示（Prompt）**：通用异步收发器（UART）外设

**说明（Help）**

通过 eSPI 外设通道（Peripheral Channel）启用 UART。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_UART_SOC_MAPPING"></a>

## 85.54 `CONFIG_ESPI_PERIPHERAL_UART_SOC_MAPPING`

**提示（Prompt）**：作为逻辑 eSPI UART（Logical eSPI UART）公开的 SoC 端口

**说明（Help）**

告知驱动：应将主机经 eSPI 发送的 UART 通信数据转发到哪个 SoC UART。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_UART && (CONFIG_ESPI_XEC || CONFIG_ESPI_XEC_V2) && CONFIG_ESPI
```

**默认值（Defaults）**

```text
2 if CONFIG_SOC_SERIES_MEC15XX
1 if !CONFIG_SOC_SERIES_MEC15XX
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_UART`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_UART)、[`CONFIG_ESPI_XEC`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_SOC_SERIES_MEC15XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC15XX)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_ACPI_EC2"></a>

## 85.55 `CONFIG_ESPI_PERIPHERAL_XEC_ACPI_EC2`

**提示（Prompt）**：通过 eSPI 提供 SoC ACPI EC 2

**说明（Help）**

启用 ACPI EC2 接口，使其可经由 eSPI 外设通道（Peripheral Channel）上的主机 I/O（Host I/O）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_ACPI_EC3"></a>

## 85.56 `CONFIG_ESPI_PERIPHERAL_XEC_ACPI_EC3`

**提示（Prompt）**：通过 eSPI 提供 SoC ACPI EC 3

**说明（Help）**

启用 ACPI EC3 接口，使其可经由 eSPI 外设通道（Peripheral Channel）上的主机 I/O（Host I/O）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_ACPI_EC4"></a>

## 85.57 `CONFIG_ESPI_PERIPHERAL_XEC_ACPI_EC4`

**提示（Prompt）**：通过 eSPI 提供 SoC ACPI EC 4

**说明（Help）**

启用 ACPI EC4 接口，使其可经由 eSPI 外设通道（Peripheral Channel）上的主机 I/O（Host I/O）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_ACPI_PM1"></a>

## 85.58 `CONFIG_ESPI_PERIPHERAL_XEC_ACPI_PM1`

**提示（Prompt）**：通过 eSPI 提供 SoC ACPI PM1

**说明（Help）**

启用 ACPI PM1 接口，使其可经由 eSPI 外设通道（Peripheral Channel）上的主机 I/O（Host I/O）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_EMI0"></a>

## 85.59 `CONFIG_ESPI_PERIPHERAL_XEC_EMI0`

**提示（Prompt）**：通过 eSPI 提供 SoC EMI 0

**说明（Help）**

启用 EMI 0 接口，使其可经由 eSPI 外设通道（Peripheral Channel）上的主机 I/O（Host I/O）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_EMI1"></a>

## 85.60 `CONFIG_ESPI_PERIPHERAL_XEC_EMI1`

**提示（Prompt）**：通过 eSPI 提供 SoC EMI 1

**说明（Help）**

启用 EMI 1 接口，使其可经由 eSPI 外设通道（Peripheral Channel）上的主机 I/O（Host I/O）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_EMI2"></a>

## 85.61 `CONFIG_ESPI_PERIPHERAL_XEC_EMI2`

**提示（Prompt）**：通过 eSPI 提供 SoC EMI 2

**说明（Help）**

启用 EMI 2 接口，使其可经由 eSPI 外设通道（Peripheral Channel）上的主机 I/O（Host I/O）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX"></a>

## 85.62 `CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX`

**提示（Prompt）**：通过 eSPI 提供 SoC 邮箱（Mailbox）

**说明（Help）**

启用一个 32 字节邮箱接口（Mailbox Interface），使其可经由 eSPI 外设通道（Peripheral Channel）上的主机 I/O（Host I/O）访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX_PORT_NUM"></a>

## 85.63 `CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX_PORT_NUM`

**提示（Prompt）**：XEC 邮箱的主机 I/O 外设端口（Host I/O Peripheral Port）

**说明（Help）**

XEC 邮箱基地址寄存器（Mailbox BAR）所映射到的主机 I/O（Host I/O）端口。确保该值不与其他主机 I/O 外设冲突。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX && CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**默认值（Defaults）**

```text
0x0360
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 通过 eSPI 提供 SoC 邮箱（Mailbox）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX)、[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX_SIRQ_SLOT"></a>

## 85.64 `CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX_SIRQ_SLOT`

**提示（Prompt）**：XEC 邮箱外设的串行中断槽位号（Serial-IRQ Slot Number）

**说明（Help）**

用于向主机发送非系统管理中断（Non-SMI Interrupt）的串行中断槽位号（Serial-IRQ Slot Number）。范围为 `0` 至 `255`，其中 `255` 表示禁用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX && CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 通过 eSPI 提供 SoC 邮箱（Mailbox）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX)、[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX_SMI_SIRQ_SLOT"></a>

## 85.65 `CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX_SMI_SIRQ_SLOT`

**提示（Prompt）**：XEC 邮箱外设的系统管理中断（SMI）串行中断槽位号（Serial-IRQ Slot Number）

**说明（Help）**

用于向主机发送系统管理中断（SMI）的串行中断槽位号（Serial-IRQ Slot Number）。范围为 `0` 至 `255`，其中 `255` 表示禁用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX && CONFIG_ESPI_PERIPHERAL_CHANNEL && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 通过 eSPI 提供 SoC 邮箱（Mailbox）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_XEC_MAILBOX)、[`CONFIG_ESPI_PERIPHERAL_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CHANNEL)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_RTS5912"></a>

## 85.66 `CONFIG_ESPI_RTS5912`

**提示（Prompt）**：Realtek RTS5912 eSPI 驱动

**说明（Help）**

启用瑞昱（Realtek）RTS5912 eSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_ESPI_ENABLED && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.rts5912:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.rts5912#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_RTS5912_PRESERVED_DATA_HOOKS"></a>

## 85.67 `CONFIG_ESPI_RTS5912_PRESERVED_DATA_HOOKS`

**提示（Prompt）**：保存和恢复内部状态的函数（Save and Restore Internal State）

**说明（Help）**

RTS5912 eSPI 驱动的一部分状态由软件缓存，无法根据硬件寄存器推导。当驱动用于多镜像固件产品（Multi-Image Firmware Product，例如 A/B、RO/RW），且镜像之间的跳转未执行完整硬件复位时，缓存会被清除，不再反映硬件状态。此选项启用一对驱动专用函数，可在软重启（Soft Reboot）之前导出需要保留的状态数据，之后再恢复。调用方负责在这期间将状态数据保存在安全的位置，例如电池备份 RAM（BBRAM）、非易失 RAM（NVRAM）等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_RTS5912 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.rts5912:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.rts5912#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → Realtek RTS5912 eSPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_RTS5912`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_RTS5912)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_TAF"></a>

## 85.68 `CONFIG_ESPI_TAF`

**提示（Prompt）**：eSPI 目标附接闪存（TAF）驱动

**说明（Help）**

启用目标附接闪存（Target Attached Flash，TAF）eSPI 驱动。TAF 依赖 eSPI 驱动和闪存通道（Flash Channel）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_FLASH_CHANNEL && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_FLASH_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_FLASH_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_TAF_ACCESS_MODE_CHOICE"></a>

## 85.69 `CONFIG_ESPI_TAF_ACCESS_MODE_CHOICE`

**提示（Prompt）**：eSPI TAF 读取访问模式（Read Access Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**默认值（Defaults）**

```text
CONFIG_ESPI_TAF_AUTO_MODE
```

**可选项（Choices）**

```text
CONFIG_ESPI_TAF_AUTO_MODE
CONFIG_ESPI_TAF_MANUAL_MODE
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_ESPI_TAF_AUTO_MODE`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF_AUTO_MODE)、[`CONFIG_ESPI_TAF_MANUAL_MODE`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF_MANUAL_MODE)。

<a id="CONFIG_ESPI_TAF_AUTO_MODE"></a>

## 85.70 `CONFIG_ESPI_TAF_AUTO_MODE`

**提示（Prompt）**：eSPI TAF 自动模式（Automatic Mode）

**说明（Help）**

此设置使 eSPI TAF 读取使用自动模式（Automatic Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPI_TAF_ACCESS_MODE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → eSPI TAF 读取访问模式（Read Access Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_TAF_ACCESS_MODE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF_ACCESS_MODE_CHOICE)。

<a id="CONFIG_ESPI_TAF_INIT_PRIORITY"></a>

## 85.71 `CONFIG_ESPI_TAF_INIT_PRIORITY`

**提示（Prompt）**：eSPI TAF 驱动初始化优先级（Initialization Priority）

**说明（Help）**

eSPI TAF 驱动的初始化优先级（Initialization Priority）。TAF 驱动必须在 eSPI 驱动之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_TAF && CONFIG_ESPI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/espi/Kconfig:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → eSPI 目标附接闪存（TAF）驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_TAF`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_TAF_MANUAL_MODE"></a>

## 85.72 `CONFIG_ESPI_TAF_MANUAL_MODE`

**提示（Prompt）**：eSPI TAF 手动模式（Manual Mode）

**说明（Help）**

此设置使 eSPI TAF 读取使用手动模式（Manual Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPI_TAF_ACCESS_MODE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → eSPI TAF 读取访问模式（Read Access Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_TAF_ACCESS_MODE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF_ACCESS_MODE_CHOICE)。

<a id="CONFIG_ESPI_TAF_NPCX"></a>

## 85.73 `CONFIG_ESPI_TAF_NPCX`

**提示（Prompt）**：新唐（Nuvoton）NPCX 嵌入式控制器（Embedded Controller，EC）eSPI TAF 驱动

**说明（Help）**

此选项为 NPCX4/NPCK3 系列处理器启用 Intel 增强型串行外设接口目标附接闪存（Enhanced Serial Peripheral Interface Target Attached Flash，eSPI TAF）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESPI_NPCX_NPCXN_V3 || CONFIG_ESPI_NPCX_NPCKN_V1) && CONFIG_FLASH && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NPCX_NPCXN_V3`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_NPCXN_V3)、[`CONFIG_ESPI_NPCX_NPCKN_V1`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NPCX_NPCKN_V1)、[`CONFIG_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_TAF_NPCX_RPMC_SUPPORT"></a>

## 85.74 `CONFIG_ESPI_TAF_NPCX_RPMC_SUPPORT`

**提示（Prompt）**：eSPI TAF RPMC 支持

**说明（Help）**

此选项启用 eSPI TAF RPMC 请求处理程序（Request Handler）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_TAF_NPCX && CONFIG_ESPI
```

**主动选择（Selects）**

```text
CONFIG_FLASH_EX_OP_ENABLED
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_TAF_NPCX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF_NPCX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_FLASH_EX_OP_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_EX_OP_ENABLED)。

<a id="CONFIG_ESPI_TAF_NPCX_STS_AWAIT_TIMEOUT"></a>

## 85.75 `CONFIG_ESPI_TAF_NPCX_STS_AWAIT_TIMEOUT`

**提示（Prompt）**：等待自动读取状态（Automatic Read Status）的超时时间，以微秒为单位

**说明（Help）**

此选项指定检查自动读取状态（Automatic Read Status）时的超时时间，以微秒（µs）为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_TAF_NPCX && CONFIG_ESPI
```

**默认值（Defaults）**

```text
20000
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_TAF_NPCX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF_NPCX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_TAF_NXP"></a>

## 85.76 `CONFIG_ESPI_TAF_NXP`

**提示（Prompt）**：NXP eSPI 目标附接闪存（Target Attached Flash，TAF）驱动

**说明（Help）**

启用 NXP eSPI 目标附接闪存（Target Attached Flash，TAF）驱动。这是一个绑定到 `espi_saf_driver_api` 的独立设备。它共享父级 `nxp,espi` 控制器的寄存器块（Register Block）和中断（Interrupt）；父驱动将主机闪存请求转发给本驱动，本驱动针对本地闪存设备处理请求，并向主机返回完成通知（Completion）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_NXP && DT_HAS_NXP_ESPI_TAF_ENABLED && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/espi/Kconfig.nxp:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.nxp#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → NXP eSPI 目标驱动（Target Driver）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_NXP`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NXP)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH)。

<a id="CONFIG_ESPI_TAF_PR_NUM"></a>

## 85.77 `CONFIG_ESPI_TAF_PR_NUM`

**提示（Prompt）**：保护区域设置组数（Protection Region Settings Sets）

**说明（Help）**

此大小表示从设备附接闪存（Slave Attached Flash）保护区域（Protection Region）的组数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_TAF_TX_AVAIL_CHECK_TIME"></a>

## 85.78 `CONFIG_ESPI_TAF_TX_AVAIL_CHECK_TIME`

**提示（Prompt）**：闪存发送可用状态检查间隔（Flash TX Available Check Time），以微秒为单位

**说明（Help）**

此选项设置检查主机是否已发送 `GET_FLASH_C` 命令来取回结果的时间间隔，以微秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_TAF_NPCX && CONFIG_ESPI
```

**默认值（Defaults）**

```text
1000000
```

**定义位置（Location）**：[`drivers/espi/Kconfig.npcx:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.npcx#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_TAF_NPCX`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_TAF_NPCX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_TAF_XEC"></a>

## 85.79 `CONFIG_ESPI_TAF_XEC`

**提示（Prompt）**：Microchip XEC eSPI TAF 驱动

**说明（Help）**

启用 MEC15xx 系列的 Microchip XEC TAF eSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_MEC15XX && DT_HAS_MICROCHIP_XEC_ESPI_SAF_ENABLED && (CONFIG_ESPI_XEC || CONFIG_ESPI_XEC_V2) && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MEC15XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_ESPI_XEC`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_TAF_XEC_V2"></a>

## 85.80 `CONFIG_ESPI_TAF_XEC_V2`

**提示（Prompt）**：Microchip XEC eSPI TAF V2 驱动

**说明（Help）**

启用 MEC172x 系列的 Microchip XEC TAF eSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_ESPI_SAF_V2_ENABLED && (CONFIG_SOC_SERIES_MEC172X || CONFIG_SOC_SERIES_MEC174X || CONFIG_SOC_SERIES_MEC175X || CONFIG_SOC_SERIES_MEC165XB) && (CONFIG_ESPI_XEC || CONFIG_ESPI_XEC_V2) && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MEC172X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_SERIES_MEC174X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC174X)、[`CONFIG_SOC_SERIES_MEC175X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC175X)、[`CONFIG_SOC_SERIES_MEC165XB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC165XB)、[`CONFIG_ESPI_XEC`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC)、[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_TARGET"></a>

## 85.81 `CONFIG_ESPI_TARGET`

**提示（Prompt）**：eSPI 目标驱动（Target Driver）

**说明（Help）**

启用目标模式（Target Mode）的 eSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ESPI_NXP
```

**定义位置（Location）**：[`drivers/espi/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_ESPI_NXP`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_NXP)。

<a id="CONFIG_ESPI_VWIRE_CHANNEL"></a>

## 85.82 `CONFIG_ESPI_VWIRE_CHANNEL`

**提示（Prompt）**：eSPI 虚拟线通道（Virtual Wire Channel）

**说明（Help）**

eSPI 控制器（Controller）支持虚拟线通道（Virtual Wire Channel）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_VWIRE_VALID_BIT_CHECK"></a>

## 85.83 `CONFIG_ESPI_VWIRE_VALID_BIT_CHECK`

**提示（Prompt）**：eSPI 虚拟线有效位检查（Virtual Wire Valid Bit Check）

**说明（Help）**

启用对 eSPI 虚拟线有效位（Virtual Wire Valid Bit）的检查。未设置此配置时，将新值按先前保留的有效值处理，并返回收到的虚拟线电平（Virtual Wire Level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_VWIRE_CHANNEL && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/espi/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → eSPI 虚拟线通道（Virtual Wire Channel）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_VWIRE_CHANNEL`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_VWIRE_CHANNEL)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_XEC"></a>

## 85.84 `CONFIG_ESPI_XEC`

**提示（Prompt）**：Microchip XEC eSPI 驱动

**说明（Help）**

启用 MEC15xx 系列的 Microchip XEC eSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_ESPI_ENABLED && CONFIG_SOC_SERIES_MEC15XX && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MEC15XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_ESPI_XEC_P80_MULTIBYTE"></a>

## 85.85 `CONFIG_ESPI_XEC_P80_MULTIBYTE`

**提示（Prompt）**：主机可在一次 eSPI 事务中写入 1/2/4 字节的端口 80（Port80）数据

**说明（Help）**

嵌入式控制器（EC）可接受主机在一次 eSPI 事务（Transaction）中写入的 1、2 或 4 字节端口 80（Port 80）数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_XEC_V2 && CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80 && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_DEBUG_PORT_80)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_XEC_PERIPHERAL_ACPI_SHD_MEM_SIZE"></a>

## 85.86 `CONFIG_ESPI_XEC_PERIPHERAL_ACPI_SHD_MEM_SIZE`

**提示（Prompt）**：MEC172X 系列共享内存的主机 I/O 外设端口大小（Host I/O Peripheral Port Size）

**说明（Help）**

主机与嵌入式控制器（EC）通过共享内存区域（Shared Memory Region）通信、返回 ACPI 响应数据时使用的端口大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESPI_XEC_V2 || CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION) && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_XEC_PERIPHERAL_HOST_CMD_PARAM_SIZE"></a>

## 85.87 `CONFIG_ESPI_XEC_PERIPHERAL_HOST_CMD_PARAM_SIZE`

**提示（Prompt）**：MEC172X 系列 EC 主机命令的主机 I/O 外设端口大小（Host I/O Peripheral Port Size）

**说明（Help）**

主机与嵌入式控制器（EC）通过共享内存区域（Shared Memory Region）通信、返回主机命令参数数据时使用的端口大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESPI_XEC_V2 || CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD) && CONFIG_ESPI_XEC_V2 && CONFIG_ESPI
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_XEC_V2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_XEC_V2)、[`CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)。

<a id="CONFIG_ESPI_XEC_V2"></a>

## 85.88 `CONFIG_ESPI_XEC_V2`

**提示（Prompt）**：Microchip XEC eSPI V2 驱动

**说明（Help）**

启用 MEC172x/4x/5x 系列的 Microchip XEC eSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_ESPI_V2_ENABLED && !CONFIG_SOC_SERIES_MEC15XX && CONFIG_ESPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/espi/Kconfig.xec:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.xec#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MEC15XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_1024"></a>

## 85.89 `CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_1024`

**提示（Prompt）**：1024

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → ACPI 共享内存区域（Shared Memory Region）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_128"></a>

## 85.90 `CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_128`

**提示（Prompt）**：128

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → ACPI 共享内存区域（Shared Memory Region）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_16"></a>

## 85.91 `CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_16`

**提示（Prompt）**：16

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → ACPI 共享内存区域（Shared Memory Region）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_2048"></a>

## 85.92 `CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_2048`

**提示（Prompt）**：2048

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → ACPI 共享内存区域（Shared Memory Region）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_256"></a>

## 85.93 `CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_256`

**提示（Prompt）**：256。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → ACPI 共享内存区域（Shared Memory Region）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_32"></a>

## 85.94 `CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_32`

**提示（Prompt）**：32

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → ACPI 共享内存区域（Shared Memory Region）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_512"></a>

## 85.95 `CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_512`

**提示（Prompt）**：512

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → ACPI 共享内存区域（Shared Memory Region）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_64"></a>

## 85.96 `CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_64`

**提示（Prompt）**：64

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → ACPI 共享内存区域（Shared Memory Region）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE"></a>

## 85.97 `CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_CHOICE`

**提示（Prompt）**：ACPI 共享内存区域（Shared Memory Region）的 H2RAM 空间

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION && CONFIG_ESPI_IT8XXX2 && CONFIG_ESPI
```

**默认值（Defaults）**

```text
CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_256
```

**可选项（Choices）**

```text
CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_16
CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_32
CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_64
CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_128
CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_256
CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_512
CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_1024
CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_2048
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION)、[`CONFIG_ESPI_IT8XXX2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_IT8XXX2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_256`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_256)、[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_16`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_16)、[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_32`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_32)、[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_64`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_64)、[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_128`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_128)、[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_512`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_512)、[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_1024`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_1024)、[`CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_2048`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_ACPI_SHM_SIZE_2048)。

<a id="CONFIG_IT8XXX2_H2RAM_HC_SIZE_1024"></a>

## 85.98 `CONFIG_IT8XXX2_H2RAM_HC_SIZE_1024`

**提示（Prompt）**：1024

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → EC 主机命令（Host Command）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_HC_SIZE_128"></a>

## 85.99 `CONFIG_IT8XXX2_H2RAM_HC_SIZE_128`

**提示（Prompt）**：128

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → EC 主机命令（Host Command）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_HC_SIZE_16"></a>

## 85.100 `CONFIG_IT8XXX2_H2RAM_HC_SIZE_16`

**提示（Prompt）**：16

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → EC 主机命令（Host Command）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P084_drivers_entropy_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P086_drivers_espi_配置项参考_2.md)
