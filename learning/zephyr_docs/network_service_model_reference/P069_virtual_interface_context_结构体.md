---
id: learning.zephyr-docs.network-service-model-reference.page-69
title: virtual_interface_context_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtual__interface__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_virtual\_interface\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvirtual__interface__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

绑定到实际网络接口所需的虚拟第二层（Virtual L2）上下文。

```c
#include <zephyr/net/virtual.h>
```

<a id="details"></a>

绑定到实际网络接口所需的虚拟第二层（Virtual L2）上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_a4a0aada1d7af7a86d2a4b12063f35c71"></a>

```c
struct net_if * iface
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[iface](#a4a0aada1d7af7a86d2a4b12063f35c71)。

此虚拟网络接口所附接的另一个网络接口。

<a id="r_a493cef75dd5000b19eab5db156015c6e"></a>

```c
enum net_l2_flags virtual_l2_flags
```

相关声明：[net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)、[virtual_l2_flags](#a493cef75dd5000b19eab5db156015c6e)。

表示虚拟接口支持哪些二层（L2）特性。

<a id="r_a7e4699c462a1edfdb755833a9ab28d8f"></a>

```c
bool is_init
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_init](#a7e4699c462a1edfdb755833a9ab28d8f)。

此上下文是否已经初始化。

<a id="r_ade8a686b9c002c064e2ae9e1815b6601"></a>

```c
struct net_linkaddr lladdr
```

相关声明：[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[lladdr](#ade8a686b9c002c064e2ae9e1815b6601)。

此网络接口的链路地址（link address）。

<a id="r_a7d53af8860331f23b8ff83ba0bfcaacf"></a>

```c
char name [VIRTUAL_MAX_NAME_LEN]
```

相关声明：[name](#a7d53af8860331f23b8ff83ba0bfcaacf)。

此二层（L2）实现的用户友好名称。

## 69.2\_详细说明（Detailed Documentation）

<a id="a4a0aada1d7af7a86d2a4b12063f35c71"></a>

### `iface`

```c
struct net_if* virtual_interface_context::iface
```

此虚拟网络接口所附接的另一个网络接口。

这些值可以串接，使虚拟网络接口能够运行在其他虚拟接口之上。

<a id="a7e4699c462a1edfdb755833a9ab28d8f"></a>

### `is_init`

```c
bool virtual_interface_context::is_init
```

此上下文是否已经初始化。

<a id="ade8a686b9c002c064e2ae9e1815b6601"></a>

### `lladdr`

```c
struct net_linkaddr virtual_interface_context::lladdr
```

此网络接口的链路地址（link address）。

<a id="a7d53af8860331f23b8ff83ba0bfcaacf"></a>

### `name`

```c
char virtual_interface_context::name[VIRTUAL_MAX_NAME_LEN]
```

此二层（L2）实现的用户友好名称。

<a id="a493cef75dd5000b19eab5db156015c6e"></a>

### `virtual_l2_flags`

```c
enum net_l2_flags virtual_interface_context::virtual_l2_flags
```

表示虚拟接口支持哪些二层（L2）特性。

本数据类型文档由以下文件生成：

- `zephyr/net/virtual.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/net/virtual.h](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h_source.html)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_virtual_interface_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_wireguard_allowed_ip_结构体.md)
