---
id: learning.zephyr-docs.api-source-reference.page-344
title: igmp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/igmp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第344章\_igmp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/igmp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/igmp_8h.html)。

## 344.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
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
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00059"></a>
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
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00081"></a>
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
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="agroup__igmp_html_gad41f6f3d566de753a35e346bb2819a2b"></a>
<a id="agroup__igmp_html_gaf694dd42fb040c2aecf4638383f2a919"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astructigmp__param_html"></a>
<a id="astructigmp__param_html_a2b60c5de6e21371dacc7f7f34ba6904b"></a>
<a id="astructigmp__param_html_a5c76562c4679766f5132036febf05a03"></a>
<a id="astructigmp__param_html_acb8f39f66f0c11733cf855f4303b0495"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__in__addr_html"></a>

```c
/*
 * Copyright (c) 2021 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_IGMP_H_
#define ZEPHYR_INCLUDE_NET_IGMP_H_


#include <zephyr/types.h>

#include <zephyr/net/net_if.h>
#include <zephyr/net/net_ip.h>

#ifdef __cplusplus
extern "C" {
#endif

struct igmp_param {
        struct net_in_addr *source_list;
        size_t sources_len;
        bool include;
};

#if defined(CONFIG_NET_IPV4_IGMP)
int net_ipv4_igmp_join(struct net_if *iface, const struct net_in_addr *addr,
                       const struct igmp_param *param);
#else
static inline int net_ipv4_igmp_join(struct net_if *iface, const struct net_in_addr *addr,
                                     const struct igmp_param *param)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(addr);
        ARG_UNUSED(param);

        return -ENOSYS;
}
#endif

#if defined(CONFIG_NET_IPV4_IGMP)
int net_ipv4_igmp_leave(struct net_if *iface, const struct net_in_addr *addr);
#else
static inline int net_ipv4_igmp_leave(struct net_if *iface,
                                      const struct net_in_addr *addr)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(addr);

        return -ENOSYS;
}
#endif

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_IGMP_H_ */
```

## 344.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 99 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_IGMP_H_`。

## 344.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/igmp_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [igmp_param](../network_service_model_reference/P025_igmp_param_结构体.md)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [source_list](../network_service_model_reference/P025_igmp_param_结构体.md#a5c76562c4679766f5132036febf05a03)
- [sources_len](../network_service_model_reference/P025_igmp_param_结构体.md#acb8f39f66f0c11733cf855f4303b0495)
- [include](../network_service_model_reference/P025_igmp_param_结构体.md#a2b60c5de6e21371dacc7f7f34ba6904b)
- [net_ipv4_igmp_join](https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html#gad41f6f3d566de753a35e346bb2819a2b)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [net_ipv4_igmp_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html#gaf694dd42fb040c2aecf4638383f2a919)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [igmp_param::include](../network_service_model_reference/P025_igmp_param_结构体.md#a2b60c5de6e21371dacc7f7f34ba6904b)
- [igmp_param::source_list](../network_service_model_reference/P025_igmp_param_结构体.md#a5c76562c4679766f5132036febf05a03)
- [igmp_param::sources_len](../network_service_model_reference/P025_igmp_param_结构体.md#acb8f39f66f0c11733cf855f4303b0495)

---

[上一章](P343_ifx_cyw20829.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P345_iis2dlpc.h_源码浏览.md)
