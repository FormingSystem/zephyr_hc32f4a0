---
id: learning.zephyr-docs.api-file-runtime-reference.page-27
title: zephyr__net__ipv4_nat.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipv4__nat_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_net\_\_ipv4\_nat.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__nat_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr网络协议栈的IPv4网络地址转换（NAT）与iptable接口。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/net/net_core.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_pkt.h>
```

查看此文件的源码。

Zephyr网络协议栈的IPv4网络地址转换（NAT）与iptable接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 27.1\_数据结构（Data Structures）

<a id="r_net_5Fiptable_5Frule_5Fparams"></a>

```c
struct net_iptable_rule_params
```

相关声明：[net_iptable_rule_params](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md)。

定义iptable规则（Rule）的参数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.2\_函数（Functions）

<a id="r_ga83c32791968479d187622f931764b201"></a>

```c
int net_ipv4_table_rule_add (struct net_iptable_rule_params *param)
```

相关声明：[net_ipv4_table_rule_add](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html#ga83c32791968479d187622f931764b201)、[net_iptable_rule_params](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md)。

添加一条新的 iptable 规则（Rule）。

<a id="r_ga2732dba0a704fbb4fc2b75ee7e455271"></a>

```c
void net_ipv4_table_rule_del (int idx)
```

相关声明：[net_ipv4_table_rule_del](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html#ga2732dba0a704fbb4fc2b75ee7e455271)。

按索引（Index）删除一条 iptable 规则（Rule）。

<a id="r_gaddb6f51b57a9bd5522ba82784577cc21"></a>

```c
void net_ipv4_nat_init (void)
```

相关声明：[net_ipv4_nat_init](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html#gaddb6f51b57a9bd5522ba82784577cc21)。

初始化 IPv4 网络地址转换子系统（NAT Subsystem）。


## 27.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/net/net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h_source.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P410_ipv4_nat.h_源码浏览.md)
- [net_iptable_rule_params](../network_core_model_reference/P101_net_iptable_rule_params_结构体.md)
- [net_ipv4_table_rule_add](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html#ga83c32791968479d187622f931764b201)
- [net_ipv4_table_rule_del](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html#ga2732dba0a704fbb4fc2b75ee7e455271)
- [net_ipv4_nat_init](https://docs.zephyrproject.org/latest/doxygen/html/group__nat.html#gaddb6f51b57a9bd5522ba82784577cc21)

<a id="header-details"></a>

---

[上一章](P026_zephyr__posix__sys__ioctl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__dt-bindings__sensor__it51xxx_tach.h_文件参考.md)
