---
id: learning.zephyr-docs.networking.page-117
title: gPTP通用精确时间协议
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/gptp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_gPTP通用精确时间协议

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/gptp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

此通用精确时间协议栈（generic Precision Time Protocol，gPTP）支持 [IEEE 802.1AS-2011 标准](https://standards.ieee.org/findstds/standard/802.1AS-2011.html)所定义的协议和过程。该标准的主题是“桥接局域网中对时间敏感的应用的定时与同步”（Timing and Synchronization for Time-Sensitive Applications in Bridged Local Area Networks）。

## 2. 支持的特性（Supported Features）

协议栈处理 IEEE 802.1AS-2011 所定义的通信和状态机，并支持该标准附录 A 中针对全双工点到点链路端点（Full-duplex Point-to-point Link Endpoint）的强制要求。

原则上，协议栈可以处理多个网络接口上的通信；这些接口在标准中也称“端口”（Port）。因此，它可以充当 802.1AS 网桥。不过，原文明确说明，这种工作模式尚未在 Zephyr OS 上完成验证。

在采用 IEEE 802.1AS 车载配置规范（Automotive Profile）、不交换 Announce 消息的网络中，协议栈也可以作为静态配置的时间接收端运行，详见第 5 节。

## 3. 支持的硬件（Supported Hardware）

协议栈本身与硬件无关，但以太网驱动必须启用以太网帧时间戳（Ethernet Frame Timestamping）支持。

原文列出的开发板如下：

- [FRDM-K64F](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)。
- [Nucleo H743ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_h743zi/doc/index.html#nucleo_h743zi)。
- [Nucleo H745ZI-Q](https://docs.zephyrproject.org/latest/boards/st/nucleo_h745zi_q/doc/index.html#nucleo_h745zi_q)。
- [Nucleo F767ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_f767zi/doc/index.html#nucleo_f767zi)。
- [SAM E70(B) Xplained](https://docs.zephyrproject.org/latest/boards/atmel/sam/sam_e70_xplained/doc/index.html#sam_e70_xplained)。
- [原生模拟器（Native Simulator，native_sim）](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)：只能用于简单测试，缺少硬件时钟使其能力受限。
- [X86 的 QEMU 仿真](../qemu_catalog_reference/P003_QEMU_X86.md#qemu_x86)：属于仿真实现，缺少硬件时钟使其能力受限。

## 4. 启用协议栈（Enabling the Stack）

在 `prj.conf` 文件中启用 [`CONFIG_NET_GPTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP)。

## 5. 静态时间接收端（Static timeReceiver Operation）

采用 IEEE 802.1AS 车载配置规范，即 AVnu《车载以太网 AVB 功能与互操作规范》（Automotive Ethernet AVB Functional and Interoperability Specification）的网络，使用静态端口角色，而不运行最佳主时钟算法（Best Master Clock Algorithm，BMCA）。

此类网络中的网桥发送同步消息（Sync）和跟随消息（Follow_Up），不发送通告消息（Announce），也不必在时间发送端（timeTransmitter）端口上响应对等链路时延（Pdelay）请求。默认协议栈不能与这样的网桥同步：收不到 Announce 时，端口永远无法进入时间接收端（timeReceiver，原文也称 “slave”）角色。

启用 [`CONFIG_NET_GPTP_STATIC_TIME_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP_STATIC_TIME_RECEIVER) 可将节点配置为静态时间接收端：绕过 BMCA 和全部 Announce 处理，所有端口固定为时间接收端，强制设置 `asCapable`，使同步不依赖 Pdelay 测量；本地时钟仅根据收到的 Sync 和 Follow_Up 消息进行校准。即使设置了 [`CONFIG_NET_GPTP_GM_CAPABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP_GM_CAPABLE)，节点也不会成为最高主时钟（Grandmaster），永远不会发送 Sync 或 Announce 消息。

这对应于 linuxptp 的 ptp4l 车载时间接收端配置：BMCA 为 `noop`，以及 `clientOnly`、`inhibit_announce`、`asCapable` 为 `true`、`ignore_source_id`。在标准中，以这种方式禁用 BMCA 对应 IEEE 802.1AS-2020 第 10.3.14 条的外部端口配置（External Port Configuration）；该机制源于 IEEE 1588-2019 第 17.6.2 条。

> 译注——版本依据：上述选项及行为可在官方 [gPTP Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig) 中核对。本页描述读取当日的官方 `latest`，不能据此认定较旧源码或任意网卡驱动已具有同样能力。

## 6. 应用接口（Application Interfaces）

标准第 9 节定义的下列应用接口已经提供：

| 标准接口 | Zephyr 接口 |
| --- | --- |
| 时钟源时间（ClockSourceTime） | [`gptp_clk_src_time_invoke()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9b27c9a741fb0ca72eff78e334e629fe) |
| 目标时钟相位不连续通知（ClockTargetPhaseDiscontinuity） | [`gptp_register_phase_dis_cb()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gaad2282df9cbf7f05f557285323af8f07) |
| 目标时钟事件捕获（ClockTargetEventCapture） | [`gptp_event_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9a8e2ccf20d0430b4e62f3302462c6eb) |

## 7. 测试（Testing）

原文说明，此协议栈曾使用 [OpenAVnu gPTP](https://github.com/AVnu/gptp) 和 [Linux ptp4l](https://linuxptp.sourceforge.net/) 守护进程进行非正式测试。Zephyr 源码发行包中的[gPTP 示例应用](P121_gPTP示例.md#gptp)可用于测试。

## 8. API 参考（API Reference）

[gPTP 支持接口（gPTP Support）](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html)。

相关代码示例：[gPTP 示例](P121_gPTP示例.md#gptp)，启用 gPTP，并通过网络命令行（net-shell）监测其功能。


<a id="generic-precision-time-protocol-gptp"></a>
<a id="gptp-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="overview"></a>
<a id="supported-features"></a>
<a id="supported-hardware"></a>
<a id="enabling-the-stack"></a>
<a id="static-timereceiver-operation"></a>
<a id="application-interfaces"></a>
<a id="testing"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：LLDP链路层发现协议](P116_LLDP链路层发现协议.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：IEEE8021Qav流量整形](P118_IEEE8021Qav流量整形.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P116_LLDP链路层发现协议.md) · [返回大纲](大纲.md) · [下一章](P118_IEEE8021Qav流量整形.md)

</details>

<!-- reading-navigation:end -->
