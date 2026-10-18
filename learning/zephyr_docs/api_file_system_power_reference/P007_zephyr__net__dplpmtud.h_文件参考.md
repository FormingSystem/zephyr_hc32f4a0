---
id: learning.zephyr-docs.api-file-system-power-reference.page-7
title: zephyr__net__dplpmtud.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dplpmtud_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_net\_\_dplpmtud.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dplpmtud_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数据报分组层路径MTU发现（Datagram PLPMTUD）面向传输层的API。

<a id="details"></a>

```c
#include <zephyr/net/net_ip.h>
```

查看此文件的源码。

数据报分组层路径MTU发现（Datagram PLPMTUD）面向传输层的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_net_5Fdplpmtud_5Fpath"></a>

```c
struct net_dplpmtud_path
```

相关声明：[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

归传输层所有的数据报分组层路径MTU发现（DPLPMTUD）路径句柄。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_gaa0811def61117eb41aeb473052cdacc7"></a>

```c
#define NET_DPLPMTUD_BASE_PLPMTU 1200U
```

相关声明：[NET_DPLPMTUD_BASE_PLPMTU](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaa0811def61117eb41aeb473052cdacc7)。

RFC 8899／RFC 9000 为基于 UDP 的传输规定的默认基础分组化层路径最大传输单元（Base PLPMTU）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.3\_枚举（Enumerations）

<a id="r_ga8ad5c097467be2001f385f1f403b4376"></a>

```c
enum net_dplpmtud_state { NET_DPLPMTUD_STATE_BASE = 0 , NET_DPLPMTUD_STATE_SEARCHING , NET_DPLPMTUD_STATE_SEARCH_COMPLETE , NET_DPLPMTUD_STATE_ERROR }
```

相关声明：[net_dplpmtud_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga8ad5c097467be2001f385f1f403b4376)、[NET_DPLPMTUD_STATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376a8562af32b8a2e8575aa8ab5715a9dae7)、[NET_DPLPMTUD_STATE_SEARCHING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376a901a51fd4db48131cf11e62a4cc72b09)、[NET_DPLPMTUD_STATE_SEARCH_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376a04e0fec02aef8095e5f0f42982d823e2)、[NET_DPLPMTUD_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376ab880e0ba1bdb2307566711cdcf95bab7)。

数据报分组化层路径 MTU 发现（DPLPMTUD）的搜索状态（Search State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.4\_函数（Functions）

<a id="r_ga90b9864def9a47bb48783629ab5017fc"></a>

```c
int net_dplpmtud_init_path (struct net_dplpmtud_path *path, const struct net_sockaddr *dst, uint16_t max_plpmtu)
```

相关声明：[net_dplpmtud_init_path](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga90b9864def9a47bb48783629ab5017fc)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为远端目的地初始化 DPLPMTUD 路径句柄（Path Handle）。

<a id="r_ga7d1720efbd54fe04bdbfae5ffd53f4f1"></a>

```c
void net_dplpmtud_set_path_max_plpmtu (struct net_dplpmtud_path *path, uint16_t max_plpmtu)
```

相关声明：[net_dplpmtud_set_path_max_plpmtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga7d1720efbd54fe04bdbfae5ffd53f4f1)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更新路径的传输层本地最大 PLPMTU（Transport-local Maximum PLPMTU）。

<a id="r_gaca014d4c339c7152805055bac4fc033a"></a>

```c
void net_dplpmtud_reopen_path_search (struct net_dplpmtud_path *path)
```

相关声明：[net_dplpmtud_reopen_path_search](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaca014d4c339c7152805055bac4fc033a)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

重新启动路径的 PLPMTU 搜索（Search）。

<a id="r_gac5d971f112c15245febec53c6220ade9"></a>

```c
int net_dplpmtud_get_path_mtu (struct net_dplpmtud_path *path)
```

相关声明：[net_dplpmtud_get_path_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gac5d971f112c15245febec53c6220ade9)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

获取路径当前已验证的 PLPMTU（Validated PLPMTU）。

<a id="r_gaa36c73f87f48f1ce43d1ab96aa7328e5"></a>

```c
int net_dplpmtud_get_path_probe_size (struct net_dplpmtud_path *path)
```

相关声明：[net_dplpmtud_get_path_probe_size](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaa36c73f87f48f1ce43d1ab96aa7328e5)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

获取传输层可为路径发送的下一个探测大小（Probe Size）。

<a id="r_ga86037b3a53ee6fc5cb9c9d57a8e3a69c"></a>

```c
bool net_dplpmtud_path_probe_in_flight (struct net_dplpmtud_path *path)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_dplpmtud_path_probe_in_flight](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga86037b3a53ee6fc5cb9c9d57a8e3a69c)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

检查路径是否存在正在传输的探测（Probe in Flight）。

<a id="r_ga5db1cdda7708b3186670a9c176fa1384"></a>

```c
int net_dplpmtud_on_path_probe_sent (struct net_dplpmtud_path *path, uint16_t probe_size)
```

相关声明：[net_dplpmtud_on_path_probe_sent](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga5db1cdda7708b3186670a9c176fa1384)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

报告已为路径发送探测（Probe）。

<a id="r_ga4be5d1abe82e1bf2591d1804eacb401e"></a>

```c
int net_dplpmtud_on_path_probe_acked (struct net_dplpmtud_path *path, uint16_t probe_size)
```

相关声明：[net_dplpmtud_on_path_probe_acked](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga4be5d1abe82e1bf2591d1804eacb401e)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

报告路径的探测（Probe）已获确认（Acknowledged）。

<a id="r_ga8cb73dde5eff26e8fc6e8af967e7877f"></a>

```c
int net_dplpmtud_on_path_probe_lost (struct net_dplpmtud_path *path, uint16_t probe_size)
```

相关声明：[net_dplpmtud_on_path_probe_lost](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga8cb73dde5eff26e8fc6e8af967e7877f)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

报告路径的探测（Probe）已丢失（Lost）。

<a id="r_ga9ac65913e3237c9b66c1c0ab5a4ced56"></a>

```c
void net_dplpmtud_note_path_blackhole (struct net_dplpmtud_path *path)
```

相关声明：[net_dplpmtud_note_path_blackhole](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga9ac65913e3237c9b66c1c0ab5a4ced56)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

报告路径的黑洞回退（Black-hole Fallback）。


## 7.5\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P146_dplpmtud.h_源码浏览.md)
- [net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)
- [NET_DPLPMTUD_BASE_PLPMTU](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaa0811def61117eb41aeb473052cdacc7)
- [RFC 8899](https://datatracker.ietf.org/doc/html/rfc8899)
- [RFC 9000](https://datatracker.ietf.org/doc/html/rfc9000)
- [net_dplpmtud_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga8ad5c097467be2001f385f1f403b4376)
- [NET_DPLPMTUD_STATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376a8562af32b8a2e8575aa8ab5715a9dae7)
- [NET_DPLPMTUD_STATE_SEARCHING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376a901a51fd4db48131cf11e62a4cc72b09)
- [NET_DPLPMTUD_STATE_SEARCH_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376a04e0fec02aef8095e5f0f42982d823e2)
- [NET_DPLPMTUD_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gga8ad5c097467be2001f385f1f403b4376ab880e0ba1bdb2307566711cdcf95bab7)
- [net_dplpmtud_init_path](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga90b9864def9a47bb48783629ab5017fc)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_dplpmtud_set_path_max_plpmtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga7d1720efbd54fe04bdbfae5ffd53f4f1)
- [net_dplpmtud_reopen_path_search](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaca014d4c339c7152805055bac4fc033a)
- [net_dplpmtud_get_path_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gac5d971f112c15245febec53c6220ade9)
- [net_dplpmtud_get_path_probe_size](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaa36c73f87f48f1ce43d1ab96aa7328e5)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_dplpmtud_path_probe_in_flight](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga86037b3a53ee6fc5cb9c9d57a8e3a69c)
- [net_dplpmtud_on_path_probe_sent](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga5db1cdda7708b3186670a9c176fa1384)
- [net_dplpmtud_on_path_probe_acked](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga4be5d1abe82e1bf2591d1804eacb401e)
- [net_dplpmtud_on_path_probe_lost](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga8cb73dde5eff26e8fc6e8af967e7877f)
- [net_dplpmtud_note_path_blackhole](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga9ac65913e3237c9b66c1c0ab5a4ced56)

<a id="header-details"></a>

---

[上一章](P006_zephyr__drivers__dma__dma_bee.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__mfd__adp5360.h_文件参考.md)
