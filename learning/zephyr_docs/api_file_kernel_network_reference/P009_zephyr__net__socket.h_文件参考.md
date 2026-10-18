---
id: learning.zephyr-docs.api-file-kernel-network-reference.page-9
title: zephyr__net__socket.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_net\_\_socket.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BSD套接字（BSD Sockets）兼容API的定义。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/socket_select.h>
#include <zephyr/net/socket_poll.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/fdtable.h>
#include <zephyr/net/dns_resolve.h>
#include <stdlib.h>
#include <zephyr/syscalls/socket.h>
```

查看此文件的源码。

兼容 BSD 套接字（BSD Sockets）的 API 定义。供应用程序使用的类 BSD 套接字 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_zsock_5Ftls_5Fcert_5Fverify_5Fcb"></a>

```c
struct zsock_tls_cert_verify_cb
```

相关声明：[zsock_tls_cert_verify_cb](../posix_system_model_reference/P031_zsock_tls_cert_verify_cb_结构体.md)。

ZSOCK_TLS_CERT_VERIFY_CALLBACK套接字选项的数据结构。

<a id="r_zsock_5Faddrinfo"></a>

```c
struct zsock_addrinfo
```

相关声明：[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

查询地址信息（Address Information）时使用的定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="define-members-0"></a>

### poll() 的选项（Options for poll()）

<a id="r_ga6ade0deb4952e1ea23b368d9eceee9ed"></a>

```c
#define ZSOCK_POLLIN 1
```

相关声明：[ZSOCK_POLLIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6ade0deb4952e1ea23b368d9eceee9ed)。

`zsock_poll`：轮询可读（Readability）状态。

<a id="r_ga1c96c16d5000db0fa4b69055ebb97839"></a>

```c
#define ZSOCK_POLLPRI 2
```

相关声明：[ZSOCK_POLLPRI](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1c96c16d5000db0fa4b69055ebb97839)。

`zsock_poll`：轮询异常状况（Exceptional Condition）。

<a id="r_ga9ca302c64dfb676798ce03100894ca3e"></a>

```c
#define ZSOCK_POLLOUT 4
```

相关声明：[ZSOCK_POLLOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga9ca302c64dfb676798ce03100894ca3e)。

`zsock_poll`：轮询可写（Writability）状态。

<a id="r_gad44368a112fbf91436a2439e7b767641"></a>

```c
#define ZSOCK_POLLERR 8
```

相关声明：[ZSOCK_POLLERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad44368a112fbf91436a2439e7b767641)。

`zsock_poll`：轮询结果包含错误状况（Error Condition），仅用作输出值。

<a id="r_gadd341cd5c1f6d7deeaedc5c58dc56fe7"></a>

```c
#define ZSOCK_POLLHUP 0x10
```

相关声明：[ZSOCK_POLLHUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gadd341cd5c1f6d7deeaedc5c58dc56fe7)。

`zsock_poll`：轮询检测到连接已关闭（Closed Connection），仅用作输出值。

<a id="r_ga45c5b0efca6e09e4f7db78d1d007bf67"></a>

```c
#define ZSOCK_POLLNVAL 0x20
```

相关声明：[ZSOCK_POLLNVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga45c5b0efca6e09e4f7db78d1d007bf67)。

`zsock_poll`：无效套接字（Invalid Socket），仅用作输出值。

<a id="define-members-1"></a>

### 发送和接收数据的选项（Options for sending and receiving data）

<a id="r_gae7da123a40584192b65af77e918080b9"></a>

```c
#define ZSOCK_MSG_PEEK 0x02
```

相关声明：[ZSOCK_MSG_PEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae7da123a40584192b65af77e918080b9)。

`zsock_recv`：读取数据，但不将其从套接字输入队列（Socket Input Queue）移除。

<a id="r_gabdc593f541a4f9a607cfe140cee19c4a"></a>

```c
#define ZSOCK_MSG_CTRUNC 0x08
```

相关声明：[ZSOCK_MSG_CTRUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gabdc593f541a4f9a607cfe140cee19c4a)。

`zsock_recvmsg`：控制数据缓冲区（Control Data Buffer）过小。

<a id="r_gae594c5e74cd473df8e3328a4cd935ce1"></a>

```c
#define ZSOCK_MSG_TRUNC 0x20
```

相关声明：[ZSOCK_MSG_TRUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae594c5e74cd473df8e3328a4cd935ce1)。

`zsock_recv`：返回数据报（Datagram）的实际长度，即使它超过传入的缓冲区长度。

<a id="r_ga92cf4460e23f376bf130d885ea64ed6b"></a>

```c
#define ZSOCK_MSG_DONTWAIT 0x40
```

相关声明：[ZSOCK_MSG_DONTWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga92cf4460e23f376bf130d885ea64ed6b)。

`zsock_recv`/`zsock_send`：将本次操作覆盖为非阻塞（Non-blocking）操作。

<a id="r_ga00b950f50302d97c27111da49f5289fb"></a>

```c
#define ZSOCK_MSG_WAITALL 0x100
```

相关声明：[ZSOCK_MSG_WAITALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga00b950f50302d97c27111da49f5289fb)。

`zsock_recv`：阻塞（Block），直到能够返回要求的全部数据量。

<a id="define-members-2"></a>

### shutdown() 函数的选项（Options for shutdown() function）

<a id="r_ga2a58cbc62db1e559898ea979454d74d4"></a>

```c
#define ZSOCK_SHUT_RD 0
```

相关声明：[ZSOCK_SHUT_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2a58cbc62db1e559898ea979454d74d4)。

`zsock_shutdown`：关闭读取方向（Reading）。

<a id="r_ga87630f1abe81c4e33a24cb1f1ebb3571"></a>

```c
#define ZSOCK_SHUT_WR 1
```

相关声明：[ZSOCK_SHUT_WR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga87630f1abe81c4e33a24cb1f1ebb3571)。

`zsock_shutdown`：关闭写入方向（Writing）。

<a id="r_ga788dcff81663a9fb01e32b53bca13e2d"></a>

```c
#define ZSOCK_SHUT_RDWR 2
```

相关声明：[ZSOCK_SHUT_RDWR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga788dcff81663a9fb01e32b53bca13e2d)。

`zsock_shutdown`：同时关闭读取和写入方向（Reading and Writing）。

<a id="define-members-3"></a>

### TLS 套接字选项（Socket options）

<a id="r_ga7209d2f574caf7bf18dfc135b1e89c33"></a>

```c
#define ZSOCK_SOL_TLS 282
```

相关声明：[ZSOCK_SOL_TLS](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga7209d2f574caf7bf18dfc135b1e89c33)。

传输层安全（TLS）的协议层级（Protocol Level）。

<a id="r_ga7e47484ee379d42f1d90d652796f0406"></a>

```c
#define ZSOCK_TLS_SEC_TAG_LIST 1
```

相关声明：[ZSOCK_TLS_SEC_TAG_LIST](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga7e47484ee379d42f1d90d652796f0406)。

用于选择 TLS 凭据（TLS Credentials）的套接字选项（Socket Option）。

<a id="r_ga46e839d445926ba59de5da0edf0f2507"></a>

```c
#define ZSOCK_TLS_HOSTNAME 2
```

相关声明：[ZSOCK_TLS_HOSTNAME](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga46e839d445926ba59de5da0edf0f2507)。

用于设置主机名（Hostname）的只写套接字选项（Write-only Socket Option）。

<a id="r_ga93b27c4d4ed48976d1b8d8307e753d3f"></a>

```c
#define ZSOCK_TLS_CIPHERSUITE_LIST 3
```

相关声明：[ZSOCK_TLS_CIPHERSUITE_LIST](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga93b27c4d4ed48976d1b8d8307e753d3f)。

用于选择密码套件（Ciphersuites）的套接字选项（Socket Option）。

<a id="r_gae186f97c3783a29ad4c3df7dd566da95"></a>

```c
#define ZSOCK_TLS_CIPHERSUITE_USED 4
```

相关声明：[ZSOCK_TLS_CIPHERSUITE_USED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gae186f97c3783a29ad4c3df7dd566da95)。

用于读取 TLS 握手（Handshake）期间选定密码套件（Ciphersuite）的只读套接字选项。

<a id="r_gac02711515e3bdfabe41061cfc65f5c67"></a>

```c
#define ZSOCK_TLS_PEER_VERIFY 5
```

相关声明：[ZSOCK_TLS_PEER_VERIFY](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gac02711515e3bdfabe41061cfc65f5c67)。

用于设置 TLS 连接对端验证等级（Peer Verification Level）的只写套接字选项。

<a id="r_ga7f7a51d68a1901948696d597f0548488"></a>

```c
#define ZSOCK_TLS_DTLS_ROLE 6
```

相关声明：[ZSOCK_TLS_DTLS_ROLE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga7f7a51d68a1901948696d597f0548488)。

用于设置数据报传输层安全（DTLS）连接角色（Role）的只写套接字选项。

<a id="r_ga21e38f62fbd83c39a71aec844445a101"></a>

```c
#define ZSOCK_TLS_ALPN_LIST 7
```

相关声明：[ZSOCK_TLS_ALPN_LIST](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga21e38f62fbd83c39a71aec844445a101)。

用于设置所支持应用层协议（Application Layer Protocols）的套接字选项。

<a id="r_gaa480277784420697eeebbbd71043404a"></a>

```c
#define ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MIN 8
```

相关声明：[ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MIN](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaa480277784420697eeebbbd71043404a)。

用于设置 DTLS 最小握手超时时间（Min Handshake Timeout）的套接字选项。

<a id="r_gaea9de0d195605882ab6e94cf2ea13907"></a>

```c
#define ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MAX 9
```

相关声明：[ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MAX](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaea9de0d195605882ab6e94cf2ea13907)。

用于设置 DTLS 最大握手超时时间（Max Handshake Timeout）的套接字选项。

<a id="r_gac976e4d41ca9ef41debb4c997b28b43a"></a>

```c
#define ZSOCK_TLS_CERT_NOCOPY 10
```

相关声明：[ZSOCK_TLS_CERT_NOCOPY](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gac976e4d41ca9ef41debb4c997b28b43a)。

在可能的情况下阻止将证书（Certificates）复制到 Mbed TLS 堆中的套接字选项。

<a id="r_gab446ab6448359979f2d5e895729be993"></a>

```c
#define ZSOCK_TLS_NATIVE 11
```

相关声明：[ZSOCK_TLS_NATIVE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gab446ab6448359979f2d5e895729be993)。

与卸载（Offloading）配合使用的 TLS 套接字选项。

<a id="r_gacc4c3078ac3169958739ae3425f90a94"></a>

```c
#define ZSOCK_TLS_SESSION_CACHE 12
```

相关声明：[ZSOCK_TLS_SESSION_CACHE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gacc4c3078ac3169958739ae3425f90a94)。

控制套接字上 TLS 会话缓存（Session Caching）的套接字选项。

<a id="r_gaf1ad38710d9131206f80d9bd8ea7e66f"></a>

```c
#define ZSOCK_TLS_SESSION_CACHE_PURGE 13
```

相关声明：[ZSOCK_TLS_SESSION_CACHE_PURGE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaf1ad38710d9131206f80d9bd8ea7e66f)。

立即清除会话缓存（Session Cache）的只写套接字选项。

<a id="r_gaf57ee9894cc4bb7f3fa88e08f7842aa1"></a>

```c
#define ZSOCK_TLS_DTLS_CID 14
```

相关声明：[ZSOCK_TLS_DTLS_CID](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaf57ee9894cc4bb7f3fa88e08f7842aa1)。

控制 DTLS 连接 ID（CID）的只写套接字选项。

<a id="r_ga7158a9a83f566702be6611866123a0f3"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS 15
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga7158a9a83f566702be6611866123a0f3)。

获取 DTLS 连接 ID 状态（CID Status）的只读套接字选项。

<a id="r_gac98e03783df8195b76725f8f31fefa1e"></a>

```c
#define ZSOCK_TLS_DTLS_CID_VALUE 16
```

相关声明：[ZSOCK_TLS_DTLS_CID_VALUE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gac98e03783df8195b76725f8f31fefa1e)。

设置或获取 DTLS 会话所使用连接 ID（Connection ID）值的套接字选项。

<a id="r_ga58b97b28c49ee9dca9b8e80f934b4796"></a>

```c
#define ZSOCK_TLS_DTLS_PEER_CID_VALUE 17
```

相关声明：[ZSOCK_TLS_DTLS_PEER_CID_VALUE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga58b97b28c49ee9dca9b8e80f934b4796)。

获取从对端接收的 DTLS 连接 ID（Connection ID）值的只读套接字选项。

<a id="r_gaa6198fcf99c8bc37699655a9f34cbfb3"></a>

```c
#define ZSOCK_TLS_DTLS_HANDSHAKE_ON_CONNECT 18
```

相关声明：[ZSOCK_TLS_DTLS_HANDSHAKE_ON_CONNECT](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaa6198fcf99c8bc37699655a9f34cbfb3)。

配置 DTLS 套接字在 connect() 时行为的套接字选项。

<a id="r_ga1aaed12ee67d524fd97b7f129b89c70e"></a>

```c
#define ZSOCK_TLS_CERT_VERIFY_RESULT 19
```

相关声明：[ZSOCK_TLS_CERT_VERIFY_RESULT](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga1aaed12ee67d524fd97b7f129b89c70e)。

在套接字设置了 TLS_PEER_VERIFY_OPTIONAL 时，获取最近一次握手的证书验证结果（Certificate Verification Result）的只读套接字选项。

<a id="r_ga4425112197a30ca359c57de0e824f0d1"></a>

```c
#define ZSOCK_TLS_CERT_VERIFY_CALLBACK 20
```

相关声明：[ZSOCK_TLS_CERT_VERIFY_CALLBACK](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga4425112197a30ca359c57de0e824f0d1)。

为套接字配置证书验证回调（Certificate Verification Callback）的只写套接字选项。

<a id="r_ga2a4337feada2ae7415dc095e8cd03c7b"></a>

```c
#define ZSOCK_TLS_MAX_FRAGMENT_LENGTH 21
```

相关声明：[ZSOCK_TLS_MAX_FRAGMENT_LENGTH](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga2a4337feada2ae7415dc095e8cd03c7b)。

为 TLS 1.2 配置每个套接字最大分片长度（Max Fragment Length，MFL）的只写套接字选项。

<a id="r_gaa6b53c582059322fb2abc1aaab4ee989"></a>

```c
#define ZSOCK_TLS_MFL_DEFAULT -1
```

相关声明：[ZSOCK_TLS_MFL_DEFAULT](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaa6b53c582059322fb2abc1aaab4ee989)。

使用根据全局 Kconfig 配置推导的最大分片长度（MFL）。

<a id="r_ga4428a55bc1b2c3598fbefd551126f342"></a>

```c
#define ZSOCK_TLS_MFL_DISABLED 0
```

相关声明：[ZSOCK_TLS_MFL_DISABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga4428a55bc1b2c3598fbefd551126f342)。

不发送最大分片长度扩展（MFL Extension）。

<a id="r_ga373ff68ef9c42deff07140c42ea63c0a"></a>

```c
#define ZSOCK_TLS_MFL_512 1
```

相关声明：[ZSOCK_TLS_MFL_512](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga373ff68ef9c42deff07140c42ea63c0a)。

通告最大分片（Max Fragment）为 512 字节。

<a id="r_ga6480b3675b8ec9c39af42208775bc8e9"></a>

```c
#define ZSOCK_TLS_MFL_1024 2
```

相关声明：[ZSOCK_TLS_MFL_1024](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga6480b3675b8ec9c39af42208775bc8e9)。

通告最大分片（Max Fragment）为 1024 字节。

<a id="r_ga25fb9c75cca8c77db2a492ef11f3164a"></a>

```c
#define ZSOCK_TLS_MFL_2048 3
```

相关声明：[ZSOCK_TLS_MFL_2048](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga25fb9c75cca8c77db2a492ef11f3164a)。

通告最大分片（Max Fragment）为 2048 字节。

<a id="r_gaa5df8ff4408d6e3b62c47e0838d481a2"></a>

```c
#define ZSOCK_TLS_MFL_4096 4
```

相关声明：[ZSOCK_TLS_MFL_4096](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaa5df8ff4408d6e3b62c47e0838d481a2)。

通告最大分片（Max Fragment）为 4096 字节。

<a id="r_ga8341e61b00eda2e56deac47e53e96da2"></a>

```c
#define ZSOCK_TLS_PEER_VERIFY_NONE 0
```

相关声明：[ZSOCK_TLS_PEER_VERIFY_NONE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga8341e61b00eda2e56deac47e53e96da2)。

禁用对端验证（Peer Verification Disabled）。

<a id="r_gaef97aaad3f4a97a2954e8aad1fd7857e"></a>

```c
#define ZSOCK_TLS_PEER_VERIFY_OPTIONAL 1
```

相关声明：[ZSOCK_TLS_PEER_VERIFY_OPTIONAL](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaef97aaad3f4a97a2954e8aad1fd7857e)。

对端验证可选（Peer Verification Optional）。

<a id="r_gab9a4437457cdf80141d4567cef754a7a"></a>

```c
#define ZSOCK_TLS_PEER_VERIFY_REQUIRED 2
```

相关声明：[ZSOCK_TLS_PEER_VERIFY_REQUIRED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gab9a4437457cdf80141d4567cef754a7a)。

必须验证对端（Peer Verification Required）。

<a id="r_ga3b96ba39bdcb5b0682e13a6ff421780c"></a>

```c
#define ZSOCK_TLS_DTLS_ROLE_CLIENT 0
```

相关声明：[ZSOCK_TLS_DTLS_ROLE_CLIENT](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga3b96ba39bdcb5b0682e13a6ff421780c)。

DTLS 会话中的客户端角色（Client Role）。

<a id="r_gadeff0aead8c8aa093418fbeb759ad59a"></a>

```c
#define ZSOCK_TLS_DTLS_ROLE_SERVER 1
```

相关声明：[ZSOCK_TLS_DTLS_ROLE_SERVER](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gadeff0aead8c8aa093418fbeb759ad59a)。

DTLS 会话中的服务器角色（Server Role）。

<a id="r_gaf774285e3c5459c25098c5e371299c02"></a>

```c
#define ZSOCK_TLS_CERT_NOCOPY_NONE 0
```

相关声明：[ZSOCK_TLS_CERT_NOCOPY_NONE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaf774285e3c5459c25098c5e371299c02)。

在堆中复制证书（Certificate Duplicated in Heap）。

<a id="r_ga3c08db9b4bb990f127f42cccbe049b58"></a>

```c
#define ZSOCK_TLS_CERT_NOCOPY_OPTIONAL 1
```

相关声明：[ZSOCK_TLS_CERT_NOCOPY_OPTIONAL](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga3c08db9b4bb990f127f42cccbe049b58)。

若证书为 DER 格式，则不在堆中复制。

<a id="r_gaf66290b67a7deee2847c9a7301df177d"></a>

```c
#define ZSOCK_TLS_SESSION_CACHE_DISABLED 0
```

相关声明：[ZSOCK_TLS_SESSION_CACHE_DISABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaf66290b67a7deee2847c9a7301df177d)。

禁用 TLS 会话缓存（Session Caching）。

<a id="r_ga92cc4f8261b5d669cc3032d4b0e0a76a"></a>

```c
#define ZSOCK_TLS_SESSION_CACHE_ENABLED 1
```

相关声明：[ZSOCK_TLS_SESSION_CACHE_ENABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga92cc4f8261b5d669cc3032d4b0e0a76a)。

启用 TLS 会话缓存（Session Caching）。

<a id="r_ga701820487b6651e16319235c43ade526"></a>

```c
#define ZSOCK_TLS_DTLS_CID_DISABLED 0
```

相关声明：[ZSOCK_TLS_DTLS_CID_DISABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga701820487b6651e16319235c43ade526)。

连接 ID（CID）已禁用。

<a id="r_ga5037d23a87ce456873b68c3712d00177"></a>

```c
#define ZSOCK_TLS_DTLS_CID_SUPPORTED 1
```

相关声明：[ZSOCK_TLS_DTLS_CID_SUPPORTED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga5037d23a87ce456873b68c3712d00177)。

支持连接 ID（CID）。

<a id="r_gae53fd78b605b6c65f164f449146d369e"></a>

```c
#define ZSOCK_TLS_DTLS_CID_ENABLED 2
```

相关声明：[ZSOCK_TLS_DTLS_CID_ENABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gae53fd78b605b6c65f164f449146d369e)。

连接 ID（CID）已启用。

<a id="r_gadbe80ee9dcc81383086f99da6f7d6468"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_DISABLED 0
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS_DISABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gadbe80ee9dcc81383086f99da6f7d6468)。

连接 ID（CID）已禁用。

<a id="r_ga307213073d76058f6a276dd7493e2bd2"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_DOWNLINK 1
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS_DOWNLINK](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga307213073d76058f6a276dd7493e2bd2)。

本端正在使用连接 ID（CID）。

<a id="r_ga14275c57f01cb81292049aabe468ec3f"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_UPLINK 2
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS_UPLINK](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga14275c57f01cb81292049aabe468ec3f)。

对端正在使用连接 ID（CID）。

<a id="r_ga46da3503cbb491f471121cd50a342b03"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_BIDIRECTIONAL 3
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS_BIDIRECTIONAL](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga46da3503cbb491f471121cd50a342b03)。

本端与对端均在使用连接 ID（CID）。

<a id="define-members-4"></a>

### getaddrinfo() 提示信息的标志（Flags for getaddrinfo() hints）

<a id="r_ga6a63246ff9f8106f533d4d929185a550"></a>

```c
#define ZSOCK_AI_PASSIVE 0x1
```

相关声明：[ZSOCK_AI_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6a63246ff9f8106f533d4d929185a550)。

用于 `bind()` 的地址，而非用于 `connect()` 的地址。

<a id="r_gab1d9d790b3117fa8a0f997fc45e0f5fd"></a>

```c
#define ZSOCK_AI_CANONNAME 0x2
```

相关声明：[ZSOCK_AI_CANONNAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab1d9d790b3117fa8a0f997fc45e0f5fd)。

填充 `ai_canonname`。

<a id="r_ga22b39ed3a330312a68778c8fa8f0f99e"></a>

```c
#define ZSOCK_AI_NUMERICHOST 0x4
```

相关声明：[ZSOCK_AI_NUMERICHOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga22b39ed3a330312a68778c8fa8f0f99e)。

假定主机地址采用数字表示（Numeric Notation），不进行域名系统（DNS）查询。

<a id="r_ga8913ef12daf85f8f7e364fb8bbc0d546"></a>

```c
#define ZSOCK_AI_V4MAPPED 0x8
```

相关声明：[ZSOCK_AI_V4MAPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8913ef12daf85f8f7e364fb8bbc0d546)。

对于 IPv6，可以返回 IPv4 映射地址（IPv4 Mapped Address）。

<a id="r_gae24cbe0ed18c68e181940954a8116829"></a>

```c
#define ZSOCK_AI_ALL 0x10
```

相关声明：[ZSOCK_AI_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae24cbe0ed18c68e181940954a8116829)。

对于 IPv6，可以同时返回原生 IPv6 地址（Native IPv6 Address）和 IPv4 映射地址（Mapped IPv4 Address）。

<a id="r_ga727bf0f112fbdd9ff1be890177ae42c7"></a>

```c
#define ZSOCK_AI_ADDRCONFIG 0x20
```

相关声明：[ZSOCK_AI_ADDRCONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga727bf0f112fbdd9ff1be890177ae42c7)。

IPv4/IPv6 支持取决于本地系统配置（Local System Configuration）。

<a id="r_ga88b89291f68f34337f8c2416a147e671"></a>

```c
#define ZSOCK_AI_NUMERICSERV 0x400
```

相关声明：[ZSOCK_AI_NUMERICSERV](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga88b89291f68f34337f8c2416a147e671)。

假定服务（Service，即端口）为数字形式。

<a id="r_ga7cd2b1b26066eee23497b1b39ed564c3"></a>

```c
#define ZSOCK_AI_EXTFLAGS 0x800
```

相关声明：[ZSOCK_AI_EXTFLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7cd2b1b26066eee23497b1b39ed564c3)。

存在额外标志（Extra Flags），参见 RFC 5014。

<a id="define-members-5"></a>

### getnameinfo() 的标志（Flags for getnameinfo()）

<a id="r_gaae950d30c261a1b36972fd4e5aa3a3a6"></a>

```c
#define ZSOCK_NI_NUMERICHOST 1
```

相关声明：[ZSOCK_NI_NUMERICHOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaae950d30c261a1b36972fd4e5aa3a3a6)。

`zsock_getnameinfo()`：解析为数字形式的地址（Numeric Address）。

<a id="r_ga91cf6f543827efd4a75d92a9ddacfae6"></a>

```c
#define ZSOCK_NI_NUMERICSERV 2
```

相关声明：[ZSOCK_NI_NUMERICSERV](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga91cf6f543827efd4a75d92a9ddacfae6)。

`zsock_getnameinfo()`：解析为数字形式的端口号（Numeric Port Number）。

<a id="r_ga2f57f503276a43cc049fc66269792239"></a>

```c
#define ZSOCK_NI_NOFQDN 4
```

相关声明：[ZSOCK_NI_NOFQDN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2f57f503276a43cc049fc66269792239)。

`zsock_getnameinfo()`：仅返回主机名（Hostname），而非完全限定域名（FQDN）。

<a id="r_ga237a8f33470e18c8a2323ab1dd3811d2"></a>

```c
#define ZSOCK_NI_NAMEREQD 8
```

相关声明：[ZSOCK_NI_NAMEREQD](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga237a8f33470e18c8a2323ab1dd3811d2)。

`zsock_getnameinfo()`：为兼容性而保留的空操作选项（Dummy Option）。

<a id="r_ga313f921684f9dd3beb14677243dcb84f"></a>

```c
#define ZSOCK_NI_DGRAM 16
```

相关声明：[ZSOCK_NI_DGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga313f921684f9dd3beb14677243dcb84f)。

`zsock_getnameinfo()`：为兼容性而保留的空操作选项（Dummy Option）。

<a id="r_ga9ca20495ac25f8007c8a14ce2f3f5533"></a>

```c
#define ZSOCK_NI_MAXHOST 64
```

相关声明：[ZSOCK_NI_MAXHOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga9ca20495ac25f8007c8a14ce2f3f5533)。

`zsock_getnameinfo()`：支持的最大主机名（Hostname）长度。

<a id="define-members-6"></a>

### 套接字级选项（Socket level options (ZSOCK_SOL_SOCKET)）

<a id="r_gaaa2786e0b2410518b6f99e0ee196f4d4"></a>

```c
#define ZSOCK_SOL_SOCKET 1
```

相关声明：[ZSOCK_SOL_SOCKET](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaaa2786e0b2410518b6f99e0ee196f4d4)。

套接字级选项（Socket-level Option）。

<a id="r_ga37b17a378127c92ededcf397e88d6180"></a>

```c
#define ZSOCK_SO_DEBUG 1
```

相关声明：[ZSOCK_SO_DEBUG](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga37b17a378127c92ededcf397e88d6180)。

记录调试信息（Debugging Information）；为兼容性而保留，实际忽略。

<a id="r_gac2031f7190b1557d9d5020a93326d214"></a>

```c
#define ZSOCK_SO_REUSEADDR 2
```

相关声明：[ZSOCK_SO_REUSEADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac2031f7190b1557d9d5020a93326d214)。

地址复用（Address Reuse）。

<a id="r_ga950c4ad7cb1272272e6db23a20cb24a5"></a>

```c
#define ZSOCK_SO_TYPE 3
```

相关声明：[ZSOCK_SO_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga950c4ad7cb1272272e6db23a20cb24a5)。

套接字类型（Socket Type）。

<a id="r_ga60c9f18f25723883ded6c104bd04040c"></a>

```c
#define ZSOCK_SO_ERROR 4
```

相关声明：[ZSOCK_SO_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga60c9f18f25723883ded6c104bd04040c)。

异步错误（Async Error）。

<a id="r_ga037a8a927bc5afc9deb73946fbac30f6"></a>

```c
#define ZSOCK_SO_DONTROUTE 5
```

相关声明：[ZSOCK_SO_DONTROUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga037a8a927bc5afc9deb73946fbac30f6)。

绕过正常路由（Routing），直接发送到主机；为兼容性而保留，实际忽略。

<a id="r_gab0e987e826705874cc821d730a81b117"></a>

```c
#define ZSOCK_SO_BROADCAST 6
```

相关声明：[ZSOCK_SO_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab0e987e826705874cc821d730a81b117)。

支持发送广播消息（Broadcast Messages）；为兼容性而保留，实际忽略。

<a id="r_gaea93c05216e4a1d518406f42e7c7f8bc"></a>

```c
#define ZSOCK_SO_SNDBUF 7
```

相关声明：[ZSOCK_SO_SNDBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaea93c05216e4a1d518406f42e7c7f8bc)。

套接字发送缓冲区（Socket Send Buffer）的大小。

<a id="r_gad841445fdb66a8303e49b36f2aa52faa"></a>

```c
#define ZSOCK_SO_RCVBUF 8
```

相关声明：[ZSOCK_SO_RCVBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad841445fdb66a8303e49b36f2aa52faa)。

套接字接收缓冲区（Socket Receive Buffer）的大小。

<a id="r_ga4b3afec80a72e66b8c9e0f4e38cceaea"></a>

```c
#define ZSOCK_SO_KEEPALIVE 9
```

相关声明：[ZSOCK_SO_KEEPALIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga4b3afec80a72e66b8c9e0f4e38cceaea)。

启用连接上的保活消息（Keep-alive Messages）发送。

<a id="r_ga252b932a5cdc4909885b4d0a7968a5f3"></a>

```c
#define ZSOCK_SO_OOBINLINE 10
```

相关声明：[ZSOCK_SO_OOBINLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga252b932a5cdc4909885b4d0a7968a5f3)。

将带外数据（Out-of-band Data）放入接收流（Receive Stream）；为兼容性而保留，实际忽略。

<a id="r_ga477c2939c20f24ae4119d6ef8b248c08"></a>

```c
#define ZSOCK_SO_PRIORITY 12
```

相关声明：[ZSOCK_SO_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga477c2939c20f24ae4119d6ef8b248c08)。

套接字优先级（Socket Priority）。

<a id="r_ga7390a499529d767680cf7ac578f9586d"></a>

```c
#define ZSOCK_SO_LINGER 13
```

相关声明：[ZSOCK_SO_LINGER](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7390a499529d767680cf7ac578f9586d)。

套接字关闭时延迟结束（Linger）。

<a id="r_gacc93dbba4441b1617173bf9ca3c36c66"></a>

```c
#define ZSOCK_SO_REUSEPORT 15
```

相关声明：[ZSOCK_SO_REUSEPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gacc93dbba4441b1617173bf9ca3c36c66)。

允许多个套接字（Socket）复用同一个端口（Port）。

<a id="r_gaa1ee3324ef29c0bcb66c893f8f0a0a22"></a>

```c
#define ZSOCK_SO_RCVLOWAT 18
```

相关声明：[ZSOCK_SO_RCVLOWAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa1ee3324ef29c0bcb66c893f8f0a0a22)。

接收低水位（Receive Low Watermark）；为兼容性而保留，实际忽略。

<a id="r_ga87e4d65779b4c60b9a0c1ced480ed033"></a>

```c
#define ZSOCK_SO_SNDLOWAT 19
```

相关声明：[ZSOCK_SO_SNDLOWAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga87e4d65779b4c60b9a0c1ced480ed033)。

发送低水位（Send Low Watermark）；为兼容性而保留，实际忽略。

<a id="r_ga127dd9d8339be8b435ace9d6ad95e850"></a>

```c
#define ZSOCK_SO_RCVTIMEO 20
```

相关声明：[ZSOCK_SO_RCVTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga127dd9d8339be8b435ace9d6ad95e850)。

接收超时（Receive Timeout）。适用于 `recv()` 等接收函数，但不适用于 `connect()`。

<a id="r_ga786304b8676b8bc6466a7235396a07f7"></a>

```c
#define ZSOCK_SO_SNDTIMEO 21
```

相关声明：[ZSOCK_SO_SNDTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga786304b8676b8bc6466a7235396a07f7)。

发送超时（Send Timeout）。

<a id="r_ga067cb2ba7575f3c26e7458ea3276fe06"></a>

```c
#define ZSOCK_SO_BINDTODEVICE 25
```

相关声明：[ZSOCK_SO_BINDTODEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga067cb2ba7575f3c26e7458ea3276fe06)。

将套接字（Socket）绑定到接口（Interface）。

<a id="r_ga4064b264e8c62b18177ed538dc486966"></a>

```c
#define ZSOCK_SO_ACCEPTCONN 30
```

相关声明：[ZSOCK_SO_ACCEPTCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga4064b264e8c62b18177ed538dc486966)。

套接字接受传入连接（Incoming Connections）；为兼容性而保留，实际忽略。

<a id="r_ga77fdf74646e0c3b28240ae5899cee058"></a>

```c
#define ZSOCK_SO_TIMESTAMPING 37
```

相关声明：[ZSOCK_SO_TIMESTAMPING](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga77fdf74646e0c3b28240ae5899cee058)。

为发送（TX）、接收（RX）或两种方向的数据包添加时间戳（Timestamp）。

<a id="r_ga1b6d5006c4dade22d3a1c8679aa74d39"></a>

```c
#define ZSOCK_SO_PROTOCOL 38
```

相关声明：[ZSOCK_SO_PROTOCOL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1b6d5006c4dade22d3a1c8679aa74d39)。

套接字（Socket）使用的协议（Protocol）。

<a id="r_ga19f5176efede119e11a9c3fb66b9f152"></a>

```c
#define ZSOCK_SO_DOMAIN 39
```

相关声明：[ZSOCK_SO_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga19f5176efede119e11a9c3fb66b9f152)。

套接字（Socket）使用的域（Domain）。

<a id="r_ga3f136ae14247139586f85cd45d046fb3"></a>

```c
#define ZSOCK_SO_SOCKS5 60
```

相关声明：[ZSOCK_SO_SOCKS5](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga3f136ae14247139586f85cd45d046fb3)。

为套接字（Socket）启用 SOCKS5。

<a id="r_ga091f558e4c5c15e615281ba21feb130f"></a>

```c
#define ZSOCK_SO_TXTIME 61
```

相关声明：[ZSOCK_SO_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga091f558e4c5c15e615281ba21feb130f)。

套接字发送时间（Socket TX Time），即数据应发送的时刻。

<a id="r_gaf965ab6d61f7252b4c6b0750d47d6c5c"></a>

```c
#define ZSOCK_SCM_TXTIME ZSOCK_SO_TXTIME
```

相关声明：[ZSOCK_SCM_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf965ab6d61f7252b4c6b0750d47d6c5c)、[ZSOCK_SO_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga091f558e4c5c15e615281ba21feb130f)。

套接字发送时间（Socket TX Time），与 `SO_TXTIME` 相同。

<a id="r_gaf851a5752668188d6c9d66f6d349377a"></a>

```c
#define ZSOCK_SOF_TIMESTAMPING_RX_HARDWARE BIT(0)
```

相关声明：[ZSOCK_SOF_TIMESTAMPING_RX_HARDWARE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf851a5752668188d6c9d66f6d349377a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间戳生成标志（Timestamp Generation Flags）。

<a id="r_gafe8cfcce94475fa2dcc2d0e56d6a7134"></a>

```c
#define ZSOCK_SOF_TIMESTAMPING_TX_HARDWARE BIT(1)
```

相关声明：[ZSOCK_SOF_TIMESTAMPING_TX_HARDWARE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gafe8cfcce94475fa2dcc2d0e56d6a7134)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求由网络适配器（Network Adapter）生成的发送时间戳（TX Timestamp）。

<a id="define-members-7"></a>

### TCP 级选项（TCP level options (NET_IPPROTO_TCP)）

<a id="r_gaed65035762b59c3717cdc856a15f92fa"></a>

```c
#define ZSOCK_TCP_NODELAY 1
```

相关声明：[ZSOCK_TCP_NODELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaed65035762b59c3717cdc856a15f92fa)。

禁用 TCP 缓冲（Buffering）；为兼容性而保留，实际忽略。

<a id="r_ga720e01b6ceaff867dd673cdd8b648bf2"></a>

```c
#define ZSOCK_TCP_KEEPIDLE 2
```

相关声明：[ZSOCK_TCP_KEEPIDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga720e01b6ceaff867dd673cdd8b648bf2)。

经过此时间后开始发送保活消息（Keepalive），单位为秒。

<a id="r_ga1ebb7dbc45bf6b1b01cb5fe482a3f1b8"></a>

```c
#define ZSOCK_TCP_KEEPINTVL 3
```

相关声明：[ZSOCK_TCP_KEEPINTVL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1ebb7dbc45bf6b1b01cb5fe482a3f1b8)。

保活消息（Keepalive）之间的间隔，单位为秒。

<a id="r_ga0b29b699728d87c097ff51c95d2f80b1"></a>

```c
#define ZSOCK_TCP_KEEPCNT 4
```

相关声明：[ZSOCK_TCP_KEEPCNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga0b29b699728d87c097ff51c95d2f80b1)。

断开连接前发送的保活消息（Keepalive）数量。

<a id="define-members-8"></a>

### UDP 级选项（UDP level options (NET_IPPROTO_UDP)）

<a id="r_ga8e63f889afc9ca06bfea2b90e4e88b3e"></a>

```c
#define ZSOCK_UDP_OPT 1
```

相关声明：[ZSOCK_UDP_OPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8e63f889afc9ca06bfea2b90e4e88b3e)。

启用或禁用所有 UDP 选项（UDP Options），值为 `int` 类型布尔值；这些选项来自 RFC 9868。

<a id="r_ga0394de45aedd088ebcfb11006836572c"></a>

```c
#define ZSOCK_UDP_OPT_OCS 2
```

相关声明：[ZSOCK_UDP_OPT_OCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga0394de45aedd088ebcfb11006836572c)。

启用或禁用 UDP OCS，值为 `int` 类型布尔值（Boolean）。

<a id="r_ga1e80d0746eac06c45ef53011cefb9b66"></a>

```c
#define ZSOCK_UDP_OPT_APC 3
```

相关声明：[ZSOCK_UDP_OPT_APC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1e80d0746eac06c45ef53011cefb9b66)。

启用或禁用 UDP APC 选项（Option），值为 `int` 类型布尔值。

<a id="r_ga44c749f760057277985a91525ad75846"></a>

```c
#define ZSOCK_UDP_OPT_FRAG 4
```

相关声明：[ZSOCK_UDP_OPT_FRAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga44c749f760057277985a91525ad75846)。

启用或禁用 UDP 分片选项（Fragmentation Option），值为 `int` 类型布尔值。

<a id="r_gaa976bda2ebe370345e7d9324fd0102e1"></a>

```c
#define ZSOCK_UDP_OPT_MDS 5
```

相关声明：[ZSOCK_UDP_OPT_MDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa976bda2ebe370345e7d9324fd0102e1)。

设置或获取 UDP MDS 选项值（Option Value），类型为 `uint16_t`。

<a id="r_ga023dea5abc5f784df8e988492bc5bfb4"></a>

```c
#define ZSOCK_UDP_OPT_MRDS 6
```

相关声明：[ZSOCK_UDP_OPT_MRDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga023dea5abc5f784df8e988492bc5bfb4)。

设置或获取 UDP MRDS 选项值（Option Value），类型为 `struct net_udp_opt_mrds`。

<a id="r_ga62c9b039d368e75991937619e9adf8cc"></a>

```c
#define ZSOCK_UDP_OPT_REQ 7
```

相关声明：[ZSOCK_UDP_OPT_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga62c9b039d368e75991937619e9adf8cc)。

启用或禁用 UDP REQ 选项（Option），值为 `int` 类型布尔值。

<a id="r_gaec4348215929b4deff996dcac0ccd5d3"></a>

```c
#define ZSOCK_UDP_OPT_RES 8
```

相关声明：[ZSOCK_UDP_OPT_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaec4348215929b4deff996dcac0ccd5d3)。

启用或禁用 UDP RES 选项（Option），值为 `int` 类型布尔值。

<a id="r_gaaf3a09237d37bb112ee72504d926cd89"></a>

```c
#define ZSOCK_UDP_OPT_TIME 9
```

相关声明：[ZSOCK_UDP_OPT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaaf3a09237d37bb112ee72504d926cd89)。

启用或禁用 UDP TIME 选项（Option），值为 `int` 类型布尔值。

<a id="r_gac336fbf99b335b69a05004b6ca6a0104"></a>

```c
#define ZSOCK_UDP_OPT_AUTH 10
```

相关声明：[ZSOCK_UDP_OPT_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac336fbf99b335b69a05004b6ca6a0104)。

启用或禁用 UDP AUTH 选项（Option），值为 `int` 类型布尔值。

<a id="r_ga92c67eface4732a6b8faf182fc91dfcb"></a>

```c
#define ZSOCK_UDP_OPT_EXP 11
```

相关声明：[ZSOCK_UDP_OPT_EXP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga92c67eface4732a6b8faf182fc91dfcb)。

启用或禁用 UDP EXP 选项（Option），值为 `int` 类型布尔值。

<a id="r_gaf0ea7830aa95f7fe5c88bbc6b11f9627"></a>

```c
#define ZSOCK_UDP_OPT_UCMP 12
```

相关声明：[ZSOCK_UDP_OPT_UCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf0ea7830aa95f7fe5c88bbc6b11f9627)。

启用或禁用 UDP UCMP 选项（Option），值为 `int` 类型布尔值。

<a id="r_gaf95d8f076a0d4232992aea0f2545b65f"></a>

```c
#define ZSOCK_UDP_OPT_UENC 13
```

相关声明：[ZSOCK_UDP_OPT_UENC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf95d8f076a0d4232992aea0f2545b65f)。

启用或禁用 UDP UENC 选项（Option），值为 `int` 类型布尔值。

<a id="r_ga3d3737422eb33cf98300e18c5e24a214"></a>

```c
#define ZSOCK_UDP_OPT_UEXP 14
```

相关声明：[ZSOCK_UDP_OPT_UEXP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga3d3737422eb33cf98300e18c5e24a214)。

启用或禁用 UDP UEXP 选项（Option），值为 `int` 类型布尔值。

<a id="r_ga989a840540b557473a4a4438915f59de"></a>

```c
#define ZSOCK_UDP_OPT_DPLPMTUD 15
```

相关声明：[ZSOCK_UDP_OPT_DPLPMTUD](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga989a840540b557473a4a4438915f59de)。

通过 UDP 选项启用或禁用数据报分包层路径 MTU 发现（DPLPMTUD），参见 RFC 9869；值为 `int` 类型布尔值。

<a id="r_ga5cd27e199f4507097b9ab2f74ba88c10"></a>

```c
#define ZSOCK_UDP_OPT_DPLPMTUD_APP_RESPOND 16
```

相关声明：[ZSOCK_UDP_OPT_DPLPMTUD_APP_RESPOND](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5cd27e199f4507097b9ab2f74ba88c10)。

由应用程序自行完成 REQ→RES 回显（Echo），而非由协议栈处理；值为 `int` 类型布尔值。

<a id="r_ga86605887c247cf1a11701c5675c7895d"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_APC 1
```

相关声明：[ZSOCK_UDP_OPT_CMSG_APC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga86605887c247cf1a11701c5675c7895d)。

辅助数据（Ancillary Data）中 `IPPROTO_UDP` 级别的控制消息（cmsg）类型。

<a id="r_ga473e4bab8f40c07e7bfc618f256868eb"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_MDS 2
```

相关声明：[ZSOCK_UDP_OPT_CMSG_MDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga473e4bab8f40c07e7bfc618f256868eb)。

对端 MDS（Peer MDS），类型为 `uint16_t`。

<a id="r_ga2e00bde85be42b224689e67b9519ba91"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_MRDS 3
```

相关声明：[ZSOCK_UDP_OPT_CMSG_MRDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2e00bde85be42b224689e67b9519ba91)。

结构体（Structure）：`struct net_udp_opt_mrds`。

<a id="r_ga663d30569b681b857b2d3da8c9c5975a"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_REQ 4
```

相关声明：[ZSOCK_UDP_OPT_CMSG_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga663d30569b681b857b2d3da8c9c5975a)。

回显请求令牌（Echo Request Token），类型为 `uint32_t`。

<a id="r_ga4cea51ab6931e1020694569edaedb78b"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_RES 5
```

相关声明：[ZSOCK_UDP_OPT_CMSG_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga4cea51ab6931e1020694569edaedb78b)。

回显响应令牌（Echo Response Token），类型为 `uint32_t`。

<a id="r_ga0cde876903364ec01f633a1b973f0e6e"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_TIME 6
```

相关声明：[ZSOCK_UDP_OPT_CMSG_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga0cde876903364ec01f633a1b973f0e6e)。

结构体（Structure）：`struct net_udp_opt_time`。

<a id="define-members-9"></a>

### IPv4 层级选项（IPv4 Level Options，NET_IPPROTO_IP）

<a id="r_gad86db5ae0a9b9a971cb5ec75532595f9"></a>

```c
#define ZSOCK_IP_TOS 1
```

相关声明：[ZSOCK_IP_TOS](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gad86db5ae0a9b9a971cb5ec75532595f9)。

设置或获取传出数据包的服务类型（Type of Service，TOS）值。

<a id="r_ga87e8da2dafd3794240c5e1cdb2ef39fc"></a>

```c
#define ZSOCK_IP_TTL 2
```

相关声明：[ZSOCK_IP_TTL](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga87e8da2dafd3794240c5e1cdb2ef39fc)。

设置或获取传出数据包的生存时间（Time to Live，TTL）值。

<a id="r_ga19b4e323fdbc59c7d8853658b4e15e16"></a>

```c
#define ZSOCK_IP_PKTINFO 8
```

相关声明：[ZSOCK_IP_PKTINFO](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga19b4e323fdbc59c7d8853658b4e15e16)。

传递 `IP_PKTINFO` 辅助消息（Ancillary Message）；其中包含 `pktinfo` 结构体，提供传入数据包的相关信息。

<a id="r_ga32348af8cfe5540ffc85a70c642fb3e4"></a>

```c
#define ZSOCK_IP_RECVTTL 12
```

相关声明：[ZSOCK_IP_RECVTTL](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga32348af8cfe5540ffc85a70c642fb3e4)。

传递 `IP_RECVTTL` 辅助消息（Ancillary Message），其中包含传入数据包的生存时间（Time to Live）信息。

<a id="r_gaea02e9ad4ca5347a7026388f0009e730"></a>

```c
#define ZSOCK_IP_MTU 14
```

相关声明：[ZSOCK_IP_MTU](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gaea02e9ad4ca5347a7026388f0009e730)。

获取当前套接字（Socket）目前已知的路径最大传输单元（Path MTU）。

<a id="r_ga3c8f7f8895a3daae11dcd439eb2499a3"></a>

```c
#define ZSOCK_IP_DONTFRAG 15
```

相关声明：[ZSOCK_IP_DONTFRAG](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga3c8f7f8895a3daae11dcd439eb2499a3)。

禁用此套接字（Socket）的本地 IPv4 分片（Fragmentation）。

<a id="r_gaa14b3e744b44603a2aa520cacbeef95b"></a>

```c
#define ZSOCK_IP_MULTICAST_IF 32
```

相关声明：[ZSOCK_IP_MULTICAST_IF](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gaa14b3e744b44603a2aa520cacbeef95b)。

设置 IPv4 多播数据报（Multicast Datagram）使用的网络接口。

<a id="r_gab94fd2f344c2c3f1462ccec2f876b8f2"></a>

```c
#define ZSOCK_IP_MULTICAST_TTL 33
```

相关声明：[ZSOCK_IP_MULTICAST_TTL](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gab94fd2f344c2c3f1462ccec2f876b8f2)。

设置 IPv4 多播生存时间（Multicast TTL）值。

<a id="r_gaf5c2aec9a1fcaf0515ccd7d1d5b57cb2"></a>

```c
#define ZSOCK_IP_MULTICAST_LOOP 34
```

相关声明：[ZSOCK_IP_MULTICAST_LOOP](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gaf5c2aec9a1fcaf0515ccd7d1d5b57cb2)。

设置 IPv4 多播回环（Multicast Loop）值。

<a id="r_ga9bd617872815d3752e9464f98d32e1ce"></a>

```c
#define ZSOCK_IP_ADD_MEMBERSHIP 35
```

相关声明：[ZSOCK_IP_ADD_MEMBERSHIP](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga9bd617872815d3752e9464f98d32e1ce)。

加入 IPv4 多播组（Multicast Group）。

<a id="r_ga5bf7c18d0400ee370db3bfeab812598a"></a>

```c
#define ZSOCK_IP_DROP_MEMBERSHIP 36
```

相关声明：[ZSOCK_IP_DROP_MEMBERSHIP](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga5bf7c18d0400ee370db3bfeab812598a)。

离开 IPv4 多播组（Multicast Group）。

<a id="r_gaceaecf7f826715aab2740c57c6ec6407"></a>

```c
#define ZSOCK_IP_LOCAL_PORT_RANGE 51
```

相关声明：[ZSOCK_IP_LOCAL_PORT_RANGE](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gaceaecf7f826715aab2740c57c6ec6407)。

针对给定套接字（Socket）缩小全局端口范围（Global Port Range）。

<a id="define-members-10"></a>

### IPv6 层级选项（IPv6 Level Options，NET_IPPROTO_IPV6）

<a id="r_ga6b3364d4ea2e4c34f1de975e6f66961b"></a>

```c
#define ZSOCK_IPV6_UNICAST_HOPS 16
```

相关声明：[ZSOCK_IPV6_UNICAST_HOPS](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga6b3364d4ea2e4c34f1de975e6f66961b)。

设置套接字的单播跳数限制（Unicast Hop Limit）。

<a id="r_ga4f15d7b5032536896c0785f16830329d"></a>

```c
#define ZSOCK_IPV6_MULTICAST_IF 17
```

相关声明：[ZSOCK_IPV6_MULTICAST_IF](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga4f15d7b5032536896c0785f16830329d)。

设置套接字的多播输出网络接口索引（Multicast Output Network Interface Index）。

<a id="r_ga78bda8f2e2c0e0fc3cf9788c42d8b6f8"></a>

```c
#define ZSOCK_IPV6_MULTICAST_HOPS 18
```

相关声明：[ZSOCK_IPV6_MULTICAST_HOPS](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga78bda8f2e2c0e0fc3cf9788c42d8b6f8)。

设置套接字的多播跳数限制（Multicast Hop Limit）。

<a id="r_ga6fc007f21de54e12697a21712ca095c3"></a>

```c
#define ZSOCK_IPV6_MULTICAST_LOOP 19
```

相关声明：[ZSOCK_IPV6_MULTICAST_LOOP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga6fc007f21de54e12697a21712ca095c3)。

设置套接字的多播环回位（Multicast Loop Bit）。

<a id="r_gae438698778cfe58c28c7928f9b227f30"></a>

```c
#define ZSOCK_IPV6_ADD_MEMBERSHIP 20
```

相关声明：[ZSOCK_IPV6_ADD_MEMBERSHIP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gae438698778cfe58c28c7928f9b227f30)。

加入 IPv6 多播组（Multicast Group）。

<a id="r_ga1d70e019e1341a3d54dfd7a819cb7071"></a>

```c
#define ZSOCK_IPV6_DROP_MEMBERSHIP 21
```

相关声明：[ZSOCK_IPV6_DROP_MEMBERSHIP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga1d70e019e1341a3d54dfd7a819cb7071)。

离开 IPv6 多播组（Multicast Group）。

<a id="r_gab524aa153b4a7005f988d7bb167bacab"></a>

```c
#define ZSOCK_IPV6_JOIN_GROUP ZSOCK_IPV6_ADD_MEMBERSHIP
```

相关声明：[ZSOCK_IPV6_JOIN_GROUP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gab524aa153b4a7005f988d7bb167bacab)、[ZSOCK_IPV6_ADD_MEMBERSHIP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gae438698778cfe58c28c7928f9b227f30)。

加入 IPv6 多播组（Multicast Group）。

<a id="r_ga1b2fc808d5b602e658d88d66f1f1d1d1"></a>

```c
#define ZSOCK_IPV6_LEAVE_GROUP ZSOCK_IPV6_DROP_MEMBERSHIP
```

相关声明：[ZSOCK_IPV6_LEAVE_GROUP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga1b2fc808d5b602e658d88d66f1f1d1d1)、[ZSOCK_IPV6_DROP_MEMBERSHIP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga1d70e019e1341a3d54dfd7a819cb7071)。

离开 IPv6 多播组（Multicast Group）。

<a id="r_gac37821fc6bd4b484ff36a00dea505245"></a>

```c
#define ZSOCK_IPV6_MTU 24
```

相关声明：[ZSOCK_IPV6_MTU](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gac37821fc6bd4b484ff36a00dea505245)。

对于 getsockopt()，获取指定套接字当前已知的 IPv6 路径最大传输单元（Path MTU）。

<a id="r_ga44b16e54bc2922153e9a07d628cf1cba"></a>

```c
#define ZSOCK_IPV6_DONTFRAG 62
```

相关声明：[ZSOCK_IPV6_DONTFRAG](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga44b16e54bc2922153e9a07d628cf1cba)。

对此套接字禁用本地 IPv6 分片（Fragmentation）。

<a id="r_ga004e5f8352ae9c6d8096919e44fdd874"></a>

```c
#define ZSOCK_IPV6_V6ONLY 26
```

相关声明：[ZSOCK_IPV6_V6ONLY](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga004e5f8352ae9c6d8096919e44fdd874)。

不支持 IPv4 访问。

<a id="r_gab399d0b2da77aa4331490bb312aa2fb0"></a>

```c
#define ZSOCK_IPV6_RECVPKTINFO 49
```

相关声明：[ZSOCK_IPV6_RECVPKTINFO](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gab399d0b2da77aa4331490bb312aa2fb0)。

传递 IPV6_RECVPKTINFO 辅助消息（Ancillary Message），其中包含 in6_pktinfo 结构体，提供入站数据包的一些信息。

<a id="r_ga24b054ba13a54ae2064aea31f52d7ed0"></a>

```c
#define ZSOCK_IPV6_PKTINFO 50
```

相关声明：[ZSOCK_IPV6_PKTINFO](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga24b054ba13a54ae2064aea31f52d7ed0)。

在辅助数据（Ancillary Data）中返回 in6_pktinfo 结构体的选项。

<a id="r_gad0c689068bc6bff4369a1ea9b36d09a9"></a>

```c
#define ZSOCK_IPV6_RECVHOPLIMIT 51
```

相关声明：[ZSOCK_IPV6_RECVHOPLIMIT](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gad0c689068bc6bff4369a1ea9b36d09a9)。

传递 IPV6_RECVHOPLIMIT 辅助消息（Ancillary Message），其中包含入站数据包的跳数限制（Hop Limit）信息。

<a id="r_ga92c73652d38a41b8acea0a69362f3e0d"></a>

```c
#define ZSOCK_IPV6_HOPLIMIT 52
```

相关声明：[ZSOCK_IPV6_HOPLIMIT](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga92c73652d38a41b8acea0a69362f3e0d)。

设置或获取出站数据包的跳数限制（Hoplimit）值。

<a id="r_ga6fd9aed65cb7a1a7eface8455501212b"></a>

```c
#define ZSOCK_IPV6_ADDR_PREFERENCES 72
```

相关声明：[ZSOCK_IPV6_ADDR_PREFERENCES](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga6fd9aed65cb7a1a7eface8455501212b)。

RFC 5014：源地址选择（Source Address Selection）。

<a id="r_ga061badf1fcadf353667f10a64b77bcb5"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_TMP 0x0001
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_TMP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga061badf1fcadf353667f10a64b77bcb5)。

优先使用临时地址（Temporary Address）作为源地址。

<a id="r_ga3acbfad85a26f4a71b51e570369122a4"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_PUBLIC 0x0002
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_PUBLIC](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga3acbfad85a26f4a71b51e570369122a4)。

优先使用公共地址（Public Address）作为源地址。

<a id="r_ga2ecb5f065f2f8806ff7ee680ce3b8bee"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_PUBTMP_DEFAULT 0x0100
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_PUBTMP_DEFAULT](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga2ecb5f065f2f8806ff7ee680ce3b8bee)。

根据输出接口配置，选择公共地址（Public Address）或临时地址（Temporary Address）作为默认源地址；这是默认值。

<a id="r_ga60f0a56613fdf6532dd2549273f6e6a2"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_COA 0x0004
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_COA](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga60f0a56613fdf6532dd2549273f6e6a2)。

优先使用转交地址（Care-of Address）作为源地址。

<a id="r_gac9afff595eac9ca47c0e14da20531d6b"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_HOME 0x0400
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_HOME](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gac9afff595eac9ca47c0e14da20531d6b)。

优先使用家乡地址（Home Address）作为源地址。

<a id="r_gaa3b4dd46e7b1fdeaae6db4a692c7f57a"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_CGA 0x0008
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_CGA](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gaa3b4dd46e7b1fdeaae6db4a692c7f57a)。

优先使用密码生成地址（Cryptographically Generated Address，CGA）作为源地址。

<a id="r_gaa10785a8136550462a895621b2866d0f"></a>

```c
#define ZSOCK_IPV6_PREFER_SRC_NONCGA 0x0800
```

相关声明：[ZSOCK_IPV6_PREFER_SRC_NONCGA](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gaa10785a8136550462a895621b2866d0f)。

优先使用非 CGA 地址作为源地址。

<a id="r_gabe60a1f3a16e4b0a4b2c997f91497c62"></a>

```c
#define ZSOCK_IPV6_TCLASS 67
```

相关声明：[ZSOCK_IPV6_TCLASS](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gabe60a1f3a16e4b0a4b2c997f91497c62)。

设置或获取出站数据包的流量类别（Traffic Class）值。

<a id="define-members-11"></a>

### listen() 的待连接队列大小（Backlog size for listen()）

<a id="r_ga95372181a0f868383e6631de84145e39"></a>

```c
#define ZSOCK_SOMAXCONN 128
```

相关声明：[ZSOCK_SOMAXCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga95372181a0f868383e6631de84145e39)。

`listen`：待连接队列（Backlog Queue）的最大长度。

<a id="define-members-12"></a>

### 检查特殊 IPv6 地址的宏（Macros for checking special IPv6 addresses.）

<a id="r_ga3ff22595e17c630cf07d40a5e178ecce"></a>

```c
#define ZSOCK_IN6_IS_ADDR_UNSPECIFIED(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga3ff22595e17c630cf07d40a5e178ecce)。

检查是否为未指定的 IPv6 地址（Unspecified IPv6 Address）。

<a id="r_gac92eaa41e32e464249bf703d16f869b4"></a>

```c
#define ZSOCK_IN6_IS_ADDR_LOOPBACK(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_LOOPBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac92eaa41e32e464249bf703d16f869b4)。

检查是否为 IPv6 回环地址（Loopback Address）。

<a id="r_gac8fceb6a75060068126f4a4ea5b24fb9"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MULTICAST(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MULTICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac8fceb6a75060068126f4a4ea5b24fb9)。

检查是否为 IPv6 多播地址（Multicast Address）。

<a id="r_gaa2ea2ea293a83c2b3c4851ce517d38bf"></a>

```c
#define ZSOCK_IN6_IS_ADDR_LINKLOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_LINKLOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa2ea2ea293a83c2b3c4851ce517d38bf)。

检查是否为 IPv6 链路本地地址（Link Local Address）。

<a id="r_ga91dc0bd2f4fb09cefad741ee0b1e2c20"></a>

```c
#define ZSOCK_IN6_IS_ADDR_SITELOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_SITELOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga91dc0bd2f4fb09cefad741ee0b1e2c20)。

检查是否为 IPv6 站点本地地址（Site Local Address）。

<a id="r_ga11df060795e7146f2294ef50d4832cfa"></a>

```c
#define ZSOCK_IN6_IS_ADDR_V4MAPPED(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_V4MAPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga11df060795e7146f2294ef50d4832cfa)。

检查是否为 IPv4 映射的 IPv6 地址（IPv4 Mapped IPv6 Address）。

<a id="r_ga42c8ad2a3bb2c223148ab4155be091a2"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_GLOBAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_GLOBAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga42c8ad2a3bb2c223148ab4155be091a2)。

检查是否为 IPv6 全局多播地址（Multicast Global Address）。

<a id="r_ga106dff01f87ce99d72d54048f837fbdb"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_NODELOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_NODELOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga106dff01f87ce99d72d54048f837fbdb)。

检查是否为 IPv6 节点本地多播地址（Multicast Node Local Address）。

<a id="r_ga00067e1cde69c9ae9ad71f0356314964"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_LINKLOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_LINKLOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga00067e1cde69c9ae9ad71f0356314964)。

检查是否为 IPv6 链路本地多播地址（Multicast Link Local Address）。

<a id="r_ga76114e85298c02cb5cb37e6a8d9ad566"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_SITELOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_SITELOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga76114e85298c02cb5cb37e6a8d9ad566)。

检查是否为 IPv6 站点本地多播地址（Multicast Site Local Address）。

<a id="r_gae0982428d5720288e7273d442d07d035"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_ORGLOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_ORGLOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae0982428d5720288e7273d442d07d035)。

检查是否为 IPv6 组织本地多播地址（Multicast Organization Local Address）。

<a id="define-members-13"></a>

### 套接字级选项（Socket Level Options，ZSOCK_SOL_PACKET）

<a id="r_ga64d5f1636f942f9ff1f02d9918482931"></a>

```c
#define ZSOCK_SOL_PACKET 263
```

相关声明：[ZSOCK_SOL_PACKET](../api_extension_topic_reference/P022_分组套接字的套接字选项（Socket options for packet socket）.md#ga64d5f1636f942f9ff1f02d9918482931)。

数据包套接字级选项（Packet Socket-Level Option）。

<a id="r_ga9674edba4b48e4cc2d1e01a101cead9b"></a>

```c
#define ZSOCK_PACKET_ADD_MEMBERSHIP 1
```

相关声明：[ZSOCK_PACKET_ADD_MEMBERSHIP](../api_extension_topic_reference/P022_分组套接字的套接字选项（Socket options for packet socket）.md#ga9674edba4b48e4cc2d1e01a101cead9b)。

向数据包套接字（Packet Socket）添加多播组成员资格（Multicast Group Membership）。

<a id="r_ga59b254e51063accfb18916b17373d2f6"></a>

```c
#define ZSOCK_PACKET_DROP_MEMBERSHIP 2
```

相关声明：[ZSOCK_PACKET_DROP_MEMBERSHIP](../api_extension_topic_reference/P022_分组套接字的套接字选项（Socket options for packet socket）.md#ga59b254e51063accfb18916b17373d2f6)。

从数据包套接字（Packet Socket）移除多播组成员资格（Multicast Group Membership）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="r_ga21a871d1fa6b6beeed88408761877873"></a>

```c
void * zsock_get_context_object (int sock)
```

相关声明：[zsock_get_context_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga21a871d1fa6b6beeed88408761877873)。

获取文件描述符（File Descriptor）关联的网络上下文（Net Context）。

<a id="r_ga5693d19a0bdff45a5cb09227683d8631"></a>

```c
int zsock_socket (int family, int type, int proto)
```

相关声明：[zsock_socket](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5693d19a0bdff45a5cb09227683d8631)。

创建网络套接字（Network Socket）。

<a id="r_ga1f5e089c9fb39d3a8884502a11e389b3"></a>

```c
int zsock_socketpair (int family, int type, int proto, int *sv)
```

相关声明：[zsock_socketpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1f5e089c9fb39d3a8884502a11e389b3)。

创建一对未命名且相互连接的套接字（Unnamed Pair of Connected Sockets）。

<a id="r_gae60d7ca486955dd79a2821d1f646c349"></a>

```c
int zsock_close (int sock)
```

相关声明：[zsock_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae60d7ca486955dd79a2821d1f646c349)。

关闭网络套接字（Network Socket）。

<a id="r_gac56432bf901efaf8ef782430ac143f03"></a>

```c
int zsock_shutdown (int sock, int how)
```

相关声明：[zsock_shutdown](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac56432bf901efaf8ef782430ac143f03)。

关闭套接字（Socket）的发送／接收操作。

<a id="r_ga70909e3233d6523d0ad9566b5edd117c"></a>

```c
int zsock_bind (int sock, const struct net_sockaddr *addr, net_socklen_t addrlen)
```

相关声明：[zsock_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga70909e3233d6523d0ad9566b5edd117c)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

将套接字（Socket）绑定到本地网络地址（Local Network Address）。

<a id="r_gad858da9650c1270faf5229e3888d7db1"></a>

```c
int zsock_connect (int sock, const struct net_sockaddr *addr, net_socklen_t addrlen)
```

相关声明：[zsock_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad858da9650c1270faf5229e3888d7db1)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

将套接字（Socket）连接到对端网络地址（Peer Network Address）。

<a id="r_gae8ea59ea82063aa28a9b72da2f08c9fd"></a>

```c
int zsock_listen (int sock, int backlog)
```

相关声明：[zsock_listen](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae8ea59ea82063aa28a9b72da2f08c9fd)。

设置流式套接字（STREAM Socket），使其接受对端连接（Peer Connection）。

<a id="r_ga1532a65955c402cbb365becb58167f19"></a>

```c
int zsock_accept (int sock, struct net_sockaddr *addr, net_socklen_t *addrlen)
```

相关声明：[zsock_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1532a65955c402cbb365becb58167f19)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

在监听套接字（Listening Socket）上接受连接。

<a id="r_ga9f4ff3d1637393cbe74bd111cc6f432a"></a>

```c
ssize_t zsock_sendto (int sock, const void *buf, size_t len, int flags, const struct net_sockaddr *dest_addr, net_socklen_t addrlen)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_sendto](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga9f4ff3d1637393cbe74bd111cc6f432a)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

向任意网络地址（Network Address）发送数据。

<a id="r_ga2d8c2173986f67dde6dc5721bf690855"></a>

```c
static ssize_t zsock_send (int sock, const void *buf, size_t len, int flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2d8c2173986f67dde6dc5721bf690855)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

向已连接的对端（Connected Peer）发送数据。

<a id="r_gad3274fe71d43caf8c4d92fffb589375e"></a>

```c
ssize_t zsock_sendmsg (int sock, const struct net_msghdr *msg, int flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_sendmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad3274fe71d43caf8c4d92fffb589375e)、[net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

向任意网络地址（Network Address）发送数据。

<a id="r_ga89271d76123b0a69e0c40ae4de58bd0a"></a>

```c
ssize_t zsock_recvfrom (int sock, void *buf, size_t max_len, int flags, struct net_sockaddr *src_addr, net_socklen_t *addrlen)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_recvfrom](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga89271d76123b0a69e0c40ae4de58bd0a)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

从任意网络地址（Network Address）接收数据。

<a id="r_ga02b0de9a15c2d1133b87216d6afc203f"></a>

```c
ssize_t zsock_recvmsg (int sock, struct net_msghdr *msg, int flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_recvmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga02b0de9a15c2d1133b87216d6afc203f)、[net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从任意网络地址（Network Address）接收消息（Message）。

<a id="r_ga8a7d82cfb02a45de59ccd05614eb78d6"></a>

```c
static ssize_t zsock_recv (int sock, void *buf, size_t max_len, int flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8a7d82cfb02a45de59ccd05614eb78d6)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从已连接的对端（Connected Peer）接收数据。

<a id="r_gab069dc3ebc140af65801a73fcac4f629"></a>

```c
int zsock_fcntl_impl (int sock, int cmd, int flags)
```

相关声明：[zsock_fcntl_impl](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab069dc3ebc140af65801a73fcac4f629)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

控制套接字（Socket）的阻塞／非阻塞模式（Blocking/Non-blocking Mode）。

<a id="r_ga0255a43336642aaeeaa5bff4c29c9389"></a>

```c
int zsock_ioctl_impl (int sock, unsigned long request, va_list ap)
```

相关声明：[zsock_ioctl_impl](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga0255a43336642aaeeaa5bff4c29c9389)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

控制底层套接字参数（Underlying Socket Parameters）。

<a id="r_ga518361903c9fac3766164d38243872e3"></a>

```c
static int zsock_poll (struct zsock_pollfd *fds, int nfds, int timeout)
```

相关声明：[zsock_poll](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga518361903c9fac3766164d38243872e3)、[zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)。

高效轮询多个套接字（Socket）的事件（Event）。

<a id="r_ga6aa12f0dbed8ded425555debba044a98"></a>

```c
int zsock_getsockopt (int sock, int level, int optname, void *optval, net_socklen_t *optlen)
```

相关声明：[zsock_getsockopt](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6aa12f0dbed8ded425555debba044a98)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

获取各种套接字选项（Socket Options）。

<a id="r_ga71ac8d52c87b9182a9f1a03614e3dba7"></a>

```c
int zsock_setsockopt (int sock, int level, int optname, const void *optval, net_socklen_t optlen)
```

相关声明：[zsock_setsockopt](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga71ac8d52c87b9182a9f1a03614e3dba7)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

设置各种套接字选项（Socket Options）。

<a id="r_ga78b0ca26c0aaf5e64b05da8caa8c253c"></a>

```c
int zsock_getpeername (int sock, struct net_sockaddr *addr, net_socklen_t *addrlen)
```

相关声明：[zsock_getpeername](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga78b0ca26c0aaf5e64b05da8caa8c253c)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

获取对端名称（Peer Name）。

<a id="r_ga6bf17561e03600ed870dff702b513d9c"></a>

```c
int zsock_getsockname (int sock, struct net_sockaddr *addr, net_socklen_t *addrlen)
```

相关声明：[zsock_getsockname](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6bf17561e03600ed870dff702b513d9c)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

获取套接字名称（Socket Name）。

<a id="r_ga8b348d886f1bc4f4cdf6e2260844f6e1"></a>

```c
int zsock_gethostname (char *buf, size_t len)
```

相关声明：[zsock_gethostname](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8b348d886f1bc4f4cdf6e2260844f6e1)。

获取本地主机名（Local Host Name）。

<a id="r_gad3dbb44d7b49249c124e41041aca6536"></a>

```c
static char * zsock_inet_ntop (net_sa_family_t family, const void *src, char *dst, size_t size)
```

相关声明：[zsock_inet_ntop](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad3dbb44d7b49249c124e41041aca6536)、[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)。

将网络地址（Network Address）从内部表示转换为数字 ASCII 形式（Numeric ASCII Form）。

<a id="r_gaf0130ad342c6873d68bdc51d9cf1167b"></a>

```c
int zsock_inet_pton (net_sa_family_t family, const char *src, void *dst)
```

相关声明：[zsock_inet_pton](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf0130ad342c6873d68bdc51d9cf1167b)、[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)。

将网络地址（Network Address）从数字 ASCII 形式（Numeric ASCII Form）转换为内部表示。

<a id="r_gaf59c97c9bd07f188e3f06b2372ac1856"></a>

```c
int zsock_getaddrinfo (const char *host, const char *service, const struct zsock_addrinfo *hints, struct zsock_addrinfo **res)
```

相关声明：[zsock_getaddrinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf59c97c9bd07f188e3f06b2372ac1856)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

将域名（Domain Name）解析为一个或多个网络地址（Network Address）。

<a id="r_ga7953da2e52bcfad51b877de6d7fd6cc9"></a>

```c
void zsock_freeaddrinfo (struct zsock_addrinfo *ai)
```

相关声明：[zsock_freeaddrinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7953da2e52bcfad51b877de6d7fd6cc9)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

释放 `zsock_getaddrinfo()` 返回的结果。

<a id="r_gaa9d9e97c347b3854dc73d7ba33d8ca4b"></a>

```c
const char * zsock_gai_strerror (int errcode)
```

相关声明：[zsock_gai_strerror](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa9d9e97c347b3854dc73d7ba33d8ca4b)。

将 `zsock_getaddrinfo()` 的错误码（Error Code）转换为文本消息。

<a id="r_ga5b02979bf93763a9cc5711c7267d5de8"></a>

```c
int zsock_getnameinfo (const struct net_sockaddr *addr, net_socklen_t addrlen, char *host, net_socklen_t hostlen, char *serv, net_socklen_t servlen, int flags)
```

相关声明：[zsock_getnameinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5b02979bf93763a9cc5711c7267d5de8)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将网络地址（Network Address）解析为域名（Domain Name）或 ASCII 地址。

<a id="r_ga8a8e90b68fb77179677f237bc22289ec"></a>

```c
int zsock_send_all (int sock, const void *buf, size_t len, int flags, k_timeout_t timeout, size_t *sent_len)
```

相关声明：[zsock_send_all](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8a8e90b68fb77179677f237bc22289ec)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向任意网络地址（Network Address）发送数据。

<a id="r_ga4d2d0823ad8785ffdc2ae327e8651d3f"></a>

```c
int zsock_sendmsg_all (int sock, const struct net_msghdr *msg, int flags, k_timeout_t timeout, size_t *sent_len)
```

相关声明：[zsock_sendmsg_all](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga4d2d0823ad8785ffdc2ae327e8651d3f)、[net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向任意网络地址（Network Address）发送数据。


## 9.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/socket_select.h](../api_source_reference/P802_socket_select.h_源码浏览.md)
- [zephyr/net/socket_poll.h](../api_source_supplement_reference/P184_socket_poll.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/fdtable.h](../api_source_architecture_reference/P007_fdtable.h_源码浏览.md)
- [zephyr/net/dns_resolve.h](../api_source_transport_clock_reference/P008_dns_resolve.h_源码浏览.md)
- [stdlib.h](../api_source_configuration_reference/P107_stdlib.h_源码浏览.md)
- [查看此文件的源码。](../api_source_socket_ethernet_reference/P006_socket.h_源码浏览.md)
- [zsock_tls_cert_verify_cb](../posix_system_model_reference/P031_zsock_tls_cert_verify_cb_结构体.md)
- [ZSOCK_TLS_CERT_VERIFY_CALLBACK](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga4425112197a30ca359c57de0e824f0d1)
- [zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)
- [ZSOCK_POLLIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6ade0deb4952e1ea23b368d9eceee9ed)
- [ZSOCK_POLLPRI](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1c96c16d5000db0fa4b69055ebb97839)
- [ZSOCK_POLLOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga9ca302c64dfb676798ce03100894ca3e)
- [ZSOCK_POLLERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad44368a112fbf91436a2439e7b767641)
- [ZSOCK_POLLHUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gadd341cd5c1f6d7deeaedc5c58dc56fe7)
- [ZSOCK_POLLNVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga45c5b0efca6e09e4f7db78d1d007bf67)
- [ZSOCK_MSG_PEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae7da123a40584192b65af77e918080b9)
- [ZSOCK_MSG_CTRUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gabdc593f541a4f9a607cfe140cee19c4a)
- [ZSOCK_MSG_TRUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae594c5e74cd473df8e3328a4cd935ce1)
- [ZSOCK_MSG_DONTWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga92cf4460e23f376bf130d885ea64ed6b)
- [ZSOCK_MSG_WAITALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga00b950f50302d97c27111da49f5289fb)
- [ZSOCK_SHUT_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2a58cbc62db1e559898ea979454d74d4)
- [ZSOCK_SHUT_WR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga87630f1abe81c4e33a24cb1f1ebb3571)
- [ZSOCK_SHUT_RDWR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga788dcff81663a9fb01e32b53bca13e2d)
- [ZSOCK_SOL_TLS](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga7209d2f574caf7bf18dfc135b1e89c33)
- [ZSOCK_TLS_SEC_TAG_LIST](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga7e47484ee379d42f1d90d652796f0406)
- [ZSOCK_TLS_HOSTNAME](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga46e839d445926ba59de5da0edf0f2507)
- [ZSOCK_TLS_CIPHERSUITE_LIST](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga93b27c4d4ed48976d1b8d8307e753d3f)
- [ZSOCK_TLS_CIPHERSUITE_USED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gae186f97c3783a29ad4c3df7dd566da95)
- [ZSOCK_TLS_PEER_VERIFY](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gac02711515e3bdfabe41061cfc65f5c67)
- [ZSOCK_TLS_DTLS_ROLE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga7f7a51d68a1901948696d597f0548488)
- [ZSOCK_TLS_ALPN_LIST](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga21e38f62fbd83c39a71aec844445a101)
- [ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MIN](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaa480277784420697eeebbbd71043404a)
- [ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MAX](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaea9de0d195605882ab6e94cf2ea13907)
- [ZSOCK_TLS_CERT_NOCOPY](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gac976e4d41ca9ef41debb4c997b28b43a)
- [ZSOCK_TLS_NATIVE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gab446ab6448359979f2d5e895729be993)
- [ZSOCK_TLS_SESSION_CACHE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gacc4c3078ac3169958739ae3425f90a94)
- [ZSOCK_TLS_SESSION_CACHE_PURGE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaf1ad38710d9131206f80d9bd8ea7e66f)
- [ZSOCK_TLS_DTLS_CID](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaf57ee9894cc4bb7f3fa88e08f7842aa1)
- [ZSOCK_TLS_DTLS_CID_STATUS](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga7158a9a83f566702be6611866123a0f3)
- [ZSOCK_TLS_DTLS_CID_VALUE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gac98e03783df8195b76725f8f31fefa1e)
- [ZSOCK_TLS_DTLS_PEER_CID_VALUE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga58b97b28c49ee9dca9b8e80f934b4796)
- [ZSOCK_TLS_DTLS_HANDSHAKE_ON_CONNECT](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaa6198fcf99c8bc37699655a9f34cbfb3)
- [connect()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)
- [ZSOCK_TLS_CERT_VERIFY_RESULT](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga1aaed12ee67d524fd97b7f129b89c70e)
- [ZSOCK_TLS_MAX_FRAGMENT_LENGTH](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga2a4337feada2ae7415dc095e8cd03c7b)
- [ZSOCK_TLS_MFL_DEFAULT](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaa6b53c582059322fb2abc1aaab4ee989)
- [ZSOCK_TLS_MFL_DISABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga4428a55bc1b2c3598fbefd551126f342)
- [ZSOCK_TLS_MFL_512](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga373ff68ef9c42deff07140c42ea63c0a)
- [ZSOCK_TLS_MFL_1024](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga6480b3675b8ec9c39af42208775bc8e9)
- [ZSOCK_TLS_MFL_2048](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga25fb9c75cca8c77db2a492ef11f3164a)
- [ZSOCK_TLS_MFL_4096](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaa5df8ff4408d6e3b62c47e0838d481a2)
- [ZSOCK_TLS_PEER_VERIFY_NONE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga8341e61b00eda2e56deac47e53e96da2)
- [ZSOCK_TLS_PEER_VERIFY_OPTIONAL](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaef97aaad3f4a97a2954e8aad1fd7857e)
- [ZSOCK_TLS_PEER_VERIFY_REQUIRED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gab9a4437457cdf80141d4567cef754a7a)
- [ZSOCK_TLS_DTLS_ROLE_CLIENT](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga3b96ba39bdcb5b0682e13a6ff421780c)
- [ZSOCK_TLS_DTLS_ROLE_SERVER](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gadeff0aead8c8aa093418fbeb759ad59a)
- [ZSOCK_TLS_CERT_NOCOPY_NONE](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaf774285e3c5459c25098c5e371299c02)
- [ZSOCK_TLS_CERT_NOCOPY_OPTIONAL](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga3c08db9b4bb990f127f42cccbe049b58)
- [ZSOCK_TLS_SESSION_CACHE_DISABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gaf66290b67a7deee2847c9a7301df177d)
- [ZSOCK_TLS_SESSION_CACHE_ENABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga92cc4f8261b5d669cc3032d4b0e0a76a)
- [ZSOCK_TLS_DTLS_CID_DISABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga701820487b6651e16319235c43ade526)
- [ZSOCK_TLS_DTLS_CID_SUPPORTED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga5037d23a87ce456873b68c3712d00177)
- [ZSOCK_TLS_DTLS_CID_ENABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gae53fd78b605b6c65f164f449146d369e)
- [ZSOCK_TLS_DTLS_CID_STATUS_DISABLED](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#gadbe80ee9dcc81383086f99da6f7d6468)
- [ZSOCK_TLS_DTLS_CID_STATUS_DOWNLINK](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga307213073d76058f6a276dd7493e2bd2)
- [ZSOCK_TLS_DTLS_CID_STATUS_UPLINK](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga14275c57f01cb81292049aabe468ec3f)
- [ZSOCK_TLS_DTLS_CID_STATUS_BIDIRECTIONAL](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md#ga46da3503cbb491f471121cd50a342b03)
- [ZSOCK_AI_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6a63246ff9f8106f533d4d929185a550)
- [bind()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a05b4e957a092db3e68281988ceb32df8)
- [ZSOCK_AI_CANONNAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab1d9d790b3117fa8a0f997fc45e0f5fd)
- [ZSOCK_AI_NUMERICHOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga22b39ed3a330312a68778c8fa8f0f99e)
- [ZSOCK_AI_V4MAPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8913ef12daf85f8f7e364fb8bbc0d546)
- [ZSOCK_AI_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae24cbe0ed18c68e181940954a8116829)
- [ZSOCK_AI_ADDRCONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga727bf0f112fbdd9ff1be890177ae42c7)
- [ZSOCK_AI_NUMERICSERV](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga88b89291f68f34337f8c2416a147e671)
- [ZSOCK_AI_EXTFLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7cd2b1b26066eee23497b1b39ed564c3)
- [RFC 5014](https://datatracker.ietf.org/doc/html/rfc5014)
- [ZSOCK_NI_NUMERICHOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaae950d30c261a1b36972fd4e5aa3a3a6)
- [zsock_getnameinfo()](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5b02979bf93763a9cc5711c7267d5de8)
- [ZSOCK_NI_NUMERICSERV](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga91cf6f543827efd4a75d92a9ddacfae6)
- [ZSOCK_NI_NOFQDN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2f57f503276a43cc049fc66269792239)
- [ZSOCK_NI_NAMEREQD](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga237a8f33470e18c8a2323ab1dd3811d2)
- [ZSOCK_NI_DGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga313f921684f9dd3beb14677243dcb84f)
- [ZSOCK_NI_MAXHOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga9ca20495ac25f8007c8a14ce2f3f5533)
- [ZSOCK_SOL_SOCKET](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaaa2786e0b2410518b6f99e0ee196f4d4)
- [ZSOCK_SO_DEBUG](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga37b17a378127c92ededcf397e88d6180)
- [ZSOCK_SO_REUSEADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac2031f7190b1557d9d5020a93326d214)
- [ZSOCK_SO_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga950c4ad7cb1272272e6db23a20cb24a5)
- [ZSOCK_SO_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga60c9f18f25723883ded6c104bd04040c)
- [ZSOCK_SO_DONTROUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga037a8a927bc5afc9deb73946fbac30f6)
- [ZSOCK_SO_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab0e987e826705874cc821d730a81b117)
- [ZSOCK_SO_SNDBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaea93c05216e4a1d518406f42e7c7f8bc)
- [ZSOCK_SO_RCVBUF](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad841445fdb66a8303e49b36f2aa52faa)
- [ZSOCK_SO_KEEPALIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga4b3afec80a72e66b8c9e0f4e38cceaea)
- [ZSOCK_SO_OOBINLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga252b932a5cdc4909885b4d0a7968a5f3)
- [ZSOCK_SO_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga477c2939c20f24ae4119d6ef8b248c08)
- [ZSOCK_SO_LINGER](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7390a499529d767680cf7ac578f9586d)
- [ZSOCK_SO_REUSEPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gacc93dbba4441b1617173bf9ca3c36c66)
- [ZSOCK_SO_RCVLOWAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa1ee3324ef29c0bcb66c893f8f0a0a22)
- [ZSOCK_SO_SNDLOWAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga87e4d65779b4c60b9a0c1ced480ed033)
- [ZSOCK_SO_RCVTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga127dd9d8339be8b435ace9d6ad95e850)
- [recv()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)
- [ZSOCK_SO_SNDTIMEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga786304b8676b8bc6466a7235396a07f7)
- [ZSOCK_SO_BINDTODEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga067cb2ba7575f3c26e7458ea3276fe06)
- [ZSOCK_SO_ACCEPTCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga4064b264e8c62b18177ed538dc486966)
- [ZSOCK_SO_TIMESTAMPING](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga77fdf74646e0c3b28240ae5899cee058)
- [ZSOCK_SO_PROTOCOL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1b6d5006c4dade22d3a1c8679aa74d39)
- [ZSOCK_SO_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga19f5176efede119e11a9c3fb66b9f152)
- [ZSOCK_SO_SOCKS5](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga3f136ae14247139586f85cd45d046fb3)
- [ZSOCK_SO_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga091f558e4c5c15e615281ba21feb130f)
- [ZSOCK_SCM_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf965ab6d61f7252b4c6b0750d47d6c5c)
- [ZSOCK_SOF_TIMESTAMPING_RX_HARDWARE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf851a5752668188d6c9d66f6d349377a)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [ZSOCK_SOF_TIMESTAMPING_TX_HARDWARE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gafe8cfcce94475fa2dcc2d0e56d6a7134)
- [ZSOCK_TCP_NODELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaed65035762b59c3717cdc856a15f92fa)
- [ZSOCK_TCP_KEEPIDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga720e01b6ceaff867dd673cdd8b648bf2)
- [ZSOCK_TCP_KEEPINTVL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1ebb7dbc45bf6b1b01cb5fe482a3f1b8)
- [ZSOCK_TCP_KEEPCNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga0b29b699728d87c097ff51c95d2f80b1)
- [ZSOCK_UDP_OPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8e63f889afc9ca06bfea2b90e4e88b3e)
- [RFC 9868](https://datatracker.ietf.org/doc/html/rfc9868)
- [ZSOCK_UDP_OPT_OCS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga0394de45aedd088ebcfb11006836572c)
- [ZSOCK_UDP_OPT_APC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1e80d0746eac06c45ef53011cefb9b66)
- [ZSOCK_UDP_OPT_FRAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga44c749f760057277985a91525ad75846)
- [ZSOCK_UDP_OPT_MDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa976bda2ebe370345e7d9324fd0102e1)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [ZSOCK_UDP_OPT_MRDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga023dea5abc5f784df8e988492bc5bfb4)
- [ZSOCK_UDP_OPT_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga62c9b039d368e75991937619e9adf8cc)
- [ZSOCK_UDP_OPT_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaec4348215929b4deff996dcac0ccd5d3)
- [ZSOCK_UDP_OPT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaaf3a09237d37bb112ee72504d926cd89)
- [ZSOCK_UDP_OPT_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac336fbf99b335b69a05004b6ca6a0104)
- [ZSOCK_UDP_OPT_EXP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga92c67eface4732a6b8faf182fc91dfcb)
- [ZSOCK_UDP_OPT_UCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf0ea7830aa95f7fe5c88bbc6b11f9627)
- [ZSOCK_UDP_OPT_UENC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf95d8f076a0d4232992aea0f2545b65f)
- [ZSOCK_UDP_OPT_UEXP](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga3d3737422eb33cf98300e18c5e24a214)
- [ZSOCK_UDP_OPT_DPLPMTUD](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga989a840540b557473a4a4438915f59de)
- [RFC 9869](https://datatracker.ietf.org/doc/html/rfc9869)
- [ZSOCK_UDP_OPT_DPLPMTUD_APP_RESPOND](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5cd27e199f4507097b9ab2f74ba88c10)
- [ZSOCK_UDP_OPT_CMSG_APC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga86605887c247cf1a11701c5675c7895d)
- [ZSOCK_UDP_OPT_CMSG_MDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga473e4bab8f40c07e7bfc618f256868eb)
- [ZSOCK_UDP_OPT_CMSG_MRDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2e00bde85be42b224689e67b9519ba91)
- [ZSOCK_UDP_OPT_CMSG_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga663d30569b681b857b2d3da8c9c5975a)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ZSOCK_UDP_OPT_CMSG_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga4cea51ab6931e1020694569edaedb78b)
- [ZSOCK_UDP_OPT_CMSG_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga0cde876903364ec01f633a1b973f0e6e)
- [ZSOCK_IP_TOS](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gad86db5ae0a9b9a971cb5ec75532595f9)
- [ZSOCK_IP_TTL](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga87e8da2dafd3794240c5e1cdb2ef39fc)
- [ZSOCK_IP_PKTINFO](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga19b4e323fdbc59c7d8853658b4e15e16)
- [ZSOCK_IP_RECVTTL](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga32348af8cfe5540ffc85a70c642fb3e4)
- [ZSOCK_IP_MTU](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gaea02e9ad4ca5347a7026388f0009e730)
- [ZSOCK_IP_DONTFRAG](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga3c8f7f8895a3daae11dcd439eb2499a3)
- [ZSOCK_IP_MULTICAST_IF](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gaa14b3e744b44603a2aa520cacbeef95b)
- [ZSOCK_IP_MULTICAST_TTL](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gab94fd2f344c2c3f1462ccec2f876b8f2)
- [ZSOCK_IP_MULTICAST_LOOP](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gaf5c2aec9a1fcaf0515ccd7d1d5b57cb2)
- [ZSOCK_IP_ADD_MEMBERSHIP](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga9bd617872815d3752e9464f98d32e1ce)
- [ZSOCK_IP_DROP_MEMBERSHIP](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#ga5bf7c18d0400ee370db3bfeab812598a)
- [ZSOCK_IP_LOCAL_PORT_RANGE](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md#gaceaecf7f826715aab2740c57c6ec6407)
- [ZSOCK_IPV6_UNICAST_HOPS](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga6b3364d4ea2e4c34f1de975e6f66961b)
- [ZSOCK_IPV6_MULTICAST_IF](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga4f15d7b5032536896c0785f16830329d)
- [ZSOCK_IPV6_MULTICAST_HOPS](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga78bda8f2e2c0e0fc3cf9788c42d8b6f8)
- [ZSOCK_IPV6_MULTICAST_LOOP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga6fc007f21de54e12697a21712ca095c3)
- [ZSOCK_IPV6_ADD_MEMBERSHIP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gae438698778cfe58c28c7928f9b227f30)
- [ZSOCK_IPV6_DROP_MEMBERSHIP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga1d70e019e1341a3d54dfd7a819cb7071)
- [ZSOCK_IPV6_JOIN_GROUP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gab524aa153b4a7005f988d7bb167bacab)
- [ZSOCK_IPV6_LEAVE_GROUP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga1b2fc808d5b602e658d88d66f1f1d1d1)
- [ZSOCK_IPV6_MTU](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gac37821fc6bd4b484ff36a00dea505245)
- [getsockopt()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)
- [ZSOCK_IPV6_DONTFRAG](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga44b16e54bc2922153e9a07d628cf1cba)
- [ZSOCK_IPV6_V6ONLY](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga004e5f8352ae9c6d8096919e44fdd874)
- [ZSOCK_IPV6_RECVPKTINFO](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gab399d0b2da77aa4331490bb312aa2fb0)
- [ZSOCK_IPV6_PKTINFO](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga24b054ba13a54ae2064aea31f52d7ed0)
- [ZSOCK_IPV6_RECVHOPLIMIT](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gad0c689068bc6bff4369a1ea9b36d09a9)
- [ZSOCK_IPV6_HOPLIMIT](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga92c73652d38a41b8acea0a69362f3e0d)
- [ZSOCK_IPV6_ADDR_PREFERENCES](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga6fd9aed65cb7a1a7eface8455501212b)
- [ZSOCK_IPV6_PREFER_SRC_TMP](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga061badf1fcadf353667f10a64b77bcb5)
- [ZSOCK_IPV6_PREFER_SRC_PUBLIC](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga3acbfad85a26f4a71b51e570369122a4)
- [ZSOCK_IPV6_PREFER_SRC_PUBTMP_DEFAULT](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga2ecb5f065f2f8806ff7ee680ce3b8bee)
- [ZSOCK_IPV6_PREFER_SRC_COA](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#ga60f0a56613fdf6532dd2549273f6e6a2)
- [ZSOCK_IPV6_PREFER_SRC_HOME](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gac9afff595eac9ca47c0e14da20531d6b)
- [ZSOCK_IPV6_PREFER_SRC_CGA](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gaa3b4dd46e7b1fdeaae6db4a692c7f57a)
- [ZSOCK_IPV6_PREFER_SRC_NONCGA](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gaa10785a8136550462a895621b2866d0f)
- [ZSOCK_IPV6_TCLASS](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md#gabe60a1f3a16e4b0a4b2c997f91497c62)
- [ZSOCK_SOMAXCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga95372181a0f868383e6631de84145e39)
- [ZSOCK_IN6_IS_ADDR_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga3ff22595e17c630cf07d40a5e178ecce)
- [ZSOCK_IN6_IS_ADDR_LOOPBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac92eaa41e32e464249bf703d16f869b4)
- [ZSOCK_IN6_IS_ADDR_MULTICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac8fceb6a75060068126f4a4ea5b24fb9)
- [ZSOCK_IN6_IS_ADDR_LINKLOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa2ea2ea293a83c2b3c4851ce517d38bf)
- [ZSOCK_IN6_IS_ADDR_SITELOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga91dc0bd2f4fb09cefad741ee0b1e2c20)
- [ZSOCK_IN6_IS_ADDR_V4MAPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga11df060795e7146f2294ef50d4832cfa)
- [ZSOCK_IN6_IS_ADDR_MC_GLOBAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga42c8ad2a3bb2c223148ab4155be091a2)
- [ZSOCK_IN6_IS_ADDR_MC_NODELOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga106dff01f87ce99d72d54048f837fbdb)
- [ZSOCK_IN6_IS_ADDR_MC_LINKLOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga00067e1cde69c9ae9ad71f0356314964)
- [ZSOCK_IN6_IS_ADDR_MC_SITELOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga76114e85298c02cb5cb37e6a8d9ad566)
- [ZSOCK_IN6_IS_ADDR_MC_ORGLOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae0982428d5720288e7273d442d07d035)
- [ZSOCK_SOL_PACKET](../api_extension_topic_reference/P022_分组套接字的套接字选项（Socket options for packet socket）.md#ga64d5f1636f942f9ff1f02d9918482931)
- [ZSOCK_PACKET_ADD_MEMBERSHIP](../api_extension_topic_reference/P022_分组套接字的套接字选项（Socket options for packet socket）.md#ga9674edba4b48e4cc2d1e01a101cead9b)
- [ZSOCK_PACKET_DROP_MEMBERSHIP](../api_extension_topic_reference/P022_分组套接字的套接字选项（Socket options for packet socket）.md#ga59b254e51063accfb18916b17373d2f6)
- [zsock_get_context_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga21a871d1fa6b6beeed88408761877873)
- [zsock_socket](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5693d19a0bdff45a5cb09227683d8631)
- [zsock_socketpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1f5e089c9fb39d3a8884502a11e389b3)
- [zsock_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae60d7ca486955dd79a2821d1f646c349)
- [zsock_shutdown](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gac56432bf901efaf8ef782430ac143f03)
- [zsock_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga70909e3233d6523d0ad9566b5edd117c)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [zsock_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad858da9650c1270faf5229e3888d7db1)
- [zsock_listen](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae8ea59ea82063aa28a9b72da2f08c9fd)
- [zsock_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1532a65955c402cbb365becb58167f19)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [zsock_sendto](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga9f4ff3d1637393cbe74bd111cc6f432a)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zsock_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2d8c2173986f67dde6dc5721bf690855)
- [zsock_sendmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad3274fe71d43caf8c4d92fffb589375e)
- [net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)
- [zsock_recvfrom](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga89271d76123b0a69e0c40ae4de58bd0a)
- [zsock_recvmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga02b0de9a15c2d1133b87216d6afc203f)
- [zsock_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8a7d82cfb02a45de59ccd05614eb78d6)
- [zsock_fcntl_impl](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gab069dc3ebc140af65801a73fcac4f629)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [zsock_ioctl_impl](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga0255a43336642aaeeaa5bff4c29c9389)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [zsock_poll](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga518361903c9fac3766164d38243872e3)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [zsock_getsockopt](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6aa12f0dbed8ded425555debba044a98)
- [zsock_setsockopt](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga71ac8d52c87b9182a9f1a03614e3dba7)
- [zsock_getpeername](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga78b0ca26c0aaf5e64b05da8caa8c253c)
- [zsock_getsockname](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6bf17561e03600ed870dff702b513d9c)
- [zsock_gethostname](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8b348d886f1bc4f4cdf6e2260844f6e1)
- [zsock_inet_ntop](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad3dbb44d7b49249c124e41041aca6536)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [zsock_inet_pton](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf0130ad342c6873d68bdc51d9cf1167b)
- [zsock_getaddrinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaf59c97c9bd07f188e3f06b2372ac1856)
- [zsock_freeaddrinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga7953da2e52bcfad51b877de6d7fd6cc9)
- [zsock_gai_strerror](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gaa9d9e97c347b3854dc73d7ba33d8ca4b)
- [zsock_send_all](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga8a8e90b68fb77179677f237bc22289ec)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [zsock_sendmsg_all](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga4d2d0823ad8785ffdc2ae327e8651d3f)

<a id="header-details"></a>

---

[上一章](P008_zephyr__display__mipi_display.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__net__net_ip.h_文件参考.md)
