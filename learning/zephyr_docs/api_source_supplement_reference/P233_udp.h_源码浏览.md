---
id: learning.zephyr-docs.api-source-supplement-reference.page-233
title: udp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/udp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第233章\_udp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/udp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/udp_8h.html)。

## 233.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00035"></a>
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
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="anet__core_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="astructnet__pkt_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_UDP_H_
#define ZEPHYR_INCLUDE_NET_UDP_H_

#include <zephyr/types.h>

#include <zephyr/net/net_core.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_pkt.h>

#ifdef __cplusplus
extern "C" {
#endif

/* These APIs are mostly meant for Zephyr internal use so do not generate
 * documentation for them.
 */


#if defined(CONFIG_NET_UDP)
struct net_udp_hdr *net_udp_get_hdr(struct net_pkt *pkt,
                                    struct net_udp_hdr *hdr);
#else
static inline struct net_udp_hdr *net_udp_get_hdr(struct net_pkt *pkt,
                                                  struct net_udp_hdr *hdr)
{
        return NULL;
}
#endif /* CONFIG_NET_UDP */

#if defined(CONFIG_NET_UDP)
struct net_udp_hdr *net_udp_set_hdr(struct net_pkt *pkt,
                                    struct net_udp_hdr *hdr);
#else
static inline struct net_udp_hdr *net_udp_set_hdr(struct net_pkt *pkt,
                                                  struct net_udp_hdr *hdr)
{
        return NULL;
}
#endif /* CONFIG_NET_UDP */



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_UDP_H_ */
```

## 233.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 24 行

这些 API 主要供 Zephyr 内部使用，因此不为它们生成文档。

### 注释 3：原第 62 行

条件编译配置（Configuration）标记：`CONFIG_NET_UDP`。

### 注释 4：原第 88 行

条件编译配置（Configuration）标记：`CONFIG_NET_UDP`。

### 注释 5：原第 100 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_UDP_H_`。

## 233.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/udp_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/net/net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)

---

[上一章](P232_uart_mcumgr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P234_usb_audio.h_源码浏览.md)
