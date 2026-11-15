---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-11
title: 以太网介质无关接口支持函数（Ethernet MII Support Functions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mii.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_以太网介质无关接口支持函数（Ethernet MII Support Functions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mii.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网介质无关接口（Media independent interface，MII）函数。

<a id="details"></a>

以太网介质独立接口函数（Ethernet Media Independent Interface Functions，MII）。自 1.7 引入，版本 0.8.0。

<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_mii_2Eh"></a>

```c
file mii.h
```

相关声明：[mii.h](../api_file_bluetooth_media_reference/P008_zephyr__net__mii.h_文件参考.md)。

IEEE 802.3第2节规定的媒体独立接口（MII）兼容PHY收发器的定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_gacac6f915a8d0e3f8244c571646b3fc92"></a>

```c
#define MII_ADVERTISE_ALL
```

相关声明：[MII_ADVERTISE_ALL](#gacac6f915a8d0e3f8244c571646b3fc92)。

通告全部速率（Advertise All Speeds）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 11.3\_MII管理寄存器（MII management registers）

<a id="r_ga9137acedc42ff140f244da7473cff29e"></a>

```c
#define MII_BMCR 0x0
```

相关声明：[MII_BMCR](#ga9137acedc42ff140f244da7473cff29e)。

基本模式控制寄存器（Basic Mode Control Register）。

<a id="r_gaa2f632686d6298a7c898b1c805586aab"></a>

```c
#define MII_BMSR 0x1
```

相关声明：[MII_BMSR](#gaa2f632686d6298a7c898b1c805586aab)。

基本模式状态寄存器（Basic Mode Status Register）。

<a id="r_ga87196e916598cea91b6ce400ad0cc34a"></a>

```c
#define MII_PHYID1R 0x2
```

相关声明：[MII_PHYID1R](#ga87196e916598cea91b6ce400ad0cc34a)。

PHY 标识 1 寄存器（PHY ID 1 Register）。

<a id="r_ga40766cdb8f9c3ffee64720f0f0ea2f15"></a>

```c
#define MII_PHYID2R 0x3
```

相关声明：[MII_PHYID2R](#ga40766cdb8f9c3ffee64720f0f0ea2f15)。

PHY 标识 2 寄存器（PHY ID 2 Register）。

<a id="r_gaacb2ab0ea5579b5d9e30b075991add1d"></a>

```c
#define MII_ANAR 0x4
```

相关声明：[MII_ANAR](#gaacb2ab0ea5579b5d9e30b075991add1d)。

自动协商通告寄存器（Auto-Negotiation Advertisement Register）。

<a id="r_ga445e8381a9ea9724054bfacc10bb4c81"></a>

```c
#define MII_ANLPAR 0x5
```

相关声明：[MII_ANLPAR](#ga445e8381a9ea9724054bfacc10bb4c81)。

自动协商链路伙伴能力寄存器（Auto-Negotiation Link Partner Ability Register）。

<a id="r_ga6e5634d8831e21f963ddc16b91d5f6b9"></a>

```c
#define MII_ANER 0x6
```

相关声明：[MII_ANER](#ga6e5634d8831e21f963ddc16b91d5f6b9)。

自动协商扩展寄存器（Auto-Negotiation Expansion Register）。

<a id="r_ga3f3ed3ecfd22b34b840ff2473ca68490"></a>

```c
#define MII_ANNPTR 0x7
```

相关声明：[MII_ANNPTR](#ga3f3ed3ecfd22b34b840ff2473ca68490)。

自动协商下一页发送寄存器（Auto-Negotiation Next Page Transmit Register）。

<a id="r_gaf17d80457d4a609d16793870d4a76bdf"></a>

```c
#define MII_ANLPRNPR 0x8
```

相关声明：[MII_ANLPRNPR](#gaf17d80457d4a609d16793870d4a76bdf)。

自动协商链路伙伴接收下一页寄存器（Auto-Negotiation Link Partner Received Next Page Register）。

<a id="r_ga9e258e8e518579ac5f9a8809ddc6aedb"></a>

```c
#define MII_1KTCR 0x9
```

相关声明：[MII_1KTCR](#ga9e258e8e518579ac5f9a8809ddc6aedb)。

1000BASE-T 控制寄存器（Control Register）。

<a id="r_ga49a74b346b13cc80c159c0f8f6b9c0f0"></a>

```c
#define MII_1KSTSR 0xa
```

相关声明：[MII_1KSTSR](#ga49a74b346b13cc80c159c0f8f6b9c0f0)。

1000BASE-T 状态寄存器（Status Register）。

<a id="r_ga7d6687385994aac21782308af560b224"></a>

```c
#define MII_MMD_ACR 0xd
```

相关声明：[MII_MMD_ACR](#ga7d6687385994aac21782308af560b224)。

MMD 访问控制寄存器（Access Control Register）。

<a id="r_ga378832f55be1a03977c829f09dd1d364"></a>

```c
#define MII_MMD_AADR 0xe
```

相关声明：[MII_MMD_AADR](#ga378832f55be1a03977c829f09dd1d364)。

MMD 访问地址数据寄存器（Access Address Data Register）。

<a id="r_gaa705f43dba50029d5395379e1f2b802d"></a>

```c
#define MII_ESTAT 0xf
```

相关声明：[MII_ESTAT](#gaa705f43dba50029d5395379e1f2b802d)。

扩展状态寄存器（Extended Status Register）。

## 11.4\_基本模式控制寄存器位定义（Basic Mode Control Register (BMCR) bit definitions）

<a id="r_ga54df4d055d02d507cf52eb1a2811f1de"></a>

```c
#define MII_BMCR_RESET_BIT 15
```

相关声明：[MII_BMCR_RESET_BIT](#ga54df4d055d02d507cf52eb1a2811f1de)。

PHY 复位位位置（Reset Bit Position）。

<a id="r_ga6e79703869a5e6459a4cbf2c103b8ed1"></a>

```c
#define MII_BMCR_LOOPBACK_BIT 14
```

相关声明：[MII_BMCR_LOOPBACK_BIT](#ga6e79703869a5e6459a4cbf2c103b8ed1)。

环回模式位位置（Loopback Mode Bit Position）。

<a id="r_ga689b3d9154d01a6cd2ac12ca252d5dc6"></a>

```c
#define MII_BMCR_SPEED_LSB_BIT 13
```

相关声明：[MII_BMCR_SPEED_LSB_BIT](#ga689b3d9154d01a6cd2ac12ca252d5dc6)。

速率选择最低有效位位置（Speed Selection LSB Bit Position）。

<a id="r_ga780566e06059ce969cf2c7149cd28560"></a>

```c
#define MII_BMCR_AUTONEG_ENABLE_BIT 12
```

相关声明：[MII_BMCR_AUTONEG_ENABLE_BIT](#ga780566e06059ce969cf2c7149cd28560)。

自动协商使能位位置（Auto-Negotiation Enable Bit Position）。

<a id="r_gafc726725b78ff3aed31a7ec30e168831"></a>

```c
#define MII_BMCR_POWER_DOWN_BIT 11
```

相关声明：[MII_BMCR_POWER_DOWN_BIT](#gafc726725b78ff3aed31a7ec30e168831)。

掉电位位置（Power-down Bit Position）。

<a id="r_ga0c5b114330969ddfeb8a042b33561bb4"></a>

```c
#define MII_BMCR_ISOLATE_BIT 10
```

相关声明：[MII_BMCR_ISOLATE_BIT](#ga0c5b114330969ddfeb8a042b33561bb4)。

隔离位位置（Isolate Bit Position）。

<a id="r_gaca9844340da91e466e7303e9f5b0425f"></a>

```c
#define MII_BMCR_AUTONEG_RESTART_BIT 9
```

相关声明：[MII_BMCR_AUTONEG_RESTART_BIT](#gaca9844340da91e466e7303e9f5b0425f)。

重新启动自动协商位位置（Restart Auto-Negotiation Bit Position）。

<a id="r_ga728082a7fb53de09ed3259e14fe6a539"></a>

```c
#define MII_BMCR_DUPLEX_MODE_BIT 8
```

相关声明：[MII_BMCR_DUPLEX_MODE_BIT](#ga728082a7fb53de09ed3259e14fe6a539)。

双工模式位位置（Duplex Mode Bit Position）。

<a id="r_gad75a0984bdbebe75921c6986a5122f30"></a>

```c
#define MII_BMCR_SPEED_MSB_BIT 6
```

相关声明：[MII_BMCR_SPEED_MSB_BIT](#gad75a0984bdbebe75921c6986a5122f30)。

速率选择最高有效位位置（Speed Selection MSB Bit Position）。

<a id="r_ga1001ac1540dc5bb6c4962f63b5fd6c3a"></a>

```c
#define MII_BMCR_RESET BIT(MII_BMCR_RESET_BIT)
```

相关声明：[MII_BMCR_RESET](#ga1001ac1540dc5bb6c4962f63b5fd6c3a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_RESET_BIT](#ga54df4d055d02d507cf52eb1a2811f1de)。

PHY 复位（Reset）。

<a id="r_gaaade3d675167c736186a03dad857a7c9"></a>

```c
#define MII_BMCR_LOOPBACK BIT(MII_BMCR_LOOPBACK_BIT)
```

相关声明：[MII_BMCR_LOOPBACK](#gaaade3d675167c736186a03dad857a7c9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_LOOPBACK_BIT](#ga6e79703869a5e6459a4cbf2c103b8ed1)。

启用环回模式（Loopback Mode）。

<a id="r_ga19ef6d51e7bc231892635d856dd6a747"></a>

```c
#define MII_BMCR_SPEED_LSB BIT(MII_BMCR_SPEED_LSB_BIT)
```

相关声明：[MII_BMCR_SPEED_LSB](#ga19ef6d51e7bc231892635d856dd6a747)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_SPEED_LSB_BIT](#ga689b3d9154d01a6cd2ac12ca252d5dc6)。

速率编码（Speed Encoding）：10 = 1000 Mbps；01 = 100 Mbps；00 = 10 Mbps。

<a id="r_gaf58b450219ae18dfa2526c685a0402a7"></a>

```c
#define MII_BMCR_AUTONEG_ENABLE BIT(MII_BMCR_AUTONEG_ENABLE_BIT)
```

相关声明：[MII_BMCR_AUTONEG_ENABLE](#gaf58b450219ae18dfa2526c685a0402a7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_AUTONEG_ENABLE_BIT](#ga780566e06059ce969cf2c7149cd28560)。

启用自动协商（Auto-Negotiation Enable）。

<a id="r_ga2598b7655be14619dffc44b9a6db36b8"></a>

```c
#define MII_BMCR_POWER_DOWN BIT(MII_BMCR_POWER_DOWN_BIT)
```

相关声明：[MII_BMCR_POWER_DOWN](#ga2598b7655be14619dffc44b9a6db36b8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_POWER_DOWN_BIT](#gafc726725b78ff3aed31a7ec30e168831)。

掉电模式（Power Down Mode）。

<a id="r_ga288b983fab32fb073cc42c3817b2c217"></a>

```c
#define MII_BMCR_ISOLATE BIT(MII_BMCR_ISOLATE_BIT)
```

相关声明：[MII_BMCR_ISOLATE](#ga288b983fab32fb073cc42c3817b2c217)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_ISOLATE_BIT](#ga0c5b114330969ddfeb8a042b33561bb4)。

在电气上将 PHY 与介质独立接口（MII）隔离。

<a id="r_ga110d6e1bfdbb37aa95cf1b32c54d8fa0"></a>

```c
#define MII_BMCR_AUTONEG_RESTART BIT(MII_BMCR_AUTONEG_RESTART_BIT)
```

相关声明：[MII_BMCR_AUTONEG_RESTART](#ga110d6e1bfdbb37aa95cf1b32c54d8fa0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_AUTONEG_RESTART_BIT](#gaca9844340da91e466e7303e9f5b0425f)。

重新启动自动协商（Auto-negotiation）。

<a id="r_ga288bc52d6545ec634e6c2da04dbe86d3"></a>

```c
#define MII_BMCR_DUPLEX_MODE BIT(MII_BMCR_DUPLEX_MODE_BIT)
```

相关声明：[MII_BMCR_DUPLEX_MODE](#ga288bc52d6545ec634e6c2da04dbe86d3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_DUPLEX_MODE_BIT](#ga728082a7fb53de09ed3259e14fe6a539)。

全双工模式（Full Duplex Mode）。

<a id="r_ga94e2ff6468b89371ec22a087ad5477d4"></a>

```c
#define MII_BMCR_SPEED_MSB BIT(MII_BMCR_SPEED_MSB_BIT)
```

相关声明：[MII_BMCR_SPEED_MSB](#ga94e2ff6468b89371ec22a087ad5477d4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_SPEED_MSB_BIT](#gad75a0984bdbebe75921c6986a5122f30)。

速率编码（Speed Encoding）：10 = 1000 Mbps；01 = 100 Mbps；00 = 10 Mbps。

<a id="r_gaf562ae173424ea0d41afd68d11f87115"></a>

```c
#define MII_BMCR_SPEED_MASK (MII_BMCR_SPEED_MSB | MII_BMCR_SPEED_LSB)
```

相关声明：[MII_BMCR_SPEED_MASK](#gaf562ae173424ea0d41afd68d11f87115)、[MII_BMCR_SPEED_MSB](#ga94e2ff6468b89371ec22a087ad5477d4)、[MII_BMCR_SPEED_LSB](#ga19ef6d51e7bc231892635d856dd6a747)。

链路速率字段（Link Speed Field）。

<a id="r_ga4d31aeaad35fe6a358aef1eef1c5b4cf"></a>

```c
#define MII_BMCR_SPEED_10 0
```

相关声明：[MII_BMCR_SPEED_10](#ga4d31aeaad35fe6a358aef1eef1c5b4cf)。

选择 10 Mb/s 速率（Speed）。

<a id="r_gaf52c7fc2b468c142ae63605a201900d4"></a>

```c
#define MII_BMCR_SPEED_100 BIT(MII_BMCR_SPEED_LSB_BIT)
```

相关声明：[MII_BMCR_SPEED_100](#gaf52c7fc2b468c142ae63605a201900d4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_SPEED_LSB_BIT](#ga689b3d9154d01a6cd2ac12ca252d5dc6)。

选择 100 Mb/s 速率（Speed）。

<a id="r_gaae2f486072b95b3e829d0e1bd4b8d893"></a>

```c
#define MII_BMCR_SPEED_1000 BIT(MII_BMCR_SPEED_MSB_BIT)
```

相关声明：[MII_BMCR_SPEED_1000](#gaae2f486072b95b3e829d0e1bd4b8d893)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMCR_SPEED_MSB_BIT](#gad75a0984bdbebe75921c6986a5122f30)。

选择 1000 Mb/s 速率（Speed）。

## 11.5\_基本模式状态寄存器位定义（Basic Mode Status Register (BMSR) bit definitions）

<a id="r_ga6d815d61b5566b26fb0eb2cf78be689d"></a>

```c
#define MII_BMSR_100BASE_T4_BIT 15
```

相关声明：[MII_BMSR_100BASE_T4_BIT](#ga6d815d61b5566b26fb0eb2cf78be689d)。

100BASE-T4 能力位位置（Capable Bit Position）。

<a id="r_ga85d42ee9a1dd81d27ba74ec4fff8e61a"></a>

```c
#define MII_BMSR_100BASE_X_FULL_BIT 14
```

相关声明：[MII_BMSR_100BASE_X_FULL_BIT](#ga85d42ee9a1dd81d27ba74ec4fff8e61a)。

100BASE-X 全双工能力位位置（Full Duplex Capable Bit Position）。

<a id="r_ga1502cf548fb5393b698fd1fcbe5d6a3b"></a>

```c
#define MII_BMSR_100BASE_X_HALF_BIT 13
```

相关声明：[MII_BMSR_100BASE_X_HALF_BIT](#ga1502cf548fb5393b698fd1fcbe5d6a3b)。

100BASE-X 半双工能力位位置（Half Duplex Capable Bit Position）。

<a id="r_ga2aefc1cd403db957440b01e5df54a7fa"></a>

```c
#define MII_BMSR_10_FULL_BIT 12
```

相关声明：[MII_BMSR_10_FULL_BIT](#ga2aefc1cd403db957440b01e5df54a7fa)。

10 Mb/s 全双工能力位位置（Full Duplex Capable Bit Position）。

<a id="r_gab5cbdb762b820a7265fccdbeba80478a"></a>

```c
#define MII_BMSR_10_HALF_BIT 11
```

相关声明：[MII_BMSR_10_HALF_BIT](#gab5cbdb762b820a7265fccdbeba80478a)。

10 Mb/s 半双工能力位位置（Half Duplex Capable Bit Position）。

<a id="r_ga37c6de155f12c3c2d3593040386e2590"></a>

```c
#define MII_BMSR_100BASE_T2_FULL_BIT 10
```

相关声明：[MII_BMSR_100BASE_T2_FULL_BIT](#ga37c6de155f12c3c2d3593040386e2590)。

100BASE-T2 全双工能力位位置（Full Duplex Capable Bit Position）。

<a id="r_gab0e7bf45469a11187ee00eed60f27408"></a>

```c
#define MII_BMSR_100BASE_T2_HALF_BIT 9
```

相关声明：[MII_BMSR_100BASE_T2_HALF_BIT](#gab0e7bf45469a11187ee00eed60f27408)。

100BASE-T2 半双工能力位位置（Half Duplex Capable Bit Position）。

<a id="r_ga017891e6a6cb799e2795d27d482bacf1"></a>

```c
#define MII_BMSR_EXTEND_STATUS_BIT 8
```

相关声明：[MII_BMSR_EXTEND_STATUS_BIT](#ga017891e6a6cb799e2795d27d482bacf1)。

扩展状态信息位位置（Extended Status Information Bit Position）。

<a id="r_ga5fe389f8d8dbb6900ee8edcbae645ca7"></a>

```c
#define MII_BMSR_MF_PREAMB_SUPPR_BIT 6
```

相关声明：[MII_BMSR_MF_PREAMB_SUPPR_BIT](#ga5fe389f8d8dbb6900ee8edcbae645ca7)。

前导码抑制能力位位置（Preamble Suppression Capable Bit Position）。

<a id="r_ga110eb8cc56b72287f30da929838029e0"></a>

```c
#define MII_BMSR_AUTONEG_COMPLETE_BIT 5
```

相关声明：[MII_BMSR_AUTONEG_COMPLETE_BIT](#ga110eb8cc56b72287f30da929838029e0)。

自动协商完成位位置（Auto-Negotiation Complete Bit Position）。

<a id="r_gaf8cd939b545f4d9cb8798169d1e1b718"></a>

```c
#define MII_BMSR_REMOTE_FAULT_BIT 4
```

相关声明：[MII_BMSR_REMOTE_FAULT_BIT](#gaf8cd939b545f4d9cb8798169d1e1b718)。

远端故障位位置（Remote Fault Bit Position）。

<a id="r_ga0c456682a2aa1e678b753edc90dd7173"></a>

```c
#define MII_BMSR_AUTONEG_ABILITY_BIT 3
```

相关声明：[MII_BMSR_AUTONEG_ABILITY_BIT](#ga0c456682a2aa1e678b753edc90dd7173)。

自动协商能力位位置（Auto-Negotiation Ability Bit Position）。

<a id="r_gace14dd35d99a13fea32169bba957cf64"></a>

```c
#define MII_BMSR_LINK_STATUS_BIT 2
```

相关声明：[MII_BMSR_LINK_STATUS_BIT](#gace14dd35d99a13fea32169bba957cf64)。

链路状态位位置（Link Status Bit Position）。

<a id="r_ga302ccc7731400f1552d870b6c60daf6b"></a>

```c
#define MII_BMSR_JABBER_DETECT_BIT 1
```

相关声明：[MII_BMSR_JABBER_DETECT_BIT](#ga302ccc7731400f1552d870b6c60daf6b)。

异常长发送检测位位置（Jabber Detect Bit Position）。

<a id="r_ga430bd15994b0ee73b0802f0a2760e67b"></a>

```c
#define MII_BMSR_EXTEND_CAPAB_BIT 0
```

相关声明：[MII_BMSR_EXTEND_CAPAB_BIT](#ga430bd15994b0ee73b0802f0a2760e67b)。

扩展能力位位置（Extended Capability Bit Position）。

<a id="r_gac8a404aa082745cb7699739bf58fc530"></a>

```c
#define MII_BMSR_100BASE_T4 BIT(MII_BMSR_100BASE_T4_BIT)
```

相关声明：[MII_BMSR_100BASE_T4](#gac8a404aa082745cb7699739bf58fc530)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_100BASE_T4_BIT](#ga6d815d61b5566b26fb0eb2cf78be689d)。

具有 100BASE-T4 能力（Capable）。

<a id="r_ga090c828a41acfc824b56ec2a9a57082a"></a>

```c
#define MII_BMSR_100BASE_X_FULL BIT(MII_BMSR_100BASE_X_FULL_BIT)
```

相关声明：[MII_BMSR_100BASE_X_FULL](#ga090c828a41acfc824b56ec2a9a57082a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_100BASE_X_FULL_BIT](#ga85d42ee9a1dd81d27ba74ec4fff8e61a)。

具有 100BASE-X 全双工能力（Full Duplex Capable）。

<a id="r_ga608ec5361c44f25c34ae6138ae7ffef9"></a>

```c
#define MII_BMSR_100BASE_X_HALF BIT(MII_BMSR_100BASE_X_HALF_BIT)
```

相关声明：[MII_BMSR_100BASE_X_HALF](#ga608ec5361c44f25c34ae6138ae7ffef9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_100BASE_X_HALF_BIT](#ga1502cf548fb5393b698fd1fcbe5d6a3b)。

具有 100BASE-X 半双工能力（Half Duplex Capable）。

<a id="r_ga4f085921a6b0f0586326b1bdc8f62b31"></a>

```c
#define MII_BMSR_10_FULL BIT(MII_BMSR_10_FULL_BIT)
```

相关声明：[MII_BMSR_10_FULL](#ga4f085921a6b0f0586326b1bdc8f62b31)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_10_FULL_BIT](#ga2aefc1cd403db957440b01e5df54a7fa)。

具有 10 Mb/s 全双工能力（Full Duplex Capable）。

<a id="r_ga8505886511fef3ec2d8630a957de4478"></a>

```c
#define MII_BMSR_10_HALF BIT(MII_BMSR_10_HALF_BIT)
```

相关声明：[MII_BMSR_10_HALF](#ga8505886511fef3ec2d8630a957de4478)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_10_HALF_BIT](#gab5cbdb762b820a7265fccdbeba80478a)。

具有 10 Mb/s 半双工能力（Half Duplex Capable）。

<a id="r_ga93fb7b79b3da2ae1757fe98237dd2d6b"></a>

```c
#define MII_BMSR_100BASE_T2_FULL BIT(MII_BMSR_100BASE_T2_FULL_BIT)
```

相关声明：[MII_BMSR_100BASE_T2_FULL](#ga93fb7b79b3da2ae1757fe98237dd2d6b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_100BASE_T2_FULL_BIT](#ga37c6de155f12c3c2d3593040386e2590)。

具有 100BASE-T2 全双工能力（Full Duplex Capable）。

<a id="r_gafb0d83d336eda611d45580be48f15d02"></a>

```c
#define MII_BMSR_100BASE_T2_HALF BIT(MII_BMSR_100BASE_T2_HALF_BIT)
```

相关声明：[MII_BMSR_100BASE_T2_HALF](#gafb0d83d336eda611d45580be48f15d02)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_100BASE_T2_HALF_BIT](#gab0e7bf45469a11187ee00eed60f27408)。

具有 100BASE-T2 半双工能力（Half Duplex Capable）。

<a id="r_ga24992988cde973ce2a954fe372a5ad0e"></a>

```c
#define MII_BMSR_EXTEND_STATUS BIT(MII_BMSR_EXTEND_STATUS_BIT)
```

相关声明：[MII_BMSR_EXTEND_STATUS](#ga24992988cde973ce2a954fe372a5ad0e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_EXTEND_STATUS_BIT](#ga017891e6a6cb799e2795d27d482bacf1)。

寄存器 15 中的扩展状态信息（Extended Status Information）。

<a id="r_gae85e29e0f9a50898f93ff6e5a5f763e4"></a>

```c
#define MII_BMSR_MF_PREAMB_SUPPR BIT(MII_BMSR_MF_PREAMB_SUPPR_BIT)
```

相关声明：[MII_BMSR_MF_PREAMB_SUPPR](#gae85e29e0f9a50898f93ff6e5a5f763e4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_MF_PREAMB_SUPPR_BIT](#ga5fe389f8d8dbb6900ee8edcbae645ca7)。

PHY 接受省略前导码（Preamble Suppressed）的管理帧（Management Frames）。

<a id="r_gac5b9ac6b54ce146c91197660c2ccd207"></a>

```c
#define MII_BMSR_AUTONEG_COMPLETE BIT(MII_BMSR_AUTONEG_COMPLETE_BIT)
```

相关声明：[MII_BMSR_AUTONEG_COMPLETE](#gac5b9ac6b54ce146c91197660c2ccd207)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_AUTONEG_COMPLETE_BIT](#ga110eb8cc56b72287f30da929838029e0)。

自动协商过程（Auto-negotiation Process）已完成。

<a id="r_ga0dd8421740c52ecd5e6a53e969d2e48a"></a>

```c
#define MII_BMSR_REMOTE_FAULT BIT(MII_BMSR_REMOTE_FAULT_BIT)
```

相关声明：[MII_BMSR_REMOTE_FAULT](#ga0dd8421740c52ecd5e6a53e969d2e48a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_REMOTE_FAULT_BIT](#gaf8cd939b545f4d9cb8798169d1e1b718)。

检测到远端故障（Remote Fault）。

<a id="r_gafc344357c76d6a41c5fa432d55355fce"></a>

```c
#define MII_BMSR_AUTONEG_ABILITY BIT(MII_BMSR_AUTONEG_ABILITY_BIT)
```

相关声明：[MII_BMSR_AUTONEG_ABILITY](#gafc344357c76d6a41c5fa432d55355fce)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_AUTONEG_ABILITY_BIT](#ga0c456682a2aa1e678b753edc90dd7173)。

PHY 能够执行自动协商（Auto-Negotiation）。

<a id="r_ga884d39c456206cee38ce5a9a9ca01599"></a>

```c
#define MII_BMSR_LINK_STATUS BIT(MII_BMSR_LINK_STATUS_BIT)
```

相关声明：[MII_BMSR_LINK_STATUS](#ga884d39c456206cee38ce5a9a9ca01599)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_LINK_STATUS_BIT](#gace14dd35d99a13fea32169bba957cf64)。

链路已建立（Link Up）。

<a id="r_gad9ef4a2223dfee6826b0fdc8b25802ea"></a>

```c
#define MII_BMSR_JABBER_DETECT BIT(MII_BMSR_JABBER_DETECT_BIT)
```

相关声明：[MII_BMSR_JABBER_DETECT](#gad9ef4a2223dfee6826b0fdc8b25802ea)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_JABBER_DETECT_BIT](#ga302ccc7731400f1552d870b6c60daf6b)。

检测到异常长发送状态（Jabber Condition）。

<a id="r_gab225377deb09eb179b7efee199c7edd4"></a>

```c
#define MII_BMSR_EXTEND_CAPAB BIT(MII_BMSR_EXTEND_CAPAB_BIT)
```

相关声明：[MII_BMSR_EXTEND_CAPAB](#gab225377deb09eb179b7efee199c7edd4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_BMSR_EXTEND_CAPAB_BIT](#ga430bd15994b0ee73b0802f0a2760e67b)。

扩展寄存器能力（Extended Register Capabilities）。

## 11.6\_自动协商通告与链路伙伴能力（Auto-negotiation Advertisement (ANAR) and Link Partner Ability）

自动协商链路伙伴能力寄存器（ANLPAR）的寄存器位定义（Register Bit Definitions）。

<a id="r_ga22cb9fe314c187beee08d1c1e41d8373"></a>

```c
#define MII_ADVERTISE_NEXT_PAGE_BIT 15
```

相关声明：[MII_ADVERTISE_NEXT_PAGE_BIT](#ga22cb9fe314c187beee08d1c1e41d8373)。

下一页位位置（Next Page Bit Position）。

<a id="r_gaf8344fb430b18d38d4abdc0143375df6"></a>

```c
#define MII_ADVERTISE_LPACK_BIT 14
```

相关声明：[MII_ADVERTISE_LPACK_BIT](#gaf8344fb430b18d38d4abdc0143375df6)。

链路伙伴确认位位置（Link Partner Acknowledge Bit Position）。

<a id="r_ga6bce3c2f70cddc50205a330158612f8c"></a>

```c
#define MII_ADVERTISE_REMOTE_FAULT_BIT 13
```

相关声明：[MII_ADVERTISE_REMOTE_FAULT_BIT](#ga6bce3c2f70cddc50205a330158612f8c)。

远端故障位位置（Remote Fault Bit Position）。

<a id="r_ga4c5ac54f1516343790181acfbf5529c8"></a>

```c
#define MII_ADVERTISE_ASYM_PAUSE_BIT 11
```

相关声明：[MII_ADVERTISE_ASYM_PAUSE_BIT](#ga4c5ac54f1516343790181acfbf5529c8)。

非对称暂停位位置（Asymmetric Pause Bit Position）。

<a id="r_ga35994af1965ff3f9aa68d203241f97d3"></a>

```c
#define MII_ADVERTISE_PAUSE_BIT 10
```

相关声明：[MII_ADVERTISE_PAUSE_BIT](#ga35994af1965ff3f9aa68d203241f97d3)。

暂停位位置（Pause Bit Position）。

<a id="r_ga825049982099c0601da4f801fccb6e64"></a>

```c
#define MII_ADVERTISE_100BASE_T4_BIT 9
```

相关声明：[MII_ADVERTISE_100BASE_T4_BIT](#ga825049982099c0601da4f801fccb6e64)。

100BASE-T4 支持位位置（Support Bit Position）。

<a id="r_ga02d2b86da4062c296c154013b255d720"></a>

```c
#define MII_ADVERTISE_100_FULL_BIT 8
```

相关声明：[MII_ADVERTISE_100_FULL_BIT](#ga02d2b86da4062c296c154013b255d720)。

100BASE-X 全双工支持位位置（Full Duplex Support Bit Position）。

<a id="r_ga949f20431a0ccfef97e6d2b5ee0484c0"></a>

```c
#define MII_ADVERTISE_100_HALF_BIT 7
```

相关声明：[MII_ADVERTISE_100_HALF_BIT](#ga949f20431a0ccfef97e6d2b5ee0484c0)。

100BASE-X 半双工支持位位置（Half Duplex Support Bit Position）。

<a id="r_ga4ee2f6bdb657842db35e396839896cc8"></a>

```c
#define MII_ADVERTISE_10_FULL_BIT 6
```

相关声明：[MII_ADVERTISE_10_FULL_BIT](#ga4ee2f6bdb657842db35e396839896cc8)。

10 Mb/s 全双工支持位位置（Full Duplex Support Bit Position）。

<a id="r_ga622c65ecfadf01ff4bb4f9dd06393428"></a>

```c
#define MII_ADVERTISE_10_HALF_BIT 5
```

相关声明：[MII_ADVERTISE_10_HALF_BIT](#ga622c65ecfadf01ff4bb4f9dd06393428)。

10 Mb/s 半双工支持位位置（Half Duplex Support Bit Position）。

<a id="r_ga4e567fc428a19d55c13c6be38091ed59"></a>

```c
#define MII_ADVERTISE_NEXT_PAGE BIT(MII_ADVERTISE_NEXT_PAGE_BIT)
```

相关声明：[MII_ADVERTISE_NEXT_PAGE](#ga4e567fc428a19d55c13c6be38091ed59)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_NEXT_PAGE_BIT](#ga22cb9fe314c187beee08d1c1e41d8373)。

下一页（Next Page）。

<a id="r_gaca8ed07be80166e8abaefb4135008989"></a>

```c
#define MII_ADVERTISE_LPACK BIT(MII_ADVERTISE_LPACK_BIT)
```

相关声明：[MII_ADVERTISE_LPACK](#gaca8ed07be80166e8abaefb4135008989)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_LPACK_BIT](#gaf8344fb430b18d38d4abdc0143375df6)。

链路伙伴确认响应（Link Partner Acknowledge Response）。

<a id="r_ga3e1cfef9ac347b86324d25c1d00a07ef"></a>

```c
#define MII_ADVERTISE_REMOTE_FAULT BIT(MII_ADVERTISE_REMOTE_FAULT_BIT)
```

相关声明：[MII_ADVERTISE_REMOTE_FAULT](#ga3e1cfef9ac347b86324d25c1d00a07ef)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_REMOTE_FAULT_BIT](#ga6bce3c2f70cddc50205a330158612f8c)。

远端故障（Remote Fault）。

<a id="r_gaf8b5e7fc3226b89b875f46a50165e332"></a>

```c
#define MII_ADVERTISE_ASYM_PAUSE BIT(MII_ADVERTISE_ASYM_PAUSE_BIT)
```

相关声明：[MII_ADVERTISE_ASYM_PAUSE](#gaf8b5e7fc3226b89b875f46a50165e332)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_ASYM_PAUSE_BIT](#ga4c5ac54f1516343790181acfbf5529c8)。

尝试协商非对称暂停（Asymmetric Pause）。

<a id="r_ga7b3dfbe50b37378cbf45d15f9ef88c7f"></a>

```c
#define MII_ADVERTISE_PAUSE BIT(MII_ADVERTISE_PAUSE_BIT)
```

相关声明：[MII_ADVERTISE_PAUSE](#ga7b3dfbe50b37378cbf45d15f9ef88c7f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_PAUSE_BIT](#ga35994af1965ff3f9aa68d203241f97d3)。

尝试协商暂停（Pause）。

<a id="r_ga11a26530d734fb68be5538ac36019821"></a>

```c
#define MII_ADVERTISE_100BASE_T4 BIT(MII_ADVERTISE_100BASE_T4_BIT)
```

相关声明：[MII_ADVERTISE_100BASE_T4](#ga11a26530d734fb68be5538ac36019821)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_100BASE_T4_BIT](#ga825049982099c0601da4f801fccb6e64)。

尝试协商 100BASE-T4 支持（Support）。

<a id="r_ga72f632c88cf6c472b893c326d7a8d263"></a>

```c
#define MII_ADVERTISE_100_FULL BIT(MII_ADVERTISE_100_FULL_BIT)
```

相关声明：[MII_ADVERTISE_100_FULL](#ga72f632c88cf6c472b893c326d7a8d263)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_100_FULL_BIT](#ga02d2b86da4062c296c154013b255d720)。

尝试协商 100BASE-X 全双工支持（Full Duplex Support）。

<a id="r_ga357539fe99d327cae0e76acd5059876f"></a>

```c
#define MII_ADVERTISE_100_HALF BIT(MII_ADVERTISE_100_HALF_BIT)
```

相关声明：[MII_ADVERTISE_100_HALF](#ga357539fe99d327cae0e76acd5059876f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_100_HALF_BIT](#ga949f20431a0ccfef97e6d2b5ee0484c0)。

尝试协商 100BASE-X 支持（Support）。

<a id="r_ga44ee311ef785619a215de80fc0286a4c"></a>

```c
#define MII_ADVERTISE_10_FULL BIT(MII_ADVERTISE_10_FULL_BIT)
```

相关声明：[MII_ADVERTISE_10_FULL](#ga44ee311ef785619a215de80fc0286a4c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_10_FULL_BIT](#ga4ee2f6bdb657842db35e396839896cc8)。

尝试协商 10 Mb/s 全双工支持（Full Duplex Support）。

<a id="r_gac5c508943ce4006fa2f934c25436fdb5"></a>

```c
#define MII_ADVERTISE_10_HALF BIT(MII_ADVERTISE_10_HALF_BIT)
```

相关声明：[MII_ADVERTISE_10_HALF](#gac5c508943ce4006fa2f934c25436fdb5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_10_HALF_BIT](#ga622c65ecfadf01ff4bb4f9dd06393428)。

尝试协商 10 Mb/s 半双工支持（Half Duplex Support）。

<a id="r_gac01baecf625bbb6d55a14ac0c2b181bd"></a>

```c
#define MII_ADVERTISE_SEL_MASK (0x1F << 0)
```

相关声明：[MII_ADVERTISE_SEL_MASK](#gac01baecf625bbb6d55a14ac0c2b181bd)。

选择器字段掩码（Selector Field Mask）。

<a id="r_ga9abdfc8110120f54612c712d86cab3ac"></a>

```c
#define MII_ADVERTISE_SEL_IEEE_802_3 0x01
```

相关声明：[MII_ADVERTISE_SEL_IEEE_802_3](#ga9abdfc8110120f54612c712d86cab3ac)。

选择器字段（Selector Field）。

## 11.7\_1000BASE-T控制寄存器位定义（1000BASE-T Control Register bit definitions）

<a id="r_gabeda2717f8c4d425ccf4562ff6fac4fb"></a>

```c
#define MII_ADVERTISE_1000_FULL_BIT 9
```

相关声明：[MII_ADVERTISE_1000_FULL_BIT](#gabeda2717f8c4d425ccf4562ff6fac4fb)。

1000BASE-T 全双工支持位位置（Full Duplex Support Bit Position）。

<a id="r_gaaeef419de1d90bfd58ba3452218e9004"></a>

```c
#define MII_ADVERTISE_1000_HALF_BIT 8
```

相关声明：[MII_ADVERTISE_1000_HALF_BIT](#gaaeef419de1d90bfd58ba3452218e9004)。

1000BASE-T 半双工支持位位置（Half Duplex Support Bit Position）。

<a id="r_ga028ddaf632ced31e57249883c90ed921"></a>

```c
#define MII_ADVERTISE_1000_FULL BIT(MII_ADVERTISE_1000_FULL_BIT)
```

相关声明：[MII_ADVERTISE_1000_FULL](#ga028ddaf632ced31e57249883c90ed921)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_1000_FULL_BIT](#gabeda2717f8c4d425ccf4562ff6fac4fb)。

尝试协商 1000BASE-T 全双工支持（Full Duplex Support）。

<a id="r_ga5f36d375690560688185d1207687611b"></a>

```c
#define MII_ADVERTISE_1000_HALF BIT(MII_ADVERTISE_1000_HALF_BIT)
```

相关声明：[MII_ADVERTISE_1000_HALF](#ga5f36d375690560688185d1207687611b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[MII_ADVERTISE_1000_HALF_BIT](#gaaeef419de1d90bfd58ba3452218e9004)。

尝试协商 1000BASE-T 半双工支持（Half Duplex Support）。

## 11.8\_扩展状态寄存器位定义（Extended Status Register bit definitions）

<a id="r_ga846525a526aa9704a175c84771e48290"></a>

```c
#define MII_ESTAT_1000BASE_X_FULL BIT(15)
```

相关声明：[MII_ESTAT_1000BASE_X_FULL](#ga846525a526aa9704a175c84771e48290)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

具有 1000BASE-X 全双工能力（Full-duplex Capable）。

<a id="r_gabec9696aa599caca1131f869827bbc95"></a>

```c
#define MII_ESTAT_1000BASE_X_HALF BIT(14)
```

相关声明：[MII_ESTAT_1000BASE_X_HALF](#gabec9696aa599caca1131f869827bbc95)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

具有 1000BASE-X 半双工能力（Half-duplex Capable）。

<a id="r_gada0831dbbb86ff717b40c23c73345731"></a>

```c
#define MII_ESTAT_1000BASE_T_FULL BIT(13)
```

相关声明：[MII_ESTAT_1000BASE_T_FULL](#gada0831dbbb86ff717b40c23c73345731)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

具有 1000BASE-T 全双工能力（Full-duplex Capable）。

<a id="r_ga42e8d732fd9806e218599871fd1291d5"></a>

```c
#define MII_ESTAT_1000BASE_T_HALF BIT(12)
```

相关声明：[MII_ESTAT_1000BASE_T_HALF](#ga42e8d732fd9806e218599871fd1291d5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

具有 1000BASE-T 半双工能力（Half-duplex Capable）。

## 11.9\_MMD访问控制寄存器位定义（MMD Access Control Register (MII_MMD_ACR) bit definitions）

<a id="r_gae4ac896c90a75cdc4869797708823673"></a>

```c
#define MII_MMD_ACR_DEVAD_MASK (0x1F << 0)
```

相关声明：[MII_MMD_ACR_DEVAD_MASK](#gae4ac896c90a75cdc4869797708823673)。

设备地址掩码（DEVAD Mask）。

<a id="r_ga0f312eab9b4d51af4a72f7cb3898754a"></a>

```c
#define MII_MMD_ACR_ADDR (0x00 << 14)
```

相关声明：[MII_MMD_ACR_ADDR](#ga0f312eab9b4d51af4a72f7cb3898754a)。

地址（Address）。

<a id="r_ga6cac36daf5db44274cd60a05b77819f4"></a>

```c
#define MII_MMD_ACR_DATA_NO_POS_INC (0x01 << 14)
```

相关声明：[MII_MMD_ACR_DATA_NO_POS_INC](#ga6cac36daf5db44274cd60a05b77819f4)。

数据访问，不后递增（No Post Increment）。

<a id="r_ga3be4dced4eec405c42467ba51c5efb9c"></a>

```c
#define MII_MMD_ACR_DATA_RW_POS_INC (0x10 << 14)
```

相关声明：[MII_MMD_ACR_DATA_RW_POS_INC](#ga3be4dced4eec405c42467ba51c5efb9c)。

数据访问，读写后均递增（Post Increment on Reads and Writes）。

<a id="r_ga48f56892c3e8d6ec7e90a7e36dd67309"></a>

```c
#define MII_MMD_ACR_DATA_W_POS_INC (0x11 << 14)
```

相关声明：[MII_MMD_ACR_DATA_W_POS_INC](#ga48f56892c3e8d6ec7e90a7e36dd67309)。

数据访问，仅写后递增（Post Increment on Writes Only）。

## 11.10\_详细说明（Detailed Documentation）

<a id="ga49a74b346b13cc80c159c0f8f6b9c0f0"></a>

### `MII_1KSTSR`

```c
#define MII_1KSTSR 0xa
```

```c
#include <zephyr/net/mii.h>
```

1000BASE-T 状态寄存器（Status Register）。

<a id="ga9e258e8e518579ac5f9a8809ddc6aedb"></a>

### `MII_1KTCR`

```c
#define MII_1KTCR 0x9
```

```c
#include <zephyr/net/mii.h>
```

1000BASE-T 控制寄存器（Control Register）。

<a id="ga028ddaf632ced31e57249883c90ed921"></a>

### `MII_ADVERTISE_1000_FULL`

```c
#define MII_ADVERTISE_1000_FULL BIT(MII_ADVERTISE_1000_FULL_BIT)
```

```c
#include <zephyr/net/mii.h>
```

尝试协商 1000BASE-T 全双工支持（Full Duplex Support）。

<a id="gabeda2717f8c4d425ccf4562ff6fac4fb"></a>

### `MII_ADVERTISE_1000_FULL_BIT`

```c
#define MII_ADVERTISE_1000_FULL_BIT 9
```

```c
#include <zephyr/net/mii.h>
```

1000BASE-T 全双工支持位位置（Full Duplex Support Bit Position）。

<a id="ga5f36d375690560688185d1207687611b"></a>

### `MII_ADVERTISE_1000_HALF`

```c
#define MII_ADVERTISE_1000_HALF BIT(MII_ADVERTISE_1000_HALF_BIT)
```

```c
#include <zephyr/net/mii.h>
```

尝试协商 1000BASE-T 半双工支持（Half Duplex Support）。

<a id="gaaeef419de1d90bfd58ba3452218e9004"></a>

### `MII_ADVERTISE_1000_HALF_BIT`

```c
#define MII_ADVERTISE_1000_HALF_BIT 8
```

```c
#include <zephyr/net/mii.h>
```

1000BASE-T 半双工支持位位置（Half Duplex Support Bit Position）。

<a id="ga72f632c88cf6c472b893c326d7a8d263"></a>

### `MII_ADVERTISE_100_FULL`

```c
#define MII_ADVERTISE_100_FULL BIT(MII_ADVERTISE_100_FULL_BIT)
```

```c
#include <zephyr/net/mii.h>
```

尝试协商 100BASE-X 全双工支持（Full Duplex Support）。

<a id="ga02d2b86da4062c296c154013b255d720"></a>

### `MII_ADVERTISE_100_FULL_BIT`

```c
#define MII_ADVERTISE_100_FULL_BIT 8
```

```c
#include <zephyr/net/mii.h>
```

100BASE-X 全双工支持位位置（Full Duplex Support Bit Position）。

<a id="ga357539fe99d327cae0e76acd5059876f"></a>

### `MII_ADVERTISE_100_HALF`

```c
#define MII_ADVERTISE_100_HALF BIT(MII_ADVERTISE_100_HALF_BIT)
```

```c
#include <zephyr/net/mii.h>
```

尝试协商 100BASE-X 支持（Support）。

<a id="ga949f20431a0ccfef97e6d2b5ee0484c0"></a>

### `MII_ADVERTISE_100_HALF_BIT`

```c
#define MII_ADVERTISE_100_HALF_BIT 7
```

```c
#include <zephyr/net/mii.h>
```

100BASE-X 半双工支持位位置（Half Duplex Support Bit Position）。

<a id="ga11a26530d734fb68be5538ac36019821"></a>

### `MII_ADVERTISE_100BASE_T4`

```c
#define MII_ADVERTISE_100BASE_T4 BIT(MII_ADVERTISE_100BASE_T4_BIT)
```

```c
#include <zephyr/net/mii.h>
```

尝试协商 100BASE-T4 支持（Support）。

<a id="ga825049982099c0601da4f801fccb6e64"></a>

### `MII_ADVERTISE_100BASE_T4_BIT`

```c
#define MII_ADVERTISE_100BASE_T4_BIT 9
```

```c
#include <zephyr/net/mii.h>
```

100BASE-T4 支持位位置（Support Bit Position）。

<a id="ga44ee311ef785619a215de80fc0286a4c"></a>

### `MII_ADVERTISE_10_FULL`

```c
#define MII_ADVERTISE_10_FULL BIT(MII_ADVERTISE_10_FULL_BIT)
```

```c
#include <zephyr/net/mii.h>
```

尝试协商 10 Mb/s 全双工支持（Full Duplex Support）。

<a id="ga4ee2f6bdb657842db35e396839896cc8"></a>

### `MII_ADVERTISE_10_FULL_BIT`

```c
#define MII_ADVERTISE_10_FULL_BIT 6
```

```c
#include <zephyr/net/mii.h>
```

10 Mb/s 全双工支持位位置（Full Duplex Support Bit Position）。

<a id="gac5c508943ce4006fa2f934c25436fdb5"></a>

### `MII_ADVERTISE_10_HALF`

```c
#define MII_ADVERTISE_10_HALF BIT(MII_ADVERTISE_10_HALF_BIT)
```

```c
#include <zephyr/net/mii.h>
```

尝试协商 10 Mb/s 半双工支持（Half Duplex Support）。

<a id="ga622c65ecfadf01ff4bb4f9dd06393428"></a>

### `MII_ADVERTISE_10_HALF_BIT`

```c
#define MII_ADVERTISE_10_HALF_BIT 5
```

```c
#include <zephyr/net/mii.h>
```

10 Mb/s 半双工支持位位置（Half Duplex Support Bit Position）。

<a id="gacac6f915a8d0e3f8244c571646b3fc92"></a>

### `MII_ADVERTISE_ALL`

```c
#define MII_ADVERTISE_ALL
```

```c
#include <zephyr/net/mii.h>
```

展开值（Value）：

```c
(MII_ADVERTISE_10_HALF | MII_ADVERTISE_10_FULL |\
MII_ADVERTISE_100_HALF | MII_ADVERTISE_100_FULL |\
MII_ADVERTISE_SEL_IEEE_802_3)
```

通告全部速率（Advertise All Speeds）。

<a id="gaf8b5e7fc3226b89b875f46a50165e332"></a>

### `MII_ADVERTISE_ASYM_PAUSE`

```c
#define MII_ADVERTISE_ASYM_PAUSE BIT(MII_ADVERTISE_ASYM_PAUSE_BIT)
```

```c
#include <zephyr/net/mii.h>
```

尝试协商非对称暂停（Asymmetric Pause）。

<a id="ga4c5ac54f1516343790181acfbf5529c8"></a>

### `MII_ADVERTISE_ASYM_PAUSE_BIT`

```c
#define MII_ADVERTISE_ASYM_PAUSE_BIT 11
```

```c
#include <zephyr/net/mii.h>
```

非对称暂停位位置（Asymmetric Pause Bit Position）。

<a id="gaca8ed07be80166e8abaefb4135008989"></a>

### `MII_ADVERTISE_LPACK`

```c
#define MII_ADVERTISE_LPACK BIT(MII_ADVERTISE_LPACK_BIT)
```

```c
#include <zephyr/net/mii.h>
```

链路伙伴确认响应（Link Partner Acknowledge Response）。

<a id="gaf8344fb430b18d38d4abdc0143375df6"></a>

### `MII_ADVERTISE_LPACK_BIT`

```c
#define MII_ADVERTISE_LPACK_BIT 14
```

```c
#include <zephyr/net/mii.h>
```

链路伙伴确认位位置（Link Partner Acknowledge Bit Position）。

<a id="ga4e567fc428a19d55c13c6be38091ed59"></a>

### `MII_ADVERTISE_NEXT_PAGE`

```c
#define MII_ADVERTISE_NEXT_PAGE BIT(MII_ADVERTISE_NEXT_PAGE_BIT)
```

```c
#include <zephyr/net/mii.h>
```

下一页（Next Page）。

<a id="ga22cb9fe314c187beee08d1c1e41d8373"></a>

### `MII_ADVERTISE_NEXT_PAGE_BIT`

```c
#define MII_ADVERTISE_NEXT_PAGE_BIT 15
```

```c
#include <zephyr/net/mii.h>
```

下一页位位置（Next Page Bit Position）。

<a id="ga7b3dfbe50b37378cbf45d15f9ef88c7f"></a>

### `MII_ADVERTISE_PAUSE`

```c
#define MII_ADVERTISE_PAUSE BIT(MII_ADVERTISE_PAUSE_BIT)
```

```c
#include <zephyr/net/mii.h>
```

尝试协商暂停（Pause）。

<a id="ga35994af1965ff3f9aa68d203241f97d3"></a>

### `MII_ADVERTISE_PAUSE_BIT`

```c
#define MII_ADVERTISE_PAUSE_BIT 10
```

```c
#include <zephyr/net/mii.h>
```

暂停位位置（Pause Bit Position）。

<a id="ga3e1cfef9ac347b86324d25c1d00a07ef"></a>

### `MII_ADVERTISE_REMOTE_FAULT`

```c
#define MII_ADVERTISE_REMOTE_FAULT BIT(MII_ADVERTISE_REMOTE_FAULT_BIT)
```

```c
#include <zephyr/net/mii.h>
```

远端故障（Remote Fault）。

<a id="ga6bce3c2f70cddc50205a330158612f8c"></a>

### `MII_ADVERTISE_REMOTE_FAULT_BIT`

```c
#define MII_ADVERTISE_REMOTE_FAULT_BIT 13
```

```c
#include <zephyr/net/mii.h>
```

远端故障位位置（Remote Fault Bit Position）。

<a id="ga9abdfc8110120f54612c712d86cab3ac"></a>

### `MII_ADVERTISE_SEL_IEEE_802_3`

```c
#define MII_ADVERTISE_SEL_IEEE_802_3 0x01
```

```c
#include <zephyr/net/mii.h>
```

选择器字段（Selector Field）。

<a id="gac01baecf625bbb6d55a14ac0c2b181bd"></a>

### `MII_ADVERTISE_SEL_MASK`

```c
#define MII_ADVERTISE_SEL_MASK (0x1F << 0)
```

```c
#include <zephyr/net/mii.h>
```

选择器字段掩码（Selector Field Mask）。

<a id="gaacb2ab0ea5579b5d9e30b075991add1d"></a>

### `MII_ANAR`

```c
#define MII_ANAR 0x4
```

```c
#include <zephyr/net/mii.h>
```

自动协商通告寄存器（Auto-Negotiation Advertisement Register）。

<a id="ga6e5634d8831e21f963ddc16b91d5f6b9"></a>

### `MII_ANER`

```c
#define MII_ANER 0x6
```

```c
#include <zephyr/net/mii.h>
```

自动协商扩展寄存器（Auto-Negotiation Expansion Register）。

<a id="ga445e8381a9ea9724054bfacc10bb4c81"></a>

### `MII_ANLPAR`

```c
#define MII_ANLPAR 0x5
```

```c
#include <zephyr/net/mii.h>
```

自动协商链路伙伴能力寄存器（Auto-Negotiation Link Partner Ability Register）。

<a id="gaf17d80457d4a609d16793870d4a76bdf"></a>

### `MII_ANLPRNPR`

```c
#define MII_ANLPRNPR 0x8
```

```c
#include <zephyr/net/mii.h>
```

自动协商链路伙伴接收下一页寄存器（Auto-Negotiation Link Partner Received Next Page Register）。

<a id="ga3f3ed3ecfd22b34b840ff2473ca68490"></a>

### `MII_ANNPTR`

```c
#define MII_ANNPTR 0x7
```

```c
#include <zephyr/net/mii.h>
```

自动协商下一页发送寄存器（Auto-Negotiation Next Page Transmit Register）。

<a id="ga9137acedc42ff140f244da7473cff29e"></a>

### `MII_BMCR`

```c
#define MII_BMCR 0x0
```

```c
#include <zephyr/net/mii.h>
```

基本模式控制寄存器（Basic Mode Control Register）。

<a id="gaf58b450219ae18dfa2526c685a0402a7"></a>

### `MII_BMCR_AUTONEG_ENABLE`

```c
#define MII_BMCR_AUTONEG_ENABLE BIT(MII_BMCR_AUTONEG_ENABLE_BIT)
```

```c
#include <zephyr/net/mii.h>
```

启用自动协商（Auto-Negotiation Enable）。

<a id="ga780566e06059ce969cf2c7149cd28560"></a>

### `MII_BMCR_AUTONEG_ENABLE_BIT`

```c
#define MII_BMCR_AUTONEG_ENABLE_BIT 12
```

```c
#include <zephyr/net/mii.h>
```

自动协商使能位位置（Auto-Negotiation Enable Bit Position）。

<a id="ga110d6e1bfdbb37aa95cf1b32c54d8fa0"></a>

### `MII_BMCR_AUTONEG_RESTART`

```c
#define MII_BMCR_AUTONEG_RESTART BIT(MII_BMCR_AUTONEG_RESTART_BIT)
```

```c
#include <zephyr/net/mii.h>
```

重新启动自动协商（Auto-negotiation）。

<a id="gaca9844340da91e466e7303e9f5b0425f"></a>

### `MII_BMCR_AUTONEG_RESTART_BIT`

```c
#define MII_BMCR_AUTONEG_RESTART_BIT 9
```

```c
#include <zephyr/net/mii.h>
```

重新启动自动协商位位置（Restart Auto-Negotiation Bit Position）。

<a id="ga288bc52d6545ec634e6c2da04dbe86d3"></a>

### `MII_BMCR_DUPLEX_MODE`

```c
#define MII_BMCR_DUPLEX_MODE BIT(MII_BMCR_DUPLEX_MODE_BIT)
```

```c
#include <zephyr/net/mii.h>
```

全双工模式（Full Duplex Mode）。

<a id="ga728082a7fb53de09ed3259e14fe6a539"></a>

### `MII_BMCR_DUPLEX_MODE_BIT`

```c
#define MII_BMCR_DUPLEX_MODE_BIT 8
```

```c
#include <zephyr/net/mii.h>
```

双工模式位位置（Duplex Mode Bit Position）。

<a id="ga288b983fab32fb073cc42c3817b2c217"></a>

### `MII_BMCR_ISOLATE`

```c
#define MII_BMCR_ISOLATE BIT(MII_BMCR_ISOLATE_BIT)
```

```c
#include <zephyr/net/mii.h>
```

在电气上将 PHY 与介质独立接口（MII）隔离。

<a id="ga0c5b114330969ddfeb8a042b33561bb4"></a>

### `MII_BMCR_ISOLATE_BIT`

```c
#define MII_BMCR_ISOLATE_BIT 10
```

```c
#include <zephyr/net/mii.h>
```

隔离位位置（Isolate Bit Position）。

<a id="gaaade3d675167c736186a03dad857a7c9"></a>

### `MII_BMCR_LOOPBACK`

```c
#define MII_BMCR_LOOPBACK BIT(MII_BMCR_LOOPBACK_BIT)
```

```c
#include <zephyr/net/mii.h>
```

启用环回模式（Loopback Mode）。

<a id="ga6e79703869a5e6459a4cbf2c103b8ed1"></a>

### `MII_BMCR_LOOPBACK_BIT`

```c
#define MII_BMCR_LOOPBACK_BIT 14
```

```c
#include <zephyr/net/mii.h>
```

环回模式位位置（Loopback Mode Bit Position）。

<a id="ga2598b7655be14619dffc44b9a6db36b8"></a>

### `MII_BMCR_POWER_DOWN`

```c
#define MII_BMCR_POWER_DOWN BIT(MII_BMCR_POWER_DOWN_BIT)
```

```c
#include <zephyr/net/mii.h>
```

掉电模式（Power Down Mode）。

<a id="gafc726725b78ff3aed31a7ec30e168831"></a>

### `MII_BMCR_POWER_DOWN_BIT`

```c
#define MII_BMCR_POWER_DOWN_BIT 11
```

```c
#include <zephyr/net/mii.h>
```

掉电位位置（Power-down Bit Position）。

<a id="ga1001ac1540dc5bb6c4962f63b5fd6c3a"></a>

### `MII_BMCR_RESET`

```c
#define MII_BMCR_RESET BIT(MII_BMCR_RESET_BIT)
```

```c
#include <zephyr/net/mii.h>
```

PHY 复位（Reset）。

<a id="ga54df4d055d02d507cf52eb1a2811f1de"></a>

### `MII_BMCR_RESET_BIT`

```c
#define MII_BMCR_RESET_BIT 15
```

```c
#include <zephyr/net/mii.h>
```

PHY 复位位位置（Reset Bit Position）。

<a id="ga4d31aeaad35fe6a358aef1eef1c5b4cf"></a>

### `MII_BMCR_SPEED_10`

```c
#define MII_BMCR_SPEED_10 0
```

```c
#include <zephyr/net/mii.h>
```

选择 10 Mb/s 速率（Speed）。

<a id="gaf52c7fc2b468c142ae63605a201900d4"></a>

### `MII_BMCR_SPEED_100`

```c
#define MII_BMCR_SPEED_100 BIT(MII_BMCR_SPEED_LSB_BIT)
```

```c
#include <zephyr/net/mii.h>
```

选择 100 Mb/s 速率（Speed）。

<a id="gaae2f486072b95b3e829d0e1bd4b8d893"></a>

### `MII_BMCR_SPEED_1000`

```c
#define MII_BMCR_SPEED_1000 BIT(MII_BMCR_SPEED_MSB_BIT)
```

```c
#include <zephyr/net/mii.h>
```

选择 1000 Mb/s 速率（Speed）。

<a id="ga19ef6d51e7bc231892635d856dd6a747"></a>

### `MII_BMCR_SPEED_LSB`

```c
#define MII_BMCR_SPEED_LSB BIT(MII_BMCR_SPEED_LSB_BIT)
```

```c
#include <zephyr/net/mii.h>
```

速率编码（Speed Encoding）：10 = 1000 Mbps；01 = 100 Mbps；00 = 10 Mbps。

<a id="ga689b3d9154d01a6cd2ac12ca252d5dc6"></a>

### `MII_BMCR_SPEED_LSB_BIT`

```c
#define MII_BMCR_SPEED_LSB_BIT 13
```

```c
#include <zephyr/net/mii.h>
```

速率选择最低有效位位置（Speed Selection LSB Bit Position）。

<a id="gaf562ae173424ea0d41afd68d11f87115"></a>

### `MII_BMCR_SPEED_MASK`

```c
#define MII_BMCR_SPEED_MASK (MII_BMCR_SPEED_MSB | MII_BMCR_SPEED_LSB)
```

```c
#include <zephyr/net/mii.h>
```

链路速率字段（Link Speed Field）。

<a id="ga94e2ff6468b89371ec22a087ad5477d4"></a>

### `MII_BMCR_SPEED_MSB`

```c
#define MII_BMCR_SPEED_MSB BIT(MII_BMCR_SPEED_MSB_BIT)
```

```c
#include <zephyr/net/mii.h>
```

速率编码（Speed Encoding）：10 = 1000 Mbps；01 = 100 Mbps；00 = 10 Mbps。

<a id="gad75a0984bdbebe75921c6986a5122f30"></a>

### `MII_BMCR_SPEED_MSB_BIT`

```c
#define MII_BMCR_SPEED_MSB_BIT 6
```

```c
#include <zephyr/net/mii.h>
```

速率选择最高有效位位置（Speed Selection MSB Bit Position）。

<a id="gaa2f632686d6298a7c898b1c805586aab"></a>

### `MII_BMSR`

```c
#define MII_BMSR 0x1
```

```c
#include <zephyr/net/mii.h>
```

基本模式状态寄存器（Basic Mode Status Register）。

<a id="ga93fb7b79b3da2ae1757fe98237dd2d6b"></a>

### `MII_BMSR_100BASE_T2_FULL`

```c
#define MII_BMSR_100BASE_T2_FULL BIT(MII_BMSR_100BASE_T2_FULL_BIT)
```

```c
#include <zephyr/net/mii.h>
```

具有 100BASE-T2 全双工能力（Full Duplex Capable）。

<a id="ga37c6de155f12c3c2d3593040386e2590"></a>

### `MII_BMSR_100BASE_T2_FULL_BIT`

```c
#define MII_BMSR_100BASE_T2_FULL_BIT 10
```

```c
#include <zephyr/net/mii.h>
```

100BASE-T2 全双工能力位位置（Full Duplex Capable Bit Position）。

<a id="gafb0d83d336eda611d45580be48f15d02"></a>

### `MII_BMSR_100BASE_T2_HALF`

```c
#define MII_BMSR_100BASE_T2_HALF BIT(MII_BMSR_100BASE_T2_HALF_BIT)
```

```c
#include <zephyr/net/mii.h>
```

具有 100BASE-T2 半双工能力（Half Duplex Capable）。

<a id="gab0e7bf45469a11187ee00eed60f27408"></a>

### `MII_BMSR_100BASE_T2_HALF_BIT`

```c
#define MII_BMSR_100BASE_T2_HALF_BIT 9
```

```c
#include <zephyr/net/mii.h>
```

100BASE-T2 半双工能力位位置（Half Duplex Capable Bit Position）。

<a id="gac8a404aa082745cb7699739bf58fc530"></a>

### `MII_BMSR_100BASE_T4`

```c
#define MII_BMSR_100BASE_T4 BIT(MII_BMSR_100BASE_T4_BIT)
```

```c
#include <zephyr/net/mii.h>
```

具有 100BASE-T4 能力（Capable）。

<a id="ga6d815d61b5566b26fb0eb2cf78be689d"></a>

### `MII_BMSR_100BASE_T4_BIT`

```c
#define MII_BMSR_100BASE_T4_BIT 15
```

```c
#include <zephyr/net/mii.h>
```

100BASE-T4 能力位位置（Capable Bit Position）。

<a id="ga090c828a41acfc824b56ec2a9a57082a"></a>

### `MII_BMSR_100BASE_X_FULL`

```c
#define MII_BMSR_100BASE_X_FULL BIT(MII_BMSR_100BASE_X_FULL_BIT)
```

```c
#include <zephyr/net/mii.h>
```

具有 100BASE-X 全双工能力（Full Duplex Capable）。

<a id="ga85d42ee9a1dd81d27ba74ec4fff8e61a"></a>

### `MII_BMSR_100BASE_X_FULL_BIT`

```c
#define MII_BMSR_100BASE_X_FULL_BIT 14
```

```c
#include <zephyr/net/mii.h>
```

100BASE-X 全双工能力位位置（Full Duplex Capable Bit Position）。

<a id="ga608ec5361c44f25c34ae6138ae7ffef9"></a>

### `MII_BMSR_100BASE_X_HALF`

```c
#define MII_BMSR_100BASE_X_HALF BIT(MII_BMSR_100BASE_X_HALF_BIT)
```

```c
#include <zephyr/net/mii.h>
```

具有 100BASE-X 半双工能力（Half Duplex Capable）。

<a id="ga1502cf548fb5393b698fd1fcbe5d6a3b"></a>

### `MII_BMSR_100BASE_X_HALF_BIT`

```c
#define MII_BMSR_100BASE_X_HALF_BIT 13
```

```c
#include <zephyr/net/mii.h>
```

100BASE-X 半双工能力位位置（Half Duplex Capable Bit Position）。

<a id="ga4f085921a6b0f0586326b1bdc8f62b31"></a>

### `MII_BMSR_10_FULL`

```c
#define MII_BMSR_10_FULL BIT(MII_BMSR_10_FULL_BIT)
```

```c
#include <zephyr/net/mii.h>
```

具有 10 Mb/s 全双工能力（Full Duplex Capable）。

<a id="ga2aefc1cd403db957440b01e5df54a7fa"></a>

### `MII_BMSR_10_FULL_BIT`

```c
#define MII_BMSR_10_FULL_BIT 12
```

```c
#include <zephyr/net/mii.h>
```

10 Mb/s 全双工能力位位置（Full Duplex Capable Bit Position）。

<a id="ga8505886511fef3ec2d8630a957de4478"></a>

### `MII_BMSR_10_HALF`

```c
#define MII_BMSR_10_HALF BIT(MII_BMSR_10_HALF_BIT)
```

```c
#include <zephyr/net/mii.h>
```

具有 10 Mb/s 半双工能力（Half Duplex Capable）。

<a id="gab5cbdb762b820a7265fccdbeba80478a"></a>

### `MII_BMSR_10_HALF_BIT`

```c
#define MII_BMSR_10_HALF_BIT 11
```

```c
#include <zephyr/net/mii.h>
```

10 Mb/s 半双工能力位位置（Half Duplex Capable Bit Position）。

<a id="gafc344357c76d6a41c5fa432d55355fce"></a>

### `MII_BMSR_AUTONEG_ABILITY`

```c
#define MII_BMSR_AUTONEG_ABILITY BIT(MII_BMSR_AUTONEG_ABILITY_BIT)
```

```c
#include <zephyr/net/mii.h>
```

PHY 能够执行自动协商（Auto-Negotiation）。

<a id="ga0c456682a2aa1e678b753edc90dd7173"></a>

### `MII_BMSR_AUTONEG_ABILITY_BIT`

```c
#define MII_BMSR_AUTONEG_ABILITY_BIT 3
```

```c
#include <zephyr/net/mii.h>
```

自动协商能力位位置（Auto-Negotiation Ability Bit Position）。

<a id="gac5b9ac6b54ce146c91197660c2ccd207"></a>

### `MII_BMSR_AUTONEG_COMPLETE`

```c
#define MII_BMSR_AUTONEG_COMPLETE BIT(MII_BMSR_AUTONEG_COMPLETE_BIT)
```

```c
#include <zephyr/net/mii.h>
```

自动协商过程（Auto-negotiation Process）已完成。

<a id="ga110eb8cc56b72287f30da929838029e0"></a>

### `MII_BMSR_AUTONEG_COMPLETE_BIT`

```c
#define MII_BMSR_AUTONEG_COMPLETE_BIT 5
```

```c
#include <zephyr/net/mii.h>
```

自动协商完成位位置（Auto-Negotiation Complete Bit Position）。

<a id="gab225377deb09eb179b7efee199c7edd4"></a>

### `MII_BMSR_EXTEND_CAPAB`

```c
#define MII_BMSR_EXTEND_CAPAB BIT(MII_BMSR_EXTEND_CAPAB_BIT)
```

```c
#include <zephyr/net/mii.h>
```

扩展寄存器能力（Extended Register Capabilities）。

<a id="ga430bd15994b0ee73b0802f0a2760e67b"></a>

### `MII_BMSR_EXTEND_CAPAB_BIT`

```c
#define MII_BMSR_EXTEND_CAPAB_BIT 0
```

```c
#include <zephyr/net/mii.h>
```

扩展能力位位置（Extended Capability Bit Position）。

<a id="ga24992988cde973ce2a954fe372a5ad0e"></a>

### `MII_BMSR_EXTEND_STATUS`

```c
#define MII_BMSR_EXTEND_STATUS BIT(MII_BMSR_EXTEND_STATUS_BIT)
```

```c
#include <zephyr/net/mii.h>
```

寄存器 15 中的扩展状态信息（Extended Status Information）。

<a id="ga017891e6a6cb799e2795d27d482bacf1"></a>

### `MII_BMSR_EXTEND_STATUS_BIT`

```c
#define MII_BMSR_EXTEND_STATUS_BIT 8
```

```c
#include <zephyr/net/mii.h>
```

扩展状态信息位位置（Extended Status Information Bit Position）。

<a id="gad9ef4a2223dfee6826b0fdc8b25802ea"></a>

### `MII_BMSR_JABBER_DETECT`

```c
#define MII_BMSR_JABBER_DETECT BIT(MII_BMSR_JABBER_DETECT_BIT)
```

```c
#include <zephyr/net/mii.h>
```

检测到异常长发送状态（Jabber Condition）。

<a id="ga302ccc7731400f1552d870b6c60daf6b"></a>

### `MII_BMSR_JABBER_DETECT_BIT`

```c
#define MII_BMSR_JABBER_DETECT_BIT 1
```

```c
#include <zephyr/net/mii.h>
```

异常长发送检测位位置（Jabber Detect Bit Position）。

<a id="ga884d39c456206cee38ce5a9a9ca01599"></a>

### `MII_BMSR_LINK_STATUS`

```c
#define MII_BMSR_LINK_STATUS BIT(MII_BMSR_LINK_STATUS_BIT)
```

```c
#include <zephyr/net/mii.h>
```

链路已建立（Link Up）。

<a id="gace14dd35d99a13fea32169bba957cf64"></a>

### `MII_BMSR_LINK_STATUS_BIT`

```c
#define MII_BMSR_LINK_STATUS_BIT 2
```

```c
#include <zephyr/net/mii.h>
```

链路状态位位置（Link Status Bit Position）。

<a id="gae85e29e0f9a50898f93ff6e5a5f763e4"></a>

### `MII_BMSR_MF_PREAMB_SUPPR`

```c
#define MII_BMSR_MF_PREAMB_SUPPR BIT(MII_BMSR_MF_PREAMB_SUPPR_BIT)
```

```c
#include <zephyr/net/mii.h>
```

PHY 接受省略前导码（Preamble Suppressed）的管理帧（Management Frames）。

<a id="ga5fe389f8d8dbb6900ee8edcbae645ca7"></a>

### `MII_BMSR_MF_PREAMB_SUPPR_BIT`

```c
#define MII_BMSR_MF_PREAMB_SUPPR_BIT 6
```

```c
#include <zephyr/net/mii.h>
```

前导码抑制能力位位置（Preamble Suppression Capable Bit Position）。

<a id="ga0dd8421740c52ecd5e6a53e969d2e48a"></a>

### `MII_BMSR_REMOTE_FAULT`

```c
#define MII_BMSR_REMOTE_FAULT BIT(MII_BMSR_REMOTE_FAULT_BIT)
```

```c
#include <zephyr/net/mii.h>
```

检测到远端故障（Remote Fault）。

<a id="gaf8cd939b545f4d9cb8798169d1e1b718"></a>

### `MII_BMSR_REMOTE_FAULT_BIT`

```c
#define MII_BMSR_REMOTE_FAULT_BIT 4
```

```c
#include <zephyr/net/mii.h>
```

远端故障位位置（Remote Fault Bit Position）。

<a id="gaa705f43dba50029d5395379e1f2b802d"></a>

### `MII_ESTAT`

```c
#define MII_ESTAT 0xf
```

```c
#include <zephyr/net/mii.h>
```

扩展状态寄存器（Extended Status Register）。

<a id="gada0831dbbb86ff717b40c23c73345731"></a>

### `MII_ESTAT_1000BASE_T_FULL`

```c
#define MII_ESTAT_1000BASE_T_FULL BIT(13)
```

```c
#include <zephyr/net/mii.h>
```

具有 1000BASE-T 全双工能力（Full-duplex Capable）。

<a id="ga42e8d732fd9806e218599871fd1291d5"></a>

### `MII_ESTAT_1000BASE_T_HALF`

```c
#define MII_ESTAT_1000BASE_T_HALF BIT(12)
```

```c
#include <zephyr/net/mii.h>
```

具有 1000BASE-T 半双工能力（Half-duplex Capable）。

<a id="ga846525a526aa9704a175c84771e48290"></a>

### `MII_ESTAT_1000BASE_X_FULL`

```c
#define MII_ESTAT_1000BASE_X_FULL BIT(15)
```

```c
#include <zephyr/net/mii.h>
```

具有 1000BASE-X 全双工能力（Full-duplex Capable）。

<a id="gabec9696aa599caca1131f869827bbc95"></a>

### `MII_ESTAT_1000BASE_X_HALF`

```c
#define MII_ESTAT_1000BASE_X_HALF BIT(14)
```

```c
#include <zephyr/net/mii.h>
```

具有 1000BASE-X 半双工能力（Half-duplex Capable）。

<a id="ga378832f55be1a03977c829f09dd1d364"></a>

### `MII_MMD_AADR`

```c
#define MII_MMD_AADR 0xe
```

```c
#include <zephyr/net/mii.h>
```

MMD 访问地址数据寄存器（Access Address Data Register）。

<a id="ga7d6687385994aac21782308af560b224"></a>

### `MII_MMD_ACR`

```c
#define MII_MMD_ACR 0xd
```

```c
#include <zephyr/net/mii.h>
```

MMD 访问控制寄存器（Access Control Register）。

<a id="ga0f312eab9b4d51af4a72f7cb3898754a"></a>

### `MII_MMD_ACR_ADDR`

```c
#define MII_MMD_ACR_ADDR (0x00 << 14)
```

```c
#include <zephyr/net/mii.h>
```

地址（Address）。

<a id="ga6cac36daf5db44274cd60a05b77819f4"></a>

### `MII_MMD_ACR_DATA_NO_POS_INC`

```c
#define MII_MMD_ACR_DATA_NO_POS_INC (0x01 << 14)
```

```c
#include <zephyr/net/mii.h>
```

数据访问，不后递增（No Post Increment）。

<a id="ga3be4dced4eec405c42467ba51c5efb9c"></a>

### `MII_MMD_ACR_DATA_RW_POS_INC`

```c
#define MII_MMD_ACR_DATA_RW_POS_INC (0x10 << 14)
```

```c
#include <zephyr/net/mii.h>
```

数据访问，读写后均递增（Post Increment on Reads and Writes）。

<a id="ga48f56892c3e8d6ec7e90a7e36dd67309"></a>

### `MII_MMD_ACR_DATA_W_POS_INC`

```c
#define MII_MMD_ACR_DATA_W_POS_INC (0x11 << 14)
```

```c
#include <zephyr/net/mii.h>
```

数据访问，仅写后递增（Post Increment on Writes Only）。

<a id="gae4ac896c90a75cdc4869797708823673"></a>

### `MII_MMD_ACR_DEVAD_MASK`

```c
#define MII_MMD_ACR_DEVAD_MASK (0x1F << 0)
```

```c
#include <zephyr/net/mii.h>
```

设备地址掩码（DEVAD Mask）。

<a id="ga87196e916598cea91b6ce400ad0cc34a"></a>

### `MII_PHYID1R`

```c
#define MII_PHYID1R 0x2
```

```c
#include <zephyr/net/mii.h>
```

PHY 标识 1 寄存器（PHY ID 1 Register）。

<a id="ga40766cdb8f9c3ffee64720f0f0ea2f15"></a>

### `MII_PHYID2R`

```c
#define MII_PHYID2R 0x3
```

```c
#include <zephyr/net/mii.h>
```

PHY 标识 2 寄存器（PHY ID 2 Register）。


## 11.11\_原页交叉引用（Cross References）

- [mii.h](../api_file_bluetooth_media_reference/P008_zephyr__net__mii.h_文件参考.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__ethernet__mii_html_ga357539fe99d327cae0e76acd5059876f"></a>
<a id="agroup__ethernet__mii_html_ga44ee311ef785619a215de80fc0286a4c"></a>
<a id="agroup__ethernet__mii_html_ga72f632c88cf6c472b893c326d7a8d263"></a>
<a id="agroup__ethernet__mii_html_ga9abdfc8110120f54612c712d86cab3ac"></a>
<a id="agroup__ethernet__mii_html_gac5c508943ce4006fa2f934c25436fdb5"></a>

---

[上一章](P010_电池充电器（Battery Charger）.md) · [返回大纲](大纲.md) · [下一章](P012_电量计（Fuel Gauge）.md)
