---
id: learning.zephyr-docs.kconfig-reference.page-134
title: "`drivers/pcie`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第134章\_`drivers/pcie`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/pcie` 的 14 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PCIE"></a>

## 134.1 `CONFIG_PCIE`

**提示（Prompt）**：新 PCI/PCIe 根复合体（Root Complex）支持

**说明（Help）**

此选项启用新 PCI(e) 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_ELKHART_LAKE
CONFIG_SOC_NOVA_LAKE
CONFIG_SOC_WILDCAT_LAKE
CONFIG_SOC_ALDER_LAKE
CONFIG_SOC_RAPTOR_LAKE
CONFIG_SOC_APOLLO_LAKE
CONFIG_SOC_PANTHER_LAKE
CONFIG_CAN_KVASER_PCI
CONFIG_NVME
CONFIG_ETH_E1000
CONFIG_ETH_IVSHMEM
CONFIG_SMBUS_INTEL_PCH
CONFIG_VIRTIO_PCI
```

**定义位置（Location）**：[`drivers/pcie/host/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ELKHART_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ELKHART_LAKE)、[`CONFIG_SOC_NOVA_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NOVA_LAKE)、[`CONFIG_SOC_WILDCAT_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_WILDCAT_LAKE)、[`CONFIG_SOC_ALDER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ALDER_LAKE)、[`CONFIG_SOC_RAPTOR_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RAPTOR_LAKE)、[`CONFIG_SOC_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO_LAKE)、[`CONFIG_SOC_PANTHER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PANTHER_LAKE)、[`CONFIG_CAN_KVASER_PCI`](P060_drivers_can_配置项参考.md#CONFIG_CAN_KVASER_PCI)、[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_ETH_E1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_E1000)、[`CONFIG_ETH_IVSHMEM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_IVSHMEM)、[`CONFIG_SMBUS_INTEL_PCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SMBUS_INTEL_PCH)、[`CONFIG_VIRTIO_PCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO_PCI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ELKHART_LAKE`、`CONFIG_SOC_NOVA_LAKE`、`CONFIG_SOC_WILDCAT_LAKE`、`CONFIG_SOC_ALDER_LAKE`、`CONFIG_SOC_RAPTOR_LAKE`、`CONFIG_SOC_APOLLO_LAKE`、`CONFIG_SOC_PANTHER_LAKE`。

<a id="CONFIG_PCIE_BRCMSTB"></a>

## 134.2 `CONFIG_PCIE_BRCMSTB`

**提示（Prompt）**：Broadcom 机顶盒（Set-top Box）SoC PCIe 驱动

**说明（Help）**

启用 Broadcom 机顶盒 SoC PCIe 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_BRCMSTB_PCIE_ENABLED && CONFIG_PCIE_CONTROLLER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pcie/controller/Kconfig.brcmstb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/controller/Kconfig.brcmstb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_CONTROLLER`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE_CONTROLLER)。

<a id="CONFIG_PCIE_CONTROLLER"></a>

## 134.3 `CONFIG_PCIE_CONTROLLER`

**提示（Prompt）**：PCIe 控制器管理（Controller Management）

**说明（Help）**

添加 PCIe 控制器管理支持，适用于该管理未像 x86 平台那样由系统固件处理的情况。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pcie/host/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持

<a id="CONFIG_PCIE_ECAM"></a>

## 134.4 `CONFIG_PCIE_ECAM`

**提示（Prompt）**：PCIe 增强配置地址映射（ECAM）控制器支持

**说明（Help）**

添加使用增强配置地址映射（Enhanced Configuration Address Mapping，ECAM）配置的 PCIe 控制器支持，允许将所有出站 I/O 和内存事务层数据包（MEM TLP）从内存空间映射到 PCIe 配置空间中任意 256 MB 区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PCI_HOST_ECAM_GENERIC_ENABLED && CONFIG_PCIE_CONTROLLER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pcie/controller/Kconfig.ecam:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/controller/Kconfig.ecam#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_PCIE_CONTROLLER`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE_CONTROLLER)。

<a id="CONFIG_PCIE_ENDPOINT"></a>

## 134.5 `CONFIG_PCIE_ENDPOINT`

**提示（Prompt）**：PCIe 端点（Endpoint）支持

**说明（Help）**

此选项启用 PCIe 端点支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_DMA_IPROC_PAX
CONFIG_DMA_IPROC_PAX_V2
```

**定义位置（Location）**：[`drivers/pcie/endpoint/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/endpoint/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DMA_IPROC_PAX`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_IPROC_PAX)、[`CONFIG_DMA_IPROC_PAX_V2`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_IPROC_PAX_V2)。

<a id="CONFIG_PCIE_EP_IPROC"></a>

## 134.6 `CONFIG_PCIE_EP_IPROC`

**提示（Prompt）**：Broadcom iProc PCIe 端点（EP）驱动

**说明（Help）**

此选项启用 Broadcom iProc PCIe EP 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_IPROC_PCIE_EP_ENABLED && CONFIG_PCIE_ENDPOINT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/pcie/endpoint/Kconfig.iproc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/endpoint/Kconfig.iproc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PCIe 端点（Endpoint）支持

**配置项引用（Symbol References）**：[`CONFIG_PCIE_ENDPOINT`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE_ENDPOINT)。

<a id="CONFIG_PCIE_EP_IPROC_INIT_CFG"></a>

## 134.7 `CONFIG_PCIE_EP_IPROC_INIT_CFG`

**提示（Prompt）**：重新初始化 PCIe MSI/MSI-X 配置

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PCIE_EP_IPROC && CONFIG_PCIE_ENDPOINT
```

**定义位置（Location）**：[`drivers/pcie/endpoint/Kconfig.iproc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/endpoint/Kconfig.iproc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PCIe 端点（Endpoint）支持 → Broadcom iProc PCIe 端点（EP）驱动

**配置项引用（Symbol References）**：[`CONFIG_PCIE_EP_IPROC`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE_EP_IPROC)、[`CONFIG_PCIE_ENDPOINT`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE_ENDPOINT)。

<a id="CONFIG_PCIE_INIT_PRIORITY"></a>

## 134.8 `CONFIG_PCIE_INIT_PRIORITY`

**提示（Prompt）**：PCIe 初始化优先级

**说明（Help）**

PCIe 主机驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PCIE
```

**默认值（Defaults）**

```text
41
```

**定义位置（Location）**：[`drivers/pcie/host/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持

**配置项引用（Symbol References）**：[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)。

<a id="CONFIG_PCIE_MSI"></a>

## 134.9 `CONFIG_PCIE_MSI`

**提示（Prompt）**：PCI(e) 消息信号中断（MSI）支持

**说明（Help）**

尽可能使用消息信号中断（Message-Signaled Interrupts，MSI）。启用后，支持 MSI 的 PCI(e) 设备会在运行时配置为使用它。PCIe 设备要产生中断，通常必须启用此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PCIE
```

**被选择（Selected by）**

```text
CONFIG_SOC_ELKHART_LAKE
CONFIG_SOC_NOVA_LAKE
CONFIG_SOC_WILDCAT_LAKE
CONFIG_SOC_ALDER_LAKE
CONFIG_SOC_RAPTOR_LAKE
CONFIG_SOC_APOLLO_LAKE
CONFIG_SOC_PANTHER_LAKE
CONFIG_NVME
```

**定义位置（Location）**：[`drivers/pcie/host/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持

**配置项引用（Symbol References）**：[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)、[`CONFIG_SOC_ELKHART_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ELKHART_LAKE)、[`CONFIG_SOC_NOVA_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NOVA_LAKE)、[`CONFIG_SOC_WILDCAT_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_WILDCAT_LAKE)、[`CONFIG_SOC_ALDER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ALDER_LAKE)、[`CONFIG_SOC_RAPTOR_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RAPTOR_LAKE)、[`CONFIG_SOC_APOLLO_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO_LAKE)、[`CONFIG_SOC_PANTHER_LAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PANTHER_LAKE)、[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ELKHART_LAKE`、`CONFIG_SOC_NOVA_LAKE`、`CONFIG_SOC_WILDCAT_LAKE`、`CONFIG_SOC_ALDER_LAKE`、`CONFIG_SOC_RAPTOR_LAKE`、`CONFIG_SOC_APOLLO_LAKE`、`CONFIG_SOC_PANTHER_LAKE`。

<a id="CONFIG_PCIE_MSI_MULTI_VECTOR"></a>

## 134.10 `CONFIG_PCIE_MSI_MULTI_VECTOR`

**提示（Prompt）**：MSI 多向量（Multi-vector）支持

**说明（Help）**

MSI 最多支持 32 种不同消息。此选项启用该能力，使每条消息都能分配到一个向量。选定架构必须提供必要逻辑。如果硬件无法管理这些向量，或没有任何外设需要此功能，应禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PCIE_MSI && CONFIG_PCIE
```

**被选择（Selected by）**

```text
CONFIG_NVME
CONFIG_ETH_INTEL_IGC
```

**定义位置（Location）**：[`drivers/pcie/host/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持 → PCI(e) 消息信号中断（MSI）支持

**配置项引用（Symbol References）**：[`CONFIG_PCIE_MSI`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE_MSI)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)、[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_ETH_INTEL_IGC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_INTEL_IGC)。

<a id="CONFIG_PCIE_MSI_X"></a>

## 134.11 `CONFIG_PCIE_MSI_X`

**提示（Prompt）**：MSI-X 支持

**说明（Help）**

一个或多个设备支持 MSI-X 时，需要启用此项。若设备同时支持 MSI-X 与 MSI，则使用 MSI-X，并在该设备上禁用 MSI。如果还希望 MSI-X 支持多向量，请启用 `PCIE_MSI_MULTI_VECTOR`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PCIE_MSI && CONFIG_PCIE
```

**被选择（Selected by）**

```text
CONFIG_NVME
CONFIG_ETH_INTEL_IGC
```

**定义位置（Location）**：[`drivers/pcie/host/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持 → PCI(e) 消息信号中断（MSI）支持

**配置项引用（Symbol References）**：[`CONFIG_PCIE_MSI`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE_MSI)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)、[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_ETH_INTEL_IGC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_INTEL_IGC)。

<a id="CONFIG_PCIE_PRT"></a>

## 134.12 `CONFIG_PCIE_PRT`

**提示（Prompt）**：通过 ACPI PRT（PCI 路由表）获取中断请求信息的支持

**说明（Help）**

启用通过 ACPI PCI 路由表（PCI Routing Table，PRT）获取传统 PCI 中断的路由信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PCIE
```

**默认值（Defaults）**

```text
y if CONFIG_ACPI_DSDT_SUPPORT
```

**定义位置（Location）**：[`drivers/pcie/host/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持

**配置项引用（Symbol References）**：[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)、[`CONFIG_ACPI_DSDT_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ACPI_DSDT_SUPPORT)。

<a id="CONFIG_PCIE_PTM"></a>

## 134.13 `CONFIG_PCIE_PTM`

**提示（Prompt）**：PCI(e) 精确时间管理（Precision Time Management，PTM）支持

**说明（Help）**

同时启用 PTM 根（Root）与请求方（Requester）功能支持。由 PCIe 设备驱动负责启用其 PTM 请求方能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PCIE
```

**定义位置（Location）**：[`drivers/pcie/host/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持

**配置项引用（Symbol References）**：[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)。

<a id="CONFIG_PCIE_SHELL"></a>

## 134.14 `CONFIG_PCIE_SHELL`

**提示（Prompt）**：PCIe／新 PCI 命令行（Shell）

**说明（Help）**

启用通过内置 Shell 调试 PCI(e) 的命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_PCIE
```

**定义位置（Location）**：[`drivers/pcie/host/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pcie/host/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 新 PCI/PCIe 根复合体（Root Complex）支持

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)。

<!-- kconfig-navigation -->

[上一章](P133_drivers_otp_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P135_drivers_peci_配置项参考.md)
