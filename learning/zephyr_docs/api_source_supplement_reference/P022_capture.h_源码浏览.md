---
id: learning.zephyr-docs.api-source-supplement-reference.page-22
title: capture.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/capture_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_capture.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/capture_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/capture_8h.html)。

## 22.1\_原始可见代码（Source Code）

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
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00089"></a>
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
<a id="foldopen00115"></a>
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
<a id="foldopen00138"></a>
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
<a id="foldopen00168"></a>
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
<a id="l00183"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="foldopen00222"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="foldopen00255"></a>
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
<a id="foldopen00266"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="foldopen00291"></a>
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
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="foldopen00325"></a>
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
<a id="foldopen00339"></a>
<a id="l00339"></a>
<a id="l00341"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00347"></a>
<a id="l00349"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="foldopen00375"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__device__model_html_ga15386ca9ab38f3e30183c18f604fa835"></a>
<a id="agroup__net__capture_html_ga32c66260fc888dcd38b6a3cffca3b951"></a>
<a id="agroup__net__capture_html_ga54aba9a796ba312554ef9589b879f204"></a>
<a id="agroup__net__capture_html_ga651987b8b1e713865cff01412934f3cc"></a>
<a id="agroup__net__capture_html_ga7a56719068938c34c9c6149296074d01"></a>
<a id="agroup__net__capture_html_ga8b6c9d07ae0e1ee906129cb2f0b411ec"></a>
<a id="agroup__net__capture_html_ga9f567c3392745ea24f70f736c8973584"></a>
<a id="agroup__net__capture_html_gab280c0c6cc607bdb07211a9450eae262"></a>
<a id="agroup__net__capture_html_gab68bfc9510ce093447eba513c8e8d288"></a>
<a id="agroup__net__capture_html_gabd019c0856ed170da5b74f153f12768a"></a>
<a id="agroup__net__capture_html_gad67ec9d34a7e4f85a4f507b30981fad8"></a>
<a id="agroup__net__capture_html_gaec06d9e76514c8fd2d7bc4e738fa8e5c"></a>
<a id="agroup__net__capture_html_gaf449c308080dc126e2e7c03b38d2a0aa"></a>
<a id="agroup__net__capture_html_gga8b6c9d07ae0e1ee906129cb2f0b411eca29604d550ee5aaf22808e7fa9c93526d"></a>
<a id="agroup__net__capture_html_gga8b6c9d07ae0e1ee906129cb2f0b411eca9d0c1f31a408bc6b56b106e356f0be88"></a>
<a id="agroup__net__capture_html_gga8b6c9d07ae0e1ee906129cb2f0b411ecac19ae62e8505d342c1c2351e61a64ce5"></a>
<a id="agroup__net__capture_html_gga8b6c9d07ae0e1ee906129cb2f0b411ecae4772d47a9130a69f0477d4e8ed64264"></a>
<a id="agroup__net__capture_html_gga8b6c9d07ae0e1ee906129cb2f0b411ecaf12e4a87c90d5fa6ced21051dac65631"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="akernel_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html_a16485de18b1ec93572e5d74b4a04e42f"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>
<a id="astructnet__capture__cooked_html"></a>
<a id="astructnet__capture__cooked_html_a17d3b9b877451bb809e6b23314117952"></a>
<a id="astructnet__capture__cooked_html_a30df8c6901fb132c77482b08d1a9d8a7"></a>
<a id="astructnet__capture__cooked_html_a953de700c9bb28dd350a7ad3b89d900b"></a>
<a id="astructnet__capture__info_html"></a>
<a id="astructnet__capture__info_html_a07af2811c444bbeb2be9d420e0fd885b"></a>
<a id="astructnet__capture__info_html_a1f5786c3158d6941f3a35d99cffab985"></a>
<a id="astructnet__capture__info_html_a302986ad94398191d8ec4e1d9961a4df"></a>
<a id="astructnet__capture__info_html_a856a912643ac30a4d269a1a88300552d"></a>
<a id="astructnet__capture__info_html_afba544c1bdc06824db93ce409804b65b"></a>
<a id="astructnet__capture__info_html_afc7d04a4e4b6f36a94847c27386dd384"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__sockaddr_html"></a>

```c


/*
 * Copyright (c) 2021 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_CAPTURE_H_
#define ZEPHYR_INCLUDE_NET_CAPTURE_H_

#include <zephyr/kernel.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif



struct net_if;
struct net_pkt;
struct device;

struct net_capture_interface_api {
        int (*cleanup)(const struct device *dev);

        int (*enable)(const struct device *dev, struct net_if *iface);

        int (*disable)(const struct device *dev);

        bool (*is_enabled)(const struct device *dev);

        int (*send)(const struct device *dev, struct net_if *iface, struct net_pkt *pkt);
};


int net_capture_setup(const char *remote_addr, const char *my_local_addr, const char *peer_addr,
                      const struct device **dev);

static inline int net_capture_cleanup(const struct device *dev)
{
#if defined(CONFIG_NET_CAPTURE)
        const struct net_capture_interface_api *api =
                (const struct net_capture_interface_api *)dev->api;

        return api->cleanup(dev);
#else
        ARG_UNUSED(dev);

        return -ENOTSUP;
#endif
}

static inline int net_capture_enable(const struct device *dev, struct net_if *iface)
{
#if defined(CONFIG_NET_CAPTURE)
        const struct net_capture_interface_api *api =
                (const struct net_capture_interface_api *)dev->api;

        return api->enable(dev, iface);
#else
        ARG_UNUSED(dev);
        ARG_UNUSED(iface);

        return -ENOTSUP;
#endif
}

static inline bool net_capture_is_enabled(const struct device *dev)
{
#if defined(CONFIG_NET_CAPTURE)
        const struct net_capture_interface_api *api;

        if (dev == NULL) {
                /* TODO: Go through all capture devices instead of one */
                dev = device_get_binding("NET_CAPTURE0");
                if (dev == NULL) {
                        return false;
                }
        }

        api = (const struct net_capture_interface_api *)dev->api;

        return api->is_enabled(dev);
#else
        ARG_UNUSED(dev);

        return false;
#endif
}

static inline int net_capture_disable(const struct device *dev)
{
#if defined(CONFIG_NET_CAPTURE)
        const struct net_capture_interface_api *api =
                (const struct net_capture_interface_api *)dev->api;

        return api->disable(dev);
#else
        ARG_UNUSED(dev);

        return -ENOTSUP;
#endif
}


static inline int net_capture_send(const struct device *dev, struct net_if *iface,
                                   struct net_pkt *pkt)
{
#if defined(CONFIG_NET_CAPTURE)
        const struct net_capture_interface_api *api =
                (const struct net_capture_interface_api *)dev->api;

        return api->send(dev, iface, pkt);
#else
        ARG_UNUSED(dev);
        ARG_UNUSED(iface);
        ARG_UNUSED(pkt);

        return -ENOTSUP;
#endif
}


#if defined(CONFIG_NET_CAPTURE)
void net_capture_pkt(struct net_if *iface, struct net_pkt *pkt);
#else
static inline void net_capture_pkt(struct net_if *iface, struct net_pkt *pkt)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(pkt);
}
#endif


#if defined(CONFIG_NET_CAPTURE)
int net_capture_pkt_with_status(struct net_if *iface, struct net_pkt *pkt);
#else
static inline int net_capture_pkt_with_status(struct net_if *iface, struct net_pkt *pkt)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(pkt);

        return -ENOTSUP;
}
#endif


enum net_capture_packet_type {
        NET_CAPTURE_HOST,
        NET_CAPTURE_BROADCAST,
        NET_CAPTURE_MULTICAST,
        NET_CAPTURE_OTHERHOST,
        NET_CAPTURE_OUTGOING,
};

#define NET_CAPTURE_LL_ADDRLEN 8

struct net_capture_cooked {
        uint16_t hatype;
        uint16_t halen;
        uint8_t addr[NET_CAPTURE_LL_ADDRLEN];
};

#if defined(CONFIG_NET_CAPTURE_COOKED_MODE)
int net_capture_cooked_setup(struct net_capture_cooked *ctx,
                             uint16_t hatype,
                             uint16_t halen,
                             uint8_t *addr);
#else
static inline int net_capture_cooked_setup(struct net_capture_cooked *ctx,
                                           uint16_t hatype,
                                           uint16_t halen,
                                           uint8_t *addr)
{
        ARG_UNUSED(ctx);
        ARG_UNUSED(hatype);
        ARG_UNUSED(halen);
        ARG_UNUSED(addr);

        return -ENOTSUP;
}
#endif

#if defined(CONFIG_NET_CAPTURE_COOKED_MODE)
void net_capture_data(struct net_capture_cooked *ctx,
                      const uint8_t *data, size_t len,
                      enum net_capture_packet_type type,
                      uint16_t ptype);
#else
static inline void net_capture_data(struct net_capture_cooked *ctx,
                                    const uint8_t *data, size_t len,
                                    enum net_capture_packet_type type,
                                    uint16_t ptype)
{
        ARG_UNUSED(ctx);
        ARG_UNUSED(data);
        ARG_UNUSED(len);
        ARG_UNUSED(type);
        ARG_UNUSED(ptype);
}
#endif

struct net_capture_info {
        const struct device *capture_dev;
        struct net_if *capture_iface;
        struct net_if *tunnel_iface;
        struct net_sockaddr *peer;
        struct net_sockaddr *local;
        bool is_enabled;
};

typedef void (*net_capture_cb_t)(struct net_capture_info *info, void *user_data);

#if defined(CONFIG_NET_CAPTURE)
void net_capture_foreach(net_capture_cb_t cb, void *user_data);
#else
static inline void net_capture_foreach(net_capture_cb_t cb, void *user_data)
{
        ARG_UNUSED(cb);
        ARG_UNUSED(user_data);
}
#endif


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_CAPTURE_H_ */
```

## 22.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2021 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 144 行

待办（TODO）：遍历所有抓包设备，而不是只处理一个。

### 注释 3：原第 390 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_CAPTURE_H_`。

## 22.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/capture_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [send](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a16485de18b1ec93572e5d74b4a04e42f)
- [net_capture_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gab280c0c6cc607bdb07211a9450eae262)
- [net_capture_cleanup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga7a56719068938c34c9c6149296074d01)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [net_capture_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gaf449c308080dc126e2e7c03b38d2a0aa)
- [net_capture_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga651987b8b1e713865cff01412934f3cc)
- [device_get_binding](../device_reference/P001_设备模型公共接口.md#ga15386ca9ab38f3e30183c18f604fa835)
- [net_capture_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga32c66260fc888dcd38b6a3cffca3b951)
- [net_capture_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga54aba9a796ba312554ef9589b879f204)
- [net_capture_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga8b6c9d07ae0e1ee906129cb2f0b411ec)
- [NET_CAPTURE_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411ecac19ae62e8505d342c1c2351e61a64ce5)
- [NET_CAPTURE_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411eca9d0c1f31a408bc6b56b106e356f0be88)
- [NET_CAPTURE_MULTICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411eca29604d550ee5aaf22808e7fa9c93526d)
- [NET_CAPTURE_OTHERHOST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411ecae4772d47a9130a69f0477d4e8ed64264)
- [NET_CAPTURE_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411ecaf12e4a87c90d5fa6ced21051dac65631)
- [net_capture_cooked](../network_core_model_reference/P050_net_capture_cooked_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [hatype](../network_core_model_reference/P050_net_capture_cooked_结构体.md#a17d3b9b877451bb809e6b23314117952)
- [halen](../network_core_model_reference/P050_net_capture_cooked_结构体.md#a953de700c9bb28dd350a7ad3b89d900b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [addr](../network_core_model_reference/P050_net_capture_cooked_结构体.md#a30df8c6901fb132c77482b08d1a9d8a7)
- [NET_CAPTURE_LL_ADDRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gad67ec9d34a7e4f85a4f507b30981fad8)
- [net_capture_cooked_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga9f567c3392745ea24f70f736c8973584)
- [net_capture_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gab68bfc9510ce093447eba513c8e8d288)
- [net_capture_info](../network_core_model_reference/P051_net_capture_info_结构体.md)
- [capture_dev](../network_core_model_reference/P051_net_capture_info_结构体.md#afc7d04a4e4b6f36a94847c27386dd384)
- [capture_iface](../network_core_model_reference/P051_net_capture_info_结构体.md#afba544c1bdc06824db93ce409804b65b)
- [tunnel_iface](../network_core_model_reference/P051_net_capture_info_结构体.md#a302986ad94398191d8ec4e1d9961a4df)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [peer](../network_core_model_reference/P051_net_capture_info_结构体.md#a07af2811c444bbeb2be9d420e0fd885b)
- [local](../network_core_model_reference/P051_net_capture_info_结构体.md#a856a912643ac30a4d269a1a88300552d)
- [is_enabled](../network_core_model_reference/P051_net_capture_info_结构体.md#a1f5786c3158d6941f3a35d99cffab985)
- [net_capture_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gaec06d9e76514c8fd2d7bc4e738fa8e5c)
- [net_capture_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gabd019c0856ed170da5b74f153f12768a)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [net_capture_cooked::hatype](../network_core_model_reference/P050_net_capture_cooked_结构体.md#a17d3b9b877451bb809e6b23314117952)
- [net_capture_cooked::addr](../network_core_model_reference/P050_net_capture_cooked_结构体.md#a30df8c6901fb132c77482b08d1a9d8a7)
- [net_capture_cooked::halen](../network_core_model_reference/P050_net_capture_cooked_结构体.md#a953de700c9bb28dd350a7ad3b89d900b)
- [net_capture_info::peer](../network_core_model_reference/P051_net_capture_info_结构体.md#a07af2811c444bbeb2be9d420e0fd885b)
- [net_capture_info::is_enabled](../network_core_model_reference/P051_net_capture_info_结构体.md#a1f5786c3158d6941f3a35d99cffab985)
- [net_capture_info::tunnel_iface](../network_core_model_reference/P051_net_capture_info_结构体.md#a302986ad94398191d8ec4e1d9961a4df)
- [net_capture_info::local](../network_core_model_reference/P051_net_capture_info_结构体.md#a856a912643ac30a4d269a1a88300552d)
- [net_capture_info::capture_iface](../network_core_model_reference/P051_net_capture_info_结构体.md#afba544c1bdc06824db93ce409804b65b)
- [net_capture_info::capture_dev](../network_core_model_reference/P051_net_capture_info_结构体.md#afc7d04a4e4b6f36a94847c27386dd384)

---

[上一章](P021_bq274xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P023_ccc.h_源码浏览.md)
