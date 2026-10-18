---
id: learning.zephyr-docs.network-service-model-reference.page-1
title: canbus_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcanbus__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_canbus\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcanbus__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CAN第二层（L2）网络驱动API。

```c
#include <zephyr/net/canbus.h>
```

<a id="details"></a>

CAN第二层（L2）网络驱动API。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_af8f809bf252a5d261209af2b7b3096f7"></a>

```c
struct net_if_api iface_api
```

相关声明：[iface_api](#af8f809bf252a5d261209af2b7b3096f7)。

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="r_a31fee4b60f4ab2f832e0599c23337b6c"></a>

```c
int(* send )(const struct device *dev, struct net_pkt *pkt)
```

相关声明：[send](#a31fee4b60f4ab2f832e0599c23337b6c)、[device](../device_reference/P002_设备对象结构.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

通过套接字（socket）发送控制器局域网（CAN）数据包。

<a id="r_abff03e6144170f8f223e11a7f28b59b7"></a>

```c
void(* close )(const struct device *dev, int filter_id)
```

相关声明：[close](#abff03e6144170f8f223e11a7f28b59b7)、[device](../device_reference/P002_设备对象结构.md)。

关闭关联的 CAN 套接字。

<a id="r_a03a36b089a813aecaab120acf66542d2"></a>

```c
int(* setsockopt )(const struct device *dev, void *obj, int level, int optname, const void *optval, net_socklen_t optlen)
```

相关声明：[setsockopt](#a03a36b089a813aecaab120acf66542d2)、[device](../device_reference/P002_设备对象结构.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

设置 CAN 套接字选项。

<a id="r_ade7bbf8e2f366425ed4da89b78272885"></a>

```c
int(* getsockopt )(const struct device *dev, void *obj, int level, int optname, const void *optval, net_socklen_t *optlen)
```

相关声明：[getsockopt](#ade7bbf8e2f366425ed4da89b78272885)、[device](../device_reference/P002_设备对象结构.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

获取 CAN 套接字选项。

## 1.2\_详细说明（Detailed Documentation）

<a id="abff03e6144170f8f223e11a7f28b59b7"></a>

### `close`

```c
void(* canbus_api::close) (const struct device *dev, int filter_id)
```

关闭关联的 CAN 套接字。

<a id="ade7bbf8e2f366425ed4da89b78272885"></a>

### `getsockopt`

```c
int(* canbus_api::getsockopt) (const struct device *dev, void *obj, int level, int optname, const void *optval, net_socklen_t *optlen)
```

获取 CAN 套接字选项。

<a id="af8f809bf252a5d261209af2b7b3096f7"></a>

### `iface_api`

```c
struct net_if_api canbus_api::iface_api
```

`net_if_api` 必须放在此结构体的首个位置，以便与网络接口 API 兼容。

<a id="a31fee4b60f4ab2f832e0599c23337b6c"></a>

### `send`

```c
int(* canbus_api::send) (const struct device *dev, struct net_pkt *pkt)
```

通过套接字（socket）发送控制器局域网（CAN）数据包。

<a id="a03a36b089a813aecaab120acf66542d2"></a>

### `setsockopt`

```c
int(* canbus_api::setsockopt) (const struct device *dev, void *obj, int level, int optname, const void *optval, net_socklen_t optlen)
```

设置 CAN 套接字选项。

本数据类型文档由以下文件生成：

- `zephyr/net/canbus.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/net/canbus.h](https://docs.zephyrproject.org/latest/doxygen/html/canbus_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_dsa_api_结构体.md)
