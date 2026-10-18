---
id: learning.zephyr-docs.api-file-input-wake-protocol-reference.page-6
title: zephyr__usb_c__tcpci.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tcpci_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_usb\_c\_\_tcpci.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tcpci_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Type-C端口控制器接口（Port Controller Interface）的寄存器与字段定义。

查看此文件的源码。

<a id="details"></a>

Type-C 端口控制器接口（Type-C Port Controller Interface，TCPCI）的寄存器与字段定义。本文件包含寄存器地址、字段及掩码，用于从寄存器值提取指定数据，可供所有符合 TCPCI 规范的 TCPC 驱动使用。这些寄存器与字段符合《Type-C 端口控制器接口规范》Revision 2.0、Version 1.3。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_ac81b442c1da80aa411d06f4829149edb"></a>

```c
#define TCPC_REG_VENDOR_ID 0x0
```

相关声明：[TCPC_REG_VENDOR_ID](#ac81b442c1da80aa411d06f4829149edb)。

寄存器地址（Register Address）：厂商 ID（Vendor ID）。

<a id="r_a298d4f136a7834f0b00e458aca64dcde"></a>

```c
#define TCPC_REG_PRODUCT_ID 0x2
```

相关声明：[TCPC_REG_PRODUCT_ID](#a298d4f136a7834f0b00e458aca64dcde)。

寄存器地址（Register Address）：产品 ID（Product ID）。

<a id="r_a2448e8e0bba63c1dece60361515f8393"></a>

```c
#define TCPC_REG_BCD_DEV 0x4
```

相关声明：[TCPC_REG_BCD_DEV](#a2448e8e0bba63c1dece60361515f8393)。

寄存器地址（Register Address）：TCPC 版本（Version）。

<a id="r_a67e70b7ed5d7f1ea18bee26314677633"></a>

```c
#define TCPC_REG_TC_REV 0x6
```

相关声明：[TCPC_REG_TC_REV](#a67e70b7ed5d7f1ea18bee26314677633)。

寄存器地址（Register Address）：USB Type-C 版本（Version）。

<a id="r_a9bbad168da5862eb7c8494925380546d"></a>

```c
#define TCPC_REG_TC_REV_MAJOR_MASK GENMASK(7, 4)
```

相关声明：[TCPC_REG_TC_REV_MAJOR_MASK](#a9bbad168da5862eb7c8494925380546d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 Type-C 发行版本主版本部分的掩码（Major Release Mask）。

<a id="r_ac87ba6ce928e84bffc2333584bfabcf7"></a>

```c
#define TCPC_REG_TC_REV_MAJOR(reg)
```

相关声明：[TCPC_REG_TC_REV_MAJOR](#ac87ba6ce928e84bffc2333584bfabcf7)。

提取支持的 Type-C 发行版本主版本部分的宏（Major Release Extraction Macro）。

<a id="r_a6a1e3d112af2697f1945614c57df9f26"></a>

```c
#define TCPC_REG_TC_REV_MINOR_MASK GENMASK(3, 0)
```

相关声明：[TCPC_REG_TC_REV_MINOR_MASK](#a6a1e3d112af2697f1945614c57df9f26)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 Type-C 发行版本次版本部分的掩码（Minor Release Mask）。

<a id="r_a9892dc0a9d01deaf56e8a28546489e65"></a>

```c
#define TCPC_REG_TC_REV_MINOR(reg)
```

相关声明：[TCPC_REG_TC_REV_MINOR](#a9892dc0a9d01deaf56e8a28546489e65)。

提取支持的 Type-C 发行版本次版本部分的宏（Minor Release Extraction Macro）。

<a id="r_ac8e53caa68f00ab934c3636d6fab1981"></a>

```c
#define TCPC_REG_PD_REV 0x8
```

相关声明：[TCPC_REG_PD_REV](#ac8e53caa68f00ab934c3636d6fab1981)。

寄存器地址（Register Address）：USB 电力传输修订版本（Power Delivery Revision）。

<a id="r_a248e7ad12084944b3255883ee883d335"></a>

```c
#define TCPC_REG_PD_REV_REV_MAJOR_MASK GENMASK(15, 12)
```

相关声明：[TCPC_REG_PD_REV_REV_MAJOR_MASK](#a248e7ad12084944b3255883ee883d335)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 USB PD 修订版本（Revision）主版本部分的掩码。

<a id="r_a80f6d51ecf6b817d825d52f3552551d3"></a>

```c
#define TCPC_REG_PD_REV_REV_MAJOR(reg)
```

相关声明：[TCPC_REG_PD_REV_REV_MAJOR](#a80f6d51ecf6b817d825d52f3552551d3)。

提取支持的 USB PD 修订版本（Revision）主版本部分的宏。

<a id="r_ab42fdb425046a9b68a29241f81685d65"></a>

```c
#define TCPC_REG_PD_REV_REV_MINOR_MASK GENMASK(11, 8)
```

相关声明：[TCPC_REG_PD_REV_REV_MINOR_MASK](#ab42fdb425046a9b68a29241f81685d65)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 USB PD 修订版本（Revision）次版本部分的掩码。

<a id="r_a5da3d67228275a828efb9fca1862e7c2"></a>

```c
#define TCPC_REG_PD_REV_REV_MINOR(reg)
```

相关声明：[TCPC_REG_PD_REV_REV_MINOR](#a5da3d67228275a828efb9fca1862e7c2)。

提取支持的 USB PD 修订版本（Revision）次版本部分的宏。

<a id="r_a20bfddfd4d72c697639c742796968482"></a>

```c
#define TCPC_REG_PD_REV_VER_MAJOR_MASK GENMASK(7, 4)
```

相关声明：[TCPC_REG_PD_REV_VER_MAJOR_MASK](#a20bfddfd4d72c697639c742796968482)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 USB PD 版本（Version）主版本部分的掩码。

<a id="r_a9d505ec3fe9f2029fc855d5127a36633"></a>

```c
#define TCPC_REG_PD_REV_VER_MAJOR(reg)
```

相关声明：[TCPC_REG_PD_REV_VER_MAJOR](#a9d505ec3fe9f2029fc855d5127a36633)。

提取支持的 USB PD 版本（Version）主版本部分的宏。

<a id="r_ab3b6a60982e7e9192b2cf4fbda9aa453"></a>

```c
#define TCPC_REG_PD_REV_VER_MINOR_MASK GENMASK(3, 0)
```

相关声明：[TCPC_REG_PD_REV_VER_MINOR_MASK](#ab3b6a60982e7e9192b2cf4fbda9aa453)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 USB PD 版本（Version）次版本部分的掩码。

<a id="r_af6ce6eaa30960a799436e4841520d183"></a>

```c
#define TCPC_REG_PD_REV_VER_MINOR(reg)
```

相关声明：[TCPC_REG_PD_REV_VER_MINOR](#af6ce6eaa30960a799436e4841520d183)。

提取支持的 USB PD 版本（Version）次版本部分的宏。

<a id="r_a25bd2e39fa396a3c097244a14d4a53b3"></a>

```c
#define TCPC_REG_PD_INT_REV 0xa
```

相关声明：[TCPC_REG_PD_INT_REV](#a25bd2e39fa396a3c097244a14d4a53b3)。

寄存器地址（Register Address）：接口修订版本与版本（Revision and Version）。

<a id="r_afd52534290a2b7d738ea73888d16419f"></a>

```c
#define TCPC_REG_PD_INT_REV_REV_MAJOR_MASK GENMASK(15, 12)
```

相关声明：[TCPC_REG_PD_INT_REV_REV_MAJOR_MASK](#afd52534290a2b7d738ea73888d16419f)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 USB 端口控制器接口修订版本（Revision）主版本部分的掩码。

<a id="r_acbd18c6ccab38cf4227a7f82741de5cb"></a>

```c
#define TCPC_REG_PD_INT_REV_REV_MAJOR(reg)
```

相关声明：[TCPC_REG_PD_INT_REV_REV_MAJOR](#acbd18c6ccab38cf4227a7f82741de5cb)。

提取支持的 USB 端口控制器接口修订版本（Revision）主版本部分的宏。

<a id="r_a66e85404023d11733db1d71a1625f4e9"></a>

```c
#define TCPC_REG_PD_INT_REV_REV_MINOR_MASK GENMASK(11, 8)
```

相关声明：[TCPC_REG_PD_INT_REV_REV_MINOR_MASK](#a66e85404023d11733db1d71a1625f4e9)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 USB 端口控制器接口修订版本（Revision）次版本部分的掩码。

<a id="r_ada1c0275ebfe2e5e558e7026531f89a6"></a>

```c
#define TCPC_REG_PD_INT_REV_REV_MINOR(reg)
```

相关声明：[TCPC_REG_PD_INT_REV_REV_MINOR](#ada1c0275ebfe2e5e558e7026531f89a6)。

提取支持的 USB 端口控制器接口修订版本（Revision）次版本部分的宏。

<a id="r_a19c752a82a935fd74d9c22be4f9c2e79"></a>

```c
#define TCPC_REG_PD_INT_REV_VER_MAJOR_MASK GENMASK(7, 4)
```

相关声明：[TCPC_REG_PD_INT_REV_VER_MAJOR_MASK](#a19c752a82a935fd74d9c22be4f9c2e79)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 USB 端口控制器接口版本（Version）主版本部分的掩码。

<a id="r_a30bac3197df65667c80168e808008056"></a>

```c
#define TCPC_REG_PD_INT_REV_VER_MAJOR(reg)
```

相关声明：[TCPC_REG_PD_INT_REV_VER_MAJOR](#a30bac3197df65667c80168e808008056)。

提取支持的 USB 端口控制器接口版本（Version）主版本部分的宏。

<a id="r_af929c39cfc085b1dfe90ce46848fa39a"></a>

```c
#define TCPC_REG_PD_INT_REV_VER_MINOR_MASK GENMASK(3, 0)
```

相关声明：[TCPC_REG_PD_INT_REV_VER_MINOR_MASK](#af929c39cfc085b1dfe90ce46848fa39a)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 USB 端口控制器接口版本（Version）次版本部分的掩码。

<a id="r_ae1f08c2a243063a390cc45ba84ee1b8b"></a>

```c
#define TCPC_REG_PD_INT_REV_VER_MINOR(reg)
```

相关声明：[TCPC_REG_PD_INT_REV_VER_MINOR](#ae1f08c2a243063a390cc45ba84ee1b8b)。

提取支持的 USB 端口控制器接口版本（Version）次版本部分的宏。

<a id="r_a2912dc3a362dd0a50388934fef0f99f4"></a>

```c
#define TCPC_REG_ALERT 0x10
```

相关声明：[TCPC_REG_ALERT](#a2912dc3a362dd0a50388934fef0f99f4)。

寄存器地址（Register Address）：告警（Alert）。

<a id="r_a2f336fd5d5eccc008a88a40c61535a63"></a>

```c
#define TCPC_REG_ALERT_NONE 0x0000
```

相关声明：[TCPC_REG_ALERT_NONE](#a2f336fd5d5eccc008a88a40c61535a63)。

用于清除告警（Clear Alert）的值。

<a id="r_af773296fd7587c55cef03240f26bd07a"></a>

```c
#define TCPC_REG_ALERT_MASK_ALL 0xffff
```

相关声明：[TCPC_REG_ALERT_MASK_ALL](#af773296fd7587c55cef03240f26bd07a)。

覆盖所有告警位（Alert Bits）的值掩码。

<a id="r_adfbf14335108bfcdd44dd530318e58c3"></a>

```c
#define TCPC_REG_ALERT_VENDOR_DEF BIT(15)
```

相关声明：[TCPC_REG_ALERT_VENDOR_DEF](#adfbf14335108bfcdd44dd530318e58c3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

厂商定义告警位（Vendor Defined Alert Bit）。

<a id="r_a90fe3405bf387ab726dd09fd935a3dee"></a>

```c
#define TCPC_REG_ALERT_ALERT_EXT BIT(14)
```

相关声明：[TCPC_REG_ALERT_ALERT_EXT](#a90fe3405bf387ab726dd09fd935a3dee)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

扩展告警位（Extended Alert Bit）。

<a id="r_a2655ef7f43979b32a5df5c28982d7af6"></a>

```c
#define TCPC_REG_ALERT_EXT_STATUS BIT(13)
```

相关声明：[TCPC_REG_ALERT_EXT_STATUS](#a2655ef7f43979b32a5df5c28982d7af6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

扩展状态告警位（Extended Status Alert Bit）。

<a id="r_a0569d2eaffe745605cfe43a21d070bac"></a>

```c
#define TCPC_REG_ALERT_RX_BEGINNING BIT(12)
```

相关声明：[TCPC_REG_ALERT_RX_BEGINNING](#a0569d2eaffe745605cfe43a21d070bac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

数据接收开始位（Beginning of Data Receive Bit）。

<a id="r_afe588ff7743a0eeafa5cada02777eb0a"></a>

```c
#define TCPC_REG_ALERT_VBUS_DISCNCT BIT(11)
```

相关声明：[TCPC_REG_ALERT_VBUS_DISCNCT](#afe588ff7743a0eeafa5cada02777eb0a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 断开连接告警位（Disconnection Alert Bit）。

<a id="r_a7e3e12d0b0a0acfee08bdfd2cd4f849f"></a>

```c
#define TCPC_REG_ALERT_RX_BUF_OVF BIT(10)
```

相关声明：[TCPC_REG_ALERT_RX_BUF_OVF](#a7e3e12d0b0a0acfee08bdfd2cd4f849f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

接收缓冲区溢出告警位（Receive Buffer Overflow Alert Bit）。

<a id="r_af48632dbad216d1cef4adbeb60645e2a"></a>

```c
#define TCPC_REG_ALERT_FAULT BIT(9)
```

相关声明：[TCPC_REG_ALERT_FAULT](#af48632dbad216d1cef4adbeb60645e2a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

故障告警位（Fault Alert Bit）。

<a id="r_a512d3df7520be440e2b34455ae1953e1"></a>

```c
#define TCPC_REG_ALERT_V_ALARM_LO BIT(8)
```

相关声明：[TCPC_REG_ALERT_V_ALARM_LO](#a512d3df7520be440e2b34455ae1953e1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 低电压报警位（Low VBUS Alarm Bit）。

<a id="r_a99145be67b60b4b1600b634933612fc7"></a>

```c
#define TCPC_REG_ALERT_V_ALARM_HI BIT(7)
```

相关声明：[TCPC_REG_ALERT_V_ALARM_HI](#a99145be67b60b4b1600b634933612fc7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 高电压报警位（High VBUS Alarm Bit）。

<a id="r_a796239522f17dca1a1980e22361806bb"></a>

```c
#define TCPC_REG_ALERT_TX_SUCCESS BIT(6)
```

相关声明：[TCPC_REG_ALERT_TX_SUCCESS](#a796239522f17dca1a1980e22361806bb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

传输成功位（Transmission Success Bit）。

<a id="r_aebf0469fd43f152c6269df4fe53bca07"></a>

```c
#define TCPC_REG_ALERT_TX_DISCARDED BIT(5)
```

相关声明：[TCPC_REG_ALERT_TX_DISCARDED](#aebf0469fd43f152c6269df4fe53bca07)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

传输丢弃告警位（Transmission Discard Alert Bit）。

<a id="r_a0ee35769b5e6770ef1b20eb2d8cfd830"></a>

```c
#define TCPC_REG_ALERT_TX_FAILED BIT(4)
```

相关声明：[TCPC_REG_ALERT_TX_FAILED](#a0ee35769b5e6770ef1b20eb2d8cfd830)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

传输失败告警位（Transmission Fail Alert Bit）。

<a id="r_a98032350a32b76b6010c91a657e552ef"></a>

```c
#define TCPC_REG_ALERT_RX_HARD_RST BIT(3)
```

相关声明：[TCPC_REG_ALERT_RX_HARD_RST](#a98032350a32b76b6010c91a657e552ef)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

收到硬复位告警位（Received Hard Reset Alert Bit）。

<a id="r_aeecc16c85ab4e3091fdb000474f73ecd"></a>

```c
#define TCPC_REG_ALERT_RX_STATUS BIT(2)
```

相关声明：[TCPC_REG_ALERT_RX_STATUS](#aeecc16c85ab4e3091fdb000474f73ecd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

已收到数据告警位（Data Received Alert Bit）。

<a id="r_a39dd56e219d607211c10f313cca524ad"></a>

```c
#define TCPC_REG_ALERT_POWER_STATUS BIT(1)
```

相关声明：[TCPC_REG_ALERT_POWER_STATUS](#a39dd56e219d607211c10f313cca524ad)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电源状态告警位（Power Status Alert Bit）。

<a id="r_a162d24b8d3b425c3f18dd1ed0fc73919"></a>

```c
#define TCPC_REG_ALERT_CC_STATUS BIT(0)
```

相关声明：[TCPC_REG_ALERT_CC_STATUS](#a162d24b8d3b425c3f18dd1ed0fc73919)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

配置通道线状态告警位（CC Lines Status Alert Bit）。

<a id="r_a3f4f765c1fe2e7a4b75827e5a381f053"></a>

```c
#define TCPC_REG_ALERT_TX_COMPLETE (TCPC_REG_ALERT_TX_SUCCESS | TCPC_REG_ALERT_TX_DISCARDED | TCPC_REG_ALERT_TX_FAILED)
```

相关声明：[TCPC_REG_ALERT_TX_COMPLETE](#a3f4f765c1fe2e7a4b75827e5a381f053)、[TCPC_REG_ALERT_TX_SUCCESS](#a796239522f17dca1a1980e22361806bb)、[TCPC_REG_ALERT_TX_DISCARDED](#aebf0469fd43f152c6269df4fe53bca07)、[TCPC_REG_ALERT_TX_FAILED](#a0ee35769b5e6770ef1b20eb2d8cfd830)。

任意传输状态告警（Transmission Status Alert）对应的位集合。

<a id="r_ae66b8c8732e19348b3bee4509ed97453"></a>

```c
#define TCPC_REG_ALERT_MASK 0x12
```

相关声明：[TCPC_REG_ALERT_MASK](#ae66b8c8732e19348b3bee4509ed97453)。

寄存器地址：告警掩码（Alert Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

<a id="r_a1358f98fb30c51b45ff2fe35eed2431c"></a>

```c
#define TCPC_REG_POWER_STATUS_MASK 0x14
```

相关声明：[TCPC_REG_POWER_STATUS_MASK](#a1358f98fb30c51b45ff2fe35eed2431c)。

寄存器地址：电源状态掩码（Power Status Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

<a id="r_a3a6d7e0a7641251361c8991630e6e35b"></a>

```c
#define TCPC_REG_FAULT_STATUS_MASK 0x15
```

相关声明：[TCPC_REG_FAULT_STATUS_MASK](#a3a6d7e0a7641251361c8991630e6e35b)。

寄存器地址：故障状态掩码（Fault Status Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

<a id="r_ad8d4a179cf4ca331988d3085faabe40e"></a>

```c
#define TCPC_REG_EXT_STATUS_MASK 0x16
```

相关声明：[TCPC_REG_EXT_STATUS_MASK](#ad8d4a179cf4ca331988d3085faabe40e)。

寄存器地址：扩展状态掩码（Extended Status Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

<a id="r_a6e5e4f39a81278645ca9045f3648d3d8"></a>

```c
#define TCPC_REG_ALERT_EXT_MASK 0x17
```

相关声明：[TCPC_REG_ALERT_EXT_MASK](#a6e5e4f39a81278645ca9045f3648d3d8)。

寄存器地址：扩展告警掩码（Extended Alert Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

<a id="r_af0974e48cbc9c96c61bb9d7b5c81c1f2"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT 0x18
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT](#af0974e48cbc9c96c61bb9d7b5c81c1f2)。

寄存器地址：标准输出配置（Configure Standard Output）。

<a id="r_a23f41760b310d34ff81decbec419fe59"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_HIGH_Z BIT(7)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_HIGH_Z](#a23f41760b310d34ff81decbec419fe59)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

高阻输出位（High Impedance Outputs Bit）。

<a id="r_a1f8f1deec957703b32c7704cbfe63c5c"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_DBG_ACC_CONN_N BIT(6)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_DBG_ACC_CONN_N](#a1f8f1deec957703b32c7704cbfe63c5c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

调试附件已连接信号位（Debug Accessory Connected#）。

<a id="r_a8d6fc07d7be8c4042929f45ff449381d"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_AUDIO_CONN_N BIT(5)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_AUDIO_CONN_N](#a8d6fc07d7be8c4042929f45ff449381d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

音频附件已连接信号位（Audio Accessory Connected#）。

<a id="r_a8f91eacfa5f50bdf8d4e187967c34686"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_ACTIVE_CABLE BIT(4)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_ACTIVE_CABLE](#a8f91eacfa5f50bdf8d4e187967c34686)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

有源线缆位（Active Cable Bit）。

<a id="r_a592a89b62ec5d9cf724a28e836cf2804"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_MASK (3 << 2)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_MUX_MASK](#a592a89b62ec5d9cf724a28e836cf2804)。

多路复用器控制值掩码（Mux Control Value Mask）。

<a id="r_ae791c676d7d2e6abd9ee59acdca7ad3d"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_NONE (0 << 2)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_MUX_NONE](#ae791c676d7d2e6abd9ee59acdca7ad3d)。

多路复用器（Mux）取值：无连接。

<a id="r_a0b26b6588c8836f33b76575047afe099"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB (1 << 2)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB](#a0b26b6588c8836f33b76575047afe099)。

多路复用器（Mux）取值：USB 3.1 已连接。

<a id="r_af821127c6e9f29f25012aedb148f3f84"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_DP (2 << 2)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_MUX_DP](#af821127c6e9f29f25012aedb148f3f84)。

多路复用器（Mux）取值：4 通道 DisplayPort 替代模式（DP Alternate Mode）。

<a id="r_a7099c9623ef26f505c4a7d63c83a09be"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB_DP (3 << 2)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB_DP](#a7099c9623ef26f505c4a7d63c83a09be)。

多路复用器（Mux）取值：USB 3.1 加 DP 0、1 线路。

<a id="r_a1d6ec65538daf13b8ca9b8c2257b2b0f"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_CONN_PRESENT BIT(1)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_CONN_PRESENT](#a1d6ec65538daf13b8ca9b8c2257b2b0f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

连接存在位（Connection Present Bit）。

<a id="r_a2bd794c9a986a9d573c08591e7aad86e"></a>

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_CONNECTOR_FLIPPED BIT(0)
```

相关声明：[TCPC_REG_CONFIG_STD_OUTPUT_CONNECTOR_FLIPPED](#a2bd794c9a986a9d573c08591e7aad86e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

连接器方向位（Connector Orientation Bit）。

<a id="r_a5be1063bb4f9c7db7f9f6a870858455d"></a>

```c
#define TCPC_REG_TCPC_CTRL 0x19
```

相关声明：[TCPC_REG_TCPC_CTRL](#a5be1063bb4f9c7db7f9f6a870858455d)。

寄存器地址：端口控制器控制（TCPC Control）。

<a id="r_a3e023fad44f6e27c2b3b39f436c359d2"></a>

```c
#define TCPC_REG_TCPC_CTRL_SMBUS_PEC BIT(7)
```

相关声明：[TCPC_REG_TCPC_CTRL_SMBUS_PEC](#a3e023fad44f6e27c2b3b39f436c359d2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

SMBus 数据包错误码（PEC）使能位。

<a id="r_aa672c46d6a4332ba050c535b17693497"></a>

```c
#define TCPC_REG_TCPC_CTRL_EN_LOOK4CONNECTION_ALERT BIT(6)
```

相关声明：[TCPC_REG_TCPC_CTRL_EN_LOOK4CONNECTION_ALERT](#aa672c46d6a4332ba050c535b17693497)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

发现连接时使能告警有效输出（Alert Assertion）的位。

<a id="r_ab28ab0d34d76d44bd66570cec9f6c08f"></a>

```c
#define TCPC_REG_TCPC_CTRL_WATCHDOG_TIMER BIT(5)
```

相关声明：[TCPC_REG_TCPC_CTRL_WATCHDOG_TIMER](#ab28ab0d34d76d44bd66570cec9f6c08f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

看门狗监视位（Watchdog Monitoring Bit）。

<a id="r_a990e2cad707373a0741ec1d679b9fe30"></a>

```c
#define TCPC_REG_TCPC_CTRL_DEBUG_ACC_CONTROL BIT(4)
```

相关声明：[TCPC_REG_TCPC_CTRL_DEBUG_ACC_CONTROL](#a990e2cad707373a0741ec1d679b9fe30)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能端口管理器（TCPM）控制调试附件的位。

<a id="r_a63e57b4638e0a221cc1a5d0ad0c5daf9"></a>

```c
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_MASK GENMASK(3, 2)
```

相关声明：[TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_MASK](#a63e57b4638e0a221cc1a5d0ad0c5daf9)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

掩码（Mask）。

<a id="r_a857522248dd727c57c63958aa3ca9d52"></a>

```c
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_DISABLED 0
```

相关声明：[TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_DISABLED](#a857522248dd727c57c63958aa3ca9d52)。

禁用时钟拉伸（Clock Stretching）的取值。

<a id="r_a3915ad947314f254aa741d29b68478ae"></a>

```c
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_ALWAYS (2 << 2)
```

相关声明：[TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_ALWAYS](#a3915ad947314f254aa741d29b68478ae)。

使能有限时钟拉伸（Limited Clock Stretching）的取值。

<a id="r_ae39a550bcf4bf6ec6a2cf23c6938933d"></a>

```c
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_NO_ALERT (3 << 2)
```

相关声明：[TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_NO_ALERT](#ae39a550bcf4bf6ec6a2cf23c6938933d)。

仅在告警未置为有效（Alert Not Asserted）时使能时钟拉伸的取值。

<a id="r_aebc9538529f9d9e516dec8973445ba0a"></a>

```c
#define TCPC_REG_TCPC_CTRL_BIST_TEST_MODE BIT(1)
```

相关声明：[TCPC_REG_TCPC_CTRL_BIST_TEST_MODE](#aebc9538529f9d9e516dec8973445ba0a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内建自测试模式（BIST Test Mode）使能位。

<a id="r_a8d44838af49c8eb316668a014eb71704"></a>

```c
#define TCPC_REG_TCPC_CTRL_PLUG_ORIENTATION BIT(0)
```

相关声明：[TCPC_REG_TCPC_CTRL_PLUG_ORIENTATION](#a8d44838af49c8eb316668a014eb71704)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

插头方向与 VCONN 目标（Plug Orientation and VCONN Destination）位。

<a id="r_a06d954c1171e6b8804214d73b5010444"></a>

```c
#define TCPC_REG_ROLE_CTRL 0x1a
```

相关声明：[TCPC_REG_ROLE_CTRL](#a06d954c1171e6b8804214d73b5010444)。

寄存器地址：角色控制（Role Control）。

<a id="r_a7c0ebf31802f08dc392a8ecbc019ef1d"></a>

```c
#define TCPC_REG_ROLE_CTRL_DRP_MASK BIT(6)
```

相关声明：[TCPC_REG_ROLE_CTRL_DRP_MASK](#a7c0ebf31802f08dc392a8ecbc019ef1d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

双角色端口位（Dual-role Port Bit）。

<a id="r_aff7095f3362ec2fb1b98a5f27c6a55bd"></a>

```c
#define TCPC_REG_ROLE_CTRL_RP_MASK GENMASK(5, 4)
```

相关声明：[TCPC_REG_ROLE_CTRL_RP_MASK](#aff7095f3362ec2fb1b98a5f27c6a55bd)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

从寄存器值提取上拉电阻（Rp）值的掩码。

<a id="r_a3c8cc683f79e6c5a0649af7e4a005792"></a>

```c
#define TCPC_REG_ROLE_CTRL_CC2_MASK GENMASK(3, 2)
```

相关声明：[TCPC_REG_ROLE_CTRL_CC2_MASK](#a3c8cc683f79e6c5a0649af7e4a005792)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

从寄存器值提取 CC2 上下拉配置（Pull）值的掩码。

<a id="r_a968371033f0493924fc19156357039f0"></a>

```c
#define TCPC_REG_ROLE_CTRL_CC1_MASK GENMASK(1, 0)
```

相关声明：[TCPC_REG_ROLE_CTRL_CC1_MASK](#a968371033f0493924fc19156357039f0)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

用于提取 CC1 配置的掩码（Mask）。译注：原文写作 `CC!`；此项对应 `TCPC_REG_ROLE_CTRL_CC1_MASK`，按宏名称译为 CC1，详细说明的后续文字为从寄存器值提取上下拉配置。

<a id="r_a2763dec90728fb301ea56118da50e7b7"></a>

```c
#define TCPC_REG_ROLE_CTRL_SET(drp, rp, cc1, cc2)
```

相关声明：[TCPC_REG_ROLE_CTRL_SET](#a2763dec90728fb301ea56118da50e7b7)。

根据 `drp`、`rp` 和配置通道线（CC Lines）的值设置寄存器值的宏。

<a id="r_a5b8503dba17f2aa86e334a2e9975aed7"></a>

```c
#define TCPC_REG_ROLE_CTRL_DRP(reg)
```

相关声明：[TCPC_REG_ROLE_CTRL_DRP](#a5b8503dba17f2aa86e334a2e9975aed7)。

从寄存器值提取双角色端口位（Dual-role Port Bit）的宏。

<a id="r_ac3e73dc4203eb9f7926d682e5e755356"></a>

```c
#define TCPC_REG_ROLE_CTRL_RP(reg)
```

相关声明：[TCPC_REG_ROLE_CTRL_RP](#ac3e73dc4203eb9f7926d682e5e755356)。

从寄存器值提取 `enum tc_rp_value` 的宏。

<a id="r_ae265027a9005b40b53342953df43d5a8"></a>

```c
#define TCPC_REG_ROLE_CTRL_CC2(reg)
```

相关声明：[TCPC_REG_ROLE_CTRL_CC2](#ae265027a9005b40b53342953df43d5a8)。

从寄存器值提取 CC2 的 `enum tc_cc_pull` 的宏。

<a id="r_a4d92739010143fed7976ce7d14859106"></a>

```c
#define TCPC_REG_ROLE_CTRL_CC1(reg)
```

相关声明：[TCPC_REG_ROLE_CTRL_CC1](#a4d92739010143fed7976ce7d14859106)。

从寄存器值提取 CC1 的 `enum tc_cc_pull` 的宏。

<a id="r_ab820a732a55091e9cc1b2c41e555cfe0"></a>

```c
#define TCPC_REG_FAULT_CTRL 0x1b
```

相关声明：[TCPC_REG_FAULT_CTRL](#ab820a732a55091e9cc1b2c41e555cfe0)。

寄存器地址：故障控制（Fault Control）。

<a id="r_aec1969186b70dc923e6f8d9827b8a766"></a>

```c
#define TCPC_REG_FAULT_CTRL_VBUS_FORCE_OFF BIT(4)
```

相关声明：[TCPC_REG_FAULT_CTRL_VBUS_FORCE_OFF](#aec1969186b70dc923e6f8d9827b8a766)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

阻止标准输入信号强制关闭 VBUS 控制（Force Off VBUS Control）的位。

<a id="r_ab57a9e89d53bfd55565c8f33739390bd"></a>

```c
#define TCPC_REG_FAULT_CTRL_VBUS_DISCHARGE_FAULT BIT(3)
```

相关声明：[TCPC_REG_FAULT_CTRL_VBUS_DISCHARGE_FAULT](#ab57a9e89d53bfd55565c8f33739390bd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用 VBUS 放电故障检测定时器（Discharge Fault Detection Timer）的位。

<a id="r_a0ae16ec1e71eaaf0c74f0c6b29ea54f8"></a>

```c
#define TCPC_REG_FAULT_CTRL_VBUS_OCP_FAULT_DIS BIT(2)
```

相关声明：[TCPC_REG_FAULT_CTRL_VBUS_OCP_FAULT_DIS](#a0ae16ec1e71eaaf0c74f0c6b29ea54f8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用 VBUS 过流检测（Over Current Detection）的位。

<a id="r_ab471e71bcbef59d68aabb150e6ec7944"></a>

```c
#define TCPC_REG_FAULT_CTRL_VBUS_OVP_FAULT_DIS BIT(1)
```

相关声明：[TCPC_REG_FAULT_CTRL_VBUS_OVP_FAULT_DIS](#ab471e71bcbef59d68aabb150e6ec7944)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用 VBUS 过压检测（Over Voltage Detection）的位。

<a id="r_a9299f9bb8d4c79173a239b196f28ac4e"></a>

```c
#define TCPC_REG_FAULT_CTRL_VCONN_OCP_FAULT_DIS BIT(0)
```

相关声明：[TCPC_REG_FAULT_CTRL_VCONN_OCP_FAULT_DIS](#a9299f9bb8d4c79173a239b196f28ac4e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用 VCONN 过流检测（Over Current Detection）的位。

<a id="r_a2812837d13a05d4a645bbfa41cff7aee"></a>

```c
#define TCPC_REG_POWER_CTRL 0x1c
```

相关声明：[TCPC_REG_POWER_CTRL](#a2812837d13a05d4a645bbfa41cff7aee)。

寄存器地址：电源控制（Power Control）。

<a id="r_a3948eb5f06b80c835a84bb004ff7bded"></a>

```c
#define TCPC_REG_POWER_CTRL_FRS_ENABLE BIT(7)
```

相关声明：[TCPC_REG_POWER_CTRL_FRS_ENABLE](#a3948eb5f06b80c835a84bb004ff7bded)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

快速角色交换使能位（Fast Role Swap Enable Bit）。

<a id="r_af308532252e239e508944be24589d140"></a>

```c
#define TCPC_REG_POWER_CTRL_VBUS_VOL_MONITOR_DIS BIT(6)
```

相关声明：[TCPC_REG_POWER_CTRL_VBUS_VOL_MONITOR_DIS](#af308532252e239e508944be24589d140)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用 VBUS 电压监测（Voltage Monitoring）的位。

<a id="r_aa77568b8e2f41c88b99bb6b4fa10841a"></a>

```c
#define TCPC_REG_POWER_CTRL_VOLT_ALARM_DIS BIT(5)
```

相关声明：[TCPC_REG_POWER_CTRL_VOLT_ALARM_DIS](#aa77568b8e2f41c88b99bb6b4fa10841a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用电压报警（Voltage Alarms）的位。

<a id="r_a7f9af17bb101c2c57b6b18ab07537f10"></a>

```c
#define TCPC_REG_POWER_CTRL_AUTO_DISCHARGE_DISCONNECT BIT(4)
```

相关声明：[TCPC_REG_POWER_CTRL_AUTO_DISCHARGE_DISCONNECT](#a7f9af17bb101c2c57b6b18ab07537f10)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能基于 VBUS 电压自动放电（Automatic Discharge）的位。

<a id="r_a9319ea4d6e1176c85d91a1199c9b1d75"></a>

```c
#define TCPC_REG_POWER_CTRL_BLEED_DISCHARGE BIT(3)
```

相关声明：[TCPC_REG_POWER_CTRL_BLEED_DISCHARGE](#a9319ea4d6e1176c85d91a1199c9b1d75)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能 VBUS 泄放（Bleed Discharge）的位。

<a id="r_ae1a14dfde02dd7e51cb252beb6de3321"></a>

```c
#define TCPC_REG_POWER_CTRL_FORCE_DISCHARGE BIT(2)
```

相关声明：[TCPC_REG_POWER_CTRL_FORCE_DISCHARGE](#ae1a14dfde02dd7e51cb252beb6de3321)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能 VBUS 强制放电（Forced Discharge）的位。

<a id="r_a5ca6c7232aa8706cada5485028a14109"></a>

```c
#define TCPC_REG_POWER_CTRL_VCONN_SUPP BIT(1)
```

相关声明：[TCPC_REG_POWER_CTRL_VCONN_SUPP](#a5ca6c7232aa8706cada5485028a14109)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能支持的 VCONN 功率（VCONN Power Supported）的位。

<a id="r_a6c2757aad33c9467ee5339b2c556fcd2"></a>

```c
#define TCPC_REG_POWER_CTRL_VCONN_EN BIT(0)
```

相关声明：[TCPC_REG_POWER_CTRL_VCONN_EN](#a6c2757aad33c9467ee5339b2c556fcd2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能向配置通道线（CC Line）提供 VCONN 电源的位。

<a id="r_a46c5b1be60f4ed058f81df1e0aa391d6"></a>

```c
#define TCPC_REG_CC_STATUS 0x1d
```

相关声明：[TCPC_REG_CC_STATUS](#a46c5b1be60f4ed058f81df1e0aa391d6)。

寄存器地址：配置通道线状态（CC Lines Status）。

<a id="r_aa4a7868d1503a45f8fbc1cf599b64381"></a>

```c
#define TCPC_REG_CC_STATUS_LOOK4CONNECTION BIT(5)
```

相关声明：[TCPC_REG_CC_STATUS_LOOK4CONNECTION](#aa4a7868d1503a45f8fbc1cf599b64381)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

TCPC 主动查找连接（Looking for Connection）的位，适用于双角色端口（DRP）及仅受电端／供电端模式。

<a id="r_a23c8b7998f4431a3a511f888e67a4922"></a>

```c
#define TCPC_REG_CC_STATUS_CONNECT_RESULT BIT(4)
```

相关声明：[TCPC_REG_CC_STATUS_CONNECT_RESULT](#a23c8b7998f4431a3a511f888e67a4922)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

连接结果位（Connection Result Bit）：呈现下拉电阻 Rd 时置位，呈现上拉电阻 Rp 时清零。

<a id="r_a24e24cd118532bd78b8c82e5bf896820"></a>

```c
#define TCPC_REG_CC_STATUS_CC2_STATE_MASK GENMASK(3, 2)
```

相关声明：[TCPC_REG_CC_STATUS_CC2_STATE_MASK](#a24e24cd118532bd78b8c82e5bf896820)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

CC2 线路状态（Line State）的掩码。

<a id="r_a9dec41c0e03ce148f2a7d3281ebeb722"></a>

```c
#define TCPC_REG_CC_STATUS_CC2_STATE(reg)
```

相关声明：[TCPC_REG_CC_STATUS_CC2_STATE](#a9dec41c0e03ce148f2a7d3281ebeb722)。

提取 CC2 线路状态值（Status Value）的宏。

<a id="r_a754af0239b587e79932f58a172c24dd3"></a>

```c
#define TCPC_REG_CC_STATUS_CC1_STATE_MASK GENMASK(1, 0)
```

相关声明：[TCPC_REG_CC_STATUS_CC1_STATE_MASK](#a754af0239b587e79932f58a172c24dd3)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

CC1 线路状态（Line State）的掩码。

<a id="r_a060f5130c6102e46628117cf468d0a9f"></a>

```c
#define TCPC_REG_CC_STATUS_CC1_STATE(reg)
```

相关声明：[TCPC_REG_CC_STATUS_CC1_STATE](#a060f5130c6102e46628117cf468d0a9f)。

提取 CC1 线路状态值（Status Value）的宏。

<a id="r_a8b8c47fc9df661b15b662c2b0b52bb1b"></a>

```c
#define TCPC_REG_POWER_STATUS 0x1e
```

相关声明：[TCPC_REG_POWER_STATUS](#a8b8c47fc9df661b15b662c2b0b52bb1b)。

寄存器地址：电源状态（Power Status）。

<a id="r_a8ef2658290efe1ec162ce989f7cb6c94"></a>

```c
#define TCPC_REG_POWER_STATUS_DEBUG_ACC_CON BIT(7)
```

相关声明：[TCPC_REG_POWER_STATUS_DEBUG_ACC_CON](#a8ef2658290efe1ec162ce989f7cb6c94)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

调试附件已连接位（Debug Accessory Connected Bit）。

<a id="r_ace7c591c22de6ef1091a6e8b6330fd4c"></a>

```c
#define TCPC_REG_POWER_STATUS_UNINIT BIT(6)
```

相关声明：[TCPC_REG_POWER_STATUS_UNINIT](#ace7c591c22de6ef1091a6e8b6330fd4c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部初始化进行中位（Internal Initialization In-progress Bit）。

<a id="r_a0390bb8babb73e1bf51b9042b5651646"></a>

```c
#define TCPC_REG_POWER_STATUS_SOURCING_HV BIT(5)
```

相关声明：[TCPC_REG_POWER_STATUS_SOURCING_HV](#a0390bb8babb73e1bf51b9042b5651646)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

正在提供高电压位（Sourcing High Voltage Bit）。

<a id="r_af05c7cc4b4aac0eacc57c9db205d7567"></a>

```c
#define TCPC_REG_POWER_STATUS_SOURCING_VBUS BIT(4)
```

相关声明：[TCPC_REG_POWER_STATUS_SOURCING_VBUS](#af05c7cc4b4aac0eacc57c9db205d7567)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

正在提供 VBUS 电源位（Sourcing VBUS Bit）。

<a id="r_a655efec9f1a6ef9cfc69d5c332d165da"></a>

```c
#define TCPC_REG_POWER_STATUS_VBUS_DET BIT(3)
```

相关声明：[TCPC_REG_POWER_STATUS_VBUS_DET](#a655efec9f1a6ef9cfc69d5c332d165da)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 检测使能位（Detection Enabled Bit）。

<a id="r_acae1371112df4ce0f156e84539ec05a9"></a>

```c
#define TCPC_REG_POWER_STATUS_VBUS_PRES BIT(2)
```

相关声明：[TCPC_REG_POWER_STATUS_VBUS_PRES](#acae1371112df4ce0f156e84539ec05a9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 存在位（Present Bit）。

<a id="r_ae9302652868a84227ac9442e00aeecd3"></a>

```c
#define TCPC_REG_POWER_STATUS_VCONN_PRES BIT(1)
```

相关声明：[TCPC_REG_POWER_STATUS_VCONN_PRES](#ae9302652868a84227ac9442e00aeecd3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VCONN 存在位（Present Bit）。

<a id="r_a75cf8cfaa3c2c3149ad73e917ff3ab54"></a>

```c
#define TCPC_REG_POWER_STATUS_SINKING_VBUS BIT(0)
```

相关声明：[TCPC_REG_POWER_STATUS_SINKING_VBUS](#a75cf8cfaa3c2c3149ad73e917ff3ab54)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

正在从 VBUS 受电位（Sinking VBUS Bit）。

<a id="r_a558e8c8d1e50ef135afebaf2d65a40b5"></a>

```c
#define TCPC_REG_FAULT_STATUS 0x1f
```

相关声明：[TCPC_REG_FAULT_STATUS](#a558e8c8d1e50ef135afebaf2d65a40b5)。

寄存器地址：故障状态（Fault Status）。

<a id="r_aec48a88fd81cf610ad3dac92c7ba825f"></a>

```c
#define TCPC_REG_FAULT_STATUS_ALL_REGS_RESET BIT(7)
```

相关声明：[TCPC_REG_FAULT_STATUS_ALL_REGS_RESET](#aec48a88fd81cf610ad3dac92c7ba825f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

所有寄存器已复位为默认值的位（All Registers Reset to Default Bit）。

<a id="r_ab140bad4bc9ca3f8bf59ef005ce5f2e2"></a>

```c
#define TCPC_REG_FAULT_STATUS_FORCE_OFF_VBUS BIT(6)
```

相关声明：[TCPC_REG_FAULT_STATUS_FORCE_OFF_VBUS](#ab140bad4bc9ca3f8bf59ef005ce5f2e2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

因外部故障强制关闭 VBUS（Force VBUS Off）的位。

<a id="r_a035b4cdca5e34b16419f78f39767479b"></a>

```c
#define TCPC_REG_FAULT_STATUS_AUTO_DISCHARGE_FAIL BIT(5)
```

相关声明：[TCPC_REG_FAULT_STATUS_AUTO_DISCHARGE_FAIL](#a035b4cdca5e34b16419f78f39767479b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

自动放电失败位（Auto Discharge Failed Bit）。

<a id="r_aef11ca61ad37b817ca08816a7b9e2a2d"></a>

```c
#define TCPC_REG_FAULT_STATUS_FORCE_DISCHARGE_FAIL BIT(4)
```

相关声明：[TCPC_REG_FAULT_STATUS_FORCE_DISCHARGE_FAIL](#aef11ca61ad37b817ca08816a7b9e2a2d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

强制放电失败位（Force Discharge Failed Bit）。

<a id="r_a1ac9d22a9a7999da7b68d6c2edb2ca13"></a>

```c
#define TCPC_REG_FAULT_STATUS_VBUS_OVER_CURRENT BIT(3)
```

相关声明：[TCPC_REG_FAULT_STATUS_VBUS_OVER_CURRENT](#a1ac9d22a9a7999da7b68d6c2edb2ca13)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部或外部 VBUS 过流位（Over Current Bit）。

<a id="r_a9032f5f3dee6830457a8fd06ff78c356"></a>

```c
#define TCPC_REG_FAULT_STATUS_VBUS_OVER_VOLTAGE BIT(2)
```

相关声明：[TCPC_REG_FAULT_STATUS_VBUS_OVER_VOLTAGE](#a9032f5f3dee6830457a8fd06ff78c356)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部或外部 VBUS 过压位（Over Voltage Bit）。

<a id="r_a0dfd803a4f1a7aea8376d945df5de8d8"></a>

```c
#define TCPC_REG_FAULT_STATUS_VCONN_OVER_CURRENT BIT(1)
```

相关声明：[TCPC_REG_FAULT_STATUS_VCONN_OVER_CURRENT](#a0dfd803a4f1a7aea8376d945df5de8d8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VCONN 过流位（Over Current Bit）。

<a id="r_a78d783025aed6f6118744a443d881eb5"></a>

```c
#define TCPC_REG_FAULT_STATUS_I2C_INTERFACE_ERR BIT(0)
```

相关声明：[TCPC_REG_FAULT_STATUS_I2C_INTERFACE_ERR](#a78d783025aed6f6118744a443d881eb5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I2C 接口错误位（Interface Error Bit）。

<a id="r_a80738bada4f82681fb36cfc019390245"></a>

```c
#define TCPC_REG_EXT_STATUS 0x20
```

相关声明：[TCPC_REG_EXT_STATUS](#a80738bada4f82681fb36cfc019390245)。

寄存器地址：扩展状态（Extended Status）。

<a id="r_ae266a7de13017c05be74f4163babcc95"></a>

```c
#define TCPC_REG_EXT_STATUS_SAFE0V BIT(0)
```

相关声明：[TCPC_REG_EXT_STATUS_SAFE0V](#ae266a7de13017c05be74f4163babcc95)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 处于安全零电压（vSafe0V）的位。

<a id="r_a18b16eb65336476a01ecef65a60eb8cf"></a>

```c
#define TCPC_REG_ALERT_EXT 0x21
```

相关声明：[TCPC_REG_ALERT_EXT](#a18b16eb65336476a01ecef65a60eb8cf)。

寄存器地址：扩展告警（Alert Extended）。

<a id="r_aa49f73642ef4a513ba1e585d9d515c40"></a>

```c
#define TCPC_REG_ALERT_EXT_TIMER_EXPIRED BIT(2)
```

相关声明：[TCPC_REG_ALERT_EXT_TIMER_EXPIRED](#aa49f73642ef4a513ba1e585d9d515c40)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

定时器到期位（Timer Expired Bit）。

<a id="r_abfdd8a966a0922ca9b0f0b4e8d813d0d"></a>

```c
#define TCPC_REG_ALERT_EXT_SRC_FRS BIT(1)
```

相关声明：[TCPC_REG_ALERT_EXT_SRC_FRS](#abfdd8a966a0922ca9b0f0b4e8d813d0d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

供电端快速角色交换位（Source Fast Role Swap Bit）。

<a id="r_a226652120eb8ccb442953727e1a8faef"></a>

```c
#define TCPC_REG_ALERT_EXT_SNK_FRS BIT(0)
```

相关声明：[TCPC_REG_ALERT_EXT_SNK_FRS](#a226652120eb8ccb442953727e1a8faef)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

受电端快速角色交换位（Sink Fast Role Swap Bit）。

<a id="r_a786e23ebac906747f484f7395b5f8815"></a>

```c
#define TCPC_REG_COMMAND 0x23
```

相关声明：[TCPC_REG_COMMAND](#a786e23ebac906747f484f7395b5f8815)。

寄存器地址：命令（Command）。

<a id="r_abca86d8ca8afaa0372a28de4b6f38598"></a>

```c
#define TCPC_REG_COMMAND_WAKE_I2C 0x11
```

相关声明：[TCPC_REG_COMMAND_WAKE_I2C](#abca86d8ca8afaa0372a28de4b6f38598)。

唤醒 I2C 命令（Wake I2C Command）的取值。

<a id="r_aeab573fd25108d577e79efc75a618f00"></a>

```c
#define TCPC_REG_COMMAND_DISABLE_VBUS_DETECT 0x22
```

相关声明：[TCPC_REG_COMMAND_DISABLE_VBUS_DETECT](#aeab573fd25108d577e79efc75a618f00)。

禁用 VBUS 检测命令（Disable VBUS Detect）的取值：禁用 VBUS 存在检测及 vSafe0V 检测。

<a id="r_a601725f09f99ac7f8c015ba6259b6308"></a>

```c
#define TCPC_REG_COMMAND_ENABLE_VBUS_DETECT 0x33
```

相关声明：[TCPC_REG_COMMAND_ENABLE_VBUS_DETECT](#a601725f09f99ac7f8c015ba6259b6308)。

使能 VBUS 检测命令（Enable VBUS Detect）的取值：使能 VBUS 存在检测及 vSafe0V 检测。

<a id="r_aa452968b9e6c1d0716e5f65bc99da707"></a>

```c
#define TCPC_REG_COMMAND_SNK_CTRL_LOW 0x44
```

相关声明：[TCPC_REG_COMMAND_SNK_CTRL_LOW](#aa452968b9e6c1d0716e5f65bc99da707)。

禁用 VBUS 受电（Disable Sink VBUS）的取值：禁用从 VBUS 接收电力。

<a id="r_ab978fbd78be69065e60a41501ee688a8"></a>

```c
#define TCPC_REG_COMMAND_SNK_CTRL_HIGH 0x55
```

相关声明：[TCPC_REG_COMMAND_SNK_CTRL_HIGH](#ab978fbd78be69065e60a41501ee688a8)。

使能 VBUS 受电（Sink VBUS）的取值：使能从 VBUS 接收电力及 VBUS 存在检测。

<a id="r_a4abac8ab83a504d5abde30d23916dc67"></a>

```c
#define TCPC_REG_COMMAND_SRC_CTRL_LOW 0x66
```

相关声明：[TCPC_REG_COMMAND_SRC_CTRL_LOW](#a4abac8ab83a504d5abde30d23916dc67)。

禁用 VBUS 供电（Disable Source VBUS）的取值：禁用通过 VBUS 提供电力。

<a id="r_ad2b892f6896c62fa8762fab51449e61f"></a>

```c
#define TCPC_REG_COMMAND_SRC_CTRL_DEF 0x77
```

相关声明：[TCPC_REG_COMMAND_SRC_CTRL_DEF](#ad2b892f6896c62fa8762fab51449e61f)。

VBUS 默认电压供电（Source VBUS Default Voltage）的取值：使能在 VBUS 上提供 vSafe5V。

<a id="r_ada9b44953e5d7e4058f5d81fd7d6859b"></a>

```c
#define TCPC_REG_COMMAND_SRC_CTRL_HV 0x88
```

相关声明：[TCPC_REG_COMMAND_SRC_CTRL_HV](#ada9b44953e5d7e4058f5d81fd7d6859b)。

VBUS 高电压供电（Source VBUS High Voltage）的取值：使能在 VBUS 上提供高电压。

<a id="r_aeb18bda1323ff68fcb4496daa54e6c8d"></a>

```c
#define TCPC_REG_COMMAND_LOOK4CONNECTION 0x99
```

相关声明：[TCPC_REG_COMMAND_LOOK4CONNECTION](#aeb18bda1323ff68fcb4496daa54e6c8d)。

查找连接（Look for Connection）的取值：如果角色设为 DRP，则启动双角色切换（DRP Toggling）。

<a id="r_a16b98dda32a66062fc615af01b78d1b7"></a>

```c
#define TCPC_REG_COMMAND_RX_ONE_MORE 0xAA
```

相关声明：[TCPC_REG_COMMAND_RX_ONE_MORE](#a16b98dda32a66062fc615af01b78d1b7)。

再接收一次（RX One More）的取值：配置接收器，使其在发送下一个 `GoodCRC` 后自动清除 `receive_detect` 寄存器。

<a id="r_ac5360c2d8c9b562012e8c4981f44a39b"></a>

```c
#define TCPC_REG_COMMAND_SEND_FRS_SIGNAL 0xCC
```

相关声明：[TCPC_REG_COMMAND_SEND_FRS_SIGNAL](#ac5360c2d8c9b562012e8c4981f44a39b)。

发送快速角色交换信号（Fast Role Swap Signal）的取值：TCPC 为供电端（Source）且电源控制寄存器已使能 FRS 时，发送 FRS。

<a id="r_a925b93707097ee2f35c989dd5647ae72"></a>

```c
#define TCPC_REG_COMMAND_RESET_TRANSMIT_BUF 0xDD
```

相关声明：[TCPC_REG_COMMAND_RESET_TRANSMIT_BUF](#a925b93707097ee2f35c989dd5647ae72)。

复位发送缓冲区（Reset Transmit Buffer）的取值：TCPC 将发送缓冲区指针复位到偏移量 1。

<a id="r_aac0e53143c26efe41d4228af32216ea3"></a>

```c
#define TCPC_REG_COMMAND_RESET_RECEIVE_BUF 0xEE
```

相关声明：[TCPC_REG_COMMAND_RESET_RECEIVE_BUF](#aac0e53143c26efe41d4228af32216ea3)。

复位接收缓冲区（Reset Receive Buffer）的取值：缓冲区指针小于等于 132 时复位到 1，否则复位到 133。

<a id="r_a67fe1eeebc7c7122962b4dca16cc439c"></a>

```c
#define TCPC_REG_COMMAND_I2CIDLE 0xFF
```

相关声明：[TCPC_REG_COMMAND_I2CIDLE](#a67fe1eeebc7c7122962b4dca16cc439c)。

I2C 空闲（I2C Idle）的取值。

<a id="r_a00691b19ec98b60c978dff404a74212a"></a>

```c
#define TCPC_REG_DEV_CAP_1 0x24
```

相关声明：[TCPC_REG_DEV_CAP_1](#a00691b19ec98b60c978dff404a74212a)。

寄存器地址：设备能力 1（Device Capabilities 1）。

<a id="r_a8667c944a8d23be51e04fc8f3f926eb2"></a>

```c
#define TCPC_REG_DEV_CAP_1_VBUS_NONDEFAULT_TARGET BIT(15)
```

相关声明：[TCPC_REG_DEV_CAP_1_VBUS_NONDEFAULT_TARGET](#a8667c944a8d23be51e04fc8f3f926eb2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 高电压目标位（High Voltage Target Bit）：置位表示实现了 `VBUS_HV_TARGET` 寄存器。

<a id="r_a4c4eb416a4bade8fa2850177e5c3afb6"></a>

```c
#define TCPC_REG_DEV_CAP_1_VBUS_OCP_REPORTING BIT(14)
```

相关声明：[TCPC_REG_DEV_CAP_1_VBUS_OCP_REPORTING](#a4c4eb416a4bade8fa2850177e5c3afb6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 过流报告位（Over Current Reporting Bit）：置位表示 TCPC 会报告 VBUS 过流。

<a id="r_a27ae574cc338e3415237e45d71c1c924"></a>

```c
#define TCPC_REG_DEV_CAP_1_VBUS_OVP_REPORTING BIT(13)
```

相关声明：[TCPC_REG_DEV_CAP_1_VBUS_OVP_REPORTING](#a27ae574cc338e3415237e45d71c1c924)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 过压报告位（Over Voltage Reporting Bit）：置位表示 TCPC 会报告 VBUS 过压。

<a id="r_a0f94cda140724bfc3dd8130b551a565f"></a>

```c
#define TCPC_REG_DEV_CAP_1_BLEED_DISCHARGE BIT(12)
```

相关声明：[TCPC_REG_DEV_CAP_1_BLEED_DISCHARGE](#a0f94cda140724bfc3dd8130b551a565f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

泄放位（Bleed Discharge Bit）：置位表示 TCPC 实现了泄放功能。

<a id="r_a6082284d3bbe7a6be544bcd2d0287aa1"></a>

```c
#define TCPC_REG_DEV_CAP_1_FORCE_DISCHARGE BIT(11)
```

相关声明：[TCPC_REG_DEV_CAP_1_FORCE_DISCHARGE](#a6082284d3bbe7a6be544bcd2d0287aa1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

强制放电位（Force Discharge Bit）：置位表示 TCPC 实现了强制放电功能。

<a id="r_ae89327b3f5836ea2b78ca46da70648e1"></a>

```c
#define TCPC_REG_DEV_CAP_1_VBUS_MEASURE_ALARM_CAPABLE BIT(10)
```

相关声明：[TCPC_REG_DEV_CAP_1_VBUS_MEASURE_ALARM_CAPABLE](#ae89327b3f5836ea2b78ca46da70648e1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 测量与报警能力位（Measurement and Alarm Capable Bit）：置位表示 TCPC 支持 VBUS 电压测量和电压报警。

<a id="r_a6e35508726be479f714c06a966fbc037"></a>

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_MASK GENMASK(9, 8)
```

相关声明：[TCPC_REG_DEV_CAP_1_SRC_RESISTOR_MASK](#a6e35508726be479f714c06a966fbc037)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的供电端电阻（Source Resistor）掩码。

<a id="r_a5708c01c881915568e290883e75c54c7"></a>

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR(reg)
```

相关声明：[TCPC_REG_DEV_CAP_1_SRC_RESISTOR](#a5708c01c881915568e290883e75c54c7)。

从寄存器值提取支持的供电端电阻（Source Resistors）的宏。该值可转换为 `enum tc_rp_value`，并视为支持的最高电流，因为 TCPC 也必须支持低于所指明值的电流。

<a id="r_a8017cae27a532a024f4b0cc2e7460ee8"></a>

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_DEF 0
```

相关声明：[TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_DEF](#a8017cae27a532a024f4b0cc2e7460ee8)。

仅支持默认上拉电阻 Rp 的取值：仅支持默认电流（Default Amperage）。

<a id="r_a08e2b60401b597d18fbbba6055cf517b"></a>

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_1P5_DEF 1
```

相关声明：[TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_1P5_DEF](#a08e2b60401b597d18fbbba6055cf517b)。

支持 Rp 1.5 A 和默认值的取值：支持 1.5 A 及默认电流（Default Amperage）。

<a id="r_a5880ca6a13c0dbc91662bd69c88f0639"></a>

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_3P0_1P5_DEF 2
```

相关声明：[TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_3P0_1P5_DEF](#a5880ca6a13c0dbc91662bd69c88f0639)。

支持 Rp 3.0 A、1.5 A 和默认值的取值：支持 3.0 A、1.5 A 及默认电流（Default Amperage）。

<a id="r_a91fa27df2ff4b97d131a3ff527cb858d"></a>

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_MASK GENMASK(7, 5)
```

相关声明：[TCPC_REG_DEV_CAP_1_POWER_ROLE_MASK](#a91fa27df2ff4b97d131a3ff527cb858d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的电源角色（Power Roles）掩码。

<a id="r_a2f35341243247196d40a11c1d6eb6037"></a>

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE(reg)
```

相关声明：[TCPC_REG_DEV_CAP_1_POWER_ROLE](#a2f35341243247196d40a11c1d6eb6037)。

从寄存器值提取支持的电源角色（Power Roles）的宏。

<a id="r_a272000f098361874b3cb86cbd7de41dd"></a>

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_OR_SNK 0
```

相关声明：[TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_OR_SNK](#a272000f098361874b3cb86cbd7de41dd)。

仅支持供电端（Source）和受电端（Sink），不支持 DRP 的取值。

<a id="r_a7e9426dc5927bc1d2d53a781596da99e"></a>

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC 1
```

相关声明：[TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC](#a7e9426dc5927bc1d2d53a781596da99e)。

仅支持供电端角色（Source Role）的取值。

<a id="r_a998f3394a685ba820f2802b7529528cf"></a>

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK 2
```

相关声明：[TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK](#a998f3394a685ba820f2802b7529528cf)。

仅支持受电端角色（Sink Role）的取值。

<a id="r_a42250c86e766f229d0e14dfccb936db7"></a>

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK_ACC 3
```

相关声明：[TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK_ACC](#a42250c86e766f229d0e14dfccb936db7)。

支持带附件的受电端角色（Sink Role with Accessory）的取值。

<a id="r_a4cedffa0db9de5fcf8a92534e0748235"></a>

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_DRP 4
```

相关声明：[TCPC_REG_DEV_CAP_1_POWER_ROLE_DRP](#a4cedffa0db9de5fcf8a92534e0748235)。

仅支持双角色端口（Dual-role Port）的取值。

<a id="r_a30418010623a871073b43d62ff16c4ee"></a>

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP_ADPT_CBL 5
```

相关声明：[TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP_ADPT_CBL](#a30418010623a871073b43d62ff16c4ee)。

支持供电端（Source）、受电端（Sink）、双角色端口（DRP）、适配器和线缆的取值。

<a id="r_a09faddef371f701a7f68e0c0b21393f7"></a>

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP 6
```

相关声明：[TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP](#a09faddef371f701a7f68e0c0b21393f7)。

支持供电端（Source）、受电端（Sink）和双角色端口（DRP）的取值。

<a id="r_a7e287e8639f0b1202d026dfb6427f791"></a>

```c
#define TCPC_REG_DEV_CAP_1_ALL_SOP_STAR_MSGS_SUPPORTED BIT(4)
```

相关声明：[TCPC_REG_DEV_CAP_1_ALL_SOP_STAR_MSGS_SUPPORTED](#a7e287e8639f0b1202d026dfb6427f791)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

调试 SOP' 和 SOP'' 支持位：置位表示支持所有 SOP* 消息（Messages）。

<a id="r_ae431e2003df86a293a89903bc61c42f3"></a>

```c
#define TCPC_REG_DEV_CAP_1_SOURCE_VCONN BIT(3)
```

相关声明：[TCPC_REG_DEV_CAP_1_SOURCE_VCONN](#ae431e2003df86a293a89903bc61c42f3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VCONN 供电位（Source VCONN Bit）：置位表示 TCPC 能切换 VCONN 电源源端。

<a id="r_a2f2f04c109419755124706bea85ca081"></a>

```c
#define TCPC_REG_DEV_CAP_1_SINK_VBUS BIT(2)
```

相关声明：[TCPC_REG_DEV_CAP_1_SINK_VBUS](#a2f2f04c109419755124706bea85ca081)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 受电位（Sink VBUS Bit）：置位表示 TCPC 能控制通向系统负载的受电路径。

<a id="r_aed48d1d1c64f94474fe5cbefc038b47f"></a>

```c
#define TCPC_REG_DEV_CAP_1_SOURCE_HV_VBUS BIT(1)
```

相关声明：[TCPC_REG_DEV_CAP_1_SOURCE_HV_VBUS](#aed48d1d1c64f94474fe5cbefc038b47f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 高电压供电位（Source High Voltage VBUS Bit）。

<a id="r_a4f80cc39de4afd8335d4e64d908243d4"></a>

```c
#define TCPC_REG_DEV_CAP_1_SOURCE_VBUS BIT(0)
```

相关声明：[TCPC_REG_DEV_CAP_1_SOURCE_VBUS](#a4f80cc39de4afd8335d4e64d908243d4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 供电位（Source VBUS Bit）：置位表示 TCPC 能控制通向 VBUS 的供电路径。

<a id="r_abeda1c146b7925452008f5a15ab400e1"></a>

```c
#define TCPC_REG_DEV_CAP_2 0x26
```

相关声明：[TCPC_REG_DEV_CAP_2](#abeda1c146b7925452008f5a15ab400e1)。

寄存器地址：设备能力 2（Device Capabilities 2）。

<a id="r_acfee304aa760748457b6d03327d47de5"></a>

```c
#define TCPC_REG_DEV_CAP_2_CAP_3_SUPPORTED BIT(15)
```

相关声明：[TCPC_REG_DEV_CAP_2_CAP_3_SUPPORTED](#acfee304aa760748457b6d03327d47de5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设备能力 3 支持位（Device Capabilities 3 Support Bit）。

<a id="r_a67056e144e2f02d5942919224d3ab3a8"></a>

```c
#define TCPC_REG_DEV_CAP_2_MSG_DISABLE_DISCONNECT BIT(14)
```

相关声明：[TCPC_REG_DEV_CAP_2_MSG_DISABLE_DISCONNECT](#a67056e144e2f02d5942919224d3ab3a8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

断开时禁用消息位（Message Disable Disconnect Bit）。

<a id="r_a0c7dbd9516f088cd99d7deb1e5ad3556"></a>

```c
#define TCPC_REG_DEV_CAP_2_GENERIC_TIMER BIT(13)
```

相关声明：[TCPC_REG_DEV_CAP_2_GENERIC_TIMER](#a0c7dbd9516f088cd99d7deb1e5ad3556)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

通用定时器支持位（Generic Timer Support Bit）。

<a id="r_a6ea7c4ca877ad8a676161ca17e254f69"></a>

```c
#define TCPC_REG_DEV_CAP_2_LONG_MSG BIT(12)
```

相关声明：[TCPC_REG_DEV_CAP_2_LONG_MSG](#a6ea7c4ca877ad8a676161ca17e254f69)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

长消息支持位（Long Message Support Bit）：置位表示 TCPC 支持最多 264 字节的 SOP* 内容。

<a id="r_a988dce0730130679ba91651723d0dbc6"></a>

```c
#define TCPC_REG_DEV_CAP_2_SMBUS_PEC BIT(11)
```

相关声明：[TCPC_REG_DEV_CAP_2_SMBUS_PEC](#a988dce0730130679ba91651723d0dbc6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

SMBus 数据包错误码（PEC）支持位。

<a id="r_ac85f10d7f799a47f989d7c1dd4003d68"></a>

```c
#define TCPC_REG_DEV_CAP_2_SRC_FRS BIT(10)
```

相关声明：[TCPC_REG_DEV_CAP_2_SRC_FRS](#ac85f10d7f799a47f989d7c1dd4003d68)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

供电端快速角色交换支持位（Source Fast-role Swap Support Bit）。

<a id="r_a5bb59a68b7477c492ee47d36d1781b5f"></a>

```c
#define TCPC_REG_DEV_CAP_2_SNK_FRS BIT(9)
```

相关声明：[TCPC_REG_DEV_CAP_2_SNK_FRS](#a5bb59a68b7477c492ee47d36d1781b5f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

受电端快速角色交换支持位（Sink Fast-role Swap Support Bit）。

<a id="r_af548c81855e291167dbe52ac55b0fafb"></a>

```c
#define TCPC_REG_DEV_CAP_2_WATCHDOG_TIMER BIT(8)
```

相关声明：[TCPC_REG_DEV_CAP_2_WATCHDOG_TIMER](#af548c81855e291167dbe52ac55b0fafb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

看门狗定时器支持位（Watchdog Timer Support Bit）。

<a id="r_ac68a1e9c17cf5d2f146b190de46b2c3c"></a>

```c
#define TCPC_REG_DEV_CAP_2_SNK_DISC_DET BIT(7)
```

相关声明：[TCPC_REG_DEV_CAP_2_SNK_DISC_DET](#ac68a1e9c17cf5d2f146b190de46b2c3c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

受电端断开检测位（Sink Disconnect Detection Bit）。

<a id="r_a57520436e70eff9f4aaabcd39da5d97a"></a>

```c
#define TCPC_REG_DEV_CAP_2_STOP_DISCHARGE_THRESH BIT(6)
```

相关声明：[TCPC_REG_DEV_CAP_2_STOP_DISCHARGE_THRESH](#a57520436e70eff9f4aaabcd39da5d97a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

停止放电阈值位（Stop Discharge Threshold Bit）。

<a id="r_adfb8168078feb6b3243f1b3ac4b243ec"></a>

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_MASK GENMASK(5, 4)
```

相关声明：[TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_MASK](#adfb8168078feb6b3243f1b3ac4b243ec)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

电压报警分辨率（Voltage Alarm Resolution）的掩码。

<a id="r_a25f9b986e9f1da7905354b04d05c0cff"></a>

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM(reg)
```

相关声明：[TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM](#a25f9b986e9f1da7905354b04d05c0cff)。

从寄存器值提取电压报警分辨率（Voltage Alarm Resolution）的宏。

<a id="r_a5b6d8055526944064b22ea69c7338190"></a>

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_25MV 0
```

相关声明：[TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_25MV](#a5b6d8055526944064b22ea69c7338190)。

电压报警分辨率（Voltage Alarm Resolution）为 25 mV 的取值，使用电压报警寄存器的全部 10 位。

<a id="r_a25e31dd4f20c71921d3c1ab85d1fdbe6"></a>

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_50MV 1
```

相关声明：[TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_50MV](#a25e31dd4f20c71921d3c1ab85d1fdbe6)。

电压报警分辨率（Voltage Alarm Resolution）为 50 mV 的取值，仅使用电压报警寄存器的 9 位。

<a id="r_ab8b4a38996973aad7c21002e15eeedf1"></a>

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_100MV 2
```

相关声明：[TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_100MV](#ab8b4a38996973aad7c21002e15eeedf1)。

电压报警分辨率（Voltage Alarm Resolution）为 100 mV 的取值，仅使用电压报警寄存器的 8 位。

<a id="r_ad2f45b2a55372cb8c2bb698427f2de6d"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_MASK GENMASK(3, 1)
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_MASK](#ad2f45b2a55372cb8c2bb698427f2de6d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 VCONN 功率（VCONN Power Supported）掩码。

<a id="r_a50ab19de9b52847f952935fdf56f0230"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED(reg)
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED](#a50ab19de9b52847f952935fdf56f0230)。

从寄存器值提取支持的 VCONN 功率（VCONN Power Supported）的宏。

<a id="r_a3287b109c18741eae5324ce7f1ca7097"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_0W 0
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_0W](#a3287b109c18741eae5324ce7f1ca7097)。

支持 1.0 W VCONN 功率（Power）的取值。

<a id="r_a874aa9f62f1cb3191acbd318388cdc7d"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_5W 1
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_5W](#a874aa9f62f1cb3191acbd318388cdc7d)。

支持 1.5 W VCONN 功率（Power）的取值。

<a id="r_a742885690791bbde37b403daf91b60fd"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_2_0W 2
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_2_0W](#a742885690791bbde37b403daf91b60fd)。

支持 2.0 W VCONN 功率（Power）的取值。

<a id="r_ac241b239949f72fefb5f205c51862f7b"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_3_0W 3
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_3_0W](#ac241b239949f72fefb5f205c51862f7b)。

支持 3.0 W VCONN 功率（Power）的取值。

<a id="r_aee172bee77d1ec775fb1a80efeb69f43"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_4_0W 4
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_4_0W](#aee172bee77d1ec775fb1a80efeb69f43)。

支持 4.0 W VCONN 功率（Power）的取值。

<a id="r_a68704f30d8d0b09c24191d5f017532e7"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_5_0W 5
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_5_0W](#a68704f30d8d0b09c24191d5f017532e7)。

支持 5.0 W VCONN 功率（Power）的取值。

<a id="r_a1036cd426cb10f4d0984cf0967d0c530"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_6_0W 6
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_6_0W](#a1036cd426cb10f4d0984cf0967d0c530)。

支持 6.0 W VCONN 功率（Power）的取值。

<a id="r_a0b3fad2c934a4a2457d7a06401698503"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_EXTERNAL 7
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_EXTERNAL](#a0b3fad2c934a4a2457d7a06401698503)。

支持外部 VCONN 电源（External VCONN Power）的取值。

<a id="r_a93469c1c4c3e71457264cf8d47cd7833"></a>

```c
#define TCPC_REG_DEV_CAP_2_VCONN_OVC_FAULT BIT(0)
```

相关声明：[TCPC_REG_DEV_CAP_2_VCONN_OVC_FAULT](#a93469c1c4c3e71457264cf8d47cd7833)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VCONN 过流故障检测能力位（Overcurrent Fault Capable Bit）：置位表示 TCPC 能检测 VCONN 过流。

<a id="r_aa694b54fb0753fae36be1650d69d23fd"></a>

```c
#define TCPC_REG_STD_INPUT_CAP 0x28
```

相关声明：[TCPC_REG_STD_INPUT_CAP](#aa694b54fb0753fae36be1650d69d23fd)。

寄存器地址：标准输入能力（Standard Input Capabilities）。

<a id="r_a488f8de2a651ede27ae4f2decc66fdfe"></a>

```c
#define TCPC_REG_STD_INPUT_CAP_SRC_FRS_MASK GENMASK(4, 3)
```

相关声明：[TCPC_REG_STD_INPUT_CAP_SRC_FRS_MASK](#a488f8de2a651ede27ae4f2decc66fdfe)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

供电端快速角色交换（Source Fast Role Swap）的掩码。

<a id="r_a2abf1d902a911882e767e777d11faa9a"></a>

```c
#define TCPC_REG_STD_INPUT_CAP_SRC_FRS(reg)
```

相关声明：[TCPC_REG_STD_INPUT_CAP_SRC_FRS](#a2abf1d902a911882e767e777d11faa9a)。

从寄存器值提取供电端快速角色交换（Source Fast Role Swap）配置的宏。

<a id="r_a65fd3ac4a027333305b8b6162cd36c57"></a>

```c
#define TCPC_REG_STD_INTPU_CAP_SRC_FRS_NONE 0
```

相关声明：[TCPC_REG_STD_INTPU_CAP_SRC_FRS_NONE](#a65fd3ac4a027333305b8b6162cd36c57)。

TCPC 不具有供电端快速角色交换引脚（Source Fast Role Swap Pin）的取值。

<a id="r_ab7efd85994fdfaab7580d39259359c78"></a>

```c
#define TCPC_REG_STD_INTPU_CAP_SRC_FRS_INPUT 1
```

相关声明：[TCPC_REG_STD_INTPU_CAP_SRC_FRS_INPUT](#ab7efd85994fdfaab7580d39259359c78)。

TCPC 具有仅输入的供电端快速角色交换引脚（Input-only Pin）的取值。

<a id="r_a03fe81146cf0aa1f7f9398a3a7389183"></a>

```c
#define TCPC_REG_STD_INTPU_CAP_SRC_FRS_BOTH 2
```

相关声明：[TCPC_REG_STD_INTPU_CAP_SRC_FRS_BOTH](#a03fe81146cf0aa1f7f9398a3a7389183)。

TCPC 具有兼作输入和输出的供电端快速角色交换引脚（Input and Output Pin）的取值。

<a id="r_a312bedca7d20ec62efa1cd0b6a585b96"></a>

```c
#define TCPC_REG_STD_INPUT_CAP_EXT_OVP BIT(2)
```

相关声明：[TCPC_REG_STD_INPUT_CAP_EXT_OVP](#a312bedca7d20ec62efa1cd0b6a585b96)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 外部过压故障位（External Over Voltage Fault Bit）。

<a id="r_ab2d3d3d8c3701a8e040062f0bc990bc7"></a>

```c
#define TCPC_REG_STD_INPUT_CAP_EXT_OCP BIT(1)
```

相关声明：[TCPC_REG_STD_INPUT_CAP_EXT_OCP](#ab2d3d3d8c3701a8e040062f0bc990bc7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 外部过流故障位（External Over Current Fault Bit）。

<a id="r_a9674e7ce46e0b2891cb585e34660403d"></a>

```c
#define TCPC_REG_STD_INPUT_CAP_FORCE_OFF_VBUS BIT(0)
```

相关声明：[TCPC_REG_STD_INPUT_CAP_FORCE_OFF_VBUS](#a9674e7ce46e0b2891cb585e34660403d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

具有强制关闭 VBUS 功能的位（Force Off VBUS Present Bit）。

<a id="r_aee8dedd72106140fac5f74a86059aab8"></a>

```c
#define TCPC_REG_STD_OUTPUT_CAP 0x29
```

相关声明：[TCPC_REG_STD_OUTPUT_CAP](#aee8dedd72106140fac5f74a86059aab8)。

寄存器地址：标准输出能力（Standard Output Capabilities）。

<a id="r_a5802b9ce7baf28c5a5430818d0f637a5"></a>

```c
#define TCPC_REG_STD_OUTPUT_CAP_SNK_DISC_DET BIT(7)
```

相关声明：[TCPC_REG_STD_OUTPUT_CAP_SNK_DISC_DET](#a5802b9ce7baf28c5a5430818d0f637a5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 受电端断开检测指示位（Sink Disconnect Detect Indicator Bit）。

<a id="r_a50a36f30796ed51d87b64e2f2099e6eb"></a>

```c
#define TCPC_REG_STD_OUTPUT_CAP_DBG_ACCESSORY BIT(6)
```

相关声明：[TCPC_REG_STD_OUTPUT_CAP_DBG_ACCESSORY](#a50a36f30796ed51d87b64e2f2099e6eb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

调试附件指示位（Debug Accessory Indicator Bit）。

<a id="r_a57e0aee8e070c3294c5580c7d1043454"></a>

```c
#define TCPC_REG_STD_OUTPUT_CAP_VBUS_PRESENT_MON BIT(5)
```

相关声明：[TCPC_REG_STD_OUTPUT_CAP_VBUS_PRESENT_MON](#a57e0aee8e070c3294c5580c7d1043454)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

VBUS 存在监测位（Present Monitor Bit）。

<a id="r_abfa7770503e634cb7479b8ee16556045"></a>

```c
#define TCPC_REG_STD_OUTPUT_CAP_AUDIO_ACCESSORY BIT(4)
```

相关声明：[TCPC_REG_STD_OUTPUT_CAP_AUDIO_ACCESSORY](#abfa7770503e634cb7479b8ee16556045)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

音频适配器附件指示位（Audio Adapter Accessory Indicator Bit）。

<a id="r_ae3d5652cf07c2ea2a6154ef30c961892"></a>

```c
#define TCPC_REG_STD_OUTPUT_CAP_ACTIVE_CABLE BIT(3)
```

相关声明：[TCPC_REG_STD_OUTPUT_CAP_ACTIVE_CABLE](#ae3d5652cf07c2ea2a6154ef30c961892)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

有源线缆指示位（Active Cable Indicator Bit）。

<a id="r_a915aeabb332fe9a5ad97c5253121fdd8"></a>

```c
#define TCPC_REG_STD_OUTPUT_CAP_MUX_CFG_CTRL BIT(2)
```

相关声明：[TCPC_REG_STD_OUTPUT_CAP_MUX_CFG_CTRL](#a915aeabb332fe9a5ad97c5253121fdd8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

多路复用器配置控制位（Mux Configuration Control Bit）。

<a id="r_a532b8a6d0bde03f665cff5fde3a2851c"></a>

```c
#define TCPC_REG_STD_OUTPUT_CAP_CONN_PRESENT BIT(1)
```

相关声明：[TCPC_REG_STD_OUTPUT_CAP_CONN_PRESENT](#a532b8a6d0bde03f665cff5fde3a2851c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

连接存在位（Connection Present Bit）。

<a id="r_af476ab76f277de3bbf6d57b4276919b4"></a>

```c
#define TCPC_REG_STD_OUTPUT_CAP_CONN_ORIENTATION BIT(0)
```

相关声明：[TCPC_REG_STD_OUTPUT_CAP_CONN_ORIENTATION](#af476ab76f277de3bbf6d57b4276919b4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

连接器方向位（Connector Orientation Bit）。

<a id="r_a16121b97ee1e7f165d0025ecd585f427"></a>

```c
#define TCPC_REG_CONFIG_EXT_1 0x2A
```

相关声明：[TCPC_REG_CONFIG_EXT_1](#a16121b97ee1e7f165d0025ecd585f427)。

寄存器地址：扩展配置 1（Configure Extended 1）。

<a id="r_a0af59ec473fbda22621cffe478331c64"></a>

```c
#define TCPC_REG_CONFIG_EXT_1_FRS_SNK_DIR BIT(1)
```

相关声明：[TCPC_REG_CONFIG_EXT_1_FRS_SNK_DIR](#a0af59ec473fbda22621cffe478331c64)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

快速角色交换双向引脚位（FR Swap Bidirectional Pin Bit）。

<a id="r_aee3fc0666cef8ad88c585016cb31ecb0"></a>

```c
#define TCPC_REG_CONFIG_EXT_1_STD_IN_SRC_FRS BIT(0)
```

相关声明：[TCPC_REG_CONFIG_EXT_1_STD_IN_SRC_FRS](#aee3fc0666cef8ad88c585016cb31ecb0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

标准输入供电端快速角色交换位（Standard Input Source FR Swap Bit）。

<a id="r_a76c6a5c1a7d0198013973a55e1431719"></a>

```c
#define TCPC_REG_GENERIC_TIMER 0x2c
```

相关声明：[TCPC_REG_GENERIC_TIMER](#a76c6a5c1a7d0198013973a55e1431719)。

寄存器地址：通用定时器（Generic Timer）。仅在设备能力 2 寄存器中的通用定时器位被置位时可用。

<a id="r_a8e023b1f3626de6b2a437c837e3a5710"></a>

```c
#define TCPC_REG_MSG_HDR_INFO 0x2e
```

相关声明：[TCPC_REG_MSG_HDR_INFO](#a8e023b1f3626de6b2a437c837e3a5710)。

寄存器地址：消息头信息（Message Header Info）。

<a id="r_a500c924a80c45acb6b4477779385bac5"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_CABLE_PLUG BIT(4)
```

相关声明：[TCPC_REG_MSG_HDR_INFO_CABLE_PLUG](#a500c924a80c45acb6b4477779385bac5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

线缆插头位（Cable Plug Bit）。

<a id="r_af94599c39af76bd1e01df2a1930ca2c5"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE_MASK BIT(3)
```

相关声明：[TCPC_REG_MSG_HDR_INFO_DATA_ROLE_MASK](#af94599c39af76bd1e01df2a1930ca2c5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

数据角色（Data Role）掩码。

<a id="r_ab9e8965712c5f13f567d0178e73551f7"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE(reg)
```

相关声明：[TCPC_REG_MSG_HDR_INFO_DATA_ROLE](#ab9e8965712c5f13f567d0178e73551f7)。

从寄存器值提取数据角色（Data Role）的宏。

<a id="r_a4f7ea550b6d820d9b86a7afc420596a1"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE_UFP 0
```

相关声明：[TCPC_REG_MSG_HDR_INFO_DATA_ROLE_UFP](#a4f7ea550b6d820d9b86a7afc420596a1)。

数据角色设为上行端口（Upstream Facing Port，UFP）的取值。

<a id="r_ac4a04f6d7819681401d8ebac0cb25e08"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE_DFP 1
```

相关声明：[TCPC_REG_MSG_HDR_INFO_DATA_ROLE_DFP](#ac4a04f6d7819681401d8ebac0cb25e08)。

数据角色设为下行端口（Downstream Facing Port，DFP）的取值。

<a id="r_a7a41fdf846fe7f8e92ecab27d8c37783"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV_MASK GENMASK(2, 1)
```

相关声明：[TCPC_REG_MSG_HDR_INFO_PD_REV_MASK](#a7a41fdf846fe7f8e92ecab27d8c37783)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

电力传输规范修订版本（Power Delivery Specification Revision）的掩码。

<a id="r_a1f763ba2525b282767482fa57be59980"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV(reg)
```

相关声明：[TCPC_REG_MSG_HDR_INFO_PD_REV](#a1f763ba2525b282767482fa57be59980)。

从寄存器值提取电力传输规范修订版本（Power Delivery Specification Revision）的宏。

<a id="r_ae801ed8e5aafa46cdac2069ada02ecf6"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV_1_0 0
```

相关声明：[TCPC_REG_MSG_HDR_INFO_PD_REV_1_0](#ae801ed8e5aafa46cdac2069ada02ecf6)。

电力传输规范修订版本（Power Delivery Specification Revision）1.0 的取值。

<a id="r_a2838fa832bca1c90542d90a5820e1357"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV_2_0 1
```

相关声明：[TCPC_REG_MSG_HDR_INFO_PD_REV_2_0](#a2838fa832bca1c90542d90a5820e1357)。

电力传输规范修订版本（Power Delivery Specification Revision）2.0 的取值。

<a id="r_a7395930393c3447ef14db5e4487b1f4c"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV_3_0 2
```

相关声明：[TCPC_REG_MSG_HDR_INFO_PD_REV_3_0](#a7395930393c3447ef14db5e4487b1f4c)。

电力传输规范修订版本（Power Delivery Specification Revision）3.0 的取值。

<a id="r_aa2165616615d1e49b3da8e9e526409c9"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE_MASK BIT(0)
```

相关声明：[TCPC_REG_MSG_HDR_INFO_POWER_ROLE_MASK](#aa2165616615d1e49b3da8e9e526409c9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电源角色（Power Role）掩码。

<a id="r_a1f80d9e5d2af199216569abdb900d633"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE(reg)
```

相关声明：[TCPC_REG_MSG_HDR_INFO_POWER_ROLE](#a1f80d9e5d2af199216569abdb900d633)。

从寄存器值提取电源角色（Power Role）的宏。

<a id="r_aee6088ee18bec85173e4cbf551795077"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SNK 0
```

相关声明：[TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SNK](#aee6088ee18bec85173e4cbf551795077)。

电源角色设为受电端（Sink）的取值。

<a id="r_a30c5d66afbb1a9feb175f29d229ef3de"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SRC 1
```

相关声明：[TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SRC](#a30c5d66afbb1a9feb175f29d229ef3de)。

电源角色设为供电端（Source）的取值。

<a id="r_a6204b3b3f8df72131d2bd1fef0be7261"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_SET(pd_rev_type, drole, prole)
```

相关声明：[TCPC_REG_MSG_HDR_INFO_SET](#a6204b3b3f8df72131d2bd1fef0be7261)、[pd_rev_type](../api_socket_lora_topic_reference/P012_USB 电力传输（USB Power Delivery）.md#gab68c6b6e33449c5ceadfc9217dd7a700)。

使用参数中的 PD 修订版本、数据角色和电源角色设置寄存器值，并设置为非线缆插头（Non-cable Plug）的宏。

<a id="r_a288dd01f2ad8dd4785bcfbe7e8975230"></a>

```c
#define TCPC_REG_MSG_HDR_INFO_ROLES_MASK (TCPC_REG_MSG_HDR_INFO_SET(3, 1, 1))
```

相关声明：[TCPC_REG_MSG_HDR_INFO_ROLES_MASK](#a288dd01f2ad8dd4785bcfbe7e8975230)、[TCPC_REG_MSG_HDR_INFO_SET](#a6204b3b3f8df72131d2bd1fef0be7261)。

PD 修订版本（Revision）、电源角色（Power Role）和数据角色（Data Role）的掩码。

<a id="r_a5c8b27d3985859742e8fb0bbb8b91ab3"></a>

```c
#define TCPC_REG_RX_DETECT 0x2f
```

相关声明：[TCPC_REG_RX_DETECT](#a5c8b27d3985859742e8fb0bbb8b91ab3)。

寄存器地址：接收检测（Receive Detect）。

<a id="r_a5241355ce8ea7ef2e5222cfcc7ef7c14"></a>

```c
#define TCPC_REG_RX_DETECT_MSG_DISABLE_DISCONNECT BIT(7)
```

相关声明：[TCPC_REG_RX_DETECT_MSG_DISABLE_DISCONNECT](#a5241355ce8ea7ef2e5222cfcc7ef7c14)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

断开时禁用消息位（Message Disable Disconnect Bit）。

<a id="r_aaf4c0249c33ed98919164ba64f8715db"></a>

```c
#define TCPC_REG_RX_DETECT_CABLE_RST BIT(6)
```

相关声明：[TCPC_REG_RX_DETECT_CABLE_RST](#aaf4c0249c33ed98919164ba64f8715db)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

线缆复位（Cable Reset）使能位。

<a id="r_a77dc544a1fe3083f0b52cfaae8248c36"></a>

```c
#define TCPC_REG_RX_DETECT_HRST BIT(5)
```

相关声明：[TCPC_REG_RX_DETECT_HRST](#a77dc544a1fe3083f0b52cfaae8248c36)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

硬复位（Hard Reset）使能位。

<a id="r_a1f2d37d68844c10411adc5090229fa21"></a>

```c
#define TCPC_REG_RX_DETECT_SOPPP_DBG BIT(4)
```

相关声明：[TCPC_REG_RX_DETECT_SOPPP_DBG](#a1f2d37d68844c10411adc5090229fa21)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

SOP_DBG'' 消息（Message）使能位。

<a id="r_a2159c1a117c9c35c779e9852e609a54d"></a>

```c
#define TCPC_REG_RX_DETECT_SOPP_DBG BIT(3)
```

相关声明：[TCPC_REG_RX_DETECT_SOPP_DBG](#a2159c1a117c9c35c779e9852e609a54d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

SOP_DBG' 消息（Message）使能位。

<a id="r_a5326c588fffc385cf6368a5149f4ed92"></a>

```c
#define TCPC_REG_RX_DETECT_SOPPP BIT(2)
```

相关声明：[TCPC_REG_RX_DETECT_SOPPP](#a5326c588fffc385cf6368a5149f4ed92)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

SOP'' 消息（Message）使能位。

<a id="r_a2112c2d15ef5490e489bae450c690320"></a>

```c
#define TCPC_REG_RX_DETECT_SOPP BIT(1)
```

相关声明：[TCPC_REG_RX_DETECT_SOPP](#a2112c2d15ef5490e489bae450c690320)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

SOP' 消息（Message）使能位。

<a id="r_a2d25f62dcf34358d1f95c81ffcc22544"></a>

```c
#define TCPC_REG_RX_DETECT_SOP BIT(0)
```

相关声明：[TCPC_REG_RX_DETECT_SOP](#a2d25f62dcf34358d1f95c81ffcc22544)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

SOP 消息（Message）使能位。

<a id="r_abda68103a95c3f2e02c3ed538f6d7852"></a>

```c
#define TCPC_REG_RX_DETECT_SOP_HRST_MASK (TCPC_REG_RX_DETECT_SOP | TCPC_REG_RX_DETECT_HRST)
```

相关声明：[TCPC_REG_RX_DETECT_SOP_HRST_MASK](#abda68103a95c3f2e02c3ed538f6d7852)、[TCPC_REG_RX_DETECT_SOP](#a2d25f62dcf34358d1f95c81ffcc22544)、[TCPC_REG_RX_DETECT_HRST](#a77dc544a1fe3083f0b52cfaae8248c36)。

检测 SOP 消息及硬复位信号（Hard Reset Signals）的掩码。

<a id="r_a4abcaf2f1a2204e6b3f408ed5872d91d"></a>

```c
#define TCPC_REG_RX_DETECT_SOP_SOPP_SOPPP_HRST_MASK
```

相关声明：[TCPC_REG_RX_DETECT_SOP_SOPP_SOPPP_HRST_MASK](#a4abcaf2f1a2204e6b3f408ed5872d91d)。

检测 SOP、SOP'、SOP'' 消息及硬复位信号（Hard Reset Signals）的掩码。

<a id="r_a4daad9b00cbea6bc95dd71438f40cd43"></a>

```c
#define TCPC_REG_RX_BUFFER 0x30
```

相关声明：[TCPC_REG_RX_BUFFER](#a4daad9b00cbea6bc95dd71438f40cd43)。

寄存器地址：接收缓冲区（Receive Buffer），包括可读字节数、接收缓冲帧类型和接收缓冲字节。在 TCPC Rev 2.0 中，`RECEIVE_BUFFER` 由三组寄存器组成：`READABLE_BYTE_COUNT`、`RX_BUF_FRAME_TYPE` 和 `RX_BUF_BYTE_x`。

<a id="r_ac35deff33f359763004e3a7bd151e880"></a>

```c
#define TCPC_REG_TRANSMIT 0x50
```

相关声明：[TCPC_REG_TRANSMIT](#ac35deff33f359763004e3a7bd151e880)。

寄存器地址：发送（Transmit）。

<a id="r_aeefbf28250aede27a29ed6b9cfe1a36f"></a>

```c
#define TCPC_REG_TRANSMIT_SET_WITH_RETRY(retries, type)
```

相关声明：[TCPC_REG_TRANSMIT_SET_WITH_RETRY](#aeefbf28250aede27a29ed6b9cfe1a36f)。

根据消息类型（Message Type）和重试次数（Retries Count）设置发送寄存器的宏。

<a id="r_abaaca2dc2fe5e8532ff078a5f7e3b200"></a>

```c
#define TCPC_REG_TRANSMIT_SET_WITHOUT_RETRY(type)
```

相关声明：[TCPC_REG_TRANSMIT_SET_WITHOUT_RETRY](#abaaca2dc2fe5e8532ff078a5f7e3b200)。

根据消息类型（Message Type）设置发送寄存器，并禁用重试的宏。

<a id="r_abfd747a6b0791d38a84ae3128fc5a028"></a>

```c
#define TCPC_REG_TRANSMIT_TYPE_SOP 0
```

相关声明：[TCPC_REG_TRANSMIT_TYPE_SOP](#abfd747a6b0791d38a84ae3128fc5a028)。

发送 SOP 类型消息（Message）的取值。

<a id="r_af8cc6c6554a088bc6426449f8562d5db"></a>

```c
#define TCPC_REG_TRANSMIT_TYPE_SOPP 1
```

相关声明：[TCPC_REG_TRANSMIT_TYPE_SOPP](#af8cc6c6554a088bc6426449f8562d5db)。

发送 SOP' 类型消息（Message）的取值。

<a id="r_ac808ad1c100f22495c6bc270786e311c"></a>

```c
#define TCPC_REG_TRANSMIT_TYPE_SOPPP 2
```

相关声明：[TCPC_REG_TRANSMIT_TYPE_SOPPP](#ac808ad1c100f22495c6bc270786e311c)。

发送 SOP'' 类型消息（Message）的取值。

<a id="r_a45b07f17c4e9a1ab943d0756839abf3e"></a>

```c
#define TCPC_REG_TRANSMIT_TYPE_SOP_DBG_P 3
```

相关声明：[TCPC_REG_TRANSMIT_TYPE_SOP_DBG_P](#a45b07f17c4e9a1ab943d0756839abf3e)。

发送 SOP_DBG' 类型消息（Message）的取值。

<a id="r_a5a03279d861be9015cc8536dc0b40205"></a>

```c
#define TCPC_REG_TRANSMIT_TYPE_SOP_DBG_PP 4
```

相关声明：[TCPC_REG_TRANSMIT_TYPE_SOP_DBG_PP](#a5a03279d861be9015cc8536dc0b40205)。

发送 SOP_DBG'' 类型消息（Message）的取值。

<a id="r_a17cd5977a9ede551e78d3e01b6eb208b"></a>

```c
#define TCPC_REG_TRANSMIT_TYPE_HRST 5
```

相关声明：[TCPC_REG_TRANSMIT_TYPE_HRST](#a17cd5977a9ede551e78d3e01b6eb208b)。

发送硬复位信号（Hard Reset Signal）的取值。

<a id="r_aff9f4bdd730c629437f05453c70deac7"></a>

```c
#define TCPC_REG_TRANSMIT_TYPE_CABLE_RST 6
```

相关声明：[TCPC_REG_TRANSMIT_TYPE_CABLE_RST](#aff9f4bdd730c629437f05453c70deac7)。

发送线缆复位信号（Cable Reset Signal）的取值。

<a id="r_a538258b3939d8d99397786bf359d472b"></a>

```c
#define TCPC_REG_TRANSMIT_TYPE_BIST 7
```

相关声明：[TCPC_REG_TRANSMIT_TYPE_BIST](#a538258b3939d8d99397786bf359d472b)。

发送内建自测试载波模式 2（BIST Carrier Mode 2）的取值。

<a id="r_a9d51fa2448c2cf6566033611387c2d51"></a>

```c
#define TCPC_REG_TX_BUFFER 0x51
```

相关声明：[TCPC_REG_TX_BUFFER](#a9d51fa2448c2cf6566033611387c2d51)。

寄存器地址：发送缓冲区（Transmit Buffer）。在 TCPC Rev 2.0 中，`TRANSMIT_BUFFER` 保存 `I2C_WRITE_BYTE_COUNT`，以及 TCPM 最近写入 `TX_BUF_BYTE_x` 的 SOP* USB PD 消息载荷部分，包括头和／或数据字节。

<a id="r_a08350059745d7e71150f5d4321fd1983"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE 0x70
```

相关声明：[TCPC_REG_VBUS_VOLTAGE](#a08350059745d7e71150f5d4321fd1983)。

寄存器地址：VBUS 电压（Voltage）。

<a id="r_a2b433b9683e5d87faf825c739a985063"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_MEASUREMENT_MASK GENMASK(9, 0)
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_MEASUREMENT_MASK](#a2b433b9683e5d87faf825c739a985063)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

VBUS 电压测量值（Voltage Measurement）的掩码。

<a id="r_a7a4dd82c861fc09b4eb3b8bbe2c066df"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_MEASUREMENT(reg)
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_MEASUREMENT](#a7a4dd82c861fc09b4eb3b8bbe2c066df)。

从寄存器值提取 VBUS 测量值（Measurement）的宏。

<a id="r_a8a4427814137f1bcd29bcf03d38c448a"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_SCALE_FACTOR_MASK GENMASK(11, 10)
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_SCALE_FACTOR_MASK](#a8a4427814137f1bcd29bcf03d38c448a)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

比例因子（Scale Factor）的掩码。

<a id="r_a85fce4d69cb3e25360d7373d4dfe4aab"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_SCALE(reg)
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_SCALE](#a85fce4d69cb3e25360d7373d4dfe4aab)。

从寄存器值提取 VBUS 电压比例（Voltage Scale）的宏。

<a id="r_a4ef01ebd0721491e0336215b8d02f362"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_LSB 25
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_LSB](#a4ef01ebd0721491e0336215b8d02f362)。

VBUS 电压测量分辨率（Voltage Measurement Resolution）。

<a id="r_a44a388e875c298eec029c12d9d74d01d"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_VBUS(x)
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_VBUS](#a44a388e875c298eec029c12d9d74d01d)。

考虑比例因子（Scale Factor），将寄存器值转换为实际电压测量值的宏。

<a id="r_ae34235441f657c818ef76c342a0d31ce"></a>

```c
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH 0x72
```

相关声明：[TCPC_REG_VBUS_SINK_DISCONNECT_THRESH](#ae34235441f657c818ef76c342a0d31ce)。

寄存器地址：VBUS 受电端断开阈值（Sink Disconnect Threshold）。

<a id="r_a5f14456afefb9f4067c60f6b56a4fc5f"></a>

```c
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_LSB 25
```

相关声明：[TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_LSB](#a5f14456afefb9f4067c60f6b56a4fc5f)。

寄存器中存储数值的分辨率（Resolution）。

<a id="r_affabe58babbeda3d7fdf574e24fad4af"></a>

```c
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_MASK GENMASK(11, 0)
```

相关声明：[TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_MASK](#affabe58babbeda3d7fdf574e24fad4af)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

电压触发点（Voltage Trip Point）有效位的掩码。

<a id="r_af722b3898795034132d8d1a0faa9548e"></a>

```c
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_DEFAULT 0x008C /* 3.5 V */
```

相关声明：[TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_DEFAULT](#af722b3898795034132d8d1a0faa9548e)。

VBUS 受电端断开阈值（Sink Disconnect Threshold）的默认值。

<a id="r_a5fad6cf61808e3d348febefaff8e143b"></a>

```c
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH 0x74
```

相关声明：[TCPC_REG_VBUS_STOP_DISCHARGE_THRESH](#a5fad6cf61808e3d348febefaff8e143b)。

寄存器地址：VBUS 受电端断开阈值（Sink Disconnect Threshold）。

<a id="r_a5957aba93c23e722fb8387bcaa5c77f9"></a>

```c
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_LSB 25
```

相关声明：[TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_LSB](#a5957aba93c23e722fb8387bcaa5c77f9)。

寄存器中存储数值的分辨率（Resolution）。

<a id="r_a35c517353c32bb43234a5795fe458f75"></a>

```c
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_MASK GENMASK(11, 0)
```

相关声明：[TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_MASK](#a35c517353c32bb43234a5795fe458f75)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

电压触发点（Voltage Trip Point）有效位的掩码。

<a id="r_a101c1813f155407644db8e68039bc62e"></a>

```c
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_DEFAULT 0x0020 /* 0.8 V */
```

相关声明：[TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_DEFAULT](#a101c1813f155407644db8e68039bc62e)。

VBUS 停止放电阈值（Stop Discharge Threshold）的默认值。

<a id="r_ac3a3f13d1189b5ac1694dd05e8c2d15b"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG 0x76
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG](#ac3a3f13d1189b5ac1694dd05e8c2d15b)。

寄存器地址：VBUS 高电压报警（Voltage Alarm High）。

<a id="r_aa6614362ab8e07b711006efc7f6d97f5"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_LSB 25
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_LSB](#aa6614362ab8e07b711006efc7f6d97f5)。

寄存器中存储数值的分辨率（Resolution）。

<a id="r_a33b30eb4bafa65700161f6f6dd947c5a"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_MASK GENMASK(11, 0)
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_MASK](#a33b30eb4bafa65700161f6f6dd947c5a)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

电压触发点（Voltage Trip Point）有效位的掩码。

<a id="r_a64356ee1d195c91d23646e79eeb405ce"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG 0x78
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG](#a64356ee1d195c91d23646e79eeb405ce)。

寄存器地址：VBUS 低电压报警（Voltage Alarm Low）。

<a id="r_a2d8ea62d4b2e46c1f98e8a04a262a56a"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_LSB 25
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_LSB](#a2d8ea62d4b2e46c1f98e8a04a262a56a)。

寄存器中存储数值的分辨率（Resolution）。

<a id="r_a7d7b3f9e6573e608ce84a1c60e446b78"></a>

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_MASK GENMASK(11, 0)
```

相关声明：[TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_MASK](#a7d7b3f9e6573e608ce84a1c60e446b78)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

电压触发点（Voltage Trip Point）有效位的掩码。

<a id="r_a0597b5a24eb3a8104a79efa09dcc37fd"></a>

```c
#define TCPC_REG_VBUS_NONDEFAULT_TARGET 0x7a
```

相关声明：[TCPC_REG_VBUS_NONDEFAULT_TARGET](#a0597b5a24eb3a8104a79efa09dcc37fd)。

寄存器地址：VBUS 非默认目标值（Nondefault Target）。仅在设备能力 1 寄存器中的 VBUS 非默认目标位被置位时可用。

<a id="r_a28dd8cdcb9bbb5fc5a649fa409813244"></a>

```c
#define TCPC_REG_VBUS_NONDEFAULT_TARGET_LSB 20
```

相关声明：[TCPC_REG_VBUS_NONDEFAULT_TARGET_LSB](#a28dd8cdcb9bbb5fc5a649fa409813244)。

寄存器中存储数值的分辨率（Resolution）。

<a id="r_a91f18df1e7b9ff826582ec697567b055"></a>

```c
#define TCPC_REG_DEV_CAP_3 0x7c
```

相关声明：[TCPC_REG_DEV_CAP_3](#a91f18df1e7b9ff826582ec697567b055)。

寄存器地址：设备能力 3（Device Capabilities 3）。

<a id="r_ad200e3bdb166affa1cf99627e01871d6"></a>

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_MASK GENMASK(2, 0)
```

相关声明：[TCPC_REG_DEV_CAP_3_VBUS_MAX_MASK](#ad200e3bdb166affa1cf99627e01871d6)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

支持的 VBUS 电压（Voltage Support）的掩码。

<a id="r_a3608d2c0ef67b1293376d575a6c07d00"></a>

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX(reg)
```

相关声明：[TCPC_REG_DEV_CAP_3_VBUS_MAX](#a3608d2c0ef67b1293376d575a6c07d00)。

从寄存器值提取支持的 VBUS 电压（Voltage Support）的宏。

<a id="r_ab6bebb59087feefaf93172b5cd9cf10e"></a>

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_5V 0
```

相关声明：[TCPC_REG_DEV_CAP_3_VBUS_MAX_5V](#ab6bebb59087feefaf93172b5cd9cf10e)。

支持 5 V 标称电压（Nominal Voltage）的取值。

<a id="r_ac0f7dcf300e40fdaf3d8f2bd20b1ce55"></a>

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_9V 1
```

相关声明：[TCPC_REG_DEV_CAP_3_VBUS_MAX_9V](#ac0f7dcf300e40fdaf3d8f2bd20b1ce55)。

支持 9 V 标称电压（Nominal Voltage）的取值。

<a id="r_ae477e64f64647b1841f2f805b15a36be"></a>

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_15V 2
```

相关声明：[TCPC_REG_DEV_CAP_3_VBUS_MAX_15V](#ae477e64f64647b1841f2f805b15a36be)。

支持 15 V 标称电压（Nominal Voltage）的取值。

<a id="r_a30164a9fc8efd1a9a648118039c6c6c8"></a>

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_20V 3
```

相关声明：[TCPC_REG_DEV_CAP_3_VBUS_MAX_20V](#a30164a9fc8efd1a9a648118039c6c6c8)。

支持 20 V 标称电压（Nominal Voltage）的取值。

<a id="r_a8ec266376652e3cd7715caa04c91d42a"></a>

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_28V 4
```

相关声明：[TCPC_REG_DEV_CAP_3_VBUS_MAX_28V](#a8ec266376652e3cd7715caa04c91d42a)。

支持 28 V 标称电压（Nominal Voltage）的取值。

<a id="r_a476095fd742e2c25fc7ff06bf89c0799"></a>

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_36V 5
```

相关声明：[TCPC_REG_DEV_CAP_3_VBUS_MAX_36V](#a476095fd742e2c25fc7ff06bf89c0799)。

支持 36 V 标称电压（Nominal Voltage）的取值。

<a id="r_a8cb7da0661d1fdf18c6b89eb0b2825e9"></a>

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_48V 6
```

相关声明：[TCPC_REG_DEV_CAP_3_VBUS_MAX_48V](#a8cb7da0661d1fdf18c6b89eb0b2825e9)。

支持 48 V 标称电压（Nominal Voltage）的取值。

## 6.2\_详细说明（Detailed Documentation）

<a id="a2912dc3a362dd0a50388934fef0f99f4"></a>

### `TCPC_REG_ALERT`

```c
#define TCPC_REG_ALERT 0x10
```

寄存器地址（Register Address）：告警（Alert）。

<a id="a90fe3405bf387ab726dd09fd935a3dee"></a>

### `TCPC_REG_ALERT_ALERT_EXT`

```c
#define TCPC_REG_ALERT_ALERT_EXT BIT(14)
```

扩展告警位（Extended Alert Bit）。

<a id="a162d24b8d3b425c3f18dd1ed0fc73919"></a>

### `TCPC_REG_ALERT_CC_STATUS`

```c
#define TCPC_REG_ALERT_CC_STATUS BIT(0)
```

配置通道线状态告警位（CC Lines Status Alert Bit）。

<a id="a18b16eb65336476a01ecef65a60eb8cf"></a>

### `TCPC_REG_ALERT_EXT`

```c
#define TCPC_REG_ALERT_EXT 0x21
```

寄存器地址：扩展告警（Alert Extended）。

<a id="a6e5e4f39a81278645ca9045f3648d3d8"></a>

### `TCPC_REG_ALERT_EXT_MASK`

```c
#define TCPC_REG_ALERT_EXT_MASK 0x17
```

寄存器地址：扩展告警掩码（Extended Alert Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

**参阅（See Also）**：另请参见 `TCPC_REG_ALERT_EXT` 寄存器。

<a id="a226652120eb8ccb442953727e1a8faef"></a>

### `TCPC_REG_ALERT_EXT_SNK_FRS`

```c
#define TCPC_REG_ALERT_EXT_SNK_FRS BIT(0)
```

受电端快速角色交换位（Sink Fast Role Swap Bit）。

置位表示已收到快速角色交换信号（Fast Role Swap Signal）。

<a id="abfdd8a966a0922ca9b0f0b4e8d813d0d"></a>

### `TCPC_REG_ALERT_EXT_SRC_FRS`

```c
#define TCPC_REG_ALERT_EXT_SRC_FRS BIT(1)
```

供电端快速角色交换位（Source Fast Role Swap Bit）。

因标准输入为低电平而发送 FRS 信号时置位。

<a id="a2655ef7f43979b32a5df5c28982d7af6"></a>

### `TCPC_REG_ALERT_EXT_STATUS`

```c
#define TCPC_REG_ALERT_EXT_STATUS BIT(13)
```

扩展状态告警位（Extended Status Alert Bit）。

<a id="aa49f73642ef4a513ba1e585d9d515c40"></a>

### `TCPC_REG_ALERT_EXT_TIMER_EXPIRED`

```c
#define TCPC_REG_ALERT_EXT_TIMER_EXPIRED BIT(2)
```

定时器到期位（Timer Expired Bit）。

<a id="af48632dbad216d1cef4adbeb60645e2a"></a>

### `TCPC_REG_ALERT_FAULT`

```c
#define TCPC_REG_ALERT_FAULT BIT(9)
```

故障告警位（Fault Alert Bit）。

<a id="ae66b8c8732e19348b3bee4509ed97453"></a>

### `TCPC_REG_ALERT_MASK`

```c
#define TCPC_REG_ALERT_MASK 0x12
```

寄存器地址：告警掩码（Alert Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

**参阅（See Also）**：另请参见 `TCPC_REG_ALERT` 寄存器。

<a id="af773296fd7587c55cef03240f26bd07a"></a>

### `TCPC_REG_ALERT_MASK_ALL`

```c
#define TCPC_REG_ALERT_MASK_ALL 0xffff
```

覆盖所有告警位（Alert Bits）的值掩码。

<a id="a2f336fd5d5eccc008a88a40c61535a63"></a>

### `TCPC_REG_ALERT_NONE`

```c
#define TCPC_REG_ALERT_NONE 0x0000
```

用于清除告警（Clear Alert）的值。

<a id="a39dd56e219d607211c10f313cca524ad"></a>

### `TCPC_REG_ALERT_POWER_STATUS`

```c
#define TCPC_REG_ALERT_POWER_STATUS BIT(1)
```

电源状态告警位（Power Status Alert Bit）。

<a id="a0569d2eaffe745605cfe43a21d070bac"></a>

### `TCPC_REG_ALERT_RX_BEGINNING`

```c
#define TCPC_REG_ALERT_RX_BEGINNING BIT(12)
```

数据接收开始位（Beginning of Data Receive Bit）。

<a id="a7e3e12d0b0a0acfee08bdfd2cd4f849f"></a>

### `TCPC_REG_ALERT_RX_BUF_OVF`

```c
#define TCPC_REG_ALERT_RX_BUF_OVF BIT(10)
```

接收缓冲区溢出告警位（Receive Buffer Overflow Alert Bit）。

<a id="a98032350a32b76b6010c91a657e552ef"></a>

### `TCPC_REG_ALERT_RX_HARD_RST`

```c
#define TCPC_REG_ALERT_RX_HARD_RST BIT(3)
```

收到硬复位告警位（Received Hard Reset Alert Bit）。

<a id="aeecc16c85ab4e3091fdb000474f73ecd"></a>

### `TCPC_REG_ALERT_RX_STATUS`

```c
#define TCPC_REG_ALERT_RX_STATUS BIT(2)
```

已收到数据告警位（Data Received Alert Bit）。

<a id="a3f4f765c1fe2e7a4b75827e5a381f053"></a>

### `TCPC_REG_ALERT_TX_COMPLETE`

```c
#define TCPC_REG_ALERT_TX_COMPLETE (TCPC_REG_ALERT_TX_SUCCESS | TCPC_REG_ALERT_TX_DISCARDED | TCPC_REG_ALERT_TX_FAILED)
```

任意传输状态告警（Transmission Status Alert）对应的位集合。

<a id="aebf0469fd43f152c6269df4fe53bca07"></a>

### `TCPC_REG_ALERT_TX_DISCARDED`

```c
#define TCPC_REG_ALERT_TX_DISCARDED BIT(5)
```

传输丢弃告警位（Transmission Discard Alert Bit）。

<a id="a0ee35769b5e6770ef1b20eb2d8cfd830"></a>

### `TCPC_REG_ALERT_TX_FAILED`

```c
#define TCPC_REG_ALERT_TX_FAILED BIT(4)
```

传输失败告警位（Transmission Fail Alert Bit）。

<a id="a796239522f17dca1a1980e22361806bb"></a>

### `TCPC_REG_ALERT_TX_SUCCESS`

```c
#define TCPC_REG_ALERT_TX_SUCCESS BIT(6)
```

传输成功位（Transmission Success Bit）。

<a id="a99145be67b60b4b1600b634933612fc7"></a>

### `TCPC_REG_ALERT_V_ALARM_HI`

```c
#define TCPC_REG_ALERT_V_ALARM_HI BIT(7)
```

VBUS 高电压报警位（High VBUS Alarm Bit）。

<a id="a512d3df7520be440e2b34455ae1953e1"></a>

### `TCPC_REG_ALERT_V_ALARM_LO`

```c
#define TCPC_REG_ALERT_V_ALARM_LO BIT(8)
```

VBUS 低电压报警位（Low VBUS Alarm Bit）。

<a id="afe588ff7743a0eeafa5cada02777eb0a"></a>

### `TCPC_REG_ALERT_VBUS_DISCNCT`

```c
#define TCPC_REG_ALERT_VBUS_DISCNCT BIT(11)
```

VBUS 断开连接告警位（Disconnection Alert Bit）。

<a id="adfbf14335108bfcdd44dd530318e58c3"></a>

### `TCPC_REG_ALERT_VENDOR_DEF`

```c
#define TCPC_REG_ALERT_VENDOR_DEF BIT(15)
```

厂商定义告警位（Vendor Defined Alert Bit）。

<a id="a2448e8e0bba63c1dece60361515f8393"></a>

### `TCPC_REG_BCD_DEV`

```c
#define TCPC_REG_BCD_DEV 0x4
```

寄存器地址（Register Address）：TCPC 版本（Version）。

<a id="a46c5b1be60f4ed058f81df1e0aa391d6"></a>

### `TCPC_REG_CC_STATUS`

```c
#define TCPC_REG_CC_STATUS 0x1d
```

寄存器地址：配置通道线状态（CC Lines Status）。

<a id="a060f5130c6102e46628117cf468d0a9f"></a>

### `TCPC_REG_CC_STATUS_CC1_STATE`

```c
#define TCPC_REG_CC_STATUS_CC1_STATE ( reg)
```

展开值（Value）：

```c
((reg) & TCPC_REG_CC_STATUS_CC1_STATE_MASK)
```

提取 CC1 线路状态值（Status Value）的宏。

参见 CC2 宏的相关说明。

<a id="a754af0239b587e79932f58a172c24dd3"></a>

### `TCPC_REG_CC_STATUS_CC1_STATE_MASK`

```c
#define TCPC_REG_CC_STATUS_CC1_STATE_MASK GENMASK(1, 0)
```

CC1 线路状态（Line State）的掩码。

<a id="a9dec41c0e03ce148f2a7d3281ebeb722"></a>

### `TCPC_REG_CC_STATUS_CC2_STATE`

```c
#define TCPC_REG_CC_STATUS_CC2_STATE ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_CC_STATUS_CC2_STATE_MASK) >> 2)
```

提取 CC2 线路状态值（Status Value）的宏。

此值的解释取决于角色控制寄存器（Role Control Register）中的 CC2 配置值，以及本寄存器中的连接结果（Connect Result）。具体解释参见 TCPCI 规范中的 CC_STATUS 寄存器定义。

<a id="a24e24cd118532bd78b8c82e5bf896820"></a>

### `TCPC_REG_CC_STATUS_CC2_STATE_MASK`

```c
#define TCPC_REG_CC_STATUS_CC2_STATE_MASK GENMASK(3, 2)
```

CC2 线路状态（Line State）的掩码。

<a id="a23c8b7998f4431a3a511f888e67a4922"></a>

### `TCPC_REG_CC_STATUS_CONNECT_RESULT`

```c
#define TCPC_REG_CC_STATUS_CONNECT_RESULT BIT(4)
```

连接结果位（Connection Result Bit）：呈现下拉电阻 Rd 时置位，呈现上拉电阻 Rp 时清零。

<a id="aa4a7868d1503a45f8fbc1cf599b64381"></a>

### `TCPC_REG_CC_STATUS_LOOK4CONNECTION`

```c
#define TCPC_REG_CC_STATUS_LOOK4CONNECTION BIT(5)
```

TCPC 主动查找连接（Looking for Connection）的位，适用于双角色端口（DRP）及仅受电端／供电端模式。

<a id="a786e23ebac906747f484f7395b5f8815"></a>

### `TCPC_REG_COMMAND`

```c
#define TCPC_REG_COMMAND 0x23
```

寄存器地址：命令（Command）。

<a id="aeab573fd25108d577e79efc75a618f00"></a>

### `TCPC_REG_COMMAND_DISABLE_VBUS_DETECT`

```c
#define TCPC_REG_COMMAND_DISABLE_VBUS_DETECT 0x22
```

禁用 VBUS 检测命令（Disable VBUS Detect）的取值：禁用 VBUS 存在检测及 vSafe0V 检测。

<a id="a601725f09f99ac7f8c015ba6259b6308"></a>

### `TCPC_REG_COMMAND_ENABLE_VBUS_DETECT`

```c
#define TCPC_REG_COMMAND_ENABLE_VBUS_DETECT 0x33
```

使能 VBUS 检测命令（Enable VBUS Detect）的取值：使能 VBUS 存在检测及 vSafe0V 检测。

<a id="a67fe1eeebc7c7122962b4dca16cc439c"></a>

### `TCPC_REG_COMMAND_I2CIDLE`

```c
#define TCPC_REG_COMMAND_I2CIDLE 0xFF
```

I2C 空闲（I2C Idle）的取值。

<a id="aeb18bda1323ff68fcb4496daa54e6c8d"></a>

### `TCPC_REG_COMMAND_LOOK4CONNECTION`

```c
#define TCPC_REG_COMMAND_LOOK4CONNECTION 0x99
```

查找连接（Look for Connection）的取值：如果角色设为 DRP，则启动双角色切换（DRP Toggling）。

<a id="aac0e53143c26efe41d4228af32216ea3"></a>

### `TCPC_REG_COMMAND_RESET_RECEIVE_BUF`

```c
#define TCPC_REG_COMMAND_RESET_RECEIVE_BUF 0xEE
```

复位接收缓冲区（Reset Receive Buffer）的取值：缓冲区指针小于等于 132 时复位到 1，否则复位到 133。

<a id="a925b93707097ee2f35c989dd5647ae72"></a>

### `TCPC_REG_COMMAND_RESET_TRANSMIT_BUF`

```c
#define TCPC_REG_COMMAND_RESET_TRANSMIT_BUF 0xDD
```

复位发送缓冲区（Reset Transmit Buffer）的取值：TCPC 将发送缓冲区指针复位到偏移量 1。

<a id="a16b98dda32a66062fc615af01b78d1b7"></a>

### `TCPC_REG_COMMAND_RX_ONE_MORE`

```c
#define TCPC_REG_COMMAND_RX_ONE_MORE 0xAA
```

再接收一次（RX One More）的取值：配置接收器，使其在发送下一个 `GoodCRC` 后自动清除 `receive_detect` 寄存器。

<a id="ac5360c2d8c9b562012e8c4981f44a39b"></a>

### `TCPC_REG_COMMAND_SEND_FRS_SIGNAL`

```c
#define TCPC_REG_COMMAND_SEND_FRS_SIGNAL 0xCC
```

发送快速角色交换信号（Fast Role Swap Signal）的取值：TCPC 为供电端（Source）且电源控制寄存器已使能 FRS 时，发送 FRS。

<a id="ab978fbd78be69065e60a41501ee688a8"></a>

### `TCPC_REG_COMMAND_SNK_CTRL_HIGH`

```c
#define TCPC_REG_COMMAND_SNK_CTRL_HIGH 0x55
```

使能 VBUS 受电（Sink VBUS）的取值：使能从 VBUS 接收电力及 VBUS 存在检测。

<a id="aa452968b9e6c1d0716e5f65bc99da707"></a>

### `TCPC_REG_COMMAND_SNK_CTRL_LOW`

```c
#define TCPC_REG_COMMAND_SNK_CTRL_LOW 0x44
```

禁用 VBUS 受电（Disable Sink VBUS）的取值：禁用从 VBUS 接收电力。

<a id="ad2b892f6896c62fa8762fab51449e61f"></a>

### `TCPC_REG_COMMAND_SRC_CTRL_DEF`

```c
#define TCPC_REG_COMMAND_SRC_CTRL_DEF 0x77
```

VBUS 默认电压供电（Source VBUS Default Voltage）的取值：使能在 VBUS 上提供 vSafe5V。

<a id="ada9b44953e5d7e4058f5d81fd7d6859b"></a>

### `TCPC_REG_COMMAND_SRC_CTRL_HV`

```c
#define TCPC_REG_COMMAND_SRC_CTRL_HV 0x88
```

VBUS 高电压供电（Source VBUS High Voltage）的取值：使能在 VBUS 上提供高电压。

<a id="a4abac8ab83a504d5abde30d23916dc67"></a>

### `TCPC_REG_COMMAND_SRC_CTRL_LOW`

```c
#define TCPC_REG_COMMAND_SRC_CTRL_LOW 0x66
```

禁用 VBUS 供电（Disable Source VBUS）的取值：禁用通过 VBUS 提供电力。

<a id="abca86d8ca8afaa0372a28de4b6f38598"></a>

### `TCPC_REG_COMMAND_WAKE_I2C`

```c
#define TCPC_REG_COMMAND_WAKE_I2C 0x11
```

唤醒 I2C 命令（Wake I2C Command）的取值。

<a id="a16121b97ee1e7f165d0025ecd585f427"></a>

### `TCPC_REG_CONFIG_EXT_1`

```c
#define TCPC_REG_CONFIG_EXT_1 0x2A
```

寄存器地址：扩展配置 1（Configure Extended 1）。

<a id="a0af59ec473fbda22621cffe478331c64"></a>

### `TCPC_REG_CONFIG_EXT_1_FRS_SNK_DIR`

```c
#define TCPC_REG_CONFIG_EXT_1_FRS_SNK_DIR BIT(1)
```

快速角色交换双向引脚位（FR Swap Bidirectional Pin Bit）。

置位时，双向快速角色交换引脚（Bidirectional FR Swap Pin）配置为标准输出信号；清零时，配置为标准输入信号。

<a id="aee3fc0666cef8ad88c585016cb31ecb0"></a>

### `TCPC_REG_CONFIG_EXT_1_STD_IN_SRC_FRS`

```c
#define TCPC_REG_CONFIG_EXT_1_STD_IN_SRC_FRS BIT(0)
```

标准输入供电端快速角色交换位（Standard Input Source FR Swap Bit）。

置位时，阻止供电端快速角色交换输入信号触发快速角色交换信号（Fast Role Swap Signal）的发送；清零时，允许该输入信号触发发送。

<a id="af0974e48cbc9c96c61bb9d7b5c81c1f2"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT 0x18
```

寄存器地址：标准输出配置（Configure Standard Output）。

<a id="a8f91eacfa5f50bdf8d4e187967c34686"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_ACTIVE_CABLE`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_ACTIVE_CABLE BIT(4)
```

有源线缆位（Active Cable Bit）。

<a id="a8d6fc07d7be8c4042929f45ff449381d"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_AUDIO_CONN_N`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_AUDIO_CONN_N BIT(5)
```

音频附件已连接信号位（Audio Accessory Connected#）。

<a id="a1d6ec65538daf13b8ca9b8c2257b2b0f"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_CONN_PRESENT`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_CONN_PRESENT BIT(1)
```

连接存在位（Connection Present Bit）。

<a id="a2bd794c9a986a9d573c08591e7aad86e"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_CONNECTOR_FLIPPED`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_CONNECTOR_FLIPPED BIT(0)
```

连接器方向位（Connector Orientation Bit）。

<a id="a1f8f1deec957703b32c7704cbfe63c5c"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_DBG_ACC_CONN_N`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_DBG_ACC_CONN_N BIT(6)
```

调试附件已连接信号位（Debug Accessory Connected#）。

<a id="a23f41760b310d34ff81decbec419fe59"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_HIGH_Z`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_HIGH_Z BIT(7)
```

高阻输出位（High Impedance Outputs Bit）。

<a id="af821127c6e9f29f25012aedb148f3f84"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_MUX_DP`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_DP (2 << 2)
```

多路复用器（Mux）取值：4 通道 DisplayPort 替代模式（DP Alternate Mode）。

<a id="a592a89b62ec5d9cf724a28e836cf2804"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_MUX_MASK`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_MASK (3 << 2)
```

多路复用器控制值掩码（Mux Control Value Mask）。

<a id="ae791c676d7d2e6abd9ee59acdca7ad3d"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_MUX_NONE`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_NONE (0 << 2)
```

多路复用器（Mux）取值：无连接。

<a id="a0b26b6588c8836f33b76575047afe099"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB (1 << 2)
```

多路复用器（Mux）取值：USB 3.1 已连接。

<a id="a7099c9623ef26f505c4a7d63c83a09be"></a>

### `TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB_DP`

```c
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB_DP (3 << 2)
```

多路复用器（Mux）取值：USB 3.1 加 DP 0、1 线路。

<a id="a00691b19ec98b60c978dff404a74212a"></a>

### `TCPC_REG_DEV_CAP_1`

```c
#define TCPC_REG_DEV_CAP_1 0x24
```

寄存器地址：设备能力 1（Device Capabilities 1）。

<a id="a7e287e8639f0b1202d026dfb6427f791"></a>

### `TCPC_REG_DEV_CAP_1_ALL_SOP_STAR_MSGS_SUPPORTED`

```c
#define TCPC_REG_DEV_CAP_1_ALL_SOP_STAR_MSGS_SUPPORTED BIT(4)
```

调试 SOP' 和 SOP'' 支持位：置位表示支持所有 SOP* 消息（Messages）。

<a id="a0f94cda140724bfc3dd8130b551a565f"></a>

### `TCPC_REG_DEV_CAP_1_BLEED_DISCHARGE`

```c
#define TCPC_REG_DEV_CAP_1_BLEED_DISCHARGE BIT(12)
```

泄放位（Bleed Discharge Bit）：置位表示 TCPC 实现了泄放功能。

<a id="a6082284d3bbe7a6be544bcd2d0287aa1"></a>

### `TCPC_REG_DEV_CAP_1_FORCE_DISCHARGE`

```c
#define TCPC_REG_DEV_CAP_1_FORCE_DISCHARGE BIT(11)
```

强制放电位（Force Discharge Bit）：置位表示 TCPC 实现了强制放电功能。

<a id="a2f35341243247196d40a11c1d6eb6037"></a>

### `TCPC_REG_DEV_CAP_1_POWER_ROLE`

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_DEV_CAP_1_POWER_ROLE_MASK) >> 5)
```

从寄存器值提取支持的电源角色（Power Roles）的宏。

<a id="a4cedffa0db9de5fcf8a92534e0748235"></a>

### `TCPC_REG_DEV_CAP_1_POWER_ROLE_DRP`

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_DRP 4
```

仅支持双角色端口（Dual-role Port）的取值。

<a id="a91fa27df2ff4b97d131a3ff527cb858d"></a>

### `TCPC_REG_DEV_CAP_1_POWER_ROLE_MASK`

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_MASK GENMASK(7, 5)
```

支持的电源角色（Power Roles）掩码。

<a id="a998f3394a685ba820f2802b7529528cf"></a>

### `TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK`

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK 2
```

仅支持受电端角色（Sink Role）的取值。

<a id="a42250c86e766f229d0e14dfccb936db7"></a>

### `TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK_ACC`

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK_ACC 3
```

支持带附件的受电端角色（Sink Role with Accessory）的取值。

<a id="a7e9426dc5927bc1d2d53a781596da99e"></a>

### `TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC`

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC 1
```

仅支持供电端角色（Source Role）的取值。

<a id="a272000f098361874b3cb86cbd7de41dd"></a>

### `TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_OR_SNK`

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_OR_SNK 0
```

仅支持供电端（Source）和受电端（Sink），不支持 DRP 的取值。

<a id="a09faddef371f701a7f68e0c0b21393f7"></a>

### `TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP`

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP 6
```

支持供电端（Source）、受电端（Sink）和双角色端口（DRP）的取值。

<a id="a30418010623a871073b43d62ff16c4ee"></a>

### `TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP_ADPT_CBL`

```c
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP_ADPT_CBL 5
```

支持供电端（Source）、受电端（Sink）、双角色端口（DRP）、适配器和线缆的取值。

<a id="a2f2f04c109419755124706bea85ca081"></a>

### `TCPC_REG_DEV_CAP_1_SINK_VBUS`

```c
#define TCPC_REG_DEV_CAP_1_SINK_VBUS BIT(2)
```

VBUS 受电位（Sink VBUS Bit）：置位表示 TCPC 能控制通向系统负载的受电路径。

<a id="aed48d1d1c64f94474fe5cbefc038b47f"></a>

### `TCPC_REG_DEV_CAP_1_SOURCE_HV_VBUS`

```c
#define TCPC_REG_DEV_CAP_1_SOURCE_HV_VBUS BIT(1)
```

VBUS 高电压供电位（Source High Voltage VBUS Bit）。

置位表示 TCPC 能控制通向 VBUS 的高电压供电路径（Source High Voltage Path）。

<a id="a4f80cc39de4afd8335d4e64d908243d4"></a>

### `TCPC_REG_DEV_CAP_1_SOURCE_VBUS`

```c
#define TCPC_REG_DEV_CAP_1_SOURCE_VBUS BIT(0)
```

VBUS 供电位（Source VBUS Bit）：置位表示 TCPC 能控制通向 VBUS 的供电路径。

<a id="ae431e2003df86a293a89903bc61c42f3"></a>

### `TCPC_REG_DEV_CAP_1_SOURCE_VCONN`

```c
#define TCPC_REG_DEV_CAP_1_SOURCE_VCONN BIT(3)
```

VCONN 供电位（Source VCONN Bit）：置位表示 TCPC 能切换 VCONN 电源源端。

<a id="a5708c01c881915568e290883e75c54c7"></a>

### `TCPC_REG_DEV_CAP_1_SRC_RESISTOR`

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_DEV_CAP_1_SRC_RESISTOR_MASK) >> 8)
```

从寄存器值提取支持的供电端电阻（Source Resistors）的宏。该值可转换为 `enum tc_rp_value`，并视为支持的最高电流，因为 TCPC 也必须支持低于所指明值的电流。

<a id="a6e35508726be479f714c06a966fbc037"></a>

### `TCPC_REG_DEV_CAP_1_SRC_RESISTOR_MASK`

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_MASK GENMASK(9, 8)
```

支持的供电端电阻（Source Resistor）掩码。

<a id="a08e2b60401b597d18fbbba6055cf517b"></a>

### `TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_1P5_DEF`

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_1P5_DEF 1
```

支持 Rp 1.5 A 和默认值的取值：支持 1.5 A 及默认电流（Default Amperage）。

<a id="a5880ca6a13c0dbc91662bd69c88f0639"></a>

### `TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_3P0_1P5_DEF`

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_3P0_1P5_DEF 2
```

支持 Rp 3.0 A、1.5 A 和默认值的取值：支持 3.0 A、1.5 A 及默认电流（Default Amperage）。

<a id="a8017cae27a532a024f4b0cc2e7460ee8"></a>

### `TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_DEF`

```c
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_DEF 0
```

仅支持默认上拉电阻 Rp 的取值：仅支持默认电流（Default Amperage）。

<a id="ae89327b3f5836ea2b78ca46da70648e1"></a>

### `TCPC_REG_DEV_CAP_1_VBUS_MEASURE_ALARM_CAPABLE`

```c
#define TCPC_REG_DEV_CAP_1_VBUS_MEASURE_ALARM_CAPABLE BIT(10)
```

VBUS 测量与报警能力位（Measurement and Alarm Capable Bit）：置位表示 TCPC 支持 VBUS 电压测量和电压报警。

<a id="a8667c944a8d23be51e04fc8f3f926eb2"></a>

### `TCPC_REG_DEV_CAP_1_VBUS_NONDEFAULT_TARGET`

```c
#define TCPC_REG_DEV_CAP_1_VBUS_NONDEFAULT_TARGET BIT(15)
```

VBUS 高电压目标位（High Voltage Target Bit）：置位表示实现了 `VBUS_HV_TARGET` 寄存器。

<a id="a4c4eb416a4bade8fa2850177e5c3afb6"></a>

### `TCPC_REG_DEV_CAP_1_VBUS_OCP_REPORTING`

```c
#define TCPC_REG_DEV_CAP_1_VBUS_OCP_REPORTING BIT(14)
```

VBUS 过流报告位（Over Current Reporting Bit）：置位表示 TCPC 会报告 VBUS 过流。

<a id="a27ae574cc338e3415237e45d71c1c924"></a>

### `TCPC_REG_DEV_CAP_1_VBUS_OVP_REPORTING`

```c
#define TCPC_REG_DEV_CAP_1_VBUS_OVP_REPORTING BIT(13)
```

VBUS 过压报告位（Over Voltage Reporting Bit）：置位表示 TCPC 会报告 VBUS 过压。

<a id="abeda1c146b7925452008f5a15ab400e1"></a>

### `TCPC_REG_DEV_CAP_2`

```c
#define TCPC_REG_DEV_CAP_2 0x26
```

寄存器地址：设备能力 2（Device Capabilities 2）。

<a id="acfee304aa760748457b6d03327d47de5"></a>

### `TCPC_REG_DEV_CAP_2_CAP_3_SUPPORTED`

```c
#define TCPC_REG_DEV_CAP_2_CAP_3_SUPPORTED BIT(15)
```

设备能力 3 支持位（Device Capabilities 3 Support Bit）。

<a id="a0c7dbd9516f088cd99d7deb1e5ad3556"></a>

### `TCPC_REG_DEV_CAP_2_GENERIC_TIMER`

```c
#define TCPC_REG_DEV_CAP_2_GENERIC_TIMER BIT(13)
```

通用定时器支持位（Generic Timer Support Bit）。

<a id="a6ea7c4ca877ad8a676161ca17e254f69"></a>

### `TCPC_REG_DEV_CAP_2_LONG_MSG`

```c
#define TCPC_REG_DEV_CAP_2_LONG_MSG BIT(12)
```

长消息支持位（Long Message Support Bit）：置位表示 TCPC 支持最多 264 字节的 SOP* 内容。

一次 I2C 事务最多可写入 132 字节。此位清零时，TCPC 仅支持 30 字节的 SOP* 消息内容。

<a id="a67056e144e2f02d5942919224d3ab3a8"></a>

### `TCPC_REG_DEV_CAP_2_MSG_DISABLE_DISCONNECT`

```c
#define TCPC_REG_DEV_CAP_2_MSG_DISABLE_DISCONNECT BIT(14)
```

断开时禁用消息位（Message Disable Disconnect Bit）。

<a id="a988dce0730130679ba91651723d0dbc6"></a>

### `TCPC_REG_DEV_CAP_2_SMBUS_PEC`

```c
#define TCPC_REG_DEV_CAP_2_SMBUS_PEC BIT(11)
```

SMBus 数据包错误码（PEC）支持位。

置位表示可在 TCPC 控制寄存器中使能 SMBus 数据包错误码（PEC）。

<a id="ac68a1e9c17cf5d2f146b190de46b2c3c"></a>

### `TCPC_REG_DEV_CAP_2_SNK_DISC_DET`

```c
#define TCPC_REG_DEV_CAP_2_SNK_DISC_DET BIT(7)
```

受电端断开检测位（Sink Disconnect Detection Bit）。

置位时，可设置受电端断开阈值（Sink Disconnect Threshold）；否则，使用状态寄存器中的 VBUS 存在值（Present Value）指示受电端断开。

<a id="a5bb59a68b7477c492ee47d36d1781b5f"></a>

### `TCPC_REG_DEV_CAP_2_SNK_FRS`

```c
#define TCPC_REG_DEV_CAP_2_SNK_FRS BIT(9)
```

受电端快速角色交换支持位（Sink Fast-role Swap Support Bit）。

置位表示 TCPC 能以受电端（Sink）身份发送 FRS。

<a id="ac85f10d7f799a47f989d7c1dd4003d68"></a>

### `TCPC_REG_DEV_CAP_2_SRC_FRS`

```c
#define TCPC_REG_DEV_CAP_2_SRC_FRS BIT(10)
```

供电端快速角色交换支持位（Source Fast-role Swap Support Bit）。

置位表示 TCPC 能以供电端（Source）身份发送 FRS。

<a id="a57520436e70eff9f4aaabcd39da5d97a"></a>

### `TCPC_REG_DEV_CAP_2_STOP_DISCHARGE_THRESH`

```c
#define TCPC_REG_DEV_CAP_2_STOP_DISCHARGE_THRESH BIT(6)
```

停止放电阈值位（Stop Discharge Threshold Bit）。

置位表示 TCPM 能通过 VBUS 停止放电阈值寄存器（Stop Discharge Threshold Register），设置禁用强制 VBUS 放电的电压阈值。

<a id="a25f9b986e9f1da7905354b04d05c0cff"></a>

### `TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM`

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_MASK) >> 4)
```

从寄存器值提取电压报警分辨率（Voltage Alarm Resolution）的宏。

<a id="ab8b4a38996973aad7c21002e15eeedf1"></a>

### `TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_100MV`

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_100MV 2
```

电压报警分辨率（Voltage Alarm Resolution）为 100 mV 的取值，仅使用电压报警寄存器的 8 位。

<a id="a5b6d8055526944064b22ea69c7338190"></a>

### `TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_25MV`

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_25MV 0
```

电压报警分辨率（Voltage Alarm Resolution）为 25 mV 的取值，使用电压报警寄存器的全部 10 位。

<a id="a25e31dd4f20c71921d3c1ab85d1fdbe6"></a>

### `TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_50MV`

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_50MV 1
```

电压报警分辨率（Voltage Alarm Resolution）为 50 mV 的取值，仅使用电压报警寄存器的 9 位。

<a id="adfb8168078feb6b3243f1b3ac4b243ec"></a>

### `TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_MASK`

```c
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_MASK GENMASK(5, 4)
```

电压报警分辨率（Voltage Alarm Resolution）的掩码。

<a id="a93469c1c4c3e71457264cf8d47cd7833"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_OVC_FAULT`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_OVC_FAULT BIT(0)
```

VCONN 过流故障检测能力位（Overcurrent Fault Capable Bit）：置位表示 TCPC 能检测 VCONN 过流。

<a id="a50ab19de9b52847f952935fdf56f0230"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_MASK) >> 1)
```

从寄存器值提取支持的 VCONN 功率（VCONN Power Supported）的宏。

<a id="a3287b109c18741eae5324ce7f1ca7097"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_0W`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_0W 0
```

支持 1.0 W VCONN 功率（Power）的取值。

<a id="a874aa9f62f1cb3191acbd318388cdc7d"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_5W`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_5W 1
```

支持 1.5 W VCONN 功率（Power）的取值。

<a id="a742885690791bbde37b403daf91b60fd"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_2_0W`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_2_0W 2
```

支持 2.0 W VCONN 功率（Power）的取值。

<a id="ac241b239949f72fefb5f205c51862f7b"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_3_0W`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_3_0W 3
```

支持 3.0 W VCONN 功率（Power）的取值。

<a id="aee172bee77d1ec775fb1a80efeb69f43"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_4_0W`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_4_0W 4
```

支持 4.0 W VCONN 功率（Power）的取值。

<a id="a68704f30d8d0b09c24191d5f017532e7"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_5_0W`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_5_0W 5
```

支持 5.0 W VCONN 功率（Power）的取值。

<a id="a1036cd426cb10f4d0984cf0967d0c530"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_6_0W`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_6_0W 6
```

支持 6.0 W VCONN 功率（Power）的取值。

<a id="a0b3fad2c934a4a2457d7a06401698503"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_EXTERNAL`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_EXTERNAL 7
```

支持外部 VCONN 电源（External VCONN Power）的取值。

<a id="ad2f45b2a55372cb8c2bb698427f2de6d"></a>

### `TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_MASK`

```c
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_MASK GENMASK(3, 1)
```

支持的 VCONN 功率（VCONN Power Supported）掩码。

<a id="af548c81855e291167dbe52ac55b0fafb"></a>

### `TCPC_REG_DEV_CAP_2_WATCHDOG_TIMER`

```c
#define TCPC_REG_DEV_CAP_2_WATCHDOG_TIMER BIT(8)
```

看门狗定时器支持位（Watchdog Timer Support Bit）。

置位表示可在 TCPC 控制寄存器中使能看门狗（Watchdog）。

<a id="a91f18df1e7b9ff826582ec697567b055"></a>

### `TCPC_REG_DEV_CAP_3`

```c
#define TCPC_REG_DEV_CAP_3 0x7c
```

寄存器地址：设备能力 3（Device Capabilities 3）。

<a id="a3608d2c0ef67b1293376d575a6c07d00"></a>

### `TCPC_REG_DEV_CAP_3_VBUS_MAX`

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX ( reg)
```

展开值（Value）：

```c
((reg) & TCPC_REG_DEV_CAP_3_VBUS_MAX_MASK)
```

从寄存器值提取支持的 VBUS 电压（Voltage Support）的宏。

<a id="ae477e64f64647b1841f2f805b15a36be"></a>

### `TCPC_REG_DEV_CAP_3_VBUS_MAX_15V`

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_15V 2
```

支持 15 V 标称电压（Nominal Voltage）的取值。

<a id="a30164a9fc8efd1a9a648118039c6c6c8"></a>

### `TCPC_REG_DEV_CAP_3_VBUS_MAX_20V`

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_20V 3
```

支持 20 V 标称电压（Nominal Voltage）的取值。

<a id="a8ec266376652e3cd7715caa04c91d42a"></a>

### `TCPC_REG_DEV_CAP_3_VBUS_MAX_28V`

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_28V 4
```

支持 28 V 标称电压（Nominal Voltage）的取值。

<a id="a476095fd742e2c25fc7ff06bf89c0799"></a>

### `TCPC_REG_DEV_CAP_3_VBUS_MAX_36V`

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_36V 5
```

支持 36 V 标称电压（Nominal Voltage）的取值。

<a id="a8cb7da0661d1fdf18c6b89eb0b2825e9"></a>

### `TCPC_REG_DEV_CAP_3_VBUS_MAX_48V`

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_48V 6
```

支持 48 V 标称电压（Nominal Voltage）的取值。

<a id="ab6bebb59087feefaf93172b5cd9cf10e"></a>

### `TCPC_REG_DEV_CAP_3_VBUS_MAX_5V`

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_5V 0
```

支持 5 V 标称电压（Nominal Voltage）的取值。

<a id="ac0f7dcf300e40fdaf3d8f2bd20b1ce55"></a>

### `TCPC_REG_DEV_CAP_3_VBUS_MAX_9V`

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_9V 1
```

支持 9 V 标称电压（Nominal Voltage）的取值。

<a id="ad200e3bdb166affa1cf99627e01871d6"></a>

### `TCPC_REG_DEV_CAP_3_VBUS_MAX_MASK`

```c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_MASK GENMASK(2, 0)
```

支持的 VBUS 电压（Voltage Support）的掩码。

<a id="a80738bada4f82681fb36cfc019390245"></a>

### `TCPC_REG_EXT_STATUS`

```c
#define TCPC_REG_EXT_STATUS 0x20
```

寄存器地址：扩展状态（Extended Status）。

<a id="ad8d4a179cf4ca331988d3085faabe40e"></a>

### `TCPC_REG_EXT_STATUS_MASK`

```c
#define TCPC_REG_EXT_STATUS_MASK 0x16
```

寄存器地址：扩展状态掩码（Extended Status Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

**参阅（See Also）**：另请参见 `TCPC_REG_EXT_STATUS` 寄存器。

<a id="ae266a7de13017c05be74f4163babcc95"></a>

### `TCPC_REG_EXT_STATUS_SAFE0V`

```c
#define TCPC_REG_EXT_STATUS_SAFE0V BIT(0)
```

VBUS 处于安全零电压（vSafe0V）的位。

TCPC 检测到 VBUS 低于 0.8 V 时置位。

<a id="ab820a732a55091e9cc1b2c41e555cfe0"></a>

### `TCPC_REG_FAULT_CTRL`

```c
#define TCPC_REG_FAULT_CTRL 0x1b
```

寄存器地址：故障控制（Fault Control）。

<a id="ab57a9e89d53bfd55565c8f33739390bd"></a>

### `TCPC_REG_FAULT_CTRL_VBUS_DISCHARGE_FAULT`

```c
#define TCPC_REG_FAULT_CTRL_VBUS_DISCHARGE_FAULT BIT(3)
```

禁用 VBUS 放电故障检测定时器（Discharge Fault Detection Timer）的位。

<a id="aec1969186b70dc923e6f8d9827b8a766"></a>

### `TCPC_REG_FAULT_CTRL_VBUS_FORCE_OFF`

```c
#define TCPC_REG_FAULT_CTRL_VBUS_FORCE_OFF BIT(4)
```

阻止标准输入信号强制关闭 VBUS 控制（Force Off VBUS Control）的位。

<a id="a0ae16ec1e71eaaf0c74f0c6b29ea54f8"></a>

### `TCPC_REG_FAULT_CTRL_VBUS_OCP_FAULT_DIS`

```c
#define TCPC_REG_FAULT_CTRL_VBUS_OCP_FAULT_DIS BIT(2)
```

禁用 VBUS 过流检测（Over Current Detection）的位。

<a id="ab471e71bcbef59d68aabb150e6ec7944"></a>

### `TCPC_REG_FAULT_CTRL_VBUS_OVP_FAULT_DIS`

```c
#define TCPC_REG_FAULT_CTRL_VBUS_OVP_FAULT_DIS BIT(1)
```

禁用 VBUS 过压检测（Over Voltage Detection）的位。

<a id="a9299f9bb8d4c79173a239b196f28ac4e"></a>

### `TCPC_REG_FAULT_CTRL_VCONN_OCP_FAULT_DIS`

```c
#define TCPC_REG_FAULT_CTRL_VCONN_OCP_FAULT_DIS BIT(0)
```

禁用 VCONN 过流检测（Over Current Detection）的位。

<a id="a558e8c8d1e50ef135afebaf2d65a40b5"></a>

### `TCPC_REG_FAULT_STATUS`

```c
#define TCPC_REG_FAULT_STATUS 0x1f
```

寄存器地址：故障状态（Fault Status）。

<a id="aec48a88fd81cf610ad3dac92c7ba825f"></a>

### `TCPC_REG_FAULT_STATUS_ALL_REGS_RESET`

```c
#define TCPC_REG_FAULT_STATUS_ALL_REGS_RESET BIT(7)
```

所有寄存器已复位为默认值的位（All Registers Reset to Default Bit）。

<a id="a035b4cdca5e34b16419f78f39767479b"></a>

### `TCPC_REG_FAULT_STATUS_AUTO_DISCHARGE_FAIL`

```c
#define TCPC_REG_FAULT_STATUS_AUTO_DISCHARGE_FAIL BIT(5)
```

自动放电失败位（Auto Discharge Failed Bit）。

<a id="aef11ca61ad37b817ca08816a7b9e2a2d"></a>

### `TCPC_REG_FAULT_STATUS_FORCE_DISCHARGE_FAIL`

```c
#define TCPC_REG_FAULT_STATUS_FORCE_DISCHARGE_FAIL BIT(4)
```

强制放电失败位（Force Discharge Failed Bit）。

<a id="ab140bad4bc9ca3f8bf59ef005ce5f2e2"></a>

### `TCPC_REG_FAULT_STATUS_FORCE_OFF_VBUS`

```c
#define TCPC_REG_FAULT_STATUS_FORCE_OFF_VBUS BIT(6)
```

因外部故障强制关闭 VBUS（Force VBUS Off）的位。

<a id="a78d783025aed6f6118744a443d881eb5"></a>

### `TCPC_REG_FAULT_STATUS_I2C_INTERFACE_ERR`

```c
#define TCPC_REG_FAULT_STATUS_I2C_INTERFACE_ERR BIT(0)
```

I2C 接口错误位（Interface Error Bit）。

<a id="a3a6d7e0a7641251361c8991630e6e35b"></a>

### `TCPC_REG_FAULT_STATUS_MASK`

```c
#define TCPC_REG_FAULT_STATUS_MASK 0x15
```

寄存器地址：故障状态掩码（Fault Status Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

**参阅（See Also）**：另请参见 `TCPC_REG_FAULT_STATUS` 寄存器。

<a id="a1ac9d22a9a7999da7b68d6c2edb2ca13"></a>

### `TCPC_REG_FAULT_STATUS_VBUS_OVER_CURRENT`

```c
#define TCPC_REG_FAULT_STATUS_VBUS_OVER_CURRENT BIT(3)
```

内部或外部 VBUS 过流位（Over Current Bit）。

<a id="a9032f5f3dee6830457a8fd06ff78c356"></a>

### `TCPC_REG_FAULT_STATUS_VBUS_OVER_VOLTAGE`

```c
#define TCPC_REG_FAULT_STATUS_VBUS_OVER_VOLTAGE BIT(2)
```

内部或外部 VBUS 过压位（Over Voltage Bit）。

<a id="a0dfd803a4f1a7aea8376d945df5de8d8"></a>

### `TCPC_REG_FAULT_STATUS_VCONN_OVER_CURRENT`

```c
#define TCPC_REG_FAULT_STATUS_VCONN_OVER_CURRENT BIT(1)
```

VCONN 过流位（Over Current Bit）。

<a id="a76c6a5c1a7d0198013973a55e1431719"></a>

### `TCPC_REG_GENERIC_TIMER`

```c
#define TCPC_REG_GENERIC_TIMER 0x2c
```

寄存器地址：通用定时器（Generic Timer）。仅在设备能力 2 寄存器中的通用定时器位被置位时可用。

此寄存器宽度为 16 位，分辨率（Resolution）为 0.1 ms。

<a id="a8e023b1f3626de6b2a437c837e3a5710"></a>

### `TCPC_REG_MSG_HDR_INFO`

```c
#define TCPC_REG_MSG_HDR_INFO 0x2e
```

寄存器地址：消息头信息（Message Header Info）。

<a id="a500c924a80c45acb6b4477779385bac5"></a>

### `TCPC_REG_MSG_HDR_INFO_CABLE_PLUG`

```c
#define TCPC_REG_MSG_HDR_INFO_CABLE_PLUG BIT(4)
```

线缆插头位（Cable Plug Bit）。

置位表示消息源自线缆插头（Cable Plug）。

<a id="ab9e8965712c5f13f567d0178e73551f7"></a>

### `TCPC_REG_MSG_HDR_INFO_DATA_ROLE`

```c
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_MSG_HDR_INFO_DATA_ROLE_MASK) >> 3)
```

从寄存器值提取数据角色（Data Role）的宏。

<a id="ac4a04f6d7819681401d8ebac0cb25e08"></a>

### `TCPC_REG_MSG_HDR_INFO_DATA_ROLE_DFP`

```c
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE_DFP 1
```

数据角色设为下行端口（Downstream Facing Port，DFP）的取值。

<a id="af94599c39af76bd1e01df2a1930ca2c5"></a>

### `TCPC_REG_MSG_HDR_INFO_DATA_ROLE_MASK`

```c
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE_MASK BIT(3)
```

数据角色（Data Role）掩码。

<a id="a4f7ea550b6d820d9b86a7afc420596a1"></a>

### `TCPC_REG_MSG_HDR_INFO_DATA_ROLE_UFP`

```c
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE_UFP 0
```

数据角色设为上行端口（Upstream Facing Port，UFP）的取值。

<a id="a1f763ba2525b282767482fa57be59980"></a>

### `TCPC_REG_MSG_HDR_INFO_PD_REV`

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_MSG_HDR_INFO_PD_REV_MASK) >> 1)
```

从寄存器值提取电力传输规范修订版本（Power Delivery Specification Revision）的宏。

<a id="ae801ed8e5aafa46cdac2069ada02ecf6"></a>

### `TCPC_REG_MSG_HDR_INFO_PD_REV_1_0`

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV_1_0 0
```

电力传输规范修订版本（Power Delivery Specification Revision）1.0 的取值。

<a id="a2838fa832bca1c90542d90a5820e1357"></a>

### `TCPC_REG_MSG_HDR_INFO_PD_REV_2_0`

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV_2_0 1
```

电力传输规范修订版本（Power Delivery Specification Revision）2.0 的取值。

<a id="a7395930393c3447ef14db5e4487b1f4c"></a>

### `TCPC_REG_MSG_HDR_INFO_PD_REV_3_0`

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV_3_0 2
```

电力传输规范修订版本（Power Delivery Specification Revision）3.0 的取值。

<a id="a7a41fdf846fe7f8e92ecab27d8c37783"></a>

### `TCPC_REG_MSG_HDR_INFO_PD_REV_MASK`

```c
#define TCPC_REG_MSG_HDR_INFO_PD_REV_MASK GENMASK(2, 1)
```

电力传输规范修订版本（Power Delivery Specification Revision）的掩码。

<a id="a1f80d9e5d2af199216569abdb900d633"></a>

### `TCPC_REG_MSG_HDR_INFO_POWER_ROLE`

```c
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE ( reg)
```

展开值（Value）：

```c
((reg) & TCPC_REG_MSG_HDR_INFO_POWER_ROLE_MASK)
```

从寄存器值提取电源角色（Power Role）的宏。

<a id="aa2165616615d1e49b3da8e9e526409c9"></a>

### `TCPC_REG_MSG_HDR_INFO_POWER_ROLE_MASK`

```c
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE_MASK BIT(0)
```

电源角色（Power Role）掩码。

<a id="aee6088ee18bec85173e4cbf551795077"></a>

### `TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SNK`

```c
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SNK 0
```

电源角色设为受电端（Sink）的取值。

<a id="a30c5d66afbb1a9feb175f29d229ef3de"></a>

### `TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SRC`

```c
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SRC 1
```

电源角色设为供电端（Source）的取值。

<a id="a288dd01f2ad8dd4785bcfbe7e8975230"></a>

### `TCPC_REG_MSG_HDR_INFO_ROLES_MASK`

```c
#define TCPC_REG_MSG_HDR_INFO_ROLES_MASK (TCPC_REG_MSG_HDR_INFO_SET(3, 1, 1))
```

PD 修订版本（Revision）、电源角色（Power Role）和数据角色（Data Role）的掩码。

<a id="a6204b3b3f8df72131d2bd1fef0be7261"></a>

### `TCPC_REG_MSG_HDR_INFO_SET`

```c
#define TCPC_REG_MSG_HDR_INFO_SET ( pd_rev_type, drole, prole )
```

展开值（Value）：

```c
((drole) << 3 | (pd_rev_type << 1) | (prole))
```

使用参数中的 PD 修订版本、数据角色和电源角色设置寄存器值，并设置为非线缆插头（Non-cable Plug）的宏。

<a id="a25bd2e39fa396a3c097244a14d4a53b3"></a>

### `TCPC_REG_PD_INT_REV`

```c
#define TCPC_REG_PD_INT_REV 0xa
```

寄存器地址（Register Address）：接口修订版本与版本（Revision and Version）。

<a id="acbd18c6ccab38cf4227a7f82741de5cb"></a>

### `TCPC_REG_PD_INT_REV_REV_MAJOR`

```c
#define TCPC_REG_PD_INT_REV_REV_MAJOR ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_PD_INT_REV_REV_MAJOR_MASK) >> 12)
```

提取支持的 USB 端口控制器接口修订版本（Revision）主版本部分的宏。

<a id="afd52534290a2b7d738ea73888d16419f"></a>

### `TCPC_REG_PD_INT_REV_REV_MAJOR_MASK`

```c
#define TCPC_REG_PD_INT_REV_REV_MAJOR_MASK GENMASK(15, 12)
```

支持的 USB 端口控制器接口修订版本（Revision）主版本部分的掩码。

<a id="ada1c0275ebfe2e5e558e7026531f89a6"></a>

### `TCPC_REG_PD_INT_REV_REV_MINOR`

```c
#define TCPC_REG_PD_INT_REV_REV_MINOR ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_PD_INT_REV_REV_MINOR_MASK) >> 8)
```

提取支持的 USB 端口控制器接口修订版本（Revision）次版本部分的宏。

<a id="a66e85404023d11733db1d71a1625f4e9"></a>

### `TCPC_REG_PD_INT_REV_REV_MINOR_MASK`

```c
#define TCPC_REG_PD_INT_REV_REV_MINOR_MASK GENMASK(11, 8)
```

支持的 USB 端口控制器接口修订版本（Revision）次版本部分的掩码。

<a id="a30bac3197df65667c80168e808008056"></a>

### `TCPC_REG_PD_INT_REV_VER_MAJOR`

```c
#define TCPC_REG_PD_INT_REV_VER_MAJOR ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_PD_INT_REV_VER_MAJOR_MASK) >> 4)
```

提取支持的 USB 端口控制器接口版本（Version）主版本部分的宏。

<a id="a19c752a82a935fd74d9c22be4f9c2e79"></a>

### `TCPC_REG_PD_INT_REV_VER_MAJOR_MASK`

```c
#define TCPC_REG_PD_INT_REV_VER_MAJOR_MASK GENMASK(7, 4)
```

支持的 USB 端口控制器接口版本（Version）主版本部分的掩码。

<a id="ae1f08c2a243063a390cc45ba84ee1b8b"></a>

### `TCPC_REG_PD_INT_REV_VER_MINOR`

```c
#define TCPC_REG_PD_INT_REV_VER_MINOR ( reg)
```

展开值（Value）：

```c
((reg) & TCPC_REG_PD_INT_REV_VER_MINOR_MASK)
```

提取支持的 USB 端口控制器接口版本（Version）次版本部分的宏。

<a id="af929c39cfc085b1dfe90ce46848fa39a"></a>

### `TCPC_REG_PD_INT_REV_VER_MINOR_MASK`

```c
#define TCPC_REG_PD_INT_REV_VER_MINOR_MASK GENMASK(3, 0)
```

支持的 USB 端口控制器接口版本（Version）次版本部分的掩码。

<a id="ac8e53caa68f00ab934c3636d6fab1981"></a>

### `TCPC_REG_PD_REV`

```c
#define TCPC_REG_PD_REV 0x8
```

寄存器地址（Register Address）：USB 电力传输修订版本（Power Delivery Revision）。

<a id="a80f6d51ecf6b817d825d52f3552551d3"></a>

### `TCPC_REG_PD_REV_REV_MAJOR`

```c
#define TCPC_REG_PD_REV_REV_MAJOR ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_PD_REV_REV_MAJOR_MASK) >> 12)
```

提取支持的 USB PD 修订版本（Revision）主版本部分的宏。

<a id="a248e7ad12084944b3255883ee883d335"></a>

### `TCPC_REG_PD_REV_REV_MAJOR_MASK`

```c
#define TCPC_REG_PD_REV_REV_MAJOR_MASK GENMASK(15, 12)
```

支持的 USB PD 修订版本（Revision）主版本部分的掩码。

<a id="a5da3d67228275a828efb9fca1862e7c2"></a>

### `TCPC_REG_PD_REV_REV_MINOR`

```c
#define TCPC_REG_PD_REV_REV_MINOR ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_PD_REV_REV_MINOR_MASK) >> 8)
```

提取支持的 USB PD 修订版本（Revision）次版本部分的宏。

<a id="ab42fdb425046a9b68a29241f81685d65"></a>

### `TCPC_REG_PD_REV_REV_MINOR_MASK`

```c
#define TCPC_REG_PD_REV_REV_MINOR_MASK GENMASK(11, 8)
```

支持的 USB PD 修订版本（Revision）次版本部分的掩码。

<a id="a9d505ec3fe9f2029fc855d5127a36633"></a>

### `TCPC_REG_PD_REV_VER_MAJOR`

```c
#define TCPC_REG_PD_REV_VER_MAJOR ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_PD_REV_VER_MAJOR_MASK) >> 4)
```

提取支持的 USB PD 版本（Version）主版本部分的宏。

<a id="a20bfddfd4d72c697639c742796968482"></a>

### `TCPC_REG_PD_REV_VER_MAJOR_MASK`

```c
#define TCPC_REG_PD_REV_VER_MAJOR_MASK GENMASK(7, 4)
```

支持的 USB PD 版本（Version）主版本部分的掩码。

<a id="af6ce6eaa30960a799436e4841520d183"></a>

### `TCPC_REG_PD_REV_VER_MINOR`

```c
#define TCPC_REG_PD_REV_VER_MINOR ( reg)
```

展开值（Value）：

```c
((reg) & TCPC_REG_PD_REV_VER_MINOR_MASK)
```

提取支持的 USB PD 版本（Version）次版本部分的宏。

<a id="ab3b6a60982e7e9192b2cf4fbda9aa453"></a>

### `TCPC_REG_PD_REV_VER_MINOR_MASK`

```c
#define TCPC_REG_PD_REV_VER_MINOR_MASK GENMASK(3, 0)
```

支持的 USB PD 版本（Version）次版本部分的掩码。

<a id="a2812837d13a05d4a645bbfa41cff7aee"></a>

### `TCPC_REG_POWER_CTRL`

```c
#define TCPC_REG_POWER_CTRL 0x1c
```

寄存器地址：电源控制（Power Control）。

<a id="a7f9af17bb101c2c57b6b18ab07537f10"></a>

### `TCPC_REG_POWER_CTRL_AUTO_DISCHARGE_DISCONNECT`

```c
#define TCPC_REG_POWER_CTRL_AUTO_DISCHARGE_DISCONNECT BIT(4)
```

使能基于 VBUS 电压自动放电（Automatic Discharge）的位。

<a id="a9319ea4d6e1176c85d91a1199c9b1d75"></a>

### `TCPC_REG_POWER_CTRL_BLEED_DISCHARGE`

```c
#define TCPC_REG_POWER_CTRL_BLEED_DISCHARGE BIT(3)
```

使能 VBUS 泄放（Bleed Discharge）的位。

<a id="ae1a14dfde02dd7e51cb252beb6de3321"></a>

### `TCPC_REG_POWER_CTRL_FORCE_DISCHARGE`

```c
#define TCPC_REG_POWER_CTRL_FORCE_DISCHARGE BIT(2)
```

使能 VBUS 强制放电（Forced Discharge）的位。

<a id="a3948eb5f06b80c835a84bb004ff7bded"></a>

### `TCPC_REG_POWER_CTRL_FRS_ENABLE`

```c
#define TCPC_REG_POWER_CTRL_FRS_ENABLE BIT(7)
```

快速角色交换使能位（Fast Role Swap Enable Bit）。

<a id="af308532252e239e508944be24589d140"></a>

### `TCPC_REG_POWER_CTRL_VBUS_VOL_MONITOR_DIS`

```c
#define TCPC_REG_POWER_CTRL_VBUS_VOL_MONITOR_DIS BIT(6)
```

禁用 VBUS 电压监测（Voltage Monitoring）的位。

<a id="a6c2757aad33c9467ee5339b2c556fcd2"></a>

### `TCPC_REG_POWER_CTRL_VCONN_EN`

```c
#define TCPC_REG_POWER_CTRL_VCONN_EN BIT(0)
```

使能向配置通道线（CC Line）提供 VCONN 电源的位。

<a id="a5ca6c7232aa8706cada5485028a14109"></a>

### `TCPC_REG_POWER_CTRL_VCONN_SUPP`

```c
#define TCPC_REG_POWER_CTRL_VCONN_SUPP BIT(1)
```

使能支持的 VCONN 功率（VCONN Power Supported）的位。

置位时，TCPC 向 VCONN 提供的功率至少为设备能力寄存器中“支持的 VCONN 功率（VCONN Power Supported）”字段指示的值；清零时，至少向 VCONN 提供 1 W 功率。

<a id="aa77568b8e2f41c88b99bb6b4fa10841a"></a>

### `TCPC_REG_POWER_CTRL_VOLT_ALARM_DIS`

```c
#define TCPC_REG_POWER_CTRL_VOLT_ALARM_DIS BIT(5)
```

禁用电压报警（Voltage Alarms）的位。

<a id="a8b8c47fc9df661b15b662c2b0b52bb1b"></a>

### `TCPC_REG_POWER_STATUS`

```c
#define TCPC_REG_POWER_STATUS 0x1e
```

寄存器地址：电源状态（Power Status）。

<a id="a8ef2658290efe1ec162ce989f7cb6c94"></a>

### `TCPC_REG_POWER_STATUS_DEBUG_ACC_CON`

```c
#define TCPC_REG_POWER_STATUS_DEBUG_ACC_CON BIT(7)
```

调试附件已连接位（Debug Accessory Connected Bit）。

<a id="a1358f98fb30c51b45ff2fe35eed2431c"></a>

### `TCPC_REG_POWER_STATUS_MASK`

```c
#define TCPC_REG_POWER_STATUS_MASK 0x14
```

寄存器地址：电源状态掩码（Power Status Mask）。各掩码位的位置与对应状态位相同，参见后续引用。

**参阅（See Also）**：另请参见 `TCPC_REG_POWER_STATUS` 寄存器。

<a id="a75cf8cfaa3c2c3149ad73e917ff3ab54"></a>

### `TCPC_REG_POWER_STATUS_SINKING_VBUS`

```c
#define TCPC_REG_POWER_STATUS_SINKING_VBUS BIT(0)
```

正在从 VBUS 受电位（Sinking VBUS Bit）。

置位表示 TCPC 正从 VBUS 向系统负载受电（Sinking）。

<a id="a0390bb8babb73e1bf51b9042b5651646"></a>

### `TCPC_REG_POWER_STATUS_SOURCING_HV`

```c
#define TCPC_REG_POWER_STATUS_SOURCING_HV BIT(5)
```

正在提供高电压位（Sourcing High Voltage Bit）。

置位表示所提供的电压高于 vSafe5V。

<a id="af05c7cc4b4aac0eacc57c9db205d7567"></a>

### `TCPC_REG_POWER_STATUS_SOURCING_VBUS`

```c
#define TCPC_REG_POWER_STATUS_SOURCING_VBUS BIT(4)
```

正在提供 VBUS 电源位（Sourcing VBUS Bit）。

置位表示已使能 VBUS 供电（Sourcing）。

<a id="ace7c591c22de6ef1091a6e8b6330fd4c"></a>

### `TCPC_REG_POWER_STATUS_UNINIT`

```c
#define TCPC_REG_POWER_STATUS_UNINIT BIT(6)
```

内部初始化进行中位（Internal Initialization In-progress Bit）。

置位表示仅寄存器 00～0F 包含有效数据。

<a id="a655efec9f1a6ef9cfc69d5c332d165da"></a>

### `TCPC_REG_POWER_STATUS_VBUS_DET`

```c
#define TCPC_REG_POWER_STATUS_VBUS_DET BIT(3)
```

VBUS 检测使能位（Detection Enabled Bit）。

<a id="acae1371112df4ce0f156e84539ec05a9"></a>

### `TCPC_REG_POWER_STATUS_VBUS_PRES`

```c
#define TCPC_REG_POWER_STATUS_VBUS_PRES BIT(2)
```

VBUS 存在位（Present Bit）。

置位时，VBUS 应高于 4 V；清零时，VBUS 应低于 3.5 V。

<a id="ae9302652868a84227ac9442e00aeecd3"></a>

### `TCPC_REG_POWER_STATUS_VCONN_PRES`

```c
#define TCPC_REG_POWER_STATUS_VCONN_PRES BIT(1)
```

VCONN 存在位（Present Bit）。

CC1 或 CC2 上存在 VCONN 时置位，阈值（Threshold）固定为 2.4 V。

<a id="a298d4f136a7834f0b00e458aca64dcde"></a>

### `TCPC_REG_PRODUCT_ID`

```c
#define TCPC_REG_PRODUCT_ID 0x2
```

寄存器地址（Register Address）：产品 ID（Product ID）。

<a id="a06d954c1171e6b8804214d73b5010444"></a>

### `TCPC_REG_ROLE_CTRL`

```c
#define TCPC_REG_ROLE_CTRL 0x1a
```

寄存器地址：角色控制（Role Control）。

<a id="a4d92739010143fed7976ce7d14859106"></a>

### `TCPC_REG_ROLE_CTRL_CC1`

```c
#define TCPC_REG_ROLE_CTRL_CC1 ( reg)
```

展开值（Value）：

```c
((reg) & TCPC_REG_ROLE_CTRL_CC1_MASK)
```

从寄存器值提取 CC1 的 `enum tc_cc_pull` 的宏。

<a id="a968371033f0493924fc19156357039f0"></a>

### `TCPC_REG_ROLE_CTRL_CC1_MASK`

```c
#define TCPC_REG_ROLE_CTRL_CC1_MASK GENMASK(1, 0)
```

用于提取 CC1 配置的掩码（Mask）。译注：原文写作 `CC!`；此项对应 `TCPC_REG_ROLE_CTRL_CC1_MASK`，按宏名称译为 CC1，详细说明的后续文字为从寄存器值提取上下拉配置。

从寄存器值提取上下拉配置值（Pull Value）。

<a id="ae265027a9005b40b53342953df43d5a8"></a>

### `TCPC_REG_ROLE_CTRL_CC2`

```c
#define TCPC_REG_ROLE_CTRL_CC2 ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_ROLE_CTRL_CC2_MASK) >> 2)
```

从寄存器值提取 CC2 的 `enum tc_cc_pull` 的宏。

<a id="a3c8cc683f79e6c5a0649af7e4a005792"></a>

### `TCPC_REG_ROLE_CTRL_CC2_MASK`

```c
#define TCPC_REG_ROLE_CTRL_CC2_MASK GENMASK(3, 2)
```

从寄存器值提取 CC2 上下拉配置（Pull）值的掩码。

<a id="a5b8503dba17f2aa86e334a2e9975aed7"></a>

### `TCPC_REG_ROLE_CTRL_DRP`

```c
#define TCPC_REG_ROLE_CTRL_DRP ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_ROLE_CTRL_DRP_MASK) >> 6)
```

从寄存器值提取双角色端口位（Dual-role Port Bit）的宏。

<a id="a7c0ebf31802f08dc392a8ecbc019ef1d"></a>

### `TCPC_REG_ROLE_CTRL_DRP_MASK`

```c
#define TCPC_REG_ROLE_CTRL_DRP_MASK BIT(6)
```

双角色端口位（Dual-role Port Bit）。

<a id="ac3e73dc4203eb9f7926d682e5e755356"></a>

### `TCPC_REG_ROLE_CTRL_RP`

```c
#define TCPC_REG_ROLE_CTRL_RP ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_ROLE_CTRL_RP_MASK) >> 4)
```

从寄存器值提取 `enum tc_rp_value` 的宏。

<a id="aff7095f3362ec2fb1b98a5f27c6a55bd"></a>

### `TCPC_REG_ROLE_CTRL_RP_MASK`

```c
#define TCPC_REG_ROLE_CTRL_RP_MASK GENMASK(5, 4)
```

从寄存器值提取上拉电阻（Rp）值的掩码。

<a id="a2763dec90728fb301ea56118da50e7b7"></a>

### `TCPC_REG_ROLE_CTRL_SET`

```c
#define TCPC_REG_ROLE_CTRL_SET ( drp, rp, cc1, cc2 )
```

展开值（Value）：

```c
((((drp) << 6) & TCPC_REG_ROLE_CTRL_DRP_MASK) |                                            \
 (((rp) << 4) & TCPC_REG_ROLE_CTRL_RP_MASK) |                                              \
 (((cc2) << 2) & TCPC_REG_ROLE_CTRL_CC2_MASK) | ((cc1) & TCPC_REG_ROLE_CTRL_CC1_MASK))
```

根据 `drp`、`rp` 和配置通道线（CC Lines）的值设置寄存器值的宏。

<a id="a4daad9b00cbea6bc95dd71438f40cd43"></a>

### `TCPC_REG_RX_BUFFER`

```c
#define TCPC_REG_RX_BUFFER 0x30
```

寄存器地址：接收缓冲区（Receive Buffer），包括可读字节数、接收缓冲帧类型和接收缓冲字节。在 TCPC Rev 2.0 中，`RECEIVE_BUFFER` 由三组寄存器组成：`READABLE_BYTE_COUNT`、`RX_BUF_FRAME_TYPE` 和 `RX_BUF_BYTE_x`。

这些寄存器只能通过读取公共寄存器地址 `30h` 访问。

<a id="a5c8b27d3985859742e8fb0bbb8b91ab3"></a>

### `TCPC_REG_RX_DETECT`

```c
#define TCPC_REG_RX_DETECT 0x2f
```

寄存器地址：接收检测（Receive Detect）。

<a id="aaf4c0249c33ed98919164ba64f8715db"></a>

### `TCPC_REG_RX_DETECT_CABLE_RST`

```c
#define TCPC_REG_RX_DETECT_CABLE_RST BIT(6)
```

线缆复位（Cable Reset）使能位。

置位表示 TCPC 将检测线缆复位信号（Cable Reset Signal）。

<a id="a77dc544a1fe3083f0b52cfaae8248c36"></a>

### `TCPC_REG_RX_DETECT_HRST`

```c
#define TCPC_REG_RX_DETECT_HRST BIT(5)
```

硬复位（Hard Reset）使能位。

置位表示 TCPC 将检测硬复位信号（Hard Reset Signal）。

<a id="a5241355ce8ea7ef2e5222cfcc7ef7c14"></a>

### `TCPC_REG_RX_DETECT_MSG_DISABLE_DISCONNECT`

```c
#define TCPC_REG_RX_DETECT_MSG_DISABLE_DISCONNECT BIT(7)
```

断开时禁用消息位（Message Disable Disconnect Bit）。

置位时，配置为受电端（Sink）的 TCPC 在检测到 `SNK.Open` 状态持续规范规定的消抖时间后，应禁用 PD 消息传递（Message Delivery）。清零时，受电端 TCPC 在告警寄存器中的 VBUS 受电端断开检测标志置位时禁用 PD 消息传递。

<a id="a2d25f62dcf34358d1f95c81ffcc22544"></a>

### `TCPC_REG_RX_DETECT_SOP`

```c
#define TCPC_REG_RX_DETECT_SOP BIT(0)
```

SOP 消息（Message）使能位。

置位表示 TCPC 将检测 SOP 消息（Messages）。

<a id="abda68103a95c3f2e02c3ed538f6d7852"></a>

### `TCPC_REG_RX_DETECT_SOP_HRST_MASK`

```c
#define TCPC_REG_RX_DETECT_SOP_HRST_MASK (TCPC_REG_RX_DETECT_SOP | TCPC_REG_RX_DETECT_HRST)
```

检测 SOP 消息及硬复位信号（Hard Reset Signals）的掩码。

<a id="a4abcaf2f1a2204e6b3f408ed5872d91d"></a>

### `TCPC_REG_RX_DETECT_SOP_SOPP_SOPPP_HRST_MASK`

```c
#define TCPC_REG_RX_DETECT_SOP_SOPP_SOPPP_HRST_MASK
```

展开值（Value）：

```c
(TCPC_REG_RX_DETECT_SOP | TCPC_REG_RX_DETECT_SOPP | TCPC_REG_RX_DETECT_SOPPP |             \
 TCPC_REG_RX_DETECT_HRST)
```

检测 SOP、SOP'、SOP'' 消息及硬复位信号（Hard Reset Signals）的掩码。

<a id="a2112c2d15ef5490e489bae450c690320"></a>

### `TCPC_REG_RX_DETECT_SOPP`

```c
#define TCPC_REG_RX_DETECT_SOPP BIT(1)
```

SOP' 消息（Message）使能位。

置位表示 TCPC 将检测 SOP' 消息（Messages）。

<a id="a2159c1a117c9c35c779e9852e609a54d"></a>

### `TCPC_REG_RX_DETECT_SOPP_DBG`

```c
#define TCPC_REG_RX_DETECT_SOPP_DBG BIT(3)
```

SOP_DBG' 消息（Message）使能位。

置位表示 TCPC 将检测 SOP_DBG' 消息（Messages）。

<a id="a5326c588fffc385cf6368a5149f4ed92"></a>

### `TCPC_REG_RX_DETECT_SOPPP`

```c
#define TCPC_REG_RX_DETECT_SOPPP BIT(2)
```

SOP'' 消息（Message）使能位。

置位表示 TCPC 将检测 SOP'' 消息（Messages）。

<a id="a1f2d37d68844c10411adc5090229fa21"></a>

### `TCPC_REG_RX_DETECT_SOPPP_DBG`

```c
#define TCPC_REG_RX_DETECT_SOPPP_DBG BIT(4)
```

SOP_DBG'' 消息（Message）使能位。

置位表示 TCPC 将检测 SOP_DBG'' 消息（Messages）。

<a id="aa694b54fb0753fae36be1650d69d23fd"></a>

### `TCPC_REG_STD_INPUT_CAP`

```c
#define TCPC_REG_STD_INPUT_CAP 0x28
```

寄存器地址：标准输入能力（Standard Input Capabilities）。

<a id="ab2d3d3d8c3701a8e040062f0bc990bc7"></a>

### `TCPC_REG_STD_INPUT_CAP_EXT_OCP`

```c
#define TCPC_REG_STD_INPUT_CAP_EXT_OCP BIT(1)
```

VBUS 外部过流故障位（External Over Current Fault Bit）。

置位表示 TCPC 具有该输入引脚（Input Pin）。

<a id="a312bedca7d20ec62efa1cd0b6a585b96"></a>

### `TCPC_REG_STD_INPUT_CAP_EXT_OVP`

```c
#define TCPC_REG_STD_INPUT_CAP_EXT_OVP BIT(2)
```

VBUS 外部过压故障位（External Over Voltage Fault Bit）。

置位表示 TCPC 具有该输入引脚（Input Pin）。

<a id="a9674e7ce46e0b2891cb585e34660403d"></a>

### `TCPC_REG_STD_INPUT_CAP_FORCE_OFF_VBUS`

```c
#define TCPC_REG_STD_INPUT_CAP_FORCE_OFF_VBUS BIT(0)
```

具有强制关闭 VBUS 功能的位（Force Off VBUS Present Bit）。

置位表示 TCPC 具有该输入引脚（Input Pin）。

<a id="a2abf1d902a911882e767e777d11faa9a"></a>

### `TCPC_REG_STD_INPUT_CAP_SRC_FRS`

```c
#define TCPC_REG_STD_INPUT_CAP_SRC_FRS ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_STD_INPUT_CAP_SRC_FRS_MASK) >> 3)
```

从寄存器值提取供电端快速角色交换（Source Fast Role Swap）配置的宏。

<a id="a488f8de2a651ede27ae4f2decc66fdfe"></a>

### `TCPC_REG_STD_INPUT_CAP_SRC_FRS_MASK`

```c
#define TCPC_REG_STD_INPUT_CAP_SRC_FRS_MASK GENMASK(4, 3)
```

供电端快速角色交换（Source Fast Role Swap）的掩码。

<a id="a03fe81146cf0aa1f7f9398a3a7389183"></a>

### `TCPC_REG_STD_INTPU_CAP_SRC_FRS_BOTH`

```c
#define TCPC_REG_STD_INTPU_CAP_SRC_FRS_BOTH 2
```

TCPC 具有兼作输入和输出的供电端快速角色交换引脚（Input and Output Pin）的取值。

<a id="ab7efd85994fdfaab7580d39259359c78"></a>

### `TCPC_REG_STD_INTPU_CAP_SRC_FRS_INPUT`

```c
#define TCPC_REG_STD_INTPU_CAP_SRC_FRS_INPUT 1
```

TCPC 具有仅输入的供电端快速角色交换引脚（Input-only Pin）的取值。

<a id="a65fd3ac4a027333305b8b6162cd36c57"></a>

### `TCPC_REG_STD_INTPU_CAP_SRC_FRS_NONE`

```c
#define TCPC_REG_STD_INTPU_CAP_SRC_FRS_NONE 0
```

TCPC 不具有供电端快速角色交换引脚（Source Fast Role Swap Pin）的取值。

<a id="aee8dedd72106140fac5f74a86059aab8"></a>

### `TCPC_REG_STD_OUTPUT_CAP`

```c
#define TCPC_REG_STD_OUTPUT_CAP 0x29
```

寄存器地址：标准输出能力（Standard Output Capabilities）。

<a id="ae3d5652cf07c2ea2a6154ef30c961892"></a>

### `TCPC_REG_STD_OUTPUT_CAP_ACTIVE_CABLE`

```c
#define TCPC_REG_STD_OUTPUT_CAP_ACTIVE_CABLE BIT(3)
```

有源线缆指示位（Active Cable Indicator Bit）。

<a id="abfa7770503e634cb7479b8ee16556045"></a>

### `TCPC_REG_STD_OUTPUT_CAP_AUDIO_ACCESSORY`

```c
#define TCPC_REG_STD_OUTPUT_CAP_AUDIO_ACCESSORY BIT(4)
```

音频适配器附件指示位（Audio Adapter Accessory Indicator Bit）。

<a id="af476ab76f277de3bbf6d57b4276919b4"></a>

### `TCPC_REG_STD_OUTPUT_CAP_CONN_ORIENTATION`

```c
#define TCPC_REG_STD_OUTPUT_CAP_CONN_ORIENTATION BIT(0)
```

连接器方向位（Connector Orientation Bit）。

<a id="a532b8a6d0bde03f665cff5fde3a2851c"></a>

### `TCPC_REG_STD_OUTPUT_CAP_CONN_PRESENT`

```c
#define TCPC_REG_STD_OUTPUT_CAP_CONN_PRESENT BIT(1)
```

连接存在位（Connection Present Bit）。

<a id="a50a36f30796ed51d87b64e2f2099e6eb"></a>

### `TCPC_REG_STD_OUTPUT_CAP_DBG_ACCESSORY`

```c
#define TCPC_REG_STD_OUTPUT_CAP_DBG_ACCESSORY BIT(6)
```

调试附件指示位（Debug Accessory Indicator Bit）。

<a id="a915aeabb332fe9a5ad97c5253121fdd8"></a>

### `TCPC_REG_STD_OUTPUT_CAP_MUX_CFG_CTRL`

```c
#define TCPC_REG_STD_OUTPUT_CAP_MUX_CFG_CTRL BIT(2)
```

多路复用器配置控制位（Mux Configuration Control Bit）。

<a id="a5802b9ce7baf28c5a5430818d0f637a5"></a>

### `TCPC_REG_STD_OUTPUT_CAP_SNK_DISC_DET`

```c
#define TCPC_REG_STD_OUTPUT_CAP_SNK_DISC_DET BIT(7)
```

VBUS 受电端断开检测指示位（Sink Disconnect Detect Indicator Bit）。

<a id="a57e0aee8e070c3294c5580c7d1043454"></a>

### `TCPC_REG_STD_OUTPUT_CAP_VBUS_PRESENT_MON`

```c
#define TCPC_REG_STD_OUTPUT_CAP_VBUS_PRESENT_MON BIT(5)
```

VBUS 存在监测位（Present Monitor Bit）。

<a id="a67e70b7ed5d7f1ea18bee26314677633"></a>

### `TCPC_REG_TC_REV`

```c
#define TCPC_REG_TC_REV 0x6
```

寄存器地址（Register Address）：USB Type-C 版本（Version）。

<a id="ac87ba6ce928e84bffc2333584bfabcf7"></a>

### `TCPC_REG_TC_REV_MAJOR`

```c
#define TCPC_REG_TC_REV_MAJOR ( reg)
```

展开值（Value）：

```c
(((reg) & TCPC_REG_TC_REV_MAJOR_MASK) >> 4)
```

提取支持的 Type-C 发行版本主版本部分的宏（Major Release Extraction Macro）。

<a id="a9bbad168da5862eb7c8494925380546d"></a>

### `TCPC_REG_TC_REV_MAJOR_MASK`

```c
#define TCPC_REG_TC_REV_MAJOR_MASK GENMASK(7, 4)
```

支持的 Type-C 发行版本主版本部分的掩码（Major Release Mask）。

<a id="a9892dc0a9d01deaf56e8a28546489e65"></a>

### `TCPC_REG_TC_REV_MINOR`

```c
#define TCPC_REG_TC_REV_MINOR ( reg)
```

展开值（Value）：

```c
((reg) & TCPC_REG_TC_REV_MINOR_MASK)
```

提取支持的 Type-C 发行版本次版本部分的宏（Minor Release Extraction Macro）。

<a id="a6a1e3d112af2697f1945614c57df9f26"></a>

### `TCPC_REG_TC_REV_MINOR_MASK`

```c
#define TCPC_REG_TC_REV_MINOR_MASK GENMASK(3, 0)
```

支持的 Type-C 发行版本次版本部分的掩码（Minor Release Mask）。

<a id="a5be1063bb4f9c7db7f9f6a870858455d"></a>

### `TCPC_REG_TCPC_CTRL`

```c
#define TCPC_REG_TCPC_CTRL 0x19
```

寄存器地址：端口控制器控制（TCPC Control）。

<a id="aebc9538529f9d9e516dec8973445ba0a"></a>

### `TCPC_REG_TCPC_CTRL_BIST_TEST_MODE`

```c
#define TCPC_REG_TCPC_CTRL_BIST_TEST_MODE BIT(1)
```

内建自测试模式（BIST Test Mode）使能位。

<a id="a857522248dd727c57c63958aa3ca9d52"></a>

### `TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_DISABLED`

```c
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_DISABLED 0
```

禁用时钟拉伸（Clock Stretching）的取值。

<a id="a3915ad947314f254aa741d29b68478ae"></a>

### `TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_ALWAYS`

```c
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_ALWAYS (2 << 2)
```

使能有限时钟拉伸（Limited Clock Stretching）的取值。

<a id="ae39a550bcf4bf6ec6a2cf23c6938933d"></a>

### `TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_NO_ALERT`

```c
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_NO_ALERT (3 << 2)
```

仅在告警未置为有效（Alert Not Asserted）时使能时钟拉伸的取值。

<a id="a63e57b4638e0a221cc1a5d0ad0c5daf9"></a>

### `TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_MASK`

```c
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_MASK GENMASK(3, 2)
```

掩码（Mask）。

<a id="a990e2cad707373a0741ec1d679b9fe30"></a>

### `TCPC_REG_TCPC_CTRL_DEBUG_ACC_CONTROL`

```c
#define TCPC_REG_TCPC_CTRL_DEBUG_ACC_CONTROL BIT(4)
```

使能端口管理器（TCPM）控制调试附件的位。

<a id="aa672c46d6a4332ba050c535b17693497"></a>

### `TCPC_REG_TCPC_CTRL_EN_LOOK4CONNECTION_ALERT`

```c
#define TCPC_REG_TCPC_CTRL_EN_LOOK4CONNECTION_ALERT BIT(6)
```

发现连接时使能告警有效输出（Alert Assertion）的位。

<a id="a8d44838af49c8eb316668a014eb71704"></a>

### `TCPC_REG_TCPC_CTRL_PLUG_ORIENTATION`

```c
#define TCPC_REG_TCPC_CTRL_PLUG_ORIENTATION BIT(0)
```

插头方向与 VCONN 目标（Plug Orientation and VCONN Destination）位。

<a id="a3e023fad44f6e27c2b3b39f436c359d2"></a>

### `TCPC_REG_TCPC_CTRL_SMBUS_PEC`

```c
#define TCPC_REG_TCPC_CTRL_SMBUS_PEC BIT(7)
```

SMBus 数据包错误码（PEC）使能位。

<a id="ab28ab0d34d76d44bd66570cec9f6c08f"></a>

### `TCPC_REG_TCPC_CTRL_WATCHDOG_TIMER`

```c
#define TCPC_REG_TCPC_CTRL_WATCHDOG_TIMER BIT(5)
```

看门狗监视位（Watchdog Monitoring Bit）。

<a id="ac35deff33f359763004e3a7bd151e880"></a>

### `TCPC_REG_TRANSMIT`

```c
#define TCPC_REG_TRANSMIT 0x50
```

寄存器地址：发送（Transmit）。

<a id="aeefbf28250aede27a29ed6b9cfe1a36f"></a>

### `TCPC_REG_TRANSMIT_SET_WITH_RETRY`

```c
#define TCPC_REG_TRANSMIT_SET_WITH_RETRY ( retries, type )
```

展开值（Value）：

```c
((retries) << 4 | (type))
```

根据消息类型（Message Type）和重试次数（Retries Count）设置发送寄存器的宏。

<a id="abaaca2dc2fe5e8532ff078a5f7e3b200"></a>

### `TCPC_REG_TRANSMIT_SET_WITHOUT_RETRY`

```c
#define TCPC_REG_TRANSMIT_SET_WITHOUT_RETRY ( type)
```

展开值（Value）：

```c
(type)
```

根据消息类型（Message Type）设置发送寄存器，并禁用重试的宏。

<a id="a538258b3939d8d99397786bf359d472b"></a>

### `TCPC_REG_TRANSMIT_TYPE_BIST`

```c
#define TCPC_REG_TRANSMIT_TYPE_BIST 7
```

发送内建自测试载波模式 2（BIST Carrier Mode 2）的取值。

<a id="aff9f4bdd730c629437f05453c70deac7"></a>

### `TCPC_REG_TRANSMIT_TYPE_CABLE_RST`

```c
#define TCPC_REG_TRANSMIT_TYPE_CABLE_RST 6
```

发送线缆复位信号（Cable Reset Signal）的取值。

<a id="a17cd5977a9ede551e78d3e01b6eb208b"></a>

### `TCPC_REG_TRANSMIT_TYPE_HRST`

```c
#define TCPC_REG_TRANSMIT_TYPE_HRST 5
```

发送硬复位信号（Hard Reset Signal）的取值。

<a id="abfd747a6b0791d38a84ae3128fc5a028"></a>

### `TCPC_REG_TRANSMIT_TYPE_SOP`

```c
#define TCPC_REG_TRANSMIT_TYPE_SOP 0
```

发送 SOP 类型消息（Message）的取值。

<a id="a45b07f17c4e9a1ab943d0756839abf3e"></a>

### `TCPC_REG_TRANSMIT_TYPE_SOP_DBG_P`

```c
#define TCPC_REG_TRANSMIT_TYPE_SOP_DBG_P 3
```

发送 SOP_DBG' 类型消息（Message）的取值。

<a id="a5a03279d861be9015cc8536dc0b40205"></a>

### `TCPC_REG_TRANSMIT_TYPE_SOP_DBG_PP`

```c
#define TCPC_REG_TRANSMIT_TYPE_SOP_DBG_PP 4
```

发送 SOP_DBG'' 类型消息（Message）的取值。

<a id="af8cc6c6554a088bc6426449f8562d5db"></a>

### `TCPC_REG_TRANSMIT_TYPE_SOPP`

```c
#define TCPC_REG_TRANSMIT_TYPE_SOPP 1
```

发送 SOP' 类型消息（Message）的取值。

<a id="ac808ad1c100f22495c6bc270786e311c"></a>

### `TCPC_REG_TRANSMIT_TYPE_SOPPP`

```c
#define TCPC_REG_TRANSMIT_TYPE_SOPPP 2
```

发送 SOP'' 类型消息（Message）的取值。

<a id="a9d51fa2448c2cf6566033611387c2d51"></a>

### `TCPC_REG_TX_BUFFER`

```c
#define TCPC_REG_TX_BUFFER 0x51
```

寄存器地址：发送缓冲区（Transmit Buffer）。在 TCPC Rev 2.0 中，`TRANSMIT_BUFFER` 保存 `I2C_WRITE_BYTE_COUNT`，以及 TCPM 最近写入 `TX_BUF_BYTE_x` 的 SOP* USB PD 消息载荷部分，包括头和／或数据字节。

`TX_BUF_BYTE_x` 是“隐藏的（Hidden）”，只能通过写入寄存器地址 `51h` 访问。

<a id="a0597b5a24eb3a8104a79efa09dcc37fd"></a>

### `TCPC_REG_VBUS_NONDEFAULT_TARGET`

```c
#define TCPC_REG_VBUS_NONDEFAULT_TARGET 0x7a
```

寄存器地址：VBUS 非默认目标值（Nondefault Target）。仅在设备能力 1 寄存器中的 VBUS 非默认目标位被置位时可用。

此寄存器用于在向命令寄存器发送 VBUS 非默认电压供电命令（Source VBUS Nondefault Voltage Command）时，提供 VBUS 非默认电压值。

<a id="a28dd8cdcb9bbb5fc5a649fa409813244"></a>

### `TCPC_REG_VBUS_NONDEFAULT_TARGET_LSB`

```c
#define TCPC_REG_VBUS_NONDEFAULT_TARGET_LSB 20
```

寄存器中存储数值的分辨率（Resolution）。

从寄存器读出的值必须乘以此值，才能得到单位为 mV 的实际电压；要将以 mV 表示的电压写入寄存器，必须先除以此常量。规范将其定义为 20 mV。

<a id="ae34235441f657c818ef76c342a0d31ce"></a>

### `TCPC_REG_VBUS_SINK_DISCONNECT_THRESH`

```c
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH 0x72
```

寄存器地址：VBUS 受电端断开阈值（Sink Disconnect Threshold）。

<a id="af722b3898795034132d8d1a0faa9548e"></a>

### `TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_DEFAULT`

```c
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_DEFAULT 0x008C /* 3.5 V */
```

VBUS 受电端断开阈值（Sink Disconnect Threshold）的默认值。

<a id="a5f14456afefb9f4067c60f6b56a4fc5f"></a>

### `TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_LSB`

```c
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_LSB 25
```

寄存器中存储数值的分辨率（Resolution）。

从寄存器读出的值必须乘以此值，才能得到单位为 mV 的实际电压；要将以 mV 表示的电压写入寄存器，必须先除以此常量。规范将其定义为 25 mV。

<a id="affabe58babbeda3d7fdf574e24fad4af"></a>

### `TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_MASK`

```c
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_MASK GENMASK(11, 0)
```

电压触发点（Voltage Trip Point）有效位的掩码。

<a id="a5fad6cf61808e3d348febefaff8e143b"></a>

### `TCPC_REG_VBUS_STOP_DISCHARGE_THRESH`

```c
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH 0x74
```

寄存器地址：VBUS 受电端断开阈值（Sink Disconnect Threshold）。

<a id="a101c1813f155407644db8e68039bc62e"></a>

### `TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_DEFAULT`

```c
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_DEFAULT 0x0020 /* 0.8 V */
```

VBUS 停止放电阈值（Stop Discharge Threshold）的默认值。

<a id="a5957aba93c23e722fb8387bcaa5c77f9"></a>

### `TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_LSB`

```c
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_LSB 25
```

寄存器中存储数值的分辨率（Resolution）。

从寄存器读出的值必须乘以此值，才能得到单位为 mV 的实际电压；要将以 mV 表示的电压写入寄存器，必须先除以此常量。规范将其定义为 25 mV。

<a id="a35c517353c32bb43234a5795fe458f75"></a>

### `TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_MASK`

```c
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_MASK GENMASK(11, 0)
```

电压触发点（Voltage Trip Point）有效位的掩码。

<a id="a08350059745d7e71150f5d4321fd1983"></a>

### `TCPC_REG_VBUS_VOLTAGE`

```c
#define TCPC_REG_VBUS_VOLTAGE 0x70
```

寄存器地址：VBUS 电压（Voltage）。

<a id="ac3a3f13d1189b5ac1694dd05e8c2d15b"></a>

### `TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG`

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG 0x76
```

寄存器地址：VBUS 高电压报警（Voltage Alarm High）。

<a id="aa6614362ab8e07b711006efc7f6d97f5"></a>

### `TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_LSB`

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_LSB 25
```

寄存器中存储数值的分辨率（Resolution）。

从寄存器读出的值必须乘以此值，才能得到单位为 mV 的实际电压；要将以 mV 表示的电压写入寄存器，必须先除以此常量。规范将其定义为 25 mV。

<a id="a33b30eb4bafa65700161f6f6dd947c5a"></a>

### `TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_MASK`

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_MASK GENMASK(11, 0)
```

电压触发点（Voltage Trip Point）有效位的掩码。

<a id="a64356ee1d195c91d23646e79eeb405ce"></a>

### `TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG`

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG 0x78
```

寄存器地址：VBUS 低电压报警（Voltage Alarm Low）。

<a id="a2d8ea62d4b2e46c1f98e8a04a262a56a"></a>

### `TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_LSB`

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_LSB 25
```

寄存器中存储数值的分辨率（Resolution）。

从寄存器读出的值必须乘以此值，才能得到单位为 mV 的实际电压；要将以 mV 表示的电压写入寄存器，必须先除以此常量。规范将其定义为 25 mV。

<a id="a7d7b3f9e6573e608ce84a1c60e446b78"></a>

### `TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_MASK`

```c
#define TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_MASK GENMASK(11, 0)
```

电压触发点（Voltage Trip Point）有效位的掩码。

<a id="a4ef01ebd0721491e0336215b8d02f362"></a>

### `TCPC_REG_VBUS_VOLTAGE_LSB`

```c
#define TCPC_REG_VBUS_VOLTAGE_LSB 25
```

VBUS 电压测量分辨率（Voltage Measurement Resolution）。

规定值为 25 mV。

<a id="a7a4dd82c861fc09b4eb3b8bbe2c066df"></a>

### `TCPC_REG_VBUS_VOLTAGE_MEASUREMENT`

```c
#define TCPC_REG_VBUS_VOLTAGE_MEASUREMENT ( reg)
```

展开值（Value）：

```c
((reg) & TCPC_REG_VBUS_VOLTAGE_MEASUREMENT_MASK)
```

从寄存器值提取 VBUS 测量值（Measurement）的宏。

<a id="a2b433b9683e5d87faf825c739a985063"></a>

### `TCPC_REG_VBUS_VOLTAGE_MEASUREMENT_MASK`

```c
#define TCPC_REG_VBUS_VOLTAGE_MEASUREMENT_MASK GENMASK(9, 0)
```

VBUS 电压测量值（Voltage Measurement）的掩码。

<a id="a85fce4d69cb3e25360d7373d4dfe4aab"></a>

### `TCPC_REG_VBUS_VOLTAGE_SCALE`

```c
#define TCPC_REG_VBUS_VOLTAGE_SCALE ( reg)
```

展开值（Value）：

```c
(1 << (((reg) & TCPC_REG_VBUS_VOLTAGE_SCALE_FACTOR_MASK) >> 10))
```

从寄存器值提取 VBUS 电压比例（Voltage Scale）的宏。

<a id="a8a4427814137f1bcd29bcf03d38c448a"></a>

### `TCPC_REG_VBUS_VOLTAGE_SCALE_FACTOR_MASK`

```c
#define TCPC_REG_VBUS_VOLTAGE_SCALE_FACTOR_MASK GENMASK(11, 10)
```

比例因子（Scale Factor）的掩码。

<a id="a44a388e875c298eec029c12d9d74d01d"></a>

### `TCPC_REG_VBUS_VOLTAGE_VBUS`

```c
#define TCPC_REG_VBUS_VOLTAGE_VBUS ( x)
```

展开值（Value）：

```c
(TCPC_REG_VBUS_VOLTAGE_SCALE(x) * TCPC_REG_VBUS_VOLTAGE_MEASUREMENT(x) *                   \
 TCPC_REG_VBUS_VOLTAGE_LSB)
```

考虑比例因子（Scale Factor），将寄存器值转换为实际电压测量值的宏。

<a id="ac81b442c1da80aa411d06f4829149edb"></a>

### `TCPC_REG_VENDOR_ID`

```c
#define TCPC_REG_VENDOR_ID 0x0
```

寄存器地址（Register Address）：厂商 ID（Vendor ID）。


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P112_tcpci.h_源码浏览.md)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)
- [pd_rev_type](../api_socket_lora_topic_reference/P012_USB 电力传输（USB Power Delivery）.md#gab68c6b6e33449c5ceadfc9217dd7a700)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="atcpci_8h_html_a754af0239b587e79932f58a172c24dd3"></a>
<a id="atcpci_8h_html_a24e24cd118532bd78b8c82e5bf896820"></a>
<a id="atcpci_8h_html_a91fa27df2ff4b97d131a3ff527cb858d"></a>
<a id="atcpci_8h_html_a6e35508726be479f714c06a966fbc037"></a>
<a id="atcpci_8h_html_adfb8168078feb6b3243f1b3ac4b243ec"></a>
<a id="atcpci_8h_html_ad2f45b2a55372cb8c2bb698427f2de6d"></a>
<a id="atcpci_8h_html_ad200e3bdb166affa1cf99627e01871d6"></a>
<a id="atcpci_8h_html_af94599c39af76bd1e01df2a1930ca2c5"></a>
<a id="atcpci_8h_html_a7a41fdf846fe7f8e92ecab27d8c37783"></a>
<a id="atcpci_8h_html_aa2165616615d1e49b3da8e9e526409c9"></a>
<a id="agroup__usb__power__delivery_html_gab68c6b6e33449c5ceadfc9217dd7a700"></a>
<a id="atcpci_8h_html_afd52534290a2b7d738ea73888d16419f"></a>
<a id="atcpci_8h_html_a66e85404023d11733db1d71a1625f4e9"></a>
<a id="atcpci_8h_html_a19c752a82a935fd74d9c22be4f9c2e79"></a>
<a id="atcpci_8h_html_af929c39cfc085b1dfe90ce46848fa39a"></a>
<a id="atcpci_8h_html_a248e7ad12084944b3255883ee883d335"></a>
<a id="atcpci_8h_html_ab42fdb425046a9b68a29241f81685d65"></a>
<a id="atcpci_8h_html_a20bfddfd4d72c697639c742796968482"></a>
<a id="atcpci_8h_html_ab3b6a60982e7e9192b2cf4fbda9aa453"></a>
<a id="atcpci_8h_html_a968371033f0493924fc19156357039f0"></a>
<a id="atcpci_8h_html_a3c8cc683f79e6c5a0649af7e4a005792"></a>
<a id="atcpci_8h_html_a7c0ebf31802f08dc392a8ecbc019ef1d"></a>
<a id="atcpci_8h_html_aff7095f3362ec2fb1b98a5f27c6a55bd"></a>
<a id="atcpci_8h_html_a2112c2d15ef5490e489bae450c690320"></a>
<a id="atcpci_8h_html_a2d25f62dcf34358d1f95c81ffcc22544"></a>
<a id="atcpci_8h_html_a5326c588fffc385cf6368a5149f4ed92"></a>
<a id="atcpci_8h_html_a77dc544a1fe3083f0b52cfaae8248c36"></a>
<a id="atcpci_8h_html_a488f8de2a651ede27ae4f2decc66fdfe"></a>
<a id="atcpci_8h_html_a9bbad168da5862eb7c8494925380546d"></a>
<a id="atcpci_8h_html_a6a1e3d112af2697f1945614c57df9f26"></a>
<a id="atcpci_8h_html_a2b433b9683e5d87faf825c739a985063"></a>
<a id="atcpci_8h_html_a8a4427814137f1bcd29bcf03d38c448a"></a>
<a id="atcpci_8h_html_a4ef01ebd0721491e0336215b8d02f362"></a>
<a id="atcpci_8h_html_a7a4dd82c861fc09b4eb3b8bbe2c066df"></a>
<a id="atcpci_8h_html_a85fce4d69cb3e25360d7373d4dfe4aab"></a>

---

[上一章](P005_zephyr__bluetooth__classic__sdp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dt-bindings__wuc__wuc_nxp_wuu.h_文件参考.md)
