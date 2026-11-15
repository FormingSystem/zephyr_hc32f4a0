---
id: learning.zephyr-docs.network-service-model-reference.page-68
title: virtual_interface_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtual__interface__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_virtual\_interface\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvirtual__interface__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

虚拟第二层（Virtual L2）的API操作。

```c
#include <zephyr/net/virtual.h>
```

<a id="details"></a>

虚拟第二层（Virtual L2）的API操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_aee1250773938536ab28e129113073ae7"></a>

```c
struct net_if_api iface_api
```

相关声明：[iface_api](#aee1250773938536ab28e129113073ae7)。

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="r_a827cd13d885b7cc2f80eddd73e438e07"></a>

```c
enum virtual_interface_caps(* get_capabilities )(struct net_if *iface)
```

相关声明：[virtual_interface_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga8f188f5c2f19960d7113da52aefe8091)、[get_capabilities](#a827cd13d885b7cc2f80eddd73e438e07)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取虚拟接口（virtual interface）的能力。

<a id="r_af28a6ed36799006d185fab9129c6c120"></a>

```c
int(* start )(const struct device *dev)
```

相关声明：[start](#af28a6ed36799006d185fab9129c6c120)、[device](../device_reference/P002_设备对象结构.md)。

启动设备（Start the Device）。

<a id="r_a09a317009d31ac5e9340c3ca7d2191c4"></a>

```c
int(* stop )(const struct device *dev)
```

相关声明：[stop](#a09a317009d31ac5e9340c3ca7d2191c4)、[device](../device_reference/P002_设备对象结构.md)。

停止设备（Stop the Device）。

<a id="r_a6fbfa013374bbafaa610b0a054d3a415"></a>

```c
int(* send )(struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[send](#a6fbfa013374bbafaa610b0a054d3a415)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

发送网络数据包。

<a id="r_a6f21e33e39caa00d51cca900a26f7070"></a>

```c
enum net_verdict(* recv )(struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)、[recv](#a6f21e33e39caa00d51cca900a26f7070)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

接收网络数据包。

<a id="r_a753258a8929347877997ca5d6a76eb8c"></a>

```c
int(* attach )(struct net_if *virtual_iface, struct net_if *iface)
```

相关声明：[attach](#a753258a8929347877997ca5d6a76eb8c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将附接信息（attachment information）传给虚拟接口。

<a id="r_a591f1b7df5313c4a225dceaa04b1eeae"></a>

```c
int(* set_config )(struct net_if *iface, enum virtual_interface_config_type type, const struct virtual_interface_config *config)
```

相关声明：[set_config](#a591f1b7df5313c4a225dceaa04b1eeae)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置特定的二层（L2）配置。

<a id="r_a4ff5b92897926616778eb6fb696ebb16"></a>

```c
int(* get_config )(struct net_if *iface, enum virtual_interface_config_type type, struct virtual_interface_config *config)
```

相关声明：[get_config](#a4ff5b92897926616778eb6fb696ebb16)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取特定的二层（L2）配置。

## 68.2\_详细说明（Detailed Documentation）

<a id="a753258a8929347877997ca5d6a76eb8c"></a>

### `attach`

```c
int(* virtual_interface_api::attach) (struct net_if *virtual_iface, struct net_if *iface)
```

将附接信息（attachment information）传给虚拟接口。

<a id="a827cd13d885b7cc2f80eddd73e438e07"></a>

### `get_capabilities`

```c
enum virtual_interface_caps(* virtual_interface_api::get_capabilities) (struct net_if *iface)
```

获取虚拟接口（virtual interface）的能力。

<a id="a4ff5b92897926616778eb6fb696ebb16"></a>

### `get_config`

```c
int(* virtual_interface_api::get_config) (struct net_if *iface, enum virtual_interface_config_type type, struct virtual_interface_config *config)
```

获取特定的二层（L2）配置。

<a id="aee1250773938536ab28e129113073ae7"></a>

### `iface_api`

```c
struct net_if_api virtual_interface_api::iface_api
```

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="a6f21e33e39caa00d51cca900a26f7070"></a>

### `recv`

```c
enum net_verdict(* virtual_interface_api::recv) (struct net_if *iface, struct net_pkt *pkt)
```

接收网络数据包。

如果此接口接受数据包并将其交给上层，回调返回 `NET_OK`；如果应丢弃数据包，返回 `NET_DROP`；如果要交给下一个接口，返回 `NET_CONTINUE`。

<a id="a6fbfa013374bbafaa610b0a054d3a415"></a>

### `send`

```c
int(* virtual_interface_api::send) (struct net_if *iface, struct net_pkt *pkt)
```

发送网络数据包。

<a id="a591f1b7df5313c4a225dceaa04b1eeae"></a>

### `set_config`

```c
int(* virtual_interface_api::set_config) (struct net_if *iface, enum virtual_interface_config_type type, const struct virtual_interface_config *config)
```

设置特定的二层（L2）配置。

<a id="af28a6ed36799006d185fab9129c6c120"></a>

### `start`

```c
int(* virtual_interface_api::start) (const struct device *dev)
```

启动设备（Start the Device）。

<a id="a09a317009d31ac5e9340c3ca7d2191c4"></a>

### `stop`

```c
int(* virtual_interface_api::stop) (const struct device *dev)
```

停止设备（Stop the Device）。

本数据类型文档由以下文件生成：

- `zephyr/net/virtual.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/net/virtual.h](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h_source.html)
- [virtual_interface_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga8f188f5c2f19960d7113da52aefe8091)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_ssh_transport_event_channel_open_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_virtual_interface_context_结构体.md)
