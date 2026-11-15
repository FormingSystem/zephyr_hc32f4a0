---
id: learning.zephyr-docs.kconfig-reference.page-183
title: "`drivers/virtio`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第183章\_`drivers/virtio`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/virtio` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_VIRTIO"></a>

## 183.1 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_VIRTIO`

**提示（Prompt）**：VIRTIO 的堆内存池（Heap Memory Pool）大小

**说明（Help）**

设置 VIRTIO 的堆内存池（Heap Memory Pool）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIRTIO
```

**默认值（Defaults）**

```text
32768
```

**定义位置（Location）**：[`drivers/virtio/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtio/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持

**配置项引用（Symbol References）**：[`CONFIG_VIRTIO`](P183_drivers_virtio_配置项参考.md#CONFIG_VIRTIO)。

<a id="CONFIG_VIRTIO"></a>

## 183.2 `CONFIG_VIRTIO`

**提示（Prompt）**：VIRTIO 支持

**说明（Help）**

启用 VIRTIO 相关选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_DISK_DRIVER_VIRTIO_BLK
CONFIG_ENTROPY_VIRTIO
CONFIG_ETH_VIRTIO_NET
CONFIG_GPIO_VIRTIO
CONFIG_I2C_VIRTIO
CONFIG_INPUT_VIRTIO
CONFIG_UART_VIRTIO_CONSOLE
CONFIG_SPI_VIRTIO
CONFIG_FILE_SYSTEM_VIRTIOFS
```

**定义位置（Location）**：[`drivers/virtio/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtio/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_VIRTIO_BLK`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_VIRTIO_BLK)、[`CONFIG_ENTROPY_VIRTIO`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_VIRTIO)、[`CONFIG_ETH_VIRTIO_NET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_VIRTIO_NET)、[`CONFIG_GPIO_VIRTIO`](P100_drivers_gpio_配置项参考_3.md#CONFIG_GPIO_VIRTIO)、[`CONFIG_I2C_VIRTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_VIRTIO)、[`CONFIG_INPUT_VIRTIO`](P112_drivers_input_配置项参考_2.md#CONFIG_INPUT_VIRTIO)、[`CONFIG_UART_VIRTIO_CONSOLE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_VIRTIO_CONSOLE)、[`CONFIG_SPI_VIRTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_VIRTIO)、[`CONFIG_FILE_SYSTEM_VIRTIOFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM_VIRTIOFS)。

<a id="CONFIG_VIRTIO_MMIO"></a>

## 183.3 `CONFIG_VIRTIO_MMIO`

**提示（Prompt）**：通过内存映射输入输出（MMIO）使用 VIRTIO

**说明（Help）**

启用通过内存映射输入输出（MMIO）使用 VIRTIO 的相关选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_MMIO_ENABLED && CONFIG_VIRTIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/virtio/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtio/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持

**配置项引用（Symbol References）**：[`CONFIG_VIRTIO`](P183_drivers_virtio_配置项参考.md#CONFIG_VIRTIO)。

<a id="CONFIG_VIRTIO_PCI"></a>

## 183.4 `CONFIG_VIRTIO_PCI`

**提示（Prompt）**：通过 PCI 使用 VIRTIO

**说明（Help）**

启用通过 PCI 使用 VIRTIO 的相关选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_PCI_ENABLED && CONFIG_VIRTIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PCIE
```

**定义位置（Location）**：[`drivers/virtio/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/virtio/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持

**配置项引用（Symbol References）**：[`CONFIG_VIRTIO`](P183_drivers_virtio_配置项参考.md#CONFIG_VIRTIO)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)。

<!-- kconfig-navigation -->

[上一章](P182_drivers_video_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P184_drivers_virtualization_配置项参考.md)
