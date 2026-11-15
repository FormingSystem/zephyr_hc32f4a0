---
id: learning.zephyr-docs.api-file-reference.page-158
title: zephyr__posix__netinet__in.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/in_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第158章\_zephyr\_\_posix\_\_netinet\_\_in.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/in_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/net/socket.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 158.1\_宏定义（Macros）

<a id="r_a73e57c1190f8731fb8b0217f929c4e1b"></a>

```c
#define in_addr net_in_addr
```

相关声明：[in_addr](#a73e57c1190f8731fb8b0217f929c4e1b)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

<a id="r_a75e4bdec5e6afb661e8cbae72452fde7"></a>

```c
#define in6_addr net_in6_addr
```

相关声明：[in6_addr](#a75e4bdec5e6afb661e8cbae72452fde7)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

<a id="r_a93b37007689284fd9c4bde1a8f4b9199"></a>

```c
#define INET_ADDRSTRLEN NET_INET_ADDRSTRLEN
```

相关声明：[INET_ADDRSTRLEN](#a93b37007689284fd9c4bde1a8f4b9199)、[NET_INET_ADDRSTRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae864ce227183974771322ba07f8c493d)。

<a id="r_af776b22a727aae7c9f4d869d50df47e8"></a>

```c
#define INET6_ADDRSTRLEN NET_INET6_ADDRSTRLEN
```

相关声明：[INET6_ADDRSTRLEN](#af776b22a727aae7c9f4d869d50df47e8)、[NET_INET6_ADDRSTRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga29969b236fa78c479836cbd143b099f3)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 158.2\_类型定义（Typedefs）

<a id="r_a979d51fa99f7145221b3ed1afff5b827"></a>

```c
typedef uint16_t in_port_t
```

相关声明：[uint16_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[in_port_t](#a979d51fa99f7145221b3ed1afff5b827)。

## 158.3\_详细说明（Detailed Documentation）

<a id="a75e4bdec5e6afb661e8cbae72452fde7"></a>

### `in6_addr`

```c
#define in6_addr net_in6_addr
```

<a id="a73e57c1190f8731fb8b0217f929c4e1b"></a>

### `in_addr`

```c
#define in_addr net_in_addr
```

<a id="af776b22a727aae7c9f4d869d50df47e8"></a>

### `INET6_ADDRSTRLEN`

```c
#define INET6_ADDRSTRLEN NET_INET6_ADDRSTRLEN
```

<a id="a93b37007689284fd9c4bde1a8f4b9199"></a>

### `INET_ADDRSTRLEN`

```c
#define INET_ADDRSTRLEN NET_INET_ADDRSTRLEN
```

<a id="a979d51fa99f7145221b3ed1afff5b827"></a>

### `in_port_t`

```c
typedef uint16_t in_port_t
```


## 158.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P358_in.h_源码浏览.md)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [NET_INET_ADDRSTRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae864ce227183974771322ba07f8c493d)
- [NET_INET6_ADDRSTRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga29969b236fa78c479836cbd143b099f3)
- [uint16_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P157_zephyr__dt-bindings__power__imx_spc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P159_zephyr__posix__sys__time.h_文件参考.md)
