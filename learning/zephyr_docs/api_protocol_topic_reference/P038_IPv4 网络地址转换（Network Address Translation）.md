---
id: learning.zephyr-docs.api-protocol-topic-reference.page-38
title: IPv4 网络地址转换（Network Address Translation）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_IPv4 网络地址转换（Network Address Translation）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 Zephyr 4.5 起提供；API 版本为 0.1.0。本头文件定义 Zephyr 网络子系统中用于 IPv4 网络地址转换（Network Address Translation，NAT）及基于规则的 iptable 操作的数据结构和 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 38.1\_数据结构（Data Structures）

<a id="r_net_5Fiptable_5Frule_5Fparams"></a>

```c
struct net_iptable_rule_params
```

相关声明：[net_iptable_rule_params](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md)。

定义iptable规则（Rule）的参数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 38.2\_函数（Functions）

<a id="r_ga83c32791968479d187622f931764b201"></a>

```c
int net_ipv4_table_rule_add (struct net_iptable_rule_params *param)
```

相关声明：[net_ipv4_table_rule_add](#ga83c32791968479d187622f931764b201)、[net_iptable_rule_params](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md)。

添加一条新的 iptable 规则（Rule）。

<a id="r_ga2732dba0a704fbb4fc2b75ee7e455271"></a>

```c
void net_ipv4_table_rule_del (int idx)
```

相关声明：[net_ipv4_table_rule_del](#ga2732dba0a704fbb4fc2b75ee7e455271)。

按索引（Index）删除一条 iptable 规则（Rule）。

<a id="r_gaddb6f51b57a9bd5522ba82784577cc21"></a>

```c
void net_ipv4_nat_init (void)
```

相关声明：[net_ipv4_nat_init](#gaddb6f51b57a9bd5522ba82784577cc21)。

初始化 IPv4 网络地址转换子系统（NAT Subsystem）。

## 38.3\_详细说明（Detailed Documentation）

<a id="gaddb6f51b57a9bd5522ba82784577cc21"></a>

### `net_ipv4_nat_init()`

```c
void net_ipv4_nat_init ( void )
```

```c
#include <zephyr/net/ipv4_nat.h>
```

初始化 IPv4 网络地址转换子系统（NAT Subsystem）。

准备内部 NAT 状态，使其能够运行。

<a id="ga83c32791968479d187622f931764b201"></a>

### `net_ipv4_table_rule_add()`

```c
int net_ipv4_table_rule_add ( struct net_iptable_rule_params * param)
```

```c
#include <zephyr/net/ipv4_nat.h>
```

添加一条新的 iptable 规则（Rule）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 规则配置（rule configuration）及匹配条件（match criteria）。 |

**返回（Returns）**：返回值：成功时返回非负的规则索引，出错时返回负错误码。

<a id="ga2732dba0a704fbb4fc2b75ee7e455271"></a>

### `net_ipv4_table_rule_del()`

```c
void net_ipv4_table_rule_del ( int idx)
```

```c
#include <zephyr/net/ipv4_nat.h>
```

按索引（Index）删除一条 iptable 规则（Rule）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | 待移除规则的索引（rule index）。 |


## 38.4\_原页交叉引用（Cross References）

- [net_iptable_rule_params](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md)
- [zephyr/net/ipv4_nat.h](../api_file_runtime_reference/P027_zephyr__net__ipv4_nat.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P037_MSPI 回调 API（MSPI callback API）.md) · [返回大纲](大纲.md) · [下一章](P039_导航（Navigation）.md)
