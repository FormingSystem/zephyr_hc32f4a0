---
id: learning.zephyr-docs.api-file-supplement-reference.page-79
title: zephyr__posix__netdb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_zephyr\_\_posix\_\_netdb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/net/socket.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 79.1\_数据结构（Data Structures）

<a id="r_hostent"></a>

```c
struct hostent
```

相关声明：[hostent](../posix_system_model_reference/P004_hostent_结构体.md)。

<a id="r_netent"></a>

```c
struct netent
```

相关声明：[netent](../posix_system_model_reference/P008_netent_结构体.md)。

<a id="r_protoent"></a>

```c
struct protoent
```

相关声明：[protoent](../posix_system_model_reference/P010_protoent_结构体.md)。

<a id="r_servent"></a>

```c
struct servent
```

相关声明：[servent](../posix_system_model_reference/P016_servent_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 79.2\_宏定义（Macros）

<a id="r_aefdeadf85356cc2fa0870d86a6055eb1"></a>

```c
#define NI_MAXSERV 32
```

相关声明：[NI_MAXSERV](#aefdeadf85356cc2fa0870d86a6055eb1)。

为使用 `getnameinfo` 的应用程序提供合理的大小（Size）。

<a id="r_a3f3b38f2ac6688612a0fd20f3e6210be"></a>

```c
#define EAI_BADFLAGS DNS_EAI_BADFLAGS
```

相关声明：[EAI_BADFLAGS](#a3f3b38f2ac6688612a0fd20f3e6210be)、[DNS_EAI_BADFLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea9989bb26c930dcf90b5aaab224f19793)。

<a id="r_a0bb00f48d6ba1e8c55b7d85c8e3a19a7"></a>

```c
#define EAI_NONAME DNS_EAI_NONAME
```

相关声明：[EAI_NONAME](#a0bb00f48d6ba1e8c55b7d85c8e3a19a7)、[DNS_EAI_NONAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f)。

<a id="r_a7a0f2f10f8778fe201a68932d18434e5"></a>

```c
#define EAI_AGAIN DNS_EAI_AGAIN
```

相关声明：[EAI_AGAIN](#a7a0f2f10f8778fe201a68932d18434e5)、[DNS_EAI_AGAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9)。

<a id="r_acfc712115bf29357d33472da2209dc15"></a>

```c
#define EAI_FAIL DNS_EAI_FAIL
```

相关声明：[EAI_FAIL](#acfc712115bf29357d33472da2209dc15)、[DNS_EAI_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455)。

<a id="r_aae1a32f26ffbb7461251d7c4a7c3a0a2"></a>

```c
#define EAI_NODATA DNS_EAI_NODATA
```

相关声明：[EAI_NODATA](#aae1a32f26ffbb7461251d7c4a7c3a0a2)、[DNS_EAI_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2)。

<a id="r_a33d8eb0c89167f95dcdaf23386631174"></a>

```c
#define EAI_MEMORY DNS_EAI_MEMORY
```

相关声明：[EAI_MEMORY](#a33d8eb0c89167f95dcdaf23386631174)、[DNS_EAI_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673)。

<a id="r_a8e864fa95f26341c27127deb6237c88c"></a>

```c
#define EAI_SYSTEM DNS_EAI_SYSTEM
```

相关声明：[EAI_SYSTEM](#a8e864fa95f26341c27127deb6237c88c)、[DNS_EAI_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eae932d5596c55d090cf2ebe43ad59bd35)。

<a id="r_ac7f08e3ee3c38f7c869beb5a44c9f651"></a>

```c
#define EAI_SERVICE DNS_EAI_SERVICE
```

相关声明：[EAI_SERVICE](#ac7f08e3ee3c38f7c869beb5a44c9f651)、[DNS_EAI_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaeb7d2677167f5bc230da2eea2a81d06c)。

<a id="r_a110777c2c99dab32101324b3b1dd1df5"></a>

```c
#define EAI_SOCKTYPE DNS_EAI_SOCKTYPE
```

相关声明：[EAI_SOCKTYPE](#a110777c2c99dab32101324b3b1dd1df5)、[DNS_EAI_SOCKTYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaba718125a826939380fdbcc9c1fb4512)。

<a id="r_a1d195add54c14a8903441848fb2f7da6"></a>

```c
#define EAI_FAMILY DNS_EAI_FAMILY
```

相关声明：[EAI_FAMILY](#a1d195add54c14a8903441848fb2f7da6)、[DNS_EAI_FAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8440de8b7109dfcca71acca6c7ac4103)。

<a id="r_a01d6798d308152b919a0b9f998bbd336"></a>

```c
#define EAI_OVERFLOW DNS_EAI_OVERFLOW
```

相关声明：[EAI_OVERFLOW](#a01d6798d308152b919a0b9f998bbd336)、[DNS_EAI_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f)。

<a id="r_af6bd8540206fe6379df889064f4a9748"></a>

```c
#define addrinfo zsock_addrinfo
```

相关声明：[addrinfo](#af6bd8540206fe6379df889064f4a9748)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 79.3\_函数（Functions）

<a id="r_accc64bf7bad3dd2a6b683c10533aa076"></a>

```c
void endhostent (void)
```

相关声明：[endhostent](#accc64bf7bad3dd2a6b683c10533aa076)。

<a id="r_a9c23830b9c634ac761f3f2daa3e6b724"></a>

```c
void endnetent (void)
```

相关声明：[endnetent](#a9c23830b9c634ac761f3f2daa3e6b724)。

<a id="r_a3ac0597abceec2060997db1355d462f8"></a>

```c
void endprotoent (void)
```

相关声明：[endprotoent](#a3ac0597abceec2060997db1355d462f8)。

<a id="r_adf81140af263bf72a02dc4a484e98d6a"></a>

```c
void endservent (void)
```

相关声明：[endservent](#adf81140af263bf72a02dc4a484e98d6a)。

<a id="r_ae854ec9955d62f1791342f9c2b8abcee"></a>

```c
void freeaddrinfo (struct zsock_addrinfo *ai)
```

相关声明：[freeaddrinfo](#ae854ec9955d62f1791342f9c2b8abcee)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

<a id="r_a8033b3171adc399803161694ea422c4f"></a>

```c
const char * gai_strerror (int errcode)
```

相关声明：[gai_strerror](#a8033b3171adc399803161694ea422c4f)。

<a id="r_adc9ea491d9008de7cd9e0a5b9147ca70"></a>

```c
int getaddrinfo (const char *host, const char *service, const struct zsock_addrinfo *hints, struct zsock_addrinfo **res)
```

相关声明：[getaddrinfo](#adc9ea491d9008de7cd9e0a5b9147ca70)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

<a id="r_a4b9065f385acd38096aa190110429420"></a>

```c
struct hostent * gethostent (void)
```

相关声明：[hostent](../posix_system_model_reference/P004_hostent_结构体.md)、[gethostent](#a4b9065f385acd38096aa190110429420)。

<a id="r_a5c82f7d491ae353012f42bf60e9c9f20"></a>

```c
int getnameinfo (const struct sockaddr *addr, socklen_t addrlen, char *host, socklen_t hostlen, char *serv, socklen_t servlen, int flags)
```

相关声明：[getnameinfo](#a5c82f7d491ae353012f42bf60e9c9f20)、[socklen_t](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a3f5f480bed01f54df564b99350f1d1bb)、[socklen_t](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a3f5f480bed01f54df564b99350f1d1bb)、[socklen_t](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a3f5f480bed01f54df564b99350f1d1bb)、[flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_a0f38280702a5ae01bd02e2e574bfce35"></a>

```c
struct netent * getnetbyaddr (uint32_t net, int type)
```

相关声明：[netent](../posix_system_model_reference/P008_netent_结构体.md)、[getnetbyaddr](#a0f38280702a5ae01bd02e2e574bfce35)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a34ad0dc5368b67dbdb492cf09badc2f4"></a>

```c
struct netent * getnetbyname (const char *name)
```

相关声明：[netent](../posix_system_model_reference/P008_netent_结构体.md)、[getnetbyname](#a34ad0dc5368b67dbdb492cf09badc2f4)。

<a id="r_a199e7f8bde21efa3d6d44efd870a72a9"></a>

```c
struct netent * getnetent (void)
```

相关声明：[netent](../posix_system_model_reference/P008_netent_结构体.md)、[getnetent](#a199e7f8bde21efa3d6d44efd870a72a9)。

<a id="r_a3173746d8bc19a57e57d76f5f8abe5fd"></a>

```c
struct protoent * getprotobyname (const char *name)
```

相关声明：[protoent](../posix_system_model_reference/P010_protoent_结构体.md)、[getprotobyname](#a3173746d8bc19a57e57d76f5f8abe5fd)。

<a id="r_ac4f01c33d33a644fdda8b19bf18a325a"></a>

```c
struct protoent * getprotobynumber (int proto)
```

相关声明：[protoent](../posix_system_model_reference/P010_protoent_结构体.md)、[getprotobynumber](#ac4f01c33d33a644fdda8b19bf18a325a)。

<a id="r_a816ddf34b4aa42f0b9c70c81ce832fb2"></a>

```c
struct protoent * getprotoent (void)
```

相关声明：[protoent](../posix_system_model_reference/P010_protoent_结构体.md)、[getprotoent](#a816ddf34b4aa42f0b9c70c81ce832fb2)。

<a id="r_a9d976afa60cead1e7f82bad149626b7f"></a>

```c
struct servent * getservbyname (const char *name, const char *proto)
```

相关声明：[servent](../posix_system_model_reference/P016_servent_结构体.md)、[getservbyname](#a9d976afa60cead1e7f82bad149626b7f)。

<a id="r_a070fa0f353af9fc05138caeb6348c29a"></a>

```c
struct servent * getservbyport (int port, const char *proto)
```

相关声明：[servent](../posix_system_model_reference/P016_servent_结构体.md)、[getservbyport](#a070fa0f353af9fc05138caeb6348c29a)。

<a id="r_aa04c5e5229bf6ad9dc77bb261577df10"></a>

```c
struct servent * getservent (void)
```

相关声明：[servent](../posix_system_model_reference/P016_servent_结构体.md)、[getservent](#aa04c5e5229bf6ad9dc77bb261577df10)。

<a id="r_ad3c7650e6d2bc3c27f9f089af05ee481"></a>

```c
void sethostent (int stayopen)
```

相关声明：[sethostent](#ad3c7650e6d2bc3c27f9f089af05ee481)。

<a id="r_a0a2c07c88b888c1c181e8f277f53aee9"></a>

```c
void setnetent (int stayopen)
```

相关声明：[setnetent](#a0a2c07c88b888c1c181e8f277f53aee9)。

<a id="r_a6a806414e4ae5bffb09e3a1d25d8db75"></a>

```c
void setprotoent (int stayopen)
```

相关声明：[setprotoent](#a6a806414e4ae5bffb09e3a1d25d8db75)。

<a id="r_ab2238818a534ce99ec4b5f4a22b659da"></a>

```c
void setservent (int stayopen)
```

相关声明：[setservent](#ab2238818a534ce99ec4b5f4a22b659da)。

## 79.4\_详细说明（Detailed Documentation）

<a id="af6bd8540206fe6379df889064f4a9748"></a>

### `addrinfo`

```c
#define addrinfo zsock_addrinfo
```

<a id="a7a0f2f10f8778fe201a68932d18434e5"></a>

### `EAI_AGAIN`

```c
#define EAI_AGAIN DNS_EAI_AGAIN
```

<a id="a3f3b38f2ac6688612a0fd20f3e6210be"></a>

### `EAI_BADFLAGS`

```c
#define EAI_BADFLAGS DNS_EAI_BADFLAGS
```

<a id="acfc712115bf29357d33472da2209dc15"></a>

### `EAI_FAIL`

```c
#define EAI_FAIL DNS_EAI_FAIL
```

<a id="a1d195add54c14a8903441848fb2f7da6"></a>

### `EAI_FAMILY`

```c
#define EAI_FAMILY DNS_EAI_FAMILY
```

<a id="a33d8eb0c89167f95dcdaf23386631174"></a>

### `EAI_MEMORY`

```c
#define EAI_MEMORY DNS_EAI_MEMORY
```

<a id="aae1a32f26ffbb7461251d7c4a7c3a0a2"></a>

### `EAI_NODATA`

```c
#define EAI_NODATA DNS_EAI_NODATA
```

<a id="a0bb00f48d6ba1e8c55b7d85c8e3a19a7"></a>

### `EAI_NONAME`

```c
#define EAI_NONAME DNS_EAI_NONAME
```

<a id="a01d6798d308152b919a0b9f998bbd336"></a>

### `EAI_OVERFLOW`

```c
#define EAI_OVERFLOW DNS_EAI_OVERFLOW
```

<a id="ac7f08e3ee3c38f7c869beb5a44c9f651"></a>

### `EAI_SERVICE`

```c
#define EAI_SERVICE DNS_EAI_SERVICE
```

<a id="a110777c2c99dab32101324b3b1dd1df5"></a>

### `EAI_SOCKTYPE`

```c
#define EAI_SOCKTYPE DNS_EAI_SOCKTYPE
```

<a id="a8e864fa95f26341c27127deb6237c88c"></a>

### `EAI_SYSTEM`

```c
#define EAI_SYSTEM DNS_EAI_SYSTEM
```

<a id="aefdeadf85356cc2fa0870d86a6055eb1"></a>

### `NI_MAXSERV`

```c
#define NI_MAXSERV 32
```

为使用 `getnameinfo` 的应用程序提供合理的大小（Size）。

<a id="accc64bf7bad3dd2a6b683c10533aa076"></a>

### `endhostent()`

```c
void endhostent ( void )
```

<a id="a9c23830b9c634ac761f3f2daa3e6b724"></a>

### `endnetent()`

```c
void endnetent ( void )
```

<a id="a3ac0597abceec2060997db1355d462f8"></a>

### `endprotoent()`

```c
void endprotoent ( void )
```

<a id="adf81140af263bf72a02dc4a484e98d6a"></a>

### `endservent()`

```c
void endservent ( void )
```

<a id="ae854ec9955d62f1791342f9c2b8abcee"></a>

### `freeaddrinfo()`

```c
void freeaddrinfo ( struct zsock_addrinfo * ai)
```

<a id="a8033b3171adc399803161694ea422c4f"></a>

### `gai_strerror()`

```c
const char * gai_strerror ( int errcode)
```

<a id="adc9ea491d9008de7cd9e0a5b9147ca70"></a>

### `getaddrinfo()`

```c
int getaddrinfo ( const char * host, const char * service, const struct zsock_addrinfo * hints, struct zsock_addrinfo ** res )
```

<a id="a4b9065f385acd38096aa190110429420"></a>

### `gethostent()`

```c
struct hostent * gethostent ( void )
```

<a id="a5c82f7d491ae353012f42bf60e9c9f20"></a>

### `getnameinfo()`

```c
int getnameinfo ( const struct sockaddr * addr, socklen_t addrlen, char * host, socklen_t hostlen, char * serv, socklen_t servlen, int flags )
```

<a id="a0f38280702a5ae01bd02e2e574bfce35"></a>

### `getnetbyaddr()`

```c
struct netent * getnetbyaddr ( uint32_t net, int type )
```

<a id="a34ad0dc5368b67dbdb492cf09badc2f4"></a>

### `getnetbyname()`

```c
struct netent * getnetbyname ( const char * name)
```

<a id="a199e7f8bde21efa3d6d44efd870a72a9"></a>

### `getnetent()`

```c
struct netent * getnetent ( void )
```

<a id="a3173746d8bc19a57e57d76f5f8abe5fd"></a>

### `getprotobyname()`

```c
struct protoent * getprotobyname ( const char * name)
```

<a id="ac4f01c33d33a644fdda8b19bf18a325a"></a>

### `getprotobynumber()`

```c
struct protoent * getprotobynumber ( int proto)
```

<a id="a816ddf34b4aa42f0b9c70c81ce832fb2"></a>

### `getprotoent()`

```c
struct protoent * getprotoent ( void )
```

<a id="a9d976afa60cead1e7f82bad149626b7f"></a>

### `getservbyname()`

```c
struct servent * getservbyname ( const char * name, const char * proto )
```

<a id="a070fa0f353af9fc05138caeb6348c29a"></a>

### `getservbyport()`

```c
struct servent * getservbyport ( int port, const char * proto )
```

<a id="aa04c5e5229bf6ad9dc77bb261577df10"></a>

### `getservent()`

```c
struct servent * getservent ( void )
```

<a id="ad3c7650e6d2bc3c27f9f089af05ee481"></a>

### `sethostent()`

```c
void sethostent ( int stayopen)
```

<a id="a0a2c07c88b888c1c181e8f277f53aee9"></a>

### `setnetent()`

```c
void setnetent ( int stayopen)
```

<a id="a6a806414e4ae5bffb09e3a1d25d8db75"></a>

### `setprotoent()`

```c
void setprotoent ( int stayopen)
```

<a id="ab2238818a534ce99ec4b5f4a22b659da"></a>

### `setservent()`

```c
void setservent ( int stayopen)
```


## 79.5\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P578_netdb.h_源码浏览.md)
- [hostent](../posix_system_model_reference/P004_hostent_结构体.md)
- [netent](../posix_system_model_reference/P008_netent_结构体.md)
- [protoent](../posix_system_model_reference/P010_protoent_结构体.md)
- [servent](../posix_system_model_reference/P016_servent_结构体.md)
- [DNS_EAI_BADFLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea9989bb26c930dcf90b5aaab224f19793)
- [DNS_EAI_NONAME](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f)
- [DNS_EAI_AGAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9)
- [DNS_EAI_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455)
- [DNS_EAI_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2)
- [DNS_EAI_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673)
- [DNS_EAI_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eae932d5596c55d090cf2ebe43ad59bd35)
- [DNS_EAI_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaeb7d2677167f5bc230da2eea2a81d06c)
- [DNS_EAI_SOCKTYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58eaba718125a826939380fdbcc9c1fb4512)
- [DNS_EAI_FAMILY](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8440de8b7109dfcca71acca6c7ac4103)
- [DNS_EAI_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f)
- [zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)
- [socklen_t](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a3f5f480bed01f54df564b99350f1d1bb)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P078_zephyr__net__net_log.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P080_zephyr__bluetooth__mesh__od_priv_proxy_srv.h_文件参考.md)
