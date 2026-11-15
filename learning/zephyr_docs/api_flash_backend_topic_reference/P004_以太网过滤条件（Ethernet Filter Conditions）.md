---
id: learning.zephyr-docs.api-flash-backend-topic-reference.page-4
title: 以太网过滤条件（Ethernet Filter Conditions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_以太网过滤条件（Ethernet Filter Conditions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

**引入版本（Since）：**3.0。**版本（Version）：**0.8.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="r_gad2141ad8d6639c9b92569d55130ca1b1"></a>

```c
#define NPF_ETH_SRC_ADDR_MATCH(_name, _addr_array)
```

相关声明：[NPF_ETH_SRC_ADDR_MATCH](#gad2141ad8d6639c9b92569d55130ca1b1)。

静态定义“源地址匹配”（Source Address Match）数据包过滤条件。

<a id="r_ga228eaa3784f663d8f2e2711e26409043"></a>

```c
#define NPF_ETH_SRC_ADDR_UNMATCH(_name, _addr_array)
```

相关声明：[NPF_ETH_SRC_ADDR_UNMATCH](#ga228eaa3784f663d8f2e2711e26409043)。

静态定义“源地址不匹配”（Source Address Unmatch）数据包过滤条件。

<a id="r_ga3d22d687bcd56b7727c51c7bc7f36cac"></a>

```c
#define NPF_ETH_DST_ADDR_MATCH(_name, _addr_array)
```

相关声明：[NPF_ETH_DST_ADDR_MATCH](#ga3d22d687bcd56b7727c51c7bc7f36cac)。

静态定义“目的地址匹配”（Destination Address Match）数据包过滤条件。

<a id="r_ga3b8a8a22eb992c0e02223f70723c3641"></a>

```c
#define NPF_ETH_DST_ADDR_UNMATCH(_name, _addr_array)
```

相关声明：[NPF_ETH_DST_ADDR_UNMATCH](#ga3b8a8a22eb992c0e02223f70723c3641)。

静态定义“目的地址不匹配”（Destination Address Unmatch）数据包过滤条件。

<a id="r_ga0e06ebc4c9a1a960651be1ba89eeb2fd"></a>

```c
#define NPF_ETH_SRC_ADDR_MASK_MATCH(_name, _addr_array, ...)
```

相关声明：[NPF_ETH_SRC_ADDR_MASK_MATCH](#ga0e06ebc4c9a1a960651be1ba89eeb2fd)。

静态定义“带掩码的源地址匹配”（Source Address Match with Mask）数据包过滤条件。

<a id="r_ga7cf793af7b91eccc6e675ff19ed59a14"></a>

```c
#define NPF_ETH_DST_ADDR_MASK_MATCH(_name, _addr_array, ...)
```

相关声明：[NPF_ETH_DST_ADDR_MASK_MATCH](#ga7cf793af7b91eccc6e675ff19ed59a14)。

静态定义“带掩码的目的地址匹配”（Destination Address Match with Mask）数据包过滤条件。

<a id="r_gace7de72d4c64e128a825f28f94d8b1b2"></a>

```c
#define NPF_ETH_TYPE_MATCH(_name, _type)
```

相关声明：[NPF_ETH_TYPE_MATCH](#gace7de72d4c64e128a825f28f94d8b1b2)。

静态定义“以太网类型匹配”（Ethernet Type Match）数据包过滤条件。

<a id="r_gab9bf6d58433e273220c5fab76f608545"></a>

```c
#define NPF_ETH_TYPE_UNMATCH(_name, _type)
```

相关声明：[NPF_ETH_TYPE_UNMATCH](#gab9bf6d58433e273220c5fab76f608545)。

静态定义“以太网类型不匹配”（Ethernet Type Unmatch）数据包过滤条件。

<a id="r_ga2d67631c0fdd659a8e9db62c6f0a87bf"></a>

```c
#define NPF_ETH_VLAN_TYPE_MATCH(_name, _type)
```

相关声明：[NPF_ETH_VLAN_TYPE_MATCH](#ga2d67631c0fdd659a8e9db62c6f0a87bf)。

静态定义“以太网 VLAN 头部类型匹配”（Ethernet VLAN Header Type Match）数据包过滤条件。

<a id="r_ga49af5d0231e15932607da955ca7e4b34"></a>

```c
#define NPF_ETH_VLAN_TYPE_UNMATCH(_name, _type)
```

相关声明：[NPF_ETH_VLAN_TYPE_UNMATCH](#ga49af5d0231e15932607da955ca7e4b34)。

静态定义“以太网 VLAN 头部类型不匹配”（Ethernet VLAN Header Type Unmatch）数据包过滤条件。

<a id="r_ga61b8c41e90b61041c50cd6206c4dfcfe"></a>

```c
#define NPF_LOCAL_IN_MATCH(_name, _handler, _user_data)
```

相关声明：[NPF_LOCAL_IN_MATCH](#ga61b8c41e90b61041c50cd6206c4dfcfe)。

静态定义“local_in 匹配”（local_in Match）数据包过滤条件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.2\_类型定义（Typedefs）

<a id="r_ga673493f74227912cf8f5827a77af012f"></a>

```c
typedef bool npf_local_in_fn_t(struct net_pkt *pkt, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[npf_local_in_fn_t](#ga673493f74227912cf8f5827a77af012f)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

用于取得网络数据包处理判定（Verdict）的函数。

<a id="r_ga7522a5a2188f7afbdc1a0528782ce0ef"></a>

```c
typedef void(* npf_rule_cb_t) (struct npf_rule *rule, enum npf_rule_type type, void *user_data)
```

相关声明：[npf_rule_cb_t](#ga7522a5a2188f7afbdc1a0528782ce0ef)、[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)、[npf_rule_type](#gaad4624a8e6c9491572e2a89739304530)。

遍历网络数据包过滤规则（Packet Filter Rules）时使用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_gaad4624a8e6c9491572e2a89739304530"></a>

```c
enum npf_rule_type { NPF_RULE_TYPE_UNKNOWN = 0 , NPF_RULE_TYPE_SEND , NPF_RULE_TYPE_RECV , NPF_RULE_TYPE_LOCAL_IN_RECV , NPF_RULE_TYPE_IPV4_RECV , NPF_RULE_TYPE_IPV6_RECV }
```

相关声明：[npf_rule_type](#gaad4624a8e6c9491572e2a89739304530)、[NPF_RULE_TYPE_UNKNOWN](#ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca)、[NPF_RULE_TYPE_SEND](#ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81)、[NPF_RULE_TYPE_RECV](#ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f)、[NPF_RULE_TYPE_LOCAL_IN_RECV](#ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b)、[NPF_RULE_TYPE_IPV4_RECV](#ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc)、[NPF_RULE_TYPE_IPV6_RECV](#ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2)。

数据包过滤规则类型（Packet Filter Rule Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga188b9d73f47a77ce05d728250606e7ec"></a>

```c
void npf_rules_foreach (npf_rule_cb_t cb, void *user_data)
```

相关声明：[npf_rules_foreach](#ga188b9d73f47a77ce05d728250606e7ec)、[npf_rule_cb_t](#ga7522a5a2188f7afbdc1a0528782ce0ef)。

遍历所有网络数据包过滤规则（Packet Filter Rules），并为每条规则调用回调。

## 4.5\_详细说明（Detailed Documentation）

<a id="ga7cf793af7b91eccc6e675ff19ed59a14"></a>

### `NPF_ETH_DST_ADDR_MASK_MATCH`

```c
#define NPF_ETH_DST_ADDR_MASK_MATCH ( _name, _addr_array, ... )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_addr _name = {                              \
        .addresses = (_addr_array),                             \
        .nb_addresses = ARRAY_SIZE(_addr_array),                \
        .mask.addr = { __VA_ARGS__ },                           \
        .test.fn = npf_eth_dst_addr_match,                      \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "eth dst mask",                \
                    .test.type = NPF_TEST_TYPE_ETH_DST_ADDR_MASK_MATCH,)) \
}
```

静态定义“带掩码的目的地址匹配”（Destination Address Match with Mask）数据包过滤条件。

应用指定掩码（Mask）后，检查数据包目的地址是否与所给集合中的任一以太网地址（Ethernet Address）匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_addr_array` | 用于比较的 `struct net_eth_addr` 条目数组。 |
| `...` | 最多 6 个掩码字节（Mask Bytes）。 |

<a id="ga3d22d687bcd56b7727c51c7bc7f36cac"></a>

### `NPF_ETH_DST_ADDR_MATCH`

```c
#define NPF_ETH_DST_ADDR_MATCH ( _name, _addr_array )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_addr _name = {                              \
        .addresses = (_addr_array),                             \
        .nb_addresses = ARRAY_SIZE(_addr_array),                \
        .test.fn = npf_eth_dst_addr_match,                      \
        .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },    \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "eth dst",                     \
                    .test.type = NPF_TEST_TYPE_ETH_DST_ADDR_MATCH,)) \
}
```

静态定义“目的地址匹配”（Destination Address Match）数据包过滤条件。

检查数据包目的地址（Destination Address）是否与所给集合中的任一以太网地址匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_addr_array` | 用于比较的 `struct net_eth_addr` 条目数组。 |

<a id="ga3b8a8a22eb992c0e02223f70723c3641"></a>

### `NPF_ETH_DST_ADDR_UNMATCH`

```c
#define NPF_ETH_DST_ADDR_UNMATCH ( _name, _addr_array )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_addr _name = {                              \
        .addresses = (_addr_array),                             \
        .nb_addresses = ARRAY_SIZE(_addr_array),                \
        .test.fn = npf_eth_dst_addr_unmatch,                    \
        .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },    \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "!eth dst",                    \
                    .test.type = NPF_TEST_TYPE_ETH_DST_ADDR_UNMATCH,)) \
}
```

静态定义“目的地址不匹配”（Destination Address Unmatch）数据包过滤条件。

检查数据包目的地址（Destination Address）是否与所给集合中的所有以太网地址都不匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_addr_array` | 用于比较的 `struct net_eth_addr` 条目数组。 |

<a id="ga0e06ebc4c9a1a960651be1ba89eeb2fd"></a>

### `NPF_ETH_SRC_ADDR_MASK_MATCH`

```c
#define NPF_ETH_SRC_ADDR_MASK_MATCH ( _name, _addr_array, ... )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_addr _name = {                              \
        .addresses = (_addr_array),                             \
        .nb_addresses = ARRAY_SIZE(_addr_array),                \
        .mask.addr = { __VA_ARGS__ },                           \
        .test.fn = npf_eth_src_addr_match,                      \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "eth src mask",                \
                    .test.type = NPF_TEST_TYPE_ETH_SRC_ADDR_MASK_MATCH,)) \
}
```

静态定义“带掩码的源地址匹配”（Source Address Match with Mask）数据包过滤条件。

应用指定掩码（Mask）后，检查数据包源地址是否与所给集合中的任一以太网地址（Ethernet Address）匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_addr_array` | 用于比较的 `struct net_eth_addr` 条目数组。 |
| `...` | 最多 6 个掩码字节（Mask Bytes）。 |

<a id="gad2141ad8d6639c9b92569d55130ca1b1"></a>

### `NPF_ETH_SRC_ADDR_MATCH`

```c
#define NPF_ETH_SRC_ADDR_MATCH ( _name, _addr_array )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_addr _name = {                              \
        .addresses = (_addr_array),                             \
        .nb_addresses = ARRAY_SIZE(_addr_array),                \
        .test.fn = npf_eth_src_addr_match,                      \
        .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },    \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "eth src",                     \
                    .test.type = NPF_TEST_TYPE_ETH_SRC_ADDR_MATCH,)) \
}
```

静态定义“源地址匹配”（Source Address Match）数据包过滤条件。

检查数据包源地址（Source Address）是否与所给集合中的任一以太网地址匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_addr_array` | 用于比较的 `struct net_eth_addr` 条目数组。 |

<a id="ga228eaa3784f663d8f2e2711e26409043"></a>

### `NPF_ETH_SRC_ADDR_UNMATCH`

```c
#define NPF_ETH_SRC_ADDR_UNMATCH ( _name, _addr_array )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_addr _name = {                              \
        .addresses = (_addr_array),                             \
        .nb_addresses = ARRAY_SIZE(_addr_array),                \
        .test.fn = npf_eth_src_addr_unmatch,                    \
        .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },    \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "!eth src",                    \
                    .test.type = NPF_TEST_TYPE_ETH_SRC_ADDR_UNMATCH,)) \
}
```

静态定义“源地址不匹配”（Source Address Unmatch）数据包过滤条件。

检查数据包源地址（Source Address）是否与所给集合中的所有以太网地址都不匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_addr_array` | 用于比较的 `struct net_eth_addr` 条目数组。 |

<a id="gace7de72d4c64e128a825f28f94d8b1b2"></a>

### `NPF_ETH_TYPE_MATCH`

```c
#define NPF_ETH_TYPE_MATCH ( _name, _type )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_type _name = {                              \
        .type = net_htons(_type),                               \
        .test.fn = npf_eth_type_match,                          \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "eth type",                    \
                    .test.type = NPF_TEST_TYPE_ETH_TYPE_MATCH,)) \
}
```

静态定义“以太网类型匹配”（Ethernet Type Match）数据包过滤条件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_type` | 要匹配的以太网类型（Ethernet Type）。 |

<a id="gab9bf6d58433e273220c5fab76f608545"></a>

### `NPF_ETH_TYPE_UNMATCH`

```c
#define NPF_ETH_TYPE_UNMATCH ( _name, _type )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_type _name = {                              \
        .type = net_htons(_type),                               \
        .test.fn = npf_eth_type_unmatch,                        \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "!eth type",                   \
                    .test.type = NPF_TEST_TYPE_ETH_TYPE_UNMATCH,)) \
}
```

静态定义“以太网类型不匹配”（Ethernet Type Unmatch）数据包过滤条件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_type` | 要排除的以太网类型（Ethernet Type）。 |

<a id="ga2d67631c0fdd659a8e9db62c6f0a87bf"></a>

### `NPF_ETH_VLAN_TYPE_MATCH`

```c
#define NPF_ETH_VLAN_TYPE_MATCH ( _name, _type )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_type _name = {                              \
        .type = net_htons(_type),                               \
        .test.fn = npf_eth_vlan_type_match,                     \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "eth vlan type",               \
                    .test.type = NPF_TEST_TYPE_ETH_VLAN_TYPE_MATCH,)) \
}
```

静态定义“以太网 VLAN 头部类型匹配”（Ethernet VLAN Header Type Match）数据包过滤条件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_type` | 要匹配的以太网 VLAN 头部类型（Header Type）。 |

<a id="ga49af5d0231e15932607da955ca7e4b34"></a>

### `NPF_ETH_VLAN_TYPE_UNMATCH`

```c
#define NPF_ETH_VLAN_TYPE_UNMATCH ( _name, _type )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_eth_type _name = {                              \
        .type = net_htons(_type),                               \
        .test.fn = npf_eth_vlan_type_unmatch,                   \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "!eth vlan type",              \
                    .test.type = NPF_TEST_TYPE_ETH_VLAN_TYPE_UNMATCH,)) \
}
```

静态定义“以太网 VLAN 头部类型不匹配”（Ethernet VLAN Header Type Unmatch）数据包过滤条件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_type` | 要排除的以太网 VLAN 头部类型（Header Type）。 |

<a id="ga61b8c41e90b61041c50cd6206c4dfcfe"></a>

### `NPF_LOCAL_IN_MATCH`

```c
#define NPF_LOCAL_IN_MATCH ( _name, _handler, _user_data )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_test_local_in _name = {                              \
        .test.fn = npf_local_in_match,                          \
        .fn = (_handler),                                       \
        .user_data = (_user_data),                              \
        IF_ENABLED(NPF_TEST_ENABLE_NAME,                        \
                   (.test.name = "local_in",                    \
                    .test.type = NPF_TEST_TYPE_LOCAL_IN_MATCH,)) \
}
```

静态定义“local_in 匹配”（local_in Match）数据包过滤条件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 条件名称（Condition Name）。 |
| `_handler` | `local_in` 钩子（Hook）调用的函数。 |
| `_user_data` | 传给处理函数（Handler）的可选用户数据指针。 |

<a id="ga673493f74227912cf8f5827a77af012f"></a>

### `npf_local_in_fn_t`

```c
typedef bool npf_local_in_fn_t(struct net_pkt *pkt, void *user_data)
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

用于取得网络数据包处理判定（Verdict）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 指向要评估的网络数据包（Network Packet）的指针。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

**返回（Returns）**：返回值：数据包匹配时返回 `true`，否则返回 `false`。

<a id="ga7522a5a2188f7afbdc1a0528782ce0ef"></a>

### `npf_rule_cb_t`

```c
typedef void(* npf_rule_cb_t) (struct npf_rule *rule, enum npf_rule_type type, void *user_data)
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

遍历网络数据包过滤规则（Packet Filter Rules）时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rule` | 指向当前网络数据包过滤规则（Packet Filter Rule）的指针。 |
| `type` | 规则类型（Rule Type）：`rx`、`tx`、`local_in`、IPv4 或 IPv6。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="gaad4624a8e6c9491572e2a89739304530"></a>

### `npf_rule_type`

```c
enum npf_rule_type
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

数据包过滤规则类型（Packet Filter Rule Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPF_RULE_TYPE_UNKNOWN` | 未知规则类型（Unknown Rule Type）。 |
| `NPF_RULE_TYPE_SEND` | 用于传出数据包（Outgoing Packets）的规则。 |
| `NPF_RULE_TYPE_RECV` | 用于传入数据包（Incoming Packets）的规则。 |
| `NPF_RULE_TYPE_LOCAL_IN_RECV` | 用于本地传入数据包（Local Incoming Packets）的规则。 |
| `NPF_RULE_TYPE_IPV4_RECV` | 用于 IPv4 传入数据包（Incoming Packets）的规则。 |
| `NPF_RULE_TYPE_IPV6_RECV` | 用于 IPv6 传入数据包（Incoming Packets）的规则。 |

<a id="ga188b9d73f47a77ce05d728250606e7ec"></a>

### `npf_rules_foreach()`

```c
void npf_rules_foreach ( npf_rule_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

遍历所有网络数据包过滤规则（Packet Filter Rules），并为每条规则调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |


## 4.6\_原页交叉引用（Cross References）

- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)
- [zephyr/net/net_pkt_filter.h](../api_file_secure_value_reference/P010_zephyr__net__net_pkt_filter.h_文件参考.md)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [net_htons](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae20291eed240d648d0ef7e13822f925f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__ip__4__6_html_gae20291eed240d648d0ef7e13822f925f"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca"></a>
<a id="ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81"></a>
<a id="ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f"></a>
<a id="ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b"></a>
<a id="ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc"></a>
<a id="ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_微芯（Microchip）.md) · [返回大纲](大纲.md) · [下一章](P005_PCIe 控制器驱动后端 API.md)
