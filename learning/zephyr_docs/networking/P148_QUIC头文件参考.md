---
id: learning.zephyr-docs.networking.api-148
title: QUIC头文件参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/quic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第148章\_QUIC头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/quic_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 148.1\_阅读说明与来源

译注：先读[QUIC传输接口指南](P143_QUIC传输接口.md)及[回显示例目录](P144_QUIC示例目录.md)，理解连接套接字、流套接字和 TLS 握手的关系，再按符号查询本组参考。

本组：[完整API参考](P147_QUIC完整API参考.md) · [头文件参考](P148_QUIC头文件参考.md) · [头文件源码](P149_QUIC头文件源码.md) · [会话状态](P150_QUIC会话状态.md) · [会话传输参数](P151_QUIC会话传输参数.md) · [统计数据](P152_QUIC统计数据.md) · [全局统计](P153_QUIC全局统计数据.md)。

Zephyr 的 QUIC 实现。

```c
#include <zephyr/types.h>
```

```c
#include <stddef.h>
```

```c
#include <stdbool.h>
```

```c
#include <zephyr/net/net_ip.h>
```

Zephyr 的 QUIC 实现。

## 148.2\_数据结构（Data Structures）

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

## 148.3\_宏定义（Macros）

<a id="r_gad0638e0b5903257b18ba1ed79103bdc5"></a>

```c
#define ZSOCK_SOL_QUIC 284
```

供 `getsockopt`／`setsockopt` 使用的 QUIC 套接字选项级别（Socket Option Level）。

相关声明：[ZSOCK_SOL_QUIC](P147_QUIC完整API参考.md#gad0638e0b5903257b18ba1ed79103bdc5)。

<a id="r_ga50d0ecc2871e8bafb68d38abb564d295"></a>

```c
#define QUIC_SESSION_STATE_VERSION 2U
```

`struct quic_session_state` 的版本。

相关声明：[QUIC_SESSION_STATE_VERSION](P147_QUIC完整API参考.md#ga50d0ecc2871e8bafb68d38abb564d295)。

<a id="r_ga8f757a00b692d8eaa39536557f326306"></a>

```c
#define QUIC_MAX_SESSION_TICKET_LEN 256U
```

通过 `struct quic_session_state` 导出的序列化票据（Serialized Ticket）的最大长度。

相关声明：[QUIC_MAX_SESSION_TICKET_LEN](P147_QUIC完整API参考.md#ga8f757a00b692d8eaa39536557f326306)。

<a id="r_ga6c21dda81654cab53209bc1dca4909d2"></a>

```c
#define QUIC_MAX_RESUMPTION_PSK_LEN 48U
```

通过 `struct quic_session_state` 导出的会话恢复预共享密钥（Pre-Shared Key，PSK）的最大长度。

相关声明：[QUIC_MAX_RESUMPTION_PSK_LEN](P147_QUIC完整API参考.md#ga6c21dda81654cab53209bc1dca4909d2)。

## 148.4\_枚举（Enumerations）

<a id="r_ga290d25ba3fe401d61b0c35556e67a04c"></a>

```c
enum quic_stream_direction { QUIC_STREAM_BIDIRECTIONAL = 0x00 , QUIC_STREAM_UNIDIRECTIONAL = 0x02 }
```

流方向（Stream Direction）。

相关声明：[quic_stream_direction](P147_QUIC完整API参考.md#ga290d25ba3fe401d61b0c35556e67a04c)、[QUIC_STREAM_BIDIRECTIONAL](P147_QUIC完整API参考.md#gga290d25ba3fe401d61b0c35556e67a04caef4a4cac2a980c26800f5ace0e1f5a55)、[QUIC_STREAM_UNIDIRECTIONAL](P147_QUIC完整API参考.md#gga290d25ba3fe401d61b0c35556e67a04caed835dd5e19cbbf3f9d4e1a98017084f)。

<a id="r_ga8c36dbae839efb95be6ea6a8c98f8847"></a>

```c
enum quic_stream_initiator { QUIC_STREAM_CLIENT = 0x00 , QUIC_STREAM_SERVER = 0x01 }
```

流发起者（Stream Initiator）。

相关声明：[quic_stream_initiator](P147_QUIC完整API参考.md#ga8c36dbae839efb95be6ea6a8c98f8847)、[QUIC_STREAM_CLIENT](P147_QUIC完整API参考.md#gga8c36dbae839efb95be6ea6a8c98f8847a5c654090eb3849cfc67e62168abb5ae1)、[QUIC_STREAM_SERVER](P147_QUIC完整API参考.md#gga8c36dbae839efb95be6ea6a8c98f8847a5e1a358566686da7522ba96b2c8de3f1)。

<a id="r_ga006f049efb2b5a9e3ff7821434edc93b"></a>

```c
enum { ZSOCK_QUIC_SO_STREAM_TYPE = 1 , ZSOCK_QUIC_SO_CERT_CHAIN_ADD = 2 , ZSOCK_QUIC_SO_CERT_CHAIN_DEL = 3 , ZSOCK_QUIC_SO_STOP_SENDING_CODE = 4 , ZSOCK_QUIC_SO_SESSION_STATE = 5 , ZSOCK_QUIC_SO_SESSION_TICKET_ENABLE = 6 , ZSOCK_QUIC_SO_MAX_EARLY_DATA_SIZE = 7 , ZSOCK_QUIC_SO_STREAM_EARLY_DATA = 8 }
```

在 `ZSOCK_SOL_QUIC` 级别通过 `getsockopt`／`setsockopt` 使用的 QUIC 套接字选项。

相关声明：[ZSOCK_QUIC_SO_STREAM_TYPE](P147_QUIC完整API参考.md#gga006f049efb2b5a9e3ff7821434edc93ba5f816ebe05cd77bbe7111337bbce49cc)、[ZSOCK_QUIC_SO_CERT_CHAIN_ADD](P147_QUIC完整API参考.md#gga006f049efb2b5a9e3ff7821434edc93ba82c17b20fa9ffbfa2ce1430767734d05)、[ZSOCK_QUIC_SO_CERT_CHAIN_DEL](P147_QUIC完整API参考.md#gga006f049efb2b5a9e3ff7821434edc93ba75de1d0c9aa28a01e0f9c6b36ba2f90f)、[ZSOCK_QUIC_SO_STOP_SENDING_CODE](P147_QUIC完整API参考.md#gga006f049efb2b5a9e3ff7821434edc93ba349bcf4a847826cd63e174ceaaa33f1e)、[ZSOCK_QUIC_SO_SESSION_STATE](P147_QUIC完整API参考.md#gga006f049efb2b5a9e3ff7821434edc93bab8ad7ba1d668055e6842651f768ec41b)、[ZSOCK_QUIC_SO_SESSION_TICKET_ENABLE](P147_QUIC完整API参考.md#gga006f049efb2b5a9e3ff7821434edc93ba05f712f8a31261e125468735d4c46bc8)、[ZSOCK_QUIC_SO_MAX_EARLY_DATA_SIZE](P147_QUIC完整API参考.md#gga006f049efb2b5a9e3ff7821434edc93ba6222ebc1d597ca2dc9203db51c0bbdfe)、[ZSOCK_QUIC_SO_STREAM_EARLY_DATA](P147_QUIC完整API参考.md#gga006f049efb2b5a9e3ff7821434edc93baeb6f405c6e2ffa93d3ad64f6ee854b06)。

## 148.5\_函数（Functions）

<a id="r_gac5b95872bf7fa74b7a1d2c7b011fd99f"></a>

```c
int quic_connection_open (const struct net_sockaddr *remote_addr, const struct net_sockaddr *local_addr)
```

创建新的 QUIC 连接套接字（Connection Socket）。

相关声明：[quic_connection_open](P147_QUIC完整API参考.md#gac5b95872bf7fa74b7a1d2c7b011fd99f)。

<a id="r_gade13e997f7a3f9c79590c56ef2bb72c3"></a>

```c
int quic_connection_close (int sock)
```

关闭 QUIC 套接字。

相关声明：[quic_connection_close](P147_QUIC完整API参考.md#gade13e997f7a3f9c79590c56ef2bb72c3)。

<a id="r_ga2d32dd11cff3f02426749955f5a72bd8"></a>

```c
int quic_stream_open (int connection_sock, enum quic_stream_initiator initiator, enum quic_stream_direction direction, uint8_t priority)
```

在已建立的 QUIC 连接内创建新的 QUIC 流套接字（Stream Socket）。

相关声明：[quic_stream_open](P147_QUIC完整API参考.md#ga2d32dd11cff3f02426749955f5a72bd8)、[quic_stream_initiator](P147_QUIC完整API参考.md#ga8c36dbae839efb95be6ea6a8c98f8847)、[quic_stream_direction](P147_QUIC完整API参考.md#ga290d25ba3fe401d61b0c35556e67a04c)。

<a id="r_gae1501fa858907f12bd308442425ebeeb"></a>

```c
int quic_stream_close (int sock)
```

关闭 QUIC 流套接字。

相关声明：[quic_stream_close](P147_QUIC完整API参考.md#gae1501fa858907f12bd308442425ebeeb)。

<a id="r_ga520012661ae348538e817e3cfed35a70"></a>

```c
bool quic_is_stream_socket (int sock)
```

检查给定套接字是否为 QUIC 流套接字。

相关声明：[quic_is_stream_socket](P147_QUIC完整API参考.md#ga520012661ae348538e817e3cfed35a70)。

<a id="r_ga19d171ac47d79394d58b371b43585786"></a>

```c
bool quic_is_connection_socket (int sock)
```

检查给定套接字是否为 QUIC 连接套接字。

相关声明：[quic_is_connection_socket](P147_QUIC完整API参考.md#ga19d171ac47d79394d58b371b43585786)。

<a id="r_ga6ae488ec3f462f5a15c8b3106f293ad2"></a>

```c
int quic_stream_get_id (int sock, uint64_t *stream_id)
```

取得给定 QUIC 流套接字所关联的流标识（Stream ID）。

相关声明：[quic_stream_get_id](P147_QUIC完整API参考.md#ga6ae488ec3f462f5a15c8b3106f293ad2)。

## 148.6\_相关源码与使用边界

声明来自 `<zephyr/net/quic.h>`。本仓库的[对应头文件](../../../include/zephyr/net/quic.h)可用于源码追踪，版本可能与官网 `latest` 不同；官方原始头文件及实现的读取摘要见[来源记录](../SOURCES.md)。

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

[上一章](P147_QUIC完整API参考.md) · [返回大纲](大纲.md) · [下一章](P149_QUIC头文件源码.md)
