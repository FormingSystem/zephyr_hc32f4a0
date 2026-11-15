---
id: learning.zephyr-docs.api-source-reference.page-578
title: netdb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第578章\_netdb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html)。

## 578.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="anet_2socket_8h_html"></a>
<a id="anetdb_8h_html_a070fa0f353af9fc05138caeb6348c29a"></a>
<a id="anetdb_8h_html_a0a2c07c88b888c1c181e8f277f53aee9"></a>
<a id="anetdb_8h_html_a0f38280702a5ae01bd02e2e574bfce35"></a>
<a id="anetdb_8h_html_a199e7f8bde21efa3d6d44efd870a72a9"></a>
<a id="anetdb_8h_html_a3173746d8bc19a57e57d76f5f8abe5fd"></a>
<a id="anetdb_8h_html_a34ad0dc5368b67dbdb492cf09badc2f4"></a>
<a id="anetdb_8h_html_a3ac0597abceec2060997db1355d462f8"></a>
<a id="anetdb_8h_html_a4b9065f385acd38096aa190110429420"></a>
<a id="anetdb_8h_html_a5c82f7d491ae353012f42bf60e9c9f20"></a>
<a id="anetdb_8h_html_a6a806414e4ae5bffb09e3a1d25d8db75"></a>
<a id="anetdb_8h_html_a8033b3171adc399803161694ea422c4f"></a>
<a id="anetdb_8h_html_a816ddf34b4aa42f0b9c70c81ce832fb2"></a>
<a id="anetdb_8h_html_a9c23830b9c634ac761f3f2daa3e6b724"></a>
<a id="anetdb_8h_html_a9d976afa60cead1e7f82bad149626b7f"></a>
<a id="anetdb_8h_html_aa04c5e5229bf6ad9dc77bb261577df10"></a>
<a id="anetdb_8h_html_ab2238818a534ce99ec4b5f4a22b659da"></a>
<a id="anetdb_8h_html_ac4f01c33d33a644fdda8b19bf18a325a"></a>
<a id="anetdb_8h_html_accc64bf7bad3dd2a6b683c10533aa076"></a>
<a id="anetdb_8h_html_ad3c7650e6d2bc3c27f9f089af05ee481"></a>
<a id="anetdb_8h_html_adc9ea491d9008de7cd9e0a5b9147ca70"></a>
<a id="anetdb_8h_html_adf81140af263bf72a02dc4a484e98d6a"></a>
<a id="anetdb_8h_html_ae854ec9955d62f1791342f9c2b8abcee"></a>
<a id="anetdb_8h_html_af6bd8540206fe6379df889064f4a9748"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aposix_2sys_2socket_8h_html_a3f5f480bed01f54df564b99350f1d1bb"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructhostent_html"></a>
<a id="astructhostent_html_a405ebb31a6922898809635b03f0faf06"></a>
<a id="astructhostent_html_a439d6e5efa18bc14aab63b14a12ae371"></a>
<a id="astructhostent_html_a4ff8499f29c5111435d6ed4adccfb621"></a>
<a id="astructhostent_html_ab9db18bfcc6adfc9c944b0c06ec2dccc"></a>
<a id="astructhostent_html_ac266a0b528443e9479f2d8e1680b5e78"></a>
<a id="astructnetent_html"></a>
<a id="astructnetent_html_a108f91da08bdf576c768429286b0f5c1"></a>
<a id="astructnetent_html_ab872aa2c431de28a5a72fc0cae693f0b"></a>
<a id="astructnetent_html_ad6d1687141f88ffde193f198b2c36735"></a>
<a id="astructnetent_html_ae04a32bad76f6bd5cc350179ea88a1ee"></a>
<a id="astructprotoent_html"></a>
<a id="astructprotoent_html_a3ee5b885146ea094cc17e0e210cfc606"></a>
<a id="astructprotoent_html_aa0adbe8a3e56d93695d9e1d171e1f2f4"></a>
<a id="astructprotoent_html_ac70bd11c764a52b2ed1a7c54760b5385"></a>
<a id="astructservent_html"></a>
<a id="astructservent_html_a1bdae74e6bdf91235fbba6d08eb4537c"></a>
<a id="astructservent_html_a379e36da163ba55b73d770a27bb2430b"></a>
<a id="astructservent_html_a3f8d3cf12c142b8f0bfab810975783d5"></a>
<a id="astructservent_html_a6f0175c9ea10b6749032259c26677815"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_NETDB_H_
#define ZEPHYR_INCLUDE_POSIX_NETDB_H_

#include <zephyr/net/socket.h>

#ifndef NI_MAXSERV
#define NI_MAXSERV 32
#endif

#define EAI_BADFLAGS DNS_EAI_BADFLAGS
#define EAI_NONAME DNS_EAI_NONAME
#define EAI_AGAIN DNS_EAI_AGAIN
#define EAI_FAIL DNS_EAI_FAIL
#define EAI_NODATA DNS_EAI_NODATA
#define EAI_MEMORY DNS_EAI_MEMORY
#define EAI_SYSTEM DNS_EAI_SYSTEM
#define EAI_SERVICE DNS_EAI_SERVICE
#define EAI_SOCKTYPE DNS_EAI_SOCKTYPE
#define EAI_FAMILY DNS_EAI_FAMILY
#define EAI_OVERFLOW DNS_EAI_OVERFLOW

#ifdef __cplusplus
extern "C" {
#endif

struct hostent {
        char *h_name;
        char **h_aliases;
        int h_addrtype;
        int h_length;
        char **h_addr_list;
};

struct netent {
        char *n_name;
        char **n_aliases;
        int n_addrtype;
        uint32_t n_net;
};

struct protoent {
        char *p_name;
        char **p_aliases;
        int p_proto;
};

struct servent {
        char *s_name;
        char **s_aliases;
        int s_port;
        char *s_proto;
};

#define addrinfo zsock_addrinfo

void endhostent(void);
void endnetent(void);
void endprotoent(void);
void endservent(void);
void freeaddrinfo(struct addrinfo *ai);
const char *gai_strerror(int errcode);
int getaddrinfo(const char *host, const char *service, const struct addrinfo *hints,
                struct addrinfo **res);
struct hostent *gethostent(void);
int getnameinfo(const struct sockaddr *addr, socklen_t addrlen, char *host, socklen_t hostlen,
                char *serv, socklen_t servlen, int flags);
struct netent *getnetbyaddr(uint32_t net, int type);
struct netent *getnetbyname(const char *name);
struct netent *getnetent(void);
struct protoent *getprotobyname(const char *name);
struct protoent *getprotobynumber(int proto);
struct protoent *getprotoent(void);
struct servent *getservbyname(const char *name, const char *proto);
struct servent *getservbyport(int port, const char *proto);
struct servent *getservent(void);
void sethostent(int stayopen);
void setnetent(int stayopen);
void setprotoent(int stayopen);
void setservent(int stayopen);

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_INCLUDE_POSIX_NETDB_H_ */
```

## 578.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 91 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_NETDB_H_`。

## 578.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [hostent](../posix_system_model_reference/P004_hostent_结构体.md)
- [h_name](../posix_system_model_reference/P004_hostent_结构体.md#a439d6e5efa18bc14aab63b14a12ae371)
- [h_aliases](../posix_system_model_reference/P004_hostent_结构体.md#ac266a0b528443e9479f2d8e1680b5e78)
- [h_addrtype](../posix_system_model_reference/P004_hostent_结构体.md#a405ebb31a6922898809635b03f0faf06)
- [h_length](../posix_system_model_reference/P004_hostent_结构体.md#ab9db18bfcc6adfc9c944b0c06ec2dccc)
- [h_addr_list](../posix_system_model_reference/P004_hostent_结构体.md#a4ff8499f29c5111435d6ed4adccfb621)
- [netent](../posix_system_model_reference/P008_netent_结构体.md)
- [n_name](../posix_system_model_reference/P008_netent_结构体.md#ad6d1687141f88ffde193f198b2c36735)
- [n_aliases](../posix_system_model_reference/P008_netent_结构体.md#ab872aa2c431de28a5a72fc0cae693f0b)
- [n_addrtype](../posix_system_model_reference/P008_netent_结构体.md#ae04a32bad76f6bd5cc350179ea88a1ee)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [n_net](../posix_system_model_reference/P008_netent_结构体.md#a108f91da08bdf576c768429286b0f5c1)
- [protoent](../posix_system_model_reference/P010_protoent_结构体.md)
- [p_name](../posix_system_model_reference/P010_protoent_结构体.md#ac70bd11c764a52b2ed1a7c54760b5385)
- [p_aliases](../posix_system_model_reference/P010_protoent_结构体.md#aa0adbe8a3e56d93695d9e1d171e1f2f4)
- [p_proto](../posix_system_model_reference/P010_protoent_结构体.md#a3ee5b885146ea094cc17e0e210cfc606)
- [servent](../posix_system_model_reference/P016_servent_结构体.md)
- [s_name](../posix_system_model_reference/P016_servent_结构体.md#a1bdae74e6bdf91235fbba6d08eb4537c)
- [s_aliases](../posix_system_model_reference/P016_servent_结构体.md#a3f8d3cf12c142b8f0bfab810975783d5)
- [s_port](../posix_system_model_reference/P016_servent_结构体.md#a6f0175c9ea10b6749032259c26677815)
- [s_proto](../posix_system_model_reference/P016_servent_结构体.md#a379e36da163ba55b73d770a27bb2430b)
- [endhostent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#accc64bf7bad3dd2a6b683c10533aa076)
- [endnetent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a9c23830b9c634ac761f3f2daa3e6b724)
- [endprotoent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a3ac0597abceec2060997db1355d462f8)
- [endservent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#adf81140af263bf72a02dc4a484e98d6a)
- [freeaddrinfo](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#ae854ec9955d62f1791342f9c2b8abcee)
- [addrinfo](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#af6bd8540206fe6379df889064f4a9748)
- [gai_strerror](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a8033b3171adc399803161694ea422c4f)
- [getaddrinfo](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#adc9ea491d9008de7cd9e0a5b9147ca70)
- [gethostent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a4b9065f385acd38096aa190110429420)
- [getnameinfo](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a5c82f7d491ae353012f42bf60e9c9f20)
- [socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a3f5f480bed01f54df564b99350f1d1bb)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [getnetbyaddr](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a0f38280702a5ae01bd02e2e574bfce35)
- [getnetbyname](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a34ad0dc5368b67dbdb492cf09badc2f4)
- [getnetent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a199e7f8bde21efa3d6d44efd870a72a9)
- [getprotobyname](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a3173746d8bc19a57e57d76f5f8abe5fd)
- [getprotobynumber](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#ac4f01c33d33a644fdda8b19bf18a325a)
- [getprotoent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a816ddf34b4aa42f0b9c70c81ce832fb2)
- [getservbyname](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a9d976afa60cead1e7f82bad149626b7f)
- [getservbyport](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a070fa0f353af9fc05138caeb6348c29a)
- [getservent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#aa04c5e5229bf6ad9dc77bb261577df10)
- [sethostent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#ad3c7650e6d2bc3c27f9f089af05ee481)
- [setnetent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a0a2c07c88b888c1c181e8f277f53aee9)
- [setprotoent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#a6a806414e4ae5bffb09e3a1d25d8db75)
- [setservent](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html#ab2238818a534ce99ec4b5f4a22b659da)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [hostent::h_addrtype](../posix_system_model_reference/P004_hostent_结构体.md#a405ebb31a6922898809635b03f0faf06)
- [hostent::h_name](../posix_system_model_reference/P004_hostent_结构体.md#a439d6e5efa18bc14aab63b14a12ae371)
- [hostent::h_addr_list](../posix_system_model_reference/P004_hostent_结构体.md#a4ff8499f29c5111435d6ed4adccfb621)
- [hostent::h_length](../posix_system_model_reference/P004_hostent_结构体.md#ab9db18bfcc6adfc9c944b0c06ec2dccc)
- [hostent::h_aliases](../posix_system_model_reference/P004_hostent_结构体.md#ac266a0b528443e9479f2d8e1680b5e78)
- [netent::n_net](../posix_system_model_reference/P008_netent_结构体.md#a108f91da08bdf576c768429286b0f5c1)
- [netent::n_aliases](../posix_system_model_reference/P008_netent_结构体.md#ab872aa2c431de28a5a72fc0cae693f0b)
- [netent::n_name](../posix_system_model_reference/P008_netent_结构体.md#ad6d1687141f88ffde193f198b2c36735)
- [netent::n_addrtype](../posix_system_model_reference/P008_netent_结构体.md#ae04a32bad76f6bd5cc350179ea88a1ee)
- [protoent::p_proto](../posix_system_model_reference/P010_protoent_结构体.md#a3ee5b885146ea094cc17e0e210cfc606)
- [protoent::p_aliases](../posix_system_model_reference/P010_protoent_结构体.md#aa0adbe8a3e56d93695d9e1d171e1f2f4)
- [protoent::p_name](../posix_system_model_reference/P010_protoent_结构体.md#ac70bd11c764a52b2ed1a7c54760b5385)
- [servent::s_name](../posix_system_model_reference/P016_servent_结构体.md#a1bdae74e6bdf91235fbba6d08eb4537c)
- [servent::s_proto](../posix_system_model_reference/P016_servent_结构体.md#a379e36da163ba55b73d770a27bb2430b)
- [servent::s_aliases](../posix_system_model_reference/P016_servent_结构体.md#a3f8d3cf12c142b8f0bfab810975783d5)
- [servent::s_port](../posix_system_model_reference/P016_servent_结构体.md#a6f0175c9ea10b6749032259c26677815)

---

[上一章](P577_net_offload.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P579_nordic-domain-id-nrf54h20.h_源码浏览.md)
