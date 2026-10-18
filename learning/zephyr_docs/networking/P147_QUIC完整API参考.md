---
id: learning.zephyr-docs.networking.api-147
title: QUIC完整API参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__quic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第147章\_QUIC完整API参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__quic.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 147.1\_阅读说明与来源

译注：先读[QUIC传输接口指南](P143_QUIC传输接口.md)及[回显示例目录](P144_QUIC示例目录.md)，理解连接套接字、流套接字和 TLS 握手的关系，再按符号查询本组参考。

本组：[完整API参考](P147_QUIC完整API参考.md) · [头文件参考](P148_QUIC头文件参考.md) · [头文件源码](P149_QUIC头文件源码.md) · [会话状态](P150_QUIC会话状态.md) · [会话传输参数](P151_QUIC会话传输参数.md) · [统计数据](P152_QUIC统计数据.md) · [全局统计](P153_QUIC全局统计数据.md)。

QUIC 库（QUIC Library）。

QUIC 库（QUIC Library）。引入版本（Since）：4.5；API 版本（Version）：`0.1.0`。注意（Note）：服务端模式会针对不支持的版本发送版本协商（Version Negotiation）报文，并可在对端地址验证之前执行 [RFC 9000](https://datatracker.ietf.org/doc/html/rfc9000.html) 的反放大限制（Anti-Amplification Limit），包括基于 Retry 和 NEW_TOKEN 的地址验证令牌（Address-Validation Token）。

## 147.2\_数据结构（Data Structures）

<a id="r_net_5Fstats_5Fquic"></a>

```c
struct net_stats_quic
```

QUIC 统计数据（QUIC Statistics）。

相关声明：[net_stats_quic](P152_QUIC统计数据.md)。

<a id="r_net_5Fstats_5Fquic_5Fglobal"></a>

```c
struct net_stats_quic_global
```

QUIC 全局统计数据（QUIC Global Statistics）。

相关声明：[net_stats_quic_global](P153_QUIC全局统计数据.md)。

<a id="r_quic_5Fsession_5Ftransport_5Fparams"></a>

```c
struct quic_session_transport_params
```

为会话恢复保存的对端传输参数（Remembered Peer Transport Parameters）。

相关声明：[quic_session_transport_params](P151_QUIC会话传输参数.md)。

<a id="r_quic_5Fsession_5Fstate"></a>

```c
struct quic_session_state
```

可恢复的 QUIC 客户端会话状态（Resumable QUIC Client Session State）。

相关声明：[quic_session_state](P150_QUIC会话状态.md)。

## 147.3\_宏定义（Macros）

<a id="r_gad0638e0b5903257b18ba1ed79103bdc5"></a>

```c
#define ZSOCK_SOL_QUIC 284
```

供 `getsockopt`／`setsockopt` 使用的 QUIC 套接字选项级别（Socket Option Level）。

<a id="r_ga50d0ecc2871e8bafb68d38abb564d295"></a>

```c
#define QUIC_SESSION_STATE_VERSION 2U
```

`struct quic_session_state` 的版本。

<a id="r_ga8f757a00b692d8eaa39536557f326306"></a>

```c
#define QUIC_MAX_SESSION_TICKET_LEN 256U
```

通过 `struct quic_session_state` 导出的序列化票据（Serialized Ticket）的最大长度。

<a id="r_ga6c21dda81654cab53209bc1dca4909d2"></a>

```c
#define QUIC_MAX_RESUMPTION_PSK_LEN 48U
```

通过 `struct quic_session_state` 导出的会话恢复预共享密钥（Pre-Shared Key，PSK）的最大长度。

## 147.4\_枚举（Enumerations）

<a id="r_ga290d25ba3fe401d61b0c35556e67a04c"></a>

```c
enum quic_stream_direction { QUIC_STREAM_BIDIRECTIONAL = 0x00 , QUIC_STREAM_UNIDIRECTIONAL = 0x02 }
```

流方向（Stream Direction）。

<a id="r_ga8c36dbae839efb95be6ea6a8c98f8847"></a>

```c
enum quic_stream_initiator { QUIC_STREAM_CLIENT = 0x00 , QUIC_STREAM_SERVER = 0x01 }
```

流发起者（Stream Initiator）。

<a id="r_ga006f049efb2b5a9e3ff7821434edc93b"></a>

```c
enum { ZSOCK_QUIC_SO_STREAM_TYPE = 1 , ZSOCK_QUIC_SO_CERT_CHAIN_ADD = 2 , ZSOCK_QUIC_SO_CERT_CHAIN_DEL = 3 , ZSOCK_QUIC_SO_STOP_SENDING_CODE = 4 , ZSOCK_QUIC_SO_SESSION_STATE = 5 , ZSOCK_QUIC_SO_SESSION_TICKET_ENABLE = 6 , ZSOCK_QUIC_SO_MAX_EARLY_DATA_SIZE = 7 , ZSOCK_QUIC_SO_STREAM_EARLY_DATA = 8 }
```

在 `ZSOCK_SOL_QUIC` 级别通过 `getsockopt`／`setsockopt` 使用的 QUIC 套接字选项。

## 147.5\_函数（Functions）

<a id="r_gac5b95872bf7fa74b7a1d2c7b011fd99f"></a>

```c
int quic_connection_open (const struct net_sockaddr *remote_addr, const struct net_sockaddr *local_addr)
```

创建新的 QUIC 连接套接字（Connection Socket）。

<a id="r_gade13e997f7a3f9c79590c56ef2bb72c3"></a>

```c
int quic_connection_close (int sock)
```

关闭 QUIC 套接字。

<a id="r_ga2d32dd11cff3f02426749955f5a72bd8"></a>

```c
int quic_stream_open (int connection_sock, enum quic_stream_initiator initiator, enum quic_stream_direction direction, uint8_t priority)
```

在已建立的 QUIC 连接内创建新的 QUIC 流套接字（Stream Socket）。

<a id="r_gae1501fa858907f12bd308442425ebeeb"></a>

```c
int quic_stream_close (int sock)
```

关闭 QUIC 流套接字。

<a id="r_ga520012661ae348538e817e3cfed35a70"></a>

```c
bool quic_is_stream_socket (int sock)
```

检查给定套接字是否为 QUIC 流套接字。

<a id="r_ga19d171ac47d79394d58b371b43585786"></a>

```c
bool quic_is_connection_socket (int sock)
```

检查给定套接字是否为 QUIC 连接套接字。

<a id="r_ga6ae488ec3f462f5a15c8b3106f293ad2"></a>

```c
int quic_stream_get_id (int sock, uint64_t *stream_id)
```

取得给定 QUIC 流套接字所关联的流标识（Stream ID）。

## 147.6\_详细说明（Detailed Documentation）

<a id="ga6c21dda81654cab53209bc1dca4909d2"></a>

### `QUIC_MAX_RESUMPTION_PSK_LEN`

```c
#define QUIC_MAX_RESUMPTION_PSK_LEN 48U
```

```c
#include <zephyr/net/quic.h>
```

通过 `struct quic_session_state` 导出的会话恢复预共享密钥（Pre-Shared Key，PSK）的最大长度。

<a id="ga8f757a00b692d8eaa39536557f326306"></a>

### `QUIC_MAX_SESSION_TICKET_LEN`

```c
#define QUIC_MAX_SESSION_TICKET_LEN 256U
```

```c
#include <zephyr/net/quic.h>
```

通过 `struct quic_session_state` 导出的序列化票据（Serialized Ticket）的最大长度。

<a id="ga50d0ecc2871e8bafb68d38abb564d295"></a>

### `QUIC_SESSION_STATE_VERSION`

```c
#define QUIC_SESSION_STATE_VERSION 2U
```

```c
#include <zephyr/net/quic.h>
```

`struct quic_session_state` 的版本。

<a id="gad0638e0b5903257b18ba1ed79103bdc5"></a>

### `ZSOCK_SOL_QUIC`

```c
#define ZSOCK_SOL_QUIC 284
```

```c
#include <zephyr/net/quic.h>
```

供 `getsockopt`／`setsockopt` 使用的 QUIC 套接字选项级别（Socket Option Level）。

<a id="ga006f049efb2b5a9e3ff7821434edc93b"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/net/quic.h>
```

在 `ZSOCK_SOL_QUIC` 级别通过 `getsockopt`／`setsockopt` 使用的 QUIC 套接字选项。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ZSOCK_QUIC_SO_STREAM_TYPE` | 获取流类型，返回方向与发起者位的组合，即 `direction \| initiator`。 |
| `ZSOCK_QUIC_SO_CERT_CHAIN_ADD` | 向证书链（Certificate Chain）添加一个中间证书（Intermediate Certificate）。 选项值为指向 `sec_tag_t` 的指针，引用此前通过 `tls_credential_add()` 注册的凭据；凭据类型为 `TLS_CREDENTIAL_CA_CERTIFICATE` 或 `TLS_CREDENTIAL_PUBLIC_CERTIFICATE`。选项长度必须为 `sizeof(sec_tag_t)`。可多次调用以添加多个中间证书。 |
| `ZSOCK_QUIC_SO_CERT_CHAIN_DEL` | 从证书链中删除一个中间证书。 选项值为指向 `sec_tag_t` 的指针，引用此前通过 `ZSOCK_QUIC_SO_CERT_CHAIN_ADD` 添加的凭据。选项长度必须为 `sizeof(sec_tag_t)` 或 0。长度设为 0 时，可以将选项值设为 `NULL` 以省略该值，并删除全部中间证书。 |
| `ZSOCK_QUIC_SO_STOP_SENDING_CODE` | 设置关闭流时发送 `STOP_SENDING` 帧所使用的错误码。 |
| `ZSOCK_QUIC_SO_SESSION_STATE` | 导出或导入可恢复的客户端会话状态（Session State）。 选项值为指向 `struct quic_session_state` 的指针。客户端收到 `NewSessionTicket` 后，在已连接的客户端连接套接字上调用 `getsockopt()` 取得状态；随后在新的客户端连接套接字打开首个流之前，通过 `setsockopt()` 导入返回的状态，以尝试会话恢复，并在允许时使用 0-RTT。0-RTT 数据可能被重放或被对端拒绝，因此应用只能发送可安全重放（Replay-Safe）的早期数据（Early Data），并准备在握手完成后重试。关闭 `CONFIG_QUIC_0RTT` 时，导入状态仍可进行 1-RTT 恢复，但不会启用早期数据。 |
| `ZSOCK_QUIC_SO_SESSION_TICKET_ENABLE` | 启用或禁用服务端会话票据签发（Session Ticket Issuance）。 选项值为指向 `int` 的指针。在握手前对监听套接字或服务端连接套接字设置非零值，可使服务端在握手完成后发送 `NewSessionTicket`。 |
| `ZSOCK_QUIC_SO_MAX_EARLY_DATA_SIZE` | 为本服务端签发的票据启用 0-RTT 早期数据。 选项值为指向 `uint32_t` 的指针，应在握手前设置到监听套接字或服务端连接套接字。0 表示对新签发票据保持禁用 0-RTT；任何非零值均启用。按照 [RFC 9001](https://datatracker.ietf.org/doc/html/rfc9001.html) 第 4.6.1 节，票据始终通告固定哨兵值（Sentinel）`0xffffffff`，恢复会话的客户端可发送的早期数据量由连接的流量控制／传输参数限制，而不是由此值限制。因此本选项只是启用开关，不是字节上限。它仅影响新签发的票据；应用仍须在协议层把已接受的早期数据视为可被重放的数据。非零值要求启用 `CONFIG_QUIC_0RTT`，否则 `setsockopt()` 以 `ENOTSUP` 失败。 |
| `ZSOCK_QUIC_SO_STREAM_EARLY_DATA` | 查询 QUIC 流是否收到过被接受的 0-RTT 数据。 选项值为指向 `int` 的指针，仅对 QUIC 流套接字有效。非零结果表示此流的接收侧在当前连接上已经携带过被接受的早期数据。 |

<a id="ga290d25ba3fe401d61b0c35556e67a04c"></a>

### `quic_stream_direction`

```c
enum quic_stream_direction
```

```c
#include <zephyr/net/quic.h>
```

流方向（Stream Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `QUIC_STREAM_BIDIRECTIONAL` | 双向流（Bidirectional Stream）。 |
| `QUIC_STREAM_UNIDIRECTIONAL` | 单向流（Unidirectional Stream）。 |

<a id="ga8c36dbae839efb95be6ea6a8c98f8847"></a>

### `quic_stream_initiator`

```c
enum quic_stream_initiator
```

```c
#include <zephyr/net/quic.h>
```

流发起者（Stream Initiator）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `QUIC_STREAM_CLIENT` | 客户端发起的流（Client-Initiated Stream）。 |
| `QUIC_STREAM_SERVER` | 服务端发起的流（Server-Initiated Stream）。 |

<a id="gade13e997f7a3f9c79590c56ef2bb72c3"></a>

### `quic_connection_close()`

```c
int quic_connection_close ( int sock)
```

```c
#include <zephyr/net/quic.h>
```

关闭 QUIC 套接字。

关闭连接并终止 TLS 会话。对连接套接字执行的操作与 `zsock_close` 相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 要关闭的 QUIC 连接套接字。 |

**返回（Returns）**：成功返回 0，失败返回小于 0 的值。

<a id="gac5b95872bf7fa74b7a1d2c7b011fd99f"></a>

### `quic_connection_open()`

```c
int quic_connection_open ( const struct net_sockaddr * remote_addr, const struct net_sockaddr * local_addr )
```

```c
#include <zephyr/net/quic.h>
```

创建新的 QUIC 连接套接字（Connection Socket）。

创建新的 QUIC 连接上下文（Connection Context），作为后续全部通信的基础。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `remote_addr` | 远程连接端点地址（Remote Endpoint Address）。客户端模式下，是要连接的服务端地址；服务端模式下，绑定监听者时为 `NULL` 或未指定。 |
| `local_addr` | 本地连接端点地址（Local Endpoint Address）。客户端模式下，若为 `NULL`，系统自动选择本地地址并将套接字绑定到临时端口（Ephemeral Port）；服务端模式下，是要监听的地址。 |

**返回（Returns）**：成功返回新 QUIC 连接套接字，失败返回小于 0 的值。

> 译注（源码核对）：[官方套接字实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/quic_socket.c)对客户端先返回连接描述符，首次打开流时再启动握手，使应用有机会先设置证书和 ALPN。返回非负连接描述符不等于 TLS 握手已经成功。服务端通过连接套接字接受流的流程见[指南](P143_QUIC传输接口.md)。

<a id="ga19d171ac47d79394d58b371b43585786"></a>

### `quic_is_connection_socket()`

```c
bool quic_is_connection_socket ( int sock)
```

```c
#include <zephyr/net/quic.h>
```

检查给定套接字是否为 QUIC 连接套接字。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 要检查的套接字。 |

**返回（Returns）**：若该套接字为 QUIC 连接套接字，返回 `true`，否则返回 `false`。

<a id="ga520012661ae348538e817e3cfed35a70"></a>

### `quic_is_stream_socket()`

```c
bool quic_is_stream_socket ( int sock)
```

```c
#include <zephyr/net/quic.h>
```

检查给定套接字是否为 QUIC 流套接字。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 要检查的套接字。 |

**返回（Returns）**：若该套接字为 QUIC 流套接字，返回 `true`，否则返回 `false`。

<a id="gae1501fa858907f12bd308442425ebeeb"></a>

### `quic_stream_close()`

```c
int quic_stream_close ( int sock)
```

```c
#include <zephyr/net/quic.h>
```

关闭 QUIC 流套接字。

关闭指定流，不关闭底层连接。对流套接字执行的操作与 `zsock_close` 相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 要关闭的 QUIC 流套接字。 |

**返回（Returns）**：成功返回 0，失败返回小于 0 的值。

<a id="ga6ae488ec3f462f5a15c8b3106f293ad2"></a>

### `quic_stream_get_id()`

```c
int quic_stream_get_id ( int sock, uint64_t * stream_id )
```

```c
#include <zephyr/net/quic.h>
```

取得给定 QUIC 流套接字所关联的流标识（Stream ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 要检查的套接字。 |
| `stream_id` | 指向用于保存流标识的存储位置的指针。 |

**返回（Returns）**：成功返回 0，失败返回小于 0 的值。

> 译注（源码核对）：成功状态由函数返回值给出，64 位 QUIC 流标识写入 `stream_id`，不能把返回的 0 当作流标识。当前实现会写入该指针而不单独检查它是否为 `NULL`，调用者须提供有效可写的 `uint64_t` 对象。套接字描述符与协议流标识是不同对象。

<a id="ga2d32dd11cff3f02426749955f5a72bd8"></a>

### `quic_stream_open()`

```c
int quic_stream_open ( int connection_sock, enum quic_stream_initiator initiator, enum quic_stream_direction direction, uint8_t priority )
```

```c
#include <zephyr/net/quic.h>
```

在已建立的 QUIC 连接内创建新的 QUIC 流套接字（Stream Socket）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `connection_sock` | 要在其上创建流的连接，即 `quic_connection_open()` 返回的套接字标识。 |
| `initiator` | 流发起者，取 `QUIC_STREAM_CLIENT`（客户端）或 `QUIC_STREAM_SERVER`（服务端）。 |
| `direction` | 流方向，单向或双向。`QUIC_STREAM_BIDIRECTIONAL` 表示双方均可读写；`QUIC_STREAM_UNIDIRECTIONAL` 表示仅发起者可写。 |
| `priority` | 用于调度流数据的优先级（Priority Level），范围 0–255。 |

**返回（Returns）**：成功返回新 QUIC 流套接字，失败返回小于 0 的值。

> 译注（源码核对）：当前官方实现会在客户端首次打开流时启动握手；未启用可用的早期数据时，它等待握手完成，超时分支返回 `-ETIMEDOUT`。已准备好 0-RTT 时可在握手尚未完成时返回流，因此原文“已建立的连接”不应理解成所有调用都必须先独立完成 TLS 握手。发起者和方向是两组独立位，不要把“客户端发起”与“双向”混为一项；原文只规定优先级取值 0–255，没有在本页承诺跨连接的公平性或完整调度策略。

## 147.7\_相关源码与使用边界

声明来自 `<zephyr/net/quic.h>`。本仓库的[对应头文件](../../../include/zephyr/net/quic.h)可用于源码追踪，版本可能与官网 `latest` 不同；官方原始头文件及实现的读取摘要见[来源记录](../SOURCES.md)。

> 译注——恢复状态不是任意序列化协议：导出必须等到收到 `NewSessionTicket`，并检查返回结果；仅握手完成还不保证有可恢复票据。`issue_time_ms` 是本地单调时钟，不是 UTC 时间或服务端签发时间。结构含派生 PSK，不能当作普通调试信息公开。不同版本、ABI 或时钟起点之间不能仅凭保存了一份内存字节就假定状态可直接复用；原文只给出本结构和套接字导入／导出接口。0-RTT 的重放与拒绝处理仍由应用按协议承担。

> 译注——错误约定：上述 `quic_*` 辅助接口按各自声明判断负返回值；标准 `zsock_getsockopt()`／`zsock_setsockopt()` 则使用失败返回 `-1` 并设置 `errno` 的套接字约定，不能混淆。当前[官方套接字实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/quic_socket.c)在流上设置 `ZSOCK_QUIC_SO_STOP_SENDING_CODE` 时要求值为 `uint64_t`，长度为 `sizeof(uint64_t)`；查询 `ZSOCK_QUIC_SO_STREAM_TYPE` 或 `ZSOCK_QUIC_SO_STREAM_EARLY_DATA` 的输出长度要求为 `sizeof(int)`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga006f049efb2b5a9e3ff7821434edc93ba5f816ebe05cd77bbe7111337bbce49cc"></a>
<a id="gga006f049efb2b5a9e3ff7821434edc93ba82c17b20fa9ffbfa2ce1430767734d05"></a>
<a id="gga006f049efb2b5a9e3ff7821434edc93ba75de1d0c9aa28a01e0f9c6b36ba2f90f"></a>
<a id="gga006f049efb2b5a9e3ff7821434edc93ba349bcf4a847826cd63e174ceaaa33f1e"></a>
<a id="gga006f049efb2b5a9e3ff7821434edc93bab8ad7ba1d668055e6842651f768ec41b"></a>
<a id="gga006f049efb2b5a9e3ff7821434edc93ba05f712f8a31261e125468735d4c46bc8"></a>
<a id="gga006f049efb2b5a9e3ff7821434edc93ba6222ebc1d597ca2dc9203db51c0bbdfe"></a>
<a id="gga006f049efb2b5a9e3ff7821434edc93baeb6f405c6e2ffa93d3ad64f6ee854b06"></a>
<a id="gga290d25ba3fe401d61b0c35556e67a04caef4a4cac2a980c26800f5ace0e1f5a55"></a>
<a id="gga290d25ba3fe401d61b0c35556e67a04caed835dd5e19cbbf3f9d4e1a98017084f"></a>
<a id="gga8c36dbae839efb95be6ea6a8c98f8847a5c654090eb3849cfc67e62168abb5ae1"></a>
<a id="gga8c36dbae839efb95be6ea6a8c98f8847a5e1a358566686da7522ba96b2c8de3f1"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P146_QUIC回显服务端.md) · [返回大纲](大纲.md) · [下一章](P148_QUIC头文件参考.md)
