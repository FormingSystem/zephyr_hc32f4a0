---
id: learning.zephyr-docs.api-source-supplement-reference.page-67
title: events.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/events_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_events.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/events_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/events_8h.html)。

## 67.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="agroup__xen__event__channels_html_ga0597d0e7f40eca8dd73a131c95e346d4"></a>
<a id="agroup__xen__event__channels_html_ga1e631dcb6d0ab84d2b63cced85f28d47"></a>
<a id="agroup__xen__event__channels_html_ga2ac07d6eff7d3406716917578b5f7daf"></a>
<a id="agroup__xen__event__channels_html_ga3d6fce57c67b5ad26532e3721de59328"></a>
<a id="agroup__xen__event__channels_html_ga46ba842a0e4f518d03683253d35b7126"></a>
<a id="agroup__xen__event__channels_html_ga4b07a630ef8286be5ab8b120393f5be0"></a>
<a id="agroup__xen__event__channels_html_ga74e60b33dd93a62835e86b251a9cd43c"></a>
<a id="agroup__xen__event__channels_html_ga761efce6eab19f91b33391d4bf516fff"></a>
<a id="agroup__xen__event__channels_html_ga76e7a069825b569709b1e5342a648598"></a>
<a id="agroup__xen__event__channels_html_gabad4417540bf329eca43842bf83549e9"></a>
<a id="agroup__xen__event__channels_html_gabed06147ec0c0f9650ac7348a04ee430"></a>
<a id="agroup__xen__event__channels_html_gac9ccbc6f134743ad39396712c47facf9"></a>
<a id="agroup__xen__event__channels_html_gadc0a69c0205307e86458ada50aa0302d"></a>
<a id="agroup__xen__event__channels_html_gae5391f2b67ddbd598f33d796ba591568"></a>
<a id="agroup__xen__event__channels_html_gaf6542be4472fb2d1dc17deca6c323972"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2021-2025 EPAM Systems
 * Copyright (c) 2022 Arm Limited (or its affiliates). All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_XEN_EVENTS_H_
#define ZEPHYR_INCLUDE_XEN_EVENTS_H_

#include <xen/public/event_channel.h>

#include <zephyr/kernel.h>


typedef void (*evtchn_cb_t)(void *priv);

/* Internal event-channel callback slot. */
struct event_channel_handle {
        evtchn_cb_t cb;
        void *priv;
};
typedef struct event_channel_handle evtchn_handle_t;

int evtchn_status(evtchn_status_t *status);

int evtchn_close(evtchn_port_t port);

int evtchn_set_priority(evtchn_port_t port, uint32_t priority);

int notify_evtchn(evtchn_port_t port);

int alloc_unbound_event_channel(domid_t remote_dom);

int alloc_unbound_event_channel_dom0(domid_t dom, domid_t remote_dom);

int bind_interdomain_event_channel(domid_t remote_dom, evtchn_port_t remote_port,
                                   evtchn_cb_t cb, void *data);

int bind_event_channel(evtchn_port_t port, evtchn_cb_t cb, void *data);

int unbind_event_channel(evtchn_port_t port);

int get_missed_events(evtchn_port_t port);

int mask_event_channel(evtchn_port_t port);

int unmask_event_channel(evtchn_port_t port);

void clear_event_channel(evtchn_port_t port);

int xen_events_init(void);


#endif /* ZEPHYR_INCLUDE_XEN_EVENTS_H_ */
```

## 67.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021-2025 EPAM Systems。

版权（Copyright）：© 2022 Arm Limited (or its affiliates). All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

内部事件通道回调槽位（Event-channel callback slot）。

### 注释 3：原第 217 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_EVENTS_H_`。

## 67.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/events_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [evtchn_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga1e631dcb6d0ab84d2b63cced85f28d47)
- [evtchn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gae5391f2b67ddbd598f33d796ba591568)
- [evtchn_close](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gabed06147ec0c0f9650ac7348a04ee430)
- [evtchn_set_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga761efce6eab19f91b33391d4bf516fff)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [notify_evtchn](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga3d6fce57c67b5ad26532e3721de59328)
- [alloc_unbound_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga46ba842a0e4f518d03683253d35b7126)
- [alloc_unbound_event_channel_dom0](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga76e7a069825b569709b1e5342a648598)
- [bind_interdomain_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gadc0a69c0205307e86458ada50aa0302d)
- [bind_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga74e60b33dd93a62835e86b251a9cd43c)
- [unbind_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gabad4417540bf329eca43842bf83549e9)
- [get_missed_events](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga2ac07d6eff7d3406716917578b5f7daf)
- [mask_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga4b07a630ef8286be5ab8b120393f5be0)
- [unmask_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gac9ccbc6f134743ad39396712c47facf9)
- [clear_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga0597d0e7f40eca8dd73a131c95e346d4)
- [xen_events_init](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gaf6542be4472fb2d1dc17deca6c323972)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P066_esp_wifi_mesh.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P068_exc_handle.h_源码浏览.md)
