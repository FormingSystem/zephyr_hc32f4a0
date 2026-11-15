---
id: learning.zephyr-docs.network-service-model-reference.page-2
title: dsa_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdsa__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_dsa\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdsa__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

提供分布式交换架构（DSA）交换机API回调的结构；它扩展了struct ethernet_api。

```c
#include <zephyr/net/dsa_core.h>
```

<a id="details"></a>

提供分布式交换架构（DSA）交换机API回调的结构；它扩展了struct ethernet_api。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_af715363f30777917905a6e0b94059a8d"></a>

```c
struct net_if *(* recv )(struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[recv](#af715363f30777917905a6e0b94059a8d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

分布式交换架构（DSA）辅助回调。

<a id="r_aae906b6ec5bff5a7fbba1bf43312e71d"></a>

```c
struct net_pkt *(* xmit )(struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[xmit](#aae906b6ec5bff5a7fbba1bf43312e71d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

在用户端口（user port）上发送带标签（tagging）的数据包。

<a id="r_a5117a72ebe047a23f18e168282b74a30"></a>

```c
int(* port_init )(const struct device *dev)
```

相关声明：[port_init](#a5117a72ebe047a23f18e168282b74a30)、[device](../device_reference/P002_设备对象结构.md)。

端口初始化。

<a id="r_ae93ff737cfc6f911e0972b28988f8d1b"></a>

```c
void(* port_phylink_change )(const struct device *phy_dev, struct phy_link_state *state, const struct device *dev)
```

相关声明：[port_phylink_change](#ae93ff737cfc6f911e0972b28988f8d1b)、[device](../device_reference/P002_设备对象结构.md)、[phy_link_state](P040_phy_link_state_结构体.md)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)、[device](../device_reference/P002_设备对象结构.md)。

端口链路变化。

<a id="r_aca5e37c3e5a441ddca1403ac733e011d"></a>

```c
int(* port_txtstamp )(const struct device *dev, struct net_pkt *pkt)
```

相关声明：[port_txtstamp](#aca5e37c3e5a441ddca1403ac733e011d)、[device](../device_reference/P002_设备对象结构.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

端口发送（TX）时间戳处理。

<a id="r_a3ad664182c5cee8786600d4dcd9bae1a"></a>

```c
int(* switch_setup )(const struct dsa_switch_context *dsa_switch_ctx)
```

相关声明：[switch_setup](#a3ad664182c5cee8786600d4dcd9bae1a)、[dsa_switch_context](P004_dsa_switch_context_结构体.md)。

交换机设置（Switch setup）。

<a id="r_aa72473bfb8a85f95f4d3b56cd87e7257"></a>

```c
int(* connect_tag_protocol )(struct dsa_switch_context *dsa_switch_ctx, int tag_proto)
```

相关声明：[connect_tag_protocol](#aa72473bfb8a85f95f4d3b56cd87e7257)、[dsa_switch_context](P004_dsa_switch_context_结构体.md)。

将交换机连接到标签协议（tag protocol）。

<a id="r_a7d0809973c38681d5e35613ce999fa1c"></a>

```c
enum ethernet_hw_caps(* get_capabilities )(const struct device *dev)
```

相关声明：[ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)、[get_capabilities](#a7d0809973c38681d5e35613ce999fa1c)、[device](../device_reference/P002_设备对象结构.md)。

获取设备能力（capabilities）。

<a id="r_ae941da97713f1e3511c03509b1f2386f"></a>

```c
int(* set_config )(const struct device *dev, enum ethernet_config_type type, const struct ethernet_config *config)
```

相关声明：[set_config](#ae941da97713f1e3511c03509b1f2386f)、[device](../device_reference/P002_设备对象结构.md)。

设置特定的硬件配置。

<a id="r_a1893ae289acf61ce96d9ad9bb11f43d9"></a>

```c
int(* get_config )(const struct device *dev, enum ethernet_config_type type, struct ethernet_config *config)
```

相关声明：[get_config](#a1893ae289acf61ce96d9ad9bb11f43d9)、[device](../device_reference/P002_设备对象结构.md)。

获取硬件专用配置。

## 2.2\_详细说明（Detailed Documentation）

<a id="aa72473bfb8a85f95f4d3b56cd87e7257"></a>

### `connect_tag_protocol`

```c
int(* dsa_api::connect_tag_protocol) (struct dsa_switch_context *dsa_switch_ctx, int tag_proto)
```

将交换机连接到标签协议（tag protocol）。

<a id="a7d0809973c38681d5e35613ce999fa1c"></a>

### `get_capabilities`

```c
enum ethernet_hw_caps(* dsa_api::get_capabilities) (const struct device *dev)
```

获取设备能力（capabilities）。

<a id="a1893ae289acf61ce96d9ad9bb11f43d9"></a>

### `get_config`

```c
int(* dsa_api::get_config) (const struct device *dev, enum ethernet_config_type type, struct ethernet_config *config)
```

获取硬件专用配置。

<a id="a5117a72ebe047a23f18e168282b74a30"></a>

### `port_init`

```c
int(* dsa_api::port_init) (const struct device *dev)
```

端口初始化。

<a id="ae93ff737cfc6f911e0972b28988f8d1b"></a>

### `port_phylink_change`

```c
void(* dsa_api::port_phylink_change) (const struct device *phy_dev, struct phy_link_state *state, const struct device *dev)
```

端口链路变化。

<a id="aca5e37c3e5a441ddca1403ac733e011d"></a>

### `port_txtstamp`

```c
int(* dsa_api::port_txtstamp) (const struct device *dev, struct net_pkt *pkt)
```

端口发送（TX）时间戳处理。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_NET_L2_PTP_TIMESTAMPING`。

<a id="af715363f30777917905a6e0b94059a8d"></a>

### `recv`

```c
struct net_if *(* dsa_api::recv) (struct net_if *iface, struct net_pkt *pkt)
```

分布式交换架构（DSA）辅助回调。

处理传输端口（conduit port）接收到的数据包，进行去标签（untagging）及重定向。

<a id="ae941da97713f1e3511c03509b1f2386f"></a>

### `set_config`

```c
int(* dsa_api::set_config) (const struct device *dev, enum ethernet_config_type type, const struct ethernet_config *config)
```

设置特定的硬件配置。

<a id="a3ad664182c5cee8786600d4dcd9bae1a"></a>

### `switch_setup`

```c
int(* dsa_api::switch_setup) (const struct dsa_switch_context *dsa_switch_ctx)
```

交换机设置（Switch setup）。

<a id="aae906b6ec5bff5a7fbba1bf43312e71d"></a>

### `xmit`

```c
struct net_pkt *(* dsa_api::xmit) (struct net_if *iface, struct net_pkt *pkt)
```

在用户端口（user port）上发送带标签（tagging）的数据包。

本数据类型文档由以下文件生成：

- `zephyr/net/dsa_core.h`

## 2.3\_原页交叉引用（Cross References）

- [ethernet_api](P007_ethernet_api_结构体.md)
- [zephyr/net/dsa_core.h](https://docs.zephyrproject.org/latest/doxygen/html/dsa__core_8h_source.html)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [phy_link_state](P040_phy_link_state_结构体.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [dsa_switch_context](P004_dsa_switch_context_结构体.md)
- [ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)
- [CONFIG_NET_L2_PTP_TIMESTAMPING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_canbus_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_dsa_port_config_结构体.md)
