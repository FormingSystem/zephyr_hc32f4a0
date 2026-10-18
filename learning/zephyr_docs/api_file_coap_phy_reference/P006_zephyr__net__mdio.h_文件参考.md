---
id: learning.zephyr-docs.api-file-coap-phy-reference.page-6
title: zephyr__net__mdio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net_2mdio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_net\_\_mdio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net_2mdio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.3管理接口（Management Interface）的定义。

查看此文件的源码。

<a id="details"></a>

IEEE 802.3管理接口（Management Interface）的定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_ga2aa490a7b68e2ad92d01440a240c118e"></a>

```c
#define MDIO_MMD_PMAPMD 0x01U
```

相关声明：[MDIO_MMD_PMAPMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga2aa490a7b68e2ad92d01440a240c118e)。

物理介质连接／物理介质相关（Physical Medium Attachment / Physical Medium Dependent，PMA／PMD）。

<a id="r_ga3e8b5218550de81211db3d78e16b5f7c"></a>

```c
#define MDIO_MMD_WIS 0x02U
```

相关声明：[MDIO_MMD_WIS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga3e8b5218550de81211db3d78e16b5f7c)。

广域网接口子层（WAN Interface Sublayer，WIS）。

<a id="r_gab071c192b965230e107b7111fa901c23"></a>

```c
#define MDIO_MMD_PCS 0x03U
```

相关声明：[MDIO_MMD_PCS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab071c192b965230e107b7111fa901c23)。

物理编码子层（Physical Coding Sublayer，PCS）。

<a id="r_ga7e34a58a18740b276e54095bae9b0421"></a>

```c
#define MDIO_MMD_PHYXS 0x04U
```

相关声明：[MDIO_MMD_PHYXS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga7e34a58a18740b276e54095bae9b0421)。

PHY 扩展子层（PHY Extender Sublayer）。

<a id="r_gaa8e0fb0cf10bc5584d34eed46d3d21ff"></a>

```c
#define MDIO_MMD_DTEXS 0x05U
```

相关声明：[MDIO_MMD_DTEXS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaa8e0fb0cf10bc5584d34eed46d3d21ff)。

数据终端设备扩展子层（DTE Extender Sublayer）。

<a id="r_gaf6a80fb3d3090cba631aad20026e23c1"></a>

```c
#define MDIO_MMD_TC 0x06U
```

相关声明：[MDIO_MMD_TC](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaf6a80fb3d3090cba631aad20026e23c1)。

传输汇聚（Transmission Convergence）。

<a id="r_ga47459e9e120969a7fc3a7ada2abdd440"></a>

```c
#define MDIO_MMD_AN 0x07U
```

相关声明：[MDIO_MMD_AN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga47459e9e120969a7fc3a7ada2abdd440)。

自动协商（Auto-negotiation）。

<a id="r_ga991d5fc38be73371ac3b0bae8a04f63d"></a>

```c
#define MDIO_MMD_SEPARATED_PMA1 0x08U
```

相关声明：[MDIO_MMD_SEPARATED_PMA1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga991d5fc38be73371ac3b0bae8a04f63d)。

分离的物理介质连接（Separated PMA）1。

<a id="r_gacde2c812689ada4b7006e1ab4262eaf2"></a>

```c
#define MDIO_MMD_SEPARATED_PMA2 0x09U
```

相关声明：[MDIO_MMD_SEPARATED_PMA2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gacde2c812689ada4b7006e1ab4262eaf2)。

分离的物理介质连接（Separated PMA）2。

<a id="r_gaee49981a836d3b2a2cf12b3e4bb703b5"></a>

```c
#define MDIO_MMD_SEPARATED_PMA3 0x0AU
```

相关声明：[MDIO_MMD_SEPARATED_PMA3](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaee49981a836d3b2a2cf12b3e4bb703b5)。

分离的物理介质连接（Separated PMA）3。

<a id="r_gac57c99dcb72884df7e538e2af1804244"></a>

```c
#define MDIO_MMD_SEPARATED_PMA4 0x0BU
```

相关声明：[MDIO_MMD_SEPARATED_PMA4](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gac57c99dcb72884df7e538e2af1804244)。

分离的物理介质连接（Separated PMA）4。

<a id="r_gab8a03ec360a743225345dd6bb64882f1"></a>

```c
#define MDIO_MMD_C22EXT 0x1DU
```

相关声明：[MDIO_MMD_C22EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab8a03ec360a743225345dd6bb64882f1)。

第 22 条款扩展（Clause 22 Extension）。

<a id="r_ga71e8d72d50c484557a2e39c622490956"></a>

```c
#define MDIO_MMD_VENDOR_SPECIFIC1 0x1EU
```

相关声明：[MDIO_MMD_VENDOR_SPECIFIC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga71e8d72d50c484557a2e39c622490956)。

厂商专用（Vendor Specific）1。

<a id="r_gaac45f28f75bcfeca861d06b99239cc77"></a>

```c
#define MDIO_MMD_VENDOR_SPECIFIC2 0x1FU
```

相关声明：[MDIO_MMD_VENDOR_SPECIFIC2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaac45f28f75bcfeca861d06b99239cc77)。

厂商专用（Vendor Specific）2。

<a id="r_gaab4d7fa609d78bb982f2e0baae2facc9"></a>

```c
#define MDIO_CTRL1 0x0000U
```

相关声明：[MDIO_CTRL1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaab4d7fa609d78bb982f2e0baae2facc9)。

控制（Control）1。

<a id="r_ga684cd28a49124170c327f279db8ba512"></a>

```c
#define MDIO_STAT1 0x0001U
```

相关声明：[MDIO_STAT1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga684cd28a49124170c327f279db8ba512)。

状态（Status）1。

<a id="r_ga8a63e5b18fa478566b230f22172e998f"></a>

```c
#define MDIO_DEVID1 0x0002U
```

相关声明：[MDIO_DEVID1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga8a63e5b18fa478566b230f22172e998f)。

设备标识符（Device Identifier）1。

<a id="r_gaafa088ec5cbe2a4b4023a2c8310b1ae1"></a>

```c
#define MDIO_DEVID2 0x0003U
```

相关声明：[MDIO_DEVID2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaafa088ec5cbe2a4b4023a2c8310b1ae1)。

设备标识符（Device Identifier）2。

<a id="r_ga75c8d4845abbcb0d0b283dcf24ea684a"></a>

```c
#define MDIO_SPEED 0x0004U
```

相关声明：[MDIO_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga75c8d4845abbcb0d0b283dcf24ea684a)。

速率能力（Speed Ability）。

<a id="r_ga210f57aa1971b2f77765fdc47a2b00f2"></a>

```c
#define MDIO_DEVS1 0x0005U
```

相关声明：[MDIO_DEVS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga210f57aa1971b2f77765fdc47a2b00f2)。

封装内设备（Devices in Package）1。

<a id="r_ga4d095f2392dd8d94ff014e510e164a16"></a>

```c
#define MDIO_DEVS2 0x0006U
```

相关声明：[MDIO_DEVS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga4d095f2392dd8d94ff014e510e164a16)。

封装内设备（Devices in Package）2。

<a id="r_ga3c3d4c2f16cfdd4f2a4f6781069b2395"></a>

```c
#define MDIO_CTRL2 0x0007U
```

相关声明：[MDIO_CTRL2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga3c3d4c2f16cfdd4f2a4f6781069b2395)。

控制（Control）2。

<a id="r_ga1cc7343ad758f8c070f6b28b568e2a00"></a>

```c
#define MDIO_STAT2 0x0008U
```

相关声明：[MDIO_STAT2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga1cc7343ad758f8c070f6b28b568e2a00)。

状态（Status）2。

<a id="r_gaead8a046d17d07f54cf5cae793cc7392"></a>

```c
#define MDIO_PKGID1 0x000EU
```

相关声明：[MDIO_PKGID1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaead8a046d17d07f54cf5cae793cc7392)。

封装标识符（Package Identifier）1。

<a id="r_gadd799e84b3cc7a31f57962fe29a1800f"></a>

```c
#define MDIO_PKGID2 0x000FU
```

相关声明：[MDIO_PKGID2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gadd799e84b3cc7a31f57962fe29a1800f)。

封装标识符（Package Identifier）2。

<a id="r_ga12b7f932606a306043434433c6c721ff"></a>

```c
#define MDIO_PCS_EEE_CAP 0x0014U
```

相关声明：[MDIO_PCS_EEE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga12b7f932606a306043434433c6c721ff)。

<a id="r_gabe093365122e043bbceb08f6c354dda2"></a>

```c
#define MDIO_AN_EEE_ADV 0x003CU
```

相关声明：[MDIO_AN_EEE_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabe093365122e043bbceb08f6c354dda2)。

<a id="r_ga52b4b4aac146d80fe6581f612878df09"></a>

```c
#define MDIO_AN_T1_CTRL 0x0200U
```

相关声明：[MDIO_AN_T1_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga52b4b4aac146d80fe6581f612878df09)。

BASE-T1 自动协商控制（Auto-negotiation Control）。

<a id="r_ga698a5175bfa98c727579e0be12204cff"></a>

```c
#define MDIO_AN_T1_STAT 0x0201U
```

相关声明：[MDIO_AN_T1_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga698a5175bfa98c727579e0be12204cff)。

BASE-T1 自动协商状态（Auto-negotiation Status）。

<a id="r_ga69e18d3aafb29972b8746b2ca5e67b3b"></a>

```c
#define MDIO_AN_T1_ADV_L 0x0202U
```

相关声明：[MDIO_AN_T1_ADV_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga69e18d3aafb29972b8746b2ca5e67b3b)。

BASE-T1 自动协商通告寄存器（Auto-negotiation Advertisement Register）[15:0]。

<a id="r_gad870783cb015fd3bf7e07a437b429ec6"></a>

```c
#define MDIO_AN_T1_ADV_M 0x0203U
```

相关声明：[MDIO_AN_T1_ADV_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gad870783cb015fd3bf7e07a437b429ec6)。

BASE-T1 自动协商通告寄存器（Auto-negotiation Advertisement Register）[31:16]。

<a id="r_ga85201e69432f1749c9f29f351565d8f2"></a>

```c
#define MDIO_AN_T1_ADV_H 0x0204U
```

相关声明：[MDIO_AN_T1_ADV_H](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga85201e69432f1749c9f29f351565d8f2)。

BASE-T1 自动协商通告寄存器（Auto-negotiation Advertisement Register）[47:32]。

<a id="r_ga380d4d00a27e889ec400bc11fed8c4a7"></a>

```c
#define MDIO_AN_T1_LP_ADV_L 0x0205U
```

相关声明：[MDIO_AN_T1_LP_ADV_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga380d4d00a27e889ec400bc11fed8c4a7)。

BASE-T1 自动协商链路伙伴能力寄存器（Auto-negotiation Link Partner Ability Register）[15:0]。

<a id="r_ga9be473383b78d977aaa3b0ed25a2bd81"></a>

```c
#define MDIO_AN_T1_LP_ADV_M 0x0206U
```

相关声明：[MDIO_AN_T1_LP_ADV_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga9be473383b78d977aaa3b0ed25a2bd81)。

BASE-T1 自动协商链路伙伴能力寄存器（Auto-negotiation Link Partner Ability Register）[31:16]。

<a id="r_gaabc4793b527e65c2d665b5bb0c1fe874"></a>

```c
#define MDIO_AN_T1_LP_ADV_H 0x0207U
```

相关声明：[MDIO_AN_T1_LP_ADV_H](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaabc4793b527e65c2d665b5bb0c1fe874)。

BASE-T1 自动协商链路伙伴能力寄存器（Auto-negotiation Link Partner Ability Register）[47:32]。

<a id="r_ga8a2295bc2f17aa0444e302ebadb34f6b"></a>

```c
#define MDIO_PMA_PMD_BT1_CTRL 0x0834U
```

相关声明：[MDIO_PMA_PMD_BT1_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga8a2295bc2f17aa0444e302ebadb34f6b)。

BASE-T1 物理介质连接／物理介质相关子层（PMA/PMD）控制寄存器。

<a id="r_gabef35b68eb8a6e27c90dc5c5ea2001aa"></a>

```c
#define MDIO_AN_T1_CTRL_RESTART BIT(9)
```

相关声明：[MDIO_AN_T1_CTRL_RESTART](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabef35b68eb8a6e27c90dc5c5ea2001aa)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

重新启动自动协商（Auto-negotiation Restart）。

<a id="r_gac186dd4bb083f29368b2af4750daece7"></a>

```c
#define MDIO_AN_T1_CTRL_EN BIT(12)
```

相关声明：[MDIO_AN_T1_CTRL_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gac186dd4bb083f29368b2af4750daece7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启用自动协商（Auto-negotiation Enable）。

<a id="r_gac1f927e0b3fbd99a1f4a85bada0f7a94"></a>

```c
#define MDIO_AN_T1_STAT_LINK_STATUS BIT(2)
```

相关声明：[MDIO_AN_T1_STAT_LINK_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gac1f927e0b3fbd99a1f4a85bada0f7a94)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

链路状态（Link Status）。

<a id="r_ga912f2bddd1b8573e6420152e43060bdc"></a>

```c
#define MDIO_AN_T1_STAT_ABLE BIT(3)
```

相关声明：[MDIO_AN_T1_STAT_ABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga912f2bddd1b8573e6420152e43060bdc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

自动协商能力（Auto-negotiation Ability）。

<a id="r_ga7acdb2f35803d1f3e8e5ce2e340a6e30"></a>

```c
#define MDIO_AN_T1_STAT_REMOTE_FAULT BIT(4)
```

相关声明：[MDIO_AN_T1_STAT_REMOTE_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga7acdb2f35803d1f3e8e5ce2e340a6e30)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

自动协商远端故障（Auto-negotiation Remote Fault）。

<a id="r_ga5f1496d45ba3404aabd05ae9f574ade7"></a>

```c
#define MDIO_AN_T1_STAT_COMPLETE BIT(5)
```

相关声明：[MDIO_AN_T1_STAT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga5f1496d45ba3404aabd05ae9f574ade7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

自动协商完成（Auto-negotiation Complete）。

<a id="r_ga638f63292ab5ddd4e301ddd9e4d70418"></a>

```c
#define MDIO_AN_T1_STAT_PAGE_RX BIT(6)
```

相关声明：[MDIO_AN_T1_STAT_PAGE_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga638f63292ab5ddd4e301ddd9e4d70418)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

已接收页面（Page Received）。

<a id="r_ga404345912bcad2c6691483910928f85a"></a>

```c
#define MDIO_AN_T1_ADV_L_PAUSE_CAP BIT(10)
```

相关声明：[MDIO_AN_T1_ADV_L_PAUSE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga404345912bcad2c6691483910928f85a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

暂停能力（Pause Ability）。

<a id="r_gae19eabc9238eae96ef8055f37fb0882e"></a>

```c
#define MDIO_AN_T1_ADV_L_PAUSE_ASYM BIT(11)
```

相关声明：[MDIO_AN_T1_ADV_L_PAUSE_ASYM](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gae19eabc9238eae96ef8055f37fb0882e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

暂停能力（Pause Ability）。

<a id="r_gaa227d9a74c324e64935e77811e7c2dcc"></a>

```c
#define MDIO_AN_T1_ADV_L_FORCE_MS BIT(12)
```

相关声明：[MDIO_AN_T1_ADV_L_FORCE_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaa227d9a74c324e64935e77811e7c2dcc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

强制主／从配置（Force Master/Slave Configuration）。

<a id="r_gabc9d0dfa5a8e534f0b3c33a94ed0dd03"></a>

```c
#define MDIO_AN_T1_ADV_L_REMOTE_FAULT BIT(13)
```

相关声明：[MDIO_AN_T1_ADV_L_REMOTE_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabc9d0dfa5a8e534f0b3c33a94ed0dd03)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

远端故障（Remote Fault）。

<a id="r_gaf6f17971533580a89bde8c52bc110363"></a>

```c
#define MDIO_AN_T1_ADV_L_ACK BIT(14)
```

相关声明：[MDIO_AN_T1_ADV_L_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaf6f17971533580a89bde8c52bc110363)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

确认（Acknowledge，ACK）。

<a id="r_gab69a2d9ebd289f792aba878bc831079a"></a>

```c
#define MDIO_AN_T1_ADV_L_NEXT_PAGE_REQ BIT(15)
```

相关声明：[MDIO_AN_T1_ADV_L_NEXT_PAGE_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab69a2d9ebd289f792aba878bc831079a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

下一页请求（Next Page Request）。

<a id="r_ga32e41aa9618bc858f9ca70fabef9bf37"></a>

```c
#define MDIO_AN_T1_ADV_M_B10L BIT(14)
```

相关声明：[MDIO_AN_T1_ADV_M_B10L](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga32e41aa9618bc858f9ca70fabef9bf37)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 能力（Ability）。

<a id="r_ga2ada131bfc4e87d3c8993ce3d0ca2d48"></a>

```c
#define MDIO_AN_T1_ADV_M_MST BIT(4)
```

相关声明：[MDIO_AN_T1_ADV_M_MST](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga2ada131bfc4e87d3c8993ce3d0ca2d48)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

主／从配置（Master/Slave Configuration）。

<a id="r_ga534444217d2388e5d752d60a03ca68b0"></a>

```c
#define MDIO_AN_T1_ADV_H_10L_TX_HI_REQ BIT(12)
```

相关声明：[MDIO_AN_T1_ADV_H_10L_TX_HI_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga534444217d2388e5d752d60a03ca68b0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 高电平发送工作模式请求（High Level Transmit Operating Mode Request）。

<a id="r_ga581d91721dd6f1aab1462c63df48d50a"></a>

```c
#define MDIO_AN_T1_ADV_H_10L_TX_HI BIT(13)
```

相关声明：[MDIO_AN_T1_ADV_H_10L_TX_HI](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga581d91721dd6f1aab1462c63df48d50a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 高电平发送工作模式能力（High Level Transmit Operating Mode Ability）。

<a id="r_gaa32e3e61e0cca8590fe4747258c4e768"></a>

```c
#define MDIO_AN_T1_ADV_H_10L_EEE BIT(14)
```

相关声明：[MDIO_AN_T1_ADV_H_10L_EEE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaa32e3e61e0cca8590fe4747258c4e768)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 节能以太网能力（Energy Efficient Ethernet Ability，EEE）。

<a id="r_ga11863eaaeb876c1d3dc83d1ee9e045d2"></a>

```c
#define MDIO_PMA_PMD_BT1_CTRL_CFG_MST BIT(14)
```

相关声明：[MDIO_PMA_PMD_BT1_CTRL_CFG_MST](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga11863eaaeb876c1d3dc83d1ee9e045d2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

BASE-T1 主／从配置（Master/Slave Configuration）。

<a id="r_ga490f3bb0e91ddbe9783864040d2054a8"></a>

```c
#define MDIO_PMA_B10L_CTRL 0x08F6U
```

相关声明：[MDIO_PMA_B10L_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga490f3bb0e91ddbe9783864040d2054a8)。

10BASE-T1L 物理介质连接控制（PMA Control）。

<a id="r_ga17955956be0807edf50f24f3d6b1a175"></a>

```c
#define MDIO_PMA_B10L_STAT 0x08F7U
```

相关声明：[MDIO_PMA_B10L_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga17955956be0807edf50f24f3d6b1a175)。

10BASE-T1L 物理介质连接状态（PMA Status）。

<a id="r_ga7977551cdf9b2933ffd8978533f46880"></a>

```c
#define MDIO_PMA_B10L_TEST_CTRL 0x08F8U
```

相关声明：[MDIO_PMA_B10L_TEST_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga7977551cdf9b2933ffd8978533f46880)。

10BASE-T1L 测试模式控制（Test Mode Control）。

<a id="r_gad55902f2a79193162459a6b90d508a41"></a>

```c
#define MDIO_PMA_B10L_LINK_STAT 0x8302U
```

相关声明：[MDIO_PMA_B10L_LINK_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gad55902f2a79193162459a6b90d508a41)。

10BASE-T1L PMA 链路状态（link status）。

<a id="r_gaafbb9fbd657bf59ee11a1c832ff4d4a0"></a>

```c
#define MDIO_PCS_B10L_CTRL 0x08E6U
```

相关声明：[MDIO_PCS_B10L_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaafbb9fbd657bf59ee11a1c832ff4d4a0)。

10BASE-T1L 物理编码子层（PCS）控制。

<a id="r_ga66181040f5b5d5301203914700d02dd7"></a>

```c
#define MDIO_PCS_B10L_STAT 0x08E7U
```

相关声明：[MDIO_PCS_B10L_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga66181040f5b5d5301203914700d02dd7)。

10BASE-T1L PCS 状态。

<a id="r_ga0d68932ddfa3b8194b6b085def230aa4"></a>

```c
#define MDIO_PMA_B10L_CTRL_TX_DIS_MODE_EN BIT(14)
```

相关声明：[MDIO_PMA_B10L_CTRL_TX_DIS_MODE_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga0d68932ddfa3b8194b6b085def230aa4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 发送禁用模式（Transmit Disable Mode）。

<a id="r_gae27e01f297d07281f2210f82ce1c41cb"></a>

```c
#define MDIO_PMA_B10L_CTRL_TX_LVL_HI BIT(12)
```

相关声明：[MDIO_PMA_B10L_CTRL_TX_LVL_HI](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gae27e01f297d07281f2210f82ce1c41cb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 发送电压幅度控制（Transmit Voltage Amplitude Control）。

<a id="r_ga1d8b5fa13bc9b3e685f5123614ceeac0"></a>

```c
#define MDIO_PMA_B10L_CTRL_EEE BIT(10)
```

相关声明：[MDIO_PMA_B10L_CTRL_EEE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga1d8b5fa13bc9b3e685f5123614ceeac0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启用 10BASE-T1L 节能以太网（EEE Enable）。

<a id="r_gaf5e632085ce3efb8fbbd33ca166e577d"></a>

```c
#define MDIO_PMA_B10L_CTRL_LB_PMA_LOC_EN BIT(0)
```

相关声明：[MDIO_PMA_B10L_CTRL_LB_PMA_LOC_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaf5e632085ce3efb8fbbd33ca166e577d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 物理介质连接环回（PMA Loopback）。

<a id="r_gaa3e658df0baa6377224b1580a7d2bd1c"></a>

```c
#define MDIO_PMA_B10L_STAT_LINK BIT(0)
```

相关声明：[MDIO_PMA_B10L_STAT_LINK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaa3e658df0baa6377224b1580a7d2bd1c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L PMA 接收链路建立（Receive Link Up）。

<a id="r_ga8a3919a982c3d7b038b4774aefec0289"></a>

```c
#define MDIO_PMA_B10L_STAT_FAULT BIT(1)
```

相关声明：[MDIO_PMA_B10L_STAT_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga8a3919a982c3d7b038b4774aefec0289)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 检测到故障条件（Fault Condition）。

<a id="r_gafad692e7e73ca3ba3ee267915745aa5b"></a>

```c
#define MDIO_PMA_B10L_STAT_POLARITY BIT(2)
```

相关声明：[MDIO_PMA_B10L_STAT_POLARITY](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gafad692e7e73ca3ba3ee267915745aa5b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 接收极性反转（Receive Polarity Reversed）。

<a id="r_ga1017896c84e1a32568f695bc84834894"></a>

```c
#define MDIO_PMA_B10L_STAT_RECV_FAULT BIT(9)
```

相关声明：[MDIO_PMA_B10L_STAT_RECV_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga1017896c84e1a32568f695bc84834894)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 能够检测接收路径故障（Receive Path Fault）。

<a id="r_ga54bec9909ebcc69b84da93a6e7bdbba6"></a>

```c
#define MDIO_PMA_B10L_STAT_EEE BIT(10)
```

相关声明：[MDIO_PMA_B10L_STAT_EEE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga54bec9909ebcc69b84da93a6e7bdbba6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L PHY 具有节能以太网能力（EEE Ability）。

<a id="r_ga6f4c3046c404635897a188ccf6c364a5"></a>

```c
#define MDIO_PMA_B10L_STAT_LOW_POWER BIT(11)
```

相关声明：[MDIO_PMA_B10L_STAT_LOW_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga6f4c3046c404635897a188ccf6c364a5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L PMA 具有低功耗能力（Low-power Ability）。

<a id="r_gab289ba626543006aebe04da57b53b050"></a>

```c
#define MDIO_PMA_B10L_STAT_2V4_ABLE BIT(12)
```

相关声明：[MDIO_PMA_B10L_STAT_2V4_ABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab289ba626543006aebe04da57b53b050)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L PHY 具有 2.4 Vpp 工作模式能力（Operating Mode Ability）。

<a id="r_gade5d7df4d74c0bcc3c6260d49d6d51a1"></a>

```c
#define MDIO_PMA_B10L_STAT_LB_ABLE BIT(13)
```

相关声明：[MDIO_PMA_B10L_STAT_LB_ABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gade5d7df4d74c0bcc3c6260d49d6d51a1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L PHY 具有环回能力（Loopback Ability）。

<a id="r_gabc67200086817a137be1a09ba9d6dbd0"></a>

```c
#define MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_MASK GENMASK(15, 13)
```

相关声明：[MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabc67200086817a137be1a09ba9d6dbd0)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

10BASE-T1L 测试模式字段（Test Mode Field）。

<a id="r_gaf0562da9e89a3665245e85a792e9d76d"></a>

```c
#define MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_1 BIT(13)
```

相关声明：[MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaf0562da9e89a3665245e85a792e9d76d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

选择 10BASE-T1L 测试模式（Test Mode）1。

<a id="r_gada32553d20a2242bfb556f0b6f6f18b6"></a>

```c
#define MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_2 BIT(14)
```

相关声明：[MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gada32553d20a2242bfb556f0b6f6f18b6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

选择 10BASE-T1L 测试模式（Test Mode）2。

<a id="r_ga4b446dc8278325bbc396f253b33ea887"></a>

```c
#define MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_3 (BIT(13) | BIT(14))
```

相关声明：[MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga4b446dc8278325bbc396f253b33ea887)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

选择 10BASE-T1L 测试模式（Test Mode）3。

<a id="r_gaff70ac51be8f32a0cbcb5046f92a727f"></a>

```c
#define MDIO_PMA_B10L_LINK_STAT_REM_RCVR_STAT_OK_LL BIT(9)
```

相关声明：[MDIO_PMA_B10L_LINK_STAT_REM_RCVR_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaff70ac51be8f32a0cbcb5046f92a727f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 远端接收器状态正常，低电平锁存（Remote Receiver Status OK Latch Low）。

<a id="r_gac03f000f6beef4a1debadaaca339b601"></a>

```c
#define MDIO_PMA_B10L_LINK_STAT_REM_RCVR_STAT_OK BIT(8)
```

相关声明：[MDIO_PMA_B10L_LINK_STAT_REM_RCVR_STAT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gac03f000f6beef4a1debadaaca339b601)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 远端接收器状态正常（Remote Receiver Status OK）。

<a id="r_ga51784a68c7a237a32d846723c01ec873"></a>

```c
#define MDIO_PMA_B10L_LINK_STAT_LOC_RCVR_STAT_OK_LL BIT(7)
```

相关声明：[MDIO_PMA_B10L_LINK_STAT_LOC_RCVR_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga51784a68c7a237a32d846723c01ec873)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 本地接收器状态正常（Local Receiver Status OK）。

<a id="r_ga08ca50389a30a21148525c7d9b212b6f"></a>

```c
#define MDIO_PMA_B10L_LINK_STAT_LOC_RCVR_STAT_OK BIT(6)
```

相关声明：[MDIO_PMA_B10L_LINK_STAT_LOC_RCVR_STAT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga08ca50389a30a21148525c7d9b212b6f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 本地接收器状态正常（Local Receiver Status OK）。

<a id="r_ga9b6a1e683e1cc964bc41cefbc2f9d91b"></a>

```c
#define MDIO_PMA_B10L_LINK_STAT_DSCR_STAT_OK_LL BIT(5)
```

相关声明：[MDIO_PMA_B10L_LINK_STAT_DSCR_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga9b6a1e683e1cc964bc41cefbc2f9d91b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 解扰器状态正常，低电平锁存（Descrambler Status OK Latch Low）。

<a id="r_gabdd013ea8c586918c54c258a6f1ae2eb"></a>

```c
#define MDIO_PMA_B10L_LINK_STAT_DSCR_STAT_OK BIT(4)
```

相关声明：[MDIO_PMA_B10L_LINK_STAT_DSCR_STAT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabdd013ea8c586918c54c258a6f1ae2eb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 解扰器状态正常（Descrambler Status OK）。

<a id="r_ga987f6dabf90e98985d0d11b7392701fc"></a>

```c
#define MDIO_PMA_B10L_LINK_STAT_LINK_STAT_OK_LL BIT(1)
```

相关声明：[MDIO_PMA_B10L_LINK_STAT_LINK_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga987f6dabf90e98985d0d11b7392701fc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 链路状态正常，低电平锁存（Link Status OK Latch Low）。

<a id="r_gab7d5ca01e536e68d9f9b90b7f24d0bf5"></a>

```c
#define MDIO_PMA_B10L_LINK_STAT_LINK_STAT_OK BIT(0)
```

相关声明：[MDIO_PMA_B10L_LINK_STAT_LINK_STAT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab7d5ca01e536e68d9f9b90b7f24d0bf5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L 链路状态正常（Link Status OK）。

<a id="r_ga6d2c4c50608d24fb8106841ca9a79714"></a>

```c
#define MDIO_PCS_B10L_CTRL_LB_PCS_EN BIT(14)
```

相关声明：[MDIO_PCS_B10L_CTRL_LB_PCS_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga6d2c4c50608d24fb8106841ca9a79714)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启用 10BASE-T1L PCS 环回（Loopback Enable）。

<a id="r_gab6abfd0df706b72684124db458491d9b"></a>

```c
#define MDIO_PCS_B10L_STAT_DSCR_STAT_OK_LL BIT(2)
```

相关声明：[MDIO_PCS_B10L_STAT_DSCR_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab6abfd0df706b72684124db458491d9b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

10BASE-T1L PCS 解扰器状态（Descrambler Status）。

<a id="r_ga535402b2cc3207645ed5485b762cd52f"></a>

```c
#define MDIO_AN_EEE_ADV_1000T BIT(2)
```

相关声明：[MDIO_AN_EEE_ADV_1000T](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga535402b2cc3207645ed5485b762cd52f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通告 1000T 能力（Advertise 1000T Capability）。

<a id="r_ga13b78fc17dcf75c515b58bf3571608ce"></a>

```c
#define MDIO_AN_EEE_ADV_100TX BIT(1)
```

相关声明：[MDIO_AN_EEE_ADV_100TX](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga13b78fc17dcf75c515b58bf3571608ce)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通告 100TX 能力（Advertise 100TX Capability）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.2\_枚举（Enumerations）

<a id="r_ga304f668820ee91a63512c174e405b492"></a>

```c
enum mdio_opcode { MDIO_OP_C22_WRITE = 1 , MDIO_OP_C22_READ = 2 , MDIO_OP_C45_ADDRESS = 0 , MDIO_OP_C45_WRITE = 1 , MDIO_OP_C45_READ_INC = 2 , MDIO_OP_C45_READ = 3 }
```

相关声明：[mdio_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga304f668820ee91a63512c174e405b492)、[MDIO_OP_C22_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a1792985f314fb97951befbd6bef29e6d)、[MDIO_OP_C22_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a1990de139b54d7e17f57245ad254db46)、[MDIO_OP_C45_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492ad6ad469f50d382878c1d1b57c2a6a371)、[MDIO_OP_C45_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492af969ce4b1ebc4dd291edc4c14f6c551f)、[MDIO_OP_C45_READ_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a2b901e2c23d60d424ec9c9d2610483dd)、[MDIO_OP_C45_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a0335bfebfd1557bc33cac6daedbf11b1)。

MDIO 事务操作码（Transaction Operation Code）。


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_register_time_reference/P006_mdio.h_源码浏览.md)
- [MDIO_MMD_PMAPMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga2aa490a7b68e2ad92d01440a240c118e)
- [MDIO_MMD_WIS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga3e8b5218550de81211db3d78e16b5f7c)
- [MDIO_MMD_PCS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab071c192b965230e107b7111fa901c23)
- [MDIO_MMD_PHYXS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga7e34a58a18740b276e54095bae9b0421)
- [MDIO_MMD_DTEXS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaa8e0fb0cf10bc5584d34eed46d3d21ff)
- [MDIO_MMD_TC](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaf6a80fb3d3090cba631aad20026e23c1)
- [MDIO_MMD_AN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga47459e9e120969a7fc3a7ada2abdd440)
- [MDIO_MMD_SEPARATED_PMA1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga991d5fc38be73371ac3b0bae8a04f63d)
- [MDIO_MMD_SEPARATED_PMA2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gacde2c812689ada4b7006e1ab4262eaf2)
- [MDIO_MMD_SEPARATED_PMA3](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaee49981a836d3b2a2cf12b3e4bb703b5)
- [MDIO_MMD_SEPARATED_PMA4](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gac57c99dcb72884df7e538e2af1804244)
- [MDIO_MMD_C22EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab8a03ec360a743225345dd6bb64882f1)
- [MDIO_MMD_VENDOR_SPECIFIC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga71e8d72d50c484557a2e39c622490956)
- [MDIO_MMD_VENDOR_SPECIFIC2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaac45f28f75bcfeca861d06b99239cc77)
- [MDIO_CTRL1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaab4d7fa609d78bb982f2e0baae2facc9)
- [MDIO_STAT1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga684cd28a49124170c327f279db8ba512)
- [MDIO_DEVID1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga8a63e5b18fa478566b230f22172e998f)
- [MDIO_DEVID2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaafa088ec5cbe2a4b4023a2c8310b1ae1)
- [MDIO_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga75c8d4845abbcb0d0b283dcf24ea684a)
- [MDIO_DEVS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga210f57aa1971b2f77765fdc47a2b00f2)
- [MDIO_DEVS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga4d095f2392dd8d94ff014e510e164a16)
- [MDIO_CTRL2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga3c3d4c2f16cfdd4f2a4f6781069b2395)
- [MDIO_STAT2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga1cc7343ad758f8c070f6b28b568e2a00)
- [MDIO_PKGID1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaead8a046d17d07f54cf5cae793cc7392)
- [MDIO_PKGID2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gadd799e84b3cc7a31f57962fe29a1800f)
- [MDIO_PCS_EEE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga12b7f932606a306043434433c6c721ff)
- [MDIO_AN_EEE_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabe093365122e043bbceb08f6c354dda2)
- [MDIO_AN_T1_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga52b4b4aac146d80fe6581f612878df09)
- [MDIO_AN_T1_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga698a5175bfa98c727579e0be12204cff)
- [MDIO_AN_T1_ADV_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga69e18d3aafb29972b8746b2ca5e67b3b)
- [MDIO_AN_T1_ADV_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gad870783cb015fd3bf7e07a437b429ec6)
- [MDIO_AN_T1_ADV_H](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga85201e69432f1749c9f29f351565d8f2)
- [MDIO_AN_T1_LP_ADV_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga380d4d00a27e889ec400bc11fed8c4a7)
- [MDIO_AN_T1_LP_ADV_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga9be473383b78d977aaa3b0ed25a2bd81)
- [MDIO_AN_T1_LP_ADV_H](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaabc4793b527e65c2d665b5bb0c1fe874)
- [MDIO_PMA_PMD_BT1_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga8a2295bc2f17aa0444e302ebadb34f6b)
- [MDIO_AN_T1_CTRL_RESTART](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabef35b68eb8a6e27c90dc5c5ea2001aa)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MDIO_AN_T1_CTRL_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gac186dd4bb083f29368b2af4750daece7)
- [MDIO_AN_T1_STAT_LINK_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gac1f927e0b3fbd99a1f4a85bada0f7a94)
- [MDIO_AN_T1_STAT_ABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga912f2bddd1b8573e6420152e43060bdc)
- [MDIO_AN_T1_STAT_REMOTE_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga7acdb2f35803d1f3e8e5ce2e340a6e30)
- [MDIO_AN_T1_STAT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga5f1496d45ba3404aabd05ae9f574ade7)
- [MDIO_AN_T1_STAT_PAGE_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga638f63292ab5ddd4e301ddd9e4d70418)
- [MDIO_AN_T1_ADV_L_PAUSE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga404345912bcad2c6691483910928f85a)
- [MDIO_AN_T1_ADV_L_PAUSE_ASYM](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gae19eabc9238eae96ef8055f37fb0882e)
- [MDIO_AN_T1_ADV_L_FORCE_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaa227d9a74c324e64935e77811e7c2dcc)
- [MDIO_AN_T1_ADV_L_REMOTE_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabc9d0dfa5a8e534f0b3c33a94ed0dd03)
- [MDIO_AN_T1_ADV_L_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaf6f17971533580a89bde8c52bc110363)
- [MDIO_AN_T1_ADV_L_NEXT_PAGE_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab69a2d9ebd289f792aba878bc831079a)
- [MDIO_AN_T1_ADV_M_B10L](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga32e41aa9618bc858f9ca70fabef9bf37)
- [MDIO_AN_T1_ADV_M_MST](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga2ada131bfc4e87d3c8993ce3d0ca2d48)
- [MDIO_AN_T1_ADV_H_10L_TX_HI_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga534444217d2388e5d752d60a03ca68b0)
- [MDIO_AN_T1_ADV_H_10L_TX_HI](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga581d91721dd6f1aab1462c63df48d50a)
- [MDIO_AN_T1_ADV_H_10L_EEE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaa32e3e61e0cca8590fe4747258c4e768)
- [MDIO_PMA_PMD_BT1_CTRL_CFG_MST](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga11863eaaeb876c1d3dc83d1ee9e045d2)
- [MDIO_PMA_B10L_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga490f3bb0e91ddbe9783864040d2054a8)
- [MDIO_PMA_B10L_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga17955956be0807edf50f24f3d6b1a175)
- [MDIO_PMA_B10L_TEST_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga7977551cdf9b2933ffd8978533f46880)
- [MDIO_PMA_B10L_LINK_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gad55902f2a79193162459a6b90d508a41)
- [MDIO_PCS_B10L_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaafbb9fbd657bf59ee11a1c832ff4d4a0)
- [MDIO_PCS_B10L_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga66181040f5b5d5301203914700d02dd7)
- [MDIO_PMA_B10L_CTRL_TX_DIS_MODE_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga0d68932ddfa3b8194b6b085def230aa4)
- [MDIO_PMA_B10L_CTRL_TX_LVL_HI](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gae27e01f297d07281f2210f82ce1c41cb)
- [MDIO_PMA_B10L_CTRL_EEE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga1d8b5fa13bc9b3e685f5123614ceeac0)
- [MDIO_PMA_B10L_CTRL_LB_PMA_LOC_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaf5e632085ce3efb8fbbd33ca166e577d)
- [MDIO_PMA_B10L_STAT_LINK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaa3e658df0baa6377224b1580a7d2bd1c)
- [MDIO_PMA_B10L_STAT_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga8a3919a982c3d7b038b4774aefec0289)
- [MDIO_PMA_B10L_STAT_POLARITY](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gafad692e7e73ca3ba3ee267915745aa5b)
- [MDIO_PMA_B10L_STAT_RECV_FAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga1017896c84e1a32568f695bc84834894)
- [MDIO_PMA_B10L_STAT_EEE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga54bec9909ebcc69b84da93a6e7bdbba6)
- [MDIO_PMA_B10L_STAT_LOW_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga6f4c3046c404635897a188ccf6c364a5)
- [MDIO_PMA_B10L_STAT_2V4_ABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab289ba626543006aebe04da57b53b050)
- [MDIO_PMA_B10L_STAT_LB_ABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gade5d7df4d74c0bcc3c6260d49d6d51a1)
- [MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabc67200086817a137be1a09ba9d6dbd0)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaf0562da9e89a3665245e85a792e9d76d)
- [MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gada32553d20a2242bfb556f0b6f6f18b6)
- [MDIO_PMA_B10L_TEST_CTRL_TEST_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga4b446dc8278325bbc396f253b33ea887)
- [MDIO_PMA_B10L_LINK_STAT_REM_RCVR_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gaff70ac51be8f32a0cbcb5046f92a727f)
- [MDIO_PMA_B10L_LINK_STAT_REM_RCVR_STAT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gac03f000f6beef4a1debadaaca339b601)
- [MDIO_PMA_B10L_LINK_STAT_LOC_RCVR_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga51784a68c7a237a32d846723c01ec873)
- [MDIO_PMA_B10L_LINK_STAT_LOC_RCVR_STAT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga08ca50389a30a21148525c7d9b212b6f)
- [MDIO_PMA_B10L_LINK_STAT_DSCR_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga9b6a1e683e1cc964bc41cefbc2f9d91b)
- [MDIO_PMA_B10L_LINK_STAT_DSCR_STAT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gabdd013ea8c586918c54c258a6f1ae2eb)
- [MDIO_PMA_B10L_LINK_STAT_LINK_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga987f6dabf90e98985d0d11b7392701fc)
- [MDIO_PMA_B10L_LINK_STAT_LINK_STAT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab7d5ca01e536e68d9f9b90b7f24d0bf5)
- [MDIO_PCS_B10L_CTRL_LB_PCS_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga6d2c4c50608d24fb8106841ca9a79714)
- [MDIO_PCS_B10L_STAT_DSCR_STAT_OK_LL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gab6abfd0df706b72684124db458491d9b)
- [MDIO_AN_EEE_ADV_1000T](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga535402b2cc3207645ed5485b762cd52f)
- [MDIO_AN_EEE_ADV_100TX](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga13b78fc17dcf75c515b58bf3571608ce)
- [mdio_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#ga304f668820ee91a63512c174e405b492)
- [MDIO_OP_C22_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a1792985f314fb97951befbd6bef29e6d)
- [MDIO_OP_C22_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a1990de139b54d7e17f57245ad254db46)
- [MDIO_OP_C45_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492ad6ad469f50d382878c1d1b57c2a6a371)
- [MDIO_OP_C45_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492af969ce4b1ebc4dd291edc4c14f6c551f)
- [MDIO_OP_C45_READ_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a2b901e2c23d60d424ec9c9d2610483dd)
- [MDIO_OP_C45_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mdio.html#gga304f668820ee91a63512c174e405b492a0335bfebfd1557bc33cac6daedbf11b1)

<a id="header-details"></a>

---

[上一章](P005_zephyr__dt-bindings__mfd__infineon-hppass.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__net_buf.h_文件参考.md)
