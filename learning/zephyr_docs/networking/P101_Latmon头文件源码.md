---
id: learning.zephyr-docs.networking.api-101
title: Latmon头文件源码
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/latmon_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_Latmon头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/latmon_8h_source.html)。读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 101.1\_阅读说明与来源

译注：先读[Latmon网络服务](P094_Latmon网络延迟监测服务.md)与[客户端示例](P095_Latmon客户端示例.md)，再查本组接口。

本组：[完整API参考](P099_Latmon完整API参考.md) · [头文件参考](P100_Latmon头文件参考.md) · [头文件源码](P101_Latmon头文件源码.md)。

下方保留官方Doxygen源码浏览页展示的全部代码、标识符及版权／许可注释。仅移除网页行号，将展示用不换行空格还原为普通空格，并清除行尾空白。原页面省略了部分生成API文档的注释，原行号因此存在跳跃；此展示不能替代完整原始头文件。接口注释译文见本组API页。

## 101.2\_原始源码展示

<a id="l00001"></a>
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
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="agroup__latmon_html_ga16b7b3ed71c2726564875e183a800de7"></a>
<a id="agroup__latmon_html_ga36586599ee161959414097dbbd54a2d3"></a>
<a id="agroup__latmon_html_ga48e9ce13fd948701739fcc2cd9e1a6b0"></a>
<a id="agroup__latmon_html_ga6c8ad5a0a35ea7ef098c024ec142edc7"></a>
<a id="agroup__latmon_html_ga968ebd93287d3968695c0dfebc7493d1"></a>
<a id="akernel_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html_a4dcc080bfb18d95d173bc205084f8b0a"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructnet__in__addr_html"></a>
<a id="astructnet__sockaddr_html"></a>

```c


/*
 * Copyright (c) 2025 Jorge A. Ramirez Ortiz <jorge.ramirez@oss.qualcomm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_LATMON_H_
#define ZEPHYR_INCLUDE_NET_LATMON_H_

#include <zephyr/kernel.h>
#include <zephyr/net/net_ip.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef int (*net_latmon_measure_t)(uint32_t *delta);

void net_latmon_start(int latmus, net_latmon_measure_t measure_func);

int net_latmon_connect(int socket, struct net_in_addr *ip);

int net_latmon_get_socket(struct net_sockaddr *bind_addr);

bool net_latmon_running(void);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_LATMON_H_ */
```

## 101.3\_源码注释译文

版权：2025年Jorge A. Ramirez Ortiz，原作者邮箱与署名在代码中保留；许可标识为`Apache-2.0`。末尾`#endif`注释标明结束头文件包含保护（Header Include Guard）`ZEPHYR_INCLUDE_NET_LATMON_H_`。

[上一章](P100_Latmon头文件参考.md) · [返回大纲](大纲.md) · [下一章](P102_zperf完整API参考.md)
