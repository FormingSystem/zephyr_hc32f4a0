---
id: learning.zephyr-docs.api-source-supplement-reference.page-113
title: smp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第113章\_smp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html)。

## 113.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
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
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html_a191eb8c8a5a531b158374a1071925ca7"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html_a6705014150cda88212d6eb6143d044d4"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html_aa05d01653e39ef61a93f33319c9a00ed"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html_aa05d01653e39ef61a93f33319c9a00eda7d9455ed10c150d699de2598af9dcb7a"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html_aa05d01653e39ef61a93f33319c9a00edaee0064c0e66c35a1822c101a83693f33"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html_ac31c28afe322fb0e9ca49e8a1fb7002b"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html_ad6b5e8c30760366c0e9d6c843605de93"></a>
<a id="amgmt_2mcumgr_2transport_2smp_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructcbor__nb__reader_html"></a>
<a id="astructcbor__nb__reader_html_a1bfa99724cc6de5d93d88415e5231d09"></a>
<a id="astructcbor__nb__reader_html_a7cbec04a9c1fd8a1f8feed0de8d1be1d"></a>
<a id="astructcbor__nb__writer_html"></a>
<a id="astructcbor__nb__writer_html_a6aa71f361798e61f19e5f0c46cdf1ad5"></a>
<a id="astructcbor__nb__writer_html_af8832d941c69207bc80ed22def5e3125"></a>
<a id="astructgroup_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructsmp__streamer_html"></a>
<a id="astructsmp__streamer_html_a00f6b8731e1a789939eaec106d746daf"></a>
<a id="astructsmp__streamer_html_a478b0732071a888bd83ccd03bdd51e85"></a>
<a id="astructsmp__streamer_html_ad5f6bcfcea32075ff61afc1b6c4972be"></a>
<a id="astructsmp__transport_html"></a>

```c
/*
 * Copyright (c) 2018-2021 mcumgr authors
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_SMP_SMP_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_SMP_SMP_H_

#include <zephyr/net_buf.h>
#include <zephyr/mgmt/mcumgr/transport/smp.h>

#include <zcbor_common.h>

#ifdef __cplusplus
extern "C" {
#endif

enum smp_mcumgr_version_t {
        SMP_MCUMGR_VERSION_1 = 0,

        SMP_MCUMGR_VERSION_2,
};

struct cbor_nb_reader {
        struct net_buf *nb;
        /* CONFIG_MCUMGR_SMP_CBOR_MAX_DECODING_LEVELS + 2 translates to minimal
         * zcbor backup states.
         */
        zcbor_state_t zs[CONFIG_MCUMGR_SMP_CBOR_MAX_DECODING_LEVELS + 2];
};

struct cbor_nb_writer {
        struct net_buf *nb;
        zcbor_state_t zs[CONFIG_MCUMGR_SMP_CBOR_MAX_ENCODING_LEVELS + 2];

#if defined(CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL)
        uint16_t error_group;
        uint16_t error_ret;
#endif
};

struct net_buf *smp_packet_alloc(void);

void smp_packet_free(struct net_buf *nb);


size_t smp_packet_buffers_available(void);


struct smp_streamer {
        struct smp_transport *smpt;
        struct cbor_nb_reader *reader;
        struct cbor_nb_writer *writer;

#ifdef CONFIG_MCUMGR_SMP_VERBOSE_ERR_RESPONSE
        const char *rc_rsn;
#endif
};

int smp_process_request_packet(struct smp_streamer *streamer, void *req);

bool smp_add_cmd_err(zcbor_state_t *zse, uint16_t group, uint16_t ret);

#if defined(CONFIG_MCUMGR_SMP_SUPPORT_ORIGINAL_PROTOCOL)
typedef int (*smp_translate_error_fn)(uint16_t err);
#endif

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_SMP_SMP_H_ */
```

## 113.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2021 mcumgr authors。

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

`CONFIG_MCUMGR_SMP_CBOR_MAX_DECODING_LEVELS + 2` 对应所需的最少 zcbor 备份状态（Backup states）数量。

### 注释 3：原第 151 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_SMP_SMP_H_`。

## 113.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/mgmt/mcumgr/transport/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html)
- [smp_mcumgr_version_t](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#aa05d01653e39ef61a93f33319c9a00ed)
- [SMP_MCUMGR_VERSION_1](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#aa05d01653e39ef61a93f33319c9a00edaee0064c0e66c35a1822c101a83693f33)
- [SMP_MCUMGR_VERSION_2](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#aa05d01653e39ef61a93f33319c9a00eda7d9455ed10c150d699de2598af9dcb7a)
- [cbor_nb_reader](../system_service_model_reference/P001_cbor_nb_reader_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [nb](../system_service_model_reference/P001_cbor_nb_reader_结构体.md#a1bfa99724cc6de5d93d88415e5231d09)
- [zs](../system_service_model_reference/P001_cbor_nb_reader_结构体.md#a7cbec04a9c1fd8a1f8feed0de8d1be1d)
- [cbor_nb_writer](../system_service_model_reference/P002_cbor_nb_writer_结构体.md)
- [nb](../system_service_model_reference/P002_cbor_nb_writer_结构体.md#af8832d941c69207bc80ed22def5e3125)
- [zs](../system_service_model_reference/P002_cbor_nb_writer_结构体.md#a6aa71f361798e61f19e5f0c46cdf1ad5)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [smp_packet_alloc](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#ac31c28afe322fb0e9ca49e8a1fb7002b)
- [smp_packet_free](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#ad6b5e8c30760366c0e9d6c843605de93)
- [smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [smpt](../system_service_model_reference/P080_smp_streamer_结构体.md#a478b0732071a888bd83ccd03bdd51e85)
- [reader](../system_service_model_reference/P080_smp_streamer_结构体.md#ad5f6bcfcea32075ff61afc1b6c4972be)
- [writer](../system_service_model_reference/P080_smp_streamer_结构体.md#a00f6b8731e1a789939eaec106d746daf)
- [smp_process_request_packet](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#a6705014150cda88212d6eb6143d044d4)
- [smp_add_cmd_err](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#a191eb8c8a5a531b158374a1071925ca7)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [cbor_nb_reader::nb](../system_service_model_reference/P001_cbor_nb_reader_结构体.md#a1bfa99724cc6de5d93d88415e5231d09)
- [cbor_nb_reader::zs](../system_service_model_reference/P001_cbor_nb_reader_结构体.md#a7cbec04a9c1fd8a1f8feed0de8d1be1d)
- [cbor_nb_writer::zs](../system_service_model_reference/P002_cbor_nb_writer_结构体.md#a6aa71f361798e61f19e5f0c46cdf1ad5)
- [cbor_nb_writer::nb](../system_service_model_reference/P002_cbor_nb_writer_结构体.md#af8832d941c69207bc80ed22def5e3125)
- [smp_streamer::writer](../system_service_model_reference/P080_smp_streamer_结构体.md#a00f6b8731e1a789939eaec106d746daf)
- [smp_streamer::smpt](../system_service_model_reference/P080_smp_streamer_结构体.md#a478b0732071a888bd83ccd03bdd51e85)
- [smp_streamer::reader](../system_service_model_reference/P080_smp_streamer_结构体.md#ad5f6bcfcea32075ff61afc1b6c4972be)

---

[上一章](P112_metric.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P114_mic_privacy.h_源码浏览.md)
