---
id: learning.zephyr-docs.api-source-reference.page-800
title: sntp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sntp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第800章\_sntp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sntp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sntp_8h.html)。

## 800.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00022"></a>
<a id="l00031"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__sntp_html_ga0cff25edb11ae944dd24a234450a2f3d"></a>
<a id="agroup__sntp_html_ga25c894db6d24a5e729b4edcb8917ce9c"></a>
<a id="agroup__sntp_html_ga25ef46cc74be71bbe2f76de7c30cbe45"></a>
<a id="agroup__sntp_html_ga8771cdc6e64ab1489b333cc0c1731e9f"></a>
<a id="agroup__sntp_html_gab3395460258400a9b36d97418c706988"></a>
<a id="agroup__sntp_html_gab6adcd7259bdfa841b57e535c380508d"></a>
<a id="agroup__sntp_html_gac73db957041a6814abb286fd9143ddb5"></a>
<a id="agroup__sntp_html_gacd621da6168cf064d0bf6c370f6ca597"></a>
<a id="agroup__sntp_html_gadb5603eeaea68e0823f8a3f6a1b8a6c1"></a>
<a id="agroup__sntp_html_gaeb595e89c56fbb619010e3c8d7b2b5b1"></a>
<a id="anet_2socket_8h_html"></a>
<a id="asocket__service_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructnet__socket__service__desc_html"></a>
<a id="astructnet__socket__service__event_html"></a>
<a id="astructsntp__ctx_html"></a>
<a id="astructsntp__ctx_html_a58bd69ad86d00183e32ed07a9fbebfdc"></a>
<a id="astructsntp__time_html"></a>
<a id="astructsntp__time_html_a59a1abe8f7129bad82e33e5709cf46af"></a>
<a id="astructsntp__time_html_a7dc90613b6ac0265ff49b931a786354f"></a>
<a id="astructsntp__time_html_ad33fb2e743756bde8538ac6d2ff3eae8"></a>
<a id="astructzsock__pollfd_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2017 Linaro Limited
 * SPDX-FileCopyrightText: Copyright (c) 2019 Intel Corporation
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_SNTP_H_
#define ZEPHYR_INCLUDE_NET_SNTP_H_

#include <zephyr/net/socket.h>
#include <zephyr/net/socket_service.h>

#ifdef __cplusplus
extern "C" {
#endif


struct sntp_time {
        uint64_t seconds;
        uint32_t fraction;
        uint32_t rsp_delay_us;
#if defined(CONFIG_SNTP_UNCERTAINTY)
        uint64_t uptime_us;
        uint32_t uncertainty_us;
#endif
};

struct sntp_ctx {

        struct {
                struct zsock_pollfd fds[1];
                int nfds;
                int fd;
        } sock;

        struct sntp_time expected_orig_ts;
};

int sntp_init(struct sntp_ctx *ctx, const struct net_sockaddr *addr,
              net_socklen_t addr_len);

int sntp_query(struct sntp_ctx *ctx, uint32_t timeout, struct sntp_time *ts);

int sntp_recv_response(struct sntp_ctx *ctx, uint32_t timeout, struct sntp_time *ts);

void sntp_close(struct sntp_ctx *ctx);

int sntp_init_async(struct sntp_ctx *ctx, const struct net_sockaddr *addr, net_socklen_t addr_len,
                    const struct net_socket_service_desc *service);

int sntp_send_async(struct sntp_ctx *ctx);

int sntp_read_async(struct net_socket_service_event *event, struct sntp_time *ts);

void sntp_close_async(const struct net_socket_service_desc *service);

int sntp_simple(const char *server, uint32_t timeout,
                struct sntp_time *ts);

int sntp_simple_addr(struct net_sockaddr *addr, net_socklen_t addr_len, uint32_t timeout,
                     struct sntp_time *ts);

#ifdef __cplusplus
}
#endif


#endif
```

## 800.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2017 Linaro Limited。

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2019 Intel Corporation。

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 800.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sntp_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/net/socket_service.h](https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h.html)
- [sntp_time](../network_application_model_reference/P088_sntp_time_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [seconds](../network_application_model_reference/P088_sntp_time_结构体.md#a7dc90613b6ac0265ff49b931a786354f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [fraction](../network_application_model_reference/P088_sntp_time_结构体.md#ad33fb2e743756bde8538ac6d2ff3eae8)
- [rsp_delay_us](../network_application_model_reference/P088_sntp_time_结构体.md#a59a1abe8f7129bad82e33e5709cf46af)
- [sntp_ctx](../network_application_model_reference/P087_sntp_ctx_结构体.md)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [expected_orig_ts](../network_application_model_reference/P087_sntp_ctx_结构体.md#a58bd69ad86d00183e32ed07a9fbebfdc)
- [sntp_init](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gab3395460258400a9b36d97418c706988)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [sntp_query](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga25ef46cc74be71bbe2f76de7c30cbe45)
- [sntp_recv_response](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga8771cdc6e64ab1489b333cc0c1731e9f)
- [sntp_close](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga0cff25edb11ae944dd24a234450a2f3d)
- [sntp_init_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gacd621da6168cf064d0bf6c370f6ca597)
- [net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)
- [sntp_send_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gab6adcd7259bdfa841b57e535c380508d)
- [sntp_read_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gac73db957041a6814abb286fd9143ddb5)
- [net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)
- [sntp_close_async](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gaeb595e89c56fbb619010e3c8d7b2b5b1)
- [sntp_simple](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#ga25c894db6d24a5e729b4edcb8917ce9c)
- [sntp_simple_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gadb5603eeaea68e0823f8a3f6a1b8a6c1)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [socket_service.h](https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h.html)
- [sntp_ctx::expected_orig_ts](../network_application_model_reference/P087_sntp_ctx_结构体.md#a58bd69ad86d00183e32ed07a9fbebfdc)
- [sntp_time::rsp_delay_us](../network_application_model_reference/P088_sntp_time_结构体.md#a59a1abe8f7129bad82e33e5709cf46af)
- [sntp_time::seconds](../network_application_model_reference/P088_sntp_time_结构体.md#a7dc90613b6ac0265ff49b931a786354f)
- [sntp_time::fraction](../network_application_model_reference/P088_sntp_time_结构体.md#ad33fb2e743756bde8538ac6d2ff3eae8)

---

[上一章](P799_snps-designware-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P801_sntp_server.h_源码浏览.md)
