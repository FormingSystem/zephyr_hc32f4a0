---
id: learning.zephyr-docs.api-source-supplement-reference.page-109
title: mdns_responder.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_mdns\_responder.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h.html)。

## 109.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00059"></a>
<a id="l00060"></a>
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
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="adns__sd_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="amdns__responder_8h_html_a085957294062f9948c213070dc912a34"></a>
<a id="amdns__responder_8h_html_a4682ee30bf3e739790dbcaede5485777"></a>
<a id="amdns__responder_8h_html_ae8b53e59ec3e159e34ffda276a2f72dc"></a>
<a id="anet__if_8h_html"></a>
<a id="astructdns__sd__rec_html"></a>
<a id="astructnet__if_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_MDNS_RESPONDER_H_
#define ZEPHYR_INCLUDE_NET_MDNS_RESPONDER_H_

#include <stddef.h>
#include <errno.h>
#include <zephyr/net/dns_sd.h>
#include <zephyr/net/net_if.h>

#ifdef __cplusplus
extern "C" {
#endif

int mdns_responder_set_ext_records(const struct dns_sd_rec *records, size_t count);

#if defined(CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL) || defined(__DOXYGEN__)
int mdns_responder_enable_iface(struct net_if *iface);

int mdns_responder_disable_iface(struct net_if *iface);

#else /* CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL */

static inline int mdns_responder_enable_iface(struct net_if *iface)
{
        ARG_UNUSED(iface);

        return -ENOTSUP;
}

static inline int mdns_responder_disable_iface(struct net_if *iface)
{
        ARG_UNUSED(iface);

        return -ENOTSUP;
}

#endif /* CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL || __DOXYGEN__ */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_MDNS_RESPONDER_H_ */
```

## 109.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 78 行

条件编译配置（Configuration）标记：`CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL`。

### 注释 3：原第 94 行

条件编译表达式：`CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL || __DOXYGEN__`。

### 注释 4：原第 100 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_MDNS_RESPONDER_H_`。

## 109.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/net/dns_sd.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__sd_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [mdns_responder_set_ext_records](https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h.html#a4682ee30bf3e739790dbcaede5485777)
- [dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)
- [mdns_responder_enable_iface](https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h.html#ae8b53e59ec3e159e34ffda276a2f72dc)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [mdns_responder_disable_iface](https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h.html#a085957294062f9948c213070dc912a34)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [dns_sd.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__sd_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)

---

[上一章](P108_mcs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P110_mem_manage.h_源码浏览.md)
