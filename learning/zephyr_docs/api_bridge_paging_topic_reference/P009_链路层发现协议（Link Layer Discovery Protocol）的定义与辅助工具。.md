---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-9
title: 链路层发现协议（Link Layer Discovery Protocol）的定义与辅助工具。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_链路层发现协议（Link Layer Discovery Protocol）的定义与辅助工具。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LLDP 定义与辅助工具。

<a id="details"></a>

链路层发现协议（LLDP）的定义和辅助接口。自 1.13 起提供，版本 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_net_5Flldp_5Fchassis_5Ftlv"></a>

```c
struct net_lldp_chassis_tlv
```

相关声明：[net_lldp_chassis_tlv](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md)。

机箱ID类型-长度-值（Chassis ID TLV），见IEEE 802.1AB第8.5.2节。

<a id="r_net_5Flldp_5Fport_5Ftlv"></a>

```c
struct net_lldp_port_tlv
```

相关声明：[net_lldp_port_tlv](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md)。

端口ID类型-长度-值（Port ID TLV），见IEEE 802.1AB第8.5.3节。

<a id="r_net_5Flldp_5Ftime_5Fto_5Flive_5Ftlv"></a>

```c
struct net_lldp_time_to_live_tlv
```

相关声明：[net_lldp_time_to_live_tlv](../network_core_model_reference/P108_net_lldp_time_to_live_tlv_结构体.md)。

生存时间类型-长度-值（Time To Live TLV），见IEEE 802.1AB第8.5.4节。

<a id="r_net_5Flldpdu"></a>

```c
struct net_lldpdu
```

相关声明：[net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)。

按IEEE 802.1AB第8.2节“LLDPDU格式”的规定，链路层发现协议数据单元（LLDPDU）应按以下顺序包含类型-长度-值（TLV）项。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_ga961bc59567ffa2d5a4d21290d1d78407"></a>

```c
#define net_lldp_set_lldpdu(iface)
```

相关声明：[net_lldp_set_lldpdu](#ga961bc59567ffa2d5a4d21290d1d78407)。

为网络接口设置 LLDP 协议数据单元（LLDPDU）。

<a id="r_gafdd1b4cea9f560597c31a0e42d5341e0"></a>

```c
#define net_lldp_unset_lldpdu(iface)
```

相关声明：[net_lldp_unset_lldpdu](#gafdd1b4cea9f560597c31a0e42d5341e0)。

取消网络接口的 LLDP 协议数据单元（LLDPDU）设置。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.3\_类型定义（Typedefs）

<a id="r_ga1e9fb662d7cdfc3c4c68cfd0312987cf"></a>

```c
typedef enum net_verdict(* net_lldp_recv_cb_t) (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_lldp_recv_cb_t](#ga1e9fb662d7cdfc3c4c68cfd0312987cf)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

LLDP 接收数据包回调（Receive Packet Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.4\_枚举（Enumerations）

<a id="r_gadd4273e4fe55757729008ce081771899"></a>

```c
enum net_lldp_tlv_type { LLDP_TLV_END_LLDPDU = 0 , LLDP_TLV_CHASSIS_ID = 1 , LLDP_TLV_PORT_ID = 2 , LLDP_TLV_TTL = 3 , LLDP_TLV_PORT_DESC = 4 , LLDP_TLV_SYSTEM_NAME = 5 , LLDP_TLV_SYSTEM_DESC = 6 , LLDP_TLV_SYSTEM_CAPABILITIES = 7 , LLDP_TLV_MANAGEMENT_ADDR = 8 , LLDP_TLV_ORG_SPECIFIC = 127 }
```

相关声明：[net_lldp_tlv_type](#gadd4273e4fe55757729008ce081771899)、[LLDP_TLV_END_LLDPDU](#ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a)、[LLDP_TLV_CHASSIS_ID](#ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6)、[LLDP_TLV_PORT_ID](#ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45)、[LLDP_TLV_TTL](#ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c)、[LLDP_TLV_PORT_DESC](#ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0)、[LLDP_TLV_SYSTEM_NAME](#ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9)、[LLDP_TLV_SYSTEM_DESC](#ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782)、[LLDP_TLV_SYSTEM_CAPABILITIES](#ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521)、[LLDP_TLV_MANAGEMENT_ADDR](#ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5)、[LLDP_TLV_ORG_SPECIFIC](#ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad)。

类型－长度－值（TLV）类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.5\_函数（Functions）

<a id="r_ga0efa1813c537dcf02e021db60049c284"></a>

```c
int net_lldp_config (struct net_if *iface, const struct net_lldpdu *lldpdu)
```

相关声明：[net_lldp_config](#ga0efa1813c537dcf02e021db60049c284)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)。

为网络接口设置 LLDP 数据单元（Data Unit）。

<a id="r_ga9702175375a71eaab20f450291cb51ad"></a>

```c
int net_lldp_config_optional (struct net_if *iface, const uint8_t *tlv, size_t len)
```

相关声明：[net_lldp_config_optional](#ga9702175375a71eaab20f450291cb51ad)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为网络接口设置可选 LLDP TLV。

<a id="r_ga61845c96c65d6df83f422a68e31162cf"></a>

```c
int net_lldp_register_callback (struct net_if *iface, net_lldp_recv_cb_t cb)
```

相关声明：[net_lldp_register_callback](#ga61845c96c65d6df83f422a68e31162cf)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_lldp_recv_cb_t](#ga1e9fb662d7cdfc3c4c68cfd0312987cf)。

注册 LLDP 接收（Rx）回调函数。

## 9.6\_详细说明（Detailed Documentation）

<a id="ga961bc59567ffa2d5a4d21290d1d78407"></a>

### `net_lldp_set_lldpdu`

```c
#define net_lldp_set_lldpdu ( iface)
```

```c
#include <zephyr/net/lldp.h>
```

为网络接口设置 LLDP 协议数据单元（LLDPDU）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值：出错时返回小于 0 的值；若在 `lldp` 数组中找到 `iface`，则返回其索引。

<a id="gafdd1b4cea9f560597c31a0e42d5341e0"></a>

### `net_lldp_unset_lldpdu`

```c
#define net_lldp_unset_lldpdu ( iface)
```

```c
#include <zephyr/net/lldp.h>
```

取消网络接口的 LLDP 协议数据单元（LLDPDU）设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

<a id="ga1e9fb662d7cdfc3c4c68cfd0312987cf"></a>

### `net_lldp_recv_cb_t`

```c
typedef enum net_verdict(* net_lldp_recv_cb_t) (struct net_if *iface, struct net_pkt *pkt)
```

```c
#include <zephyr/net/lldp.h>
```

LLDP 接收数据包回调（Receive Packet Callback）。

接收到数据包时调用此回调函数（Callback）。它负责释放数据包，或者返回恰当的 `net_verdict`，告知协议栈需要由协议栈释放该数据包。

返回值（Returns）：

- `NET_DROP`：数据包无效、被拒绝，或希望由协议栈释放它。在这种情况下，核心协议栈会释放数据包。
- `NET_OK`：数据包已被接受；此时 `net_pkt` 的所有权（Ownership）转移给回调函数，核心网络协议栈不再管理它。

<a id="gadd4273e4fe55757729008ce081771899"></a>

### `net_lldp_tlv_type`

```c
enum net_lldp_tlv_type
```

```c
#include <zephyr/net/lldp.h>
```

类型－长度－值（TLV）类型。

请参阅 IEEE 802.1AB 标准中的表 8-1。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LLDP_TLV_END_LLDPDU` | LLDP 数据单元结束标记（End Of LLDPDU），可选。 |
| `LLDP_TLV_CHASSIS_ID` | 机箱标识符（Chassis ID），必需。 |
| `LLDP_TLV_PORT_ID` | 端口标识符（Port ID），必需。 |
| `LLDP_TLV_TTL` | 生存时间（Time To Live），必需。 |
| `LLDP_TLV_PORT_DESC` | 端口描述（Port Description），可选。 |
| `LLDP_TLV_SYSTEM_NAME` | 系统名称（System Name），可选。 |
| `LLDP_TLV_SYSTEM_DESC` | 系统描述（System Description），可选。 |
| `LLDP_TLV_SYSTEM_CAPABILITIES` | 系统能力（System Capability），可选。 |
| `LLDP_TLV_MANAGEMENT_ADDR` | 管理地址（Management Address），可选。 |
| `LLDP_TLV_ORG_SPECIFIC` | 组织特定的类型－长度－值条目（Organization-specific TLVs），可选。 |

<a id="ga0efa1813c537dcf02e021db60049c284"></a>

### `net_lldp_config()`

```c
int net_lldp_config ( struct net_if * iface, const struct net_lldpdu * lldpdu )
```

```c
#include <zephyr/net/lldp.h>
```

为网络接口设置 LLDP 数据单元（Data Unit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `lldpdu` | LLDP 数据单元结构体（Data Unit Struct）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga9702175375a71eaab20f450291cb51ad"></a>

### `net_lldp_config_optional()`

```c
int net_lldp_config_optional ( struct net_if * iface, const uint8_t * tlv, size_t len )
```

```c
#include <zephyr/net/lldp.h>
```

为网络接口设置可选 LLDP TLV。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `tlv` | 位于必需部分之后的 LLDP 可选类型－长度－值条目（Optional TLVs）。 |
| `len` | 可选 TLV 的长度（Length）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga61845c96c65d6df83f422a68e31162cf"></a>

### `net_lldp_register_callback()`

```c
int net_lldp_register_callback ( struct net_if * iface, net_lldp_recv_cb_t cb )
```

```c
#include <zephyr/net/lldp.h>
```

注册 LLDP 接收（Rx）回调函数。

注册回调函数（Callback）时，接口加入 LLDP 多播组（Multicast Group）；将回调设置为 `NULL` 时，接口离开该组。这样，对于在硬件中筛选多播帧的设备，只要存在接收方，就会把 LLDP 帧向上传递。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `cb` | 回调函数（Callback Function）；传入 `NULL` 则注销。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。


## 9.7\_原页交叉引用（Cross References）

- [net_lldp_chassis_tlv](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md)
- [net_lldp_port_tlv](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md)
- [net_lldp_time_to_live_tlv](../network_core_model_reference/P108_net_lldp_time_to_live_tlv_结构体.md)
- [net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/net/lldp.h](../api_file_service_interface_reference/P033_zephyr__net__lldp.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a"></a>
<a id="ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6"></a>
<a id="ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45"></a>
<a id="ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c"></a>
<a id="ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0"></a>
<a id="ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9"></a>
<a id="ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782"></a>
<a id="ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521"></a>
<a id="ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5"></a>
<a id="ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_BCM283x 中断控制器（Interrupt controllers）.md) · [返回大纲](大纲.md) · [下一章](P010_LSM6DSO16IS API主题.md)
