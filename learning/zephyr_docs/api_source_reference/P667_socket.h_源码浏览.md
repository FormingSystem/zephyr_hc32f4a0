---
id: learning.zephyr-docs.api-source-reference.page-667
title: socket.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第667章\_socket.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html)。

## 667.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="foldopen00020"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="anet_2socket_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aposix_2sys_2socket_8h_html_a05b4e957a092db3e68281988ceb32df8"></a>
<a id="aposix_2sys_2socket_8h_html_a16485de18b1ec93572e5d74b4a04e42f"></a>
<a id="aposix_2sys_2socket_8h_html_a1c41b0d557d19b5031e668b1997dc73a"></a>
<a id="aposix_2sys_2socket_8h_html_a2d33f1c2b99a5d0df682f54c3ccb2ffa"></a>
<a id="aposix_2sys_2socket_8h_html_a3f5f480bed01f54df564b99350f1d1bb"></a>
<a id="aposix_2sys_2socket_8h_html_a4dcc080bfb18d95d173bc205084f8b0a"></a>
<a id="aposix_2sys_2socket_8h_html_a5580f3aa0827aae89459c24b91f80cae"></a>
<a id="aposix_2sys_2socket_8h_html_a56dcc24333a632cc8cdb8265151c0e7f"></a>
<a id="aposix_2sys_2socket_8h_html_a66e3de379c18201b21c889035ec54864"></a>
<a id="aposix_2sys_2socket_8h_html_a7005ffbeeff92be5394ff3244da79028"></a>
<a id="aposix_2sys_2socket_8h_html_a71c8788caef89a362e35ce5855e77077"></a>
<a id="aposix_2sys_2socket_8h_html_a8a2ad4261d3978ba299926f45d56ed74"></a>
<a id="aposix_2sys_2socket_8h_html_a8dadddc96fee56a9f8b0904aca02eab2"></a>
<a id="aposix_2sys_2socket_8h_html_a90f0aa598d0f4ab4ea99ecf289a6a7fb"></a>
<a id="aposix_2sys_2socket_8h_html_abef44fb98f476ef2adba92bbdb362a1b"></a>
<a id="aposix_2sys_2socket_8h_html_ac223969ed767c313123d06547db45ff8"></a>
<a id="aposix_2sys_2socket_8h_html_adee01662b0cf762a014efd87ab811276"></a>
<a id="aposix_2sys_2socket_8h_html_ae074d22829eb79c596fd60d0f9f9611f"></a>
<a id="aposix_2sys_2socket_8h_html_afcde75d283454d9d266b2ac6ebd867fe"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructlinger_html"></a>
<a id="astructlinger_html_a2b7d01c9a43f95d2ba6f6cf0ec68b412"></a>
<a id="astructlinger_html_aa917aeadf061af6ed64aad87df3255fc"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_SYS_SOCKET_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_SOCKET_H_

#include <sys/types.h>

#undef ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS
#define ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS
#include <zephyr/net/socket.h>
#undef ZEPHYR_INCLUDE_NET_COMPAT_MODE_SYMBOLS

#ifdef __cplusplus
extern "C" {
#endif

struct linger {
        int  l_onoff;
        int  l_linger;
};

#if !defined(CONFIG_NET_NAMESPACE_COMPAT_MODE)
typedef uint32_t socklen_t;
struct msghdr;
struct sockaddr;

#define MSG_PEEK     ZSOCK_MSG_PEEK
#define MSG_TRUNC    ZSOCK_MSG_TRUNC
#define MSG_DONTWAIT ZSOCK_MSG_DONTWAIT
#define MSG_WAITALL  ZSOCK_MSG_WAITALL

#define SHUT_RD   ZSOCK_SHUT_RD
#define SHUT_WR   ZSOCK_SHUT_WR
#define SHUT_RDWR ZSOCK_SHUT_RDWR
#endif

int accept(int sock, struct sockaddr *addr, socklen_t *addrlen);
int bind(int sock, const struct sockaddr *addr, socklen_t addrlen);
int connect(int sock, const struct sockaddr *addr, socklen_t addrlen);
int getpeername(int sock, struct sockaddr *addr, socklen_t *addrlen);
int getsockname(int sock, struct sockaddr *addr, socklen_t *addrlen);
int getsockopt(int sock, int level, int optname, void *optval, socklen_t *optlen);
int listen(int sock, int backlog);
ssize_t recv(int sock, void *buf, size_t max_len, int flags);
ssize_t recvfrom(int sock, void *buf, size_t max_len, int flags, struct sockaddr *src_addr,
                 socklen_t *addrlen);
ssize_t recvmsg(int sock, struct msghdr *msg, int flags);
ssize_t send(int sock, const void *buf, size_t len, int flags);
ssize_t sendmsg(int sock, const struct msghdr *message, int flags);
ssize_t sendto(int sock, const void *buf, size_t len, int flags, const struct sockaddr *dest_addr,
               socklen_t addrlen);
int setsockopt(int sock, int level, int optname, const void *optval, socklen_t optlen);
int shutdown(int sock, int how);
int sockatmark(int s);
int socket(int family, int type, int proto);
int socketpair(int family, int type, int proto, int sv[2]);

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_INCLUDE_POSIX_SYS_SOCKET_H_ */
```

## 667.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 65 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_SOCKET_H_`。

## 667.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [linger](../posix_system_model_reference/P006_linger_结构体.md)
- [l_onoff](../posix_system_model_reference/P006_linger_结构体.md#aa917aeadf061af6ed64aad87df3255fc)
- [l_linger](../posix_system_model_reference/P006_linger_结构体.md#a2b7d01c9a43f95d2ba6f6cf0ec68b412)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a3f5f480bed01f54df564b99350f1d1bb)
- [accept](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a66e3de379c18201b21c889035ec54864)
- [bind](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a05b4e957a092db3e68281988ceb32df8)
- [connect](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a90f0aa598d0f4ab4ea99ecf289a6a7fb)
- [getpeername](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a5580f3aa0827aae89459c24b91f80cae)
- [getsockname](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#abef44fb98f476ef2adba92bbdb362a1b)
- [getsockopt](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a2d33f1c2b99a5d0df682f54c3ccb2ffa)
- [listen](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a7005ffbeeff92be5394ff3244da79028)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [recv](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#adee01662b0cf762a014efd87ab811276)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [recvfrom](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a1c41b0d557d19b5031e668b1997dc73a)
- [recvmsg](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#ae074d22829eb79c596fd60d0f9f9611f)
- [send](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a16485de18b1ec93572e5d74b4a04e42f)
- [sendmsg](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a8a2ad4261d3978ba299926f45d56ed74)
- [sendto](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#ac223969ed767c313123d06547db45ff8)
- [setsockopt](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a71c8788caef89a362e35ce5855e77077)
- [shutdown](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a8dadddc96fee56a9f8b0904aca02eab2)
- [sockatmark](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#afcde75d283454d9d266b2ac6ebd867fe)
- [socket](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a4dcc080bfb18d95d173bc205084f8b0a)
- [socketpair](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a56dcc24333a632cc8cdb8265151c0e7f)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [linger::l_linger](../posix_system_model_reference/P006_linger_结构体.md#a2b7d01c9a43f95d2ba6f6cf0ec68b412)
- [linger::l_onoff](../posix_system_model_reference/P006_linger_结构体.md#aa917aeadf061af6ed64aad87df3255fc)

---

[上一章](P666_eventfd.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P668_posix_arch_console.h_源码浏览.md)
