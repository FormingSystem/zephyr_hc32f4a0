---
id: learning.zephyr-docs.network-core-model-reference.page-51
title: net_capture_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__capture__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_net\_capture\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__capture__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络数据包捕获（Network Packet Capture）的设备信息。

```c
#include <zephyr/net/capture.h>
```

<a id="details"></a>

网络数据包捕获（Network Packet Capture）的设备信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_afc7d04a4e4b6f36a94847c27386dd384"></a>

```c
const struct device * capture_dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[capture_dev](#afc7d04a4e4b6f36a94847c27386dd384)。

捕获设备（Capture Device）。

<a id="r_afba544c1bdc06824db93ce409804b65b"></a>

```c
struct net_if * capture_iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[capture_iface](#afba544c1bdc06824db93ce409804b65b)。

捕获网络数据包的网络接口（Network Interface）。

<a id="r_a302986ad94398191d8ec4e1d9961a4df"></a>

```c
struct net_if * tunnel_iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[tunnel_iface](#a302986ad94398191d8ec4e1d9961a4df)。

用于发送所捕获数据包的IP内封装IP隧道（IPIP Tunnel）网络接口。

<a id="r_a07af2811c444bbeb2be9d420e0fd885b"></a>

```c
struct net_sockaddr * peer
```

相关声明：[net_sockaddr](P117_net_sockaddr_结构体.md)、[peer](#a07af2811c444bbeb2be9d420e0fd885b)。

对端的内部隧道IP地址（Peer Inner Tunnel IP Address）。

<a id="r_a856a912643ac30a4d269a1a88300552d"></a>

```c
struct net_sockaddr * local
```

相关声明：[net_sockaddr](P117_net_sockaddr_结构体.md)、[local](#a856a912643ac30a4d269a1a88300552d)。

本地的内部隧道IP地址（Local Inner Tunnel IP Address）。

<a id="r_a1f5786c3158d6941f3a35d99cffab985"></a>

```c
bool is_enabled
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_enabled](#a1f5786c3158d6941f3a35d99cffab985)。

当前是否启用捕获（Capture）。

## 51.2\_详细说明（Detailed Documentation）

<a id="afc7d04a4e4b6f36a94847c27386dd384"></a>

### `capture_dev`

```c
const struct device* net_capture_info::capture_dev
```

捕获设备（Capture Device）。

<a id="afba544c1bdc06824db93ce409804b65b"></a>

### `capture_iface`

```c
struct net_if* net_capture_info::capture_iface
```

捕获网络数据包的网络接口（Network Interface）。

<a id="a1f5786c3158d6941f3a35d99cffab985"></a>

### `is_enabled`

```c
bool net_capture_info::is_enabled
```

当前是否启用捕获（Capture）。

<a id="a856a912643ac30a4d269a1a88300552d"></a>

### `local`

```c
struct net_sockaddr* net_capture_info::local
```

本地的内部隧道IP地址（Local Inner Tunnel IP Address）。

<a id="a07af2811c444bbeb2be9d420e0fd885b"></a>

### `peer`

```c
struct net_sockaddr* net_capture_info::peer
```

对端的内部隧道IP地址（Peer Inner Tunnel IP Address）。

<a id="a302986ad94398191d8ec4e1d9961a4df"></a>

### `tunnel_iface`

```c
struct net_if* net_capture_info::tunnel_iface
```

用于发送所捕获数据包的IP内封装IP隧道（IPIP Tunnel）网络接口。

本数据类型文档由以下文件生成：

- `zephyr/net/capture.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/net/capture.h](https://docs.zephyrproject.org/latest/doxygen/html/capture_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [net_if](P079_net_if_结构体.md)
- [net_sockaddr](P117_net_sockaddr_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_net_capture_cooked_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_net_cmsghdr_结构体.md)
