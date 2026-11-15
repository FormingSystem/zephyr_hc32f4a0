---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-13
title: 数据报分组层路径 MTU 发现 API（Datagram PLPMTUD API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_数据报分组层路径 MTU 发现 API（Datagram PLPMTUD API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 4.5 起提供，版本 0.1.0。适用于 UDP 传输的通用数据报分包层路径 MTU 发现（Datagram Packetization Layer Path MTU Discovery，DPLPMTUD；`:rfc:8899`）。协议栈管理每个目的地的搜索状态，包括已验证的分包层路径 MTU（PLPMTU）、探测大小及重试计数。各传输层负责构造探测包、以禁止分片（Don't Fragment）方式发送，并通过其丢失恢复路径进行确认。典型集成流程：建立连接时调用 `net_dplpmtud_init_path()`；使用 `net_dplpmtud_get_path_mtu()` 确定出站数据报大小；当 `net_dplpmtud_get_path_probe_size()` 返回大于 0 的值，且 `net_dplpmtud_path_probe_in_flight()` 为 `false` 时，启用 `IP_DONTFRAG`／`IPV6_DONTFRAG`，并按返回大小发送探测数据报。发送探测前调用 `net_dplpmtud_on_path_probe_sent()`，随后调用 `net_dplpmtud_on_path_probe_acked()` 或 `net_dplpmtud_on_path_probe_lost()`。通过路径 MTU 目的地缓存（PMTU Destination Cache）收到的 ICMP 数据包过大（Packet Too Big，PTB）更新会自动应用。验证成功的探测结果会写回该缓存，供协议栈其他使用方使用。QUIC 在内部使用此 API；参见 `:ref:quic_dplpmtud`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_net_5Fdplpmtud_5Fpath"></a>

```c
struct net_dplpmtud_path
```

相关声明：[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

归传输层所有的数据报分组层路径MTU发现（DPLPMTUD）路径句柄。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.2\_宏定义（Macros）

<a id="r_gaa0811def61117eb41aeb473052cdacc7"></a>

```c
#define NET_DPLPMTUD_BASE_PLPMTU 1200U
```

相关声明：[NET_DPLPMTUD_BASE_PLPMTU](#gaa0811def61117eb41aeb473052cdacc7)。

RFC 8899／RFC 9000 为基于 UDP 的传输规定的默认基础分组化层路径最大传输单元（Base PLPMTU）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.3\_枚举（Enumerations）

<a id="r_ga8ad5c097467be2001f385f1f403b4376"></a>

```c
enum net_dplpmtud_state { NET_DPLPMTUD_STATE_BASE = 0 , NET_DPLPMTUD_STATE_SEARCHING , NET_DPLPMTUD_STATE_SEARCH_COMPLETE , NET_DPLPMTUD_STATE_ERROR }
```

相关声明：[net_dplpmtud_state](#ga8ad5c097467be2001f385f1f403b4376)、[NET_DPLPMTUD_STATE_BASE](#gga8ad5c097467be2001f385f1f403b4376a8562af32b8a2e8575aa8ab5715a9dae7)、[NET_DPLPMTUD_STATE_SEARCHING](#gga8ad5c097467be2001f385f1f403b4376a901a51fd4db48131cf11e62a4cc72b09)、[NET_DPLPMTUD_STATE_SEARCH_COMPLETE](#gga8ad5c097467be2001f385f1f403b4376a04e0fec02aef8095e5f0f42982d823e2)、[NET_DPLPMTUD_STATE_ERROR](#gga8ad5c097467be2001f385f1f403b4376ab880e0ba1bdb2307566711cdcf95bab7)。

数据报分组化层路径 MTU 发现（DPLPMTUD）的搜索状态（Search State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_ga90b9864def9a47bb48783629ab5017fc"></a>

```c
int net_dplpmtud_init_path (struct net_dplpmtud_path *path, const struct net_sockaddr *dst, uint16_t max_plpmtu)
```

相关声明：[net_dplpmtud_init_path](#ga90b9864def9a47bb48783629ab5017fc)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为远端目的地初始化 DPLPMTUD 路径句柄（Path Handle）。

<a id="r_ga7d1720efbd54fe04bdbfae5ffd53f4f1"></a>

```c
void net_dplpmtud_set_path_max_plpmtu (struct net_dplpmtud_path *path, uint16_t max_plpmtu)
```

相关声明：[net_dplpmtud_set_path_max_plpmtu](#ga7d1720efbd54fe04bdbfae5ffd53f4f1)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更新路径的传输层本地最大 PLPMTU（Transport-local Maximum PLPMTU）。

<a id="r_gaca014d4c339c7152805055bac4fc033a"></a>

```c
void net_dplpmtud_reopen_path_search (struct net_dplpmtud_path *path)
```

相关声明：[net_dplpmtud_reopen_path_search](#gaca014d4c339c7152805055bac4fc033a)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

重新启动路径的 PLPMTU 搜索（Search）。

<a id="r_gac5d971f112c15245febec53c6220ade9"></a>

```c
int net_dplpmtud_get_path_mtu (struct net_dplpmtud_path *path)
```

相关声明：[net_dplpmtud_get_path_mtu](#gac5d971f112c15245febec53c6220ade9)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

获取路径当前已验证的 PLPMTU（Validated PLPMTU）。

<a id="r_gaa36c73f87f48f1ce43d1ab96aa7328e5"></a>

```c
int net_dplpmtud_get_path_probe_size (struct net_dplpmtud_path *path)
```

相关声明：[net_dplpmtud_get_path_probe_size](#gaa36c73f87f48f1ce43d1ab96aa7328e5)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

获取传输层可为路径发送的下一个探测大小（Probe Size）。

<a id="r_ga86037b3a53ee6fc5cb9c9d57a8e3a69c"></a>

```c
bool net_dplpmtud_path_probe_in_flight (struct net_dplpmtud_path *path)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_dplpmtud_path_probe_in_flight](#ga86037b3a53ee6fc5cb9c9d57a8e3a69c)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

检查路径是否存在正在传输的探测（Probe in Flight）。

<a id="r_ga5db1cdda7708b3186670a9c176fa1384"></a>

```c
int net_dplpmtud_on_path_probe_sent (struct net_dplpmtud_path *path, uint16_t probe_size)
```

相关声明：[net_dplpmtud_on_path_probe_sent](#ga5db1cdda7708b3186670a9c176fa1384)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

报告已为路径发送探测（Probe）。

<a id="r_ga4be5d1abe82e1bf2591d1804eacb401e"></a>

```c
int net_dplpmtud_on_path_probe_acked (struct net_dplpmtud_path *path, uint16_t probe_size)
```

相关声明：[net_dplpmtud_on_path_probe_acked](#ga4be5d1abe82e1bf2591d1804eacb401e)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

报告路径的探测（Probe）已获确认（Acknowledged）。

<a id="r_ga8cb73dde5eff26e8fc6e8af967e7877f"></a>

```c
int net_dplpmtud_on_path_probe_lost (struct net_dplpmtud_path *path, uint16_t probe_size)
```

相关声明：[net_dplpmtud_on_path_probe_lost](#ga8cb73dde5eff26e8fc6e8af967e7877f)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

报告路径的探测（Probe）已丢失（Lost）。

<a id="r_ga9ac65913e3237c9b66c1c0ab5a4ced56"></a>

```c
void net_dplpmtud_note_path_blackhole (struct net_dplpmtud_path *path)
```

相关声明：[net_dplpmtud_note_path_blackhole](#ga9ac65913e3237c9b66c1c0ab5a4ced56)、[net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)。

报告路径的黑洞回退（Black-hole Fallback）。

## 13.5\_详细说明（Detailed Documentation）

<a id="gaa0811def61117eb41aeb473052cdacc7"></a>

### `NET_DPLPMTUD_BASE_PLPMTU`

```c
#define NET_DPLPMTUD_BASE_PLPMTU 1200U
```

```c
#include <zephyr/net/dplpmtud.h>
```

RFC 8899／RFC 9000 为基于 UDP 的传输规定的默认基础分组化层路径最大传输单元（Base PLPMTU）。

<a id="ga8ad5c097467be2001f385f1f403b4376"></a>

### `net_dplpmtud_state`

```c
enum net_dplpmtud_state
```

```c
#include <zephyr/net/dplpmtud.h>
```

数据报分组化层路径 MTU 发现（DPLPMTUD）的搜索状态（Search State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_DPLPMTUD_STATE_BASE` | 路径正在使用基础分包层路径 MTU（Base PLPMTU）。 |
| `NET_DPLPMTUD_STATE_SEARCHING` | 路径正在主动探测更大的分包层路径 MTU（PLPMTU）。 |
| `NET_DPLPMTUD_STATE_SEARCH_COMPLETE` | 路径没有更大的候选探测值（Probe Candidate）。 |
| `NET_DPLPMTUD_STATE_ERROR` | 路径在检测到黑洞（Black Hole）后已回退。 |

<a id="gac5d971f112c15245febec53c6220ade9"></a>

### `net_dplpmtud_get_path_mtu()`

```c
int net_dplpmtud_get_path_mtu ( struct net_dplpmtud_path * path)
```

```c
#include <zephyr/net/dplpmtud.h>
```

获取路径当前已验证的 PLPMTU（Validated PLPMTU）。

路径必须已通过 `net_dplpmtud_init_path()` 初始化。此次调用不会创建按目的地维护的 DPLPMTUD 状态（Per-destination State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 已初始化的路径句柄（Path Handle）。 |

**返回（Returns）**：返回值：成功返回已验证的分包层路径 MTU（PLPMTU），否则返回负 errno 值。

<a id="gaa36c73f87f48f1ce43d1ab96aa7328e5"></a>

### `net_dplpmtud_get_path_probe_size()`

```c
int net_dplpmtud_get_path_probe_size ( struct net_dplpmtud_path * path)
```

```c
#include <zephyr/net/dplpmtud.h>
```

获取传输层可为路径发送的下一个探测大小（Probe Size）。

路径必须已通过 `net_dplpmtud_init_path()` 初始化。此次调用不会创建按目的地维护的 DPLPMTUD 状态（Per-destination State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 已初始化的路径句柄（Path Handle）。 |

**返回（Returns）**：返回值：下一次探测大小（Probe Size）；当前不需要探测时返回 0，出错时返回负 errno 值。

<a id="ga90b9864def9a47bb48783629ab5017fc"></a>

### `net_dplpmtud_init_path()`

```c
int net_dplpmtud_init_path ( struct net_dplpmtud_path * path, const struct net_sockaddr * dst, uint16_t max_plpmtu )
```

```c
#include <zephyr/net/dplpmtud.h>
```

为远端目的地初始化 DPLPMTUD 路径句柄（Path Handle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 要初始化的路径句柄（Path Handle）。 |
| `dst` | 远端目的地址（Remote Destination Address）。 |
| `max_plpmtu` | 传输层本地的最大分包层路径 MTU（PLPMTU）；为 0 时不设此上限。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 参数无效。 |
| `-ENOMEM` | 无法创建 DPLPMTUD 状态条目（State Entry）时。 |

<a id="ga9ac65913e3237c9b66c1c0ab5a4ced56"></a>

### `net_dplpmtud_note_path_blackhole()`

```c
void net_dplpmtud_note_path_blackhole ( struct net_dplpmtud_path * path)
```

```c
#include <zephyr/net/dplpmtud.h>
```

报告路径的黑洞回退（Black-hole Fallback）。

将已验证的 PLPMTU 向基础大小回退，停止探测，并将路径记录为错误状态（Error State）。若传输层在未收到 ICMP PTB 的情况下检测到黑洞（Black Hole），也可调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 已初始化的路径句柄（Path Handle）。 |

<a id="ga4be5d1abe82e1bf2591d1804eacb401e"></a>

### `net_dplpmtud_on_path_probe_acked()`

```c
int net_dplpmtud_on_path_probe_acked ( struct net_dplpmtud_path * path, uint16_t probe_size )
```

```c
#include <zephyr/net/dplpmtud.h>
```

报告路径的探测（Probe）已获确认（Acknowledged）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 已初始化的路径句柄（Path Handle）。 |
| `probe_size` | 传输层已确认的探测大小（Acknowledged Probe Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 否则返回 errno 错误码。 |

<a id="ga8cb73dde5eff26e8fc6e8af967e7877f"></a>

### `net_dplpmtud_on_path_probe_lost()`

```c
int net_dplpmtud_on_path_probe_lost ( struct net_dplpmtud_path * path, uint16_t probe_size )
```

```c
#include <zephyr/net/dplpmtud.h>
```

报告路径的探测（Probe）已丢失（Lost）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 已初始化的路径句柄（Path Handle）。 |
| `probe_size` | 传输层声明为丢失的探测大小（Lost Probe Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 否则返回 errno 错误码。 |

<a id="ga5db1cdda7708b3186670a9c176fa1384"></a>

### `net_dplpmtud_on_path_probe_sent()`

```c
int net_dplpmtud_on_path_probe_sent ( struct net_dplpmtud_path * path, uint16_t probe_size )
```

```c
#include <zephyr/net/dplpmtud.h>
```

报告已为路径发送探测（Probe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 已初始化的路径句柄（Path Handle）。 |
| `probe_size` | 传输层发送的探测大小（Sent Probe Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 参数无效。 |
| `-EMSGSIZE` | 探测大小超过传输层本地路径上限（Transport-local Path Limit）时。 |
| `negative` | 否则返回来自 DPLPMTUD 核心的 errno 错误码。 |

<a id="ga86037b3a53ee6fc5cb9c9d57a8e3a69c"></a>

### `net_dplpmtud_path_probe_in_flight()`

```c
bool net_dplpmtud_path_probe_in_flight ( struct net_dplpmtud_path * path)
```

```c
#include <zephyr/net/dplpmtud.h>
```

检查路径是否存在正在传输的探测（Probe in Flight）。

路径必须已通过 `net_dplpmtud_init_path()` 初始化。此次调用不会创建按目的地维护的 DPLPMTUD 状态（Per-destination State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 已初始化的路径句柄（Path Handle）。 |

**返回（Returns）**：返回值：有在途探测（Probe in Flight）时返回 `true`，否则返回 `false`。

<a id="gaca014d4c339c7152805055bac4fc033a"></a>

### `net_dplpmtud_reopen_path_search()`

```c
void net_dplpmtud_reopen_path_search ( struct net_dplpmtud_path * path)
```

```c
#include <zephyr/net/dplpmtud.h>
```

重新启动路径的 PLPMTU 搜索（Search）。

重置搜索，使其从基础 PLPMTU 重新开始，搜索至该条目的当前上限，并清除任何过时的在途探测状态（In-flight Probe State）。这样，新启动或重新启动的探测器会从头验证路径。

按目的地维护的 DPLPMTUD 状态（Per-destination State）由多个使用方共享，其生命周期长于单个传输对象／套接字。先前运行可能已将其留在不再产生探测的终止状态（Terminal State）：可能是搜索已完成，即已验证的 PLPMTU 达到上限；也可能是在没有响应方、反复丢失探测后搜索失败。两种情况下，单纯重新启用都不会发送探测。因此，传输层重新关联到某个目的地并重新启用探测时，应调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 已初始化的路径句柄（Path Handle）。 |

<a id="ga7d1720efbd54fe04bdbfae5ffd53f4f1"></a>

### `net_dplpmtud_set_path_max_plpmtu()`

```c
void net_dplpmtud_set_path_max_plpmtu ( struct net_dplpmtud_path * path, uint16_t max_plpmtu )
```

```c
#include <zephyr/net/dplpmtud.h>
```

更新路径的传输层本地最大 PLPMTU（Transport-local Maximum PLPMTU）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 已初始化的路径句柄（Path Handle）。 |
| `max_plpmtu` | 传输层本地的最大分包层路径 MTU（PLPMTU）；为 0 时不设此上限。 |


## 13.6\_原页交叉引用（Cross References）

- [net_dplpmtud_path](../network_core_model_reference/P058_net_dplpmtud_path_结构体.md)
- [RFC 8899](https://datatracker.ietf.org/doc/html/rfc8899)
- [RFC 9000](https://datatracker.ietf.org/doc/html/rfc9000)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/dplpmtud.h](../api_file_system_power_reference/P007_zephyr__net__dplpmtud.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8ad5c097467be2001f385f1f403b4376a8562af32b8a2e8575aa8ab5715a9dae7"></a>
<a id="gga8ad5c097467be2001f385f1f403b4376a901a51fd4db48131cf11e62a4cc72b09"></a>
<a id="gga8ad5c097467be2001f385f1f403b4376a04e0fec02aef8095e5f0f42982d823e2"></a>
<a id="gga8ad5c097467be2001f385f1f403b4376ab880e0ba1bdb2307566711cdcf95bab7"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_简单管理协议客户端（SMP client）.md) · [返回大纲](大纲.md) · [下一章](P014_性能监控单元（PMU）.md)
