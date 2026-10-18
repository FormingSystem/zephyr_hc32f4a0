---
id: learning.zephyr-docs.network-core-model-reference.page-179
title: wifi_nm_mgd_iface_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__nm__mgd__iface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第179章\_wifi\_nm\_mgd\_iface\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__nm__mgd__iface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi网络管理的接口（Network Managed Interfaces）。

```c
#include <zephyr/net/wifi_nm.h>
```

<a id="details"></a>

Wi-Fi网络管理的接口（Network Managed Interfaces）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 179.1\_数据成员（Data Fields）

<a id="r_adf401562151097f8be118fc609e7f86a"></a>

```c
unsigned char type
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[type](#adf401562151097f8be118fc609e7f86a)。

Wi‑Fi 接口类型（Wi-Fi interface type）。

<a id="r_abd10caf51a7890d24af51c91a58f1e4d"></a>

```c
struct net_if * iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[iface](#abd10caf51a7890d24af51c91a58f1e4d)。

受管理的网络接口（Managed network interfaces）。

## 179.2\_详细说明（Detailed Documentation）

<a id="abd10caf51a7890d24af51c91a58f1e4d"></a>

### `iface`

```c
struct net_if* wifi_nm_mgd_iface::iface
```

受管理的网络接口（Managed network interfaces）。

<a id="adf401562151097f8be118fc609e7f86a"></a>

### `type`

```c
unsigned char wifi_nm_mgd_iface::type
```

Wi‑Fi 接口类型（Wi-Fi interface type）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_nm.h`

## 179.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_nm.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__nm_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [net_if](P079_net_if_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P178_wifi_nm_instance_结构体.md) · [返回大纲](大纲.md) · [下一章](P180_wifi_ps_config_结构体.md)
