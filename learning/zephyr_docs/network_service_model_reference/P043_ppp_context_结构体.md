---
id: learning.zephyr-docs.network-service-model-reference.page-43
title: ppp_context_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structppp__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_ppp\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structppp__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

特定网络接口的点对点协议第二层（PPP L2）上下文。

```c
#include <zephyr/net/ppp.h>
```

<a id="details"></a>

特定网络接口的点对点协议第二层（PPP L2）上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_a6b327cafe07a0807163589471a9bdae8"></a>

```c
atomic_t flags
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[flags](#a6b327cafe07a0807163589471a9bdae8)。

表示点对点协议（PPP）状态的标志，会被多个线程访问。

<a id="r_a5671d7ba465c424004f0460e5ed0d3ba"></a>

```c
struct k_work_delayable startup
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[startup](#a5671d7ba465c424004f0460e5ed0d3ba)。

PPP 启动工作项（startup worker）。

```c
struct {
```

<a id="r_a95ece10ca63e64c3efc4e131a2449e6e"></a>

```c
struct ppp_fsm fsm
```

相关声明：[ppp_fsm](P044_ppp_fsm_结构体.md)、[fsm](#ac555024228a1e1d830c915a098428bc5)。

链路控制协议（LCP）的有限状态机（FSM）。

<a id="r_ae50c7d41b569842761063599cfa298b3"></a>

```c
struct lcp_options my_options
```

相关声明：[lcp_options](P028_lcp_options_结构体.md)、[my_options](#a37f609192ee6b739d7018d5a07ce179f)。

本端希望请求的选项。

<a id="r_a6f933e36f81b69b906eab3fcf216c097"></a>

```c
struct lcp_options peer_options
```

相关声明：[lcp_options](P028_lcp_options_结构体.md)、[peer_options](#a80fffd30b145b0842e36299ac78d5da8)。

对端希望请求的选项。

<a id="r_ac210352c904ecbe1fa6c39343018edfb"></a>

```c
uint32_t magic
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[magic](#a4d91bf9e6e36415b13be02ccf03d3e40)。

魔数（Magic-Number）值。

<a id="r_ab8a1c6a9cbbcbcb186a1755bca9f4aab"></a>

```c
struct ppp_my_option_data my_options_data [(1+IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_MRU)+IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_PFC)+IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_ACFC))]
```

相关声明：[my_options_data](#a9d9d3bc0e8434ad93d1904905a2ad75f)、[IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)、[IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)、[IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)。

选项数据。

<a id="r_a7705aedba900cf1de66b02ad488b7161"></a>

```c
} lcp
```

相关声明：[lcp](#a7705aedba900cf1de66b02ad488b7161)。

LCP 选项。

<a id="r_a3b0bfb9c3ceece34565b282efa74390e"></a>

```c
struct net_if * iface
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[iface](#a3b0bfb9c3ceece34565b282efa74390e)。

与此 PPP 连接关联的网络接口。

<a id="r_a6afb964ef87696fdadb5cb0c714bd841"></a>

```c
enum ppp_phase phase
```

相关声明：[ppp_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga284e237a6323f2daffc444a73a4b8b6b)、[phase](#a6afb964ef87696fdadb5cb0c714bd841)。

PPP 链路当前所处阶段（phase）。

<a id="r_a1afa42c99b098407f8bba11e50178c84"></a>

```c
struct k_sem wait_ppp_link_terminated
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[wait_ppp_link_terminated](#a1afa42c99b098407f8bba11e50178c84)。

PPP 链路终止时发出的信号。

<a id="r_ae784688e2d78f7427c6672583e326d94"></a>

```c
struct k_sem wait_ppp_link_down
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[wait_ppp_link_down](#ae784688e2d78f7427c6672583e326d94)。

PPP 链路关闭（down）时发出的信号。

<a id="r_a1c6674bad19047abcc3097bf5ff5f31d"></a>

```c
enum net_l2_flags ppp_l2_flags
```

相关声明：[net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)、[ppp_l2_flags](#a1c6674bad19047abcc3097bf5ff5f31d)。

表示 PPP 支持哪些特性。

<a id="r_a2e04c6e411fe5b07d9d2cda1a61db57f"></a>

```c
int network_protos_open
```

相关声明：[network_protos_open](#a2e04c6e411fe5b07d9d2cda1a61db57f)。

表示有多少个网络协议已打开（open）。

<a id="r_a9dd6e156897c53d488344bbbe05d4ae1"></a>

```c
int network_protos_up
```

相关声明：[network_protos_up](#a9dd6e156897c53d488344bbbe05d4ae1)。

表示有多少个网络协议已启用（up）。

<a id="r_a3d97c93b183ca455daf0e3bc2b9c25e1"></a>

```c
uint16_t is_ready_to_serve: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[is_ready_to_serve](#a3d97c93b183ca455daf0e3bc2b9c25e1)。

PPP 是否已准备好接收数据包。

<a id="r_a7f103857c7412a6ee9471b6c67baea71"></a>

```c
uint16_t is_enabled: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[is_enabled](#a7f103857c7412a6ee9471b6c67baea71)。

PPP 二层（L2）是否已启用。

<a id="r_acdee16f229cb6aa0672630de1d3ee39b"></a>

```c
uint16_t is_enable_done: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[is_enable_done](#acdee16f229cb6aa0672630de1d3ee39b)。

PPP 启用操作待处理。

<a id="r_a861216f943c5af5d5db58f10ba4263ac"></a>

```c
uint16_t is_ipcp_up: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[is_ipcp_up](#a861216f943c5af5d5db58f10ba4263ac)。

IP 控制协议（IPCP）状态：启用或关闭（up/down）。

<a id="r_a7ef9ac6bb1f86ea417032fe93fc7e8a0"></a>

```c
uint16_t is_ipcp_open: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[is_ipcp_open](#a7ef9ac6bb1f86ea417032fe93fc7e8a0)。

IPCP 的打开状态：已打开或已关闭（open/closed）。

<a id="r_a7b4ee6988626cb69c012a0b58c27bef5"></a>

```c
uint16_t is_ipv6cp_up: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[is_ipv6cp_up](#a7b4ee6988626cb69c012a0b58c27bef5)。

IPv6 控制协议（IPV6CP）状态：启用或关闭（up/down）。

<a id="r_ab139c8d6f1d16c702cb9ca92a7f82178"></a>

```c
uint16_t is_ipv6cp_open: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[is_ipv6cp_open](#ab139c8d6f1d16c702cb9ca92a7f82178)。

IPV6CP 的打开状态：已打开或已关闭（open/closed）。

<a id="r_a52227a05ce8a63f3a4f7535e60fdf979"></a>

```c
uint16_t is_pap_up: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[is_pap_up](#a52227a05ce8a63f3a4f7535e60fdf979)。

密码验证协议（PAP）状态：启用或关闭（up/down）。

<a id="r_a80c2c3248c47fac7fce8d463cfbc0c9f"></a>

```c
uint16_t is_pap_open: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[is_pap_open](#a80c2c3248c47fac7fce8d463cfbc0c9f)。

PAP 的打开状态：已打开或已关闭（open/closed）。

## 43.2\_详细说明（Detailed Documentation）

<a id="a6b327cafe07a0807163589471a9bdae8"></a>

### `flags`

```c
atomic_t ppp_context::flags
```

表示点对点协议（PPP）状态的标志，会被多个线程访问。

<a id="ac555024228a1e1d830c915a098428bc5"></a>

### `fsm`

```c
struct ppp_fsm ppp_context::fsm
```

链路控制协议（LCP）的有限状态机（FSM）。

<a id="a3b0bfb9c3ceece34565b282efa74390e"></a>

### `iface`

```c
struct net_if* ppp_context::iface
```

与此 PPP 连接关联的网络接口。

<a id="acdee16f229cb6aa0672630de1d3ee39b"></a>

### `is_enable_done`

```c
uint16_t ppp_context::is_enable_done
```

PPP 启用操作待处理。

<a id="a7f103857c7412a6ee9471b6c67baea71"></a>

### `is_enabled`

```c
uint16_t ppp_context::is_enabled
```

PPP 二层（L2）是否已启用。

<a id="a7ef9ac6bb1f86ea417032fe93fc7e8a0"></a>

### `is_ipcp_open`

```c
uint16_t ppp_context::is_ipcp_open
```

IPCP 的打开状态：已打开或已关闭（open/closed）。

<a id="a861216f943c5af5d5db58f10ba4263ac"></a>

### `is_ipcp_up`

```c
uint16_t ppp_context::is_ipcp_up
```

IP 控制协议（IPCP）状态：启用或关闭（up/down）。

<a id="ab139c8d6f1d16c702cb9ca92a7f82178"></a>

### `is_ipv6cp_open`

```c
uint16_t ppp_context::is_ipv6cp_open
```

IPV6CP 的打开状态：已打开或已关闭（open/closed）。

<a id="a7b4ee6988626cb69c012a0b58c27bef5"></a>

### `is_ipv6cp_up`

```c
uint16_t ppp_context::is_ipv6cp_up
```

IPv6 控制协议（IPV6CP）状态：启用或关闭（up/down）。

<a id="a80c2c3248c47fac7fce8d463cfbc0c9f"></a>

### `is_pap_open`

```c
uint16_t ppp_context::is_pap_open
```

PAP 的打开状态：已打开或已关闭（open/closed）。

<a id="a52227a05ce8a63f3a4f7535e60fdf979"></a>

### `is_pap_up`

```c
uint16_t ppp_context::is_pap_up
```

密码验证协议（PAP）状态：启用或关闭（up/down）。

<a id="a3d97c93b183ca455daf0e3bc2b9c25e1"></a>

### `is_ready_to_serve`

```c
uint16_t ppp_context::is_ready_to_serve
```

PPP 是否已准备好接收数据包。

<a id="a7705aedba900cf1de66b02ad488b7161"></a>

### `[struct]`

```c
struct { ... } ppp_context::lcp
```

LCP 选项。

<a id="a4d91bf9e6e36415b13be02ccf03d3e40"></a>

### `magic`

```c
uint32_t ppp_context::magic
```

魔数（Magic-Number）值。

<a id="a37f609192ee6b739d7018d5a07ce179f"></a>

### `my_options`

```c
struct lcp_options ppp_context::my_options
```

本端希望请求的选项。

<a id="a9d9d3bc0e8434ad93d1904905a2ad75f"></a>

### `my_options_data`

```c
struct ppp_my_option_data ppp_context::my_options_data[(1+IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_MRU)+IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_PFC)+IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_ACFC))]
```

选项数据。

<a id="a2e04c6e411fe5b07d9d2cda1a61db57f"></a>

### `network_protos_open`

```c
int ppp_context::network_protos_open
```

表示有多少个网络协议已打开（open）。

<a id="a9dd6e156897c53d488344bbbe05d4ae1"></a>

### `network_protos_up`

```c
int ppp_context::network_protos_up
```

表示有多少个网络协议已启用（up）。

<a id="a80fffd30b145b0842e36299ac78d5da8"></a>

### `peer_options`

```c
struct lcp_options ppp_context::peer_options
```

对端希望请求的选项。

<a id="a6afb964ef87696fdadb5cb0c714bd841"></a>

### `phase`

```c
enum ppp_phase ppp_context::phase
```

PPP 链路当前所处阶段（phase）。

<a id="a1c6674bad19047abcc3097bf5ff5f31d"></a>

### `ppp_l2_flags`

```c
enum net_l2_flags ppp_context::ppp_l2_flags
```

表示 PPP 支持哪些特性。

<a id="a5671d7ba465c424004f0460e5ed0d3ba"></a>

### `startup`

```c
struct k_work_delayable ppp_context::startup
```

PPP 启动工作项（startup worker）。

<a id="ae784688e2d78f7427c6672583e326d94"></a>

### `wait_ppp_link_down`

```c
struct k_sem ppp_context::wait_ppp_link_down
```

PPP 链路关闭（down）时发出的信号。

<a id="a1afa42c99b098407f8bba11e50178c84"></a>

### `wait_ppp_link_terminated`

```c
struct k_sem ppp_context::wait_ppp_link_terminated
```

PPP 链路终止时发出的信号。

本数据类型文档由以下文件生成：

- `zephyr/net/ppp.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/net/ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h_source.html)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [ppp_fsm](P044_ppp_fsm_结构体.md)
- [lcp_options](P028_lcp_options_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [ppp_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga284e237a6323f2daffc444a73a4b8b6b)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_ppp_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_ppp_fsm_结构体.md)
