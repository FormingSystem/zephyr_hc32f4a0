---
id: learning.zephyr-docs.api-source-supplement-reference.page-86
title: hdlc_rcp_if.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_hdlc\_rcp\_if.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h.html)。

## 86.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00068"></a>
<a id="l00069"></a>
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
<a id="ahdlc__rcp__if_8h_html_a31b4a1434d2faad2878344367caf1b53"></a>
<a id="anet__if_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructhdlc__api_html"></a>
<a id="astructhdlc__api_html_a2b18e7cd6dc393769b3d3ad2c8bf63ed"></a>
<a id="astructhdlc__api_html_a33486d7c73df2958bf89bfe500b27464"></a>
<a id="astructhdlc__api_html_a5a1958253b254008cd142c2c3ab33d2a"></a>
<a id="astructhdlc__api_html_abeb64661526d0a3e241e6515707284de"></a>
<a id="astructhdlc__api_html_ac9054a3a7bf0b2e364857334a62e4c08"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2024, NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_HDLC_RCP_IF_HDLC_RCP_IF_H_
#define ZEPHYR_INCLUDE_NET_HDLC_RCP_IF_HDLC_RCP_IF_H_


#include <zephyr/sys/util.h>
#include <zephyr/net/net_if.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef void (*hdlc_rx_callback_t)(const uint8_t *data, uint16_t len, void *param);

struct hdlc_api {
        struct net_if_api iface_api;

        int (*register_rx_cb)(hdlc_rx_callback_t hdlc_rx_callback, void *param);

        int (*send)(const uint8_t *frame, uint16_t length);

        int (*deinit)(void);

        int (*deferred_init)(void);
};

/* Make sure that the interface API is properly setup inside
 * HDLC interface API struct (it is the first one).
 */
BUILD_ASSERT(offsetof(struct hdlc_api, iface_api) == 0);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_HDLC_RCP_IF_HDLC_RCP_IF_H_ */
```

## 86.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024, NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 80 行

确保接口 API 正确放置在 HDLC 接口 API 结构体内，即作为其第一个成员。

### 注释 3：原第 89 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_HDLC_RCP_IF_HDLC_RCP_IF_H_`。

## 86.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [hdlc_rx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h.html#a31b4a1434d2faad2878344367caf1b53)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [hdlc_api](../network_service_model_reference/P023_hdlc_api_结构体.md)
- [iface_api](../network_service_model_reference/P023_hdlc_api_结构体.md#abeb64661526d0a3e241e6515707284de)
- [register_rx_cb](../network_service_model_reference/P023_hdlc_api_结构体.md#a2b18e7cd6dc393769b3d3ad2c8bf63ed)
- [send](../network_service_model_reference/P023_hdlc_api_结构体.md#a5a1958253b254008cd142c2c3ab33d2a)
- [deinit](../network_service_model_reference/P023_hdlc_api_结构体.md#a33486d7c73df2958bf89bfe500b27464)
- [deferred_init](../network_service_model_reference/P023_hdlc_api_结构体.md#ac9054a3a7bf0b2e364857334a62e4c08)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [hdlc_api::register_rx_cb](../network_service_model_reference/P023_hdlc_api_结构体.md#a2b18e7cd6dc393769b3d3ad2c8bf63ed)
- [hdlc_api::deinit](../network_service_model_reference/P023_hdlc_api_结构体.md#a33486d7c73df2958bf89bfe500b27464)
- [hdlc_api::send](../network_service_model_reference/P023_hdlc_api_结构体.md#a5a1958253b254008cd142c2c3ab33d2a)
- [hdlc_api::iface_api](../network_service_model_reference/P023_hdlc_api_结构体.md#abeb64661526d0a3e241e6515707284de)
- [hdlc_api::deferred_init](../network_service_model_reference/P023_hdlc_api_结构体.md#ac9054a3a7bf0b2e364857334a62e4c08)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P085_hci.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P087_hpack.h_源码浏览.md)
