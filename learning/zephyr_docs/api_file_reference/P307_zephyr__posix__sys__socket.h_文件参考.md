---
id: learning.zephyr-docs.api-file-reference.page-307
title: zephyr__posix__sys__socket.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第307章\_zephyr\_\_posix\_\_sys\_\_socket.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <sys/types.h>
#include <zephyr/net/socket.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 307.1\_数据结构（Data Structures）

<a id="r_linger"></a>

```c
struct linger
```

相关声明：[linger](../posix_system_model_reference/P006_linger_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 307.2\_宏定义（Macros）

<a id="r_ac6e72c7e05dd849f9ec7debf3ee8597c"></a>

```c
#define ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS
```

相关声明：[ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS](#ac6e72c7e05dd849f9ec7debf3ee8597c)。

<a id="r_a60c35b1016d0d87fe1066ea817acad98"></a>

```c
#define MSG_PEEK ZSOCK_MSG_PEEK
```

相关声明：[MSG_PEEK](#a60c35b1016d0d87fe1066ea817acad98)、[ZSOCK_MSG_PEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae7da123a40584192b65af77e918080b9)。

<a id="r_a6a90f17f258e36353f09375263324f41"></a>

```c
#define MSG_TRUNC ZSOCK_MSG_TRUNC
```

相关声明：[MSG_TRUNC](#a6a90f17f258e36353f09375263324f41)、[ZSOCK_MSG_TRUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae594c5e74cd473df8e3328a4cd935ce1)。

<a id="r_ab18d3d439e4a9c8d0f73e7166e8eb376"></a>

```c
#define MSG_DONTWAIT ZSOCK_MSG_DONTWAIT
```

相关声明：[MSG_DONTWAIT](#ab18d3d439e4a9c8d0f73e7166e8eb376)、[ZSOCK_MSG_DONTWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga92cf4460e23f376bf130d885ea64ed6b)。

<a id="r_a0c0fac4635e91ca9d839e20a09d3989e"></a>

```c
#define MSG_WAITALL ZSOCK_MSG_WAITALL
```

相关声明：[MSG_WAITALL](#a0c0fac4635e91ca9d839e20a09d3989e)、[ZSOCK_MSG_WAITALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga00b950f50302d97c27111da49f5289fb)。

<a id="r_af1c8cf84ac37451afaef3bde9976b6e1"></a>

```c
#define SHUT_RD ZSOCK_SHUT_RD
```

相关声明：[SHUT_RD](#af1c8cf84ac37451afaef3bde9976b6e1)、[ZSOCK_SHUT_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2a58cbc62db1e559898ea979454d74d4)。

<a id="r_addb0a758e6fafdd89f5b7120f84738eb"></a>

```c
#define SHUT_WR ZSOCK_SHUT_WR
```

相关声明：[SHUT_WR](#addb0a758e6fafdd89f5b7120f84738eb)、[ZSOCK_SHUT_WR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga87630f1abe81c4e33a24cb1f1ebb3571)。

<a id="r_a80c54d1399557c97a0c81a319d08e9db"></a>

```c
#define SHUT_RDWR ZSOCK_SHUT_RDWR
```

相关声明：[SHUT_RDWR](#a80c54d1399557c97a0c81a319d08e9db)、[ZSOCK_SHUT_RDWR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga788dcff81663a9fb01e32b53bca13e2d)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 307.3\_类型定义（Typedefs）

<a id="r_a3f5f480bed01f54df564b99350f1d1bb"></a>

```c
typedef uint32_t socklen_t
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 307.4\_函数（Functions）

<a id="r_a66e3de379c18201b21c889035ec54864"></a>

```c
int accept (int sock, struct sockaddr *addr, socklen_t *addrlen)
```

相关声明：[accept](#a66e3de379c18201b21c889035ec54864)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="r_a05b4e957a092db3e68281988ceb32df8"></a>

```c
int bind (int sock, const struct sockaddr *addr, socklen_t addrlen)
```

相关声明：[bind](#a05b4e957a092db3e68281988ceb32df8)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="r_a90f0aa598d0f4ab4ea99ecf289a6a7fb"></a>

```c
int connect (int sock, const struct sockaddr *addr, socklen_t addrlen)
```

相关声明：[connect](#a90f0aa598d0f4ab4ea99ecf289a6a7fb)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="r_a5580f3aa0827aae89459c24b91f80cae"></a>

```c
int getpeername (int sock, struct sockaddr *addr, socklen_t *addrlen)
```

相关声明：[getpeername](#a5580f3aa0827aae89459c24b91f80cae)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="r_abef44fb98f476ef2adba92bbdb362a1b"></a>

```c
int getsockname (int sock, struct sockaddr *addr, socklen_t *addrlen)
```

相关声明：[getsockname](#abef44fb98f476ef2adba92bbdb362a1b)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="r_a2d33f1c2b99a5d0df682f54c3ccb2ffa"></a>

```c
int getsockopt (int sock, int level, int optname, void *optval, socklen_t *optlen)
```

相关声明：[getsockopt](#a2d33f1c2b99a5d0df682f54c3ccb2ffa)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="r_a7005ffbeeff92be5394ff3244da79028"></a>

```c
int listen (int sock, int backlog)
```

相关声明：[listen](#a7005ffbeeff92be5394ff3244da79028)。

<a id="r_adee01662b0cf762a014efd87ab811276"></a>

```c
ssize_t recv (int sock, void *buf, size_t max_len, int flags)
```

相关声明：[ssize_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[recv](#adee01662b0cf762a014efd87ab811276)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_a1c41b0d557d19b5031e668b1997dc73a"></a>

```c
ssize_t recvfrom (int sock, void *buf, size_t max_len, int flags, struct sockaddr *src_addr, socklen_t *addrlen)
```

相关声明：[ssize_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[recvfrom](#a1c41b0d557d19b5031e668b1997dc73a)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="r_ae074d22829eb79c596fd60d0f9f9611f"></a>

```c
ssize_t recvmsg (int sock, struct msghdr *msg, int flags)
```

相关声明：[ssize_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[recvmsg](#ae074d22829eb79c596fd60d0f9f9611f)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_a16485de18b1ec93572e5d74b4a04e42f"></a>

```c
ssize_t send (int sock, const void *buf, size_t len, int flags)
```

相关声明：[ssize_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[send](#a16485de18b1ec93572e5d74b4a04e42f)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_a8a2ad4261d3978ba299926f45d56ed74"></a>

```c
ssize_t sendmsg (int sock, const struct msghdr *message, int flags)
```

相关声明：[ssize_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[sendmsg](#a8a2ad4261d3978ba299926f45d56ed74)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_ac223969ed767c313123d06547db45ff8"></a>

```c
ssize_t sendto (int sock, const void *buf, size_t len, int flags, const struct sockaddr *dest_addr, socklen_t addrlen)
```

相关声明：[ssize_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[sendto](#ac223969ed767c313123d06547db45ff8)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="r_a71c8788caef89a362e35ce5855e77077"></a>

```c
int setsockopt (int sock, int level, int optname, const void *optval, socklen_t optlen)
```

相关声明：[setsockopt](#a71c8788caef89a362e35ce5855e77077)、[socklen_t](#a3f5f480bed01f54df564b99350f1d1bb)。

<a id="r_a8dadddc96fee56a9f8b0904aca02eab2"></a>

```c
int shutdown (int sock, int how)
```

相关声明：[shutdown](#a8dadddc96fee56a9f8b0904aca02eab2)。

<a id="r_afcde75d283454d9d266b2ac6ebd867fe"></a>

```c
int sockatmark (int s)
```

相关声明：[sockatmark](#afcde75d283454d9d266b2ac6ebd867fe)。

<a id="r_a4dcc080bfb18d95d173bc205084f8b0a"></a>

```c
int socket (int family, int type, int proto)
```

相关声明：[socket](#a4dcc080bfb18d95d173bc205084f8b0a)。

<a id="r_a56dcc24333a632cc8cdb8265151c0e7f"></a>

```c
int socketpair (int family, int type, int proto, int sv[2])
```

相关声明：[socketpair](#a56dcc24333a632cc8cdb8265151c0e7f)。

## 307.5\_详细说明（Detailed Documentation）

<a id="ab18d3d439e4a9c8d0f73e7166e8eb376"></a>

### `MSG_DONTWAIT`

```c
#define MSG_DONTWAIT ZSOCK_MSG_DONTWAIT
```

<a id="a60c35b1016d0d87fe1066ea817acad98"></a>

### `MSG_PEEK`

```c
#define MSG_PEEK ZSOCK_MSG_PEEK
```

<a id="a6a90f17f258e36353f09375263324f41"></a>

### `MSG_TRUNC`

```c
#define MSG_TRUNC ZSOCK_MSG_TRUNC
```

<a id="a0c0fac4635e91ca9d839e20a09d3989e"></a>

### `MSG_WAITALL`

```c
#define MSG_WAITALL ZSOCK_MSG_WAITALL
```

<a id="af1c8cf84ac37451afaef3bde9976b6e1"></a>

### `SHUT_RD`

```c
#define SHUT_RD ZSOCK_SHUT_RD
```

<a id="a80c54d1399557c97a0c81a319d08e9db"></a>

### `SHUT_RDWR`

```c
#define SHUT_RDWR ZSOCK_SHUT_RDWR
```

<a id="addb0a758e6fafdd89f5b7120f84738eb"></a>

### `SHUT_WR`

```c
#define SHUT_WR ZSOCK_SHUT_WR
```

<a id="ac6e72c7e05dd849f9ec7debf3ee8597c"></a>

### `ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS`

```c
#define ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS
```

<a id="a3f5f480bed01f54df564b99350f1d1bb"></a>

### `socklen_t`

```c
typedef uint32_t socklen_t
```

<a id="a66e3de379c18201b21c889035ec54864"></a>

### `accept()`

```c
int accept ( int sock, struct sockaddr * addr, socklen_t * addrlen )
```

<a id="a05b4e957a092db3e68281988ceb32df8"></a>

### `bind()`

```c
int bind ( int sock, const struct sockaddr * addr, socklen_t addrlen )
```

<a id="a90f0aa598d0f4ab4ea99ecf289a6a7fb"></a>

### `connect()`

```c
int connect ( int sock, const struct sockaddr * addr, socklen_t addrlen )
```

<a id="a5580f3aa0827aae89459c24b91f80cae"></a>

### `getpeername()`

```c
int getpeername ( int sock, struct sockaddr * addr, socklen_t * addrlen )
```

<a id="abef44fb98f476ef2adba92bbdb362a1b"></a>

### `getsockname()`

```c
int getsockname ( int sock, struct sockaddr * addr, socklen_t * addrlen )
```

<a id="a2d33f1c2b99a5d0df682f54c3ccb2ffa"></a>

### `getsockopt()`

```c
int getsockopt ( int sock, int level, int optname, void * optval, socklen_t * optlen )
```

<a id="a7005ffbeeff92be5394ff3244da79028"></a>

### `listen()`

```c
int listen ( int sock, int backlog )
```

<a id="adee01662b0cf762a014efd87ab811276"></a>

### `recv()`

```c
ssize_t recv ( int sock, void * buf, size_t max_len, int flags )
```

<a id="a1c41b0d557d19b5031e668b1997dc73a"></a>

### `recvfrom()`

```c
ssize_t recvfrom ( int sock, void * buf, size_t max_len, int flags, struct sockaddr * src_addr, socklen_t * addrlen )
```

<a id="ae074d22829eb79c596fd60d0f9f9611f"></a>

### `recvmsg()`

```c
ssize_t recvmsg ( int sock, struct msghdr * msg, int flags )
```

<a id="a16485de18b1ec93572e5d74b4a04e42f"></a>

### `send()`

```c
ssize_t send ( int sock, const void * buf, size_t len, int flags )
```

<a id="a8a2ad4261d3978ba299926f45d56ed74"></a>

### `sendmsg()`

```c
ssize_t sendmsg ( int sock, const struct msghdr * message, int flags )
```

<a id="ac223969ed767c313123d06547db45ff8"></a>

### `sendto()`

```c
ssize_t sendto ( int sock, const void * buf, size_t len, int flags, const struct sockaddr * dest_addr, socklen_t addrlen )
```

<a id="a71c8788caef89a362e35ce5855e77077"></a>

### `setsockopt()`

```c
int setsockopt ( int sock, int level, int optname, const void * optval, socklen_t optlen )
```

<a id="a8dadddc96fee56a9f8b0904aca02eab2"></a>

### `shutdown()`

```c
int shutdown ( int sock, int how )
```

<a id="afcde75d283454d9d266b2ac6ebd867fe"></a>

### `sockatmark()`

```c
int sockatmark ( int s)
```

<a id="a4dcc080bfb18d95d173bc205084f8b0a"></a>

### `socket()`

```c
int socket ( int family, int type, int proto )
```

<a id="a56dcc24333a632cc8cdb8265151c0e7f"></a>

### `socketpair()`

```c
int socketpair ( int family, int type, int proto, int sv[2] )
```


## 307.6\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P667_socket.h_源码浏览.md)
- [linger](../posix_system_model_reference/P006_linger_结构体.md)
- [ZSOCK_MSG_PEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae7da123a40584192b65af77e918080b9)
- [ZSOCK_MSG_TRUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae594c5e74cd473df8e3328a4cd935ce1)
- [ZSOCK_MSG_DONTWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga92cf4460e23f376bf130d885ea64ed6b)
- [ZSOCK_MSG_WAITALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga00b950f50302d97c27111da49f5289fb)
- [ZSOCK_SHUT_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga2a58cbc62db1e559898ea979454d74d4)
- [ZSOCK_SHUT_WR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga87630f1abe81c4e33a24cb1f1ebb3571)
- [ZSOCK_SHUT_RDWR](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga788dcff81663a9fb01e32b53bca13e2d)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ssize_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P306_zephyr__posix__poll.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P308_zephyr__drivers__console__posix_arch_console.h_文件参考.md)
