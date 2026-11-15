---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-16
title: 点对点协议二层_驱动支持函数（PPP L2_driver Support Functions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_点对点协议二层\_驱动支持函数（PPP L2\_driver Support Functions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

点对点协议（Point-to-point，PPP）二层/驱动支持函数。

<a id="details"></a>

点对点协议（Point-to-Point Protocol，PPP）的二层／驱动支持函数（L2/Driver Support Functions）。自 2.0 起提供（Since 2.0），版本（Version）0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.1\_数据结构（Data Structures）

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

## 16.2\_宏定义（Macros）

<a id="r_gaec050624f0693600196068d8f5413e6f"></a>

```c
#define PPP_MRU CONFIG_NET_PPP_MTU_MRU
```

相关声明：[PPP_MRU](#gaec050624f0693600196068d8f5413e6f)。

PPP 最大接收单元（Maximum Receive Unit，MRU）。

<a id="r_gacc51e91347721a8255ae891ddc43636b"></a>

```c
#define PPP_MTU PPP_MRU
```

相关声明：[PPP_MTU](#gacc51e91347721a8255ae891ddc43636b)、[PPP_MRU](#gaec050624f0693600196068d8f5413e6f)。

PPP 最大传输单元（Maximum Transfer Unit，MTU）。

<a id="r_ga2e5d0ae66bf076123cb29effc0a8e894"></a>

```c
#define PPP_MAX_TERMINATE_REASON_LEN 32
```

相关声明：[PPP_MAX_TERMINATE_REASON_LEN](#ga2e5d0ae66bf076123cb29effc0a8e894)。

终止描述字符串（Terminate Description String）的最大长度。

<a id="r_gaad7380b3a502f4b649348b733124f21a"></a>

```c
#define PPP_INTERFACE_IDENTIFIER_LEN 8
```

相关声明：[PPP_INTERFACE_IDENTIFIER_LEN](#gaad7380b3a502f4b649348b733124f21a)。

网络接口标识符（Network Interface Identifier）的长度。

<a id="r_gaa584f3427a21343ab692b5ec3a9573ec"></a>

```c
#define LCP_NUM_MY_OPTIONS
```

相关声明：[LCP_NUM_MY_OPTIONS](#gaa584f3427a21343ab692b5ec3a9573ec)。

<a id="r_ga8f76a2b72607bd98711a3bac0381d0f9"></a>

```c
#define NET_PPP_DEFAULT_ASYNC_MAP (0xffffffffU)
```

相关声明：[NET_PPP_DEFAULT_ASYNC_MAP](#ga8f76a2b72607bd98711a3bac0381d0f9)。

PPP 异步控制字符映射（Asynchronous Control Character Map，ACCM）的默认值。

<a id="r_ga17c4e8cc92e0e9261d0b2dcc704b2f93"></a>

```c
#define NET_EVENT_PPP_CARRIER_ON (NET_PPP_EVENT | NET_EVENT_PPP_CMD_CARRIER_ON)
```

相关声明：[NET_EVENT_PPP_CARRIER_ON](#ga17c4e8cc92e0e9261d0b2dcc704b2f93)。

PPP 载波接通（Carrier On）时发出的事件。

<a id="r_ga2b3c11bbdc7b36d4381811b210340e45"></a>

```c
#define NET_EVENT_PPP_CARRIER_OFF (NET_PPP_EVENT | NET_EVENT_PPP_CMD_CARRIER_OFF)
```

相关声明：[NET_EVENT_PPP_CARRIER_OFF](#ga2b3c11bbdc7b36d4381811b210340e45)。

PPP 载波断开（Carrier Off）时发出的事件。

<a id="r_ga4853534532ac4875321785a70c5a1b19"></a>

```c
#define NET_EVENT_PPP_PHASE_RUNNING (NET_PPP_EVENT | NET_EVENT_PPP_CMD_PHASE_RUNNING)
```

相关声明：[NET_EVENT_PPP_PHASE_RUNNING](#ga4853534532ac4875321785a70c5a1b19)。

PPP 进入运行阶段（Running Phase）时发出的事件。

<a id="r_ga7aa5d07daa3f8bb45cf1bd0c30c6fc7a"></a>

```c
#define NET_EVENT_PPP_PHASE_DEAD (NET_PPP_EVENT | NET_EVENT_PPP_CMD_PHASE_DEAD)
```

相关声明：[NET_EVENT_PPP_PHASE_DEAD](#ga7aa5d07daa3f8bb45cf1bd0c30c6fc7a)。

PPP 进入终止阶段（Dead Phase）时发出的事件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 16.3\_类型定义（Typedefs）

<a id="r_ga15afa05abc0446201c912c75644306bf"></a>

```c
typedef void(* net_ppp_lcp_echo_reply_cb_t) (void *user_data, size_t user_data_len)
```

相关声明：[net_ppp_lcp_echo_reply_cb_t](#ga15afa05abc0446201c912c75644306bf)。

需要接收回送应答（Echo-Reply）时可调用的回调函数（Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.4\_枚举（Enumerations）

<a id="r_ga8ad7cc0d142a6e7ea82c45bec2cc3670"></a>

```c
enum ppp_protocol_type { PPP_IP = 0x0021 , PPP_IPV6 = 0x0057 , PPP_IPCP = 0x8021 , PPP_ECP = 0x8053 , PPP_IPV6CP = 0x8057 , PPP_CCP = 0x80FD , PPP_LCP = 0xc021 , PPP_PAP = 0xc023 , PPP_CHAP = 0xc223 , PPP_EAP = 0xc227 }
```

相关声明：[ppp_protocol_type](#ga8ad7cc0d142a6e7ea82c45bec2cc3670)、[PPP_IP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6)、[PPP_IPV6](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe)、[PPP_IPCP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21)、[PPP_ECP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44)、[PPP_IPV6CP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0)、[PPP_CCP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b)、[PPP_LCP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9)、[PPP_PAP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206)、[PPP_CHAP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25)、[PPP_EAP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2)。

PPP 协议类型（Protocol Types）。

<a id="r_ga284e237a6323f2daffc444a73a4b8b6b"></a>

```c
enum ppp_phase { PPP_DEAD , PPP_ESTABLISH , PPP_AUTH , PPP_NETWORK , PPP_RUNNING , PPP_TERMINATE }
```

相关声明：[ppp_phase](#ga284e237a6323f2daffc444a73a4b8b6b)、[PPP_DEAD](#gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d)、[PPP_ESTABLISH](#gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4)、[PPP_AUTH](#gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a)、[PPP_NETWORK](#gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af)、[PPP_RUNNING](#gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7)、[PPP_TERMINATE](#gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7)。

PPP 阶段（Phases）。

<a id="r_gac8f3d915c930d61831bcb13d6201b15c"></a>

```c
enum lcp_option_type { LCP_OPTION_RESERVED = 0 , LCP_OPTION_MRU = 1 , LCP_OPTION_ASYNC_CTRL_CHAR_MAP = 2 , LCP_OPTION_AUTH_PROTO = 3 , LCP_OPTION_QUALITY_PROTO = 4 , LCP_OPTION_MAGIC_NUMBER = 5 , LCP_OPTION_PROTO_COMPRESS = 7 , LCP_OPTION_ADDR_CTRL_COMPRESS = 8 }
```

相关声明：[lcp_option_type](#gac8f3d915c930d61831bcb13d6201b15c)、[LCP_OPTION_RESERVED](#ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3)、[LCP_OPTION_MRU](#ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe)、[LCP_OPTION_ASYNC_CTRL_CHAR_MAP](#ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef)、[LCP_OPTION_AUTH_PROTO](#ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743)、[LCP_OPTION_QUALITY_PROTO](#ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9)、[LCP_OPTION_MAGIC_NUMBER](#ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8)、[LCP_OPTION_PROTO_COMPRESS](#ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4)、[LCP_OPTION_ADDR_CTRL_COMPRESS](#ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524)。

RFC 1661 第 6 节中的链路控制协议（Link Control Protocol，LCP）选项类型。

<a id="r_ga1064e3d8c6aa3d3161e399d6937162b6"></a>

```c
enum ipcp_option_type { IPCP_OPTION_RESERVED = 0 , IPCP_OPTION_IP_ADDRESSES = 1 , IPCP_OPTION_IP_COMP_PROTO = 2 , IPCP_OPTION_IP_ADDRESS = 3 , IPCP_OPTION_DNS1 = 129 , IPCP_OPTION_NBNS1 = 130 , IPCP_OPTION_DNS2 = 131 , IPCP_OPTION_NBNS2 = 132 }
```

相关声明：[ipcp_option_type](#ga1064e3d8c6aa3d3161e399d6937162b6)、[IPCP_OPTION_RESERVED](#gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b)、[IPCP_OPTION_IP_ADDRESSES](#gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b)、[IPCP_OPTION_IP_COMP_PROTO](#gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6)、[IPCP_OPTION_IP_ADDRESS](#gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9)、[IPCP_OPTION_DNS1](#gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931)、[IPCP_OPTION_NBNS1](#gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552)、[IPCP_OPTION_DNS2](#gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964)、[IPCP_OPTION_NBNS2](#gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad)。

RFC 1332 中的 IP 控制协议（IP Control Protocol，IPCP）选项类型。

<a id="r_gaf30172a9fead40463d129a5afeaf1ac3"></a>

```c
enum ipv6cp_option_type { IPV6CP_OPTION_RESERVED = 0 , IPV6CP_OPTION_INTERFACE_IDENTIFIER = 1 }
```

相关声明：[ipv6cp_option_type](#gaf30172a9fead40463d129a5afeaf1ac3)、[IPV6CP_OPTION_RESERVED](#ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858)、[IPV6CP_OPTION_INTERFACE_IDENTIFIER](#ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7)。

RFC 5072 中的 IPv6 控制协议（IPv6 Control Protocol，IPV6CP）选项类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.5\_函数（Functions）

<a id="r_gaabf883cfefc9910b9b9d8931e68b320c"></a>

```c
void net_ppp_init (struct net_if *iface)
```

相关声明：[net_ppp_init](#gaabf883cfefc9910b9b9d8931e68b320c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

为指定接口初始化 PPP 二层协议栈（L2 Stack）。

<a id="r_ga716727874cecc8ee358da6c76adedc0a"></a>

```c
uint32_t ppp_peer_async_control_character_map (struct net_if *iface)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[ppp_peer_async_control_character_map](#ga716727874cecc8ee358da6c76adedc0a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取 PPP 对端的异步控制字符映射（Asynchronous Control Character Map，ACCM）。

<a id="r_ga1436cf5cfcb6752e41c9e06a0ee30030"></a>

```c
static void ppp_mgmt_raise_carrier_on_event (struct net_if *iface)
```

相关声明：[ppp_mgmt_raise_carrier_on_event](#ga1436cf5cfcb6752e41c9e06a0ee30030)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

PPP 连接时产生 CARRIER_ON 事件。

<a id="r_gad96b2c77cf6a066d55d78c5d63cb9bd0"></a>

```c
static void ppp_mgmt_raise_carrier_off_event (struct net_if *iface)
```

相关声明：[ppp_mgmt_raise_carrier_off_event](#gad96b2c77cf6a066d55d78c5d63cb9bd0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

PPP 断开连接时产生 CARRIER_OFF 事件。

<a id="r_ga74e94e9fcae30bc386c5e3d951ed5882"></a>

```c
static void ppp_mgmt_raise_phase_running_event (struct net_if *iface)
```

相关声明：[ppp_mgmt_raise_phase_running_event](#ga74e94e9fcae30bc386c5e3d951ed5882)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

PPP 到达 RUNNING 阶段时产生 PHASE_RUNNING 事件。

<a id="r_gad7f41d9012098ed1a04f897e252cc32d"></a>

```c
static void ppp_mgmt_raise_phase_dead_event (struct net_if *iface)
```

相关声明：[ppp_mgmt_raise_phase_dead_event](#gad7f41d9012098ed1a04f897e252cc32d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

PPP 到达 DEAD 阶段时产生 PHASE_DEAD 事件。

<a id="r_ga9893a7c93b3d23b96b4d83aa1204c500"></a>

```c
static int net_ppp_ping (int idx, int32_t timeout)
```

相关声明：[net_ppp_ping](#ga9893a7c93b3d23b96b4d83aa1204c500)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

向对端发送 PPP 回送请求（Echo-Request）。

<a id="r_ga4f6104cff735f9829762b6552a7346bf"></a>

```c
static struct ppp_context * net_ppp_context_get (int idx)
```

相关声明：[ppp_context](../network_service_model_reference/P043_ppp_context_结构体.md)、[net_ppp_context_get](#ga4f6104cff735f9829762b6552a7346bf)。

获取 PPP 上下文（Context）信息。

## 16.6\_详细说明（Detailed Documentation）

<a id="gaa584f3427a21343ab692b5ec3a9573ec"></a>

### `LCP_NUM_MY_OPTIONS`

```c
#define LCP_NUM_MY_OPTIONS
```

```c
#include <zephyr/net/ppp.h>
```

展开值（Value）：

```c
(1                                              \
+ IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_MRU)                      \
+ IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_PFC)                      \
+ IS_ENABLED(CONFIG_NET_L2_PPP_OPTION_ACFC))
```

<a id="ga2b3c11bbdc7b36d4381811b210340e45"></a>

### `NET_EVENT_PPP_CARRIER_OFF`

```c
#define NET_EVENT_PPP_CARRIER_OFF (NET_PPP_EVENT | NET_EVENT_PPP_CMD_CARRIER_OFF)
```

```c
#include <zephyr/net/ppp.h>
```

PPP 载波断开（Carrier Off）时发出的事件。

<a id="ga17c4e8cc92e0e9261d0b2dcc704b2f93"></a>

### `NET_EVENT_PPP_CARRIER_ON`

```c
#define NET_EVENT_PPP_CARRIER_ON (NET_PPP_EVENT | NET_EVENT_PPP_CMD_CARRIER_ON)
```

```c
#include <zephyr/net/ppp.h>
```

PPP 载波接通（Carrier On）时发出的事件。

<a id="ga7aa5d07daa3f8bb45cf1bd0c30c6fc7a"></a>

### `NET_EVENT_PPP_PHASE_DEAD`

```c
#define NET_EVENT_PPP_PHASE_DEAD (NET_PPP_EVENT | NET_EVENT_PPP_CMD_PHASE_DEAD)
```

```c
#include <zephyr/net/ppp.h>
```

PPP 进入终止阶段（Dead Phase）时发出的事件。

<a id="ga4853534532ac4875321785a70c5a1b19"></a>

### `NET_EVENT_PPP_PHASE_RUNNING`

```c
#define NET_EVENT_PPP_PHASE_RUNNING (NET_PPP_EVENT | NET_EVENT_PPP_CMD_PHASE_RUNNING)
```

```c
#include <zephyr/net/ppp.h>
```

PPP 进入运行阶段（Running Phase）时发出的事件。

<a id="ga8f76a2b72607bd98711a3bac0381d0f9"></a>

### `NET_PPP_DEFAULT_ASYNC_MAP`

```c
#define NET_PPP_DEFAULT_ASYNC_MAP (0xffffffffU)
```

```c
#include <zephyr/net/ppp.h>
```

PPP 异步控制字符映射（Asynchronous Control Character Map，ACCM）的默认值。

<a id="gaad7380b3a502f4b649348b733124f21a"></a>

### `PPP_INTERFACE_IDENTIFIER_LEN`

```c
#define PPP_INTERFACE_IDENTIFIER_LEN 8
```

```c
#include <zephyr/net/ppp.h>
```

网络接口标识符（Network Interface Identifier）的长度。

<a id="ga2e5d0ae66bf076123cb29effc0a8e894"></a>

### `PPP_MAX_TERMINATE_REASON_LEN`

```c
#define PPP_MAX_TERMINATE_REASON_LEN 32
```

```c
#include <zephyr/net/ppp.h>
```

终止描述字符串（Terminate Description String）的最大长度。

<a id="gaec050624f0693600196068d8f5413e6f"></a>

### `PPP_MRU`

```c
#define PPP_MRU CONFIG_NET_PPP_MTU_MRU
```

```c
#include <zephyr/net/ppp.h>
```

PPP 最大接收单元（Maximum Receive Unit，MRU）。

<a id="gacc51e91347721a8255ae891ddc43636b"></a>

### `PPP_MTU`

```c
#define PPP_MTU PPP_MRU
```

```c
#include <zephyr/net/ppp.h>
```

PPP 最大传输单元（Maximum Transfer Unit，MTU）。

<a id="ga15afa05abc0446201c912c75644306bf"></a>

### `net_ppp_lcp_echo_reply_cb_t`

```c
typedef void(* net_ppp_lcp_echo_reply_cb_t) (void *user_data, size_t user_data_len)
```

```c
#include <zephyr/net/ppp.h>
```

需要接收回送应答（Echo-Reply）时可调用的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `user_data` | 用户可设置的数据（User Data），传给回调函数。 |
| `user_data_len` | 用户数据长度（User Data Length）。 |

<a id="ga1064e3d8c6aa3d3161e399d6937162b6"></a>

### `ipcp_option_type`

```c
enum ipcp_option_type
```

```c
#include <zephyr/net/ppp.h>
```

RFC 1332 中的 IP 控制协议（IP Control Protocol，IPCP）选项类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IPCP_OPTION_RESERVED` | 保留的 IPCP 选项值（Reserved Option Value），请勿使用。 |
| `IPCP_OPTION_IP_ADDRESSES` | IP 地址（IP Addresses）。 |
| `IPCP_OPTION_IP_COMP_PROTO` | IP 压缩协议（IP Compression Protocol）。 |
| `IPCP_OPTION_IP_ADDRESS` | IP 地址（IP Address）。 |
| `IPCP_OPTION_DNS1` | 主 DNS 服务器地址（Primary DNS Server Address）。 |
| `IPCP_OPTION_NBNS1` | 主 NBNS 服务器地址（Primary NBNS Server Address）。 |
| `IPCP_OPTION_DNS2` | 次 DNS 服务器地址（Secondary DNS Server Address）。 |
| `IPCP_OPTION_NBNS2` | 次 NBNS 服务器地址（Secondary NBNS Server Address）。 |

<a id="gaf30172a9fead40463d129a5afeaf1ac3"></a>

### `ipv6cp_option_type`

```c
enum ipv6cp_option_type
```

```c
#include <zephyr/net/ppp.h>
```

RFC 5072 中的 IPv6 控制协议（IPv6 Control Protocol，IPV6CP）选项类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IPV6CP_OPTION_RESERVED` | 保留的 IPV6CP 选项值（Reserved Option Value），请勿使用。 |
| `IPV6CP_OPTION_INTERFACE_IDENTIFIER` | 接口标识符（Interface identifier）。 |

<a id="gac8f3d915c930d61831bcb13d6201b15c"></a>

### `lcp_option_type`

```c
enum lcp_option_type
```

```c
#include <zephyr/net/ppp.h>
```

RFC 1661 第 6 节中的链路控制协议（Link Control Protocol，LCP）选项类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LCP_OPTION_RESERVED` | 保留选项值（Reserved Option Value），请勿使用。 |
| `LCP_OPTION_MRU` | 最大接收单元（Maximum-Receive-Unit）。 |
| `LCP_OPTION_ASYNC_CTRL_CHAR_MAP` | 异步控制字符映射（Async-Control-Character-Map）。 |
| `LCP_OPTION_AUTH_PROTO` | 认证协议（Authentication-Protocol）。 |
| `LCP_OPTION_QUALITY_PROTO` | 质量协议（Quality-Protocol）。 |
| `LCP_OPTION_MAGIC_NUMBER` | 魔数（Magic-Number）。 |
| `LCP_OPTION_PROTO_COMPRESS` | 协议字段压缩（Protocol-Field-Compression）。 |
| `LCP_OPTION_ADDR_CTRL_COMPRESS` | 地址与控制字段压缩（Address-and-Control-Field-Compression）。 |

<a id="ga284e237a6323f2daffc444a73a4b8b6b"></a>

### `ppp_phase`

```c
enum ppp_phase
```

```c
#include <zephyr/net/ppp.h>
```

PPP 阶段（Phases）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PPP_DEAD` | 物理层（Physical Layer）未就绪。 |
| `PPP_ESTABLISH` | 正在建立链路（Link）。 |
| `PPP_AUTH` | 与对端进行链路认证（Link Authentication）。 |
| `PPP_NETWORK` | 建立网络连接（Network Connection Establishment）。 |
| `PPP_RUNNING` | 网络正在运行（Network Running）。 |
| `PPP_TERMINATE` | 终止链路（Link Termination）。 |

<a id="ga8ad7cc0d142a6e7ea82c45bec2cc3670"></a>

### `ppp_protocol_type`

```c
enum ppp_protocol_type
```

```c
#include <zephyr/net/ppp.h>
```

PPP 协议类型（Protocol Types）。

详情参见 https://www.iana.org/assignments/ppp-numbers/ppp-numbers.xhtml 。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PPP_IP` | RFC 1332 规范。 |
| `PPP_IPV6` | RFC 5072 规范。 |
| `PPP_IPCP` | RFC 1332 规范。 |
| `PPP_ECP` | RFC 1968 规范。 |
| `PPP_IPV6CP` | RFC 5072 规范。 |
| `PPP_CCP` | RFC 1962 规范。 |
| `PPP_LCP` | RFC 1661 规范。 |
| `PPP_PAP` | RFC 1334 规范。 |
| `PPP_CHAP` | RFC 1334 规范。 |
| `PPP_EAP` | RFC 2284 规范。 |

<a id="ga4f6104cff735f9829762b6552a7346bf"></a>

### `net_ppp_context_get()`

```c
struct ppp_context * net_ppp_context_get ( int idx)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ppp.h>
```

获取 PPP 上下文（Context）信息。

仅供网络命令行（Net-shell）打印 PPP 信息使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | PPP 网络接口索引（Network Interface Index）。 |

返回（Returns）：PPP 上下文（Context）；idx 无效时返回 NULL。

<a id="gaabf883cfefc9910b9b9d8931e68b320c"></a>

### `net_ppp_init()`

```c
void net_ppp_init ( struct net_if * iface)
```

```c
#include <zephyr/net/ppp.h>
```

为指定接口初始化 PPP 二层协议栈（L2 Stack）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的有效指针。 |

<a id="ga9893a7c93b3d23b96b4d83aa1204c500"></a>

### `net_ppp_ping()`

```c
int net_ppp_ping ( int idx, int32_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ppp.h>
```

向对端发送 PPP 回送请求（Echo-Request）。

预期收到回送应答（Echo-Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | PPP 网络接口索引（Network Interface Index）。 |
| `timeout` | 等待回送应答（Echo-Reply）的时间，单位为毫秒。 |

返回（Returns）：收到 Echo-Reply 时为 0；超时或网络索引不是有效 PPP 网络索引时小于 0。

<a id="gad96b2c77cf6a066d55d78c5d63cb9bd0"></a>

### `ppp_mgmt_raise_carrier_off_event()`

```c
void ppp_mgmt_raise_carrier_off_event ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ppp.h>
```

PPP 断开连接时产生 CARRIER_OFF 事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | PPP 网络接口（Network Interface）。 |

<a id="ga1436cf5cfcb6752e41c9e06a0ee30030"></a>

### `ppp_mgmt_raise_carrier_on_event()`

```c
void ppp_mgmt_raise_carrier_on_event ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ppp.h>
```

PPP 连接时产生 CARRIER_ON 事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | PPP 网络接口（Network Interface）。 |

<a id="gad7f41d9012098ed1a04f897e252cc32d"></a>

### `ppp_mgmt_raise_phase_dead_event()`

```c
void ppp_mgmt_raise_phase_dead_event ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ppp.h>
```

PPP 到达 DEAD 阶段时产生 PHASE_DEAD 事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | PPP 网络接口（Network Interface）。 |

<a id="ga74e94e9fcae30bc386c5e3d951ed5882"></a>

### `ppp_mgmt_raise_phase_running_event()`

```c
void ppp_mgmt_raise_phase_running_event ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ppp.h>
```

PPP 到达 RUNNING 阶段时产生 PHASE_RUNNING 事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | PPP 网络接口（Network Interface）。 |

<a id="ga716727874cecc8ee358da6c76adedc0a"></a>

### `ppp_peer_async_control_character_map()`

```c
uint32_t ppp_peer_async_control_character_map ( struct net_if * iface)
```

```c
#include <zephyr/net/ppp.h>
```

获取 PPP 对端的异步控制字符映射（Asynchronous Control Character Map，ACCM）。

PPP 链路控制协议（LCP）协商完成前，此函数返回默认值 0xffffffff；协商完成后，返回对端提供的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | PPP 网络接口（Network Interface）。 |

返回（Returns）：uint32_t，当前异步控制字符映射（Asynchronous Control Character Map）的位掩码。


## 16.7\_原页交叉引用（Cross References）

- [ppp_api](../network_service_model_reference/P042_ppp_api_结构体.md)
- [ppp_fsm](../network_service_model_reference/P044_ppp_fsm_结构体.md)
- [lcp_options](../network_service_model_reference/P028_lcp_options_结构体.md)
- [ipcp_options](../network_service_model_reference/P026_ipcp_options_结构体.md)
- [ipv6cp_options](../network_service_model_reference/P027_ipv6cp_options_结构体.md)
- [ppp_context](../network_service_model_reference/P043_ppp_context_结构体.md)
- [RFC 1661, section-6](https://datatracker.ietf.org/doc/html/rfc1661#section-6)
- [RFC 1332 规范。](https://datatracker.ietf.org/doc/html/rfc1332)
- [RFC 5072 规范。](https://datatracker.ietf.org/doc/html/rfc5072)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/net/ppp.h](../api_file_battery_interrupt_reference/P008_zephyr__net__ppp.h_文件参考.md)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [https://www.iana.org/assignments/ppp-numbers/ppp-numbers.xhtml](https://www.iana.org/assignments/ppp-numbers/ppp-numbers.xhtml)
- [RFC 1968 规范。](https://datatracker.ietf.org/doc/html/rfc1968)
- [RFC 1962 规范。](https://datatracker.ietf.org/doc/html/rfc1962)
- [RFC 1661 规范。](https://datatracker.ietf.org/doc/html/rfc1661)
- [RFC 1334 规范。](https://datatracker.ietf.org/doc/html/rfc1334)
- [RFC 2284 规范。](https://datatracker.ietf.org/doc/html/rfc2284)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b"></a>
<a id="gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b"></a>
<a id="gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6"></a>
<a id="gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9"></a>
<a id="gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931"></a>
<a id="gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552"></a>
<a id="gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964"></a>
<a id="gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad"></a>
<a id="ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858"></a>
<a id="ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7"></a>
<a id="ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3"></a>
<a id="ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe"></a>
<a id="ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef"></a>
<a id="ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743"></a>
<a id="ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9"></a>
<a id="ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8"></a>
<a id="ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4"></a>
<a id="ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524"></a>
<a id="gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d"></a>
<a id="gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4"></a>
<a id="gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a"></a>
<a id="gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af"></a>
<a id="gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7"></a>
<a id="gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25"></a>
<a id="gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_MFD M5PM1 接口.md) · [返回大纲](大纲.md) · [下一章](P017_系统控制与管理接口（SCMI）.md)
