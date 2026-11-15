---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-14
title: TLS 套接字选项（Socket options）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__secure__sockets__options.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_TLS 套接字选项（Socket options）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__secure__sockets__options.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 1.13 引入，版本 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_zsock_5Ftls_5Fcert_5Fverify_5Fcb"></a>

```c
struct zsock_tls_cert_verify_cb
```

相关声明：[zsock_tls_cert_verify_cb](../posix_system_model_reference/P031_zsock_tls_cert_verify_cb_结构体.md)。

ZSOCK_TLS_CERT_VERIFY_CALLBACK套接字选项的数据结构。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 14.2\_TLS 套接字选项（Socket options）

<a id="r_ga7209d2f574caf7bf18dfc135b1e89c33"></a>

```c
#define ZSOCK_SOL_TLS 282
```

相关声明：[ZSOCK_SOL_TLS](#ga7209d2f574caf7bf18dfc135b1e89c33)。

传输层安全（TLS）的协议层级（Protocol Level）。

<a id="r_ga7e47484ee379d42f1d90d652796f0406"></a>

```c
#define ZSOCK_TLS_SEC_TAG_LIST 1
```

相关声明：[ZSOCK_TLS_SEC_TAG_LIST](#ga7e47484ee379d42f1d90d652796f0406)。

用于选择 TLS 凭据（TLS Credentials）的套接字选项（Socket Option）。

<a id="r_ga46e839d445926ba59de5da0edf0f2507"></a>

```c
#define ZSOCK_TLS_HOSTNAME 2
```

相关声明：[ZSOCK_TLS_HOSTNAME](#ga46e839d445926ba59de5da0edf0f2507)。

用于设置主机名（Hostname）的只写套接字选项（Write-only Socket Option）。

<a id="r_ga93b27c4d4ed48976d1b8d8307e753d3f"></a>

```c
#define ZSOCK_TLS_CIPHERSUITE_LIST 3
```

相关声明：[ZSOCK_TLS_CIPHERSUITE_LIST](#ga93b27c4d4ed48976d1b8d8307e753d3f)。

用于选择密码套件（Ciphersuites）的套接字选项（Socket Option）。

<a id="r_gae186f97c3783a29ad4c3df7dd566da95"></a>

```c
#define ZSOCK_TLS_CIPHERSUITE_USED 4
```

相关声明：[ZSOCK_TLS_CIPHERSUITE_USED](#gae186f97c3783a29ad4c3df7dd566da95)。

用于读取 TLS 握手（Handshake）期间选定密码套件（Ciphersuite）的只读套接字选项。

<a id="r_gac02711515e3bdfabe41061cfc65f5c67"></a>

```c
#define ZSOCK_TLS_PEER_VERIFY 5
```

相关声明：[ZSOCK_TLS_PEER_VERIFY](#gac02711515e3bdfabe41061cfc65f5c67)。

用于设置 TLS 连接对端验证等级（Peer Verification Level）的只写套接字选项。

<a id="r_ga7f7a51d68a1901948696d597f0548488"></a>

```c
#define ZSOCK_TLS_DTLS_ROLE 6
```

相关声明：[ZSOCK_TLS_DTLS_ROLE](#ga7f7a51d68a1901948696d597f0548488)。

用于设置数据报传输层安全（DTLS）连接角色（Role）的只写套接字选项。

<a id="r_ga21e38f62fbd83c39a71aec844445a101"></a>

```c
#define ZSOCK_TLS_ALPN_LIST 7
```

相关声明：[ZSOCK_TLS_ALPN_LIST](#ga21e38f62fbd83c39a71aec844445a101)。

用于设置所支持应用层协议（Application Layer Protocols）的套接字选项。

<a id="r_gaa480277784420697eeebbbd71043404a"></a>

```c
#define ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MIN 8
```

相关声明：[ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MIN](#gaa480277784420697eeebbbd71043404a)。

用于设置 DTLS 最小握手超时时间（Min Handshake Timeout）的套接字选项。

<a id="r_gaea9de0d195605882ab6e94cf2ea13907"></a>

```c
#define ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MAX 9
```

相关声明：[ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MAX](#gaea9de0d195605882ab6e94cf2ea13907)。

用于设置 DTLS 最大握手超时时间（Max Handshake Timeout）的套接字选项。

<a id="r_gac976e4d41ca9ef41debb4c997b28b43a"></a>

```c
#define ZSOCK_TLS_CERT_NOCOPY 10
```

相关声明：[ZSOCK_TLS_CERT_NOCOPY](#gac976e4d41ca9ef41debb4c997b28b43a)。

在可能的情况下阻止将证书（Certificates）复制到 Mbed TLS 堆中的套接字选项。

<a id="r_gab446ab6448359979f2d5e895729be993"></a>

```c
#define ZSOCK_TLS_NATIVE 11
```

相关声明：[ZSOCK_TLS_NATIVE](#gab446ab6448359979f2d5e895729be993)。

与卸载（Offloading）配合使用的 TLS 套接字选项。

<a id="r_gacc4c3078ac3169958739ae3425f90a94"></a>

```c
#define ZSOCK_TLS_SESSION_CACHE 12
```

相关声明：[ZSOCK_TLS_SESSION_CACHE](#gacc4c3078ac3169958739ae3425f90a94)。

控制套接字上 TLS 会话缓存（Session Caching）的套接字选项。

<a id="r_gaf1ad38710d9131206f80d9bd8ea7e66f"></a>

```c
#define ZSOCK_TLS_SESSION_CACHE_PURGE 13
```

相关声明：[ZSOCK_TLS_SESSION_CACHE_PURGE](#gaf1ad38710d9131206f80d9bd8ea7e66f)。

立即清除会话缓存（Session Cache）的只写套接字选项。

<a id="r_gaf57ee9894cc4bb7f3fa88e08f7842aa1"></a>

```c
#define ZSOCK_TLS_DTLS_CID 14
```

相关声明：[ZSOCK_TLS_DTLS_CID](#gaf57ee9894cc4bb7f3fa88e08f7842aa1)。

控制 DTLS 连接 ID（CID）的只写套接字选项。

<a id="r_ga7158a9a83f566702be6611866123a0f3"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS 15
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS](#ga7158a9a83f566702be6611866123a0f3)。

获取 DTLS 连接 ID 状态（CID Status）的只读套接字选项。

<a id="r_gac98e03783df8195b76725f8f31fefa1e"></a>

```c
#define ZSOCK_TLS_DTLS_CID_VALUE 16
```

相关声明：[ZSOCK_TLS_DTLS_CID_VALUE](#gac98e03783df8195b76725f8f31fefa1e)。

设置或获取 DTLS 会话所使用连接 ID（Connection ID）值的套接字选项。

<a id="r_ga58b97b28c49ee9dca9b8e80f934b4796"></a>

```c
#define ZSOCK_TLS_DTLS_PEER_CID_VALUE 17
```

相关声明：[ZSOCK_TLS_DTLS_PEER_CID_VALUE](#ga58b97b28c49ee9dca9b8e80f934b4796)。

获取从对端接收的 DTLS 连接 ID（Connection ID）值的只读套接字选项。

<a id="r_gaa6198fcf99c8bc37699655a9f34cbfb3"></a>

```c
#define ZSOCK_TLS_DTLS_HANDSHAKE_ON_CONNECT 18
```

相关声明：[ZSOCK_TLS_DTLS_HANDSHAKE_ON_CONNECT](#gaa6198fcf99c8bc37699655a9f34cbfb3)。

配置 DTLS 套接字在 connect() 时行为的套接字选项。

<a id="r_ga1aaed12ee67d524fd97b7f129b89c70e"></a>

```c
#define ZSOCK_TLS_CERT_VERIFY_RESULT 19
```

相关声明：[ZSOCK_TLS_CERT_VERIFY_RESULT](#ga1aaed12ee67d524fd97b7f129b89c70e)。

在套接字设置了 TLS_PEER_VERIFY_OPTIONAL 时，获取最近一次握手的证书验证结果（Certificate Verification Result）的只读套接字选项。

<a id="r_ga4425112197a30ca359c57de0e824f0d1"></a>

```c
#define ZSOCK_TLS_CERT_VERIFY_CALLBACK 20
```

相关声明：[ZSOCK_TLS_CERT_VERIFY_CALLBACK](#ga4425112197a30ca359c57de0e824f0d1)。

为套接字配置证书验证回调（Certificate Verification Callback）的只写套接字选项。

<a id="r_ga2a4337feada2ae7415dc095e8cd03c7b"></a>

```c
#define ZSOCK_TLS_MAX_FRAGMENT_LENGTH 21
```

相关声明：[ZSOCK_TLS_MAX_FRAGMENT_LENGTH](#ga2a4337feada2ae7415dc095e8cd03c7b)。

为 TLS 1.2 配置每个套接字最大分片长度（Max Fragment Length，MFL）的只写套接字选项。

<a id="r_gaa6b53c582059322fb2abc1aaab4ee989"></a>

```c
#define ZSOCK_TLS_MFL_DEFAULT -1
```

相关声明：[ZSOCK_TLS_MFL_DEFAULT](#gaa6b53c582059322fb2abc1aaab4ee989)。

使用根据全局 Kconfig 配置推导的最大分片长度（MFL）。

<a id="r_ga4428a55bc1b2c3598fbefd551126f342"></a>

```c
#define ZSOCK_TLS_MFL_DISABLED 0
```

相关声明：[ZSOCK_TLS_MFL_DISABLED](#ga4428a55bc1b2c3598fbefd551126f342)。

不发送最大分片长度扩展（MFL Extension）。

<a id="r_ga373ff68ef9c42deff07140c42ea63c0a"></a>

```c
#define ZSOCK_TLS_MFL_512 1
```

相关声明：[ZSOCK_TLS_MFL_512](#ga373ff68ef9c42deff07140c42ea63c0a)。

通告最大分片（Max Fragment）为 512 字节。

<a id="r_ga6480b3675b8ec9c39af42208775bc8e9"></a>

```c
#define ZSOCK_TLS_MFL_1024 2
```

相关声明：[ZSOCK_TLS_MFL_1024](#ga6480b3675b8ec9c39af42208775bc8e9)。

通告最大分片（Max Fragment）为 1024 字节。

<a id="r_ga25fb9c75cca8c77db2a492ef11f3164a"></a>

```c
#define ZSOCK_TLS_MFL_2048 3
```

相关声明：[ZSOCK_TLS_MFL_2048](#ga25fb9c75cca8c77db2a492ef11f3164a)。

通告最大分片（Max Fragment）为 2048 字节。

<a id="r_gaa5df8ff4408d6e3b62c47e0838d481a2"></a>

```c
#define ZSOCK_TLS_MFL_4096 4
```

相关声明：[ZSOCK_TLS_MFL_4096](#gaa5df8ff4408d6e3b62c47e0838d481a2)。

通告最大分片（Max Fragment）为 4096 字节。

<a id="r_ga8341e61b00eda2e56deac47e53e96da2"></a>

```c
#define ZSOCK_TLS_PEER_VERIFY_NONE 0
```

相关声明：[ZSOCK_TLS_PEER_VERIFY_NONE](#ga8341e61b00eda2e56deac47e53e96da2)。

禁用对端验证（Peer Verification Disabled）。

<a id="r_gaef97aaad3f4a97a2954e8aad1fd7857e"></a>

```c
#define ZSOCK_TLS_PEER_VERIFY_OPTIONAL 1
```

相关声明：[ZSOCK_TLS_PEER_VERIFY_OPTIONAL](#gaef97aaad3f4a97a2954e8aad1fd7857e)。

对端验证可选（Peer Verification Optional）。

<a id="r_gab9a4437457cdf80141d4567cef754a7a"></a>

```c
#define ZSOCK_TLS_PEER_VERIFY_REQUIRED 2
```

相关声明：[ZSOCK_TLS_PEER_VERIFY_REQUIRED](#gab9a4437457cdf80141d4567cef754a7a)。

必须验证对端（Peer Verification Required）。

<a id="r_ga3b96ba39bdcb5b0682e13a6ff421780c"></a>

```c
#define ZSOCK_TLS_DTLS_ROLE_CLIENT 0
```

相关声明：[ZSOCK_TLS_DTLS_ROLE_CLIENT](#ga3b96ba39bdcb5b0682e13a6ff421780c)。

DTLS 会话中的客户端角色（Client Role）。

<a id="r_gadeff0aead8c8aa093418fbeb759ad59a"></a>

```c
#define ZSOCK_TLS_DTLS_ROLE_SERVER 1
```

相关声明：[ZSOCK_TLS_DTLS_ROLE_SERVER](#gadeff0aead8c8aa093418fbeb759ad59a)。

DTLS 会话中的服务器角色（Server Role）。

<a id="r_gaf774285e3c5459c25098c5e371299c02"></a>

```c
#define ZSOCK_TLS_CERT_NOCOPY_NONE 0
```

相关声明：[ZSOCK_TLS_CERT_NOCOPY_NONE](#gaf774285e3c5459c25098c5e371299c02)。

在堆中复制证书（Certificate Duplicated in Heap）。

<a id="r_ga3c08db9b4bb990f127f42cccbe049b58"></a>

```c
#define ZSOCK_TLS_CERT_NOCOPY_OPTIONAL 1
```

相关声明：[ZSOCK_TLS_CERT_NOCOPY_OPTIONAL](#ga3c08db9b4bb990f127f42cccbe049b58)。

若证书为 DER 格式，则不在堆中复制。

<a id="r_gaf66290b67a7deee2847c9a7301df177d"></a>

```c
#define ZSOCK_TLS_SESSION_CACHE_DISABLED 0
```

相关声明：[ZSOCK_TLS_SESSION_CACHE_DISABLED](#gaf66290b67a7deee2847c9a7301df177d)。

禁用 TLS 会话缓存（Session Caching）。

<a id="r_ga92cc4f8261b5d669cc3032d4b0e0a76a"></a>

```c
#define ZSOCK_TLS_SESSION_CACHE_ENABLED 1
```

相关声明：[ZSOCK_TLS_SESSION_CACHE_ENABLED](#ga92cc4f8261b5d669cc3032d4b0e0a76a)。

启用 TLS 会话缓存（Session Caching）。

<a id="r_ga701820487b6651e16319235c43ade526"></a>

```c
#define ZSOCK_TLS_DTLS_CID_DISABLED 0
```

相关声明：[ZSOCK_TLS_DTLS_CID_DISABLED](#ga701820487b6651e16319235c43ade526)。

连接 ID（CID）已禁用。

<a id="r_ga5037d23a87ce456873b68c3712d00177"></a>

```c
#define ZSOCK_TLS_DTLS_CID_SUPPORTED 1
```

相关声明：[ZSOCK_TLS_DTLS_CID_SUPPORTED](#ga5037d23a87ce456873b68c3712d00177)。

支持连接 ID（CID）。

<a id="r_gae53fd78b605b6c65f164f449146d369e"></a>

```c
#define ZSOCK_TLS_DTLS_CID_ENABLED 2
```

相关声明：[ZSOCK_TLS_DTLS_CID_ENABLED](#gae53fd78b605b6c65f164f449146d369e)。

连接 ID（CID）已启用。

<a id="r_gadbe80ee9dcc81383086f99da6f7d6468"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_DISABLED 0
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS_DISABLED](#gadbe80ee9dcc81383086f99da6f7d6468)。

连接 ID（CID）已禁用。

<a id="r_ga307213073d76058f6a276dd7493e2bd2"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_DOWNLINK 1
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS_DOWNLINK](#ga307213073d76058f6a276dd7493e2bd2)。

本端正在使用连接 ID（CID）。

<a id="r_ga14275c57f01cb81292049aabe468ec3f"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_UPLINK 2
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS_UPLINK](#ga14275c57f01cb81292049aabe468ec3f)。

对端正在使用连接 ID（CID）。

<a id="r_ga46da3503cbb491f471121cd50a342b03"></a>

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_BIDIRECTIONAL 3
```

相关声明：[ZSOCK_TLS_DTLS_CID_STATUS_BIDIRECTIONAL](#ga46da3503cbb491f471121cd50a342b03)。

本端与对端均在使用连接 ID（CID）。

## 14.3\_详细说明（Detailed Documentation）

<a id="ga7209d2f574caf7bf18dfc135b1e89c33"></a>

### `ZSOCK_SOL_TLS`

```c
#define ZSOCK_SOL_TLS 282
```

```c
#include <zephyr/net/socket.h>
```

传输层安全（TLS）的协议层级（Protocol Level）。

此处采用与 Linux 相同的 TLS 套接字协议层级（Socket Protocol Level）。

<a id="ga21e38f62fbd83c39a71aec844445a101"></a>

### `ZSOCK_TLS_ALPN_LIST`

```c
#define ZSOCK_TLS_ALPN_LIST 7
```

```c
#include <zephyr/net/socket.h>
```

用于设置所支持应用层协议（Application Layer Protocols）的套接字选项。

接受并返回由 NULL 结尾字符串组成的 const char 数组，表示 TLS 握手期间列出的受支持应用层协议（Application Layer Protocols）。

<a id="gac976e4d41ca9ef41debb4c997b28b43a"></a>

### `ZSOCK_TLS_CERT_NOCOPY`

```c
#define ZSOCK_TLS_CERT_NOCOPY 10
```

```c
#include <zephyr/net/socket.h>
```

在可能的情况下阻止将证书（Certificates）复制到 Mbed TLS 堆中的套接字选项。

此选项仅对 DER 证书有效，对于 PEM 证书会被忽略。

<a id="gaf774285e3c5459c25098c5e371299c02"></a>

### `ZSOCK_TLS_CERT_NOCOPY_NONE`

```c
#define ZSOCK_TLS_CERT_NOCOPY_NONE 0
```

```c
#include <zephyr/net/socket.h>
```

在堆中复制证书（Certificate Duplicated in Heap）。

<a id="ga3c08db9b4bb990f127f42cccbe049b58"></a>

### `ZSOCK_TLS_CERT_NOCOPY_OPTIONAL`

```c
#define ZSOCK_TLS_CERT_NOCOPY_OPTIONAL 1
```

```c
#include <zephyr/net/socket.h>
```

若证书为 DER 格式，则不在堆中复制。

<a id="ga4425112197a30ca359c57de0e824f0d1"></a>

### `ZSOCK_TLS_CERT_VERIFY_CALLBACK`

```c
#define ZSOCK_TLS_CERT_VERIFY_CALLBACK 20
```

```c
#include <zephyr/net/socket.h>
```

为套接字配置证书验证回调（Certificate Verification Callback）的只写套接字选项。

此选项接受指向 zsock_tls_cert_verify_cb 结构体的指针；结构体包含实际回调函数指针和应用定义的上下文（Context）指针。

设置后，证书验证（Certificate Verification）委托给注册的回调。此时应用负责验证所提供证书，并决定继续还是中止握手（Handshake）。

仅在启用 CONFIG_NET_SOCKETS_TLS_CERT_VERIFY_CALLBACK Kconfig 选项时可用。

<a id="ga1aaed12ee67d524fd97b7f129b89c70e"></a>

### `ZSOCK_TLS_CERT_VERIFY_RESULT`

```c
#define ZSOCK_TLS_CERT_VERIFY_RESULT 19
```

```c
#include <zephyr/net/socket.h>
```

在套接字设置了 TLS_PEER_VERIFY_OPTIONAL 时，获取最近一次握手的证书验证结果（Certificate Verification Result）的只读套接字选项。

此选项接受指向 32 位无符号整数的指针，返回时该整数保存验证结果（Verification Result）。0 表示验证成功，否则以一组标志表示结果。对于 Mbed TLS 后端，标志定义在 x509.h 头文件的 “X509 Verify codes” 部分。

<a id="ga93b27c4d4ed48976d1b8d8307e753d3f"></a>

### `ZSOCK_TLS_CIPHERSUITE_LIST`

```c
#define ZSOCK_TLS_CIPHERSUITE_LIST 3
```

```c
#include <zephyr/net/socket.h>
```

用于选择密码套件（Ciphersuites）的套接字选项（Socket Option）。

接受并返回由 IANA 分配的密码套件标识符（Ciphersuite Identifiers）构成的整数数组。未设置时，套接字允许系统中所有可用密码套件，这是 Mbed TLS 的默认行为。

<a id="gae186f97c3783a29ad4c3df7dd566da95"></a>

### `ZSOCK_TLS_CIPHERSUITE_USED`

```c
#define ZSOCK_TLS_CIPHERSUITE_USED 4
```

```c
#include <zephyr/net/socket.h>
```

用于读取 TLS 握手（Handshake）期间选定密码套件（Ciphersuite）的只读套接字选项。

返回一个整数，其中包含选定密码套件的 IANA 分配标识符（IANA Assigned Ciphersuite Identifier）。

<a id="gaf57ee9894cc4bb7f3fa88e08f7842aa1"></a>

### `ZSOCK_TLS_DTLS_CID`

```c
#define ZSOCK_TLS_DTLS_CID 14
```

```c
#include <zephyr/net/socket.h>
```

控制 DTLS 连接 ID（CID）的只写套接字选项。

此选项接受表示设置的整数，允许值为 0、1 和 2。在套接字连接前设置才有效。

- 0：禁用 DTLS 连接 ID（CID）。
- 1：启用 DTLS 连接 ID（CID），向对端发送长度为 0 的 CID 值。
- 2：启用 DTLS 连接 ID（CID），向对端发送最近通过 TLS_DTLS_CID_VALUE 设置的值；没有设置时使用随机值。

<a id="ga701820487b6651e16319235c43ade526"></a>

### `ZSOCK_TLS_DTLS_CID_DISABLED`

```c
#define ZSOCK_TLS_DTLS_CID_DISABLED 0
```

```c
#include <zephyr/net/socket.h>
```

连接 ID（CID）已禁用。

<a id="gae53fd78b605b6c65f164f449146d369e"></a>

### `ZSOCK_TLS_DTLS_CID_ENABLED`

```c
#define ZSOCK_TLS_DTLS_CID_ENABLED 2
```

```c
#include <zephyr/net/socket.h>
```

连接 ID（CID）已启用。

<a id="ga7158a9a83f566702be6611866123a0f3"></a>

### `ZSOCK_TLS_DTLS_CID_STATUS`

```c
#define ZSOCK_TLS_DTLS_CID_STATUS 15
```

```c
#include <zephyr/net/socket.h>
```

获取 DTLS 连接 ID 状态（CID Status）的只读套接字选项。

此选项接受指向整数的指针，返回时该整数表示设置。可能返回的值为：

- 0：DTLS 连接 ID（CID）已禁用。
- 1：在下行方向（Downlink）接收连接 ID（CID）。
- 2：在上行方向（Uplink）发送连接 ID（CID）。
- 3：双向使用连接 ID（CID）。

<a id="ga46da3503cbb491f471121cd50a342b03"></a>

### `ZSOCK_TLS_DTLS_CID_STATUS_BIDIRECTIONAL`

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_BIDIRECTIONAL 3
```

```c
#include <zephyr/net/socket.h>
```

本端与对端均在使用连接 ID（CID）。

<a id="gadbe80ee9dcc81383086f99da6f7d6468"></a>

### `ZSOCK_TLS_DTLS_CID_STATUS_DISABLED`

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_DISABLED 0
```

```c
#include <zephyr/net/socket.h>
```

连接 ID（CID）已禁用。

<a id="ga307213073d76058f6a276dd7493e2bd2"></a>

### `ZSOCK_TLS_DTLS_CID_STATUS_DOWNLINK`

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_DOWNLINK 1
```

```c
#include <zephyr/net/socket.h>
```

本端正在使用连接 ID（CID）。

<a id="ga14275c57f01cb81292049aabe468ec3f"></a>

### `ZSOCK_TLS_DTLS_CID_STATUS_UPLINK`

```c
#define ZSOCK_TLS_DTLS_CID_STATUS_UPLINK 2
```

```c
#include <zephyr/net/socket.h>
```

对端正在使用连接 ID（CID）。

<a id="ga5037d23a87ce456873b68c3712d00177"></a>

### `ZSOCK_TLS_DTLS_CID_SUPPORTED`

```c
#define ZSOCK_TLS_DTLS_CID_SUPPORTED 1
```

```c
#include <zephyr/net/socket.h>
```

支持连接 ID（CID）。

<a id="gac98e03783df8195b76725f8f31fefa1e"></a>

### `ZSOCK_TLS_DTLS_CID_VALUE`

```c
#define ZSOCK_TLS_DTLS_CID_VALUE 16
```

```c
#include <zephyr/net/socket.h>
```

设置或获取 DTLS 会话所使用连接 ID（Connection ID）值的套接字选项。

此选项接受保存连接 ID（CID）值的字节数组。

<a id="gaa6198fcf99c8bc37699655a9f34cbfb3"></a>

### `ZSOCK_TLS_DTLS_HANDSHAKE_ON_CONNECT`

```c
#define ZSOCK_TLS_DTLS_HANDSHAKE_ON_CONNECT 18
```

```c
#include <zephyr/net/socket.h>
```

配置 DTLS 套接字在 connect() 时行为的套接字选项。

设置后，DTLS connect() 会与配置的对端执行握手（Handshake），这是默认行为。否则，DTLS connect() 只配置对端地址，与普通 UDP 套接字相同，不尝试执行 DTLS 握手；握手在随后的 send()／recv() 调用中进行。

<a id="gaea9de0d195605882ab6e94cf2ea13907"></a>

### `ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MAX`

```c
#define ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MAX 9
```

```c
#include <zephyr/net/socket.h>
```

用于设置 DTLS 最大握手超时时间（Max Handshake Timeout）的套接字选项。

超时时间（Timeout）从 min 开始，每次重传时加倍，直到达到 max。最小值和最大值是两个独立选项，单位为毫秒。

<a id="gaa480277784420697eeebbbd71043404a"></a>

### `ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MIN`

```c
#define ZSOCK_TLS_DTLS_HANDSHAKE_TIMEOUT_MIN 8
```

```c
#include <zephyr/net/socket.h>
```

用于设置 DTLS 最小握手超时时间（Min Handshake Timeout）的套接字选项。

超时时间（Timeout）从 min 开始，每次重传时加倍，直到达到 max。最小值和最大值是两个独立选项，单位为毫秒。

<a id="ga58b97b28c49ee9dca9b8e80f934b4796"></a>

### `ZSOCK_TLS_DTLS_PEER_CID_VALUE`

```c
#define ZSOCK_TLS_DTLS_PEER_CID_VALUE 17
```

```c
#include <zephyr/net/socket.h>
```

获取从对端接收的 DTLS 连接 ID（Connection ID）值的只读套接字选项。

此选项接受指向字节数组的指针，返回时数组保存连接 ID（CID）值。如果对端未提供连接 ID，返回的 optlen 为 0；否则为 CID 值的长度。

<a id="ga7f7a51d68a1901948696d597f0548488"></a>

### `ZSOCK_TLS_DTLS_ROLE`

```c
#define ZSOCK_TLS_DTLS_ROLE 6
```

```c
#include <zephyr/net/socket.h>
```

用于设置数据报传输层安全（DTLS）连接角色（Role）的只写套接字选项。

此选项与 TLS 连接无关，因为 TLS 根据 connect()／listen() 的使用方式选择角色（Role）。DTLS 默认采用客户端角色。此选项接受一个表示 TLS 角色的整数，取值与 Mbed TLS 兼容：

- 0：客户端（Client）。
- 1：服务器（Server）。

<a id="ga3b96ba39bdcb5b0682e13a6ff421780c"></a>

### `ZSOCK_TLS_DTLS_ROLE_CLIENT`

```c
#define ZSOCK_TLS_DTLS_ROLE_CLIENT 0
```

```c
#include <zephyr/net/socket.h>
```

DTLS 会话中的客户端角色（Client Role）。

<a id="gadeff0aead8c8aa093418fbeb759ad59a"></a>

### `ZSOCK_TLS_DTLS_ROLE_SERVER`

```c
#define ZSOCK_TLS_DTLS_ROLE_SERVER 1
```

```c
#include <zephyr/net/socket.h>
```

DTLS 会话中的服务器角色（Server Role）。

<a id="ga46e839d445926ba59de5da0edf0f2507"></a>

### `ZSOCK_TLS_HOSTNAME`

```c
#define ZSOCK_TLS_HOSTNAME 2
```

```c
#include <zephyr/net/socket.h>
```

用于设置主机名（Hostname）的只写套接字选项（Write-only Socket Option）。

接受包含主机名（Hostname）的字符串；可为 NULL，以禁用主机名验证。TLS 客户端默认强制检查主机名。

<a id="ga2a4337feada2ae7415dc095e8cd03c7b"></a>

### `ZSOCK_TLS_MAX_FRAGMENT_LENGTH`

```c
#define ZSOCK_TLS_MAX_FRAGMENT_LENGTH 21
```

```c
#include <zephyr/net/socket.h>
```

为 TLS 1.2 配置每个套接字最大分片长度（Max Fragment Length，MFL）的只写套接字选项。

设置后，仅为此套接字覆盖根据编译时缓冲区大小推导的全局最大分片长度（MFL）。接受指向 int 的指针，其中保存一个 ZSOCK_TLS_MFL_* 值。

默认情况下，即未设置此选项时，套接字通告根据 CONFIG_MBEDTLS_SSL_IN_CONTENT_LEN／CONFIG_MBEDTLS_SSL_OUT_CONTENT_LEN 推导的最大分片长度（MFL）。此前调用覆盖了该值后，传入 ZSOCK_TLS_MFL_DEFAULT 可恢复此默认行为。

要求启用 CONFIG_NET_SOCKETS_TLS_SET_MAX_FRAGMENT_LENGTH。

<a id="ga6480b3675b8ec9c39af42208775bc8e9"></a>

### `ZSOCK_TLS_MFL_1024`

```c
#define ZSOCK_TLS_MFL_1024 2
```

```c
#include <zephyr/net/socket.h>
```

通告最大分片（Max Fragment）为 1024 字节。

<a id="ga25fb9c75cca8c77db2a492ef11f3164a"></a>

### `ZSOCK_TLS_MFL_2048`

```c
#define ZSOCK_TLS_MFL_2048 3
```

```c
#include <zephyr/net/socket.h>
```

通告最大分片（Max Fragment）为 2048 字节。

<a id="gaa5df8ff4408d6e3b62c47e0838d481a2"></a>

### `ZSOCK_TLS_MFL_4096`

```c
#define ZSOCK_TLS_MFL_4096 4
```

```c
#include <zephyr/net/socket.h>
```

通告最大分片（Max Fragment）为 4096 字节。

<a id="ga373ff68ef9c42deff07140c42ea63c0a"></a>

### `ZSOCK_TLS_MFL_512`

```c
#define ZSOCK_TLS_MFL_512 1
```

```c
#include <zephyr/net/socket.h>
```

通告最大分片（Max Fragment）为 512 字节。

<a id="gaa6b53c582059322fb2abc1aaab4ee989"></a>

### `ZSOCK_TLS_MFL_DEFAULT`

```c
#define ZSOCK_TLS_MFL_DEFAULT -1
```

```c
#include <zephyr/net/socket.h>
```

使用根据全局 Kconfig 配置推导的最大分片长度（MFL）。

<a id="ga4428a55bc1b2c3598fbefd551126f342"></a>

### `ZSOCK_TLS_MFL_DISABLED`

```c
#define ZSOCK_TLS_MFL_DISABLED 0
```

```c
#include <zephyr/net/socket.h>
```

不发送最大分片长度扩展（MFL Extension）。

<a id="gab446ab6448359979f2d5e895729be993"></a>

### `ZSOCK_TLS_NATIVE`

```c
#define ZSOCK_TLS_NATIVE 11
```

```c
#include <zephyr/net/socket.h>
```

与卸载（Offloading）配合使用的 TLS 套接字选项。

此选项指示网络协议栈仅卸载（Offload）底层 TCP／UDP 通信。TLS／DTLS 操作由 Zephyr 原生 TLS／DTLS 套接字实现处理。

注意：只有使用套接字分派器（Socket Dispatcher），即启用 CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER 时，此选项才适用。此时它应是新建套接字设置的第一个选项。随后，应用可使用 SO_BINDTODEVICE 为底层 TCP／UDP 套接字选择专用网络接口。

<a id="gac02711515e3bdfabe41061cfc65f5c67"></a>

### `ZSOCK_TLS_PEER_VERIFY`

```c
#define ZSOCK_TLS_PEER_VERIFY 5
```

```c
#include <zephyr/net/socket.h>
```

用于设置 TLS 连接对端验证等级（Peer Verification Level）的只写套接字选项。

此选项接受一个表示对端验证等级（Peer Verification Level）的整数，取值与 Mbed TLS 兼容：

- 0：不验证（None）。
- 1：可选验证（Optional）。
- 2：必须验证（Required）。

未设置时，套接字使用 Mbed TLS 默认值：服务器不验证，客户端必须验证。

<a id="ga8341e61b00eda2e56deac47e53e96da2"></a>

### `ZSOCK_TLS_PEER_VERIFY_NONE`

```c
#define ZSOCK_TLS_PEER_VERIFY_NONE 0
```

```c
#include <zephyr/net/socket.h>
```

禁用对端验证（Peer Verification Disabled）。

<a id="gaef97aaad3f4a97a2954e8aad1fd7857e"></a>

### `ZSOCK_TLS_PEER_VERIFY_OPTIONAL`

```c
#define ZSOCK_TLS_PEER_VERIFY_OPTIONAL 1
```

```c
#include <zephyr/net/socket.h>
```

对端验证可选（Peer Verification Optional）。

<a id="gab9a4437457cdf80141d4567cef754a7a"></a>

### `ZSOCK_TLS_PEER_VERIFY_REQUIRED`

```c
#define ZSOCK_TLS_PEER_VERIFY_REQUIRED 2
```

```c
#include <zephyr/net/socket.h>
```

必须验证对端（Peer Verification Required）。

<a id="ga7e47484ee379d42f1d90d652796f0406"></a>

### `ZSOCK_TLS_SEC_TAG_LIST`

```c
#define ZSOCK_TLS_SEC_TAG_LIST 1
```

```c
#include <zephyr/net/socket.h>
```

用于选择 TLS 凭据（TLS Credentials）的套接字选项（Socket Option）。

接受并返回 sec_tag_t 数组，指示特定套接字应使用哪些 TLS 凭据（TLS Credentials）。

<a id="gacc4c3078ac3169958739ae3425f90a94"></a>

### `ZSOCK_TLS_SESSION_CACHE`

```c
#define ZSOCK_TLS_SESSION_CACHE 12
```

```c
#include <zephyr/net/socket.h>
```

控制套接字上 TLS 会话缓存（Session Caching）的套接字选项。

接受的值（Accepted Values）：

- 0：禁用（Disabled）。
- 1：启用（Enabled）。

对于 TLS 1.3，收到 NewSessionTicket 报文时缓存会话（Sessions）；该报文在握手完成后到达。应用需要从套接字接收数据或轮询套接字，才能处理并缓存票据（Ticket）。最近收到的票据替换该对端的缓存条目。

<a id="gaf66290b67a7deee2847c9a7301df177d"></a>

### `ZSOCK_TLS_SESSION_CACHE_DISABLED`

```c
#define ZSOCK_TLS_SESSION_CACHE_DISABLED 0
```

```c
#include <zephyr/net/socket.h>
```

禁用 TLS 会话缓存（Session Caching）。

<a id="ga92cc4f8261b5d669cc3032d4b0e0a76a"></a>

### `ZSOCK_TLS_SESSION_CACHE_ENABLED`

```c
#define ZSOCK_TLS_SESSION_CACHE_ENABLED 1
```

```c
#include <zephyr/net/socket.h>
```

启用 TLS 会话缓存（Session Caching）。

<a id="gaf1ad38710d9131206f80d9bd8ea7e66f"></a>

### `ZSOCK_TLS_SESSION_CACHE_PURGE`

```c
#define ZSOCK_TLS_SESSION_CACHE_PURGE 13
```

```c
#include <zephyr/net/socket.h>
```

立即清除会话缓存（Session Cache）的只写套接字选项。

此选项接受任何值（Any Value）。


## 14.4\_原页交叉引用（Cross References）

- [zsock_tls_cert_verify_cb](../posix_system_model_reference/P031_zsock_tls_cert_verify_cb_结构体.md)
- [connect()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [send()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)
- [sec_tag_t](../api_memory_timer_topic_reference/P011_传输层安全（TLS）的凭据管理。.md#gaadfe9694309e473f7be74ed98dfb36d3)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P013_MAX30009 API主题.md) · [返回大纲](大纲.md) · [下一章](P015_SIMCom SIM7080 API主题.md)
