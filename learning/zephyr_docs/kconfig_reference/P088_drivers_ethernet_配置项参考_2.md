---
id: learning.zephyr-docs.kconfig-reference.page-88
title: "`drivers/ethernet`配置项参考（2/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第88章\_`drivers/ethernet`配置项参考（2/4）

本章翻译官方 Kconfig 数据库中 `drivers/ethernet` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ETH_MCHP_BUF_RX_COUNT"></a>

## 88.1 `CONFIG_ETH_MCHP_BUF_RX_COUNT`

**提示（Prompt）**：SAM ETH 驱动预先分配的网络接收缓冲区（Network RX Buffers）

**说明（Help）**

以太网驱动永久分配的网络缓冲区（Network Buffer）数量。这些缓冲区用于接收路径，由驱动预先分配并提供给 GMAC 模块，用于填入传入数据。其数量必须足以容纳至少一个完整以太网帧（Ethernet Frame）。SAM ETH 驱动始终为自身分配此数量的缓冲区，因此会占用 `NET_BUF_RX_COUNT` 所规定的整个网络协议栈的接收数据缓冲区总量，减少其余可用数量。必须确保 `NET_PKT_RX_COUNT` 足够大，至少可容纳两个以太网帧：一个由 GMAC 模块接收，另一个由上层网络协议栈处理。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_MCHP_GMAC_G1 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.mchp:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.mchp#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Microchip G1 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_MCHP_GMAC_G1`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_MCHP_GMAC_G1)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_MCHP_GMAC_G1"></a>

## 88.2 `CONFIG_ETH_MCHP_GMAC_G1`

**提示（Prompt）**：Microchip G1 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 Microchip 微控制器（MCU）系列的以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF_FIXED_DATA_SIZE && DT_HAS_MICROCHIP_GMAC_G1_ETH_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT && CONFIG_DCACHE
CONFIG_PINCTRL
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**弱选择（Implies）**

```text
CONFIG_NVMEM if n
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.mchp:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.mchp#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_FIXED_DATA_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_FIXED_DATA_SIZE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_MCHP_RX_THREAD_PRIORITY"></a>

## 88.3 `CONFIG_ETH_MCHP_RX_THREAD_PRIORITY`

**提示（Prompt）**：MCHP 接收工作线程优先级（RX Work Thread Priority）

**说明（Help）**

以太网驱动在线程中处理接收（RX）。此选项设置该线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_MCHP_GMAC_G1 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.mchp:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.mchp#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Microchip G1 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_MCHP_GMAC_G1`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_MCHP_GMAC_G1)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_MCHP_RX_THREAD_STACK_SIZE"></a>

## 88.4 `CONFIG_ETH_MCHP_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：MCHP 接收工作线程栈大小（RX Work Thread Stack Size）

**说明（Help）**

接收线程（RX Thread）的栈大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_MCHP_GMAC_G1 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1600
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.mchp:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.mchp#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Microchip G1 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_MCHP_GMAC_G1`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_MCHP_GMAC_G1)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NATIVE_TAP"></a>

## 88.5 `CONFIG_ETH_NATIVE_TAP`

**提示（Prompt）**：原生 TAP 以太网驱动（Native TAP Ethernet Driver）

**说明（Help）**

启用 `native_sim` TAP 以太网驱动。此驱动运行于主机系统（Host System）的一个进程中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_TAP_ENABLED && CONFIG_ARCH_POSIX && CONFIG_NET_L2_ETHERNET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.native_tap:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.native_tap#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NATIVE_TAP_DEV_NAME"></a>

## 88.6 `CONFIG_ETH_NATIVE_TAP_DEV_NAME`

**提示（Prompt）**：主机以太网 TUN/TAP 设备名称（Device Name）

**说明（Help）**

此选项设置主机系统（Host System）中的 TUN/TAP 设备名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NATIVE_TAP && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
"/dev/net/tun"
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.native_tap:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.native_tap#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 原生 TAP 以太网驱动（Native TAP Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NATIVE_TAP`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NATIVE_TAP)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NATIVE_TAP_RX_TIMEOUT"></a>

## 88.7 `CONFIG_ETH_NATIVE_TAP_RX_TIMEOUT`

**提示（Prompt）**：以太网接收超时（Ethernet RX Timeout）

**说明（Help）**

原生 TAP 以太网驱动（Native TAP Ethernet Driver）反复检查是否有新数据。此选项指定没有新数据时，线程在两次检查之间休眠多久。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NATIVE_TAP && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1 if CONFIG_NET_GPTP
50
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.native_tap:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.native_tap#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 原生 TAP 以太网驱动（Native TAP Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NATIVE_TAP`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NATIVE_TAP)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_GPTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP)。

<a id="CONFIG_ETH_NATIVE_TAP_VLAN_TAG_STRIP"></a>

## 88.8 `CONFIG_ETH_NATIVE_TAP_VLAN_TAG_STRIP`

**提示（Prompt）**：从接收帧中剥离虚拟局域网标签（Strip VLAN Tag）

**说明（Help）**

原生 TAP 以太网驱动会剥离接收以太网帧（Rx Ethernet Frame）中的虚拟局域网标签（VLAN Tag），并将标签信息设置到网络数据包元数据（Metadata）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_VLAN && CONFIG_ETH_NATIVE_TAP && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.native_tap:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.native_tap#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 原生 TAP 以太网驱动（Native TAP Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_NET_VLAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN)、[`CONFIG_ETH_NATIVE_TAP`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NATIVE_TAP)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NET_IF_NO_AUTO_START"></a>

## 88.9 `CONFIG_ETH_NET_IF_NO_AUTO_START`

**提示（Prompt）**：禁用以太网接口自动启动（Interface Auto-Start）

**说明（Help）**

此选项允许用户在接口进入工作状态之前完成配置。例如，可通过 `net_if_set_link_addr(iface, mac, 6, NET_LINK_ETHERNET)` 配置 MAC 地址。完成全部配置后，必须调用 `net_if_up()` 启用接口（Bring the Interface Up）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET || CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NIC_MODEL"></a>

## 88.10 `CONFIG_ETH_NIC_MODEL`

原库同名定义共 6 条；本项为数据库第 6168 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

指定要使用的 QEMU 网络模型（Network Model）。此值作为参数传给 QEMU 命令行选项 `-nic`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_E1000 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
"e1000"
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.e1000:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.e1000#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Intel® PRO/1000 千兆以太网驱动（Gigabit Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_E1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_E1000)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NIC_MODEL--record-6169"></a>

## 88.11 `CONFIG_ETH_NIC_MODEL`

原库同名定义共 6 条；本项为数据库第 6169 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

指定要使用的 QEMU 网络模型（Network Model）。此值作为参数传给 QEMU 命令行选项 `-nic`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_IVSHMEM && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
"ivshmem"
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.ivshmem:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.ivshmem#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 虚拟机间共享内存以太网驱动（Inter-VM Shared Memory Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_IVSHMEM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_IVSHMEM)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NIC_MODEL--record-6170"></a>

## 88.12 `CONFIG_ETH_NIC_MODEL`

原库同名定义共 6 条；本项为数据库第 6170 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

指定要使用的 QEMU 网络模型（Network Model）。此值作为参数传给 QEMU 命令行选项 `-nic`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_SMSC911X && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
"lan9118"
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.smsc911x:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.smsc911x#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → SMSC911x/9220 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_SMSC911X`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SMSC911X)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NIC_MODEL--record-6171"></a>

## 88.13 `CONFIG_ETH_NIC_MODEL`

原库同名定义共 6 条；本项为数据库第 6171 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

指定要使用的 QEMU 网络模型（Network Model）。此值作为参数传给 QEMU 命令行选项 `-nic`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_STELLARIS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
"stellaris"
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stellaris:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stellaris#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → TI Stellaris 微控制器（MCU）系列的以太网（Ethernet）驱动。

**配置项引用（Symbol References）**：[`CONFIG_ETH_STELLARIS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STELLARIS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NIC_MODEL--record-6172"></a>

## 88.14 `CONFIG_ETH_NIC_MODEL`

原库同名定义共 6 条；本项为数据库第 6172 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

告知 QEMU 要使用的网络模型（Network Model）。此值作为参数传给 QEMU 命令行选项 `-nic`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_VIRTIO_NET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
"virtio-net-device" if CONFIG_VIRTIO_MMIO
"virtio-net-pci" if CONFIG_VIRTIO_PCI
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.virtio_net:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.virtio_net#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → VIRTIO 网络半虚拟化设备驱动（Networking Paravirtualization Device Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_VIRTIO_NET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_VIRTIO_NET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_VIRTIO_MMIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO_MMIO)、[`CONFIG_VIRTIO_PCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO_PCI)。

<a id="CONFIG_ETH_NIC_MODEL--record-6173"></a>

## 88.15 `CONFIG_ETH_NIC_MODEL`

原库同名定义共 6 条；本项为数据库第 6173 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启动 QEMU 时使用的 `-nic` 参数值。此参数指定 QEMU 应模拟的以太网控制器（Ethernet Controller）类型。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_XLNX_GEM && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
"cadence_gem"
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.xlnx_gem:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.xlnx_gem#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Xilinx GEM 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_XLNX_GEM`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XLNX_GEM)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NIC_MODEL_ONBOARD"></a>

## 88.16 `CONFIG_ETH_NIC_MODEL_ONBOARD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由 QEMU 网卡模型（NIC Model，`ETH_NIC_MODEL`）内建于所仿真机器中的驱动选中。此类网卡无法通过 QEMU 的 `-device` 选项创建，因此改用 `-nic` 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_ETH_SMSC911X
CONFIG_ETH_STELLARIS
CONFIG_ETH_XLNX_GEM
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_SMSC911X`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SMSC911X)、[`CONFIG_ETH_STELLARIS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STELLARIS)、[`CONFIG_ETH_XLNX_GEM`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XLNX_GEM)。

<a id="CONFIG_ETH_NUMAKER_DWC_ETHER_1000"></a>

## 88.17 `CONFIG_ETH_NUMAKER_DWC_ETHER_1000`

**提示（Prompt）**：用于基于 DWC 以太网 MAC 的 Nuvoton NuMaker 的驱动

**说明（Help）**

在新唐（Nuvoton）NuMaker M467 和 M55M1 SoC 上启用 Synopsys DesignWare MAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_M46X || CONFIG_SOC_SERIES_M55M1X) && DT_HAS_NUVOTON_NUMAKER_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_DWC_ETHER_1000_CORE
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_PINCTRL
CONFIG_RESET
CONFIG_CLOCK_CONTROL
CONFIG_HWINFO
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_M46X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M46X)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_HWINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HWINFO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_NXP_DWC_ETHER_QOS"></a>

## 88.18 `CONFIG_ETH_NXP_DWC_ETHER_QOS`

**提示（Prompt）**：用于基于 DWC Ethernet QoS 的 NXP 的驱动

**说明（Help）**

在 NXP MCX N / MCX A / MCX E31 和 S32K3 系列 SoC 上启用 Synopsys DesignWare MAC 驱动；在这些 SoC 中，该 IP 名为 EMAC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ETH_NXP_ENET_QOS && !CONFIG_ETH_NXP_S32_GMAC && (CONFIG_SOC_SERIES_MCXE31X || CONFIG_SOC_FAMILY_MCXN || CONFIG_SOC_FAMILY_MCXA || CONFIG_SOC_SERIES_S32K3) && (DT_HAS_NXP_ENET_QOS_ENABLED || DT_HAS_NXP_S32_GMAC_ENABLED) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_DWC_ETHER_QOS_CORE
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_PINCTRL
CONFIG_RESET if n
CONFIG_HWINFO
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_HWINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HWINFO)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_FAMILY_MCXN`、`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_NXP_ENET"></a>

## 88.19 `CONFIG_ETH_NXP_ENET`

**提示（Prompt）**：NXP ENET 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 NXP ENET 以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ENET_MAC_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_CPU_HAS_DCACHE
CONFIG_ARM_MPU if CONFIG_CPU_CORTEX_M7
CONFIG_PINCTRL
CONFIG_HWINFO if n
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**弱选择（Implies）**

```text
CONFIG_NET_POWER_MANAGEMENT
CONFIG_NVMEM if n
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_enet:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_enet#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_CPU_CORTEX_M7`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M7)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_HWINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HWINFO)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_POWER_MANAGEMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_POWER_MANAGEMENT)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_POWER_MANAGEMENT`。

<a id="CONFIG_ETH_NXP_ENET_HW_ACCELERATION"></a>

## 88.20 `CONFIG_ETH_NXP_ENET_HW_ACCELERATION`

**提示（Prompt）**：硬件加速（Hardware Acceleration）

**说明（Help）**

为以下功能启用硬件加速（Hardware Acceleration）：

- IPv4、UDP 和 TCP 校验和（Checksum），同时用于接收（Rx）和发送（Tx）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD && CONFIG_ETH_NXP_ENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_enet:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_enet#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_NET_CHECKSUM_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD)、[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_MULTICAST_FILTER"></a>

## 88.21 `CONFIG_ETH_NXP_ENET_MULTICAST_FILTER`

**提示（Prompt）**：组播目标地址过滤（Multicast Destination Address Filtering）

**说明（Help）**

在 MAC 中启用组播目标地址过滤（Multicast Destination Address Filtering）支持。MAC 使用组地址哈希表（Group-Address Hash Table，`GAUR` / `GALR`）进行非精确过滤（Imperfect Filtering）。仅接收其计算出的哈希位在表中已置位的组播，其余组播均由 MAC 丢弃。禁用此项时，哈希表对所有组播地址开放，因此接收不依赖为各组安装对应哈希项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_enet:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_enet#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_QOS"></a>

## 88.22 `CONFIG_ETH_NXP_ENET_QOS`

**提示（Prompt）**：NXP ENET QOS 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 NXP ENET QOS 以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ENET_QOS_ENABLED && (CONFIG_SOC_FAMILY_MCXA || CONFIG_SOC_FAMILY_MCXN) && CONFIG_NET_BUF_FIXED_DATA_SIZE && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_FAMILY_MCXN || (!CONFIG_PTP_CLOCK && CONFIG_SOC_FAMILY_MCXA)
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/eth_nxp_enet_qos/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_nxp_enet_qos/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_NET_BUF_FIXED_DATA_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_FIXED_DATA_SIZE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_FAMILY_MCXN`。

<a id="CONFIG_ETH_NXP_ENET_QOS_DMA_RESET_WAIT_TIME"></a>

## 88.23 `CONFIG_ETH_NXP_ENET_QOS_DMA_RESET_WAIT_TIME`

**提示（Prompt）**：等待软件复位（Software Reset）的时间，以微秒为单位

**说明（Help）**

允许软件复位（Software Reset）耗用的时间，以微秒（µs）为单位。值为 `0` 时，驱动无限等待。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET_QOS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`drivers/ethernet/eth_nxp_enet_qos/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_nxp_enet_qos/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET QOS 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_QOS_RX_BUFFER_DESCRIPTORS"></a>

## 88.24 `CONFIG_ETH_NXP_ENET_QOS_RX_BUFFER_DESCRIPTORS`

**提示（Prompt）**：接收缓冲区描述符数量（RX Buffer Descriptor Count）

**说明（Help）**

接收（RX）缓冲区描述符（Buffer Descriptor）的数量。每个描述符引用一个大小为 `CONFIG_NET_BUF_DATA_SIZE` 的缓冲区，且该大小的最低两位被忽略。因此应将此数量设得足够大，使所有缓冲区合计至少能够接收一个最大大小的帧。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET_QOS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[4, 1024]
```

**定义位置（Location）**：[`drivers/ethernet/eth_nxp_enet_qos/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_nxp_enet_qos/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET QOS 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_QOS_RX_THREAD_PRIORITY"></a>

## 88.25 `CONFIG_ETH_NXP_ENET_QOS_RX_THREAD_PRIORITY`

**提示（Prompt）**：ENET QOS 接收线程的协作式优先级（RX Cooperative Priority）

**说明（Help）**

ENET QOS 接收线程的协作式优先级（RX Cooperative Priority）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET_QOS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/ethernet/eth_nxp_enet_qos/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_nxp_enet_qos/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET QOS 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_QOS_RX_THREAD_STACK_SIZE"></a>

## 88.26 `CONFIG_ETH_NXP_ENET_QOS_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：ENET QOS 接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

ENET QOS 接收线程（RX Thread）的栈大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET_QOS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/ethernet/eth_nxp_enet_qos/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_nxp_enet_qos/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET QOS 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_QOS_TX_BUFFER_DESCRIPTORS"></a>

## 88.27 `CONFIG_ETH_NXP_ENET_QOS_TX_BUFFER_DESCRIPTORS`

**提示（Prompt）**：发送缓冲区描述符数量（TX Buffer Descriptor Count）

**说明（Help）**

发送（TX）缓冲区描述符（Buffer Descriptor）的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET_QOS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[4, 1024]
```

**定义位置（Location）**：[`drivers/ethernet/eth_nxp_enet_qos/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_nxp_enet_qos/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET QOS 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_QOS_TX_TIMEOUT_MS"></a>

## 88.28 `CONFIG_ETH_NXP_ENET_QOS_TX_TIMEOUT_MS`

**提示（Prompt）**：发送完成超时时间（Transmit Completion Timeout），以毫秒为单位

**说明（Help）**

等待发送 DMA 回写已交给它的帧的描述符（Descriptor）的时间。超过此时间后仍未完成的帧会被放弃：发送路径（Transmit Path）被复位，数据包归还到其池（Pool）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET_QOS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[10, 10000]
```

**定义位置（Location）**：[`drivers/ethernet/eth_nxp_enet_qos/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_nxp_enet_qos/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET QOS 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS"></a>

## 88.29 `CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS`

**提示（Prompt）**：唯一 MAC 地址支持（Unique MAC Address Support）

**说明（Help）**

启用基于设备通用唯一标识符（UUID）的唯一 MAC 地址（Unique MAC Address）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET_QOS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_HWINFO
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ethernet/eth_nxp_enet_qos/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_nxp_enet_qos/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET QOS 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_HWINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HWINFO)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_ETH_NXP_ENET_RMII_EXT_CLK"></a>

## 88.30 `CONFIG_ETH_NXP_ENET_RMII_EXT_CLK`

**提示（Prompt）**：来自外部源的 RMII 时钟（External RMII Clock）

**说明（Help）**

设置此选项后，ENET 时钟模块使用外部源 `ENET_1588_CLKIN` 提供的 RMII 参考时钟（Reference Clock）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_enet:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_enet#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_RX_BUFFERS"></a>

## 88.31 `CONFIG_ETH_NXP_ENET_RX_BUFFERS`

**提示（Prompt）**：以太网驱动的接收缓冲区数量（RX Buffer Count）

**说明（Help）**

设置提供给 NXP ENET 驱动的接收缓冲区（RX Buffer）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[6, 16]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_enet:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_enet#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_RX_THREAD_PRIORITY"></a>

## 88.32 `CONFIG_ETH_NXP_ENET_RX_THREAD_PRIORITY`

**提示（Prompt）**：NXP ENET 驱动接收协作式线程优先级（RX Cooperative Thread Priority）

**说明（Help）**

ENET MAC 驱动在协作式工作队列线程（Cooperative Workqueue Thread）中处理接收（RX）。此选项设置该线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_enet:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_enet#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_RX_THREAD_STACK_SIZE"></a>

## 88.33 `CONFIG_ETH_NXP_ENET_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：NXP ENET 接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

ENET 接收线程（RX Thread）的栈大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1600
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_enet:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_enet#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_TX_BUFFERS"></a>

## 88.34 `CONFIG_ETH_NXP_ENET_TX_BUFFERS`

**提示（Prompt）**：以太网驱动的发送缓冲区数量（TX Buffer Count）

**说明（Help）**

设置提供给 NXP ENET 驱动的发送缓冲区（TX Buffer）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_enet:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_enet#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_ENET_USE_DTCM_FOR_DMA_BUFFER"></a>

## 88.35 `CONFIG_ETH_NXP_ENET_USE_DTCM_FOR_DMA_BUFFER`

**提示（Prompt）**：使用 DTCM 存放硬件 DMA 缓冲区（Hardware DMA Buffers）

**说明（Help）**

将硬件 DMA 缓冲区放入数据紧耦合内存（DTCM），以改善网络性能（Networking Performance）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_ENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
n if CONFIG_CPU_CORTEX_M7
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_enet:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_enet#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP ENET 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_CPU_CORTEX_M7`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M7)。

<a id="CONFIG_ETH_NXP_IMX_MSGINTR"></a>

## 88.36 `CONFIG_ETH_NXP_IMX_MSGINTR`

**提示（Prompt）**：消息中断模块选择（Message Interrupt Module Select）

**说明（Help）**

选择消息中断模块（Message Interrupt Module）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_ETH_NXP_IMX_NETC_MSI_GIC && CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC_MSI_GIC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC_MSI_GIC)、[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_NETC"></a>

## 88.37 `CONFIG_ETH_NXP_IMX_NETC`

**提示（Prompt）**：NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**说明（Help）**

为 NXP i.MX SoC 启用以太网与网络控制器（Ethernet and Network Controller，NETC）驱动。支持物理站点接口（Physical Station Interface，PSI）和虚拟站点接口（Virtual Station Interface，VSI）。

注意：VSI 支持面向非对称多处理（AMP）场景，即 Zephyr 拥有一个 VSI（虚拟功能，VF），另一个操作系统拥有 PSI（物理功能，PF）。Zephyr PSI 驱动既不实现单根 I/O 虚拟化（SR-IOV），也不实现 PSI 到 VSI 消息通道的 PSI 一侧，因此不支持将 Zephyr VSI 与 Zephyr PSI 配对。目前仅测试过 Zephyr VSI 与 Linux PSI 配对的情况。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NXP_IMX_NETC_PSI_ENABLED || DT_HAS_NXP_IMX_NETC_VSI_ENABLED) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_NXP_IMX_NETC_MSI_GIC"></a>

## 88.38 `CONFIG_ETH_NXP_IMX_NETC_MSI_GIC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将 GIC ITS 控制器用作 NXP NETC 的消息信号中断（MSI）模块

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GIC_V3_ITS && CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if n && DT_HAS_ARM_GIC_V3_ITS_ENABLED
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_GIC_V3_ITS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_GIC_V3_ITS)、[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_NETC_VSI_READY_POLL_INTERVAL_MS"></a>

## 88.39 `CONFIG_ETH_NXP_IMX_NETC_VSI_READY_POLL_INTERVAL_MS`

**提示（Prompt）**：VSI 就绪条件轮询间隔（Readiness-Gate Poll Interval），以毫秒为单位

**说明（Help）**

VSI 服务线程在首次访问站点接口（SI）之前，轮询各项就绪条件（Readiness Gate）的间隔。这些条件包括：节点具有 `clocks` 属性时可选的 SCMI 时钟状态条件（Clock-Status Gate），以及 ECAM 中父物理功能（PF）的 SR-IOV 虚拟功能启用位（VF-Enable Bits）。两种检查均不会引发访问故障，因为它们从不访问尚未开始地址译码的 SI。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_NETC_VSI_ENABLED && CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[1, 10000]
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_RX_BUDGET"></a>

## 88.40 `CONFIG_ETH_NXP_IMX_RX_BUDGET`

**提示（Prompt）**：接收线程工作预算（RX Thread Budget）

**说明（Help）**

当仍有工作待处理时，预算（Budget）参数限制驱动在接收线程（RX Thread）中完成多少工作后必须让出处理器（Yield）。这可防止接收线程使其他线程饥饿（Starvation）。每个收到的帧算作一个工作单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_RX_RING_BUF_SIZE"></a>

## 88.41 `CONFIG_ETH_NXP_IMX_RX_RING_BUF_SIZE`

**提示（Prompt）**：接收环数据缓冲区大小（RX Ring Data Buffer Size）

**说明（Help）**

接收（RX）数据缓冲区的大小，以字节为单位。必须足以存储一个完整以太网帧（Ethernet Frame），且必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1518
```

**取值范围（Ranges）**

```text
[64, 1536]
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_RX_RING_LEN"></a>

## 88.42 `CONFIG_ETH_NXP_IMX_RX_RING_LEN`

**提示（Prompt）**：接收环长度（RX Ring Length）

**说明（Help）**

接收环（RX Ring）的长度。数值必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
16 if CONFIG_PTP_CLOCK_NXP_NETC
8
```

**取值范围（Ranges）**

```text
[8, 256]
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_CLOCK_NXP_NETC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK_NXP_NETC)。

<a id="CONFIG_ETH_NXP_IMX_RX_RING_NUM"></a>

## 88.43 `CONFIG_ETH_NXP_IMX_RX_RING_NUM`

**提示（Prompt）**：接收环数量（RX Ring Number）

**说明（Help）**

使用的接收环（RX Ring）数量。实际最大值可能因平台而异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 1023]
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_RX_THREAD_PRIO"></a>

## 88.44 `CONFIG_ETH_NXP_IMX_RX_THREAD_PRIO`

**提示（Prompt）**：接收线程优先级（RX Thread Priority）

**说明（Help）**

接收线程（RX Thread）的优先级。接收线程是协作式线程（Cooperative Thread）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_RX_THREAD_STACK_SIZE"></a>

## 88.45 `CONFIG_ETH_NXP_IMX_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

接收线程（RX Thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_TX_RING_BUF_SIZE"></a>

## 88.46 `CONFIG_ETH_NXP_IMX_TX_RING_BUF_SIZE`

**提示（Prompt）**：发送环数据缓冲区大小（TX Ring Data Buffer Size）

**说明（Help）**

发送（TX）数据缓冲区的大小，以字节为单位。必须足以存储一个完整以太网帧（Ethernet Frame），且必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1518
```

**取值范围（Ranges）**

```text
[64, 1536]
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_TX_RING_LEN"></a>

## 88.47 `CONFIG_ETH_NXP_IMX_TX_RING_LEN`

**提示（Prompt）**：发送环长度（TX Ring Length）

**说明（Help）**

发送环（TX Ring）的长度。数值必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[8, 256]
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_IMX_TX_RING_NUM"></a>

## 88.48 `CONFIG_ETH_NXP_IMX_TX_RING_NUM`

**提示（Prompt）**：发送环数量（TX Ring Number）

**说明（Help）**

使用的发送环（TX Ring）数量。实际最大值可能因平台而异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_IMX_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 1023]
```

**定义位置（Location）**：[`drivers/ethernet/nxp_imx_netc/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/nxp_imx_netc/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP i.MX 以太网与网络控制器（Ethernet and Network Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_CLOCK_CONFIG_IDX"></a>

## 88.49 `CONFIG_ETH_NXP_S32_CLOCK_CONFIG_IDX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项指定用于初始化 GMAC/EMAC 时钟的时钟配置（Clock Configuration）索引，索引从 `0` 开始。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_GMAC"></a>

## 88.50 `CONFIG_ETH_NXP_S32_GMAC`

**提示（Prompt）**：NXP S32 GMAC 驱动

**说明（Help）**

为 NXP S32 SoC 启用 GMAC/EMAC 以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_GMAC_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if !CONFIG_PTP_CLOCK
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_PINCTRL
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_NXP_S32_LOOPBACK"></a>

## 88.51 `CONFIG_ETH_NXP_S32_LOOPBACK`

**提示（Prompt）**：MAC 环回（Loopback）

**说明（Help）**

MAC 以环回模式（Loopback Mode）运行。数据经过对应的发送 PHY 接口模块，通过内部 FIFO 环回到内部 MII/GMII 接口。此模式需要 MII/GMII 接收时钟输入信号（Rx Clock Input）才能正常工作，因为发送时钟并不会在内部环回。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_MAC_FILTER_TABLE_SIZE"></a>

## 88.52 `CONFIG_ETH_NXP_S32_MAC_FILTER_TABLE_SIZE`

**提示（Prompt）**：MAC 过滤哈希表大小（Filter Hash Table Size）

**说明（Help）**

MAC 过滤哈希表（Filter Hash Table）支持的最大条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[8, 128]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_MULTICAST_FILTER"></a>

## 88.53 `CONFIG_ETH_NXP_S32_MULTICAST_FILTER`

**提示（Prompt）**：组播目标地址过滤（Multicast Destination Address Filtering）

**说明（Help）**

在 MAC 中启用组播目标地址过滤（Multicast Destination Address Filtering）支持。MAC 使用 64 位哈希表（Hash Table）进行非精确过滤（Imperfect Filtering）。对收到的组播地址计算 CRC，使用其高 6 位作为哈希表索引。仅接收所计算哈希值对应位在组播表中已置位的组播，其余组播由 MAC 丢弃。禁用此项时，MAC 接收全部组播。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_MULTICAST_MAC_FILTER_TABLE_SIZE"></a>

## 88.54 `CONFIG_ETH_NXP_S32_MULTICAST_MAC_FILTER_TABLE_SIZE`

**提示（Prompt）**：组播 MAC 过滤哈希表大小（Multicast Filter Hash Table Size）

**说明（Help）**

组播 MAC 过滤哈希表（Multicast MAC Filter Hash Table）支持的最大条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 8]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_NETC"></a>

## 88.55 `CONFIG_ETH_NXP_S32_NETC`

**提示（Prompt）**：NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**说明（Help）**

为 NXP S32 SoC 启用以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NXP_S32_NETC_PSI_ENABLED || DT_HAS_NXP_S32_NETC_VSI_ENABLED) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MBOX
CONFIG_PINCTRL
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MBOX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBOX)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_NXP_S32_RX_BUDGET"></a>

## 88.56 `CONFIG_ETH_NXP_S32_RX_BUDGET`

原库同名定义共 2 条；本项为数据库第 6214 条记录，各定义分别保留。

**提示（Prompt）**：接收线程工作预算（RX Thread Budget）

**说明（Help）**

当仍有工作待处理时，预算（Budget）参数限制驱动在接收线程（RX Thread）中完成多少工作后必须让出处理器（Yield）。这可防止接收线程使其他线程饥饿（Starvation）。每个收到的帧算作一个工作单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_BUDGET--record-6215"></a>

## 88.57 `CONFIG_ETH_NXP_S32_RX_BUDGET`

原库同名定义共 2 条；本项为数据库第 6215 条记录，各定义分别保留。

**提示（Prompt）**：接收线程工作预算（RX Thread Budget）

**说明（Help）**

当仍有工作待处理时，预算（Budget）参数限制驱动在接收线程（RX Thread）中完成多少工作后必须让出处理器（Yield）。这可防止接收线程使其他线程饥饿（Starvation）。每个收到的帧算作一个工作单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_IRQ_PACKET_THRESHOLD"></a>

## 88.58 `CONFIG_ETH_NXP_S32_RX_IRQ_PACKET_THRESHOLD`

**提示（Prompt）**：接收中断合并数据包阈值（RX Interrupt Coalescing Packet Threshold）

**说明（Help）**

接收中断合并数据包阈值（RX Interrupt Coalescing Packet Threshold）。此值决定发出中断之前必须收到的最少数据包数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 511]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_IRQ_TIMER_THRESHOLD"></a>

## 88.59 `CONFIG_ETH_NXP_S32_RX_IRQ_TIMER_THRESHOLD`

**提示（Prompt）**：接收中断合并定时器阈值（RX Interrupt Coalescing Timer Threshold）

**说明（Help）**

接收中断合并定时器阈值（RX Interrupt Coalescing Timer Threshold），以 NETC 时钟周期为单位。此值决定从收到第一个数据包，到达到接收中断合并数据包阈值之前，允许经过的最长时间。如果尚未达到数据包阈值而定时器先到期，则发出中断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
60000
```

**取值范围（Ranges）**

```text
[1, 4294967295]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_RING_BUF_SIZE"></a>

## 88.60 `CONFIG_ETH_NXP_S32_RX_RING_BUF_SIZE`

原库同名定义共 2 条；本项为数据库第 6218 条记录，各定义分别保留。

**提示（Prompt）**：接收环数据缓冲区大小（RX Ring Data Buffer Size）

**说明（Help）**

接收（RX）数据缓冲区的大小，以字节为单位。必须足以存储一个完整以太网帧（Ethernet Frame），且必须是数据总线宽度（Data Bus Width）的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1536
```

**取值范围（Ranges）**

```text
[64, 1536]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_RING_BUF_SIZE--record-6219"></a>

## 88.61 `CONFIG_ETH_NXP_S32_RX_RING_BUF_SIZE`

原库同名定义共 2 条；本项为数据库第 6219 条记录，各定义分别保留。

**提示（Prompt）**：接收环数据缓冲区大小（RX Ring Data Buffer Size）

**说明（Help）**

接收（RX）数据缓冲区的大小，以字节为单位。必须足以存储一个完整以太网帧（Ethernet Frame），且必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1536
```

**取值范围（Ranges）**

```text
[64, 1536]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_RING_LEN"></a>

## 88.62 `CONFIG_ETH_NXP_S32_RX_RING_LEN`

原库同名定义共 2 条；本项为数据库第 6220 条记录，各定义分别保留。

**提示（Prompt）**：接收环长度（RX Ring Length）

**说明（Help）**

接收环（RX Ring）的长度。`ETH_NXP_S32_RX_RING_BUF_SIZE * ETH_NXP_S32_RX_RING_LEN` 必须是接收 FIFO 块大小（RX FIFO Block Size）的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[4, 128]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_RING_LEN--record-6221"></a>

## 88.63 `CONFIG_ETH_NXP_S32_RX_RING_LEN`

原库同名定义共 2 条；本项为数据库第 6221 条记录，各定义分别保留。

**提示（Prompt）**：接收环长度（RX Ring Length）

**说明（Help）**

接收环（RX Ring）的长度。数值必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[8, 256]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_THREAD_PRIO"></a>

## 88.64 `CONFIG_ETH_NXP_S32_RX_THREAD_PRIO`

原库同名定义共 2 条；本项为数据库第 6222 条记录，各定义分别保留。

**提示（Prompt）**：接收线程优先级（RX Thread Priority）

**说明（Help）**

接收线程（RX Thread）的优先级。接收线程是协作式线程（Cooperative Thread）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_THREAD_PRIO--record-6223"></a>

## 88.65 `CONFIG_ETH_NXP_S32_RX_THREAD_PRIO`

原库同名定义共 2 条；本项为数据库第 6223 条记录，各定义分别保留。

**提示（Prompt）**：接收线程优先级（RX Thread Priority）

**说明（Help）**

接收线程（RX Thread）的优先级。接收线程是协作式线程（Cooperative Thread）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_THREAD_STACK_SIZE"></a>

## 88.66 `CONFIG_ETH_NXP_S32_RX_THREAD_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 6224 条记录，各定义分别保留。

**提示（Prompt）**：接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

接收线程（RX Thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_RX_THREAD_STACK_SIZE--record-6225"></a>

## 88.67 `CONFIG_ETH_NXP_S32_RX_THREAD_STACK_SIZE`

原库同名定义共 2 条；本项为数据库第 6225 条记录，各定义分别保留。

**提示（Prompt）**：接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

接收线程（RX Thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_TX_RING_BUF_SIZE"></a>

## 88.68 `CONFIG_ETH_NXP_S32_TX_RING_BUF_SIZE`

原库同名定义共 2 条；本项为数据库第 6226 条记录，各定义分别保留。

**提示（Prompt）**：发送环数据缓冲区大小（TX Ring Data Buffer Size）

**说明（Help）**

发送（TX）数据缓冲区的大小，以字节为单位。必须足以存储一个完整以太网帧（Ethernet Frame），且必须是数据总线宽度（Data Bus Width）的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1536
```

**取值范围（Ranges）**

```text
[64, 1536]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_TX_RING_BUF_SIZE--record-6227"></a>

## 88.69 `CONFIG_ETH_NXP_S32_TX_RING_BUF_SIZE`

原库同名定义共 2 条；本项为数据库第 6227 条记录，各定义分别保留。

**提示（Prompt）**：发送环数据缓冲区大小（TX Ring Data Buffer Size）

**说明（Help）**

发送（TX）数据缓冲区的大小，以字节为单位。必须足以存储一个完整以太网帧（Ethernet Frame），且必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1536
```

**取值范围（Ranges）**

```text
[64, 1536]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_TX_RING_LEN"></a>

## 88.70 `CONFIG_ETH_NXP_S32_TX_RING_LEN`

原库同名定义共 2 条；本项为数据库第 6228 条记录，各定义分别保留。

**提示（Prompt）**：发送环长度（TX Ring Length）

**说明（Help）**

发送环（TX Ring）的长度。`ETH_NXP_S32_TX_RING_BUF_SIZE * ETH_NXP_S32_TX_RING_LEN` 必须是发送 FIFO 块大小（TX FIFO Block Size）的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[4, 128]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_gmac:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_gmac#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 GMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_TX_RING_LEN--record-6229"></a>

## 88.71 `CONFIG_ETH_NXP_S32_TX_RING_LEN`

原库同名定义共 2 条；本项为数据库第 6229 条记录，各定义分别保留。

**提示（Prompt）**：发送环长度（TX Ring Length）

**说明（Help）**

发送环（TX Ring）的长度。数值必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[8, 256]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_NXP_S32_VSI_INIT_PRIORITY"></a>

## 88.72 `CONFIG_ETH_NXP_S32_VSI_INIT_PRIORITY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

虚拟站点接口（VSI）的初始化优先级（Initialization Priority）。数值必须大于物理站点接口（PSI）的初始化优先级 `CONFIG_ETH_INIT_PRIORITY`，且小于 `CONFIG_NET_INIT_PRIO`，以便 VSI 在 PSI 之后、网络子系统之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_NXP_S32_NETC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
81
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.nxp_s32_netc:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.nxp_s32_netc#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → NXP S32 以太网交换机与控制器（Ethernet Switch and Controller，NETC）驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_PHY_API_PLCA"></a>

## 88.73 `CONFIG_ETH_PHY_API_PLCA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

以太网物理层（PHY）驱动如果实现了物理层冲突避免（PLCA）相关 API 函数，应选中此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_PHY_MICROCHIP_T1S
CONFIG_PHY_NXP_T1S
CONFIG_PHY_ADIN1140
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PHY_MICROCHIP_T1S`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_MICROCHIP_T1S)、[`CONFIG_PHY_NXP_T1S`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PHY_NXP_T1S)、[`CONFIG_PHY_ADIN1140`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_PHY_ADIN1140)。

<a id="CONFIG_ETH_PHY_DRIVER"></a>

## 88.74 `CONFIG_ETH_PHY_DRIVER`

**提示（Prompt）**：以太网物理层驱动（Ethernet PHY Drivers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/phy/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/phy/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_QEMU_EXTRA_ARGS"></a>

## 88.75 `CONFIG_ETH_QEMU_EXTRA_ARGS`

**提示（Prompt）**：QEMU `-netdev` 选项的额外参数（Extra Arguments）

**说明（Help）**

启用以太网网络功能时，传给 QEMU `-netdev` 选项的额外参数（Extra Arguments）。此选项可包含多个 QEMU 选项参数，各参数之间必须用逗号 `,` 分隔，且不能有空格。例如：`"script=no"` 或 `"script=no,downscript=no"`。可用选项参见 [QEMU 调用说明（Invocation）](https://www.qemu.org/docs/master/system/invocation.html#hxtool-5)。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_QEMU_ETHERNET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_QEMU_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_ETHERNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_QEMU_IFACE_NAME"></a>

## 88.76 `CONFIG_ETH_QEMU_IFACE_NAME`

**提示（Prompt）**：QEMU 网络接口名称（Network Interface Name）

**说明（Help）**

QEMU 使用的网络接口名称（Network Interface Name）。此值作为参数传给 QEMU 命令行选项 `-netdev`。必须在启动 QEMU 之前创建该网络接口，可使用 `net-tools` 工程中的 `net-setup.sh` 脚本创建。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_QEMU_ETHERNET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
"zeth"
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_QEMU_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_ETHERNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_RA_RX_THREAD_PRIORITY"></a>

## 88.77 `CONFIG_ETH_RA_RX_THREAD_PRIORITY`

**提示（Prompt）**：瑞萨（Renesas）RA 以太网接收线程优先级（Receive Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_RENESAS_RA && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 瑞萨（Renesas）RA 以太网（Ethernet）

**配置项引用（Symbol References）**：[`CONFIG_ETH_RENESAS_RA`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_RA_RX_THREAD_STACK_SIZE"></a>

## 88.78 `CONFIG_ETH_RA_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：内部传入数据包处理线程的栈大小（Stack Size）

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_RENESAS_RA && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 瑞萨（Renesas）RA 以太网（Ethernet）

**配置项引用（Symbol References）**：[`CONFIG_ETH_RENESAS_RA`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_RENESAS_RA"></a>

## 88.79 `CONFIG_ETH_RENESAS_RA`

**提示（Prompt）**：瑞萨（Renesas）RA 以太网（Ethernet）

**说明（Help）**

启用瑞萨（Renesas）RA 以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_ETHER
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_USE_RA_FSP_ETHER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_ETHER)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_RENESAS_RA_RMAC"></a>

## 88.80 `CONFIG_ETH_RENESAS_RA_RMAC`

**提示（Prompt）**：瑞萨（Renesas）RA 以太网 RMAC 驱动

**说明（Help）**

增加瑞萨（Renesas）RA 以太网设备驱动（Ethernet Device Driver）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_ETHERNET_RMAC_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_RMAC
CONFIG_USE_RA_FSP_LAYER3_SWITCH
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra_rmac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra_rmac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_USE_RA_FSP_RMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_RMAC)、[`CONFIG_USE_RA_FSP_LAYER3_SWITCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_LAYER3_SWITCH)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_RENESAS_RA_RX_THREAD_PRIORITY"></a>

## 88.81 `CONFIG_ETH_RENESAS_RA_RX_THREAD_PRIORITY`

**提示（Prompt）**：瑞萨（Renesas）RA 以太网接收线程优先级（Receive Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_RENESAS_RA_RMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra_rmac:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra_rmac#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 瑞萨（Renesas）RA 以太网 RMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_RENESAS_RA_RMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA_RMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_RENESAS_RA_RX_THREAD_STACK_SIZE"></a>

## 88.82 `CONFIG_ETH_RENESAS_RA_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：内部传入数据包处理线程的栈大小（Stack Size）

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_RENESAS_RA_RMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra_rmac:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra_rmac#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 瑞萨（Renesas）RA 以太网 RMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_RENESAS_RA_RMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA_RMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_RENESAS_RA_USE_HW_WRITEBACK"></a>

## 88.83 `CONFIG_ETH_RENESAS_RA_USE_HW_WRITEBACK`

**提示（Prompt）**：等待硬件回写以太网缓冲区（Hardware Writeback）

**说明（Help）**

启用此选项，等待以太网描述符回写（Ethernet Descriptor Writeback），确保发送帧（TX Frame）成功写入。启用后，以太网写操作的耗时可能略微增加。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_RENESAS_RA_RMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra_rmac:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra_rmac#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 瑞萨（Renesas）RA 以太网 RMAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_RENESAS_RA_RMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA_RMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_RENESAS_RA_USE_NS_BUF"></a>

## 88.84 `CONFIG_ETH_RENESAS_RA_USE_NS_BUF`

**提示（Prompt）**：使用非安全段（Non-Secure Section）存放缓冲区

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_HAS_TEE && !CONFIG_ARM_SECURE_FIRMWARE && !CONFIG_ARM_NONSECURE_FIRMWARE && CONFIG_ETH_RENESAS_RA && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_RA6M5 || CONFIG_SOC_SERIES_RA6M4
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 瑞萨（Renesas）RA 以太网（Ethernet）

**配置项引用（Symbol References）**：[`CONFIG_CPU_HAS_TEE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_TEE)、[`CONFIG_ARM_SECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_SECURE_FIRMWARE)、[`CONFIG_ARM_NONSECURE_FIRMWARE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_FIRMWARE)、[`CONFIG_ETH_RENESAS_RA`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_SOC_SERIES_RA6M5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M5)、[`CONFIG_SOC_SERIES_RA6M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA6M4)。

<a id="CONFIG_ETH_RENESAS_RX_BUF_NUM"></a>

## 88.85 `CONFIG_ETH_RENESAS_RX_BUF_NUM`

**提示（Prompt）**：接收缓冲区数量（Receive Buffer Count）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_RENESAS_RA && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 瑞萨（Renesas）RA 以太网（Ethernet）

**配置项引用（Symbol References）**：[`CONFIG_ETH_RENESAS_RA`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_RENESAS_TX_BUF_NUM"></a>

## 88.86 `CONFIG_ETH_RENESAS_TX_BUF_NUM`

**提示（Prompt）**：发送缓冲区数量（Transmit Buffer Count）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_RENESAS_RA && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.renesas_ra:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.renesas_ra#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 瑞萨（Renesas）RA 以太网（Ethernet）

**配置项引用（Symbol References）**：[`CONFIG_ETH_RENESAS_RA`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_RENESAS_RA)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS"></a>

## 88.87 `CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS`

**提示（Prompt）**：用于基于 DWC Ethernet QoS 的 Rockchip RK3588 的驱动

**说明（Help）**

在瑞芯微（Rockchip）RK3588 上启用 Synopsys DesignWare MAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_RK3588 && CONFIG_64BIT && DT_HAS_ROCKCHIP_RK3588_GMAC_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_DWC_ETHER_QOS_CORE
CONFIG_CLOCK_CONTROL
CONFIG_RESET
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_SYSCON
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_RK3588`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3588)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_RK3588`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_SAM_GMAC"></a>

## 88.88 `CONFIG_ETH_SAM_GMAC`

**提示（Prompt）**：Atmel SAM 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 Atmel SAM 微控制器（MCU）系列的以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF_FIXED_DATA_SIZE && (DT_HAS_ATMEL_SAM_GMAC_ENABLED || DT_HAS_ATMEL_SAM0_GMAC_ENABLED) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_PINCTRL
```

**弱选择（Implies）**

```text
CONFIG_NVMEM if n || n
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/esp_8266/boards/sam4e_xpro.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/esp_8266/boards/sam4e_xpro.defconfig)。

```text
n
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.sam_gmac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.sam_gmac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_FIXED_DATA_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_FIXED_DATA_SIZE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_SAM_GMAC_BUF_RX_COUNT"></a>

## 88.89 `CONFIG_ETH_SAM_GMAC_BUF_RX_COUNT`

**提示（Prompt）**：SAM ETH 驱动预先分配的网络接收缓冲区（Network RX Buffers）

**说明（Help）**

以太网驱动永久分配的网络缓冲区（Network Buffer）数量。这些缓冲区用于接收路径，由驱动预先分配并提供给 GMAC 模块，用于填入传入数据。其数量必须足以容纳至少一个完整以太网帧（Ethernet Frame）。SAM ETH 驱动始终为自身分配此数量的缓冲区，因此会占用 `NET_BUF_RX_COUNT` 所规定的整个网络协议栈的接收数据缓冲区总量，减少其余可用数量。必须确保 `NET_PKT_RX_COUNT` 足够大，至少可容纳两个以太网帧：一个由 GMAC 模块接收，另一个由上层网络协议栈处理。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_SAM_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.sam_gmac:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.sam_gmac#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Atmel SAM 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_SAM_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_SAM_GMAC_FORCED_QUEUE"></a>

## 88.90 `CONFIG_ETH_SAM_GMAC_FORCED_QUEUE`

**提示（Prompt）**：强制数据包进入的队列（Queue）

**说明（Help）**

强制将数据包路由到哪个队列（Queue）。此设置同时影响发送（TX）队列和接收（RX）队列的配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_SAM_GMAC_FORCE_QUEUE && CONFIG_ETH_SAM_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 1] if CONFIG_ETH_SAM_GMAC_QUEUES = 2
[0, 2] if CONFIG_ETH_SAM_GMAC_QUEUES = 3
[0, 3] if CONFIG_ETH_SAM_GMAC_QUEUES = 4
[0, 4] if CONFIG_ETH_SAM_GMAC_QUEUES = 5
[0, 5] if CONFIG_ETH_SAM_GMAC_QUEUES = 6
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.sam_gmac:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.sam_gmac#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Atmel SAM 以太网驱动（Ethernet Driver） → 强制全部流量经过指定队列（Specific Queue）

**配置项引用（Symbol References）**：[`CONFIG_ETH_SAM_GMAC_FORCE_QUEUE`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC_FORCE_QUEUE)、[`CONFIG_ETH_SAM_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_SAM_GMAC_QUEUES`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC_QUEUES)。

<a id="CONFIG_ETH_SAM_GMAC_FORCE_QUEUE"></a>

## 88.91 `CONFIG_ETH_SAM_GMAC_FORCE_QUEUE`

**提示（Prompt）**：强制全部流量经过指定队列（Specific Queue）

**说明（Help）**

此选项仅用于调试（Debugging）。可用它将全部流量强制路由到指定硬件队列（Hardware Queue），便于验证所选队列是否实际工作。只有启用的接收流量类别（RX Traffic Class）不超过 4 个时才有效，因为 SAM GMAC 硬件最多支持筛选 4 个流量类别。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_SAM_GMAC_QUEUES > 1 && CONFIG_NET_TC_RX_COUNT < 5 && CONFIG_ETH_SAM_GMAC && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.sam_gmac:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.sam_gmac#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Atmel SAM 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_SAM_GMAC_QUEUES`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC_QUEUES)、[`CONFIG_NET_TC_RX_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TC_RX_COUNT)、[`CONFIG_ETH_SAM_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_SAM_GMAC_QUEUES"></a>

## 88.92 `CONFIG_ETH_SAM_GMAC_QUEUES`

**提示（Prompt）**：活动的硬件发送和接收队列数量（Active Hardware TX and RX Queue Count）

**说明（Help）**

选择驱动使用的硬件队列（Hardware Queue）数量。数据包根据自身优先级被路由到相应队列。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_SAM_GMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 0] if CONFIG_SOC_SERIES_SAMX7X || CONFIG_SOC_SERIES_SAM4E || CONFIG_SOC_SERIES_SAME54
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.sam_gmac:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.sam_gmac#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Atmel SAM 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_SAM_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_SAM_GMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_SERIES_SAM4E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4E)、[`CONFIG_SOC_SERIES_SAME54`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME54)。

<a id="CONFIG_ETH_SMSC911X"></a>

## 88.93 `CONFIG_ETH_SMSC911X`

**提示（Prompt）**：SMSC911x/9220 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 SMSC/LAN911x/9220 系列芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SMSC_LAN9220_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_NIC_MODEL_ONBOARD
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.smsc911x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.smsc911x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_NIC_MODEL_ONBOARD`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NIC_MODEL_ONBOARD)。

<a id="CONFIG_ETH_SMSC91X"></a>

## 88.94 `CONFIG_ETH_SMSC91X`

**提示（Prompt）**：SMSC91x 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 SMSC/LAN91x 系列芯片的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SMSC_LAN91C111_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MDIO
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.smsc91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.smsc91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_ETH_STELLARIS"></a>

## 88.95 `CONFIG_ETH_STELLARIS`

**提示（Prompt）**：TI Stellaris 微控制器（MCU）系列的以太网（Ethernet）驱动。

**说明（Help）**

Stellaris 板载以太网控制器（On-Board Ethernet Controller）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_STELLARIS_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_NIC_MODEL_ONBOARD
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stellaris:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stellaris#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_NIC_MODEL_ONBOARD`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NIC_MODEL_ONBOARD)。

<a id="CONFIG_ETH_STM32_DWC_ETHER_1000"></a>

## 88.96 `CONFIG_ETH_STM32_DWC_ETHER_1000`

**提示（Prompt）**：用于基于 DWC 以太网 MAC 的 STM32 的驱动

**说明（Help）**

在 STM32 F1/F2/F4/F7 上启用 Synopsys DesignWare MAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ETH_STM32_HAL && (CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32F4X || CONFIG_SOC_SERIES_STM32F2X || CONFIG_SOC_SERIES_STM32F1X) && DT_HAS_ST_STM32_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_DWC_ETHER_1000_CORE
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT && !n
CONFIG_PINCTRL
CONFIG_RESET
CONFIG_HWINFO
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_HWINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HWINFO)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_STM32_DWC_ETHER_QOS"></a>

## 88.97 `CONFIG_ETH_STM32_DWC_ETHER_QOS`

**提示（Prompt）**：用于基于 DWC Ethernet QoS 的 STM32 的驱动

**说明（Help）**

在 STM32 C5/H5/H7/H7RS/MP13/N6 系列 SoC 上启用 Synopsys DesignWare MAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ETH_STM32_HAL && (CONFIG_SOC_SERIES_STM32C5X || CONFIG_SOC_SERIES_STM32H5X || CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H7RSX || CONFIG_SOC_SERIES_STM32MP13X || CONFIG_SOC_SERIES_STM32N6X) && DT_HAS_ST_STM32_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_DWC_ETHER_QOS_CORE
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_PINCTRL
CONFIG_RESET
CONFIG_HWINFO
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_HWINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HWINFO)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32MP13X`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_STM32_HAL"></a>

## 88.98 `CONFIG_ETH_STM32_HAL`

**提示（Prompt）**：STM32 HAL 以太网驱动（Ethernet Driver）

**说明（Help）**

启用基于 STM32 硬件抽象层（HAL）的以太网驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if !(CONFIG_PTP_CLOCK && (CONFIG_SOC_SERIES_STM32C5X || CONFIG_SOC_SERIES_STM32F1X || CONFIG_SOC_SERIES_STM32F2X || CONFIG_SOC_SERIES_STM32F4X || CONFIG_SOC_SERIES_STM32MP13X))
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_ETH
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_HWINFO
CONFIG_PINCTRL
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET && !CONFIG_SOC_SERIES_STM32H5X
```

**弱选择（Implies）**

```text
CONFIG_NVMEM if n
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_USE_STM32_HAL_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_ETH)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_HWINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HWINFO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32MP13X`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`、`CONFIG_SOC_SERIES_STM32H5X`。

<a id="CONFIG_ETH_STM32_HAL2_API"></a>

## 88.99 `CONFIG_ETH_STM32_HAL2_API`

**提示（Prompt）**：使用官方 STM32Cube2 硬件抽象层（HAL）驱动

**说明（Help）**

使用官方 STM32Cube2 硬件抽象层（HAL）驱动，代替另外两种驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_HAL2 && <choice CONFIG_ETH_STM32_HAL_API_VERSION>
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
CONFIG_USE_STM32_HAL_SBS
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver） → STM32Cube HAL 以太网版本（Ethernet Version）

**配置项引用（Symbol References）**：[`CONFIG_STM32_HAL2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_HAL2)、[`CONFIG_ETH_STM32_HAL_API_VERSION`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_STM32_HAL_API_VERSION)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_USE_STM32_HAL_SBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_SBS)。

<a id="CONFIG_ETH_STM32_HAL_API_V1"></a>

## 88.100 `CONFIG_ETH_STM32_HAL_API_V1`

**提示（Prompt）**：使用旧版 STM32Cube 硬件抽象层（HAL）驱动

**说明（Help）**

以旧版硬件抽象层（HAL）为基础，并将其作为当前官方 API 版本的驱动版本。仅适用于 STM32F1 和 STM32F2 SoC 系列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_STM32F1X || CONFIG_SOC_SERIES_STM32F2X) && <choice CONFIG_ETH_STM32_HAL_API_VERSION>
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.stm32_hal:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.stm32_hal#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → STM32 HAL 以太网驱动（Ethernet Driver） → STM32Cube HAL 以太网版本（Ethernet Version）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_ETH_STM32_HAL_API_VERSION`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_STM32_HAL_API_VERSION)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F2X`。

<!-- kconfig-navigation -->

[上一章](P087_drivers_ethernet_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P089_drivers_ethernet_配置项参考_3.md)
