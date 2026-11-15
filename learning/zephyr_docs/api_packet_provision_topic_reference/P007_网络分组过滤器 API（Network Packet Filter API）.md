---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-7
title: 网络分组过滤器 API（Network Packet Filter API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_网络分组过滤器 API（Network Packet Filter API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络分组过滤器 API（Network Packet Filter API）

<a id="details"></a>

网络数据包过滤器（Network Packet Filter）API。自 3.0 起提供，版本 0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 7.1\_主题（Topics）

<a id="r_npf_5Fbasic_5Fcond"></a>

相关声明：[基本过滤条件（Basic Filter Conditions）](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md)。

<a id="r_npf_5Feth_5Fcond"></a>

相关声明：[以太网过滤条件（Ethernet Filter Conditions）](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.2\_数据结构（Data Structures）

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

## 7.3\_宏定义（Macros）

<a id="r_ga2f45093d5ad164d5c51a8996f7f04d32"></a>

```c
#define NPF_RULE(_name, _result, ...)
```

相关声明：[NPF_RULE](#ga2f45093d5ad164d5c51a8996f7f04d32)。

静态定义一条数据包过滤规则（Packet Filter Rule）。

<a id="r_ga3b740a5ca1ad99aa593bfa30a39c41f2"></a>

```c
#define NPF_PRIORITY(_name, _priority, ...)
```

相关声明：[NPF_PRIORITY](#ga3b740a5ca1ad99aa593bfa30a39c41f2)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.4\_函数（Functions）

<a id="r_ga3b2a85558b6756e76760d9a40c780e28"></a>

```c
void npf_insert_rule (struct npf_rule_list *rules, struct npf_rule *rule)
```

相关声明：[npf_insert_rule](#ga3b2a85558b6756e76760d9a40c780e28)、[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)。

在所给规则列表（Rule List）首部插入规则。

<a id="r_gadfa956e4af3c45460846fc22f863e697"></a>

```c
void npf_append_rule (struct npf_rule_list *rules, struct npf_rule *rule)
```

相关声明：[npf_append_rule](#gadfa956e4af3c45460846fc22f863e697)、[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)。

在所给规则列表（Rule List）末尾追加规则。

<a id="r_ga4d7426db901debff35e1de5805e06c71"></a>

```c
bool npf_remove_rule (struct npf_rule_list *rules, struct npf_rule *rule)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[npf_remove_rule](#ga4d7426db901debff35e1de5805e06c71)、[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)。

从所给规则列表（Rule List）移除规则。

<a id="r_ga54916eb4943e4b47cd31eb23827d0dd5"></a>

```c
bool npf_remove_all_rules (struct npf_rule_list *rules)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[npf_remove_all_rules](#ga54916eb4943e4b47cd31eb23827d0dd5)、[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)。

从所给规则列表（Rule List）移除全部规则。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 7.5\_变量（Variables）

<a id="r_gaac489d75c023952243589cba7ff7367a"></a>

```c
struct npf_rule npf_default_ok
```

相关声明：[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)、[npf_default_ok](#gaac489d75c023952243589cba7ff7367a)。

接受数据包的默认规则列表终止项（Default Rule List Termination）。

<a id="r_ga8fc592feedeceb5172f8747a29697dd7"></a>

```c
struct npf_rule npf_default_drop
```

相关声明：[npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)、[npf_default_drop](#ga8fc592feedeceb5172f8747a29697dd7)。

拒绝数据包的默认规则列表终止项（Default Rule List Termination）。

<a id="r_ga8017a041d3168c76e39bdfac011b9315"></a>

```c
struct npf_rule_list npf_send_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_send_rules](#ga8017a041d3168c76e39bdfac011b9315)。

用于传出数据包（Outgoing Packets）的规则列表。

<a id="r_ga9714529658625e906264a46ad1a9be6f"></a>

```c
struct npf_rule_list npf_recv_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_recv_rules](#ga9714529658625e906264a46ad1a9be6f)。

用于传入数据包（Incoming Packets）的规则列表。

<a id="r_ga571e9fb34eb4e3cbf38f885b5e786021"></a>

```c
struct npf_rule_list npf_local_in_recv_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_local_in_recv_rules](#ga571e9fb34eb4e3cbf38f885b5e786021)。

用于本地传入数据包（Local Incoming Packets）的规则列表。

<a id="r_gad521d7ac3270970833aec48d8a517d85"></a>

```c
struct npf_rule_list npf_ipv4_recv_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_ipv4_recv_rules](#gad521d7ac3270970833aec48d8a517d85)。

用于 IPv4 传入数据包（Incoming Packets）的规则列表。

<a id="r_gab91ca81aab2da48066538d72caf0c8ae"></a>

```c
struct npf_rule_list npf_ipv6_recv_rules
```

相关声明：[npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)、[npf_ipv6_recv_rules](#gab91ca81aab2da48066538d72caf0c8ae)。

用于 IPv6 传入数据包（Incoming Packets）的规则列表。

## 7.6\_详细说明（Detailed Documentation）

<a id="ga3b740a5ca1ad99aa593bfa30a39c41f2"></a>

### `NPF_PRIORITY`

```c
#define NPF_PRIORITY ( _name, _priority, ... )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_rule _name = {                                       \
        .result = NET_CONTINUE,                                 \
        .priority = (_priority),                                \
        .nb_tests = NUM_VA_ARGS_LESS_1(__VA_ARGS__) + 1,        \
        .tests = {FOR_EACH(Z_NPF_TEST_ADDR, (,), __VA_ARGS__)}, \
}
```

<a id="ga2f45093d5ad164d5c51a8996f7f04d32"></a>

### `NPF_RULE`

```c
#define NPF_RULE ( _name, _result, ... )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

展开值（Value）：

```c
struct npf_rule _name = {                                         \
        .result = (_result),                                      \
        .nb_tests = NUM_VA_ARGS_LESS_1(__VA_ARGS__) + 1,          \
        .tests = { FOR_EACH(Z_NPF_TEST_ADDR, (,), __VA_ARGS__) }, \
}
```

静态定义一条数据包过滤规则（Packet Filter Rule）。

使用数量可变的过滤条件（Filter Conditions）创建规则。随后可将此规则插入或追加到所给网络数据包路径（Packet Path）的规则列表。

示例：

原始示例（Example）：

```c
static NPF_SIZE_MAX(maxsize_200, 200);
static NPF_ETH_TYPE_MATCH(ip_packet, NET_ETH_PTYPE_IP);

static NPF_RULE(small_ip_pkt, NET_OK, ip_packet, maxsize_200);

void install_my_filter(void)
{
    npf_insert_recv_rule(&npf_default_drop);
    npf_insert_recv_rule(&small_ip_pkt);
}
```

上述规则接受大小不超过 200 字节的 IP 数据包，并丢弃其他全部数据包。

实现相同结果的另一种效率较低的方式如下：

原始示例（Example）：

```c
static NPF_SIZE_MIN(minsize_201, 201);
static NPF_ETH_TYPE_UNMATCH(not_ip_packet, NET_ETH_PTYPE_IP);

static NPF_RULE(reject_big_pkts, NET_DROP, minsize_201);
static NPF_RULE(reject_non_ip, NET_DROP, not_ip_packet);

void install_my_filter(void) {
    npf_append_recv_rule(&reject_big_pkts);
    npf_append_recv_rule(&reject_non_ip);
    npf_append_recv_rule(&npf_default_ok);
}
```

列表中第一条满足全部条件的规则决定数据包的处理结果。若某个条件为假，则继续评估列表中的下一条规则。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 此规则的名称（Rule Name）。 |
| `_result` | 所有条件均满足时的数据包处理结果，为 `NET_OK` 或 `NET_DROP`。 |
| `...` | 此规则的条件列表（Condition List）。 |

<a id="gadfa956e4af3c45460846fc22f863e697"></a>

### `npf_append_rule()`

```c
void npf_append_rule ( struct npf_rule_list * rules, struct npf_rule * rule )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

在所给规则列表（Rule List）末尾追加规则。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rules` | 受影响的规则列表（Rule List）。 |
| `rule` | 要追加的规则（Rule）。 |

<a id="ga3b2a85558b6756e76760d9a40c780e28"></a>

### `npf_insert_rule()`

```c
void npf_insert_rule ( struct npf_rule_list * rules, struct npf_rule * rule )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

在所给规则列表（Rule List）首部插入规则。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rules` | 受影响的规则列表（Rule List）。 |
| `rule` | 要插入的规则（Rule）。 |

<a id="ga54916eb4943e4b47cd31eb23827d0dd5"></a>

### `npf_remove_all_rules()`

```c
bool npf_remove_all_rules ( struct npf_rule_list * rules)
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

从所给规则列表（Rule List）移除全部规则。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rules` | 受影响的规则列表（Rule List）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 至少从规则列表移除了一条规则时。 |

<a id="ga4d7426db901debff35e1de5805e06c71"></a>

### `npf_remove_rule()`

```c
bool npf_remove_rule ( struct npf_rule_list * rules, struct npf_rule * rule )
```

```c
#include <zephyr/net/net_pkt_filter.h>
```

从所给规则列表（Rule List）移除规则。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rules` | 受影响的规则列表（Rule List）。 |
| `rule` | 要移除的规则（Rule）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 在规则列表中找到并移除了所给规则时。 |

<a id="ga8fc592feedeceb5172f8747a29697dd7"></a>

### `npf_default_drop`

```c
struct npf_rule npf_default_drop
```

声明属性：`extern`。

```c
#include <zephyr/net/net_pkt_filter.h>
```

拒绝数据包的默认规则列表终止项（Default Rule List Termination）。

<a id="gaac489d75c023952243589cba7ff7367a"></a>

### `npf_default_ok`

```c
struct npf_rule npf_default_ok
```

声明属性：`extern`。

```c
#include <zephyr/net/net_pkt_filter.h>
```

接受数据包的默认规则列表终止项（Default Rule List Termination）。

<a id="gad521d7ac3270970833aec48d8a517d85"></a>

### `npf_ipv4_recv_rules`

```c
struct npf_rule_list npf_ipv4_recv_rules
```

声明属性：`extern`。

```c
#include <zephyr/net/net_pkt_filter.h>
```

用于 IPv4 传入数据包（Incoming Packets）的规则列表。

<a id="gab91ca81aab2da48066538d72caf0c8ae"></a>

### `npf_ipv6_recv_rules`

```c
struct npf_rule_list npf_ipv6_recv_rules
```

声明属性：`extern`。

```c
#include <zephyr/net/net_pkt_filter.h>
```

用于 IPv6 传入数据包（Incoming Packets）的规则列表。

<a id="ga571e9fb34eb4e3cbf38f885b5e786021"></a>

### `npf_local_in_recv_rules`

```c
struct npf_rule_list npf_local_in_recv_rules
```

声明属性：`extern`。

```c
#include <zephyr/net/net_pkt_filter.h>
```

用于本地传入数据包（Local Incoming Packets）的规则列表。

<a id="ga9714529658625e906264a46ad1a9be6f"></a>

### `npf_recv_rules`

```c
struct npf_rule_list npf_recv_rules
```

声明属性：`extern`。

```c
#include <zephyr/net/net_pkt_filter.h>
```

用于传入数据包（Incoming Packets）的规则列表。

<a id="ga8017a041d3168c76e39bdfac011b9315"></a>

### `npf_send_rules`

```c
struct npf_rule_list npf_send_rules
```

声明属性：`extern`。

```c
#include <zephyr/net/net_pkt_filter.h>
```

用于传出数据包（Outgoing Packets）的规则列表。


## 7.7\_原页交叉引用（Cross References）

- [基本过滤条件（Basic Filter Conditions）](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md)
- [以太网过滤条件（Ethernet Filter Conditions）](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html)
- [npf_test](../network_service_model_reference/P037_npf_test_结构体.md)
- [npf_rule](../network_service_model_reference/P035_npf_rule_结构体.md)
- [npf_rule_list](../network_service_model_reference/P036_npf_rule_list_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/net_pkt_filter.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h.html)
- [NET_CONTINUE](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)
- [NUM_VA_ARGS_LESS_1](../util_reference/P001_通用工具公共接口.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)
- [FOR_EACH](../util_reference/P001_通用工具公共接口.md#ga278c8b7cbbea2f585e371d3568f3cb12)
- [NPF_SIZE_MAX](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gacd56b9bcf2b2ba4759402650a9bff67a)
- [NPF_ETH_TYPE_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gace7de72d4c64e128a825f28f94d8b1b2)
- [NET_OK](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)
- [NPF_SIZE_MIN](../api_power_policy_topic_reference/P009_基本过滤条件（Basic Filter Conditions）.md#gaf142455f9bea3dea8faa0a913072b63e)
- [NPF_ETH_TYPE_UNMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__npf__eth__cond.html#gab9bf6d58433e273220c5fab76f608545)
- [NET_DROP](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__net__core_html_gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f"></a>
<a id="agroup__sys-util_html_ga278c8b7cbbea2f585e371d3568f3cb12"></a>
<a id="agroup__sys-util_html_ga8a0e9835e0a8f864ffc2359b9c419cc2"></a>
<a id="astructnpf__rule_html"></a>
<a id="agroup__net__core_html_gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047"></a>
<a id="agroup__net__pkt__filter_html_ga2f45093d5ad164d5c51a8996f7f04d32"></a>
<a id="agroup__net__pkt__filter_html_ga8fc592feedeceb5172f8747a29697dd7"></a>
<a id="agroup__npf__basic__cond_html_gacd56b9bcf2b2ba4759402650a9bff67a"></a>
<a id="agroup__npf__eth__cond_html_gace7de72d4c64e128a825f28f94d8b1b2"></a>
<a id="agroup__net__core_html_gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3"></a>
<a id="agroup__net__pkt__filter_html_gaac489d75c023952243589cba7ff7367a"></a>
<a id="agroup__npf__basic__cond_html_gaf142455f9bea3dea8faa0a913072b63e"></a>
<a id="agroup__npf__eth__cond_html_gab9bf6d58433e273220c5fab76f608545"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P006_键盘矩阵（Keyboard Matrix）.md) · [返回大纲](大纲.md) · [下一章](P008_PCIe 控制器（PCIe Controller）.md)
