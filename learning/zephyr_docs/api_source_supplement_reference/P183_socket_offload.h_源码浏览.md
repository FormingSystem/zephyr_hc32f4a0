---
id: learning.zephyr-docs.api-source-supplement-reference.page-183
title: socket_offload.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第183章\_socket\_offload.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h.html)。

## 183.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="anet_2socket_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="asocket__offload_8h_html_a0d0123d234cd292282a272cb2e2eeb3c"></a>
<a id="asocket__offload_8h_html_a1b56446dd816af7101088bb0a474d0f4"></a>
<a id="asocket__offload_8h_html_a87f67b6c07b7271778e919ccc88b6d7b"></a>
<a id="asocket__offload_8h_html_af341a4e569196545165962e17544d2c9"></a>
<a id="astructsocket__dns__offload_html"></a>
<a id="astructsocket__dns__offload_html_a5241208180bcc8f553d0db6e74e5c115"></a>
<a id="astructsocket__dns__offload_html_a73640bb24b4838c337ef1a61ffd4949f"></a>
<a id="astructzsock__addrinfo_html"></a>

```c
/*
 * Copyright (c) 2018 Linaro Limited.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_SOCKET_OFFLOAD_H_
#define ZEPHYR_INCLUDE_NET_SOCKET_OFFLOAD_H_

#include <zephyr/net/net_ip.h>
#include <zephyr/net/socket.h>

#ifdef __cplusplus
extern "C" {
#endif

struct socket_dns_offload {
        int (*getaddrinfo)(const char *node, const char *service,
                           const struct zsock_addrinfo *hints,
                           struct zsock_addrinfo **res);
        void (*freeaddrinfo)(struct zsock_addrinfo *res);
};

void socket_offload_dns_register(const struct socket_dns_offload *ops);

int socket_offload_dns_deregister(const struct socket_dns_offload *ops);

void socket_offload_dns_enable(bool enable);

#if defined(CONFIG_NET_SOCKETS_OFFLOAD)
bool socket_offload_dns_is_enabled(void);
#else
#define socket_offload_dns_is_enabled() false
#endif /* defined(CONFIG_NET_SOCKETS_OFFLOAD) */



int socket_offload_getaddrinfo(const char *node, const char *service,
                               const struct zsock_addrinfo *hints,
                               struct zsock_addrinfo **res);

void socket_offload_freeaddrinfo(struct zsock_addrinfo *res);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_SOCKET_OFFLOAD_H_ */
```

## 183.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Linaro Limited.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

条件编译表达式：`defined(CONFIG_NET_SOCKETS_OFFLOAD)`。

### 注释 3：原第 88 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SOCKET_OFFLOAD_H_`。

## 183.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [socket_dns_offload](../network_service_model_reference/P055_socket_dns_offload_结构体.md)
- [getaddrinfo](../network_service_model_reference/P055_socket_dns_offload_结构体.md#a5241208180bcc8f553d0db6e74e5c115)
- [zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)
- [freeaddrinfo](../network_service_model_reference/P055_socket_dns_offload_结构体.md#a73640bb24b4838c337ef1a61ffd4949f)
- [socket_offload_dns_register](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h.html#a1b56446dd816af7101088bb0a474d0f4)
- [socket_offload_dns_deregister](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h.html#a87f67b6c07b7271778e919ccc88b6d7b)
- [socket_offload_dns_enable](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h.html#a0d0123d234cd292282a272cb2e2eeb3c)
- [socket_offload_dns_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h.html#af341a4e569196545165962e17544d2c9)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [socket_dns_offload::getaddrinfo](../network_service_model_reference/P055_socket_dns_offload_结构体.md#a5241208180bcc8f553d0db6e74e5c115)
- [socket_dns_offload::freeaddrinfo](../network_service_model_reference/P055_socket_dns_offload_结构体.md#a73640bb24b4838c337ef1a61ffd4949f)

---

[上一章](P182_six301-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P184_socket_poll.h_源码浏览.md)
