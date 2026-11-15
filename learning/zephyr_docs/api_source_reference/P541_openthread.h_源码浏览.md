---
id: learning.zephyr-docs.api-source-reference.page-541
title: openthread.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第541章\_openthread.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html)。

## 541.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_2thread_8h_html_a6379f5a1f19ffbc262a6877c4f6e3647"></a>
<a id="akernel_8h_html"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a14ea88a5f4e4a9e014f2381cd853e8de"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a1d81606d48cfb714ba59b94400bbce23"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a4178b72288585869e2c941acdc21db57"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a420c3321272141f63ea86166b84ec845"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a4d213cad99e6eeb747bd0057248251e5"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a517a538fa32afac8ca8968ada2cea89d"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a558165d2e49e9335649c94ac0be53392"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a76aff0a483b1462707f80de5185b17e4"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a8f95392e11afa85e9bd80569c1793e76"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_a9499c4c69a0094f0b7ef803ac05fb19a"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_ab5669622dfd83d3a5175fa47325dade3"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_ae3945bc3549118dc5420f9859588282d"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_ae4ad25613f8eada1a0a29426a2f4a518"></a>
<a id="amodules_2openthread_2include_2openthread_8h_html_af52cc96d5d4be673f16eb4856de6cc58"></a>
<a id="astructk__work__q_html"></a>
<a id="astructopenthread__state__changed__callback_html"></a>
<a id="astructopenthread__state__changed__callback_html_a5c36164b8db65f2493c17a61c3434128"></a>
<a id="astructopenthread__state__changed__callback_html_a8bf9761ba1e70d9bfcdcda108109d52f"></a>
<a id="astructopenthread__state__changed__callback_html_ae5a1648859eeb3df7a285becf33c8219"></a>

```c
/*
 * Copyright (c) 2025 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_MODULES_OPENTHREAD_OPENTHREAD_H_
#define ZEPHYR_MODULES_OPENTHREAD_OPENTHREAD_H_

#include <zephyr/kernel.h>

#include <openthread/instance.h>
#include <openthread/message.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef void (*openthread_receive_cb)(struct otMessage *message, void *context);


struct openthread_state_changed_callback {
        otStateChangedCallback otCallback;

        void *user_data;

        sys_snode_t node;
};

int openthread_state_changed_callback_register(struct openthread_state_changed_callback *cb);

int openthread_state_changed_callback_unregister(struct openthread_state_changed_callback *cb);

k_tid_t openthread_thread_id_get(void);

struct k_work_q *openthread_work_q_get(void);

struct otInstance *openthread_get_default_instance(void);

int openthread_init(void);

int openthread_run(void);

int openthread_stop(void);

void openthread_set_receive_cb(openthread_receive_cb cb, void *context);

#if defined(CONFIG_OPENTHREAD_NAT64_TRANSLATOR) || defined(__DOXYGEN__)
void openthread_set_nat64_receive_cb(openthread_receive_cb cb, void *context);
#endif /* CONFIG_OPENTHREAD_NAT64_TRANSLATOR */

void openthread_mutex_lock(void);

int openthread_mutex_try_lock(void);

void openthread_mutex_unlock(void);

#if defined(CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)
void openthread_notify_border_router_work(void);
#endif /* CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_MODULES_OPENTHREAD_OPENTHREAD_H_ */
```

## 541.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 155 行

条件编译配置（Configuration）标记：`CONFIG_OPENTHREAD_NAT64_TRANSLATOR`。

### 注释 3：原第 185 行

条件编译配置（Configuration）标记：`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`。

### 注释 4：原第 191 行

头文件保护宏（Header guard）标记：`ZEPHYR_MODULES_OPENTHREAD_OPENTHREAD_H_`。

## 541.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [openthread_receive_cb](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a8f95392e11afa85e9bd80569c1793e76)
- [openthread_state_changed_callback](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md)
- [otCallback](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md#a8bf9761ba1e70d9bfcdcda108109d52f)
- [user_data](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md#ae5a1648859eeb3df7a285becf33c8219)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md#a5c36164b8db65f2493c17a61c3434128)
- [openthread_state_changed_callback_register](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a4178b72288585869e2c941acdc21db57)
- [openthread_state_changed_callback_unregister](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#ae4ad25613f8eada1a0a29426a2f4a518)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [openthread_thread_id_get](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a9499c4c69a0094f0b7ef803ac05fb19a)
- [k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)
- [openthread_work_q_get](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a1d81606d48cfb714ba59b94400bbce23)
- [openthread_get_default_instance](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a517a538fa32afac8ca8968ada2cea89d)
- [openthread_init](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a4d213cad99e6eeb747bd0057248251e5)
- [openthread_run](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a558165d2e49e9335649c94ac0be53392)
- [openthread_stop](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#af52cc96d5d4be673f16eb4856de6cc58)
- [openthread_set_receive_cb](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a14ea88a5f4e4a9e014f2381cd853e8de)
- [openthread_set_nat64_receive_cb](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a76aff0a483b1462707f80de5185b17e4)
- [openthread_mutex_lock](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#ae3945bc3549118dc5420f9859588282d)
- [openthread_mutex_try_lock](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#ab5669622dfd83d3a5175fa47325dade3)
- [openthread_mutex_unlock](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a420c3321272141f63ea86166b84ec845)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [openthread_state_changed_callback::node](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md#a5c36164b8db65f2493c17a61c3434128)
- [openthread_state_changed_callback::otCallback](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md#a8bf9761ba1e70d9bfcdcda108109d52f)
- [openthread_state_changed_callback::user_data](../network_service_model_reference/P039_openthread_state_changed_callback_结构体.md#ae5a1648859eeb3df7a285becf33c8219)

---

[上一章](P540_keys.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P542_mpipe.h_源码浏览.md)
