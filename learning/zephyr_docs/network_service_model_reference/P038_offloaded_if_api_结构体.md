---
id: learning.zephyr-docs.network-service-model-reference.page-38
title: offloaded_if_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structoffloaded__if__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_offloaded\_if\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structoffloaded__if__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

供卸载接口/网络设备（Offloaded Interfaces / Network Devices）使用的扩展net_if_api，可处理管理启用/停用状态变化。

```c
#include <zephyr/net/offloaded_netdev.h>
```

<a id="details"></a>

供卸载接口/网络设备（Offloaded Interfaces / Network Devices）使用的扩展net_if_api，可处理管理启用/停用状态变化。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a24cc2bd70d18075731be617955e3e1a8"></a>

```c
struct net_if_api iface_api
```

相关声明：[iface_api](#a24cc2bd70d18075731be617955e3e1a8)。

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="r_aadf471a8e3ae22f3294df1cab090a7a3"></a>

```c
int(* enable )(const struct net_if *iface, bool state)
```

相关声明：[enable](#aadf471a8e3ae22f3294df1cab090a7a3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

启用或禁用设备，以响应管理状态（admin state）的变化。

<a id="r_a5ae87a9ed455f62958e1f2fa8cb715e7"></a>

```c
enum offloaded_net_if_types(* get_type )(void)
```

相关声明：[offloaded_net_if_types](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#gac1980977f6da3ace33ede7949d43f81f)、[get_type](#a5ae87a9ed455f62958e1f2fa8cb715e7)。

卸载型网络设备（offloaded net device）的类型。

## 38.2\_详细说明（Detailed Documentation）

<a id="aadf471a8e3ae22f3294df1cab090a7a3"></a>

### `enable`

```c
int(* offloaded_if_api::enable) (const struct net_if *iface, bool state)
```

启用或禁用设备，以响应管理状态（admin state）的变化。

<a id="a5ae87a9ed455f62958e1f2fa8cb715e7"></a>

### `get_type`

```c
enum offloaded_net_if_types(* offloaded_if_api::get_type) (void)
```

卸载型网络设备（offloaded net device）的类型。

<a id="a24cc2bd70d18075731be617955e3e1a8"></a>

### `iface_api`

```c
struct net_if_api offloaded_if_api::iface_api
```

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

本数据类型文档由以下文件生成：

- `zephyr/net/offloaded_netdev.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/net/offloaded_netdev.h](https://docs.zephyrproject.org/latest/doxygen/html/offloaded__netdev_8h_source.html)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [offloaded_net_if_types](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#gac1980977f6da3ace33ede7949d43f81f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_npf_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_openthread_state_changed_callback_结构体.md)
