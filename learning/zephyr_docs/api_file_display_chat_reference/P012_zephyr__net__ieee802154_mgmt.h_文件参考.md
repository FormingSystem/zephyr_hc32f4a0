---
id: learning.zephyr-docs.api-file-display-chat-reference.page-12
title: zephyr__net__ieee802154_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_net\_\_ieee802154\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.15.4管理（Management）接口的公共头文件。

<a id="details"></a>

```c
#include <zephyr/net/ieee802154.h>
#include <zephyr/net/net_mgmt.h>
```

查看此文件的源码。

IEEE 802.15.4 管理接口（Management Interface）公共头文件。注意（Note）：本文件对该标准的所有引用均指向 IEEE 802.15.4-2020。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_ieee802154_5Freq_5Fparams"></a>

```c
struct ieee802154_req_params
```

相关声明：[ieee802154_req_params](../network_core_model_reference/P042_ieee802154_req_params_结构体.md)。

扫描参数（Scanning Parameters）。

<a id="r_ieee802154_5Fsecurity_5Fparams"></a>

```c
struct ieee802154_security_params
```

相关声明：[ieee802154_security_params](../network_core_model_reference/P045_ieee802154_security_params_结构体.md)。

安全参数（Security Parameters）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 命令宏（Command Macros）

IEEE 802.15.4 网络管理命令（Net Management Commands）。

应用可以通过网络管理宏（Network Management Macro）调用这些 IEEE 802.15.4 子系统网络管理命令。

除非另有说明，所有属性和参数中的标量（Scalars）采用 CPU 字节序，字节数组（Byte Arrays）采用大端字节序（Big Endian）。

此枚举引用了以下 IEEE 802.15.4 MAC 管理服务原语（Management Service Primitives）：

此枚举引用了以下 IEEE 802.15.4 MAC 数据服务原语（Data Service Primitives）：

MAC PIB 属性（mac.../sec...）：参见第 8.4.3 节和第 9.5 节。PHY PIB 属性（phy...）：参见第 11.3 节。两者均通过 MLME-SET/GET 原语（Primitives）访问。

<a id="r_ga9fb911bed94845e723d686ded38929da"></a>

```c
#define NET_REQUEST_IEEE802154_SET_ACK (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_SET_ACK)
```

相关声明：[NET_REQUEST_IEEE802154_SET_ACK](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga9fb911bed94845e723d686ded38929da)。

为所有后续 MLME-DATA（即 TX）请求设置 AckTx。

<a id="r_gafa484eb90d0c8d3d7ef01b5a7edb2a18"></a>

```c
#define NET_REQUEST_IEEE802154_UNSET_ACK (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_UNSET_ACK)
```

相关声明：[NET_REQUEST_IEEE802154_UNSET_ACK](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gafa484eb90d0c8d3d7ef01b5a7edb2a18)。

为所有后续 MLME-DATA 请求清除 AckTx。

<a id="r_ga72d022935a39436e95f61cceb8001ed9"></a>

```c
#define NET_REQUEST_IEEE802154_PASSIVE_SCAN (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_PASSIVE_SCAN)
```

相关声明：[NET_REQUEST_IEEE802154_PASSIVE_SCAN](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga72d022935a39436e95f61cceb8001ed9)。

MLME-SCAN(PASSIVE, ...) 请求（Request）。

<a id="r_gab7ad1a0db3c9a361eab52e0cf484d11b"></a>

```c
#define NET_REQUEST_IEEE802154_ACTIVE_SCAN (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_ACTIVE_SCAN)
```

相关声明：[NET_REQUEST_IEEE802154_ACTIVE_SCAN](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gab7ad1a0db3c9a361eab52e0cf484d11b)。

MLME-SCAN(ACTIVE, ...) 请求（Request）。

<a id="r_gaefba66b873c90b3db1ad9bfce98ceebe"></a>

```c
#define NET_REQUEST_IEEE802154_CANCEL_SCAN (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_CANCEL_SCAN)
```

相关声明：[NET_REQUEST_IEEE802154_CANCEL_SCAN](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gaefba66b873c90b3db1ad9bfce98ceebe)。

取消正在进行的 MLME-SCAN(...) 命令，属于非标准操作（Non-standard）。

<a id="r_ga01e2180457cd99095e56ae3fa9f79dbf"></a>

```c
#define NET_REQUEST_IEEE802154_ASSOCIATE (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_ASSOCIATE)
```

相关声明：[NET_REQUEST_IEEE802154_ASSOCIATE](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga01e2180457cd99095e56ae3fa9f79dbf)。

MLME-ASSOCIATE(...) 请求（Request）。

<a id="r_gace7c47eba4e022f54000932814ce4edd"></a>

```c
#define NET_REQUEST_IEEE802154_DISASSOCIATE (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_DISASSOCIATE)
```

相关声明：[NET_REQUEST_IEEE802154_DISASSOCIATE](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gace7c47eba4e022f54000932814ce4edd)。

MLME-DISASSOCIATE(...) 请求（Request）。

<a id="r_ga5cc7d53ae273c9977de07305efbc0ced"></a>

```c
#define NET_REQUEST_IEEE802154_SET_CHANNEL (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_SET_CHANNEL)
```

相关声明：[NET_REQUEST_IEEE802154_SET_CHANNEL](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga5cc7d53ae273c9977de07305efbc0ced)。

MLME-SET(phyCurrentChannel) 请求（Request）。

<a id="r_gad154b4b5affb3a8a59226a241c84a14b"></a>

```c
#define NET_REQUEST_IEEE802154_GET_CHANNEL (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_GET_CHANNEL)
```

相关声明：[NET_REQUEST_IEEE802154_GET_CHANNEL](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gad154b4b5affb3a8a59226a241c84a14b)。

MLME-GET(phyCurrentChannel) 请求（Request）。

<a id="r_ga9428b28728e2060586761e1f08cf983c"></a>

```c
#define NET_REQUEST_IEEE802154_SET_PAN_ID (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_SET_PAN_ID)
```

相关声明：[NET_REQUEST_IEEE802154_SET_PAN_ID](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga9428b28728e2060586761e1f08cf983c)。

MLME-SET(macPanId) 请求（Request）。

<a id="r_ga8a0a0c9c6b3762ebe06df860aee9431f"></a>

```c
#define NET_REQUEST_IEEE802154_GET_PAN_ID (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_GET_PAN_ID)
```

相关声明：[NET_REQUEST_IEEE802154_GET_PAN_ID](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga8a0a0c9c6b3762ebe06df860aee9431f)。

MLME-GET(macPanId) 请求（Request）。

<a id="r_gadfb408432bfd2f58eea8d695747471e9"></a>

```c
#define NET_REQUEST_IEEE802154_SET_EXT_ADDR (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_SET_EXT_ADDR)
```

相关声明：[NET_REQUEST_IEEE802154_SET_EXT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gadfb408432bfd2f58eea8d695747471e9)。

以大端字节序（Big Endian Byte Order）设置接口扩展地址（Extended Interface Address），属于非标准操作；参见第 7.1 节和第 8.4.3.1 节。

<a id="r_gaf64388508d21c5a17896c82ef1e3ac66"></a>

```c
#define NET_REQUEST_IEEE802154_GET_EXT_ADDR (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_GET_EXT_ADDR)
```

相关声明：[NET_REQUEST_IEEE802154_GET_EXT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gaf64388508d21c5a17896c82ef1e3ac66)。

类似 MLME-GET(macExtendedAddress)，但采用大端字节序（Big Endian Byte Order）。

<a id="r_ga9b5411f4d458421c0528e0e850c54465"></a>

```c
#define NET_REQUEST_IEEE802154_SET_SHORT_ADDR (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_SET_SHORT_ADDR)
```

相关声明：[NET_REQUEST_IEEE802154_SET_SHORT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga9b5411f4d458421c0528e0e850c54465)。

MLME-SET(macShortAddress) 请求，仅允许协调器（Co-ordinators）使用。

<a id="r_ga60b38fa4a0a1248e5e491cd7b2b85241"></a>

```c
#define NET_REQUEST_IEEE802154_GET_SHORT_ADDR (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_GET_SHORT_ADDR)
```

相关声明：[NET_REQUEST_IEEE802154_GET_SHORT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga60b38fa4a0a1248e5e491cd7b2b85241)。

MLME-GET(macShortAddress) 请求（Request）。

<a id="r_ga09451cec03058d5936c98722f7110965"></a>

```c
#define NET_REQUEST_IEEE802154_SET_COORD_SHORT_ADDR (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_SET_COORD_SHORT_ADDR)
```

相关声明：[NET_REQUEST_IEEE802154_SET_COORD_SHORT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga09451cec03058d5936c98722f7110965)。

MLME-SET(macCoordShortAddress) 请求（Request）。

<a id="r_gacf3d54e1dc130e3f76ef26ed00bfe778"></a>

```c
#define NET_REQUEST_IEEE802154_GET_COORD_SHORT_ADDR (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_GET_COORD_SHORT_ADDR)
```

相关声明：[NET_REQUEST_IEEE802154_GET_COORD_SHORT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gacf3d54e1dc130e3f76ef26ed00bfe778)。

MLME-GET(macCoordShortAddress) 请求（Request）。

<a id="r_gaf6f6083f63bfb8dff4c85ec90d0ea306"></a>

```c
#define NET_REQUEST_IEEE802154_SET_COORD_EXT_ADDR (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_SET_COORD_EXT_ADDR)
```

相关声明：[NET_REQUEST_IEEE802154_SET_COORD_EXT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gaf6f6083f63bfb8dff4c85ec90d0ea306)。

MLME-SET(macCoordExtendedAddress) 请求（Request）。

<a id="r_ga486101e2d7293118d80418a8e00877f2"></a>

```c
#define NET_REQUEST_IEEE802154_GET_COORD_EXT_ADDR (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_GET_COORD_EXT_ADDR)
```

相关声明：[NET_REQUEST_IEEE802154_GET_COORD_EXT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga486101e2d7293118d80418a8e00877f2)。

MLME-GET(macCoordExtendedAddress) 请求（Request）。

<a id="r_ga07062abc2ce8ebb326e89bee768c3638"></a>

```c
#define NET_REQUEST_IEEE802154_GET_TX_POWER (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_GET_TX_POWER)
```

相关声明：[NET_REQUEST_IEEE802154_GET_TX_POWER](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga07062abc2ce8ebb326e89bee768c3638)。

MLME-SET(phyUnicastTxPower/phyBroadcastTxPower) 请求，当前不区分二者。

<a id="r_ga4399c84db1c15406685d218a2e1190f4"></a>

```c
#define NET_REQUEST_IEEE802154_SET_TX_POWER (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_SET_TX_POWER)
```

相关声明：[NET_REQUEST_IEEE802154_SET_TX_POWER](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga4399c84db1c15406685d218a2e1190f4)。

MLME-GET(phyUnicastTxPower/phyBroadcastTxPower) 请求（Request）。

<a id="r_ga907b00f07cdbe9fe33e19ec323d56654"></a>

```c
#define NET_REQUEST_IEEE802154_SET_SECURITY_SETTINGS (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_SET_SECURITY_SETTINGS)
```

相关声明：[NET_REQUEST_IEEE802154_SET_SECURITY_SETTINGS](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga907b00f07cdbe9fe33e19ec323d56654)。

配置基本的 `sec*` MAC PIB 属性（Attributes），同时隐含设置 macSecurityEnabled=true。

<a id="r_ga120d2a00dd3ade6d413e1763c41075df"></a>

```c
#define NET_REQUEST_IEEE802154_GET_SECURITY_SETTINGS (NET_IEEE802154_BASE | NET_REQUEST_IEEE802154_CMD_GET_SECURITY_SETTINGS)
```

相关声明：[NET_REQUEST_IEEE802154_GET_SECURITY_SETTINGS](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga120d2a00dd3ade6d413e1763c41075df)。

获取已配置的 `sec*` 属性（Attributes）。

<a id="define-members-1"></a>

### 事件宏（Event Macros）

IEEE 802.15.4 网络管理事件（Net Management Events）。

应用可以通过 net_mgmt_init_event_callback、net_mgmt_add_event_callback 和 net_mgmt_del_event_callback 订阅这些 IEEE 802.15.4 子系统网络管理事件。

<a id="r_ga0442eaa04068a7b66f9b4ae40b570470"></a>

```c
#define NET_EVENT_IEEE802154_SCAN_RESULT (NET_IEEE802154_EVENT | NET_EVENT_IEEE802154_CMD_SCAN_RESULT)
```

相关声明：[NET_EVENT_IEEE802154_SCAN_RESULT](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga0442eaa04068a7b66f9b4ae40b570470)。

通知 NET_REQUEST_IEEE802154_ACTIVE_SCAN 或 NET_REQUEST_IEEE802154_PASSIVE_SCAN 网络管理命令（Net Management Commands）的结果。


## 12.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154.h](../api_source_configuration_reference/P031_ieee802154.h_源码浏览.md)
- [zephyr/net/net_mgmt.h](../api_source_timing_sensor_reference/P009_net_mgmt.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P339_ieee802154_mgmt.h_源码浏览.md)
- [ieee802154_req_params](../network_core_model_reference/P042_ieee802154_req_params_结构体.md)
- [ieee802154_security_params](../network_core_model_reference/P045_ieee802154_security_params_结构体.md)
- [网络管理（Network Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html)
- [NET_REQUEST_IEEE802154_SET_ACK](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga9fb911bed94845e723d686ded38929da)
- [NET_REQUEST_IEEE802154_UNSET_ACK](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gafa484eb90d0c8d3d7ef01b5a7edb2a18)
- [NET_REQUEST_IEEE802154_PASSIVE_SCAN](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga72d022935a39436e95f61cceb8001ed9)
- [NET_REQUEST_IEEE802154_ACTIVE_SCAN](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gab7ad1a0db3c9a361eab52e0cf484d11b)
- [NET_REQUEST_IEEE802154_CANCEL_SCAN](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gaefba66b873c90b3db1ad9bfce98ceebe)
- [NET_REQUEST_IEEE802154_ASSOCIATE](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga01e2180457cd99095e56ae3fa9f79dbf)
- [NET_REQUEST_IEEE802154_DISASSOCIATE](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gace7c47eba4e022f54000932814ce4edd)
- [NET_REQUEST_IEEE802154_SET_CHANNEL](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga5cc7d53ae273c9977de07305efbc0ced)
- [NET_REQUEST_IEEE802154_GET_CHANNEL](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gad154b4b5affb3a8a59226a241c84a14b)
- [NET_REQUEST_IEEE802154_SET_PAN_ID](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga9428b28728e2060586761e1f08cf983c)
- [NET_REQUEST_IEEE802154_GET_PAN_ID](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga8a0a0c9c6b3762ebe06df860aee9431f)
- [NET_REQUEST_IEEE802154_SET_EXT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gadfb408432bfd2f58eea8d695747471e9)
- [NET_REQUEST_IEEE802154_GET_EXT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gaf64388508d21c5a17896c82ef1e3ac66)
- [NET_REQUEST_IEEE802154_SET_SHORT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga9b5411f4d458421c0528e0e850c54465)
- [NET_REQUEST_IEEE802154_GET_SHORT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga60b38fa4a0a1248e5e491cd7b2b85241)
- [NET_REQUEST_IEEE802154_SET_COORD_SHORT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga09451cec03058d5936c98722f7110965)
- [NET_REQUEST_IEEE802154_GET_COORD_SHORT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gacf3d54e1dc130e3f76ef26ed00bfe778)
- [NET_REQUEST_IEEE802154_SET_COORD_EXT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#gaf6f6083f63bfb8dff4c85ec90d0ea306)
- [NET_REQUEST_IEEE802154_GET_COORD_EXT_ADDR](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga486101e2d7293118d80418a8e00877f2)
- [NET_REQUEST_IEEE802154_GET_TX_POWER](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga07062abc2ce8ebb326e89bee768c3638)
- [NET_REQUEST_IEEE802154_SET_TX_POWER](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga4399c84db1c15406685d218a2e1190f4)
- [NET_REQUEST_IEEE802154_SET_SECURITY_SETTINGS](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga907b00f07cdbe9fe33e19ec323d56654)
- [NET_REQUEST_IEEE802154_GET_SECURITY_SETTINGS](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga120d2a00dd3ade6d413e1763c41075df)
- [net_mgmt_init_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga4e42b6d16b863ca374d032682e8c11fb)
- [net_mgmt_add_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae53f5bbc973b0f414107eca75ac0c26f)
- [net_mgmt_del_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga4960bfb01ecd891da72c57f17587f946)
- [NET_EVENT_IEEE802154_SCAN_RESULT](../api_memory_network_topic_reference/P013_IEEE 802.15.4 网络管理（Net Management）.md#ga0442eaa04068a7b66f9b4ae40b570470)

<a id="header-details"></a>

---

[上一章](P011_zephyr__drivers__i2s.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__dt-bindings__clock__imx_ccm_rev3.h_文件参考.md)
