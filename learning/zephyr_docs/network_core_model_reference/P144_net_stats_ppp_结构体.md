---
id: learning.zephyr-docs.network-core-model-reference.page-144
title: net_stats_ppp_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ppp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第144章\_net\_stats\_ppp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ppp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全部点对点协议（PPP）专用统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

全部点对点协议（PPP）专用统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 144.1\_数据成员（Data Fields）

<a id="r_ab2b48da7f19d4b83e3f41b41979b7ed8"></a>

```c
struct net_stats_bytes bytes
```

相关声明：[net_stats_bytes](P126_net_stats_bytes_结构体.md)、[bytes](#ab2b48da7f19d4b83e3f41b41979b7ed8)。

接收与发送的总字节数（Total bytes）。

<a id="r_a71fc81f3c5f3e65a476b3391f086d340"></a>

```c
struct net_stats_pkts pkts
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[pkts](#a71fc81f3c5f3e65a476b3391f086d340)。

接收与发送的数据包总数（Total packets）。

<a id="r_ae2e0a47a539e9d7bc97f9c63f889b276"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#ae2e0a47a539e9d7bc97f9c63f889b276)。

已接收及丢弃的点对点协议帧（PPP frames）数量。

<a id="r_a1332b31980f82236aeb0c3f9444e2ac6"></a>

```c
net_stats_t chkerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[chkerr](#a1332b31980f82236aeb0c3f9444e2ac6)。

接收到的校验和错误的点对点协议帧（PPP frames with a bad checksum）数量。

## 144.2\_详细说明（Detailed Documentation）

<a id="ab2b48da7f19d4b83e3f41b41979b7ed8"></a>

### `bytes`

```c
struct net_stats_bytes net_stats_ppp::bytes
```

接收与发送的总字节数（Total bytes）。

<a id="a1332b31980f82236aeb0c3f9444e2ac6"></a>

### `chkerr`

```c
net_stats_t net_stats_ppp::chkerr
```

接收到的校验和错误的点对点协议帧（PPP frames with a bad checksum）数量。

<a id="ae2e0a47a539e9d7bc97f9c63f889b276"></a>

### `drop`

```c
net_stats_t net_stats_ppp::drop
```

已接收及丢弃的点对点协议帧（PPP frames）数量。

<a id="a71fc81f3c5f3e65a476b3391f086d340"></a>

### `pkts`

```c
struct net_stats_pkts net_stats_ppp::pkts
```

接收与发送的数据包总数（Total packets）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 144.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_bytes](P126_net_stats_bytes_结构体.md)
- [net_stats_pkts](P142_net_stats_pkts_结构体.md)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P143_net_stats_pm_结构体.md) · [返回大纲](大纲.md) · [下一章](P145_net_stats_raw_结构体.md)
