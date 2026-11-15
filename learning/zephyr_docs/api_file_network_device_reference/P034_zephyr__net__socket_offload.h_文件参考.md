---
id: learning.zephyr-docs.api-file-network-device-reference.page-34
title: zephyr__net__socket_offload.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_net\_\_socket\_offload.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

套接字卸载重定向（Socket Offload Redirect）的API。

<a id="details"></a>

```c
#include <zephyr/net/net_ip.h>
#include <zephyr/net/socket.h>
```

查看此文件的源码。

套接字卸载重定向（Socket Offload Redirect）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 34.1\_数据结构（Data Structures）

<a id="r_socket_5Fdns_5Foffload"></a>

```c
struct socket_dns_offload
```

相关声明：[socket_dns_offload](../network_service_model_reference/P055_socket_dns_offload_结构体.md)。

卸载式套接字DNS（Offloaded Socket DNS）的API接口。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 34.2\_宏定义（Macros）

<a id="r_af341a4e569196545165962e17544d2c9"></a>

```c
#define socket_offload_dns_is_enabled()
```

相关声明：[socket_offload_dns_is_enabled](#af341a4e569196545165962e17544d2c9)。

检查域名系统卸载（DNS Offloading）是否启用。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 34.3\_函数（Functions）

<a id="r_a1b56446dd816af7101088bb0a474d0f4"></a>

```c
void socket_offload_dns_register (const struct socket_dns_offload *ops)
```

相关声明：[socket_offload_dns_register](#a1b56446dd816af7101088bb0a474d0f4)、[socket_dns_offload](../network_service_model_reference/P055_socket_dns_offload_结构体.md)。

注册卸载套接字（Offloaded Socket）的 DNS API 接口。

<a id="r_a87f67b6c07b7271778e919ccc88b6d7b"></a>

```c
int socket_offload_dns_deregister (const struct socket_dns_offload *ops)
```

相关声明：[socket_offload_dns_deregister](#a87f67b6c07b7271778e919ccc88b6d7b)、[socket_dns_offload](../network_service_model_reference/P055_socket_dns_offload_结构体.md)。

注销卸载套接字（Offloaded Socket）的 DNS API 接口。

<a id="r_a0d0123d234cd292282a272cb2e2eeb3c"></a>

```c
void socket_offload_dns_enable (bool enable)
```

相关声明：[socket_offload_dns_enable](#a0d0123d234cd292282a272cb2e2eeb3c)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在运行时启用／禁用 DNS 卸载（DNS Offloading）。

## 34.4\_详细说明（Detailed Documentation）

<a id="af341a4e569196545165962e17544d2c9"></a>

### `socket_offload_dns_is_enabled`

```c
#define socket_offload_dns_is_enabled ( )
```

展开值（Value）：

```c
false
```

检查域名系统卸载（DNS Offloading）是否启用。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | DNS 卸载 API（Offloaded API）已注册且已启用。 |
| `false` | DNS 卸载（DNS Offloading）已禁用。 |

<a id="a87f67b6c07b7271778e919ccc88b6d7b"></a>

### `socket_offload_dns_deregister()`

```c
int socket_offload_dns_deregister ( const struct socket_dns_offload * ops)
```

注销卸载套接字（Offloaded Socket）的 DNS API 接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ops` | 指向卸载套接字 DNS API 接口的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | DNS 卸载 API（Offloaded API）尚未注册。 |

<a id="a0d0123d234cd292282a272cb2e2eeb3c"></a>

### `socket_offload_dns_enable()`

```c
void socket_offload_dns_enable ( bool enable)
```

在运行时启用／禁用 DNS 卸载（DNS Offloading）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enable` | 是否启用或禁用 DNS 卸载（DNS Offloading）。 |

<a id="a1b56446dd816af7101088bb0a474d0f4"></a>

### `socket_offload_dns_register()`

```c
void socket_offload_dns_register ( const struct socket_dns_offload * ops)
```

注册卸载套接字（Offloaded Socket）的 DNS API 接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ops` | 指向卸载套接字 DNS API 接口的指针。 |


## 34.5\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/socket.h](../api_source_socket_ethernet_reference/P006_socket.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P183_socket_offload.h_源码浏览.md)
- [socket_dns_offload](../network_service_model_reference/P055_socket_dns_offload_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P033_zephyr__net__sntp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__net__socket_service.h_文件参考.md)
