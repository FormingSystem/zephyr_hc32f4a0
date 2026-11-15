---
id: learning.zephyr-docs.api-source-device-reference.page-55
title: virtual.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_virtual.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h.html)。

## 55.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
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
<a id="l00105"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
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
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00341"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__ip__4__6_html_ga8b4cfadf1b284e52d6905ca88657b48a"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="agroup__net__if_html_gaeb8c703f273bc07ae9bb7a0d8bfe6f3d"></a>
<a id="agroup__net__l2_html_gac7db0cc6c56d371a5803873074ec2516"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__virtual_html_ga2aaba616ed4fecc27138d5aae58a634f"></a>
<a id="agroup__virtual_html_ga30f92f519a6f204ebeccd6053f17eaf0"></a>
<a id="agroup__virtual_html_ga5cba6ff65402b591a0e42d05f258671f"></a>
<a id="agroup__virtual_html_ga6c63773925ef7d96b0ba03d8978fd499"></a>
<a id="agroup__virtual_html_ga8f188f5c2f19960d7113da52aefe8091"></a>
<a id="agroup__virtual_html_gaa7ff8ebb83fe98a1dfd23f319317a8de"></a>
<a id="agroup__virtual_html_gabadf14eaa02978cde7030c99ddd3e279"></a>
<a id="agroup__virtual_html_gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071"></a>
<a id="agroup__virtual_html_gga8f188f5c2f19960d7113da52aefe8091a145ffaeae08793e4c93ea7be320efe2b"></a>
<a id="agroup__virtual_html_gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed"></a>
<a id="agroup__virtual_html_gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__linkaddr_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructvirtual__interface__api_html"></a>
<a id="astructvirtual__interface__api_html_a09a317009d31ac5e9340c3ca7d2191c4"></a>
<a id="astructvirtual__interface__api_html_a4ff5b92897926616778eb6fb696ebb16"></a>
<a id="astructvirtual__interface__api_html_a591f1b7df5313c4a225dceaa04b1eeae"></a>
<a id="astructvirtual__interface__api_html_a6f21e33e39caa00d51cca900a26f7070"></a>
<a id="astructvirtual__interface__api_html_a6fbfa013374bbafaa610b0a054d3a415"></a>
<a id="astructvirtual__interface__api_html_a753258a8929347877997ca5d6a76eb8c"></a>
<a id="astructvirtual__interface__api_html_a827cd13d885b7cc2f80eddd73e438e07"></a>
<a id="astructvirtual__interface__api_html_aee1250773938536ab28e129113073ae7"></a>
<a id="astructvirtual__interface__api_html_af28a6ed36799006d185fab9129c6c120"></a>
<a id="astructvirtual__interface__context_html"></a>
<a id="astructvirtual__interface__context_html_a493cef75dd5000b19eab5db156015c6e"></a>
<a id="astructvirtual__interface__context_html_a4a0aada1d7af7a86d2a4b12063f35c71"></a>
<a id="astructvirtual__interface__context_html_a7d53af8860331f23b8ff83ba0bfcaacf"></a>
<a id="astructvirtual__interface__context_html_a7e4699c462a1edfdb755833a9ab28d8f"></a>
<a id="astructvirtual__interface__context_html_ade8a686b9c002c064e2ae9e1815b6601"></a>
<a id="asys_2util_8h_html"></a>

```c


/*
 * Copyright (c) 2021 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_VIRTUAL_H_
#define ZEPHYR_INCLUDE_NET_VIRTUAL_H_

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/sys/atomic.h>

#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_pkt.h>

#include <zephyr/sys/util.h>
#include <zephyr/net/net_if.h>

#ifdef __cplusplus
extern "C" {
#endif


enum virtual_interface_caps {
        VIRTUAL_INTERFACE_IPIP = BIT(1),

        VIRTUAL_INTERFACE_VLAN = BIT(2),

        VIRTUAL_INTERFACE_BRIDGE = BIT(3),

        VIRTUAL_INTERFACE_VPN = BIT(4),

        /* Marker for capabilities - must be at the end of the enum.
         * It is here because the capability list cannot be empty.
         */
        VIRTUAL_INTERFACE_NUM_CAPS
};


enum virtual_interface_config_type {
        VIRTUAL_INTERFACE_CONFIG_TYPE_PEER_ADDRESS,
        VIRTUAL_INTERFACE_CONFIG_TYPE_MTU,
        VIRTUAL_INTERFACE_CONFIG_TYPE_LINK_TYPE,
        VIRTUAL_INTERFACE_CONFIG_TYPE_PRIVATE_KEY,
        VIRTUAL_INTERFACE_CONFIG_TYPE_PUBLIC_KEY,
};

struct virtual_interface_link_types {
        int count;
        uint16_t type[COND_CODE_1(CONFIG_NET_CAPTURE_COOKED_MODE,
                                  (CONFIG_NET_CAPTURE_COOKED_MODE_MAX_LINK_TYPES),
                                  (1))];
};

#if !defined(NET_VIRTUAL_MAX_PUBLIC_KEY_LEN)
#define NET_VIRTUAL_MAX_PUBLIC_KEY_LEN 32U
#endif

struct virtual_interface_config {
        net_sa_family_t family;
        union {
                struct net_in_addr peer4addr;
                struct net_in6_addr peer6addr;
                int mtu;
                struct virtual_interface_link_types link_types;
                struct {
                        size_t len;
                        uint8_t *data;
                } private_key;
                struct {
                        size_t len;
                        uint8_t data[NET_VIRTUAL_MAX_PUBLIC_KEY_LEN];
                } public_key;
        };
};

#if defined(CONFIG_NET_L2_VIRTUAL)
#define VIRTUAL_MAX_NAME_LEN CONFIG_NET_L2_VIRTUAL_MAX_NAME_LEN
#else
#define VIRTUAL_MAX_NAME_LEN 0
#endif

struct virtual_interface_api {
        struct net_if_api iface_api;

        enum virtual_interface_caps (*get_capabilities)(struct net_if *iface);

        int (*start)(const struct device *dev);

        int (*stop)(const struct device *dev);

        int (*send)(struct net_if *iface, struct net_pkt *pkt);

        enum net_verdict (*recv)(struct net_if *iface, struct net_pkt *pkt);

        int (*attach)(struct net_if *virtual_iface, struct net_if *iface);

        int (*set_config)(struct net_if *iface,
                          enum virtual_interface_config_type type,
                          const struct virtual_interface_config *config);

        int (*get_config)(struct net_if *iface,
                          enum virtual_interface_config_type type,
                          struct virtual_interface_config *config);
};

/* Make sure that the network interface API is properly setup inside
 * Virtual API struct (it is the first one).
 */
BUILD_ASSERT(offsetof(struct virtual_interface_api, iface_api) == 0);

struct virtual_interface_context {
        /* Keep track of contexts */
        sys_snode_t node;

        /* My virtual network interface */
        struct net_if *virtual_iface;

        struct net_if *iface;

        enum net_l2_flags virtual_l2_flags;

        bool is_init;

        struct net_linkaddr lladdr;

        char name[VIRTUAL_MAX_NAME_LEN];
};

int net_virtual_interface_attach(struct net_if *virtual_iface,
                                  struct net_if *iface);

struct net_if *net_virtual_get_iface(struct net_if *iface);

char *net_virtual_get_name(struct net_if *iface, char *buf, size_t len);

void net_virtual_set_name(struct net_if *iface, const char *name);

enum net_l2_flags net_virtual_set_flags(struct net_if *iface,
                                        enum net_l2_flags flags);

enum net_verdict net_virtual_input(struct net_if *input_iface,
                                   struct net_addr *remote_addr,
                                   struct net_pkt *pkt);


#if defined(CONFIG_NET_L2_VIRTUAL)
void net_virtual_init(struct net_if *iface);
#else
static inline void net_virtual_init(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#if defined(CONFIG_NET_L2_VIRTUAL)
void net_virtual_disable(struct net_if *iface);
#else
static inline void net_virtual_disable(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#if defined(CONFIG_NET_L2_VIRTUAL)
void net_virtual_enable(struct net_if *iface);
#else
static inline void net_virtual_enable(struct net_if *iface)
{
        ARG_UNUSED(iface);
}
#endif

#define VIRTUAL_L2_CTX_TYPE     struct virtual_interface_context

static inline enum virtual_interface_caps
net_virtual_get_iface_capabilities(struct net_if *iface)
{
        const struct device *dev = net_if_get_device(iface);
        const struct virtual_interface_api *virt;

        NET_ASSERT(dev != NULL);

        virt = (const struct virtual_interface_api *)dev->api;

        NET_ASSERT(virt != NULL);

        if (!virt->get_capabilities) {
                return (enum virtual_interface_caps)0;
        }

        return virt->get_capabilities(iface);
}

#define Z_NET_VIRTUAL_INTERFACE_INIT(node_id, dev_id, name, init_fn,    \
                                     pm, data, config, prio, api, mtu)  \
        Z_NET_DEVICE_INIT(node_id, dev_id, name, init_fn, pm, data,     \
                          config, prio, api, VIRTUAL_L2,                \
                          NET_L2_GET_CTX_TYPE(VIRTUAL_L2), mtu)

#define Z_NET_VIRTUAL_INTERFACE_INIT_INSTANCE(node_id, dev_id, name,    \
                                              inst, init_fn, pm, data,  \
                                              config, prio, api, mtu)   \
        Z_NET_DEVICE_INIT_INSTANCE(node_id, dev_id, name, inst,         \
                                   init_fn, pm, data,                   \
                                   config, prio, api, VIRTUAL_L2,       \
                                   NET_L2_GET_CTX_TYPE(VIRTUAL_L2), mtu)

#define NET_VIRTUAL_INTERFACE_INIT(dev_id, name, init_fn, pm, data,     \
                                   config, prio, api, mtu)              \
        Z_NET_VIRTUAL_INTERFACE_INIT(DT_INVALID_NODE, dev_id, name,     \
                                     init_fn, pm, data, config, prio,   \
                                     api, mtu)

#define NET_VIRTUAL_INTERFACE_INIT_INSTANCE(dev_id, name, inst,          \
                                            init_fn, pm, data,           \
                                            config, prio, api, mtu)      \
        Z_NET_VIRTUAL_INTERFACE_INIT_INSTANCE(DT_INVALID_NODE, dev_id,   \
                                              name, inst,                \
                                              init_fn, pm, data, config, \
                                              prio, api, mtu)


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_VIRTUAL_H_ */
```

## 55.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2021 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 53 行

能力标记（Capability Marker），必须位于枚举（Enum）的末尾。保留此标记是因为能力列表（Capability List）不能为空。

### 注释 3：原第 148 行

确保网络接口 API（Network Interface API）已在虚拟 API 结构体（Virtual API Struct）中正确设置；它是结构体中的第一个成员。

### 注释 4：原第 157 行

跟踪上下文（Contexts）。

### 注释 5：原第 160 行

我的虚拟网络接口（My Virtual Network Interface）。

### 注释 6：原第 407 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_VIRTUAL_H_`。

## 55.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [virtual_interface_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga8f188f5c2f19960d7113da52aefe8091)
- [VIRTUAL_INTERFACE_IPIP](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [VIRTUAL_INTERFACE_VLAN](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b)
- [VIRTUAL_INTERFACE_BRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed)
- [VIRTUAL_INTERFACE_VPN](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gga8f188f5c2f19960d7113da52aefe8091a145ffaeae08793e4c93ea7be320efe2b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [virtual_interface_api](../network_service_model_reference/P068_virtual_interface_api_结构体.md)
- [iface_api](../network_service_model_reference/P068_virtual_interface_api_结构体.md#aee1250773938536ab28e129113073ae7)
- [get_capabilities](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a827cd13d885b7cc2f80eddd73e438e07)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [start](../network_service_model_reference/P068_virtual_interface_api_结构体.md#af28a6ed36799006d185fab9129c6c120)
- [device](../device_reference/P002_设备对象结构.md)
- [stop](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a09a317009d31ac5e9340c3ca7d2191c4)
- [send](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a6fbfa013374bbafaa610b0a054d3a415)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [recv](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a6f21e33e39caa00d51cca900a26f7070)
- [attach](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a753258a8929347877997ca5d6a76eb8c)
- [set_config](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a591f1b7df5313c4a225dceaa04b1eeae)
- [get_config](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a4ff5b92897926616778eb6fb696ebb16)
- [virtual_interface_context](../network_service_model_reference/P069_virtual_interface_context_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [iface](../network_service_model_reference/P069_virtual_interface_context_结构体.md#a4a0aada1d7af7a86d2a4b12063f35c71)
- [net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)
- [virtual_l2_flags](../network_service_model_reference/P069_virtual_interface_context_结构体.md#a493cef75dd5000b19eab5db156015c6e)
- [is_init](../network_service_model_reference/P069_virtual_interface_context_结构体.md#a7e4699c462a1edfdb755833a9ab28d8f)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [lladdr](../network_service_model_reference/P069_virtual_interface_context_结构体.md#ade8a686b9c002c064e2ae9e1815b6601)
- [name](../network_service_model_reference/P069_virtual_interface_context_结构体.md#a7d53af8860331f23b8ff83ba0bfcaacf)
- [net_virtual_interface_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga5cba6ff65402b591a0e42d05f258671f)
- [net_virtual_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gabadf14eaa02978cde7030c99ddd3e279)
- [net_virtual_get_name](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gaa7ff8ebb83fe98a1dfd23f319317a8de)
- [net_virtual_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga2aaba616ed4fecc27138d5aae58a634f)
- [net_virtual_set_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga30f92f519a6f204ebeccd6053f17eaf0)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_virtual_input](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#ga6c63773925ef7d96b0ba03d8978fd499)
- [net_if_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [virtual_interface_api::stop](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a09a317009d31ac5e9340c3ca7d2191c4)
- [virtual_interface_api::get_config](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a4ff5b92897926616778eb6fb696ebb16)
- [virtual_interface_api::set_config](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a591f1b7df5313c4a225dceaa04b1eeae)
- [virtual_interface_api::recv](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a6f21e33e39caa00d51cca900a26f7070)
- [virtual_interface_api::send](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a6fbfa013374bbafaa610b0a054d3a415)
- [virtual_interface_api::attach](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a753258a8929347877997ca5d6a76eb8c)
- [virtual_interface_api::get_capabilities](../network_service_model_reference/P068_virtual_interface_api_结构体.md#a827cd13d885b7cc2f80eddd73e438e07)
- [virtual_interface_api::iface_api](../network_service_model_reference/P068_virtual_interface_api_结构体.md#aee1250773938536ab28e129113073ae7)
- [virtual_interface_api::start](../network_service_model_reference/P068_virtual_interface_api_结构体.md#af28a6ed36799006d185fab9129c6c120)
- [virtual_interface_context::virtual_l2_flags](../network_service_model_reference/P069_virtual_interface_context_结构体.md#a493cef75dd5000b19eab5db156015c6e)
- [virtual_interface_context::iface](../network_service_model_reference/P069_virtual_interface_context_结构体.md#a4a0aada1d7af7a86d2a4b12063f35c71)
- [virtual_interface_context::name](../network_service_model_reference/P069_virtual_interface_context_结构体.md#a7d53af8860331f23b8ff83ba0bfcaacf)
- [virtual_interface_context::is_init](../network_service_model_reference/P069_virtual_interface_context_结构体.md#a7e4699c462a1edfdb755833a9ab28d8f)
- [virtual_interface_context::lladdr](../network_service_model_reference/P069_virtual_interface_context_结构体.md#ade8a686b9c002c064e2ae9e1815b6601)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P054_veml7700.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P056_winstream.h_源码浏览.md)
