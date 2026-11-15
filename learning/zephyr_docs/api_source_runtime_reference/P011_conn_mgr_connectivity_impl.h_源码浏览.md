---
id: learning.zephyr-docs.api-source-runtime-reference.page-11
title: conn_mgr_connectivity_impl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_conn\_mgr\_connectivity\_impl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h.html)。

## 11.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="foldopen00176"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00190"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="foldopen00240"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="foldopen00258"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="foldopen00272"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="foldopen00297"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="foldopen00313"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="foldopen00329"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="foldopen00353"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="aconn__mgr__connectivity_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__clock__apis_html_ga0bb4b83f0222193b21a8910311bab0ca"></a>
<a id="agroup__conn__mgr__connectivity__impl_html_ga128931a6fabce79829af5aebecd59985"></a>
<a id="agroup__conn__mgr__connectivity__impl_html_ga27be6dec40356facce7da18a31a2c12a"></a>
<a id="agroup__conn__mgr__connectivity__impl_html_ga4f0f3244f48c5e0204faf8278c2bd94f"></a>
<a id="agroup__conn__mgr__connectivity__impl_html_ga5fc0ba9d7bf365352e665d1c9a055889"></a>
<a id="agroup__conn__mgr__connectivity__impl_html_ga94a4930a6d7c4db4427dfdfad8f3c154"></a>
<a id="agroup__conn__mgr__connectivity_html_gaf10fb532a3dd07ec8c692a72643d0e3f"></a>
<a id="agroup__iterable__section__apis_html_gad723296f2650c25dd278e8586bfaf0ab"></a>
<a id="agroup__mutex__apis_html_ga360f4c0e7258b0d7030cdb1f452b2c31"></a>
<a id="agroup__mutex__apis_html_ga850549358645249c285669baa49c33b0"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructconn__mgr__conn__api_html"></a>
<a id="astructconn__mgr__conn__api_html_a15d4bd909af1a2d3348fdec822bca7b7"></a>
<a id="astructconn__mgr__conn__api_html_a2490ac680ca52c93ab0c7f48c04f673c"></a>
<a id="astructconn__mgr__conn__api_html_a5636cced185825bd6c6997b427fd6121"></a>
<a id="astructconn__mgr__conn__api_html_a92064a4752f0c9621c5c6a745708a66e"></a>
<a id="astructconn__mgr__conn__api_html_ad2bb08d518e2f797002ca5257889a59e"></a>
<a id="astructconn__mgr__conn__api_html_aee0d0fc9ef3361c8859b69128a087ba5"></a>
<a id="astructconn__mgr__conn__binding_html"></a>
<a id="astructconn__mgr__conn__binding_html_a288749353194206b8d8766f8f17aff48"></a>
<a id="astructconn__mgr__conn__binding_html_a50a8484896227f81aaf62f7f9a913985"></a>
<a id="astructconn__mgr__conn__binding_html_a59bd71867b19e002c310d85496833e8f"></a>
<a id="astructconn__mgr__conn__binding_html_a8474461cf7b00132441227aae07511ab"></a>
<a id="astructconn__mgr__conn__binding_html_a9b842340ebe872f30935b8f7e75d3605"></a>
<a id="astructconn__mgr__conn__binding_html_ad9102e2cf44b5940b21b1d160fea7611"></a>
<a id="astructconn__mgr__conn__impl_html"></a>
<a id="astructconn__mgr__conn__impl_html_a1229707a1b919659647412cb1eecd61b"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructnet__if_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_IMPL_H_
#define ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_IMPL_H_

#include <zephyr/device.h>
#include <zephyr/net/net_if.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/net_mgmt.h>
#include <zephyr/net/conn_mgr_connectivity.h>

#ifdef __cplusplus
extern "C" {
#endif


/* Forward declaration */
struct conn_mgr_conn_binding;

struct conn_mgr_conn_api {
        bool (*has_connection_config)(struct conn_mgr_conn_binding *const binding);

        int (*connect)(struct conn_mgr_conn_binding *const binding);

        int (*disconnect)(struct conn_mgr_conn_binding *const binding);

        void (*init)(struct conn_mgr_conn_binding *const binding);

        int (*set_opt)(struct conn_mgr_conn_binding *const binding,
                       int optname, const void *optval, size_t optlen);

        int (*get_opt)(struct conn_mgr_conn_binding *const binding,
                       int optname, void *optval, size_t *optlen);
};

#define CONN_MGR_CONN_IMPL_GET_NAME(conn_id)            __conn_mgr_conn_##conn_id
#define CONN_MGR_CONN_IMPL_GET_CTX_TYPE(conn_id)        conn_id##_CTX_TYPE

struct conn_mgr_conn_impl {
        struct conn_mgr_conn_api *api;
};

#define CONN_MGR_CONN_DEFINE(conn_id, conn_api)                                         \
        const struct conn_mgr_conn_impl CONN_MGR_CONN_IMPL_GET_NAME(conn_id) = {        \
                .api = conn_api,                                                        \
        };

#define CONN_MGR_CONN_DECLARE_PUBLIC(conn_id)                                           \
        extern const struct conn_mgr_conn_impl CONN_MGR_CONN_IMPL_GET_NAME(conn_id)

#define CONN_MGR_CONN_BINDING_GET_NAME(dev_id, sfx)     __conn_mgr_bndg_##dev_id##_##sfx
#define CONN_MGR_CONN_BINDING_GET_DATA(dev_id, sfx)     __conn_mgr_bndg_data_##dev_id##_##sfx
#define CONN_MGR_CONN_BINDING_GET_MUTEX(dev_id, sfx)    __conn_mgr_bndg_mutex_##dev_id##_##sfx

struct conn_mgr_conn_binding {
        struct net_if *iface;

        const struct conn_mgr_conn_impl *impl;

        void *ctx;


        uint32_t flags;

        int timeout;

        int idle_timeout;


        /* Internal-use work item for tracking interface idle timeouts */
        struct k_work_delayable idle_worker;

        /* Internal-use mutex for protecting access to the binding and API functions. */
        struct k_mutex *mutex;
};

#define CONN_MGR_BIND_CONN_INST(dev_id, inst, conn_id)                                          \
        K_MUTEX_DEFINE(CONN_MGR_CONN_BINDING_GET_MUTEX(dev_id, inst));                          \
        static CONN_MGR_CONN_IMPL_GET_CTX_TYPE(conn_id)                                         \
                                        CONN_MGR_CONN_BINDING_GET_DATA(dev_id, inst);           \
        static STRUCT_SECTION_ITERABLE(conn_mgr_conn_binding,                                   \
                                        CONN_MGR_CONN_BINDING_GET_NAME(dev_id, inst)) = {       \
                .iface = NET_IF_GET(dev_id, inst),                                              \
                .impl = &(CONN_MGR_CONN_IMPL_GET_NAME(conn_id)),                                \
                .ctx = &(CONN_MGR_CONN_BINDING_GET_DATA(dev_id, inst)),                         \
                .mutex = &(CONN_MGR_CONN_BINDING_GET_MUTEX(dev_id, inst))                       \
        };

#define CONN_MGR_BIND_CONN(dev_id, conn_id)             \
        CONN_MGR_BIND_CONN_INST(dev_id, 0, conn_id)

static inline struct conn_mgr_conn_binding *conn_mgr_if_get_binding(struct net_if *iface)
{
        STRUCT_SECTION_FOREACH(conn_mgr_conn_binding, binding) {
                if (iface == binding->iface) {
                        if (binding->impl->api) {
                                return binding;
                        }
                        return NULL;
                }
        }
        return NULL;
}

static inline void conn_mgr_binding_lock(struct conn_mgr_conn_binding *binding)
{
        (void)k_mutex_lock(binding->mutex, K_FOREVER);
}

static inline void conn_mgr_binding_unlock(struct conn_mgr_conn_binding *binding)
{
        (void)k_mutex_unlock(binding->mutex);
}

static inline void conn_mgr_binding_set_flag(struct conn_mgr_conn_binding *binding,
                                             enum conn_mgr_if_flag flag, bool value)
{
        conn_mgr_binding_lock(binding);

        binding->flags &= ~BIT(flag);
        if (value) {
                binding->flags |= BIT(flag);
        }

        conn_mgr_binding_unlock(binding);
}

static inline bool conn_mgr_binding_get_flag(struct conn_mgr_conn_binding *binding,
                                             enum conn_mgr_if_flag flag)
{
        bool value = false;

        conn_mgr_binding_lock(binding);

        value = !!(binding->flags & BIT(flag));

        conn_mgr_binding_unlock(binding);

        return value;
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_IMPL_H_ */
```

## 11.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 35 行

前向声明（Forward declaration）。

### 注释 3：原第 225 行

内部使用的工作项（Work item），用于跟踪接口空闲超时。

### 注释 4：原第 228 行

内部使用的互斥锁（Mutex），保护对绑定对象和 API 函数的访问。

### 注释 5：原第 375 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_CONN_MGR_CONNECTIVITY_IMPL_H_`。

## 11.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [zephyr/net/conn_mgr_connectivity.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity_8h.html)
- [conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)
- [conn_mgr_conn_api](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [has_connection_config](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#a2490ac680ca52c93ab0c7f48c04f673c)
- [connect](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#a92064a4752f0c9621c5c6a745708a66e)
- [disconnect](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#aee0d0fc9ef3361c8859b69128a087ba5)
- [init](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#ad2bb08d518e2f797002ca5257889a59e)
- [set_opt](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#a5636cced185825bd6c6997b427fd6121)
- [get_opt](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#a15d4bd909af1a2d3348fdec822bca7b7)
- [conn_mgr_conn_impl](../modem_wireless_model_reference/P011_conn_mgr_conn_impl_结构体.md)
- [api](../modem_wireless_model_reference/P011_conn_mgr_conn_impl_结构体.md#a1229707a1b919659647412cb1eecd61b)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [iface](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a59bd71867b19e002c310d85496833e8f)
- [impl](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a288749353194206b8d8766f8f17aff48)
- [ctx](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#ad9102e2cf44b5940b21b1d160fea7611)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a9b842340ebe872f30935b8f7e75d3605)
- [timeout](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a8474461cf7b00132441227aae07511ab)
- [idle_timeout](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a50a8484896227f81aaf62f7f9a913985)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [conn_mgr_if_get_binding](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga5fc0ba9d7bf365352e665d1c9a055889)
- [STRUCT_SECTION_FOREACH](../iterable_reference/P001_可遍历段公共接口.md#gad723296f2650c25dd278e8586bfaf0ab)
- [conn_mgr_binding_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga27be6dec40356facce7da18a31a2c12a)
- [k_mutex_lock](../synchronization_reference/P006_互斥量公共接口.md#ga850549358645249c285669baa49c33b0)
- [K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)
- [conn_mgr_binding_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga94a4930a6d7c4db4427dfdfad8f3c154)
- [k_mutex_unlock](../synchronization_reference/P006_互斥量公共接口.md#ga360f4c0e7258b0d7030cdb1f452b2c31)
- [conn_mgr_binding_set_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga4f0f3244f48c5e0204faf8278c2bd94f)
- [conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)
- [~BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [conn_mgr_binding_get_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga128931a6fabce79829af5aebecd59985)
- [conn_mgr_connectivity.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity_8h.html)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [conn_mgr_conn_api::get_opt](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#a15d4bd909af1a2d3348fdec822bca7b7)
- [conn_mgr_conn_api::has_connection_config](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#a2490ac680ca52c93ab0c7f48c04f673c)
- [conn_mgr_conn_api::set_opt](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#a5636cced185825bd6c6997b427fd6121)
- [conn_mgr_conn_api::connect](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#a92064a4752f0c9621c5c6a745708a66e)
- [conn_mgr_conn_api::init](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#ad2bb08d518e2f797002ca5257889a59e)
- [conn_mgr_conn_api::disconnect](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md#aee0d0fc9ef3361c8859b69128a087ba5)
- [conn_mgr_conn_binding::impl](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a288749353194206b8d8766f8f17aff48)
- [conn_mgr_conn_binding::idle_timeout](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a50a8484896227f81aaf62f7f9a913985)
- [conn_mgr_conn_binding::iface](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a59bd71867b19e002c310d85496833e8f)
- [conn_mgr_conn_binding::timeout](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a8474461cf7b00132441227aae07511ab)
- [conn_mgr_conn_binding::flags](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a9b842340ebe872f30935b8f7e75d3605)
- [conn_mgr_conn_binding::ctx](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#ad9102e2cf44b5940b21b1d160fea7611)
- [conn_mgr_conn_impl::api](../modem_wireless_model_reference/P011_conn_mgr_conn_impl_结构体.md#a1229707a1b919659647412cb1eecd61b)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P010_conn_mgr_connectivity.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P012_dma_bee.h_源码浏览.md)
