---
id: learning.zephyr-docs.api-source-supplement-reference.page-146
title: policy.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pm_2policy_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第146章\_policy.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pm_2policy_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P068_电源管理策略头文件.md)。

## 146.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00036"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
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
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
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
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__subsys__pm__states_html_ga20e2f5ea9027a3653e5b9cc5aa1e21d5"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga059074d867befbe9c6b7afc170ee09b3"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga0c4fee04c7434e2ba741be8d5b1036c6"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga12f4d121aa8be0eb66381713b481a8b1"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga1c8634f68224aa64f05a373dfad5cb09"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga39f14c8509dee55ed084b4111584b766"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga43ad016f054543cf96c2362ccf12d29a"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga4cfc3c450387663b6e1bf9bb966baad8"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga4e66c09a5c8694e48b7be6b61667aeca"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga6483bd320881d697de27493b4f2d92d1"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga66ec68b1873f7e694a55608e9ad6ee5d"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga708b7d2f8cb5f09738e3c6e5937c475e"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga7965f17a8a82ea107f0cdd1afdc93afa"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga848627f6d143ece582711a16cab5442a"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga8ca62cfeef8d4ebb58800e3ac6b645ee"></a>
<a id="agroup__subsys__pm__sys__policy_html_ga9448e31e1bd1a8b02defe6d1427197ff"></a>
<a id="agroup__subsys__pm__sys__policy_html_gaadcb851b1bfb312ea0960918dc9f869e"></a>
<a id="agroup__subsys__pm__sys__policy_html_gab2a0a73416b3fcb535fa54a1f3b4c267"></a>
<a id="agroup__subsys__pm__sys__policy_html_gabbb379f8572f164addafe93ad3468f3d"></a>
<a id="agroup__subsys__pm__sys__policy_html_gacf77adf6eaf5258e03ce1923d685ed3b"></a>
<a id="agroup__subsys__pm__sys__policy_html_gadd21b48a4cadb7c05e74ff7fdd335386"></a>
<a id="agroup__subsys__pm__sys__policy_html_gae2680fcc323e161362e4a5aa5339ac12"></a>
<a id="agroup__subsys__pm__sys__policy_html_gae81343e186bcef8732c700bc1e3e207b"></a>
<a id="agroup__subsys__pm__sys__policy_html_gafb90036c42bce2cc44466427b2907a81"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aslist_8h_html"></a>
<a id="astate_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructdevice_html"></a>
<a id="astructpm__policy__event_html"></a>
<a id="astructpm__policy__latency__request_html"></a>
<a id="astructpm__policy__latency__subscription_html"></a>
<a id="astructpm__state__constraints_html"></a>
<a id="astructpm__state__info_html"></a>
<a id="astructpm__state__info_html_a422bc0c9aedc107dbfa57c3ac8eb2445"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_PM_POLICY_H_
#define ZEPHYR_INCLUDE_PM_POLICY_H_

#include <stdbool.h>
#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/pm/state.h>
#include <zephyr/sys/slist.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef void (*pm_policy_latency_changed_cb_t)(int32_t latency);

struct pm_policy_latency_subscription {
        sys_snode_t node;
        pm_policy_latency_changed_cb_t cb;
};

struct pm_policy_latency_request {
        sys_snode_t node;
        uint32_t value_us;
};

struct pm_policy_event {
        sys_snode_t node;
        int64_t uptime_ticks;
};


const struct pm_state_info *pm_policy_next_state(uint8_t cpu, int32_t ticks);


#define PM_ALL_SUBSTATES (UINT8_MAX)

#if defined(CONFIG_PM) || defined(__DOXYGEN__)
void pm_policy_state_lock_get(enum pm_state state, uint8_t substate_id);

void pm_policy_state_lock_put(enum pm_state state, uint8_t substate_id);

void pm_policy_state_all_lock_get(void);

void pm_policy_state_all_lock_put(void);

void pm_policy_state_constraints_get(struct pm_state_constraints *constraints);

void pm_policy_state_constraints_put(struct pm_state_constraints *constraints);

bool pm_policy_state_lock_is_active(enum pm_state state, uint8_t substate_id);

bool pm_policy_state_is_available(enum pm_state state, uint8_t substate_id);

bool pm_policy_state_any_active(void);

void pm_policy_event_register(struct pm_policy_event *evt, int64_t uptime_ticks);

void pm_policy_event_update(struct pm_policy_event *evt, int64_t uptime_ticks);

void pm_policy_event_unregister(struct pm_policy_event *evt);

int64_t pm_policy_next_event_ticks(void);

#if defined(CONFIG_PM_CUSTOM_TICKS_HOOK) || defined(__DOXYGEN__)
int64_t pm_policy_next_custom_ticks(void);
#endif /* CONFIG_PM_CUSTOM_TICKS_HOOK */

#else
static inline void pm_policy_state_lock_get(enum pm_state state, uint8_t substate_id)
{
        ARG_UNUSED(state);
        ARG_UNUSED(substate_id);
}

static inline void pm_policy_state_lock_put(enum pm_state state, uint8_t substate_id)
{
        ARG_UNUSED(state);
        ARG_UNUSED(substate_id);
}

static inline void pm_policy_state_all_lock_get(void)
{
}

static inline void pm_policy_state_all_lock_put(void)
{
}

static inline bool pm_policy_state_lock_is_active(enum pm_state state, uint8_t substate_id)
{
        ARG_UNUSED(state);
        ARG_UNUSED(substate_id);

        return false;
}

static inline void pm_policy_event_register(struct pm_policy_event *evt, int64_t uptime_ticks)
{
        ARG_UNUSED(evt);
        ARG_UNUSED(uptime_ticks);
}

static inline void pm_policy_event_update(struct pm_policy_event *evt, int64_t uptime_ticks)
{
        ARG_UNUSED(evt);
        ARG_UNUSED(uptime_ticks);
}

static inline void pm_policy_event_unregister(struct pm_policy_event *evt)
{
        ARG_UNUSED(evt);
}

static inline int64_t pm_policy_next_event_ticks(void)
{
        return -1;
}
#ifdef CONFIG_PM_CUSTOM_TICKS_HOOK

static inline int64_t pm_policy_next_custom_ticks(void)
{
        return -1;
}
#endif /* CONFIG_PM_CUSTOM_TICKS_HOOK */

#endif /* CONFIG_PM */

#if defined(CONFIG_PM_POLICY_DEVICE_CONSTRAINTS) || defined(__DOXYGEN__)
void pm_policy_device_power_lock_get(const struct device *dev);

void pm_policy_device_power_lock_put(const struct device *dev);

bool pm_policy_device_is_disabling_state(const struct device *dev,
                                         enum pm_state state, uint8_t substate_id);

#else

static inline void pm_policy_device_power_lock_get(const struct device *dev)
{
        ARG_UNUSED(dev);
}

static inline void pm_policy_device_power_lock_put(const struct device *dev)
{
        ARG_UNUSED(dev);
}

static inline bool pm_policy_device_is_disabling_state(const struct device *dev,
                                                       enum pm_state state,
                                                       uint8_t substate_id)
{
        ARG_UNUSED(dev);
        ARG_UNUSED(state);
        ARG_UNUSED(substate_id);

        return false;
}
#endif /* CONFIG_PM_POLICY_DEVICE_CONSTRAINTS */

#if defined(CONFIG_PM) || defined(CONFIG_PM_POLICY_LATENCY_STANDALONE) || defined(__DOXYGEN__)
void pm_policy_latency_request_add(struct pm_policy_latency_request *req,
                                   uint32_t value_us);

void pm_policy_latency_request_update(struct pm_policy_latency_request *req,
                                      uint32_t value_us);

void pm_policy_latency_request_remove(struct pm_policy_latency_request *req);

void pm_policy_latency_changed_subscribe(struct pm_policy_latency_subscription *req,
                                         pm_policy_latency_changed_cb_t cb);

void pm_policy_latency_changed_unsubscribe(struct pm_policy_latency_subscription *req);
#else
static inline void pm_policy_latency_request_add(
        struct pm_policy_latency_request *req, uint32_t value_us)
{
        ARG_UNUSED(req);
        ARG_UNUSED(value_us);
}

static inline void pm_policy_latency_request_update(
        struct pm_policy_latency_request *req, uint32_t value_us)
{
        ARG_UNUSED(req);
        ARG_UNUSED(value_us);
}

static inline void pm_policy_latency_request_remove(
        struct pm_policy_latency_request *req)
{
        ARG_UNUSED(req);
}
#endif /* CONFIG_PM CONFIG_PM_POLICY_LATENCY_STANDALONE */


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_PM_POLICY_H_ */
```

## 146.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 313 行

条件编译配置（Configuration）标记：`CONFIG_PM_CUSTOM_TICKS_HOOK`。

### 注释 3：原第 371 行

条件编译配置（Configuration）标记：`CONFIG_PM_CUSTOM_TICKS_HOOK`。

### 注释 4：原第 373 行

条件编译配置（Configuration）标记：`CONFIG_PM`。

### 注释 5：原第 439 行

条件编译配置（Configuration）标记：`CONFIG_PM_POLICY_DEVICE_CONSTRAINTS`。

### 注释 6：原第 505 行

条件编译配置标记：`CONFIG_PM`、`CONFIG_PM_POLICY_LATENCY_STANDALONE`。

### 注释 7：原第 515 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PM_POLICY_H_`。

## 146.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P068_电源管理策略头文件.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/pm/state.h](../power/P071_电源状态头文件.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [pm_policy_latency_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#gab2a0a73416b3fcb535fa54a1f3b4c267)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [pm_policy_latency_subscription](../power/P044_电源策略延迟订阅结构.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [pm_policy_latency_request](../power/P043_电源策略延迟请求结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pm_policy_event](../power/P042_电源策略事件结构.md)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [pm_state_info](../power/P047_电源状态信息结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pm_policy_state_lock_get](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#gabbb379f8572f164addafe93ad3468f3d)
- [pm_state](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#ga20e2f5ea9027a3653e5b9cc5aa1e21d5)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [substate_id](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#a422bc0c9aedc107dbfa57c3ac8eb2445)
- [pm_policy_state_lock_put](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga12f4d121aa8be0eb66381713b481a8b1)
- [pm_policy_state_all_lock_get](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#gae81343e186bcef8732c700bc1e3e207b)
- [pm_policy_state_all_lock_put](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#gadd21b48a4cadb7c05e74ff7fdd335386)
- [pm_policy_state_constraints_get](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga43ad016f054543cf96c2362ccf12d29a)
- [pm_state_constraints](../power/P046_电源状态约束集合.md)
- [pm_policy_state_constraints_put](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga7965f17a8a82ea107f0cdd1afdc93afa)
- [pm_policy_state_lock_is_active](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga39f14c8509dee55ed084b4111584b766)
- [pm_policy_state_is_available](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga1c8634f68224aa64f05a373dfad5cb09)
- [pm_policy_state_any_active](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga0c4fee04c7434e2ba741be8d5b1036c6)
- [pm_policy_event_register](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga4e66c09a5c8694e48b7be6b61667aeca)
- [pm_policy_event_update](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga059074d867befbe9c6b7afc170ee09b3)
- [pm_policy_event_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga9448e31e1bd1a8b02defe6d1427197ff)
- [pm_policy_next_event_ticks](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#gae2680fcc323e161362e4a5aa5339ac12)
- [pm_policy_next_custom_ticks](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga66ec68b1873f7e694a55608e9ad6ee5d)
- [pm_policy_device_power_lock_get](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga708b7d2f8cb5f09738e3c6e5937c475e)
- [device](../device_reference/P002_设备对象结构.md)
- [pm_policy_device_power_lock_put](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#gafb90036c42bce2cc44466427b2907a81)
- [pm_policy_device_is_disabling_state](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga4cfc3c450387663b6e1bf9bb966baad8)
- [pm_policy_latency_request_add](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga848627f6d143ece582711a16cab5442a)
- [pm_policy_latency_request_update](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga6483bd320881d697de27493b4f2d92d1)
- [pm_policy_latency_request_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#gaadcb851b1bfb312ea0960918dc9f869e)
- [pm_policy_latency_changed_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#gacf77adf6eaf5258e03ce1923d685ed3b)
- [pm_policy_latency_changed_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga8ca62cfeef8d4ebb58800e3ac6b645ee)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [state.h](../power/P071_电源状态头文件.md)
- [pm_state_info::substate_id](https://docs.zephyrproject.org/latest/doxygen/html/structpm__state__info.html#a422bc0c9aedc107dbfa57c3ac8eb2445)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P145_pipe.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P147_pm_s2ram.h_源码浏览.md)
