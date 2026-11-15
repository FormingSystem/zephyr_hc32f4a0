---
id: learning.zephyr-docs.api-source-configuration-reference.page-71
title: device.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pm_2device_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_device.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pm_2device_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P069_设备电源管理头文件.md)。

## 71.1\_原始可见代码（Source Code）

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
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00085"></a>
<a id="l00109"></a>
<a id="l00126"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00154"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00173"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="foldopen00213"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="foldopen00237"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="foldopen00261"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
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
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="foldopen00413"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="foldopen00428"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="foldopen00443"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="foldopen00457"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="foldopen00468"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="foldopen00479"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="foldopen00547"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="foldopen00567"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="aatomic_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__subsys__pm__device_html_ga0716c6158804ac48022280d8d237f8c1"></a>
<a id="agroup__subsys__pm__device_html_ga1d7ab9b0b497e016b9b22d2506cd23f9"></a>
<a id="agroup__subsys__pm__device_html_ga32eb5e210d2f0ba533b0185a94c8744e"></a>
<a id="agroup__subsys__pm__device_html_ga3840d6e7832a00b93763247a5951bfde"></a>
<a id="agroup__subsys__pm__device_html_ga4c366f49e326a8b8e01d90cb2ee424ba"></a>
<a id="agroup__subsys__pm__device_html_ga561c0789071e3c3963f21f4c4a1bb2c6"></a>
<a id="agroup__subsys__pm__device_html_ga74fde62f71393fb9863916b3a2e5c460"></a>
<a id="agroup__subsys__pm__device_html_ga765a5412f66070ccefd8e80ed9f62b1b"></a>
<a id="agroup__subsys__pm__device_html_ga7ea002352f3d1c90aecff1d54c255a06"></a>
<a id="agroup__subsys__pm__device_html_ga81d4ee32f5bbb1b343234b9b3afc0179"></a>
<a id="agroup__subsys__pm__device_html_ga8b527314f0c61b85602876b4f5a52275"></a>
<a id="agroup__subsys__pm__device_html_ga8ff7c3197d5ded860878302d00ac709c"></a>
<a id="agroup__subsys__pm__device_html_ga9cfb6437873089714635d2b26aafefac"></a>
<a id="agroup__subsys__pm__device_html_ga9e926dffd7eafc567499ce1ea537486b"></a>
<a id="agroup__subsys__pm__device_html_gaa10a3f1ce71409cb591db416a1611377"></a>
<a id="agroup__subsys__pm__device_html_gac818aafb748b57d70909808b45d89379"></a>
<a id="agroup__subsys__pm__device_html_gad109511e4314fa6145ee97dd655ec7bb"></a>
<a id="agroup__subsys__pm__device_html_gad563094c2d4ad066bc4ce30586e13fb3"></a>
<a id="agroup__subsys__pm__device_html_gadf145eb83c32eac741ab08fb7b262a55"></a>
<a id="agroup__subsys__pm__device_html_gae59a1fbcd2399717076fbfcee1e5e411"></a>
<a id="agroup__subsys__pm__device_html_gaee5546eacb9be7caa9d59ab63926cc4c"></a>
<a id="agroup__subsys__pm__device_html_gafb12ecf4679dd449e2faad0ede2c75fd"></a>
<a id="agroup__subsys__pm__device_html_gaffcf0aea5df10657235d4ed1f8c74d5a"></a>
<a id="agroup__subsys__pm__device_html_gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5"></a>
<a id="agroup__subsys__pm__device_html_gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2"></a>
<a id="agroup__subsys__pm__device_html_gga561c0789071e3c3963f21f4c4a1bb2c6a51a5904aff980deff73d29568b6f7deb"></a>
<a id="agroup__subsys__pm__device_html_gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7"></a>
<a id="agroup__subsys__pm__device_html_ggaee5546eacb9be7caa9d59ab63926cc4ca2bcd7dee3a85b27157bbc465bacf521e"></a>
<a id="agroup__subsys__pm__device_html_ggaee5546eacb9be7caa9d59ab63926cc4ca5b7ae11deaee85eb0b8452bc89383790"></a>
<a id="agroup__subsys__pm__device_html_ggaee5546eacb9be7caa9d59ab63926cc4ca757c6ab81eeac0d6afae479d6a0ac564"></a>
<a id="agroup__subsys__pm__device_html_ggaee5546eacb9be7caa9d59ab63926cc4cac7690e0ffd27742acf58fdbdb7b89544"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="akernel_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a05ebf64a113d562fb9328ea62cfa8f99"></a>
<a id="astructk__event_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__spinlock_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructpm__device__base_html"></a>
<a id="astructpm__device__base_html_a4a9eeb093de1b1e60222b25a06a6361d"></a>
<a id="astructpm__device__base_html_abd3a07f0e7c54cb0bee7f835be79dac6"></a>
<a id="astructpm__device__base_html_af4c9ef16800538148dcfa1d93b69bccb"></a>
<a id="astructpm__device__base_html_af9a24c7aaa0425b335fe147908c1fd4d"></a>
<a id="astructpm__device__isr_html"></a>
<a id="astructpm__device__isr_html_a24d7dd68bb57794be25450389fc95b33"></a>
<a id="astructpm__device__isr_html_ad501eabcd3370e9edb6b0851928fd7ac"></a>
<a id="astructpm__device_html"></a>
<a id="astructpm__device_html_a5dc3b48b3139d546206c8b9cacaf09fd"></a>
<a id="astructpm__device_html_aa8ed27c6c0cff89062922bedae4dca35"></a>
<a id="astructpm__device_html_ab7e54f9195359f60cc0a4b06677df0c7"></a>
<a id="astructpm__device_html_aec09c5708cda21c6e3af2a4e7082b432"></a>
<a id="astructpm__device_html_afb5db0142ebab7891a42f71b59fd55cb"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2015 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_PM_DEVICE_H_
#define ZEPHYR_INCLUDE_PM_DEVICE_H_

#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif



struct device;

enum pm_device_flag {
        PM_DEVICE_FLAG_BUSY,
        PM_DEVICE_FLAG_TURN_ON_FAILED,
        PM_DEVICE_FLAG_PD_CLAIMED,
        PM_DEVICE_FLAG_WS_CAPABLE,
        PM_DEVICE_FLAG_WS_ENABLED,
        PM_DEVICE_FLAG_RUNTIME_ENABLED,
        PM_DEVICE_FLAG_PD,
        PM_DEVICE_FLAG_RUNTIME_AUTO,
        PM_DEVICE_FLAG_ISR_SAFE,
        PM_DEVICE_FLAG_PD_SUSPENDED,
};


#define PM_DEVICE_ISR_SAFE 1

enum pm_device_state {
        PM_DEVICE_STATE_ACTIVE,
        PM_DEVICE_STATE_SUSPENDED,
        PM_DEVICE_STATE_SUSPENDING,
        PM_DEVICE_STATE_OFF
};

enum pm_device_action {
        PM_DEVICE_ACTION_SUSPEND,
        PM_DEVICE_ACTION_RESUME,
        PM_DEVICE_ACTION_TURN_OFF,
        PM_DEVICE_ACTION_TURN_ON,
};

typedef int (*pm_device_action_cb_t)(const struct device *dev,
                                     enum pm_device_action action);

typedef bool (*pm_device_action_failed_cb_t)(const struct device *dev,
                                         int err);

struct pm_device_base {
        atomic_t flags;
        enum pm_device_state state;
        pm_device_action_cb_t action_cb;
#if defined(CONFIG_PM_DEVICE_RUNTIME) || defined(__DOXYGEN__)
        uint32_t usage;
#endif /* CONFIG_PM_DEVICE_RUNTIME */
#ifdef CONFIG_PM_DEVICE_POWER_DOMAIN
        const struct device *domain;
#endif /* CONFIG_PM_DEVICE_POWER_DOMAIN */
};

struct pm_device {
        struct pm_device_base base;
#if defined(CONFIG_PM_DEVICE_RUNTIME) || defined(__DOXYGEN__)
        const struct device *dev;
        struct k_sem lock;
#if defined(CONFIG_PM_DEVICE_RUNTIME_ASYNC) || defined(__DOXYGEN__)
        struct k_event event;
        struct k_work_delayable work;
#endif /* CONFIG_PM_DEVICE_RUNTIME_ASYNC */
#endif /* CONFIG_PM_DEVICE_RUNTIME */
};

struct pm_device_isr {
        struct pm_device_base base;
#if defined(CONFIG_PM_DEVICE_RUNTIME) || defined(__DOXYGEN__)
        struct k_spinlock lock;
#endif
};

/* Base part must be the first element. */
BUILD_ASSERT(offsetof(struct pm_device, base) == 0);
BUILD_ASSERT(offsetof(struct pm_device_isr, base) == 0);


#ifdef CONFIG_PM_DEVICE_RUNTIME_ASYNC
#define Z_PM_DEVICE_RUNTIME_INIT(obj)                   \
        .lock = Z_SEM_INITIALIZER(obj.lock, 1, 1),      \
        .event = Z_EVENT_INITIALIZER(obj.event),
#elif CONFIG_PM_DEVICE_RUNTIME
#define Z_PM_DEVICE_RUNTIME_INIT(obj)                   \
        .lock = Z_SEM_INITIALIZER(obj.lock, 1, 1),
#else
#define Z_PM_DEVICE_RUNTIME_INIT(obj)
#endif /* CONFIG_PM_DEVICE_RUNTIME */

#ifdef CONFIG_PM_DEVICE_POWER_DOMAIN
#define Z_PM_DEVICE_POWER_DOMAIN_INIT(_node_id)                 \
        .domain = DEVICE_DT_GET_OR_NULL(DT_PHANDLE(_node_id,    \
                                   power_domains)),
#else
#define Z_PM_DEVICE_POWER_DOMAIN_INIT(obj)
#endif /* CONFIG_PM_DEVICE_POWER_DOMAIN */

#define Z_PM_DEVICE_FLAGS(node_id)                                       \
        (COND_CODE_1(                                                    \
                 DT_NODE_EXISTS(node_id),                                \
                 ((DT_PROP_OR(node_id, wakeup_source, 0)                 \
                         << PM_DEVICE_FLAG_WS_CAPABLE) |                 \
                  (DT_PROP_OR(node_id, zephyr_pm_device_runtime_auto, 0) \
                         << PM_DEVICE_FLAG_RUNTIME_AUTO) |               \
                  (DT_NODE_HAS_COMPAT(node_id, power_domain) <<          \
                         PM_DEVICE_FLAG_PD)),                            \
                 (0)))

#define Z_PM_DEVICE_BASE_INIT(obj, node_id, pm_action_cb, _flags)            \
        {                                                                    \
                .flags = ATOMIC_INIT(Z_PM_DEVICE_FLAGS(node_id) | (_flags)), \
                .state = PM_DEVICE_STATE_ACTIVE,                             \
                .action_cb = pm_action_cb,                                   \
                Z_PM_DEVICE_POWER_DOMAIN_INIT(node_id)                       \
        }

#define Z_PM_DEVICE_INIT(obj, node_id, pm_action_cb, isr_safe)                  \
        {                                                                       \
                .base = Z_PM_DEVICE_BASE_INIT(obj, node_id, pm_action_cb,       \
                                isr_safe ? BIT(PM_DEVICE_FLAG_ISR_SAFE) : 0),   \
                COND_CODE_1(isr_safe, (), (Z_PM_DEVICE_RUNTIME_INIT(obj)))      \
        }

#define Z_PM_DEVICE_NAME(dev_id) _CONCAT(__pm_device_, dev_id)

#ifdef CONFIG_PM
#define Z_PM_DEVICE_DEFINE_SLOT(dev_id)                                 \
        static STRUCT_SECTION_ITERABLE_ALTERNATE(pm_device_slots, device, \
                        _CONCAT(__pm_slot_, dev_id))
#else
#define Z_PM_DEVICE_DEFINE_SLOT(dev_id)
#endif /* CONFIG_PM */

#ifdef CONFIG_PM_DEVICE
#define Z_PM_DEVICE_DEFINE(node_id, dev_id, pm_action_cb, isr_safe)             \
        Z_PM_DEVICE_DEFINE_SLOT(dev_id);                                        \
        static struct COND_CODE_1(isr_safe, (pm_device_isr), (pm_device))       \
                Z_PM_DEVICE_NAME(dev_id) =                                      \
                Z_PM_DEVICE_INIT(Z_PM_DEVICE_NAME(dev_id), node_id,             \
                                 pm_action_cb, isr_safe)

#define Z_PM_DEVICE_GET(dev_id) ((struct pm_device_base *)&Z_PM_DEVICE_NAME(dev_id))

#else
#define Z_PM_DEVICE_DEFINE(node_id, dev_id, pm_action_cb, isr_safe)
#define Z_PM_DEVICE_GET(dev_id) NULL
#endif /* CONFIG_PM_DEVICE */


#define PM_DEVICE_DEFINE(dev_id, pm_action_cb, ...)                     \
        Z_PM_DEVICE_DEFINE(DT_INVALID_NODE, dev_id, pm_action_cb,       \
                        COND_CODE_1(IS_EMPTY(__VA_ARGS__), (0), (__VA_ARGS__)))

#define PM_DEVICE_DT_DEFINE(node_id, pm_action_cb, ...) \
        Z_PM_DEVICE_DEFINE(node_id, Z_DEVICE_DT_DEV_ID(node_id), pm_action_cb, \
                        COND_CODE_1(IS_EMPTY(__VA_ARGS__), (0), (__VA_ARGS__)))

#define PM_DEVICE_DT_INST_DEFINE(idx, pm_action_cb, ...)                \
        Z_PM_DEVICE_DEFINE(DT_DRV_INST(idx),                            \
                           Z_DEVICE_DT_DEV_ID(DT_DRV_INST(idx)),        \
                           pm_action_cb,                                \
                           COND_CODE_1(IS_EMPTY(__VA_ARGS__), (0), (__VA_ARGS__)))

#define PM_DEVICE_GET(dev_id) \
        Z_PM_DEVICE_GET(dev_id)

#define PM_DEVICE_DT_GET(node_id) \
        PM_DEVICE_GET(Z_DEVICE_DT_DEV_ID(node_id))

#define PM_DEVICE_DT_INST_GET(idx) \
        PM_DEVICE_DT_GET(DT_DRV_INST(idx))

const char *pm_device_state_str(enum pm_device_state state);

int pm_device_action_run(const struct device *dev,
                enum pm_device_action action);

void pm_device_children_action_run(const struct device *dev,
                enum pm_device_action action,
                pm_device_action_failed_cb_t failure_cb);

#if defined(CONFIG_PM_DEVICE) || defined(__DOXYGEN__)
int pm_device_state_get(const struct device *dev,
                        enum pm_device_state *state);

static inline void pm_device_init_suspended(const struct device *dev)
{
        struct pm_device_base *pm = dev->pm_base;

        pm->state = PM_DEVICE_STATE_SUSPENDED;
}

static inline void pm_device_init_off(const struct device *dev)
{
        struct pm_device_base *pm = dev->pm_base;

        pm->state = PM_DEVICE_STATE_OFF;
}

void pm_device_busy_set(const struct device *dev);

void pm_device_busy_clear(const struct device *dev);

bool pm_device_is_any_busy(void);

bool pm_device_is_busy(const struct device *dev);

bool pm_device_wakeup_enable(const struct device *dev, bool enable);

bool pm_device_wakeup_is_enabled(const struct device *dev);

bool pm_device_wakeup_is_capable(const struct device *dev);

bool pm_device_on_power_domain(const struct device *dev);

int pm_device_power_domain_add(const struct device *dev,
                               const struct device *domain);

int pm_device_power_domain_remove(const struct device *dev,
                                  const struct device *domain);

bool pm_device_is_powered(const struct device *dev);

int pm_device_driver_init(const struct device *dev, pm_device_action_cb_t action_cb);

int pm_device_driver_deinit(const struct device *dev, pm_device_action_cb_t action_cb);
#else
static inline int pm_device_state_get(const struct device *dev,
                                      enum pm_device_state *state)
{
        ARG_UNUSED(dev);

        *state = PM_DEVICE_STATE_ACTIVE;

        return 0;
}

static inline void pm_device_init_suspended(const struct device *dev)
{
        ARG_UNUSED(dev);
}
static inline void pm_device_init_off(const struct device *dev)
{
        ARG_UNUSED(dev);
}
static inline void pm_device_busy_set(const struct device *dev)
{
        ARG_UNUSED(dev);
}
static inline void pm_device_busy_clear(const struct device *dev)
{
        ARG_UNUSED(dev);
}
static inline bool pm_device_is_any_busy(void) { return false; }
static inline bool pm_device_is_busy(const struct device *dev)
{
        ARG_UNUSED(dev);
        return false;
}
static inline bool pm_device_wakeup_enable(const struct device *dev,
                                           bool enable)
{
        ARG_UNUSED(dev);
        ARG_UNUSED(enable);
        return false;
}
static inline bool pm_device_wakeup_is_enabled(const struct device *dev)
{
        ARG_UNUSED(dev);
        return false;
}
static inline bool pm_device_wakeup_is_capable(const struct device *dev)
{
        ARG_UNUSED(dev);
        return false;
}
static inline bool pm_device_on_power_domain(const struct device *dev)
{
        ARG_UNUSED(dev);
        return false;
}

static inline int pm_device_power_domain_add(const struct device *dev,
                                             const struct device *domain)
{
        ARG_UNUSED(dev);
        ARG_UNUSED(domain);
        return -ENOSYS;
}

static inline int pm_device_power_domain_remove(const struct device *dev,
                                                const struct device *domain)
{
        ARG_UNUSED(dev);
        ARG_UNUSED(domain);
        return -ENOSYS;
}

static inline bool pm_device_is_powered(const struct device *dev)
{
        ARG_UNUSED(dev);
        return true;
}

static inline int pm_device_driver_init(const struct device *dev, pm_device_action_cb_t action_cb)
{
        int rc;

        /* When power management is not enabled, all drivers should initialise to active state */
        rc = action_cb(dev, PM_DEVICE_ACTION_TURN_ON);
        if ((rc < 0) && (rc != -ENOTSUP)) {
                return rc;
        }

        rc = action_cb(dev, PM_DEVICE_ACTION_RESUME);
        if (rc < 0) {
                return rc;
        }

        return 0;
}

static inline int pm_device_driver_deinit(const struct device *dev, pm_device_action_cb_t action_cb)
{
        return action_cb(dev, PM_DEVICE_ACTION_SUSPEND);
}

#endif /* CONFIG_PM_DEVICE */


#ifdef __cplusplus
}
#endif

#endif
```

## 71.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2015 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 223 行

条件编译配置（Configuration）标记：`CONFIG_PM_DEVICE_RUNTIME`。

### 注释 3：原第 227 行

条件编译配置（Configuration）标记：`CONFIG_PM_DEVICE_POWER_DOMAIN`。

### 注释 4：原第 250 行

条件编译配置（Configuration）标记：`CONFIG_PM_DEVICE_RUNTIME_ASYNC`。

### 注释 5：原第 251 行

条件编译配置（Configuration）标记：`CONFIG_PM_DEVICE_RUNTIME`。

### 注释 6：原第 270 行

基础部分（Base part）必须是第一个元素。

### 注释 7：原第 285 行

条件编译配置（Configuration）标记：`CONFIG_PM_DEVICE_RUNTIME`。

### 注释 8：原第 293 行

条件编译配置（Configuration）标记：`CONFIG_PM_DEVICE_POWER_DOMAIN`。

### 注释 9：原第 371 行

条件编译配置（Configuration）标记：`CONFIG_PM`。

### 注释 10：原第 398 行

条件编译配置（Configuration）标记：`CONFIG_PM_DEVICE`。

### 注释 11：原第 825 行

未启用电源管理时，所有驱动都应初始化为活动状态（Active state）。

### 注释 12：原第 844 行

条件编译配置（Configuration）标记：`CONFIG_PM_DEVICE`。

## 71.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P069_设备电源管理头文件.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [pm_device_state](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga561c0789071e3c3963f21f4c4a1bb2c6)
- [PM_DEVICE_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7)
- [PM_DEVICE_STATE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5)
- [PM_DEVICE_STATE_SUSPENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gga561c0789071e3c3963f21f4c4a1bb2c6a51a5904aff980deff73d29568b6f7deb)
- [PM_DEVICE_STATE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2)
- [pm_device_action](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gaee5546eacb9be7caa9d59ab63926cc4c)
- [PM_DEVICE_ACTION_SUSPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ggaee5546eacb9be7caa9d59ab63926cc4ca5b7ae11deaee85eb0b8452bc89383790)
- [PM_DEVICE_ACTION_RESUME](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ggaee5546eacb9be7caa9d59ab63926cc4ca757c6ab81eeac0d6afae479d6a0ac564)
- [PM_DEVICE_ACTION_TURN_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ggaee5546eacb9be7caa9d59ab63926cc4ca2bcd7dee3a85b27157bbc465bacf521e)
- [PM_DEVICE_ACTION_TURN_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ggaee5546eacb9be7caa9d59ab63926cc4cac7690e0ffd27742acf58fdbdb7b89544)
- [pm_device_action_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga81d4ee32f5bbb1b343234b9b3afc0179)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [pm_device_action_failed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga9cfb6437873089714635d2b26aafefac)
- [pm_device_base](../power/P038_设备电源管理基础结构.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__base.html#af9a24c7aaa0425b335fe147908c1fd4d)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__base.html#af4c9ef16800538148dcfa1d93b69bccb)
- [action_cb](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__base.html#abd3a07f0e7c54cb0bee7f835be79dac6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [usage](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__base.html#a4a9eeb093de1b1e60222b25a06a6361d)
- [pm_device](../power/P039_通用设备运行时电源结构.md)
- [base](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#afb5db0142ebab7891a42f71b59fd55cb)
- [dev](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#aec09c5708cda21c6e3af2a4e7082b432)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [lock](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#ab7e54f9195359f60cc0a4b06677df0c7)
- [k_event](../eventpoll_reference/P002_内核事件结构.md)
- [event](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#aa8ed27c6c0cff89062922bedae4dca35)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [work](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#a5dc3b48b3139d546206c8b9cacaf09fd)
- [pm_device_isr](../power/P040_中断安全设备电源结构.md)
- [base](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__isr.html#ad501eabcd3370e9edb6b0851928fd7ac)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [lock](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__isr.html#a24d7dd68bb57794be25450389fc95b33)
- [pm_device_state_str](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gad109511e4314fa6145ee97dd655ec7bb)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [pm_device_action_run](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga3840d6e7832a00b93763247a5951bfde)
- [pm_device_children_action_run](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga765a5412f66070ccefd8e80ed9f62b1b)
- [pm_device_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gaffcf0aea5df10657235d4ed1f8c74d5a)
- [pm_device_init_suspended](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga4c366f49e326a8b8e01d90cb2ee424ba)
- [pm_base](../device_reference/P002_设备对象结构.md#a05ebf64a113d562fb9328ea62cfa8f99)
- [pm_device_init_off](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gafb12ecf4679dd449e2faad0ede2c75fd)
- [pm_device_busy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga7ea002352f3d1c90aecff1d54c255a06)
- [pm_device_busy_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga8b527314f0c61b85602876b4f5a52275)
- [pm_device_is_any_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gae59a1fbcd2399717076fbfcee1e5e411)
- [pm_device_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga8ff7c3197d5ded860878302d00ac709c)
- [pm_device_wakeup_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga74fde62f71393fb9863916b3a2e5c460)
- [pm_device_wakeup_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga0716c6158804ac48022280d8d237f8c1)
- [pm_device_wakeup_is_capable](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gac818aafb748b57d70909808b45d89379)
- [pm_device_on_power_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga32eb5e210d2f0ba533b0185a94c8744e)
- [pm_device_power_domain_add](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gaa10a3f1ce71409cb591db416a1611377)
- [pm_device_power_domain_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga1d7ab9b0b497e016b9b22d2506cd23f9)
- [pm_device_is_powered](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga9e926dffd7eafc567499ce1ea537486b)
- [pm_device_driver_init](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gad563094c2d4ad066bc4ce30586e13fb3)
- [pm_device_driver_deinit](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gadf145eb83c32eac741ab08fb7b262a55)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::pm_base](../device_reference/P002_设备对象结构.md#a05ebf64a113d562fb9328ea62cfa8f99)
- [pm_device_base::usage](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__base.html#a4a9eeb093de1b1e60222b25a06a6361d)
- [pm_device_base::action_cb](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__base.html#abd3a07f0e7c54cb0bee7f835be79dac6)
- [pm_device_base::state](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__base.html#af4c9ef16800538148dcfa1d93b69bccb)
- [pm_device_base::flags](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__base.html#af9a24c7aaa0425b335fe147908c1fd4d)
- [pm_device_isr::lock](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__isr.html#a24d7dd68bb57794be25450389fc95b33)
- [pm_device_isr::base](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device__isr.html#ad501eabcd3370e9edb6b0851928fd7ac)
- [pm_device::work](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#a5dc3b48b3139d546206c8b9cacaf09fd)
- [pm_device::event](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#aa8ed27c6c0cff89062922bedae4dca35)
- [pm_device::lock](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#ab7e54f9195359f60cc0a4b06677df0c7)
- [pm_device::dev](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#aec09c5708cda21c6e3af2a4e7082b432)
- [pm_device::base](https://docs.zephyrproject.org/latest/doxygen/html/structpm__device.html#afb5db0142ebab7891a42f71b59fd55cb)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P070_pinctrl_soc_bflb_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P072_pulse_io.h_源码浏览.md)
