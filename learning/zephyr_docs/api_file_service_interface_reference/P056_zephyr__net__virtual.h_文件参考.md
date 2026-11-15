---
id: learning.zephyr-docs.api-file-service-interface-reference.page-56
title: zephyr__net__virtual.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_zephyr\_\_net\_\_virtual.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

虚拟网络接口（Virtual Network Interface）。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/sys/util.h>
#include <zephyr/net/net_if.h>
```

查看此文件的源码。

虚拟网络接口（Virtual Network Interface）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 56.1\_数据结构（Data Structures）

<a id="r_virtual_5Finterface_5Fapi"></a>

```c
struct virtual_interface_api
```

相关声明：[virtual_interface_api](../network_service_model_reference/P068_virtual_interface_api_结构体.md)。

虚拟第二层（Virtual L2）的API操作。

<a id="r_virtual_5Finterface_5Fcontext"></a>

```c
struct virtual_interface_context
```

相关声明：[virtual_interface_context](../network_service_model_reference/P069_virtual_interface_context_结构体.md)。

绑定到实际网络接口所需的虚拟第二层（Virtual L2）上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 56.2\_宏定义（Macros）

<a id="r_ga74a5c258a08397f881a8922516ac5d3a"></a>

```c
#define NET_VIRTUAL_INTERFACE_INIT(dev_id, name, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[NET_VIRTUAL_INTERFACE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga74a5c258a08397f881a8922516ac5d3a)。

创建虚拟网络接口（Virtual Network Interface）。

<a id="r_ga1846d4173bcd4b40a05b70c5fde18f91"></a>

```c
#define NET_VIRTUAL_INTERFACE_INIT_INSTANCE(dev_id, name, inst, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[NET_VIRTUAL_INTERFACE_INIT_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga1846d4173bcd4b40a05b70c5fde18f91)。

创建虚拟网络接口（Virtual Network Interface）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 56.3\_枚举（Enumerations）

<a id="r_ga8f188f5c2f19960d7113da52aefe8091"></a>

```c
enum virtual_interface_caps { VIRTUAL_INTERFACE_IPIP = BIT(1) , VIRTUAL_INTERFACE_VLAN = BIT(2) , VIRTUAL_INTERFACE_BRIDGE = BIT(3) , VIRTUAL_INTERFACE_VPN = BIT(4) }
```

相关声明：[virtual_interface_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga8f188f5c2f19960d7113da52aefe8091)、[VIRTUAL_INTERFACE_IPIP](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071)、[VIRTUAL_INTERFACE_VLAN](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b)、[VIRTUAL_INTERFACE_BRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed)、[VIRTUAL_INTERFACE_VPN](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a145ffaeae08793e4c93ea7be320efe2b)。

虚拟接口能力（Virtual Interface Capabilities）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 56.4\_函数（Functions）

<a id="r_ga5cba6ff65402b591a0e42d05f258671f"></a>

```c
int net_virtual_interface_attach (struct net_if *virtual_iface, struct net_if *iface)
```

相关声明：[net_virtual_interface_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga5cba6ff65402b591a0e42d05f258671f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将虚拟网络接口（Virtual Network Interface）附接到指定网络接口。

<a id="r_gabadf14eaa02978cde7030c99ddd3e279"></a>

```c
struct net_if * net_virtual_get_iface (struct net_if *iface)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_virtual_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gabadf14eaa02978cde7030c99ddd3e279)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回与此虚拟网络接口关联的网络接口。

<a id="r_gaa7ff8ebb83fe98a1dfd23f319317a8de"></a>

```c
char * net_virtual_get_name (struct net_if *iface, char *buf, size_t len)
```

相关声明：[net_virtual_get_name](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gaa7ff8ebb83fe98a1dfd23f319317a8de)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回虚拟网络接口二层（L2）的名称。

<a id="r_ga2aaba616ed4fecc27138d5aae58a634f"></a>

```c
void net_virtual_set_name (struct net_if *iface, const char *name)
```

相关声明：[net_virtual_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga2aaba616ed4fecc27138d5aae58a634f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置虚拟网络接口二层（L2）的名称。

<a id="r_ga30f92f519a6f204ebeccd6053f17eaf0"></a>

```c
enum net_l2_flags net_virtual_set_flags (struct net_if *iface, enum net_l2_flags flags)
```

相关声明：[net_l2_flags](../api_protocol_topic_reference/P040_网络二层抽象层（Network L2 Abstraction Layer）.md#gac7db0cc6c56d371a5803873074ec2516)、[net_virtual_set_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga30f92f519a6f204ebeccd6053f17eaf0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_l2_flags](../api_protocol_topic_reference/P040_网络二层抽象层（Network L2 Abstraction Layer）.md#gac7db0cc6c56d371a5803873074ec2516)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

设置虚拟网络接口的二层（L2）标志。

<a id="r_ga6c63773925ef7d96b0ba03d8978fd499"></a>

```c
enum net_verdict net_virtual_input (struct net_if *input_iface, struct net_addr *remote_addr, struct net_pkt *pkt)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_virtual_input](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga6c63773925ef7d96b0ba03d8978fd499)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

若启用隧道（Tunneling），则将 IP 数据包送入协议栈（Stack）。


## 56.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h_source.html)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P055_virtual.h_源码浏览.md)
- [virtual_interface_api](../network_service_model_reference/P068_virtual_interface_api_结构体.md)
- [virtual_interface_context](../network_service_model_reference/P069_virtual_interface_context_结构体.md)
- [NET_VIRTUAL_INTERFACE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga74a5c258a08397f881a8922516ac5d3a)
- [NET_VIRTUAL_INTERFACE_INIT_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga1846d4173bcd4b40a05b70c5fde18f91)
- [virtual_interface_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga8f188f5c2f19960d7113da52aefe8091)
- [VIRTUAL_INTERFACE_IPIP](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071)
- [VIRTUAL_INTERFACE_VLAN](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b)
- [VIRTUAL_INTERFACE_BRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed)
- [VIRTUAL_INTERFACE_VPN](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a145ffaeae08793e4c93ea7be320efe2b)
- [net_virtual_interface_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga5cba6ff65402b591a0e42d05f258671f)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_virtual_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gabadf14eaa02978cde7030c99ddd3e279)
- [net_virtual_get_name](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gaa7ff8ebb83fe98a1dfd23f319317a8de)
- [net_virtual_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga2aaba616ed4fecc27138d5aae58a634f)
- [net_l2_flags](../api_protocol_topic_reference/P040_网络二层抽象层（Network L2 Abstraction Layer）.md#gac7db0cc6c56d371a5803873074ec2516)
- [net_virtual_set_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga30f92f519a6f204ebeccd6053f17eaf0)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [net_virtual_input](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga6c63773925ef7d96b0ba03d8978fd499)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)

<a id="header-details"></a>

---

[上一章](P055_zephyr__modem__at__user_pipe.h_文件参考.md) · [返回大纲](大纲.md)
