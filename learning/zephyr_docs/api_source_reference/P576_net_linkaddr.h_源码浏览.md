---
id: learning.zephyr-docs.api-source-reference.page-576
title: net_linkaddr.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__linkaddr_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第576章\_net\_linkaddr.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__linkaddr_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__linkaddr_8h.html)。

## 576.1\_原始可见代码（Source Code）

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
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00102"></a>
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
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00151"></a>
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
<a id="foldopen00179"></a>
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
<a id="l00191"></a>
<a id="l00192"></a>
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
<a id="foldopen00209"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__net__linkaddr_html_ga1230eb353dd8f6671bf8ed31c464b712"></a>
<a id="agroup__net__linkaddr_html_ga1312c2322bc4a4f1c3b76d6466806b24"></a>
<a id="agroup__net__linkaddr_html_ga36387353825a70fbe54dd16d076a9e26"></a>
<a id="agroup__net__linkaddr_html_ga4061ecaf3b1c4c06968ef6a744de0185"></a>
<a id="agroup__net__linkaddr_html_ga5680cf2ac9302bbee824148f36193b2b"></a>
<a id="agroup__net__linkaddr_html_gab0c451240b31d61749b724eaa6d61d45"></a>
<a id="agroup__net__linkaddr_html_gae8a73ee528b82ae36357bd066dc8128b"></a>
<a id="agroup__net__linkaddr_html_gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34"></a>
<a id="agroup__net__linkaddr_html_gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3"></a>
<a id="agroup__net__linkaddr_html_gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8"></a>
<a id="agroup__net__linkaddr_html_gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b"></a>
<a id="agroup__net__linkaddr_html_gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a"></a>
<a id="agroup__net__linkaddr_html_gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_gae37becfaa095a9df5c5c788bce5aa06f"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astring_8h_html_a4137694174d4ca2fad886a1db355015c"></a>
<a id="astring_8h_html_ad8bfbfa1e4ad284ded921dd775735521"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astructnet__linkaddr_html"></a>
<a id="astructnet__linkaddr_html_a58de2645f8c7d31c97026f0bd5262881"></a>
<a id="astructnet__linkaddr_html_a5f5b4c3d353261d0fab8011aa09f00d7"></a>
<a id="astructnet__linkaddr_html_a7b2f8ebe68b557eb9cbb4c2f2ecd70e0"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_NET_LINKADDR_H_
#define ZEPHYR_INCLUDE_NET_NET_LINKADDR_H_

#include <zephyr/types.h>
#include <stdbool.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif


#if CONFIG_NET_LINK_ADDR_CUSTOM_LENGTH > 0
#define NET_LINK_ADDR_MAX_LENGTH CONFIG_NET_LINK_ADDR_CUSTOM_LENGTH

#if defined(CONFIG_NET_L2_PHY_IEEE802154) || defined(CONFIG_NET_L2_PPP)
BUILD_ASSERT(CONFIG_NET_LINK_ADDR_CUSTOM_LENGTH >= 8,
             "CONFIG_NET_LINK_ADDR_CUSTOM_LENGTH too low, required at least 8");
#endif

#if defined(CONFIG_NET_L2_ETHERNET)
BUILD_ASSERT(CONFIG_NET_LINK_ADDR_CUSTOM_LENGTH >= 6,
             "CONFIG_NET_LINK_ADDR_CUSTOM_LENGTH too low, required at least 6");
#endif

#elif defined(CONFIG_NET_L2_PHY_IEEE802154) || defined(CONFIG_NET_L2_PPP)
#define NET_LINK_ADDR_MAX_LENGTH 8
#else
#define NET_LINK_ADDR_MAX_LENGTH 6
#endif

enum net_link_type {
        NET_LINK_UNKNOWN = 0,
        NET_LINK_IEEE802154,
        NET_LINK_BLUETOOTH,
        NET_LINK_ETHERNET,
        NET_LINK_DUMMY,
        NET_LINK_CANBUS_RAW,
} __packed;

struct net_linkaddr {
        uint8_t type;

        uint8_t len;

        uint8_t addr[NET_LINK_ADDR_MAX_LENGTH]; /* in big endian */
};

static inline bool net_linkaddr_cmp(struct net_linkaddr *lladdr1,
                                    struct net_linkaddr *lladdr2)
{
        if (!lladdr1 || !lladdr2) {
                return false;
        }

        if (lladdr1->len != lladdr2->len) {
                return false;
        }

        return !memcmp(lladdr1->addr, lladdr2->addr, lladdr1->len);
}

static inline int net_linkaddr_set(struct net_linkaddr *lladdr,
                                   const uint8_t *new_addr,
                                   uint8_t new_len)
{
        if (lladdr == NULL || new_addr == NULL) {
                return -EINVAL;
        }

        if (new_len > NET_LINK_ADDR_MAX_LENGTH) {
                return -EMSGSIZE;
        }

        lladdr->len = new_len;
        memcpy(lladdr->addr, new_addr, new_len);

        return 0;
}

static inline int net_linkaddr_copy(struct net_linkaddr *dst,
                                    const struct net_linkaddr *src)
{
        if (dst == NULL || src == NULL) {
                return -EINVAL;
        }

        if (src->len > NET_LINK_ADDR_MAX_LENGTH) {
                return -EMSGSIZE;
        }

        dst->type = src->type;
        dst->len = src->len;
        memcpy(dst->addr, src->addr, src->len);

        return 0;
}

static inline int net_linkaddr_create(struct net_linkaddr *lladdr,
                                      const uint8_t *addr, uint8_t len,
                                      enum net_link_type type)
{
        if (lladdr == NULL) {
                return -EINVAL;
        }

        if (len > NET_LINK_ADDR_MAX_LENGTH) {
                return -EMSGSIZE;
        }

        if (addr == NULL) {
                memset(lladdr->addr, 0, NET_LINK_ADDR_MAX_LENGTH);
        } else {
                memcpy(lladdr->addr, addr, len);
        }

        lladdr->type = type;
        lladdr->len = len;

        return 0;
}

static inline int net_linkaddr_clear(struct net_linkaddr *lladdr)
{
        return net_linkaddr_create(lladdr, NULL, 0, NET_LINK_UNKNOWN);
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_NET_LINKADDR_H_ */
```

## 576.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 91 行

采用大端序（Big Endian）。

### 注释 3：原第 222 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_LINKADDR_H_`。

## 576.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__linkaddr_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [net_link_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga1312c2322bc4a4f1c3b76d6466806b24)
- [NET_LINK_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34)
- [NET_LINK_IEEE802154](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3)
- [NET_LINK_BLUETOOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a)
- [NET_LINK_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b)
- [NET_LINK_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8)
- [NET_LINK_CANBUS_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [type](../network_core_model_reference/P105_net_linkaddr_结构体.md#a5f5b4c3d353261d0fab8011aa09f00d7)
- [len](../network_core_model_reference/P105_net_linkaddr_结构体.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)
- [addr](../network_core_model_reference/P105_net_linkaddr_结构体.md#a58de2645f8c7d31c97026f0bd5262881)
- [NET_LINK_ADDR_MAX_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga5680cf2ac9302bbee824148f36193b2b)
- [net_linkaddr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga36387353825a70fbe54dd16d076a9e26)
- [memcmp](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#ad8bfbfa1e4ad284ded921dd775735521)
- [net_linkaddr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gab0c451240b31d61749b724eaa6d61d45)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [EMSGSIZE](../error_reference/P003_系统错误号公共接口.md#gae37becfaa095a9df5c5c788bce5aa06f)
- [memcpy](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#af0f01bffcd16daa9143f6014d10a25ad)
- [net_linkaddr_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga1230eb353dd8f6671bf8ed31c464b712)
- [net_linkaddr_create](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#gae8a73ee528b82ae36357bd066dc8128b)
- [memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)
- [net_linkaddr_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga4061ecaf3b1c4c06968ef6a744de0185)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [net_linkaddr::addr](../network_core_model_reference/P105_net_linkaddr_结构体.md#a58de2645f8c7d31c97026f0bd5262881)
- [net_linkaddr::type](../network_core_model_reference/P105_net_linkaddr_结构体.md#a5f5b4c3d353261d0fab8011aa09f00d7)
- [net_linkaddr::len](../network_core_model_reference/P105_net_linkaddr_结构体.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)

---

[上一章](P575_net_l2.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P577_net_offload.h_源码浏览.md)
