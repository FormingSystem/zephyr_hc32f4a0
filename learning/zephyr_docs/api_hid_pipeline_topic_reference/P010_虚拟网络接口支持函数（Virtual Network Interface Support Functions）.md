---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-10
title: 虚拟网络接口支持函数（Virtual Network Interface Support Functions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_虚拟网络接口支持函数（Virtual Network Interface Support Functions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

虚拟网络接口支持函数（Virtual network interface support functions）

<a id="details"></a>

虚拟网络接口（Virtual Network Interface）支持函数。自 2.6 起提供，版本 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

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

## 10.2\_宏定义（Macros）

<a id="r_ga74a5c258a08397f881a8922516ac5d3a"></a>

```c
#define NET_VIRTUAL_INTERFACE_INIT(dev_id, name, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[NET_VIRTUAL_INTERFACE_INIT](#ga74a5c258a08397f881a8922516ac5d3a)。

创建虚拟网络接口（Virtual Network Interface）。

<a id="r_ga1846d4173bcd4b40a05b70c5fde18f91"></a>

```c
#define NET_VIRTUAL_INTERFACE_INIT_INSTANCE(dev_id, name, inst, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[NET_VIRTUAL_INTERFACE_INIT_INSTANCE](#ga1846d4173bcd4b40a05b70c5fde18f91)。

创建虚拟网络接口（Virtual Network Interface）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.3\_枚举（Enumerations）

<a id="r_ga8f188f5c2f19960d7113da52aefe8091"></a>

```c
enum virtual_interface_caps { VIRTUAL_INTERFACE_IPIP = BIT(1) , VIRTUAL_INTERFACE_VLAN = BIT(2) , VIRTUAL_INTERFACE_BRIDGE = BIT(3) , VIRTUAL_INTERFACE_VPN = BIT(4) }
```

相关声明：[virtual_interface_caps](#ga8f188f5c2f19960d7113da52aefe8091)、[VIRTUAL_INTERFACE_IPIP](#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071)、[VIRTUAL_INTERFACE_VLAN](#gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b)、[VIRTUAL_INTERFACE_BRIDGE](#gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed)、[VIRTUAL_INTERFACE_VPN](#gga8f188f5c2f19960d7113da52aefe8091a145ffaeae08793e4c93ea7be320efe2b)。

虚拟接口能力（Virtual Interface Capabilities）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.4\_函数（Functions）

<a id="r_ga5cba6ff65402b591a0e42d05f258671f"></a>

```c
int net_virtual_interface_attach (struct net_if *virtual_iface, struct net_if *iface)
```

相关声明：[net_virtual_interface_attach](#ga5cba6ff65402b591a0e42d05f258671f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将虚拟网络接口（Virtual Network Interface）附接到指定网络接口。

<a id="r_gabadf14eaa02978cde7030c99ddd3e279"></a>

```c
struct net_if * net_virtual_get_iface (struct net_if *iface)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_virtual_get_iface](#gabadf14eaa02978cde7030c99ddd3e279)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回与此虚拟网络接口关联的网络接口。

<a id="r_gaa7ff8ebb83fe98a1dfd23f319317a8de"></a>

```c
char * net_virtual_get_name (struct net_if *iface, char *buf, size_t len)
```

相关声明：[net_virtual_get_name](#gaa7ff8ebb83fe98a1dfd23f319317a8de)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回虚拟网络接口二层（L2）的名称。

<a id="r_ga2aaba616ed4fecc27138d5aae58a634f"></a>

```c
void net_virtual_set_name (struct net_if *iface, const char *name)
```

相关声明：[net_virtual_set_name](#ga2aaba616ed4fecc27138d5aae58a634f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置虚拟网络接口二层（L2）的名称。

<a id="r_ga30f92f519a6f204ebeccd6053f17eaf0"></a>

```c
enum net_l2_flags net_virtual_set_flags (struct net_if *iface, enum net_l2_flags flags)
```

相关声明：[net_l2_flags](../api_protocol_topic_reference/P040_网络二层抽象层（Network L2 Abstraction Layer）.md#gac7db0cc6c56d371a5803873074ec2516)、[net_virtual_set_flags](#ga30f92f519a6f204ebeccd6053f17eaf0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_l2_flags](../api_protocol_topic_reference/P040_网络二层抽象层（Network L2 Abstraction Layer）.md#gac7db0cc6c56d371a5803873074ec2516)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

设置虚拟网络接口的二层（L2）标志。

<a id="r_ga6c63773925ef7d96b0ba03d8978fd499"></a>

```c
enum net_verdict net_virtual_input (struct net_if *input_iface, struct net_addr *remote_addr, struct net_pkt *pkt)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_virtual_input](#ga6c63773925ef7d96b0ba03d8978fd499)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

若启用隧道（Tunneling），则将 IP 数据包送入协议栈（Stack）。

## 10.5\_详细说明（Detailed Documentation）

<a id="ga74a5c258a08397f881a8922516ac5d3a"></a>

### `NET_VIRTUAL_INTERFACE_INIT`

```c
#define NET_VIRTUAL_INTERFACE_INIT ( dev_id, name, init_fn, pm, data, config, prio, api, mtu )
```

```c
#include <zephyr/net/virtual.h>
```

展开值（Value）：

```c
Z_NET_VIRTUAL_INTERFACE_INIT(DT_INVALID_NODE, dev_id, name,     \
                             init_fn, pm, data, config, prio,   \
                             api, mtu)
```

创建虚拟网络接口（Virtual Network Interface）。

通过在运行时调用 `net_virtual_interface_attach()` 绑定到另一个接口。在 IP 隧道驱动中设置对端 IP 地址以建立隧道（Tunneling）时，会自动完成附加。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_id` | 网络设备标识（Network Device ID）。 |
| `name` | 该驱动实例向系统公开的名称（Name）。 |
| `init_fn` | 驱动初始化函数（Init Function）的地址。 |
| `pm` | 与设备关联的 `struct pm_device` 引用，可选。 |
| `data` | 指向设备私有数据（Private Data）的指针。 |
| `config` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `prio` | 执行配置的初始化层级（Initialization Level）。 |
| `api` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |
| `mtu` | 此网络接口的最大传输单元（MTU），单位为字节。这是默认值，可在运行时调整。 |

<a id="ga1846d4173bcd4b40a05b70c5fde18f91"></a>

### `NET_VIRTUAL_INTERFACE_INIT_INSTANCE`

```c
#define NET_VIRTUAL_INTERFACE_INIT_INSTANCE ( dev_id, name, inst, init_fn, pm, data, config, prio, api, mtu )
```

```c
#include <zephyr/net/virtual.h>
```

展开值（Value）：

```c
Z_NET_VIRTUAL_INTERFACE_INIT_INSTANCE(DT_INVALID_NODE, dev_id,   \
                                      name, inst,                \
                                      init_fn, pm, data, config, \
                                      prio, api, mtu)
```

创建虚拟网络接口（Virtual Network Interface）。

通过在运行时调用 `net_virtual_interface_attach()` 绑定到另一个接口。在 IP 隧道驱动中设置对端 IP 地址以建立隧道（Tunneling）时，会自动完成附加。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_id` | 网络设备标识（Network Device ID）。 |
| `name` | 该驱动实例向系统公开的名称（Name）。 |
| `inst` | 实例编号。 |
| `init_fn` | 驱动初始化函数（Init Function）的地址。 |
| `pm` | 与设备关联的 `struct pm_device` 引用，可选。 |
| `data` | 指向设备私有数据（Private Data）的指针。 |
| `config` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `prio` | 执行配置的初始化层级（Initialization Level）。 |
| `api` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |
| `mtu` | 此网络接口的最大传输单元（MTU），单位为字节。这是默认值，可在运行时调整。 |

<a id="ga8f188f5c2f19960d7113da52aefe8091"></a>

### `virtual_interface_caps`

```c
enum virtual_interface_caps
```

```c
#include <zephyr/net/virtual.h>
```

虚拟接口能力（Virtual Interface Capabilities）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIRTUAL_INTERFACE_IPIP` | IPIP 隧道（Tunnel）。 |
| `VIRTUAL_INTERFACE_VLAN` | 虚拟局域网接口（VLAN）。 |
| `VIRTUAL_INTERFACE_BRIDGE` | 虚拟以太网桥接口（Virtual Ethernet Bridge Interface）。 |
| `VIRTUAL_INTERFACE_VPN` | 虚拟专用网接口（VPN Interface）。 |

<a id="gabadf14eaa02978cde7030c99ddd3e279"></a>

### `net_virtual_get_iface()`

```c
struct net_if * net_virtual_get_iface ( struct net_if * iface)
```

```c
#include <zephyr/net/virtual.h>
```

返回与此虚拟网络接口关联的网络接口。

返回的网络接口位于此虚拟网络接口的下层。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 虚拟网络接口（Virtual Network Interface）。 |

**返回（Returns）**：返回值：与此虚拟接口关联的网络接口；若不存在则返回 `NULL`。

<a id="gaa7ff8ebb83fe98a1dfd23f319317a8de"></a>

### `net_virtual_get_name()`

```c
char * net_virtual_get_name ( struct net_if * iface, char * buf, size_t len )
```

```c
#include <zephyr/net/virtual.h>
```

返回虚拟网络接口二层（L2）的名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 虚拟网络接口（Virtual Network Interface）。 |
| `buf` | 用于保存名称的缓冲区（Buffer）。 |
| `len` | 缓冲区最大长度（Max Buffer Length）。 |

**返回（Returns）**：返回值：虚拟网络接口的名称（Name）。

<a id="ga6c63773925ef7d96b0ba03d8978fd499"></a>

### `net_virtual_input()`

```c
enum net_verdict net_virtual_input ( struct net_if * input_iface, struct net_addr * remote_addr, struct net_pkt * pkt )
```

```c
#include <zephyr/net/virtual.h>
```

若启用隧道（Tunneling），则将 IP 数据包送入协议栈（Stack）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `input_iface` | 接收 `pkt` 数据包的网络接口（Network Interface）。 |
| `remote_addr` | 发送方 IP 地址（Sender IP Address）。 |
| `pkt` | 网络数据包（Network Packet）。 |

**返回（Returns）**：返回值：如何处理数据包的判定（Verdict）。

<a id="ga5cba6ff65402b591a0e42d05f258671f"></a>

### `net_virtual_interface_attach()`

```c
int net_virtual_interface_attach ( struct net_if * virtual_iface, struct net_if * iface )
```

```c
#include <zephyr/net/virtual.h>
```

将虚拟网络接口（Virtual Network Interface）附接到指定网络接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virtual_iface` | 虚拟网络接口（Virtual Network Interface）。 |
| `iface` | 当前附加到的网络接口（Network Interface）。若要分离，可为 `NULL`。 |

**返回（Returns）**：返回值：成功返回 0；附加失败时返回小于 0 的值。

<a id="ga30f92f519a6f204ebeccd6053f17eaf0"></a>

### `net_virtual_set_flags()`

```c
enum net_l2_flags net_virtual_set_flags ( struct net_if * iface, enum net_l2_flags flags )
```

```c
#include <zephyr/net/virtual.h>
```

设置虚拟网络接口的二层（L2）标志。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 虚拟网络接口（Virtual Network Interface）。 |
| `flags` | 要设置的二层标志（L2 Flags）。 |

**返回（Returns）**：返回值：先前设置的标志（Previous Flags）。

<a id="ga2aaba616ed4fecc27138d5aae58a634f"></a>

### `net_virtual_set_name()`

```c
void net_virtual_set_name ( struct net_if * iface, const char * name )
```

```c
#include <zephyr/net/virtual.h>
```

设置虚拟网络接口二层（L2）的名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 虚拟网络接口（Virtual Network Interface）。 |
| `name` | 虚拟二层（Virtual L2 Layer）的名称。 |


## 10.6\_原页交叉引用（Cross References）

- [virtual_interface_api](../network_service_model_reference/P068_virtual_interface_api_结构体.md)
- [virtual_interface_context](../network_service_model_reference/P069_virtual_interface_context_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_l2_flags](../api_protocol_topic_reference/P040_网络二层抽象层（Network L2 Abstraction Layer）.md#gac7db0cc6c56d371a5803873074ec2516)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [zephyr/net/virtual.h](../api_file_service_interface_reference/P056_zephyr__net__virtual.h_文件参考.md)
- [DT_INVALID_NODE](../dt_identity_reference/P001_设备树节点标识宏.md#ga710cc4455dd7e738f43f750153163855)
- [pm_device](../power/P039_通用设备运行时电源结构.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-id_html_ga710cc4455dd7e738f43f750153163855"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071"></a>
<a id="gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b"></a>
<a id="gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed"></a>
<a id="gga8f188f5c2f19960d7113da52aefe8091a145ffaeae08793e4c93ea7be320efe2b"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_脉冲 I_O（Pulse IO）.md) · [返回大纲](大纲.md) · [下一章](P011_Wi-Fi 凭据库（Credentials library）.md)
