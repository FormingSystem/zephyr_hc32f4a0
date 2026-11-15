---
id: learning.zephyr-docs.networking.page-143
title: QUIC传输接口
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/quic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第143章\_QUIC传输接口

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/quic.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

QUIC 是由 [RFC 9000](https://datatracker.ietf.org/doc/html/rfc9000.html) 标准化的通用多路复用传输协议（Multiplexed Transport Protocol）。它运行于用户数据报协议（User Datagram Protocol，UDP）之上，提供有序、可靠的字节流（Byte Stream）传递，并集成传输层安全协议 TLS 1.3（[RFC 9001](https://datatracker.ietf.org/doc/html/rfc9001.html)）、流多路复用（Stream Multiplexing）和连接迁移（Connection Migration）。Zephyr 通过 [`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC) 提供 QUIC 实现。

与嵌入式使用相关的主要特性如下。

- **流多路复用**：双向流（Bidirectional Stream）和单向流（Unidirectional Stream）共享一个 UDP 套接字，避免传输层的队头阻塞（Head-of-Line Blocking）。
- **集成 TLS 1.3**：握手（Handshake）是连接建立过程的一部分，不需要独立的 TLS 层。
- **流量控制（Flow Control）**：按流和连接分别提供基于额度（Credit）的控制，避免高速发送方压垮资源受限的接收方。
- **丢包恢复（Loss Recovery）**：探测超时（Probe Timeout，PTO）机制重传数据，不依赖 ICMP 或 TCP 式的 ACK 时钟。
- **路径 MTU 发现（Path MTU Discovery）**：数据报分包层路径 MTU 发现（Datagram Packetization Layer PMTU Discovery，DPLPMTUD；RFC 9000 第 14.3 节）在握手后探测路径，只有探测得到确认后才增大发送长度。
- **套接字集成（Socket Integration）**：数据传输使用标准 Zephyr 调用，包括 `zsock_send`、`zsock_recv`、`zsock_recvmsg`、`zsock_sendmsg` 和 `zsock_close`。
- **双协议栈（Dual Stack）**：支持 IPv4 和 IPv6 连接。

> 原文提示：Zephyr 的 QUIC 支持目前属于实验性功能（Experimental）。通过 `CONFIG_QUIC=y` 启用；不同发行版之间的 API 和 Kconfig 选项可能变化。

## 2. 架构与概念（Architecture & Concepts）

使用本库前，应先理解连接（Connection）与流（Stream）的关系。

- **QUIC 连接套接字（QUIC Connection Socket）**表示通往对端的“通道”，负责 TLS 握手、拥塞控制（Congestion Control）和连接终止。通常使用它创建流，而不直接在它上面发送应用数据。
- **QUIC 流套接字（QUIC Stream Socket）**表示连接内部的轻量数据通道，实际应用数据通过它进行 `send` 或 `recv`。

## 3. 应用工作流程（Application Workflow）

### 3.1 客户端应用（Client Application）

客户端连接远程服务器，打开流，发送请求，再读取响应。

**步骤 1：设置地址。**

```c
struct net_sockaddr_in remote_addr = {
    .sin_family = NET_AF_INET,
    .sin_port = net_htons(4422),
};

zsock_inet_pton(NET_AF_INET, "192.0.2.1", &remote_addr.sin_addr);
```

**步骤 2：打开 QUIC 连接。** 首次创建流时会自动进行 TLS 握手。

```c
int conn_sock = quic_connection_open((struct net_sockaddr *)&remote_addr, NULL);
if (conn_sock < 0) {
    /* Handle error */
}

/* The TLS handshake occurs automatically upon the first stream creation. */
```

**步骤 3：打开流。** 这里创建由客户端发起的双向流。

```c
/* Create a bidirectional stream initiated by the client */
int stream_sock = quic_stream_open(conn_sock,
                                   QUIC_STREAM_CLIENT,
                                   QUIC_STREAM_BIDIRECTIONAL,
                                   0);
```

**步骤 4：传输数据。** 在流套接字上调用标准套接字接口。

```c
zsock_send(stream_sock, "Hello Server", 12, 0);

char buffer[64];
zsock_recv(stream_sock, buffer, sizeof(buffer), 0);
```

**步骤 5：清理。**

```c
quic_stream_close(stream_sock);
quic_connection_close(conn_sock);
```

### 3.2 服务端应用（Server Application）

服务端绑定本地端口，等待传入连接，接受流并处理数据。

**步骤 1：绑定连接套接字。**

```c
struct net_sockaddr_in local_addr = {
   .sin_family = NET_AF_INET,
   .sin_port = net_htons(4422),
   .sin_addr.s_addr = NET_INADDR_ANY,
};

/* Create the listening context */
int conn_sock = quic_connection_open(NULL, (struct net_sockaddr *)&local_addr);
```

**步骤 2：接受传入的流。** [`quic_connection_open()`](P147_QUIC完整API参考.md#gac5b95872bf7fa74b7a1d2c7b011fd99f) 创建的套接字作为“父对象”。在连接套接字上调用 [`zsock_accept()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1532a65955c402cbb365becb58167f19)，取得对端发起的新流的文件描述符（File Descriptor）。

```c
struct net_sockaddr_in peer_addr;
net_socklen_t addrlen = sizeof(peer_addr);

/* Block until a client opens a stream */
int stream_sock = zsock_accept(conn_sock, (struct net_sockaddr *)&peer_addr, &addrlen);

if (stream_sock >= 0) {
    /* Handle the new stream (read/write data) */
    char buf[128];
    int len = zsock_recv(stream_sock, buf, sizeof(buf), 0);

    /* Echo back */
    zsock_send(stream_sock, buf, len, 0);

    /* Close the stream when done, also zsock_close() can be used */
    quic_stream_close(stream_sock);
}
```

> 译注——片段边界：以上保留官方流程片段，不是可直接拼接的完整应用。证书和 ALPN 必须按下一节在创建流之前设置；原文 ALPN 片段中的 `quic_sock` 指连接套接字，应与所在应用的 `conn_sock` 对应。实际应用还需检查地址转换、打开、接收和发送的返回值；尤其不能把失败的 `zsock_recv()` 所返回的负数当作发送长度，接收返回 0 以及部分发送也应分别处理。

## 4. TLS 与安全配置（TLS & Security Configuration）

QUIC 传输通过 Mbed TLS 和 PSA API 执行密码操作。证书、密钥等安全凭据（Security Credentials）由 Zephyr TLS 凭据子系统（TLS Credentials Subsystem）管理。

### 4.1 管理证书（Managing Certificates）

打开连接前，必须使用 [`tls_credential_add()`](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga640ff6dd3eb4d5017feaab6fab2bb2f7) 注册证书。

- **证书颁发机构证书（Certificate Authority Certificate，CA Certificate）**：客户端验证服务端时需要。
- **服务端证书与私钥（Server Certificate & Private Key）**：服务端需要。

下面是加载凭据的原文示例；`...` 代表需要提供的 PEM 或 DER 数据。

```c
#include <zephyr/net/tls_credentials.h>

/* Tag ID to reference credentials later */
#define MY_SEC_TAG 1

static const char server_cert[] = ...; /* PEM or DER data */
static const char priv_key[] = ...;    /* PEM or DER data */

void setup_credentials(void) {
    tls_credential_add(MY_SEC_TAG, TLS_CREDENTIAL_PUBLIC_CERTIFICATE,
                       server_cert, sizeof(server_cert));
    tls_credential_add(MY_SEC_TAG, TLS_CREDENTIAL_PRIVATE_KEY,
                       priv_key, sizeof(priv_key));
}
```

### 4.2 将凭据应用于 QUIC（Applying Credentials to QUIC）

创建连接套接字后立即使用 [`zsock_setsockopt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga71ac8d52c87b9182a9f1a03614e3dba7) 为它设置凭据，必须在创建流之前完成。

对端证书验证（Peer Certificate Verification）采用与 Zephyr TLS 套接字相同的默认策略：客户端默认要求验证成功；服务端默认不验证客户端证书，除非显式启用 `ZSOCK_TLS_PEER_VERIFY`。因此，客户端未加载 CA 证书时，默认会握手失败。应用若有意跳过服务端身份验证，必须显式设置 `ZSOCK_TLS_PEER_VERIFY = MBEDTLS_SSL_VERIFY_NONE`。

```c
sec_tag_t sec_tag_list[] = { MY_SEC_TAG };

zsock_setsockopt(conn_sock, ZSOCK_SOL_TLS, ZSOCK_TLS_SEC_TAG_LIST,
                 sec_tag_list, sizeof(sec_tag_list));
```

### 4.3 将 ALPN 应用于 QUIC（Applying ALPN to QUIC）

QUIC 必须使用应用层协议协商（Application-Layer Protocol Negotiation，ALPN），以协商两个 QUIC 端点之上运行的应用协议。创建连接套接字后立即通过 [`zsock_setsockopt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga71ac8d52c87b9182a9f1a03614e3dba7) 设置 ALPN 列表，也必须在创建流之前完成。原文要求列表元素为常量，不能使用变量。

```c
const char * const alpn_list[] = {
    "echo-quic",
    NULL
};

ret = zsock_setsockopt(quic_sock, ZSOCK_SOL_TLS, ZSOCK_TLS_ALPN_LIST,
                            alpn_list, sizeof(alpn_list));
if (ret < 0) {
    LOG_ERR("Failed to set ALPN (%d)", -errno);
}
```

## 5. 会话恢复与 0-RTT（Session Resumption and 0-RTT）

完整握手后，服务端可以签发 TLS 1.3 `NewSessionTicket`。客户端保存产生的会话状态（Session State），在后续连接中提交它，以便不经过完整握手恢复会话；服务端允许时，还可在握手完成前的首轮报文中发送 0-RTT 早期数据（Early Data）。RTT 指往返时间（Round-Trip Time）。

[`CONFIG_QUIC_0RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_0RTT) 控制是否编译 0-RTT 支持，默认关闭。无需启用它即可进行 1-RTT 会话恢复；启用后增加早期数据的提出、接受和重放处理。

> 原文警告：网络攻击者可以重放 0-RTT 早期数据（RFC 9001 第 9.2 节）。只能用 0-RTT 发送幂等（Idempotent）或可安全重放（Replay-Safe）操作的数据，并准备处理对端拒绝早期数据的情况：此时必须在握手完成后重试。协议栈让已签发票据只能使用一次，并设置票据年龄有效窗口，但这些防重放状态仅保存在各实例的内存中，重启后不会保留，也不会在多个服务端实例间共享。

### 5.1 客户端：导出与复用会话状态

握手后，从连接套接字读取并保存可恢复状态。在新连接上，必须在打开第一个流之前导入。启用 0-RTT 后，第一个流的数据会作为早期数据携带。

```c
struct quic_session_state state;
net_socklen_t optlen = sizeof(state);

/* After the first connection's handshake completes: */
zsock_getsockopt(conn_sock, ZSOCK_SOL_QUIC, ZSOCK_QUIC_SO_SESSION_STATE,
                 &state, &optlen);

/* On a later connection, before the first stream is opened: */
zsock_setsockopt(new_conn_sock, ZSOCK_SOL_QUIC, ZSOCK_QUIC_SO_SESSION_STATE,
                 &state, sizeof(state));
```

`struct quic_session_state` 含有会话恢复秘密（Resumption Secret），应作为敏感数据安全保存。其结构布局版本由 `QUIC_SESSION_STATE_VERSION` 标识。

> 译注——导出时机：详细API明确要求客户端已收到 `NewSessionTicket` 后才能导出可恢复状态，仅完成握手并不保证票据已经到达。应检查 `zsock_getsockopt()` 的结果，成功后再保存和复用，见[会话状态参考](P150_QUIC会话状态.md)。

### 5.2 服务端：签发票据与允许 0-RTT

握手前，在监听套接字或服务端连接套接字上设置下列选项。

- `ZSOCK_QUIC_SO_SESSION_TICKET_ENABLE`：传入指向 `int` 的指针。非零值让服务端在握手后发送 `NewSessionTicket`，从而允许 1-RTT 恢复。
- `ZSOCK_QUIC_SO_MAX_EARLY_DATA_SIZE`：传入指向 `uint32_t` 的指针。任意非零值均为新签发票据启用 0-RTT；要求启用 [`CONFIG_QUIC_0RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_0RTT)，否则 `setsockopt()` 以 `ENOTSUP` 失败。按照 RFC 9001 第 4.6.1 节，票据始终通告固定的 `0xffffffff` 哨兵值（Sentinel）。客户端实际可发送的早期数据量受连接的流量控制／传输参数限制，因此本选项是启用开关，不是字节预算。

```c
int enable = 1;
uint32_t early_data = 1; /* non-zero enables 0-RTT for issued tickets */

zsock_setsockopt(quic_sock, ZSOCK_SOL_QUIC, ZSOCK_QUIC_SO_SESSION_TICKET_ENABLE,
                 &enable, sizeof(enable));
zsock_setsockopt(quic_sock, ZSOCK_SOL_QUIC, ZSOCK_QUIC_SO_MAX_EARLY_DATA_SIZE,
                 &early_data, sizeof(early_data));
```

### 5.3 每个流的早期数据状态

服务端可在流套接字上用 `ZSOCK_QUIC_SO_STREAM_EARLY_DATA` 查询指定流是否携带了已接受的 0-RTT 数据，参数为指向 `int` 的指针。协议层可据此实施重放保护，例如 HTTP/3 对非幂等的早期请求返回 `425 Too Early`。

## 6. 路径 MTU 发现（DPLPMTUD）

Zephyr QUIC 协议栈按照 RFC 9000 第 14.3 节执行 DPLPMTUD。RFC 8899 的搜索状态放在通用 [数据报 PLPMTUD API](P139_数据报分组层路径MTU发现.md#net-dplpmtud) 子系统中；QUIC 提供探测包（`PING` 加填充）、禁止分片的 UDP 发送，以及通过其恢复机制取得的 ACK／丢包确认。

其目标是找到不发生 IP 层分片即可通过路径的最大 UDP 载荷长度，再用该长度发送应用数据包。

### 6.1 行为（Behavior）

TLS 握手完成后，协议栈可能发送含 `PING` 帧和填充的数据报，探测更大的路径 MTU。底层 UDP 套接字发送时启用禁止分片（Don't Fragment），相关选项为 [IPv4 和 IPv6 套接字选项](P040_BSD套接字.md#ip-socket-options)中的 [`ZSOCK_IP_DONTFRAG`](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv4__socket__options.html#ga3c8f7f8895a3daae11dcd439eb2499a3)、[`ZSOCK_IPV6_DONTFRAG`](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv6__socket__options.html#ga44b16e54bc2922153e9a07d628cf1cba)。这些操作由内部完成，应用无需配置 QUIC 使用的 UDP 套接字。

协议栈跟踪三个相关上限。

1. **对端 `max_udp_payload_size` 传输参数**：对端在握手期间通告的上限。
2. **本地上限（Local Ceiling）**：接口或套接字 MTU 减去 IP 和 UDP 首部开销。
3. **已验证发送长度（Validated Send Size）**：得到 ACK 确认的最大探测长度，它决定实际可发送的 QUIC 包长度。

发送长度从 QUIC 要求的最小 UDP 载荷 1200 字节开始。当已验证长度低于本地和对端上限时，协议栈用二分搜索寻找可用的更大长度。探测 ACK 会提高已验证上限；探测反复丢失则缩小搜索区间。流帧大小始终限制在当前已验证上限内，因此高 MTU 路径在探测成功后会自动提高吞吐量。

### 6.2 与丢包恢复的交互（Interaction with Loss Recovery）

DPLPMTUD 探测属于会触发确认的报文（ACK-Eliciting），与流数据参与同一套丢包恢复机制。PTO 到期时，优先重传在途（In-Flight）流帧；只有没有流数据需要重传时才发送 DPLPMTUD 探测，这也是通常发送单独 `PING` 探测的场合。

当前没有面向应用的 QUIC API 来启用、禁用或调整 DPLPMTUD。握手完成后，只要路径可能支持更大的 MTU，就自动开始探测。自行实现 UDP 协议的传输层可以复用上述通用数据报 PLPMTUD API。

## 7. 配置选项（Configure Options）

以下选项位于 `if QUIC` 块内，只有启用 [`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC) 才可见。表格中的默认值和说明按官方页面保留；本节末尾给出与本次读取源码的差异。

### 7.1 连接与流数量（Connection and Stream Counts）

| 选项 | 原文默认值 | 说明 |
| --- | --- | --- |
| [`CONFIG_QUIC_MAX_CONTEXTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_CONTEXTS) | 1 | 系统中同时存在的 QUIC 连接的最大数量。每个上下文（Context）都有独立的 TLS 状态、流量控制窗口和已发送包历史，内存随此值线性增长。 |
| [`CONFIG_QUIC_MAX_STREAMS_BIDI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_STREAMS_BIDI) | 3–5 | 每个连接的双向流上限。流在构建时分配；未使用的流槽位仍占用其 TX／RX 缓冲区。 |
| [`CONFIG_QUIC_MAX_STREAMS_UNI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_STREAMS_UNI) | 0 | 每个连接的单向流上限。设为 0 可完全禁用单向流，回收相应缓冲区 RAM。 |
| [`CONFIG_QUIC_MAX_ENDPOINTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_ENDPOINTS) | 2–3 | UDP 端点套接字数量。只用一个 IP 版本连接一个服务端的客户端需要 2 个，双栈服务端角色需要 3 个。可考虑启用 [`CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6)，使 IPv4／IPv6 共用一个套接字。 |
| [`CONFIG_QUIC_MAX_PEER_CIDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_PEER_CIDS) | 4 | 每个连接跟踪的对端连接标识（Connection ID，CID）数量。资源极紧且不需要连接迁移的设备可以减至 1。 |

### 7.2 QUIC 传输参数与流量控制（QUIC Transport Parameters / Flow Control）

这些值在握手期间通告给远程对端（见 RFC 9000 第 18.2 节），决定对端在收到窗口更新前可以发送多少数据。每个值应匹配相应的本地接收缓冲区大小；原文指出，通告窗口大于接收缓冲区会造成缓冲区溢出，小于缓冲区则不能充分利用内存。

| 选项 | 原文默认值 | 说明 |
| --- | --- | --- |
| [`CONFIG_QUIC_INITIAL_MAX_DATA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_INITIAL_MAX_DATA) | 16384 | 连接级接收额度，单位字节。必须至少等于任一流的 `INITIAL_MAX_STREAM_DATA`，否则连接窗口会成为瓶颈。可从 `streams_bidi x INITIAL_MAX_STREAM_DATA_BIDI_LOCAL` 开始设置。 |
| [`CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_LOCAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_LOCAL) | 16384 | 本地发起双向流的初始接收窗口；设为 [`CONFIG_QUIC_STREAM_RX_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_RX_BUFFER_SIZE)。 |
| [`CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_REMOTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_REMOTE) | 16384 | 对端发起双向流的初始接收窗口；设为 [`CONFIG_QUIC_STREAM_RX_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_RX_BUFFER_SIZE)。 |
| [`CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_UNI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_UNI) | 16384 | 对端打开的单向流的初始接收窗口；仅在 `CONFIG_QUIC_MAX_STREAMS_UNI > 0` 时有意义。 |
| [`CONFIG_QUIC_INITIAL_MAX_STREAMS_BIDI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_INITIAL_MAX_STREAMS_BIDI) | `QUIC_MAX_STREAMS_BIDI` | 对端在收到 `MAX_STREAMS` 帧之前可以打开的双向流上限，默认等于本地构建时上限。 |
| [`CONFIG_QUIC_INITIAL_MAX_STREAMS_UNI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_INITIAL_MAX_STREAMS_UNI) | `QUIC_MAX_STREAMS_UNI` | 对端可以打开的单向流上限。 |
| [`CONFIG_QUIC_STREAM_RX_WINDOW_UPDATE_THRESHOLD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_RX_WINDOW_UPDATE_THRESHOLD) | 25 | 流接收缓冲区消耗达到此百分比时，发送 `MAX_STREAM_DATA` 补充对端窗口。较小值（如 15%）更频繁地更新窗口，可改善高时延链路吞吐量，但会增加控制帧。 |

### 7.3 缓冲区大小与 RAM 分配（Buffer Sizes and RAM Allocation）

这些选项直接控制 QUIC 子系统初始化时分配的 RAM。各项之间的关系见下一节内存模型（Memory Model）。

| 选项 | 原文默认值 | 说明 |
| --- | --- | --- |
| [`CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN) | 1500 | 每个端点的接收暂存缓冲区（RX Staging Buffer）大小，单位字节，应等于网络 MTU。结合 [`CONFIG_QUIC_PKT_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_PKT_COUNT)，原文计算总暂存量为 `endpoints x pkt_count x this value`。 |
| [`CONFIG_QUIC_TX_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_TX_BUFFER_SIZE) | 1500 | 每个端点用于组装输出包的缓冲区，应至少等于网络 MTU；为满足 IPv6 要求最小为 1280，最大为 1500。在较大路径 MTU 被确认前，DPLPMTUD 的已验证 UDP 载荷上限可能小于此值，见前面的路径 MTU 发现说明。 |
| [`CONFIG_QUIC_CRYPTO_RX_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_CRYPTO_RX_BUFFER_SIZE) | 4096 | 每个端点在 TLS 握手期间共享的 CRYPTO 帧重组（Reassembly）缓冲区。QUIC 顺序经过 Initial → Handshake → Application 加密级别，同一缓冲区可复用。浏览器互操作至少需要 4096 字节：Chrome／Firefox 可能把总计约 4 KiB 的 ClientHello 拆成 10 个或更多 CRYPTO 帧片段。嵌入式设备之间使用小证书时可减至 2048。范围 1024–8192。 |
| [`CONFIG_QUIC_CRYPTO_OOO_SLOTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_CRYPTO_OOO_SLOTS) | 8 | 每个端点的乱序（Out-of-Order，OOO）CRYPTO 帧元数据槽位数。每槽约 8 字节，在前面的空缺填补前记录一个乱序片段的偏移和长度。浏览器互操作需要 8 槽，仅嵌入式部署可减至 4 槽。范围 4–16。 |
| [`CONFIG_QUIC_STREAM_TX_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_TX_BUFFER_SIZE) | 8192 | 每流保存已发出但未确认数据的缓冲区。发送方无法越过未确认窗口，因此这是高时延链路吞吐量的主要限制参数。至少应达到带宽时延积（Bandwidth-Delay Product，BDP）：`throughput_bytes_per_ms x rtt_ms`。 |
| [`CONFIG_QUIC_STREAM_RX_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_RX_BUFFER_SIZE) | `QUIC_STREAM_TX_BUFFER_SIZE` | 每流接收缓冲区，默认等于 TX 缓冲区，适合对称请求／响应模式。原文称可针对非对称工作负载（例如仅下载的流）独立减小。 |
| [`CONFIG_QUIC_STREAM_OOO_SLOTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_OOO_SLOTS) | 4 | 每流乱序 STREAM 帧槽位数，每槽最多保存 [`CONFIG_QUIC_STREAM_OOO_SEG_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_OOO_SEG_SIZE) 字节。无丢包的本地网络可设为 2；有明显重排的广域网（Wide Area Network，WAN）链路可增至 8 或更多。 |
| [`CONFIG_QUIC_STREAM_OOO_SEG_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_OOO_SEG_SIZE) | 1280 | 一个已缓冲乱序段的最大长度。设为 MTU 可避免将传入帧拆分；乱序交付少见时可减至 512 字节。 |
| [`CONFIG_QUIC_SENT_PKT_HISTORY_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SENT_PKT_HISTORY_SIZE) | 64 | 最近已发送包记录的环形缓冲区深度，每项约 24 字节。应能同时覆盖全部在途包，至少为 `ceil(STREAM_TX_BUFFER_SIZE / TX_BUFFER_SIZE) x 2`。丢包或高时延 WAN 可增至 128–256。 |
| [`CONFIG_QUIC_TLS_TRANSCRIPT_BUF_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_TLS_TRANSCRIPT_BUF_LEN) | 4096 | 每连接累积 TLS 1.3 握手记录（Handshake Transcript）的缓冲区，用于 Finished 消息认证码（MAC）计算和 HKDF 密钥派生。4096 字节覆盖典型 RSA-2048、EC P-256 证书握手；较长证书链或 RSA-4096 可增至 6144–8192。总 RAM 为此值乘 [`CONFIG_QUIC_MAX_CONTEXTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_CONTEXTS)。 |

> 译注——非对称流的方向：下载接收方需要足够的 RX 缓冲区，不能仅因“只下载”就缩小接收缓冲区。应按本端实际发送／接收方向分别选择 TX、RX 容量，并使通告的接收窗口与可用接收容量匹配。

### 7.4 超时选项（Timeout Options）

| 选项 | 原文默认值 | 说明 |
| --- | --- | --- |
| [`CONFIG_QUIC_MAX_IDLE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_IDLE_TIMEOUT) | 30000 | 不活动达到此毫秒数后静默关闭连接。原文称双方通告后采用较小值，设 0 则完全禁用空闲超时。建议回环（Loopback）5000 ms、局域网（LAN）10000 ms、WAN 30000 ms。 |
| [`CONFIG_QUIC_CONNECT_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_CONNECT_TIMEOUT) | 3000 | 等待握手完成的毫秒数，超时后 `connect()` 失败。至少应为预期 RTT 的 10 倍，以容纳握手中的丢包。 |
| [`CONFIG_QUIC_MAX_PTO_TIMEOUT_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_PTO_TIMEOUT_MS) | 10000 | PTO 指数退避（Exponential Backoff）的毫秒上限。每次连续探测超时后翻倍，即 `PTO_n = PTO_base x 2^n`。此上限防止重传延迟过长，不应超过 [`CONFIG_QUIC_MAX_IDLE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_IDLE_TIMEOUT)。 |

### 7.5 服务线程选项（Service Thread Options）

| 选项 | 原文默认值 | 说明 |
| --- | --- | --- |
| [`CONFIG_QUIC_SERVICE_THREAD_PRIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SERVICE_THREAD_PRIO) | `NUM_PREEMPT_PRIORITIES` | QUIC 服务分派线程优先级。非负为抢占式（Preemptive），0 最高；负数为协作式（Cooperative）。 |
| [`CONFIG_QUIC_SERVICE_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SERVICE_STACK_SIZE) | 4096 | QUIC 服务线程栈的字节数。默认 4096 可满足 Mbed TLS 握手；仅在 RAM 极紧且分析确认不需要这部分余量时才缩小。 |
| [`CONFIG_QUIC_PKT_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_PKT_COUNT) | `QUIC_MAX_ENDPOINTS` | 同时待处理的接收包数量。默认等于端点数，使每端点同时可有一个包处于处理中。高吞吐场景可增加，例如设为端点数的 2 倍。 |

> 译注——网页与当前源码的容量口径：本次读取的官方 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig) 中，`QUIC_MAX_CONTEXTS` 默认跟随 `QUIC_MAX_ENDPOINTS`，服务端还需为监听套接字预留一个上下文。三个 `QUIC_INITIAL_MAX_STREAM_DATA_*` 默认跟随 RX 缓冲区，而非固定为表中的 16384；HTTP/3 服务端的单向流默认值也有条件分支。官方 [quic.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/quic.c) 的 `streams[]` 是系统共享数组，长度为 `CONFIG_QUIC_MAX_STREAMS_BIDI + CONFIG_QUIC_MAX_STREAMS_UNI`，并非每个连接各有这一份数组；`quic_pkts` 也是由 [`CONFIG_QUIC_PKT_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_PKT_COUNT) 控制的全局内存块池。以下原文公式和优化器采用的估算口径不能直接当作当前实现的实际分配量。配置以所用源码和最终生成的 `.config` 为准，本文不把当前 `main` 当作官网构建的固定提交。

## 8. 内存模型（Memory Model）

下表为原文给出的 RAM 区域及其随配置变化的公式，未特别标注的长度均为字节；`total_streams` 在原文模型中表示连接数乘每连接双向、单向流数量之和。

| 内存区域（Memory Region） | 原文公式（Formula） |
| --- | --- |
| 端点 RX 暂存（Endpoint RX Staging） | `QUIC_MAX_ENDPOINTS x QUIC_PKT_COUNT x QUIC_ENDPOINT_PENDING_DATA_LEN` |
| 端点 TX 缓冲区（Endpoint TX Buffers） | `QUIC_MAX_ENDPOINTS x QUIC_TX_BUFFER_SIZE` |
| 加密 RX 缓冲区（Crypto RX Buffers） | `QUIC_MAX_ENDPOINTS x QUIC_CRYPTO_RX_BUFFER_SIZE` |
| 加密乱序槽位（Crypto OOO Slots） | `QUIC_MAX_ENDPOINTS x QUIC_CRYPTO_OOO_SLOTS x 8` |
| 流 TX 缓冲区（Stream TX Buffers） | `(QUIC_MAX_CONTEXTS x (QUIC_MAX_STREAMS_BIDI + QUIC_MAX_STREAMS_UNI)) x QUIC_STREAM_TX_BUFFER_SIZE` |
| 流 RX 缓冲区（Stream RX Buffers） | `(QUIC_MAX_CONTEXTS x (QUIC_MAX_STREAMS_BIDI + QUIC_MAX_STREAMS_UNI)) x QUIC_STREAM_RX_BUFFER_SIZE` |
| 流乱序缓冲区（Stream OOO Buffers） | `total_streams x QUIC_STREAM_OOO_SLOTS x QUIC_STREAM_OOO_SEG_SIZE` |
| 已发送包历史（Sent-Packet History） | `QUIC_MAX_CONTEXTS x QUIC_SENT_PKT_HISTORY_SIZE x 24` |
| TLS 握手记录缓冲区（TLS Transcript Buffers） | `QUIC_MAX_CONTEXTS x QUIC_TLS_TRANSCRIPT_BUF_LEN` |
| TLS 上下文／Mbed TLS（TLS Context） | `~8192 x QUIC_MAX_CONTEXTS`，为依赖密码套件的估计值 |
| 连接状态（Connection State） | `~512 x QUIC_MAX_CONTEXTS` |
| 流状态（Stream State） | `~128 x total_streams` |

下面是原文给出的粗略最小估计：一个连接、三个双向流、1500 字节流缓冲区，采用 LAN 客户端默认设置。

```text
Endpoint RX staging :  2 x 1 x 1500 = 3 000 B
Endpoint TX         :  2 x 1500      = 3 000 B
Crypto RX buffers   :  2 x 2048      = 4 096 B  (embedded client, LAN)
Crypto OOO slots    :  2 x 4 x 8     =   256 B
Stream TX           :  3 x 1500      = 4 500 B
Stream RX           :  3 x 1500      = 4 500 B
OOO buffers         :  3 x 2 x 512   = 3 072 B
Sent-pkt history    :  1 x 16 x 24   =   384 B
TLS transcript      :  1 x 4096      = 4 096 B
TLS context         :  1 x 8192      = 8 192 B
State overhead      :  512 + 3x128   =   896 B
---------------------------------------------
Approximate total                   ~ 35 992 B (~35 KiB)
```

流较少时，每个连接的 Mbed TLS 上下文占主要开销；流较多时，TX／RX 缓冲区成为主要开销。

> 译注——算术与模型：原始清单中 `2 x 4 x 8` 应为 64 B，原文却写为 256 B；只修正这一项，所列项目合计为 35800 B，而不是 35992 B。该清单的 `pkt_count` 取 1，也不同于后面优化器例子的 2。上面的源码容量差异仍然适用；这些数字是估算，不是链接映射（Linker Map）或运行时内存测量结果。

## 9. Kconfig 优化器（Kconfig Optimizer）

同时满足内存效率和目标吞吐量，需要平衡多个相互关联的参数。Zephyr 为此提供 Python 优化脚本：

```text
scripts/net/quic-kconfig-optimizer.py
```

脚本接收部署场景，包括连接数、MTU、网络类型、预期 RTT 和 RAM 预算，输出推荐的 `CONFIG_` 值、RAM 分项估计以及可粘贴的 `prj.conf` 片段。

### 9.1 前提（Prerequisites）

脚本要求 Python 3.8 或更新版本，无标准库以外的依赖。以下命令在持有所述官方脚本的 Zephyr 源码根目录、Bash 终端执行；检查版本应显示 3.8 或以上。它只输出配置建议，不构建固件。

```sh
python3 --version   # must be 3.8+
```

### 9.2 交互模式（Interactive Mode）

不传参数进入引导式交互模式，每项默认值显示在方括号内，按 Enter 接受。

```sh
python3 scripts/net/quic-kconfig-optimizer.py
```

以下为原文交互示例；它依次询问连接数、每连接双向流／单向流数、MTU、RAM 预算、角色、IP 版本、RTT、丢包率、消息长度、是否预计乱序以及网络类型。

```text
============================================================
  Zephyr QUIC Kconfig Optimizer -- Interactive Mode
============================================================
  Press Enter to accept [default] values.

Max QUIC connections (QUIC_MAX_CONTEXTS) [1]: 2
Bidirectional streams per connection [3]:
Unidirectional streams per connection [0]:
Network MTU in bytes [1500]:
RAM budget in bytes (0 = no limit) [0]: 131072
Device role [client] (client/server/both):
IP version(s) [ipv4] (ipv4/ipv6/both):
Expected RTT in ms [10]: 50
Expected packet loss rate (%) [0.0]:
Typical application message size (bytes) [1024]: 4096
Expect out-of-order delivery? [no] (yes/no):
Network type [lan] (lan/wan/loopback):
```

### 9.3 命令行模式（Command-Line Mode）

全部参数可通过命令行提供。所需参数齐全时，脚本跳过交互提示，便于持续集成（Continuous Integration，CI）流水线和脚本化板级启动工作。

```sh
python3 scripts/net/quic-kconfig-optimizer.py \
    --contexts        2          \
    --streams-bidi    3          \
    --streams-uni     0          \
    --mtu             1500       \
    --ram-budget      131072     \
    --role            client     \
    --ip-version      ipv4       \
    --rtt-ms          50         \
    --loss-rate       0.0        \
    --app-message-size 4096      \
    --ooo-expected    no         \
    --network-type    lan
```

原文说明：只提供部分参数时，对缺少的参数回退到交互模式。

```sh
# Pre-fill the constraints, fill the rest interactively
python3 scripts/net/quic-kconfig-optimizer.py \
    --contexts 1 --streams-bidi 3 --ram-budget 65536
```

> 译注——部分参数没有预填：本次读取的官方 [优化器源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/net/quic-kconfig-optimizer.py) 在任一必需参数缺失时直接调用 `gather_interactive()`，没有将已提供的 CLI 参数合并进去。因此上面的部分参数示例实际会重新询问全部项目，不能依赖它预填 `--ram-budget` 等约束。要无人值守执行，应像前一个完整命令一样提供全部必需参数。

### 9.4 输入参数（Input Parameters）

| 参数 | CLI 标志 | 默认值 | 说明 |
| --- | --- | --- | --- |
| 最大连接数（Max Connections） | `--contexts` | 1 | 直接对应 [`CONFIG_QUIC_MAX_CONTEXTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_CONTEXTS)；TLS 上下文、连接状态和已发送包历史的内存随之线性增长。 |
| 双向流（Bidi Streams） | `--streams-bidi` | 3 | 原文模型中的每连接双向流数。每个连接的每个流均分配 TX／RX 缓冲区，启动时预留 `contexts x streams_bidi x 2 x stream_buf` 字节。 |
| 单向流（Uni Streams） | `--streams-uni` | 0 | 原文模型中的每连接单向流数；不需要时设 0，避免分配相应接收缓冲区。 |
| 最大传输单元（MTU） | `--mtu` | 1500 | 网络 MTU 字节数，为 [`CONFIG_QUIC_TX_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_TX_BUFFER_SIZE) 和 [`CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN) 设定下限。需满足 IPv6 最小 MTU 且没有路径 MTU 发现的网络使用 1280。 |
| RAM 预算（RAM Budget） | `--ram-budget` | 0（不限） | QUIC 估算 RAM 字节数的硬上限；超出时脚本报错退出。0 表示不检查预算，只报告估计值。 |
| 设备角色（Device Role） | `--role` | `client` | `client`、`server` 或 `both`；影响端点推荐数量，服务端和双栈设备通常需要一个额外端点。 |
| IP 版本（IP Version） | `--ip-version` | `ipv4` | `ipv4`、`ipv6` 或 `both`；原文指出，选 `both` 且未启用 [`CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6) 时需要额外端点。 |
| 预期 RTT（Expected RTT） | `--rtt-ms` | 10 | 设备与对端的往返毫秒数，用于确定 [`CONFIG_QUIC_CONNECT_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_CONNECT_TIMEOUT)、[`CONFIG_QUIC_MAX_PTO_TIMEOUT_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_PTO_TIMEOUT_MS) 和窗口更新阈值。 |
| 丢包率（Packet Loss Rate） | `--loss-rate` | 0.0 | 预期丢包百分比，范围 0–100。达到 2% 时将流缓冲区翻倍以保持流水线满载；达到 5% 时将已发送包历史设为至少 128 项，以便检测丢包。 |
| 消息长度（Message Size） | `--app-message-size` | 1024 | 典型应用载荷字节数。流缓冲区至少容纳两倍此值，使前一条消息等待确认时，下一条完整消息仍可在途传输。 |
| 预计乱序（OOO Expected） | `--ooo-expected` | `no` | 是否预计乱序交付，取 `yes`／`no`。`no` 时将乱序槽位减为 2、段大小减为 512 B；原文给出的节省量为 `total_streams x (default_slots - 2) x seg_size`。 |
| 网络类型（Network Type） | `--network-type` | `lan` | `lan`、`wan` 或 `loopback`；控制空闲超时、PTO 上限，以及是否把流缓冲区翻倍来覆盖 WAN 较大的带宽时延积。 |

> 译注——启发式边界：该脚本目前将端点 TX 大小限制在 1280–1500，而不是对任意 `--mtu` 都保证缓冲区不小于 MTU；流缓冲区最多为 65535 字节，因此大消息的“两倍”目标也可能受上限限制。脚本按消息大小、512 字节对齐和 WAN／丢包条件估算流缓冲区，没有输入目标带宽，也没有据 RTT 计算真实 BDP。`both` 端点数量的实现条件为“双栈且角色是 server／both”，脚本未读取工作区的 IPv4 映射配置。表格是原文参数说明，不是完整约束求解保证。

### 9.5 输出区域（Output Sections）

优化器打印五部分。

1. **输入参数（Input Parameters）**：回显全部输入，便于核对。
2. **推荐 Kconfig 值（Recommended Kconfig Values）**：按连接数量、传输参数、缓冲区大小和超时分组输出 `CONFIG_*`。
3. **估计 RAM 用量（Estimated RAM Usage）**：每个内存区域的大小与按比例绘制的 ASCII 条形图；给出 RAM 预算时显示利用百分比。
4. **prj.conf 片段（prj.conf Snippet）**：可粘贴到 `prj.conf` 或板级 `.conf` 覆盖文件的 Kconfig 选项。
5. **补充说明（Additional Notes）**：根据输入给出的部署提示和建议，例如服务栈可能过小、连接级流量窗口可能成为瓶颈。

### 9.6 输出示例（Example Output）

原文以下输出对应一个最小客户端配置：一个连接、三个双向流、以太网 LAN、10 ms RTT、1 KiB 消息、无乱序。

```text
========================================================================
         QUIC Kconfig Optimizer -- Recommended Settings
========================================================================

------------------------------------------------------------------------
  INPUT PARAMETERS
------------------------------------------------------------------------
  Max connections (QUIC_MAX_CONTEXTS)            1
  Bidi streams per connection                    3
  Uni  streams per connection                    0
  MTU (bytes)                                    1500
  RAM budget                                     unlimited
  Device role                                    client
  IP version                                     ipv4
  Expected RTT (ms)                              10
  Expected packet loss (%)                       0.0
  Typical message size (bytes)                   1024
  Out-of-order delivery expected                 no
  Network type                                   lan

------------------------------------------------------------------------
  RECOMMENDED Kconfig VALUES
------------------------------------------------------------------------

  [Connection / stream counts]
    CONFIG_QUIC_MAX_CONTEXTS                              1
    CONFIG_QUIC_MAX_STREAMS_BIDI                         3
    CONFIG_QUIC_MAX_STREAMS_UNI                          0
    CONFIG_QUIC_MAX_ENDPOINTS                            2
    CONFIG_QUIC_PKT_COUNT                                2

  [QUIC transport parameters (flow control)]
    CONFIG_QUIC_INITIAL_MAX_DATA                         6144
    CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_LOCAL       2048
    CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_REMOTE      2048
    CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_UNI              16384
    CONFIG_QUIC_INITIAL_MAX_STREAMS_BIDI                 3
    CONFIG_QUIC_INITIAL_MAX_STREAMS_UNI                  0
    CONFIG_QUIC_STREAM_RX_WINDOW_UPDATE_THRESHOLD        25

  [Buffer sizes (RAM)]
    CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN                1500
    CONFIG_QUIC_TX_BUFFER_SIZE                           1500
    CONFIG_QUIC_CRYPTO_RX_BUFFER_SIZE                    2048
    CONFIG_QUIC_CRYPTO_OOO_SLOTS                         4
    CONFIG_QUIC_STREAM_TX_BUFFER_SIZE                    2048
    CONFIG_QUIC_STREAM_RX_BUFFER_SIZE                    2048
    CONFIG_QUIC_STREAM_OOO_SLOTS                         2
    CONFIG_QUIC_STREAM_OOO_SEG_SIZE                      512
    CONFIG_QUIC_SENT_PKT_HISTORY_SIZE                    16
    CONFIG_QUIC_TLS_TRANSCRIPT_BUF_LEN                   4096

  [Timeouts]
    CONFIG_QUIC_MAX_IDLE_TIMEOUT                         10000
    CONFIG_QUIC_CONNECT_TIMEOUT                          3000
    CONFIG_QUIC_MAX_PTO_TIMEOUT_MS                       5000

------------------------------------------------------------------------
  ESTIMATED RAM USAGE
------------------------------------------------------------------------
  Endpoint RX staging              9 KiB  ######
  Endpoint TX buffers              3 KiB  ##
  Crypto RX buffers                4 KiB  ###
  Crypto OOO slots                  64 B
  Stream TX buffers                6 KiB  ####
  Stream RX buffers                6 KiB  ####
  Stream OOO buffers               2 KiB  #
  Stream state overhead            0 KiB
  Sent-packet history              0 KiB
  TLS context overhead             8 KiB  #####
  Connection state overhead        0 KiB
  TLS transcript buffers           4 KiB  ##
  TOTAL                           42 KiB  ######################## <-- TOTAL

------------------------------------------------------------------------
  prj.conf SNIPPET
------------------------------------------------------------------------

CONFIG_QUIC_MAX_CONTEXTS=1
CONFIG_QUIC_MAX_STREAMS_BIDI=3
...
```

> 译注——这是原网页示意输出：本次对保存的官方脚本执行相同输入的纯计算，得到端点 RX 暂存 6000 B、流乱序缓冲区 3072 B、总计 42088 B，报告四舍五入为 41 KiB；与上面原文的 9 KiB、2 KiB、42 KiB 不一致。原文 `prj.conf` 片段末尾的 `...` 是省略标记，不能作为配置项粘贴。应使用脚本实际输出的完整片段，并另行核对 Kconfig 范围和生成的配置。该纯计算不代表固件构建或实际 RAM 测量。

### 9.7 最小物联网传感器（Minimal IoT Sensor）

场景为仅 IPv4 的客户端、RAM 预算紧张：向云端打开一个 QUIC 连接，用一个双向流上报遥测（Telemetry），QUIC 可用 RAM 为 48 KiB。

```sh
python3 scripts/net/quic-kconfig-optimizer.py \
    --contexts 1 --streams-bidi 1 --streams-uni 0 \
    --mtu 1280 --ram-budget 49152 \
    --role client --ip-version ipv4 \
    --rtt-ms 80 --loss-rate 0.5 \
    --app-message-size 256 \
    --ooo-expected no --network-type wan
```

原文说明：脚本将流缓冲区设为最小值 1500 B，因为 `2 x 256 = 512 < 1500`；乱序槽位为 2，已发送包历史为 16 项，在尽量节省 RAM 的同时处理 WAN 上预期的 0.5% 丢包。

> 译注——当前脚本结果：本次纯计算得到流缓冲区 **3072 B**、历史 **64 项**、总估算 **37632 B**。原因是 1280 字节先按 512 对齐为 1536，再因 `wan` 翻倍；WAN 同时把历史下限提高为 64。它仍低于 49152 B 预算，但不能按原文的 1500／16 配置理解。

### 9.8 双栈服务端（Dual-Stack Server）

场景为支持 IPv4 和 IPv6 的边缘网关，接受最多四个同时连接的客户端，为 QUIC 提供 256 KiB RAM。

```sh
python3 scripts/net/quic-kconfig-optimizer.py \
    --contexts 4 --streams-bidi 3 --streams-uni 1 \
    --mtu 1500 --ram-budget 262144 \
    --role server --ip-version both \
    --rtt-ms 5 --loss-rate 0.0 \
    --app-message-size 8192 \
    --ooo-expected no --network-type lan
```

原文说明：脚本推荐三个端点，括号中解释为两个监听套接字加各客户端地址族的端点；流缓冲区为 16 KiB，容纳 `2 x 8192 B` 消息。在四个上下文、每个四个流的模型下，这些缓冲区将占据主要 RAM。

> 译注——该预算例子会失败：官方脚本的原参数估算为 **627472 B（约 613 KiB）**，超过 **262144 B（256 KiB）**，因而报错退出，不会输出一套符合预算的配置。仅模型中的 16 个流的 TX 和 RX 就各需 262144 B。上面“两个监听加各地址族”的文字也不是三个端点的明确分配推导；当前 Kconfig 还要求服务端连接上下文考虑监听者。应依据实际实现重新确定并发连接、共享流池和缓冲区需求；不把这个例子视为已验证可承载四个客户端的配置。

### 9.9 有丢包的高吞吐 WAN（High-Throughput WAN Link with Packet Loss）

场景为通过蜂窝 WAN 连接的数据聚合器，链路有可测丢包，需要持续吞吐固件更新载荷。

```sh
python3 scripts/net/quic-kconfig-optimizer.py \
    --contexts 1 --streams-bidi 2 --streams-uni 0 \
    --mtu 1400 --ram-budget 0 \
    --role client --ip-version ipv4 \
    --rtt-ms 150 --loss-rate 3.0 \
    --app-message-size 32768 \
    --ooo-expected yes --network-type wan
```

原文说明：因丢包率至少 2%，脚本将流缓冲区翻倍；高时延 WAN 使用 15% 窗口更新阈值，让对端发送窗口保持开放，充分利用流水线。乱序槽位设为 8、每段 1280 字节，以应对蜂窝链路重排。

> 译注——上限仍有效：本次纯计算的每流缓冲区为 **65535 B**，已达到脚本上限，并非无限翻倍；历史 128 项，总估算 315468 B。WAN 与丢包条件通过逻辑“或”触发一次翻倍，不叠加翻两次。

## 10. 调优指南（Tuning Guidelines）

- **从优化器默认值开始，再测量。** 原文将这些启发式规则定位为保守建议。使用 Zephyr 网络统计 [`CONFIG_NET_STATISTICS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_STATISTICS) 观察实际流窗口停顿和乱序事件，再决定是否增大缓冲区。
- **流缓冲区通常是主要 RAM 开销。** 原文多连接模型由 `contexts x streams x 2 x stream_buf` 主导，容量减半可同比节省。只有分析显示发送方持续停顿时，才把容量增至超过 BDP；实际全局流池差异见第 7 节译注。
- **避免连接级窗口成为瓶颈。** [`CONFIG_QUIC_INITIAL_MAX_DATA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_INITIAL_MAX_DATA) 至少应等于最大的单流窗口，否则即使单流窗口开放，连接额度也会限制吞吐量。
- **CRYPTO 缓冲区随端点而非连接数量增长。** [`CONFIG_QUIC_CRYPTO_RX_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_CRYPTO_RX_BUFFER_SIZE) 和 [`CONFIG_QUIC_CRYPTO_OOO_SLOTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_CRYPTO_OOO_SLOTS) 每个端点分配一份，RAM 开销为 `QUIC_MAX_ENDPOINTS x buffer_size`。默认 4096 字节用于 Chrome／Firefox 将 ClientHello 拆成多个小 CRYPTO 帧时的互操作；双方均为 Zephyr 嵌入式设备时可减至 2048。
- **使用 IPv4 映射的 IPv6（IPv4-Mapped IPv6）。** 同时需要两种协议时，启用 [`CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6) 可让一个 UDP 套接字服务两种地址族，使 [`CONFIG_QUIC_MAX_ENDPOINTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_ENDPOINTS) 减少一个并节约相关缓冲区 RAM。
- **禁用未使用的流方向。** 原文建议仅用客户端发起流时，将 [`CONFIG_QUIC_MAX_STREAMS_UNI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_STREAMS_UNI) 设为 0，优化器会自动计入。译注：发起者和单／双向是两个不同属性；只有确实不使用单向流时才设 0，客户端也可以发起单向流。
- **乱序内存按流分配。** `QUIC_STREAM_OOO_SLOTS x QUIC_STREAM_OOO_SEG_SIZE x total_streams` 可能很可观。原文认为可靠 LAN 上可把 [`CONFIG_QUIC_STREAM_OOO_SLOTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_OOO_SLOTS) 设为 2、[`CONFIG_QUIC_STREAM_OOO_SEG_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_STREAM_OOO_SEG_SIZE) 设为 512，每连接节省数 KiB；是否足够仍应结合实际重排和所用源码确认。

## 11. API 参考与相关示例（API Reference）

详细类型、选项和函数见 [QUIC 库参考](P147_QUIC完整API参考.md)。本章只覆盖原指南；详细 API、头文件与会话／统计结构均在各自参考页维护，并分别登记翻译状态。

- [QUIC 回显客户端](P145_QUIC回显客户端.md#quic-client-echo)：通过 QUIC API 和套接字服务 API 实现简单 IPv4／IPv6 客户端。
- [QUIC 回显服务端](P146_QUIC回显服务端.md#quic-service-echo)：通过相同接口实现简单 IPv4／IPv6 服务端。


<a id="quic-transport-interface"></a>
<a id="id1"></a>
<a id="contents"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="id10"></a>
<a id="id11"></a>
<a id="id12"></a>
<a id="id13"></a>
<a id="id14"></a>
<a id="id15"></a>
<a id="id16"></a>
<a id="id17"></a>
<a id="id18"></a>
<a id="id19"></a>
<a id="id20"></a>
<a id="id21"></a>
<a id="id22"></a>
<a id="id23"></a>
<a id="id24"></a>
<a id="id25"></a>
<a id="id26"></a>
<a id="id27"></a>
<a id="id28"></a>
<a id="id29"></a>
<a id="id30"></a>
<a id="id31"></a>
<a id="id32"></a>
<a id="id33"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="index-1"></a>
<a id="index-2"></a>
<a id="architecture-concepts"></a>
<a id="application-workflow"></a>
<a id="client-application"></a>
<a id="server-application"></a>
<a id="tls-security-configuration"></a>
<a id="managing-certificates"></a>
<a id="applying-credentials-to-quic"></a>
<a id="applying-alpn-to-quic"></a>
<a id="session-resumption-and-0-rtt"></a>
<a id="quic-session-resumption"></a>
<a id="index-3"></a>
<a id="index-4"></a>
<a id="path-mtu-discovery-dplpmtud"></a>
<a id="quic-dplpmtud"></a>
<a id="index-5"></a>
<a id="behavior"></a>
<a id="interaction-with-loss-recovery"></a>
<a id="configure-options"></a>
<a id="connection-and-stream-counts"></a>
<a id="quic-transport-parameters-flow-control"></a>
<a id="index-6"></a>
<a id="buffer-sizes-and-ram-allocation"></a>
<a id="timeout-options"></a>
<a id="service-thread-options"></a>
<a id="memory-model"></a>
<a id="kconfig-optimizer"></a>
<a id="prerequisites"></a>
<a id="usage-interactive-mode"></a>
<a id="usage-command-line-mode"></a>
<a id="input-parameters"></a>
<a id="output-sections"></a>
<a id="example-output"></a>
<a id="minimal-iot-sensor-client-ipv4-only-tight-ram-budget"></a>
<a id="dual-stack-server-ipv4-ipv6-multiple-clients"></a>
<a id="high-throughput-wan-link-with-packet-loss"></a>
<a id="tuning-guidelines"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：RTP实时传输协议](P141_RTP实时传输协议.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：网络跟踪](P154_网络跟踪.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P142_RTP发送示例.md) · [返回大纲](大纲.md) · [下一章](P144_QUIC示例目录.md)

</details>

<!-- reading-navigation:end -->
