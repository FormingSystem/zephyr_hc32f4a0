---
id: learning.zephyr-docs.networking.page-128
title: PTP精确时间协议
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ptp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第128章\_PTP精确时间协议

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ptp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

精确时间协议（Precision Time Protocol，PTP）是一种在应用层实现的网络协议，用于同步计算机网络中的时钟，精度可以达到亚微秒级。协议栈支持 [IEEE 1588-2019 标准](https://standards.ieee.org/ieee/1588/6825/)所定义的协议和过程，即《网络测量和控制系统的精确时钟同步协议标准》（IEEE Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems）。PTP 有多种配置规范（Profile），可运行在第二层以太网（L2 Ethernet）或第三层 UDP/IPv4、UDP/IPv6 之上。

这种精度依靠对协议数据包进行硬件时间戳（Hardware Timestamping）处理实现。

Zephyr 的 PTP 实现包含以下部分：

- 处理传入消息和事件的 PTP 协议栈线程。
- 与 `ptp_clock` 驱动集成。
- 在系统初始化阶段执行的 PTP 初始化。

实现会自动创建 PTP 端口（PTP Port），每个端口对应一个独立网络接口。

## 2. 支持的特性（Supported Features）

此实现没有支持标准规定的全部特性。下表保留原文列出的支持状态；“—”表示原表留空，并不把它解释成已支持。

| 特性（Feature） | 支持（Supported） |
| --- | --- |
| 普通时钟（Ordinary Clock） | 是（yes） |
| 边界时钟（Boundary Clock） | 是（yes） |
| 透明时钟（Transparent Clock） | — |
| 管理节点（Management Node） | — |
| 端到端时延机制（End to end delay mechanism） | 是（yes） |
| 对等时延机制（Peer to peer delay mechanism） | 是，两步式（yes (two-step)） |
| 组播工作模式（Multicast operation mode） | 是（yes） |
| 混合工作模式（Hybrid operation mode） | 是（yes） |
| 单播工作模式（Unicast operation mode） | — |
| 非易失存储（Non-volatile storage） | — |
| UDP IPv4 传输协议（UDP IPv4 transport protocol） | 是（yes） |
| UDP IPv6 传输协议（UDP IPv6 transport protocol） | 是（yes） |
| IEEE 802.3 以太网传输协议（IEEE 802.3 (Ethernet) transport protocol） | 是（yes） |
| 硬件时间戳（Hardware timestamping） | 是（yes） |
| 软件时间戳（Software timestamping） | — |
| 仅作时间接收端的 PTP 实例（TIME_RECEIVER_ONLY PTP Instance） | 是（yes） |
| 仅作时间发送端的 PTP 实例（TIME_TRANSMITTER_ONLY PTP Instance） | — |

## 3. 网络传输模式（Network Transmission Modes）

通过 Kconfig 选择项 `PTP_NETWORK_MODE` 选择传输模式。

### 3.1 组播模式（Multicast Mode）

默认选项 [`CONFIG_PTP_NETWORK_MODE_MULTICAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_NETWORK_MODE_MULTICAST) 使用标准 PTP 模式，所有 PTP 消息都发送到默认组播地址。每个节点因此会接收到其他所有节点的时延请求／响应消息对（`Delay_Req` / `Delay_Resp`），使网络流量增加。在只有少量时间接收端（timeReceiver）的小型网络中，这通常不是问题。

### 3.2 混合模式（Hybrid Mode）

[`CONFIG_PTP_NETWORK_MODE_HYBRID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_NETWORK_MODE_HYBRID) 仍将通告（`Announce`）、同步（`Sync`）和跟随（`Follow_Up`）消息发送到默认组播地址，但时间接收端把 `Delay_Req` 直接单播到当前时间发送端（timeTransmitter）的协议地址。该地址在 IP 传输中为 IP 地址，在 IEEE 802.3 传输中为 MAC 地址。时间发送端随后向请求方单播 `Delay_Resp`。

这种方式减少了 PTP 流量，有助于扩展到包含大量时间接收端的网络。混合模式只要求网络支持从时间发送端到时间接收端的组播传输。它兼容 linuxptp 的 `hybrid_e2e` 选项和 sfptpd 的 `hybrid` 网络模式，但不支持单播协商（Unicast Negotiation）。

如果时间发送端连续未响应 [`CONFIG_PTP_HYBRID_FALLBACK_ATTEMPTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_HYBRID_FALLBACK_ATTEMPTS) 次单播 `Delay_Req`，PTP 端口会记录错误并退回组播时延测量，直到选出新的时间发送端前都保持组播。可启用 [`CONFIG_PTP_NETWORK_MODE_HYBRID_NO_FALLBACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_NETWORK_MODE_HYBRID_NO_FALLBACK) 禁用回退，此时端口始终发送单播 `Delay_Req`。

混合模式要求端到端时延机制（End-to-End，E2E），即 [`CONFIG_PTP_DELAY_MECHANISM_E2E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_DELAY_MECHANISM_E2E)，且支持全部传输协议：UDP IPv4、UDP IPv6 和 IEEE 802.3。

## 4. 支持的管理消息（Supported Management Messages）

依据 IEEE 1588-2019 第 15.5.2.3 节表 59，下表列出管理消息的类型—长度—值字段（Type-Length-Value，TLV）支持情况。保留 `Management_ID` 及原标识符，另加中文含义便于查阅。允许操作中的 `GET` 表示读取，`SET` 表示设置，`COMMAND` 表示执行命令；“—”表示原表留空。

| 管理标识（Management_ID） | 原标识符（Management_ID name） | 中文含义 | 允许操作（Allowed actions） |
| --- | --- | --- | --- |
| 0x0000 | `NULL_PTP_MANAGEMENT` | 空 PTP 管理操作 | GET SET COMMAND |
| 0x0001 | `CLOCK_DESCRIPTION` | 时钟描述 | GET |
| 0x0002 | `USER_DESCRIPTION` | 用户描述 | GET |
| 0x0003 | `SAVE_IN_NON_VOLATILE_STORAGE` | 保存到非易失存储 | — |
| 0x0004 | `RESET_NON_VOLATILE_STORAGE` | 重置非易失存储 | — |
| 0x0005 | `INITIALIZE` | 初始化 | — |
| 0x0006 | `FAULT_LOG` | 故障日志 | — |
| 0x0007 | `FAULT_LOG_RESET` | 重置故障日志 | — |
| 0x2000 | `DEFAULT_DATA_SET` | 默认数据集 | GET |
| 0x2001 | `CURRENT_DATA_SET` | 当前数据集 | GET |
| 0x2002 | `PARENT_DATA_SET` | 父数据集 | GET |
| 0x2003 | `TIME_PROPERTIES_DATA_SET` | 时间属性数据集 | GET |
| 0x2004 | `PORT_DATA_SET` | 端口数据集 | GET |
| 0x2005 | `PRIORITY1` | 优先级 1 | GET SET |
| 0x2006 | `PRIORITY2` | 优先级 2 | GET SET |
| 0x2007 | `DOMAIN` | 时间域 | GET SET |
| 0x2008 | `TIME_RECEIVER_ONLY` | 仅作时间接收端 | GET SET |
| 0x2009 | `LOG_ANNOUNCE_INTERVAL` | Announce 对数间隔 | GET SET |
| 0x200A | `ANNOUNCE_RECEIPT_TIMEOUT` | Announce 接收超时 | GET SET |
| 0x200B | `LOG_SYNC_INTERVAL` | Sync 对数间隔 | GET SET |
| 0x200C | `VERSION_NUMBER` | 版本号 | GET SET |
| 0x200D | `ENABLE_PORT` | 启用端口 | COMMAND |
| 0x200E | `DISABLE_PORT` | 禁用端口 | COMMAND |
| 0x200F | `TIME` | 时间 | GET SET |
| 0x2010 | `CLOCK_ACCURACY` | 时钟准确度 | GET SET |
| 0x2011 | `UTC_PROPERTIES` | UTC 属性 | GET SET |
| 0x2012 | `TRACEBILITY_PROPERTIES` | 可追溯性属性 | GET SET |
| 0x2013 | `TIMESCALE_PROPERTIES` | 时间尺度属性 | GET SET |
| 0x2014 | `UNICAST_NEGOTIATION_ENABLE` | 启用单播协商 | — |
| 0x2015 | `PATH_TRACE_LIST` | 路径追踪列表 | — |
| 0x2016 | `PATH_TRACE_ENABLE` | 启用路径追踪 | — |
| 0x2017 | `GRANDMASTER_CLUSTER_TABLE` | 最高主时钟集群表 | — |
| 0x2018 | `UNICAST_TIME_TRANSMITTER_TABLE` | 单播时间发送端表 | — |
| 0x2019 | `UNICAST_TIME_TRANSMITTER_MAX_TABLE_SIZE` | 单播时间发送端表最大容量 | — |
| 0x201A | `ACCEPTABLE_TIME_TRANSMITTER_TABLE` | 可接受时间发送端表 | — |
| 0x201B | `ACCEPTABLE_TIME_TRANSMITTER_TABLE_ENABLED` | 启用可接受时间发送端表 | — |
| 0x201C | `ACCEPTABLE_TIME_TRANSMITTER_MAX_TABLE_SIZE` | 可接受时间发送端表最大容量 | — |
| 0x201D | `ALTERNATE_TIME_TRANSMITTER` | 备用时间发送端 | — |
| 0x201E | `ALTERNATE_TIME_OFFSET_ENABLE` | 启用备用时间偏移 | — |
| 0x201F | `ALTERNATE_TIME_OFFSET_NAME` | 备用时间偏移名称 | — |
| 0x2020 | `ALTERNATE_TIME_OFFSET_MAX_KEY` | 备用时间偏移最大键值 | — |
| 0x2021 | `ALTERNATE_TIME_OFFSET_PROPERTIES` | 备用时间偏移属性 | — |
| 0x3000 | `EXTERNAL_PORT_CONFIGURATION_ENABLED` | 启用外部端口配置 | — |
| 0x3001 | `TIME_TRANSMITTER_ONLY` | 仅作时间发送端 | — |
| 0x3002 | `HOLDOVER_UPGRADE_ENABLE` | 启用保持模式升级 | — |
| 0x3003 | `EXT_PORT_CONFIG_PORT_DATA_SET` | 外部端口配置的端口数据集 | — |
| 0x4000 | `TRANSPARENT_CLOCK_DEFAULT_DATA_SET` | 透明时钟默认数据集 | — |
| 0x4001 | `TRANSPARENT_CLOCK_PORT_DATA_SET` | 透明时钟端口数据集 | — |
| 0x4002 | `PRIMARY_DOMAIN` | 主时间域 | — |
| 0x6000 | `DELAY_MECHANISM` | 时延机制 | GET |
| 0x6001 | `LOG_MIN_PDELAY_REQ_INTERVAL` | 最小 Pdelay 请求对数间隔 | GET SET |

> 译注——标识符保留：`TRACEBILITY_PROPERTIES` 的拼写按官方原表保留，不在表内自行替换源码或协议标识符。

## 5. 时间戳说明（Timestamping Notes）

接收硬件时间戳不可用或无效时，同步处理会回退到在接收处理期间读取 PTP 硬件时钟（PTP Hardware Clock，PHC）。从帧到达至 PHC 读取之间的数据包处理路径和调度延迟，会引入额外抖动。

对于没有驱动提供真实 RX 硬件时间戳的第二层 `AF_PACKET` 路径，这属于预期行为。

IEEE 802.3 传输采用两步模式（Two-step Mode）发送 Sync，随后由 TX 时间戳回调生成 Follow_Up。如果发送时间戳缺失或到达太晚，协议栈记录警告，并跳过该 Sync 序号对应的 Follow_Up；之后的周期继续正常发送 Sync，即尽力而为（Best-effort）的行为。

可通过 [`CONFIG_PTP_DELAY_MECHANISM_P2P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_DELAY_MECHANISM_P2P) 选择对等时延测量（Peer-to-Peer，P2P）。首先支持的是两步 `Pdelay_Req` / `Pdelay_Resp` / `Pdelay_Resp_Follow_Up` 流程。一步式（One-step）`Pdelay_Resp` 样本会被拒绝并记录日志，留待后续实现。

> 译注——支持表与回退：第 2 节没有把“软件时间戳”标为支持；这里描述的是缺少有效接收硬件时间戳时读取 PHC 的回退处理。它不等于具有相同精度的软件时间戳方案，亚微秒描述也不构成任意配置的同步精度保证。

## 6. 支持的硬件（Supported Hardware）

协议栈本身与硬件无关，但以太网驱动必须启用以太网帧时间戳支持。原文列出以下开发板：

- [Nucleo H563ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_h563zi/doc/index.html#nucleo_h563zi)。
- [Nucleo H743ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_h743zi/doc/index.html#nucleo_h743zi)。
- [Nucleo H745ZI-Q](https://docs.zephyrproject.org/latest/boards/st/nucleo_h745zi_q/doc/index.html#nucleo_h745zi_q)。
- [Nucleo F767ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_f767zi/doc/index.html#nucleo_f767zi)。
- [FRDM-MCXN947](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html#frdm_mcxn947)。
- [原生模拟器（native_sim）](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)：仅用于简单测试，缺少硬件时钟导致能力受限。

## 7. 启用协议栈（Enabling the Stack）

在 `prj.conf` 中启用 [`CONFIG_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP)。

## 8. 测试（Testing）

原文说明，协议栈曾使用 [Linux ptp4l](https://linuxptp.sourceforge.net/) 守护进程进行非正式测试，也曾在 [Nucleo H563ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_h563zi/doc/index.html#nucleo_h563zi) 和 [FRDM-MCXN947](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html#frdm_mcxn947) 上连接 GPS 时钟测试，既有以太网直连方式，也有中间连接支持 PTP 的交换机的方式。测试使用 [PTP 示例应用](P132_PTP示例.md#ptp)，覆盖 UDP IPv4、UDP IPv6 和 IEEE 802.3 传输。

非正式测试矩阵如下：

| 测试组合 | IEEE 802.3 | UDP IPv4 | UDP IPv6 |
| --- | --- | --- | --- |
| ptp4l 守护进程（ptp4l daemons） | 是（yes） | 是（yes） | 是（yes） |
| GPS 时钟直连（GPS Clock (direct link)） | 是（yes） | 是（yes） | 是（yes） |
| 支持 PTP 的交换机（PTP-capable switch） | 是（yes） | 是（yes） | 是（yes） |
| GPS 时钟加支持 PTP 的交换机（GPS Clock + PTP-capable switch） | 是（yes） | 是（yes） | 是（yes） |

对等时延测量已经针对普通时钟（Ordinary Clock）用途实现并验证。边界时钟（Boundary Clock）预期共用端口级 Pdelay 机制，但尚未在多端口硬件上完成验证。

可使用 Zephyr 源码发行包中的 [PTP 示例](P132_PTP示例.md#ptp)继续测试。

## 9. API 参考（API Reference）

[PTP 支持接口（PTP Support）](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html)。

相关代码示例：[PTP](P132_PTP示例.md#ptp)，启用 PTP，通过日志监测消息和事件。


<a id="precision-time-protocol-ptp"></a>
<a id="ptp-interface"></a>
<a id="contents"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="id10"></a>
<a id="id11"></a>
<a id="overview"></a>
<a id="supported-features"></a>
<a id="id1"></a>
<a id="network-transmission-modes"></a>
<a id="supported-management-messages"></a>
<a id="id2"></a>
<a id="timestamping-notes"></a>
<a id="supported-hardware"></a>
<a id="enabling-the-stack"></a>
<a id="testing"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：时间敏感网络](P127_时间敏感网络.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：PTP时间格式](P129_PTP时间格式.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P127_时间敏感网络.md) · [返回大纲](大纲.md) · [下一章](P129_PTP时间格式.md)

</details>

<!-- reading-navigation:end -->
