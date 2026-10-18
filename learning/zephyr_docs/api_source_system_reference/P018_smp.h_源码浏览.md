---
id: learning.zephyr-docs.api-source-system-reference.page-18
title: smp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_smp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html)。

## 18.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="foldopen00208"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="foldopen00276"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="foldopen00296"></a>
<a id="l00296"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="foldopen00323"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="agroup__mcumgr__transport__smp_html_ga032db1c1b6f4d4212e6dc67fbd28c115"></a>
<a id="agroup__mcumgr__transport__smp_html_ga095edd916780b458e8cbd701969c0640"></a>
<a id="agroup__mcumgr__transport__smp_html_ga0d8277e9da18c896749e2392c7ea1ac7"></a>
<a id="agroup__mcumgr__transport__smp_html_ga0f249aa3fed3044d9bad811e92e4135c"></a>
<a id="agroup__mcumgr__transport__smp_html_ga2085e89b99428a61596d90e084d7c5e2"></a>
<a id="agroup__mcumgr__transport__smp_html_ga4570f81d545ae51e68f5a2c3ede4f170"></a>
<a id="agroup__mcumgr__transport__smp_html_ga477587b2b514bdc74560c5ab94ff792a"></a>
<a id="agroup__mcumgr__transport__smp_html_ga4da3579b031ba6a90448ad9248f52155"></a>
<a id="agroup__mcumgr__transport__smp_html_ga50fcdcef18ae4c937ced9f323715e1e1"></a>
<a id="agroup__mcumgr__transport__smp_html_ga5d886a11df0c49ca18e23e246ab2fab9"></a>
<a id="agroup__mcumgr__transport__smp_html_ga662f893037193923610de1e8793fd971"></a>
<a id="agroup__mcumgr__transport__smp_html_ga67c3481cdc81c20e0c35b4eaa185619e"></a>
<a id="agroup__mcumgr__transport__smp_html_ga77d54c0bd6afc69f73613575b671e089"></a>
<a id="agroup__mcumgr__transport__smp_html_ga840da7e00d590459b656dcbe0dd6f6f4"></a>
<a id="agroup__mcumgr__transport__smp_html_ga87ccc623b5907d7d65b24ed99bd57ec5"></a>
<a id="agroup__mcumgr__transport__smp_html_gadadf97eb50e871f5942b4774c643eba2"></a>
<a id="agroup__mcumgr__transport__smp_html_gae2531ab1dba2992b8465cd49349c5116"></a>
<a id="agroup__mcumgr__transport__smp_html_gaf275034765327b52b900046d71c411ee"></a>
<a id="agroup__mcumgr__transport__smp_html_gafb488cd9854b74c8e5802db3c8fe6116"></a>
<a id="agroup__mcumgr__transport__smp_html_gga5d886a11df0c49ca18e23e246ab2fab9a06953c39575f3903299011cde915ac13"></a>
<a id="agroup__mcumgr__transport__smp_html_gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7"></a>
<a id="agroup__mcumgr__transport__smp_html_gga5d886a11df0c49ca18e23e246ab2fab9a3de5af5fe47980cdf749abc1694d84eb"></a>
<a id="agroup__mcumgr__transport__smp_html_gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43"></a>
<a id="agroup__mcumgr__transport__smp_html_gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe"></a>
<a id="agroup__mcumgr__transport__smp_html_gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863"></a>
<a id="agroup__mcumgr__transport__smp_html_gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342"></a>
<a id="agroup__mcumgr__transport__smp_html_gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f"></a>
<a id="agroup__mcumgr__transport__smp_html_gga5d886a11df0c49ca18e23e246ab2fab9addcf3d287f359bad85104d2a37b4e5c8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__fifo_html"></a>
<a id="astructk__work_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructsmp__client__transport__entry_html"></a>
<a id="astructsmp__client__transport__entry_html_a6a8a368d3db1f03b4e6774d4a86123c2"></a>
<a id="astructsmp__client__transport__entry_html_a83e2e2851f48a8c13e296b3b1ce1d209"></a>
<a id="astructsmp__client__transport__entry_html_ad8ebd9f6bc7d322c51e6aecb2e926022"></a>
<a id="astructsmp__client__transport__entry_html_aebf774d7d0fe4eebe2e230a3680e0acf"></a>
<a id="astructsmp__transport__api__t_html"></a>
<a id="astructsmp__transport__api__t_html_a3b7000867da67eacaf122963e79bb500"></a>
<a id="astructsmp__transport__api__t_html_a3da771527b2ab8c63ddb7920405fca8c"></a>
<a id="astructsmp__transport__api__t_html_a5c8ab9d564d8cc013d28155763f8b20e"></a>
<a id="astructsmp__transport__api__t_html_a68a94fa4f1a1e5e5bea3c1a2d58ef08e"></a>
<a id="astructsmp__transport__api__t_html_a811fefe5287c7050701705f8db51f16d"></a>
<a id="astructsmp__transport__api__t_html_aa408fcddf2262cd6eef52c5b451b7f08"></a>
<a id="astructsmp__transport__api__t_html_aa779d7dcea55385963a0c0054b95f9da"></a>
<a id="astructsmp__transport__api__t_html_aaea5ecb91fc45c3dd4c4785e733fbfa1"></a>
<a id="astructsmp__transport__api__t_html_acc98fb8a8e7e674ec907939831de1809"></a>
<a id="astructsmp__transport__api__t_html_acfeec0f2b18fa4d8518e96d10b2e879a"></a>
<a id="astructsmp__transport__api__t_html_ae3153c9a27123de510e4ee83cc9c0c62"></a>
<a id="astructsmp__transport__bridge_html"></a>
<a id="astructsmp__transport__bridge_html_a8999f556cdde306d93e94c501e190317"></a>
<a id="astructsmp__transport__bridge_html_aab41981338e090d13ea6581ed9101914"></a>
<a id="astructsmp__transport__bridge_html_ae2f098cd30fa5793fb8725845a04931e"></a>
<a id="astructsmp__transport_html"></a>
<a id="astructsmp__transport_html_a2bb0436ae57a1c1d084f3fed1aa16652"></a>
<a id="astructsmp__transport_html_a929ff7e97273dd18920ddc8426c6646f"></a>
<a id="astructsmp__transport_html_ab732e7d9574b78635a90ff559306daaa"></a>

```c
/*
 * Copyright Runtime.io 2018. All rights reserved.
 * Copyright (c) 2022-2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_H_

#include <zephyr/kernel.h>
#include <zcbor_common.h>

#ifdef __cplusplus
extern "C" {
#endif


struct smp_transport;
struct zephyr_smp_transport;
struct net_buf;
struct smp_transport_bridge;
struct smp_client_transport_entry;

typedef int (*smp_transport_out_fn)(struct net_buf *nb);

typedef uint16_t (*smp_transport_get_mtu_fn)(const struct net_buf *nb) __deprecated;

typedef int (*smp_transport_ud_copy_fn)(struct net_buf *dst,
                                        const struct net_buf *src);

typedef void (*smp_transport_ud_free_fn)(void *ud);

typedef bool (*smp_transport_query_valid_check_fn)(struct net_buf *nb, void *arg);

typedef void (*smp_transport_ud_req_init_fn)(struct net_buf *nb, void *priv);

typedef bool (*smp_transport_bridge_connect_fn)(struct smp_transport_bridge *bridge,
                                                bool direction, uint32_t mode, bool same_transport,
                                                zcbor_state_t *input_data,
                                                zcbor_state_t *output_data);

typedef void (*smp_transport_bridge_disconnect_fn)(struct smp_transport_bridge *bridge,
                                                   bool direction);

typedef int (*smp_transport_bridge_out_fn)(const struct smp_transport_bridge *bridge,
                                           struct net_buf *nb, bool direction);

typedef bool (*mgmt_client_transport_cb_t)(const struct smp_client_transport_entry *transport,
                                           void *user_data);

typedef bool (*smp_transport_bridge_modes_fn)(zcbor_state_t *output_data, int *rc);

typedef bool (*smp_transport_bridge_config_details_fn)(uint32_t mode, zcbor_state_t *output_data,
                                                       int *rc);

struct smp_transport_api_t {
        smp_transport_out_fn output;

        uint16_t (*get_mtu)(const struct net_buf *nb) __deprecated;

        smp_transport_ud_copy_fn ud_copy;

        smp_transport_ud_free_fn ud_free;

        smp_transport_query_valid_check_fn query_valid_check;

        smp_transport_ud_req_init_fn ud_init;

#if defined(CONFIG_MCUMGR_GRP_TRANSPORT) || defined(__DOXYGEN__)
        smp_transport_bridge_connect_fn bridge_connect;

        smp_transport_bridge_disconnect_fn bridge_disconnect;

        smp_transport_bridge_out_fn bridge_output;

#if defined(CONFIG_MCUMGR_GRP_TRANSPORT_INFO_FUNCTIONS) || defined(__DOXYGEN__)
        smp_transport_bridge_modes_fn bridge_modes;

        smp_transport_bridge_config_details_fn bridge_config_details;
#endif
#endif
};

struct smp_transport {
        /* Must be the first member. */
        struct k_work work;

        /* FIFO containing incoming requests to be processed. */
        struct k_fifo fifo;

        /* Function pointers */
        struct smp_transport_api_t functions;

#ifdef CONFIG_MCUMGR_TRANSPORT_REASSEMBLY
        /* Packet reassembly internal data, API access only */
        struct {
                struct net_buf *current;        /* net_buf used for reassembly */
                uint16_t expected;              /* expected bytes to come */
        } __reassembly;
#endif
};

struct smp_transport_bridge {
        uint8_t status;

        struct smp_transport *incoming_transport;

        struct smp_transport *outgoing_transport;
};

enum smp_transport_type {
        SMP_SERIAL_TRANSPORT = 0,
        SMP_RAW_SERIAL_TRANSPORT,
        SMP_BLUETOOTH_TRANSPORT,
        SMP_SHELL_TRANSPORT,
        SMP_UDP_IPV4_TRANSPORT,
        SMP_UDP_IPV6_TRANSPORT,
        SMP_LORAWAN_TRANSPORT,
        SMP_SPI_TRANSPORT,


        SMP_USER_DEFINED_TRANSPORT = 64,
};

struct smp_client_transport_entry {
        sys_snode_t node;
        struct smp_transport *smpt;
        int smpt_type;

#if defined(CONFIG_MCUMGR_GRP_TRANSPORT_INFO_FUNCTIONS) || defined(__DOXYGEN__)
        char *name;
#endif
};

int smp_transport_init(struct smp_transport *smpt);

void smp_rx_remove_invalid(struct smp_transport *zst, void *arg);

void smp_rx_clear(struct smp_transport *zst);

void smp_client_transport_register(struct smp_client_transport_entry *entry);

struct smp_transport *smp_client_transport_get(int smpt_type);

bool smp_client_transport_foreach(mgmt_client_transport_cb_t user_cb, void *user_data);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_H_ */
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：Runtime.io 2018. All rights reserved.。

版权（Copyright）：© 2022-2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 255 行

必须是第一个成员。

### 注释 3：原第 258 行

存放待处理输入请求（Incoming Requests）的先进先出队列（FIFO）。

### 注释 4：原第 261 行

函数指针（Function Pointers）。

### 注释 5：原第 265 行

数据包重组内部数据（Packet Reassembly Internal Data），只能通过 API 访问。

### 注释 6：原第 267 行

用于重组（Reassembly）的 `net_buf`。

### 注释 7：原第 268 行

预期将到达的字节数（Expected Bytes to Come）。

### 注释 8：原第 398 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_H_`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)
- [smp_client_transport_entry](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md)
- [smp_transport_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4da3579b031ba6a90448ad9248f52155)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [smp_transport_get_mtu_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga2085e89b99428a61596d90e084d7c5e2)
- [smp_transport_ud_copy_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga840da7e00d590459b656dcbe0dd6f6f4)
- [smp_transport_ud_free_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0f249aa3fed3044d9bad811e92e4135c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [smp_transport_query_valid_check_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga77d54c0bd6afc69f73613575b671e089)
- [smp_transport_ud_req_init_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga095edd916780b458e8cbd701969c0640)
- [smp_transport_bridge_connect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga032db1c1b6f4d4212e6dc67fbd28c115)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [smp_transport_bridge_disconnect_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga50fcdcef18ae4c937ced9f323715e1e1)
- [smp_transport_bridge_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gadadf97eb50e871f5942b4774c643eba2)
- [mgmt_client_transport_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga477587b2b514bdc74560c5ab94ff792a)
- [smp_transport_bridge_modes_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4570f81d545ae51e68f5a2c3ede4f170)
- [smp_transport_bridge_config_details_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga0d8277e9da18c896749e2392c7ea1ac7)
- [smp_transport_api_t](../system_service_model_reference/P082_smp_transport_api_t_结构体.md)
- [output](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#aa779d7dcea55385963a0c0054b95f9da)
- [get_mtu](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#acfeec0f2b18fa4d8518e96d10b2e879a)
- [ud_copy](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#ae3153c9a27123de510e4ee83cc9c0c62)
- [ud_free](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#acc98fb8a8e7e674ec907939831de1809)
- [query_valid_check](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a811fefe5287c7050701705f8db51f16d)
- [ud_init](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a3b7000867da67eacaf122963e79bb500)
- [bridge_connect](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a5c8ab9d564d8cc013d28155763f8b20e)
- [bridge_disconnect](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#aaea5ecb91fc45c3dd4c4785e733fbfa1)
- [bridge_output](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#aa408fcddf2262cd6eef52c5b451b7f08)
- [bridge_modes](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a68a94fa4f1a1e5e5bea3c1a2d58ef08e)
- [bridge_config_details](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a3da771527b2ab8c63ddb7920405fca8c)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [work](../system_service_model_reference/P081_smp_transport_结构体.md#a2bb0436ae57a1c1d084f3fed1aa16652)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [fifo](../system_service_model_reference/P081_smp_transport_结构体.md#a929ff7e97273dd18920ddc8426c6646f)
- [functions](../system_service_model_reference/P081_smp_transport_结构体.md#ab732e7d9574b78635a90ff559306daaa)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [status](../system_service_model_reference/P083_smp_transport_bridge_结构体.md#a8999f556cdde306d93e94c501e190317)
- [incoming_transport](../system_service_model_reference/P083_smp_transport_bridge_结构体.md#ae2f098cd30fa5793fb8725845a04931e)
- [outgoing_transport](../system_service_model_reference/P083_smp_transport_bridge_结构体.md#aab41981338e090d13ea6581ed9101914)
- [smp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga5d886a11df0c49ca18e23e246ab2fab9)
- [SMP_SERIAL_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342)
- [SMP_RAW_SERIAL_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a06953c39575f3903299011cde915ac13)
- [SMP_BLUETOOTH_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe)
- [SMP_SHELL_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43)
- [SMP_UDP_IPV4_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f)
- [SMP_UDP_IPV6_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7)
- [SMP_LORAWAN_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9addcf3d287f359bad85104d2a37b4e5c8)
- [SMP_SPI_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9a3de5af5fe47980cdf749abc1694d84eb)
- [SMP_USER_DEFINED_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md#ad8ebd9f6bc7d322c51e6aecb2e926022)
- [smpt](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md#aebf774d7d0fe4eebe2e230a3680e0acf)
- [smpt_type](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md#a6a8a368d3db1f03b4e6774d4a86123c2)
- [name](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md#a83e2e2851f48a8c13e296b3b1ce1d209)
- [smp_transport_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gaf275034765327b52b900046d71c411ee)
- [smp_rx_remove_invalid](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga87ccc623b5907d7d65b24ed99bd57ec5)
- [smp_rx_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga662f893037193923610de1e8793fd971)
- [smp_client_transport_register](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gafb488cd9854b74c8e5802db3c8fe6116)
- [smp_client_transport_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga67c3481cdc81c20e0c35b4eaa185619e)
- [smp_client_transport_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#gae2531ab1dba2992b8465cd49349c5116)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [smp_client_transport_entry::smpt_type](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md#a6a8a368d3db1f03b4e6774d4a86123c2)
- [smp_client_transport_entry::name](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md#a83e2e2851f48a8c13e296b3b1ce1d209)
- [smp_client_transport_entry::node](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md#ad8ebd9f6bc7d322c51e6aecb2e926022)
- [smp_client_transport_entry::smpt](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md#aebf774d7d0fe4eebe2e230a3680e0acf)
- [smp_transport_api_t::ud_init](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a3b7000867da67eacaf122963e79bb500)
- [smp_transport_api_t::bridge_config_details](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a3da771527b2ab8c63ddb7920405fca8c)
- [smp_transport_api_t::bridge_connect](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a5c8ab9d564d8cc013d28155763f8b20e)
- [smp_transport_api_t::bridge_modes](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a68a94fa4f1a1e5e5bea3c1a2d58ef08e)
- [smp_transport_api_t::query_valid_check](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#a811fefe5287c7050701705f8db51f16d)
- [smp_transport_api_t::bridge_output](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#aa408fcddf2262cd6eef52c5b451b7f08)
- [smp_transport_api_t::output](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#aa779d7dcea55385963a0c0054b95f9da)
- [smp_transport_api_t::bridge_disconnect](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#aaea5ecb91fc45c3dd4c4785e733fbfa1)
- [smp_transport_api_t::ud_free](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#acc98fb8a8e7e674ec907939831de1809)
- [smp_transport_api_t::get_mtu](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#acfeec0f2b18fa4d8518e96d10b2e879a)
- [smp_transport_api_t::ud_copy](../system_service_model_reference/P082_smp_transport_api_t_结构体.md#ae3153c9a27123de510e4ee83cc9c0c62)
- [smp_transport_bridge::status](../system_service_model_reference/P083_smp_transport_bridge_结构体.md#a8999f556cdde306d93e94c501e190317)
- [smp_transport_bridge::outgoing_transport](../system_service_model_reference/P083_smp_transport_bridge_结构体.md#aab41981338e090d13ea6581ed9101914)
- [smp_transport_bridge::incoming_transport](../system_service_model_reference/P083_smp_transport_bridge_结构体.md#ae2f098cd30fa5793fb8725845a04931e)
- [smp_transport::work](../system_service_model_reference/P081_smp_transport_结构体.md#a2bb0436ae57a1c1d084f3fed1aa16652)
- [smp_transport::fifo](../system_service_model_reference/P081_smp_transport_结构体.md#a929ff7e97273dd18920ddc8426c6646f)
- [smp_transport::functions](../system_service_model_reference/P081_smp_transport_结构体.md#ab732e7d9574b78635a90ff559306daaa)

---

[上一章](P017_mchp-xec-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P019_mm_drv_intel_adsp_mtl_tlb.h_源码浏览.md)
