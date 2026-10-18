---
id: learning.zephyr-docs.api-source-reference.page-113
title: conn_mgr_monitor.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__monitor_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第113章\_conn\_mgr\_monitor.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__monitor_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__monitor_8h.html)。

## 113.1\_原始可见代码（Source Code）

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
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="agroup__conn__mgr_html_ga6bd1ee46dc2e3dae554fce49e82c6187"></a>
<a id="agroup__conn__mgr_html_ga7bad393c43a24df7a03176830b05b288"></a>
<a id="agroup__conn__mgr_html_gacc8735b835dea9b31531fcca9fe8a979"></a>
<a id="agroup__conn__mgr_html_gacdde95f41f32e7a829d8cd3a6d0e2277"></a>
<a id="agroup__conn__mgr_html_gad96056478dcbcb568dd2ef8d5d2ad50b"></a>
<a id="agroup__conn__mgr_html_gada16a88ec2c1db71fc39782b0696dac2"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__l2_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_CONN_MGR_MONITOR_H_
#define ZEPHYR_INCLUDE_NET_CONN_MGR_MONITOR_H_

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_NET_CONNECTION_MANAGER) || defined(__DOXYGEN__)


struct net_if;
struct net_l2;

void conn_mgr_mon_resend_status(void);

void conn_mgr_ignore_iface(struct net_if *iface);

void conn_mgr_watch_iface(struct net_if *iface);

bool conn_mgr_is_iface_ignored(struct net_if *iface);

void conn_mgr_ignore_l2(const struct net_l2 *l2);

void conn_mgr_watch_l2(const struct net_l2 *l2);


#else

#define conn_mgr_mon_resend_status(...)
#define conn_mgr_ignore_iface(...)
#define conn_mgr_watch_iface(...)
#define conn_mgr_ignore_l2(...)
#define conn_mgr_watch_l2(...)

#endif /* CONFIG_NET_CONNECTION_MANAGER */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_CONN_MGR_MONITOR_H_ */
```

## 113.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 106 行

条件编译配置（Configuration）标记：`CONFIG_NET_CONNECTION_MANAGER`。

### 注释 3：原第 112 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_CONN_MGR_MONITOR_H_`。

## 113.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__monitor_8h.html)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_l2](../network_core_model_reference/P103_net_l2_结构体.md)
- [conn_mgr_mon_resend_status](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gacdde95f41f32e7a829d8cd3a6d0e2277)
- [conn_mgr_ignore_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#ga7bad393c43a24df7a03176830b05b288)
- [conn_mgr_watch_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gacc8735b835dea9b31531fcca9fe8a979)
- [conn_mgr_is_iface_ignored](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gada16a88ec2c1db71fc39782b0696dac2)
- [conn_mgr_ignore_l2](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#ga6bd1ee46dc2e3dae554fce49e82c6187)
- [conn_mgr_watch_l2](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gad96056478dcbcb568dd2ef8d5d2ad50b)

---

[上一章](P112_confstr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P114_connectivity_wifi_mgmt.h_源码浏览.md)
