---
id: learning.zephyr-docs.api-source-reference.page-575
title: net_l2.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__l2_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第575章\_net\_l2.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__l2_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__l2_8h.html)。

## 575.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
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
<a id="l00162"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="acapture_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__ip__4__6_html_gaf06819bf427cc58be1229b27b373ca31"></a>
<a id="agroup__net__capture_html_ga54aba9a796ba312554ef9589b879f204"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="agroup__net__l2_html_gac7db0cc6c56d371a5803873074ec2516"></a>
<a id="agroup__net__l2_html_ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1"></a>
<a id="agroup__net__l2_html_ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1"></a>
<a id="agroup__net__l2_html_ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8"></a>
<a id="agroup__net__l2_html_ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="anet__buf_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__l2_html"></a>
<a id="astructnet__l2_html_a17d649732c3bb6bf9cc77a4939eb8801"></a>
<a id="astructnet__l2_html_a1faa6e5b0c9228dd52c64fc7f2fd8036"></a>
<a id="astructnet__l2_html_a492c5c75801b9c8784c9322805869334"></a>
<a id="astructnet__l2_html_a5d42c51eb8dc4d6a990aa9ff88a66b94"></a>
<a id="astructnet__l2_html_a9aed44777aa01efcd45874679c6ea1c2"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__pkt_html_a7590eeacf06469206cb7e7949acfa7b2"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_NET_L2_H_
#define ZEPHYR_INCLUDE_NET_NET_L2_H_

#include <zephyr/device.h>
#include <zephyr/net_buf.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/capture.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif


struct net_if;

enum net_l2_flags {
        NET_L2_MULTICAST                        = BIT(0),

        NET_L2_MULTICAST_SKIP_JOIN_SOLICIT_NODE = BIT(1),

        NET_L2_PROMISC_MODE                     = BIT(2),

        NET_L2_POINT_TO_POINT                   = BIT(3),
} __packed;

struct net_l2 {
        enum net_verdict (*recv)(struct net_if *iface, struct net_pkt *pkt);

        int (*send)(struct net_if *iface, struct net_pkt *pkt);

        int (*enable)(struct net_if *iface, bool state);

        enum net_l2_flags (*get_flags)(struct net_if *iface);

        int (*alloc)(struct net_if *iface, struct net_pkt *pkt,
                     size_t size, enum net_ip_protocol proto,
                     k_timeout_t timeout);
};

#define NET_L2_GET_NAME(_name) _net_l2_##_name
#define NET_L2_DECLARE_PUBLIC(_name)                                    \
        extern const struct net_l2 NET_L2_GET_NAME(_name)
#define NET_L2_GET_CTX_TYPE(_name) _name##_CTX_TYPE

#define VIRTUAL_L2              VIRTUAL
NET_L2_DECLARE_PUBLIC(VIRTUAL_L2);

#define DUMMY_L2                DUMMY
#define DUMMY_L2_CTX_TYPE       void*
NET_L2_DECLARE_PUBLIC(DUMMY_L2);

#define OFFLOADED_NETDEV_L2 OFFLOADED_NETDEV
NET_L2_DECLARE_PUBLIC(OFFLOADED_NETDEV_L2);

#define ETHERNET_L2             ETHERNET
NET_L2_DECLARE_PUBLIC(ETHERNET_L2);

#define PPP_L2                  PPP
NET_L2_DECLARE_PUBLIC(PPP_L2);

#define IEEE802154_L2           IEEE802154
NET_L2_DECLARE_PUBLIC(IEEE802154_L2);

#define OPENTHREAD_L2           OPENTHREAD
NET_L2_DECLARE_PUBLIC(OPENTHREAD_L2);

#define CANBUS_RAW_L2           CANBUS_RAW
#define CANBUS_RAW_L2_CTX_TYPE  void*
NET_L2_DECLARE_PUBLIC(CANBUS_RAW_L2);

#ifdef CONFIG_NET_L2_CUSTOM_IEEE802154
#ifndef CUSTOM_IEEE802154_L2
#define CUSTOM_IEEE802154_L2    CUSTOM_IEEE802154
#endif
#define CUSTOM_IEEE802154_L2_CTX_TYPE   void*
NET_L2_DECLARE_PUBLIC(CUSTOM_IEEE802154_L2);
#endif /* CONFIG_NET_L2_CUSTOM_IEEE802154 */

#define NET_L2_INIT(_name, _recv_fn, _send_fn, _enable_fn, _get_flags_fn, ...) \
        const STRUCT_SECTION_ITERABLE(net_l2,                           \
                                      NET_L2_GET_NAME(_name)) = {       \
                .recv = (_recv_fn),                                     \
                .send = (_send_fn),                                     \
                .enable = (_enable_fn),                                 \
                .get_flags = (_get_flags_fn),                           \
                .alloc = COND_CODE_0(NUM_VA_ARGS_LESS_1(LIST_DROP_EMPTY(__VA_ARGS__, _)), \
                                     (NULL),                            \
                                     (GET_ARG_N(1, __VA_ARGS__))),      \
        }

#define NET_L2_GET_DATA(name, sfx) _net_l2_data_##name##sfx

#define NET_L2_DATA_INIT(name, sfx, ctx_type)                           \
        static ctx_type NET_L2_GET_DATA(name, sfx) __used;

typedef int (*net_l2_send_t)(const struct device *dev, struct net_pkt *pkt);

static inline int net_l2_send(net_l2_send_t send_fn,
                              const struct device *dev,
                              struct net_if *iface,
                              struct net_pkt *pkt)
{
        net_capture_pkt(iface, pkt);

        return send_fn(dev, pkt);
}



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_NET_L2_H_ */
```

## 575.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 130 行

条件编译配置（Configuration）标记：`CONFIG_NET_L2_CUSTOM_IEEE802154`。

### 注释 3：原第 171 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_L2_H_`。

## 575.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__l2_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/capture.h](https://docs.zephyrproject.org/latest/doxygen/html/capture_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)
- [NET_L2_MULTICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [NET_L2_MULTICAST_SKIP_JOIN_SOLICIT_NODE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1)
- [NET_L2_PROMISC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8)
- [NET_L2_POINT_TO_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1)
- [net_l2](../network_core_model_reference/P103_net_l2_结构体.md)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [recv](../network_core_model_reference/P103_net_l2_结构体.md#a1faa6e5b0c9228dd52c64fc7f2fd8036)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [send](../network_core_model_reference/P103_net_l2_结构体.md#a17d649732c3bb6bf9cc77a4939eb8801)
- [enable](../network_core_model_reference/P103_net_l2_结构体.md#a5d42c51eb8dc4d6a990aa9ff88a66b94)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [get_flags](../network_core_model_reference/P103_net_l2_结构体.md#a492c5c75801b9c8784c9322805869334)
- [alloc](../network_core_model_reference/P103_net_l2_结构体.md#a9aed44777aa01efcd45874679c6ea1c2)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [device](../device_reference/P002_设备对象结构.md)
- [iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)
- [net_capture_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga54aba9a796ba312554ef9589b879f204)
- [capture.h](https://docs.zephyrproject.org/latest/doxygen/html/capture_8h.html)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_l2::send](../network_core_model_reference/P103_net_l2_结构体.md#a17d649732c3bb6bf9cc77a4939eb8801)
- [net_l2::recv](../network_core_model_reference/P103_net_l2_结构体.md#a1faa6e5b0c9228dd52c64fc7f2fd8036)
- [net_l2::get_flags](../network_core_model_reference/P103_net_l2_结构体.md#a492c5c75801b9c8784c9322805869334)
- [net_l2::enable](../network_core_model_reference/P103_net_l2_结构体.md#a5d42c51eb8dc4d6a990aa9ff88a66b94)
- [net_l2::alloc](../network_core_model_reference/P103_net_l2_结构体.md#a9aed44777aa01efcd45874679c6ea1c2)
- [net_pkt::iface](../network_core_model_reference/P114_net_pkt_结构体.md#a7590eeacf06469206cb7e7949acfa7b2)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P574_counter.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P576_net_linkaddr.h_源码浏览.md)
