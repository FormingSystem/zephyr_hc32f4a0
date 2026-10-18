---
id: learning.zephyr-docs.api-source-reference.page-674
title: promiscuous.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/promiscuous_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第674章\_promiscuous.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/promiscuous_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/promiscuous_8h.html)。

## 674.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00079"></a>
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
<a id="l00090"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="agroup__promiscuous_html_ga089aebe5ce5b6ffc48b485d361bf9e7a"></a>
<a id="agroup__promiscuous_html_ga2fc01f791b635c54e85346cf898b324e"></a>
<a id="agroup__promiscuous_html_gac1a4b50b547d0f4b9396d71eecafd926"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__pkt_html_a7590eeacf06469206cb7e7949acfa7b2"></a>

```c


/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_PROMISCUOUS_H_
#define ZEPHYR_INCLUDE_NET_PROMISCUOUS_H_


#include <zephyr/net/net_pkt.h>
#include <zephyr/net/net_if.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_NET_PROMISCUOUS_MODE)
struct net_pkt *net_promisc_mode_wait_data(k_timeout_t timeout);
#else
static inline struct net_pkt *net_promisc_mode_wait_data(k_timeout_t timeout)
{
        ARG_UNUSED(timeout);

        return NULL;
}
#endif /* CONFIG_NET_PROMISCUOUS_MODE */

#if defined(CONFIG_NET_PROMISCUOUS_MODE)
int net_promisc_mode_on(struct net_if *iface);
#else
static inline int net_promisc_mode_on(struct net_if *iface)
{
        ARG_UNUSED(iface);

        return -ENOTSUP;
}
#endif /* CONFIG_NET_PROMISCUOUS_MODE */

#if defined(CONFIG_NET_PROMISCUOUS_MODE)
int net_promisc_mode_off(struct net_if *iface);
#else
static inline int net_promisc_mode_off(struct net_if *iface)
{
        ARG_UNUSED(iface);

        return -ENOTSUP;
}
#endif /* CONFIG_NET_PROMISCUOUS_MODE */

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_PROMISCUOUS_H_ */
```

## 674.2\_可见注释译文（Comments）

### 注释 1：原第 8 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

条件编译配置（Configuration）标记：`CONFIG_NET_PROMISCUOUS_MODE`。

### 注释 3：原第 67 行

条件编译配置（Configuration）标记：`CONFIG_NET_PROMISCUOUS_MODE`。

### 注释 4：原第 85 行

条件编译配置（Configuration）标记：`CONFIG_NET_PROMISCUOUS_MODE`。

### 注释 5：原第 95 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PROMISCUOUS_H_`。

## 674.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/promiscuous_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_promisc_mode_wait_data](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html#ga2fc01f791b635c54e85346cf898b324e)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_promisc_mode_on](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html#gac1a4b50b547d0f4b9396d71eecafd926)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [net_promisc_mode_off](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html#ga089aebe5ce5b6ffc48b485d361bf9e7a)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_pkt::iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)

---

[上一章](P673_priv_beacon_srv.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P675_protected_storage.h_源码浏览.md)
