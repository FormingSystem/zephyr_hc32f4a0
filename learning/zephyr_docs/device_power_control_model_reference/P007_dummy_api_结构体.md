---
id: learning.zephyr-docs.device-power-control-model-reference.page-7
title: dummy_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdummy__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_dummy\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdummy__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

虚拟第二层（Dummy L2）的API操作。

```c
#include <zephyr/net/dummy.h>
```

<a id="details"></a>

虚拟第二层（Dummy L2）的API操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_ade5d5f20076909da1e9ea7a819192cf1"></a>

```c
struct net_if_api iface_api
```

相关声明：[iface_api](#ade5d5f20076909da1e9ea7a819192cf1)。

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="r_a3a6110e3de2300931ac5e0aeabbd7311"></a>

```c
int(* send )(const struct device *dev, struct net_pkt *pkt)
```

相关声明：[send](#a3a6110e3de2300931ac5e0aeabbd7311)、[device](../device_reference/P002_设备对象结构.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

发送网络数据包。

<a id="r_a35fcbed7d17542ef32c80a09177cb1b5"></a>

```c
enum net_verdict(* recv )(struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)、[recv](#a35fcbed7d17542ef32c80a09177cb1b5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

接收网络数据包；此功能仅用于有限场景，例如接收捕获的数据包并对其进行后处理。

<a id="r_a9f535aaf72c9e6781cceffdd019b3f85"></a>

```c
int(* start )(const struct device *dev)
```

相关声明：[start](#a9f535aaf72c9e6781cceffdd019b3f85)、[device](../device_reference/P002_设备对象结构.md)。

启动设备（Start the Device）。

<a id="r_a092fe1f0d12b091dad21e6dd7c717aa3"></a>

```c
int(* stop )(const struct device *dev)
```

相关声明：[stop](#a092fe1f0d12b091dad21e6dd7c717aa3)、[device](../device_reference/P002_设备对象结构.md)。

停止设备（Stop the Device）。

## 7.2\_详细说明（Detailed Documentation）

<a id="ade5d5f20076909da1e9ea7a819192cf1"></a>

### `iface_api`

```c
struct net_if_api dummy_api::iface_api
```

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="a35fcbed7d17542ef32c80a09177cb1b5"></a>

### `recv`

```c
enum net_verdict(* dummy_api::recv) (struct net_if *iface, struct net_pkt *pkt)
```

接收网络数据包；此功能仅用于有限场景，例如接收捕获的数据包并对其进行后处理。

<a id="a3a6110e3de2300931ac5e0aeabbd7311"></a>

### `send`

```c
int(* dummy_api::send) (const struct device *dev, struct net_pkt *pkt)
```

发送网络数据包。

<a id="a9f535aaf72c9e6781cceffdd019b3f85"></a>

### `start`

```c
int(* dummy_api::start) (const struct device *dev)
```

启动设备（Start the Device）。

绑定的网络接口启用时调用。

<a id="a092fe1f0d12b091dad21e6dd7c717aa3"></a>

### `stop`

```c
int(* dummy_api::stop) (const struct device *dev)
```

停止设备（Stop the Device）。

绑定的网络接口停用时调用。

本数据类型文档由以下文件生成：

- `zephyr/net/dummy.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/net/dummy.h](https://docs.zephyrproject.org/latest/doxygen/html/dummy_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_dtc_transfer_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_esp32_clock_config_结构体.md)
