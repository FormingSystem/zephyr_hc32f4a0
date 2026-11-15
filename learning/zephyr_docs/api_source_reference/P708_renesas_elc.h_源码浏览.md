---
id: learning.zephyr-docs.api-source-reference.page-708
title: renesas_elc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__elc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第708章\_renesas\_elc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__elc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__elc_8h.html)。

## 708.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00154"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00165"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="foldopen00178"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="foldopen00193"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="foldopen00206"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="foldopen00217"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="foldopen00230"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="foldopen00243"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00265"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="foldopen00293"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="foldopen00306"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="foldopen00317"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="foldopen00330"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="foldopen00343"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00364"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__renesas__elc__interface_html_ga444e17d01310283e61bcde9a1022c47a"></a>
<a id="agroup__renesas__elc__interface_html_ga65c950ccf0087c514daf6d543a0a7ecf"></a>
<a id="agroup__renesas__elc__interface_html_gaac75089657f841c80225aa40de9c2a93"></a>
<a id="agroup__renesas__elc__interface_html_gab3b55b83b38469854aae726a71f6ad55"></a>
<a id="agroup__renesas__elc__interface_html_gafbffc029fd9482be578bd05cbdb3a03f"></a>
<a id="akernel_8h_html"></a>
<a id="asignal_8h_html_a5d326f119f87d0facaa662520f8c322a"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructrenesas__elc__dt__spec_html"></a>
<a id="astructrenesas__elc__dt__spec_html_a7b20982a91e3bb944c7aaf94b6fd33dd"></a>
<a id="astructrenesas__elc__dt__spec_html_a9004b468890e2901b4316e9f2fa648ea"></a>
<a id="astructrenesas__elc__dt__spec_html_ae759c1c19bd7c69d14165a12331f3df4"></a>
<a id="asyscall__handler_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_INTERCONN_RENESAS_ELC_RENESAS_ELC_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_INTERCONN_RENESAS_ELC_RENESAS_ELC_H_


#include <stdint.h>
#include <zephyr/sys/slist.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/internal/syscall_handler.h>

#ifdef __cplusplus
extern "C" {
#endif

struct renesas_elc_dt_spec {
        const struct device *dev;
        uint32_t peripheral;
        uint32_t event;
};

#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME(node_id, name)                                      \
        DEVICE_DT_GET(DT_PHANDLE_BY_NAME(node_id, renesas_elcs, name))

#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX(node_id, idx)                                        \
        DEVICE_DT_GET(DT_PHANDLE_BY_IDX(node_id, renesas_elcs, idx))

#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_NAME_OR_NULL(node_id, name)                              \
        DEVICE_DT_GET_OR_NULL(DT_PHANDLE_BY_NAME(node_id, renesas_elcs, name))

#define RENESAS_ELC_DT_SPEC_DEVICE_GET_BY_IDX_OR_NULL(node_id, idx)                                \
        DEVICE_DT_GET_OR_NULL(DT_PHANDLE_BY_IDX(node_id, renesas_elcs, idx))

#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME(inst, name)                                    \
        DEVICE_DT_GET(DT_PHANDLE_BY_NAME(DT_DRV_INST(inst), renesas_elcs, name))

#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX(inst, idx)                                      \
        DEVICE_DT_GET(DT_PHANDLE_BY_IDX(DT_DRV_INST(inst), renesas_elcs, idx))

#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_NAME_OR_NULL(inst, name)                            \
        DEVICE_DT_GET_OR_NULL(DT_PHANDLE_BY_NAME(DT_DRV_INST(inst), renesas_elcs, name))

#define RENESAS_ELC_DT_SPEC_DEVICE_INST_GET_BY_IDX_OR_NULL(inst, idx)                              \
        DEVICE_DT_GET_OR_NULL(DT_PHANDLE_BY_IDX(DT_DRV_INST(inst), renesas_elcs, idx))

#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME(node_id, name)                                  \
        DT_PHA_BY_NAME(node_id, renesas_elcs, name, peripheral)

#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX(node_id, idx)                                    \
        DT_PHA_BY_IDX(node_id, renesas_elcs, idx, peripheral)

#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR(node_id, name, default_value)                \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, renesas_elcs),                                       \
                (RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME(node_id, name)),                       \
                (default_value))

#define RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR(node_id, idx, default_value)                  \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, renesas_elcs),                                       \
                (RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX(node_id, idx)),                         \
                (default_value))

#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME(inst, name)                                \
        RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME(DT_DRV_INST(inst), name)

#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX(inst, idx)                                  \
        RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX(DT_DRV_INST(inst), idx)

#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_NAME_OR(inst, name, default_value)              \
        RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)

#define RENESAS_ELC_DT_SPEC_PERIPHERAL_INST_GET_BY_IDX_OR(inst, idx, default_value)                \
        RENESAS_ELC_DT_SPEC_PERIPHERAL_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)

#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME(node_id, name)                                       \
        DT_PHA_BY_NAME(node_id, renesas_elcs, name, event)

#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX(node_id, idx)                                         \
        DT_PHA_BY_IDX(node_id, renesas_elcs, idx, event)

#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR(node_id, name, default_value)                     \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, renesas_elcs),                                       \
                (RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME(node_id, name)),                            \
                (default_value))

#define RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR(node_id, idx, default_value)                       \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, renesas_elcs),                                       \
                (RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX(node_id, idx)),                              \
                (default_value))

#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME(inst, name)                                     \
        RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME(DT_DRV_INST(inst), name)

#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX(inst, idx)                                       \
        RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX(DT_DRV_INST(inst), idx)

#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_NAME_OR(inst, name, default_value)                   \
        RENESAS_ELC_DT_SPEC_EVENT_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)

#define RENESAS_ELC_DT_SPEC_EVENT_INST_GET_BY_IDX_OR(inst, idx, default_value)                     \
        RENESAS_ELC_DT_SPEC_EVENT_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)

__subsystem struct renesas_elc_driver_api {
        int (*software_event_generate)(const struct device *dev, uint32_t event);
        int (*link_set)(const struct device *dev, uint32_t peripheral, uint32_t signal);
        int (*link_break)(const struct device *dev, uint32_t peripheral);
        int (*enable)(const struct device *dev);
        int (*disable)(const struct device *dev);
};


__syscall int renesas_elc_software_event_generate(const struct device *dev, uint32_t event);

static inline int z_impl_renesas_elc_software_event_generate(const struct device *dev,
                                                             uint32_t event)
{
        return DEVICE_API_GET(renesas_elc, dev)->software_event_generate(dev, event);
}

__syscall int renesas_elc_link_set(const struct device *dev, uint32_t peripheral, uint32_t event);

static inline int z_impl_renesas_elc_link_set(const struct device *dev, uint32_t peripheral,
                                              uint32_t event)
{
        return DEVICE_API_GET(renesas_elc, dev)->link_set(dev, peripheral, event);
}

__syscall int renesas_elc_link_break(const struct device *dev, uint32_t peripheral);

static inline int z_impl_renesas_elc_link_break(const struct device *dev, uint32_t peripheral)
{
        return DEVICE_API_GET(renesas_elc, dev)->link_break(dev, peripheral);
}

__syscall int renesas_elc_enable(const struct device *dev);

static inline int z_impl_renesas_elc_enable(const struct device *dev)
{
        return DEVICE_API_GET(renesas_elc, dev)->enable(dev);
}

__syscall int renesas_elc_disable(const struct device *dev);

static inline int z_impl_renesas_elc_disable(const struct device *dev)
{
        return DEVICE_API_GET(renesas_elc, dev)->disable(dev);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/renesas_elc.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_INTERCONN_RENESAS_ELC_RENESAS_ELC_H_ */
```

## 708.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 468 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_INTERCONN_RENESAS_ELC_RENESAS_ELC_H_`。

## 708.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__elc_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/internal/syscall_handler.h](../syscall_boot_reference/P004_系统调用处理头文件参考.md)
- [renesas_elc_dt_spec](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md#ae759c1c19bd7c69d14165a12331f3df4)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [peripheral](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md#a7b20982a91e3bb944c7aaf94b6fd33dd)
- [event](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md#a9004b468890e2901b4316e9f2fa648ea)
- [signal](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#a5d326f119f87d0facaa662520f8c322a)
- [renesas_elc_software_event_generate](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gab3b55b83b38469854aae726a71f6ad55)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [renesas_elc_link_set](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga444e17d01310283e61bcde9a1022c47a)
- [renesas_elc_link_break](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#ga65c950ccf0087c514daf6d543a0a7ecf)
- [renesas_elc_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gafbffc029fd9482be578bd05cbdb3a03f)
- [renesas_elc_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__elc__interface.html#gaac75089657f841c80225aa40de9c2a93)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [renesas_elc_dt_spec::peripheral](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md#a7b20982a91e3bb944c7aaf94b6fd33dd)
- [renesas_elc_dt_spec::event](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md#a9004b468890e2901b4316e9f2fa648ea)
- [renesas_elc_dt_spec::dev](../device_power_control_model_reference/P073_renesas_elc_dt_spec_结构体.md#ae759c1c19bd7c69d14165a12331f3df4)
- [syscall_handler.h](../syscall_boot_reference/P004_系统调用处理头文件参考.md)

---

[上一章](P707_renesas,ra-sdram.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P709_renesas_ra_external_interrupt.h_源码浏览.md)
