---
id: learning.zephyr-docs.api-source-network-reference.page-12
title: lldp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_lldp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h.html)。

## 12.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
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
<a id="l00124"></a>
<a id="foldopen00126"></a>
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
<a id="foldopen00141"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="agroup__lldp_html_ga0efa1813c537dcf02e021db60049c284"></a>
<a id="agroup__lldp_html_ga1e9fb662d7cdfc3c4c68cfd0312987cf"></a>
<a id="agroup__lldp_html_ga61845c96c65d6df83f422a68e31162cf"></a>
<a id="agroup__lldp_html_ga961bc59567ffa2d5a4d21290d1d78407"></a>
<a id="agroup__lldp_html_ga9702175375a71eaab20f450291cb51ad"></a>
<a id="agroup__lldp_html_gadd4273e4fe55757729008ce081771899"></a>
<a id="agroup__lldp_html_gafdd1b4cea9f560597c31a0e42d5341e0"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6"></a>
<a id="agroup__lldp_html_ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__lldp__chassis__tlv_html"></a>
<a id="astructnet__lldp__chassis__tlv_html_a37b7e81a670595d1c6c77a45bf9cfc73"></a>
<a id="astructnet__lldp__chassis__tlv_html_ad9d415f6a1e9018953728de1b529fd98"></a>
<a id="astructnet__lldp__chassis__tlv_html_af81d3102ad0ec1f7ef76bb1533dcc7cd"></a>
<a id="astructnet__lldp__port__tlv_html"></a>
<a id="astructnet__lldp__port__tlv_html_a572a6fd721c68796a572410ac62f2f93"></a>
<a id="astructnet__lldp__port__tlv_html_a710beaeda2ddd7933464e07cb87a2bfe"></a>
<a id="astructnet__lldp__port__tlv_html_aecc83eaec39284b33c2e7cf07f0ffa05"></a>
<a id="astructnet__lldp__time__to__live__tlv_html"></a>
<a id="astructnet__lldp__time__to__live__tlv_html_a78b88d66184a0d25c413baf2fec495ab"></a>
<a id="astructnet__lldp__time__to__live__tlv_html_ab967792a938a5d67f744e53be8d5f0fd"></a>
<a id="astructnet__lldpdu_html"></a>
<a id="astructnet__lldpdu_html_a1a1c80fe7462ddbfd84289735013834c"></a>
<a id="astructnet__lldpdu_html_aa55adafc5528576017c37a28413bdaf9"></a>
<a id="astructnet__lldpdu_html_afbe0618b6d849b8ee7b225844ac399df"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__pkt_html_a7590eeacf06469206cb7e7949acfa7b2"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_LLDP_H_
#define ZEPHYR_INCLUDE_NET_LLDP_H_


#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>

#ifdef __cplusplus
extern "C" {
#endif


#define LLDP_TLV_GET_LENGTH(type_length)        (type_length & BIT_MASK(9))
#define LLDP_TLV_GET_TYPE(type_length)          ((uint8_t)(type_length >> 9))

/* LLDP Definitions */

/* According to the spec, End of LLDPDU TLV value is constant. */
#define NET_LLDP_END_LLDPDU_VALUE 0x0000

/*
 * For the Chassis ID TLV Value, if subtype is a MAC address then we must
 * use values from CONFIG_NET_LLDP_CHASSIS_ID_MAC0 through
 * CONFIG_NET_LLDP_CHASSIS_ID_MAC5. If not, we use CONFIG_NET_LLDP_CHASSIS_ID.
 *
 * FIXME: implement a similar scheme for subtype 5 (network address).
 */
#if defined(CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE)
#if (CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE == 4)
#define NET_LLDP_CHASSIS_ID_VALUE               \
        {                                       \
          CONFIG_NET_LLDP_CHASSIS_ID_MAC0,      \
          CONFIG_NET_LLDP_CHASSIS_ID_MAC1,      \
          CONFIG_NET_LLDP_CHASSIS_ID_MAC2,      \
          CONFIG_NET_LLDP_CHASSIS_ID_MAC3,      \
          CONFIG_NET_LLDP_CHASSIS_ID_MAC4,      \
          CONFIG_NET_LLDP_CHASSIS_ID_MAC5       \
        }

#define NET_LLDP_CHASSIS_ID_VALUE_LEN (6)
#else
#define NET_LLDP_CHASSIS_ID_VALUE CONFIG_NET_LLDP_CHASSIS_ID
#define NET_LLDP_CHASSIS_ID_VALUE_LEN (sizeof(CONFIG_NET_LLDP_CHASSIS_ID) - 1)
#endif
#else
#define NET_LLDP_CHASSIS_ID_VALUE 0
#define NET_LLDP_CHASSIS_ID_VALUE_LEN 0
#endif

/*
 * For the Port ID TLV Value, if subtype is a MAC address then we must
 * use values from CONFIG_NET_LLDP_PORT_ID_MAC0 through
 * CONFIG_NET_LLDP_PORT_ID_MAC5. If not, we use CONFIG_NET_LLDP_PORT_ID.
 *
 * FIXME: implement a similar scheme for subtype 4 (network address).
 */
#if defined(CONFIG_NET_LLDP_PORT_ID_SUBTYPE)
#if (CONFIG_NET_LLDP_PORT_ID_SUBTYPE == 3)
#define NET_LLDP_PORT_ID_VALUE          \
        {                               \
          CONFIG_NET_LLDP_PORT_ID_MAC0, \
          CONFIG_NET_LLDP_PORT_ID_MAC1, \
          CONFIG_NET_LLDP_PORT_ID_MAC2, \
          CONFIG_NET_LLDP_PORT_ID_MAC3, \
          CONFIG_NET_LLDP_PORT_ID_MAC4, \
          CONFIG_NET_LLDP_PORT_ID_MAC5  \
        }

#define NET_LLDP_PORT_ID_VALUE_LEN (6)
#else
#define NET_LLDP_PORT_ID_VALUE CONFIG_NET_LLDP_PORT_ID
#define NET_LLDP_PORT_ID_VALUE_LEN (sizeof(CONFIG_NET_LLDP_PORT_ID) - 1)
#endif
#else
#define NET_LLDP_PORT_ID_VALUE 0
#define NET_LLDP_PORT_ID_VALUE_LEN 0
#endif

/*
 * TLVs Length.
 * Note that TLVs that have a subtype must have a byte added to their length.
 */
#define NET_LLDP_CHASSIS_ID_TLV_LEN (NET_LLDP_CHASSIS_ID_VALUE_LEN + 1)
#define NET_LLDP_PORT_ID_TLV_LEN (NET_LLDP_PORT_ID_VALUE_LEN + 1)
#define NET_LLDP_TTL_TLV_LEN (2)

/*
 * Time to Live value.
 * Calculate based on section 9.2.5.22 from LLDP spec.
 *
 * FIXME: when the network interface is about to be ‘disabled’ TTL shall be set
 * to zero so LLDP Rx agents can invalidate the entry related to this node.
 */
#if defined(CONFIG_NET_LLDP_TX_INTERVAL) && defined(CONFIG_NET_LLDP_TX_HOLD)
#define NET_LLDP_TTL \
        MIN((CONFIG_NET_LLDP_TX_INTERVAL * CONFIG_NET_LLDP_TX_HOLD) + 1, 65535)
#endif


struct net_if;


enum net_lldp_tlv_type {
        LLDP_TLV_END_LLDPDU          = 0,
        LLDP_TLV_CHASSIS_ID          = 1,
        LLDP_TLV_PORT_ID             = 2,
        LLDP_TLV_TTL                 = 3,
        LLDP_TLV_PORT_DESC           = 4,
        LLDP_TLV_SYSTEM_NAME         = 5,
        LLDP_TLV_SYSTEM_DESC         = 6,
        LLDP_TLV_SYSTEM_CAPABILITIES = 7,
        LLDP_TLV_MANAGEMENT_ADDR     = 8,
        /* Types 9 - 126 are reserved. */
        LLDP_TLV_ORG_SPECIFIC       = 127,
};

struct net_lldp_chassis_tlv {
        uint16_t type_length;
        uint8_t subtype;
        uint8_t value[NET_LLDP_CHASSIS_ID_VALUE_LEN];
} __packed;

struct net_lldp_port_tlv {
        uint16_t type_length;
        uint8_t subtype;
        uint8_t value[NET_LLDP_PORT_ID_VALUE_LEN];
} __packed;

struct net_lldp_time_to_live_tlv {
        uint16_t type_length;
        uint16_t ttl;
} __packed;

struct net_lldpdu {
        struct net_lldp_chassis_tlv chassis_id;
        struct net_lldp_port_tlv port_id;
        struct net_lldp_time_to_live_tlv ttl;
} __packed;

int net_lldp_config(struct net_if *iface, const struct net_lldpdu *lldpdu);

int net_lldp_config_optional(struct net_if *iface, const uint8_t *tlv,
                             size_t len);

typedef enum net_verdict (*net_lldp_recv_cb_t)(struct net_if *iface,
                                               struct net_pkt *pkt);

int net_lldp_register_callback(struct net_if *iface, net_lldp_recv_cb_t cb);

#if defined(CONFIG_NET_LLDP)
int net_lldp_set_lldpdu(struct net_if *iface);
#else
#define net_lldp_set_lldpdu(iface)
#endif

#if defined(CONFIG_NET_LLDP)
void net_lldp_unset_lldpdu(struct net_if *iface);
#else
#define net_lldp_unset_lldpdu(iface)
#endif

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_LLDP_H_ */
```

## 12.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

链路层发现协议定义（LLDP Definitions）。

### 注释 3：原第 39 行

根据规范（Specification），LLDP 协议数据单元结束类型长度值（End of LLDPDU TLV）的值是常量。

### 注释 4：原第 42 行

对于机箱标识类型长度值（Chassis ID TLV），若子类型（Subtype）是 MAC 地址，则必须使用 `CONFIG_NET_LLDP_CHASSIS_ID_MAC0` 至 `CONFIG_NET_LLDP_CHASSIS_ID_MAC5` 的值；否则使用 `CONFIG_NET_LLDP_CHASSIS_ID`。

待修复（FIXME）：为子类型 5，即网络地址（Network Address），实现类似机制。

### 注释 5：原第 71 行

对于端口标识类型长度值（Port ID TLV），若子类型（Subtype）是 MAC 地址，则必须使用 `CONFIG_NET_LLDP_PORT_ID_MAC0` 至 `CONFIG_NET_LLDP_PORT_ID_MAC5` 的值；否则使用 `CONFIG_NET_LLDP_PORT_ID`。

待修复（FIXME）：为子类型 4，即网络地址（Network Address），实现类似机制。

### 注释 6：原第 100 行

类型长度值结构的长度（TLVs Length）。
注意，具有子类型（Subtype）的 TLV，其长度必须增加一个字节。

### 注释 7：原第 108 行

生存时间值（Time to Live，TTL），根据 LLDP 规范第 9.2.5.22 节计算。

待修复（FIXME）：当网络接口即将被禁用（Disabled）时，应将 TTL 设置为零，使 LLDP 接收代理（Rx Agents）能够使与本节点相关的条目失效（Invalidate）。

### 注释 8：原第 136 行

类型（Types）9～126 为保留值（Reserved）。

### 注释 9：原第 263 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_LLDP_H_`。

## 12.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_lldp_tlv_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#gadd4273e4fe55757729008ce081771899)
- [LLDP_TLV_END_LLDPDU](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a)
- [LLDP_TLV_CHASSIS_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6)
- [LLDP_TLV_PORT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45)
- [LLDP_TLV_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c)
- [LLDP_TLV_PORT_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0)
- [LLDP_TLV_SYSTEM_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9)
- [LLDP_TLV_SYSTEM_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782)
- [LLDP_TLV_SYSTEM_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521)
- [LLDP_TLV_MANAGEMENT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5)
- [LLDP_TLV_ORG_SPECIFIC](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad)
- [net_lldp_chassis_tlv](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [type_length](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md#af81d3102ad0ec1f7ef76bb1533dcc7cd)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [subtype](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md#ad9d415f6a1e9018953728de1b529fd98)
- [value](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md#a37b7e81a670595d1c6c77a45bf9cfc73)
- [net_lldp_port_tlv](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md)
- [type_length](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md#a710beaeda2ddd7933464e07cb87a2bfe)
- [subtype](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md#a572a6fd721c68796a572410ac62f2f93)
- [value](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md#aecc83eaec39284b33c2e7cf07f0ffa05)
- [net_lldp_time_to_live_tlv](../network_core_model_reference/P108_net_lldp_time_to_live_tlv_结构体.md)
- [type_length](../network_core_model_reference/P108_net_lldp_time_to_live_tlv_结构体.md#a78b88d66184a0d25c413baf2fec495ab)
- [ttl](../network_core_model_reference/P108_net_lldp_time_to_live_tlv_结构体.md#ab967792a938a5d67f744e53be8d5f0fd)
- [net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)
- [chassis_id](../network_core_model_reference/P109_net_lldpdu_结构体.md#a1a1c80fe7462ddbfd84289735013834c)
- [port_id](../network_core_model_reference/P109_net_lldpdu_结构体.md#aa55adafc5528576017c37a28413bdaf9)
- [ttl](../network_core_model_reference/P109_net_lldpdu_结构体.md#afbe0618b6d849b8ee7b225844ac399df)
- [net_lldp_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga0efa1813c537dcf02e021db60049c284)
- [net_lldp_config_optional](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga9702175375a71eaab20f450291cb51ad)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [net_lldp_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga1e9fb662d7cdfc3c4c68cfd0312987cf)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_lldp_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga61845c96c65d6df83f422a68e31162cf)
- [iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)
- [net_lldp_set_lldpdu](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga961bc59567ffa2d5a4d21290d1d78407)
- [net_lldp_unset_lldpdu](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#gafdd1b4cea9f560597c31a0e42d5341e0)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_lldp_chassis_tlv::value](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md#a37b7e81a670595d1c6c77a45bf9cfc73)
- [net_lldp_chassis_tlv::subtype](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md#ad9d415f6a1e9018953728de1b529fd98)
- [net_lldp_chassis_tlv::type_length](../network_core_model_reference/P106_net_lldp_chassis_tlv_结构体.md#af81d3102ad0ec1f7ef76bb1533dcc7cd)
- [net_lldp_port_tlv::subtype](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md#a572a6fd721c68796a572410ac62f2f93)
- [net_lldp_port_tlv::type_length](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md#a710beaeda2ddd7933464e07cb87a2bfe)
- [net_lldp_port_tlv::value](../network_core_model_reference/P107_net_lldp_port_tlv_结构体.md#aecc83eaec39284b33c2e7cf07f0ffa05)
- [net_lldp_time_to_live_tlv::type_length](../network_core_model_reference/P108_net_lldp_time_to_live_tlv_结构体.md#a78b88d66184a0d25c413baf2fec495ab)
- [net_lldp_time_to_live_tlv::ttl](../network_core_model_reference/P108_net_lldp_time_to_live_tlv_结构体.md#ab967792a938a5d67f744e53be8d5f0fd)
- [net_lldpdu::chassis_id](../network_core_model_reference/P109_net_lldpdu_结构体.md#a1a1c80fe7462ddbfd84289735013834c)
- [net_lldpdu::port_id](../network_core_model_reference/P109_net_lldpdu_结构体.md#aa55adafc5528576017c37a28413bdaf9)
- [net_lldpdu::ttl](../network_core_model_reference/P109_net_lldpdu_结构体.md#afbe0618b6d849b8ee7b225844ac399df)
- [net_pkt::iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)

---

[上一章](P011_img_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P013_net_if.h_源码浏览.md)
