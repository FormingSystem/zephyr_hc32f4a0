---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-8
title: zephyr__net__net_context.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_net\_\_net\_context.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络上下文定义（Network Context Definitions）。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_stats.h>
#include <zephyr/net/dplpmtud.h>
```

查看此文件的源码。

网络上下文定义（Network Context Definitions）。供应用定义网络连接（Network Connection）的 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_net_5Fcontext"></a>

```c
struct net_context
```

相关声明：[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

注意，上下文中不保存实际源IP地址，因为该地址已在网络接口结构（Network Interface Struct）中设置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_ga5e2f5fcc08863a4090bc04040ee88d29"></a>

```c
#define NET_CONTEXT_IN_USE BIT(0)
```

相关声明：[NET_CONTEXT_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga5e2f5fcc08863a4090bc04040ee88d29)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此上下文（Context）是否正在使用。

<a id="r_gac8f6e3a16d52e8e376c38eec0ed8a940"></a>

```c
#define NET_CONTEXT_FAMILY (BIT(3) | BIT(4) | BIT(5))
```

相关声明：[NET_CONTEXT_FAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gac8f6e3a16d52e8e376c38eec0ed8a940)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

地址族（Address Family）、连接类型（Connection Type）和 IP 协议（IP Protocol）存储在位字段（Bit Field）中，以节省空间。

<a id="r_gac9b4cf9beecaac5bf05db3111c803678"></a>

```c
#define NET_CONTEXT_TYPE (BIT(6) | BIT(7))
```

相关声明：[NET_CONTEXT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gac9b4cf9beecaac5bf05db3111c803678)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

连接类型（Connection Type）：数据报（Datagram）、流（Stream）或原始类型（Raw）。

<a id="r_ga84206421e8f2e1eb114d393f0c81428b"></a>

```c
#define NET_CONTEXT_REMOTE_ADDR_SET BIT(8)
```

相关声明：[NET_CONTEXT_REMOTE_ADDR_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga84206421e8f2e1eb114d393f0c81428b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

远端地址已设置（Remote Address Set）。

<a id="r_gaa337bccec2c1df42540f236bb33a70e1"></a>

```c
#define NET_CONTEXT_BOUND_TO_IFACE BIT(9)
```

相关声明：[NET_CONTEXT_BOUND_TO_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa337bccec2c1df42540f236bb33a70e1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

上下文已绑定到特定接口（Specific Interface）。

<a id="r_ga717b1aaa11d589bfe929d98be5be19ed"></a>

```c
#define NET_CONTEXT_LOCAL_ADDR_SET BIT(10)
```

相关声明：[NET_CONTEXT_LOCAL_ADDR_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga717b1aaa11d589bfe929d98be5be19ed)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

本地地址（Local Address）已绑定到此上下文。

<a id="r_ga41d258362d6a7a703bc0b65d08e2b4c4"></a>

```c
#define net_context_setup_pools(context, tx_slab, data_pool)
```

相关声明：[net_context_setup_pools](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga41d258362d6a7a703bc0b65d08e2b4c4)。

为上下文发送操作设置自定义网络缓冲池（Custom Network Buffer Pools）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.3\_类型定义（Typedefs）

<a id="r_gafa485a6fae8237dd7e6856f4567b2317"></a>

```c
typedef void(* net_context_recv_cb_t) (struct net_context *context, struct net_pkt *pkt, union net_ip_header *ip_hdr, union net_proto_header *proto_hdr, int status, void *user_data)
```

相关声明：[net_context_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafa485a6fae8237dd7e6856f4567b2317)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

网络数据接收回调（Network Data Receive Callback）。

<a id="r_gab3caccfe9fa1bc7ce0e4654192a5de93"></a>

```c
typedef void(* net_context_send_cb_t) (struct net_context *context, int status, void *user_data)
```

相关声明：[net_context_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3caccfe9fa1bc7ce0e4654192a5de93)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

网络数据发送回调（Network Data Send Callback）。

<a id="r_gaf05114d2edc8b5fb485fd37f3d0821ba"></a>

```c
typedef void(* net_tcp_accept_cb_t) (struct net_context *new_context, struct net_sockaddr *addr, net_socklen_t addrlen, int status, void *user_data)
```

相关声明：[net_tcp_accept_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf05114d2edc8b5fb485fd37f3d0821ba)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

接受连接回调（Accept Callback）。

<a id="r_ga120ae8d4ff788ab21b19c11ed1738a71"></a>

```c
typedef void(* net_context_connect_cb_t) (struct net_context *context, int status, void *user_data)
```

相关声明：[net_context_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga120ae8d4ff788ab21b19c11ed1738a71)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

连接回调（Connection Callback）。

<a id="r_ga3bb4bbd522ede36213bafe86f2d1d770"></a>

```c
typedef struct k_mem_slab *(* net_pkt_get_slab_func_t) (void)
```

相关声明：[net_pkt_get_slab_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga3bb4bbd522ede36213bafe86f2d1d770)。

用于获取 `net_pkt` 分配所用内存块池（Slab）的函数。

<a id="r_gae3082af116955d4175c025a02b296c91"></a>

```c
typedef struct net_buf_pool *(* net_pkt_get_pool_func_t) (void)
```

相关声明：[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[net_pkt_get_pool_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gae3082af116955d4175c025a02b296c91)。

用于获取 `net_buf` 分配所用缓冲池（Pool）的函数。

<a id="r_gaa82d80fa18693b98dc363c35104075ba"></a>

```c
typedef void(* net_context_cb_t) (struct net_context *context, void *user_data)
```

相关声明：[net_context_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa82d80fa18693b98dc363c35104075ba)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

遍历网络上下文（Network Context）时使用的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.4\_枚举（Enumerations）

<a id="r_gab03a354899ff68f6b9d127bc3bb5e17d"></a>

```c
enum net_context_option { NET_OPT_PRIORITY = 1 , NET_OPT_TXTIME = 2 , NET_OPT_SOCKS5 = 3 , NET_OPT_RCVTIMEO = 4 , NET_OPT_SNDTIMEO = 5 , NET_OPT_RCVBUF = 6 , NET_OPT_SNDBUF = 7 , NET_OPT_DSCP_ECN = 8 , NET_OPT_REUSEADDR = 9 , NET_OPT_REUSEPORT = 10 , NET_OPT_IPV6_V6ONLY = 11 , NET_OPT_RECV_PKTINFO = 12 , NET_OPT_MCAST_TTL = 13 , NET_OPT_MCAST_HOP_LIMIT = 14 , NET_OPT_UNICAST_HOP_LIMIT = 15 , NET_OPT_TTL = 16 , NET_OPT_ADDR_PREFERENCES = 17 , NET_OPT_TIMESTAMPING = 18 , NET_OPT_MCAST_IFINDEX = 19 , NET_OPT_MTU = 20 , NET_OPT_LOCAL_PORT_RANGE = 21 , NET_OPT_IPV6_MCAST_LOOP = 22 , NET_OPT_IPV4_MCAST_LOOP = 23 , NET_OPT_RECV_HOPLIMIT = 24 , NET_OPT_DONT_FRAGMENT = 25 , NET_OPT_LINGER = 26 , NET_OPT_UDP_OPT = 27 , NET_OPT_UDP_OPT_OCS = 28 , NET_OPT_UDP_OPT_APC = 29 , NET_OPT_UDP_OPT_FRAG = 30 , NET_OPT_UDP_OPT_MDS = 31 , NET_OPT_UDP_OPT_MRDS = 32 , NET_OPT_UDP_OPT_REQ = 33 , NET_OPT_UDP_OPT_RES = 34 , NET_OPT_UDP_OPT_TIME = 35 , NET_OPT_UDP_OPT_AUTH = 36 , NET_OPT_UDP_OPT_EXP = 37 , NET_OPT_UDP_OPT_UCMP = 38 , NET_OPT_UDP_OPT_UENC = 39 , NET_OPT_UDP_OPT_UEXP = 40 , NET_OPT_UDP_OPT_DPLPMTUD = 41 , NET_OPT_UDP_OPT_DPLPMTUD_APP_RESPOND = 42 }
```

相关声明：[net_context_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab03a354899ff68f6b9d127bc3bb5e17d)、[NET_OPT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c)、[NET_OPT_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184)、[NET_OPT_SOCKS5](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c)、[NET_OPT_RCVTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076)、[NET_OPT_SNDTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668)、[NET_OPT_RCVBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1)、[NET_OPT_SNDBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08)、[NET_OPT_DSCP_ECN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c)、[NET_OPT_REUSEADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561)、[NET_OPT_REUSEPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4)、[NET_OPT_IPV6_V6ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c)、[NET_OPT_RECV_PKTINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a)、[NET_OPT_MCAST_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e)、[NET_OPT_MCAST_HOP_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d)、[NET_OPT_UNICAST_HOP_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3)、[NET_OPT_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184)、[NET_OPT_ADDR_PREFERENCES](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d)、[NET_OPT_TIMESTAMPING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2)、[NET_OPT_MCAST_IFINDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da98136d42db895cf6f3e35ee418e0b7eb)、[NET_OPT_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dad6b8627398a90dd622f433e8b3fee3a3)、[NET_OPT_LOCAL_PORT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da469d1d21e088eba6f96ec0a679636ba7)、[NET_OPT_IPV6_MCAST_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dab1615ef9a3bf84daf964a445476bc04c)、[NET_OPT_IPV4_MCAST_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da38adf4f5e3fba71f152a05c208e6f9f0)、[NET_OPT_RECV_HOPLIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da3f5fea1c10f55d4db1d72bba2959445e)、[NET_OPT_DONT_FRAGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dad5099786ebcdc0198cf3cd1db465387d)、[NET_OPT_LINGER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae0ed5497e4d356ca2bdea0a120dcb6ee)、[NET_OPT_UDP_OPT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dacd227331833af7fb92b84f3ceb80f3ab)、[NET_OPT_UDP_OPT_OCS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da9dec13665201fdc9be87490cde2f3253)、[NET_OPT_UDP_OPT_APC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da69e538d1b4732c865384340989f011c8)、[NET_OPT_UDP_OPT_FRAG](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da9db3637a09382655835493aed186a549)、[NET_OPT_UDP_OPT_MDS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da104d851b3c8884c875dbbc9d1e6c64ae)、[NET_OPT_UDP_OPT_MRDS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da12c660c9ee2dd9d9d2de36980949aa9f)、[NET_OPT_UDP_OPT_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da6441103cc8e0e3cf724d2ea79cf18dcb)、[NET_OPT_UDP_OPT_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae72a8a6e3f4a7a14370cd1267820c71d)、[NET_OPT_UDP_OPT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da61c105080d36bca8b4405527af4aaac4)、[NET_OPT_UDP_OPT_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dab4dd4a3acee76f82c37fd16fd5f53867)、[NET_OPT_UDP_OPT_EXP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daa3a443af92a7bc45aa9cc81ca4a1de0c)、[NET_OPT_UDP_OPT_UCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da98f7a13028a2deb6eee31f1bad7c20b7)、[NET_OPT_UDP_OPT_UENC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae95fc08de9277a59c42d6bf6355ec201)、[NET_OPT_UDP_OPT_UEXP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da885dadd317c676c4d9be316df29ff276)、[NET_OPT_UDP_OPT_DPLPMTUD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da4c24ea3a7cafcd9eddfc15a5725d75d2)、[NET_OPT_UDP_OPT_DPLPMTUD_APP_RESPOND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daf50b6d1ab2da2df3b2ba1f991fc8011e)。

网络上下文选项（Network Context Options）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.5\_函数（Functions）

<a id="r_ga423103d5c386b602737e23ee81f2a961"></a>

```c
static bool net_context_is_used (struct net_context *context)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_is_used](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga423103d5c386b602737e23ee81f2a961)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

此上下文（Context）是否正在使用。

<a id="r_ga2f6d614158c999fa68e518393c0a9c35"></a>

```c
static bool net_context_is_bound_to_iface (struct net_context *context)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_is_bound_to_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga2f6d614158c999fa68e518393c0a9c35)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

此上下文是否已绑定到网络接口（Network Interface）。

<a id="r_ga8e93032d6b65d9b5dfc0f64ecdf3a6b5"></a>

```c
static bool net_context_is_local_addr_set (struct net_context *context)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_is_local_addr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga8e93032d6b65d9b5dfc0f64ecdf3a6b5)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

是否已有本地地址（Local Address）绑定到此上下文。

<a id="r_ga53bd5f35a142f1d43f90d3bde99778e0"></a>

```c
static enum net_context_state net_context_get_state (struct net_context *context)
```

相关声明：[net_context_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga53bd5f35a142f1d43f90d3bde99778e0)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的状态（State）。

<a id="r_gaac934209341db606a4d563b3c48cce45"></a>

```c
static void net_context_set_state (struct net_context *context, enum net_context_state state)
```

相关声明：[net_context_set_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaac934209341db606a4d563b3c48cce45)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置此网络上下文的状态（State）。

<a id="r_ga4c3de0a3b7f27dd8ac9d0f415710faad"></a>

```c
static net_sa_family_t net_context_get_family (struct net_context *context)
```

相关声明：[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[net_context_get_family](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga4c3de0a3b7f27dd8ac9d0f415710faad)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的地址族（Address Family）。

<a id="r_ga37bbecc848430590d5d68d2880c83c1e"></a>

```c
static void net_context_set_family (struct net_context *context, net_sa_family_t family)
```

相关声明：[net_context_set_family](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga37bbecc848430590d5d68d2880c83c1e)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)。

设置此网络上下文的地址族（Address Family）。

<a id="r_ga24b4d99dddc4fabf383f5d8079650337"></a>

```c
static enum net_sock_type net_context_get_type (struct net_context *context)
```

相关声明：[net_sock_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaaab4268707dbe08348b98fb028e7aa5c)、[net_context_get_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga24b4d99dddc4fabf383f5d8079650337)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的上下文类型（Context Type）。

<a id="r_ga01c11c1dfce101df046df9ade00ed277"></a>

```c
static void net_context_set_type (struct net_context *context, enum net_sock_type type)
```

相关声明：[net_context_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga01c11c1dfce101df046df9ade00ed277)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sock_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaaab4268707dbe08348b98fb028e7aa5c)。

设置此网络上下文的上下文类型（Context Type）。

<a id="r_ga581582c0461b36088d21d0fd433cc284"></a>

```c
static void net_context_set_can_filter_id (struct net_context *context, int filter_id)
```

相关声明：[net_context_set_can_filter_id](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga581582c0461b36088d21d0fd433cc284)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

设置此网络上下文的 CAN 过滤器标识符（CAN Filter ID）。

<a id="r_ga7f4d732a99cb9e86fcd5226fbbb727f4"></a>

```c
static int net_context_get_can_filter_id (struct net_context *context)
```

相关声明：[net_context_get_can_filter_id](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga7f4d732a99cb9e86fcd5226fbbb727f4)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的 CAN 过滤器标识符（CAN Filter ID）。

<a id="r_gadf41291ca5be067e830d121000ca3f51"></a>

```c
static uint16_t net_context_get_proto (struct net_context *context)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_context_get_proto](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gadf41291ca5be067e830d121000ca3f51)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此网络上下文的 IP 协议（IP Protocol）。

<a id="r_gadcd0049229580244ea89fbc98bf23a81"></a>

```c
static void net_context_set_proto (struct net_context *context, uint16_t proto)
```

相关声明：[net_context_set_proto](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gadcd0049229580244ea89fbc98bf23a81)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置此网络上下文的 IP 协议（IP Protocol）。

<a id="r_gafe6b8c9af4464cd471285817d6d61087"></a>

```c
static struct net_if * net_context_get_iface (struct net_context *context)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_context_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafe6b8c9af4464cd471285817d6d61087)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的网络接口（Network Interface）。

<a id="r_ga10399e3f3d159de9325ac7632ce25c51"></a>

```c
static void net_context_set_iface (struct net_context *context, struct net_if *iface)
```

相关声明：[net_context_set_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga10399e3f3d159de9325ac7632ce25c51)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置此上下文的网络接口（Network Interface）。

<a id="r_ga2f8fccd2453227706e313ac056f1c6ef"></a>

```c
static void net_context_bind_iface (struct net_context *context, struct net_if *iface)
```

相关声明：[net_context_bind_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga2f8fccd2453227706e313ac056f1c6ef)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将网络接口（Network Interface）绑定到此上下文。

<a id="r_ga9cdb3e5849a5b2663e0a38ac2a39a427"></a>

```c
static uint8_t net_context_get_ipv4_ttl (struct net_context *context)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_context_get_ipv4_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga9cdb3e5849a5b2663e0a38ac2a39a427)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的 IPv4 生存时间值（Time-to-live，TTL）。

<a id="r_ga11672ca3ebdae63b0013ad76959304d5"></a>

```c
static void net_context_set_ipv4_ttl (struct net_context *context, uint8_t ttl)
```

相关声明：[net_context_set_ipv4_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga11672ca3ebdae63b0013ad76959304d5)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置此上下文的 IPv4 生存时间值（Time-to-live，TTL）。

<a id="r_ga3db832f40b6a0b975a282ef354a7bffc"></a>

```c
static uint8_t net_context_get_ipv4_mcast_ttl (struct net_context *context)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_context_get_ipv4_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga3db832f40b6a0b975a282ef354a7bffc)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的 IPv4 组播生存时间值（Multicast TTL）。

<a id="r_gab2a2064fa33613a60ad40597d0971774"></a>

```c
static void net_context_set_ipv4_mcast_ttl (struct net_context *context, uint8_t ttl)
```

相关声明：[net_context_set_ipv4_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab2a2064fa33613a60ad40597d0971774)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置此上下文的 IPv4 组播生存时间值（Multicast TTL）。

<a id="r_ga977b08a77586e0e4752bff725139427c"></a>

```c
static uint8_t net_context_get_ipv6_hop_limit (struct net_context *context)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_context_get_ipv6_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga977b08a77586e0e4752bff725139427c)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的 IPv6 跳数限制值（Hop Limit）。

<a id="r_ga0cbf8377e7757881033aab3e718b1a61"></a>

```c
static void net_context_set_ipv6_hop_limit (struct net_context *context, uint8_t hop_limit)
```

相关声明：[net_context_set_ipv6_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga0cbf8377e7757881033aab3e718b1a61)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置此上下文的 IPv6 跳数限制值（Hop Limit）。

<a id="r_ga99b5f0ded5d56b735e051ede5651f435"></a>

```c
static uint8_t net_context_get_ipv6_mcast_hop_limit (struct net_context *context)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_context_get_ipv6_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga99b5f0ded5d56b735e051ede5651f435)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取此上下文的 IPv6 组播跳数限制值（Multicast Hop Limit）。

<a id="r_gaf29d5ee244c552d78171938a903fbaca"></a>

```c
static void net_context_set_ipv6_mcast_hop_limit (struct net_context *context, uint8_t hop_limit)
```

相关声明：[net_context_set_ipv6_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf29d5ee244c552d78171938a903fbaca)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置此上下文的 IPv6 组播跳数限制值（Multicast Hop Limit）。

<a id="r_ga9bd6b5e9429b6e845d41f6cbf242c092"></a>

```c
static void net_context_set_proxy_enabled (struct net_context *context, bool enable)
```

相关声明：[net_context_set_proxy_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga9bd6b5e9429b6e845d41f6cbf242c092)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为此上下文启用或禁用 SOCKS 代理支持（SOCKS Proxy Support）。

<a id="r_ga5c3a841ff54ddb53cedcccefde5a7d7a"></a>

```c
static bool net_context_is_proxy_enabled (struct net_context *context)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_is_proxy_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga5c3a841ff54ddb53cedcccefde5a7d7a)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

此上下文的 SOCKS 代理支持（SOCKS Proxy Support）是启用还是禁用。

<a id="r_ga37fbf84456a4142330d74eed1f3c24f6"></a>

```c
int net_context_get (net_sa_family_t family, enum net_sock_type type, uint16_t ip_proto, struct net_context **context)
```

相关声明：[net_context_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga37fbf84456a4142330d74eed1f3c24f6)、[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[net_sock_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaaab4268707dbe08348b98fb028e7aa5c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取网络上下文（Network Context）。

<a id="r_ga1d6b64e302c546db589c661f4b6bda98"></a>

```c
int net_context_put (struct net_context *context)
```

相关声明：[net_context_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga1d6b64e302c546db589c661f4b6bda98)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

关闭网络上下文（Network Context），并释放其引用（Unref）。

<a id="r_ga4c0ef9540a0d7e800c4529274f5c22f4"></a>

```c
int net_context_ref (struct net_context *context)
```

相关声明：[net_context_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga4c0ef9540a0d7e800c4529274f5c22f4)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

获取一个 `net_context` 引用，增加引用计数（Reference Count），以防止该上下文被销毁。

<a id="r_ga0d391690d9d6972ce6f4baedeab64b11"></a>

```c
int net_context_unref (struct net_context *context)
```

相关声明：[net_context_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga0d391690d9d6972ce6f4baedeab64b11)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

减少网络上下文（Network Context）的引用计数（Reference Count）。

<a id="r_ga11801119ad1d62db0302479c133adb35"></a>

```c
static void net_context_signal_linger (struct net_context *context)
```

相关声明：[net_context_signal_linger](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga11801119ad1d62db0302479c133adb35)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

通知此上下文的底层连接已由传输层（Transport）关闭，使因 `SO_LINGER` 而阻塞的 `close()` 能够继续执行。

<a id="r_gae3b3892b921e4694a18e7bacee63841d"></a>

```c
static int net_context_create_ipv4_new (struct net_context *context, struct net_pkt *pkt, const struct net_in_addr *src, const struct net_in_addr *dst)
```

相关声明：[net_context_create_ipv4_new](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gae3b3892b921e4694a18e7bacee63841d)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

根据上下文，在提供的 `net_pkt` 中创建 IPv4 数据包（IPv4 Packet）。

<a id="r_gaa973878eb7f6bf69d91da992edad6409"></a>

```c
static int net_context_create_ipv6_new (struct net_context *context, struct net_pkt *pkt, const struct net_in6_addr *src, const struct net_in6_addr *dst)
```

相关声明：[net_context_create_ipv6_new](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa973878eb7f6bf69d91da992edad6409)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

根据上下文，在提供的 `net_pkt` 中创建 IPv6 数据包（IPv6 Packet）。

<a id="r_ga2023f160b4d2ebc05d665d119611ef25"></a>

```c
int net_context_bind (struct net_context *context, const struct net_sockaddr *addr, net_socklen_t addrlen)
```

相关声明：[net_context_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga2023f160b4d2ebc05d665d119611ef25)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

为套接字（Socket）分配本地地址（Local Address）。

<a id="r_ga3803c0d738fbb9d786f401aacc10a4d3"></a>

```c
int net_context_listen (struct net_context *context, int backlog)
```

相关声明：[net_context_listen](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga3803c0d738fbb9d786f401aacc10a4d3)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)。

将上下文标记为监听状态（Listening）。

<a id="r_gadf4ab08eb39803909e585b16ce68307a"></a>

```c
int net_context_connect (struct net_context *context, const struct net_sockaddr *addr, net_socklen_t addrlen, net_context_connect_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gadf4ab08eb39803909e585b16ce68307a)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[net_context_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga120ae8d4ff788ab21b19c11ed1738a71)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

创建网络连接（Network Connection）。

<a id="r_ga1b056999d9ab8f2d3b3c0f4788f36cdd"></a>

```c
int net_context_accept (struct net_context *context, net_tcp_accept_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga1b056999d9ab8f2d3b3c0f4788f36cdd)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_tcp_accept_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf05114d2edc8b5fb485fd37f3d0821ba)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

接受网络连接尝试（Network Connection Attempt）。

<a id="r_gac793e1def18200416e3f679067c56ab3"></a>

```c
int net_context_send (struct net_context *context, const void *buf, size_t len, net_context_send_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_send](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gac793e1def18200416e3f679067c56ab3)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_context_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3caccfe9fa1bc7ce0e4654192a5de93)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向对端（Peer）发送数据。

<a id="r_gafd68de53778cbd807d0e45209a83df05"></a>

```c
int net_context_sendto (struct net_context *context, const void *buf, size_t len, const struct net_sockaddr *dst_addr, net_socklen_t addrlen, net_context_send_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_sendto](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafd68de53778cbd807d0e45209a83df05)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[net_context_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3caccfe9fa1bc7ce0e4654192a5de93)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向地址指定的对端（Peer）发送数据。

<a id="r_gaf915131b95b159e299f034768cefdaea"></a>

```c
int net_context_sendmsg (struct net_context *context, const struct net_msghdr *msghdr, int flags, net_context_send_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_sendmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf915131b95b159e299f034768cefdaea)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_context_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3caccfe9fa1bc7ce0e4654192a5de93)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

将 `iovec` 中的数据发送给 `net_msghdr` 结构体指定的对端（Peer）。

<a id="r_ga74f919185f8af074c2d90aa04733dd2a"></a>

```c
int net_context_recv (struct net_context *context, net_context_recv_cb_t cb, k_timeout_t timeout, void *user_data)
```

相关声明：[net_context_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga74f919185f8af074c2d90aa04733dd2a)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_context_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafa485a6fae8237dd7e6856f4567b2317)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从上下文指定的对端（Peer）接收网络数据。

<a id="r_gab3cc2a13e24f9c263bc40cc87d752a9f"></a>

```c
int net_context_update_recv_wnd (struct net_context *context, int32_t delta)
```

相关声明：[net_context_update_recv_wnd](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3cc2a13e24f9c263bc40cc87d752a9f)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

更新此上下文的 TCP 接收窗口（TCP Receive Window）。

<a id="r_ga40c6ef5b1f8b846e5b205947e87ce585"></a>

```c
int net_context_set_option (struct net_context *context, enum net_context_option option, const void *value, uint32_t len)
```

相关声明：[net_context_set_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga40c6ef5b1f8b846e5b205947e87ce585)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_context_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab03a354899ff68f6b9d127bc3bb5e17d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置此上下文的连接选项（Connection Option）。

<a id="r_gabbb9472c54b2fbe0b519dcb68e02a44e"></a>

```c
int net_context_get_option (struct net_context *context, enum net_context_option option, void *value, uint32_t *len)
```

相关声明：[net_context_get_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gabbb9472c54b2fbe0b519dcb68e02a44e)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[net_context_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab03a354899ff68f6b9d127bc3bb5e17d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取此上下文的连接选项值（Connection Option Value）。

<a id="r_gaefead18501a966af4a7f71eb23ac17c7"></a>

```c
int net_context_set_udp_dplpmtud (struct net_context *context, bool enable)
```

相关声明：[net_context_set_udp_dplpmtud](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaefead18501a966af4a7f71eb23ac17c7)、[net_context](../network_core_model_reference/P055_net_context_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在 UDP 上下文上启用或禁用数据报分组层路径 MTU 发现（DPLPMTUD，RFC 9869）。

<a id="r_gabb751f7d213d00f8eec72a67f4ce3491"></a>

```c
void net_context_foreach (net_context_cb_t cb, void *user_data)
```

相关声明：[net_context_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gabb751f7d213d00f8eec72a67f4ce3491)、[net_context_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa82d80fa18693b98dc363c35104075ba)。

遍历全部网络连接，并为每个网络上下文（Network Context）调用回调（Callback）。

<a id="r_gad9350d40a884315ff9de4032a8d6ae71"></a>

```c
bool net_context_port_in_use (enum net_ip_protocol ip_proto, uint16_t local_port, const struct net_sockaddr *local_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_context_port_in_use](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gad9350d40a884315ff9de4032a8d6ae71)、[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

检查端口是否正在使用，即是否已绑定（Bound）。


## 8.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/net_stats.h](../api_source_interrupt_modem_reference/P007_net_stats.h_源码浏览.md)
- [zephyr/net/dplpmtud.h](../api_source_reference/P146_dplpmtud.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P022_net_context.h_源码浏览.md)
- [net_context](../network_core_model_reference/P055_net_context_结构体.md)
- [NET_CONTEXT_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga5e2f5fcc08863a4090bc04040ee88d29)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [NET_CONTEXT_FAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gac8f6e3a16d52e8e376c38eec0ed8a940)
- [NET_CONTEXT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gac9b4cf9beecaac5bf05db3111c803678)
- [NET_CONTEXT_REMOTE_ADDR_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga84206421e8f2e1eb114d393f0c81428b)
- [NET_CONTEXT_BOUND_TO_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa337bccec2c1df42540f236bb33a70e1)
- [NET_CONTEXT_LOCAL_ADDR_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga717b1aaa11d589bfe929d98be5be19ed)
- [net_context_setup_pools](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga41d258362d6a7a703bc0b65d08e2b4c4)
- [net_context_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafa485a6fae8237dd7e6856f4567b2317)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_context_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3caccfe9fa1bc7ce0e4654192a5de93)
- [net_tcp_accept_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf05114d2edc8b5fb485fd37f3d0821ba)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [net_context_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga120ae8d4ff788ab21b19c11ed1738a71)
- [net_pkt_get_slab_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga3bb4bbd522ede36213bafe86f2d1d770)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [net_pkt_get_pool_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gae3082af116955d4175c025a02b296c91)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_context_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa82d80fa18693b98dc363c35104075ba)
- [net_context_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab03a354899ff68f6b9d127bc3bb5e17d)
- [NET_OPT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c)
- [NET_OPT_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184)
- [NET_OPT_SOCKS5](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c)
- [NET_OPT_RCVTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076)
- [NET_OPT_SNDTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668)
- [NET_OPT_RCVBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1)
- [NET_OPT_SNDBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08)
- [NET_OPT_DSCP_ECN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c)
- [NET_OPT_REUSEADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561)
- [NET_OPT_REUSEPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4)
- [NET_OPT_IPV6_V6ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c)
- [NET_OPT_RECV_PKTINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a)
- [NET_OPT_MCAST_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e)
- [NET_OPT_MCAST_HOP_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d)
- [NET_OPT_UNICAST_HOP_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3)
- [NET_OPT_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184)
- [NET_OPT_ADDR_PREFERENCES](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d)
- [NET_OPT_TIMESTAMPING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2)
- [NET_OPT_MCAST_IFINDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da98136d42db895cf6f3e35ee418e0b7eb)
- [NET_OPT_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dad6b8627398a90dd622f433e8b3fee3a3)
- [NET_OPT_LOCAL_PORT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da469d1d21e088eba6f96ec0a679636ba7)
- [NET_OPT_IPV6_MCAST_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dab1615ef9a3bf84daf964a445476bc04c)
- [NET_OPT_IPV4_MCAST_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da38adf4f5e3fba71f152a05c208e6f9f0)
- [NET_OPT_RECV_HOPLIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da3f5fea1c10f55d4db1d72bba2959445e)
- [NET_OPT_DONT_FRAGMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dad5099786ebcdc0198cf3cd1db465387d)
- [NET_OPT_LINGER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae0ed5497e4d356ca2bdea0a120dcb6ee)
- [NET_OPT_UDP_OPT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dacd227331833af7fb92b84f3ceb80f3ab)
- [NET_OPT_UDP_OPT_OCS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da9dec13665201fdc9be87490cde2f3253)
- [NET_OPT_UDP_OPT_APC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da69e538d1b4732c865384340989f011c8)
- [NET_OPT_UDP_OPT_FRAG](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da9db3637a09382655835493aed186a549)
- [NET_OPT_UDP_OPT_MDS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da104d851b3c8884c875dbbc9d1e6c64ae)
- [NET_OPT_UDP_OPT_MRDS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da12c660c9ee2dd9d9d2de36980949aa9f)
- [NET_OPT_UDP_OPT_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da6441103cc8e0e3cf724d2ea79cf18dcb)
- [NET_OPT_UDP_OPT_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae72a8a6e3f4a7a14370cd1267820c71d)
- [NET_OPT_UDP_OPT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da61c105080d36bca8b4405527af4aaac4)
- [NET_OPT_UDP_OPT_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dab4dd4a3acee76f82c37fd16fd5f53867)
- [NET_OPT_UDP_OPT_EXP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daa3a443af92a7bc45aa9cc81ca4a1de0c)
- [NET_OPT_UDP_OPT_UCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da98f7a13028a2deb6eee31f1bad7c20b7)
- [NET_OPT_UDP_OPT_UENC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17dae95fc08de9277a59c42d6bf6355ec201)
- [NET_OPT_UDP_OPT_UEXP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da885dadd317c676c4d9be316df29ff276)
- [NET_OPT_UDP_OPT_DPLPMTUD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17da4c24ea3a7cafcd9eddfc15a5725d75d2)
- [NET_OPT_UDP_OPT_DPLPMTUD_APP_RESPOND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ggab03a354899ff68f6b9d127bc3bb5e17daf50b6d1ab2da2df3b2ba1f991fc8011e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_context_is_used](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga423103d5c386b602737e23ee81f2a961)
- [net_context_is_bound_to_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga2f6d614158c999fa68e518393c0a9c35)
- [net_context_is_local_addr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga8e93032d6b65d9b5dfc0f64ecdf3a6b5)
- [net_context_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga53bd5f35a142f1d43f90d3bde99778e0)
- [net_context_set_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaac934209341db606a4d563b3c48cce45)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [net_context_get_family](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga4c3de0a3b7f27dd8ac9d0f415710faad)
- [net_context_set_family](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga37bbecc848430590d5d68d2880c83c1e)
- [net_sock_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaaab4268707dbe08348b98fb028e7aa5c)
- [net_context_get_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga24b4d99dddc4fabf383f5d8079650337)
- [net_context_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga01c11c1dfce101df046df9ade00ed277)
- [net_context_set_can_filter_id](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga581582c0461b36088d21d0fd433cc284)
- [net_context_get_can_filter_id](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga7f4d732a99cb9e86fcd5226fbbb727f4)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_context_get_proto](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gadf41291ca5be067e830d121000ca3f51)
- [net_context_set_proto](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gadcd0049229580244ea89fbc98bf23a81)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_context_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafe6b8c9af4464cd471285817d6d61087)
- [net_context_set_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga10399e3f3d159de9325ac7632ce25c51)
- [net_context_bind_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga2f8fccd2453227706e313ac056f1c6ef)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_context_get_ipv4_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga9cdb3e5849a5b2663e0a38ac2a39a427)
- [net_context_set_ipv4_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga11672ca3ebdae63b0013ad76959304d5)
- [net_context_get_ipv4_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga3db832f40b6a0b975a282ef354a7bffc)
- [net_context_set_ipv4_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab2a2064fa33613a60ad40597d0971774)
- [net_context_get_ipv6_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga977b08a77586e0e4752bff725139427c)
- [net_context_set_ipv6_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga0cbf8377e7757881033aab3e718b1a61)
- [net_context_get_ipv6_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga99b5f0ded5d56b735e051ede5651f435)
- [net_context_set_ipv6_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf29d5ee244c552d78171938a903fbaca)
- [net_context_set_proxy_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga9bd6b5e9429b6e845d41f6cbf242c092)
- [net_context_is_proxy_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga5c3a841ff54ddb53cedcccefde5a7d7a)
- [net_context_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga37fbf84456a4142330d74eed1f3c24f6)
- [net_context_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga1d6b64e302c546db589c661f4b6bda98)
- [net_context_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga4c0ef9540a0d7e800c4529274f5c22f4)
- [net_context_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga0d391690d9d6972ce6f4baedeab64b11)
- [net_context_signal_linger](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga11801119ad1d62db0302479c133adb35)
- [net_context_create_ipv4_new](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gae3b3892b921e4694a18e7bacee63841d)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_context_create_ipv6_new](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaa973878eb7f6bf69d91da992edad6409)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [net_context_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga2023f160b4d2ebc05d665d119611ef25)
- [net_context_listen](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga3803c0d738fbb9d786f401aacc10a4d3)
- [net_context_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gadf4ab08eb39803909e585b16ce68307a)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_context_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga1b056999d9ab8f2d3b3c0f4788f36cdd)
- [net_context_send](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gac793e1def18200416e3f679067c56ab3)
- [net_context_sendto](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafd68de53778cbd807d0e45209a83df05)
- [net_context_sendmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf915131b95b159e299f034768cefdaea)
- [net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_context_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga74f919185f8af074c2d90aa04733dd2a)
- [net_context_update_recv_wnd](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3cc2a13e24f9c263bc40cc87d752a9f)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [net_context_set_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga40c6ef5b1f8b846e5b205947e87ce585)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_context_get_option](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gabbb9472c54b2fbe0b519dcb68e02a44e)
- [net_context_set_udp_dplpmtud](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaefead18501a966af4a7f71eb23ac17c7)
- [RFC 9869](https://datatracker.ietf.org/doc/html/rfc9869)
- [net_context_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gabb751f7d213d00f8eec72a67f4ce3491)
- [net_context_port_in_use](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gad9350d40a884315ff9de4032a8d6ae71)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)

<a id="header-details"></a>

---

[上一章](P007_zephyr__drivers__misc__max2221x__max2221x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__net__net_pkt.h_文件参考.md)
