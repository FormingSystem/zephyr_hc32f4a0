---
id: learning.zephyr-docs.api-file-storage-event-reference.page-12
title: zephyr__net__ieee802154.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ieee802154_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_net\_\_ieee802154.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.15.4原生第二层协议栈（Native L2 Stack）的公共头文件。

<a id="details"></a>

```c
#include <limits.h>
#include <zephyr/net/net_l2.h>
#include <zephyr/net/net_mgmt.h>
#include <zephyr/crypto/cipher.h>
#include <zephyr/net/ieee802154_radio.h>
```

查看此文件的源码。

IEEE 802.15.4 原生二层协议栈（Native L2 Stack）公共头文件。**注意（Note）：**本文件全部标准引用均指 IEEE 802.15.4-2020。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_ieee802154_5Fsecurity_5Fctx"></a>

```c
struct ieee802154_security_ctx
```

相关声明：[ieee802154_security_ctx](../network_core_model_reference/P044_ieee802154_security_ctx_结构体.md)。

接口级安全属性（Interface-Level Security Attributes），见第9.5节。

<a id="r_ieee802154_5Fcontext"></a>

```c
struct ieee802154_context
```

相关声明：[ieee802154_context](../network_core_model_reference/P015_ieee802154_context_结构体.md)。

IEEE 802.15.4第二层（L2）的上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_gac63b5ae7ed99b168871b5fc08ecde7a1"></a>

```c
#define IEEE802154_MAX_PHY_PACKET_SIZE 127
```

相关声明：[IEEE802154_MAX_PHY_PACKET_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gac63b5ae7ed99b168871b5fc08ecde7a1)。

表示物理层（PHY）常量 `aMaxPhyPacketSize`，参见 11.3 节。

<a id="r_ga1243000b59167777e078060fd3c1c218"></a>

```c
#define IEEE802154_FCS_LENGTH 2
```

相关声明：[IEEE802154_FCS_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga1243000b59167777e078060fd3c1c218)。

表示帧校验序列长度（Frame Check Sequence Length），参见 7.2.1.1 节。

<a id="r_ga987d42d1d8117ec58cf3f9cae4e66139"></a>

```c
#define IEEE802154_MTU (IEEE802154_MAX_PHY_PACKET_SIZE - IEEE802154_FCS_LENGTH)
```

相关声明：[IEEE802154_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga987d42d1d8117ec58cf3f9cae4e66139)、[IEEE802154_MAX_PHY_PACKET_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gac63b5ae7ed99b168871b5fc08ecde7a1)、[IEEE802154_FCS_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga1243000b59167777e078060fd3c1c218)。

IEEE 802.15.4“硬件”最大传输单元（Hardware MTU），不要与三层／IP MTU 混淆，即：

<a id="r_gaee7ec8e4ba396f3cd658bcb22a9352e8"></a>

```c
#define IEEE802154_SHORT_ADDR_LENGTH 2
```

相关声明：[IEEE802154_SHORT_ADDR_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gaee7ec8e4ba396f3cd658bcb22a9352e8)。

IEEE 802.15.4 短地址长度（Short Address Length）。

<a id="r_ga355350794ec26788bc855da53d311bea"></a>

```c
#define IEEE802154_EXT_ADDR_LENGTH 8
```

相关声明：[IEEE802154_EXT_ADDR_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga355350794ec26788bc855da53d311bea)。

IEEE 802.15.4 扩展地址长度（Extended Address Length）。

<a id="r_gae405ed23baf91fa3d96c81d5121faa1a"></a>

```c
#define IEEE802154_MAX_ADDR_LENGTH IEEE802154_EXT_ADDR_LENGTH
```

相关声明：[IEEE802154_MAX_ADDR_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gae405ed23baf91fa3d96c81d5121faa1a)、[IEEE802154_EXT_ADDR_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga355350794ec26788bc855da53d311bea)。

IEEE 802.15.4 最大地址长度（Maximum Address Length）。

<a id="r_ga692a16d957c1e1ce76808cda325fd6c5"></a>

```c
#define IEEE802154_NO_CHANNEL USHRT_MAX
```

相关声明：[IEEE802154_NO_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga692a16d957c1e1ce76808cda325fd6c5)。

特殊信道值（Channel Value），按上下文表示“所有”信道（All Channels）或“任意”信道（Any Channel）。

<a id="r_gafae1906dc9b39c93690b127efaaacacb"></a>

```c
#define IEEE802154_BROADCAST_ADDRESS 0xffff
```

相关声明：[IEEE802154_BROADCAST_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gafae1906dc9b39c93690b127efaaacacb)。

表示 IEEE 802.15.4 广播短地址（Broadcast Short Address），参见 6.1、8.4.3 节和表 8-94 的 `macShortAddress`。

<a id="r_ga43369b4a9ea0961395cd135b9fe18d03"></a>

```c
#define IEEE802154_NO_SHORT_ADDRESS_ASSIGNED 0xfffe
```

相关声明：[IEEE802154_NO_SHORT_ADDRESS_ASSIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga43369b4a9ea0961395cd135b9fe18d03)。

表示特殊 IEEE 802.15.4 短地址（Short Address）：设备已与协调器（Coordinator）关联，但未取得短地址。参见 6.4.1、8.4.3 节和表 8-94 的 `macShortAddress`。

<a id="r_ga1a40fed9dcd802af0283d7808e8b283b"></a>

```c
#define IEEE802154_BROADCAST_PAN_ID 0xffff
```

相关声明：[IEEE802154_BROADCAST_PAN_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga1a40fed9dcd802af0283d7808e8b283b)。

表示 IEEE 802.15.4 广播 PAN ID（Broadcast PAN ID），参见 6.1 节。

<a id="r_gaf6718b4e9873d9b2e6786103ebcea1bc"></a>

```c
#define IEEE802154_SHORT_ADDRESS_NOT_ASSOCIATED IEEE802154_BROADCAST_ADDRESS
```

相关声明：[IEEE802154_SHORT_ADDRESS_NOT_ASSOCIATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gaf6718b4e9873d9b2e6786103ebcea1bc)、[IEEE802154_BROADCAST_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gafae1906dc9b39c93690b127efaaacacb)。

表示设备未关联（Not Associated）时，MAC PIB 属性 `macShortAddress` 的特殊值，参见 8.4.3 节表 8-94。

<a id="r_ga89cc35f42374255c986bcd23f15bfc14"></a>

```c
#define IEEE802154_PAN_ID_NOT_ASSOCIATED IEEE802154_BROADCAST_PAN_ID
```

相关声明：[IEEE802154_PAN_ID_NOT_ASSOCIATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga89cc35f42374255c986bcd23f15bfc14)、[IEEE802154_BROADCAST_PAN_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga1a40fed9dcd802af0283d7808e8b283b)。

表示设备未关联（Not Associated）时，MAC PIB 属性 `macPanId` 的特殊值，参见 8.4.3 节表 8-94。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.3\_枚举（Enumerations）

<a id="r_ga7a4fb2d89381bba54514bf8396fb6d26"></a>

```c
enum ieee802154_device_role { IEEE802154_DEVICE_ROLE_ENDDEVICE , IEEE802154_DEVICE_ROLE_COORDINATOR , IEEE802154_DEVICE_ROLE_PAN_COORDINATOR }
```

相关声明：[ieee802154_device_role](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga7a4fb2d89381bba54514bf8396fb6d26)、[IEEE802154_DEVICE_ROLE_ENDDEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gga7a4fb2d89381bba54514bf8396fb6d26a9909ce934f56e6b5b6c1bc53345a65b5)、[IEEE802154_DEVICE_ROLE_COORDINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gga7a4fb2d89381bba54514bf8396fb6d26abc23f55210c7ff0747bddc9c679b4f68)、[IEEE802154_DEVICE_ROLE_PAN_COORDINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gga7a4fb2d89381bba54514bf8396fb6d26a2b25d9e19f374d3f3ef6329bdf942340)。

IEEE 802.15.4 设备角色（Device Role）。


## 12.4\_原页交叉引用（Cross References）

- [limits.h](../api_source_runtime_reference/P039_limits.h_源码浏览.md)
- [zephyr/net/net_l2.h](../api_source_reference/P575_net_l2.h_源码浏览.md)
- [zephyr/net/net_mgmt.h](../api_source_timing_sensor_reference/P009_net_mgmt.h_源码浏览.md)
- [zephyr/crypto/cipher.h](../crypto/P014_密码算法头文件源码.md)
- [zephyr/net/ieee802154_radio.h](../api_source_network_reference/P010_ieee802154_radio.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P031_ieee802154.h_源码浏览.md)
- [ieee802154_security_ctx](../network_core_model_reference/P044_ieee802154_security_ctx_结构体.md)
- [ieee802154_context](../network_core_model_reference/P015_ieee802154_context_结构体.md)
- [IEEE802154_MAX_PHY_PACKET_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gac63b5ae7ed99b168871b5fc08ecde7a1)
- [IEEE802154_FCS_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga1243000b59167777e078060fd3c1c218)
- [IEEE802154_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga987d42d1d8117ec58cf3f9cae4e66139)
- [IEEE802154_SHORT_ADDR_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gaee7ec8e4ba396f3cd658bcb22a9352e8)
- [IEEE802154_EXT_ADDR_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga355350794ec26788bc855da53d311bea)
- [IEEE802154_MAX_ADDR_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gae405ed23baf91fa3d96c81d5121faa1a)
- [IEEE802154_NO_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga692a16d957c1e1ce76808cda325fd6c5)
- [IEEE802154_BROADCAST_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gafae1906dc9b39c93690b127efaaacacb)
- [IEEE802154_NO_SHORT_ADDRESS_ASSIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga43369b4a9ea0961395cd135b9fe18d03)
- [IEEE802154_BROADCAST_PAN_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga1a40fed9dcd802af0283d7808e8b283b)
- [IEEE802154_SHORT_ADDRESS_NOT_ASSOCIATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gaf6718b4e9873d9b2e6786103ebcea1bc)
- [IEEE802154_PAN_ID_NOT_ASSOCIATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga89cc35f42374255c986bcd23f15bfc14)
- [ieee802154_device_role](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga7a4fb2d89381bba54514bf8396fb6d26)
- [IEEE802154_DEVICE_ROLE_ENDDEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gga7a4fb2d89381bba54514bf8396fb6d26a9909ce934f56e6b5b6c1bc53345a65b5)
- [IEEE802154_DEVICE_ROLE_COORDINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gga7a4fb2d89381bba54514bf8396fb6d26abc23f55210c7ff0747bddc9c679b4f68)
- [IEEE802154_DEVICE_ROLE_PAN_COORDINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#gga7a4fb2d89381bba54514bf8396fb6d26a2b25d9e19f374d3f3ef6329bdf942340)

<a id="header-details"></a>

---

[上一章](P011_zephyr__platform__hooks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__dt-bindings__sensor__lps2xdf.h_文件参考.md)
