---
id: learning.zephyr-docs.api-source-reference.page-877
title: trickle.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/trickle_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第877章\_trickle.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/trickle_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/trickle_8h.html)。

## 877.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="agroup__trickle_html_ga6674fac118a187320d73dc742f0e216f"></a>
<a id="agroup__trickle_html_ga8477e45a95abccfb714e3f3369686c6d"></a>
<a id="agroup__trickle_html_ga95ceb01a7d56ce5a9d9128a42e1f8eb9"></a>
<a id="agroup__trickle_html_gac412d65ad2a8483920de32c1e0ae6be5"></a>
<a id="agroup__trickle_html_gacefb4b5ba518fd1e3f776df012998a9b"></a>
<a id="agroup__trickle_html_gad0815f9368a17532c8b5293a122cd8a9"></a>
<a id="agroup__trickle_html_gaef7719dc563ae9bb93ed5313ed568b44"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__core_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructnet__trickle_html"></a>
<a id="astructnet__trickle_html_a01ffd968b645bb66db67c759520298aa"></a>
<a id="astructnet__trickle_html_a2a1fb8ad04123ebcb781bc3e0173d8be"></a>
<a id="astructnet__trickle_html_a2dde5d732f009a85a27ff6fa0c778636"></a>
<a id="astructnet__trickle_html_a40f69e10d41e34541ca88c092d6a3341"></a>
<a id="astructnet__trickle_html_a6186d8e41cce5193851587d1c72162ea"></a>
<a id="astructnet__trickle_html_a63a3cbf019c99def91e3a9dde7c2f9b4"></a>
<a id="astructnet__trickle_html_a7c3399e45f85874cec48434d605066d9"></a>
<a id="astructnet__trickle_html_aaa03f7763e6bd335b932896ee4433b3b"></a>
<a id="astructnet__trickle_html_aab8a98c8a918528db6f2ddec85df4796"></a>
<a id="astructnet__trickle_html_aaf14e013a0fa74488a26cd7ff476f6e7"></a>
<a id="astructnet__trickle_html_ae9f7ecd9b9730cd1c232ead5d21fec05"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_TRICKLE_H_
#define ZEPHYR_INCLUDE_NET_TRICKLE_H_

#include <stdbool.h>
#include <zephyr/types.h>

#include <zephyr/kernel.h>
#include <zephyr/net/net_core.h>

#ifdef __cplusplus
extern "C" {
#endif


struct net_trickle;

typedef void (*net_trickle_cb_t)(struct net_trickle *trickle,
                                 bool do_suppress, void *user_data);

struct net_trickle {
        uint32_t I;
        uint32_t Imin;
        uint32_t Istart;
        uint32_t Imax_abs;
        uint8_t Imax;

        uint8_t k;
        uint8_t c;

        bool double_to;

        struct k_work_delayable timer;
        net_trickle_cb_t cb;
        void *user_data;
};

#define NET_TRICKLE_INFINITE_REDUNDANCY 0

int net_trickle_create(struct net_trickle *trickle,
                       uint32_t Imin,
                       uint8_t Imax,
                       uint8_t k);

int net_trickle_start(struct net_trickle *trickle,
                      net_trickle_cb_t cb,
                      void *user_data);

int net_trickle_stop(struct net_trickle *trickle);

void net_trickle_consistency(struct net_trickle *trickle);

void net_trickle_inconsistency(struct net_trickle *trickle);

static inline bool net_trickle_is_running(struct net_trickle *trickle)
{
        if (trickle == NULL) {
                return false;
        }

        return trickle->I != 0U;
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_TRICKLE_H_ */
```

## 877.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 154 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_TRICKLE_H_`。

## 877.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/trickle_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [net_trickle](../network_core_model_reference/P155_net_trickle_结构体.md)
- [net_trickle_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gaef7719dc563ae9bb93ed5313ed568b44)
- [user_data](../network_core_model_reference/P155_net_trickle_结构体.md#a40f69e10d41e34541ca88c092d6a3341)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [I](../network_core_model_reference/P155_net_trickle_结构体.md#a6186d8e41cce5193851587d1c72162ea)
- [Imin](../network_core_model_reference/P155_net_trickle_结构体.md#aaf14e013a0fa74488a26cd7ff476f6e7)
- [Istart](../network_core_model_reference/P155_net_trickle_结构体.md#aab8a98c8a918528db6f2ddec85df4796)
- [Imax_abs](../network_core_model_reference/P155_net_trickle_结构体.md#ae9f7ecd9b9730cd1c232ead5d21fec05)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [Imax](../network_core_model_reference/P155_net_trickle_结构体.md#a01ffd968b645bb66db67c759520298aa)
- [k](../network_core_model_reference/P155_net_trickle_结构体.md#a7c3399e45f85874cec48434d605066d9)
- [c](../network_core_model_reference/P155_net_trickle_结构体.md#aaa03f7763e6bd335b932896ee4433b3b)
- [double_to](../network_core_model_reference/P155_net_trickle_结构体.md#a2a1fb8ad04123ebcb781bc3e0173d8be)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [timer](../network_core_model_reference/P155_net_trickle_结构体.md#a2dde5d732f009a85a27ff6fa0c778636)
- [cb](../network_core_model_reference/P155_net_trickle_结构体.md#a63a3cbf019c99def91e3a9dde7c2f9b4)
- [net_trickle_create](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gac412d65ad2a8483920de32c1e0ae6be5)
- [net_trickle_start](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#ga6674fac118a187320d73dc742f0e216f)
- [net_trickle_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#ga8477e45a95abccfb714e3f3369686c6d)
- [net_trickle_consistency](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gacefb4b5ba518fd1e3f776df012998a9b)
- [net_trickle_inconsistency](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#gad0815f9368a17532c8b5293a122cd8a9)
- [net_trickle_is_running](https://docs.zephyrproject.org/latest/doxygen/html/group__trickle.html#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [net_trickle::Imax](../network_core_model_reference/P155_net_trickle_结构体.md#a01ffd968b645bb66db67c759520298aa)
- [net_trickle::double_to](../network_core_model_reference/P155_net_trickle_结构体.md#a2a1fb8ad04123ebcb781bc3e0173d8be)
- [net_trickle::timer](../network_core_model_reference/P155_net_trickle_结构体.md#a2dde5d732f009a85a27ff6fa0c778636)
- [net_trickle::user_data](../network_core_model_reference/P155_net_trickle_结构体.md#a40f69e10d41e34541ca88c092d6a3341)
- [net_trickle::I](../network_core_model_reference/P155_net_trickle_结构体.md#a6186d8e41cce5193851587d1c72162ea)
- [net_trickle::cb](../network_core_model_reference/P155_net_trickle_结构体.md#a63a3cbf019c99def91e3a9dde7c2f9b4)
- [net_trickle::k](../network_core_model_reference/P155_net_trickle_结构体.md#a7c3399e45f85874cec48434d605066d9)
- [net_trickle::c](../network_core_model_reference/P155_net_trickle_结构体.md#aaa03f7763e6bd335b932896ee4433b3b)
- [net_trickle::Istart](../network_core_model_reference/P155_net_trickle_结构体.md#aab8a98c8a918528db6f2ddec85df4796)
- [net_trickle::Imin](../network_core_model_reference/P155_net_trickle_结构体.md#aaf14e013a0fa74488a26cd7ff476f6e7)
- [net_trickle::Imax_abs](../network_core_model_reference/P155_net_trickle_结构体.md#ae9f7ecd9b9730cd1c232ead5d21fec05)

---

[上一章](P876_transport.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P878_uaol.h_源码浏览.md)
