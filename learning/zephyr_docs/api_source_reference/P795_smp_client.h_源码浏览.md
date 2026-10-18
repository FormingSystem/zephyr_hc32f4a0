---
id: learning.zephyr-docs.api-source-reference.page-795
title: smp_client.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第795章\_smp\_client.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html)。

## 795.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="agroup__mcumgr__smp__client_html_ga07f36d0ac230d158c2959e8010444e47"></a>
<a id="agroup__mcumgr__smp__client_html_ga57ec028fc6bcb3591298815b1d9b8a3b"></a>
<a id="agroup__mcumgr__smp__client_html_ga9552e2cce2711d7d0ea19ca170661419"></a>
<a id="agroup__mcumgr__smp__client_html_gace302f95e5f45076db72fbecf190f0f5"></a>
<a id="agroup__mcumgr__smp__client_html_gae7818782c9eefcc78911c589078ece26"></a>
<a id="agroup__mcumgr__smp__client_html_gae7974bf0e951403f6dfe8b33a2547acc"></a>
<a id="agroup__mcumgr__smp__client_html_gaeb20d13ddf14ddb924b0a84a014abda5"></a>
<a id="agroup__mcumgr__smp__client_html_gaf4142d0950845de6a207d02aaa6a8982"></a>
<a id="akernel_8h_html"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html_aa05d01653e39ef61a93f33319c9a00ed"></a>
<a id="amgmt_2mcumgr_2transport_2smp_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructgroup_html"></a>
<a id="astructk__fifo_html"></a>
<a id="astructk__work_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ade8055f804d5a1fea13e55d71d92a5e7"></a>
<a id="astructsmp__client__object_html"></a>
<a id="astructsmp__client__object_html_a01507d6fa5a75751b39ccda82d0836ef"></a>
<a id="astructsmp__client__object_html_a0de9e7ee538b84cf1a6065b7b8b0bc53"></a>
<a id="astructsmp__client__object_html_a5d3cf1e109692112bf52b0b8514bab9f"></a>
<a id="astructsmp__client__object_html_a9623a174f2be0f73903ee860b2ea374e"></a>
<a id="astructsmp__client__object_html_ae4c73b23b90ef9f6cb8a93efde992c8a"></a>
<a id="astructsmp__transport_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_SMP_SMP_CLIENT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_SMP_SMP_CLIENT_H_

#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
#include <mgmt/mcumgr/transport/smp_internal.h>
#include <zephyr/mgmt/mcumgr/smp/smp.h>
#include <zephyr/mgmt/mcumgr/transport/smp.h>


struct smp_client_object {
        struct k_work work;
        struct k_fifo tx_fifo;
        struct smp_transport *smpt;
        uint8_t smp_seq;
        void *priv;
};

#ifdef __cplusplus
extern "C" {
#endif

int smp_client_object_init(struct smp_client_object *smp_client, int smp_type);

static inline void smp_client_object_set_data(struct smp_client_object *smp_client, void *data)
{
        smp_client->priv = data;
}

static inline void *smp_client_object_get_data(struct smp_client_object *smp_client)
{
        return smp_client->priv;
}

typedef int (*smp_client_res_fn)(struct net_buf *nb, void *user_data);

int smp_client_single_response(const struct smp_transport *smpt, struct net_buf *nb,
                               const struct smp_hdr *res_hdr);

struct net_buf *smp_client_buf_allocation(struct smp_client_object *smp_client, uint16_t group,
                                          uint8_t command_id, uint8_t op,
                                          enum smp_mcumgr_version_t version);
void smp_client_buf_free(struct net_buf *nb);

int smp_client_send_cmd(struct smp_client_object *smp_client, struct net_buf *nb,
                        smp_client_res_fn cb, void *user_data, int timeout_in_sec);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_SMP_SMP_CLIENT_H_ */
```

## 795.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 154 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_SMP_SMP_CLIENT_H_`。

## 795.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/mgmt/mcumgr/smp/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html)
- [zephyr/mgmt/mcumgr/transport/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [work](../system_service_model_reference/P078_smp_client_object_结构体.md#ae4c73b23b90ef9f6cb8a93efde992c8a)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [tx_fifo](../system_service_model_reference/P078_smp_client_object_结构体.md#a5d3cf1e109692112bf52b0b8514bab9f)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [smpt](../system_service_model_reference/P078_smp_client_object_结构体.md#a01507d6fa5a75751b39ccda82d0836ef)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [smp_seq](../system_service_model_reference/P078_smp_client_object_结构体.md#a0de9e7ee538b84cf1a6065b7b8b0bc53)
- [priv](../system_service_model_reference/P078_smp_client_object_结构体.md#a9623a174f2be0f73903ee860b2ea374e)
- [smp_client_object_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#ga07f36d0ac230d158c2959e8010444e47)
- [smp_client_object_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gaf4142d0950845de6a207d02aaa6a8982)
- [smp_client_object_get_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#ga9552e2cce2711d7d0ea19ca170661419)
- [smp_client_res_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gae7974bf0e951403f6dfe8b33a2547acc)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [user_data](../network_core_model_reference/P046_net_buf_结构体.md#ade8055f804d5a1fea13e55d71d92a5e7)
- [smp_client_single_response](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gae7818782c9eefcc78911c589078ece26)
- [smp_client_buf_allocation](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#ga57ec028fc6bcb3591298815b1d9b8a3b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [smp_mcumgr_version_t](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#aa05d01653e39ef61a93f33319c9a00ed)
- [smp_client_buf_free](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gace302f95e5f45076db72fbecf190f0f5)
- [smp_client_send_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gaeb20d13ddf14ddb924b0a84a014abda5)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html)
- [smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [net_buf::user_data](../network_core_model_reference/P046_net_buf_结构体.md#ade8055f804d5a1fea13e55d71d92a5e7)
- [smp_client_object::smpt](../system_service_model_reference/P078_smp_client_object_结构体.md#a01507d6fa5a75751b39ccda82d0836ef)
- [smp_client_object::smp_seq](../system_service_model_reference/P078_smp_client_object_结构体.md#a0de9e7ee538b84cf1a6065b7b8b0bc53)
- [smp_client_object::tx_fifo](../system_service_model_reference/P078_smp_client_object_结构体.md#a5d3cf1e109692112bf52b0b8514bab9f)
- [smp_client_object::priv](../system_service_model_reference/P078_smp_client_object_结构体.md#a9623a174f2be0f73903ee860b2ea374e)
- [smp_client_object::work](../system_service_model_reference/P078_smp_client_object_结构体.md#ae4c73b23b90ef9f6cb8a93efde992c8a)

---

[上一章](P794_smp_bt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P796_smp_dummy.h_源码浏览.md)
