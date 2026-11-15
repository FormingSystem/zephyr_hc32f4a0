---
id: learning.zephyr-docs.networking.page-40
title: BSD套接字
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/sockets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_BSD套接字

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/sockets.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 40.1 概览（Overview）

Zephyr 实现了 BSD 套接字（BSD Sockets）应用编程接口（Application Programming Interface，API）的一个子集；该接口属于 POSIX 标准的一部分。它让开发者能够复用已有网络编程经验，把简单的现有网络应用移植到 Zephyr。

这套实现遵循两个主要要求：尽量减小开销，与其他 Zephyr 子系统保持一致；默认采用独立的名称空间（Namespace），避免与 C 标准库（libc）或其他 POSIX 兼容库中的 `close()` 等常见函数名冲突。启用 [`CONFIG_POSIX_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API) 后，还会暴露 POSIX 兼容接口。

通过 [`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS) 启用 BSD 套接字兼容接口。支持的操作包括 [`socket()`](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a4dcc080bfb18d95d173bc205084f8b0a)、`close()`、`recv()`、`recvfrom()`、`send()`、`sendto()`、`connect()`、`bind()`、`listen()`、`accept()`、`fcntl()`（用于设置非阻塞模式）、`getsockopt()`、[`setsockopt()`](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a71c8788caef89a362e35ce5855e77077)、`poll()`、`select()`、`getaddrinfo()` 和 `getnameinfo()`。

默认函数名称带有 `zsock_` 前缀，例如 [`zsock_socket()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5693d19a0bdff45a5cb09227683d8631) 和 [`zsock_close()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae60d7ca486955dd79a2821d1f646c349)。启用 [`CONFIG_POSIX_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API) 后，所有这些函数还会提供不带前缀的别名，包括可能与 libc、文件系统库等发生名称冲突的 `close()` 和 `fcntl()`。

为降低复杂度和开销，Zephyr 会尽可能利用 POSIX 接口允许的短读／短写（Short Read / Short Write）行为。对于 `SOCK_STREAM` 流式套接字，一次 `recv()` 或 `send()` 实际接收或发送的数据可以少于应用请求的数量。例如，原文写作 `recv(sock, 1000, 0)` 的调用可能返回 `100`，表示只读到 100 字节；应用需要继续调用以接收剩余 900 字节。

> 译注：原文上述调用省略了接收缓冲区参数，只用于说明短读；实际接口应传入缓冲区，如 `recv(sock, buf, 1000, 0)`。不要把原文简写直接作为可编译代码。

BSD 套接字 API 用文件描述符（File Descriptor）表示套接字。文件描述符是从零开始分配的小整数，与文件、标准输入／标准输出（stdin/stdout）等特殊设备共享。内部表格将描述符映射到具体对象指针。即使没有启用其余 POSIX 子系统，例如文件系统及 stdin/stdout，BSD 套接字仍使用这张文件描述符表。

Zephyr 支持以下套接字类型。其中地址族（Address Family）表示通信地址类别，协议（Protocol）决定具体的协议实现。

| 地址族 | 类型 | 协议 | 配置与用途 |
| --- | --- | --- | --- |
| `AF_INET`、`AF_INET6` | `SOCK_DGRAM` | `IPPROTO_UDP` | 启用 [`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP) 后，收发用户数据报协议（User Datagram Protocol，UDP）数据报 |
| `AF_INET`、`AF_INET6` | `SOCK_DGRAM` | `IPPROTO_DTLS_1_x` | 启用 [`CONFIG_NET_SOCKETS_ENABLE_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_ENABLE_DTLS) 后，收发数据报传输层安全（Datagram Transport Layer Security，DTLS）数据报 |
| `AF_INET`、`AF_INET6` | `SOCK_STREAM` | `IPPROTO_TCP` | 启用 [`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP) 后，收发传输控制协议（Transmission Control Protocol，TCP）数据流 |
| `AF_INET`、`AF_INET6` | `SOCK_STREAM` | `IPPROTO_TLS_1_x` | 启用 [`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS) 后，收发传输层安全（Transport Layer Security，TLS）数据流 |
| `AF_INET`、`AF_INET6` | `SOCK_RAW` | `IPPROTO_IP`、`<proto>` | 启用 [`CONFIG_NET_SOCKETS_INET_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_INET_RAW) 后，收发 IPv4/IPv6 数据报；按指定的第四层（L4）协议过滤，`IPPROTO_IP` 是接收所有 IP 数据报的通配协议 |
| `AF_PACKET` | `SOCK_DGRAM` | `ETH_P_ALL`、`<proto>` | 启用 [`CONFIG_NET_SOCKETS_PACKET_DGRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET_DGRAM) 后，收发不带第二层（L2）头部的分组；按指定的第三层（L3）协议过滤，`ETH_P_ALL` 是接收所有分组的通配协议 |
| `AF_PACKET` | `SOCK_RAW` | `ETH_P_ALL` | 启用 [`CONFIG_NET_SOCKETS_PACKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET) 后，收发包含 L2 头部的分组 |
| `AF_CAN` | `SOCK_RAW` | `CAN_RAW` | 启用 [`CONFIG_NET_SOCKETS_CAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_CAN) 后，收发控制器局域网（Controller Area Network，CAN）分组 |

简单的客户端和服务器创建方法，见[高级回显服务器（Echo Server）](P047_高级回显服务器示例.md#sockets-echo-server)与[高级回显客户端（Echo Client）](P048_高级回显客户端示例.md#sockets-echo-client)示例。

## 40.2 IPv4 与 IPv6 套接字选项（Socket Options）

Zephyr 通过 [`zsock_setsockopt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga71ac8d52c87b9182a9f1a03614e3dba7) 和 [`zsock_getsockopt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga6aa12f0dbed8ded425555debba044a98) 支持 IP 层套接字选项。IPv4 的协议级别为 `NET_IPPROTO_IP`，IPv6 为 `NET_IPPROTO_IPV6`。选项是否可用，可能取决于 Kconfig 设置和套接字地址族。

选项列表分别见[IPv4 套接字选项](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv4__socket__options.html)与[IPv6 套接字选项](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv6__socket__options.html)。

QUIC 协议栈在基于数据报的分组化层路径最大传输单元发现（Datagram Packetization Layer Path MTU Discovery，DPLPMTUD）探测期间，会在内部使用 [`ZSOCK_IP_DONTFRAG`](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv4__socket__options.html#ga3c8f7f8895a3daae11dcd439eb2499a3) 和 [`ZSOCK_IPV6_DONTFRAG`](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv6__socket__options.html#ga44b16e54bc2922153e9a07d628cf1cba)。参见[路径 MTU 发现（DPLPMTUD）](P143_QUIC传输接口.md#quic-dplpmtud)。

## 40.3 安全套接字（Secure Sockets）

Zephyr 扩展了标准 POSIX 套接字 API，允许创建并配置 TLS 协议类型的套接字以实现安全通信。底层安全功能由 Mbed TLS 库提供，应用可以用标准套接字调用操作 TLS 和 DTLS。支持的安全协议版本见 [`net_ip_protocol_secure`](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga721da18d2a3cfd9b3a56e9efc9f6e58b) 类型。

通过 [`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS) 启用安全套接字；通过 [`CONFIG_NET_SOCKETS_ENABLE_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_ENABLE_DTLS) 启用 DTLS 支持。

### TLS 凭据子系统（TLS Credentials Subsystem）

TLS 凭据（Credential）在安全套接字使用之前必须先注册到系统，详情见 [`tls_credential_add()`](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga640ff6dd3eb4d5017feaab6fab2bb2f7)。每项凭据注册时会关联一个 [`sec_tag_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3) 类型的数值标签（Tag），之后可以在安全套接字选项中通过标签引用该凭据。

可以注册以下类型：

| 类型 | 含义 |
| --- | --- |
| `TLS_CREDENTIAL_CA_CERTIFICATE` | 证书颁发机构（Certificate Authority，CA）证书 |
| `TLS_CREDENTIAL_PUBLIC_CERTIFICATE` | 公共证书（Public Certificate） |
| `TLS_CREDENTIAL_PRIVATE_KEY` | 私钥（Private Key） |
| `TLS_CREDENTIAL_PSK` | 预共享密钥（Pre-Shared Key，PSK） |
| `TLS_CREDENTIAL_PSK_ID` | 预共享密钥标识（PSK Identity） |

例如，注册 `ca_certificate` 数组提供的 CA 证书：

```c
ret = tls_credential_add(CA_CERTIFICATE_TAG, TLS_CREDENTIAL_CA_CERTIFICATE,
                         ca_certificate, sizeof(ca_certificate));
```

默认支持可辨别编码规则（Distinguished Encoding Rules，DER）格式的证书。隐私增强邮件（Privacy-Enhanced Mail，PEM）格式支持可在 Mbed TLS 设置中启用。

### 创建安全套接字（Secure Socket Creation）

创建时指定安全协议类型，例如：

```c
sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TLS_1_2);
```

创建安全套接字时指定的协议版本，表示 TLS 会话允许使用的最低版本。

创建后可以通过套接字选项进行配置。例如，先指定 CA 证书标签：

```c
sec_tag_t sec_tag_opt[] = {
        CA_CERTIFICATE_TAG,
};

ret = setsockopt(sock, SOL_TLS, TLS_SEC_TAG_LIST,
                 sec_tag_opt, sizeof(sec_tag_opt));
```

再设置主机名（Hostname）：

```c
char host[] = "google.com";

ret = setsockopt(sock, SOL_TLS, TLS_HOSTNAME, host, sizeof(host));
```

配置完成后即可像普通 TCP 套接字一样使用。

> 原文注意事项：由于 Mbed TLS 内部数据缓冲机制及 `mbedtls_ssl_write()` 的要求，非阻塞 [`zsock_send()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2d8c2173986f67dde6dc5721bf690855) 遇到 `EAGAIN` 时，紧接着重试的 [`zsock_send()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2d8c2173986f67dde6dc5721bf690855) 必须使用与原调用相同的数据。
>
> 译注：这里的“返回 `EAGAIN`”描述的是错误条件；BSD 套接字调用失败时返回 `-1`，具体错误从 `errno` 读取。最低 TLS 版本及发送重试说明已对照官方 [`sockets_tls.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/sockets_tls.c) 和 [`socket.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/socket.h) 核对，未实际建立 TLS 连接。

Zephyr 中多个示例使用安全套接字进行通信，例如[回显服务器示例](P047_高级回显服务器示例.md#sockets-echo-server)和[HTTP GET 示例](P051_普通套接字HTTP_GET示例.md#sockets-http-get)。

### 安全套接字选项（Secure Sockets Options）

管理安全套接字的选项见[TLS 套接字选项](https://docs.zephyrproject.org/latest/doxygen/html/group__secure__sockets__options.html)。相关示例包括[HTTP 客户端（HTTP Client）](P050_HTTP客户端示例.md#sockets-http-client)，演示发出多种 HTTP 请求；以及[使用普通套接字的 HTTP GET](P051_普通套接字HTTP_GET示例.md#sockets-http-get)，演示通过普通 BSD 套接字实现 HTTP(S) 客户端。HTTP 指超文本传输协议（Hypertext Transfer Protocol），HTTPS 是通过 TLS 保护的 HTTP 通信。

## 40.4 套接字卸载（Socket Offloading）

Zephyr 允许注册自定义套接字实现，称为卸载套接字（Offloaded Socket）。对于自身提供外部 IP 协议栈及类似套接字 API 的设备，这种方式可以将其集成进 Zephyr。

通过 [`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD) 启用套接字卸载。网络驱动使用 `NET_SOCKET_OFFLOAD_REGISTER` 注册新实现，参数如下：

| 参数 | 含义 |
| --- | --- |
| `socket_name` | 该套接字实现的任意名称 |
| `prio` | 实现优先级；优先级越高，创建新套接字时越早考虑该实现。数值越小，优先级越高 |
| `_family` | 实现支持的套接字地址族；`AF_UNSPEC` 表示任意地址族 |
| `_is_supported` | 过滤函数，用于检查该实现是否支持指定的地址族、类型和协议 |
| `_handler` | 与 [`socket()`](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a4dcc080bfb18d95d173bc205084f8b0a) API 兼容的函数，用于创建卸载套接字 |

每个卸载套接字实现还应提供 `socket_op_vtable` 结构体定义的一组套接字操作。

注册的创建函数应先调用 [`zvfs_reserve_fd()`](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a0805f751464ff9a51a463841ce35ff5f) 分配新文件描述符，再执行该卸载实现特有的创建动作。若创建成功，最后用 [`zvfs_finalize_typed_fd()`](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a448172e130af96c11af2fe6511e6b262) 或 [`zvfs_finalize_fd()`](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a0bb7c530d69c9e5b1cfc61e7a11441af) 完成描述符设置。这一步注册实现套接字 API 的 `socket_op_vtable`，并可附带套接字上下文（Context）数据指针。

卸载网络接口初始化时，还应通过 [`net_if_socket_offload_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9db52875580115c743b1f35cd6c46796) 表明该接口使用套接字卸载。这个函数将创建卸载套接字的函数注册到网络接口；它与传给 `NET_SOCKET_OFFLOAD_REGISTER` 的创建函数相同。

### 卸载套接字的创建过程（Offloaded Socket Creation）

应用调用 [`socket()`](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a4dcc080bfb18d95d173bc205084f8b0a) 时，网络协议栈按优先级遍历所有已注册的原生（Native）及卸载实现。对每个实现，先检查地址族是否匹配，或该实现是否注册为 `AF_UNSPEC`；若匹配，再调用 `_is_supported` 检查其余参数。第一个满足要求、即 `_is_supported` 返回 `true` 的实现，会通过其 `_handler` 创建套接字。

因此，当多个实现支持同一组地址族、类型和协议时，最先被检查的匹配实现会创建套接字。应当把最高优先级赋给希望作为系统默认值的实现。

原生实现的优先级由 Kconfig 配置：[`CONFIG_NET_SOCKETS_TLS_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_TLS_PRIORITY) 设置原生 TLS 套接字的优先级，[`CONFIG_NET_SOCKETS_PRIORITY_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PRIORITY_DEFAULT) 设置其余原生套接字的优先级。

### 多个卸载接口的处理（Multiple Offloaded Interfaces）

[`socket()`](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a4dcc080bfb18d95d173bc205084f8b0a) 无法指定网络接口。若多个卸载实现支持相同类型的套接字，调用者不能仅通过这个函数选择某个实现；原生与卸载实现同时可用时也有相同问题。

套接字分派器（Socket Dispatcher）是一种特殊实现，用于把真正的套接字创建推迟到第一次套接字操作发生时。这使应用有机会先使用 `SO_BINDTODEVICE` 将套接字绑定到某个网络接口，从而确定相应的卸载实现。通过 [`CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER) 启用分派器。

启用后，应用可以使用 [`setsockopt()`](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a71c8788caef89a362e35ce5855e77077) 指定网络接口：

```c
/* A "dispatcher" socket is created */
sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

struct ifreq ifreq = {
   .ifr_name = "SimpleLink"
};

/* The socket is "dispatched" to a particular network interface
 * (offloaded or not).
 */
setsockopt(sock, SOL_SOCKET, SO_BINDTODEVICE, &ifreq, sizeof(ifreq));
```

代码先创建分派器套接字，再以 `SO_BINDTODEVICE` 将其分派给名为 `SimpleLink` 的网络接口；该接口可以使用卸载实现，也可以使用原生实现。

如果原生与卸载实现都支持 TLS，可以先使用 `TLS_NATIVE` 指定原生 TLS，再把它依赖的底层套接字绑定到某个网络接口：

```c
/* A "dispatcher" socket is created */
sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TLS_1_2);

int tls_native = 1;

/* The socket is "dispatched" to a native TLS socket implmeentation.
 * The underlying socket is a "dispatcher" socket now.
 */
setsockopt(sock, SOL_TLS, TLS_NATIVE, &tls_native, sizeof(tls_native));

struct ifreq ifreq = {
   .ifr_name = "SimpleLink"
};

/* The underlying socket is "dispatched" to a particular network interface
 * (offloaded or not).
 */
setsockopt(sock, SOL_SOCKET, SO_BINDTODEVICE, &ifreq, sizeof(ifreq));
```

这里第一次分派选择原生 TLS 实现，其底层仍是分派器套接字；第二次分派通过 `SO_BINDTODEVICE` 确定底层网络接口。

若没有使用 `SO_BINDTODEVICE`，第一次套接字 API 调用发生时，将按默认优先级与过滤规则进行分派。

## 40.5 API 参考与相关示例（API Reference）

完整接口分别见[BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)与[TLS 凭据管理](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)。这两份 API 参考按独立页面跟踪，本章指南完成不表示参考页也已译完。

### BSD 套接字相关示例

| 示例 | 原文说明 |
| --- | --- |
| [使用 poll() 的异步回显服务器](P045_poll异步回显示例.md#async-sockets-echo) | 用 BSD 套接字和 `poll()` 实现异步 IPv4/IPv6 TCP 回显服务器 |
| [使用 select() 的异步回显服务器](P046_select异步回显示例.md#async-sockets-echo-select) | 用 BSD 套接字和 `select()` 实现异步 IPv4/IPv6 TCP 回显服务器 |
| [AWS IoT Core MQTT](P216_AWS物联网MQTT示例.md#aws-iot-mqtt) | 连接 AWS IoT Core，使用消息队列遥测传输（Message Queuing Telemetry Transport，MQTT）发布消息 |
| [简易 HTTP 服务器](P057_简易HTTP服务器示例.md#socket-dumb-http-server) | 用 BSD 套接字实现简单、可移植的 HTTP 服务器 |
| [多线程简易 HTTP 服务器](P058_多线程HTTP服务器示例.md#socket-dumb-http-server-mt) | 用 BSD 套接字实现支持同时连接的简单 HTTP 服务器 |
| [高级回显客户端](P048_高级回显客户端示例.md#sockets-echo-client) | 发送 IP 分组，等待返回的数据并验证 |
| [高级回显服务器](P047_高级回显服务器示例.md#sockets-echo-server) | 实现 UDP/TCP 服务器，把收到的分组发回发送方 |
| [套接字服务回显服务器](P043_套接字服务回显示例.md#sockets-service-echo) | 用 BSD 套接字和套接字服务 API 实现简单的 IPv4/IPv6 TCP 回显服务器 |
| [简单回显服务器](P044_简单回显服务器示例.md#sockets-echo) | 用 BSD 套接字实现简单的 IPv4/IPv6 TCP 回显服务器 |
| [HTTP 客户端](P050_HTTP客户端示例.md#sockets-http-client) | 实现发出多种 HTTP 请求的 HTTP(S) 客户端 |
| [使用普通套接字的 HTTP GET](P051_普通套接字HTTP_GET示例.md#sockets-http-get) | 通过普通 BSD 套接字实现 HTTP(S) 客户端 |
| [HTTP 大文件下载](P052_HTTP大文件下载示例.md#sockets-big-http-download) | 通过 BSD 套接字从 Web 服务器下载大文件 |
| [mDNS 响应器](P200_mDNS响应器示例.md#mdns-responder) | 监听并响应多播域名系统（Multicast DNS，mDNS）查询 |
| [Microsoft Azure IoT Hub MQTT](P217_Azure物联网MQTT示例.md#mqtt-azure) | 连接 Azure IoT Hub，通过 MQTT 发布消息 |
| [Modbus TCP 服务器](https://docs.zephyrproject.org/latest/samples/subsys/modbus/tcp_server/README.html#modbus-tcp-server) | 提供 Modbus 命令以控制发光二极管（Light-Emitting Diode，LED） |
| [Modbus TCP 到串行网关](https://docs.zephyrproject.org/latest/samples/subsys/modbus/tcp_gateway/README.html#modbus-gateway) | 在以太网 TCP/IP 网络与 Modbus 串行线路之间建立网关 |
| [网络管理套接字](P204_网络管理套接字示例.md#sockets-net-mgmt) | 通过网络管理套接字监听网络管理事件 |
| [分组套接字](P133_数据包套接字示例.md#packet-socket) | 在以太网上使用原始分组套接字（Raw Packet Socket） |
| [SNTP 客户端](P038_SNTP客户端示例.md#sntp-client) | 使用简单网络时间协议（Simple Network Time Protocol，SNTP）获取主机的当前时间 |
| [SNTP 服务器](P039_SNTP服务器示例.md#sntp-server) | 向网络中的 SNTP 客户端提供当前时间 |
| [SocketCAN](P206_SocketCAN示例.md#socket-can) | 通过 BSD 套接字 API 收发原始 CAN 帧 |
| [套接字对（Socket Pair）](P205_套接字对示例.md#sockets-socketpair) | 使用套接字对实现线程间通信 |
| [TagoIO HTTP POST](P218_TagoIO的HTTP上报示例.md#tagoio-http-post) | 通过 HTTP 向 TagoIO 物联网（Internet of Things，IoT）云平台发送随机温度值 |
| [使用 SO_TXTIME 的 UDP 发送方](P134_SO_TXTIME定时发送示例.md#so_txtime) | 通过 `SO_TXTIME` 套接字选项控制分组发送时间 |
| [视频 TCP 服务器输出端](https://docs.zephyrproject.org/latest/samples/subsys/video/tcpserversink/README.html#video-tcpserversink) | 捕获视频帧并通过网络发给 TCP 客户端 |
| [WebSocket 客户端](P054_WebSocket客户端示例.md#sockets-websocket-client) | 实现连接到 WebSocket 服务器的客户端 |
| [Wireguard VPN](P211_WireGuard虚拟专用网示例.md#wireguard-vpn) | 实现通过 Wireguard 虚拟专用网（Virtual Private Network，VPN）连接把分组发回发送方的回显服务器 |

### TLS 凭据相关示例

原文 TLS 凭据部分另外列出以下相关示例；这里保留这一关联关系及用途。

| 示例 | 原文说明 |
| --- | --- |
| [AWS IoT Core MQTT](P216_AWS物联网MQTT示例.md#aws-iot-mqtt) | 连接 AWS IoT Core，通过 MQTT 发布消息 |
| [多线程简易 HTTP 服务器](P058_多线程HTTP服务器示例.md#socket-dumb-http-server-mt) | 用 BSD 套接字实现支持同时连接的简单 HTTP 服务器 |
| [高级回显客户端](P048_高级回显客户端示例.md#sockets-echo-client) | 发送 IP 分组，等待返回并验证 |
| [高级回显服务器](P047_高级回显服务器示例.md#sockets-echo-server) | 通过 UDP/TCP 将收到的分组发回发送方 |
| [HTTP 客户端](P050_HTTP客户端示例.md#sockets-http-client) | 发出多种 HTTP 请求的 HTTP(S) 客户端 |
| [使用普通套接字的 HTTP GET](P051_普通套接字HTTP_GET示例.md#sockets-http-get) | 通过普通 BSD 套接字实现 HTTP(S) 客户端 |
| [HTTP 服务器](P056_HTTP服务器示例.md#sockets-http-server) | 实现展示多种资源类型的 HTTP(S) 服务器 |
| [HTTP 大文件下载](P052_HTTP大文件下载示例.md#sockets-big-http-download) | 通过 BSD 套接字从 Web 服务器下载大文件 |
| [Microsoft Azure IoT Hub MQTT](P217_Azure物联网MQTT示例.md#mqtt-azure) | 连接 Azure IoT Hub，通过 MQTT 发布消息 |
| [Prometheus 示例](P220_Prometheus指标示例.md#prometheus) | 实现展示多种指标类型（Metric Type）的 Prometheus 指标服务器 |
| [TagoIO HTTP POST](P218_TagoIO的HTTP上报示例.md#tagoio-http-post) | 通过 HTTP 向 TagoIO IoT 云平台发送随机温度值 |


<a id="bsd-sockets"></a>
<a id="bsd-sockets-interface"></a>
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
<a id="overview"></a>
<a id="ipv4-and-ipv6-socket-options"></a>
<a id="ip-socket-options"></a>
<a id="ipv4-options"></a>
<a id="ipv6-options"></a>
<a id="secure-sockets"></a>
<a id="secure-sockets-interface"></a>
<a id="tls-credentials-subsystem"></a>
<a id="sockets-tls-credentials-subsys"></a>
<a id="secure-socket-creation"></a>
<a id="secure-sockets-options"></a>
<a id="socket-offloading"></a>
<a id="offloaded-socket-creation"></a>
<a id="dealing-with-multiple-offloaded-interfaces"></a>
<a id="api-reference"></a>
<a id="id1"></a>
<a id="tls-credentials"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：SNTP时间同步库](P034_SNTP时间同步库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：套接字服务](P041_套接字服务.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P039_SNTP服务器示例.md) · [返回大纲](大纲.md) · [下一章](P041_套接字服务.md)

</details>

<!-- reading-navigation:end -->
