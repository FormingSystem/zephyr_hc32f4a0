---
id: learning.zephyr-docs.network-service-model-reference.page-3
title: dsa_port_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdsa__port__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_dsa\_port\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdsa__port__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分布式交换架构（DSA）的端口配置结构。

```c
#include <zephyr/net/dsa_core.h>
```

<a id="details"></a>

分布式交换架构（DSA）的端口配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a997a4268a7aed1cc4b790d8da39c5cad"></a>

```c
struct net_eth_mac_config mcfg
```

相关声明：[net_eth_mac_config](../network_core_model_reference/P060_net_eth_mac_config_结构体.md)、[mcfg](#a997a4268a7aed1cc4b790d8da39c5cad)。

端口 MAC 地址。

<a id="r_a521f8ad8298fce309f80785b850f6eef"></a>

```c
const int port_idx
```

相关声明：[port_idx](#a521f8ad8298fce309f80785b850f6eef)。

端口索引。

<a id="r_acebba6797230c65baac4403b578e1cbb"></a>

```c
const struct device * phy_dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[phy_dev](#acebba6797230c65baac4403b578e1cbb)。

物理层（PHY）设备。

<a id="r_a8eac549c19d9f9999b95c95fa112ff97"></a>

```c
const char * phy_mode
```

相关声明：[phy_mode](#a8eac549c19d9f9999b95c95fa112ff97)。

物理层（PHY）模式。

<a id="r_a7c4578af241d554b0e8b253542c9deb6"></a>

```c
const int tag_proto
```

相关声明：[tag_proto](#a7c4578af241d554b0e8b253542c9deb6)。

标签协议（Tag protocol）。

<a id="r_a97138eca5243d1564badfe89fd04bbd4"></a>

```c
const struct device * ethernet_connection
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[ethernet_connection](#a97138eca5243d1564badfe89fd04bbd4)。

连接到此端口的以太网（Ethernet）设备。

<a id="r_a22b68800b01f9b886949f50b6976ce93"></a>

```c
const struct device * ptp_clock
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[ptp_clock](#a22b68800b01f9b886949f50b6976ce93)。

此端口使用的精确时间协议（PTP）时钟。

<a id="r_a3ab024894788e956b545d6b3114e8739"></a>

```c
void * prv_config
```

相关声明：[prv_config](#a3ab024894788e956b545d6b3114e8739)。

实例专用配置。

## 3.2\_详细说明（Detailed Documentation）

<a id="a97138eca5243d1564badfe89fd04bbd4"></a>

### `ethernet_connection`

```c
const struct device* dsa_port_config::ethernet_connection
```

连接到此端口的以太网（Ethernet）设备。

<a id="a997a4268a7aed1cc4b790d8da39c5cad"></a>

### `mcfg`

```c
struct net_eth_mac_config dsa_port_config::mcfg
```

端口 MAC 地址。

<a id="acebba6797230c65baac4403b578e1cbb"></a>

### `phy_dev`

```c
const struct device* dsa_port_config::phy_dev
```

物理层（PHY）设备。

<a id="a8eac549c19d9f9999b95c95fa112ff97"></a>

### `phy_mode`

```c
const char* dsa_port_config::phy_mode
```

物理层（PHY）模式。

<a id="a521f8ad8298fce309f80785b850f6eef"></a>

### `port_idx`

```c
const int dsa_port_config::port_idx
```

端口索引。

<a id="a3ab024894788e956b545d6b3114e8739"></a>

### `prv_config`

```c
void* dsa_port_config::prv_config
```

实例专用配置。

<a id="a22b68800b01f9b886949f50b6976ce93"></a>

### `ptp_clock`

```c
const struct device* dsa_port_config::ptp_clock
```

此端口使用的精确时间协议（PTP）时钟。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_NET_L2_PTP_TIMESTAMPING`。

<a id="a7c4578af241d554b0e8b253542c9deb6"></a>

### `tag_proto`

```c
const int dsa_port_config::tag_proto
```

标签协议（Tag protocol）。

本数据类型文档由以下文件生成：

- `zephyr/net/dsa_core.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/net/dsa_core.h](https://docs.zephyrproject.org/latest/doxygen/html/dsa__core_8h_source.html)
- [net_eth_mac_config](../network_core_model_reference/P060_net_eth_mac_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [CONFIG_NET_L2_PTP_TIMESTAMPING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_dsa_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_dsa_switch_context_结构体.md)
