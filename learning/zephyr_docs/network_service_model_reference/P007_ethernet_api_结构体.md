---
id: learning.zephyr-docs.network-service-model-reference.page-7
title: ethernet_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structethernet__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_ethernet\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网第二层（Ethernet L2）的API操作。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

以太网第二层（Ethernet L2）的API操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a03dfbaed9cdf2bdd17b0bfd28d5a1056"></a>

```c
struct net_if_api iface_api
```

相关声明：[iface_api](#a03dfbaed9cdf2bdd17b0bfd28d5a1056)。

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="r_a4ebe0d6cf70a7b5a1fff87c3ca6cb86e"></a>

```c
int(* start )(const struct device *dev, struct net_if *iface)
```

相关声明：[start](#a4ebe0d6cf70a7b5a1fff87c3ca6cb86e)、[device](../device_reference/P002_设备对象结构.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

可选地收集以太网专用统计信息。

<a id="r_a8dba118b707305e1b909a82f7742dd5e"></a>

```c
int(* stop )(const struct device *dev, struct net_if *iface)
```

相关声明：[stop](#a8dba118b707305e1b909a82f7742dd5e)、[device](../device_reference/P002_设备对象结构.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停止设备（Stop the Device）。

<a id="r_ae7c0f0b5162f5fb6b1a49ce4b52249b0"></a>

```c
enum ethernet_hw_caps(* get_capabilities )(const struct device *dev, struct net_if *iface)
```

相关声明：[ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)、[get_capabilities](#ae7c0f0b5162f5fb6b1a49ce4b52249b0)、[device](../device_reference/P002_设备对象结构.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取设备能力（capabilities）。

<a id="r_aa283f6f201f50ffdd976275374f5c828"></a>

```c
int(* set_config )(const struct device *dev, struct net_if *iface, enum ethernet_config_type type, const struct ethernet_config *config)
```

相关声明：[set_config](#aa283f6f201f50ffdd976275374f5c828)、[device](../device_reference/P002_设备对象结构.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置特定的硬件配置。

<a id="r_aa34137c564f84fdb3160a767348c4a58"></a>

```c
int(* get_config )(const struct device *dev, struct net_if *iface, enum ethernet_config_type type, struct ethernet_config *config)
```

相关声明：[get_config](#aa34137c564f84fdb3160a767348c4a58)、[device](../device_reference/P002_设备对象结构.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取硬件专用配置。

<a id="r_ae8876229a4c2dc648f29c2019cdd278f"></a>

```c
const struct device *(* get_phy )(const struct device *dev, struct net_if *iface)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[get_phy](#ae8876229a4c2dc648f29c2019cdd278f)、[device](../device_reference/P002_设备对象结构.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启用或禁用虚拟局域网（VLAN）标签时，IP 协议栈将调用此函数。

<a id="r_a8f6fd0d640b5a883c9f5150d9ed71241"></a>

```c
int(* send )(const struct device *dev, struct net_pkt *pkt)
```

相关声明：[send](#a8f6fd0d640b5a883c9f5150d9ed71241)、[device](../device_reference/P002_设备对象结构.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

发送网络数据包。

## 7.2\_详细说明（Detailed Documentation）

<a id="ae7c0f0b5162f5fb6b1a49ce4b52249b0"></a>

### `get_capabilities`

```c
enum ethernet_hw_caps(* ethernet_api::get_capabilities) (const struct device *dev, struct net_if *iface)
```

获取设备能力（capabilities）。

<a id="aa34137c564f84fdb3160a767348c4a58"></a>

### `get_config`

```c
int(* ethernet_api::get_config) (const struct device *dev, struct net_if *iface, enum ethernet_config_type type, struct ethernet_config *config)
```

获取硬件专用配置。

<a id="ae8876229a4c2dc648f29c2019cdd278f"></a>

### `get_phy`

```c
const struct device *(* ethernet_api::get_phy) (const struct device *dev, struct net_if *iface)
```

启用或禁用虚拟局域网（VLAN）标签时，IP 协议栈将调用此函数。

`enable` 为 `true` 表示已添加 VLAN 标签，为 `false` 表示已移除标签。驱动可按需使用此信息。返回与此以太网设备关联的 `ptp_clock` 设备。返回与此以太网设备关联的 PHY 设备。

<a id="a03dfbaed9cdf2bdd17b0bfd28d5a1056"></a>

### `iface_api`

```c
struct net_if_api ethernet_api::iface_api
```

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="a8f6fd0d640b5a883c9f5150d9ed71241"></a>

### `send`

```c
int(* ethernet_api::send) (const struct device *dev, struct net_pkt *pkt)
```

发送网络数据包。

<a id="aa283f6f201f50ffdd976275374f5c828"></a>

### `set_config`

```c
int(* ethernet_api::set_config) (const struct device *dev, struct net_if *iface, enum ethernet_config_type type, const struct ethernet_config *config)
```

设置特定的硬件配置。

<a id="a4ebe0d6cf70a7b5a1fff87c3ca6cb86e"></a>

### `start`

```c
int(* ethernet_api::start) (const struct device *dev, struct net_if *iface)
```

可选地收集以太网专用统计信息。

如果需要为此驱动收集统计信息，驱动应设置此指针。启动设备（Start the device）。

<a id="a8dba118b707305e1b909a82f7742dd5e"></a>

### `stop`

```c
int(* ethernet_api::stop) (const struct device *dev, struct net_if *iface)
```

停止设备（Stop the Device）。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_eth_bridge_fdb_entry_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_ethernet_filter_结构体.md)
