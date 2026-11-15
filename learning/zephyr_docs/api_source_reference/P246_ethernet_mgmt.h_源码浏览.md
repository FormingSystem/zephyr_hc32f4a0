---
id: learning.zephyr-docs.api-source-reference.page-246
title: ethernet_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第246章\_ethernet\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__mgmt_8h.html)。

## 246.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
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
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
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
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="aethernet_8h_html"></a>
<a id="agroup__ethernet__mgmt_html_ga039b86d955331f483386b04ec51c3b4d"></a>
<a id="agroup__ethernet__mgmt_html_ga07ea7707f01d0c34724e0a71c463f1ad"></a>
<a id="agroup__ethernet__mgmt_html_gac02c1f616aee2a7381aa6eebba3f799f"></a>
<a id="agroup__ethernet__mgmt_html_gaf7fe2fdca74cd547a4d015bfe0dd7536"></a>
<a id="agroup__net__mgmt_html_ga08bde8717fd8e12a338c517b22b87776"></a>
<a id="agroup__wifi__mgmt_html_ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructethernet__qav__param_html"></a>
<a id="astructethernet__qbu__param_html"></a>
<a id="astructethernet__qbv__param_html"></a>
<a id="astructethernet__txtime__param_html"></a>
<a id="astructnet__eth__addr_html"></a>
<a id="astructnet__if_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_ETHERNET_MGMT_H_
#define ZEPHYR_INCLUDE_NET_ETHERNET_MGMT_H_

#include <zephyr/net/ethernet.h>
#include <zephyr/net/net_mgmt.h>

#ifdef __cplusplus
extern "C" {
#endif



#define NET_ETHERNET_LAYER      NET_MGMT_LAYER_L2
#define NET_ETHERNET_CODE       NET_MGMT_LAYER_CODE_ETHERNET
#define NET_ETHERNET_BASE       (NET_MGMT_IFACE_BIT |                   \
                                 NET_MGMT_LAYER(NET_ETHERNET_LAYER) |   \
                                 NET_MGMT_LAYER_CODE(NET_ETHERNET_CODE))
#define NET_ETHERNET_EVENT      (NET_ETHERNET_BASE | NET_MGMT_EVENT_BIT)

enum net_request_ethernet_cmd {
        NET_REQUEST_ETHERNET_CMD_SET_MAC_ADDRESS = 1,
        NET_REQUEST_ETHERNET_CMD_SET_QAV_PARAM,
        NET_REQUEST_ETHERNET_CMD_SET_QBV_PARAM,
        NET_REQUEST_ETHERNET_CMD_SET_QBU_PARAM,
        NET_REQUEST_ETHERNET_CMD_SET_TXTIME_PARAM,
        NET_REQUEST_ETHERNET_CMD_SET_PROMISC_MODE,
        NET_REQUEST_ETHERNET_CMD_GET_PRIORITY_QUEUES_NUM,
        NET_REQUEST_ETHERNET_CMD_GET_QAV_PARAM,
        NET_REQUEST_ETHERNET_CMD_GET_PORTS_NUM,
        NET_REQUEST_ETHERNET_CMD_GET_QBV_PARAM,
        NET_REQUEST_ETHERNET_CMD_GET_QBU_PARAM,
        NET_REQUEST_ETHERNET_CMD_GET_TXTIME_PARAM,
        NET_REQUEST_ETHERNET_CMD_SET_TXINJECTION_MODE,
        NET_REQUEST_ETHERNET_CMD_GET_TXINJECTION_MODE,
        NET_REQUEST_ETHERNET_CMD_SET_MAC_FILTER,
};

#define NET_REQUEST_ETHERNET_SET_MAC_ADDRESS                            \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_SET_MAC_ADDRESS)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_SET_MAC_ADDRESS);

#define NET_REQUEST_ETHERNET_SET_QAV_PARAM                              \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_SET_QAV_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_SET_QAV_PARAM);

#define NET_REQUEST_ETHERNET_GET_PORTS_NUM                              \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_GET_PORTS_NUM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_GET_PORTS_NUM);

#define NET_REQUEST_ETHERNET_SET_QBV_PARAM                              \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_SET_QBV_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_SET_QBV_PARAM);

#define NET_REQUEST_ETHERNET_SET_QBU_PARAM                              \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_SET_QBU_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_SET_QBU_PARAM);

#define NET_REQUEST_ETHERNET_SET_TXTIME_PARAM                           \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_SET_TXTIME_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_SET_TXTIME_PARAM);

#define NET_REQUEST_ETHERNET_SET_PROMISC_MODE                           \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_SET_PROMISC_MODE)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_SET_PROMISC_MODE);

#define NET_REQUEST_ETHERNET_GET_PRIORITY_QUEUES_NUM                    \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_GET_PRIORITY_QUEUES_NUM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_GET_PRIORITY_QUEUES_NUM);

#define NET_REQUEST_ETHERNET_GET_QAV_PARAM                              \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_GET_QAV_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_GET_QAV_PARAM);

#define NET_REQUEST_ETHERNET_GET_QBV_PARAM                              \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_GET_QBV_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_GET_QBV_PARAM);

#define NET_REQUEST_ETHERNET_GET_QBU_PARAM                              \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_GET_QBU_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_GET_QBU_PARAM);

#define NET_REQUEST_ETHERNET_GET_TXTIME_PARAM                           \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_GET_TXTIME_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_GET_TXTIME_PARAM);

#define NET_REQUEST_ETHERNET_SET_TXINJECTION_MODE                               \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_SET_TXINJECTION_MODE)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_SET_TXINJECTION_MODE);

#define NET_REQUEST_ETHERNET_GET_TXINJECTION_MODE                               \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_GET_TXINJECTION_MODE)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_GET_TXINJECTION_MODE);

#define NET_REQUEST_ETHERNET_SET_MAC_FILTER                             \
        (NET_ETHERNET_BASE | NET_REQUEST_ETHERNET_CMD_SET_MAC_FILTER)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_ETHERNET_SET_MAC_FILTER);

struct net_eth_addr;
struct ethernet_qav_param;
struct ethernet_qbv_param;
struct ethernet_qbu_param;
struct ethernet_txtime_param;

struct ethernet_req_params {
        union {
                bool promisc_mode;
                bool txinjection_mode;

                struct net_eth_addr mac_address;

                struct ethernet_qav_param qav_param;
                struct ethernet_qbv_param qbv_param;
                struct ethernet_qbu_param qbu_param;
                struct ethernet_txtime_param txtime_param;

                struct ethernet_filter filter;

                int priority_queues_num;
                int ports_num;
        };
};

enum {
        NET_EVENT_ETHERNET_CMD_CARRIER_ON_VAL,
        NET_EVENT_ETHERNET_CMD_CARRIER_OFF_VAL,
        NET_EVENT_ETHERNET_CMD_VLAN_TAG_ENABLED_VAL,
        NET_EVENT_ETHERNET_CMD_VLAN_TAG_DISABLED_VAL,

        NET_EVENT_ETHERNET_CMD_MAX
};

BUILD_ASSERT(NET_EVENT_ETHERNET_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_ethernet_cmd exceeds the limit");

enum net_event_ethernet_cmd {
        NET_MGMT_CMD(NET_EVENT_ETHERNET_CMD_CARRIER_ON),
        NET_MGMT_CMD(NET_EVENT_ETHERNET_CMD_CARRIER_OFF),
        NET_MGMT_CMD(NET_EVENT_ETHERNET_CMD_VLAN_TAG_ENABLED),
        NET_MGMT_CMD(NET_EVENT_ETHERNET_CMD_VLAN_TAG_DISABLED),
};

#define NET_EVENT_ETHERNET_CARRIER_ON                                   \
        (NET_ETHERNET_EVENT | NET_EVENT_ETHERNET_CMD_CARRIER_ON)

#define NET_EVENT_ETHERNET_CARRIER_OFF                                  \
        (NET_ETHERNET_EVENT | NET_EVENT_ETHERNET_CMD_CARRIER_OFF)

#define NET_EVENT_ETHERNET_VLAN_TAG_ENABLED                             \
        (NET_ETHERNET_EVENT | NET_EVENT_ETHERNET_CMD_VLAN_TAG_ENABLED)

#define NET_EVENT_ETHERNET_VLAN_TAG_DISABLED                            \
        (NET_ETHERNET_EVENT | NET_EVENT_ETHERNET_CMD_VLAN_TAG_DISABLED)

struct net_if;


#if defined(CONFIG_NET_L2_ETHERNET_MGMT)
void ethernet_mgmt_raise_carrier_on_event(struct net_if *iface);
#else
static inline void ethernet_mgmt_raise_carrier_on_event(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#if defined(CONFIG_NET_L2_ETHERNET_MGMT)
void ethernet_mgmt_raise_carrier_off_event(struct net_if *iface);
#else
static inline void ethernet_mgmt_raise_carrier_off_event(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#if defined(CONFIG_NET_L2_ETHERNET_MGMT)
void ethernet_mgmt_raise_vlan_enabled_event(struct net_if *iface, uint16_t tag);
#else
static inline void ethernet_mgmt_raise_vlan_enabled_event(struct net_if *iface,
                                                          uint16_t tag)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(tag);
}
#endif

#if defined(CONFIG_NET_L2_ETHERNET_MGMT)
void ethernet_mgmt_raise_vlan_disabled_event(struct net_if *iface,
                                             uint16_t tag);
#else
static inline void ethernet_mgmt_raise_vlan_disabled_event(struct net_if *iface,
                                                           uint16_t tag)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(tag);
}
#endif


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_ETHERNET_MGMT_H_ */
```

## 246.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 264 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_ETHERNET_MGMT_H_`。

## 246.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__mgmt_8h.html)
- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [NET_MGMT_DEFINE_REQUEST_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga08bde8717fd8e12a338c517b22b87776)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [ethernet_qav_param](../network_service_model_reference/P010_ethernet_qav_param_结构体.md)
- [ethernet_qbv_param](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md)
- [ethernet_qbu_param](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md)
- [ethernet_txtime_param](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md)
- [NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [ethernet_mgmt_raise_carrier_on_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#ga07ea7707f01d0c34724e0a71c463f1ad)
- [ethernet_mgmt_raise_carrier_off_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#ga039b86d955331f483386b04ec51c3b4d)
- [ethernet_mgmt_raise_vlan_enabled_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#gaf7fe2fdca74cd547a4d015bfe0dd7536)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [ethernet_mgmt_raise_vlan_disabled_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#gac02c1f616aee2a7381aa6eebba3f799f)
- [ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)

---

[上一章](P245_ethernet_bridge_fdb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P247_ethernet_vlan.h_源码浏览.md)
