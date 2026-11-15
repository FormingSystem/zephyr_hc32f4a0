---
id: learning.zephyr-docs.api-file-battery-interrupt-reference.page-8
title: zephyr__net__ppp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_net\_\_ppp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

点对点协议（Point-to-Point Protocol，PPP）。

<a id="details"></a>

```c
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/net/net_stats.h>
#include <zephyr/net/net_mgmt.h>
```

查看此文件的源码。

点对点协议（Point-to-Point Protocol，PPP）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_ppp_5Fapi"></a>

```c
struct ppp_api
```

相关声明：[ppp_api](../network_service_model_reference/P042_ppp_api_结构体.md)。

点对点协议第二层（PPP L2）API。

<a id="r_ppp_5Ffsm"></a>

```c
struct ppp_fsm
```

相关声明：[ppp_fsm](../network_service_model_reference/P044_ppp_fsm_结构体.md)。

通用PPP有限状态机（Finite State Machine）。

<a id="r_lcp_5Foptions"></a>

```c
struct lcp_options
```

相关声明：[lcp_options](../network_service_model_reference/P028_lcp_options_结构体.md)。

链路控制协议（Link Control Protocol）的选项。

<a id="r_ipcp_5Foptions"></a>

```c
struct ipcp_options
```

相关声明：[ipcp_options](../network_service_model_reference/P026_ipcp_options_结构体.md)。

IPv4控制协议（Control Protocol）的选项。

<a id="r_ipv6cp_5Foptions"></a>

```c
struct ipv6cp_options
```

相关声明：[ipv6cp_options](../network_service_model_reference/P027_ipv6cp_options_结构体.md)。

IPv6控制协议（Control Protocol）的选项。

<a id="r_ppp_5Fcontext"></a>

```c
struct ppp_context
```

相关声明：[ppp_context](../network_service_model_reference/P043_ppp_context_结构体.md)。

特定网络接口的点对点协议第二层（PPP L2）上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_gaec050624f0693600196068d8f5413e6f"></a>

```c
#define PPP_MRU CONFIG_NET_PPP_MTU_MRU
```

相关声明：[PPP_MRU](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaec050624f0693600196068d8f5413e6f)。

PPP 最大接收单元（Maximum Receive Unit，MRU）。

<a id="r_gacc51e91347721a8255ae891ddc43636b"></a>

```c
#define PPP_MTU PPP_MRU
```

相关声明：[PPP_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gacc51e91347721a8255ae891ddc43636b)、[PPP_MRU](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaec050624f0693600196068d8f5413e6f)。

PPP 最大传输单元（Maximum Transfer Unit，MTU）。

<a id="r_ga2e5d0ae66bf076123cb29effc0a8e894"></a>

```c
#define PPP_MAX_TERMINATE_REASON_LEN 32
```

相关声明：[PPP_MAX_TERMINATE_REASON_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga2e5d0ae66bf076123cb29effc0a8e894)。

终止描述字符串（Terminate Description String）的最大长度。

<a id="r_gaad7380b3a502f4b649348b733124f21a"></a>

```c
#define PPP_INTERFACE_IDENTIFIER_LEN 8
```

相关声明：[PPP_INTERFACE_IDENTIFIER_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaad7380b3a502f4b649348b733124f21a)。

网络接口标识符（Network Interface Identifier）的长度。

<a id="r_gaa584f3427a21343ab692b5ec3a9573ec"></a>

```c
#define LCP_NUM_MY_OPTIONS
```

相关声明：[LCP_NUM_MY_OPTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaa584f3427a21343ab692b5ec3a9573ec)。

<a id="r_ga8f76a2b72607bd98711a3bac0381d0f9"></a>

```c
#define NET_PPP_DEFAULT_ASYNC_MAP (0xffffffffU)
```

相关声明：[NET_PPP_DEFAULT_ASYNC_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga8f76a2b72607bd98711a3bac0381d0f9)。

PPP 异步控制字符映射（Asynchronous Control Character Map，ACCM）的默认值。

<a id="r_ga17c4e8cc92e0e9261d0b2dcc704b2f93"></a>

```c
#define NET_EVENT_PPP_CARRIER_ON (NET_PPP_EVENT | NET_EVENT_PPP_CMD_CARRIER_ON)
```

相关声明：[NET_EVENT_PPP_CARRIER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga17c4e8cc92e0e9261d0b2dcc704b2f93)。

PPP 载波接通（Carrier On）时发出的事件。

<a id="r_ga2b3c11bbdc7b36d4381811b210340e45"></a>

```c
#define NET_EVENT_PPP_CARRIER_OFF (NET_PPP_EVENT | NET_EVENT_PPP_CMD_CARRIER_OFF)
```

相关声明：[NET_EVENT_PPP_CARRIER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga2b3c11bbdc7b36d4381811b210340e45)。

PPP 载波断开（Carrier Off）时发出的事件。

<a id="r_ga4853534532ac4875321785a70c5a1b19"></a>

```c
#define NET_EVENT_PPP_PHASE_RUNNING (NET_PPP_EVENT | NET_EVENT_PPP_CMD_PHASE_RUNNING)
```

相关声明：[NET_EVENT_PPP_PHASE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga4853534532ac4875321785a70c5a1b19)。

PPP 进入运行阶段（Running Phase）时发出的事件。

<a id="r_ga7aa5d07daa3f8bb45cf1bd0c30c6fc7a"></a>

```c
#define NET_EVENT_PPP_PHASE_DEAD (NET_PPP_EVENT | NET_EVENT_PPP_CMD_PHASE_DEAD)
```

相关声明：[NET_EVENT_PPP_PHASE_DEAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga7aa5d07daa3f8bb45cf1bd0c30c6fc7a)。

PPP 进入终止阶段（Dead Phase）时发出的事件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.3\_类型定义（Typedefs）

<a id="r_ga15afa05abc0446201c912c75644306bf"></a>

```c
typedef void(* net_ppp_lcp_echo_reply_cb_t) (void *user_data, size_t user_data_len)
```

相关声明：[net_ppp_lcp_echo_reply_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga15afa05abc0446201c912c75644306bf)。

需要接收回送应答（Echo-Reply）时可调用的回调函数（Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.4\_枚举（Enumerations）

<a id="r_ga8ad7cc0d142a6e7ea82c45bec2cc3670"></a>

```c
enum ppp_protocol_type { PPP_IP = 0x0021 , PPP_IPV6 = 0x0057 , PPP_IPCP = 0x8021 , PPP_ECP = 0x8053 , PPP_IPV6CP = 0x8057 , PPP_CCP = 0x80FD , PPP_LCP = 0xc021 , PPP_PAP = 0xc023 , PPP_CHAP = 0xc223 , PPP_EAP = 0xc227 }
```

相关声明：[ppp_protocol_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga8ad7cc0d142a6e7ea82c45bec2cc3670)、[PPP_IP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6)、[PPP_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe)、[PPP_IPCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21)、[PPP_ECP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44)、[PPP_IPV6CP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0)、[PPP_CCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b)、[PPP_LCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9)、[PPP_PAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206)、[PPP_CHAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25)、[PPP_EAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2)。

PPP 协议类型（Protocol Types）。

<a id="r_ga284e237a6323f2daffc444a73a4b8b6b"></a>

```c
enum ppp_phase { PPP_DEAD , PPP_ESTABLISH , PPP_AUTH , PPP_NETWORK , PPP_RUNNING , PPP_TERMINATE }
```

相关声明：[ppp_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga284e237a6323f2daffc444a73a4b8b6b)、[PPP_DEAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d)、[PPP_ESTABLISH](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4)、[PPP_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a)、[PPP_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af)、[PPP_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7)、[PPP_TERMINATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7)。

PPP 阶段（Phases）。

<a id="r_gac8f3d915c930d61831bcb13d6201b15c"></a>

```c
enum lcp_option_type { LCP_OPTION_RESERVED = 0 , LCP_OPTION_MRU = 1 , LCP_OPTION_ASYNC_CTRL_CHAR_MAP = 2 , LCP_OPTION_AUTH_PROTO = 3 , LCP_OPTION_QUALITY_PROTO = 4 , LCP_OPTION_MAGIC_NUMBER = 5 , LCP_OPTION_PROTO_COMPRESS = 7 , LCP_OPTION_ADDR_CTRL_COMPRESS = 8 }
```

相关声明：[lcp_option_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gac8f3d915c930d61831bcb13d6201b15c)、[LCP_OPTION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3)、[LCP_OPTION_MRU](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe)、[LCP_OPTION_ASYNC_CTRL_CHAR_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef)、[LCP_OPTION_AUTH_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743)、[LCP_OPTION_QUALITY_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9)、[LCP_OPTION_MAGIC_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8)、[LCP_OPTION_PROTO_COMPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4)、[LCP_OPTION_ADDR_CTRL_COMPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524)。

RFC 1661 第 6 节中的链路控制协议（Link Control Protocol，LCP）选项类型。

<a id="r_ga1064e3d8c6aa3d3161e399d6937162b6"></a>

```c
enum ipcp_option_type { IPCP_OPTION_RESERVED = 0 , IPCP_OPTION_IP_ADDRESSES = 1 , IPCP_OPTION_IP_COMP_PROTO = 2 , IPCP_OPTION_IP_ADDRESS = 3 , IPCP_OPTION_DNS1 = 129 , IPCP_OPTION_NBNS1 = 130 , IPCP_OPTION_DNS2 = 131 , IPCP_OPTION_NBNS2 = 132 }
```

相关声明：[ipcp_option_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga1064e3d8c6aa3d3161e399d6937162b6)、[IPCP_OPTION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b)、[IPCP_OPTION_IP_ADDRESSES](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b)、[IPCP_OPTION_IP_COMP_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6)、[IPCP_OPTION_IP_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9)、[IPCP_OPTION_DNS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931)、[IPCP_OPTION_NBNS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552)、[IPCP_OPTION_DNS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964)、[IPCP_OPTION_NBNS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad)。

RFC 1332 中的 IP 控制协议（IP Control Protocol，IPCP）选项类型。

<a id="r_gaf30172a9fead40463d129a5afeaf1ac3"></a>

```c
enum ipv6cp_option_type { IPV6CP_OPTION_RESERVED = 0 , IPV6CP_OPTION_INTERFACE_IDENTIFIER = 1 }
```

相关声明：[ipv6cp_option_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaf30172a9fead40463d129a5afeaf1ac3)、[IPV6CP_OPTION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858)、[IPV6CP_OPTION_INTERFACE_IDENTIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7)。

RFC 5072 中的 IPv6 控制协议（IPv6 Control Protocol，IPV6CP）选项类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.5\_函数（Functions）

<a id="r_gaabf883cfefc9910b9b9d8931e68b320c"></a>

```c
void net_ppp_init (struct net_if *iface)
```

相关声明：[net_ppp_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaabf883cfefc9910b9b9d8931e68b320c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

为指定接口初始化 PPP 二层协议栈（L2 Stack）。

<a id="r_ga716727874cecc8ee358da6c76adedc0a"></a>

```c
uint32_t ppp_peer_async_control_character_map (struct net_if *iface)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[ppp_peer_async_control_character_map](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga716727874cecc8ee358da6c76adedc0a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取 PPP 对端的异步控制字符映射（Asynchronous Control Character Map，ACCM）。

<a id="r_ga1436cf5cfcb6752e41c9e06a0ee30030"></a>

```c
static void ppp_mgmt_raise_carrier_on_event (struct net_if *iface)
```

相关声明：[ppp_mgmt_raise_carrier_on_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga1436cf5cfcb6752e41c9e06a0ee30030)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

PPP 连接时产生 CARRIER_ON 事件。

<a id="r_gad96b2c77cf6a066d55d78c5d63cb9bd0"></a>

```c
static void ppp_mgmt_raise_carrier_off_event (struct net_if *iface)
```

相关声明：[ppp_mgmt_raise_carrier_off_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gad96b2c77cf6a066d55d78c5d63cb9bd0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

PPP 断开连接时产生 CARRIER_OFF 事件。

<a id="r_ga74e94e9fcae30bc386c5e3d951ed5882"></a>

```c
static void ppp_mgmt_raise_phase_running_event (struct net_if *iface)
```

相关声明：[ppp_mgmt_raise_phase_running_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga74e94e9fcae30bc386c5e3d951ed5882)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

PPP 到达 RUNNING 阶段时产生 PHASE_RUNNING 事件。

<a id="r_gad7f41d9012098ed1a04f897e252cc32d"></a>

```c
static void ppp_mgmt_raise_phase_dead_event (struct net_if *iface)
```

相关声明：[ppp_mgmt_raise_phase_dead_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gad7f41d9012098ed1a04f897e252cc32d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

PPP 到达 DEAD 阶段时产生 PHASE_DEAD 事件。

<a id="r_ga9893a7c93b3d23b96b4d83aa1204c500"></a>

```c
static int net_ppp_ping (int idx, int32_t timeout)
```

相关声明：[net_ppp_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga9893a7c93b3d23b96b4d83aa1204c500)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

向对端发送 PPP 回送请求（Echo-Request）。

<a id="r_ga4f6104cff735f9829762b6552a7346bf"></a>

```c
static struct ppp_context * net_ppp_context_get (int idx)
```

相关声明：[ppp_context](../network_service_model_reference/P043_ppp_context_结构体.md)、[net_ppp_context_get](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga4f6104cff735f9829762b6552a7346bf)。

获取 PPP 上下文（Context）信息。


## 8.6\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/net_pkt.h](../api_source_packet_gnss_reference/P006_net_pkt.h_源码浏览.md)
- [zephyr/net/net_stats.h](../api_source_interrupt_modem_reference/P007_net_stats.h_源码浏览.md)
- [zephyr/net/net_mgmt.h](../api_source_timing_sensor_reference/P009_net_mgmt.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P045_ppp.h_源码浏览.md)
- [ppp_api](../network_service_model_reference/P042_ppp_api_结构体.md)
- [ppp_fsm](../network_service_model_reference/P044_ppp_fsm_结构体.md)
- [lcp_options](../network_service_model_reference/P028_lcp_options_结构体.md)
- [ipcp_options](../network_service_model_reference/P026_ipcp_options_结构体.md)
- [ipv6cp_options](../network_service_model_reference/P027_ipv6cp_options_结构体.md)
- [ppp_context](../network_service_model_reference/P043_ppp_context_结构体.md)
- [PPP_MRU](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaec050624f0693600196068d8f5413e6f)
- [PPP_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gacc51e91347721a8255ae891ddc43636b)
- [PPP_MAX_TERMINATE_REASON_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga2e5d0ae66bf076123cb29effc0a8e894)
- [PPP_INTERFACE_IDENTIFIER_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaad7380b3a502f4b649348b733124f21a)
- [LCP_NUM_MY_OPTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaa584f3427a21343ab692b5ec3a9573ec)
- [NET_PPP_DEFAULT_ASYNC_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga8f76a2b72607bd98711a3bac0381d0f9)
- [NET_EVENT_PPP_CARRIER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga17c4e8cc92e0e9261d0b2dcc704b2f93)
- [NET_EVENT_PPP_CARRIER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga2b3c11bbdc7b36d4381811b210340e45)
- [NET_EVENT_PPP_PHASE_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga4853534532ac4875321785a70c5a1b19)
- [NET_EVENT_PPP_PHASE_DEAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga7aa5d07daa3f8bb45cf1bd0c30c6fc7a)
- [net_ppp_lcp_echo_reply_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga15afa05abc0446201c912c75644306bf)
- [ppp_protocol_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga8ad7cc0d142a6e7ea82c45bec2cc3670)
- [PPP_IP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6)
- [PPP_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe)
- [PPP_IPCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21)
- [PPP_ECP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44)
- [PPP_IPV6CP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0)
- [PPP_CCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b)
- [PPP_LCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9)
- [PPP_PAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206)
- [PPP_CHAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25)
- [PPP_EAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2)
- [ppp_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga284e237a6323f2daffc444a73a4b8b6b)
- [PPP_DEAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d)
- [PPP_ESTABLISH](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4)
- [PPP_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a)
- [PPP_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af)
- [PPP_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7)
- [PPP_TERMINATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7)
- [lcp_option_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gac8f3d915c930d61831bcb13d6201b15c)
- [LCP_OPTION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3)
- [LCP_OPTION_MRU](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe)
- [LCP_OPTION_ASYNC_CTRL_CHAR_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef)
- [LCP_OPTION_AUTH_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743)
- [LCP_OPTION_QUALITY_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9)
- [LCP_OPTION_MAGIC_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8)
- [LCP_OPTION_PROTO_COMPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4)
- [LCP_OPTION_ADDR_CTRL_COMPRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524)
- [RFC 1661, section-6](https://datatracker.ietf.org/doc/html/rfc1661#section-6)
- [ipcp_option_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga1064e3d8c6aa3d3161e399d6937162b6)
- [IPCP_OPTION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b)
- [IPCP_OPTION_IP_ADDRESSES](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b)
- [IPCP_OPTION_IP_COMP_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6)
- [IPCP_OPTION_IP_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9)
- [IPCP_OPTION_DNS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931)
- [IPCP_OPTION_NBNS1](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552)
- [IPCP_OPTION_DNS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964)
- [IPCP_OPTION_NBNS2](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad)
- [RFC 1332](https://datatracker.ietf.org/doc/html/rfc1332)
- [ipv6cp_option_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaf30172a9fead40463d129a5afeaf1ac3)
- [IPV6CP_OPTION_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858)
- [IPV6CP_OPTION_INTERFACE_IDENTIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7)
- [RFC 5072](https://datatracker.ietf.org/doc/html/rfc5072)
- [net_ppp_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gaabf883cfefc9910b9b9d8931e68b320c)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ppp_peer_async_control_character_map](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga716727874cecc8ee358da6c76adedc0a)
- [ppp_mgmt_raise_carrier_on_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga1436cf5cfcb6752e41c9e06a0ee30030)
- [ppp_mgmt_raise_carrier_off_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gad96b2c77cf6a066d55d78c5d63cb9bd0)
- [ppp_mgmt_raise_phase_running_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga74e94e9fcae30bc386c5e3d951ed5882)
- [ppp_mgmt_raise_phase_dead_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#gad7f41d9012098ed1a04f897e252cc32d)
- [net_ppp_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga9893a7c93b3d23b96b4d83aa1204c500)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [net_ppp_context_get](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga4f6104cff735f9829762b6552a7346bf)

<a id="header-details"></a>

---

[上一章](P007_zephyr__drivers__interrupt_controller__intc_nxp_gint.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__usb-c__nxp_nx20p3483.h_文件参考.md)
