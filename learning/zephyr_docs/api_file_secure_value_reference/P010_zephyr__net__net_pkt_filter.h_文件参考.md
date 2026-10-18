---
id: learning.zephyr-docs.api-file-secure-value-reference.page-10
title: zephyr__net__net_pkt_filter.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_net\_\_net\_pkt\_filter.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络数据包过滤（Network Packet Filtering）的公共头文件。

<a id="details"></a>

```c
#include <limits.h>
#include <stdbool.h>
#include <zephyr/sys/slist.h>
#include <zephyr/net/net_core.h>
#include <zephyr/net/ethernet.h>
```

查看此文件的源码。

网络数据包过滤（Network Packet Filtering）公共头文件。网络数据包过滤根据一组基本规则，决定如何处理传入或传出的数据包。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_npf_5Ftest"></a>

```c
struct npf_test
```

相关声明：[npf_test](../network_service_model_reference/P037_npf_test_结构体.md)。

用于嵌入更大结构中的通用过滤器测试结构（Filter Test Structure）。

<a id="r_npf_5Frule"></a>

```c
struct npf_rule
```

相关声明：[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)。

过滤规则（Filter Rule）结构。

<a id="r_npf_5Frule_5Flist"></a>

```c
struct npf_rule_list
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)。

给定测试位置（Test Location）的规则集。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_ga2f45093d5ad164d5c51a8996f7f04d32"></a>

```c
#define NPF_RULE(_name, _result, ...)
```

相关声明：[NPF_RULE](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga2f45093d5ad164d5c51a8996f7f04d32)。

静态定义一条数据包过滤规则（Packet Filter Rule）。

<a id="r_ga3b740a5ca1ad99aa593bfa30a39c41f2"></a>

```c
#define NPF_PRIORITY(_name, _priority, ...)
```

相关声明：[NPF_PRIORITY](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga3b740a5ca1ad99aa593bfa30a39c41f2)。

<a id="r_ga465578272b616c6267ecd13fd86ca73b"></a>

```c
#define NPF_IFACE_MATCH(_name, _iface)
```

相关声明：[NPF_IFACE_MATCH](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#ga465578272b616c6267ecd13fd86ca73b)。

静态定义“接口匹配”（Interface Match）数据包过滤条件（Packet Filter Condition）。

<a id="r_gac3607a6736d70b0ea044a2ec7ab6d313"></a>

```c
#define NPF_IFACE_UNMATCH(_name, _iface)
```

相关声明：[NPF_IFACE_UNMATCH](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gac3607a6736d70b0ea044a2ec7ab6d313)。

静态定义“接口不匹配”（Interface Unmatch）数据包过滤条件（Packet Filter Condition）。

<a id="r_ga55021acd131e4684568aaf6434b08789"></a>

```c
#define NPF_ORIG_IFACE_MATCH(_name, _iface)
```

相关声明：[NPF_ORIG_IFACE_MATCH](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#ga55021acd131e4684568aaf6434b08789)。

静态定义“原始接口匹配”（Orig Interface Match）数据包过滤条件（Packet Filter Condition）。

<a id="r_gad959dc62d47ca3b4d2f24a6c862c7623"></a>

```c
#define NPF_ORIG_IFACE_UNMATCH(_name, _iface)
```

相关声明：[NPF_ORIG_IFACE_UNMATCH](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gad959dc62d47ca3b4d2f24a6c862c7623)。

静态定义“原始接口不匹配”（Orig Interface Unmatch）数据包过滤条件（Packet Filter Condition）。

<a id="r_gaf142455f9bea3dea8faa0a913072b63e"></a>

```c
#define NPF_SIZE_MIN(_name, _size)
```

相关声明：[NPF_SIZE_MIN](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gaf142455f9bea3dea8faa0a913072b63e)。

静态定义“数据最小大小”（Data Minimum Size）数据包过滤条件（Packet Filter Condition）。

<a id="r_gacd56b9bcf2b2ba4759402650a9bff67a"></a>

```c
#define NPF_SIZE_MAX(_name, _size)
```

相关声明：[NPF_SIZE_MAX](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gacd56b9bcf2b2ba4759402650a9bff67a)。

静态定义“数据最大大小”（Data Maximum Size）数据包过滤条件（Packet Filter Condition）。

<a id="r_gab402bb13c7899d57532d3dcf8a36ed4b"></a>

```c
#define NPF_SIZE_BOUNDS(_name, _min_size, _max_size)
```

相关声明：[NPF_SIZE_BOUNDS](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gab402bb13c7899d57532d3dcf8a36ed4b)。

静态定义“数据大小范围”（Data Bounded Size）数据包过滤条件（Packet Filter Condition）。

<a id="r_ga4dd013f0fb92eb0433f174cf40e89e00"></a>

```c
#define NPF_IP_SRC_ADDR_ALLOWLIST(_name, _ip_addr_array, _ip_addr_num, _af)
```

相关声明：[NPF_IP_SRC_ADDR_ALLOWLIST](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#ga4dd013f0fb92eb0433f174cf40e89e00)。

静态定义“IP 地址允许列表”（IP Address Allowlist）数据包过滤条件（Packet Filter Condition）。

<a id="r_ga57fe28a992b1afaf33581292fe5015bd"></a>

```c
#define NPF_IP_SRC_ADDR_BLOCKLIST(_name, _ip_addr_array, _ip_addr_num, _af)
```

相关声明：[NPF_IP_SRC_ADDR_BLOCKLIST](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#ga57fe28a992b1afaf33581292fe5015bd)。

静态定义“IP 地址阻止列表”（IP Address Blocklist）数据包过滤条件（Packet Filter Condition）。

<a id="r_gad2141ad8d6639c9b92569d55130ca1b1"></a>

```c
#define NPF_ETH_SRC_ADDR_MATCH(_name, _addr_array)
```

相关声明：[NPF_ETH_SRC_ADDR_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gad2141ad8d6639c9b92569d55130ca1b1)。

静态定义“源地址匹配”（Source Address Match）数据包过滤条件。

<a id="r_ga228eaa3784f663d8f2e2711e26409043"></a>

```c
#define NPF_ETH_SRC_ADDR_UNMATCH(_name, _addr_array)
```

相关声明：[NPF_ETH_SRC_ADDR_UNMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga228eaa3784f663d8f2e2711e26409043)。

静态定义“源地址不匹配”（Source Address Unmatch）数据包过滤条件。

<a id="r_ga3d22d687bcd56b7727c51c7bc7f36cac"></a>

```c
#define NPF_ETH_DST_ADDR_MATCH(_name, _addr_array)
```

相关声明：[NPF_ETH_DST_ADDR_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga3d22d687bcd56b7727c51c7bc7f36cac)。

静态定义“目的地址匹配”（Destination Address Match）数据包过滤条件。

<a id="r_ga3b8a8a22eb992c0e02223f70723c3641"></a>

```c
#define NPF_ETH_DST_ADDR_UNMATCH(_name, _addr_array)
```

相关声明：[NPF_ETH_DST_ADDR_UNMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga3b8a8a22eb992c0e02223f70723c3641)。

静态定义“目的地址不匹配”（Destination Address Unmatch）数据包过滤条件。

<a id="r_ga0e06ebc4c9a1a960651be1ba89eeb2fd"></a>

```c
#define NPF_ETH_SRC_ADDR_MASK_MATCH(_name, _addr_array, ...)
```

相关声明：[NPF_ETH_SRC_ADDR_MASK_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga0e06ebc4c9a1a960651be1ba89eeb2fd)。

静态定义“带掩码的源地址匹配”（Source Address Match with Mask）数据包过滤条件。

<a id="r_ga7cf793af7b91eccc6e675ff19ed59a14"></a>

```c
#define NPF_ETH_DST_ADDR_MASK_MATCH(_name, _addr_array, ...)
```

相关声明：[NPF_ETH_DST_ADDR_MASK_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga7cf793af7b91eccc6e675ff19ed59a14)。

静态定义“带掩码的目的地址匹配”（Destination Address Match with Mask）数据包过滤条件。

<a id="r_gace7de72d4c64e128a825f28f94d8b1b2"></a>

```c
#define NPF_ETH_TYPE_MATCH(_name, _type)
```

相关声明：[NPF_ETH_TYPE_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gace7de72d4c64e128a825f28f94d8b1b2)。

静态定义“以太网类型匹配”（Ethernet Type Match）数据包过滤条件。

<a id="r_gab9bf6d58433e273220c5fab76f608545"></a>

```c
#define NPF_ETH_TYPE_UNMATCH(_name, _type)
```

相关声明：[NPF_ETH_TYPE_UNMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gab9bf6d58433e273220c5fab76f608545)。

静态定义“以太网类型不匹配”（Ethernet Type Unmatch）数据包过滤条件。

<a id="r_ga2d67631c0fdd659a8e9db62c6f0a87bf"></a>

```c
#define NPF_ETH_VLAN_TYPE_MATCH(_name, _type)
```

相关声明：[NPF_ETH_VLAN_TYPE_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga2d67631c0fdd659a8e9db62c6f0a87bf)。

静态定义“以太网 VLAN 头部类型匹配”（Ethernet VLAN Header Type Match）数据包过滤条件。

<a id="r_ga49af5d0231e15932607da955ca7e4b34"></a>

```c
#define NPF_ETH_VLAN_TYPE_UNMATCH(_name, _type)
```

相关声明：[NPF_ETH_VLAN_TYPE_UNMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga49af5d0231e15932607da955ca7e4b34)。

静态定义“以太网 VLAN 头部类型不匹配”（Ethernet VLAN Header Type Unmatch）数据包过滤条件。

<a id="r_ga61b8c41e90b61041c50cd6206c4dfcfe"></a>

```c
#define NPF_LOCAL_IN_MATCH(_name, _handler, _user_data)
```

相关声明：[NPF_LOCAL_IN_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga61b8c41e90b61041c50cd6206c4dfcfe)。

静态定义“local_in 匹配”（local_in Match）数据包过滤条件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.3\_类型定义（Typedefs）

<a id="r_ga673493f74227912cf8f5827a77af012f"></a>

```c
typedef bool npf_local_in_fn_t(struct net_pkt *pkt, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[npf_local_in_fn_t](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga673493f74227912cf8f5827a77af012f)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

用于取得网络数据包处理判定（Verdict）的函数。

<a id="r_ga7522a5a2188f7afbdc1a0528782ce0ef"></a>

```c
typedef void(* npf_rule_cb_t) (struct npf_rule *rule, enum npf_rule_type type, void *user_data)
```

相关声明：[npf_rule_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga7522a5a2188f7afbdc1a0528782ce0ef)、[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)、[npf_rule_type](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gaad4624a8e6c9491572e2a89739304530)。

遍历网络数据包过滤规则（Packet Filter Rules）时使用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.4\_枚举（Enumerations）

<a id="r_gaad4624a8e6c9491572e2a89739304530"></a>

```c
enum npf_rule_type { NPF_RULE_TYPE_UNKNOWN = 0 , NPF_RULE_TYPE_SEND , NPF_RULE_TYPE_RECV , NPF_RULE_TYPE_LOCAL_IN_RECV , NPF_RULE_TYPE_IPV4_RECV , NPF_RULE_TYPE_IPV6_RECV }
```

相关声明：[npf_rule_type](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gaad4624a8e6c9491572e2a89739304530)、[NPF_RULE_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca)、[NPF_RULE_TYPE_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81)、[NPF_RULE_TYPE_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f)、[NPF_RULE_TYPE_LOCAL_IN_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b)、[NPF_RULE_TYPE_IPV4_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc)、[NPF_RULE_TYPE_IPV6_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2)。

数据包过滤规则类型（Packet Filter Rule Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.5\_函数（Functions）

<a id="r_ga3b2a85558b6756e76760d9a40c780e28"></a>

```c
void npf_insert_rule (struct npf_rule_list *rules, struct npf_rule *rule)
```

相关声明：[npf_insert_rule](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga3b2a85558b6756e76760d9a40c780e28)、[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)。

在所给规则列表（Rule List）首部插入规则。

<a id="r_gadfa956e4af3c45460846fc22f863e697"></a>

```c
void npf_append_rule (struct npf_rule_list *rules, struct npf_rule *rule)
```

相关声明：[npf_append_rule](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#gadfa956e4af3c45460846fc22f863e697)、[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)。

在所给规则列表（Rule List）末尾追加规则。

<a id="r_ga4d7426db901debff35e1de5805e06c71"></a>

```c
bool npf_remove_rule (struct npf_rule_list *rules, struct npf_rule *rule)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[npf_remove_rule](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga4d7426db901debff35e1de5805e06c71)、[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)。

从所给规则列表（Rule List）移除规则。

<a id="r_ga54916eb4943e4b47cd31eb23827d0dd5"></a>

```c
bool npf_remove_all_rules (struct npf_rule_list *rules)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[npf_remove_all_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga54916eb4943e4b47cd31eb23827d0dd5)、[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)。

从所给规则列表（Rule List）移除全部规则。

<a id="r_ga188b9d73f47a77ce05d728250606e7ec"></a>

```c
void npf_rules_foreach (npf_rule_cb_t cb, void *user_data)
```

相关声明：[npf_rules_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga188b9d73f47a77ce05d728250606e7ec)、[npf_rule_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga7522a5a2188f7afbdc1a0528782ce0ef)。

遍历所有网络数据包过滤规则（Packet Filter Rules），并为每条规则调用回调。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 10.6\_变量（Variables）

<a id="r_gaac489d75c023952243589cba7ff7367a"></a>

```c
struct npf_rule npf_default_ok
```

相关声明：[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)、[npf_default_ok](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#gaac489d75c023952243589cba7ff7367a)。

接受数据包的默认规则列表终止项（Default Rule List Termination）。

<a id="r_ga8fc592feedeceb5172f8747a29697dd7"></a>

```c
struct npf_rule npf_default_drop
```

相关声明：[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)、[npf_default_drop](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga8fc592feedeceb5172f8747a29697dd7)。

拒绝数据包的默认规则列表终止项（Default Rule List Termination）。

<a id="r_ga8017a041d3168c76e39bdfac011b9315"></a>

```c
struct npf_rule_list npf_send_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_send_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga8017a041d3168c76e39bdfac011b9315)。

用于传出数据包（Outgoing Packets）的规则列表。

<a id="r_ga9714529658625e906264a46ad1a9be6f"></a>

```c
struct npf_rule_list npf_recv_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_recv_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga9714529658625e906264a46ad1a9be6f)。

用于传入数据包（Incoming Packets）的规则列表。

<a id="r_ga571e9fb34eb4e3cbf38f885b5e786021"></a>

```c
struct npf_rule_list npf_local_in_recv_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_local_in_recv_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga571e9fb34eb4e3cbf38f885b5e786021)。

用于本地传入数据包（Local Incoming Packets）的规则列表。

<a id="r_gad521d7ac3270970833aec48d8a517d85"></a>

```c
struct npf_rule_list npf_ipv4_recv_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_ipv4_recv_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#gad521d7ac3270970833aec48d8a517d85)。

用于 IPv4 传入数据包（Incoming Packets）的规则列表。

<a id="r_gab91ca81aab2da48066538d72caf0c8ae"></a>

```c
struct npf_rule_list npf_ipv6_recv_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_ipv6_recv_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#gab91ca81aab2da48066538d72caf0c8ae)。

用于 IPv6 传入数据包（Incoming Packets）的规则列表。


## 10.7\_原页交叉引用（Cross References）

- [limits.h](../api_source_runtime_reference/P039_limits.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/net/net_core.h](../api_source_system_reference/P023_net_core.h_源码浏览.md)
- [zephyr/net/ethernet.h](../api_source_socket_ethernet_reference/P003_ethernet.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P027_net_pkt_filter.h_源码浏览.md)
- [npf_test](../network_service_model_reference/P037_npf_test_结构体.md)
- [npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)
- [npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)
- [NPF_RULE](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga2f45093d5ad164d5c51a8996f7f04d32)
- [NPF_PRIORITY](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga3b740a5ca1ad99aa593bfa30a39c41f2)
- [NPF_IFACE_MATCH](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#ga465578272b616c6267ecd13fd86ca73b)
- [NPF_IFACE_UNMATCH](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gac3607a6736d70b0ea044a2ec7ab6d313)
- [NPF_ORIG_IFACE_MATCH](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#ga55021acd131e4684568aaf6434b08789)
- [NPF_ORIG_IFACE_UNMATCH](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gad959dc62d47ca3b4d2f24a6c862c7623)
- [NPF_SIZE_MIN](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gaf142455f9bea3dea8faa0a913072b63e)
- [NPF_SIZE_MAX](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gacd56b9bcf2b2ba4759402650a9bff67a)
- [NPF_SIZE_BOUNDS](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gab402bb13c7899d57532d3dcf8a36ed4b)
- [NPF_IP_SRC_ADDR_ALLOWLIST](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#ga4dd013f0fb92eb0433f174cf40e89e00)
- [NPF_IP_SRC_ADDR_BLOCKLIST](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#ga57fe28a992b1afaf33581292fe5015bd)
- [NPF_ETH_SRC_ADDR_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gad2141ad8d6639c9b92569d55130ca1b1)
- [NPF_ETH_SRC_ADDR_UNMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga228eaa3784f663d8f2e2711e26409043)
- [NPF_ETH_DST_ADDR_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga3d22d687bcd56b7727c51c7bc7f36cac)
- [NPF_ETH_DST_ADDR_UNMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga3b8a8a22eb992c0e02223f70723c3641)
- [NPF_ETH_SRC_ADDR_MASK_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga0e06ebc4c9a1a960651be1ba89eeb2fd)
- [NPF_ETH_DST_ADDR_MASK_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga7cf793af7b91eccc6e675ff19ed59a14)
- [NPF_ETH_TYPE_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gace7de72d4c64e128a825f28f94d8b1b2)
- [NPF_ETH_TYPE_UNMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gab9bf6d58433e273220c5fab76f608545)
- [NPF_ETH_VLAN_TYPE_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga2d67631c0fdd659a8e9db62c6f0a87bf)
- [NPF_ETH_VLAN_TYPE_UNMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga49af5d0231e15932607da955ca7e4b34)
- [NPF_LOCAL_IN_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga61b8c41e90b61041c50cd6206c4dfcfe)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [npf_local_in_fn_t](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga673493f74227912cf8f5827a77af012f)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [npf_rule_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga7522a5a2188f7afbdc1a0528782ce0ef)
- [npf_rule_type](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gaad4624a8e6c9491572e2a89739304530)
- [NPF_RULE_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca)
- [NPF_RULE_TYPE_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81)
- [NPF_RULE_TYPE_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f)
- [NPF_RULE_TYPE_LOCAL_IN_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b)
- [NPF_RULE_TYPE_IPV4_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc)
- [NPF_RULE_TYPE_IPV6_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2)
- [npf_insert_rule](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga3b2a85558b6756e76760d9a40c780e28)
- [npf_append_rule](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#gadfa956e4af3c45460846fc22f863e697)
- [npf_remove_rule](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga4d7426db901debff35e1de5805e06c71)
- [npf_remove_all_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga54916eb4943e4b47cd31eb23827d0dd5)
- [npf_rules_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#ga188b9d73f47a77ce05d728250606e7ec)
- [npf_default_ok](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#gaac489d75c023952243589cba7ff7367a)
- [npf_default_drop](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga8fc592feedeceb5172f8747a29697dd7)
- [npf_send_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga8017a041d3168c76e39bdfac011b9315)
- [npf_recv_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga9714529658625e906264a46ad1a9be6f)
- [npf_local_in_recv_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#ga571e9fb34eb4e3cbf38f885b5e786021)
- [npf_ipv4_recv_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#gad521d7ac3270970833aec48d8a517d85)
- [npf_ipv6_recv_rules](../api_packet_provision_topic_reference/P007_网络分组过滤器 API（Network Packet Filter API）.md#gab91ca81aab2da48066538d72caf0c8ae)

<a id="header-details"></a>

---

[上一章](P009_zephyr__mpipe__mpipe_value.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__posix__pthread.h_文件参考.md)
