---
id: learning.zephyr-docs.api-iso-dns-lin-topic-reference.page-7
title: 域名解析库（DNS Resolve Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_域名解析库（DNS Resolve Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DNS解析库（Resolving Library）。

<a id="details"></a>

DNS 解析库（DNS Resolving Library）。自 1.8 引入，版本 0.9.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga924d2d4d3b5205a605f4ab69dffdf294"></a>

```c
#define DNS_RR_TYPE_PRIVATE_START_VALUE 65280
```

相关声明：[DNS_RR_TYPE_PRIVATE_START_VALUE](#ga924d2d4d3b5205a605f4ab69dffdf294)。

私有资源记录类型范围（Private RR Type Range）的起始值，见 RFC 6895。

<a id="r_ga4db137a83d3917bcad1489e25a639666"></a>

```c
#define DNS_RR_TYPE_PRIVATE_END_VALUE 65534
```

相关声明：[DNS_RR_TYPE_PRIVATE_END_VALUE](#ga4db137a83d3917bcad1489e25a639666)。

私有资源记录类型范围（Private RR Type Range）的结束值，见 RFC 6895。

<a id="r_gaba564a71c4fb4c44fae69015e880b0db"></a>

```c
#define DNS_MAX_NAME_SIZE 20
```

相关声明：[DNS_MAX_NAME_SIZE](#gaba564a71c4fb4c44fae69015e880b0db)。

解析所得名称（Resolved Name）的最大大小。

<a id="r_ga7b6c39611abd40d2d0510c9e38383ecc"></a>

```c
#define DNS_MAX_TEXT_SIZE 64
```

相关声明：[DNS_MAX_TEXT_SIZE](#ga7b6c39611abd40d2d0510c9e38383ecc)。

解析所得 TXT 记录（Resolved TXT Record）的最大大小。

<a id="r_gac709b355684d44e943c26c6953187df4"></a>

```c
#define DNS_MAX_PRIVATE_DATA_SIZE 128
```

相关声明：[DNS_MAX_PRIVATE_DATA_SIZE](#gac709b355684d44e943c26c6953187df4)。

私有资源记录数据（Private RR Data）的最大大小。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.3\_类型定义（Typedefs）

<a id="r_gafe22d0ef90c581982561ef0c33d1f722"></a>

```c
typedef void(* dns_resolve_cb_t) (enum dns_resolve_status status, struct dns_addrinfo *info, void *user_data)
```

相关声明：[dns_resolve_cb_t](#gafe22d0ef90c581982561ef0c33d1f722)、[dns_resolve_status](#ga5baf1fea0482fb3a940b4f5350a3c58e)、[dns_addrinfo](../network_application_model_reference/P018_dns_addrinfo_结构体.md)。

DNS 解析回调（DNS Resolve Callback）。

<a id="r_ga7892b3eda301db358b1f18720a2f638c"></a>

```c
typedef void(* dns_resolve_pkt_fw_cb_t) (struct net_buf *dns_data, size_t buf_len, void *user_data)
```

相关声明：[dns_resolve_pkt_fw_cb_t](#ga7892b3eda301db358b1f18720a2f638c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将收到的 DNS 服务器数据包传给应用的 DNS 解析回调（DNS Resolve Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.4\_枚举（Enumerations）

<a id="r_ga7169c5a920fb1b0d77910a6ab922e3f0"></a>

```c
enum dns_query_type { DNS_QUERY_TYPE_A = 1 , DNS_QUERY_TYPE_CNAME = 5 , DNS_QUERY_TYPE_PTR = 12 , DNS_QUERY_TYPE_TXT = 16 , DNS_QUERY_TYPE_AAAA = 28 , DNS_QUERY_TYPE_SRV = 33 , DNS_QUERY_TYPE_ANY = 255 , DNS_QUERY_TYPE_RESERVED = 65535 }
```

相关声明：[dns_query_type](#ga7169c5a920fb1b0d77910a6ab922e3f0)、[DNS_QUERY_TYPE_A](#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134)、[DNS_QUERY_TYPE_CNAME](#gga7169c5a920fb1b0d77910a6ab922e3f0a128aa925168ae2b096ff879c7648d2e4)、[DNS_QUERY_TYPE_PTR](#gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa)、[DNS_QUERY_TYPE_TXT](#gga7169c5a920fb1b0d77910a6ab922e3f0a42c3f3d5876b275f764a67e1bf43d850)、[DNS_QUERY_TYPE_AAAA](#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049)、[DNS_QUERY_TYPE_SRV](#gga7169c5a920fb1b0d77910a6ab922e3f0a2e976a8ed83e609b4836444d7a95d65d)、[DNS_QUERY_TYPE_ANY](#gga7169c5a920fb1b0d77910a6ab922e3f0a0b8a4c108a7ae4742d2235b64c3d8c06)、[DNS_QUERY_TYPE_RESERVED](#gga7169c5a920fb1b0d77910a6ab922e3f0aed30f5d6a68ef4503ca6f3d60d1c0e6a)。

DNS 查询类型枚举（Query Type Enum）。

<a id="r_gaeda02f82b12e9b7b4dea9fd66be123a7"></a>

```c
enum dns_server_source { DNS_SOURCE_UNKNOWN = 0 , DNS_SOURCE_MANUAL , DNS_SOURCE_DHCPV4 , DNS_SOURCE_DHCPV6 , DNS_SOURCE_IPV6_RA , DNS_SOURCE_PPP }
```

相关声明：[dns_server_source](#gaeda02f82b12e9b7b4dea9fd66be123a7)、[DNS_SOURCE_UNKNOWN](#ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9)、[DNS_SOURCE_MANUAL](#ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33)、[DNS_SOURCE_DHCPV4](#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b)、[DNS_SOURCE_DHCPV6](#ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b)、[DNS_SOURCE_IPV6_RA](#ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9)、[DNS_SOURCE_PPP](#ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902)。

添加 DNS 服务器的实体（Entity）。

<a id="r_ga8a4330071b7161e1738dd91b1f6d6097"></a>

```c
enum dns_resolve_extension { DNS_RESOLVE_NONE = 0 , DNS_RESOLVE_TXT , DNS_RESOLVE_SRV , DNS_RESOLVE_PRIVATE }
```

相关声明：[dns_resolve_extension](#ga8a4330071b7161e1738dd91b1f6d6097)、[DNS_RESOLVE_NONE](#gga8a4330071b7161e1738dd91b1f6d6097a80ada4858b77463f1af5b06660aaaf3b)、[DNS_RESOLVE_TXT](#gga8a4330071b7161e1738dd91b1f6d6097a6a5d547c65f5d265bfd4f1968ed3db98)、[DNS_RESOLVE_SRV](#gga8a4330071b7161e1738dd91b1f6d6097af0b69e02c8e086e64ce194cd66507672)、[DNS_RESOLVE_PRIVATE](#gga8a4330071b7161e1738dd91b1f6d6097a9f582f9d2424409736f32ac0051fc582)。

枚举地址信息中可用的扩展（Extensions）。

<a id="r_ga5baf1fea0482fb3a940b4f5350a3c58e"></a>

```c
enum dns_resolve_status { DNS_EAI_BADFLAGS = -1 , DNS_EAI_NONAME = -2 , DNS_EAI_AGAIN = -3 , DNS_EAI_FAIL = -4 , DNS_EAI_NODATA = -5 , DNS_EAI_FAMILY = -6 , DNS_EAI_SOCKTYPE = -7 , DNS_EAI_SERVICE = -8 , DNS_EAI_ADDRFAMILY = -9 , DNS_EAI_MEMORY = -10 , DNS_EAI_SYSTEM = -11 , DNS_EAI_OVERFLOW = -12 , DNS_EAI_INPROGRESS = -100 , DNS_EAI_CANCELED = -101 , DNS_EAI_NOTCANCELED = -102 , DNS_EAI_ALLDONE = -103 , DNS_EAI_IDN_ENCODE = -105 }
```

相关声明：[dns_resolve_status](#ga5baf1fea0482fb3a940b4f5350a3c58e)、[DNS_EAI_BADFLAGS](#gga5baf1fea0482fb3a940b4f5350a3c58ea9989bb26c930dcf90b5aaab224f19793)、[DNS_EAI_NONAME](#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f)、[DNS_EAI_AGAIN](#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9)、[DNS_EAI_FAIL](#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455)、[DNS_EAI_NODATA](#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2)、[DNS_EAI_FAMILY](#gga5baf1fea0482fb3a940b4f5350a3c58ea8440de8b7109dfcca71acca6c7ac4103)、[DNS_EAI_SOCKTYPE](#gga5baf1fea0482fb3a940b4f5350a3c58eaba718125a826939380fdbcc9c1fb4512)、[DNS_EAI_SERVICE](#gga5baf1fea0482fb3a940b4f5350a3c58eaeb7d2677167f5bc230da2eea2a81d06c)、[DNS_EAI_ADDRFAMILY](#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d)、[DNS_EAI_MEMORY](#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673)、[DNS_EAI_SYSTEM](#gga5baf1fea0482fb3a940b4f5350a3c58eae932d5596c55d090cf2ebe43ad59bd35)、[DNS_EAI_OVERFLOW](#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f)、[DNS_EAI_INPROGRESS](#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3)、[DNS_EAI_CANCELED](#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3)、[DNS_EAI_NOTCANCELED](#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f)、[DNS_EAI_ALLDONE](#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836)、[DNS_EAI_IDN_ENCODE](#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4)。

回调使用的状态值（Status Values）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.5\_函数（Functions）

<a id="r_ga13a7cbc3b59a12278f4b035013c03b1d"></a>

```c
static bool dns_query_type_is_private (enum dns_query_type type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[dns_query_type_is_private](#ga13a7cbc3b59a12278f4b035013c03b1d)、[dns_query_type](#ga7169c5a920fb1b0d77910a6ab922e3f0)。

检查查询类型是否为私有资源记录（Private RR）；RFC 6895 规定范围为 65280～65534。

<a id="r_ga27a85c421014373f6aad89634adf8c7d"></a>

```c
int dns_resolve_init (struct dns_resolve_context *ctx, const char *dns_servers_str[], const struct net_sockaddr *dns_servers_sa[])
```

相关声明：[dns_resolve_init](#ga27a85c421014373f6aad89634adf8c7d)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

初始化 DNS 解析上下文（DNS Resolving Context）。

<a id="r_ga71eab0f9dd0bc7c02c0d55e7dc6741f3"></a>

```c
int dns_resolve_init_default (struct dns_resolve_context *ctx)
```

相关声明：[dns_resolve_init_default](#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)。

使用默认 Kconfig 选项初始化 DNS 解析上下文（DNS Resolving Context）。

<a id="r_gab04f3b2347e9c59346c10180c6c9ffbc"></a>

```c
int dns_resolve_close (struct dns_resolve_context *ctx)
```

相关声明：[dns_resolve_close](#gab04f3b2347e9c59346c10180c6c9ffbc)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)。

关闭 DNS 解析上下文（DNS Resolving Context）。

<a id="r_ga3cf4e94af65585d89b4a0650dbd9d46e"></a>

```c
bool dns_resolve_is_active (struct dns_resolve_context *ctx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[dns_resolve_is_active](#ga3cf4e94af65585d89b4a0650dbd9d46e)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)。

检查 DNS 解析上下文（DNS Resolving Context）是否处于活动状态。

<a id="r_ga1d3bb0319531bfe0ae95f48bdc51c56f"></a>

```c
int dns_resolve_reconfigure (struct dns_resolve_context *ctx, const char *servers_str[], const struct net_sockaddr *servers_sa[], enum dns_server_source source)
```

相关声明：[dns_resolve_reconfigure](#ga1d3bb0319531bfe0ae95f48bdc51c56f)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[dns_server_source](#gaeda02f82b12e9b7b4dea9fd66be123a7)。

重新配置 DNS 解析上下文（DNS Resolving Context）。

<a id="r_ga3d22eed1d6d017e5bd7a2344775d33b7"></a>

```c
int dns_resolve_reconfigure_with_interfaces (struct dns_resolve_context *ctx, const char *servers_str[], const struct net_sockaddr *servers_sa[], int interfaces[], enum dns_server_source source)
```

相关声明：[dns_resolve_reconfigure_with_interfaces](#ga3d22eed1d6d017e5bd7a2344775d33b7)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[dns_server_source](#gaeda02f82b12e9b7b4dea9fd66be123a7)。

使用新服务器列表重新配置 DNS 解析上下文，并允许将服务器指定到特定网络接口（Network Interface）。

<a id="r_ga54c85b9c69c9a44f2e7bb78165cebfcb"></a>

```c
int dns_resolve_remove (struct dns_resolve_context *ctx, int if_index)
```

相关声明：[dns_resolve_remove](#ga54c85b9c69c9a44f2e7bb78165cebfcb)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)。

从 DNS 解析上下文移除服务器（Servers）。

<a id="r_gae292786587c511c223481f77a4f43017"></a>

```c
int dns_resolve_remove_source (struct dns_resolve_context *ctx, int if_index, enum dns_server_source source)
```

相关声明：[dns_resolve_remove_source](#gae292786587c511c223481f77a4f43017)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[dns_server_source](#gaeda02f82b12e9b7b4dea9fd66be123a7)。

从 DNS 解析上下文移除由特定来源（Source）添加的服务器。

<a id="r_gaf491764b213a891f296c9f91c35b1b72"></a>

```c
int dns_resolve_remove_server_addresses (struct dns_resolve_context *ctx, const struct net_sockaddr *servers_sa[], int interfaces[])
```

相关声明：[dns_resolve_remove_server_addresses](#gaf491764b213a891f296c9f91c35b1b72)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

从 DNS 解析上下文移除具有特定 IP 地址的服务器。

<a id="r_ga7701ddd6b6c5923f0d122a2bcf898cbf"></a>

```c
int dns_resolve_cancel (struct dns_resolve_context *ctx, uint16_t dns_id)
```

相关声明：[dns_resolve_cancel](#ga7701ddd6b6c5923f0d122a2bcf898cbf)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

取消待处理的 DNS 查询（Pending DNS Query）。

<a id="r_gaf2854ca9b839e7cba073e75202ac7e38"></a>

```c
int dns_resolve_cancel_with_name (struct dns_resolve_context *ctx, uint16_t dns_id, const char *query_name, enum dns_query_type query_type)
```

相关声明：[dns_resolve_cancel_with_name](#gaf2854ca9b839e7cba073e75202ac7e38)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[dns_query_type](#ga7169c5a920fb1b0d77910a6ab922e3f0)。

根据 ID、名称和类型取消待处理的 DNS 查询（Pending DNS Query）。

<a id="r_ga24f9bc24e2021b6b528bb15e4fcca49b"></a>

```c
int dns_resolve_name (struct dns_resolve_context *ctx, const char *query, enum dns_query_type type, uint16_t *dns_id, dns_resolve_cb_t cb, void *user_data, int32_t timeout)
```

相关声明：[dns_resolve_name](#ga24f9bc24e2021b6b528bb15e4fcca49b)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[dns_query_type](#ga7169c5a920fb1b0d77910a6ab922e3f0)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[dns_resolve_cb_t](#gafe22d0ef90c581982561ef0c33d1f722)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

解析 DNS 名称（DNS Name）。

<a id="r_gaf28f6f8baa97d0b2341e1bdc02b6cb8c"></a>

```c
static int dns_resolve_service (struct dns_resolve_context *ctx, const char *query, uint16_t *dns_id, dns_resolve_cb_t cb, void *user_data, int32_t timeout)
```

相关声明：[dns_resolve_service](#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[dns_resolve_cb_t](#gafe22d0ef90c581982561ef0c33d1f722)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

解析 DNS 服务（DNS Service）。

<a id="r_gae69cd758e99ea93ef8aac28366918b87"></a>

```c
struct dns_resolve_context * dns_resolve_get_default (void)
```

相关声明：[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[dns_resolve_get_default](#gae69cd758e99ea93ef8aac28366918b87)。

获取默认 DNS 上下文（DNS Context）。

<a id="r_ga3326e98da31313d33861565fe0a10bdf"></a>

```c
static void dns_resolve_enable_packet_forwarding (struct dns_resolve_context *ctx, dns_resolve_pkt_fw_cb_t cb)
```

相关声明：[dns_resolve_enable_packet_forwarding](#ga3326e98da31313d33861565fe0a10bdf)、[dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)、[dns_resolve_pkt_fw_cb_t](#ga7892b3eda301db358b1f18720a2f638c)。

为 DNS 解析上下文安装数据包转发回调（Packet Forwarding Callback）。

<a id="r_gaf891d7e21bddc8fbd029209b4339c01d"></a>

```c
static int dns_get_addr_info (const char *query, enum dns_query_type type, uint16_t *dns_id, dns_resolve_cb_t cb, void *user_data, int32_t timeout)
```

相关声明：[dns_get_addr_info](#gaf891d7e21bddc8fbd029209b4339c01d)、[dns_query_type](#ga7169c5a920fb1b0d77910a6ab922e3f0)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[dns_resolve_cb_t](#gafe22d0ef90c581982561ef0c33d1f722)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

从 DNS 获取 IP 地址信息（IP Address Info）。

<a id="r_ga54ae7aaf53b36951b27f09e1cc82df55"></a>

```c
static int dns_cancel_addr_info (uint16_t dns_id)
```

相关声明：[dns_cancel_addr_info](#ga54ae7aaf53b36951b27f09e1cc82df55)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

取消待处理的 DNS 查询（Pending DNS Query）。

<a id="r_gac8a1d620f07641e4e64ad0757c31aa45"></a>

```c
static int dns_cancel_addr_info_with_name (const char *query_name, enum dns_query_type query_type, uint16_t dns_id)
```

相关声明：[dns_cancel_addr_info_with_name](#gac8a1d620f07641e4e64ad0757c31aa45)、[dns_query_type](#ga7169c5a920fb1b0d77910a6ab922e3f0)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据 ID、名称和类型取消待处理的 DNS 查询（Pending DNS Query）。

## 7.6\_详细说明（Detailed Documentation）

<a id="gaba564a71c4fb4c44fae69015e880b0db"></a>

### `DNS_MAX_NAME_SIZE`

```c
#define DNS_MAX_NAME_SIZE 20
```

```c
#include <zephyr/net/dns_resolve.h>
```

解析所得名称（Resolved Name）的最大大小。

<a id="gac709b355684d44e943c26c6953187df4"></a>

### `DNS_MAX_PRIVATE_DATA_SIZE`

```c
#define DNS_MAX_PRIVATE_DATA_SIZE 128
```

```c
#include <zephyr/net/dns_resolve.h>
```

私有资源记录数据（Private RR Data）的最大大小。

<a id="ga7b6c39611abd40d2d0510c9e38383ecc"></a>

### `DNS_MAX_TEXT_SIZE`

```c
#define DNS_MAX_TEXT_SIZE 64
```

```c
#include <zephyr/net/dns_resolve.h>
```

解析所得 TXT 记录（Resolved TXT Record）的最大大小。

<a id="ga4db137a83d3917bcad1489e25a639666"></a>

### `DNS_RR_TYPE_PRIVATE_END_VALUE`

```c
#define DNS_RR_TYPE_PRIVATE_END_VALUE 65534
```

```c
#include <zephyr/net/dns_resolve.h>
```

私有资源记录类型范围（Private RR Type Range）的结束值，见 RFC 6895。

<a id="ga924d2d4d3b5205a605f4ab69dffdf294"></a>

### `DNS_RR_TYPE_PRIVATE_START_VALUE`

```c
#define DNS_RR_TYPE_PRIVATE_START_VALUE 65280
```

```c
#include <zephyr/net/dns_resolve.h>
```

私有资源记录类型范围（Private RR Type Range）的起始值，见 RFC 6895。

<a id="gafe22d0ef90c581982561ef0c33d1f722"></a>

### `dns_resolve_cb_t`

```c
typedef void(* dns_resolve_cb_t) (enum dns_resolve_status status, struct dns_addrinfo *info, void *user_data)
```

```c
#include <zephyr/net/dns_resolve.h>
```

DNS 解析回调（DNS Resolve Callback）。

DNS 解析成功后调用 DNS 解析回调（DNS Resolve Callback）。解析器可多次调用此回调，每个已解析地址对应一次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `status` | 查询状态（Query Status）：每解析出一个地址返回 DNS_EAI_INPROGRESS；DNS_EAI_ALLDONE 表示解析结束，此时 info 为 NULL；手动取消查询或发生超时时返回 DNS_EAI_CANCELED；服务器无法解析名称时返回 DNS_EAI_FAIL；不存在该名称时返回 DNS_EAI_NODATA；其他值表示发生错误。 |
| `info` | 查询结果（Query Results）存储于此。 |
| `user_data` | 调用 dns_resolve_name() 时给出的用户数据（User Data）。 |

<a id="ga7892b3eda301db358b1f18720a2f638c"></a>

### `dns_resolve_pkt_fw_cb_t`

```c
typedef void(* dns_resolve_pkt_fw_cb_t) (struct net_buf *dns_data, size_t buf_len, void *user_data)
```

```c
#include <zephyr/net/dns_resolve.h>
```

将收到的 DNS 服务器数据包传给应用的 DNS 解析回调（DNS Resolve Callback）。

DNS 解析成功后调用 DNS 解析数据包转发回调（DNS Resolve Packet Forwarding Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dns_data` | 指向包含 DNS 报文（DNS Message）的数据缓冲区的指针。 |
| `buf_len` | 数据长度（Data Length）。 |
| `user_data` | 调用 dns_resolve 函数时传入的用户数据（User Data）。 |

<a id="ga7169c5a920fb1b0d77910a6ab922e3f0"></a>

### `dns_query_type`

```c
enum dns_query_type
```

```c
#include <zephyr/net/dns_resolve.h>
```

DNS 查询类型枚举（Query Type Enum）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DNS_QUERY_TYPE_A` | IPv4 查询（Query）。 |
| `DNS_QUERY_TYPE_CNAME` | 规范名称查询（Canonical Name Query）。 |
| `DNS_QUERY_TYPE_PTR` | 指针查询（Pointer Query）。 |
| `DNS_QUERY_TYPE_TXT` | 文本查询（Text Query）。 |
| `DNS_QUERY_TYPE_AAAA` | IPv6 查询（Query）。 |
| `DNS_QUERY_TYPE_SRV` | 服务位置查询（Service Location Query）。 |
| `DNS_QUERY_TYPE_ANY` | 请求全部记录类型（Record Types）的查询。 |
| `DNS_QUERY_TYPE_RESERVED` | 保留的查询类型值（Reserved Query Type Value）。 |

<a id="ga8a4330071b7161e1738dd91b1f6d6097"></a>

### `dns_resolve_extension`

```c
enum dns_resolve_extension
```

```c
#include <zephyr/net/dns_resolve.h>
```

枚举地址信息中可用的扩展（Extensions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DNS_RESOLVE_NONE` | 未使用扩展（Extension）。 |
| `DNS_RESOLVE_TXT` | 返回 TXT 字段。 |
| `DNS_RESOLVE_SRV` | 返回 SRV 字段。 |
| `DNS_RESOLVE_PRIVATE` | 返回私有资源记录（Private RR）。 |

<a id="ga5baf1fea0482fb3a940b4f5350a3c58e"></a>

### `dns_resolve_status`

```c
enum dns_resolve_status
```

```c
#include <zephyr/net/dns_resolve.h>
```

回调使用的状态值（Status Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DNS_EAI_BADFLAGS` | ai_flags 字段值无效。 |
| `DNS_EAI_NONAME` | NAME 或 SERVICE 未知。 |
| `DNS_EAI_AGAIN` | 名称解析（Name Resolution）暂时失败。 |
| `DNS_EAI_FAIL` | 名称解析（Name Resolution）发生不可恢复的故障。 |
| `DNS_EAI_NODATA` | 没有与 NAME 关联的地址。 |
| `DNS_EAI_FAMILY` | 不支持 ai_family。 |
| `DNS_EAI_SOCKTYPE` | 不支持 ai_socktype。 |
| `DNS_EAI_SERVICE` | ai_socktype 不支持 SRV。 |
| `DNS_EAI_ADDRFAMILY` | 不支持 NAME 的地址族（Address Family）。 |
| `DNS_EAI_MEMORY` | 内存分配失败（Memory Allocation Failure）。 |
| `DNS_EAI_SYSTEM` | 系统错误（System Error）通过 errno 返回。 |
| `DNS_EAI_OVERFLOW` | 参数缓冲区溢出（Argument Buffer Overflow）。 |
| `DNS_EAI_INPROGRESS` | 请求正在处理（In Progress）。 |
| `DNS_EAI_CANCELED` | 请求已取消（Canceled）。 |
| `DNS_EAI_NOTCANCELED` | 请求未取消（Not Canceled）。 |
| `DNS_EAI_ALLDONE` | 全部请求完成（All Requests Done）。 |
| `DNS_EAI_IDN_ENCODE` | 国际化域名编码（IDN Encoding）失败。 |

<a id="gaeda02f82b12e9b7b4dea9fd66be123a7"></a>

### `dns_server_source`

```c
enum dns_server_source
```

```c
#include <zephyr/net/dns_resolve.h>
```

添加 DNS 服务器的实体（Entity）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DNS_SOURCE_UNKNOWN` | 来源未知（Unknown Source）。 |
| `DNS_SOURCE_MANUAL` | 服务器信息由手动添加，例如由应用程序添加。 |
| `DNS_SOURCE_DHCPV4` | 服务器信息来自 DHCPv4 服务器。 |
| `DNS_SOURCE_DHCPV6` | 服务器信息来自 DHCPv6 服务器。 |
| `DNS_SOURCE_IPV6_RA` | 服务器信息来自 IPv6 无状态地址自动配置（SLAAC），即路由器通告（Router Advertisement）。 |
| `DNS_SOURCE_PPP` | 服务器信息来自点对点协议（PPP）。 |

<a id="ga54ae7aaf53b36951b27f09e1cc82df55"></a>

### `dns_cancel_addr_info()`

```c
int dns_cancel_addr_info ( uint16_t dns_id)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/dns_resolve.h>
```

取消待处理的 DNS 查询（Pending DNS Query）。

释放待处理查询（Pending Query）所使用的 DNS 资源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dns_id` | 待处理查询的 DNS ID。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gac8a1d620f07641e4e64ad0757c31aa45"></a>

### `dns_cancel_addr_info_with_name()`

```c
int dns_cancel_addr_info_with_name ( const char * query_name, enum dns_query_type query_type, uint16_t dns_id )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/dns_resolve.h>
```

根据 ID、名称和类型取消待处理的 DNS 查询（Pending DNS Query）。

释放待处理查询（Pending Query）所使用的 DNS 资源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `query_name` | 要查询的资源名称，即主机名（Hostname）。 |
| `query_type` | 查询类型（Query Type），为 A 或 AAAA。 |
| `dns_id` | 待处理查询的 DNS ID。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gaf891d7e21bddc8fbd029209b4339c01d"></a>

### `dns_get_addr_info()`

```c
int dns_get_addr_info ( const char * query, enum dns_query_type type, uint16_t * dns_id, dns_resolve_cb_t cb, void * user_data, int32_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/dns_resolve.h>
```

从 DNS 获取 IP 地址信息（IP Address Info）。

此函数可用于解析 IPv4 或 IPv6 地址等。注意，这是异步调用（Asynchronous Call）：函数立即返回，解析结束或超时后，系统调用回调。解析器可能查询多个已配置的服务器，具体取决于配置：并行向所有服务器发送请求，或依次尝试，直到其中一个成功。只向调用者报告第一个成功响应。此变体使用系统范围的 DNS 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `query` | 调用者要解析的对象。 |
| `type` | 调用者要获取的数据类型。 |
| `dns_id` | 返回给调用者的 DNS ID。取消查询时需要此 ID；若无需取消查询，可将此参数设为 NULL。 |
| `cb` | 解析结束或超时后调用的回调（Callback）。 |
| `user_data` | 用户数据（User Data）。 |
| `timeout` | 连接超时值（Timeout）。可用值：SYS_FOREVER_MS 表示持续尝试查询，耗时过长时须由使用者手动取消；大于 0 表示开始查询，并由系统在指定毫秒数后使其超时。 |

**返回（Returns）**：返回：成功启动解析时为 0，否则小于 0。

<a id="ga13a7cbc3b59a12278f4b035013c03b1d"></a>

### `dns_query_type_is_private()`

```c
bool dns_query_type_is_private ( enum dns_query_type type)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/dns_resolve.h>
```

检查查询类型是否为私有资源记录（Private RR）；RFC 6895 规定范围为 65280～65534。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 要检查的查询类型（Query Type）。 |

**返回（Returns）**：返回：类型处于私有资源记录（Private RR）范围内时为 true，否则为 false。

<a id="ga7701ddd6b6c5923f0d122a2bcf898cbf"></a>

### `dns_resolve_cancel()`

```c
int dns_resolve_cancel ( struct dns_resolve_context * ctx, uint16_t dns_id )
```

```c
#include <zephyr/net/dns_resolve.h>
```

取消待处理的 DNS 查询（Pending DNS Query）。

释放待处理查询（Pending Query）所使用的 DNS 资源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |
| `dns_id` | 待处理查询的 DNS ID。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gaf2854ca9b839e7cba073e75202ac7e38"></a>

### `dns_resolve_cancel_with_name()`

```c
int dns_resolve_cancel_with_name ( struct dns_resolve_context * ctx, uint16_t dns_id, const char * query_name, enum dns_query_type query_type )
```

```c
#include <zephyr/net/dns_resolve.h>
```

根据 ID、名称和类型取消待处理的 DNS 查询（Pending DNS Query）。

释放待处理查询（Pending Query）所使用的 DNS 资源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |
| `dns_id` | 待处理查询的 DNS ID。 |
| `query_name` | 要查询的资源名称，即主机名（Hostname）。 |
| `query_type` | 查询类型（Query Type），为 A 或 AAAA。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gab04f3b2347e9c59346c10180c6c9ffbc"></a>

### `dns_resolve_close()`

```c
int dns_resolve_close ( struct dns_resolve_context * ctx)
```

```c
#include <zephyr/net/dns_resolve.h>
```

关闭 DNS 解析上下文（DNS Resolving Context）。

释放 DNS 解析上下文（DNS Resolving Context），并将其标记为不可用。调用者必须再次调用 dns_resolve_init()，才能重新使用该上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga3326e98da31313d33861565fe0a10bdf"></a>

### `dns_resolve_enable_packet_forwarding()`

```c
void dns_resolve_enable_packet_forwarding ( struct dns_resolve_context * ctx, dns_resolve_pkt_fw_cb_t cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/dns_resolve.h>
```

为 DNS 解析上下文安装数据包转发回调（Packet Forwarding Callback）。

安装此回调后，从 DNS 服务器收到的报文将传给该回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 指向 DNS 解析器上下文（DNS Resolver Context）的指针。如果应用要使用默认上下文，可调用 dns_resolve_get_default() 获取其指针。 |
| `cb` | 应用需要接收的 DNS 报文时调用的回调（Callback）。 |

<a id="gae69cd758e99ea93ef8aac28366918b87"></a>

### `dns_resolve_get_default()`

```c
struct dns_resolve_context * dns_resolve_get_default ( void )
```

```c
#include <zephyr/net/dns_resolve.h>
```

获取默认 DNS 上下文（DNS Context）。

系统级 DNS 上下文（System Level DNS Context）使用项目配置文件定义的 DNS 服务器。如果使用者没有定义任何 DNS 服务器，使用默认上下文解析 DNS 名称将不执行任何操作。配置选项在 subsys/net/lib/dns/Kconfig 文件中说明。

**返回（Returns）**：返回：默认 DNS 上下文（Default DNS Context）。

<a id="ga27a85c421014373f6aad89634adf8c7d"></a>

### `dns_resolve_init()`

```c
int dns_resolve_init ( struct dns_resolve_context * ctx, const char * dns_servers_str[], const struct net_sockaddr * dns_servers_sa[] )
```

```c
#include <zephyr/net/dns_resolve.h>
```

初始化 DNS 解析上下文（DNS Resolving Context）。

此函数设置 DNS 服务器地址，并初始化实际解析器使用的 DNS 上下文（DNS Context）。服务器地址可用文本、struct net_sockaddr 或两者共同指定。注意，推荐使用 dns_get_addr_info() API 解析 DNS 名称；在这种情况下，系统已设置 DNS 服务器，使用者无需调用 dns_resolve_init()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。如果上下文变量在栈上分配，则必须在整个解析期间保持有效。调用者无需预先填写该变量，也无需事后修改上下文。 |
| `dns_servers_str` | 以文本字符串表示的 DNS 服务器地址。数组以 NULL 结束，字符串中可带端口号。带或不带端口的地址语法为：IPv4：`10.0.9.1`；IPv4 加端口：`10.0.9.1:5353`；IPv6：`2001:db8::22:42`；IPv6 加端口：`[2001:db8::22:42]:5353`。 |
| `dns_servers_sa` | 以 struct net_sockaddr 表示的 DNS 服务器地址。数组以 NULL 结束。struct net_sockaddr 中的端口号可选，设为 0 时使用默认端口。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga71eab0f9dd0bc7c02c0d55e7dc6741f3"></a>

### `dns_resolve_init_default()`

```c
int dns_resolve_init_default ( struct dns_resolve_context * ctx)
```

```c
#include <zephyr/net/dns_resolve.h>
```

使用默认 Kconfig 选项初始化 DNS 解析上下文（DNS Resolving Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga3cf4e94af65585d89b4a0650dbd9d46e"></a>

### `dns_resolve_is_active()`

```c
bool dns_resolve_is_active ( struct dns_resolve_context * ctx)
```

```c
#include <zephyr/net/dns_resolve.h>
```

检查 DNS 解析上下文（DNS Resolving Context）是否处于活动状态。

使用至少一个 DNS 服务器初始化上下文后，上下文变为活动（Active）；关闭后则变为非活动。此状态不代表服务器自身的状态，例如服务器是否可达。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 已调用 dns_resolve_init() 的 DNS 上下文，或 NULL。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 上下文处于活动状态（Active）。 |
| `false` | 上下文未处于活动状态（Inactive），或 ctx 为 NULL。 |

<a id="ga24f9bc24e2021b6b528bb15e4fcca49b"></a>

### `dns_resolve_name()`

```c
int dns_resolve_name ( struct dns_resolve_context * ctx, const char * query, enum dns_query_type type, uint16_t * dns_id, dns_resolve_cb_t cb, void * user_data, int32_t timeout )
```

```c
#include <zephyr/net/dns_resolve.h>
```

解析 DNS 名称（DNS Name）。

此函数可用于解析 IPv4 或 IPv6 地址等。注意，这是异步调用（Asynchronous Call）：函数立即返回，解析结束或超时后，系统调用回调。解析器可能查询多个已配置的服务器，具体取决于配置：并行向所有服务器发送请求，或依次尝试，直到其中一个成功。只向调用者报告第一个成功响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |
| `query` | 调用者要解析的对象。 |
| `type` | 调用者要获取的数据类型。 |
| `dns_id` | 返回给调用者的 DNS ID。取消查询时需要此 ID；若无需取消查询，可将此参数设为 NULL。 |
| `cb` | 解析结束或超时后调用的回调（Callback）。 |
| `user_data` | 用户数据（User Data）。 |
| `timeout` | 查询超时值（Timeout）。可用值：SYS_FOREVER_MS 表示持续尝试查询，耗时过长时须由使用者手动取消；大于 0 表示开始查询，并由系统在指定毫秒数后使其超时。 |

**返回（Returns）**：返回：成功启动解析时为 0，否则小于 0。

<a id="ga1d3bb0319531bfe0ae95f48bdc51c56f"></a>

### `dns_resolve_reconfigure()`

```c
int dns_resolve_reconfigure ( struct dns_resolve_context * ctx, const char * servers_str[], const struct net_sockaddr * servers_sa[], enum dns_server_source source )
```

```c
#include <zephyr/net/dns_resolve.h>
```

重新配置 DNS 解析上下文（DNS Resolving Context）。

使用新的服务器列表（Server List）重新配置 DNS 上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |
| `servers_str` | 以文本字符串表示的 DNS 服务器地址。数组以 NULL 结束，字符串中可带端口号。带或不带端口的地址语法为：IPv4：`10.0.9.1`；IPv4 加端口：`10.0.9.1:5353`；IPv6：`2001:db8::22:42`；IPv6 加端口：`[2001:db8::22:42]:5353`。 |
| `servers_sa` | 以 struct net_sockaddr 表示的 DNS 服务器地址。数组以 NULL 结束。struct net_sockaddr 中的端口号可选，设为 0 时使用默认端口。 |
| `source` | DNS 服务器来源（Source），例如手动配置、DHCPv4／6 等。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga3d22eed1d6d017e5bd7a2344775d33b7"></a>

### `dns_resolve_reconfigure_with_interfaces()`

```c
int dns_resolve_reconfigure_with_interfaces ( struct dns_resolve_context * ctx, const char * servers_str[], const struct net_sockaddr * servers_sa[], int interfaces[], enum dns_server_source source )
```

```c
#include <zephyr/net/dns_resolve.h>
```

使用新服务器列表重新配置 DNS 解析上下文，并允许将服务器指定到特定网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |
| `servers_str` | 以文本字符串表示的 DNS 服务器地址。数组以 NULL 结束，字符串中可带端口号。带或不带端口的地址语法为：IPv4：`10.0.9.1`；IPv4 加端口：`10.0.9.1:5353`；IPv6：`2001:db8::22:42`；IPv6 加端口：`[2001:db8::22:42]:5353`。 |
| `servers_sa` | 以 struct net_sockaddr 表示的 DNS 服务器地址。数组以 NULL 结束。struct net_sockaddr 中的端口号可选，设为 0 时使用默认端口。 |
| `interfaces` | DNS 服务器绑定的网络接口（Network Interfaces），以网络接口索引数组表示。数组长度必须与 servers_str 和 servers_sa 数组相同。 |
| `source` | DNS 服务器来源（Source），例如手动配置、DHCPv4／6 等。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga54c85b9c69c9a44f2e7bb78165cebfcb"></a>

### `dns_resolve_remove()`

```c
int dns_resolve_remove ( struct dns_resolve_context * ctx, int if_index )
```

```c
#include <zephyr/net/dns_resolve.h>
```

从 DNS 解析上下文移除服务器（Servers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |
| `if_index` | 从中移除 DNS 服务器的网络接口（Network Interface）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gaf491764b213a891f296c9f91c35b1b72"></a>

### `dns_resolve_remove_server_addresses()`

```c
int dns_resolve_remove_server_addresses ( struct dns_resolve_context * ctx, const struct net_sockaddr * servers_sa[], int interfaces[] )
```

```c
#include <zephyr/net/dns_resolve.h>
```

从 DNS 解析上下文移除具有特定 IP 地址的服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |
| `servers_sa` | 以 struct net_sockaddr 表示的 DNS 服务器地址。数组以 NULL 结束。struct net_sockaddr 中的端口号可选，设为 0 时使用默认端口。 |
| `interfaces` | DNS 服务器绑定的网络接口（Network Interfaces），以网络接口索引数组表示。数组长度必须与 servers_sa 数组相同。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gae292786587c511c223481f77a4f43017"></a>

### `dns_resolve_remove_source()`

```c
int dns_resolve_remove_source ( struct dns_resolve_context * ctx, int if_index, enum dns_server_source source )
```

```c
#include <zephyr/net/dns_resolve.h>
```

从 DNS 解析上下文移除由特定来源（Source）添加的服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |
| `if_index` | 从中移除 DNS 服务器的网络接口（Network Interface）。 |
| `source` | DNS 服务器来源（Source），例如手动配置、DHCPv4／6 等。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="gaf28f6f8baa97d0b2341e1bdc02b6cb8c"></a>

### `dns_resolve_service()`

```c
int dns_resolve_service ( struct dns_resolve_context * ctx, const char * query, uint16_t * dns_id, dns_resolve_cb_t cb, void * user_data, int32_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/dns_resolve.h>
```

解析 DNS 服务（DNS Service）。

此函数可解析 DNS 服务发现（DNS-SD）所需的服务记录（Service Records）。注意，这是异步调用（Asynchronous Call）：函数立即返回，解析结束或超时后，系统调用回调。每收到一个响应就调用一次回调。查询必须手动取消，或通过超时取消。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | DNS 上下文（DNS Context）。 |
| `query` | 调用者要解析的对象。 |
| `dns_id` | 返回给调用者的 DNS ID。取消查询时需要此 ID；若无需取消查询，可将此参数设为 NULL。 |
| `cb` | 解析结束或超时后调用的回调（Callback）。 |
| `user_data` | 用户数据（User Data）。 |
| `timeout` | 查询超时值（Timeout）。可用值：SYS_FOREVER_MS 表示持续尝试查询，耗时过长时须由使用者手动取消；大于 0 表示开始查询，并由系统在指定毫秒数后使其超时。 |

**返回（Returns）**：返回：成功启动解析时为 0，否则小于 0。


## 7.7\_原页交叉引用（Cross References）

- [dns_resolve_txt](../network_application_model_reference/P024_dns_resolve_txt_结构体.md)
- [dns_resolve_srv](../network_application_model_reference/P023_dns_resolve_srv_结构体.md)
- [dns_resolve_private](../network_application_model_reference/P022_dns_resolve_private_结构体.md)
- [dns_addrinfo](../network_application_model_reference/P018_dns_addrinfo_结构体.md)
- [dns_resolve_context](../network_application_model_reference/P019_dns_resolve_context_结构体.md)
- [RFC 6895](https://datatracker.ietf.org/doc/html/rfc6895)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/net/dns_resolve.h](../api_file_clock_network_reference/P006_zephyr__net__dns_resolve.h_文件参考.md)
- [errno](../error_reference/P003_系统错误号公共接口.md#gab03f640d90fbc5bcb75285d08a0f25ed)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134"></a>
<a id="gga7169c5a920fb1b0d77910a6ab922e3f0a128aa925168ae2b096ff879c7648d2e4"></a>
<a id="gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa"></a>
<a id="gga7169c5a920fb1b0d77910a6ab922e3f0a42c3f3d5876b275f764a67e1bf43d850"></a>
<a id="gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049"></a>
<a id="gga7169c5a920fb1b0d77910a6ab922e3f0a2e976a8ed83e609b4836444d7a95d65d"></a>
<a id="gga7169c5a920fb1b0d77910a6ab922e3f0a0b8a4c108a7ae4742d2235b64c3d8c06"></a>
<a id="gga7169c5a920fb1b0d77910a6ab922e3f0aed30f5d6a68ef4503ca6f3d60d1c0e6a"></a>
<a id="gga8a4330071b7161e1738dd91b1f6d6097a80ada4858b77463f1af5b06660aaaf3b"></a>
<a id="gga8a4330071b7161e1738dd91b1f6d6097a6a5d547c65f5d265bfd4f1968ed3db98"></a>
<a id="gga8a4330071b7161e1738dd91b1f6d6097af0b69e02c8e086e64ce194cd66507672"></a>
<a id="gga8a4330071b7161e1738dd91b1f6d6097a9f582f9d2424409736f32ac0051fc582"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea9989bb26c930dcf90b5aaab224f19793"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea8440de8b7109dfcca71acca6c7ac4103"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58eaba718125a826939380fdbcc9c1fb4512"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58eaeb7d2677167f5bc230da2eea2a81d06c"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58eae932d5596c55d090cf2ebe43ad59bd35"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836"></a>
<a id="gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4"></a>
<a id="ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9"></a>
<a id="ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33"></a>
<a id="ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b"></a>
<a id="ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b"></a>
<a id="ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9"></a>
<a id="ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_数字音频接口（DAI）.md) · [返回大纲](大纲.md) · [下一章](P008_IEEE 802.3 管理接口。.md)
