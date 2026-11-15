---
id: learning.zephyr-docs.api-protocol-topic-reference.page-40
title: 网络二层抽象层（Network L2 Abstraction Layer）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_网络二层抽象层（Network L2 Abstraction Layer）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络第二层抽象层（Network Layer 2 abstraction layer）

<a id="details"></a>

网络第二层抽象层（Network Layer 2 abstraction layer）。自 Zephyr 1.5 起提供；API 版本为 1.0.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 40.1\_数据结构（Data Structures）

<a id="r_net_5Fl2"></a>

```c
struct net_l2
```

相关声明：[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)。

网络第二层（Network L2）结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 40.2\_枚举（Enumerations）

<a id="r_gac7db0cc6c56d371a5803873074ec2516"></a>

```c
enum net_l2_flags { NET_L2_MULTICAST = BIT(0) , NET_L2_MULTICAST_SKIP_JOIN_SOLICIT_NODE = BIT(1) , NET_L2_PROMISC_MODE = BIT(2) , NET_L2_POINT_TO_POINT = BIT(3) }
```

相关声明：[net_l2_flags](#gac7db0cc6c56d371a5803873074ec2516)、[NET_L2_MULTICAST](#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231)、[NET_L2_MULTICAST_SKIP_JOIN_SOLICIT_NODE](#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1)、[NET_L2_PROMISC_MODE](#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8)、[NET_L2_POINT_TO_POINT](#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1)。

第二层标志（L2 Flags）。

## 40.3\_详细说明（Detailed Documentation）

<a id="gac7db0cc6c56d371a5803873074ec2516"></a>

### `net_l2_flags`

```c
enum net_l2_flags
```

```c
#include <zephyr/net/net_l2.h>
```

第二层标志（L2 Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_L2_MULTICAST` | 支持 IP 多播（multicast）。 |
| `NET_L2_MULTICAST_SKIP_JOIN_SOLICIT_NODE` | 不加入被请求节点多播组（solicited-node multicast group）。 |
| `NET_L2_PROMISC_MODE` | 是否支持混杂模式（promiscuous mode）。 |
| `NET_L2_POINT_TO_POINT` | 此第二层（L2）是否为采用隧道（tunneling）的点对点连接，从而无须为网络接口配置 IP 地址等信息。 |


## 40.4\_原页交叉引用（Cross References）

- [net_l2](../network_core_model_reference/P103_net_l2_结构体.md)
- [zephyr/net/net_l2.h](../api_file_reference/P237_zephyr__net__net_l2.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231"></a>
<a id="ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1"></a>
<a id="ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8"></a>
<a id="ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1"></a>

---

[上一章](P039_导航（Navigation）.md) · [返回大纲](大纲.md) · [下一章](P041_NPCX 转速计（Tachometer）.md)
