---
id: learning.zephyr-docs.api-source-packet-gnss-reference.page-3
title: if_arp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/if__arp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_if\_arp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/if__arp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P142_zephyr__posix__net__if_arp.h_文件参考.md)。

## 3.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_NET_IF_ARP_H_
#define ZEPHYR_INCLUDE_POSIX_NET_IF_ARP_H_

#ifdef __cplusplus
extern "C" {
#endif

/* See https://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml
 * for the ARP hardware address type values.
 */
/* ARP protocol HARDWARE identifiers. */
#define ARPHRD_NETROM     0            /* From KA9Q: NET/ROM pseudo. */
#define ARPHRD_ETHER      1            /* Ethernet 10/100Mbps.  */
#define ARPHRD_EETHER     2            /* Experimental Ethernet.  */
#define ARPHRD_AX25       3            /* AX.25 Level 2.  */
#define ARPHRD_PRONET     4            /* PROnet token ring.  */
#define ARPHRD_CHAOS      5            /* Chaosnet.  */
#define ARPHRD_IEEE802    6            /* IEEE 802.2 Ethernet/TR/TB.  */
#define ARPHRD_ARCNET     7            /* ARCnet.  */
#define ARPHRD_APPLETLK   8            /* APPLEtalk.  */
#define ARPHRD_DLCI       15           /* Frame Relay DLCI.  */
#define ARPHRD_ATM        19           /* ATM.  */
#define ARPHRD_METRICOM   23           /* Metricom STRIP (new IANA id).  */
#define ARPHRD_IEEE1394   24           /* IEEE 1394 IPv4 - RFC 2734.  */
#define ARPHRD_EUI64      27           /* EUI-64.  */
#define ARPHRD_INFINIBAND 32           /* InfiniBand.  */

/* Dummy types for non ARP hardware */
#define ARPHRD_SLIP       256
#define ARPHRD_CSLIP      257
#define ARPHRD_SLIP6      258
#define ARPHRD_CSLIP6     259
#define ARPHRD_RSRVD      260          /* Notional KISS type.  */
#define ARPHRD_ADAPT      264
#define ARPHRD_ROSE       270
#define ARPHRD_X25        271          /* CCITT X.25.  */
#define ARPHRD_HWX25      272          /* Boards with X.25 in firmware.  */
#define ARPHRD_CAN        280          /* Controller Area Network.  */
#define ARPHRD_MCTP       290
#define ARPHRD_PPP        512
#define ARPHRD_CISCO      513          /* Cisco HDLC.  */
#define ARPHRD_HDLC       ARPHRD_CISCO
#define ARPHRD_LAPB       516          /* LAPB.  */
#define ARPHRD_DDCMP      517          /* Digital's DDCMP.  */
#define ARPHRD_RAWHDLC    518          /* Raw HDLC.  */
#define ARPHRD_RAWIP      519          /* Raw IP.  */
#define ARPHRD_TUNNEL     768          /* IPIP tunnel.  */
#define ARPHRD_TUNNEL6    769          /* IPIP6 tunnel.  */
#define ARPHRD_FRAD       770          /* Frame Relay Access Device.  */
#define ARPHRD_SKIP       771          /* SKIP vif.  */
#define ARPHRD_LOOPBACK   772          /* Loopback device.  */
#define ARPHRD_LOCALTLK   773          /* Localtalk device.  */
#define ARPHRD_FDDI       774          /* Fiber Distributed Data Interface. */
#define ARPHRD_BIF        775          /* AP1000 BIF.  */
#define ARPHRD_SIT        776          /* sit0 device - IPv6-in-IPv4.  */
#define ARPHRD_IPDDP      777          /* IP-in-DDP tunnel.  */
#define ARPHRD_IPGRE      778          /* GRE over IP.  */
#define ARPHRD_PIMREG     779          /* PIMSM register interface.  */
#define ARPHRD_HIPPI      780          /* High Performance Parallel I'face. */
#define ARPHRD_ASH        781          /* (Nexus Electronics) Ash.  */
#define ARPHRD_ECONET     782          /* Acorn Econet.  */
#define ARPHRD_IRDA       783          /* Linux-IrDA.  */
#define ARPHRD_FCPP       784          /* Point to point fibrechanel.  */
#define ARPHRD_FCAL       785          /* Fibrechanel arbitrated loop.  */
#define ARPHRD_FCPL       786          /* Fibrechanel public loop.  */
#define ARPHRD_FCFABRIC   787          /* Fibrechanel fabric.  */
#define ARPHRD_IEEE802_TR 800          /* Magic type ident for TR.  */
#define ARPHRD_IEEE80211  801          /* IEEE 802.11.  */
#define ARPHRD_IEEE80211_PRISM    802  /* IEEE 802.11 + Prism2 header.  */
#define ARPHRD_IEEE80211_RADIOTAP 803  /* IEEE 802.11 + radiotap header.  */
#define ARPHRD_IEEE802154         804  /* IEEE 802.15.4 header.  */
#define ARPHRD_IEEE802154_PHY     805  /* IEEE 802.15.4 PHY header.  */

#define ARPHRD_VOID       0xFFFF       /* Void type, nothing is known.  */
#define ARPHRD_NONE       0xFFFE       /* Zero header length.  */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_NET_IF_ARP_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

地址解析协议（ARP）硬件地址类型值参见 [IANA ARP 参数登记表](https://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml)。

### 注释 3：原第 16 行

地址解析协议（ARP）的硬件标识符（Hardware Identifiers）。

### 注释 4：原第 17 行

来自 KA9Q：NET/ROM 伪类型（Pseudo）。

### 注释 5：原第 18 行

10/100 Mbps 以太网（Ethernet）。

### 注释 6：原第 19 行

实验性以太网（Experimental Ethernet）。

### 注释 7：原第 20 行

AX.25 第 2 层（Level 2）。

### 注释 8：原第 21 行

PROnet 令牌环（Token Ring）。

### 注释 9：原第 22 行

Chaosnet 网络。

### 注释 10：原第 23 行

IEEE 802.2 以太网／令牌环／令牌总线（Ethernet/TR/TB）。

### 注释 11：原第 24 行

ARCnet 网络。

### 注释 12：原第 25 行

AppleTalk 网络。

### 注释 13：原第 26 行

帧中继（Frame Relay）数据链路连接标识（DLCI）。

### 注释 14：原第 27 行

异步传输模式（ATM）。

### 注释 15：原第 28 行

Metricom STRIP，新的 IANA 标识。

### 注释 16：原第 29 行

IEEE 1394 上的 IPv4，参见 RFC 2734。

### 注释 17：原第 30 行

64 位扩展唯一标识符（EUI-64）。

### 注释 18：原第 31 行

InfiniBand 互连。

### 注释 19：原第 33 行

用于非 ARP 硬件的占位类型（Dummy Types）。

### 注释 20：原第 38 行

名义上的 KISS 类型（Notional KISS Type）。

### 注释 21：原第 41 行

CCITT X.25 协议。

### 注释 22：原第 42 行

固件中包含 X.25 的开发板。

### 注释 23：原第 43 行

控制器局域网（Controller Area Network）。

### 注释 24：原第 46 行

Cisco 高级数据链路控制（HDLC）。

### 注释 25：原第 48 行

平衡型链路访问规程（LAPB）。

### 注释 26：原第 49 行

Digital 的数字数据通信消息协议（DDCMP）。

### 注释 27：原第 50 行

原始高级数据链路控制（Raw HDLC）。

### 注释 28：原第 51 行

原始 IP（Raw IP）。

### 注释 29：原第 52 行

IPIP 隧道（Tunnel）。

### 注释 30：原第 53 行

IPIP6 隧道（Tunnel）。

### 注释 31：原第 54 行

帧中继接入设备（Frame Relay Access Device）。

### 注释 32：原第 55 行

SKIP 虚拟接口（VIF）。

### 注释 33：原第 56 行

回环设备（Loopback Device）。

### 注释 34：原第 57 行

LocalTalk 设备（Device）。

### 注释 35：原第 58 行

光纤分布式数据接口（Fiber Distributed Data Interface）。

### 注释 36：原第 59 行

AP1000 BIF 接口。

### 注释 37：原第 60 行

sit0 设备，将 IPv6 封装在 IPv4 中（IPv6-in-IPv4）。

### 注释 38：原第 61 行

将 IP 封装在 DDP 中的隧道（IP-in-DDP Tunnel）。

### 注释 39：原第 62 行

在 IP 上传送通用路由封装（GRE over IP）。

### 注释 40：原第 63 行

稀疏模式协议无关组播（PIM-SM）的注册接口（Register Interface）。

### 注释 41：原第 64 行

高性能并行接口（High Performance Parallel Interface）。

### 注释 42：原第 65 行

Nexus Electronics 的 Ash。

### 注释 43：原第 66 行

Acorn Econet 网络。

### 注释 44：原第 67 行

Linux 红外数据通信（Linux-IrDA）。

### 注释 45：原第 68 行

点对点光纤通道（Point-to-point Fibre Channel）。

### 注释 46：原第 69 行

光纤通道仲裁环（Fibre Channel Arbitrated Loop）。

### 注释 47：原第 70 行

光纤通道公共环（Fibre Channel Public Loop）。

### 注释 48：原第 71 行

光纤通道交换结构（Fibre Channel Fabric）。

### 注释 49：原第 72 行

令牌环（TR）的特殊类型标识（Magic Type Identifier）。

### 注释 50：原第 73 行

IEEE 802.11 无线网络。

### 注释 51：原第 74 行

IEEE 802.11 加 Prism2 消息头（Header）。

### 注释 52：原第 75 行

IEEE 802.11 加 radiotap 消息头（Header）。

### 注释 53：原第 76 行

IEEE 802.15.4 消息头（Header）。

### 注释 54：原第 77 行

IEEE 802.15.4 物理层（PHY）消息头。

### 注释 55：原第 79 行

空类型（Void Type），没有已知信息。

### 注释 56：原第 80 行

消息头长度为零（Zero Header Length）。

### 注释 57：原第 86 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_NET_IF_ARP_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P142_zephyr__posix__net__if_arp.h_文件参考.md)

---

[上一章](P002_esp32s3-xtensa-intmux.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_protocol.h_源码浏览.md)
