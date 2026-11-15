---
id: learning.zephyr-docs.api-file-clock-network-reference.page-6
title: zephyr__net__dns_resolve.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_net\_\_dns\_resolve.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DNS解析库（Resolving Library）。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/socket_poll.h>
#include <zephyr/net/net_core.h>
#include <zephyr/sys/atomic.h>
```

查看此文件的源码。

DNS 解析库（DNS Resolving Library），为应用提供解析 DNS 名称的 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_dns_5Fresolve_5Ftxt"></a>

```c
struct dns_resolve_txt
```

相关声明：[dns_resolve_txt](../network_application_model_reference/P024_dns_resolve_txt_结构体.md)。

文本记录（TXT）的信息。

<a id="r_dns_5Fresolve_5Fsrv"></a>

```c
struct dns_resolve_srv
```

相关声明：[dns_resolve_srv](../network_application_model_reference/P023_dns_resolve_srv_结构体.md)。

服务位置记录（SRV）的信息。

<a id="r_dns_5Fresolve_5Fprivate"></a>

```c
struct dns_resolve_private
```

相关声明：[dns_resolve_private](../network_application_model_reference/P022_dns_resolve_private_结构体.md)。

私有资源记录（RR）的信息。

<a id="r_dns_5Faddrinfo"></a>

```c
struct dns_addrinfo
```

相关声明：[dns_addrinfo](../network_application_model_reference/P018_dns_addrinfo_结构体.md)。

传给接收全部结果的回调的地址信息（Address Info）结构。

<a id="r_dns_5Fresolve_5Fcontext"></a>

```c
struct dns_resolve_context
```

相关声明：[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)。

DNS解析上下文（Resolve Context）结构。

<a id="r_dns_5Fresolve_5Fcontext_3A_3Adns_5Fserver_5Finfo"></a>

```c
struct dns_resolve_context::dns_server_info
```

相关声明：[dns_resolve_context::dns_server_info](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md)。

一个已配置DNS服务器的信息。

<a id="r_dns_5Fresolve_5Fcontext_3A_3Adns_5Fpending_5Fquery"></a>

```c
struct dns_resolve_context::dns_pending_query
```

相关声明：[dns_resolve_context::dns_pending_query](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md)。

结果回调（Result Callbacks）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga924d2d4d3b5205a605f4ab69dffdf294"></a>

```c
#define DNS_RR_TYPE_PRIVATE_START_VALUE 65280
```

相关声明：[DNS_RR_TYPE_PRIVATE_START_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga924d2d4d3b5205a605f4ab69dffdf294)。

私有资源记录类型范围（Private RR Type Range）的起始值，见 RFC 6895。

<a id="r_ga4db137a83d3917bcad1489e25a639666"></a>

```c
#define DNS_RR_TYPE_PRIVATE_END_VALUE 65534
```

相关声明：[DNS_RR_TYPE_PRIVATE_END_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga4db137a83d3917bcad1489e25a639666)。

私有资源记录类型范围（Private RR Type Range）的结束值，见 RFC 6895。

<a id="r_gaba564a71c4fb4c44fae69015e880b0db"></a>

```c
#define DNS_MAX_NAME_SIZE 20
```

相关声明：[DNS_MAX_NAME_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaba564a71c4fb4c44fae69015e880b0db)。

解析所得名称（Resolved Name）的最大大小。

<a id="r_ga7b6c39611abd40d2d0510c9e38383ecc"></a>

```c
#define DNS_MAX_TEXT_SIZE 64
```

相关声明：[DNS_MAX_TEXT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7b6c39611abd40d2d0510c9e38383ecc)。

解析所得 TXT 记录（Resolved TXT Record）的最大大小。

<a id="r_gac709b355684d44e943c26c6953187df4"></a>

```c
#define DNS_MAX_PRIVATE_DATA_SIZE 128
```

相关声明：[DNS_MAX_PRIVATE_DATA_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gac709b355684d44e943c26c6953187df4)。

私有资源记录数据（Private RR Data）的最大大小。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_gafe22d0ef90c581982561ef0c33d1f722"></a>

```c
typedef void(* dns_resolve_cb_t) (enum dns_resolve_status status, struct dns_addrinfo *info, void *user_data)
```

相关声明：[dns_resolve_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gafe22d0ef90c581982561ef0c33d1f722)、[dns_resolve_status](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga5baf1fea0482fb3a940b4f5350a3c58e)、[dns_addrinfo](../network_application_model_reference/P018_dns_addrinfo_结构体.md)。

DNS 解析回调（DNS Resolve Callback）。

<a id="r_ga7892b3eda301db358b1f18720a2f638c"></a>

```c
typedef void(* dns_resolve_pkt_fw_cb_t) (struct net_buf *dns_data, size_t buf_len, void *user_data)
```

相关声明：[dns_resolve_pkt_fw_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7892b3eda301db358b1f18720a2f638c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将收到的 DNS 服务器数据包传给应用的 DNS 解析回调（DNS Resolve Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_ga7169c5a920fb1b0d77910a6ab922e3f0"></a>

```c
enum dns_query_type { DNS_QUERY_TYPE_A = 1 , DNS_QUERY_TYPE_CNAME = 5 , DNS_QUERY_TYPE_PTR = 12 , DNS_QUERY_TYPE_TXT = 16 , DNS_QUERY_TYPE_AAAA = 28 , DNS_QUERY_TYPE_SRV = 33 , DNS_QUERY_TYPE_ANY = 255 , DNS_QUERY_TYPE_RESERVED = 65535 }
```

相关声明：[dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)、[DNS_QUERY_TYPE_A](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134)、[DNS_QUERY_TYPE_CNAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a128aa925168ae2b096ff879c7648d2e4)、[DNS_QUERY_TYPE_PTR](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa)、[DNS_QUERY_TYPE_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a42c3f3d5876b275f764a67e1bf43d850)、[DNS_QUERY_TYPE_AAAA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049)、[DNS_QUERY_TYPE_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a2e976a8ed83e609b4836444d7a95d65d)、[DNS_QUERY_TYPE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a0b8a4c108a7ae4742d2235b64c3d8c06)、[DNS_QUERY_TYPE_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0aed30f5d6a68ef4503ca6f3d60d1c0e6a)。

DNS 查询类型枚举（Query Type Enum）。

<a id="r_gaeda02f82b12e9b7b4dea9fd66be123a7"></a>

```c
enum dns_server_source { DNS_SOURCE_UNKNOWN = 0 , DNS_SOURCE_MANUAL , DNS_SOURCE_DHCPV4 , DNS_SOURCE_DHCPV6 , DNS_SOURCE_IPV6_RA , DNS_SOURCE_PPP }
```

相关声明：[dns_server_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaeda02f82b12e9b7b4dea9fd66be123a7)、[DNS_SOURCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9)、[DNS_SOURCE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33)、[DNS_SOURCE_DHCPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b)、[DNS_SOURCE_DHCPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b)、[DNS_SOURCE_IPV6_RA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9)、[DNS_SOURCE_PPP](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902)。

添加 DNS 服务器的实体（Entity）。

<a id="r_ga8a4330071b7161e1738dd91b1f6d6097"></a>

```c
enum dns_resolve_extension { DNS_RESOLVE_NONE = 0 , DNS_RESOLVE_TXT , DNS_RESOLVE_SRV , DNS_RESOLVE_PRIVATE }
```

相关声明：[dns_resolve_extension](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga8a4330071b7161e1738dd91b1f6d6097)、[DNS_RESOLVE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097a80ada4858b77463f1af5b06660aaaf3b)、[DNS_RESOLVE_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097a6a5d547c65f5d265bfd4f1968ed3db98)、[DNS_RESOLVE_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097af0b69e02c8e086e64ce194cd66507672)、[DNS_RESOLVE_PRIVATE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097a9f582f9d2424409736f32ac0051fc582)。

枚举地址信息中可用的扩展（Extensions）。

<a id="r_ga5baf1fea0482fb3a940b4f5350a3c58e"></a>

```c
enum dns_resolve_status { DNS_EAI_BADFLAGS = -1 , DNS_EAI_NONAME = -2 , DNS_EAI_AGAIN = -3 , DNS_EAI_FAIL = -4 , DNS_EAI_NODATA = -5 , DNS_EAI_FAMILY = -6 , DNS_EAI_SOCKTYPE = -7 , DNS_EAI_SERVICE = -8 , DNS_EAI_ADDRFAMILY = -9 , DNS_EAI_MEMORY = -10 , DNS_EAI_SYSTEM = -11 , DNS_EAI_OVERFLOW = -12 , DNS_EAI_INPROGRESS = -100 , DNS_EAI_CANCELED = -101 , DNS_EAI_NOTCANCELED = -102 , DNS_EAI_ALLDONE = -103 , DNS_EAI_IDN_ENCODE = -105 }
```

相关声明：[dns_resolve_status](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga5baf1fea0482fb3a940b4f5350a3c58e)、[DNS_EAI_BADFLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea9989bb26c930dcf90b5aaab224f19793)、[DNS_EAI_NONAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f)、[DNS_EAI_AGAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9)、[DNS_EAI_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455)、[DNS_EAI_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2)、[DNS_EAI_FAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8440de8b7109dfcca71acca6c7ac4103)、[DNS_EAI_SOCKTYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaba718125a826939380fdbcc9c1fb4512)、[DNS_EAI_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaeb7d2677167f5bc230da2eea2a81d06c)、[DNS_EAI_ADDRFAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d)、[DNS_EAI_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673)、[DNS_EAI_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eae932d5596c55d090cf2ebe43ad59bd35)、[DNS_EAI_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f)、[DNS_EAI_INPROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3)、[DNS_EAI_CANCELED](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3)、[DNS_EAI_NOTCANCELED](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f)、[DNS_EAI_ALLDONE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836)、[DNS_EAI_IDN_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4)。

回调使用的状态值（Status Values）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_ga13a7cbc3b59a12278f4b035013c03b1d"></a>

```c
static bool dns_query_type_is_private (enum dns_query_type type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[dns_query_type_is_private](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga13a7cbc3b59a12278f4b035013c03b1d)、[dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)。

检查查询类型是否为私有资源记录（Private RR）；RFC 6895 规定范围为 65280～65534。

<a id="r_ga27a85c421014373f6aad89634adf8c7d"></a>

```c
int dns_resolve_init (struct dns_resolve_context *ctx, const char *dns_servers_str[], const struct net_sockaddr *dns_servers_sa[])
```

相关声明：[dns_resolve_init](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga27a85c421014373f6aad89634adf8c7d)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

初始化 DNS 解析上下文（DNS Resolving Context）。

<a id="r_ga71eab0f9dd0bc7c02c0d55e7dc6741f3"></a>

```c
int dns_resolve_init_default (struct dns_resolve_context *ctx)
```

相关声明：[dns_resolve_init_default](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)。

使用默认 Kconfig 选项初始化 DNS 解析上下文（DNS Resolving Context）。

<a id="r_gab04f3b2347e9c59346c10180c6c9ffbc"></a>

```c
int dns_resolve_close (struct dns_resolve_context *ctx)
```

相关声明：[dns_resolve_close](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gab04f3b2347e9c59346c10180c6c9ffbc)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)。

关闭 DNS 解析上下文（DNS Resolving Context）。

<a id="r_ga3cf4e94af65585d89b4a0650dbd9d46e"></a>

```c
bool dns_resolve_is_active (struct dns_resolve_context *ctx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[dns_resolve_is_active](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3cf4e94af65585d89b4a0650dbd9d46e)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)。

检查 DNS 解析上下文（DNS Resolving Context）是否处于活动状态。

<a id="r_ga1d3bb0319531bfe0ae95f48bdc51c56f"></a>

```c
int dns_resolve_reconfigure (struct dns_resolve_context *ctx, const char *servers_str[], const struct net_sockaddr *servers_sa[], enum dns_server_source source)
```

相关声明：[dns_resolve_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga1d3bb0319531bfe0ae95f48bdc51c56f)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[dns_server_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaeda02f82b12e9b7b4dea9fd66be123a7)。

重新配置 DNS 解析上下文（DNS Resolving Context）。

<a id="r_ga3d22eed1d6d017e5bd7a2344775d33b7"></a>

```c
int dns_resolve_reconfigure_with_interfaces (struct dns_resolve_context *ctx, const char *servers_str[], const struct net_sockaddr *servers_sa[], int interfaces[], enum dns_server_source source)
```

相关声明：[dns_resolve_reconfigure_with_interfaces](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3d22eed1d6d017e5bd7a2344775d33b7)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[dns_server_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaeda02f82b12e9b7b4dea9fd66be123a7)。

使用新服务器列表重新配置 DNS 解析上下文，并允许将服务器指定到特定网络接口（Network Interface）。

<a id="r_ga54c85b9c69c9a44f2e7bb78165cebfcb"></a>

```c
int dns_resolve_remove (struct dns_resolve_context *ctx, int if_index)
```

相关声明：[dns_resolve_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga54c85b9c69c9a44f2e7bb78165cebfcb)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)。

从 DNS 解析上下文移除服务器（Servers）。

<a id="r_gae292786587c511c223481f77a4f43017"></a>

```c
int dns_resolve_remove_source (struct dns_resolve_context *ctx, int if_index, enum dns_server_source source)
```

相关声明：[dns_resolve_remove_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gae292786587c511c223481f77a4f43017)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[dns_server_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaeda02f82b12e9b7b4dea9fd66be123a7)。

从 DNS 解析上下文移除由特定来源（Source）添加的服务器。

<a id="r_gaf491764b213a891f296c9f91c35b1b72"></a>

```c
int dns_resolve_remove_server_addresses (struct dns_resolve_context *ctx, const struct net_sockaddr *servers_sa[], int interfaces[])
```

相关声明：[dns_resolve_remove_server_addresses](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf491764b213a891f296c9f91c35b1b72)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

从 DNS 解析上下文移除具有特定 IP 地址的服务器。

<a id="r_ga7701ddd6b6c5923f0d122a2bcf898cbf"></a>

```c
int dns_resolve_cancel (struct dns_resolve_context *ctx, uint16_t dns_id)
```

相关声明：[dns_resolve_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7701ddd6b6c5923f0d122a2bcf898cbf)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

取消待处理的 DNS 查询（Pending DNS Query）。

<a id="r_gaf2854ca9b839e7cba073e75202ac7e38"></a>

```c
int dns_resolve_cancel_with_name (struct dns_resolve_context *ctx, uint16_t dns_id, const char *query_name, enum dns_query_type query_type)
```

相关声明：[dns_resolve_cancel_with_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf2854ca9b839e7cba073e75202ac7e38)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)。

根据 ID、名称和类型取消待处理的 DNS 查询（Pending DNS Query）。

<a id="r_ga24f9bc24e2021b6b528bb15e4fcca49b"></a>

```c
int dns_resolve_name (struct dns_resolve_context *ctx, const char *query, enum dns_query_type type, uint16_t *dns_id, dns_resolve_cb_t cb, void *user_data, int32_t timeout)
```

相关声明：[dns_resolve_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga24f9bc24e2021b6b528bb15e4fcca49b)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[dns_resolve_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gafe22d0ef90c581982561ef0c33d1f722)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

解析 DNS 名称（DNS Name）。

<a id="r_gaf28f6f8baa97d0b2341e1bdc02b6cb8c"></a>

```c
static int dns_resolve_service (struct dns_resolve_context *ctx, const char *query, uint16_t *dns_id, dns_resolve_cb_t cb, void *user_data, int32_t timeout)
```

相关声明：[dns_resolve_service](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[dns_resolve_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gafe22d0ef90c581982561ef0c33d1f722)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

解析 DNS 服务（DNS Service）。

<a id="r_gae69cd758e99ea93ef8aac28366918b87"></a>

```c
struct dns_resolve_context * dns_resolve_get_default (void)
```

相关声明：[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[dns_resolve_get_default](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gae69cd758e99ea93ef8aac28366918b87)。

获取默认 DNS 上下文（DNS Context）。

<a id="r_ga3326e98da31313d33861565fe0a10bdf"></a>

```c
static void dns_resolve_enable_packet_forwarding (struct dns_resolve_context *ctx, dns_resolve_pkt_fw_cb_t cb)
```

相关声明：[dns_resolve_enable_packet_forwarding](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3326e98da31313d33861565fe0a10bdf)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[dns_resolve_pkt_fw_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7892b3eda301db358b1f18720a2f638c)。

为 DNS 解析上下文安装数据包转发回调（Packet Forwarding Callback）。

<a id="r_gaf891d7e21bddc8fbd029209b4339c01d"></a>

```c
static int dns_get_addr_info (const char *query, enum dns_query_type type, uint16_t *dns_id, dns_resolve_cb_t cb, void *user_data, int32_t timeout)
```

相关声明：[dns_get_addr_info](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf891d7e21bddc8fbd029209b4339c01d)、[dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[dns_resolve_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gafe22d0ef90c581982561ef0c33d1f722)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

从 DNS 获取 IP 地址信息（IP Address Info）。

<a id="r_ga54ae7aaf53b36951b27f09e1cc82df55"></a>

```c
static int dns_cancel_addr_info (uint16_t dns_id)
```

相关声明：[dns_cancel_addr_info](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga54ae7aaf53b36951b27f09e1cc82df55)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

取消待处理的 DNS 查询（Pending DNS Query）。

<a id="r_gac8a1d620f07641e4e64ad0757c31aa45"></a>

```c
static int dns_cancel_addr_info_with_name (const char *query_name, enum dns_query_type query_type, uint16_t dns_id)
```

相关声明：[dns_cancel_addr_info_with_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gac8a1d620f07641e4e64ad0757c31aa45)、[dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据 ID、名称和类型取消待处理的 DNS 查询（Pending DNS Query）。


## 6.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/socket_poll.h](../api_source_supplement_reference/P184_socket_poll.h_源码浏览.md)
- [zephyr/net/net_core.h](../api_source_system_reference/P023_net_core.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [查看此文件的源码。](../api_source_transport_clock_reference/P008_dns_resolve.h_源码浏览.md)
- [dns_resolve_txt](../network_application_model_reference/P024_dns_resolve_txt_结构体.md)
- [dns_resolve_srv](../network_application_model_reference/P023_dns_resolve_srv_结构体.md)
- [dns_resolve_private](../network_application_model_reference/P022_dns_resolve_private_结构体.md)
- [dns_addrinfo](../network_application_model_reference/P018_dns_addrinfo_结构体.md)
- [dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)
- [dns_resolve_context::dns_server_info](../network_application_model_reference/P021_dns_resolve_context__dns_server_info_结构体.md)
- [dns_resolve_context::dns_pending_query](../network_application_model_reference/P020_dns_resolve_context__dns_pending_query_结构体.md)
- [DNS_RR_TYPE_PRIVATE_START_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga924d2d4d3b5205a605f4ab69dffdf294)
- [RFC 6895](https://datatracker.ietf.org/doc/html/rfc6895)
- [DNS_RR_TYPE_PRIVATE_END_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga4db137a83d3917bcad1489e25a639666)
- [DNS_MAX_NAME_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaba564a71c4fb4c44fae69015e880b0db)
- [DNS_MAX_TEXT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7b6c39611abd40d2d0510c9e38383ecc)
- [DNS_MAX_PRIVATE_DATA_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gac709b355684d44e943c26c6953187df4)
- [dns_resolve_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gafe22d0ef90c581982561ef0c33d1f722)
- [dns_resolve_status](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga5baf1fea0482fb3a940b4f5350a3c58e)
- [dns_resolve_pkt_fw_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7892b3eda301db358b1f18720a2f638c)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [dns_query_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7169c5a920fb1b0d77910a6ab922e3f0)
- [DNS_QUERY_TYPE_A](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134)
- [DNS_QUERY_TYPE_CNAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a128aa925168ae2b096ff879c7648d2e4)
- [DNS_QUERY_TYPE_PTR](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa)
- [DNS_QUERY_TYPE_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a42c3f3d5876b275f764a67e1bf43d850)
- [DNS_QUERY_TYPE_AAAA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049)
- [DNS_QUERY_TYPE_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a2e976a8ed83e609b4836444d7a95d65d)
- [DNS_QUERY_TYPE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a0b8a4c108a7ae4742d2235b64c3d8c06)
- [DNS_QUERY_TYPE_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0aed30f5d6a68ef4503ca6f3d60d1c0e6a)
- [dns_server_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaeda02f82b12e9b7b4dea9fd66be123a7)
- [DNS_SOURCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9)
- [DNS_SOURCE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33)
- [DNS_SOURCE_DHCPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b)
- [DNS_SOURCE_DHCPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b)
- [DNS_SOURCE_IPV6_RA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9)
- [DNS_SOURCE_PPP](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902)
- [dns_resolve_extension](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga8a4330071b7161e1738dd91b1f6d6097)
- [DNS_RESOLVE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097a80ada4858b77463f1af5b06660aaaf3b)
- [DNS_RESOLVE_TXT](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097a6a5d547c65f5d265bfd4f1968ed3db98)
- [DNS_RESOLVE_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097af0b69e02c8e086e64ce194cd66507672)
- [DNS_RESOLVE_PRIVATE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga8a4330071b7161e1738dd91b1f6d6097a9f582f9d2424409736f32ac0051fc582)
- [DNS_EAI_BADFLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea9989bb26c930dcf90b5aaab224f19793)
- [DNS_EAI_NONAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f)
- [DNS_EAI_AGAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9)
- [DNS_EAI_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455)
- [DNS_EAI_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2)
- [DNS_EAI_FAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8440de8b7109dfcca71acca6c7ac4103)
- [DNS_EAI_SOCKTYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaba718125a826939380fdbcc9c1fb4512)
- [DNS_EAI_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaeb7d2677167f5bc230da2eea2a81d06c)
- [DNS_EAI_ADDRFAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d)
- [DNS_EAI_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673)
- [DNS_EAI_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eae932d5596c55d090cf2ebe43ad59bd35)
- [DNS_EAI_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f)
- [DNS_EAI_INPROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3)
- [DNS_EAI_CANCELED](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3)
- [DNS_EAI_NOTCANCELED](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f)
- [DNS_EAI_ALLDONE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836)
- [DNS_EAI_IDN_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [dns_query_type_is_private](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga13a7cbc3b59a12278f4b035013c03b1d)
- [dns_resolve_init](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga27a85c421014373f6aad89634adf8c7d)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [dns_resolve_init_default](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)
- [dns_resolve_close](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gab04f3b2347e9c59346c10180c6c9ffbc)
- [dns_resolve_is_active](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3cf4e94af65585d89b4a0650dbd9d46e)
- [dns_resolve_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga1d3bb0319531bfe0ae95f48bdc51c56f)
- [dns_resolve_reconfigure_with_interfaces](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3d22eed1d6d017e5bd7a2344775d33b7)
- [dns_resolve_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga54c85b9c69c9a44f2e7bb78165cebfcb)
- [dns_resolve_remove_source](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gae292786587c511c223481f77a4f43017)
- [dns_resolve_remove_server_addresses](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf491764b213a891f296c9f91c35b1b72)
- [dns_resolve_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga7701ddd6b6c5923f0d122a2bcf898cbf)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [dns_resolve_cancel_with_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf2854ca9b839e7cba073e75202ac7e38)
- [dns_resolve_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga24f9bc24e2021b6b528bb15e4fcca49b)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [dns_resolve_service](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)
- [dns_resolve_get_default](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gae69cd758e99ea93ef8aac28366918b87)
- [dns_resolve_enable_packet_forwarding](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3326e98da31313d33861565fe0a10bdf)
- [dns_get_addr_info](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf891d7e21bddc8fbd029209b4339c01d)
- [dns_cancel_addr_info](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga54ae7aaf53b36951b27f09e1cc82df55)
- [dns_cancel_addr_info_with_name](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gac8a1d620f07641e4e64ad0757c31aa45)

<a id="header-details"></a>

---

[上一章](P005_zephyr__dt-bindings__gpio__digilent-pmod.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dt-bindings__pinctrl__esp-pinctrl-common.h_文件参考.md)
