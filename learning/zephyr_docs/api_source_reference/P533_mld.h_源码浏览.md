---
id: learning.zephyr-docs.api-source-reference.page-533
title: mld.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mld_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第533章\_mld.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mld_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mld_8h.html)。

## 533.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
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
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__mld_html_ga102060070f1165639735487e5bd0dbc2"></a>
<a id="agroup__mld_html_gada558afaf913bc67b7921d3a0de561f7"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__in6__addr_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_MLD_H_
#define ZEPHYR_INCLUDE_NET_MLD_H_


#include <errno.h>

#include <zephyr/net/net_if.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_NET_IPV6_MLD)
int net_ipv6_mld_join(struct net_if *iface, const struct net_in6_addr *addr);
#else
static inline int
net_ipv6_mld_join(struct net_if *iface, const struct net_in6_addr *addr)
{
        ARG_UNUSED(addr);
        ARG_UNUSED(iface);

        return -ENOTSUP;
}
#endif /* CONFIG_NET_IPV6_MLD */

#if defined(CONFIG_NET_IPV6_MLD)
int net_ipv6_mld_leave(struct net_if *iface, const struct net_in6_addr *addr);
#else
static inline int
net_ipv6_mld_leave(struct net_if *iface, const struct net_in6_addr *addr)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(addr);

        return -ENOTSUP;
}
#endif /* CONFIG_NET_IPV6_MLD */

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_MLD_H_ */
```

## 533.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 60 行

条件编译配置（Configuration）标记：`CONFIG_NET_IPV6_MLD`。

### 注释 3：原第 81 行

条件编译配置（Configuration）标记：`CONFIG_NET_IPV6_MLD`。

### 注释 4：原第 91 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_MLD_H_`。

## 533.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mld_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [net_ipv6_mld_join](https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html#ga102060070f1165639735487e5bd0dbc2)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [net_ipv6_mld_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html#gada558afaf913bc67b7921d3a0de561f7)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P532_max2221x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P534_mlx90394.h_源码浏览.md)
