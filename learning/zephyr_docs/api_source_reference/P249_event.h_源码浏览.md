---
id: learning.zephyr-docs.api-source-reference.page-249
title: event.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/event_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第249章\_event.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/event_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/event_8h.html)。

## 249.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="agroup__hawkbit__event_html_ga0ec141ff3e11c0e1d0e3f8757ace5010"></a>
<a id="agroup__hawkbit__event_html_ga49064aef93c5383f24ea41819b78c458"></a>
<a id="agroup__hawkbit__event_html_ga646c72464b0761009f42393fa313c880"></a>
<a id="agroup__hawkbit__event_html_ga794d232d73d105bd170b222ab17ce2af"></a>
<a id="agroup__hawkbit__event_html_gaa19bb74cb46e9aff7742907a86c96359"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa55dd61e8016fe6b69339e136d5ff279e"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b"></a>
<a id="agroup__hawkbit__event_html_gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_8h_html"></a>
<a id="aslist_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Vogl Electronic GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */



#ifndef ZEPHYR_INCLUDE_MGMT_HAWKBIT_EVENT_H_
#define ZEPHYR_INCLUDE_MGMT_HAWKBIT_EVENT_H_

#include <zephyr/kernel.h>
#include <zephyr/sys/slist.h>

enum hawkbit_event_type {
        HAWKBIT_EVENT_ERROR,
        HAWKBIT_EVENT_ERROR_NETWORKING,
        HAWKBIT_EVENT_ERROR_PERMISSION,
        HAWKBIT_EVENT_ERROR_METADATA,
        HAWKBIT_EVENT_ERROR_DOWNLOAD,
        HAWKBIT_EVENT_ERROR_ALLOC,
        HAWKBIT_EVENT_UPDATE_DOWNLOADED,
        HAWKBIT_EVENT_NO_UPDATE,
        HAWKBIT_EVENT_CANCEL_UPDATE,
        HAWKBIT_EVENT_START_DOWNLOAD,
        HAWKBIT_EVENT_END_DOWNLOAD,
        HAWKBIT_EVENT_START_RUN,
        HAWKBIT_EVENT_END_RUN,
        HAWKBIT_EVENT_BEFORE_REBOOT,
        HAWKBIT_EVENT_CONFIRMED_CURRENT_IMAGE,
};

struct hawkbit_event_callback;

typedef void (*hawkbit_event_callback_handler_t)(struct hawkbit_event_callback *cb,
                                                 enum hawkbit_event_type event);


struct hawkbit_event_callback {
        sys_snode_t node;

        hawkbit_event_callback_handler_t handler;

        enum hawkbit_event_type event;
};



#define HAWKBIT_EVENT_CREATE_CALLBACK(_callback, _handler, _event)                                 \
        struct hawkbit_event_callback _callback = {                                                \
                .handler = _handler,                                                               \
                .event = _event,                                                                   \
        }

static inline void hawkbit_event_init_callback(struct hawkbit_event_callback *callback,
                                               hawkbit_event_callback_handler_t handler,
                                               enum hawkbit_event_type event)
{
        __ASSERT(callback, "Callback pointer should not be NULL");
        __ASSERT(handler, "Callback handler pointer should not be NULL");

        callback->handler = handler;
        callback->event = event;
}

int hawkbit_event_add_callback(struct hawkbit_event_callback *cb);

int hawkbit_event_remove_callback(struct hawkbit_event_callback *cb);


#endif /* ZEPHYR_INCLUDE_MGMT_HAWKBIT_EVENT_H_ */
```

## 249.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Vogl Electronic GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 165 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_HAWKBIT_EVENT_H_`。

## 249.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/event_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [hawkbit_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga794d232d73d105bd170b222ab17ce2af)
- [HAWKBIT_EVENT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd)
- [HAWKBIT_EVENT_ERROR_NETWORKING](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214)
- [HAWKBIT_EVENT_ERROR_PERMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a)
- [HAWKBIT_EVENT_ERROR_METADATA](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8)
- [HAWKBIT_EVENT_ERROR_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c)
- [HAWKBIT_EVENT_ERROR_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639)
- [HAWKBIT_EVENT_UPDATE_DOWNLOADED](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4)
- [HAWKBIT_EVENT_NO_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e)
- [HAWKBIT_EVENT_CANCEL_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b)
- [HAWKBIT_EVENT_START_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55)
- [HAWKBIT_EVENT_END_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984)
- [HAWKBIT_EVENT_START_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3)
- [HAWKBIT_EVENT_END_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2)
- [HAWKBIT_EVENT_BEFORE_REBOOT](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf)
- [HAWKBIT_EVENT_CONFIRMED_CURRENT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa55dd61e8016fe6b69339e136d5ff279e)
- [hawkbit_event_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga49064aef93c5383f24ea41819b78c458)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [hawkbit_event_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga0ec141ff3e11c0e1d0e3f8757ace5010)
- [hawkbit_event_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga646c72464b0761009f42393fa313c880)
- [hawkbit_event_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gaa19bb74cb46e9aff7742907a86c96359)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)

---

[上一章](P248_ets.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P250_explorir_m.h_源码浏览.md)
