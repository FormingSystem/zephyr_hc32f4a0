---
id: learning.zephyr-docs.api-network-work-driver-reference.page-5
title: 应用网络上下文（Application network context）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_应用网络上下文（Application network context）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

应用网络上下文（Application network context）

<a id="details"></a>

应用网络上下文（Application Network Context）。自 1.0 起提供；接口版本为 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_net_5Fcontext"></a>

```c
struct net_context
```

相关声明：[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

注意，上下文中不保存实际源IP地址，因为该地址已在网络接口结构（Network Interface Struct）中设置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga5e2f5fcc08863a4090bc04040ee88d29"></a>

```c
#define NET_CONTEXT_IN_USE BIT(0)
```

相关声明：[NET_CONTEXT_IN_USE](#ga5e2f5fcc08863a4090bc04040ee88d29)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此上下文（Context）是否正在使用。

<a id="r_gac8f6e3a16d52e8e376c38eec0ed8a940"></a>

```c
#define NET_CONTEXT_FAMILY (BIT(3) | BIT(4) | BIT(5))
```

相关声明：[NET_CONTEXT_FAMILY](#gac8f6e3a16d52e8e376c38eec0ed8a940)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

地址族（Address Family）、连接类型（Connection Type）和 IP 协议（IP Protocol）存储在位字段（Bit Field）中，以节省空间。

<a id="r_gac9b4cf9beecaac5bf05db3111c803678"></a>

```c
#define NET_CONTEXT_TYPE (BIT(6) | BIT(7))
```

相关声明：[NET_CONTEXT_TYPE](#gac9b4cf9beecaac5bf05db3111c803678)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

连接类型（Connection Type）：数据报（Datagram）、流（Stream）或原始类型（Raw）。

<a id="r_ga84206421e8f2e1eb114d393f0c81428b"></a>

```c
#define NET_CONTEXT_REMOTE_ADDR_SET BIT(8)
```

相关声明：[NET_CONTEXT_REMOTE_ADDR_SET](#ga84206421e8f2e1eb114d393f0c81428b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

远端地址已设置（Remote Address Set）。

<a id="r_gaa337bccec2c1df42540f236bb33a70e1"></a>

```c
#define NET_CONTEXT_BOUND_TO_IFACE BIT(9)
```

相关声明：[NET_CONTEXT_BOUND_TO_IFACE](#gaa337bccec2c1df42540f236bb33a70e1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

上下文已绑定到特定接口（Specific Interface）。

<a id="r_ga717b1aaa11d589bfe929d98be5be19ed"></a>

```c
#define NET_CONTEXT_LOCAL_ADDR_SET BIT(10)
```

相关声明：[NET_CONTEXT_LOCAL_ADDR_SET](#ga717b1aaa11d589bfe929d98be5be19ed)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

本地地址（Local Address）已绑定到此上下文。

<a id="r_ga41d258362d6a7a703bc0b65d08e2b4c4"></a>

```c
#define net_context_setup_pools(context, tx_slab, data_pool)
```

相关声明：[net_context_setup_pools](#ga41d258362d6a7a703bc0b65d08e2b4c4)。

为上下文发送操作设置自定义网络缓冲池（Custom Network Buffer Pools）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_gafa485a6fae8237dd7e6856f4567b2317"></a>

```c
typedef void(* net_context_recv_cb_t) (struct net_context *context, struct net_pkt *pkt, union net_ip_header *ip_hdr, union net_proto_header *proto_hdr, int status, void *user_data)
```

相关声明：[net_context_recv_cb_t](#gafa485a6fae8237dd7e6856f4567b2317)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

网络数据接收回调（Network Data Receive Callback）。

<a id="r_gab3caccfe9fa1bc7ce0e4654192a5de93"></a>

```c
typedef void(* net_context_send_cb_t) (struct net_context *context, int status, void *user_data)
```

相关声明：[net_context_send_cb_t](#gab3caccfe9fa1bc7ce0e4654192a5de93)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

网络数据发送回调（Network Data Send Callback）。

<a id="r_gaf05114d2edc8b5fb485fd37f3d0821ba"></a>

```c
typedef void(* net_tcp_accept_cb_t) (struct net_context *new_context, struct net_sockaddr *addr, net_socklen_t addrlen, int status, void *user_data)
```

相关声明：[net_tcp_accept_cb_t](#gaf05114d2edc8b5fb485fd37f3d0821ba)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga361fe60d9b96001f74363788352858a0)。

接受连接回调（Accept Callback）。

<a id="r_ga120ae8d4ff788ab21b19c11ed1738a71"></a>

```c
typedef void(* net_context_connect_cb_t) (struct net_context *context, int status, void *user_data)
```

相关声明：[net_context_connect_cb_t](#ga120ae8d4ff788ab21b19c11ed1738a71)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

连接回调（Connection Callback）。

<a id="r_ga3bb4bbd522ede36213bafe86f2d1d770"></a>

```c
typedef struct k_mem_slab *(* net_pkt_get_slab_func_t) (void)
```

相关声明：[net_pkt_get_slab_func_t](#ga3bb4bbd522ede36213bafe86f2d1d770)。

用于获取 `net_pkt` 分配所用内存块池（Slab）的函数。

<a id="r_gae3082af116955d4175c025a02b296c91"></a>

```c
typedef struct net_buf_pool *(* net_pkt_get_pool_func_t) (void)
```

相关声明：[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[net_pkt_get_pool_func_t](#gae3082af116955d4175c025a02b296c91)。

用于获取 `net_buf` 分配所用缓冲池（Pool）的函数。

<a id="r_gaa82d80fa18693b98dc363c35104075ba"></a>

```c
typedef void(* net_context_cb_t) (struct net_context *context, void *user_data)
```

相关声明：[net_context_cb_t](#gaa82d80fa18693b98dc363c35104075ba)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

遍历网络上下文（Network Context）时使用的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.4\_枚举（Enumerations）

<a id="r_gab03a354899ff68f6b9d127bc3bb5e17d"></a>

```c
enum net_context_option { NET_OPT_PRIORITY = 1 , NET_OPT_TXTIME = 2 , NET_OPT_SOCKS5 = 3 , NET_OPT_RCVTIMEO = 4 , NET_OPT_SNDTIMEO = 5 , NET_OPT_RCVBUF = 6 , NET_OPT_SNDBUF = 7 , NET_OPT_DSCP_ECN = 8 , NET_OPT_REUSEADDR = 9 , NET_OPT_REUSEPORT = 10 , NET_OPT_IPV6_V6ONLY = 11 , NET_OPT_RECV_PKTINFO = 12 , NET_OPT_MCAST_TTL = 13 , NET_OPT_MCAST_HOP_LIMIT = 14 , NET_OPT_UNICAST_HOP_LIMIT = 15 , NET_OPT_TTL = 16 , NET_OPT_ADDR_PREFERENCES = 17 , NET_OPT_TIMESTAMPING = 18 , NET_OPT_MCAST_IFINDEX = 19 , NET_OPT_MTU = 20 , NET_OPT_LOCAL_PORT_RANGE = 21 , NET_OPT_IPV6_MCAST_LOOP = 22 , NET_OPT_IPV4_MCAST_LOOP = 23 , NET_OPT_RECV_HOPLIMIT = 24 , NET_OPT_DONT_FRAGMENT = 25 , NET_OPT_LINGER = 26 , NET_OPT_UDP_OPT = 27 , NET_OPT_UDP_OPT_OCS = 28 , NET_OPT_UDP_OPT_APC = 29 , NET_OPT_UDP_OPT_FRAG = 30 , NET_OPT_UDP_OPT_MDS = 31 , NET_OPT_UDP_OPT_MRDS = 32 , NET_OPT_UDP_OPT_REQ = 33 , NET_OPT_UDP_OPT_RES = 34 , NET_OPT_UDP_OPT_TIME = 35 , NET_OPT_UDP_OPT_AUTH = 36 , NET_OPT_UDP_OPT_EXP = 37 , NET_OPT_UDP_OPT_UCMP = 38 , NET_OPT_UDP_OPT_UENC = 39 , NET_OPT_UDP_OPT_UEXP = 40 , NET_OPT_UDP_OPT_DPLPMTUD = 41 , NET_OPT_UDP_OPT_DPLPMTUD_APP_RESPOND = 42 }
```

相关声明：[net_context_option](#gab03a354899ff68f6b9d127bc3bb5e17d)、[NET_OPT_PRIORITY](#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c)、[NET_OPT_TXTIME](#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184)、[NET_OPT_SOCKS5](#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c)、[NET_OPT_RCVTIMEO](#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076)、[NET_OPT_SNDTIMEO](#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668)、[NET_OPT_RCVBUF](#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1)、[NET_OPT_SNDBUF](#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08)、[NET_OPT_DSCP_ECN](#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c)、[NET_OPT_REUSEADDR](#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561)、[NET_OPT_REUSEPORT](#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4)、[NET_OPT_IPV6_V6ONLY](#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c)、[NET_OPT_RECV_PKTINFO](#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a)、[NET_OPT_MCAST_TTL](#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e)、[NET_OPT_MCAST_HOP_LIMIT](#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d)、[NET_OPT_UNICAST_HOP_LIMIT](#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3)、[NET_OPT_TTL](#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184)、[NET_OPT_ADDR_PREFERENCES](#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d)、[NET_OPT_TIMESTAMPING](#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2)、[NET_OPT_MCAST_IFINDEX](#ggab03a354899ff68f6b9d127bc3bb5e17da98136d42db895cf6f3e35ee418e0b7eb)、[NET_OPT_MTU](#ggab03a354899ff68f6b9d127bc3bb5e17dad6b8627398a90dd622f433e8b3fee3a3)、[NET_OPT_LOCAL_PORT_RANGE](#ggab03a354899ff68f6b9d127bc3bb5e17da469d1d21e088eba6f96ec0a679636ba7)、[NET_OPT_IPV6_MCAST_LOOP](#ggab03a354899ff68f6b9d127bc3bb5e17dab1615ef9a3bf84daf964a445476bc04c)、[NET_OPT_IPV4_MCAST_LOOP](#ggab03a354899ff68f6b9d127bc3bb5e17da38adf4f5e3fba71f152a05c208e6f9f0)、[NET_OPT_RECV_HOPLIMIT](#ggab03a354899ff68f6b9d127bc3bb5e17da3f5fea1c10f55d4db1d72bba2959445e)、[NET_OPT_DONT_FRAGMENT](#ggab03a354899ff68f6b9d127bc3bb5e17dad5099786ebcdc0198cf3cd1db465387d)、[NET_OPT_LINGER](#ggab03a354899ff68f6b9d127bc3bb5e17dae0ed5497e4d356ca2bdea0a120dcb6ee)、[NET_OPT_UDP_OPT](#ggab03a354899ff68f6b9d127bc3bb5e17dacd227331833af7fb92b84f3ceb80f3ab)、[NET_OPT_UDP_OPT_OCS](#ggab03a354899ff68f6b9d127bc3bb5e17da9dec13665201fdc9be87490cde2f3253)、[NET_OPT_UDP_OPT_APC](#ggab03a354899ff68f6b9d127bc3bb5e17da69e538d1b4732c865384340989f011c8)、[NET_OPT_UDP_OPT_FRAG](#ggab03a354899ff68f6b9d127bc3bb5e17da9db3637a09382655835493aed186a549)、[NET_OPT_UDP_OPT_MDS](#ggab03a354899ff68f6b9d127bc3bb5e17da104d851b3c8884c875dbbc9d1e6c64ae)、[NET_OPT_UDP_OPT_MRDS](#ggab03a354899ff68f6b9d127bc3bb5e17da12c660c9ee2dd9d9d2de36980949aa9f)、[NET_OPT_UDP_OPT_REQ](#ggab03a354899ff68f6b9d127bc3bb5e17da6441103cc8e0e3cf724d2ea79cf18dcb)、[NET_OPT_UDP_OPT_RES](#ggab03a354899ff68f6b9d127bc3bb5e17dae72a8a6e3f4a7a14370cd1267820c71d)、[NET_OPT_UDP_OPT_TIME](#ggab03a354899ff68f6b9d127bc3bb5e17da61c105080d36bca8b4405527af4aaac4)、[NET_OPT_UDP_OPT_AUTH](#ggab03a354899ff68f6b9d127bc3bb5e17dab4dd4a3acee76f82c37fd16fd5f53867)、[NET_OPT_UDP_OPT_EXP](#ggab03a354899ff68f6b9d127bc3bb5e17daa3a443af92a7bc45aa9cc81ca4a1de0c)、[NET_OPT_UDP_OPT_UCMP](#ggab03a354899ff68f6b9d127bc3bb5e17da98f7a13028a2deb6eee31f1bad7c20b7)、[NET_OPT_UDP_OPT_UENC](#ggab03a354899ff68f6b9d127bc3bb5e17dae95fc08de9277a59c42d6bf6355ec201)、[NET_OPT_UDP_OPT_UEXP](#ggab03a354899ff68f6b9d127bc3bb5e17da885dadd317c676c4d9be316df29ff276)、[NET_OPT_UDP_OPT_DPLPMTUD](#ggab03a354899ff68f6b9d127bc3bb5e17da4c24ea3a7cafcd9eddfc15a5725d75d2)、[NET_OPT_UDP_OPT_DPLPMTUD_APP_RESPOND](#ggab03a354899ff68f6b9d127bc3bb5e17daf50b6d1ab2da2df3b2ba1f991fc8011e)。

网络上下文选项（Network Context Options）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.5\_函数（Functions）

<a id="r_ga423103d5c386b602737e23ee81f2a961"></a>

```c
static bool net_context_is_used (struct net_context *context)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_is_used](#ga423103d5c386b602737e23ee81f2a961)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

此上下文（Context）是否正在使用。

<a id="r_ga2f6d614158c999fa68e518393c0a9c35"></a>

```c
static bool net_context_is_bound_to_iface (struct net_context *context)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_is_bound_to_iface](#ga2f6d614158c999fa68e518393c0a9c35)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

此上下文是否已绑定到网络接口（Network Interface）。

<a id="r_ga8e93032d6b65d9b5dfc0f64ecdf3a6b5"></a>

```c
static bool net_context_is_local_addr_set (struct net_context *context)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_is_local_addr_set](#ga8e93032d6b65d9b5dfc0f64ecdf3a6b5)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

是否已有本地地址（Local Address）绑定到此上下文。

<a id="r_ga53bd5f35a142f1d43f90d3bde99778e0"></a>

```c
static enum net_context_state net_context_get_state (struct net_context *context)
```

相关声明：[net_context_get_state](#ga53bd5f35a142f1d43f90d3bde99778e0)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的状态（State）。

<a id="r_gaac934209341db606a4d563b3c48cce45"></a>

```c
static void net_context_set_state (struct net_context *context, enum net_context_state state)
```

相关声明：[net_context_set_state](#gaac934209341db606a4d563b3c48cce45)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置此网络上下文的状态（State）。

<a id="r_ga4c3de0a3b7f27dd8ac9d0f415710faad"></a>

```c
static net_sa_family_t net_context_get_family (struct net_context *context)
```

相关声明：[net_sa_family_t](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga8b4cfadf1b284e52d6905ca88657b48a)、[net_context_get_family](#ga4c3de0a3b7f27dd8ac9d0f415710faad)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的地址族（Address Family）。

<a id="r_ga37bbecc848430590d5d68d2880c83c1e"></a>

```c
static void net_context_set_family (struct net_context *context, net_sa_family_t family)
```

相关声明：[net_context_set_family](#ga37bbecc848430590d5d68d2880c83c1e)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sa_family_t](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga8b4cfadf1b284e52d6905ca88657b48a)。

设置此网络上下文的地址族（Address Family）。

<a id="r_ga24b4d99dddc4fabf383f5d8079650337"></a>

```c
static enum net_sock_type net_context_get_type (struct net_context *context)
```

相关声明：[net_sock_type](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gaaab4268707dbe08348b98fb028e7aa5c)、[net_context_get_type](#ga24b4d99dddc4fabf383f5d8079650337)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的上下文类型（Context Type）。

<a id="r_ga01c11c1dfce101df046df9ade00ed277"></a>

```c
static void net_context_set_type (struct net_context *context, enum net_sock_type type)
```

相关声明：[net_context_set_type](#ga01c11c1dfce101df046df9ade00ed277)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sock_type](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gaaab4268707dbe08348b98fb028e7aa5c)。

设置此网络上下文的上下文类型（Context Type）。

<a id="r_ga581582c0461b36088d21d0fd433cc284"></a>

```c
static void net_context_set_can_filter_id (struct net_context *context, int filter_id)
```

相关声明：[net_context_set_can_filter_id](#ga581582c0461b36088d21d0fd433cc284)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

设置此网络上下文的 CAN 过滤器标识符（CAN Filter ID）。

<a id="r_ga7f4d732a99cb9e86fcd5226fbbb727f4"></a>

```c
static int net_context_get_can_filter_id (struct net_context *context)
```

相关声明：[net_context_get_can_filter_id](#ga7f4d732a99cb9e86fcd5226fbbb727f4)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的 CAN 过滤器标识符（CAN Filter ID）。

<a id="r_gadf41291ca5be067e830d121000ca3f51"></a>

```c
static uint16_t net_context_get_proto (struct net_context *context)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_context_get_proto](#gadf41291ca5be067e830d121000ca3f51)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的 IP 协议（IP Protocol）。

<a id="r_gadcd0049229580244ea89fbc98bf23a81"></a>

```c
static void net_context_set_proto (struct net_context *context, uint16_t proto)
```

相关声明：[net_context_set_proto](#gadcd0049229580244ea89fbc98bf23a81)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置此网络上下文的 IP 协议（IP Protocol）。

<a id="r_gafe6b8c9af4464cd471285817d6d61087"></a>

```c
static struct net_if * net_context_get_iface (struct net_context *context)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_context_get_iface](#gafe6b8c9af4464cd471285817d6d61087)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的网络接口（Network Interface）。

<a id="r_ga10399e3f3d159de9325ac7632ce25c51"></a>

```c
static void net_context_set_iface (struct net_context *context, struct net_if *iface)
```

相关声明：[net_context_set_iface](#ga10399e3f3d159de9325ac7632ce25c51)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置此上下文的网络接口（Network Interface）。

<a id="r_ga2f8fccd2453227706e313ac056f1c6ef"></a>

```c
static void net_context_bind_iface (struct net_context *context, struct net_if *iface)
```

相关声明：[net_context_bind_iface](#ga2f8fccd2453227706e313ac056f1c6ef)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将网络接口（Network Interface）绑定到此上下文。

<a id="r_ga9cdb3e5849a5b2663e0a38ac2a39a427"></a>

```c
static uint8_t net_context_get_ipv4_ttl (struct net_context *context)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_context_get_ipv4_ttl](#ga9cdb3e5849a5b2663e0a38ac2a39a427)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的 IPv4 生存时间值（Time-to-live，TTL）。

<a id="r_ga11672ca3ebdae63b0013ad76959304d5"></a>

```c
static void net_context_set_ipv4_ttl (struct net_context *context, uint8_t ttl)
```

相关声明：[net_context_set_ipv4_ttl](#ga11672ca3ebdae63b0013ad76959304d5)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置此上下文的 IPv4 生存时间值（Time-to-live，TTL）。

<a id="r_ga3db832f40b6a0b975a282ef354a7bffc"></a>

```c
static uint8_t net_context_get_ipv4_mcast_ttl (struct net_context *context)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_context_get_ipv4_mcast_ttl](#ga3db832f40b6a0b975a282ef354a7bffc)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的 IPv4 组播生存时间值（Multicast TTL）。

<a id="r_gab2a2064fa33613a60ad40597d0971774"></a>

```c
static void net_context_set_ipv4_mcast_ttl (struct net_context *context, uint8_t ttl)
```

相关声明：[net_context_set_ipv4_mcast_ttl](#gab2a2064fa33613a60ad40597d0971774)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置此上下文的 IPv4 组播生存时间值（Multicast TTL）。

<a id="r_ga977b08a77586e0e4752bff725139427c"></a>

```c
static uint8_t net_context_get_ipv6_hop_limit (struct net_context *context)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_context_get_ipv6_hop_limit](#ga977b08a77586e0e4752bff725139427c)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的 IPv6 跳数限制值（Hop Limit）。

<a id="r_ga0cbf8377e7757881033aab3e718b1a61"></a>

```c
static void net_context_set_ipv6_hop_limit (struct net_context *context, uint8_t hop_limit)
```

相关声明：[net_context_set_ipv6_hop_limit](#ga0cbf8377e7757881033aab3e718b1a61)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置此上下文的 IPv6 跳数限制值（Hop Limit）。

<a id="r_ga99b5f0ded5d56b735e051ede5651f435"></a>

```c
static uint8_t net_context_get_ipv6_mcast_hop_limit (struct net_context *context)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_context_get_ipv6_mcast_hop_limit](#ga99b5f0ded5d56b735e051ede5651f435)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的 IPv6 组播跳数限制值（Multicast Hop Limit）。

<a id="r_gaf29d5ee244c552d78171938a903fbaca"></a>

```c
static void net_context_set_ipv6_mcast_hop_limit (struct net_context *context, uint8_t hop_limit)
```

相关声明：[net_context_set_ipv6_mcast_hop_limit](#gaf29d5ee244c552d78171938a903fbaca)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置此上下文的 IPv6 组播跳数限制值（Multicast Hop Limit）。

<a id="r_ga9bd6b5e9429b6e845d41f6cbf242c092"></a>

```c
static void net_context_set_proxy_enabled (struct net_context *context, bool enable)
```

相关声明：[net_context_set_proxy_enabled](#ga9bd6b5e9429b6e845d41f6cbf242c092)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为此上下文启用或禁用 SOCKS 代理支持（SOCKS Proxy Support）。

<a id="r_ga5c3a841ff54ddb53cedcccefde5a7d7a"></a>

```c
static bool net_context_is_proxy_enabled (struct net_context *context)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_is_proxy_enabled](#ga5c3a841ff54ddb53cedcccefde5a7d7a)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

此上下文的 SOCKS 代理支持（SOCKS Proxy Support）是启用还是禁用。

<a id="r_ga37fbf84456a4142330d74eed1f3c24f6"></a>

```c
int net_context_get (net_sa_family_t family, enum net_sock_type type, uint16_t ip_proto, struct net_context **context)
```

相关声明：[net_context_get](#ga37fbf84456a4142330d74eed1f3c24f6)、[net_sa_family_t](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga8b4cfadf1b284e52d6905ca88657b48a)、[net_sock_type](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gaaab4268707dbe08348b98fb028e7aa5c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取网络上下文（Network Context）。

<a id="r_ga1d6b64e302c546db589c661f4b6bda98"></a>

```c
int net_context_put (struct net_context *context)
```

相关声明：[net_context_put](#ga1d6b64e302c546db589c661f4b6bda98)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

关闭网络上下文（Network Context），并释放其引用（Unref）。

<a id="r_ga4c0ef9540a0d7e800c4529274f5c22f4"></a>

```c
int net_context_ref (struct net_context *context)
```

相关声明：[net_context_ref](#ga4c0ef9540a0d7e800c4529274f5c22f4)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取一个 `net_context` 引用，增加引用计数（Reference Count），以防止该上下文被销毁。

<a id="r_ga0d391690d9d6972ce6f4baedeab64b11"></a>

```c
int net_context_unref (struct net_context *context)
```

相关声明：[net_context_unref](#ga0d391690d9d6972ce6f4baedeab64b11)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

减少网络上下文（Network Context）的引用计数（Reference Count）。

<a id="r_ga11801119ad1d62db0302479c133adb35"></a>

```c
static void net_context_signal_linger (struct net_context *context)
```

相关声明：[net_context_signal_linger](#ga11801119ad1d62db0302479c133adb35)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

通知此上下文的底层连接已由传输层（Transport）关闭，使因 `SO_LINGER` 而阻塞的 `close()` 能够继续执行。

<a id="r_gae3b3892b921e4694a18e7bacee63841d"></a>

```c
static int net_context_create_ipv4_new (struct net_context *context, struct net_pkt *pkt, const struct net_in_addr *src, const struct net_in_addr *dst)
```

相关声明：[net_context_create_ipv4_new](#gae3b3892b921e4694a18e7bacee63841d)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

根据上下文，在提供的 `net_pkt` 中创建 IPv4 数据包（IPv4 Packet）。

<a id="r_gaa973878eb7f6bf69d91da992edad6409"></a>

```c
static int net_context_create_ipv6_new (struct net_context *context, struct net_pkt *pkt, const struct net_in6_addr *src, const struct net_in6_addr *dst)
```

相关声明：[net_context_create_ipv6_new](#gaa973878eb7f6bf69d91da992edad6409)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

根据上下文，在提供的 `net_pkt` 中创建 IPv6 数据包（IPv6 Packet）。

<a id="r_ga2023f160b4d2ebc05d665d119611ef25"></a>

```c
int net_context_bind (struct net_context *context, const struct net_sockaddr *addr, net_socklen_t addrlen)
```

相关声明：[net_context_bind](#ga2023f160b4d2ebc05d665d119611ef25)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga361fe60d9b96001f74363788352858a0)。

为套接字（Socket）分配本地地址（Local Address）。

<a id="r_ga3803c0d738fbb9d786f401aacc10a4d3"></a>

```c
int net_context_listen (struct net_context *context, int backlog)
```

相关声明：[net_context_listen](#ga3803c0d738fbb9d786f401aacc10a4d3)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

将上下文标记为监听状态（Listening）。

<a id="r_gadf4ab08eb39803909e585b16ce68307a"></a>

```c
int net_context_connect (struct net_context *context, const struct net_sockaddr *addr, net_socklen_t addrlen, net_context_connect_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_connect](#gadf4ab08eb39803909e585b16ce68307a)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga361fe60d9b96001f74363788352858a0)、[net_context_connect_cb_t](#ga120ae8d4ff788ab21b19c11ed1738a71)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

创建网络连接（Network Connection）。

<a id="r_ga1b056999d9ab8f2d3b3c0f4788f36cdd"></a>

```c
int net_context_accept (struct net_context *context, net_tcp_accept_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_accept](#ga1b056999d9ab8f2d3b3c0f4788f36cdd)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_tcp_accept_cb_t](#gaf05114d2edc8b5fb485fd37f3d0821ba)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

接受网络连接尝试（Network Connection Attempt）。

<a id="r_gac793e1def18200416e3f679067c56ab3"></a>

```c
int net_context_send (struct net_context *context, const void *buf, size_t len, net_context_send_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_send](#gac793e1def18200416e3f679067c56ab3)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_context_send_cb_t](#gab3caccfe9fa1bc7ce0e4654192a5de93)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向对端（Peer）发送数据。

<a id="r_gafd68de53778cbd807d0e45209a83df05"></a>

```c
int net_context_sendto (struct net_context *context, const void *buf, size_t len, const struct net_sockaddr *dst_addr, net_socklen_t addrlen, net_context_send_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_sendto](#gafd68de53778cbd807d0e45209a83df05)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga361fe60d9b96001f74363788352858a0)、[net_context_send_cb_t](#gab3caccfe9fa1bc7ce0e4654192a5de93)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向地址指定的对端（Peer）发送数据。

<a id="r_gaf915131b95b159e299f034768cefdaea"></a>

```c
int net_context_sendmsg (struct net_context *context, const struct net_msghdr *msghdr, int flags, net_context_send_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_sendmsg](#gaf915131b95b159e299f034768cefdaea)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_context_send_cb_t](#gab3caccfe9fa1bc7ce0e4654192a5de93)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

将 `iovec` 中的数据发送给 `net_msghdr` 结构体指定的对端（Peer）。

<a id="r_ga74f919185f8af074c2d90aa04733dd2a"></a>

```c
int net_context_recv (struct net_context *context, net_context_recv_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_recv](#ga74f919185f8af074c2d90aa04733dd2a)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_context_recv_cb_t](#gafa485a6fae8237dd7e6856f4567b2317)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从上下文指定的对端（Peer）接收网络数据。

<a id="r_gab3cc2a13e24f9c263bc40cc87d752a9f"></a>

```c
int net_context_update_recv_wnd (struct net_context *context, int32_t delta)
```

相关声明：[net_context_update_recv_wnd](#gab3cc2a13e24f9c263bc40cc87d752a9f)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

更新此上下文的 TCP 接收窗口（TCP Receive Window）。

<a id="r_ga40c6ef5b1f8b846e5b205947e87ce585"></a>

```c
int net_context_set_option (struct net_context *context, enum net_context_option option, const void *value, uint32_t len)
```

相关声明：[net_context_set_option](#ga40c6ef5b1f8b846e5b205947e87ce585)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_context_option](#gab03a354899ff68f6b9d127bc3bb5e17d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置此上下文的连接选项（Connection Option）。

<a id="r_gabbb9472c54b2fbe0b519dcb68e02a44e"></a>

```c
int net_context_get_option (struct net_context *context, enum net_context_option option, void *value, uint32_t *len)
```

相关声明：[net_context_get_option](#gabbb9472c54b2fbe0b519dcb68e02a44e)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_context_option](#gab03a354899ff68f6b9d127bc3bb5e17d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取此上下文的连接选项值（Connection Option Value）。

<a id="r_gaefead18501a966af4a7f71eb23ac17c7"></a>

```c
int net_context_set_udp_dplpmtud (struct net_context *context, bool enable)
```

相关声明：[net_context_set_udp_dplpmtud](#gaefead18501a966af4a7f71eb23ac17c7)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在 UDP 上下文上启用或禁用数据报分组层路径 MTU 发现（DPLPMTUD，RFC 9869）。

<a id="r_gabb751f7d213d00f8eec72a67f4ce3491"></a>

```c
void net_context_foreach (net_context_cb_t cb, void *user_data)
```

相关声明：[net_context_foreach](#gabb751f7d213d00f8eec72a67f4ce3491)、[net_context_cb_t](#gaa82d80fa18693b98dc363c35104075ba)。

遍历全部网络连接，并为每个网络上下文（Network Context）调用回调（Callback）。

<a id="r_gad9350d40a884315ff9de4032a8d6ae71"></a>

```c
bool net_context_port_in_use (enum net_ip_protocol ip_proto, uint16_t local_port, const struct net_sockaddr *local_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_port_in_use](#gad9350d40a884315ff9de4032a8d6ae71)、[net_ip_protocol](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gaf06819bf427cc58be1229b27b373ca31)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

检查端口是否正在使用，即是否已绑定（Bound）。

## 5.6\_详细说明（Detailed Documentation）

<a id="gaa337bccec2c1df42540f236bb33a70e1"></a>

### `NET_CONTEXT_BOUND_TO_IFACE`

```c
#define NET_CONTEXT_BOUND_TO_IFACE BIT(9)
```

```c
#include <zephyr/net/net_context.h>
```

上下文已绑定到特定接口（Specific Interface）。

<a id="gac8f6e3a16d52e8e376c38eec0ed8a940"></a>

### `NET_CONTEXT_FAMILY`

```c
#define NET_CONTEXT_FAMILY (BIT(3) | BIT(4) | BIT(5))
```

```c
#include <zephyr/net/net_context.h>
```

地址族（Address Family）、连接类型（Connection Type）和 IP 协议（IP Protocol）存储在位字段（Bit Field）中，以节省空间。

此连接的协议族（Protocol Family）。

<a id="ga5e2f5fcc08863a4090bc04040ee88d29"></a>

### `NET_CONTEXT_IN_USE`

```c
#define NET_CONTEXT_IN_USE BIT(0)
```

```c
#include <zephyr/net/net_context.h>
```

此上下文（Context）是否正在使用。

<a id="ga717b1aaa11d589bfe929d98be5be19ed"></a>

### `NET_CONTEXT_LOCAL_ADDR_SET`

```c
#define NET_CONTEXT_LOCAL_ADDR_SET BIT(10)
```

```c
#include <zephyr/net/net_context.h>
```

本地地址（Local Address）已绑定到此上下文。

<a id="ga84206421e8f2e1eb114d393f0c81428b"></a>

### `NET_CONTEXT_REMOTE_ADDR_SET`

```c
#define NET_CONTEXT_REMOTE_ADDR_SET BIT(8)
```

```c
#include <zephyr/net/net_context.h>
```

远端地址已设置（Remote Address Set）。

<a id="ga41d258362d6a7a703bc0b65d08e2b4c4"></a>

### `net_context_setup_pools`

```c
#define net_context_setup_pools ( context, tx_slab, data_pool )
```

```c
#include <zephyr/net/net_context.h>
```

为上下文发送操作设置自定义网络缓冲池（Custom Network Buffer Pools）。

设置自定义网络缓冲池（Network Buffer Pools），供 IP 协议栈为此上下文向网络发送数据时分配网络缓冲区。使用专用缓冲区可提高给定上下文发送操作的可靠性，例如避免其他网络上下文的操作导致缓冲区耗尽（Buffer Starvation）。缓冲池按上下文设置，但多个上下文可以共享同一组缓冲区。注意：不支持按上下文设置自定义接收数据包缓冲池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 将使用给定 `net_buf` 缓冲池的上下文（Context）。 |
| `tx_slab` | 指向向调用者返回发送缓冲池（TX Pool）的函数。该缓冲池用于向网络发送数据，每个发送的网络数据包对应一个 TX `net_pkt`。 |
| `data_pool` | 指向向调用者返回数据缓冲池（DATA Pool）的函数。该缓冲池用于存储要发送到网络的数据。 |

<a id="gac9b4cf9beecaac5bf05db3111c803678"></a>

### `NET_CONTEXT_TYPE`

```c
#define NET_CONTEXT_TYPE (BIT(6) | BIT(7))
```

```c
#include <zephyr/net/net_context.h>
```

连接类型（Connection Type）：数据报（Datagram）、流（Stream）或原始类型（Raw）。

<a id="gaa82d80fa18693b98dc363c35104075ba"></a>

### `net_context_cb_t`

```c
typedef void(* net_context_cb_t) (struct net_context *context, void *user_data)
```

```c
#include <zephyr/net/net_context.h>
```

遍历网络上下文（Network Context）时使用的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 指向当前网络上下文（Network Context）的有效指针。 |
| `user_data` | 指向某些用户数据（User Data）的有效指针，或 NULL。 |

<a id="ga120ae8d4ff788ab21b19c11ed1738a71"></a>

### `net_context_connect_cb_t`

```c
typedef void(* net_context_connect_cb_t) (struct net_context *context, int status, void *user_data)
```

```c
#include <zephyr/net/net_context.h>
```

连接回调（Connection Callback）。

连接回调（Connect Callback）在连接建立过程之后调用。对于 TCP 连接，回调由接收线程（RX Thread）调用，因此使用该线程的栈和执行上下文；它在 TCP 连接建立成功或连接失败后调用。应尽量减少回调中的处理，以缩短数据包处理被阻塞的时间。对于 UDP 连接，此回调由 `net_context_connect()` 立即调用。UDP 是无连接协议（Connectionless Protocol），因此可认为连接立即建立。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的上下文（Context）。 |
| `status` | 连接建立状态（Connection Establishment Status）：成功时为 0，出错时小于 0。 |
| `user_data` | 调用 `net_context_connect()` 时提供的用户数据（User Data）。 |

<a id="gafa485a6fae8237dd7e6856f4567b2317"></a>

### `net_context_recv_cb_t`

```c
typedef void(* net_context_recv_cb_t) (struct net_context *context, struct net_pkt *pkt, union net_ip_header *ip_hdr, union net_proto_header *proto_hdr, int status, void *user_data)
```

```c
#include <zephyr/net/net_context.h>
```

网络数据接收回调（Network Data Receive Callback）。

接收回调（Recv Callback）在收到网络数据包后调用。此回调由接收线程（RX Thread）调用，因此使用该线程的栈和执行上下文。应尽量减少回调中的处理，以缩短数据包处理被阻塞的时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的上下文（Context）。 |
| `pkt` | 收到的网络缓冲区（Network Buffer）。如果 `pkt` 不为 `NULL`，则回调拥有此缓冲区，处理完成后必须尽快解除对 `pkt` 的引用（Unref）。到达结束位置（EOF）时，`pkt` 为 `NULL`。 |
| `ip_hdr` | 指向相应 IP 头（IPv4 或 IPv6 Header）的指针。 |
| `proto_hdr` | 指向相应协议头（UDP 或 TCP Header）的指针。 |
| `status` | 收到数据或连接到达结束位置（EOF）时，此值设为 0；接收数据出错时小于 0，此时 `pkt` 参数设为 `NULL`。 |
| `user_data` | 调用 `net_recv()` 时提供的用户数据（User Data）。 |

<a id="gab3caccfe9fa1bc7ce0e4654192a5de93"></a>

### `net_context_send_cb_t`

```c
typedef void(* net_context_send_cb_t) (struct net_context *context, int status, void *user_data)
```

```c
#include <zephyr/net/net_context.h>
```

网络数据发送回调（Network Data Send Callback）。

发送回调（Send Callback）在网络数据包发送后调用。此回调由发送线程（TX Thread）调用，因此使用该线程的栈和执行上下文。应尽量减少回调中的处理，以缩短数据包处理被阻塞的时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的上下文（Context）。 |
| `status` | 值大于等于 0 时表示已发送的数据量；小于 0 时表示发送数据出错。 |
| `user_data` | 调用 `net_send()` 时提供的用户数据（User Data）。 |

<a id="gae3082af116955d4175c025a02b296c91"></a>

### `net_pkt_get_pool_func_t`

```c
typedef struct net_buf_pool *(* net_pkt_get_pool_func_t) (void)
```

```c
#include <zephyr/net/net_context.h>
```

用于获取 `net_buf` 分配所用缓冲池（Pool）的函数。

**返回（Returns）**：返回值：指向有效 `struct net_buf_pool` 实例的指针。

<a id="ga3bb4bbd522ede36213bafe86f2d1d770"></a>

### `net_pkt_get_slab_func_t`

```c
typedef struct k_mem_slab *(* net_pkt_get_slab_func_t) (void)
```

```c
#include <zephyr/net/net_context.h>
```

用于获取 `net_pkt` 分配所用内存块池（Slab）的函数。

**返回（Returns）**：返回值：指向有效 `struct k_mem_slab` 实例的指针。

<a id="gaf05114d2edc8b5fb485fd37f3d0821ba"></a>

### `net_tcp_accept_cb_t`

```c
typedef void(* net_tcp_accept_cb_t) (struct net_context *new_context, struct net_sockaddr *addr, net_socklen_t addrlen, int status, void *user_data)
```

```c
#include <zephyr/net/net_context.h>
```

接受连接回调（Accept Callback）。

接受连接回调（Accept Callback）在成功建立连接后调用，或在等待连接尝试期间出错时调用。此回调由接收线程（RX Thread）调用，因此使用该线程的栈和执行上下文。应尽量减少回调中的处理，以缩短数据包处理被阻塞的时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `new_context` | 要使用的上下文（Context）。 |
| `addr` | 对端地址（Peer Address）。 |
| `addrlen` | 对端地址（Peer Address）的长度。 |
| `status` | 状态码（Status Code），成功时为 0，否则小于 0。 |
| `user_data` | 调用 `net_context_accept()` 时提供的用户数据（User Data）。 |

<a id="gab03a354899ff68f6b9d127bc3bb5e17d"></a>

### `net_context_option`

```c
enum net_context_option
```

```c
#include <zephyr/net/net_context.h>
```

网络上下文选项（Network Context Options）。

这些值映射到 BSD 套接字选项（Socket Options）值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_OPT_PRIORITY` | 上下文优先级（Context Priority）。 |
| `NET_OPT_TXTIME` | 发送时间（TX Time）。 |
| `NET_OPT_SOCKS5` | SOCKS5 代理。 |
| `NET_OPT_RCVTIMEO` | 接收超时（Receive Timeout）。 |
| `NET_OPT_SNDTIMEO` | 发送超时（Send Timeout）。 |
| `NET_OPT_RCVBUF` | 接收缓冲区。 |
| `NET_OPT_SNDBUF` | 发送缓冲区（Send Buffer）。 |
| `NET_OPT_DSCP_ECN` | 区分服务代码点（DSCP）与显式拥塞通知（ECN）。 |
| `NET_OPT_REUSEADDR` | 地址复用（Re-use Address）。 |
| `NET_OPT_REUSEPORT` | 端口复用（Re-use Port）。 |
| `NET_OPT_IPV6_V6ONLY` | 共享 IPv4 和 IPv6 端口空间（Port Space）。 |
| `NET_OPT_RECV_PKTINFO` | 接收数据包信息（Packet Information）。 |
| `NET_OPT_MCAST_TTL` | IPv4组播生存时间（Multicast TTL）。 |
| `NET_OPT_MCAST_HOP_LIMIT` | IPv6组播跳数限制（Multicast Hop Limit）。 |
| `NET_OPT_UNICAST_HOP_LIMIT` | IPv6 单播跳数限制（Unicast Hop Limit）。 |
| `NET_OPT_TTL` | IPv4 单播生存时间（Unicast TTL）。 |
| `NET_OPT_ADDR_PREFERENCES` | IPv6 地址偏好（Address Preference）。 |
| `NET_OPT_TIMESTAMPING` | 数据包时间戳（Packet Timestamping）。 |
| `NET_OPT_MCAST_IFINDEX` | IPv6 组播输出网络接口索引（Multicast Output Network Interface Index）。 |
| `NET_OPT_MTU` | IPv4 套接字路径最大传输单元（Path MTU）。 |
| `NET_OPT_LOCAL_PORT_RANGE` | 限制本地端口范围（Clamp Local Port Range）。 |
| `NET_OPT_IPV6_MCAST_LOOP` | IPv6 组播环回（Multicast Loop）。 |
| `NET_OPT_IPV4_MCAST_LOOP` | IPv4 组播环回（Multicast Loop）。 |
| `NET_OPT_RECV_HOPLIMIT` | 接收跳数限制信息（Hop Limit Information）。 |
| `NET_OPT_DONT_FRAGMENT` | 禁用本地 IP 分片（IP Fragmentation）。 |
| `NET_OPT_LINGER` | 套接字延迟关闭（Socket Linger，`SO_LINGER`）。 |
| `NET_OPT_UDP_OPT` | UDP 选项总使能（Master Enable），参见 RFC 9868。 |
| `NET_OPT_UDP_OPT_OCS` | UDP 选项：选项校验和（Option Checksum）。 |
| `NET_OPT_UDP_OPT_APC` | UDP 选项：附加载荷校验和（Additional Payload Checksum）。 |
| `NET_OPT_UDP_OPT_FRAG` | UDP 选项：分片（Fragmentation）。 |
| `NET_OPT_UDP_OPT_MDS` | UDP 选项：最大数据报大小（Maximum Datagram Size）。 |
| `NET_OPT_UDP_OPT_MRDS` | UDP 选项：最大重组数据报大小（Maximum Reassembled Datagram Size）。 |
| `NET_OPT_UDP_OPT_REQ` | UDP 选项：回显请求（Echo Request）。 |
| `NET_OPT_UDP_OPT_RES` | UDP 选项：回显响应（Echo Response）。 |
| `NET_OPT_UDP_OPT_TIME` | UDP 选项：时间戳（Timestamp）。 |
| `NET_OPT_UDP_OPT_AUTH` | UDP 选项：认证（Authentication）。 |
| `NET_OPT_UDP_OPT_EXP` | UDP 选项：实验性选项（Experimental）。 |
| `NET_OPT_UDP_OPT_UCMP` | UDP 选项：UNSAFE 类压缩（Compression）。 |
| `NET_OPT_UDP_OPT_UENC` | UDP 选项：UNSAFE 类加密（Encryption）。 |
| `NET_OPT_UDP_OPT_UEXP` | UDP 选项：UNSAFE 类实验性选项（Experimental）。 |
| `NET_OPT_UDP_OPT_DPLPMTUD` | UDP 选项：使能数据报分包层路径 MTU 发现（Datagram Packetization Layer Path MTU Discovery，DPLPMTUD），参见 RFC 9869。 |
| `NET_OPT_UDP_OPT_DPLPMTUD_APP_RESPOND` | UDP 选项：由应用程序自行回显 RES。 |

<a id="ga1b056999d9ab8f2d3b3c0f4788f36cdd"></a>

### `net_context_accept()`

```c
int net_context_accept ( struct net_context * context, net_tcp_accept_cb_t cb, k_timeout_t timeout, void * user_data )
```

```c
#include <zephyr/net/net_context.h>
```

接受网络连接尝试（Network Connection Attempt）。

接受正在建立的连接（Connection）。超时设为 `K_NO_WAIT` 时立即返回；之后每当有连接与此上下文建立时，上下文都会调用提供的回调，这是“注册处理程序后无需继续等待”的异步（Asynchronous）调用。超时设为 `K_FOREVER` 时，函数等待连接建立；大于 0 时等待指定毫秒数。连接建立后调用调用者提供的回调。即使超时设为 `K_FOREVER`，仍会调用回调，且在本函数返回前调用。超时到期时不调用回调。此函数类似 BSD `accept()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的上下文（Context）。 |
| `cb` | 调用者提供的回调函数（Callback Function）。 |
| `timeout` | 连接超时（Timeout），可取 `K_FOREVER`、`K_NO_WAIT` 或大于 0 的值。 |
| `user_data` | 调用者提供的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga2023f160b4d2ebc05d665d119611ef25"></a>

### `net_context_bind()`

```c
int net_context_bind ( struct net_context * context, const struct net_sockaddr * addr, net_socklen_t addrlen )
```

```c
#include <zephyr/net/net_context.h>
```

为套接字（Socket）分配本地地址（Local Address）。

类似 BSD 的 `bind()` 函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要赋予地址的上下文（Context）。 |
| `addr` | 要赋予的地址（Address）。 |
| `addrlen` | 地址（Address）的长度。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga2f8fccd2453227706e313ac056f1c6ef"></a>

### `net_context_bind_iface()`

```c
void net_context_bind_iface ( struct net_context * context, struct net_if * iface )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

将网络接口（Network Interface）绑定到此上下文。

此函数将网络接口（Network Interface）绑定到此上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `iface` | 网络接口（Network Interface） |

<a id="gadf4ab08eb39803909e585b16ce68307a"></a>

### `net_context_connect()`

```c
int net_context_connect ( struct net_context * context, const struct net_sockaddr * addr, net_socklen_t addrlen, net_context_connect_cb_t cb, k_timeout_t timeout, void * user_data )
```

```c
#include <zephyr/net/net_context.h>
```

创建网络连接（Network Connection）。

`net_context_connect` 函数创建到 `addr` 指定主机的网络连接。连接建立后执行用户提供的回调 `cb`。即使超时设为 `K_FOREVER`，仍调用 `cb`；超时到期时不调用。对于数据报套接字（`NET_SOCK_DGRAM`），此函数只设置对端地址（Peer Address）。此函数类似 BSD 的 `connect()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `addr` | 要连接的对端地址（Peer Address）。 |
| `addrlen` | 对端地址长度（Peer Address Length）。 |
| `cb` | 回调函数（Callback Function），不需要时设为 `NULL`。 |
| `timeout` | 连接超时（Timeout）的可能值：`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示阻塞直到连接建立；大于 0 表示等待指定毫秒数。 |
| `user_data` | 传递给回调函数的数据（Data）。 |

**返回（Returns）**：返回值：成功时为 0；传入无效参数时为 `-EINVAL`；操作不受支持或未实现时为 `-ENOTSUP`；连接操作超时时为 `-ETIMEDOUT`。

<a id="gae3b3892b921e4694a18e7bacee63841d"></a>

### `net_context_create_ipv4_new()`

```c
int net_context_create_ipv4_new ( struct net_context * context, struct net_pkt * pkt, const struct net_in_addr * src, const struct net_in_addr * dst )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

根据上下文，在提供的 `net_pkt` 中创建 IPv4 数据包（IPv4 Packet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 连接的网络上下文（Network Context）。 |
| `pkt` | 网络数据包（Network Packet）。 |
| `src` | 源地址（Source Address）；为 `NULL` 时选择默认地址。 |
| `dst` | 目的 IPv4 地址（Destination IPv4 address）。 |

**返回（Returns）**：返回值：成功时为 0，否则为负 `errno`。

<a id="gaa973878eb7f6bf69d91da992edad6409"></a>

### `net_context_create_ipv6_new()`

```c
int net_context_create_ipv6_new ( struct net_context * context, struct net_pkt * pkt, const struct net_in6_addr * src, const struct net_in6_addr * dst )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

根据上下文，在提供的 `net_pkt` 中创建 IPv6 数据包（IPv6 Packet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 连接的网络上下文（Network Context）。 |
| `pkt` | 网络数据包（Network Packet）。 |
| `src` | 源地址（Source Address）；为 `NULL` 时从上下文中选择默认地址。 |
| `dst` | 目的 IPv6 地址（Destination IPv6 address）。 |

**返回（Returns）**：返回值：成功时为 0，否则为负 `errno`。

<a id="gabb751f7d213d00f8eec72a67f4ce3491"></a>

### `net_context_foreach()`

```c
void net_context_foreach ( net_context_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/net_context.h>
```

遍历全部网络连接，并为每个网络上下文（Network Context）调用回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="ga37fbf84456a4142330d74eed1f3c24f6"></a>

### `net_context_get()`

```c
int net_context_get ( net_sa_family_t family, enum net_sock_type type, uint16_t ip_proto, struct net_context ** context )
```

```c
#include <zephyr/net/net_context.h>
```

获取网络上下文（Network Context）。

网络上下文（Network Context）用于定义连接五元组（5-tuple）：协议、远端地址、远端端口、源地址和源端口。创建上下文时，为源端口分配随机空闲端口号。此函数类似 BSD 的 `socket()`。创建的上下文引用计数（Reference Count）为 1。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `family` | IP 地址族（Address Family），为 `NET_AF_INET` 或 `NET_AF_INET6`。 |
| `type` | 套接字类型（Socket Type），为 `NET_SOCK_STREAM` 或 `NET_SOCK_DGRAM`。 |
| `ip_proto` | IP 协议，为 `NET_IPPROTO_UDP` 或 `NET_IPPROTO_TCP`。对于原始套接字访问（Raw Socket Access），此值为 IEEE 802.3 的二层协议值，参见 `ethernet.h`。 |
| `context` | 将分配的上下文（Context）返回给调用者。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga7f4d732a99cb9e86fcd5226fbbb727f4"></a>

### `net_context_get_can_filter_id()`

```c
int net_context_get_can_filter_id ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此网络上下文的 CAN 过滤器标识符（CAN Filter ID）。

此函数获取上下文的 CAN 筛选器 ID（Filter ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：此网络上下文的筛选器 ID（Filter ID）。

<a id="ga4c3de0a3b7f27dd8ac9d0f415710faad"></a>

### `net_context_get_family()`

```c
net_sa_family_t net_context_get_family ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此网络上下文的地址族（Address Family）。

此函数返回上下文的地址族（Address Family），即 IPv4 或 IPv6。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：网络地址族（Network Address Family）。

<a id="gafe6b8c9af4464cd471285817d6d61087"></a>

### `net_context_get_iface()`

```c
struct net_if * net_context_get_iface ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此上下文的网络接口（Network Interface）。

此函数返回所使用的网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：上下文已绑定接口时，返回其网络接口（Network Interface）；否则为 `NULL`。

<a id="ga3db832f40b6a0b975a282ef354a7bffc"></a>

### `net_context_get_ipv4_mcast_ttl()`

```c
uint8_t net_context_get_ipv4_mcast_ttl ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此上下文的 IPv4 组播生存时间值（Multicast TTL）。

此函数返回此上下文设置的 IPv4 组播生存时间（Multicast Time-to-live，TTL）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：IPv4 组播生存时间（Multicast TTL）值。

<a id="ga9cdb3e5849a5b2663e0a38ac2a39a427"></a>

### `net_context_get_ipv4_ttl()`

```c
uint8_t net_context_get_ipv4_ttl ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此上下文的 IPv4 生存时间值（Time-to-live，TTL）。

此函数返回此上下文设置的 IPv4 生存时间（Time-to-live，TTL）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：IPv4 生存时间（TTL）值。

<a id="ga977b08a77586e0e4752bff725139427c"></a>

### `net_context_get_ipv6_hop_limit()`

```c
uint8_t net_context_get_ipv6_hop_limit ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此上下文的 IPv6 跳数限制值（Hop Limit）。

此函数返回此上下文设置的 IPv6 跳数限制（Hop Limit）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：IPv6 跳数限制（Hop Limit）值。

<a id="ga99b5f0ded5d56b735e051ede5651f435"></a>

### `net_context_get_ipv6_mcast_hop_limit()`

```c
uint8_t net_context_get_ipv6_mcast_hop_limit ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此上下文的 IPv6 组播跳数限制值（Multicast Hop Limit）。

此函数返回此上下文设置的 IPv6 组播跳数限制（Multicast Hop Limit）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：IPv6 组播跳数限制（Multicast Hop Limit）值。

<a id="gabbb9472c54b2fbe0b519dcb68e02a44e"></a>

### `net_context_get_option()`

```c
int net_context_get_option ( struct net_context * context, enum net_context_option option, void * value, uint32_t * len )
```

```c
#include <zephyr/net/net_context.h>
```

获取此上下文的连接选项值（Connection Option Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的网络上下文（Network Context）。 |
| `option` | 要设置的选项（Option）。 |
| `value` | 选项值（Option Value） |
| `len` | 选项长度（Option Length），返回给调用者。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gadf41291ca5be067e830d121000ca3f51"></a>

### `net_context_get_proto()`

```c
uint16_t net_context_get_proto ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此网络上下文的 IP 协议（IP Protocol）。

此函数返回上下文的 IP 协议，即 UDP、TCP 或 IEEE 802.3 协议值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：网络上下文的 IP 协议。

<a id="ga53bd5f35a142f1d43f90d3bde99778e0"></a>

### `net_context_get_state()`

```c
enum net_context_state net_context_get_state ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此网络上下文的状态（State）。

此函数返回上下文状态（Context State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：网络状态（Network State）。

<a id="ga24b4d99dddc4fabf383f5d8079650337"></a>

### `net_context_get_type()`

```c
enum net_sock_type net_context_get_type ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

获取此网络上下文的上下文类型（Context Type）。

此函数返回上下文类型（Context Type），即流式（Stream）、数据报（Datagram）或原始（Raw）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：网络上下文类型（Network Context Type）。

<a id="ga2f6d614158c999fa68e518393c0a9c35"></a>

### `net_context_is_bound_to_iface()`

```c
bool net_context_is_bound_to_iface ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

此上下文是否已绑定到网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：上下文已绑定网络接口（Network Interface）时为 `true`，否则为 `false`。

<a id="ga8e93032d6b65d9b5dfc0f64ecdf3a6b5"></a>

### `net_context_is_local_addr_set()`

```c
bool net_context_is_local_addr_set ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

是否已有本地地址（Local Address）绑定到此上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：已向 `net_context::local` 赋予本地地址（Local Address）时为 `true`，否则为 `false`。

<a id="ga5c3a841ff54ddb53cedcccefde5a7d7a"></a>

### `net_context_is_proxy_enabled()`

```c
bool net_context_is_proxy_enabled ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

此上下文的 SOCKS 代理支持（SOCKS Proxy Support）是启用还是禁用。

此函数返回此上下文当前的 SOCKS 代理状态（Proxy Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：此上下文启用了 SOCKS 代理（Proxy）时为 `true`，否则为 `false`。

<a id="ga423103d5c386b602737e23ee81f2a961"></a>

### `net_context_is_used()`

```c
bool net_context_is_used ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

此上下文（Context）是否正在使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |

**返回（Returns）**：返回值：上下文当前正在使用（In Use）时为 `true`，否则为 `false`。

<a id="ga3803c0d738fbb9d786f401aacc10a4d3"></a>

### `net_context_listen()`

```c
int net_context_listen ( struct net_context * context, int backlog )
```

```c
#include <zephyr/net/net_context.h>
```

将上下文标记为监听状态（Listening）。

类似 BSD 的 `listen()` 函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的上下文（Context）。 |
| `backlog` | 待处理连接积压队列（Pending Connections Backlog）的大小。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="gad9350d40a884315ff9de4032a8d6ae71"></a>

### `net_context_port_in_use()`

```c
bool net_context_port_in_use ( enum net_ip_protocol ip_proto, uint16_t local_port, const struct net_sockaddr * local_addr )
```

```c
#include <zephyr/net/net_context.h>
```

检查端口是否正在使用，即是否已绑定（Bound）。

此函数根据指定的 `ip_proto` 和 `local_addr` 检查端口（Port）是否已绑定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ip_proto` | IP 协议。 |
| `local_port` | 要检查的端口（Port）。 |
| `local_addr` | 网络地址（Network Address）。 |

**返回（Returns）**：返回值：端口已绑定（Bound）时为 `true`，未绑定时为 `false`。

<a id="ga1d6b64e302c546db589c661f4b6bda98"></a>

### `net_context_put()`

```c
int net_context_put ( struct net_context * context)
```

```c
#include <zephyr/net/net_context.h>
```

关闭网络上下文（Network Context），并释放其引用（Unref）。

释放此上下文（Context）。调用后不能再通过它发送或接收数据。此函数类似 BSD 的 `shutdown()`。为了兼容旧行为，此函数会隐式递减引用计数（Reference Count），并可能立即销毁上下文，或在其到达最终状态时销毁。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要关闭的上下文（Context）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga74f919185f8af074c2d90aa04733dd2a"></a>

### `net_context_recv()`

```c
int net_context_recv ( struct net_context * context, net_context_recv_cb_t cb, k_timeout_t timeout, void * user_data )
```

```c
#include <zephyr/net/net_context.h>
```

从上下文指定的对端（Peer）接收网络数据。

此函数用于注册回调，使网络协议栈在收到属于此上下文的网络数据时调用它。因为它执行的是回调注册，所以超时设为 `K_NO_WAIT` 时，无需反复调用；只有回调函数或用户数据变化时，才需要再次调用以注册新值。超时为 `K_NO_WAIT` 时立即返回，为 `K_FOREVER` 时等待收到网络缓冲区，大于 0 时等待指定毫秒数。收到网络缓冲区后调用调用者提供的回调；即使超时为 `K_FOREVER` 也会调用，且在本函数返回前调用。超时到期时不调用回调。如果不需要同步行为（Synchronous Behavior），可以在编译时去掉超时功能；同步调用逻辑需要一些内存，仅使用异步调用可节省这部分内存。未设置 `CONFIG_NET_CONTEXT_SYNC_RECV` 时，忽略 `timeout` 参数值。此函数类似 BSD 的 `recv()`。注意：应在 `net_context_recv()` 之前调用 `net_context_bind()`。默认给本地端口分配随机端口号；只有 `bind()` 会根据上下文更新连接信息。如果先调用 `recv()` 再调用 `bind()`，可能因上下文已关联连接而拒绝绑定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的网络上下文（Network Context）。 |
| `cb` | 调用者提供的回调函数（Callback Function）。 |
| `timeout` | 调用者提供的超时（Timeout），可取 `K_FOREVER`、`K_NO_WAIT` 或大于 0 的值。 |
| `user_data` | 调用者提供的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga4c0ef9540a0d7e800c4529274f5c22f4"></a>

### `net_context_ref()`

```c
int net_context_ref ( struct net_context * context)
```

```c
#include <zephyr/net/net_context.h>
```

获取一个 `net_context` 引用，增加引用计数（Reference Count），以防止该上下文被销毁。

网络上下文（Network Context）只有在引用计数（Reference Count）降至零时才会被回收。注意：这不会阻止错误或 `net_context_put` 导致的任何“关闭”行为，只是防止上下文被回收并用于其他用途。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要增加引用计数（Reference Count）的上下文。 |

**返回（Returns）**：返回值：新的引用计数（Reference Count）。

<a id="gac793e1def18200416e3f679067c56ab3"></a>

### `net_context_send()`

```c
int net_context_send ( struct net_context * context, const void * buf, size_t len, net_context_send_cb_t cb, k_timeout_t timeout, void * user_data )
```

```c
#include <zephyr/net/net_context.h>
```

向对端（Peer）发送数据。

此函数用于向对端连接发送网络数据。网络缓冲区发送后，调用调用者提供的回调；注意，回调可能在本函数返回后才调用。对于 `NET_SOCK_DGRAM` 类型的上下文，必须已通过 `net_context_connect()` 设置目标地址。此函数类似 BSD 的 `send()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的网络上下文（Network Context）。 |
| `buf` | 要发送的数据缓冲区（Data Buffer）。 |
| `len` | 缓冲区（Buffer）的长度。 |
| `cb` | 调用者提供的回调函数（Callback Function）。 |
| `timeout` | 目前不使用此值。 |
| `user_data` | 调用者提供的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="gaf915131b95b159e299f034768cefdaea"></a>

### `net_context_sendmsg()`

```c
int net_context_sendmsg ( struct net_context * context, const struct net_msghdr * msghdr, int flags, net_context_send_cb_t cb, k_timeout_t timeout, void * user_data )
```

```c
#include <zephyr/net/net_context.h>
```

将 `iovec` 中的数据发送给 `net_msghdr` 结构体指定的对端（Peer）。

此函数的语义类似 POSIX 的 `sendmsg()`。对于未连接套接字（Unconnected Socket），必须设置 `net_msghdr` 中的 `msg_name` 字段；对于已连接套接字，应将 `msg_name` 设为 `NULL`，将 `msg_namelen` 设为 0。对于 UDP 套接字，`msg_control` 还可携带每个数据报的辅助数据（Ancillary Data），例如 `ZSOCK_IP_DONTFRAG` 或 `ZSOCK_IPV6_DONTFRAG`。网络缓冲区发送后，调用调用者提供的回调；注意，回调可能在本函数返回后才调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的网络上下文（Network Context）。 |
| `msghdr` | 要发送的数据（Data）。 |
| `flags` | 发送标志（Sending Flags）。 |
| `cb` | 调用者提供的回调函数（Callback Function）。 |
| `timeout` | 目前不使用此值。 |
| `user_data` | 调用者提供的用户数据（User Data）。 |

**返回（Returns）**：返回值：成功时为发送的字节数，否则为负 `errno`。

<a id="gafd68de53778cbd807d0e45209a83df05"></a>

### `net_context_sendto()`

```c
int net_context_sendto ( struct net_context * context, const void * buf, size_t len, const struct net_sockaddr * dst_addr, net_socklen_t addrlen, net_context_send_cb_t cb, k_timeout_t timeout, void * user_data )
```

```c
#include <zephyr/net/net_context.h>
```

向地址指定的对端（Peer）发送数据。

此函数用于向地址指定的对端发送网络数据。此变体仅用于 `NET_SOCK_DGRAM` 类型的数据报连接。网络缓冲区发送后，调用调用者提供的回调；注意，回调可能在本函数返回后才调用。此函数类似 BSD 的 `sendto()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的网络上下文（Network Context）。 |
| `buf` | 要发送的数据缓冲区（Data Buffer）。 |
| `len` | 缓冲区（Buffer）的长度。 |
| `dst_addr` | 目的地址（Destination Address）。 |
| `addrlen` | 地址（Address）的长度。 |
| `cb` | 调用者提供的回调函数（Callback Function）。 |
| `timeout` | 发送尝试的超时时间（Timeout）。 |
| `user_data` | 调用者提供的用户数据（User Data）。 |

**返回（Returns）**：返回值：成功时为发送的字节数，否则为负 `errno`。

<a id="ga581582c0461b36088d21d0fd433cc284"></a>

### `net_context_set_can_filter_id()`

```c
void net_context_set_can_filter_id ( struct net_context * context, int filter_id )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此网络上下文的 CAN 过滤器标识符（CAN Filter ID）。

此函数设置上下文的 CAN 筛选器 ID（Filter ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `filter_id` | CAN 筛选器 ID（Filter ID）。 |

<a id="ga37bbecc848430590d5d68d2880c83c1e"></a>

### `net_context_set_family()`

```c
void net_context_set_family ( struct net_context * context, net_sa_family_t family )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此网络上下文的地址族（Address Family）。

此函数设置上下文的地址族（Address Family），即 IPv4、IPv6 或 `AF_PACKET`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `family` | 地址族（Address Family）：`NET_AF_INET`、`NET_AF_INET6`、`NET_AF_PACKET` 或 `NET_AF_CAN`。 |

<a id="ga10399e3f3d159de9325ac7632ce25c51"></a>

### `net_context_set_iface()`

```c
void net_context_set_iface ( struct net_context * context, struct net_if * iface )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此上下文的网络接口（Network Interface）。

此函数将网络接口（Network Interface）绑定到此上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `iface` | 网络接口（Network Interface） |

<a id="gab2a2064fa33613a60ad40597d0971774"></a>

### `net_context_set_ipv4_mcast_ttl()`

```c
void net_context_set_ipv4_mcast_ttl ( struct net_context * context, uint8_t ttl )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此上下文的 IPv4 组播生存时间值（Multicast TTL）。

此函数设置此上下文的 IPv4 组播生存时间（Multicast Time-to-live，TTL）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `ttl` | IPv4 组播生存时间（Multicast Time-to-live）值。 |

<a id="ga11672ca3ebdae63b0013ad76959304d5"></a>

### `net_context_set_ipv4_ttl()`

```c
void net_context_set_ipv4_ttl ( struct net_context * context, uint8_t ttl )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此上下文的 IPv4 生存时间值（Time-to-live，TTL）。

此函数设置此上下文的 IPv4 生存时间（Time-to-live，TTL）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `ttl` | IPv4 生存时间（Time-to-live）值。 |

<a id="ga0cbf8377e7757881033aab3e718b1a61"></a>

### `net_context_set_ipv6_hop_limit()`

```c
void net_context_set_ipv6_hop_limit ( struct net_context * context, uint8_t hop_limit )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此上下文的 IPv6 跳数限制值（Hop Limit）。

此函数设置此上下文的 IPv6 跳数限制（Hop Limit）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `hop_limit` | IPv6 跳数限制（Hop Limit）值。 |

<a id="gaf29d5ee244c552d78171938a903fbaca"></a>

### `net_context_set_ipv6_mcast_hop_limit()`

```c
void net_context_set_ipv6_mcast_hop_limit ( struct net_context * context, uint8_t hop_limit )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此上下文的 IPv6 组播跳数限制值（Multicast Hop Limit）。

此函数设置此上下文的 IPv6 组播跳数限制（Multicast Hop Limit）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `hop_limit` | IPv6 组播跳数限制（Multicast Hop Limit）值。 |

<a id="ga40c6ef5b1f8b846e5b205947e87ce585"></a>

### `net_context_set_option()`

```c
int net_context_set_option ( struct net_context * context, enum net_context_option option, const void * value, uint32_t len )
```

```c
#include <zephyr/net/net_context.h>
```

设置此上下文的连接选项（Connection Option）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的网络上下文（Network Context）。 |
| `option` | 要设置的选项（Option）。 |
| `value` | 选项值（Option Value） |
| `len` | 选项长度（Option Length）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gadcd0049229580244ea89fbc98bf23a81"></a>

### `net_context_set_proto()`

```c
void net_context_set_proto ( struct net_context * context, uint16_t proto )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此网络上下文的 IP 协议（IP Protocol）。

此函数设置上下文的 IP 协议（UDP／TCP）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `proto` | 上下文 IP 协议，为 `NET_IPPROTO_UDP`、`NET_IPPROTO_TCP` 或 IEEE 802.3 协议值。 |

<a id="ga9bd6b5e9429b6e845d41f6cbf242c092"></a>

### `net_context_set_proxy_enabled()`

```c
void net_context_set_proxy_enabled ( struct net_context * context, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

为此上下文启用或禁用 SOCKS 代理支持（SOCKS Proxy Support）。

此函数使能或禁用此上下文的 SOCKS 代理支持（Proxy Support）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `enable` | 使能或禁用 SOCKS 代理（Proxy）。 |

<a id="gaac934209341db606a4d563b3c48cce45"></a>

### `net_context_set_state()`

```c
void net_context_set_state ( struct net_context * context, enum net_context_state state )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此网络上下文的状态（State）。

此函数设置上下文状态（Context State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `state` | 新的网络上下文状态（Network Context State）。 |

<a id="ga01c11c1dfce101df046df9ade00ed277"></a>

### `net_context_set_type()`

```c
void net_context_set_type ( struct net_context * context, enum net_sock_type type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

设置此网络上下文的上下文类型（Context Type）。

此函数设置上下文类型（Context Type），即流式（Stream）或数据报（Datagram）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context）。 |
| `type` | 上下文类型（Context Type），为 `NET_SOCK_STREAM` 或 `NET_SOCK_DGRAM`。 |

<a id="gaefead18501a966af4a7f71eb23ac17c7"></a>

### `net_context_set_udp_dplpmtud()`

```c
int net_context_set_udp_dplpmtud ( struct net_context * context, bool enable )
```

```c
#include <zephyr/net/net_context.h>
```

在 UDP 上下文上启用或禁用数据报分组层路径 MTU 发现（DPLPMTUD，RFC 9869）。

启用时，协议栈使用 UDP 选项探测路径最大传输单元（Path MTU），并响应收到的探测请求。必须使用 UDP 上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 网络上下文（Network Context），协议必须为 UDP。 |
| `enable` | `true` 表示使能数据报分包层路径 MTU 发现（DPLPMTUD），`false` 表示禁用。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga11801119ad1d62db0302479c133adb35"></a>

### `net_context_signal_linger()`

```c
void net_context_signal_linger ( struct net_context * context)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_context.h>
```

通知此上下文的底层连接已由传输层（Transport）关闭，使因 `SO_LINGER` 而阻塞的 `close()` 能够继续执行。

<a id="ga0d391690d9d6972ce6f4baedeab64b11"></a>

### `net_context_unref()`

```c
int net_context_unref ( struct net_context * context)
```

```c
#include <zephyr/net/net_context.h>
```

减少网络上下文（Network Context）的引用计数（Reference Count）。

递减引用计数（Reference Count）。降至零时回收上下文。注意：这不会引起任何网络可见的“关闭”行为，例如使此连接之后收到的数据包得到 TCP RST 或 ICMP 端口不可达响应。需要此类行为时，参见 `net_context_put()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要递减引用计数（Reference Count）的上下文。 |

**返回（Returns）**：返回值：新的引用计数（Reference Count）；上下文已销毁时为 0。

<a id="gab3cc2a13e24f9c263bc40cc87d752a9f"></a>

### `net_context_update_recv_wnd()`

```c
int net_context_update_recv_wnd ( struct net_context * context, int32_t delta )
```

```c
#include <zephyr/net/net_context.h>
```

更新此上下文的 TCP 接收窗口（TCP Receive Window）。

如果应用程序没有在接收回调中完全处理收到的数据，而是将其排队等，应使用此函数。在这种情况下，接收回调应按已排队数据的大小缩小接收窗口（Receive Window），即传入负值；将数据出队的函数则应传入与出队数据大小对应的正值。例如，接收回调收到含 256 字节数据的数据包并将其排队时，应以 `delta = -256` 调用此函数；如果另一个函数从已排队数据中取出 10 字节，则应以 `delta = 10` 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 要使用的 TCP 网络上下文（Network Context）。 |
| `delta` | TCP 接收窗口（Receive Window）的增量，单位为字节；负值表示减小窗口。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。


## 5.7\_原页交叉引用（Cross References）

- [net_context](../network_core_model_reference/P055_net_context_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga361fe60d9b96001f74363788352858a0)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_sa_family_t](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga8b4cfadf1b284e52d6905ca88657b48a)
- [net_sock_type](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gaaab4268707dbe08348b98fb028e7aa5c)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [RFC 9869](https://datatracker.ietf.org/doc/html/rfc9869)
- [net_ip_protocol](P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gaf06819bf427cc58be1229b27b373ca31)
- [zephyr/net/net_context.h](../api_file_network_pcie_reference/P008_zephyr__net__net_context.h_文件参考.md)
- [RFC 9868](https://datatracker.ietf.org/doc/html/rfc9868)
- [accept()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)
- [bind()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a05b4e957a092db3e68281988ceb32df8)
- [connect()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)
- [socket()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a4dcc080bfb18d95d173bc205084f8b0a)
- [ethernet.h](../api_file_usb_network_reference/P008_zephyr__net__ethernet.h_文件参考.md)
- [net_context::local](../network_core_model_reference/P055_net_context_结构体.md#a899af7c9b63a2da0ec43646f2d40a146)
- [listen()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a7005ffbeeff92be5394ff3244da79028)
- [shutdown()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a8dadddc96fee56a9f8b0904aca02eab2)
- [recv()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)
- [send()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)
- [sendmsg()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a8a2ad4261d3978ba299926f45d56ed74)
- [ZSOCK_IP_DONTFRAG](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga3c8f7f8895a3daae11dcd439eb2499a3)
- [ZSOCK_IPV6_DONTFRAG](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga44b16e54bc2922153e9a07d628cf1cba)
- [sendto()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#ac223969ed767c313123d06547db45ff8)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da98136d42db895cf6f3e35ee418e0b7eb"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dad6b8627398a90dd622f433e8b3fee3a3"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da469d1d21e088eba6f96ec0a679636ba7"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dab1615ef9a3bf84daf964a445476bc04c"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da38adf4f5e3fba71f152a05c208e6f9f0"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da3f5fea1c10f55d4db1d72bba2959445e"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dad5099786ebcdc0198cf3cd1db465387d"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dae0ed5497e4d356ca2bdea0a120dcb6ee"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dacd227331833af7fb92b84f3ceb80f3ab"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da9dec13665201fdc9be87490cde2f3253"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da69e538d1b4732c865384340989f011c8"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da9db3637a09382655835493aed186a549"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da104d851b3c8884c875dbbc9d1e6c64ae"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da12c660c9ee2dd9d9d2de36980949aa9f"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da6441103cc8e0e3cf724d2ea79cf18dcb"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dae72a8a6e3f4a7a14370cd1267820c71d"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da61c105080d36bca8b4405527af4aaac4"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dab4dd4a3acee76f82c37fd16fd5f53867"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17daa3a443af92a7bc45aa9cc81ca4a1de0c"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da98f7a13028a2deb6eee31f1bad7c20b7"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17dae95fc08de9277a59c42d6bf6355ec201"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da885dadd317c676c4d9be316df29ff276"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17da4c24ea3a7cafcd9eddfc15a5725d75d2"></a>
<a id="ggab03a354899ff68f6b9d127bc3bb5e17daf50b6d1ab2da2df3b2ba1f991fc8011e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_MAX2221X 其他功能（MISC）.md) · [返回大纲](大纲.md) · [下一章](P006_工作队列 API（Work Queue APIs）.md)
