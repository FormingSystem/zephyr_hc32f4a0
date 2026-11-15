---
id: learning.zephyr-docs.api-file-reference.page-161
title: zephyr__posix__arpa__inet.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第161章\_zephyr\_\_posix\_\_arpa\_\_inet.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <zephyr/posix/netinet/in.h>
#include <zephyr/posix/sys/socket.h>
#include <zephyr/net/socket.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 161.1\_宏定义（Macros）

<a id="r_ada37feda716b4ba89cf9dba34288141d"></a>

```c
#define ntohs(x)
```

相关声明：[ntohs](#ada37feda716b4ba89cf9dba34288141d)。

<a id="r_ac317b3e903719ba02894f1710f7f2439"></a>

```c
#define ntohl(x)
```

相关声明：[ntohl](#ac317b3e903719ba02894f1710f7f2439)。

<a id="r_a3cfcf123d4ead264289232f91f2c9ca5"></a>

```c
#define ntohll(x)
```

相关声明：[ntohll](#a3cfcf123d4ead264289232f91f2c9ca5)。

<a id="r_a51799f5ebb4c7228ef7e95c247030f42"></a>

```c
#define htons(x)
```

相关声明：[htons](#a51799f5ebb4c7228ef7e95c247030f42)。

<a id="r_ae4027a6ad07f13aa12eab285a1b46019"></a>

```c
#define htonl(x)
```

相关声明：[htonl](#ae4027a6ad07f13aa12eab285a1b46019)。

<a id="r_a9f4bf0773c45ad9a9753a1b784a13fbb"></a>

```c
#define htonll(x)
```

相关声明：[htonll](#a9f4bf0773c45ad9a9753a1b784a13fbb)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 161.2\_类型定义（Typedefs）

<a id="r_a98b38134a62f24554da0ffcabde8062c"></a>

```c
typedef uint32_t in_addr_t
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[in_addr_t](#a98b38134a62f24554da0ffcabde8062c)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 161.3\_函数（Functions）

<a id="r_a3e3b8f43e05dc3b87977b6a7a2ed09ca"></a>

```c
in_addr_t inet_addr (const char *cp)
```

相关声明：[in_addr_t](#a98b38134a62f24554da0ffcabde8062c)、[inet_addr](#a3e3b8f43e05dc3b87977b6a7a2ed09ca)。

<a id="r_aeac5d8b00354beb2127ba1468e021ef4"></a>

```c
char * inet_ntoa (struct net_in_addr in)
```

相关声明：[inet_ntoa](#aeac5d8b00354beb2127ba1468e021ef4)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

<a id="r_ae93e32740fb355baef0cab02133e7ff4"></a>

```c
char * inet_ntop (sa_family_t family, const void *src, char *dst, size_t size)
```

相关声明：[inet_ntop](#ae93e32740fb355baef0cab02133e7ff4)。

<a id="r_aabfaede889b4bc47241ab0c49a7a3cab"></a>

```c
int inet_pton (sa_family_t family, const char *src, void *dst)
```

相关声明：[inet_pton](#aabfaede889b4bc47241ab0c49a7a3cab)。

## 161.4\_详细说明（Detailed Documentation）

<a id="ae4027a6ad07f13aa12eab285a1b46019"></a>

### `htonl`

```c
#define htonl ( x)
```

展开值（Value）：

```c
net_htonl(x)
```

<a id="a9f4bf0773c45ad9a9753a1b784a13fbb"></a>

### `htonll`

```c
#define htonll ( x)
```

展开值（Value）：

```c
net_htonll(x)
```

<a id="a51799f5ebb4c7228ef7e95c247030f42"></a>

### `htons`

```c
#define htons ( x)
```

展开值（Value）：

```c
net_htons(x)
```

<a id="ac317b3e903719ba02894f1710f7f2439"></a>

### `ntohl`

```c
#define ntohl ( x)
```

展开值（Value）：

```c
net_ntohl(x)
```

<a id="a3cfcf123d4ead264289232f91f2c9ca5"></a>

### `ntohll`

```c
#define ntohll ( x)
```

展开值（Value）：

```c
net_ntohll(x)
```

<a id="ada37feda716b4ba89cf9dba34288141d"></a>

### `ntohs`

```c
#define ntohs ( x)
```

展开值（Value）：

```c
net_ntohs(x)
```

<a id="a98b38134a62f24554da0ffcabde8062c"></a>

### `in_addr_t`

```c
typedef uint32_t in_addr_t
```

<a id="a3e3b8f43e05dc3b87977b6a7a2ed09ca"></a>

### `inet_addr()`

```c
in_addr_t inet_addr ( const char * cp)
```

<a id="aeac5d8b00354beb2127ba1468e021ef4"></a>

### `inet_ntoa()`

```c
char * inet_ntoa ( struct net_in_addr in)
```

<a id="ae93e32740fb355baef0cab02133e7ff4"></a>

### `inet_ntop()`

```c
char * inet_ntop ( sa_family_t family, const void * src, char * dst, size_t size )
```

<a id="aabfaede889b4bc47241ab0c49a7a3cab"></a>

### `inet_pton()`

```c
int inet_pton ( sa_family_t family, const char * src, void * dst )
```


## 161.5\_原页交叉引用（Cross References）

- [zephyr/posix/netinet/in.h](../api_source_reference/P358_in.h_源码浏览.md)
- [zephyr/posix/sys/socket.h](../api_source_reference/P667_socket.h_源码浏览.md)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P366_inet.h_源码浏览.md)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_htonl](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga5d9e16e8f439be6f94fb3f72de13bdac)
- [net_htonll](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga7f215d5ef1d4098a7e8681500796a8f5)
- [net_htons](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae20291eed240d648d0ef7e13822f925f)
- [net_ntohl](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae18466011462c20add53de2e01505b92)
- [net_ntohll](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga35f36b83b652246e9a61c9ddfdfed4f5)
- [net_ntohs](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga4837ff0eece26b00ae46ed7c16997a97)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__ip__4__6_html_ga5d9e16e8f439be6f94fb3f72de13bdac"></a>
<a id="agroup__ip__4__6_html_ga7f215d5ef1d4098a7e8681500796a8f5"></a>
<a id="agroup__ip__4__6_html_gae20291eed240d648d0ef7e13822f925f"></a>
<a id="agroup__ip__4__6_html_gae18466011462c20add53de2e01505b92"></a>
<a id="agroup__ip__4__6_html_ga35f36b83b652246e9a61c9ddfdfed4f5"></a>
<a id="agroup__ip__4__6_html_ga4837ff0eece26b00ae46ed7c16997a97"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P160_zephyr__types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P162_zephyr__dt-bindings__dma__infineon-xmc4xxx-dma.h_文件参考.md)
