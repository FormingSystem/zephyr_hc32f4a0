---
id: learning.zephyr-docs.network-service-model-reference.page-42
title: ppp_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structppp__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_ppp\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structppp__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

点对点协议第二层（PPP L2）API。

```c
#include <zephyr/net/ppp.h>
```

<a id="details"></a>

点对点协议第二层（PPP L2）API。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_acc4e82fbaa8b933040b0a77da8a3cae0"></a>

```c
struct net_if_api iface_api
```

相关声明：[iface_api](#acc4e82fbaa8b933040b0a77da8a3cae0)。

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="r_ab85010475c4f03a48ad7629ed4947626"></a>

```c
int(* start )(const struct device *dev)
```

相关声明：[start](#ab85010475c4f03a48ad7629ed4947626)、[device](../device_reference/P002_设备对象结构.md)。

启动设备（Start the Device）。

<a id="r_a42576f1d58920f48a0d0adf888f99006"></a>

```c
int(* stop )(const struct device *dev)
```

相关声明：[stop](#a42576f1d58920f48a0d0adf888f99006)、[device](../device_reference/P002_设备对象结构.md)。

停止设备（Stop the Device）。

<a id="r_aa0ec35e57f22674ef06f8cc3bc09987f"></a>

```c
int(* send )(const struct device *dev, struct net_pkt *pkt)
```

相关声明：[send](#aa0ec35e57f22674ef06f8cc3bc09987f)、[device](../device_reference/P002_设备对象结构.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

发送网络数据包。

## 42.2\_详细说明（Detailed Documentation）

<a id="acc4e82fbaa8b933040b0a77da8a3cae0"></a>

### `iface_api`

```c
struct net_if_api ppp_api::iface_api
```

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="aa0ec35e57f22674ef06f8cc3bc09987f"></a>

### `send`

```c
int(* ppp_api::send) (const struct device *dev, struct net_pkt *pkt)
```

发送网络数据包。

<a id="ab85010475c4f03a48ad7629ed4947626"></a>

### `start`

```c
int(* ppp_api::start) (const struct device *dev)
```

启动设备（Start the Device）。

<a id="a42576f1d58920f48a0d0adf888f99006"></a>

### `stop`

```c
int(* ppp_api::stop) (const struct device *dev)
```

停止设备（Stop the Device）。

本数据类型文档由以下文件生成：

- `zephyr/net/ppp.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/net/ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_phy_plca_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_ppp_context_结构体.md)
