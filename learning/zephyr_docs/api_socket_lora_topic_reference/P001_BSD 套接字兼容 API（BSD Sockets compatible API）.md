---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-1
title: BSD 套接字兼容 API（BSD Sockets compatible API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_BSD 套接字兼容 API（BSD Sockets compatible API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BSD 套接字兼容 API（BSD Sockets compatible API）

<a id="details"></a>

兼容 BSD 套接字（BSD Sockets）的 API。起始版本（Since）：1.9。版本（Version）：1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_ipv4_5Fsocket_5Foptions"></a>

相关声明：[IPv4 套接字选项（Socket options）](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md)。

<a id="r_ipv6_5Fsocket_5Foptions"></a>

相关声明：[IPv6 套接字选项（Socket options）](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md)。

<a id="r_secure_5Fsockets_5Foptions"></a>

相关声明：[TLS 套接字选项（Socket options）](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md)。

<a id="r_packet_5Fsocket_5Foptions"></a>

相关声明：[分组套接字的套接字选项（Socket options for packet socket）](../api_extension_topic_reference/P022_分组套接字的套接字选项（Socket options for packet socket）.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.2\_数据结构（Data Structures）

<a id="r_zsock_5Faddrinfo"></a>

```c
struct zsock_addrinfo
```

相关声明：[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

查询地址信息（Address Information）时使用的定义。

<a id="r_zsock_5Fpollfd"></a>

```c
struct zsock_pollfd
```

相关声明：[zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)。

被监测套接字/文件描述符（Socket / File Descriptor）的定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.3\_宏定义（Macros）

<a id="r_ga5c88da69b8d9401d3ae02495056f7e23"></a>

```c
#define ZSOCK_FD_SETSIZE ZVFS_FD_SETSIZE
```

相关声明：[ZSOCK_FD_SETSIZE](#ga5c88da69b8d9401d3ae02495056f7e23)、[ZVFS_FD_SETSIZE](../api_file_media_sensor_reference/P003_zephyr__sys__fdtable.h_文件参考.md#ae8d10dc8bd02e619f8c384c493f53709)。

可添加到 `zsock_fd_set` 中的文件描述符数量。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.4\_类型定义（Typedefs）

<a id="r_ga1cdeeddce9000b9fd29b638c422f48f8"></a>

```c
typedef struct zvfs_fd_set zsock_fd_set
```

相关声明：[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)、[zsock_fd_set](#ga1cdeeddce9000b9fd29b638c422f48f8)。

套接字文件描述符集合（socket file descriptor set）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_ga21a871d1fa6b6beeed88408761877873"></a>

```c
void * zsock_get_context_object (int sock)
```

相关声明：[zsock_get_context_object](#ga21a871d1fa6b6beeed88408761877873)。

获取文件描述符（File Descriptor）关联的网络上下文（Net Context）。

<a id="r_ga5693d19a0bdff45a5cb09227683d8631"></a>

```c
int zsock_socket (int family, int type, int proto)
```

相关声明：[zsock_socket](#ga5693d19a0bdff45a5cb09227683d8631)。

创建网络套接字（Network Socket）。

<a id="r_ga1f5e089c9fb39d3a8884502a11e389b3"></a>

```c
int zsock_socketpair (int family, int type, int proto, int *sv)
```

相关声明：[zsock_socketpair](#ga1f5e089c9fb39d3a8884502a11e389b3)。

创建一对未命名且相互连接的套接字（Unnamed Pair of Connected Sockets）。

<a id="r_gae60d7ca486955dd79a2821d1f646c349"></a>

```c
int zsock_close (int sock)
```

相关声明：[zsock_close](#gae60d7ca486955dd79a2821d1f646c349)。

关闭网络套接字（Network Socket）。

<a id="r_gac56432bf901efaf8ef782430ac143f03"></a>

```c
int zsock_shutdown (int sock, int how)
```

相关声明：[zsock_shutdown](#gac56432bf901efaf8ef782430ac143f03)。

关闭套接字（Socket）的发送／接收操作。

<a id="r_ga70909e3233d6523d0ad9566b5edd117c"></a>

```c
int zsock_bind (int sock, const struct net_sockaddr *addr, net_socklen_t addrlen)
```

相关声明：[zsock_bind](#ga70909e3233d6523d0ad9566b5edd117c)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

将套接字（Socket）绑定到本地网络地址（Local Network Address）。

<a id="r_gad858da9650c1270faf5229e3888d7db1"></a>

```c
int zsock_connect (int sock, const struct net_sockaddr *addr, net_socklen_t addrlen)
```

相关声明：[zsock_connect](#gad858da9650c1270faf5229e3888d7db1)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

将套接字（Socket）连接到对端网络地址（Peer Network Address）。

<a id="r_gae8ea59ea82063aa28a9b72da2f08c9fd"></a>

```c
int zsock_listen (int sock, int backlog)
```

相关声明：[zsock_listen](#gae8ea59ea82063aa28a9b72da2f08c9fd)。

设置流式套接字（STREAM Socket），使其接受对端连接（Peer Connection）。

<a id="r_ga1532a65955c402cbb365becb58167f19"></a>

```c
int zsock_accept (int sock, struct net_sockaddr *addr, net_socklen_t *addrlen)
```

相关声明：[zsock_accept](#ga1532a65955c402cbb365becb58167f19)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

在监听套接字（Listening Socket）上接受连接。

<a id="r_ga9f4ff3d1637393cbe74bd111cc6f432a"></a>

```c
ssize_t zsock_sendto (int sock, const void *buf, size_t len, int flags, const struct net_sockaddr *dest_addr, net_socklen_t addrlen)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_sendto](#ga9f4ff3d1637393cbe74bd111cc6f432a)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

向任意网络地址（Network Address）发送数据。

<a id="r_ga2d8c2173986f67dde6dc5721bf690855"></a>

```c
static ssize_t zsock_send (int sock, const void *buf, size_t len, int flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_send](#ga2d8c2173986f67dde6dc5721bf690855)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

向已连接的对端（Connected Peer）发送数据。

<a id="r_gad3274fe71d43caf8c4d92fffb589375e"></a>

```c
ssize_t zsock_sendmsg (int sock, const struct net_msghdr *msg, int flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_sendmsg](#gad3274fe71d43caf8c4d92fffb589375e)、[net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

向任意网络地址（Network Address）发送数据。

<a id="r_ga89271d76123b0a69e0c40ae4de58bd0a"></a>

```c
ssize_t zsock_recvfrom (int sock, void *buf, size_t max_len, int flags, struct net_sockaddr *src_addr, net_socklen_t *addrlen)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_recvfrom](#ga89271d76123b0a69e0c40ae4de58bd0a)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

从任意网络地址（Network Address）接收数据。

<a id="r_ga02b0de9a15c2d1133b87216d6afc203f"></a>

```c
ssize_t zsock_recvmsg (int sock, struct net_msghdr *msg, int flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_recvmsg](#ga02b0de9a15c2d1133b87216d6afc203f)、[net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从任意网络地址（Network Address）接收消息（Message）。

<a id="r_ga8a7d82cfb02a45de59ccd05614eb78d6"></a>

```c
static ssize_t zsock_recv (int sock, void *buf, size_t max_len, int flags)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zsock_recv](#ga8a7d82cfb02a45de59ccd05614eb78d6)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从已连接的对端（Connected Peer）接收数据。

<a id="r_gab069dc3ebc140af65801a73fcac4f629"></a>

```c
int zsock_fcntl_impl (int sock, int cmd, int flags)
```

相关声明：[zsock_fcntl_impl](#gab069dc3ebc140af65801a73fcac4f629)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

控制套接字（Socket）的阻塞／非阻塞模式（Blocking/Non-blocking Mode）。

<a id="r_ga0255a43336642aaeeaa5bff4c29c9389"></a>

```c
int zsock_ioctl_impl (int sock, unsigned long request, va_list ap)
```

相关声明：[zsock_ioctl_impl](#ga0255a43336642aaeeaa5bff4c29c9389)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

控制底层套接字参数（Underlying Socket Parameters）。

<a id="r_ga518361903c9fac3766164d38243872e3"></a>

```c
static int zsock_poll (struct zsock_pollfd *fds, int nfds, int timeout)
```

相关声明：[zsock_poll](#ga518361903c9fac3766164d38243872e3)、[zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)。

高效轮询多个套接字（Socket）的事件（Event）。

<a id="r_ga6aa12f0dbed8ded425555debba044a98"></a>

```c
int zsock_getsockopt (int sock, int level, int optname, void *optval, net_socklen_t *optlen)
```

相关声明：[zsock_getsockopt](#ga6aa12f0dbed8ded425555debba044a98)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

获取各种套接字选项（Socket Options）。

<a id="r_ga71ac8d52c87b9182a9f1a03614e3dba7"></a>

```c
int zsock_setsockopt (int sock, int level, int optname, const void *optval, net_socklen_t optlen)
```

相关声明：[zsock_setsockopt](#ga71ac8d52c87b9182a9f1a03614e3dba7)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

设置各种套接字选项（Socket Options）。

<a id="r_ga78b0ca26c0aaf5e64b05da8caa8c253c"></a>

```c
int zsock_getpeername (int sock, struct net_sockaddr *addr, net_socklen_t *addrlen)
```

相关声明：[zsock_getpeername](#ga78b0ca26c0aaf5e64b05da8caa8c253c)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

获取对端名称（Peer Name）。

<a id="r_ga6bf17561e03600ed870dff702b513d9c"></a>

```c
int zsock_getsockname (int sock, struct net_sockaddr *addr, net_socklen_t *addrlen)
```

相关声明：[zsock_getsockname](#ga6bf17561e03600ed870dff702b513d9c)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

获取套接字名称（Socket Name）。

<a id="r_ga8b348d886f1bc4f4cdf6e2260844f6e1"></a>

```c
int zsock_gethostname (char *buf, size_t len)
```

相关声明：[zsock_gethostname](#ga8b348d886f1bc4f4cdf6e2260844f6e1)。

获取本地主机名（Local Host Name）。

<a id="r_gad3dbb44d7b49249c124e41041aca6536"></a>

```c
static char * zsock_inet_ntop (net_sa_family_t family, const void *src, char *dst, size_t size)
```

相关声明：[zsock_inet_ntop](#gad3dbb44d7b49249c124e41041aca6536)、[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)。

将网络地址（Network Address）从内部表示转换为数字 ASCII 形式（Numeric ASCII Form）。

<a id="r_gaf0130ad342c6873d68bdc51d9cf1167b"></a>

```c
int zsock_inet_pton (net_sa_family_t family, const char *src, void *dst)
```

相关声明：[zsock_inet_pton](#gaf0130ad342c6873d68bdc51d9cf1167b)、[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)。

将网络地址（Network Address）从数字 ASCII 形式（Numeric ASCII Form）转换为内部表示。

<a id="r_gaf59c97c9bd07f188e3f06b2372ac1856"></a>

```c
int zsock_getaddrinfo (const char *host, const char *service, const struct zsock_addrinfo *hints, struct zsock_addrinfo **res)
```

相关声明：[zsock_getaddrinfo](#gaf59c97c9bd07f188e3f06b2372ac1856)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

将域名（Domain Name）解析为一个或多个网络地址（Network Address）。

<a id="r_ga7953da2e52bcfad51b877de6d7fd6cc9"></a>

```c
void zsock_freeaddrinfo (struct zsock_addrinfo *ai)
```

相关声明：[zsock_freeaddrinfo](#ga7953da2e52bcfad51b877de6d7fd6cc9)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

释放 `zsock_getaddrinfo()` 返回的结果。

<a id="r_gaa9d9e97c347b3854dc73d7ba33d8ca4b"></a>

```c
const char * zsock_gai_strerror (int errcode)
```

相关声明：[zsock_gai_strerror](#gaa9d9e97c347b3854dc73d7ba33d8ca4b)。

将 `zsock_getaddrinfo()` 的错误码（Error Code）转换为文本消息。

<a id="r_ga5b02979bf93763a9cc5711c7267d5de8"></a>

```c
int zsock_getnameinfo (const struct net_sockaddr *addr, net_socklen_t addrlen, char *host, net_socklen_t hostlen, char *serv, net_socklen_t servlen, int flags)
```

相关声明：[zsock_getnameinfo](#ga5b02979bf93763a9cc5711c7267d5de8)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将网络地址（Network Address）解析为域名（Domain Name）或 ASCII 地址。

<a id="r_ga8a8e90b68fb77179677f237bc22289ec"></a>

```c
int zsock_send_all (int sock, const void *buf, size_t len, int flags, k_timeout_t timeout, size_t *sent_len)
```

相关声明：[zsock_send_all](#ga8a8e90b68fb77179677f237bc22289ec)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向任意网络地址（Network Address）发送数据。

<a id="r_ga4d2d0823ad8785ffdc2ae327e8651d3f"></a>

```c
int zsock_sendmsg_all (int sock, const struct net_msghdr *msg, int flags, k_timeout_t timeout, size_t *sent_len)
```

相关声明：[zsock_sendmsg_all](#ga4d2d0823ad8785ffdc2ae327e8651d3f)、[net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向任意网络地址（Network Address）发送数据。

<a id="r_ga1a065da89061bcb10b10663a9ffbdd10"></a>

```c
static int zsock_select (int nfds, zsock_fd_set *readfds, zsock_fd_set *writefds, zsock_fd_set *exceptfds, struct zsock_timeval *timeout)
```

相关声明：[zsock_select](#ga1a065da89061bcb10b10663a9ffbdd10)、[zsock_fd_set](#ga1cdeeddce9000b9fd29b638c422f48f8)、[zsock_fd_set](#ga1cdeeddce9000b9fd29b638c422f48f8)、[zsock_fd_set](#ga1cdeeddce9000b9fd29b638c422f48f8)。

轮询多个套接字事件的传统函数（legacy function）。

<a id="r_gaa4855f07c1329a150f371044e4384490"></a>

```c
static void ZSOCK_FD_ZERO (zsock_fd_set *set)
```

相关声明：[ZSOCK_FD_ZERO](#gaa4855f07c1329a150f371044e4384490)、[zsock_fd_set](#ga1cdeeddce9000b9fd29b638c422f48f8)。

初始化并清空 `fd_set`。

<a id="r_gab92b08adccc22a85e7a1c06bf11a88bc"></a>

```c
static int ZSOCK_FD_ISSET (int fd, zsock_fd_set *set)
```

相关声明：[ZSOCK_FD_ISSET](#gab92b08adccc22a85e7a1c06bf11a88bc)、[zsock_fd_set](#ga1cdeeddce9000b9fd29b638c422f48f8)。

检查套接字是否属于 `fd_set`。

<a id="r_ga7023ec00d24af41a7cbf5f376fb44487"></a>

```c
static void ZSOCK_FD_CLR (int fd, zsock_fd_set *set)
```

相关声明：[ZSOCK_FD_CLR](#ga7023ec00d24af41a7cbf5f376fb44487)、[zsock_fd_set](#ga1cdeeddce9000b9fd29b638c422f48f8)。

从 `fd_set` 移除套接字。

<a id="r_ga5d07f52910f6d881295ec659716767f1"></a>

```c
static void ZSOCK_FD_SET (int fd, zsock_fd_set *set)
```

相关声明：[ZSOCK_FD_SET](#ga5d07f52910f6d881295ec659716767f1)、[zsock_fd_set](#ga1cdeeddce9000b9fd29b638c422f48f8)。

将套接字添加到 `fd_set`。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.6\_poll() 的选项（Options for poll()）

<a id="r_ga6ade0deb4952e1ea23b368d9eceee9ed"></a>

```c
#define ZSOCK_POLLIN 1
```

相关声明：[ZSOCK_POLLIN](#ga6ade0deb4952e1ea23b368d9eceee9ed)。

`zsock_poll`：轮询可读（Readability）状态。

<a id="r_ga1c96c16d5000db0fa4b69055ebb97839"></a>

```c
#define ZSOCK_POLLPRI 2
```

相关声明：[ZSOCK_POLLPRI](#ga1c96c16d5000db0fa4b69055ebb97839)。

`zsock_poll`：轮询异常状况（Exceptional Condition）。

<a id="r_ga9ca302c64dfb676798ce03100894ca3e"></a>

```c
#define ZSOCK_POLLOUT 4
```

相关声明：[ZSOCK_POLLOUT](#ga9ca302c64dfb676798ce03100894ca3e)。

`zsock_poll`：轮询可写（Writability）状态。

<a id="r_gad44368a112fbf91436a2439e7b767641"></a>

```c
#define ZSOCK_POLLERR 8
```

相关声明：[ZSOCK_POLLERR](#gad44368a112fbf91436a2439e7b767641)。

`zsock_poll`：轮询结果包含错误状况（Error Condition），仅用作输出值。

<a id="r_gadd341cd5c1f6d7deeaedc5c58dc56fe7"></a>

```c
#define ZSOCK_POLLHUP 0x10
```

相关声明：[ZSOCK_POLLHUP](#gadd341cd5c1f6d7deeaedc5c58dc56fe7)。

`zsock_poll`：轮询检测到连接已关闭（Closed Connection），仅用作输出值。

<a id="r_ga45c5b0efca6e09e4f7db78d1d007bf67"></a>

```c
#define ZSOCK_POLLNVAL 0x20
```

相关声明：[ZSOCK_POLLNVAL](#ga45c5b0efca6e09e4f7db78d1d007bf67)。

`zsock_poll`：无效套接字（Invalid Socket），仅用作输出值。

## 1.7\_发送和接收数据的选项（Options for sending and receiving data）

<a id="r_gae7da123a40584192b65af77e918080b9"></a>

```c
#define ZSOCK_MSG_PEEK 0x02
```

相关声明：[ZSOCK_MSG_PEEK](#gae7da123a40584192b65af77e918080b9)。

`zsock_recv`：读取数据，但不将其从套接字输入队列（Socket Input Queue）移除。

<a id="r_gabdc593f541a4f9a607cfe140cee19c4a"></a>

```c
#define ZSOCK_MSG_CTRUNC 0x08
```

相关声明：[ZSOCK_MSG_CTRUNC](#gabdc593f541a4f9a607cfe140cee19c4a)。

`zsock_recvmsg`：控制数据缓冲区（Control Data Buffer）过小。

<a id="r_gae594c5e74cd473df8e3328a4cd935ce1"></a>

```c
#define ZSOCK_MSG_TRUNC 0x20
```

相关声明：[ZSOCK_MSG_TRUNC](#gae594c5e74cd473df8e3328a4cd935ce1)。

`zsock_recv`：返回数据报（Datagram）的实际长度，即使它超过传入的缓冲区长度。

<a id="r_ga92cf4460e23f376bf130d885ea64ed6b"></a>

```c
#define ZSOCK_MSG_DONTWAIT 0x40
```

相关声明：[ZSOCK_MSG_DONTWAIT](#ga92cf4460e23f376bf130d885ea64ed6b)。

`zsock_recv`/`zsock_send`：将本次操作覆盖为非阻塞（Non-blocking）操作。

<a id="r_ga00b950f50302d97c27111da49f5289fb"></a>

```c
#define ZSOCK_MSG_WAITALL 0x100
```

相关声明：[ZSOCK_MSG_WAITALL](#ga00b950f50302d97c27111da49f5289fb)。

`zsock_recv`：阻塞（Block），直到能够返回要求的全部数据量。

## 1.8\_shutdown() 函数的选项（Options for shutdown() function）

<a id="r_ga2a58cbc62db1e559898ea979454d74d4"></a>

```c
#define ZSOCK_SHUT_RD 0
```

相关声明：[ZSOCK_SHUT_RD](#ga2a58cbc62db1e559898ea979454d74d4)。

`zsock_shutdown`：关闭读取方向（Reading）。

<a id="r_ga87630f1abe81c4e33a24cb1f1ebb3571"></a>

```c
#define ZSOCK_SHUT_WR 1
```

相关声明：[ZSOCK_SHUT_WR](#ga87630f1abe81c4e33a24cb1f1ebb3571)。

`zsock_shutdown`：关闭写入方向（Writing）。

<a id="r_ga788dcff81663a9fb01e32b53bca13e2d"></a>

```c
#define ZSOCK_SHUT_RDWR 2
```

相关声明：[ZSOCK_SHUT_RDWR](#ga788dcff81663a9fb01e32b53bca13e2d)。

`zsock_shutdown`：同时关闭读取和写入方向（Reading and Writing）。

## 1.9\_getaddrinfo() 提示信息的标志（Flags for getaddrinfo() hints）

<a id="r_ga6a63246ff9f8106f533d4d929185a550"></a>

```c
#define ZSOCK_AI_PASSIVE 0x1
```

相关声明：[ZSOCK_AI_PASSIVE](#ga6a63246ff9f8106f533d4d929185a550)。

用于 `bind()` 的地址，而非用于 `connect()` 的地址。

<a id="r_gab1d9d790b3117fa8a0f997fc45e0f5fd"></a>

```c
#define ZSOCK_AI_CANONNAME 0x2
```

相关声明：[ZSOCK_AI_CANONNAME](#gab1d9d790b3117fa8a0f997fc45e0f5fd)。

填充 `ai_canonname`。

<a id="r_ga22b39ed3a330312a68778c8fa8f0f99e"></a>

```c
#define ZSOCK_AI_NUMERICHOST 0x4
```

相关声明：[ZSOCK_AI_NUMERICHOST](#ga22b39ed3a330312a68778c8fa8f0f99e)。

假定主机地址采用数字表示（Numeric Notation），不进行域名系统（DNS）查询。

<a id="r_ga8913ef12daf85f8f7e364fb8bbc0d546"></a>

```c
#define ZSOCK_AI_V4MAPPED 0x8
```

相关声明：[ZSOCK_AI_V4MAPPED](#ga8913ef12daf85f8f7e364fb8bbc0d546)。

对于 IPv6，可以返回 IPv4 映射地址（IPv4 Mapped Address）。

<a id="r_gae24cbe0ed18c68e181940954a8116829"></a>

```c
#define ZSOCK_AI_ALL 0x10
```

相关声明：[ZSOCK_AI_ALL](#gae24cbe0ed18c68e181940954a8116829)。

对于 IPv6，可以同时返回原生 IPv6 地址（Native IPv6 Address）和 IPv4 映射地址（Mapped IPv4 Address）。

<a id="r_ga727bf0f112fbdd9ff1be890177ae42c7"></a>

```c
#define ZSOCK_AI_ADDRCONFIG 0x20
```

相关声明：[ZSOCK_AI_ADDRCONFIG](#ga727bf0f112fbdd9ff1be890177ae42c7)。

IPv4/IPv6 支持取决于本地系统配置（Local System Configuration）。

<a id="r_ga88b89291f68f34337f8c2416a147e671"></a>

```c
#define ZSOCK_AI_NUMERICSERV 0x400
```

相关声明：[ZSOCK_AI_NUMERICSERV](#ga88b89291f68f34337f8c2416a147e671)。

假定服务（Service，即端口）为数字形式。

<a id="r_ga7cd2b1b26066eee23497b1b39ed564c3"></a>

```c
#define ZSOCK_AI_EXTFLAGS 0x800
```

相关声明：[ZSOCK_AI_EXTFLAGS](#ga7cd2b1b26066eee23497b1b39ed564c3)。

存在额外标志（Extra Flags），参见 RFC 5014。

## 1.10\_getnameinfo() 的标志（Flags for getnameinfo()）

<a id="r_gaae950d30c261a1b36972fd4e5aa3a3a6"></a>

```c
#define ZSOCK_NI_NUMERICHOST 1
```

相关声明：[ZSOCK_NI_NUMERICHOST](#gaae950d30c261a1b36972fd4e5aa3a3a6)。

`zsock_getnameinfo()`：解析为数字形式的地址（Numeric Address）。

<a id="r_ga91cf6f543827efd4a75d92a9ddacfae6"></a>

```c
#define ZSOCK_NI_NUMERICSERV 2
```

相关声明：[ZSOCK_NI_NUMERICSERV](#ga91cf6f543827efd4a75d92a9ddacfae6)。

`zsock_getnameinfo()`：解析为数字形式的端口号（Numeric Port Number）。

<a id="r_ga2f57f503276a43cc049fc66269792239"></a>

```c
#define ZSOCK_NI_NOFQDN 4
```

相关声明：[ZSOCK_NI_NOFQDN](#ga2f57f503276a43cc049fc66269792239)。

`zsock_getnameinfo()`：仅返回主机名（Hostname），而非完全限定域名（FQDN）。

<a id="r_ga237a8f33470e18c8a2323ab1dd3811d2"></a>

```c
#define ZSOCK_NI_NAMEREQD 8
```

相关声明：[ZSOCK_NI_NAMEREQD](#ga237a8f33470e18c8a2323ab1dd3811d2)。

`zsock_getnameinfo()`：为兼容性而保留的空操作选项（Dummy Option）。

<a id="r_ga313f921684f9dd3beb14677243dcb84f"></a>

```c
#define ZSOCK_NI_DGRAM 16
```

相关声明：[ZSOCK_NI_DGRAM](#ga313f921684f9dd3beb14677243dcb84f)。

`zsock_getnameinfo()`：为兼容性而保留的空操作选项（Dummy Option）。

<a id="r_ga9ca20495ac25f8007c8a14ce2f3f5533"></a>

```c
#define ZSOCK_NI_MAXHOST 64
```

相关声明：[ZSOCK_NI_MAXHOST](#ga9ca20495ac25f8007c8a14ce2f3f5533)。

`zsock_getnameinfo()`：支持的最大主机名（Hostname）长度。

## 1.11\_套接字级选项（Socket level options (ZSOCK_SOL_SOCKET)）

<a id="r_gaaa2786e0b2410518b6f99e0ee196f4d4"></a>

```c
#define ZSOCK_SOL_SOCKET 1
```

相关声明：[ZSOCK_SOL_SOCKET](#gaaa2786e0b2410518b6f99e0ee196f4d4)。

套接字级选项（Socket-level Option）。

<a id="r_ga37b17a378127c92ededcf397e88d6180"></a>

```c
#define ZSOCK_SO_DEBUG 1
```

相关声明：[ZSOCK_SO_DEBUG](#ga37b17a378127c92ededcf397e88d6180)。

记录调试信息（Debugging Information）；为兼容性而保留，实际忽略。

<a id="r_gac2031f7190b1557d9d5020a93326d214"></a>

```c
#define ZSOCK_SO_REUSEADDR 2
```

相关声明：[ZSOCK_SO_REUSEADDR](#gac2031f7190b1557d9d5020a93326d214)。

地址复用（Address Reuse）。

<a id="r_ga950c4ad7cb1272272e6db23a20cb24a5"></a>

```c
#define ZSOCK_SO_TYPE 3
```

相关声明：[ZSOCK_SO_TYPE](#ga950c4ad7cb1272272e6db23a20cb24a5)。

套接字类型（Socket Type）。

<a id="r_ga60c9f18f25723883ded6c104bd04040c"></a>

```c
#define ZSOCK_SO_ERROR 4
```

相关声明：[ZSOCK_SO_ERROR](#ga60c9f18f25723883ded6c104bd04040c)。

异步错误（Async Error）。

<a id="r_ga037a8a927bc5afc9deb73946fbac30f6"></a>

```c
#define ZSOCK_SO_DONTROUTE 5
```

相关声明：[ZSOCK_SO_DONTROUTE](#ga037a8a927bc5afc9deb73946fbac30f6)。

绕过正常路由（Routing），直接发送到主机；为兼容性而保留，实际忽略。

<a id="r_gab0e987e826705874cc821d730a81b117"></a>

```c
#define ZSOCK_SO_BROADCAST 6
```

相关声明：[ZSOCK_SO_BROADCAST](#gab0e987e826705874cc821d730a81b117)。

支持发送广播消息（Broadcast Messages）；为兼容性而保留，实际忽略。

<a id="r_gaea93c05216e4a1d518406f42e7c7f8bc"></a>

```c
#define ZSOCK_SO_SNDBUF 7
```

相关声明：[ZSOCK_SO_SNDBUF](#gaea93c05216e4a1d518406f42e7c7f8bc)。

套接字发送缓冲区（Socket Send Buffer）的大小。

<a id="r_gad841445fdb66a8303e49b36f2aa52faa"></a>

```c
#define ZSOCK_SO_RCVBUF 8
```

相关声明：[ZSOCK_SO_RCVBUF](#gad841445fdb66a8303e49b36f2aa52faa)。

套接字接收缓冲区（Socket Receive Buffer）的大小。

<a id="r_ga4b3afec80a72e66b8c9e0f4e38cceaea"></a>

```c
#define ZSOCK_SO_KEEPALIVE 9
```

相关声明：[ZSOCK_SO_KEEPALIVE](#ga4b3afec80a72e66b8c9e0f4e38cceaea)。

启用连接上的保活消息（Keep-alive Messages）发送。

<a id="r_ga252b932a5cdc4909885b4d0a7968a5f3"></a>

```c
#define ZSOCK_SO_OOBINLINE 10
```

相关声明：[ZSOCK_SO_OOBINLINE](#ga252b932a5cdc4909885b4d0a7968a5f3)。

将带外数据（Out-of-band Data）放入接收流（Receive Stream）；为兼容性而保留，实际忽略。

<a id="r_ga477c2939c20f24ae4119d6ef8b248c08"></a>

```c
#define ZSOCK_SO_PRIORITY 12
```

相关声明：[ZSOCK_SO_PRIORITY](#ga477c2939c20f24ae4119d6ef8b248c08)。

套接字优先级（Socket Priority）。

<a id="r_ga7390a499529d767680cf7ac578f9586d"></a>

```c
#define ZSOCK_SO_LINGER 13
```

相关声明：[ZSOCK_SO_LINGER](#ga7390a499529d767680cf7ac578f9586d)。

套接字关闭时延迟结束（Linger）。

<a id="r_gacc93dbba4441b1617173bf9ca3c36c66"></a>

```c
#define ZSOCK_SO_REUSEPORT 15
```

相关声明：[ZSOCK_SO_REUSEPORT](#gacc93dbba4441b1617173bf9ca3c36c66)。

允许多个套接字（Socket）复用同一个端口（Port）。

<a id="r_gaa1ee3324ef29c0bcb66c893f8f0a0a22"></a>

```c
#define ZSOCK_SO_RCVLOWAT 18
```

相关声明：[ZSOCK_SO_RCVLOWAT](#gaa1ee3324ef29c0bcb66c893f8f0a0a22)。

接收低水位（Receive Low Watermark）；为兼容性而保留，实际忽略。

<a id="r_ga87e4d65779b4c60b9a0c1ced480ed033"></a>

```c
#define ZSOCK_SO_SNDLOWAT 19
```

相关声明：[ZSOCK_SO_SNDLOWAT](#ga87e4d65779b4c60b9a0c1ced480ed033)。

发送低水位（Send Low Watermark）；为兼容性而保留，实际忽略。

<a id="r_ga127dd9d8339be8b435ace9d6ad95e850"></a>

```c
#define ZSOCK_SO_RCVTIMEO 20
```

相关声明：[ZSOCK_SO_RCVTIMEO](#ga127dd9d8339be8b435ace9d6ad95e850)。

接收超时（Receive Timeout）。适用于 `recv()` 等接收函数，但不适用于 `connect()`。

<a id="r_ga786304b8676b8bc6466a7235396a07f7"></a>

```c
#define ZSOCK_SO_SNDTIMEO 21
```

相关声明：[ZSOCK_SO_SNDTIMEO](#ga786304b8676b8bc6466a7235396a07f7)。

发送超时（Send Timeout）。

<a id="r_ga067cb2ba7575f3c26e7458ea3276fe06"></a>

```c
#define ZSOCK_SO_BINDTODEVICE 25
```

相关声明：[ZSOCK_SO_BINDTODEVICE](#ga067cb2ba7575f3c26e7458ea3276fe06)。

将套接字（Socket）绑定到接口（Interface）。

<a id="r_ga4064b264e8c62b18177ed538dc486966"></a>

```c
#define ZSOCK_SO_ACCEPTCONN 30
```

相关声明：[ZSOCK_SO_ACCEPTCONN](#ga4064b264e8c62b18177ed538dc486966)。

套接字接受传入连接（Incoming Connections）；为兼容性而保留，实际忽略。

<a id="r_ga77fdf74646e0c3b28240ae5899cee058"></a>

```c
#define ZSOCK_SO_TIMESTAMPING 37
```

相关声明：[ZSOCK_SO_TIMESTAMPING](#ga77fdf74646e0c3b28240ae5899cee058)。

为发送（TX）、接收（RX）或两种方向的数据包添加时间戳（Timestamp）。

<a id="r_ga1b6d5006c4dade22d3a1c8679aa74d39"></a>

```c
#define ZSOCK_SO_PROTOCOL 38
```

相关声明：[ZSOCK_SO_PROTOCOL](#ga1b6d5006c4dade22d3a1c8679aa74d39)。

套接字（Socket）使用的协议（Protocol）。

<a id="r_ga19f5176efede119e11a9c3fb66b9f152"></a>

```c
#define ZSOCK_SO_DOMAIN 39
```

相关声明：[ZSOCK_SO_DOMAIN](#ga19f5176efede119e11a9c3fb66b9f152)。

套接字（Socket）使用的域（Domain）。

<a id="r_ga3f136ae14247139586f85cd45d046fb3"></a>

```c
#define ZSOCK_SO_SOCKS5 60
```

相关声明：[ZSOCK_SO_SOCKS5](#ga3f136ae14247139586f85cd45d046fb3)。

为套接字（Socket）启用 SOCKS5。

<a id="r_ga091f558e4c5c15e615281ba21feb130f"></a>

```c
#define ZSOCK_SO_TXTIME 61
```

相关声明：[ZSOCK_SO_TXTIME](#ga091f558e4c5c15e615281ba21feb130f)。

套接字发送时间（Socket TX Time），即数据应发送的时刻。

<a id="r_gaf965ab6d61f7252b4c6b0750d47d6c5c"></a>

```c
#define ZSOCK_SCM_TXTIME ZSOCK_SO_TXTIME
```

相关声明：[ZSOCK_SCM_TXTIME](#gaf965ab6d61f7252b4c6b0750d47d6c5c)、[ZSOCK_SO_TXTIME](#ga091f558e4c5c15e615281ba21feb130f)。

套接字发送时间（Socket TX Time），与 `SO_TXTIME` 相同。

<a id="r_gaf851a5752668188d6c9d66f6d349377a"></a>

```c
#define ZSOCK_SOF_TIMESTAMPING_RX_HARDWARE BIT(0)
```

相关声明：[ZSOCK_SOF_TIMESTAMPING_RX_HARDWARE](#gaf851a5752668188d6c9d66f6d349377a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间戳生成标志（Timestamp Generation Flags）。

<a id="r_gafe8cfcce94475fa2dcc2d0e56d6a7134"></a>

```c
#define ZSOCK_SOF_TIMESTAMPING_TX_HARDWARE BIT(1)
```

相关声明：[ZSOCK_SOF_TIMESTAMPING_TX_HARDWARE](#gafe8cfcce94475fa2dcc2d0e56d6a7134)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

请求由网络适配器（Network Adapter）生成的发送时间戳（TX Timestamp）。

## 1.12\_TCP 级选项（TCP level options (NET_IPPROTO_TCP)）

<a id="r_gaed65035762b59c3717cdc856a15f92fa"></a>

```c
#define ZSOCK_TCP_NODELAY 1
```

相关声明：[ZSOCK_TCP_NODELAY](#gaed65035762b59c3717cdc856a15f92fa)。

禁用 TCP 缓冲（Buffering）；为兼容性而保留，实际忽略。

<a id="r_ga720e01b6ceaff867dd673cdd8b648bf2"></a>

```c
#define ZSOCK_TCP_KEEPIDLE 2
```

相关声明：[ZSOCK_TCP_KEEPIDLE](#ga720e01b6ceaff867dd673cdd8b648bf2)。

经过此时间后开始发送保活消息（Keepalive），单位为秒。

<a id="r_ga1ebb7dbc45bf6b1b01cb5fe482a3f1b8"></a>

```c
#define ZSOCK_TCP_KEEPINTVL 3
```

相关声明：[ZSOCK_TCP_KEEPINTVL](#ga1ebb7dbc45bf6b1b01cb5fe482a3f1b8)。

保活消息（Keepalive）之间的间隔，单位为秒。

<a id="r_ga0b29b699728d87c097ff51c95d2f80b1"></a>

```c
#define ZSOCK_TCP_KEEPCNT 4
```

相关声明：[ZSOCK_TCP_KEEPCNT](#ga0b29b699728d87c097ff51c95d2f80b1)。

断开连接前发送的保活消息（Keepalive）数量。

## 1.13\_UDP 级选项（UDP level options (NET_IPPROTO_UDP)）

<a id="r_ga8e63f889afc9ca06bfea2b90e4e88b3e"></a>

```c
#define ZSOCK_UDP_OPT 1
```

相关声明：[ZSOCK_UDP_OPT](#ga8e63f889afc9ca06bfea2b90e4e88b3e)。

启用或禁用所有 UDP 选项（UDP Options），值为 `int` 类型布尔值；这些选项来自 RFC 9868。

<a id="r_ga0394de45aedd088ebcfb11006836572c"></a>

```c
#define ZSOCK_UDP_OPT_OCS 2
```

相关声明：[ZSOCK_UDP_OPT_OCS](#ga0394de45aedd088ebcfb11006836572c)。

启用或禁用 UDP OCS，值为 `int` 类型布尔值（Boolean）。

<a id="r_ga1e80d0746eac06c45ef53011cefb9b66"></a>

```c
#define ZSOCK_UDP_OPT_APC 3
```

相关声明：[ZSOCK_UDP_OPT_APC](#ga1e80d0746eac06c45ef53011cefb9b66)。

启用或禁用 UDP APC 选项（Option），值为 `int` 类型布尔值。

<a id="r_ga44c749f760057277985a91525ad75846"></a>

```c
#define ZSOCK_UDP_OPT_FRAG 4
```

相关声明：[ZSOCK_UDP_OPT_FRAG](#ga44c749f760057277985a91525ad75846)。

启用或禁用 UDP 分片选项（Fragmentation Option），值为 `int` 类型布尔值。

<a id="r_gaa976bda2ebe370345e7d9324fd0102e1"></a>

```c
#define ZSOCK_UDP_OPT_MDS 5
```

相关声明：[ZSOCK_UDP_OPT_MDS](#gaa976bda2ebe370345e7d9324fd0102e1)。

设置或获取 UDP MDS 选项值（Option Value），类型为 `uint16_t`。

<a id="r_ga023dea5abc5f784df8e988492bc5bfb4"></a>

```c
#define ZSOCK_UDP_OPT_MRDS 6
```

相关声明：[ZSOCK_UDP_OPT_MRDS](#ga023dea5abc5f784df8e988492bc5bfb4)。

设置或获取 UDP MRDS 选项值（Option Value），类型为 `struct net_udp_opt_mrds`。

<a id="r_ga62c9b039d368e75991937619e9adf8cc"></a>

```c
#define ZSOCK_UDP_OPT_REQ 7
```

相关声明：[ZSOCK_UDP_OPT_REQ](#ga62c9b039d368e75991937619e9adf8cc)。

启用或禁用 UDP REQ 选项（Option），值为 `int` 类型布尔值。

<a id="r_gaec4348215929b4deff996dcac0ccd5d3"></a>

```c
#define ZSOCK_UDP_OPT_RES 8
```

相关声明：[ZSOCK_UDP_OPT_RES](#gaec4348215929b4deff996dcac0ccd5d3)。

启用或禁用 UDP RES 选项（Option），值为 `int` 类型布尔值。

<a id="r_gaaf3a09237d37bb112ee72504d926cd89"></a>

```c
#define ZSOCK_UDP_OPT_TIME 9
```

相关声明：[ZSOCK_UDP_OPT_TIME](#gaaf3a09237d37bb112ee72504d926cd89)。

启用或禁用 UDP TIME 选项（Option），值为 `int` 类型布尔值。

<a id="r_gac336fbf99b335b69a05004b6ca6a0104"></a>

```c
#define ZSOCK_UDP_OPT_AUTH 10
```

相关声明：[ZSOCK_UDP_OPT_AUTH](#gac336fbf99b335b69a05004b6ca6a0104)。

启用或禁用 UDP AUTH 选项（Option），值为 `int` 类型布尔值。

<a id="r_ga92c67eface4732a6b8faf182fc91dfcb"></a>

```c
#define ZSOCK_UDP_OPT_EXP 11
```

相关声明：[ZSOCK_UDP_OPT_EXP](#ga92c67eface4732a6b8faf182fc91dfcb)。

启用或禁用 UDP EXP 选项（Option），值为 `int` 类型布尔值。

<a id="r_gaf0ea7830aa95f7fe5c88bbc6b11f9627"></a>

```c
#define ZSOCK_UDP_OPT_UCMP 12
```

相关声明：[ZSOCK_UDP_OPT_UCMP](#gaf0ea7830aa95f7fe5c88bbc6b11f9627)。

启用或禁用 UDP UCMP 选项（Option），值为 `int` 类型布尔值。

<a id="r_gaf95d8f076a0d4232992aea0f2545b65f"></a>

```c
#define ZSOCK_UDP_OPT_UENC 13
```

相关声明：[ZSOCK_UDP_OPT_UENC](#gaf95d8f076a0d4232992aea0f2545b65f)。

启用或禁用 UDP UENC 选项（Option），值为 `int` 类型布尔值。

<a id="r_ga3d3737422eb33cf98300e18c5e24a214"></a>

```c
#define ZSOCK_UDP_OPT_UEXP 14
```

相关声明：[ZSOCK_UDP_OPT_UEXP](#ga3d3737422eb33cf98300e18c5e24a214)。

启用或禁用 UDP UEXP 选项（Option），值为 `int` 类型布尔值。

<a id="r_ga989a840540b557473a4a4438915f59de"></a>

```c
#define ZSOCK_UDP_OPT_DPLPMTUD 15
```

相关声明：[ZSOCK_UDP_OPT_DPLPMTUD](#ga989a840540b557473a4a4438915f59de)。

通过 UDP 选项启用或禁用数据报分包层路径 MTU 发现（DPLPMTUD），参见 RFC 9869；值为 `int` 类型布尔值。

<a id="r_ga5cd27e199f4507097b9ab2f74ba88c10"></a>

```c
#define ZSOCK_UDP_OPT_DPLPMTUD_APP_RESPOND 16
```

相关声明：[ZSOCK_UDP_OPT_DPLPMTUD_APP_RESPOND](#ga5cd27e199f4507097b9ab2f74ba88c10)。

由应用程序自行完成 REQ→RES 回显（Echo），而非由协议栈处理；值为 `int` 类型布尔值。

<a id="r_ga86605887c247cf1a11701c5675c7895d"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_APC 1
```

相关声明：[ZSOCK_UDP_OPT_CMSG_APC](#ga86605887c247cf1a11701c5675c7895d)。

辅助数据（Ancillary Data）中 `IPPROTO_UDP` 级别的控制消息（cmsg）类型。

<a id="r_ga473e4bab8f40c07e7bfc618f256868eb"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_MDS 2
```

相关声明：[ZSOCK_UDP_OPT_CMSG_MDS](#ga473e4bab8f40c07e7bfc618f256868eb)。

对端 MDS（Peer MDS），类型为 `uint16_t`。

<a id="r_ga2e00bde85be42b224689e67b9519ba91"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_MRDS 3
```

相关声明：[ZSOCK_UDP_OPT_CMSG_MRDS](#ga2e00bde85be42b224689e67b9519ba91)。

结构体（Structure）：`struct net_udp_opt_mrds`。

<a id="r_ga663d30569b681b857b2d3da8c9c5975a"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_REQ 4
```

相关声明：[ZSOCK_UDP_OPT_CMSG_REQ](#ga663d30569b681b857b2d3da8c9c5975a)。

回显请求令牌（Echo Request Token），类型为 `uint32_t`。

<a id="r_ga4cea51ab6931e1020694569edaedb78b"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_RES 5
```

相关声明：[ZSOCK_UDP_OPT_CMSG_RES](#ga4cea51ab6931e1020694569edaedb78b)。

回显响应令牌（Echo Response Token），类型为 `uint32_t`。

<a id="r_ga0cde876903364ec01f633a1b973f0e6e"></a>

```c
#define ZSOCK_UDP_OPT_CMSG_TIME 6
```

相关声明：[ZSOCK_UDP_OPT_CMSG_TIME](#ga0cde876903364ec01f633a1b973f0e6e)。

结构体（Structure）：`struct net_udp_opt_time`。

## 1.14\_listen() 的待连接队列大小（Backlog size for listen()）

<a id="r_ga95372181a0f868383e6631de84145e39"></a>

```c
#define ZSOCK_SOMAXCONN 128
```

相关声明：[ZSOCK_SOMAXCONN](#ga95372181a0f868383e6631de84145e39)。

`listen`：待连接队列（Backlog Queue）的最大长度。

## 1.15\_检查特殊 IPv6 地址的宏（Macros for checking special IPv6 addresses.）

<a id="r_ga3ff22595e17c630cf07d40a5e178ecce"></a>

```c
#define ZSOCK_IN6_IS_ADDR_UNSPECIFIED(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_UNSPECIFIED](#ga3ff22595e17c630cf07d40a5e178ecce)。

检查是否为未指定的 IPv6 地址（Unspecified IPv6 Address）。

<a id="r_gac92eaa41e32e464249bf703d16f869b4"></a>

```c
#define ZSOCK_IN6_IS_ADDR_LOOPBACK(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_LOOPBACK](#gac92eaa41e32e464249bf703d16f869b4)。

检查是否为 IPv6 回环地址（Loopback Address）。

<a id="r_gac8fceb6a75060068126f4a4ea5b24fb9"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MULTICAST(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MULTICAST](#gac8fceb6a75060068126f4a4ea5b24fb9)。

检查是否为 IPv6 多播地址（Multicast Address）。

<a id="r_gaa2ea2ea293a83c2b3c4851ce517d38bf"></a>

```c
#define ZSOCK_IN6_IS_ADDR_LINKLOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_LINKLOCAL](#gaa2ea2ea293a83c2b3c4851ce517d38bf)。

检查是否为 IPv6 链路本地地址（Link Local Address）。

<a id="r_ga91dc0bd2f4fb09cefad741ee0b1e2c20"></a>

```c
#define ZSOCK_IN6_IS_ADDR_SITELOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_SITELOCAL](#ga91dc0bd2f4fb09cefad741ee0b1e2c20)。

检查是否为 IPv6 站点本地地址（Site Local Address）。

<a id="r_ga11df060795e7146f2294ef50d4832cfa"></a>

```c
#define ZSOCK_IN6_IS_ADDR_V4MAPPED(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_V4MAPPED](#ga11df060795e7146f2294ef50d4832cfa)。

检查是否为 IPv4 映射的 IPv6 地址（IPv4 Mapped IPv6 Address）。

<a id="r_ga42c8ad2a3bb2c223148ab4155be091a2"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_GLOBAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_GLOBAL](#ga42c8ad2a3bb2c223148ab4155be091a2)。

检查是否为 IPv6 全局多播地址（Multicast Global Address）。

<a id="r_ga106dff01f87ce99d72d54048f837fbdb"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_NODELOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_NODELOCAL](#ga106dff01f87ce99d72d54048f837fbdb)。

检查是否为 IPv6 节点本地多播地址（Multicast Node Local Address）。

<a id="r_ga00067e1cde69c9ae9ad71f0356314964"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_LINKLOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_LINKLOCAL](#ga00067e1cde69c9ae9ad71f0356314964)。

检查是否为 IPv6 链路本地多播地址（Multicast Link Local Address）。

<a id="r_ga76114e85298c02cb5cb37e6a8d9ad566"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_SITELOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_SITELOCAL](#ga76114e85298c02cb5cb37e6a8d9ad566)。

检查是否为 IPv6 站点本地多播地址（Multicast Site Local Address）。

<a id="r_gae0982428d5720288e7273d442d07d035"></a>

```c
#define ZSOCK_IN6_IS_ADDR_MC_ORGLOCAL(addr)
```

相关声明：[ZSOCK_IN6_IS_ADDR_MC_ORGLOCAL](#gae0982428d5720288e7273d442d07d035)。

检查是否为 IPv6 组织本地多播地址（Multicast Organization Local Address）。

## 1.16\_详细说明（Detailed Documentation）

<a id="ga727bf0f112fbdd9ff1be890177ae42c7"></a>

### `ZSOCK_AI_ADDRCONFIG`

```c
#define ZSOCK_AI_ADDRCONFIG 0x20
```

```c
#include <zephyr/net/socket.h>
```

IPv4/IPv6 支持取决于本地系统配置（Local System Configuration）。

<a id="gae24cbe0ed18c68e181940954a8116829"></a>

### `ZSOCK_AI_ALL`

```c
#define ZSOCK_AI_ALL 0x10
```

```c
#include <zephyr/net/socket.h>
```

对于 IPv6，可以同时返回原生 IPv6 地址（Native IPv6 Address）和 IPv4 映射地址（Mapped IPv4 Address）。

<a id="gab1d9d790b3117fa8a0f997fc45e0f5fd"></a>

### `ZSOCK_AI_CANONNAME`

```c
#define ZSOCK_AI_CANONNAME 0x2
```

```c
#include <zephyr/net/socket.h>
```

填充 `ai_canonname`。

<a id="ga7cd2b1b26066eee23497b1b39ed564c3"></a>

### `ZSOCK_AI_EXTFLAGS`

```c
#define ZSOCK_AI_EXTFLAGS 0x800
```

```c
#include <zephyr/net/socket.h>
```

存在额外标志（Extra Flags），参见 RFC 5014。

<a id="ga22b39ed3a330312a68778c8fa8f0f99e"></a>

### `ZSOCK_AI_NUMERICHOST`

```c
#define ZSOCK_AI_NUMERICHOST 0x4
```

```c
#include <zephyr/net/socket.h>
```

假定主机地址采用数字表示（Numeric Notation），不进行域名系统（DNS）查询。

<a id="ga88b89291f68f34337f8c2416a147e671"></a>

### `ZSOCK_AI_NUMERICSERV`

```c
#define ZSOCK_AI_NUMERICSERV 0x400
```

```c
#include <zephyr/net/socket.h>
```

假定服务（Service，即端口）为数字形式。

<a id="ga6a63246ff9f8106f533d4d929185a550"></a>

### `ZSOCK_AI_PASSIVE`

```c
#define ZSOCK_AI_PASSIVE 0x1
```

```c
#include <zephyr/net/socket.h>
```

用于 `bind()` 的地址，而非用于 `connect()` 的地址。

<a id="ga8913ef12daf85f8f7e364fb8bbc0d546"></a>

### `ZSOCK_AI_V4MAPPED`

```c
#define ZSOCK_AI_V4MAPPED 0x8
```

```c
#include <zephyr/net/socket.h>
```

对于 IPv6，可以返回 IPv4 映射地址（IPv4 Mapped Address）。

<a id="ga5c88da69b8d9401d3ae02495056f7e23"></a>

### `ZSOCK_FD_SETSIZE`

```c
#define ZSOCK_FD_SETSIZE ZVFS_FD_SETSIZE
```

```c
#include <zephyr/net/socket_select.h>
```

可添加到 `zsock_fd_set` 中的文件描述符数量。

<a id="gaa2ea2ea293a83c2b3c4851ce517d38bf"></a>

### `ZSOCK_IN6_IS_ADDR_LINKLOCAL`

```c
#define ZSOCK_IN6_IS_ADDR_LINKLOCAL ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_is_ll_addr(addr)
```

检查是否为 IPv6 链路本地地址（Link Local Address）。

<a id="gac92eaa41e32e464249bf703d16f869b4"></a>

### `ZSOCK_IN6_IS_ADDR_LOOPBACK`

```c
#define ZSOCK_IN6_IS_ADDR_LOOPBACK ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_is_addr_loopback(addr)
```

检查是否为 IPv6 回环地址（Loopback Address）。

<a id="ga42c8ad2a3bb2c223148ab4155be091a2"></a>

### `ZSOCK_IN6_IS_ADDR_MC_GLOBAL`

```c
#define ZSOCK_IN6_IS_ADDR_MC_GLOBAL ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_is_addr_mcast_global(addr)
```

检查是否为 IPv6 全局多播地址（Multicast Global Address）。

<a id="ga00067e1cde69c9ae9ad71f0356314964"></a>

### `ZSOCK_IN6_IS_ADDR_MC_LINKLOCAL`

```c
#define ZSOCK_IN6_IS_ADDR_MC_LINKLOCAL ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_is_addr_mcast_link(addr)
```

检查是否为 IPv6 链路本地多播地址（Multicast Link Local Address）。

<a id="ga106dff01f87ce99d72d54048f837fbdb"></a>

### `ZSOCK_IN6_IS_ADDR_MC_NODELOCAL`

```c
#define ZSOCK_IN6_IS_ADDR_MC_NODELOCAL ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_is_addr_mcast_iface(addr)
```

检查是否为 IPv6 节点本地多播地址（Multicast Node Local Address）。

<a id="gae0982428d5720288e7273d442d07d035"></a>

### `ZSOCK_IN6_IS_ADDR_MC_ORGLOCAL`

```c
#define ZSOCK_IN6_IS_ADDR_MC_ORGLOCAL ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_is_addr_mcast_org(addr)
```

检查是否为 IPv6 组织本地多播地址（Multicast Organization Local Address）。

<a id="ga76114e85298c02cb5cb37e6a8d9ad566"></a>

### `ZSOCK_IN6_IS_ADDR_MC_SITELOCAL`

```c
#define ZSOCK_IN6_IS_ADDR_MC_SITELOCAL ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_is_addr_mcast_site(addr)
```

检查是否为 IPv6 站点本地多播地址（Multicast Site Local Address）。

<a id="gac8fceb6a75060068126f4a4ea5b24fb9"></a>

### `ZSOCK_IN6_IS_ADDR_MULTICAST`

```c
#define ZSOCK_IN6_IS_ADDR_MULTICAST ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_is_addr_mcast(addr)
```

检查是否为 IPv6 多播地址（Multicast Address）。

<a id="ga91dc0bd2f4fb09cefad741ee0b1e2c20"></a>

### `ZSOCK_IN6_IS_ADDR_SITELOCAL`

```c
#define ZSOCK_IN6_IS_ADDR_SITELOCAL ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_is_sl_addr(addr)
```

检查是否为 IPv6 站点本地地址（Site Local Address）。

<a id="ga3ff22595e17c630cf07d40a5e178ecce"></a>

### `ZSOCK_IN6_IS_ADDR_UNSPECIFIED`

```c
#define ZSOCK_IN6_IS_ADDR_UNSPECIFIED ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_addr_cmp(net_ipv6_unspecified_address(), addr)
```

检查是否为未指定的 IPv6 地址（Unspecified IPv6 Address）。

<a id="ga11df060795e7146f2294ef50d4832cfa"></a>

### `ZSOCK_IN6_IS_ADDR_V4MAPPED`

```c
#define ZSOCK_IN6_IS_ADDR_V4MAPPED ( addr)
```

```c
#include <zephyr/net/socket.h>
```

展开值（Value）：

```c
net_ipv6_addr_is_v4_mapped(addr)
```

检查是否为 IPv4 映射的 IPv6 地址（IPv4 Mapped IPv6 Address）。

<a id="gabdc593f541a4f9a607cfe140cee19c4a"></a>

### `ZSOCK_MSG_CTRUNC`

```c
#define ZSOCK_MSG_CTRUNC 0x08
```

```c
#include <zephyr/net/socket.h>
```

`zsock_recvmsg`：控制数据缓冲区（Control Data Buffer）过小。

<a id="ga92cf4460e23f376bf130d885ea64ed6b"></a>

### `ZSOCK_MSG_DONTWAIT`

```c
#define ZSOCK_MSG_DONTWAIT 0x40
```

```c
#include <zephyr/net/socket.h>
```

`zsock_recv`/`zsock_send`：将本次操作覆盖为非阻塞（Non-blocking）操作。

<a id="gae7da123a40584192b65af77e918080b9"></a>

### `ZSOCK_MSG_PEEK`

```c
#define ZSOCK_MSG_PEEK 0x02
```

```c
#include <zephyr/net/socket.h>
```

`zsock_recv`：读取数据，但不将其从套接字输入队列（Socket Input Queue）移除。

<a id="gae594c5e74cd473df8e3328a4cd935ce1"></a>

### `ZSOCK_MSG_TRUNC`

```c
#define ZSOCK_MSG_TRUNC 0x20
```

```c
#include <zephyr/net/socket.h>
```

`zsock_recv`：返回数据报（Datagram）的实际长度，即使它超过传入的缓冲区长度。

<a id="ga00b950f50302d97c27111da49f5289fb"></a>

### `ZSOCK_MSG_WAITALL`

```c
#define ZSOCK_MSG_WAITALL 0x100
```

```c
#include <zephyr/net/socket.h>
```

`zsock_recv`：阻塞（Block），直到能够返回要求的全部数据量。

<a id="ga313f921684f9dd3beb14677243dcb84f"></a>

### `ZSOCK_NI_DGRAM`

```c
#define ZSOCK_NI_DGRAM 16
```

```c
#include <zephyr/net/socket.h>
```

`zsock_getnameinfo()`：为兼容性而保留的空操作选项（Dummy Option）。

<a id="ga9ca20495ac25f8007c8a14ce2f3f5533"></a>

### `ZSOCK_NI_MAXHOST`

```c
#define ZSOCK_NI_MAXHOST 64
```

```c
#include <zephyr/net/socket.h>
```

`zsock_getnameinfo()`：支持的最大主机名（Hostname）长度。

<a id="ga237a8f33470e18c8a2323ab1dd3811d2"></a>

### `ZSOCK_NI_NAMEREQD`

```c
#define ZSOCK_NI_NAMEREQD 8
```

```c
#include <zephyr/net/socket.h>
```

`zsock_getnameinfo()`：为兼容性而保留的空操作选项（Dummy Option）。

<a id="ga2f57f503276a43cc049fc66269792239"></a>

### `ZSOCK_NI_NOFQDN`

```c
#define ZSOCK_NI_NOFQDN 4
```

```c
#include <zephyr/net/socket.h>
```

`zsock_getnameinfo()`：仅返回主机名（Hostname），而非完全限定域名（FQDN）。

<a id="gaae950d30c261a1b36972fd4e5aa3a3a6"></a>

### `ZSOCK_NI_NUMERICHOST`

```c
#define ZSOCK_NI_NUMERICHOST 1
```

```c
#include <zephyr/net/socket.h>
```

`zsock_getnameinfo()`：解析为数字形式的地址（Numeric Address）。

<a id="ga91cf6f543827efd4a75d92a9ddacfae6"></a>

### `ZSOCK_NI_NUMERICSERV`

```c
#define ZSOCK_NI_NUMERICSERV 2
```

```c
#include <zephyr/net/socket.h>
```

`zsock_getnameinfo()`：解析为数字形式的端口号（Numeric Port Number）。

<a id="gad44368a112fbf91436a2439e7b767641"></a>

### `ZSOCK_POLLERR`

```c
#define ZSOCK_POLLERR 8
```

```c
#include <zephyr/net/socket.h>
```

`zsock_poll`：轮询结果包含错误状况（Error Condition），仅用作输出值。

<a id="gadd341cd5c1f6d7deeaedc5c58dc56fe7"></a>

### `ZSOCK_POLLHUP`

```c
#define ZSOCK_POLLHUP 0x10
```

```c
#include <zephyr/net/socket.h>
```

`zsock_poll`：轮询检测到连接已关闭（Closed Connection），仅用作输出值。

<a id="ga6ade0deb4952e1ea23b368d9eceee9ed"></a>

### `ZSOCK_POLLIN`

```c
#define ZSOCK_POLLIN 1
```

```c
#include <zephyr/net/socket.h>
```

`zsock_poll`：轮询可读（Readability）状态。

<a id="ga45c5b0efca6e09e4f7db78d1d007bf67"></a>

### `ZSOCK_POLLNVAL`

```c
#define ZSOCK_POLLNVAL 0x20
```

```c
#include <zephyr/net/socket.h>
```

`zsock_poll`：无效套接字（Invalid Socket），仅用作输出值。

<a id="ga9ca302c64dfb676798ce03100894ca3e"></a>

### `ZSOCK_POLLOUT`

```c
#define ZSOCK_POLLOUT 4
```

```c
#include <zephyr/net/socket.h>
```

`zsock_poll`：轮询可写（Writability）状态。

<a id="ga1c96c16d5000db0fa4b69055ebb97839"></a>

### `ZSOCK_POLLPRI`

```c
#define ZSOCK_POLLPRI 2
```

```c
#include <zephyr/net/socket.h>
```

`zsock_poll`：轮询异常状况（Exceptional Condition）。

<a id="gaf965ab6d61f7252b4c6b0750d47d6c5c"></a>

### `ZSOCK_SCM_TXTIME`

```c
#define ZSOCK_SCM_TXTIME ZSOCK_SO_TXTIME
```

```c
#include <zephyr/net/socket.h>
```

套接字发送时间（Socket TX Time），与 `SO_TXTIME` 相同。

<a id="ga2a58cbc62db1e559898ea979454d74d4"></a>

### `ZSOCK_SHUT_RD`

```c
#define ZSOCK_SHUT_RD 0
```

```c
#include <zephyr/net/socket.h>
```

`zsock_shutdown`：关闭读取方向（Reading）。

<a id="ga788dcff81663a9fb01e32b53bca13e2d"></a>

### `ZSOCK_SHUT_RDWR`

```c
#define ZSOCK_SHUT_RDWR 2
```

```c
#include <zephyr/net/socket.h>
```

`zsock_shutdown`：同时关闭读取和写入方向（Reading and Writing）。

<a id="ga87630f1abe81c4e33a24cb1f1ebb3571"></a>

### `ZSOCK_SHUT_WR`

```c
#define ZSOCK_SHUT_WR 1
```

```c
#include <zephyr/net/socket.h>
```

`zsock_shutdown`：关闭写入方向（Writing）。

<a id="ga4064b264e8c62b18177ed538dc486966"></a>

### `ZSOCK_SO_ACCEPTCONN`

```c
#define ZSOCK_SO_ACCEPTCONN 30
```

```c
#include <zephyr/net/socket.h>
```

套接字接受传入连接（Incoming Connections）；为兼容性而保留，实际忽略。

<a id="ga067cb2ba7575f3c26e7458ea3276fe06"></a>

### `ZSOCK_SO_BINDTODEVICE`

```c
#define ZSOCK_SO_BINDTODEVICE 25
```

```c
#include <zephyr/net/socket.h>
```

将套接字（Socket）绑定到接口（Interface）。

<a id="gab0e987e826705874cc821d730a81b117"></a>

### `ZSOCK_SO_BROADCAST`

```c
#define ZSOCK_SO_BROADCAST 6
```

```c
#include <zephyr/net/socket.h>
```

支持发送广播消息（Broadcast Messages）；为兼容性而保留，实际忽略。

<a id="ga37b17a378127c92ededcf397e88d6180"></a>

### `ZSOCK_SO_DEBUG`

```c
#define ZSOCK_SO_DEBUG 1
```

```c
#include <zephyr/net/socket.h>
```

记录调试信息（Debugging Information）；为兼容性而保留，实际忽略。

<a id="ga19f5176efede119e11a9c3fb66b9f152"></a>

### `ZSOCK_SO_DOMAIN`

```c
#define ZSOCK_SO_DOMAIN 39
```

```c
#include <zephyr/net/socket.h>
```

套接字（Socket）使用的域（Domain）。

<a id="ga037a8a927bc5afc9deb73946fbac30f6"></a>

### `ZSOCK_SO_DONTROUTE`

```c
#define ZSOCK_SO_DONTROUTE 5
```

```c
#include <zephyr/net/socket.h>
```

绕过正常路由（Routing），直接发送到主机；为兼容性而保留，实际忽略。

<a id="ga60c9f18f25723883ded6c104bd04040c"></a>

### `ZSOCK_SO_ERROR`

```c
#define ZSOCK_SO_ERROR 4
```

```c
#include <zephyr/net/socket.h>
```

异步错误（Async Error）。

<a id="ga4b3afec80a72e66b8c9e0f4e38cceaea"></a>

### `ZSOCK_SO_KEEPALIVE`

```c
#define ZSOCK_SO_KEEPALIVE 9
```

```c
#include <zephyr/net/socket.h>
```

启用连接上的保活消息（Keep-alive Messages）发送。

<a id="ga7390a499529d767680cf7ac578f9586d"></a>

### `ZSOCK_SO_LINGER`

```c
#define ZSOCK_SO_LINGER 13
```

```c
#include <zephyr/net/socket.h>
```

套接字关闭时延迟结束（Linger）。

接受 `struct net_linger` 作为参数（Argument）。

<a id="ga252b932a5cdc4909885b4d0a7968a5f3"></a>

### `ZSOCK_SO_OOBINLINE`

```c
#define ZSOCK_SO_OOBINLINE 10
```

```c
#include <zephyr/net/socket.h>
```

将带外数据（Out-of-band Data）放入接收流（Receive Stream）；为兼容性而保留，实际忽略。

<a id="ga477c2939c20f24ae4119d6ef8b248c08"></a>

### `ZSOCK_SO_PRIORITY`

```c
#define ZSOCK_SO_PRIORITY 12
```

```c
#include <zephyr/net/socket.h>
```

套接字优先级（Socket Priority）。

<a id="ga1b6d5006c4dade22d3a1c8679aa74d39"></a>

### `ZSOCK_SO_PROTOCOL`

```c
#define ZSOCK_SO_PROTOCOL 38
```

```c
#include <zephyr/net/socket.h>
```

套接字（Socket）使用的协议（Protocol）。

<a id="gad841445fdb66a8303e49b36f2aa52faa"></a>

### `ZSOCK_SO_RCVBUF`

```c
#define ZSOCK_SO_RCVBUF 8
```

```c
#include <zephyr/net/socket.h>
```

套接字接收缓冲区（Socket Receive Buffer）的大小。

<a id="gaa1ee3324ef29c0bcb66c893f8f0a0a22"></a>

### `ZSOCK_SO_RCVLOWAT`

```c
#define ZSOCK_SO_RCVLOWAT 18
```

```c
#include <zephyr/net/socket.h>
```

接收低水位（Receive Low Watermark）；为兼容性而保留，实际忽略。

<a id="ga127dd9d8339be8b435ace9d6ad95e850"></a>

### `ZSOCK_SO_RCVTIMEO`

```c
#define ZSOCK_SO_RCVTIMEO 20
```

```c
#include <zephyr/net/socket.h>
```

接收超时（Receive Timeout）。适用于 `recv()` 等接收函数，但不适用于 `connect()`。

<a id="gac2031f7190b1557d9d5020a93326d214"></a>

### `ZSOCK_SO_REUSEADDR`

```c
#define ZSOCK_SO_REUSEADDR 2
```

```c
#include <zephyr/net/socket.h>
```

地址复用（Address Reuse）。

<a id="gacc93dbba4441b1617173bf9ca3c36c66"></a>

### `ZSOCK_SO_REUSEPORT`

```c
#define ZSOCK_SO_REUSEPORT 15
```

```c
#include <zephyr/net/socket.h>
```

允许多个套接字（Socket）复用同一个端口（Port）。

<a id="gaea93c05216e4a1d518406f42e7c7f8bc"></a>

### `ZSOCK_SO_SNDBUF`

```c
#define ZSOCK_SO_SNDBUF 7
```

```c
#include <zephyr/net/socket.h>
```

套接字发送缓冲区（Socket Send Buffer）的大小。

<a id="ga87e4d65779b4c60b9a0c1ced480ed033"></a>

### `ZSOCK_SO_SNDLOWAT`

```c
#define ZSOCK_SO_SNDLOWAT 19
```

```c
#include <zephyr/net/socket.h>
```

发送低水位（Send Low Watermark）；为兼容性而保留，实际忽略。

<a id="ga786304b8676b8bc6466a7235396a07f7"></a>

### `ZSOCK_SO_SNDTIMEO`

```c
#define ZSOCK_SO_SNDTIMEO 21
```

```c
#include <zephyr/net/socket.h>
```

发送超时（Send Timeout）。

<a id="ga3f136ae14247139586f85cd45d046fb3"></a>

### `ZSOCK_SO_SOCKS5`

```c
#define ZSOCK_SO_SOCKS5 60
```

```c
#include <zephyr/net/socket.h>
```

为套接字（Socket）启用 SOCKS5。

<a id="ga77fdf74646e0c3b28240ae5899cee058"></a>

### `ZSOCK_SO_TIMESTAMPING`

```c
#define ZSOCK_SO_TIMESTAMPING 37
```

```c
#include <zephyr/net/socket.h>
```

为发送（TX）、接收（RX）或两种方向的数据包添加时间戳（Timestamp）。

支持多个时间戳来源（Timestamp Sources）。

<a id="ga091f558e4c5c15e615281ba21feb130f"></a>

### `ZSOCK_SO_TXTIME`

```c
#define ZSOCK_SO_TXTIME 61
```

```c
#include <zephyr/net/socket.h>
```

套接字发送时间（Socket TX Time），即数据应发送的时刻。

<a id="ga950c4ad7cb1272272e6db23a20cb24a5"></a>

### `ZSOCK_SO_TYPE`

```c
#define ZSOCK_SO_TYPE 3
```

```c
#include <zephyr/net/socket.h>
```

套接字类型（Socket Type）。

<a id="gaf851a5752668188d6c9d66f6d349377a"></a>

### `ZSOCK_SOF_TIMESTAMPING_RX_HARDWARE`

```c
#define ZSOCK_SOF_TIMESTAMPING_RX_HARDWARE BIT(0)
```

```c
#include <zephyr/net/socket.h>
```

时间戳生成标志（Timestamp Generation Flags）。

请求由网络适配器（Network Adapter）生成的接收时间戳（RX Timestamp）。

<a id="gafe8cfcce94475fa2dcc2d0e56d6a7134"></a>

### `ZSOCK_SOF_TIMESTAMPING_TX_HARDWARE`

```c
#define ZSOCK_SOF_TIMESTAMPING_TX_HARDWARE BIT(1)
```

```c
#include <zephyr/net/socket.h>
```

请求由网络适配器（Network Adapter）生成的发送时间戳（TX Timestamp）。

可通过套接字选项（Socket Option）或控制消息（Control Message）启用。

<a id="gaaa2786e0b2410518b6f99e0ee196f4d4"></a>

### `ZSOCK_SOL_SOCKET`

```c
#define ZSOCK_SOL_SOCKET 1
```

```c
#include <zephyr/net/socket.h>
```

套接字级选项（Socket-level Option）。

<a id="ga95372181a0f868383e6631de84145e39"></a>

### `ZSOCK_SOMAXCONN`

```c
#define ZSOCK_SOMAXCONN 128
```

```c
#include <zephyr/net/socket.h>
```

`listen`：待连接队列（Backlog Queue）的最大长度。

<a id="ga0b29b699728d87c097ff51c95d2f80b1"></a>

### `ZSOCK_TCP_KEEPCNT`

```c
#define ZSOCK_TCP_KEEPCNT 4
```

```c
#include <zephyr/net/socket.h>
```

断开连接前发送的保活消息（Keepalive）数量。

<a id="ga720e01b6ceaff867dd673cdd8b648bf2"></a>

### `ZSOCK_TCP_KEEPIDLE`

```c
#define ZSOCK_TCP_KEEPIDLE 2
```

```c
#include <zephyr/net/socket.h>
```

经过此时间后开始发送保活消息（Keepalive），单位为秒。

<a id="ga1ebb7dbc45bf6b1b01cb5fe482a3f1b8"></a>

### `ZSOCK_TCP_KEEPINTVL`

```c
#define ZSOCK_TCP_KEEPINTVL 3
```

```c
#include <zephyr/net/socket.h>
```

保活消息（Keepalive）之间的间隔，单位为秒。

<a id="gaed65035762b59c3717cdc856a15f92fa"></a>

### `ZSOCK_TCP_NODELAY`

```c
#define ZSOCK_TCP_NODELAY 1
```

```c
#include <zephyr/net/socket.h>
```

禁用 TCP 缓冲（Buffering）；为兼容性而保留，实际忽略。

<a id="ga8e63f889afc9ca06bfea2b90e4e88b3e"></a>

### `ZSOCK_UDP_OPT`

```c
#define ZSOCK_UDP_OPT 1
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用所有 UDP 选项（UDP Options），值为 `int` 类型布尔值；这些选项来自 RFC 9868。

<a id="ga1e80d0746eac06c45ef53011cefb9b66"></a>

### `ZSOCK_UDP_OPT_APC`

```c
#define ZSOCK_UDP_OPT_APC 3
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP APC 选项（Option），值为 `int` 类型布尔值。

<a id="gac336fbf99b335b69a05004b6ca6a0104"></a>

### `ZSOCK_UDP_OPT_AUTH`

```c
#define ZSOCK_UDP_OPT_AUTH 10
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP AUTH 选项（Option），值为 `int` 类型布尔值。

<a id="ga86605887c247cf1a11701c5675c7895d"></a>

### `ZSOCK_UDP_OPT_CMSG_APC`

```c
#define ZSOCK_UDP_OPT_CMSG_APC 1
```

```c
#include <zephyr/net/socket.h>
```

辅助数据（Ancillary Data）中 `IPPROTO_UDP` 级别的控制消息（cmsg）类型。

CRC32c，类型为 `uint32_t`。

<a id="ga473e4bab8f40c07e7bfc618f256868eb"></a>

### `ZSOCK_UDP_OPT_CMSG_MDS`

```c
#define ZSOCK_UDP_OPT_CMSG_MDS 2
```

```c
#include <zephyr/net/socket.h>
```

对端 MDS（Peer MDS），类型为 `uint16_t`。

<a id="ga2e00bde85be42b224689e67b9519ba91"></a>

### `ZSOCK_UDP_OPT_CMSG_MRDS`

```c
#define ZSOCK_UDP_OPT_CMSG_MRDS 3
```

```c
#include <zephyr/net/socket.h>
```

结构体（Structure）：`struct net_udp_opt_mrds`。

<a id="ga663d30569b681b857b2d3da8c9c5975a"></a>

### `ZSOCK_UDP_OPT_CMSG_REQ`

```c
#define ZSOCK_UDP_OPT_CMSG_REQ 4
```

```c
#include <zephyr/net/socket.h>
```

回显请求令牌（Echo Request Token），类型为 `uint32_t`。

<a id="ga4cea51ab6931e1020694569edaedb78b"></a>

### `ZSOCK_UDP_OPT_CMSG_RES`

```c
#define ZSOCK_UDP_OPT_CMSG_RES 5
```

```c
#include <zephyr/net/socket.h>
```

回显响应令牌（Echo Response Token），类型为 `uint32_t`。

<a id="ga0cde876903364ec01f633a1b973f0e6e"></a>

### `ZSOCK_UDP_OPT_CMSG_TIME`

```c
#define ZSOCK_UDP_OPT_CMSG_TIME 6
```

```c
#include <zephyr/net/socket.h>
```

结构体（Structure）：`struct net_udp_opt_time`。

<a id="ga989a840540b557473a4a4438915f59de"></a>

### `ZSOCK_UDP_OPT_DPLPMTUD`

```c
#define ZSOCK_UDP_OPT_DPLPMTUD 15
```

```c
#include <zephyr/net/socket.h>
```

通过 UDP 选项启用或禁用数据报分包层路径 MTU 发现（DPLPMTUD），参见 RFC 9869；值为 `int` 类型布尔值。

<a id="ga5cd27e199f4507097b9ab2f74ba88c10"></a>

### `ZSOCK_UDP_OPT_DPLPMTUD_APP_RESPOND`

```c
#define ZSOCK_UDP_OPT_DPLPMTUD_APP_RESPOND 16
```

```c
#include <zephyr/net/socket.h>
```

由应用程序自行完成 REQ→RES 回显（Echo），而非由协议栈处理；值为 `int` 类型布尔值。

<a id="ga92c67eface4732a6b8faf182fc91dfcb"></a>

### `ZSOCK_UDP_OPT_EXP`

```c
#define ZSOCK_UDP_OPT_EXP 11
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP EXP 选项（Option），值为 `int` 类型布尔值。

<a id="ga44c749f760057277985a91525ad75846"></a>

### `ZSOCK_UDP_OPT_FRAG`

```c
#define ZSOCK_UDP_OPT_FRAG 4
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP 分片选项（Fragmentation Option），值为 `int` 类型布尔值。

<a id="gaa976bda2ebe370345e7d9324fd0102e1"></a>

### `ZSOCK_UDP_OPT_MDS`

```c
#define ZSOCK_UDP_OPT_MDS 5
```

```c
#include <zephyr/net/socket.h>
```

设置或获取 UDP MDS 选项值（Option Value），类型为 `uint16_t`。

<a id="ga023dea5abc5f784df8e988492bc5bfb4"></a>

### `ZSOCK_UDP_OPT_MRDS`

```c
#define ZSOCK_UDP_OPT_MRDS 6
```

```c
#include <zephyr/net/socket.h>
```

设置或获取 UDP MRDS 选项值（Option Value），类型为 `struct net_udp_opt_mrds`。

<a id="ga0394de45aedd088ebcfb11006836572c"></a>

### `ZSOCK_UDP_OPT_OCS`

```c
#define ZSOCK_UDP_OPT_OCS 2
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP OCS，值为 `int` 类型布尔值（Boolean）。

<a id="ga62c9b039d368e75991937619e9adf8cc"></a>

### `ZSOCK_UDP_OPT_REQ`

```c
#define ZSOCK_UDP_OPT_REQ 7
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP REQ 选项（Option），值为 `int` 类型布尔值。

<a id="gaec4348215929b4deff996dcac0ccd5d3"></a>

### `ZSOCK_UDP_OPT_RES`

```c
#define ZSOCK_UDP_OPT_RES 8
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP RES 选项（Option），值为 `int` 类型布尔值。

<a id="gaaf3a09237d37bb112ee72504d926cd89"></a>

### `ZSOCK_UDP_OPT_TIME`

```c
#define ZSOCK_UDP_OPT_TIME 9
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP TIME 选项（Option），值为 `int` 类型布尔值。

<a id="gaf0ea7830aa95f7fe5c88bbc6b11f9627"></a>

### `ZSOCK_UDP_OPT_UCMP`

```c
#define ZSOCK_UDP_OPT_UCMP 12
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP UCMP 选项（Option），值为 `int` 类型布尔值。

<a id="gaf95d8f076a0d4232992aea0f2545b65f"></a>

### `ZSOCK_UDP_OPT_UENC`

```c
#define ZSOCK_UDP_OPT_UENC 13
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP UENC 选项（Option），值为 `int` 类型布尔值。

<a id="ga3d3737422eb33cf98300e18c5e24a214"></a>

### `ZSOCK_UDP_OPT_UEXP`

```c
#define ZSOCK_UDP_OPT_UEXP 14
```

```c
#include <zephyr/net/socket.h>
```

启用或禁用 UDP UEXP 选项（Option），值为 `int` 类型布尔值。

<a id="ga1cdeeddce9000b9fd29b638c422f48f8"></a>

### `zsock_fd_set`

```c
typedef struct zvfs_fd_set zsock_fd_set
```

```c
#include <zephyr/net/socket_select.h>
```

套接字文件描述符集合（socket file descriptor set）。

<a id="ga1532a65955c402cbb365becb58167f19"></a>

### `zsock_accept()`

```c
int zsock_accept ( int sock, struct net_sockaddr * addr, net_socklen_t * addrlen )
```

```c
#include <zephyr/net/socket.h>
```

在监听套接字（Listening Socket）上接受连接。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `accept()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/accept.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `accept()` 名称提供。

<a id="ga70909e3233d6523d0ad9566b5edd117c"></a>

### `zsock_bind()`

```c
int zsock_bind ( int sock, const struct net_sockaddr * addr, net_socklen_t addrlen )
```

```c
#include <zephyr/net/socket.h>
```

将套接字（Socket）绑定到本地网络地址（Local Network Address）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `bind()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/bind.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `bind()` 名称提供。

<a id="gae60d7ca486955dd79a2821d1f646c349"></a>

### `zsock_close()`

```c
int zsock_close ( int sock)
```

```c
#include <zephyr/net/socket.h>
```

关闭网络套接字（Network Socket）。

关闭网络套接字（Network Socket）。如果定义了 `CONFIG_POSIX_API`，此函数也以 `close()` 名称提供，此时可能与通用 POSIX `close()` 函数冲突。

<a id="gad858da9650c1270faf5229e3888d7db1"></a>

### `zsock_connect()`

```c
int zsock_connect ( int sock, const struct net_sockaddr * addr, net_socklen_t addrlen )
```

```c
#include <zephyr/net/socket.h>
```

将套接字（Socket）连接到对端网络地址（Peer Network Address）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `connect()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/connect.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `connect()` 名称提供。

<a id="gab069dc3ebc140af65801a73fcac4f629"></a>

### `zsock_fcntl_impl()`

```c
int zsock_fcntl_impl ( int sock, int cmd, int flags )
```

```c
#include <zephyr/net/socket.h>
```

控制套接字（Socket）的阻塞／非阻塞模式（Blocking/Non-blocking Mode）。

此函数仅允许将套接字（Socket）配置为阻塞或非阻塞（`O_NONBLOCK`）操作。如果定义了 `CONFIG_POSIX_API`，此函数也以 `fcntl()` 名称提供，此时可能与通用 POSIX `fcntl()` 函数冲突。

<a id="ga7023ec00d24af41a7cbf5f376fb44487"></a>

### `ZSOCK_FD_CLR()`

```c
void ZSOCK_FD_CLR ( int fd, zsock_fd_set * set )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket_select.h>
```

从 `fd_set` 移除套接字。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `FD_CLR()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `FD_CLR()` 名称提供。

<a id="gab92b08adccc22a85e7a1c06bf11a88bc"></a>

### `ZSOCK_FD_ISSET()`

```c
int ZSOCK_FD_ISSET ( int fd, zsock_fd_set * set )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket_select.h>
```

检查套接字是否属于 `fd_set`。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `FD_ISSET()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `FD_ISSET()` 名称提供。

<a id="ga5d07f52910f6d881295ec659716767f1"></a>

### `ZSOCK_FD_SET()`

```c
void ZSOCK_FD_SET ( int fd, zsock_fd_set * set )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket_select.h>
```

将套接字添加到 `fd_set`。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `FD_SET()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `FD_SET()` 名称提供。

<a id="gaa4855f07c1329a150f371044e4384490"></a>

### `ZSOCK_FD_ZERO()`

```c
void ZSOCK_FD_ZERO ( zsock_fd_set * set)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket_select.h>
```

初始化并清空 `fd_set`。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `FD_ZERO()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `FD_ZERO()` 名称提供。

<a id="ga7953da2e52bcfad51b877de6d7fd6cc9"></a>

### `zsock_freeaddrinfo()`

```c
void zsock_freeaddrinfo ( struct zsock_addrinfo * ai)
```

```c
#include <zephyr/net/socket.h>
```

释放 `zsock_getaddrinfo()` 返回的结果。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `freeaddrinfo()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/freeaddrinfo.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `freeaddrinfo()` 名称提供。

<a id="gaa9d9e97c347b3854dc73d7ba33d8ca4b"></a>

### `zsock_gai_strerror()`

```c
const char * zsock_gai_strerror ( int errcode)
```

```c
#include <zephyr/net/socket.h>
```

将 `zsock_getaddrinfo()` 的错误码（Error Code）转换为文本消息。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `gai_strerror()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/gai_strerror.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `gai_strerror()` 名称提供。

<a id="ga21a871d1fa6b6beeed88408761877873"></a>

### `zsock_get_context_object()`

```c
void * zsock_get_context_object ( int sock)
```

```c
#include <zephyr/net/socket.h>
```

获取文件描述符（File Descriptor）关联的网络上下文（Net Context）。

启用 `CONFIG_USERSPACE` 后，内核的对象权限系统（Object Permission System）必须应用于套接字文件描述符（Socket File Descriptor）。套接字打开时，默认只有调用者拥有权限；除非明确授予权限，否则其他线程的访问将失败。

实现方式是：用 `__net_socket` 标记实现网络套接字文件描述符所关联底层对象的数据结构定义。指向这些结构体实例的所有指针，都会被内核识别为 `K_OBJ_NET_SOCKET` 类型的内核对象（Kernel Object）。

此 API 供需要向另一线程授予特定文件描述符关联对象的访问权限的线程使用。返回的指针表示底层的 `K_OBJ_NET_SOCKET`，可以传递给 `k_object_access_grant()` 等 API。

在 Linux 这样的系统中，线程（Thread）运行于进程（Process）内，并共享虚拟地址空间（Virtual Address Space）；文件描述符的作用域在进程级别实现，因此不需要这种管理方式。

但在 Zephyr 中，文件描述符的作用域（File Descriptor Scope）是全局的，而基于内存保护单元（MPU）的系统缺乏内存虚拟化硬件，无法实现类似进程的模型。它们使用独立的对象权限（Object Permissions）和内存域（Memory Domains）来定义线程的访问范围。

用户线程（User Thread）不能直接访问返回的对象，尝试访问其内存将触发故障（Fault）；此指针只能用于调用权限分配接口，其规则与设备驱动程序和进程间通信（IPC）等其他内核对象完全一致。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 文件描述符（File Descriptor）。 |

**返回（Returns）**：返回值（Returns）：指向关联网络套接字对象（Network Socket Object）的指针；如果文件描述符无效，或调用者没有访问权限，则返回 `NULL`。

<a id="gaf59c97c9bd07f188e3f06b2372ac1856"></a>

### `zsock_getaddrinfo()`

```c
int zsock_getaddrinfo ( const char * host, const char * service, const struct zsock_addrinfo * hints, struct zsock_addrinfo ** res )
```

```c
#include <zephyr/net/socket.h>
```

将域名（Domain Name）解析为一个或多个网络地址（Network Address）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `getaddrinfo()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getaddrinfo.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `getaddrinfo()` 名称提供。

<a id="ga8b348d886f1bc4f4cdf6e2260844f6e1"></a>

### `zsock_gethostname()`

```c
int zsock_gethostname ( char * buf, size_t len )
```

```c
#include <zephyr/net/socket.h>
```

获取本地主机名（Local Host Name）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `gethostname()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/gethostname.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `gethostname()` 名称提供。

<a id="ga5b02979bf93763a9cc5711c7267d5de8"></a>

### `zsock_getnameinfo()`

```c
int zsock_getnameinfo ( const struct net_sockaddr * addr, net_socklen_t addrlen, char * host, net_socklen_t hostlen, char * serv, net_socklen_t servlen, int flags )
```

```c
#include <zephyr/net/socket.h>
```

将网络地址（Network Address）解析为域名（Domain Name）或 ASCII 地址。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `getnameinfo()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getnameinfo.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `getnameinfo()` 名称提供。

<a id="ga78b0ca26c0aaf5e64b05da8caa8c253c"></a>

### `zsock_getpeername()`

```c
int zsock_getpeername ( int sock, struct net_sockaddr * addr, net_socklen_t * addrlen )
```

```c
#include <zephyr/net/socket.h>
```

获取对端名称（Peer Name）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `getpeername()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getpeername.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `getpeername()` 名称提供。

<a id="ga6bf17561e03600ed870dff702b513d9c"></a>

### `zsock_getsockname()`

```c
int zsock_getsockname ( int sock, struct net_sockaddr * addr, net_socklen_t * addrlen )
```

```c
#include <zephyr/net/socket.h>
```

获取套接字名称（Socket Name）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `getsockname()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockname.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `getsockname()` 名称提供。

<a id="ga6aa12f0dbed8ded425555debba044a98"></a>

### `zsock_getsockopt()`

```c
int zsock_getsockopt ( int sock, int level, int optname, void * optval, net_socklen_t * optlen )
```

```c
#include <zephyr/net/socket.h>
```

获取各种套接字选项（Socket Options）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 getsockopt() 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockopt.html)。在 Zephyr 中，此函数支持 POSIX 定义的套接字选项（Socket Options）的一个子集，也支持 Linux 中的部分额外选项；其中一些选项不执行实际操作，仅用于方便移植现有代码。如果定义了 `CONFIG_POSIX_API`，此函数也以 `getsockopt()` 名称提供。

<a id="gad3dbb44d7b49249c124e41041aca6536"></a>

### `zsock_inet_ntop()`

```c
char * zsock_inet_ntop ( net_sa_family_t family, const void * src, char * dst, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket.h>
```

将网络地址（Network Address）从内部表示转换为数字 ASCII 形式（Numeric ASCII Form）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `inet_ntop()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_ntop.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `inet_ntop()` 名称提供。

<a id="gaf0130ad342c6873d68bdc51d9cf1167b"></a>

### `zsock_inet_pton()`

```c
int zsock_inet_pton ( net_sa_family_t family, const char * src, void * dst )
```

```c
#include <zephyr/net/socket.h>
```

将网络地址（Network Address）从数字 ASCII 形式（Numeric ASCII Form）转换为内部表示。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `inet_pton()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_pton.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `inet_pton()` 名称提供。

<a id="ga0255a43336642aaeeaa5bff4c29c9389"></a>

### `zsock_ioctl_impl()`

```c
int zsock_ioctl_impl ( int sock, unsigned long request, va_list ap )
```

```c
#include <zephyr/net/socket.h>
```

控制底层套接字参数（Underlying Socket Parameters）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 ioctl() 说明](https://pubs.opengroup.org/onlinepubs/9699919799/functions/ioctl.html)。此函数支持查询或修改底层套接字参数（Underlying Socket Parameters）。当前支持的请求值包括：

- 请求值（Request Value）：`ZFD_IOCTL_FIONBIO`。
- 请求值（Request Value）：`ZFD_IOCTL_FIONREAD`。
- 请求值（Request Value）：`ZFD_IOCTL_FIONWRITE`。如果定义了 `CONFIG_POSIX_API`，此函数也以 `ioctl()` 名称提供，此时可能与通用 POSIX `ioctl()` 函数冲突。

<a id="gae8ea59ea82063aa28a9b72da2f08c9fd"></a>

### `zsock_listen()`

```c
int zsock_listen ( int sock, int backlog )
```

```c
#include <zephyr/net/socket.h>
```

设置流式套接字（STREAM Socket），使其接受对端连接（Peer Connection）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `listen()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/listen.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `listen()` 名称提供。

<a id="ga518361903c9fac3766164d38243872e3"></a>

### `zsock_poll()`

```c
int zsock_poll ( struct zsock_pollfd * fds, int nfds, int timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket.h>
```

高效轮询多个套接字（Socket）的事件（Event）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `poll()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/poll.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `poll()` 名称提供，此时可能与通用 POSIX `poll()` 函数冲突。

<a id="ga8a7d82cfb02a45de59ccd05614eb78d6"></a>

### `zsock_recv()`

```c
ssize_t zsock_recv ( int sock, void * buf, size_t max_len, int flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket.h>
```

从已连接的对端（Connected Peer）接收数据。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `recv()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recv.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `recv()` 名称提供。

<a id="ga89271d76123b0a69e0c40ae4de58bd0a"></a>

### `zsock_recvfrom()`

```c
ssize_t zsock_recvfrom ( int sock, void * buf, size_t max_len, int flags, struct net_sockaddr * src_addr, net_socklen_t * addrlen )
```

```c
#include <zephyr/net/socket.h>
```

从任意网络地址（Network Address）接收数据。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `recvfrom()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvfrom.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `recvfrom()` 名称提供。

<a id="ga02b0de9a15c2d1133b87216d6afc203f"></a>

### `zsock_recvmsg()`

```c
ssize_t zsock_recvmsg ( int sock, struct net_msghdr * msg, int flags )
```

```c
#include <zephyr/net/socket.h>
```

从任意网络地址（Network Address）接收消息（Message）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `recvmsg()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvmsg.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `recvmsg()` 名称提供。

<a id="ga1a065da89061bcb10b10663a9ffbdd10"></a>

### `zsock_select()`

```c
int zsock_select ( int nfds, zsock_fd_set * readfds, zsock_fd_set * writefds, zsock_fd_set * exceptfds, struct zsock_timeval * timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket_select.h>
```

轮询多个套接字事件的传统函数（legacy function）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 select() 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)。此函数用于方便移植现有代码，但由于效率较低，不建议使用，应使用 `zsock_poll()`。在 Zephyr 中，此函数仅适用于套接字（Socket），不适用于任意文件描述符（File Descriptor）。如果定义了 `CONFIG_POSIX_API`，此函数也以 `select()` 名称提供，此时可能与通用 POSIX `select()` 函数冲突。

<a id="ga2d8c2173986f67dde6dc5721bf690855"></a>

### `zsock_send()`

```c
ssize_t zsock_send ( int sock, const void * buf, size_t len, int flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socket.h>
```

向已连接的对端（Connected Peer）发送数据。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `send()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/send.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `send()` 名称提供。

<a id="ga8a8e90b68fb77179677f237bc22289ec"></a>

### `zsock_send_all()`

```c
int zsock_send_all ( int sock, const void * buf, size_t len, int flags, k_timeout_t timeout, size_t * sent_len )
```

```c
#include <zephyr/net/socket.h>
```

向任意网络地址（Network Address）发送数据。

此函数会尝试发送请求的全部数据，必要时阻塞（Block）。用户可以使用套接字发送超时（Socket Send Timeout）限制此函数消耗的时间。

参数的规范性描述（Normative Description）参见 [POSIX.1-2017 的 sendto() 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendto.html)。此函数与 `zsock_send()` 的区别在于：它尝试发送请求的全部数据，必要时阻塞（Block），直到全部数据发送完毕或超时。注意，这仅适用于 TCP 等流式套接字（Stream Socket）。如果超时设为 `K_NO_WAIT`，此函数在第一次发送尝试后返回，实际发送的数据可能少于请求的数据量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 套接字文件描述符（Socket File Descriptor）。 |
| `buf` | 指向待发送数据缓冲区（Data Buffer）的指针。 |
| `len` | 待发送数据的长度（Length）。 |
| `flags` | 发送数据所用的套接字标志（Socket Flags）。 |
| `timeout` | 等待数据发送完毕的最长时间（Maximum Time）。 |
| `sent_len` | 指向用于保存实际发送字节数（Actual Number of Bytes Sent）的变量的指针。如果调用者不需要此信息，可以设为 `NULL`。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回 `-errno`。

<a id="gad3274fe71d43caf8c4d92fffb589375e"></a>

### `zsock_sendmsg()`

```c
ssize_t zsock_sendmsg ( int sock, const struct net_msghdr * msg, int flags )
```

```c
#include <zephyr/net/socket.h>
```

向任意网络地址（Network Address）发送数据。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `sendmsg()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendmsg.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `sendmsg()` 名称提供。

<a id="ga4d2d0823ad8785ffdc2ae327e8651d3f"></a>

### `zsock_sendmsg_all()`

```c
int zsock_sendmsg_all ( int sock, const struct net_msghdr * msg, int flags, k_timeout_t timeout, size_t * sent_len )
```

```c
#include <zephyr/net/socket.h>
```

向任意网络地址（Network Address）发送数据。

此函数会尝试发送请求的全部数据，必要时阻塞（Block）。用户可以使用套接字发送超时（Socket Send Timeout）限制此函数消耗的时间。

参数的规范性描述（Normative Description）参见 [POSIX.1-2017 的 sendmsg() 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendmsg.html)。此函数与 `zsock_sendmsg()` 的区别在于：它尝试发送请求的全部数据，必要时阻塞（Block），直到全部数据发送完毕或超时。注意，这仅适用于 TCP 等流式套接字（Stream Socket）。如果超时设为 `K_NO_WAIT`，此函数在第一次发送尝试后返回，实际发送的数据可能少于请求的数据量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sock` | 套接字文件描述符（Socket File Descriptor）。 |
| `msg` | 指向描述待发送数据的消息头（Message Header）的指针。 |
| `flags` | 发送数据所用的套接字标志（Socket Flags）。 |
| `timeout` | 等待数据发送完毕的最长时间（Maximum Time）。 |
| `sent_len` | 指向用于保存实际发送字节数（Actual Number of Bytes Sent）的变量的指针。如果调用者不需要此信息，可以设为 `NULL`。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回 `-errno`。

<a id="ga9f4ff3d1637393cbe74bd111cc6f432a"></a>

### `zsock_sendto()`

```c
ssize_t zsock_sendto ( int sock, const void * buf, size_t len, int flags, const struct net_sockaddr * dest_addr, net_socklen_t addrlen )
```

```c
#include <zephyr/net/socket.h>
```

向任意网络地址（Network Address）发送数据。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `sendto()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendto.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `sendto()` 名称提供。

<a id="ga71ac8d52c87b9182a9f1a03614e3dba7"></a>

### `zsock_setsockopt()`

```c
int zsock_setsockopt ( int sock, int level, int optname, const void * optval, net_socklen_t optlen )
```

```c
#include <zephyr/net/socket.h>
```

设置各种套接字选项（Socket Options）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 setsockopt() 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/setsockopt.html)。在 Zephyr 中，此函数支持 POSIX 定义的套接字选项（Socket Options）的一个子集，也支持 Linux 中的部分额外选项；其中一些选项不执行实际操作，仅用于方便移植现有代码。如果定义了 `CONFIG_POSIX_API`，此函数也以 `setsockopt()` 名称提供。

<a id="gac56432bf901efaf8ef782430ac143f03"></a>

### `zsock_shutdown()`

```c
int zsock_shutdown ( int sock, int how )
```

```c
#include <zephyr/net/socket.h>
```

关闭套接字（Socket）的发送／接收操作。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 shutdown() 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/shutdown.html)。但此函数当前在 Zephyr 中不产生任何效果，仅为兼容现有代码而提供。如果定义了 `CONFIG_POSIX_API`，此函数也以 `shutdown()` 名称提供。

<a id="ga5693d19a0bdff45a5cb09227683d8631"></a>

### `zsock_socket()`

```c
int zsock_socket ( int family, int type, int proto )
```

```c
#include <zephyr/net/socket.h>
```

创建网络套接字（Network Socket）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `socket()` 说明](http://pubs.opengroup.org/onlinepubs/9699919799/functions/socket.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `socket()` 名称提供。

如果启用了 `CONFIG_USERSPACE`，调用者将获得返回的文件描述符所关联上下文对象（Context Object）的访问权限。

**参阅（See Also）**：另请参阅（See Also）：`zsock_get_context_object()`。

<a id="ga1f5e089c9fb39d3a8884502a11e389b3"></a>

### `zsock_socketpair()`

```c
int zsock_socketpair ( int family, int type, int proto, int * sv )
```

```c
#include <zephyr/net/socket.h>
```

创建一对未命名且相互连接的套接字（Unnamed Pair of Connected Sockets）。

规范性描述（Normative Description）参见 [POSIX.1-2017 的 `socketpair()` 说明](https://pubs.opengroup.org/onlinepubs/009695399/functions/socketpair.html)。如果定义了 `CONFIG_POSIX_API`，此函数也以 `socketpair()` 名称提供。


## 1.17\_原页交叉引用（Cross References）

- [IPv4 套接字选项（Socket options）](../api_transport_control_topic_reference/P009_IPv4 套接字选项（Socket options）.md)
- [IPv6 套接字选项（Socket options）](../api_buffer_paging_topic_reference/P010_IPv6 套接字选项（Socket options）.md)
- [TLS 套接字选项（Socket options）](../api_media_cellular_topic_reference/P014_TLS 套接字选项（Socket options）.md)
- [分组套接字的套接字选项（Socket options for packet socket）](../api_extension_topic_reference/P022_分组套接字的套接字选项（Socket options for packet socket）.md)
- [zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [ZVFS_FD_SETSIZE](../api_file_media_sensor_reference/P003_zephyr__sys__fdtable.h_文件参考.md#ae8d10dc8bd02e619f8c384c493f53709)
- [zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_msghdr](../network_core_model_reference/P112_net_msghdr_结构体.md)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [fd_set](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#ae96e561afd32b1445d8a7370f23762a2)
- [bind()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a05b4e957a092db3e68281988ceb32df8)
- [connect()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)
- [RFC 5014](https://datatracker.ietf.org/doc/html/rfc5014)
- [recv()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [RFC 9868](https://datatracker.ietf.org/doc/html/rfc9868)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [RFC 9869](https://datatracker.ietf.org/doc/html/rfc9869)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/net/socket.h](../api_file_kernel_network_reference/P009_zephyr__net__socket.h_文件参考.md)
- [zephyr/net/socket_select.h](../api_file_system_device_reference/P047_zephyr__net__socket_select.h_文件参考.md)
- [net_ipv6_is_ll_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gad072b3bf7bc05927fe27f5503a31f25c)
- [net_ipv6_is_addr_loopback](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga9af9b1750c2db50a170e1b694df24227)
- [net_ipv6_is_addr_mcast_global](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf91b9c08e327589eb0fd33d5754743cf)
- [net_ipv6_is_addr_mcast_link](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae1660acfdbf897afbc6119ae608e476f)
- [net_ipv6_is_addr_mcast_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga43b6e313f5a938d688d3bc734a299408)
- [net_ipv6_is_addr_mcast_org](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga9e7bf1c3503039c78f99f3deab277d4f)
- [net_ipv6_is_addr_mcast_site](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga9084b403ca6a591d24f975e669560b6c)
- [net_ipv6_is_addr_mcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga418a57b9f12205de21cbe83951e960bb)
- [net_ipv6_is_sl_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaec37f4f9d223e5be3c141ec1ae4ef288)
- [net_ipv6_addr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga6704d86fb9962bdb6d27a41d4053bfc7)
- [net_ipv6_unspecified_address](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf41e178ed45d6a483e240f939cd2f41d)
- [net_ipv6_addr_is_v4_mapped](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga2716cdb6f85693d7c5a96446a7a41e03)
- [net_linger](../network_core_model_reference/P104_net_linger_结构体.md)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/accept.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/accept.html)
- [accept()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)
- [CONFIG_POSIX_API](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/bind.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/bind.html)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/connect.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/connect.html)
- [fcntl()](../api_file_reference/P112_zephyr__posix__fcntl.h_文件参考.md#acfc4bf677fc9f8be66d9624175cb3775)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)
- [FD_CLR()](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#a0835759308c63ca23a1760980eea21d7)
- [FD_ISSET()](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#ac38fe1ff5db5e46e778f13ad5accdf98)
- [FD_SET()](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#a8c14b5b455292781fbcc2e34a47923d6)
- [FD_ZERO()](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#a3f88268fa19b2068723de10d848e8a42)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/freeaddrinfo.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/freeaddrinfo.html)
- [freeaddrinfo()](../api_file_supplement_reference/P079_zephyr__posix__netdb.h_文件参考.md#ae854ec9955d62f1791342f9c2b8abcee)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/gai_strerror.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/gai_strerror.html)
- [gai_strerror()](../api_file_supplement_reference/P079_zephyr__posix__netdb.h_文件参考.md#a8033b3171adc399803161694ea422c4f)
- [k_object_access_grant()](../api_radio_permission_topic_reference/P017_用户模式 API（User Mode APIs）.md#ga94087bedf96fe2a2bea437d3d585ca22)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getaddrinfo.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getaddrinfo.html)
- [getaddrinfo()](../api_file_supplement_reference/P079_zephyr__posix__netdb.h_文件参考.md#adc9ea491d9008de7cd9e0a5b9147ca70)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/gethostname.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/gethostname.html)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getnameinfo.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getnameinfo.html)
- [getnameinfo()](../api_file_supplement_reference/P079_zephyr__posix__netdb.h_文件参考.md#a5c82f7d491ae353012f42bf60e9c9f20)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getpeername.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getpeername.html)
- [getpeername()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a5580f3aa0827aae89459c24b91f80cae)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockname.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockname.html)
- [getsockname()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#abef44fb98f476ef2adba92bbdb362a1b)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockopt.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockopt.html)
- [getsockopt()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_ntop.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_ntop.html)
- [inet_ntop()](../api_file_reference/P161_zephyr__posix__arpa__inet.h_文件参考.md#ae93e32740fb355baef0cab02133e7ff4)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_pton.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_pton.html)
- [inet_pton()](../api_file_reference/P161_zephyr__posix__arpa__inet.h_文件参考.md#aabfaede889b4bc47241ab0c49a7a3cab)
- [https://pubs.opengroup.org/onlinepubs/9699919799/functions/ioctl.html](https://pubs.opengroup.org/onlinepubs/9699919799/functions/ioctl.html)
- [请求值（Request Value）：`ZFD_IOCTL_FIONBIO`。](../api_file_media_sensor_reference/P003_zephyr__sys__fdtable.h_文件参考.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530)
- [请求值（Request Value）：`ZFD_IOCTL_FIONREAD`。](../api_file_media_sensor_reference/P003_zephyr__sys__fdtable.h_文件参考.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683)
- [ZFD_IOCTL_FIONWRITE](../api_file_media_sensor_reference/P003_zephyr__sys__fdtable.h_文件参考.md#aac8cb8bde69d227a7a8e9edf2980bd20a1e88b6e9ca6cf0db43029f485af43ccb)
- [ioctl()](../api_file_runtime_reference/P026_zephyr__posix__sys__ioctl.h_文件参考.md#a1487536105f7a596481bf6bfa8de99f6)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/listen.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/listen.html)
- [listen()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a7005ffbeeff92be5394ff3244da79028)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/poll.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/poll.html)
- [poll()](../api_file_reference/P306_zephyr__posix__poll.h_文件参考.md#afa7e83ddea0ab5b08fcf614b89ac48ba)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/recv.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recv.html)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvfrom.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvfrom.html)
- [recvfrom()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a1c41b0d557d19b5031e668b1997dc73a)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvmsg.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvmsg.html)
- [recvmsg()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#ae074d22829eb79c596fd60d0f9f9611f)
- [select()](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/send.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/send.html)
- [send()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendto.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendto.html)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendmsg.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendmsg.html)
- [sendmsg()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a8a2ad4261d3978ba299926f45d56ed74)
- [sendto()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#ac223969ed767c313123d06547db45ff8)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/setsockopt.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/setsockopt.html)
- [setsockopt()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a71c8788caef89a362e35ce5855e77077)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/shutdown.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/shutdown.html)
- [shutdown()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a8dadddc96fee56a9f8b0904aca02eab2)
- [http://pubs.opengroup.org/onlinepubs/9699919799/functions/socket.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/socket.html)
- [socket()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a4dcc080bfb18d95d173bc205084f8b0a)
- [https://pubs.opengroup.org/onlinepubs/009695399/functions/socketpair.html](https://pubs.opengroup.org/onlinepubs/009695399/functions/socketpair.html)
- [socketpair()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a56dcc24333a632cc8cdb8265151c0e7f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__ip__4__6_html_gad072b3bf7bc05927fe27f5503a31f25c"></a>
<a id="agroup__ip__4__6_html_ga9af9b1750c2db50a170e1b694df24227"></a>
<a id="agroup__ip__4__6_html_gaf91b9c08e327589eb0fd33d5754743cf"></a>
<a id="agroup__ip__4__6_html_gae1660acfdbf897afbc6119ae608e476f"></a>
<a id="agroup__ip__4__6_html_ga43b6e313f5a938d688d3bc734a299408"></a>
<a id="agroup__ip__4__6_html_ga9e7bf1c3503039c78f99f3deab277d4f"></a>
<a id="agroup__ip__4__6_html_ga9084b403ca6a591d24f975e669560b6c"></a>
<a id="agroup__ip__4__6_html_ga418a57b9f12205de21cbe83951e960bb"></a>
<a id="agroup__ip__4__6_html_gaec37f4f9d223e5be3c141ec1ae4ef288"></a>
<a id="agroup__ip__4__6_html_ga6704d86fb9962bdb6d27a41d4053bfc7"></a>
<a id="agroup__ip__4__6_html_gaf41e178ed45d6a483e240f939cd2f41d"></a>
<a id="agroup__ip__4__6_html_ga2716cdb6f85693d7c5a96446a7a41e03"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）.md)
