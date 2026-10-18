---
id: learning.zephyr-docs.api-connection-topic-reference.page-9
title: 分布式交换架构（Distributed Switch Architecture，DSA）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_分布式交换架构（Distributed Switch Architecture，DSA）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分布式交换架构（Distributed Switch Architecture，DSA）。

<a id="details"></a>

分布式交换架构（Distributed Switch Architecture，DSA）。自 Zephyr 4.2 起提供；API 版本为 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_dsa_5Fswitch_5Fcontext"></a>

```c
struct dsa_switch_context
```

相关声明：[dsa_switch_context](../network_service_model_reference/P004_dsa_switch_context_结构体.md)。

分布式交换架构（DSA）交换机的上下文数据。

<a id="r_dsa_5Fapi"></a>

```c
struct dsa_api
```

相关声明：[dsa_api](../network_service_model_reference/P002_dsa_api_结构体.md)。

提供分布式交换架构（DSA）交换机API回调的结构；它扩展了struct ethernet_api。

<a id="r_dsa_5Fport_5Fconfig"></a>

```c
struct dsa_port_config
```

相关声明：[dsa_port_config](../network_service_model_reference/P003_dsa_port_config_结构体.md)。

分布式交换架构（DSA）的端口配置结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_ga012eeda4facb67b5c387b74878b53188"></a>

```c
#define DSA_PORT_INST_INIT(port, n, cfg)
```

相关声明：[DSA_PORT_INST_INIT](#ga012eeda4facb67b5c387b74878b53188)。

用于分布式交换架构端口实例初始化（DSA Port Instance Initialization）的宏（Macro）。

<a id="r_gaa7665e4b96cbc40cbae6de621f773aa4"></a>

```c
#define DSA_SWITCH_INST_INIT(n, _dapi, data, fn)
```

相关声明：[DSA_SWITCH_INST_INIT](#gaa7665e4b96cbc40cbae6de621f773aa4)。

用于分布式交换架构交换机实例初始化（DSA Switch Instance Initialization）的宏（Macro）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="r_ga16d03129d1e4c39f8662dae4b35598d9"></a>

```c
struct net_if * dsa_user_get_iface (struct net_if *iface, int port_idx)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[dsa_user_get_iface](#ga16d03129d1e4c39f8662dae4b35598d9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取用户端口（User Port）的网络接口（Network Interface）。

## 9.4\_详细说明（Detailed Documentation）

<a id="ga012eeda4facb67b5c387b74878b53188"></a>

### `DSA_PORT_INST_INIT`

```c
#define DSA_PORT_INST_INIT ( port, n, cfg )
```

```c
#include <zephyr/net/dsa_core.h>
```

展开值（Value）：

```c
ETH_NET_DEVICE_DT_DEFINE(port, dsa_port_initialize, NULL, &dsa_switch_context_##n, cfg,    \
                         CONFIG_ETH_INIT_PRIORITY, &dsa_eth_api, NET_ETH_MTU)
```

用于分布式交换架构端口实例初始化（DSA Port Instance Initialization）的宏（Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | DSA 端口节点标识符（node identifier）。 |
| `n` | DSA 实例编号。 |
| `cfg` | 指向 `dsa_port_config` 的指针。 |

<a id="gaa7665e4b96cbc40cbae6de621f773aa4"></a>

### `DSA_SWITCH_INST_INIT`

```c
#define DSA_SWITCH_INST_INIT ( n, _dapi, data, fn )
```

```c
#include <zephyr/net/dsa_core.h>
```

展开值（Value）：

```c
struct dsa_switch_context dsa_switch_context_##n = {                                       \
        .dapi = _dapi,                                                                     \
        .prv_data = data,                                                                  \
        .init_ports = 0,                                                                   \
        .num_ports = DT_INST_CHILD_NUM_STATUS_OKAY(n),                                     \
};                                                                                         \
DT_INST_FOREACH_CHILD_STATUS_OKAY_VARGS(n, fn, n);
```

用于分布式交换架构交换机实例初始化（DSA Switch Instance Initialization）的宏（Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `n` | DSA 实例编号。 |
| `_dapi` | 指向 `dsa_api` 的指针。 |
| `data` | 指向私有数据（private data）的指针。 |
| `fn` | DSA 端口实例初始化函数。 |

<a id="ga16d03129d1e4c39f8662dae4b35598d9"></a>

### `dsa_user_get_iface()`

```c
struct net_if * dsa_user_get_iface ( struct net_if * iface, int port_idx )
```

```c
#include <zephyr/net/dsa_core.h>
```

获取用户端口（User Port）的网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` iface` | 通道端口（Conduit port）。 |
| `[in] port_idx` | 端口索引。 |

**返回（Returns）**：返回值：成功时返回用户端口的网络接口；用户端口不存在时返回 `NULL`。


## 9.5\_原页交叉引用（Cross References）

- [dsa_switch_context](../network_service_model_reference/P004_dsa_switch_context_结构体.md)
- [dsa_api](../network_service_model_reference/P002_dsa_api_结构体.md)
- [ethernet_api](../network_service_model_reference/P007_ethernet_api_结构体.md)
- [dsa_port_config](../network_service_model_reference/P003_dsa_port_config_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [zephyr/net/dsa_core.h](../api_file_runtime_reference/P013_zephyr__net__dsa_core.h_文件参考.md)
- [ETH_NET_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9f67fee695953f24b1e5d9e49041aa99)
- [NET_ETH_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa337199b1edc50c9003afa5c3a951d8b)
- [DT_INST_CHILD_NUM_STATUS_OKAY](../dt_instance_reference/P001_设备树驱动实例宏.md#ga1a54403986077e46684c5198f4d53421)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__ethernet_html_ga9f67fee695953f24b1e5d9e49041aa99"></a>
<a id="agroup__ethernet_html_gaa337199b1edc50c9003afa5c3a951d8b"></a>
<a id="agroup__devicetree-inst_html_ga1a54403986077e46684c5198f4d53421"></a>
<a id="astructdsa__switch__context_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_磁盘访问（Disk Access）.md) · [返回大纲](大纲.md) · [下一章](P010_OpenISA RV32M1中断多路复用器（INTMUX）.md)
