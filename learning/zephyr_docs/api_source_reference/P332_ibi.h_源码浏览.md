---
id: learning.zephyr-docs.api-source-reference.page-332
title: ibi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ibi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第332章\_ibi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ibi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ibi_8h.html)。

## 332.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__i3c__ibi_html_ga4c6f4516e55d0ab6c539fb800d7ec45a"></a>
<a id="agroup__i3c__ibi_html_ga7bbbff351dc33d1c00abf6c22bbd50d4"></a>
<a id="agroup__i3c__ibi_html_ga7fbf838ea07516849dc1296d48af65d1"></a>
<a id="agroup__i3c__ibi_html_ga814cf622b240808216ce4e87802e965c"></a>
<a id="agroup__i3c__ibi_html_gaafc2fdf9f2402691c3ebe11d06106840"></a>
<a id="agroup__i3c__ibi_html_gab135cb893efd50c7db16c1734b6a0bab"></a>
<a id="agroup__i3c__ibi_html_gad643c7f0512e1e6dcddbe5821e70fc0d"></a>
<a id="agroup__i3c__ibi_html_gaf4be72fc9c862d996d860c0b7fbc862b"></a>
<a id="agroup__i3c__ibi_html_ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815"></a>
<a id="agroup__i3c__ibi_html_ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d"></a>
<a id="agroup__i3c__ibi_html_ggaf4be72fc9c862d996d860c0b7fbc862ba39d8f6a9b69d092eabf9ca9726deec8c"></a>
<a id="agroup__i3c__ibi_html_ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f"></a>
<a id="agroup__i3c__ibi_html_ggaf4be72fc9c862d996d860c0b7fbc862baab12781f76c743cec6b72ffa7d8c27ee"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__workqueue__apis_html_ga5add9ef0dce306a08413c4140fc0bdda"></a>
<a id="akernel_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructi3c__device__desc_html"></a>
<a id="astructi3c__ibi__payload_html"></a>
<a id="astructi3c__ibi__payload_html_aad4208fcdfef0bc9fb67c86ee1d302de"></a>
<a id="astructi3c__ibi__payload_html_ab869cf38c7a9677fda3ecf48cd358355"></a>
<a id="astructi3c__ibi__work_html"></a>
<a id="astructi3c__ibi__work_html_a08531106055235eaf85cb8fae690235c"></a>
<a id="astructi3c__ibi__work_html_a195e49bd7db79d0f1f45803e42e963ca"></a>
<a id="astructi3c__ibi__work_html_a3ec8e089facfbb187342e9bf9a525e50"></a>
<a id="astructi3c__ibi__work_html_a4a0373423ababe549d00ee13fe657315"></a>
<a id="astructi3c__ibi__work_html_a66ece8f194350c94f8991eaf1ee5bc0b"></a>
<a id="astructi3c__ibi__work_html_a6a3dfd49762d96b591b5e248f9ce1668"></a>
<a id="astructi3c__ibi__work_html_a6c75e0b678fee04f3357c2c1aa9e7376"></a>
<a id="astructi3c__ibi_html"></a>
<a id="astructi3c__ibi_html_a584e3298059e412d7d3671a451ecc117"></a>
<a id="astructi3c__ibi_html_a88b0ccd636c042ca929412c42a05bc25"></a>
<a id="astructi3c__ibi_html_aa51b8214d4a0708861ac9617f844043f"></a>
<a id="astructk__work_html"></a>

```c
/*
 * Copyright 2022 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_I3C_IBI_H_
#define ZEPHYR_INCLUDE_DRIVERS_I3C_IBI_H_


#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/slist.h>

#ifndef CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE
#define CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE 0
#endif

#ifdef __cplusplus
extern "C" {
#endif

struct i3c_device_desc;

enum i3c_ibi_type {
        I3C_IBI_TARGET_INTR,

        I3C_IBI_CONTROLLER_ROLE_REQUEST,

        I3C_IBI_HOTJOIN,

        I3C_IBI_TYPE_MAX = I3C_IBI_HOTJOIN,

        I3C_IBI_WORKQUEUE_CB,
};

struct i3c_ibi {
        enum i3c_ibi_type       ibi_type;

        uint8_t                 *payload;

        uint8_t                 payload_len;
};

struct i3c_ibi_payload {
        uint8_t payload_len;

        uint8_t payload[CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE];
};

struct i3c_ibi_work {
        sys_snode_t node;

        struct k_work work;

        enum i3c_ibi_type type;

        union {
                const struct device *controller;

                struct i3c_device_desc *target;
        };

        union {
                struct i3c_ibi_payload payload;

                k_work_handler_t work_cb;
        };
};

typedef int (*i3c_target_ibi_cb_t)(struct i3c_device_desc *target,
                                   struct i3c_ibi_payload *payload);


int i3c_ibi_work_enqueue(struct i3c_ibi_work *ibi_work);

int i3c_ibi_work_enqueue_target_irq(struct i3c_device_desc *target,
                                    uint8_t *payload, size_t payload_len);

int i3c_ibi_work_enqueue_controller_request(struct i3c_device_desc *target);

int i3c_ibi_work_enqueue_hotjoin(const struct device *dev);

int i3c_ibi_work_enqueue_cb(const struct device *dev,
                            k_work_handler_t work_cb);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_I3C_IBI_H_ */
```

## 332.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 242 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I3C_IBI_H_`。

## 332.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ibi_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [i3c_ibi_type](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gaf4be72fc9c862d996d860c0b7fbc862b)
- [I3C_IBI_TARGET_INTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d)
- [I3C_IBI_CONTROLLER_ROLE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815)
- [I3C_IBI_HOTJOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f)
- [I3C_IBI_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862baab12781f76c743cec6b72ffa7d8c27ee)
- [I3C_IBI_WORKQUEUE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba39d8f6a9b69d092eabf9ca9726deec8c)
- [i3c_ibi](../hardware/P397_I3C带内中断请求.md)
- [ibi_type](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi.html#a88b0ccd636c042ca929412c42a05bc25)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [payload](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi.html#a584e3298059e412d7d3671a451ecc117)
- [payload_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi.html#aa51b8214d4a0708861ac9617f844043f)
- [i3c_ibi_payload](../hardware/P398_I3C带内中断载荷.md)
- [payload_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__payload.html#aad4208fcdfef0bc9fb67c86ee1d302de)
- [payload](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__payload.html#ab869cf38c7a9677fda3ecf48cd358355)
- [CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga7bbbff351dc33d1c00abf6c22bbd50d4)
- [i3c_ibi_work](../hardware/P399_I3C带内中断工作项.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a66ece8f194350c94f8991eaf1ee5bc0b)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [work](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a4a0373423ababe549d00ee13fe657315)
- [type](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a3ec8e089facfbb187342e9bf9a525e50)
- [device](../device_reference/P002_设备对象结构.md)
- [controller](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a195e49bd7db79d0f1f45803e42e963ca)
- [target](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a6c75e0b678fee04f3357c2c1aa9e7376)
- [payload](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a08531106055235eaf85cb8fae690235c)
- [k_work_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5add9ef0dce306a08413c4140fc0bdda)
- [work_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a6a3dfd49762d96b591b5e248f9ce1668)
- [i3c_target_ibi_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga814cf622b240808216ce4e87802e965c)
- [i3c_ibi_work_enqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gaafc2fdf9f2402691c3ebe11d06106840)
- [i3c_ibi_work_enqueue_target_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga7fbf838ea07516849dc1296d48af65d1)
- [i3c_ibi_work_enqueue_controller_request](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gad643c7f0512e1e6dcddbe5821e70fc0d)
- [i3c_ibi_work_enqueue_hotjoin](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gab135cb893efd50c7db16c1734b6a0bab)
- [i3c_ibi_work_enqueue_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga4c6f4516e55d0ab6c539fb800d7ec45a)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [i3c_ibi_payload::payload_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__payload.html#aad4208fcdfef0bc9fb67c86ee1d302de)
- [i3c_ibi_payload::payload](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__payload.html#ab869cf38c7a9677fda3ecf48cd358355)
- [i3c_ibi_work::payload](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a08531106055235eaf85cb8fae690235c)
- [i3c_ibi_work::controller](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a195e49bd7db79d0f1f45803e42e963ca)
- [i3c_ibi_work::type](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a3ec8e089facfbb187342e9bf9a525e50)
- [i3c_ibi_work::work](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a4a0373423ababe549d00ee13fe657315)
- [i3c_ibi_work::node](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a66ece8f194350c94f8991eaf1ee5bc0b)
- [i3c_ibi_work::work_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a6a3dfd49762d96b591b5e248f9ce1668)
- [i3c_ibi_work::target](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi__work.html#a6c75e0b678fee04f3357c2c1aa9e7376)
- [i3c_ibi::payload](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi.html#a584e3298059e412d7d3671a451ecc117)
- [i3c_ibi::ibi_type](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi.html#a88b0ccd636c042ca929412c42a05bc25)
- [i3c_ibi::payload_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ibi.html#aa51b8214d4a0708861ac9617f844043f)

---

[上一章](P331_ias.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P333_icm42686.h_源码浏览.md)
