---
id: learning.zephyr-docs.api-source-device-reference.page-19
title: gptp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_gptp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h.html)。

## 19.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
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
<a id="l00047"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
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
<a id="l00123"></a>
<a id="foldopen00127"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="foldopen00136"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00242"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="agroup__gptp_html_ga06ddd41c7adf9e387d1b23bcdfccbddc"></a>
<a id="agroup__gptp_html_ga29bf157d06a5ec5bb5a2a8a0e986709d"></a>
<a id="agroup__gptp_html_ga40121c2957d58b0b5bb4468eac5de259"></a>
<a id="agroup__gptp_html_ga4af3bf8e0ef4e3833260b6365b2b1e2f"></a>
<a id="agroup__gptp_html_ga55d95859e5ec586cb2341929901220dd"></a>
<a id="agroup__gptp_html_ga5b46fb7bbe1a380e3c327c8f5abbabeb"></a>
<a id="agroup__gptp_html_ga9a8e2ccf20d0430b4e62f3302462c6eb"></a>
<a id="agroup__gptp_html_ga9b27c9a741fb0ca72eff78e334e629fe"></a>
<a id="agroup__gptp_html_ga9bd009e6027d57cd9950b0387d727e3d"></a>
<a id="agroup__gptp_html_gaad2282df9cbf7f05f557285323af8f07"></a>
<a id="agroup__gptp_html_gade00e0d8398f015031d7f77317e4b97b"></a>
<a id="agroup__gptp_html_gae4c3aac6b88e9ce21a32ba3263b9ad59"></a>
<a id="agroup__gptp_html_gaf4366741c39144e244d7555582b3b62c"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="amath_8h_html"></a>
<a id="anet__core_8h_html"></a>
<a id="aptp__time_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructgptp__clk__src__time__invoke__params_html"></a>
<a id="astructgptp__clk__src__time__invoke__params_html_a990360a4fdc5bdc8f6626e9dfdc05563"></a>
<a id="astructgptp__clk__src__time__invoke__params_html_aaf1ca90ce4e1b216c2edbb9fa72b044a"></a>
<a id="astructgptp__clk__src__time__invoke__params_html_ab2328d1a7458ccc8e7fe771e50b463eb"></a>
<a id="astructgptp__clk__src__time__invoke__params_html_ada4c313104488059a520d4a2ffff33b4"></a>
<a id="astructgptp__flags_html"></a>
<a id="astructgptp__flags_html_a36871fbae0484379b00c415affdb3f9d"></a>
<a id="astructgptp__flags_html_a90b2862e78ece1b9b7f5109f5cd5f0fd"></a>
<a id="astructgptp__hdr_html"></a>
<a id="astructgptp__hdr_html_a38d80a7ef0ed94c50baf6285b735cf4d"></a>
<a id="astructgptp__hdr_html_a435a37858ba67222f22d4cfde3322511"></a>
<a id="astructgptp__hdr_html_a4c6eadb27839a3b45461df5e2078b5a7"></a>
<a id="astructgptp__hdr_html_a50f192fb70ae8633c80fa5eeb178f852"></a>
<a id="astructgptp__hdr_html_a5fab00d293c3fb38fedf483b11f72890"></a>
<a id="astructgptp__hdr_html_a68f6642239b801f2fe602a4331743d83"></a>
<a id="astructgptp__hdr_html_a7e89c039b956b5fa7229b58dde855a20"></a>
<a id="astructgptp__hdr_html_aab942e44507bcff9af8e0a168b9fb810"></a>
<a id="astructgptp__hdr_html_ab58626c44b57827266606a4b85bf25cc"></a>
<a id="astructgptp__hdr_html_ac6340bd434fad75f7faa8386bb591412"></a>
<a id="astructgptp__hdr_html_acc57b0662f64bda3bc21c9c8b6286052"></a>
<a id="astructgptp__hdr_html_adbc9eed0fdaf07410542780c3794d642"></a>
<a id="astructgptp__hdr_html_aec4214f5392123bb3cd328b94aea8d2a"></a>
<a id="astructgptp__hdr_html_af9f79833695719ef42ecf0536bdfc317"></a>
<a id="astructgptp__phase__dis__cb_html"></a>
<a id="astructgptp__phase__dis__cb_html_a8294a9abac55d1f4406923ea4e8ed144"></a>
<a id="astructgptp__phase__dis__cb_html_a9801de29992ae2f23bbe89c417d58fe3"></a>
<a id="astructgptp__port__identity_html"></a>
<a id="astructgptp__port__identity_html_a5a0d4038aa88792290bc4619379ee48f"></a>
<a id="astructgptp__port__identity_html_a6e8473ae6ecb4ec35e3a6b5d79851fc3"></a>
<a id="astructgptp__scaled__ns_html"></a>
<a id="astructgptp__scaled__ns_html_ac1e95f32bdb1a98f945d9d05a28e8f7f"></a>
<a id="astructgptp__scaled__ns_html_af35add15383b49b677e604d61b3d9739"></a>
<a id="astructgptp__uscaled__ns_html"></a>
<a id="astructgptp__uscaled__ns_html_a11cd4f2cc15731ba91dab742fcea248f"></a>
<a id="astructgptp__uscaled__ns_html_ae374e99c81753ecd26ff9a7cac35dfa4"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__ptp__extended__time_html"></a>
<a id="astructnet__ptp__time_html"></a>

```c
/*
 * Copyright (c) 2017 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_GPTP_H_
#define ZEPHYR_INCLUDE_NET_GPTP_H_


#include <zephyr/net/net_core.h>
#include <zephyr/net/ptp_time.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif


#define GPTP_OFFSET_SCALED_LOG_VAR_UNKNOWN 0x436A

#define GPTP_PRIORITY1_NON_GM_CAPABLE      255
#define GPTP_PRIORITY1_GM_CAPABLE          248

#if defined(CONFIG_NET_GPTP_BMCA_PRIORITY2)
#define GPTP_PRIORITY2_DEFAULT             CONFIG_NET_GPTP_BMCA_PRIORITY2
#else
#define GPTP_PRIORITY2_DEFAULT             248
#endif


struct gptp_scaled_ns {
        int32_t high;

        int64_t low;
} __packed;

struct gptp_uscaled_ns {
        uint32_t high;

        uint64_t low;
} __packed;


#if defined(CONFIG_NEWLIB_LIBC)
#include <math.h>

#define GPTP_POW2(exp) pow(2, exp)
#else

static inline double gptp_pow2(int exp)
{
        double res;

        if (exp >= 0) {
                res = 1 << exp;
        } else {
                res = 1.0;

                while (exp++) {
                        res /= 2;
                }
        }

        return res;
}

#define GPTP_POW2(exp) gptp_pow2(exp)
#endif

/* Pre-calculated constants */
/* 2^16 */
#define GPTP_POW2_16    65536.0
/* 2^41 */
#define GPTP_POW2_41    2199023255552.0

/* Message types. Event messages have BIT(3) set to 0, and general messages
 * have that bit set to 1. IEEE 802.1AS chapter 10.5.2.2.2
 */
#define GPTP_SYNC_MESSAGE                0x00
#define GPTP_DELAY_REQ_MESSAGE           0x01
#define GPTP_PATH_DELAY_REQ_MESSAGE      0x02
#define GPTP_PATH_DELAY_RESP_MESSAGE     0x03
#define GPTP_FOLLOWUP_MESSAGE            0x08
#define GPTP_DELAY_RESP_MESSAGE          0x09
#define GPTP_PATH_DELAY_FOLLOWUP_MESSAGE 0x0a
#define GPTP_ANNOUNCE_MESSAGE            0x0b
#define GPTP_SIGNALING_MESSAGE           0x0c
#define GPTP_MANAGEMENT_MESSAGE          0x0d

#define GPTP_IS_EVENT_MSG(msg_type)      (!((msg_type) & BIT(3)))

#define GPTP_CLOCK_ID_LEN                8


struct gptp_port_identity {
        uint8_t clk_id[GPTP_CLOCK_ID_LEN];

        uint16_t port_number;
} __packed;

struct gptp_flags {
        union {
                uint8_t octets[2];

                uint16_t all;
        };
} __packed;

struct gptp_hdr {
        uint8_t message_type:4;

        uint8_t transport_specific:4;

        uint8_t ptp_version:4;

        uint8_t reserved0:4;

        uint16_t message_length;

        uint8_t domain_number;

        uint8_t reserved1;

        struct gptp_flags flags;

        int64_t correction_field;

        uint32_t reserved2;

        struct gptp_port_identity port_id;

        uint16_t sequence_id;

        uint8_t control;

        int8_t log_msg_interval;
} __packed;


#define GPTP_GET_CURRENT_TIME_USCALED_NS(port, uscaled_ns_ptr)          \
        do {                                                            \
                (uscaled_ns_ptr)->low =                                 \
                        gptp_get_current_time_nanosecond(port) << 16;   \
                (uscaled_ns_ptr)->high = 0;                             \
        } while (false)


typedef void (*gptp_phase_dis_callback_t)(
        uint8_t *gm_identity,
        uint16_t *time_base,
        struct gptp_scaled_ns *last_gm_ph_change,
        double *last_gm_freq_change);

struct gptp_phase_dis_cb {
        sys_snode_t node;

        gptp_phase_dis_callback_t cb;
};

struct gptp_clk_src_time_invoke_params {
        double last_gm_freq_change;

        struct net_ptp_extended_time src_time;

        struct gptp_scaled_ns last_gm_phase_change;

        uint16_t time_base_indicator;
};


#if defined(CONFIG_NET_GPTP)
void net_gptp_init(void);
#else
static inline void net_gptp_init(void)
{
}
#endif /* CONFIG_NET_GPTP */


void gptp_register_phase_dis_cb(struct gptp_phase_dis_cb *phase_dis,
                                gptp_phase_dis_callback_t cb);

void gptp_unregister_phase_dis_cb(struct gptp_phase_dis_cb *phase_dis);

void gptp_call_phase_dis_cb(void);

int gptp_event_capture(struct net_ptp_time *slave_time, bool *gm_present);

char *gptp_sprint_clock_id(const uint8_t *clk_id, char *output,
                           size_t output_len);

typedef void (*gptp_port_cb_t)(int port, struct net_if *iface,
                               void *user_data);

void gptp_foreach_port(gptp_port_cb_t cb, void *user_data);

int gptp_get_port_number(struct net_if *iface);

int gptp_set_port_number(struct net_if *iface, uint16_t port);

struct gptp_domain *gptp_get_domain(void);

void gptp_clk_src_time_invoke(struct gptp_clk_src_time_invoke_params *arg);

struct gptp_hdr *gptp_get_hdr(struct net_pkt *pkt);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_GPTP_H_ */
```

## 19.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 98 行

预先计算的常量（Pre-Calculated Constants）。

### 注释 3：原第 99 行

常量（Constant）：`2^16`。

### 注释 4：原第 101 行

常量（Constant）：`2^41`。

### 注释 5：原第 104 行

消息类型（Message Types）。事件消息（Event Messages）的 `BIT(3)` 为 0，一般消息（General Messages）的该位为 1。参见 IEEE 802.1AS 第 10.5.2.2.2 节。

### 注释 6：原第 264 行

条件编译配置（Configuration）标记：`CONFIG_NET_GPTP`。

### 注释 7：原第 383 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_GPTP_H_`。

## 19.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h.html)
- [zephyr/net/net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [zephyr/net/ptp_time.h](../api_file_runtime_reference/P052_zephyr__net__ptp_time.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [gptp_scaled_ns](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [high](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md#af35add15383b49b677e604d61b3d9739)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [low](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md#ac1e95f32bdb1a98f945d9d05a28e8f7f)
- [gptp_uscaled_ns](../network_service_model_reference/P021_gptp_uscaled_ns_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [high](../network_service_model_reference/P021_gptp_uscaled_ns_结构体.md#a11cd4f2cc15731ba91dab742fcea248f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [low](../network_service_model_reference/P021_gptp_uscaled_ns_结构体.md#ae374e99c81753ecd26ff9a7cac35dfa4)
- [math.h](../api_file_reference/P196_____w__zephyr__zephyr__lib__libc__minimal__include__math.h_文件参考.md)
- [gptp_port_identity](../network_service_model_reference/P019_gptp_port_identity_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [clk_id](../network_service_model_reference/P019_gptp_port_identity_结构体.md#a6e8473ae6ecb4ec35e3a6b5d79851fc3)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [port_number](../network_service_model_reference/P019_gptp_port_identity_结构体.md#a5a0d4038aa88792290bc4619379ee48f)
- [gptp_flags](../network_service_model_reference/P016_gptp_flags_结构体.md)
- [octets](../network_service_model_reference/P016_gptp_flags_结构体.md#a90b2862e78ece1b9b7f5109f5cd5f0fd)
- [all](../network_service_model_reference/P016_gptp_flags_结构体.md#a36871fbae0484379b00c415affdb3f9d)
- [gptp_hdr](../network_service_model_reference/P017_gptp_hdr_结构体.md)
- [message_type](../network_service_model_reference/P017_gptp_hdr_结构体.md#adbc9eed0fdaf07410542780c3794d642)
- [transport_specific](../network_service_model_reference/P017_gptp_hdr_结构体.md#acc57b0662f64bda3bc21c9c8b6286052)
- [ptp_version](../network_service_model_reference/P017_gptp_hdr_结构体.md#aab942e44507bcff9af8e0a168b9fb810)
- [reserved0](../network_service_model_reference/P017_gptp_hdr_结构体.md#af9f79833695719ef42ecf0536bdfc317)
- [message_length](../network_service_model_reference/P017_gptp_hdr_结构体.md#ab58626c44b57827266606a4b85bf25cc)
- [domain_number](../network_service_model_reference/P017_gptp_hdr_结构体.md#a435a37858ba67222f22d4cfde3322511)
- [reserved1](../network_service_model_reference/P017_gptp_hdr_结构体.md#aec4214f5392123bb3cd328b94aea8d2a)
- [flags](../network_service_model_reference/P017_gptp_hdr_结构体.md#a4c6eadb27839a3b45461df5e2078b5a7)
- [correction_field](../network_service_model_reference/P017_gptp_hdr_结构体.md#a38d80a7ef0ed94c50baf6285b735cf4d)
- [reserved2](../network_service_model_reference/P017_gptp_hdr_结构体.md#ac6340bd434fad75f7faa8386bb591412)
- [port_id](../network_service_model_reference/P017_gptp_hdr_结构体.md#a7e89c039b956b5fa7229b58dde855a20)
- [sequence_id](../network_service_model_reference/P017_gptp_hdr_结构体.md#a50f192fb70ae8633c80fa5eeb178f852)
- [control](../network_service_model_reference/P017_gptp_hdr_结构体.md#a68f6642239b801f2fe602a4331743d83)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [log_msg_interval](../network_service_model_reference/P017_gptp_hdr_结构体.md#a5fab00d293c3fb38fedf483b11f72890)
- [gptp_phase_dis_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gade00e0d8398f015031d7f77317e4b97b)
- [gptp_phase_dis_cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md#a9801de29992ae2f23bbe89c417d58fe3)
- [cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md#a8294a9abac55d1f4406923ea4e8ed144)
- [gptp_clk_src_time_invoke_params](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md)
- [last_gm_freq_change](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md#aaf1ca90ce4e1b216c2edbb9fa72b044a)
- [net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)
- [src_time](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md#a990360a4fdc5bdc8f6626e9dfdc05563)
- [last_gm_phase_change](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md#ab2328d1a7458ccc8e7fe771e50b463eb)
- [time_base_indicator](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md#ada4c313104488059a520d4a2ffff33b4)
- [gptp_register_phase_dis_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gaad2282df9cbf7f05f557285323af8f07)
- [gptp_unregister_phase_dis_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga55d95859e5ec586cb2341929901220dd)
- [gptp_call_phase_dis_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga29bf157d06a5ec5bb5a2a8a0e986709d)
- [gptp_event_capture](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9a8e2ccf20d0430b4e62f3302462c6eb)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [gptp_sprint_clock_id](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga40121c2957d58b0b5bb4468eac5de259)
- [gptp_port_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9bd009e6027d57cd9950b0387d727e3d)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [gptp_foreach_port](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga06ddd41c7adf9e387d1b23bcdfccbddc)
- [gptp_get_port_number](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gaf4366741c39144e244d7555582b3b62c)
- [gptp_set_port_number](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga4af3bf8e0ef4e3833260b6365b2b1e2f)
- [gptp_get_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gae4c3aac6b88e9ce21a32ba3263b9ad59)
- [gptp_clk_src_time_invoke](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9b27c9a741fb0ca72eff78e334e629fe)
- [gptp_get_hdr](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga5b46fb7bbe1a380e3c327c8f5abbabeb)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)
- [ptp_time.h](../api_file_runtime_reference/P052_zephyr__net__ptp_time.h_文件参考.md)
- [gptp_clk_src_time_invoke_params::src_time](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md#a990360a4fdc5bdc8f6626e9dfdc05563)
- [gptp_clk_src_time_invoke_params::last_gm_freq_change](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md#aaf1ca90ce4e1b216c2edbb9fa72b044a)
- [gptp_clk_src_time_invoke_params::last_gm_phase_change](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md#ab2328d1a7458ccc8e7fe771e50b463eb)
- [gptp_clk_src_time_invoke_params::time_base_indicator](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md#ada4c313104488059a520d4a2ffff33b4)
- [gptp_flags::all](../network_service_model_reference/P016_gptp_flags_结构体.md#a36871fbae0484379b00c415affdb3f9d)
- [gptp_flags::octets](../network_service_model_reference/P016_gptp_flags_结构体.md#a90b2862e78ece1b9b7f5109f5cd5f0fd)
- [gptp_hdr::correction_field](../network_service_model_reference/P017_gptp_hdr_结构体.md#a38d80a7ef0ed94c50baf6285b735cf4d)
- [gptp_hdr::domain_number](../network_service_model_reference/P017_gptp_hdr_结构体.md#a435a37858ba67222f22d4cfde3322511)
- [gptp_hdr::flags](../network_service_model_reference/P017_gptp_hdr_结构体.md#a4c6eadb27839a3b45461df5e2078b5a7)
- [gptp_hdr::sequence_id](../network_service_model_reference/P017_gptp_hdr_结构体.md#a50f192fb70ae8633c80fa5eeb178f852)
- [gptp_hdr::log_msg_interval](../network_service_model_reference/P017_gptp_hdr_结构体.md#a5fab00d293c3fb38fedf483b11f72890)
- [gptp_hdr::control](../network_service_model_reference/P017_gptp_hdr_结构体.md#a68f6642239b801f2fe602a4331743d83)
- [gptp_hdr::port_id](../network_service_model_reference/P017_gptp_hdr_结构体.md#a7e89c039b956b5fa7229b58dde855a20)
- [gptp_hdr::ptp_version](../network_service_model_reference/P017_gptp_hdr_结构体.md#aab942e44507bcff9af8e0a168b9fb810)
- [gptp_hdr::message_length](../network_service_model_reference/P017_gptp_hdr_结构体.md#ab58626c44b57827266606a4b85bf25cc)
- [gptp_hdr::reserved2](../network_service_model_reference/P017_gptp_hdr_结构体.md#ac6340bd434fad75f7faa8386bb591412)
- [gptp_hdr::transport_specific](../network_service_model_reference/P017_gptp_hdr_结构体.md#acc57b0662f64bda3bc21c9c8b6286052)
- [gptp_hdr::message_type](../network_service_model_reference/P017_gptp_hdr_结构体.md#adbc9eed0fdaf07410542780c3794d642)
- [gptp_hdr::reserved1](../network_service_model_reference/P017_gptp_hdr_结构体.md#aec4214f5392123bb3cd328b94aea8d2a)
- [gptp_hdr::reserved0](../network_service_model_reference/P017_gptp_hdr_结构体.md#af9f79833695719ef42ecf0536bdfc317)
- [gptp_phase_dis_cb::cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md#a8294a9abac55d1f4406923ea4e8ed144)
- [gptp_phase_dis_cb::node](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md#a9801de29992ae2f23bbe89c417d58fe3)
- [gptp_port_identity::port_number](../network_service_model_reference/P019_gptp_port_identity_结构体.md#a5a0d4038aa88792290bc4619379ee48f)
- [gptp_port_identity::clk_id](../network_service_model_reference/P019_gptp_port_identity_结构体.md#a6e8473ae6ecb4ec35e3a6b5d79851fc3)
- [gptp_scaled_ns::low](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md#ac1e95f32bdb1a98f945d9d05a28e8f7f)
- [gptp_scaled_ns::high](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md#af35add15383b49b677e604d61b3d9739)
- [gptp_uscaled_ns::high](../network_service_model_reference/P021_gptp_uscaled_ns_结构体.md#a11cd4f2cc15731ba91dab742fcea248f)
- [gptp_uscaled_ns::low](../network_service_model_reference/P021_gptp_uscaled_ns_结构体.md#ae374e99c81753ecd26ff9a7cac35dfa4)

---

[上一章](P018_gd32f4xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P020_hci_vs.h_源码浏览.md)
