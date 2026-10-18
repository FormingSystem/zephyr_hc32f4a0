---
id: learning.zephyr-docs.api-network-work-driver-reference.page-2
title: IPv4_IPv6 原语与辅助工具（Primitives and helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_IPv4\_IPv6 原语与辅助工具（Primitives and helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv4/IPv6 原语与辅助工具（Primitives and helpers）

<a id="details"></a>

IPv4／IPv6 基本操作（Primitives）与辅助函数（Helpers）。自 1.0 起提供；接口版本为 1.0.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_net_5Fin6_5Faddr"></a>

```c
struct net_in6_addr
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

IPv6地址结构（Address Struct）。

<a id="r_net_5Fin_5Faddr"></a>

```c
struct net_in_addr
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

IPv4地址结构（Address Struct）。

<a id="r_net_5Fsockaddr_5Fin6"></a>

```c
struct net_sockaddr_in6
```

相关声明：[net_sockaddr_in6](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md)。

IPv6的套接字地址结构（Socket Address Struct）。

<a id="r_net_5Fsockaddr_5Fin"></a>

```c
struct net_sockaddr_in
```

相关声明：[net_sockaddr_in](../network_core_model_reference/P119_net_sockaddr_in_结构体.md)。

IPv4的套接字地址结构（Socket Address Struct）。

<a id="r_net_5Fsockaddr_5Fll"></a>

```c
struct net_sockaddr_ll
```

相关声明：[net_sockaddr_ll](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md)。

数据包套接字（Packet Socket）的套接字地址结构。

<a id="r_net_5Fsockaddr_5Fcan"></a>

```c
struct net_sockaddr_can
```

相关声明：[net_sockaddr_can](../network_core_model_reference/P118_net_sockaddr_can_结构体.md)。

struct net_sockaddr_can：CAN套接字（Socket）使用的net_sockaddr结构。

<a id="r_net_5Fsockaddr_5Fnm"></a>

```c
struct net_sockaddr_nm
```

相关声明：[net_sockaddr_nm](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md)。

struct net_sockaddr_nm：NET_MGMT套接字（Socket）使用的net_sockaddr结构。

<a id="r_net_5Fiovec"></a>

```c
struct net_iovec
```

相关声明：[net_iovec](../network_core_model_reference/P098_net_iovec_结构体.md)。

输入输出向量（IO Vector）的数组元素。

<a id="r_net_5Fmsghdr"></a>

```c
struct net_msghdr
```

相关声明：[net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)。

消息结构（Message Struct）。

<a id="r_net_5Fcmsghdr"></a>

```c
struct net_cmsghdr
```

相关声明：[net_cmsghdr](../network_core_model_reference/P052_net_cmsghdr_结构体.md)。

控制消息辅助数据（Control Message Ancillary Data）。

<a id="r_net_5Flinger"></a>

```c
struct net_linger
```

相关声明：[net_linger](../network_core_model_reference/P104_net_linger_结构体.md)。

套接字选项SO_LINGER使用的延迟关闭选项（Linger Option）结构。

<a id="r_net_5Fsockaddr"></a>

```c
struct net_sockaddr
```

相关声明：[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

通用sockaddr结构。

<a id="r_net_5Ftuple"></a>

```c
struct net_tuple
```

相关声明：[net_tuple](../network_core_model_reference/P156_net_tuple_结构体.md)。

IPv6/IPv4网络连接元组（Network Connection Tuple）。

<a id="r_net_5Fifreq"></a>

```c
struct net_ifreq
```

相关声明：[net_ifreq](../network_core_model_reference/P093_net_ifreq_结构体.md)。

接口描述（Interface Description）结构。

<a id="r_net_5Fin_5Fpktinfo"></a>

```c
struct net_in_pktinfo
```

相关声明：[net_in_pktinfo](../network_core_model_reference/P097_net_in_pktinfo_结构体.md)。

传入的IPv4数据包信息（Packet Information）。

<a id="r_net_5Fip_5Fmreqn"></a>

```c
struct net_ip_mreqn
```

相关声明：[net_ip_mreqn](../network_core_model_reference/P100_net_ip_mreqn_结构体.md)。

加入或离开IPv4组播组（Multicast Group）时使用的结构。

<a id="r_net_5Fip_5Fmreq"></a>

```c
struct net_ip_mreq
```

相关声明：[net_ip_mreq](../network_core_model_reference/P099_net_ip_mreq_结构体.md)。

设置IPv4组播网络接口（Multicast Network Interface）时使用的结构。

<a id="r_net_5Fipv6_5Fmreq"></a>

```c
struct net_ipv6_mreq
```

相关声明：[net_ipv6_mreq](../network_core_model_reference/P102_net_ipv6_mreq_结构体.md)。

加入或离开IPv6组播组（Multicast Group）时使用的结构。

<a id="r_net_5Fpacket_5Fmreq"></a>

```c
struct net_packet_mreq
```

相关声明：[net_packet_mreq](../network_core_model_reference/P113_net_packet_mreq_结构体.md)。

设置数据包套接字（Packet Socket）组播过滤时使用的结构。

<a id="r_net_5Fin6_5Fpktinfo"></a>

```c
struct net_in6_pktinfo
```

相关声明：[net_in6_pktinfo](../network_core_model_reference/P095_net_in6_pktinfo_结构体.md)。

传入的IPv6数据包信息（Packet Information）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_gaff57ad0fabd8cdd422cf8777b3d94602"></a>

```c
#define NET_PF_UNSPEC 0
```

相关声明：[NET_PF_UNSPEC](#gaff57ad0fabd8cdd422cf8777b3d94602)。

未指定的协议族（Unspecified Protocol Family）。

<a id="r_ga3a490b5c27b98ce39dbbeb35e62fa9e0"></a>

```c
#define NET_PF_INET 1
```

相关声明：[NET_PF_INET](#ga3a490b5c27b98ce39dbbeb35e62fa9e0)。

IP 协议族版本 4（IP Protocol Family Version 4）。

<a id="r_gad794203c740ef6a24604092f3b4125e3"></a>

```c
#define NET_PF_INET6 2
```

相关声明：[NET_PF_INET6](#gad794203c740ef6a24604092f3b4125e3)。

IP 协议族版本 6（IP Protocol Family Version 6）。

<a id="r_ga54ea7d2c3dfe6f1753891da3a94cc1f0"></a>

```c
#define NET_PF_PACKET 3
```

相关声明：[NET_PF_PACKET](#ga54ea7d2c3dfe6f1753891da3a94cc1f0)。

分组协议族（Packet Family）。

<a id="r_ga84228eb6b051e8ec5a8b4ed5aaa3119f"></a>

```c
#define NET_PF_CAN 4
```

相关声明：[NET_PF_CAN](#ga84228eb6b051e8ec5a8b4ed5aaa3119f)。

控制器局域网（Controller Area Network）。

<a id="r_ga99cfb4cf13b61a0b9f11b6c12bf58371"></a>

```c
#define NET_PF_NET_MGMT 5
```

相关声明：[NET_PF_NET_MGMT](#ga99cfb4cf13b61a0b9f11b6c12bf58371)。

网络管理信息（Network Management Info）。

<a id="r_gaf062d3e0ca938d2b41c2c7f6c92d8c49"></a>

```c
#define NET_PF_LOCAL 6
```

相关声明：[NET_PF_LOCAL](#gaf062d3e0ca938d2b41c2c7f6c92d8c49)。

进程间通信（Inter-process Communication）。

<a id="r_gae9118bc697bcec58fe265899d6ca7149"></a>

```c
#define NET_PF_UNIX NET_PF_LOCAL
```

相关声明：[NET_PF_UNIX](#gae9118bc697bcec58fe265899d6ca7149)、[NET_PF_LOCAL](#gaf062d3e0ca938d2b41c2c7f6c92d8c49)。

进程间通信（Inter-process Communication）。

<a id="r_ga8702e764fa49396587469a102870b109"></a>

```c
#define NET_AF_UNSPEC NET_PF_UNSPEC
```

相关声明：[NET_AF_UNSPEC](#ga8702e764fa49396587469a102870b109)、[NET_PF_UNSPEC](#gaff57ad0fabd8cdd422cf8777b3d94602)。

未指定的地址族（Unspecified Address Family）。

<a id="r_gac53da21004b2bdc93b878da2ec4590bd"></a>

```c
#define NET_AF_INET NET_PF_INET
```

相关声明：[NET_AF_INET](#gac53da21004b2bdc93b878da2ec4590bd)、[NET_PF_INET](#ga3a490b5c27b98ce39dbbeb35e62fa9e0)。

IP 协议族版本 4（IP Protocol Family Version 4）。

<a id="r_ga502492205736b373fa35c0524ba3d4e6"></a>

```c
#define NET_AF_INET6 NET_PF_INET6
```

相关声明：[NET_AF_INET6](#ga502492205736b373fa35c0524ba3d4e6)、[NET_PF_INET6](#gad794203c740ef6a24604092f3b4125e3)。

IP 协议族版本 6（IP Protocol Family Version 6）。

<a id="r_ga090f4770cd630517b5391d36e3705e41"></a>

```c
#define NET_AF_PACKET NET_PF_PACKET
```

相关声明：[NET_AF_PACKET](#ga090f4770cd630517b5391d36e3705e41)、[NET_PF_PACKET](#ga54ea7d2c3dfe6f1753891da3a94cc1f0)。

分组协议族（Packet Family）。

<a id="r_ga1df641bd5978219a7da51ea25ea8ac2f"></a>

```c
#define NET_AF_CAN NET_PF_CAN
```

相关声明：[NET_AF_CAN](#ga1df641bd5978219a7da51ea25ea8ac2f)、[NET_PF_CAN](#ga84228eb6b051e8ec5a8b4ed5aaa3119f)。

控制器局域网（Controller Area Network）。

<a id="r_ga209390ff940aa0f0746c3a4fd4e98806"></a>

```c
#define NET_AF_NET_MGMT NET_PF_NET_MGMT
```

相关声明：[NET_AF_NET_MGMT](#ga209390ff940aa0f0746c3a4fd4e98806)、[NET_PF_NET_MGMT](#ga99cfb4cf13b61a0b9f11b6c12bf58371)。

网络管理信息（Network Management Info）。

<a id="r_ga67f6049571b9326f646a2b6ad5e29778"></a>

```c
#define NET_AF_LOCAL NET_PF_LOCAL
```

相关声明：[NET_AF_LOCAL](#ga67f6049571b9326f646a2b6ad5e29778)、[NET_PF_LOCAL](#gaf062d3e0ca938d2b41c2c7f6c92d8c49)。

进程间通信（Inter-process Communication）。

<a id="r_ga88930e91e400b4eca0a9392288490268"></a>

```c
#define NET_AF_UNIX NET_PF_UNIX
```

相关声明：[NET_AF_UNIX](#ga88930e91e400b4eca0a9392288490268)、[NET_PF_UNIX](#gae9118bc697bcec58fe265899d6ca7149)。

进程间通信（Inter-process Communication）。

<a id="r_ga4837ff0eece26b00ae46ed7c16997a97"></a>

```c
#define net_ntohs(x)
```

相关声明：[net_ntohs](#ga4837ff0eece26b00ae46ed7c16997a97)。

将 16 位值从网络字节序（Network Byte Order）转换为主机字节序（Host Byte Order）。

<a id="r_gae18466011462c20add53de2e01505b92"></a>

```c
#define net_ntohl(x)
```

相关声明：[net_ntohl](#gae18466011462c20add53de2e01505b92)。

将 32 位值从网络字节序（Network Byte Order）转换为主机字节序（Host Byte Order）。

<a id="r_ga35f36b83b652246e9a61c9ddfdfed4f5"></a>

```c
#define net_ntohll(x)
```

相关声明：[net_ntohll](#ga35f36b83b652246e9a61c9ddfdfed4f5)。

将 64 位值从网络字节序（Network Byte Order）转换为主机字节序（Host Byte Order）。

<a id="r_gae20291eed240d648d0ef7e13822f925f"></a>

```c
#define net_htons(x)
```

相关声明：[net_htons](#gae20291eed240d648d0ef7e13822f925f)。

将 16 位值从主机字节序（Host Byte Order）转换为网络字节序（Network Byte Order）。

<a id="r_ga5d9e16e8f439be6f94fb3f72de13bdac"></a>

```c
#define net_htonl(x)
```

相关声明：[net_htonl](#ga5d9e16e8f439be6f94fb3f72de13bdac)。

将 32 位值从主机字节序（Host Byte Order）转换为网络字节序（Network Byte Order）。

<a id="r_ga7f215d5ef1d4098a7e8681500796a8f5"></a>

```c
#define net_htonll(x)
```

相关声明：[net_htonll](#ga7f215d5ef1d4098a7e8681500796a8f5)。

将 64 位值从主机字节序（Host Byte Order）转换为网络字节序（Network Byte Order）。

<a id="r_ga1eefdabf590090be9f98bdf4a2f43bb4"></a>

```c
#define NET_IPV6_ADDR_SIZE 16
```

相关声明：[NET_IPV6_ADDR_SIZE](#ga1eefdabf590090be9f98bdf4a2f43bb4)。

IPv6 地址的二进制大小（Binary Size）。

<a id="r_ga10a82ea9ba9ca19f3b773bdd53c978e0"></a>

```c
#define NET_IPV4_ADDR_SIZE 4
```

相关声明：[NET_IPV4_ADDR_SIZE](#ga10a82ea9ba9ca19f3b773bdd53c978e0)。

IPv4 地址的二进制大小（Binary Size）。

<a id="r_ga1d17cfa3d3f1a6b5f3fe6476ef2db74f"></a>

```c
#define NET_CMSG_FIRSTHDR(msghdr)
```

相关声明：[NET_CMSG_FIRSTHDR](#ga1d17cfa3d3f1a6b5f3fe6476ef2db74f)。

返回指针，指向传入的 `msghdr` 所关联的辅助数据缓冲区（Ancillary Data Buffer）中的第一个 `cmsghdr`。

<a id="r_ga99a82490600a896e44a0d76e1d318950"></a>

```c
#define NET_CMSG_NXTHDR(msghdr, cmsg)
```

相关声明：[NET_CMSG_NXTHDR](#ga99a82490600a896e44a0d76e1d318950)。

返回传入的 `cmsghdr` 之后的下一个有效 `cmsghdr`。

<a id="r_ga00f6b79613665e424a343d78203ef915"></a>

```c
#define NET_CMSG_DATA(cmsg)
```

相关声明：[NET_CMSG_DATA](#ga00f6b79613665e424a343d78203ef915)。

返回指向 `cmsghdr` 的数据部分（Data Portion）的指针。

<a id="r_ga47a68c5c03dd7dbcc6222772ffe1bbb7"></a>

```c
#define NET_CMSG_SPACE(length)
```

相关声明：[NET_CMSG_SPACE](#ga47a68c5c03dd7dbcc6222772ffe1bbb7)。

返回辅助元素（Ancillary Element）占用的字节数；该元素的载荷（Payload）长度为传入的数据长度。

<a id="r_ga4fc63db80b096eacc2b5b06e2fd2563b"></a>

```c
#define NET_CMSG_LEN(length)
```

相关声明：[NET_CMSG_LEN](#ga4fc63db80b096eacc2b5b06e2fd2563b)。

返回应存入 `net_cmsghdr` 结构体的 `cmsg_len` 成员的值，并计入必要的对齐（Alignment）。

<a id="r_ga929a6597b2a4669e42cb416a84fd568f"></a>

```c
#define SOCKADDR_ALIGN (4)
```

相关声明：[SOCKADDR_ALIGN](#ga929a6597b2a4669e42cb416a84fd568f)。

<a id="r_ga3903cb074f334a50fd88815d2795773e"></a>

```c
#define NET_IN6ADDR_ANY_INIT
```

相关声明：[NET_IN6ADDR_ANY_INIT](#ga3903cb074f334a50fd88815d2795773e)。

IPv6 地址初始化器（Address Initializer）。

<a id="r_ga2987743eae5556c7374060ed3d392c2a"></a>

```c
#define NET_IN6ADDR_LOOPBACK_INIT
```

相关声明：[NET_IN6ADDR_LOOPBACK_INIT](#ga2987743eae5556c7374060ed3d392c2a)。

IPv6 回环地址初始化器（Loopback Address Initializer）。

<a id="r_gaf38d9372d95e8a3a7d502fe3eceb4e50"></a>

```c
#define NET_INADDR_ANY 0
```

相关声明：[NET_INADDR_ANY](#gaf38d9372d95e8a3a7d502fe3eceb4e50)。

IPv4 任意地址（Any Address）。

<a id="r_ga24a1863f48c95c94fb438a545428ca91"></a>

```c
#define NET_INADDR_BROADCAST 0xffffffff
```

相关声明：[NET_INADDR_BROADCAST](#ga24a1863f48c95c94fb438a545428ca91)。

IPv4 广播地址（Broadcast Address）。

<a id="r_gae117b1066c227a95aec0dd4b41000b5f"></a>

```c
#define NET_INADDR_ANY_INIT { { { NET_INADDR_ANY } } }
```

相关声明：[NET_INADDR_ANY_INIT](#gae117b1066c227a95aec0dd4b41000b5f)、[NET_INADDR_ANY](#gaf38d9372d95e8a3a7d502fe3eceb4e50)。

IPv4 地址初始化器（Address Initializer）。

<a id="r_ga4672091907479da6b09ac78f01aa5cf0"></a>

```c
#define NET_INADDR_LOOPBACK_INIT { { { 127, 0, 0, 1 } } }
```

相关声明：[NET_INADDR_LOOPBACK_INIT](#ga4672091907479da6b09ac78f01aa5cf0)。

IPv4 回环地址初始化器（Loopback Address Initializer）。

<a id="r_gae864ce227183974771322ba07f8c493d"></a>

```c
#define NET_INET_ADDRSTRLEN 16
```

相关声明：[NET_INET_ADDRSTRLEN](#gae864ce227183974771322ba07f8c493d)。

IPv4 地址字符串（Address String）的最大长度。

<a id="r_ga29969b236fa78c479836cbd143b099f3"></a>

```c
#define NET_INET6_ADDRSTRLEN 46
```

相关声明：[NET_INET6_ADDRSTRLEN](#ga29969b236fa78c479836cbd143b099f3)。

IPv6 地址字符串（Address String）的最大长度。

<a id="r_ga5b32bdfc249437709bb25bd95ec7d6d7"></a>

```c
#define NET_MAX_PRIORITIES 8
```

相关声明：[NET_MAX_PRIORITIES](#ga5b32bdfc249437709bb25bd95ec7d6d7)。

优先级值（Priority Values）的数量。

<a id="r_gae65887fe7fe408c886764d07b0c30547"></a>

```c
#define NET_PACKET_MR_MULTICAST 0
```

相关声明：[NET_PACKET_MR_MULTICAST](#gae65887fe7fe408c886764d07b0c30547)。

分组套接字（Packet Socket）的多播过滤类型（Multicast Filtering Types）。

<a id="r_gaa54e835a1878a5c044dc20fdc563078d"></a>

```c
#define NET_PACKET_MR_PROMISC 1
```

相关声明：[NET_PACKET_MR_PROMISC](#gaa54e835a1878a5c044dc20fdc563078d)。

分组套接字（Packet Socket）将接收所有数据包（Packet）。

<a id="r_ga85181972ff090b930361df798ea2ed0b"></a>

```c
#define NET_PACKET_MR_ALLMULTI 2
```

相关声明：[NET_PACKET_MR_ALLMULTI](#ga85181972ff090b930361df798ea2ed0b)。

分组套接字（Packet Socket）将接收所有多播数据包（Multicast Packet）。

<a id="r_ga75ffcc08e621c2d47d1ae043fce2acad"></a>

```c
#define net_ipaddr_copy(dest, src)
```

相关声明：[net_ipaddr_copy](#ga75ffcc08e621c2d47d1ae043fce2acad)。

复制 IPv4 或 IPv6 地址（Address）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_ga8b4cfadf1b284e52d6905ca88657b48a"></a>

```c
typedef unsigned short int net_sa_family_t
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[net_sa_family_t](#ga8b4cfadf1b284e52d6905ca88657b48a)。

套接字地址族类型（Socket Address Family Type）。

<a id="r_ga361fe60d9b96001f74363788352858a0"></a>

```c
typedef uint32_t net_socklen_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_socklen_t](#ga361fe60d9b96001f74363788352858a0)。

套接字地址（Socket Address）的长度。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_gaf06819bf427cc58be1229b27b373ca31"></a>

```c
enum net_ip_protocol { NET_IPPROTO_IP = 0 , NET_IPPROTO_ICMP = 1 , NET_IPPROTO_IGMP = 2 , NET_IPPROTO_ETH_P_ALL = 3 , NET_IPPROTO_IPIP = 4 , NET_IPPROTO_TCP = 6 , NET_IPPROTO_UDP = 17 , NET_IPPROTO_IPV6 = 41 , NET_IPPROTO_ICMPV6 = 58 , NET_IPPROTO_RAW = 255 }
```

相关声明：[net_ip_protocol](#gaf06819bf427cc58be1229b27b373ca31)、[NET_IPPROTO_IP](#ggaf06819bf427cc58be1229b27b373ca31a41d4bfab7d2a68dd7b707eb70ed88b41)、[NET_IPPROTO_ICMP](#ggaf06819bf427cc58be1229b27b373ca31a195a3c7b388ce05b61f64c9c9be9a092)、[NET_IPPROTO_IGMP](#ggaf06819bf427cc58be1229b27b373ca31a6ea6f123682a20c7895fd867504ada89)、[NET_IPPROTO_ETH_P_ALL](#ggaf06819bf427cc58be1229b27b373ca31aebe8a029d9f87fb41c5f11b6366c1692)、[NET_IPPROTO_IPIP](#ggaf06819bf427cc58be1229b27b373ca31ace713634caddd3efe8190dc0988b87a1)、[NET_IPPROTO_TCP](#ggaf06819bf427cc58be1229b27b373ca31a0ecceb13b5404e0699fa368306aeda25)、[NET_IPPROTO_UDP](#ggaf06819bf427cc58be1229b27b373ca31a3a5c18feadc81db1bf688b83120feb5a)、[NET_IPPROTO_IPV6](#ggaf06819bf427cc58be1229b27b373ca31acc28399f823adaa247347ab125eb37f4)、[NET_IPPROTO_ICMPV6](#ggaf06819bf427cc58be1229b27b373ca31a2ac71d272f68c66ce42ac81de4891896)、[NET_IPPROTO_RAW](#ggaf06819bf427cc58be1229b27b373ca31a4d7100f9fe0efb9e8ef6cb75e8c5ac97)。

来自 IANA/BSD 的协议编号（Protocol Numbers）。

<a id="r_ga721da18d2a3cfd9b3a56e9efc9f6e58b"></a>

```c
enum net_ip_protocol_secure { NET_IPPROTO_TLS_1_0 = 256 , NET_IPPROTO_TLS_1_1 = 257 , NET_IPPROTO_TLS_1_2 = 258 , NET_IPPROTO_TLS_1_3 = 259 , NET_IPPROTO_DTLS_1_0 = 272 , NET_IPPROTO_DTLS_1_2 = 273 , NET_IPPROTO_QUIC = 511 }
```

相关声明：[net_ip_protocol_secure](#ga721da18d2a3cfd9b3a56e9efc9f6e58b)、[NET_IPPROTO_TLS_1_0](#gga721da18d2a3cfd9b3a56e9efc9f6e58ba5d6d30723e865cab7561cc8c963c3658)、[NET_IPPROTO_TLS_1_1](#gga721da18d2a3cfd9b3a56e9efc9f6e58ba3f7f371f1d1729ad514f976f68738e47)、[NET_IPPROTO_TLS_1_2](#gga721da18d2a3cfd9b3a56e9efc9f6e58ba29ed7248420f90939300dffdd23bb07c)、[NET_IPPROTO_TLS_1_3](#gga721da18d2a3cfd9b3a56e9efc9f6e58bab13ec8077bb568971e80f9869b8d0529)、[NET_IPPROTO_DTLS_1_0](#gga721da18d2a3cfd9b3a56e9efc9f6e58baebb51afe0c7e1cfe37a330f6b0d72341)、[NET_IPPROTO_DTLS_1_2](#gga721da18d2a3cfd9b3a56e9efc9f6e58ba9ac0cafee2ab1cb5f16780fa17da5b8f)、[NET_IPPROTO_QUIC](#gga721da18d2a3cfd9b3a56e9efc9f6e58bab8506c41543969d01e4aaaa49c0932ab)。

TLS 协议的协议编号（Protocol Numbers）。

<a id="r_gaaab4268707dbe08348b98fb028e7aa5c"></a>

```c
enum net_sock_type { NET_SOCK_STREAM = 1 , NET_SOCK_DGRAM , NET_SOCK_RAW }
```

相关声明：[net_sock_type](#gaaab4268707dbe08348b98fb028e7aa5c)、[NET_SOCK_STREAM](#ggaaab4268707dbe08348b98fb028e7aa5ca6f049fea24a6d2d5279e736ececf3c83)、[NET_SOCK_DGRAM](#ggaaab4268707dbe08348b98fb028e7aa5caff1fd09b4fa81b8e0e8a73132c8fa3e4)、[NET_SOCK_RAW](#ggaaab4268707dbe08348b98fb028e7aa5ca892feaa0f7556622a3491683e69b6ac2)。

套接字类型（Socket Type）

<a id="r_ga7a207761e4879c140f48f93978cb2f0b"></a>

```c
enum net_ip_mtu { NET_IPV6_MTU = 1280 , NET_IPV4_MTU = 576 }
```

相关声明：[net_ip_mtu](#ga7a207761e4879c140f48f93978cb2f0b)、[NET_IPV6_MTU](#gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c)、[NET_IPV4_MTU](#gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1)。

IP 最大传输单元（Maximum Transfer Unit）。

<a id="r_gae87ef466e77ded673ed7e593d3eddffd"></a>

```c
enum net_priority { NET_PRIORITY_BK = 1 , NET_PRIORITY_BE = 0 , NET_PRIORITY_EE = 2 , NET_PRIORITY_CA = 3 , NET_PRIORITY_VI = 4 , NET_PRIORITY_VO = 5 , NET_PRIORITY_IC = 6 , NET_PRIORITY_NC = 7 }
```

相关声明：[net_priority](#gae87ef466e77ded673ed7e593d3eddffd)、[NET_PRIORITY_BK](#ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b)、[NET_PRIORITY_BE](#ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce)、[NET_PRIORITY_EE](#ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0)、[NET_PRIORITY_CA](#ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354)、[NET_PRIORITY_VI](#ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792)、[NET_PRIORITY_VO](#ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a)、[NET_PRIORITY_IC](#ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05)、[NET_PRIORITY_NC](#ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef)。

IEEE 802.1Q 附录 I.1 描述的网络数据包优先级设置（Network Packet Priority Settings）。

<a id="r_ga32e58fc83532ef57eeb6ff952f17288d"></a>

```c
enum net_addr_state { NET_ADDR_ANY_STATE = -1 , NET_ADDR_TENTATIVE = 0 , NET_ADDR_PREFERRED , NET_ADDR_DEPRECATED }
```

相关声明：[net_addr_state](#ga32e58fc83532ef57eeb6ff952f17288d)、[NET_ADDR_ANY_STATE](#gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df)、[NET_ADDR_TENTATIVE](#gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9)、[NET_ADDR_PREFERRED](#gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a)、[NET_ADDR_DEPRECATED](#gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3)。

网络地址的当前状态（Current State）。

<a id="r_gafecee2d4a331dc85ad962b81a6303e41"></a>

```c
enum net_addr_type { NET_ADDR_ANY = 0 , NET_ADDR_AUTOCONF , NET_ADDR_DHCP , NET_ADDR_MANUAL , NET_ADDR_OVERRIDABLE }
```

相关声明：[net_addr_type](#gafecee2d4a331dc85ad962b81a6303e41)、[NET_ADDR_ANY](#ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6)、[NET_ADDR_AUTOCONF](#ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006)、[NET_ADDR_DHCP](#ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db)、[NET_ADDR_MANUAL](#ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e)、[NET_ADDR_OVERRIDABLE](#ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4)。

网络地址分配给网络接口（Network Interface）的方式。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_ga9af9b1750c2db50a170e1b694df24227"></a>

```c
static bool net_ipv6_is_addr_loopback (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_loopback](#ga9af9b1750c2db50a170e1b694df24227)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为回环地址（Loopback Address）`::1`。

<a id="r_ga418a57b9f12205de21cbe83951e960bb"></a>

```c
static bool net_ipv6_is_addr_mcast (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast](#ga418a57b9f12205de21cbe83951e960bb)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为多播地址（Multicast Address）。

<a id="r_ga4314c59af790e537e384e969c58fab9d"></a>

```c
struct net_if_addr * net_if_ipv6_addr_lookup (const struct net_in6_addr *addr, struct net_if **iface)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv6_addr_lookup](#ga4314c59af790e537e384e969c58fab9d)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

<a id="r_ga9495dd7d6ef4a3251f0ba3a7508522d5"></a>

```c
static bool net_ipv6_is_my_addr (struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_my_addr](#ga9495dd7d6ef4a3251f0ba3a7508522d5)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查是否能在某个网络接口（Network Interface）中找到该 IPv6 地址。

<a id="r_gad520342d393f523c56a98fa618876b54"></a>

```c
struct net_if_mcast_addr * net_if_ipv6_maddr_lookup (const struct net_in6_addr *addr, struct net_if **iface)
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)、[net_if_ipv6_maddr_lookup](#gad520342d393f523c56a98fa618876b54)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

<a id="r_ga19bff1dd7eb407e25842ce28e04b08d9"></a>

```c
static bool net_ipv6_is_my_maddr (struct net_in6_addr *maddr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_my_maddr](#ga19bff1dd7eb407e25842ce28e04b08d9)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查是否能在某个网络接口（Network Interface）中找到该 IPv6 多播地址（Multicast Address）。

<a id="r_ga9654007b0a3c4d033df1ec3d00bd26ee"></a>

```c
static bool net_ipv6_is_prefix (const uint8_t *addr1, const uint8_t *addr2, uint8_t length)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_prefix](#ga9654007b0a3c4d033df1ec3d00bd26ee)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查应用前缀掩码（Prefix Mask）后，两个 IPv6 地址是否相同。

<a id="r_ga4e91a4298604a916731bf591acc7b326"></a>

```c
static void net_ipv6_addr_prefix_mask (const uint8_t *inaddr, uint8_t *outaddr, uint8_t prefix_len)
```

相关声明：[net_ipv6_addr_prefix_mask](#ga4e91a4298604a916731bf591acc7b326)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过单播地址（Unicast Address）和前缀掩码（Prefix Mask）获取 IPv6 网络地址（Network Address）。

<a id="r_ga6379fc7d08ed2668ac917fd370a80ef1"></a>

```c
static bool net_ipv4_is_addr_loopback (const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_is_addr_loopback](#ga6379fc7d08ed2668ac917fd370a80ef1)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查 IPv4 地址是否为回环地址（Loopback Address），即 `127.0.0.0/8` 范围内的地址。

<a id="r_ga403e318543fe3707bc9773b9b646610a"></a>

```c
static bool net_ipv4_is_addr_unspecified (const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_is_addr_unspecified](#ga403e318543fe3707bc9773b9b646610a)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查 IPv4 地址是否为未指定地址（Unspecified Address），即所有位均为零。

<a id="r_ga2f25895894c9a24467000118464a8ffe"></a>

```c
static bool net_ipv4_is_addr_mcast (const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_is_addr_mcast](#ga2f25895894c9a24467000118464a8ffe)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查 IPv4 地址是否为多播地址（Multicast Address）。

<a id="r_ga6651e4feab1a236888e85049a9ef8066"></a>

```c
static bool net_ipv4_is_ll_addr (const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_is_ll_addr](#ga6651e4feab1a236888e85049a9ef8066)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查给定的 IPv4 地址是否为链路本地地址（Link Local Address）。

<a id="r_gadce220ef01f6f329152e74f2143cbaa3"></a>

```c
static bool net_ipv4_is_private_addr (const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_is_private_addr](#gadce220ef01f6f329152e74f2143cbaa3)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查给定的 IPv4 地址是否属于私有地址范围（Private Address Range）。

<a id="r_gaf731738fb1761208739976d767736f87"></a>

```c
static void net_ipv4_addr_copy_raw (uint8_t *dest, const uint8_t *src)
```

相关声明：[net_ipv4_addr_copy_raw](#gaf731738fb1761208739976d767736f87)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

复制 IPv4 地址的原始缓冲区（Raw Buffer）。

<a id="r_ga4925e6f3734b8fc1d9cb1ca1a510b5f1"></a>

```c
static void net_ipv6_addr_copy_raw (uint8_t *dest, const uint8_t *src)
```

相关声明：[net_ipv6_addr_copy_raw](#ga4925e6f3734b8fc1d9cb1ca1a510b5f1)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

复制 IPv6 地址的原始缓冲区（Raw Buffer）。

<a id="r_ga32ffb42c62169ac9b34a0faa7c7ffd12"></a>

```c
static bool net_ipv4_addr_cmp_raw (const uint8_t *addr1, const uint8_t *addr2)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_addr_cmp_raw](#ga32ffb42c62169ac9b34a0faa7c7ffd12)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

比较两个原始 IPv4 地址缓冲区（Raw IPv4 Address Buffer）。

<a id="r_ga204eae0889a15f6369da607a705cb059"></a>

```c
static bool net_ipv4_addr_cmp (const struct net_in_addr *addr1, const struct net_in_addr *addr2)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_addr_cmp](#ga204eae0889a15f6369da607a705cb059)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

比较两个 IPv4 地址（Address）。

<a id="r_ga6704d86fb9962bdb6d27a41d4053bfc7"></a>

```c
static bool net_ipv6_addr_cmp (const struct net_in6_addr *addr1, const struct net_in6_addr *addr2)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_addr_cmp](#ga6704d86fb9962bdb6d27a41d4053bfc7)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

比较两个 IPv6 地址（Address）。

<a id="r_gafbe40461a645cf11fc8b3a07e1d9156e"></a>

```c
static bool net_ipv6_addr_cmp_raw (const uint8_t *addr1, const uint8_t *addr2)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_addr_cmp_raw](#gafbe40461a645cf11fc8b3a07e1d9156e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

比较两个原始 IPv6 地址缓冲区（Raw IPv6 Address Buffer）。

<a id="r_gad072b3bf7bc05927fe27f5503a31f25c"></a>

```c
static bool net_ipv6_is_ll_addr (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_ll_addr](#gad072b3bf7bc05927fe27f5503a31f25c)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查给定的 IPv6 地址是否为链路本地地址（Link Local Address）。

<a id="r_gaec37f4f9d223e5be3c141ec1ae4ef288"></a>

```c
static bool net_ipv6_is_sl_addr (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_sl_addr](#gaec37f4f9d223e5be3c141ec1ae4ef288)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查给定的 IPv6 地址是否为站点本地地址（Site Local Address）。

<a id="r_ga096d280f0373e50c4d40fb1b3dac2b2c"></a>

```c
static bool net_ipv6_is_ula_addr (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_ula_addr](#ga096d280f0373e50c4d40fb1b3dac2b2c)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查给定的 IPv6 地址是否为唯一本地地址（Unique Local Address）。

<a id="r_gab2d4e2746a080ff0dfbb67a8e09c15b4"></a>

```c
static bool net_ipv6_is_global_addr (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_global_addr](#gab2d4e2746a080ff0dfbb67a8e09c15b4)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查给定的 IPv6 地址是否为全局地址（Global Address）。

<a id="r_ga3d471601814ad2f4c2f9e6fb91055067"></a>

```c
static bool net_ipv6_is_private_addr (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_private_addr](#ga3d471601814ad2f4c2f9e6fb91055067)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查给定的 IPv6 地址是否属于私有／本地地址范围（Private/Local Address Range）。

<a id="r_gaf41e178ed45d6a483e240f939cd2f41d"></a>

```c
const struct net_in6_addr * net_ipv6_unspecified_address (void)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_ipv6_unspecified_address](#gaf41e178ed45d6a483e240f939cd2f41d)。

返回指向 IPv6 任意地址（Any Address，所有位均为零）的指针。

<a id="r_gac01309e4ca866366921148fa9ef74b4f"></a>

```c
const struct net_in_addr * net_ipv4_unspecified_address (void)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_ipv4_unspecified_address](#gac01309e4ca866366921148fa9ef74b4f)。

返回指向 IPv4 任意地址（Any Address，所有位均为零）的指针。

<a id="r_ga1d87e71e47d20a815dfd6acedb27bb98"></a>

```c
const struct net_in_addr * net_ipv4_broadcast_address (void)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_ipv4_broadcast_address](#ga1d87e71e47d20a815dfd6acedb27bb98)。

返回指向 IPv4 广播地址（Broadcast Address，所有位均为一）的指针。

<a id="r_ga919149bde5d0f1319ba60a9b8de1a1bc"></a>

```c
bool net_if_ipv4_addr_mask_cmp (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_mask_cmp](#ga919149bde5d0f1319ba60a9b8de1a1bc)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

<a id="r_ga49d57fb1fa9db8f5fb357daab9b5cc87"></a>

```c
static bool net_ipv4_addr_mask_cmp (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_addr_mask_cmp](#ga49d57fb1fa9db8f5fb357daab9b5cc87)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查给定地址是否属于为该接口（Interface）配置的同一子网（Subnet）。

<a id="r_ga45774258112186b5989b974df934dff1"></a>

```c
bool net_if_ipv4_is_addr_bcast (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_is_addr_bcast](#ga45774258112186b5989b974df934dff1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

<a id="r_gaff4efbe342d50083aaf33c994d864fcd"></a>

```c
static bool net_ipv4_is_addr_bcast (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_is_addr_bcast](#gaff4efbe342d50083aaf33c994d864fcd)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查给定的 IPv4 地址是否为广播地址（Broadcast Address）。

<a id="r_ga53fb4ce0130fc8d665ddfd466d2a5eb8"></a>

```c
struct net_if_addr * net_if_ipv4_addr_lookup (const struct net_in_addr *addr, struct net_if **iface)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv4_addr_lookup](#ga53fb4ce0130fc8d665ddfd466d2a5eb8)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

<a id="r_ga62623cbb70b70c87c05ba25cfd4b06c0"></a>

```c
static bool net_ipv4_is_my_addr (const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv4_is_my_addr](#ga62623cbb70b70c87c05ba25cfd4b06c0)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查该 IPv4 地址是否已分配给系统中的任意网络接口（Network Interface）。

<a id="r_ga2a2c730105721706af1fddad5bf9be2e"></a>

```c
static bool net_ipv6_is_addr_unspecified (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_unspecified](#ga2a2c730105721706af1fddad5bf9be2e)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为未指定地址（Unspecified Address），即所有位均为零。

<a id="r_gaacd8f2ea7894a0abb7a3d43a1ef60c29"></a>

```c
static bool net_ipv6_is_addr_solicited_node (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_solicited_node](#gaacd8f2ea7894a0abb7a3d43a1ef60c29)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为 RFC 3513 定义的被请求节点多播地址（Solicited Node Multicast Address）`FF02:0:0:0:0:1:FFXX:XXXX`。

<a id="r_ga91b134a31f3e29889a11bd3da518c483"></a>

```c
static bool net_ipv6_is_addr_mcast_scope (const struct net_in6_addr *addr, int scope)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_scope](#ga91b134a31f3e29889a11bd3da518c483)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为给定作用域（Scope）的多播地址（Multicast Address），即 `FFyx::`。

<a id="r_gac2616b300be2e4b7ed7e0ddffa5234f1"></a>

```c
static bool net_ipv6_is_same_mcast_scope (const struct net_in6_addr *addr_1, const struct net_in6_addr *addr_2)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_same_mcast_scope](#gac2616b300be2e4b7ed7e0ddffa5234f1)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否具有相同的多播作用域（Multicast Scope），即 `FFyx::`。

<a id="r_ga7fe843d70cbb04a6f4c022483346ad23"></a>

```c
static int net_ipv6_get_addr_mcast_scope (const struct net_in6_addr *addr)
```

相关声明：[net_ipv6_get_addr_mcast_scope](#ga7fe843d70cbb04a6f4c022483346ad23)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

返回给定 IPv6 地址的作用域（Scope）。

<a id="r_gaf91b9c08e327589eb0fd33d5754743cf"></a>

```c
static bool net_ipv6_is_addr_mcast_global (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_global](#gaf91b9c08e327589eb0fd33d5754743cf)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为全局多播地址（Global Multicast Address）`FFxE::/16`。

<a id="r_ga43b6e313f5a938d688d3bc734a299408"></a>

```c
static bool net_ipv6_is_addr_mcast_iface (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_iface](#ga43b6e313f5a938d688d3bc734a299408)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为接口作用域多播地址（Interface Scope Multicast Address）`FFx1::`。

<a id="r_gae1660acfdbf897afbc6119ae608e476f"></a>

```c
static bool net_ipv6_is_addr_mcast_link (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_link](#gae1660acfdbf897afbc6119ae608e476f)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为链路本地作用域多播地址（Link Local Scope Multicast Address）`FFx2::`。

<a id="r_ga2a508682693ec99b8006a1a1026772ea"></a>

```c
static bool net_ipv6_is_addr_mcast_mesh (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_mesh](#ga2a508682693ec99b8006a1a1026772ea)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为网状网络本地作用域多播地址（Mesh-local Scope Multicast Address）`FFx3::`。

<a id="r_ga9084b403ca6a591d24f975e669560b6c"></a>

```c
static bool net_ipv6_is_addr_mcast_site (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_site](#ga9084b403ca6a591d24f975e669560b6c)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为站点作用域多播地址（Site Scope Multicast Address）`FFx5::`。

<a id="r_ga9e7bf1c3503039c78f99f3deab277d4f"></a>

```c
static bool net_ipv6_is_addr_mcast_org (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_org](#ga9e7bf1c3503039c78f99f3deab277d4f)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为组织作用域多播地址（Organization Scope Multicast Address）`FFx8::`。

<a id="r_gaa559a6315ce432c9bc180b14cafa978f"></a>

```c
static bool net_ipv6_is_addr_mcast_group (const struct net_in6_addr *addr, const struct net_in6_addr *group)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_group](#gaa559a6315ce432c9bc180b14cafa978f)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

检查 IPv6 地址是否属于特定多播组（Multicast Group）。

<a id="r_gac20bcc70c84cff88fa68e1ab583da35f"></a>

```c
static bool net_ipv6_is_addr_mcast_all_nodes_group (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_all_nodes_group](#gac20bcc70c84cff88fa68e1ab583da35f)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否属于所有节点多播组（All Nodes Multicast Group）。

<a id="r_gae9ac492caeb14ab3796fcbb752c6d7f1"></a>

```c
static bool net_ipv6_is_addr_mcast_iface_all_nodes (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_iface_all_nodes](#gae9ac492caeb14ab3796fcbb752c6d7f1)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为接口作用域所有节点多播地址（Interface Scope All Nodes Multicast Address）`FF01::1`。

<a id="r_gabc3691a9ff73dcadadf52ec740cb0e99"></a>

```c
static bool net_ipv6_is_addr_mcast_link_all_nodes (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_is_addr_mcast_link_all_nodes](#gabc3691a9ff73dcadadf52ec740cb0e99)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查 IPv6 地址是否为链路本地作用域所有节点多播地址（Link Local Scope All Nodes Multicast Address）`FF02::1`。

<a id="r_gadf685d461f89090441348d2028082078"></a>

```c
static void net_ipv6_addr_create_solicited_node (const struct net_in6_addr *src, struct net_in6_addr *dst)
```

相关声明：[net_ipv6_addr_create_solicited_node](#gadf685d461f89090441348d2028082078)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

创建 RFC 3513 定义的被请求节点 IPv6 多播地址（Solicited Node IPv6 Multicast Address）`FF02:0:0:0:0:1:FFXX:XXXX`。

<a id="r_gaaed285ea1b276ad90404957560f82c77"></a>

```c
static void net_ipv6_addr_create (struct net_in6_addr *addr, uint16_t addr0, uint16_t addr1, uint16_t addr2, uint16_t addr3, uint16_t addr4, uint16_t addr5, uint16_t addr6, uint16_t addr7)
```

相关声明：[net_ipv6_addr_create](#gaaed285ea1b276ad90404957560f82c77)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用八个 16 位字（Word）构造 IPv6 地址。

<a id="r_ga677fe0c0ebe6bcdd6a7a7d7805841671"></a>

```c
static void net_ipv6_addr_create_ll_allnodes_mcast (struct net_in6_addr *addr)
```

相关声明：[net_ipv6_addr_create_ll_allnodes_mcast](#ga677fe0c0ebe6bcdd6a7a7d7805841671)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

创建链路本地所有节点多播 IPv6 地址（Link Local All-nodes Multicast IPv6 Address）。

<a id="r_gae20b3c01d1ee1fe7526b58eb4c0bf98c"></a>

```c
static void net_ipv6_addr_create_ll_allrouters_mcast (struct net_in6_addr *addr)
```

相关声明：[net_ipv6_addr_create_ll_allrouters_mcast](#gae20b3c01d1ee1fe7526b58eb4c0bf98c)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

创建链路本地所有路由器多播 IPv6 地址（Link Local All-routers Multicast IPv6 Address）。

<a id="r_ga2a9657d756c655322d960ef54f4b9ac4"></a>

```c
static void net_ipv6_addr_create_v4_mapped (const struct net_in_addr *addr4, struct net_in6_addr *addr6)
```

相关声明：[net_ipv6_addr_create_v4_mapped](#ga2a9657d756c655322d960ef54f4b9ac4)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

创建 IPv4 映射的 IPv6 地址（IPv4 Mapped IPv6 Address）。

<a id="r_ga2716cdb6f85693d7c5a96446a7a41e03"></a>

```c
static bool net_ipv6_addr_is_v4_mapped (const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_addr_is_v4_mapped](#ga2716cdb6f85693d7c5a96446a7a41e03)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

判断 IPv6 地址是否为 IPv4 映射地址（IPv4 Mapped Address）。

<a id="r_ga744f26c0e560ba2b6682c40c27b53f62"></a>

```c
static void net_ipv6_addr_get_v4_mapped (const struct net_in6_addr *addr6, struct net_in_addr *addr4)
```

相关声明：[net_ipv6_addr_get_v4_mapped](#ga744f26c0e560ba2b6682c40c27b53f62)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

从 IPv4 映射的 IPv6 地址（IPv4 Mapped IPv6 Address）中获取 IPv4 地址。

<a id="r_ga5aef9855e39e03a4ce2d6626040c8ae9"></a>

```c
int net_ipv6_addr_generate_iid (struct net_if *iface, const struct net_in6_addr *prefix, uint8_t *network_id, size_t network_id_len, uint8_t dad_counter, struct net_in6_addr *addr, struct net_linkaddr *lladdr)
```

相关声明：[net_ipv6_addr_generate_iid](#ga5aef9855e39e03a4ce2d6626040c8ae9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

使用前缀（Prefix）和接口标识符（Interface Identifier）生成 IPv6 地址。

<a id="r_ga871cb575f79b9e53834c13bfc9e5bd82"></a>

```c
static void net_ipv6_addr_create_iid (struct net_in6_addr *addr, struct net_linkaddr *lladdr)
```

相关声明：[net_ipv6_addr_create_iid](#ga871cb575f79b9e53834c13bfc9e5bd82)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

创建 IPv6 地址的接口标识符（Interface Identifier）。

<a id="r_ga7946673bd60ca80392d4440e23028f54"></a>

```c
static bool net_ipv6_addr_based_on_ll (const struct net_in6_addr *addr, const struct net_linkaddr *lladdr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipv6_addr_based_on_ll](#ga7946673bd60ca80392d4440e23028f54)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

检查给定地址是否基于链路层地址（Link Layer Address）。

<a id="r_ga13b4094cc06599c9af46e5e68e1c3bc3"></a>

```c
static ALWAYS_INLINE struct net_sockaddr * net_sad (const struct net_sockaddr_storage *addr)
```

相关声明：[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_sad](#ga13b4094cc06599c9af46e5e68e1c3bc3)。

从 `net_sockaddr_storage` 获取 `net_sockaddr`。

<a id="r_ga83d4270557a164eef75e1ae656470ef1"></a>

```c
static ALWAYS_INLINE struct net_sockaddr_storage * net_sas (const struct net_sockaddr *addr)
```

相关声明：[net_sas](#ga83d4270557a164eef75e1ae656470ef1)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

从 `net_sockaddr` 获取 `net_sockaddr_storage`。

<a id="r_ga4e7578614f7f0660c5a62d7746a3772c"></a>

```c
static ALWAYS_INLINE struct net_sockaddr_in6 * net_sin6 (const struct net_sockaddr *addr)
```

相关声明：[net_sockaddr_in6](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md)、[net_sin6](#ga4e7578614f7f0660c5a62d7746a3772c)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

从 `net_sockaddr` 获取 `net_sockaddr_in6`。

<a id="r_gaf92aa225bda78a3e016f6120b60c8885"></a>

```c
static ALWAYS_INLINE struct net_sockaddr_in * net_sin (const struct net_sockaddr *addr)
```

相关声明：[net_sockaddr_in](../network_core_model_reference/P119_net_sockaddr_in_结构体.md)、[net_sin](#gaf92aa225bda78a3e016f6120b60c8885)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

从 `net_sockaddr` 获取 `net_sockaddr_in`。

<a id="r_gad4ed43b91fbaa2844fa509c603fafae6"></a>

```c
static ALWAYS_INLINE struct net_sockaddr_in6_ptr * net_sin6_ptr (const struct net_sockaddr_ptr *addr)
```

相关声明：[net_sin6_ptr](#gad4ed43b91fbaa2844fa509c603fafae6)。

从 `net_sockaddr_ptr` 获取 `net_sockaddr_in6_ptr`。

<a id="r_ga6943b9d84c55709aaad323c1127a1949"></a>

```c
static ALWAYS_INLINE struct net_sockaddr_in_ptr * net_sin_ptr (const struct net_sockaddr_ptr *addr)
```

相关声明：[net_sin_ptr](#ga6943b9d84c55709aaad323c1127a1949)。

从 `sockaddr_ptr` 获取 `net_sockaddr_in_ptr`。

<a id="r_ga8846a826e8b69c01fc92239a596ca002"></a>

```c
static ALWAYS_INLINE struct net_sockaddr_ll_ptr * net_sll_ptr (const struct net_sockaddr_ptr *addr)
```

相关声明：[net_sll_ptr](#ga8846a826e8b69c01fc92239a596ca002)。

从 `sockaddr_ptr` 获取 `net_sockaddr_ll_ptr`。

<a id="r_gab1b5d776e0b10043c0538629ed4a5b8b"></a>

```c
static ALWAYS_INLINE struct net_sockaddr_can_ptr * net_can_ptr (const struct net_sockaddr_ptr *addr)
```

相关声明：[net_can_ptr](#gab1b5d776e0b10043c0538629ed4a5b8b)。

从 `net_sockaddr_ptr` 获取 `net_sockaddr_can_ptr`。

<a id="r_ga63f48d08fc2811198739ce20a72584df"></a>

```c
int net_addr_pton (net_sa_family_t family, const char *src, void *dst)
```

相关声明：[net_addr_pton](#ga63f48d08fc2811198739ce20a72584df)、[net_sa_family_t](#ga8b4cfadf1b284e52d6905ca88657b48a)。

将字符串（String）转换为 IP 地址。

<a id="r_gafbc331616a5360c68804e8bc2f653cdd"></a>

```c
char * net_addr_ntop (net_sa_family_t family, const void *src, char *dst, size_t size)
```

相关声明：[net_addr_ntop](#gafbc331616a5360c68804e8bc2f653cdd)、[net_sa_family_t](#ga8b4cfadf1b284e52d6905ca88657b48a)。

将 IP 地址转换为字符串形式（String Form）。

<a id="r_ga646cd9e85f7110bc45dc276bf8e31ef1"></a>

```c
int net_mask_len_to_netmask (net_sa_family_t family, uint8_t mask_len, struct net_sockaddr *mask)
```

相关声明：[net_mask_len_to_netmask](#ga646cd9e85f7110bc45dc276bf8e31ef1)、[net_sa_family_t](#ga8b4cfadf1b284e52d6905ca88657b48a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

根据掩码长度（Mask Length）创建网络掩码（Netmask）。

<a id="r_ga84d11fc7badd399d2c164ed21baa87c9"></a>

```c
int net_netmask_to_mask_len (net_sa_family_t family, struct net_sockaddr *mask, uint8_t *mask_len)
```

相关声明：[net_netmask_to_mask_len](#ga84d11fc7badd399d2c164ed21baa87c9)、[net_sa_family_t](#ga8b4cfadf1b284e52d6905ca88657b48a)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据网络掩码（Netmask）生成掩码长度（Mask Length）。

<a id="r_ga9086c7f94792f5af574b6eb14a6261b1"></a>

```c
bool net_ipaddr_parse (const char *str, size_t str_len, struct net_sockaddr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_ipaddr_parse](#ga9086c7f94792f5af574b6eb14a6261b1)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

解析包含 IPv4 或 IPv6 地址以及可选端口（Port）的字符串，并将信息存入用户提供的 `sockaddr` 结构体。

<a id="r_ga5e1650330284b6e295e5f714037b1d65"></a>

```c
const char * net_ipaddr_parse_mask (const char *str, size_t str_len, struct net_sockaddr *addr, uint8_t *mask_len)
```

相关声明：[net_ipaddr_parse_mask](#ga5e1650330284b6e295e5f714037b1d65)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解析包含 IPv4 或 IPv6 地址以及可选掩码长度（Mask Length）的字符串，并将信息存入用户提供的 `sockaddr` 结构体。

<a id="r_ga45f18bd1ec2040f9f21b5aaf4ffe696d"></a>

```c
int net_port_set_default (struct net_sockaddr *addr, uint16_t default_port)
```

相关声明：[net_port_set_default](#ga45f18bd1ec2040f9f21b5aaf4ffe696d)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 `sockaddr` 结构体中的默认端口（Default Port）。

<a id="r_ga78436f11373210789ed9d5d640c6daf7"></a>

```c
int net_port_set (struct net_sockaddr *addr, uint16_t port)
```

相关声明：[net_port_set](#ga78436f11373210789ed9d5d640c6daf7)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 `sockaddr` 结构体中的端口（Port）。

<a id="r_ga0b67ffabad5b8a10da72301681206b31"></a>

```c
int net_port_get (struct net_sockaddr *addr, uint16_t *port)
```

相关声明：[net_port_get](#ga0b67ffabad5b8a10da72301681206b31)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 `sockaddr` 结构体中的端口（Port）。

<a id="r_ga8047c58777b659f8a8cdb2f24ca24355"></a>

```c
static bool net_sockaddr_cmp (const struct net_sockaddr *a, const struct net_sockaddr *b)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_sockaddr_cmp](#ga8047c58777b659f8a8cdb2f24ca24355)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

比较套接字地址（Socket Address）。

<a id="r_ga1695009388402938dcc2e49b526ebd1f"></a>

```c
static int32_t net_tcp_seq_cmp (uint32_t seq1, uint32_t seq2)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[net_tcp_seq_cmp](#ga1695009388402938dcc2e49b526ebd1f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

比较 TCP 序列号（Sequence Number）。

<a id="r_gaa77b299f53e5535ac4c4bea1b6531a34"></a>

```c
static bool net_tcp_seq_greater (uint32_t seq1, uint32_t seq2)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_tcp_seq_greater](#gaa77b299f53e5535ac4c4bea1b6531a34)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查其中一个 TCP 序列号（Sequence Number）是否更大。

<a id="r_ga8b794f251cf8412c769ab415902a9f32"></a>

```c
int net_bytes_from_str (uint8_t *buf, int buf_len, const char *src)
```

相关声明：[net_bytes_from_str](#ga8b794f251cf8412c769ab415902a9f32)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将十六进制值字符串（Hex Values String）转换为字节数组（Byte Array）。

<a id="r_gae74c9ba7ff4addbce7f931bd6fa91fa0"></a>

```c
int net_tx_priority2tc (enum net_priority prio)
```

相关声明：[net_tx_priority2tc](#gae74c9ba7ff4addbce7f931bd6fa91fa0)、[net_priority](#gae87ef466e77ded673ed7e593d3eddffd)。

将发送网络数据包优先级（TX Network Packet Priority）转换为流量类别（Traffic Class），以便将数据包放入正确的发送队列（TX Queue）。

<a id="r_ga7b3c41ae9b3962090d72c130a9fa61b1"></a>

```c
int net_rx_priority2tc (enum net_priority prio)
```

相关声明：[net_rx_priority2tc](#ga7b3c41ae9b3962090d72c130a9fa61b1)、[net_priority](#gae87ef466e77ded673ed7e593d3eddffd)。

将接收网络数据包优先级（RX Network Packet Priority）转换为流量类别（Traffic Class），以便将数据包放入正确的接收队列（RX Queue）。

<a id="r_ga14bc7018e3dd7c3e320b44a077343ce4"></a>

```c
static enum net_priority net_vlan2priority (uint8_t priority)
```

相关声明：[net_priority](#gae87ef466e77ded673ed7e593d3eddffd)、[net_vlan2priority](#ga14bc7018e3dd7c3e320b44a077343ce4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将网络数据包的 VLAN 优先级（VLAN Priority）转换为网络数据包优先级（Network Packet Priority），以便将数据包放入正确的队列。

<a id="r_ga8be77d043d4d1d29e0879b3b22274629"></a>

```c
static uint8_t net_priority2vlan (enum net_priority priority)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_priority2vlan](#ga8be77d043d4d1d29e0879b3b22274629)、[net_priority](#gae87ef466e77ded673ed7e593d3eddffd)。

将网络数据包优先级（Network Packet Priority）转换为网络数据包的 VLAN 优先级（VLAN Priority）。

<a id="r_ga4c35814a1f56101f96e790d0dc97925b"></a>

```c
const char * net_family2str (net_sa_family_t family)
```

相关声明：[net_family2str](#ga4c35814a1f56101f96e790d0dc97925b)、[net_sa_family_t](#ga8b4cfadf1b284e52d6905ca88657b48a)。

以字符串形式返回网络地址族值（Network Address Family Value）。

<a id="r_ga0d22051f0ff5545b9b08e133804389f1"></a>

```c
static size_t net_family2size (net_sa_family_t family)
```

相关声明：[net_family2size](#ga0d22051f0ff5545b9b08e133804389f1)、[net_sa_family_t](#ga8b4cfadf1b284e52d6905ca88657b48a)。

返回给定地址族（Address Family）的网络地址大小（Network Address Size）。

<a id="r_gaa1f6ecf0788bac4ca943011f0ad87fb9"></a>

```c
static int net_ipv6_pe_add_filter (struct net_in6_addr *addr, bool is_denylist)
```

相关声明：[net_ipv6_pe_add_filter](#gaa1f6ecf0788bac4ca943011f0ad87fb9)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将 IPv6 前缀（Prefix）添加为隐私扩展过滤条件（Privacy Extension Filter）。

<a id="r_gac3bb5fb48ed95d43a7beb2e4f7c1c6d0"></a>

```c
static int net_ipv6_pe_del_filter (struct net_in6_addr *addr)
```

相关声明：[net_ipv6_pe_del_filter](#gac3bb5fb48ed95d43a7beb2e4f7c1c6d0)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

从隐私扩展过滤条件列表（Privacy Extension Filter List）中删除 IPv6 前缀（Prefix）。

## 2.6\_详细说明（Detailed Documentation）

<a id="ga1df641bd5978219a7da51ea25ea8ac2f"></a>

### `NET_AF_CAN`

```c
#define NET_AF_CAN NET_PF_CAN
```

```c
#include <zephyr/net/net_ip.h>
```

控制器局域网（Controller Area Network）。

<a id="gac53da21004b2bdc93b878da2ec4590bd"></a>

### `NET_AF_INET`

```c
#define NET_AF_INET NET_PF_INET
```

```c
#include <zephyr/net/net_ip.h>
```

IP 协议族版本 4（IP Protocol Family Version 4）。

<a id="ga502492205736b373fa35c0524ba3d4e6"></a>

### `NET_AF_INET6`

```c
#define NET_AF_INET6 NET_PF_INET6
```

```c
#include <zephyr/net/net_ip.h>
```

IP 协议族版本 6（IP Protocol Family Version 6）。

<a id="ga67f6049571b9326f646a2b6ad5e29778"></a>

### `NET_AF_LOCAL`

```c
#define NET_AF_LOCAL NET_PF_LOCAL
```

```c
#include <zephyr/net/net_ip.h>
```

进程间通信（Inter-process Communication）。

<a id="ga209390ff940aa0f0746c3a4fd4e98806"></a>

### `NET_AF_NET_MGMT`

```c
#define NET_AF_NET_MGMT NET_PF_NET_MGMT
```

```c
#include <zephyr/net/net_ip.h>
```

网络管理信息（Network Management Info）。

<a id="ga090f4770cd630517b5391d36e3705e41"></a>

### `NET_AF_PACKET`

```c
#define NET_AF_PACKET NET_PF_PACKET
```

```c
#include <zephyr/net/net_ip.h>
```

分组协议族（Packet Family）。

<a id="ga88930e91e400b4eca0a9392288490268"></a>

### `NET_AF_UNIX`

```c
#define NET_AF_UNIX NET_PF_UNIX
```

```c
#include <zephyr/net/net_ip.h>
```

进程间通信（Inter-process Communication）。

<a id="ga8702e764fa49396587469a102870b109"></a>

### `NET_AF_UNSPEC`

```c
#define NET_AF_UNSPEC NET_PF_UNSPEC
```

```c
#include <zephyr/net/net_ip.h>
```

未指定的地址族（Unspecified Address Family）。

<a id="ga00f6b79613665e424a343d78203ef915"></a>

### `NET_CMSG_DATA`

```c
#define NET_CMSG_DATA ( cmsg)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
((uint8_t *)(cmsg) + NET_ALIGN_D(sizeof(struct net_cmsghdr)))
```

返回指向 `cmsghdr` 的数据部分（Data Portion）的指针。

不能假定返回的指针满足任意载荷数据类型（Payload Data Types）的对齐要求。应用程序不应将其强制转换为与载荷匹配的指针类型，而应使用 `memcpy(3)`，在该位置与一个按所需类型正确声明的对象之间复制数据。

<a id="ga1d17cfa3d3f1a6b5f3fe6476ef2db74f"></a>

### `NET_CMSG_FIRSTHDR`

```c
#define NET_CMSG_FIRSTHDR ( msghdr)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
((msghdr)->msg_controllen >= sizeof(struct net_cmsghdr) ? \
 (struct net_cmsghdr *)((msghdr)->msg_control) : NULL)
```

返回指针，指向传入的 `msghdr` 所关联的辅助数据缓冲区（Ancillary Data Buffer）中的第一个 `cmsghdr`。

如果缓冲区中没有足够空间容纳 `cmsghdr`，则返回 `NULL`。

<a id="ga4fc63db80b096eacc2b5b06e2fd2563b"></a>

### `NET_CMSG_LEN`

```c
#define NET_CMSG_LEN ( length)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
(NET_ALIGN_D(sizeof(struct net_cmsghdr)) + length)
```

返回应存入 `net_cmsghdr` 结构体的 `cmsg_len` 成员的值，并计入必要的对齐（Alignment）。

以数据长度（Data Length）作为参数。

<a id="ga99a82490600a896e44a0d76e1d318950"></a>

### `NET_CMSG_NXTHDR`

```c
#define NET_CMSG_NXTHDR ( msghdr, cmsg )
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
(((cmsg) == NULL) ? NET_CMSG_FIRSTHDR(msghdr) :                  \
 (((cmsg)->cmsg_len < sizeof(struct net_cmsghdr) ||              \
   (cmsg)->cmsg_len > (size_t)((uint8_t *)((msghdr)->msg_control) + \
                               (msghdr)->msg_controllen -        \
                               (uint8_t *)(cmsg)) ||             \
   (uint8_t *)(cmsg) + NET_ALIGN_H((cmsg)->cmsg_len) +           \
   NET_ALIGN_D(sizeof(struct net_cmsghdr)) >                     \
   (uint8_t *)((msghdr)->msg_control) + (msghdr)->msg_controllen) ? \
  NULL :                                                         \
  (struct net_cmsghdr *)((uint8_t *)(cmsg) +                     \
                         NET_ALIGN_H((cmsg)->cmsg_len))))
```

返回传入的 `cmsghdr` 之后的下一个有效 `cmsghdr`。

当缓冲区剩余空间不足，或传入的 `cmsghdr` 长度无效时，返回 `NULL`。无效长度包括：小到无法容纳一个头，例如缓冲区中尚未使用且已清零的部分；或大于缓冲区剩余空间。

<a id="ga47a68c5c03dd7dbcc6222772ffe1bbb7"></a>

### `NET_CMSG_SPACE`

```c
#define NET_CMSG_SPACE ( length)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
(NET_ALIGN_D(sizeof(struct net_cmsghdr)) + NET_ALIGN_H(length))
```

返回辅助元素（Ancillary Element）占用的字节数；该元素的载荷（Payload）长度为传入的数据长度。

<a id="ga5d9e16e8f439be6f94fb3f72de13bdac"></a>

### `net_htonl`

```c
#define net_htonl ( x)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
sys_cpu_to_be32(x)
```

将 32 位值从主机字节序（Host Byte Order）转换为网络字节序（Network Byte Order）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 要转换的主机字节序（Host Byte Order）值。 |

**返回（Returns）**：返回值：网络字节序（Network Byte Order）值。

<a id="ga7f215d5ef1d4098a7e8681500796a8f5"></a>

### `net_htonll`

```c
#define net_htonll ( x)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
sys_cpu_to_be64(x)
```

将 64 位值从主机字节序（Host Byte Order）转换为网络字节序（Network Byte Order）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 要转换的主机字节序（Host Byte Order）值。 |

**返回（Returns）**：返回值：网络字节序（Network Byte Order）值。

<a id="gae20291eed240d648d0ef7e13822f925f"></a>

### `net_htons`

```c
#define net_htons ( x)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
sys_cpu_to_be16(x)
```

将 16 位值从主机字节序（Host Byte Order）转换为网络字节序（Network Byte Order）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 要转换的主机字节序（Host Byte Order）值。 |

**返回（Returns）**：返回值：网络字节序（Network Byte Order）值。

<a id="ga3903cb074f334a50fd88815d2795773e"></a>

### `NET_IN6ADDR_ANY_INIT`

```c
#define NET_IN6ADDR_ANY_INIT
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
{ { { 0, 0, 0, 0, 0, 0, 0, 0,        \
0, 0, 0, 0, 0, 0, 0, 0 } } }
```

IPv6 地址初始化器（Address Initializer）。

<a id="ga2987743eae5556c7374060ed3d392c2a"></a>

### `NET_IN6ADDR_LOOPBACK_INIT`

```c
#define NET_IN6ADDR_LOOPBACK_INIT
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
{ { { 0, 0, 0, 0, 0, 0, 0, 0,   \
0, 0, 0, 0, 0, 0, 0, 1 } } }
```

IPv6 回环地址初始化器（Loopback Address Initializer）。

<a id="gaf38d9372d95e8a3a7d502fe3eceb4e50"></a>

### `NET_INADDR_ANY`

```c
#define NET_INADDR_ANY 0
```

```c
#include <zephyr/net/net_ip.h>
```

IPv4 任意地址（Any Address）。

<a id="gae117b1066c227a95aec0dd4b41000b5f"></a>

### `NET_INADDR_ANY_INIT`

```c
#define NET_INADDR_ANY_INIT { { { NET_INADDR_ANY } } }
```

```c
#include <zephyr/net/net_ip.h>
```

IPv4 地址初始化器（Address Initializer）。

<a id="ga24a1863f48c95c94fb438a545428ca91"></a>

### `NET_INADDR_BROADCAST`

```c
#define NET_INADDR_BROADCAST 0xffffffff
```

```c
#include <zephyr/net/net_ip.h>
```

IPv4 广播地址（Broadcast Address）。

<a id="ga4672091907479da6b09ac78f01aa5cf0"></a>

### `NET_INADDR_LOOPBACK_INIT`

```c
#define NET_INADDR_LOOPBACK_INIT { { { 127, 0, 0, 1 } } }
```

```c
#include <zephyr/net/net_ip.h>
```

IPv4 回环地址初始化器（Loopback Address Initializer）。

<a id="ga29969b236fa78c479836cbd143b099f3"></a>

### `NET_INET6_ADDRSTRLEN`

```c
#define NET_INET6_ADDRSTRLEN 46
```

```c
#include <zephyr/net/net_ip.h>
```

IPv6 地址字符串（Address String）的最大长度。

会考虑可能存在的映射 IPv4 地址（Mapped IPv4 Addresses）。

<a id="gae864ce227183974771322ba07f8c493d"></a>

### `NET_INET_ADDRSTRLEN`

```c
#define NET_INET_ADDRSTRLEN 16
```

```c
#include <zephyr/net/net_ip.h>
```

IPv4 地址字符串（Address String）的最大长度。

由 POSIX 定义。

<a id="ga75ffcc08e621c2d47d1ae043fce2acad"></a>

### `net_ipaddr_copy`

```c
#define net_ipaddr_copy ( dest, src )
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
UNALIGNED_PUT(UNALIGNED_GET(src), dest)
```

复制 IPv4 或 IPv6 地址（Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dest` | 目标 IP 地址（Destination IP Address）。 |
| `src` | 源 IP 地址（Source IP Address）。 |

**返回（Returns）**：返回值：目标地址（Destination Address）。

<a id="ga10a82ea9ba9ca19f3b773bdd53c978e0"></a>

### `NET_IPV4_ADDR_SIZE`

```c
#define NET_IPV4_ADDR_SIZE 4
```

```c
#include <zephyr/net/net_ip.h>
```

IPv4 地址的二进制大小（Binary Size）。

<a id="ga1eefdabf590090be9f98bdf4a2f43bb4"></a>

### `NET_IPV6_ADDR_SIZE`

```c
#define NET_IPV6_ADDR_SIZE 16
```

```c
#include <zephyr/net/net_ip.h>
```

IPv6 地址的二进制大小（Binary Size）。

<a id="ga5b32bdfc249437709bb25bd95ec7d6d7"></a>

### `NET_MAX_PRIORITIES`

```c
#define NET_MAX_PRIORITIES 8
```

```c
#include <zephyr/net/net_ip.h>
```

优先级值（Priority Values）的数量。

<a id="gae18466011462c20add53de2e01505b92"></a>

### `net_ntohl`

```c
#define net_ntohl ( x)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
sys_be32_to_cpu(x)
```

将 32 位值从网络字节序（Network Byte Order）转换为主机字节序（Host Byte Order）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 要转换的网络字节序（Network Byte Order）值。 |

**返回（Returns）**：返回值：主机字节序（Host Byte Order）值。

<a id="ga35f36b83b652246e9a61c9ddfdfed4f5"></a>

### `net_ntohll`

```c
#define net_ntohll ( x)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
sys_be64_to_cpu(x)
```

将 64 位值从网络字节序（Network Byte Order）转换为主机字节序（Host Byte Order）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 要转换的网络字节序（Network Byte Order）值。 |

**返回（Returns）**：返回值：主机字节序（Host Byte Order）值。

<a id="ga4837ff0eece26b00ae46ed7c16997a97"></a>

### `net_ntohs`

```c
#define net_ntohs ( x)
```

```c
#include <zephyr/net/net_ip.h>
```

展开值（Value）：

```c
sys_be16_to_cpu(x)
```

将 16 位值从网络字节序（Network Byte Order）转换为主机字节序（Host Byte Order）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 要转换的网络字节序（Network Byte Order）值。 |

**返回（Returns）**：返回值：主机字节序（Host Byte Order）值。

<a id="ga85181972ff090b930361df798ea2ed0b"></a>

### `NET_PACKET_MR_ALLMULTI`

```c
#define NET_PACKET_MR_ALLMULTI 2
```

```c
#include <zephyr/net/net_ip.h>
```

分组套接字（Packet Socket）将接收所有多播数据包（Multicast Packet）。

<a id="gae65887fe7fe408c886764d07b0c30547"></a>

### `NET_PACKET_MR_MULTICAST`

```c
#define NET_PACKET_MR_MULTICAST 0
```

```c
#include <zephyr/net/net_ip.h>
```

分组套接字（Packet Socket）的多播过滤类型（Multicast Filtering Types）。

仅接收特定组播数据包（Multicast Packets）。

<a id="gaa54e835a1878a5c044dc20fdc563078d"></a>

### `NET_PACKET_MR_PROMISC`

```c
#define NET_PACKET_MR_PROMISC 1
```

```c
#include <zephyr/net/net_ip.h>
```

分组套接字（Packet Socket）将接收所有数据包（Packet）。

<a id="ga84228eb6b051e8ec5a8b4ed5aaa3119f"></a>

### `NET_PF_CAN`

```c
#define NET_PF_CAN 4
```

```c
#include <zephyr/net/net_ip.h>
```

控制器局域网（Controller Area Network）。

<a id="ga3a490b5c27b98ce39dbbeb35e62fa9e0"></a>

### `NET_PF_INET`

```c
#define NET_PF_INET 1
```

```c
#include <zephyr/net/net_ip.h>
```

IP 协议族版本 4（IP Protocol Family Version 4）。

<a id="gad794203c740ef6a24604092f3b4125e3"></a>

### `NET_PF_INET6`

```c
#define NET_PF_INET6 2
```

```c
#include <zephyr/net/net_ip.h>
```

IP 协议族版本 6（IP Protocol Family Version 6）。

<a id="gaf062d3e0ca938d2b41c2c7f6c92d8c49"></a>

### `NET_PF_LOCAL`

```c
#define NET_PF_LOCAL 6
```

```c
#include <zephyr/net/net_ip.h>
```

进程间通信（Inter-process Communication）。

<a id="ga99cfb4cf13b61a0b9f11b6c12bf58371"></a>

### `NET_PF_NET_MGMT`

```c
#define NET_PF_NET_MGMT 5
```

```c
#include <zephyr/net/net_ip.h>
```

网络管理信息（Network Management Info）。

<a id="ga54ea7d2c3dfe6f1753891da3a94cc1f0"></a>

### `NET_PF_PACKET`

```c
#define NET_PF_PACKET 3
```

```c
#include <zephyr/net/net_ip.h>
```

分组协议族（Packet Family）。

<a id="gae9118bc697bcec58fe265899d6ca7149"></a>

### `NET_PF_UNIX`

```c
#define NET_PF_UNIX NET_PF_LOCAL
```

```c
#include <zephyr/net/net_ip.h>
```

进程间通信（Inter-process Communication）。

<a id="gaff57ad0fabd8cdd422cf8777b3d94602"></a>

### `NET_PF_UNSPEC`

```c
#define NET_PF_UNSPEC 0
```

```c
#include <zephyr/net/net_ip.h>
```

未指定的协议族（Unspecified Protocol Family）。

<a id="ga929a6597b2a4669e42cb416a84fd568f"></a>

### `SOCKADDR_ALIGN`

```c
#define SOCKADDR_ALIGN (4)
```

```c
#include <zephyr/net/net_ip.h>
```

<a id="ga8b4cfadf1b284e52d6905ca88657b48a"></a>

### `net_sa_family_t`

```c
typedef unsigned short int net_sa_family_t
```

```c
#include <zephyr/net/net_ip.h>
```

套接字地址族类型（Socket Address Family Type）。

<a id="ga361fe60d9b96001f74363788352858a0"></a>

### `net_socklen_t`

```c
typedef uint32_t net_socklen_t
```

```c
#include <zephyr/net/net_ip.h>
```

套接字地址（Socket Address）的长度。

<a id="ga32e58fc83532ef57eeb6ff952f17288d"></a>

### `net_addr_state`

```c
enum net_addr_state
```

```c
#include <zephyr/net/net_ip.h>
```

网络地址的当前状态（Current State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_ADDR_ANY_STATE` | 默认地址类型（Default Address Type），无效值。 |
| `NET_ADDR_TENTATIVE` | 暂定地址（Tentative Address）。 |
| `NET_ADDR_PREFERRED` | 首选地址（Preferred Address）。 |
| `NET_ADDR_DEPRECATED` | 已弃用地址（Deprecated Address）。 |

<a id="gafecee2d4a331dc85ad962b81a6303e41"></a>

### `net_addr_type`

```c
enum net_addr_type
```

```c
#include <zephyr/net/net_ip.h>
```

网络地址分配给网络接口（Network Interface）的方式。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_ADDR_ANY` | 默认值（Default Value），此值无效。 |
| `NET_ADDR_AUTOCONF` | 自动配置地址（Auto Configured Address）。 |
| `NET_ADDR_DHCP` | 通过动态主机配置协议（DHCP）获取的地址。 |
| `NET_ADDR_MANUAL` | 手动设置的地址（Manually Set Address）。 |
| `NET_ADDR_OVERRIDABLE` | 手动设置、但可被 DHCP 覆盖的地址。 |

<a id="ga7a207761e4879c140f48f93978cb2f0b"></a>

### `net_ip_mtu`

```c
enum net_ip_mtu
```

```c
#include <zephyr/net/net_ip.h>
```

IP 最大传输单元（Maximum Transfer Unit）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_IPV6_MTU` | IPv6 最大传输单元（MTU）长度。必须能够在不分片（Fragmentation）的情况下接收此大小的 IPv6 数据包。 |
| `NET_IPV4_MTU` | IPv4 最大传输单元（MTU）长度。必须能够在不分片（Fragmentation）的情况下接收此大小的 IPv4 数据包。 |

<a id="gaf06819bf427cc58be1229b27b373ca31"></a>

### `net_ip_protocol`

```c
enum net_ip_protocol
```

```c
#include <zephyr/net/net_ip.h>
```

来自 IANA/BSD 的协议编号（Protocol Numbers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_IPPROTO_IP` | IP 协议，用于 `setsockopt()` 的伪值（Pseudo-value）。 |
| `NET_IPPROTO_ICMP` | 互联网控制报文协议（ICMP）。 |
| `NET_IPPROTO_IGMP` | 互联网组管理协议（IGMP）。 |
| `NET_IPPROTO_ETH_P_ALL` | 所有数据包（Every Packet），定义来自 Linux 的 `if_ether.h`。 |
| `NET_IPPROTO_IPIP` | IP-in-IP 隧道（IPIP Tunnels）。 |
| `NET_IPPROTO_TCP` | 传输控制协议（TCP）。 |
| `NET_IPPROTO_UDP` | 用户数据报协议（UDP）。 |
| `NET_IPPROTO_IPV6` | 互联网协议第 6 版（IPv6）。 |
| `NET_IPPROTO_ICMPV6` | IPv6 互联网控制报文协议（ICMPv6）。 |
| `NET_IPPROTO_RAW` | 原始 IP 数据包（RAW IP Packets）。 |

<a id="ga721da18d2a3cfd9b3a56e9efc9f6e58b"></a>

### `net_ip_protocol_secure`

```c
enum net_ip_protocol_secure
```

```c
#include <zephyr/net/net_ip.h>
```

TLS 协议的协议编号（Protocol Numbers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_IPPROTO_TLS_1_0` | 传输层安全协议（TLS）1.0。 |
| `NET_IPPROTO_TLS_1_1` | 传输层安全协议（TLS）1.1。 |
| `NET_IPPROTO_TLS_1_2` | 传输层安全协议（TLS）1.2。 |
| `NET_IPPROTO_TLS_1_3` | 传输层安全协议（TLS）1.3。 |
| `NET_IPPROTO_DTLS_1_0` | 数据报传输层安全协议（DTLS）1.0。 |
| `NET_IPPROTO_DTLS_1_2` | 数据报传输层安全协议（DTLS）1.2。 |
| `NET_IPPROTO_QUIC` | QUIC 协议。 |

<a id="gae87ef466e77ded673ed7e593d3eddffd"></a>

### `net_priority`

```c
enum net_priority
```

```c
#include <zephyr/net/net_ip.h>
```

IEEE 802.1Q 附录 I.1 描述的网络数据包优先级设置（Network Packet Priority Settings）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_PRIORITY_BK` | 后台（Background），最低优先级。 |
| `NET_PRIORITY_BE` | 尽力而为（Best Effort），默认优先级。 |
| `NET_PRIORITY_EE` | 优良尽力服务（Excellent Effort）。 |
| `NET_PRIORITY_CA` | 关键应用（Critical Applications）。 |
| `NET_PRIORITY_VI` | 视频（Video），延迟和抖动小于 100 ms。 |
| `NET_PRIORITY_VO` | 语音（Voice），延迟和抖动小于 10 ms。 |
| `NET_PRIORITY_IC` | 网间控制（Internetwork Control）。 |
| `NET_PRIORITY_NC` | 网络控制（Network Control），最高优先级。 |

<a id="gaaab4268707dbe08348b98fb028e7aa5c"></a>

### `net_sock_type`

```c
enum net_sock_type
```

```c
#include <zephyr/net/net_ip.h>
```

套接字类型（Socket Type）

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_SOCK_STREAM` | 流式套接字类型（Stream Socket Type）。 |
| `NET_SOCK_DGRAM` | 数据报套接字类型（Datagram Socket Type）。 |
| `NET_SOCK_RAW` | 原始套接字类型（RAW Socket Type）。 |

<a id="gafbc331616a5360c68804e8bc2f653cdd"></a>

### `net_addr_ntop()`

```c
char * net_addr_ntop ( net_sa_family_t family, const void * src, char * dst, size_t size )
```

```c
#include <zephyr/net/net_ip.h>
```

将 IP 地址转换为字符串形式（String Form）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `family` | IP 地址族（Address Family），为 `NET_AF_INET` 或 `NET_AF_INET6`。 |
| `src` | `family` 为 `NET_AF_INET` 时，指向 `struct net_in_addr`；为 `NET_AF_INET6` 时，指向 `struct net_in6_addr`。 |
| `dst` | 用于存放以空字符结尾的 IP 地址字符串的缓冲区（Buffer）。 |
| `size` | 缓冲区（Buffer）中可用的字节数。 |

**返回（Returns）**：返回值：成功时为 `dst` 指针，出错时为 `NULL`。

<a id="ga63f48d08fc2811198739ce20a72584df"></a>

### `net_addr_pton()`

```c
int net_addr_pton ( net_sa_family_t family, const char * src, void * dst )
```

```c
#include <zephyr/net/net_ip.h>
```

将字符串（String）转换为 IP 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `family` | IP 地址族（Address Family），为 `NET_AF_INET` 或 `NET_AF_INET6`。 |
| `src` | 以空字符结尾的 IP 地址字符串。 |
| `dst` | `family` 为 `NET_AF_INET` 时，指向 `struct net_in_addr`；为 `NET_AF_INET6` 时，指向 `struct net_in6_addr`。 |

**说明（Note）**：注意：此函数不会执行精确的错误检查，不要用于不可信字符串（Untrusted Strings）。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga8b794f251cf8412c769ab415902a9f32"></a>

### `net_bytes_from_str()`

```c
int net_bytes_from_str ( uint8_t * buf, int buf_len, const char * src )
```

```c
#include <zephyr/net/net_ip.h>
```

将十六进制值字符串（Hex Values String）转换为字节数组（Byte Array）。

字符串语法为 `ab:02:98:fa:42:01`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向用于写入这些字节的内存（Memory）的指针。 |
| `buf_len` | 内存区域（Memory Area）的长度。 |
| `src` | 字节字符串（String of Bytes）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gab1b5d776e0b10043c0538629ed4a5b8b"></a>

### `net_can_ptr()`

```c
ALWAYS_INLINE struct net_sockaddr_can_ptr * net_can_ptr ( const struct net_sockaddr_ptr * addr)
```

声明属性：`static`。

```c
#include <zephyr/net/net_ip.h>
```

从 `net_sockaddr_ptr` 获取 `net_sockaddr_can_ptr`。

这是一个辅助函数，可缩短需要此功能的代码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 套接字地址（Socket Address）。 |

**返回（Returns）**：返回值：指向 CAN 套接字地址（Socket Address）的指针。

<a id="ga0d22051f0ff5545b9b08e133804389f1"></a>

### `net_family2size()`

```c
size_t net_family2size ( net_sa_family_t family)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

返回给定地址族（Address Family）的网络地址大小（Network Address Size）。

IP 协议族第 4 版（IP Protocol Family Version 4）。译注：原文开头的 `<` 是注释标记残留。

IP 协议族第 4 版（IP Protocol Family Version 4）。译注：原文开头的 `<` 是注释标记残留。

IP 协议族第 6 版（IP Protocol Family Version 6）。译注：原文开头的 `<` 是注释标记残留。

IP 协议族第 6 版（IP Protocol Family Version 6）。译注：原文开头的 `<` 是注释标记残留。

数据包地址族（Packet Family）。译注：原文开头的 `<` 是注释标记残留。

数据包地址族（Packet Family）。译注：原文开头的 `<` 是注释标记残留。

进程间通信（Inter-process Communication）。译注：原文开头的 `<` 是注释标记残留。

进程间通信（Inter-process Communication）。译注：原文开头的 `<` 是注释标记残留。

进程间通信（Inter-process Communication）。译注：原文开头的 `<` 是注释标记残留。

控制器局域网（Controller Area Network，CAN）。译注：原文开头的 `<` 是注释标记残留。

控制器局域网（Controller Area Network，CAN）。译注：原文开头的 `<` 是注释标记残留。

网络管理信息（Network Management Info）。译注：原文开头的 `<` 是注释标记残留。

网络管理信息（Network Management Info）。译注：原文开头的 `<` 是注释标记残留。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `family` | 网络地址族代码（Network Address Family Code）。 |

**返回（Returns）**：返回值：网络地址大小（Network Address Size）；地址族未知时为 0。

<a id="ga4c35814a1f56101f96e790d0dc97925b"></a>

### `net_family2str()`

```c
const char * net_family2str ( net_sa_family_t family)
```

```c
#include <zephyr/net/net_ip.h>
```

以字符串形式返回网络地址族值（Network Address Family Value）。

仅用于调试（Debugging）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `family` | 网络地址族代码（Network Address Family Code）。 |

**返回（Returns）**：返回值：网络地址族（Network Address Family）的字符串；地址族未知时为 `NULL`。

<a id="ga53fb4ce0130fc8d665ddfd466d2a5eb8"></a>

### `net_if_ipv4_addr_lookup()`

```c
struct net_if_addr * net_if_ipv4_addr_lookup ( const struct net_in_addr * addr, struct net_if ** iface )
```

声明属性：`extern`。

```c
#include <zephyr/net/net_ip.h>
```

<a id="ga919149bde5d0f1319ba60a9b8de1a1bc"></a>

### `net_if_ipv4_addr_mask_cmp()`

```c
bool net_if_ipv4_addr_mask_cmp ( struct net_if * iface, const struct net_in_addr * addr )
```

声明属性：`extern`。

```c
#include <zephyr/net/net_ip.h>
```

<a id="ga45774258112186b5989b974df934dff1"></a>

### `net_if_ipv4_is_addr_bcast()`

```c
bool net_if_ipv4_is_addr_bcast ( struct net_if * iface, const struct net_in_addr * addr )
```

声明属性：`extern`。

```c
#include <zephyr/net/net_ip.h>
```

<a id="ga4314c59af790e537e384e969c58fab9d"></a>

### `net_if_ipv6_addr_lookup()`

```c
struct net_if_addr * net_if_ipv6_addr_lookup ( const struct net_in6_addr * addr, struct net_if ** iface )
```

声明属性：`extern`。

```c
#include <zephyr/net/net_ip.h>
```

<a id="gad520342d393f523c56a98fa618876b54"></a>

### `net_if_ipv6_maddr_lookup()`

```c
struct net_if_mcast_addr * net_if_ipv6_maddr_lookup ( const struct net_in6_addr * addr, struct net_if ** iface )
```

声明属性：`extern`。

```c
#include <zephyr/net/net_ip.h>
```

<a id="ga9086c7f94792f5af574b6eb14a6261b1"></a>

### `net_ipaddr_parse()`

```c
bool net_ipaddr_parse ( const char * str, size_t str_len, struct net_sockaddr * addr )
```

```c
#include <zephyr/net/net_ip.h>
```

解析包含 IPv4 或 IPv6 地址以及可选端口（Port）的字符串，并将信息存入用户提供的 `sockaddr` 结构体。

IP 地址字符串语法：`192.0.2.1:80`、`192.0.2.42`。

`[2001:db8::2]`、`2001:db::42`。注意：`str_len` 参数用于限制检查的字符数量。如果字符串不含端口号（Port Number），则不修改 `sockaddr` 中的端口号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 包含IP地址的字符串。 |
| `str_len` | 待解析字符串（String）的长度。 |
| `addr` | 指向用户提供的 `struct sockaddr` 的指针。 |

返回（Returns）：能够解析时为true，否则为false。

<a id="ga5e1650330284b6e295e5f714037b1d65"></a>

### `net_ipaddr_parse_mask()`

```c
const char * net_ipaddr_parse_mask ( const char * str, size_t str_len, struct net_sockaddr * addr, uint8_t * mask_len )
```

```c
#include <zephyr/net/net_ip.h>
```

解析包含 IPv4 或 IPv6 地址以及可选掩码长度（Mask Length）的字符串，并将信息存入用户提供的 `sockaddr` 结构体。

可以包含多个以逗号或空格分隔的 IP 地址。函数返回指向字符串中下一个 IP 地址的指针。

IP 地址字符串语法：`192.0.2.1/24`、`192.0.2.42`、`2001:db8::1/64`、`2001:db8::2`、`2001:db::42/128`；也可以写成逗号分隔的 `2001:db8::1/64,192.0.2.1,2001:db8::2,192.0.2.2/24`，或空格分隔的 `2001:db8::1/64 192.0.2.1 2001:db8::2 192.0.2.2/24`。注意：`str_len` 参数用于限制检查的字符数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 包含IP地址的字符串。 |
| `str_len` | 待解析字符串（String）的长度。 |
| `addr` | 指向用户提供的 `struct sockaddr` 的指针。 |
| `mask_len` | 指向 `mask_len` 的指针，用于将掩码长度返回给调用者。 |

**返回（Returns）**：返回值：解析出错时为 `NULL`；成功解析 IP 地址且没有其他内容要解析时为 `""`；其他值均指向字符串中逗号 `,` 或空格之后的下一个字符。

<a id="ga204eae0889a15f6369da607a705cb059"></a>

### `net_ipv4_addr_cmp()`

```c
bool net_ipv4_addr_cmp ( const struct net_in_addr * addr1, const struct net_in_addr * addr2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

比较两个 IPv4 地址（Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr1` | 指向 IPv4 地址的指针。 |
| `addr2` | 指向 IPv4 地址的指针。 |

**返回（Returns）**：**返回值（Returns）：**地址相同返回 `true`，否则返回 `false`。

<a id="ga32ffb42c62169ac9b34a0faa7c7ffd12"></a>

### `net_ipv4_addr_cmp_raw()`

```c
bool net_ipv4_addr_cmp_raw ( const uint8_t * addr1, const uint8_t * addr2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

比较两个原始 IPv4 地址缓冲区（Raw IPv4 Address Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr1` | 指向 IPv4 地址缓冲区（Buffer）的指针。 |
| `addr2` | 指向 IPv4 地址缓冲区（Buffer）的指针。 |

**返回（Returns）**：**返回值（Returns）：**地址相同返回 `true`，否则返回 `false`。

<a id="gaf731738fb1761208739976d767736f87"></a>

### `net_ipv4_addr_copy_raw()`

```c
void net_ipv4_addr_copy_raw ( uint8_t * dest, const uint8_t * src )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

复制 IPv4 地址的原始缓冲区（Raw Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dest` | 目标 IP 地址（Destination IP Address）。 |
| `src` | 源 IP 地址（Source IP Address）。 |

<a id="ga49d57fb1fa9db8f5fb357daab9b5cc87"></a>

### `net_ipv4_addr_mask_cmp()`

```c
bool net_ipv4_addr_mask_cmp ( struct net_if * iface, const struct net_in_addr * addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定地址是否属于为该接口（Interface）配置的同一子网（Subnet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向接口（Interface）的有效指针。 |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值：地址处于同一子网（Subnet）时为 `true`，否则为 `false`。

<a id="ga1d87e71e47d20a815dfd6acedb27bb98"></a>

### `net_ipv4_broadcast_address()`

```c
const struct net_in_addr * net_ipv4_broadcast_address ( void )
```

```c
#include <zephyr/net/net_ip.h>
```

返回指向 IPv4 广播地址（Broadcast Address，所有位均为一）的指针。

**返回（Returns）**：返回值：IPv4 广播地址（Broadcast Address）。

<a id="gaff4efbe342d50083aaf33c994d864fcd"></a>

### `net_ipv4_is_addr_bcast()`

```c
bool net_ipv4_is_addr_bcast ( struct net_if * iface, const struct net_in_addr * addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定的 IPv4 地址是否为广播地址（Broadcast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface），必须是有效的接口指针。 |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值：地址为广播地址（Broadcast Address）时为 `true`，否则为 `false`。

<a id="ga6379fc7d08ed2668ac917fd370a80ef1"></a>

### `net_ipv4_is_addr_loopback()`

```c
bool net_ipv4_is_addr_loopback ( const struct net_in_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv4 地址是否为回环地址（Loopback Address），即 `127.0.0.0/8` 范围内的地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值：地址为环回地址（Loopback Address）时为 `true`，否则为 `false`。

<a id="ga2f25895894c9a24467000118464a8ffe"></a>

### `net_ipv4_is_addr_mcast()`

```c
bool net_ipv4_is_addr_mcast ( const struct net_in_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv4 地址是否为多播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值：地址为组播地址（Multicast Address）时为 `true`，否则为 `false`。

<a id="ga403e318543fe3707bc9773b9b646610a"></a>

### `net_ipv4_is_addr_unspecified()`

```c
bool net_ipv4_is_addr_unspecified ( const struct net_in_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv4 地址是否为未指定地址（Unspecified Address），即所有位均为零。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值：地址为未指定地址（Unspecified Address）时为 `true`，否则为 `false`。

<a id="ga6651e4feab1a236888e85049a9ef8066"></a>

### `net_ipv4_is_ll_addr()`

```c
bool net_ipv4_is_ll_addr ( const struct net_in_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定的 IPv4 地址是否为链路本地地址（Link Local Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向 IPv4 地址的有效指针。 |

**返回（Returns）**：返回值：满足判断条件时为 `true`，否则为 `false`。

<a id="ga62623cbb70b70c87c05ba25cfd4b06c0"></a>

### `net_ipv4_is_my_addr()`

```c
bool net_ipv4_is_my_addr ( const struct net_in_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查该 IPv4 地址是否已分配给系统中的任意网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向 IPv4 地址的有效指针。 |

**返回（Returns）**：返回值：在某个网络接口（Network Interface）中找到该 IPv4 地址时为 `true`，否则为 `false`。

<a id="gadce220ef01f6f329152e74f2143cbaa3"></a>

### `net_ipv4_is_private_addr()`

```c
bool net_ipv4_is_private_addr ( const struct net_in_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定的 IPv4 地址是否属于私有地址范围（Private Address Range）。

详情参见 https://en.wikipedia.org/wiki/Reserved_IP_addresses 。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向 IPv4 地址的有效指针。 |

**返回（Returns）**：返回值：满足判断条件时为 `true`，否则为 `false`。

<a id="gac01309e4ca866366921148fa9ef74b4f"></a>

### `net_ipv4_unspecified_address()`

```c
const struct net_in_addr * net_ipv4_unspecified_address ( void )
```

```c
#include <zephyr/net/net_ip.h>
```

返回指向 IPv4 任意地址（Any Address，所有位均为零）的指针。

**返回（Returns）**：返回值：任意 IPv4 地址（Any IPv4 Address）。

<a id="ga7946673bd60ca80392d4440e23028f54"></a>

### `net_ipv6_addr_based_on_ll()`

```c
bool net_ipv6_addr_based_on_ll ( const struct net_in6_addr * addr, const struct net_linkaddr * lladdr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定地址是否基于链路层地址（Link Layer Address）。

**返回（Returns）**：返回值：满足判断条件时为 `true`，否则为 `false`。

<a id="ga6704d86fb9962bdb6d27a41d4053bfc7"></a>

### `net_ipv6_addr_cmp()`

```c
bool net_ipv6_addr_cmp ( const struct net_in6_addr * addr1, const struct net_in6_addr * addr2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

比较两个 IPv6 地址（Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr1` | 指向 IPv6 地址的指针。 |
| `addr2` | 指向 IPv6 地址的指针。 |

**返回（Returns）**：**返回值（Returns）：**地址相同返回 `true`，否则返回 `false`。

<a id="gafbe40461a645cf11fc8b3a07e1d9156e"></a>

### `net_ipv6_addr_cmp_raw()`

```c
bool net_ipv6_addr_cmp_raw ( const uint8_t * addr1, const uint8_t * addr2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

比较两个原始 IPv6 地址缓冲区（Raw IPv6 Address Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr1` | 指向 IPv6 地址缓冲区（Buffer）的指针。 |
| `addr2` | 指向 IPv6 地址缓冲区（Buffer）的指针。 |

**返回（Returns）**：**返回值（Returns）：**地址相同返回 `true`，否则返回 `false`。

<a id="ga4925e6f3734b8fc1d9cb1ca1a510b5f1"></a>

### `net_ipv6_addr_copy_raw()`

```c
void net_ipv6_addr_copy_raw ( uint8_t * dest, const uint8_t * src )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

复制 IPv6 地址的原始缓冲区（Raw Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dest` | 目标 IP 地址（Destination IP Address）。 |
| `src` | 源 IP 地址（Source IP Address）。 |

<a id="gaaed285ea1b276ad90404957560f82c77"></a>

### `net_ipv6_addr_create()`

```c
void net_ipv6_addr_create ( struct net_in6_addr * addr, uint16_t addr0, uint16_t addr1, uint16_t addr2, uint16_t addr3, uint16_t addr4, uint16_t addr5, uint16_t addr6, uint16_t addr7 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

使用八个 16 位字（Word）构造 IPv6 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |
| `addr0` | 作为地址一部分的 16 位字（Word）。 |
| `addr1` | 作为地址一部分的 16 位字（Word）。 |
| `addr2` | 作为地址一部分的 16 位字（Word）。 |
| `addr3` | 作为地址一部分的 16 位字（Word）。 |
| `addr4` | 作为地址一部分的 16 位字（Word）。 |
| `addr5` | 作为地址一部分的 16 位字（Word）。 |
| `addr6` | 作为地址一部分的 16 位字（Word）。 |
| `addr7` | 作为地址一部分的 16 位字（Word）。 |

<a id="ga871cb575f79b9e53834c13bfc9e5bd82"></a>

### `net_ipv6_addr_create_iid()`

```c
void net_ipv6_addr_create_iid ( struct net_in6_addr * addr, struct net_linkaddr * lladdr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

创建 IPv6 地址的接口标识符（Interface Identifier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |
| `lladdr` | 链路本地地址（Link-local Address）。 |

<a id="ga677fe0c0ebe6bcdd6a7a7d7805841671"></a>

### `net_ipv6_addr_create_ll_allnodes_mcast()`

```c
void net_ipv6_addr_create_ll_allnodes_mcast ( struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

创建链路本地所有节点多播 IPv6 地址（Link Local All-nodes Multicast IPv6 Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

<a id="gae20b3c01d1ee1fe7526b58eb4c0bf98c"></a>

### `net_ipv6_addr_create_ll_allrouters_mcast()`

```c
void net_ipv6_addr_create_ll_allrouters_mcast ( struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

创建链路本地所有路由器多播 IPv6 地址（Link Local All-routers Multicast IPv6 Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

<a id="gadf685d461f89090441348d2028082078"></a>

### `net_ipv6_addr_create_solicited_node()`

```c
void net_ipv6_addr_create_solicited_node ( const struct net_in6_addr * src, struct net_in6_addr * dst )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

创建 RFC 3513 定义的被请求节点 IPv6 多播地址（Solicited Node IPv6 Multicast Address）`FF02:0:0:0:0:1:FFXX:XXXX`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | IPv6地址（Address）。 |
| `dst` | IPv6地址（Address）。 |

<a id="ga2a9657d756c655322d960ef54f4b9ac4"></a>

### `net_ipv6_addr_create_v4_mapped()`

```c
void net_ipv6_addr_create_v4_mapped ( const struct net_in_addr * addr4, struct net_in6_addr * addr6 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

创建 IPv4 映射的 IPv6 地址（IPv4 Mapped IPv6 Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr4` | IPv4地址（Address）。 |
| `addr6` | 要创建的 IPv6 地址。 |

<a id="ga5aef9855e39e03a4ce2d6626040c8ae9"></a>

### `net_ipv6_addr_generate_iid()`

```c
int net_ipv6_addr_generate_iid ( struct net_if * iface, const struct net_in6_addr * prefix, uint8_t * network_id, size_t network_id_len, uint8_t dad_counter, struct net_in6_addr * addr, struct net_linkaddr * lladdr )
```

```c
#include <zephyr/net/net_ip.h>
```

使用前缀（Prefix）和接口标识符（Interface Identifier）生成 IPv6 地址。

接口标识符（Interface Identifier）可以根据 RFC 4291 定义的 EUI-64（MAC）生成，也可以根据 RFC 7217 定义的随机值生成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `prefix` | IPv6 前缀（Prefix），可省略；省略时使用 `fe80::/64`。 |
| `network_id` | 网络标识符（Network Identifier），例如 WLAN 中的 SSID；此参数可选，可以设为 `NULL`。 |
| `network_id_len` | 网络标识符（Network Identifier）的长度；设为 0 时忽略网络 ID。 |
| `dad_counter` | 重复地址检测（Duplicate Address Detection，DAD）计数器值；未知时可设为 0。 |
| `addr` | IPv6地址（Address）。 |
| `lladdr` | 链路本地地址（Link-local Address）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga744f26c0e560ba2b6682c40c27b53f62"></a>

### `net_ipv6_addr_get_v4_mapped()`

```c
void net_ipv6_addr_get_v4_mapped ( const struct net_in6_addr * addr6, struct net_in_addr * addr4 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

从 IPv4 映射的 IPv6 地址（IPv4 Mapped IPv6 Address）中获取 IPv4 地址。

IPv4 映射地址（IPv4-mapped Addresses）的形式为 `::ffff:a.b.c.d`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr6` | IPv6 地址，必须是 IPv4 映射地址（IPv4-mapped Address），参见 `net_ipv6_addr_is_v4_mapped()`。 |
| `addr4` | 要填充的 IPv4 地址。 |

<a id="ga2716cdb6f85693d7c5a96446a7a41e03"></a>

### `net_ipv6_addr_is_v4_mapped()`

```c
bool net_ipv6_addr_is_v4_mapped ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

判断 IPv6 地址是否为 IPv4 映射地址（IPv4 Mapped Address）。

IPv4 映射地址（IPv4-mapped Addresses）的形式为 `::ffff:a.b.c.d`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：IPv6 地址为 IPv4 映射地址（IPv4-mapped Address）时为 `true`，否则为 `false`。

<a id="ga4e91a4298604a916731bf591acc7b326"></a>

### `net_ipv6_addr_prefix_mask()`

```c
void net_ipv6_addr_prefix_mask ( const uint8_t * inaddr, uint8_t * outaddr, uint8_t prefix_len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

通过单播地址（Unicast Address）和前缀掩码（Prefix Mask）获取 IPv6 网络地址（Network Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inaddr` | IPv6 单播地址（Unicast Address）。 |
| `outaddr` | 应用前缀掩码后的 IPv6 地址，即网络地址（Network Address）。 |
| `prefix_len` | 前缀长度（Prefix Length），最大为 128。 |

<a id="ga7fe843d70cbb04a6f4c022483346ad23"></a>

### `net_ipv6_get_addr_mcast_scope()`

```c
int net_ipv6_get_addr_mcast_scope ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

返回给定 IPv6 地址的作用域（Scope）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址的作用域（Scope）；地址不是组播地址时为 -1。

<a id="ga9af9b1750c2db50a170e1b694df24227"></a>

### `net_ipv6_is_addr_loopback()`

```c
bool net_ipv6_is_addr_loopback ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为回环地址（Loopback Address）`::1`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为环回地址（Loopback Address）时为 `true`，否则为 `false`。

<a id="ga418a57b9f12205de21cbe83951e960bb"></a>

### `net_ipv6_is_addr_mcast()`

```c
bool net_ipv6_is_addr_mcast ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为多播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为组播地址（Multicast Address）时为 `true`，否则为 `false`。

<a id="gac20bcc70c84cff88fa68e1ab583da35f"></a>

### `net_ipv6_is_addr_mcast_all_nodes_group()`

```c
bool net_ipv6_is_addr_mcast_all_nodes_group ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否属于所有节点多播组（All Nodes Multicast Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：IPv6 组播地址属于所有节点组播组（All Nodes Multicast Group）时为 `true`，否则为 `false`。

<a id="gaf91b9c08e327589eb0fd33d5754743cf"></a>

### `net_ipv6_is_addr_mcast_global()`

```c
bool net_ipv6_is_addr_mcast_global ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为全局多播地址（Global Multicast Address）`FFxE::/16`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为全局组播地址（Global Multicast Address）时为 `true`，否则为 `false`。

<a id="gaa559a6315ce432c9bc180b14cafa978f"></a>

### `net_ipv6_is_addr_mcast_group()`

```c
bool net_ipv6_is_addr_mcast_group ( const struct net_in6_addr * addr, const struct net_in6_addr * group )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否属于特定多播组（Multicast Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |
| `group` | 组 ID 的 IPv6 地址（Group ID IPv6 Address），其值必须采用网络字节序（Network Byte Order）。 |

**返回（Returns）**：返回值：IPv6 组播地址属于给定组播组（Multicast Group）时为 `true`，否则为 `false`。

<a id="ga43b6e313f5a938d688d3bc734a299408"></a>

### `net_ipv6_is_addr_mcast_iface()`

```c
bool net_ipv6_is_addr_mcast_iface ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为接口作用域多播地址（Interface Scope Multicast Address）`FFx1::`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为接口作用域组播地址（Interface Scope Multicast Address）时为 `true`，否则为 `false`。

<a id="gae9ac492caeb14ab3796fcbb752c6d7f1"></a>

### `net_ipv6_is_addr_mcast_iface_all_nodes()`

```c
bool net_ipv6_is_addr_mcast_iface_all_nodes ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为接口作用域所有节点多播地址（Interface Scope All Nodes Multicast Address）`FF01::1`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为接口作用域的所有节点组播地址（Interface Scope All Nodes Multicast Address）时为 `true`，否则为 `false`。

<a id="gae1660acfdbf897afbc6119ae608e476f"></a>

### `net_ipv6_is_addr_mcast_link()`

```c
bool net_ipv6_is_addr_mcast_link ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为链路本地作用域多播地址（Link Local Scope Multicast Address）`FFx2::`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为链路本地作用域组播地址（Link-local Scope Multicast Address）时为 `true`，否则为 `false`。

<a id="gabc3691a9ff73dcadadf52ec740cb0e99"></a>

### `net_ipv6_is_addr_mcast_link_all_nodes()`

```c
bool net_ipv6_is_addr_mcast_link_all_nodes ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为链路本地作用域所有节点多播地址（Link Local Scope All Nodes Multicast Address）`FF02::1`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为链路本地作用域的所有节点组播地址（Link-local Scope All Nodes Multicast Address）时为 `true`，否则为 `false`。

<a id="ga2a508682693ec99b8006a1a1026772ea"></a>

### `net_ipv6_is_addr_mcast_mesh()`

```c
bool net_ipv6_is_addr_mcast_mesh ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为网状网络本地作用域多播地址（Mesh-local Scope Multicast Address）`FFx3::`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为网状网络本地作用域组播地址（Mesh-local Scope Multicast Address）时为 `true`，否则为 `false`。

<a id="ga9e7bf1c3503039c78f99f3deab277d4f"></a>

### `net_ipv6_is_addr_mcast_org()`

```c
bool net_ipv6_is_addr_mcast_org ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为组织作用域多播地址（Organization Scope Multicast Address）`FFx8::`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为组织作用域组播地址（Organization Scope Multicast Address）时为 `true`，否则为 `false`。

<a id="ga91b134a31f3e29889a11bd3da518c483"></a>

### `net_ipv6_is_addr_mcast_scope()`

```c
bool net_ipv6_is_addr_mcast_scope ( const struct net_in6_addr * addr, int scope )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为给定作用域（Scope）的多播地址（Multicast Address），即 `FFyx::`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |
| `scope` | 要检查的作用域（Scope）。 |

**返回（Returns）**：返回值：地址为给定作用域（Scope）的组播地址时为 `true`，否则为 `false`。

<a id="ga9084b403ca6a591d24f975e669560b6c"></a>

### `net_ipv6_is_addr_mcast_site()`

```c
bool net_ipv6_is_addr_mcast_site ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为站点作用域多播地址（Site Scope Multicast Address）`FFx5::`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为站点作用域组播地址（Site Scope Multicast Address）时为 `true`，否则为 `false`。

<a id="gaacd8f2ea7894a0abb7a3d43a1ef60c29"></a>

### `net_ipv6_is_addr_solicited_node()`

```c
bool net_ipv6_is_addr_solicited_node ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为 RFC 3513 定义的被请求节点多播地址（Solicited Node Multicast Address）`FF02:0:0:0:0:1:FFXX:XXXX`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为被请求节点地址（Solicited-node Address）时为 `true`，否则为 `false`。

<a id="ga2a2c730105721706af1fddad5bf9be2e"></a>

### `net_ipv6_is_addr_unspecified()`

```c
bool net_ipv6_is_addr_unspecified ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否为未指定地址（Unspecified Address），即所有位均为零。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：地址为未指定地址（Unspecified Address）时为 `true`，否则为 `false`。

<a id="gab2d4e2746a080ff0dfbb67a8e09c15b4"></a>

### `net_ipv6_is_global_addr()`

```c
bool net_ipv6_is_global_addr ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定的 IPv6 地址是否为全局地址（Global Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向 IPv6 地址的有效指针。 |

**返回（Returns）**：返回值：满足判断条件时为 `true`，否则为 `false`。

<a id="gad072b3bf7bc05927fe27f5503a31f25c"></a>

### `net_ipv6_is_ll_addr()`

```c
bool net_ipv6_is_ll_addr ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定的 IPv6 地址是否为链路本地地址（Link Local Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向 IPv6 地址的有效指针。 |

**返回（Returns）**：返回值：满足判断条件时为 `true`，否则为 `false`。

<a id="ga9495dd7d6ef4a3251f0ba3a7508522d5"></a>

### `net_ipv6_is_my_addr()`

```c
bool net_ipv6_is_my_addr ( struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查是否能在某个网络接口（Network Interface）中找到该 IPv6 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值：找到地址（Address）时为 `true`，否则为 `false`。

<a id="ga19bff1dd7eb407e25842ce28e04b08d9"></a>

### `net_ipv6_is_my_maddr()`

```c
bool net_ipv6_is_my_maddr ( struct net_in6_addr * maddr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查是否能在某个网络接口（Network Interface）中找到该 IPv6 多播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `maddr` | IPv6 组播地址（Multicast Address）。 |

**返回（Returns）**：返回值：找到地址（Address）时为 `true`，否则为 `false`。

<a id="ga9654007b0a3c4d033df1ec3d00bd26ee"></a>

### `net_ipv6_is_prefix()`

```c
bool net_ipv6_is_prefix ( const uint8_t * addr1, const uint8_t * addr2, uint8_t length )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查应用前缀掩码（Prefix Mask）后，两个 IPv6 地址是否相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr1` | 第一个 IPv6 地址。 |
| `addr2` | 第二个 IPv6 地址。 |
| `length` | 前缀长度（Prefix Length），最大为 128。 |

**返回（Returns）**：返回值：IPv6 前缀（Prefixes）相同时为 `true`，否则为 `false`。

<a id="ga3d471601814ad2f4c2f9e6fb91055067"></a>

### `net_ipv6_is_private_addr()`

```c
bool net_ipv6_is_private_addr ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定的 IPv6 地址是否属于私有／本地地址范围（Private/Local Address Range）。

详情参见 https://en.wikipedia.org/wiki/Reserved_IP_addresses 。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向 IPv6 地址的有效指针。 |

**返回（Returns）**：返回值：满足判断条件时为 `true`，否则为 `false`。

<a id="gac2616b300be2e4b7ed7e0ddffa5234f1"></a>

### `net_ipv6_is_same_mcast_scope()`

```c
bool net_ipv6_is_same_mcast_scope ( const struct net_in6_addr * addr_1, const struct net_in6_addr * addr_2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查 IPv6 地址是否具有相同的多播作用域（Multicast Scope），即 `FFyx::`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr_1` | IPv6 地址 1。 |
| `addr_2` | IPv6 地址 2。 |

**返回（Returns）**：返回值：两个地址具有相同组播作用域（Multicast Scope）时为 `true`，否则为 `false`。

<a id="gaec37f4f9d223e5be3c141ec1ae4ef288"></a>

### `net_ipv6_is_sl_addr()`

```c
bool net_ipv6_is_sl_addr ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定的 IPv6 地址是否为站点本地地址（Site Local Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向 IPv6 地址的有效指针。 |

**返回（Returns）**：返回值：满足判断条件时为 `true`，否则为 `false`。

<a id="ga096d280f0373e50c4d40fb1b3dac2b2c"></a>

### `net_ipv6_is_ula_addr()`

```c
bool net_ipv6_is_ula_addr ( const struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查给定的 IPv6 地址是否为唯一本地地址（Unique Local Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向 IPv6 地址的有效指针。 |

**返回（Returns）**：返回值：满足判断条件时为 `true`，否则为 `false`。

<a id="gaa1f6ecf0788bac4ca943011f0ad87fb9"></a>

### `net_ipv6_pe_add_filter()`

```c
int net_ipv6_pe_add_filter ( struct net_in6_addr * addr, bool is_denylist )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

将 IPv6 前缀（Prefix）添加为隐私扩展过滤条件（Privacy Extension Filter）。

注意：筛选器（Filters）可以采用允许列表（Allow Listing）或拒绝列表（Deny Listing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6前缀（Prefix）。 |
| `is_denylist` | 指示此筛选器使用允许列表（Allow Listing）还是拒绝列表（Deny Listing）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gac3bb5fb48ed95d43a7beb2e4f7c1c6d0"></a>

### `net_ipv6_pe_del_filter()`

```c
int net_ipv6_pe_del_filter ( struct net_in6_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

从隐私扩展过滤条件列表（Privacy Extension Filter List）中删除 IPv6 前缀（Prefix）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6前缀（Prefix）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gaf41e178ed45d6a483e240f939cd2f41d"></a>

### `net_ipv6_unspecified_address()`

```c
const struct net_in6_addr * net_ipv6_unspecified_address ( void )
```

```c
#include <zephyr/net/net_ip.h>
```

返回指向 IPv6 任意地址（Any Address，所有位均为零）的指针。

**返回（Returns）**：返回值：任意 IPv6 地址（Any IPv6 Address）。

<a id="ga646cd9e85f7110bc45dc276bf8e31ef1"></a>

### `net_mask_len_to_netmask()`

```c
int net_mask_len_to_netmask ( net_sa_family_t family, uint8_t mask_len, struct net_sockaddr * mask )
```

```c
#include <zephyr/net/net_ip.h>
```

根据掩码长度（Mask Length）创建网络掩码（Netmask）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `family` | IP 地址族（Address Family），为 `NET_AF_INET` 或 `NET_AF_INET6`。 |
| `mask_len` | IPv4 的网络掩码长度（Netmask Length）或 IPv6 的前缀长度（Prefix Length）。 |
| `mask` | `family` 为 `NET_AF_INET` 时，指向 `struct sockaddr_in`；为 `NET_AF_INET6` 时，指向 `struct sockaddr_in6`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga84d11fc7badd399d2c164ed21baa87c9"></a>

### `net_netmask_to_mask_len()`

```c
int net_netmask_to_mask_len ( net_sa_family_t family, struct net_sockaddr * mask, uint8_t * mask_len )
```

```c
#include <zephyr/net/net_ip.h>
```

根据网络掩码（Netmask）生成掩码长度（Mask Length）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `family` | IP 地址族（Address Family），为 `NET_AF_INET` 或 `NET_AF_INET6`。 |
| `mask` | `family` 为 `NET_AF_INET` 时，指向 `struct sockaddr_in`；为 `NET_AF_INET6` 时，指向 `struct sockaddr_in6`。 |
| `mask_len` | IPv4 的网络掩码长度（Netmask Length）或 IPv6 的前缀长度（Prefix Length）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga0b67ffabad5b8a10da72301681206b31"></a>

### `net_port_get()`

```c
int net_port_get ( struct net_sockaddr * addr, uint16_t * port )
```

```c
#include <zephyr/net/net_ip.h>
```

获取 `sockaddr` 结构体中的端口（Port）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向用户提供的 `struct sockaddr` 的指针。 |
| `port` | 指向用于返回端口号（Port Number）的变量的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。

<a id="ga78436f11373210789ed9d5d640c6daf7"></a>

### `net_port_set()`

```c
int net_port_set ( struct net_sockaddr * addr, uint16_t port )
```

```c
#include <zephyr/net/net_ip.h>
```

设置 `sockaddr` 结构体中的端口（Port）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向用户提供的 `struct sockaddr` 的指针。 |
| `port` | 要设置的端口号（Port Number）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga45f18bd1ec2040f9f21b5aaf4ffe696d"></a>

### `net_port_set_default()`

```c
int net_port_set_default ( struct net_sockaddr * addr, uint16_t default_port )
```

```c
#include <zephyr/net/net_ip.h>
```

设置 `sockaddr` 结构体中的默认端口（Default Port）。

如果端口（Port）已设置，则不执行任何操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向用户提供的 `struct sockaddr` 的指针。 |
| `default_port` | 要设置的默认端口号（Default Port Number）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga8be77d043d4d1d29e0879b3b22274629"></a>

### `net_priority2vlan()`

```c
uint8_t net_priority2vlan ( enum net_priority priority)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

将网络数据包优先级（Network Packet Priority）转换为网络数据包的 VLAN 优先级（VLAN Priority）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `priority` | 数据包优先级（Packet Priority）。 |

**返回（Returns）**：返回值：VLAN 优先级代码点（Priority Code Point，PCP）。

<a id="ga7b3c41ae9b3962090d72c130a9fa61b1"></a>

### `net_rx_priority2tc()`

```c
int net_rx_priority2tc ( enum net_priority prio)
```

```c
#include <zephyr/net/net_ip.h>
```

将接收网络数据包优先级（RX Network Packet Priority）转换为流量类别（Traffic Class），以便将数据包放入正确的接收队列（RX Queue）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prio` | 网络优先级（Network Priority）。 |

**返回（Returns）**：返回值：处理该优先级网络流量的接收流量类别（Rx Traffic Class）。

<a id="ga13b4094cc06599c9af46e5e68e1c3bc3"></a>

### `net_sad()`

```c
ALWAYS_INLINE struct net_sockaddr * net_sad ( const struct net_sockaddr_storage * addr)
```

声明属性：`static`。

```c
#include <zephyr/net/net_ip.h>
```

从 `net_sockaddr_storage` 获取 `net_sockaddr`。

这是一个辅助函数，可缩短调用它的代码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 套接字存储地址（Socket Storage Address）。 |

**返回（Returns）**：返回值：指向套接字地址（Socket Address，`struct sockaddr`）的指针。

<a id="ga83d4270557a164eef75e1ae656470ef1"></a>

### `net_sas()`

```c
ALWAYS_INLINE struct net_sockaddr_storage * net_sas ( const struct net_sockaddr * addr)
```

声明属性：`static`。

```c
#include <zephyr/net/net_ip.h>
```

从 `net_sockaddr` 获取 `net_sockaddr_storage`。

这是一个辅助函数，可缩短调用它的代码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 套接字地址（Socket Address）。 |

**返回（Returns）**：返回值：指向套接字存储地址（Socket Storage Address，`struct net_sockaddr_storage`）的指针。

<a id="gaf92aa225bda78a3e016f6120b60c8885"></a>

### `net_sin()`

```c
ALWAYS_INLINE struct net_sockaddr_in * net_sin ( const struct net_sockaddr * addr)
```

声明属性：`static`。

```c
#include <zephyr/net/net_ip.h>
```

从 `net_sockaddr` 获取 `net_sockaddr_in`。

这是一个辅助函数，可缩短调用它的代码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 套接字地址（Socket Address）。 |

**返回（Returns）**：返回值：指向 IPv4 套接字地址（Socket Address）的指针。

<a id="ga4e7578614f7f0660c5a62d7746a3772c"></a>

### `net_sin6()`

```c
ALWAYS_INLINE struct net_sockaddr_in6 * net_sin6 ( const struct net_sockaddr * addr)
```

声明属性：`static`。

```c
#include <zephyr/net/net_ip.h>
```

从 `net_sockaddr` 获取 `net_sockaddr_in6`。

这是一个辅助函数，可缩短调用它的代码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 套接字地址（Socket Address）。 |

**返回（Returns）**：返回值：指向 IPv6 套接字地址（Socket Address）的指针。

<a id="gad4ed43b91fbaa2844fa509c603fafae6"></a>

### `net_sin6_ptr()`

```c
ALWAYS_INLINE struct net_sockaddr_in6_ptr * net_sin6_ptr ( const struct net_sockaddr_ptr * addr)
```

声明属性：`static`。

```c
#include <zephyr/net/net_ip.h>
```

从 `net_sockaddr_ptr` 获取 `net_sockaddr_in6_ptr`。

这是一个辅助函数，可缩短调用它的代码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 套接字地址（Socket Address）。 |

**返回（Returns）**：返回值：指向 IPv6 套接字地址（Socket Address）的指针。

<a id="ga6943b9d84c55709aaad323c1127a1949"></a>

### `net_sin_ptr()`

```c
ALWAYS_INLINE struct net_sockaddr_in_ptr * net_sin_ptr ( const struct net_sockaddr_ptr * addr)
```

声明属性：`static`。

```c
#include <zephyr/net/net_ip.h>
```

从 `sockaddr_ptr` 获取 `net_sockaddr_in_ptr`。

这是一个辅助函数，可缩短调用它的代码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 套接字地址（Socket Address）。 |

**返回（Returns）**：返回值：指向 IPv4 套接字地址（Socket Address）的指针。

<a id="ga8846a826e8b69c01fc92239a596ca002"></a>

### `net_sll_ptr()`

```c
ALWAYS_INLINE struct net_sockaddr_ll_ptr * net_sll_ptr ( const struct net_sockaddr_ptr * addr)
```

声明属性：`static`。

```c
#include <zephyr/net/net_ip.h>
```

从 `sockaddr_ptr` 获取 `net_sockaddr_ll_ptr`。

这是一个辅助函数，可缩短调用它的代码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 套接字地址（Socket Address）。 |

**返回（Returns）**：返回值：指向链路层套接字地址（Link-layer Socket Address）的指针。

<a id="ga8047c58777b659f8a8cdb2f24ca24355"></a>

### `net_sockaddr_cmp()`

```c
bool net_sockaddr_cmp ( const struct net_sockaddr * a, const struct net_sockaddr * b )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

比较套接字地址（Socket Address）。

IP 协议族第 4 版（IP Protocol Family Version 4）。译注：原文开头的 `<` 是注释标记残留。

IP 协议族第 4 版（IP Protocol Family Version 4）。译注：原文开头的 `<` 是注释标记残留。

IP 协议族第 6 版（IP Protocol Family Version 6）。译注：原文开头的 `<` 是注释标记残留。

IP 协议族第 6 版（IP Protocol Family Version 6）。译注：原文开头的 `<` 是注释标记残留。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 第一个地址（Address）。 |
| `b` | 第二个地址（Address）。 |

**返回（Returns）**：返回值：`a` 与 `b` 相等时为 `true`，否则为 `false`。

<a id="ga1695009388402938dcc2e49b526ebd1f"></a>

### `net_tcp_seq_cmp()`

```c
int32_t net_tcp_seq_cmp ( uint32_t seq1, uint32_t seq2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

比较 TCP 序列号（Sequence Number）。

此函数比较 TCP 序列号（Sequence Numbers），并考虑回绕（Wraparound）的影响。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `seq1` | 第一个序列号（Sequence Number）。 |
| `seq2` | 第二个序列号（Sequence Number）。 |

**返回（Returns）**：返回值：`seq1 < seq2` 时小于 0，`seq1 == seq2` 时为 0，`seq1 > seq2` 时大于 0。

<a id="gaa77b299f53e5535ac4c4bea1b6531a34"></a>

### `net_tcp_seq_greater()`

```c
bool net_tcp_seq_greater ( uint32_t seq1, uint32_t seq2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

检查其中一个 TCP 序列号（Sequence Number）是否更大。

这是基于 `net_tcp_seq_cmp()` 的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `seq1` | 第一个序列号（Sequence Number）。 |
| `seq2` | 第二个序列号（Sequence Number）。 |

**返回（Returns）**：返回值：`seq1 > seq2` 时为 `true`。

<a id="gae74c9ba7ff4addbce7f931bd6fa91fa0"></a>

### `net_tx_priority2tc()`

```c
int net_tx_priority2tc ( enum net_priority prio)
```

```c
#include <zephyr/net/net_ip.h>
```

将发送网络数据包优先级（TX Network Packet Priority）转换为流量类别（Traffic Class），以便将数据包放入正确的发送队列（TX Queue）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prio` | 网络优先级（Network Priority）。 |

**返回（Returns）**：返回值：处理该优先级网络流量的发送流量类别（Tx Traffic Class）。

<a id="ga14bc7018e3dd7c3e320b44a077343ce4"></a>

### `net_vlan2priority()`

```c
enum net_priority net_vlan2priority ( uint8_t priority)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_ip.h>
```

将网络数据包的 VLAN 优先级（VLAN Priority）转换为网络数据包优先级（Network Packet Priority），以便将数据包放入正确的队列。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `priority` | VLAN 优先级（Priority）。 |

**返回（Returns）**：返回值：网络优先级（Network Priority）。


## 2.7\_原页交叉引用（Cross References）

- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_sockaddr_in6](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md)
- [net_sockaddr_in](../network_core_model_reference/P119_net_sockaddr_in_结构体.md)
- [net_sockaddr_ll](../network_core_model_reference/P121_net_sockaddr_ll_结构体.md)
- [net_sockaddr_can](../network_core_model_reference/P118_net_sockaddr_can_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_sockaddr_nm](../network_core_model_reference/P122_net_sockaddr_nm_结构体.md)
- [net_iovec](../network_core_model_reference/P098_net_iovec_结构体.md)
- [net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)
- [net_cmsghdr](../network_core_model_reference/P052_net_cmsghdr_结构体.md)
- [net_linger](../network_core_model_reference/P104_net_linger_结构体.md)
- [net_tuple](../network_core_model_reference/P156_net_tuple_结构体.md)
- [net_ifreq](../network_core_model_reference/P093_net_ifreq_结构体.md)
- [net_in_pktinfo](../network_core_model_reference/P097_net_in_pktinfo_结构体.md)
- [net_ip_mreqn](../network_core_model_reference/P100_net_ip_mreqn_结构体.md)
- [net_ip_mreq](../network_core_model_reference/P099_net_ip_mreq_结构体.md)
- [net_ipv6_mreq](../network_core_model_reference/P102_net_ipv6_mreq_结构体.md)
- [net_packet_mreq](../network_core_model_reference/P113_net_packet_mreq_结构体.md)
- [net_in6_pktinfo](../network_core_model_reference/P095_net_in6_pktinfo_结构体.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [RFC 3513](https://datatracker.ietf.org/doc/html/rfc3513)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/net/net_ip.h](../api_file_kernel_network_reference/P010_zephyr__net__net_ip.h_文件参考.md)
- [sys_cpu_to_be32](../byteorder_reference/P001_系统字节序头文件参考.md#a508d3b125adf1d30e8411381827c4f05)
- [sys_cpu_to_be64](../byteorder_reference/P001_系统字节序头文件参考.md#a6ac423744c21c1e40aabd7ecb9b9e8d5)
- [sys_cpu_to_be16](../byteorder_reference/P001_系统字节序头文件参考.md#a9e2c7b19bbba5343ee8c5f9740484a56)
- [sys_be32_to_cpu](../byteorder_reference/P001_系统字节序头文件参考.md#aee4cefae7f089197e77c487faafda269)
- [sys_be64_to_cpu](../byteorder_reference/P001_系统字节序头文件参考.md#abb4d263f2b9b1cbf1c8fbaec714fc411)
- [sys_be16_to_cpu](../byteorder_reference/P001_系统字节序头文件参考.md#a840037a5fd3d36817dc92a44469df704)
- [setsockopt()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a71c8788caef89a362e35ce5855e77077)
- [https://en.wikipedia.org/wiki/Reserved_IP_addresses](https://en.wikipedia.org/wiki/Reserved_IP_addresses)
- [RFC 4291](https://datatracker.ietf.org/doc/html/rfc4291)
- [RFC 7217](https://datatracker.ietf.org/doc/html/rfc7217)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__cmsghdr_html"></a>
<a id="agroup__ip__4__6_html_ga1d17cfa3d3f1a6b5f3fe6476ef2db74f"></a>
<a id="asys_2byteorder_8h_html_a508d3b125adf1d30e8411381827c4f05"></a>
<a id="asys_2byteorder_8h_html_a6ac423744c21c1e40aabd7ecb9b9e8d5"></a>
<a id="asys_2byteorder_8h_html_a9e2c7b19bbba5343ee8c5f9740484a56"></a>
<a id="asys_2byteorder_8h_html_aee4cefae7f089197e77c487faafda269"></a>
<a id="asys_2byteorder_8h_html_abb4d263f2b9b1cbf1c8fbaec714fc411"></a>
<a id="asys_2byteorder_8h_html_a840037a5fd3d36817dc92a44469df704"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga32e58fc83532ef57eeb6ff952f17288da1de25b6f7d4c58957bce10d5f32fb5df"></a>
<a id="gga32e58fc83532ef57eeb6ff952f17288da6581c6c65c8f4e857fe9275e9ad1f8a9"></a>
<a id="gga32e58fc83532ef57eeb6ff952f17288da8f25e58072ffdfac2832740893ad881a"></a>
<a id="gga32e58fc83532ef57eeb6ff952f17288da85f4224bf8692e4b4a09ebb7b411f9a3"></a>
<a id="ggafecee2d4a331dc85ad962b81a6303e41a1c62cc5fe7d788175da915c25fc689e6"></a>
<a id="ggafecee2d4a331dc85ad962b81a6303e41ae0dbfc40ad42a55a176578a55d0c4006"></a>
<a id="ggafecee2d4a331dc85ad962b81a6303e41a7f6748a05d02325bd41b23cd05e6d1db"></a>
<a id="ggafecee2d4a331dc85ad962b81a6303e41adc6d5d3b52bddf03930e125b0f21ae9e"></a>
<a id="ggafecee2d4a331dc85ad962b81a6303e41a4dc979a84d5aaca6ae6f0f4e1c9bbff4"></a>
<a id="gga7a207761e4879c140f48f93978cb2f0ba76d0214e90b8507d3074a5b1ab38267c"></a>
<a id="gga7a207761e4879c140f48f93978cb2f0ba500ea814a9a955fbb4a65fdf96e784d1"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31a41d4bfab7d2a68dd7b707eb70ed88b41"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31a195a3c7b388ce05b61f64c9c9be9a092"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31a6ea6f123682a20c7895fd867504ada89"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31aebe8a029d9f87fb41c5f11b6366c1692"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31ace713634caddd3efe8190dc0988b87a1"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31a0ecceb13b5404e0699fa368306aeda25"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31a3a5c18feadc81db1bf688b83120feb5a"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31acc28399f823adaa247347ab125eb37f4"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31a2ac71d272f68c66ce42ac81de4891896"></a>
<a id="ggaf06819bf427cc58be1229b27b373ca31a4d7100f9fe0efb9e8ef6cb75e8c5ac97"></a>
<a id="gga721da18d2a3cfd9b3a56e9efc9f6e58ba5d6d30723e865cab7561cc8c963c3658"></a>
<a id="gga721da18d2a3cfd9b3a56e9efc9f6e58ba3f7f371f1d1729ad514f976f68738e47"></a>
<a id="gga721da18d2a3cfd9b3a56e9efc9f6e58ba29ed7248420f90939300dffdd23bb07c"></a>
<a id="gga721da18d2a3cfd9b3a56e9efc9f6e58bab13ec8077bb568971e80f9869b8d0529"></a>
<a id="gga721da18d2a3cfd9b3a56e9efc9f6e58baebb51afe0c7e1cfe37a330f6b0d72341"></a>
<a id="gga721da18d2a3cfd9b3a56e9efc9f6e58ba9ac0cafee2ab1cb5f16780fa17da5b8f"></a>
<a id="gga721da18d2a3cfd9b3a56e9efc9f6e58bab8506c41543969d01e4aaaa49c0932ab"></a>
<a id="ggae87ef466e77ded673ed7e593d3eddffdae01a1318d81935d370f030456435202b"></a>
<a id="ggae87ef466e77ded673ed7e593d3eddffda8bc1e038efe3e2332ccd3840990a64ce"></a>
<a id="ggae87ef466e77ded673ed7e593d3eddffdac9c5e9073459374d56491c26b692d5b0"></a>
<a id="ggae87ef466e77ded673ed7e593d3eddffda38103e3ab83f8fd693a5a1c18de98354"></a>
<a id="ggae87ef466e77ded673ed7e593d3eddffda7878127d03fb7d0a34b8d68b9461e792"></a>
<a id="ggae87ef466e77ded673ed7e593d3eddffda6919b414160f3ed8ac7c391761c77e8a"></a>
<a id="ggae87ef466e77ded673ed7e593d3eddffda23090c0b06a54b8a41be3f44497b0c05"></a>
<a id="ggae87ef466e77ded673ed7e593d3eddffda05855ea3da85f60bec646a4491b554ef"></a>
<a id="ggaaab4268707dbe08348b98fb028e7aa5ca6f049fea24a6d2d5279e736ececf3c83"></a>
<a id="ggaaab4268707dbe08348b98fb028e7aa5caff1fd09b4fa81b8e0e8a73132c8fa3e4"></a>
<a id="ggaaab4268707dbe08348b98fb028e7aa5ca892feaa0f7556622a3491683e69b6ac2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_HL7800 API主题.md) · [返回大纲](大纲.md) · [下一章](P003_LTC4286 API主题.md)
