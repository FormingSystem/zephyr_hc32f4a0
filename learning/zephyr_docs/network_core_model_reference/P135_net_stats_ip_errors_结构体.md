---
id: learning.zephyr-docs.network-core-model-reference.page-135
title: net_stats_ip_errors_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ip__errors.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第135章\_net\_stats\_ip\_errors\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ip__errors.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IP层错误（Error）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

IP层错误（Error）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 135.1\_数据成员（Data Fields）

<a id="r_a3e476f659ebeaa5c5f7b6dad2d90326f"></a>

```c
net_stats_t vhlerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[vhlerr](#a3e476f659ebeaa5c5f7b6dad2d90326f)。

因 IP 版本或报头长度错误（Wrong IP version or header length）而丢弃的数据包数量。

<a id="r_a06b35742c418ebc6414fcb5c7002edde"></a>

```c
net_stats_t hblenerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[hblenerr](#a06b35742c418ebc6414fcb5c7002edde)。

因 IP 长度高字节错误（Wrong IP length, high byte）而丢弃的数据包数量。

<a id="r_a9b4bf05e9df13e1d99518125b9067bef"></a>

```c
net_stats_t lblenerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[lblenerr](#a9b4bf05e9df13e1d99518125b9067bef)。

因 IP 长度低字节错误（Wrong IP length, low byte）而丢弃的数据包数量。

<a id="r_ab84ee9dfbe5da391d60c6e3ae9abea16"></a>

```c
net_stats_t fragerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[fragerr](#ab84ee9dfbe5da391d60c6e3ae9abea16)。

因属于 IP 分片（IP fragments）而丢弃的数据包数量。

<a id="r_a872cc0beca45bbe87ae794dd8ca4e301"></a>

```c
net_stats_t chkerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[chkerr](#a872cc0beca45bbe87ae794dd8ca4e301)。

因 IP 校验和错误（IP checksum errors）而丢弃的数据包数量。

<a id="r_a978b1c23847e707ac1fa27c2b34fa85d"></a>

```c
net_stats_t protoerr
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[protoerr](#a978b1c23847e707ac1fa27c2b34fa85d)。

因既不属于 ICMP、UDP，也不属于 TCP 而丢弃的数据包数量。

## 135.2\_详细说明（Detailed Documentation）

<a id="a872cc0beca45bbe87ae794dd8ca4e301"></a>

### `chkerr`

```c
net_stats_t net_stats_ip_errors::chkerr
```

因 IP 校验和错误（IP checksum errors）而丢弃的数据包数量。

<a id="ab84ee9dfbe5da391d60c6e3ae9abea16"></a>

### `fragerr`

```c
net_stats_t net_stats_ip_errors::fragerr
```

因属于 IP 分片（IP fragments）而丢弃的数据包数量。

<a id="a06b35742c418ebc6414fcb5c7002edde"></a>

### `hblenerr`

```c
net_stats_t net_stats_ip_errors::hblenerr
```

因 IP 长度高字节错误（Wrong IP length, high byte）而丢弃的数据包数量。

<a id="a9b4bf05e9df13e1d99518125b9067bef"></a>

### `lblenerr`

```c
net_stats_t net_stats_ip_errors::lblenerr
```

因 IP 长度低字节错误（Wrong IP length, low byte）而丢弃的数据包数量。

<a id="a978b1c23847e707ac1fa27c2b34fa85d"></a>

### `protoerr`

```c
net_stats_t net_stats_ip_errors::protoerr
```

因既不属于 ICMP、UDP，也不属于 TCP 而丢弃的数据包数量。

<a id="a3e476f659ebeaa5c5f7b6dad2d90326f"></a>

### `vhlerr`

```c
net_stats_t net_stats_ip_errors::vhlerr
```

因 IP 版本或报头长度错误（Wrong IP version or header length）而丢弃的数据包数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 135.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P134_net_stats_ip_结构体.md) · [返回大纲](大纲.md) · [下一章](P136_net_stats_ipv4_igmp_结构体.md)
