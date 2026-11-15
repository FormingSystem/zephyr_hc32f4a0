---
id: learning.zephyr-docs.api-source-system-reference.page-23
title: net_core.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_net\_core.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)。

## 23.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00038"></a>
<a id="l00047"></a>
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
<a id="l00066"></a>
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
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00178"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="agroup__clock__apis_html_ga0bb4b83f0222193b21a8910311bab0ca"></a>
<a id="agroup__clock__apis_html_ga3d9541cfe2e8395af66d186efa77362f"></a>
<a id="agroup__isr__apis_html_ga8482b0dd2283d12677a9ebe321667d16"></a>
<a id="agroup__net__core_html_ga3421119d2b1797ee5d70f736a61f93b7"></a>
<a id="agroup__net__core_html_ga815b4cf2db95b80bfd9a576f12ebf6ff"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="agroup__net__core_html_gaade26b02f8fbac7989fe1b021269b08c"></a>
<a id="agroup__net__core_html_gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047"></a>
<a id="agroup__net__core_html_gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3"></a>
<a id="agroup__net__core_html_gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f"></a>
<a id="akernel_8h_html"></a>
<a id="anet__linkaddr_8h_html"></a>
<a id="anet__timeout_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__context_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>

```c


/*
 * Copyright (c) 2015 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_NET_CORE_H_
#define ZEPHYR_INCLUDE_NET_NET_CORE_H_

#include <stdbool.h>
#include <string.h>

#include <zephyr/sys/__assert.h>
#include <zephyr/kernel.h>

#include <zephyr/net/net_timeout.h>
#include <zephyr/net/net_linkaddr.h>

#ifdef __cplusplus
extern "C" {
#endif




#define NET_ASSERT(cond, ...) __ASSERT(cond, "" __VA_ARGS__)

/* This needs to be here in order to avoid circular include dependency between
 * net_pkt.h and net_if.h
 */
#if defined(CONFIG_NET_PKT_TXTIME_STATS_DETAIL) || \
        defined(CONFIG_NET_PKT_RXTIME_STATS_DETAIL)
#if !defined(NET_PKT_DETAIL_STATS_COUNT)
#if defined(CONFIG_NET_PKT_TXTIME_STATS_DETAIL)

#if defined(CONFIG_NET_PKT_RXTIME_STATS_DETAIL)
#define NET_PKT_DETAIL_STATS_COUNT 4
#else
#define NET_PKT_DETAIL_STATS_COUNT 3
#endif /* CONFIG_NET_PKT_RXTIME_STATS_DETAIL */

#else
#define NET_PKT_DETAIL_STATS_COUNT 4
#endif /* CONFIG_NET_PKT_TXTIME_STATS_DETAIL */

#endif /* !NET_PKT_DETAIL_STATS_COUNT */
#endif /* CONFIG_NET_PKT_TXTIME_STATS_DETAIL ||
          CONFIG_NET_PKT_RXTIME_STATS_DETAIL */


struct net_buf;
struct net_pkt;
struct net_context;
struct net_if;

enum net_verdict {
        NET_OK,
        NET_CONTINUE,
        NET_DROP,
};

int net_recv_data(struct net_if *iface, struct net_pkt *pkt);

int net_try_send_data(struct net_pkt *pkt, k_timeout_t timeout);

static inline int net_send_data(struct net_pkt *pkt)
{
        k_timeout_t timeout = k_is_in_isr() ? K_NO_WAIT : K_FOREVER;

        return net_try_send_data(pkt, timeout);
}


/* Some helper defines for traffic class support */
#if defined(CONFIG_NET_TC_TX_COUNT) && defined(CONFIG_NET_TC_RX_COUNT)
#define NET_TC_TX_COUNT CONFIG_NET_TC_TX_COUNT
#define NET_TC_RX_COUNT CONFIG_NET_TC_RX_COUNT

#if NET_TC_TX_COUNT > NET_TC_RX_COUNT
#define NET_TC_COUNT NET_TC_TX_COUNT
#else
#define NET_TC_COUNT NET_TC_RX_COUNT
#endif
#else /* CONFIG_NET_TC_TX_COUNT && CONFIG_NET_TC_RX_COUNT */
#define NET_TC_TX_COUNT 0
#define NET_TC_RX_COUNT 0
#define NET_TC_COUNT 0
#endif /* CONFIG_NET_TC_TX_COUNT && CONFIG_NET_TC_RX_COUNT */

#if CONFIG_NET_TC_TX_SKIP_FOR_HIGH_PRIO
#define NET_TC_TX_EFFECTIVE_COUNT (NET_TC_TX_COUNT + 1)
#else
#define NET_TC_TX_EFFECTIVE_COUNT NET_TC_TX_COUNT
#endif

#if CONFIG_NET_TC_RX_SKIP_FOR_HIGH_PRIO
#define NET_TC_RX_EFFECTIVE_COUNT (NET_TC_RX_COUNT + 1)
#else
#define NET_TC_RX_EFFECTIVE_COUNT NET_TC_RX_COUNT
#endif

struct net_l3_register {
        const char * const name;
        const struct net_l2 * const l2;
        enum net_verdict (*handler)(struct net_if *iface,
                                    uint16_t ptype,
                                    struct net_pkt *pkt);
        uint16_t ptype;
};

#define NET_L3_GET_NAME(l3_name, ptype) __net_l3_register_##l3_name##_##ptype

#define NET_L3_REGISTER(_l2_type, _name, _ptype, _handler)              \
        static const STRUCT_SECTION_ITERABLE(net_l3_register,           \
                                    NET_L3_GET_NAME(_name, _ptype)) = { \
                .ptype = _ptype,                                        \
                .handler = _handler,                                    \
                .name = STRINGIFY(_name),                               \
                .l2 = _l2_type,                                         \
        };

/* @endcond */


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_NET_CORE_H_ */
```

## 23.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2015 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

需要将其放在这里，以避免 `net_pkt.h` 与 `net_if.h` 之间形成循环包含依赖（Circular Include Dependency）。

### 注释 3：原第 64 行

条件编译配置（Configuration）标记：`CONFIG_NET_PKT_RXTIME_STATS_DETAIL`。

### 注释 4：原第 68 行

条件编译配置（Configuration）标记：`CONFIG_NET_PKT_TXTIME_STATS_DETAIL`。

### 注释 5：原第 70 行

条件编译（Conditional Compilation）：`!NET_PKT_DETAIL_STATS_COUNT`。

### 注释 6：原第 71 行

条件编译（Conditional Compilation）：`CONFIG_NET_PKT_TXTIME_STATS_DETAIL || CONFIG_NET_PKT_RXTIME_STATS_DETAIL`。

### 注释 7：原第 143 行

用于流量类别支持（Traffic Class Support）的若干辅助定义（Helper Defines）。

### 注释 8：原第 153 行

条件编译（Conditional Compilation）：`CONFIG_NET_TC_TX_COUNT && CONFIG_NET_TC_RX_COUNT`。

### 注释 9：原第 157 行

条件编译（Conditional Compilation）：`CONFIG_NET_TC_TX_COUNT && CONFIG_NET_TC_RX_COUNT`。

### 注释 10：原第 211 行

Doxygen 条件文档块结束标记：`@endcond`。

### 注释 11：原第 221 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_CORE_H_`。

## 23.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [string.h](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/net_timeout.h](../time_headers_reference/P009_网络超时头文件参考.md)
- [zephyr/net/net_linkaddr.h](https://docs.zephyrproject.org/latest/doxygen/html/net__linkaddr_8h.html)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_context](../network_core_model_reference/P055_net_context_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [NET_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)
- [NET_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)
- [NET_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)
- [net_recv_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga3421119d2b1797ee5d70f736a61f93b7)
- [net_try_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gaade26b02f8fbac7989fe1b021269b08c)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga815b4cf2db95b80bfd9a576f12ebf6ff)
- [k_is_in_isr](../fatal_irq_reference/P007_中断服务接口.md#ga8482b0dd2283d12677a9ebe321667d16)
- [K_NO_WAIT](../timer_reference/P086_系统时钟公共接口.md#ga3d9541cfe2e8395af66d186efa77362f)
- [K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_linkaddr.h](https://docs.zephyrproject.org/latest/doxygen/html/net__linkaddr_8h.html)
- [net_timeout.h](../time_headers_reference/P009_网络超时头文件参考.md)

---

[上一章](P022_net_context.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P024_net_event.h_源码浏览.md)
