---
id: learning.zephyr-docs.kconfig-reference.page-87
title: "`drivers/ethernet`配置项参考（1/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第87章\_`drivers/ethernet`配置项参考（1/4）

本章翻译官方 Kconfig 数据库中 `drivers/ethernet` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DSA_DRIVERS"></a>

## 87.1 `CONFIG_DSA_DRIVERS`

**提示（Prompt）**：分布式交换架构（Distributed Switch Architecture，DSA）设备驱动

**说明（Help）**

启用分布式交换架构（Distributed Switch Architecture，DSA）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_NET_DSA
```

**定义位置（Location）**：[`drivers/ethernet/dsa/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dsa/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_DSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DSA)。

<a id="CONFIG_DSA_NXP_IMX_NETC"></a>

## 87.2 `CONFIG_DSA_NXP_IMX_NETC`

**提示（Prompt）**：NXP i.MX NETC 支持

**说明（Help）**

增加 NXP i.MX NETC 分布式交换架构（DSA）设备驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_NETC_SWITCH_ENABLED && CONFIG_DSA_DRIVERS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_PKT_CONTROL_BLOCK if CONFIG_PTP_CLOCK_NXP_NETC
```

**定义位置（Location）**：[`drivers/ethernet/dsa/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dsa/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 分布式交换架构（Distributed Switch Architecture，DSA）设备驱动

**配置项引用（Symbol References）**：[`CONFIG_DSA_DRIVERS`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_DSA_DRIVERS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_PKT_CONTROL_BLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_CONTROL_BLOCK)、[`CONFIG_PTP_CLOCK_NXP_NETC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK_NXP_NETC)。

<a id="CONFIG_DSA_NXP_IMX_NETC_GCL_LEN"></a>

## 87.3 `CONFIG_DSA_NXP_IMX_NETC_GCL_LEN`

**提示（Prompt）**：i.MX NETC 交换机的门控列表长度（Gate Control List Length）

**说明（Help）**

要使用的门控列表（Gate Control List）数量。较小的值可节省 RAM。最大值可以是 `64`、`128` 或 `256`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DSA_NXP_IMX_NETC && CONFIG_NET_QBV && CONFIG_DSA_DRIVERS && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`drivers/ethernet/dsa/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dsa/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 分布式交换架构（Distributed Switch Architecture，DSA）设备驱动 → NXP i.MX NETC 支持

**配置项引用（Symbol References）**：[`CONFIG_DSA_NXP_IMX_NETC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_DSA_NXP_IMX_NETC)、[`CONFIG_NET_QBV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QBV)、[`CONFIG_DSA_DRIVERS`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_DSA_DRIVERS)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_DSA_TAG_PROTOCOL_NETC"></a>

## 87.4 `CONFIG_DSA_TAG_PROTOCOL_NETC`

**提示（Prompt）**：标签协议（Tag Protocol）——NETC

**说明（Help）**

NXP NETC 标签协议（Tag Protocol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_PKT_CONTROL_BLOCK
```

**定义位置（Location）**：[`drivers/ethernet/dsa/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dsa/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 分布式交换架构（Distributed Switch Architecture，DSA）设备驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_CONTROL_BLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_CONTROL_BLOCK)。

<a id="CONFIG_DWMAC_NB_RX_DESCS"></a>

## 87.5 `CONFIG_DWMAC_NB_RX_DESCS`

**提示（Prompt）**：接收描述符环（Receive Descriptor Ring）中的条目数量

**说明（Help）**

收到的数据包会分散存放到所需数量的分片缓冲区（Fragment Buffer）中。每个接收（RX）分片的大小为 `CONFIG_NET_BUF_DATA_SIZE`，每个分片对应一个描述符条目（Descriptor Entry）。较大的数量允许在 CPU 不立即介入时接收更多数据包，但需要更多临时内存（Transient Memory）。较小的数量会增加溢出（Overflow）和丢包风险。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[4, 128]
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_DWMAC_NB_TX_DESCS"></a>

## 87.6 `CONFIG_DWMAC_NB_TX_DESCS`

**提示（Prompt）**：发送描述符环（Transmit Descriptor Ring）中的条目数量

**说明（Help）**

较大的数量允许更多数据包排队，可能提高吞吐量（Throughput），但需要更多临时内存（Transient Memory）。必须有足够的描述符（Descriptor）容纳一个待发送完整大小数据包的全部分片，否则数据包会被丢弃。分片大小受 `CONFIG_NET_BUF_DATA_SIZE` 影响。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[4, 128]
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ADIN1140"></a>

## 87.7 `CONFIG_ETH_ADIN1140`

**提示（Prompt）**：ADIN1140 10BASE-T1S MAC-PHY

**说明（Help）**

ADIN1140 是符合 IEEE 802.3™-2022 的 10BASE-T1S MAC-PHY，用于 10 Mbps 单对线以太网（Single-Pair Ethernet，SPE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADIN1140_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin1140:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin1140#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ETH_ADIN1140_RX_THREAD_PRIO"></a>

## 87.8 `CONFIG_ETH_ADIN1140_RX_THREAD_PRIO`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责 ADIN1140 中断请求（IRQ）处理的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ADIN1140 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin1140:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin1140#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ADIN1140 10BASE-T1S MAC-PHY

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN1140`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN1140)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ADIN1140_RX_THREAD_STACK_SIZE"></a>

## 87.9 `CONFIG_ETH_ADIN1140_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：处理 ADIN1140 中断请求（IRQ）的线程栈大小（Stack Size）

**说明（Help）**

用于处理已触发的 ADIN1140 中断请求（IRQ）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ADIN1140 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin1140:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin1140#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ADIN1140 10BASE-T1S MAC-PHY

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN1140`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN1140)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ADIN1140_TIMEOUT"></a>

## 87.10 `CONFIG_ETH_ADIN1140_TIMEOUT`

**提示（Prompt）**：IP 缓冲区超时时间（IP Buffer Timeout）

**说明（Help）**

超时时间，以毫秒为单位。驱动等待从 IP 协议栈（IP Stack）获得内存缓冲区的最长时间，超过后丢弃以太网帧（Ethernet Frame）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ADIN1140 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin1140:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin1140#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ADIN1140 10BASE-T1S MAC-PHY

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN1140`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN1140)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ADIN2111"></a>

## 87.11 `CONFIG_ETH_ADIN2111`

**提示（Prompt）**：ADIN2111 双端口 10BASE-T1L 控制器（2-Port Controller）

**说明（Help）**

ADIN2111 是面向工业以太网（Industrial Ethernet）应用的低功耗双端口 10BASE-T1L 收发器（Transceiver），符合用于远距离 10 Mbps 单对线以太网（Single-Pair Ethernet，SPE）的 IEEE® 802.3cg-2019™ 以太网标准。ADIN2111 集成媒体访问控制（Media Access Control，MAC）和交换机（Switch），可通过串行外设接口（Serial Peripheral Interface，SPI）直接连接多种控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_ADIN2111_ENABLED || DT_HAS_ADI_ADIN1110_ENABLED) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**弱选择（Implies）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin2111:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin2111#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_ETH_ADIN2111_BUFFER_SIZE"></a>

## 87.12 `CONFIG_ETH_ADIN2111_BUFFER_SIZE`

**提示（Prompt）**：帧发送缓冲区大小（Frame Transmission Buffer Size），以字节为单位

**说明（Help）**

发送和接收缓冲区大小（Transmission and Reception Buffer Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ADIN2111 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1524
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin2111:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin2111#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ADIN2111 双端口 10BASE-T1L 控制器（2-Port Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN2111`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN2111)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ADIN2111_IRQ_THREAD_PRIO"></a>

## 87.13 `CONFIG_ETH_ADIN2111_IRQ_THREAD_PRIO`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责 ADIN INT 中断请求（IRQ）处理的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ADIN2111 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin2111:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin2111#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ADIN2111 双端口 10BASE-T1L 控制器（2-Port Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN2111`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN2111)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ADIN2111_IRQ_THREAD_STACK_SIZE"></a>

## 87.14 `CONFIG_ETH_ADIN2111_IRQ_THREAD_STACK_SIZE`

**提示（Prompt）**：处理 ADIN 中断请求（IRQ）的线程栈大小（Stack Size）

**说明（Help）**

用于处理已触发的 INT 中断请求（IRQ）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ADIN2111 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin2111:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin2111#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ADIN2111 双端口 10BASE-T1L 控制器（2-Port Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN2111`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN2111)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ADIN2111_SPI_CFG0"></a>

## 87.15 `CONFIG_ETH_ADIN2111_SPI_CFG0`

**提示（Prompt）**：SPI_CFG0

**说明（Help）**

当 ADIN 在 SPI 主机接口（Host Interface）上使用 8 位循环冗余校验（CRC，通用 SPI）或保护模式（Protection Mode，OPEN Alliance）时，必须设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ADIN2111 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin2111:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin2111#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ADIN2111 双端口 10BASE-T1L 控制器（2-Port Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN2111`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN2111)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ADIN2111_TIMEOUT"></a>

## 87.16 `CONFIG_ETH_ADIN2111_TIMEOUT`

**提示（Prompt）**：IP 缓冲区超时时间（IP Buffer Timeout）

**说明（Help）**

给定超时时间，以毫秒为单位。驱动等待从 IP 协议栈（IP Stack）获得内存缓冲区的最长时间，超过后丢弃以太网帧（Ethernet Frame）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ADIN2111 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.adin2111:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.adin2111#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ADIN2111 双端口 10BASE-T1L 控制器（2-Port Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ADIN2111`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN2111)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_BCMGENET"></a>

## 87.17 `CONFIG_ETH_BCMGENET`

**提示（Prompt）**：Broadcom GENET 千兆以太网驱动（Gigabit Ethernet Driver）

**说明（Help）**

启用 Broadcom GENET 千兆以太网（Gigabit Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_GENET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.bcmgenet:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.bcmgenet#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_BCMGENET_RX_POLLING_INTERVAL_US"></a>

## 87.18 `CONFIG_ETH_BCMGENET_RX_POLLING_INTERVAL_US`

**提示（Prompt）**：接收轮询间隔（Receive Polling Interval），以微秒为单位

**说明（Help）**

接收轮询间隔（Receive Polling Interval），以微秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_BCMGENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[100, 1000]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.bcmgenet:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.bcmgenet#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Broadcom GENET 千兆以太网驱动（Gigabit Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_BCMGENET`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_BCMGENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_BCMGENET_RX_THREAD_PRIORITY"></a>

## 87.19 `CONFIG_ETH_BCMGENET_RX_THREAD_PRIORITY`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_BCMGENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.bcmgenet:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.bcmgenet#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Broadcom GENET 千兆以太网驱动（Gigabit Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_BCMGENET`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_BCMGENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_BCMGENET_RX_THREAD_STACK_SIZE"></a>

## 87.20 `CONFIG_ETH_BCMGENET_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：内部传入数据包处理线程的栈大小（Stack Size）

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_BCMGENET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.bcmgenet:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.bcmgenet#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Broadcom GENET 千兆以太网驱动（Gigabit Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_BCMGENET`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_BCMGENET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_CH9120"></a>

## 87.21 `CONFIG_ETH_CH9120`

**提示（Prompt）**：CH9120 以太网驱动（Ethernet Driver）

**说明（Help）**

此驱动将以太网套接字（Ethernet Socket）处理卸载（Offload）到 CH9120 芯片。注意：该芯片同一时刻只支持一个 TCP/UDP 客户端连接（Client Connection），尝试打开第二个套接字会失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_CH9120_ENABLED && CONFIG_SERIAL_SUPPORT_INTERRUPT && CONFIG_ETH_DRIVER
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
CONFIG_NET_SOCKETS_OFFLOAD
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`drivers/ethernet/offload/Kconfig.wch9120:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/offload/Kconfig.wch9120#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_ETH_CH9120_RX_BUF_SIZE"></a>

## 87.22 `CONFIG_ETH_CH9120_RX_BUF_SIZE`

**提示（Prompt）**：接收环形缓冲区大小（RX Ring Buffer Size），以字节为单位

**说明（Help）**

接收环形缓冲区（Receive Ring Buffer）的大小。如果高吞吐量下发生数据丢失，应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_CH9120 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[256, 4096]
```

**定义位置（Location）**：[`drivers/ethernet/offload/Kconfig.wch9120:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/offload/Kconfig.wch9120#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → CH9120 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_CH9120`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_CH9120)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_CVSX_NB_RX_DESCS"></a>

## 87.23 `CONFIG_ETH_CVSX_NB_RX_DESCS`

**提示（Prompt）**：接收描述符环（Receive Descriptor Ring）中的条目数量

**说明（Help）**

收到的数据包会分散存放到所需数量的分片缓冲区（Fragment Buffer）中。每个接收（RX）分片的大小为 `CONFIG_NET_BUF_DATA_SIZE`，每个分片对应一个描述符条目（Descriptor Entry）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_CYCLONEV && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[4, 128]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.cyclonev:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.cyclonev#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Cyclone V 以太网 MAC 驱动（Ethernet MAC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_CYCLONEV`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_CYCLONEV)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_CVSX_NB_TX_DESCS"></a>

## 87.24 `CONFIG_ETH_CVSX_NB_TX_DESCS`

**提示（Prompt）**：发送描述符环（Transmit Descriptor Ring）中的条目数量

**说明（Help）**

较大的数量允许更多数据包排队，可能提高吞吐量（Throughput），但需要更多临时内存（Transient Memory）。必须有足够的描述符（Descriptor）容纳一个待发送完整大小数据包的全部分片，否则数据包会被丢弃。分片大小受 `CONFIG_NET_BUF_DATA_SIZE` 影响。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_CYCLONEV && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[4, 128]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.cyclonev:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.cyclonev#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Cyclone V 以太网 MAC 驱动（Ethernet MAC Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_CYCLONEV`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_CYCLONEV)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_CYCLONEV"></a>

## 87.25 `CONFIG_ETH_CYCLONEV`

**提示（Prompt）**：Cyclone V 以太网 MAC 驱动（Ethernet MAC Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_ETHERNET_CYCLONEV_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.cyclonev:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.cyclonev#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

<a id="CONFIG_ETH_DM9051"></a>

## 87.26 `CONFIG_ETH_DM9051`

**提示（Prompt）**：Davicom DM9051 以太网控制器（Ethernet Controller）

**说明（Help）**

具有 SPI 接口的 Davicom DM9051 以太网控制器（Ethernet Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_DAVICOM_DM9051_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.dm9051:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.dm9051#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ETH_DM9051_RX_THREAD_PRIORITY"></a>

## 87.27 `CONFIG_ETH_DM9051_RX_THREAD_PRIORITY`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DM9051 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.dm9051:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.dm9051#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Davicom DM9051 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DM9051`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DM9051)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DM9051_RX_THREAD_STACK_SIZE"></a>

## 87.28 `CONFIG_ETH_DM9051_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：内部传入数据包处理线程的栈大小（Stack Size）

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DM9051 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.dm9051:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.dm9051#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Davicom DM9051 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DM9051`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DM9051)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DM9051_TIMEOUT"></a>

## 87.29 `CONFIG_ETH_DM9051_TIMEOUT`

**提示（Prompt）**：IP 缓冲区超时时间（IP Buffer Timeout）

**说明（Help）**

给定超时时间，以毫秒为单位。驱动等待从 IP 协议栈（IP Stack）获得内存缓冲区的最长时间，超过后丢弃以太网帧（Ethernet Frame）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DM9051 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.dm9051:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.dm9051#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Davicom DM9051 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DM9051`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DM9051)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DRIVER"></a>

## 87.30 `CONFIG_ETH_DRIVER`

**提示（Prompt）**：以太网驱动（Ethernet Drivers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING && !CONFIG_NET_TEST
```

**被弱选择（Implied by）**

```text
CONFIG_NET_QEMU_ETHERNET
CONFIG_NET_QEMU_USER
CONFIG_NET_SLIP_TAP
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/arceli_eth_w5500/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/arceli_eth_w5500/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/esp_8266/boards/sam4e_xpro.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/esp_8266/boards/sam4e_xpro.defconfig)。

```text
n
```

来源：[`boards/shields/frdm_cr20a/boards/frdm_k64f.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/frdm_cr20a/boards/frdm_k64f.defconfig)。

```text
n
```

来源：[`boards/shields/inventek_eswifi/boards/frdm_k64f.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/inventek_eswifi/boards/frdm_k64f.defconfig)。

```text
n
```

来源：[`boards/shields/inventek_eswifi/boards/nucleo_f767zi.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/inventek_eswifi/boards/nucleo_f767zi.defconfig)。

```text
n
```

来源：[`boards/shields/link_board_eth/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/link_board_eth/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/mikroe_eth3_click/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mikroe_eth3_click/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/mikroe_eth_click/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mikroe_eth_click/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/mikroe_two_wire_eth_click/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mikroe_two_wire_eth_click/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/seeed_w5500/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/seeed_w5500/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/wiznet_w5500/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/wiznet_w5500/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TEST)、[`CONFIG_NET_QEMU_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_ETHERNET)、[`CONFIG_NET_QEMU_USER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_USER)、[`CONFIG_NET_SLIP_TAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SLIP_TAP)。

<a id="CONFIG_ETH_DRIVER_RAW_MODE"></a>

## 87.31 `CONFIG_ETH_DRIVER_RAW_MODE`

**提示（Prompt）**：不带 MAC 协议栈（MAC Stack）的以太网驱动

**说明（Help）**

此选项允许在所谓的原始模式（Raw Mode）下使用驱动，即不带 MAC 协议栈（MAC Stack）；以太网的网络二层（Net L2）不会参与构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_L2_ETHERNET && CONFIG_ETH_DRIVER
```

**主动选择（Selects）**

```text
CONFIG_NET_RAW_MODE
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)。

<a id="CONFIG_ETH_DWC_ETHER_1000_CORE"></a>

## 87.32 `CONFIG_ETH_DWC_ETHER_1000_CORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

这是 Synopsys DesignWare Ethernet MAC 10/100/1G Universal 的驱动，该 IP 也称为 `dwc_ether_mac10_100_1000_universal`。支持 IP 版本 v3.x。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF_FIXED_DATA_SIZE && CONFIG_ETH_DRIVER
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
CONFIG_ARM_MPU if CONFIG_CPU_HAS_ARM_MPU && CONFIG_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_ETH_ESP32_DWC_ETHER_1000
CONFIG_ETH_XMC_DWC_ETHER_1000
CONFIG_ETH_NUMAKER_DWC_ETHER_1000
CONFIG_ETH_STM32_DWC_ETHER_1000
```

**弱选择（Implies）**

```text
CONFIG_NVMEM if n
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_FIXED_DATA_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_FIXED_DATA_SIZE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_ARM_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_ETH_ESP32_DWC_ETHER_1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32_DWC_ETHER_1000)、[`CONFIG_ETH_XMC_DWC_ETHER_1000`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XMC_DWC_ETHER_1000)、[`CONFIG_ETH_NUMAKER_DWC_ETHER_1000`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NUMAKER_DWC_ETHER_1000)、[`CONFIG_ETH_STM32_DWC_ETHER_1000`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_DWC_ETHER_1000)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)。

<a id="CONFIG_ETH_DWC_ETHER_1000_CORE_EDFE"></a>

## 87.33 `CONFIG_ETH_DWC_ETHER_1000_CORE_EDFE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将描述符大小（Descriptor Size）增加到 32 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_ETHER_1000_CORE && !CONFIG_SOC_SERIES_STM32F1X && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if CONFIG_PTP_CLOCK_DWC_MAC
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PTP_CLOCK_DWC_MAC`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F1X`。

<a id="CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER"></a>

## 87.34 `CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER`

**提示（Prompt）**：组播过滤（Multicast Filtering）支持

**说明（Help）**

在 MAC 中启用组播过滤（Multicast Filtering），仅接收协议栈所监听地址的组播。如果禁用此项，或者硬件完全不支持过滤，MAC 将接收全部组播。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED || CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT_SUPPORTED) && CONFIG_NET_L2_ETHERNET && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.mcast:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.mcast#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED)、[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT_SUPPORTED`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH"></a>

## 87.35 `CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH`

**提示（Prompt）**：哈希过滤（Hash Filtering）

**说明（Help）**

根据目标 MAC 地址（Destination MAC Address）计算出的哈希值（Hash），执行非精确组播过滤（Imperfect Multicast Filtering）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED && <choice CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.mcast:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.mcast#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → 组播过滤（Multicast Filtering）支持 → 组播过滤模式（Multicast Filter Mode）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED)、[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_MODE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_MODE)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED"></a>

## 87.36 `CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

硬件能够对组播地址（Multicast Address）进行哈希处理，此能力由设备树（Devicetree）属性 `snps,multicast-filter-bins` 表示。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.mcast:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.mcast#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_MODE"></a>

## 87.37 `CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_MODE`

**提示（Prompt）**：组播过滤模式（Multicast Filter Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH if CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED
CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT
```

**可选项（Choices）**

```text
CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH
CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.mcast:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.mcast#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → 组播过滤（Multicast Filtering）支持

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH)、[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH_SUPPORTED)、[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT)。

<a id="CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT"></a>

## 87.38 `CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT`

**提示（Prompt）**：精确过滤（Perfect Filtering）

**说明（Help）**

利用硬件中剩余的 MAC 地址条目（Spare MAC Address Entry）进行精确组播过滤（Perfect Multicast Filtering）。一旦这些条目无法容纳所有地址，就改为接收全部组播。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT_SUPPORTED && <choice CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_MODE>
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.mcast:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.mcast#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动 → 组播过滤（Multicast Filtering）支持 → 组播过滤模式（Multicast Filter Mode）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT_SUPPORTED`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT_SUPPORTED)、[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_MODE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_MODE)。

<a id="CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT_SUPPORTED"></a>

## 87.39 `CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_PERFECT_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

硬件具有可用于精确过滤（Perfect Filtering）组播地址的剩余 MAC 地址条目，意味着设备树（Devicetree）属性 `snps,perfect-filter-entries` 大于 `1`，因为条目 `0` 保存站点地址（Station Address）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
!n
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig.mcast:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig.mcast#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_ETHER_QOS_CORE"></a>

## 87.40 `CONFIG_ETH_DWC_ETHER_QOS_CORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

这是 Synopsys DesignWare Ethernet MAC 10/100/1G Quality-of-Service 的驱动，该 IP 也称为 `dwc_ether_qos`。支持 IP 版本 v4.x 和 v5.x。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF_FIXED_DATA_SIZE && CONFIG_ETH_DRIVER
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
CONFIG_ARM_MPU if CONFIG_CPU_HAS_ARM_MPU && CONFIG_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_ETH_NXP_DWC_ETHER_QOS
CONFIG_ETH_STM32_DWC_ETHER_QOS
CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS
CONFIG_ETH_DWMAC_MMU
```

**弱选择（Implies）**

```text
CONFIG_NVMEM if n
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_FIXED_DATA_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_FIXED_DATA_SIZE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_CPU_HAS_ARM_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_ETH_NXP_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_DWC_ETHER_QOS)、[`CONFIG_ETH_STM32_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_DWC_ETHER_QOS)、[`CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS)、[`CONFIG_ETH_DWMAC_MMU`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWMAC_MMU)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)。

<a id="CONFIG_ETH_DWC_ETHER_RX_HW_CHECKSUM"></a>

## 87.41 `CONFIG_ETH_DWC_ETHER_RX_HW_CHECKSUM`

**提示（Prompt）**：使用接收硬件校验和（RX Hardware Checksum）

**说明（Help）**

启用接收校验和卸载（Receive Checksum Offload），以提高吞吐性能（Throughput Performance）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

<a id="CONFIG_ETH_DWC_ETHER_TX_HW_CHECKSUM"></a>

## 87.42 `CONFIG_ETH_DWC_ETHER_TX_HW_CHECKSUM`

**提示（Prompt）**：使用发送硬件校验和（TX Hardware Checksum）

**说明（Help）**

启用发送校验和卸载（Transmit Checksum Offload），以提高吞吐性能（Throughput Performance）。仅在发送使用存储转发模式（Store and Forward Mode）时支持；如果发送 FIFO 小于最大帧大小，则无法使用该模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_ESP32 && !CONFIG_SOC_SERIES_ESP32P4 && (CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_ETH_DWC_XGMAC"></a>

## 87.43 `CONFIG_ETH_DWC_XGMAC`

**提示（Prompt）**：Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**说明（Help）**

这是 Synopsys DesignWare XGMAC 的驱动，该硬件也称为“DesignWare Cores Ethernet XGMAC”。支持硬件版本 3.x，还需要平台专用适配层（Platform-Specific Glue）支持。目前此驱动适用于采用 Intel Agilex5 系列的目标平台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DWCXGMAC_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

<a id="CONFIG_ETH_DWC_XGMAC_ARP_OFFLOAD"></a>

## 87.44 `CONFIG_ETH_DWC_XGMAC_ARP_OFFLOAD`

**提示（Prompt）**：地址解析协议卸载（ARP Offload）

**说明（Help）**

启用地址解析协议（ARP）的硬件卸载（Hardware Offloading）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_XGMAC_BOTTOM_HALF_WORK_QUEUE"></a>

## 87.45 `CONFIG_ETH_DWC_XGMAC_BOTTOM_HALF_WORK_QUEUE`

**提示（Prompt）**：中断下半部工作队列（IRQ Bottom Half Work Queue）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_XGMAC_HW_FILTERING"></a>

## 87.46 `CONFIG_ETH_DWC_XGMAC_HW_FILTERING`

**提示（Prompt）**：硬件二层过滤（H/W L2 Filtering）

**说明（Help）**

启用对数据包进行二层过滤（L2 Filtering）的硬件支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_XGMAC_HW_L3_L4_FILTERING"></a>

## 87.47 `CONFIG_ETH_DWC_XGMAC_HW_L3_L4_FILTERING`

**提示（Prompt）**：硬件三层/四层过滤（H/W L3 L4 Filtering）

**说明（Help）**

启用对数据包进行三层/四层过滤（L3/L4 Filtering）的硬件支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_XGMAC_INTERRUPT_POLLING_INTERVAL_US"></a>

## 87.48 `CONFIG_ETH_DWC_XGMAC_INTERRUPT_POLLING_INTERVAL_US`

**提示（Prompt）**：XGMAC 中断轮询间隔（Interrupt Polling Interval），以微秒为单位

**说明（Help）**

XGMAC 中断轮询间隔（Interrupt Polling Interval），以微秒为单位

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_XGMAC_POLLING_MODE && CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver） → 轮询模式（Polling Mode）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_XGMAC_POLLING_MODE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC_POLLING_MODE)、[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_XGMAC_POLLING_MODE"></a>

## 87.49 `CONFIG_ETH_DWC_XGMAC_POLLING_MODE`

**提示（Prompt）**：轮询模式（Polling Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_XGMAC_PROMISCUOUS_EXCEPTION"></a>

## 87.50 `CONFIG_ETH_DWC_XGMAC_PROMISCUOUS_EXCEPTION`

**提示（Prompt）**：混杂模式（Promiscuous mode）

**说明（Help）**

禁用 XGMAC 设备的混杂模式（Promiscuous Mode）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PROMISCUOUS_MODE && CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_NET_PROMISCUOUS_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PROMISCUOUS_MODE)、[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_XGMAC_RX_CS_OFFLOAD"></a>

## 87.51 `CONFIG_ETH_DWC_XGMAC_RX_CS_OFFLOAD`

**提示（Prompt）**：接收校验和卸载（RX Checksum Offload）

**说明（Help）**

为 TCP/UDP/IP 数据包启用接收校验和卸载（Receive Checksum Offload）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD && CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_NET_CHECKSUM_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD)、[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_XGMAC_SW_RESET_TIMEOUT"></a>

## 87.52 `CONFIG_ETH_DWC_XGMAC_SW_RESET_TIMEOUT`

**提示（Prompt）**：检查软件复位状态（Software Reset Status）的超时时间，以微秒为单位

**说明（Help）**

检查软件复位状态（Software Reset Status）的超时时间，以毫秒为单位

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWC_XGMAC_TX_CS_OFFLOAD"></a>

## 87.53 `CONFIG_ETH_DWC_XGMAC_TX_CS_OFFLOAD`

**提示（Prompt）**：发送校验和卸载（TX Checksum Offload）

**说明（Help）**

为 TCP/UDP/IP 数据包启用发送校验和卸载（Transmit Checksum Offload）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD && CONFIG_ETH_DWC_XGMAC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/dwc_xgmac/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → DWC XGMAC 配置（Configuration） → Synopsys DesignWareCore XGMAC 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_NET_CHECKSUM_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD)、[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWMAC_MMU"></a>

## 87.54 `CONFIG_ETH_DWMAC_MMU`

**提示（Prompt）**：用于基于 MMU 的平台的 Synopsys DesignWare MAC 驱动

**说明（Help）**

在基于内存管理单元（MMU）的平台上启用 Synopsys DesignWare MAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MMU && DT_HAS_SNPS_DESIGNWARE_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_DWC_ETHER_QOS_CORE
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)。

<a id="CONFIG_ETH_DWMAC_RX_REFILL_IRQ"></a>

## 87.55 `CONFIG_ETH_DWMAC_RX_REFILL_IRQ`

**提示（Prompt）**：在中断中补充接收缓冲区（Receive Buffer Refill）

**说明（Help）**

尽可能在接收（RX）中断中补充接收缓冲池（Receive Buffer Pool）；否则在补充线程（Refill Thread）中进行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_DWMAC_RX_REFILL_THREAD_PRIORITY"></a>

## 87.56 `CONFIG_ETH_DWMAC_RX_REFILL_THREAD_PRIORITY`

**提示（Prompt）**：接收缓冲区补充线程优先级（Receive Buffer Refill Thread Priority）

**说明（Help）**

用于补充接收缓冲池（Receive Buffer Pool）的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_ETH_DWC_ETHER_QOS_CORE || CONFIG_ETH_DWC_ETHER_1000_CORE) && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_DWC_ETHER_QOS_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_QOS_CORE)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_E1000"></a>

## 87.57 `CONFIG_ETH_E1000`

**提示（Prompt）**：Intel® PRO/1000 千兆以太网驱动（Gigabit Ethernet Driver）

**说明（Help）**

启用 Intel® PRO/1000 千兆以太网（Gigabit Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_E1000_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y if !CONFIG_NET_QEMU_SLIP
```

**主动选择（Selects）**

```text
CONFIG_PCIE
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.e1000:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.e1000#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_QEMU_SLIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_SLIP)、[`CONFIG_PCIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE)。

<a id="CONFIG_ETH_E1000_PTP_CLOCK"></a>

## 87.58 `CONFIG_ETH_E1000_PTP_CLOCK`

**提示（Prompt）**：精密时间协议时钟驱动支持（PTP Clock Driver Support）【实验性】

**说明（Help）**

启用精密时间协议（PTP）时钟支持。这目前仍是一个仅用于调试的空实现（Dummy），不执行实际的 PTP 操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK && CONFIG_ETH_E1000 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.e1000:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.e1000#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Intel® PRO/1000 千兆以太网驱动（Gigabit Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK)、[`CONFIG_ETH_E1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_E1000)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_ETH_E1000_PTP_CLOCK_SRC_HZ"></a>

## 87.59 `CONFIG_ETH_E1000_PTP_CLOCK_SRC_HZ`

**提示（Prompt）**：PTP 定时器时钟源频率（Clock Source Frequency）

**说明（Help）**

设置提供给精密时间协议（PTP）定时器的时钟频率，以 Hz 为单位。数值设置正确时，定时器才能准确计时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_E1000_PTP_CLOCK && CONFIG_ETH_E1000 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
50000000
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.e1000:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.e1000#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Intel® PRO/1000 千兆以太网驱动（Gigabit Ethernet Driver） → 精密时间协议时钟驱动支持（PTP Clock Driver Support）【实验性】

**配置项引用（Symbol References）**：[`CONFIG_ETH_E1000_PTP_CLOCK`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_E1000_PTP_CLOCK)、[`CONFIG_ETH_E1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_E1000)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_E1000_RX_QUEUE_SIZE"></a>

## 87.60 `CONFIG_ETH_E1000_RX_QUEUE_SIZE`

**提示（Prompt）**：接收队列大小（Receive Queue Size）

**说明（Help）**

设置接收描述符队列（Receive Descriptor Queue）的大小。必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_E1000 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.e1000:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.e1000#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Intel® PRO/1000 千兆以太网驱动（Gigabit Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_E1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_E1000)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_E1000_TX_QUEUE_SIZE"></a>

## 87.61 `CONFIG_ETH_E1000_TX_QUEUE_SIZE`

**提示（Prompt）**：发送队列大小（Transmit Queue Size）

**说明（Help）**

设置发送描述符队列（Transmit Descriptor Queue）的大小。必须是 `8` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_E1000 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.e1000:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.e1000#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Intel® PRO/1000 千兆以太网驱动（Gigabit Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_E1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_E1000)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_E1000_VERBOSE_DEBUG"></a>

## 87.62 `CONFIG_ETH_E1000_VERBOSE_DEBUG`

**提示（Prompt）**：收发帧的十六进制转储（Hexdump）

**说明（Help）**

启用此项会打开对接收帧和发送帧的十六进制转储（Hexdump）。不要在生产环境中保持启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_E1000 && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.e1000:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.e1000#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Intel® PRO/1000 千兆以太网驱动（Gigabit Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_E1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_E1000)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ENC28J60"></a>

## 87.63 `CONFIG_ETH_ENC28J60`

**提示（Prompt）**：ENC28J60C 以太网控制器（Ethernet Controller）

**说明（Help）**

具有 SPI 接口的 ENC28J60C 独立以太网控制器（Stand-Alone Ethernet Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_ENC28J60_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.enc28j60:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.enc28j60#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ETH_ENC28J60_CLKRDY_INIT_WAIT_MS"></a>

## 87.64 `CONFIG_ETH_ENC28J60_CLKRDY_INIT_WAIT_MS`

**提示（Prompt）**：驱动初始化时等待 `CLKRDY` 位的时间

**说明（Help）**

超时时间，以毫秒为单位。驱动初始化等待振荡器启动定时器（OST）到期的最长时间，到期由 `CLKRDY` 位置位表示。超时后，驱动初始化失败并返回 `-ETIMEDOUT`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ENC28J60 && CONFIG_ETH_ENC28J60 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.enc28j60:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.enc28j60#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ENC28J60C 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ENC28J60`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ENC28J60)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ENC28J60_RX_THREAD_PRIO"></a>

## 87.65 `CONFIG_ETH_ENC28J60_RX_THREAD_PRIO`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ENC28J60 && CONFIG_ETH_ENC28J60 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.enc28j60:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.enc28j60#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ENC28J60C 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ENC28J60`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ENC28J60)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ENC28J60_RX_THREAD_STACK_SIZE"></a>

## 87.66 `CONFIG_ETH_ENC28J60_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：内部传入数据包处理线程的栈大小（Stack Size）

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ENC28J60 && CONFIG_ETH_ENC28J60 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.enc28j60:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.enc28j60#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ENC28J60C 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ENC28J60`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ENC28J60)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ENC28J60_TIMEOUT"></a>

## 87.67 `CONFIG_ETH_ENC28J60_TIMEOUT`

**提示（Prompt）**：IP 缓冲区超时时间（IP Buffer Timeout）

**说明（Help）**

给定超时时间，以毫秒为单位。驱动等待从 IP 协议栈（IP Stack）获得内存缓冲区的最长时间，超过后丢弃以太网帧（Ethernet Frame）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ENC28J60 && CONFIG_ETH_ENC28J60 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.enc28j60:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.enc28j60#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ENC28J60C 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ENC28J60`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ENC28J60)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ENC424J600"></a>

## 87.68 `CONFIG_ETH_ENC424J600`

**提示（Prompt）**：ENC424J600C 以太网控制器（Ethernet Controller）

**说明（Help）**

具有 SPI 接口的 ENC424J600C 独立以太网控制器（Stand-Alone Ethernet Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_ENC424J600_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.enc424j600:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.enc424j600#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ETH_ENC424J600_RX_THREAD_PRIO"></a>

## 87.69 `CONFIG_ETH_ENC424J600_RX_THREAD_PRIO`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ENC424J600 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.enc424j600:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.enc424j600#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ENC424J600C 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ENC424J600`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ENC424J600)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ENC424J600_RX_THREAD_STACK_SIZE"></a>

## 87.70 `CONFIG_ETH_ENC424J600_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：内部传入数据包处理线程的栈大小（Stack Size）

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ENC424J600 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.enc424j600:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.enc424j600#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ENC424J600C 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ENC424J600`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ENC424J600)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ENC424J600_TIMEOUT"></a>

## 87.71 `CONFIG_ETH_ENC424J600_TIMEOUT`

**提示（Prompt）**：IP 缓冲区超时时间（IP Buffer Timeout）

**说明（Help）**

给定超时时间，以毫秒为单位。驱动等待从 IP 协议栈（IP Stack）获得内存缓冲区的最长时间，超过后丢弃以太网帧（Ethernet Frame）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ENC424J600 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.enc424j600:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.enc424j600#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ENC424J600C 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ENC424J600`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ENC424J600)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ESP32"></a>

## 87.72 `CONFIG_ETH_ESP32`

**提示（Prompt）**：ESP32 以太网驱动（Ethernet Driver）

**说明（Help）**

启用 ESP32 以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32P4) && DT_HAS_ESPRESSIF_ESP32_ETH_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.esp32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.esp32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_ETH_ESP32_DMA_BUFFER_SIZE"></a>

## 87.73 `CONFIG_ETH_ESP32_DMA_BUFFER_SIZE`

**提示（Prompt）**：以太网 DMA 缓冲区大小（DMA Buffer Size），以字节为单位

**说明（Help）**

设置以太网 MAC DMA 使用的每个缓冲区（Buffer）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ESP32 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[256, 1600]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.esp32:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.esp32#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ESP32 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ESP32`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ESP32_DMA_RX_BUFFER_NUM"></a>

## 87.74 `CONFIG_ETH_ESP32_DMA_RX_BUFFER_NUM`

**提示（Prompt）**：以太网 DMA 接收缓冲区数量（Rx Buffer Count）

**说明（Help）**

DMA 接收缓冲区（Receive Buffer）的数量。每个缓冲区的大小为 `ETH_ESP32_DMA_BUFFER_SIZE`。增加缓冲区数量可能在一定程度上提高吞吐量（Throughput）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ESP32 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[3, 30]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.esp32:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.esp32#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ESP32 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ESP32`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ESP32_DMA_TX_BUFFER_NUM"></a>

## 87.75 `CONFIG_ETH_ESP32_DMA_TX_BUFFER_NUM`

**提示（Prompt）**：以太网 DMA 发送缓冲区数量（Tx Buffer Count）

**说明（Help）**

DMA 发送缓冲区（Transmit Buffer）的数量。每个缓冲区的大小为 `ETH_ESP32_DMA_BUFFER_SIZE`。增加缓冲区数量可能在一定程度上提高吞吐量（Throughput）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ESP32 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[3, 30]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.esp32:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.esp32#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ESP32 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ESP32`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ESP32_DWC_ETHER_1000"></a>

## 87.76 `CONFIG_ETH_ESP32_DWC_ETHER_1000`

**提示（Prompt）**：用于基于 DWC 以太网 MAC 的 ESP32 的驱动

**说明（Help）**

为 ESP32 SoC 启用 Synopsys DesignWare MAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ETH_ESP32 && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32P4) && DT_HAS_ESPRESSIF_ESP32_ETH_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ETH_DWC_ETHER_1000_CORE
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/ethernet/dwc_mac/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_mac/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Synopsys DesignWare MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_ESP32`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETH_DWC_ETHER_1000_CORE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_1000_CORE)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_ETH_ESP32_RX_THREAD_PRIORITY"></a>

## 87.77 `CONFIG_ETH_ESP32_RX_THREAD_PRIORITY`

**提示（Prompt）**：ESP32 以太网接收线程优先级（Receive Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ESP32 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.esp32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.esp32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ESP32 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ESP32`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_ESP32_RX_THREAD_STACK_SIZE"></a>

## 87.78 `CONFIG_ETH_ESP32_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：ESP32 以太网接收线程栈大小（Receive Thread Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_ESP32 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
768
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.esp32:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.esp32#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → ESP32 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_ESP32`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_GECKO"></a>

## 87.79 `CONFIG_ETH_GECKO`

**提示（Prompt）**：Silabs Gecko 以太网驱动（Ethernet Driver）

**说明（Help）**

为 Silicon Labs Gecko 芯片启用以太网（Ethernet）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_ETHERNET_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.gecko:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.gecko#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_GECKO_CARRIER_CHECK_RX_IDLE_TIMEOUT_MS"></a>

## 87.80 `CONFIG_ETH_GECKO_CARRIER_CHECK_RX_IDLE_TIMEOUT_MS`

**提示（Prompt）**：载波检查超时周期（Carrier Check Timeout Period），以毫秒为单位

**说明（Help）**

设置接收空闲超时周期（RX Idle Timeout Period），以毫秒为单位；超过此时间后，重新评估物理层器件（PHY）的载波状态（Carrier Status）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_GECKO && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[100, 30000]
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.gecko:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.gecko#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Silabs Gecko 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_GECKO`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_GECKO)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_GECKO_RX_THREAD_PRIO"></a>

## 87.81 `CONFIG_ETH_GECKO_RX_THREAD_PRIO`

**提示（Prompt）**：接收线程优先级（RX Thread Priority）

**说明（Help）**

接收线程优先级（RX Thread Priority）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_GECKO && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.gecko:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.gecko#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Silabs Gecko 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_GECKO`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_GECKO)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_GECKO_RX_THREAD_STACK_SIZE"></a>

## 87.82 `CONFIG_ETH_GECKO_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

接收线程栈大小（RX Thread Stack Size）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_GECKO && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.gecko:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.gecko#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Silabs Gecko 以太网驱动（Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_GECKO`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_GECKO)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_INIT_PRIORITY"></a>

## 87.83 `CONFIG_ETH_INIT_PRIORITY`

**提示（Prompt）**：以太网驱动初始化优先级（Ethernet Driver Init Priority）

**说明（Help）**

以太网设备驱动的初始化优先级（Initialization Priority）。除非了解修改的影响，否则不要更改此值。此优先级的数值必须小于网络协议栈（Network Stack）的对应数值，以便驱动在网络子系统（Networking Subsystem）之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET || CONFIG_ETH_DRIVER || CONFIG_MDIO
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_MDIO`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO)。

<a id="CONFIG_ETH_INTEL_IGC"></a>

## 87.84 `CONFIG_ETH_INTEL_IGC`

**提示（Prompt）**：Intel IGC MAC 驱动

**说明（Help）**

Intel i226 MAC 的以太网设备驱动（Ethernet Device Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_IGC_MAC_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PCIE_MSI_MULTI_VECTOR
CONFIG_PCIE_MSI_X
```

**定义位置（Location）**：[`drivers/ethernet/intel/Kconfig.intel_igc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/intel/Kconfig.intel_igc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PCIE_MSI_MULTI_VECTOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MSI_MULTI_VECTOR)、[`CONFIG_PCIE_MSI_X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MSI_X)。

<a id="CONFIG_ETH_INTEL_IGC_INT_PRIORITY"></a>

## 87.85 `CONFIG_ETH_INTEL_IGC_INT_PRIORITY`

**提示（Prompt）**：中断优先级。

**说明（Help）**

IGC 中断所用的 MSI-X 向量优先级（Vector Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_INTEL_IGC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`drivers/ethernet/intel/Kconfig.intel_igc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/intel/Kconfig.intel_igc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Intel IGC MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_INTEL_IGC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_INTEL_IGC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_INTEL_IGC_NET_MTU"></a>

## 87.86 `CONFIG_ETH_INTEL_IGC_NET_MTU`

**提示（Prompt）**：最大传输单元大小（MTU Size）

**说明（Help）**

最大传输单元（Maximum Transmission Unit，MTU）大小配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_INTEL_IGC && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
1500
```

**取值范围（Ranges）**

```text
[64, 1522]
```

**定义位置（Location）**：[`drivers/ethernet/intel/Kconfig.intel_igc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/intel/Kconfig.intel_igc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → Intel IGC MAC 驱动

**配置项引用（Symbol References）**：[`CONFIG_ETH_INTEL_IGC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_INTEL_IGC)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_INTEL_PLAT"></a>

## 87.87 `CONFIG_ETH_INTEL_PLAT`

**提示（Prompt）**：Intel 以太网父平台设备驱动（Parent Platform Device Driver）

**说明（Help）**

启用平台驱动（Platform Driver），获取内存映射 I/O（MMIO）映射详情，并与 MDIO、PHY、MAC 和 PTP_CLOCK 等所有子设备共享。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ETH_PLAT_ENABLED && CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`drivers/ethernet/intel/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/intel/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_IVSHMEM"></a>

## 87.88 `CONFIG_ETH_IVSHMEM`

**提示（Prompt）**：虚拟机间共享内存以太网驱动（Inter-VM Shared Memory Ethernet Driver）

**说明（Help）**

启用虚拟机间共享内存以太网驱动（Inter-VM Shared Memory Ethernet Driver），用于 Jailhouse 虚拟机监控器（Hypervisor）的单元（Cell）之间进行以太网通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIEMENS_IVSHMEM_ETH_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PCIE
CONFIG_VIRTUALIZATION
CONFIG_IVSHMEM_V2
CONFIG_IVSHMEM_DOORBELL
CONFIG_OPENAMP
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.ivshmem:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.ivshmem#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PCIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE)、[`CONFIG_VIRTUALIZATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTUALIZATION)、[`CONFIG_IVSHMEM_V2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IVSHMEM_V2)、[`CONFIG_IVSHMEM_DOORBELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IVSHMEM_DOORBELL)、[`CONFIG_OPENAMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENAMP)。

<a id="CONFIG_ETH_IVSHMEM_THREAD_PRIORITY"></a>

## 87.89 `CONFIG_ETH_IVSHMEM_THREAD_PRIORITY`

**提示（Prompt）**：IVSHMEM 以太网线程优先级（Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_IVSHMEM && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.ivshmem:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.ivshmem#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 虚拟机间共享内存以太网驱动（Inter-VM Shared Memory Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_IVSHMEM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_IVSHMEM)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_IVSHMEM_THREAD_STACK_SIZE"></a>

## 87.90 `CONFIG_ETH_IVSHMEM_THREAD_STACK_SIZE`

**提示（Prompt）**：IVSHMEM 以太网线程栈大小（Thread Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_IVSHMEM && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.ivshmem:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.ivshmem#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 虚拟机间共享内存以太网驱动（Inter-VM Shared Memory Ethernet Driver）

**配置项引用（Symbol References）**：[`CONFIG_ETH_IVSHMEM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_IVSHMEM)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_LAN865X"></a>

## 87.91 `CONFIG_ETH_LAN865X`

**提示（Prompt）**：LAN865X 10BASE-T1S 控制器（Controller）

**说明（Help）**

LAN865X 是一种低功耗 10BASE-T1S 收发器（Transceiver），符合 IEEE® 802.3cg-2019™ 以太网标准；原文在此将其描述为用于长距离（Long Reach）10 Mbps 单对线以太网（Single-Pair Ethernet，SPE）。LAN865X 集成媒体访问控制（Media Access Control，MAC）和物理层（PHY），可通过串行外设接口（Serial Peripheral Interface，SPI）直接连接多种控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_LAN865X_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_NET_L2_ETHERNET_MGMT
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.lan865x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.lan865x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_NET_L2_ETHERNET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_MGMT)。

<a id="CONFIG_ETH_LAN865X_INIT_PRIORITY"></a>

## 87.92 `CONFIG_ETH_LAN865X_INIT_PRIORITY`

**提示（Prompt）**：LAN865X 驱动初始化优先级（Init Priority）

**说明（Help）**

LAN865X 设备驱动的初始化优先级（Initialization Priority）。必须在 SPI 之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_LAN865X && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.lan865x:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.lan865x#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → LAN865X 10BASE-T1S 控制器（Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_LAN865X`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN865X)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_LAN865X_IRQ_THREAD_PRIO"></a>

## 87.93 `CONFIG_ETH_LAN865X_IRQ_THREAD_PRIO`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责 LAN INT 中断请求（IRQ）处理的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_LAN865X && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.lan865x:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.lan865x#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → LAN865X 10BASE-T1S 控制器（Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_LAN865X`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN865X)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_LAN865X_IRQ_THREAD_STACK_SIZE"></a>

## 87.94 `CONFIG_ETH_LAN865X_IRQ_THREAD_STACK_SIZE`

**提示（Prompt）**：处理中断请求（IRQ）的线程栈大小（Stack Size）

**说明（Help）**

用于处理已触发的 INT 中断请求（IRQ）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_LAN865X && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.lan865x:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.lan865x#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → LAN865X 10BASE-T1S 控制器（Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_LAN865X`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN865X)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_LAN865X_TIMEOUT"></a>

## 87.95 `CONFIG_ETH_LAN865X_TIMEOUT`

**提示（Prompt）**：IP 缓冲区超时时间（IP Buffer Timeout）

**说明（Help）**

给定超时时间，以毫秒为单位。驱动等待从 IP 协议栈（IP Stack）获得内存缓冲区的最长时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_LAN865X && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.lan865x:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.lan865x#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → LAN865X 10BASE-T1S 控制器（Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_LAN865X`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN865X)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_LAN9250"></a>

## 87.96 `CONFIG_ETH_LAN9250`

**提示（Prompt）**：LAN9250 以太网控制器（Ethernet Controller）

**说明（Help）**

具有 SPI 接口的 LAN9250 独立以太网控制器（Stand-Alone Ethernet Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_LAN9250_ENABLED && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.lan9250:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.lan9250#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ETH_LAN9250_BUF_ALLOC_TIMEOUT"></a>

## 87.97 `CONFIG_ETH_LAN9250_BUF_ALLOC_TIMEOUT`

**提示（Prompt）**：网络缓冲区分配超时时间（Network Buffer Allocation Timeout）

**说明（Help）**

给定超时时间，以毫秒为单位。驱动等待从 IP 协议栈（IP Stack）获得内存缓冲区的最长时间，超过后丢弃以太网帧（Ethernet Frame）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_LAN9250 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.lan9250:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.lan9250#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → LAN9250 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_LAN9250`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN9250)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_LAN9250_RX_THREAD_PRIO"></a>

## 87.98 `CONFIG_ETH_LAN9250_RX_THREAD_PRIO`

**提示（Prompt）**：内部传入数据包处理线程（Incoming Packet Handler）的优先级

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_LAN9250 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.lan9250:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.lan9250#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → LAN9250 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_LAN9250`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN9250)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_LAN9250_RX_THREAD_STACK_SIZE"></a>

## 87.99 `CONFIG_ETH_LAN9250_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：内部传入数据包处理线程的栈大小（Stack Size）

**说明（Help）**

负责传入数据包处理（Incoming Packet Processing）的内部线程所用的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ETH_LAN9250 && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.lan9250:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.lan9250#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → LAN9250 以太网控制器（Ethernet Controller）

**配置项引用（Symbol References）**：[`CONFIG_ETH_LAN9250`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN9250)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_ETH_LITEX_LITEETH"></a>

## 87.100 `CONFIG_ETH_LITEX_LITEETH`

**提示（Prompt）**：LiteX LiteEth 以太网核驱动（Ethernet Core Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_LITEETH_ENABLED && CONFIG_NET_L2_ETHERNET && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ethernet/Kconfig.litex:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/Kconfig.litex#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<!-- kconfig-navigation -->

[上一章](P086_drivers_espi_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P088_drivers_ethernet_配置项参考_2.md)
