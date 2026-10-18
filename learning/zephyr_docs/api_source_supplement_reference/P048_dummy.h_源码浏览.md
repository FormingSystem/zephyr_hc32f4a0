---
id: learning.zephyr-docs.api-source-supplement-reference.page-48
title: dummy.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dummy_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_dummy.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dummy_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dummy_8h.html)。

## 48.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
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
<a id="l00068"></a>
<a id="l00069"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructdummy__api_html"></a>
<a id="astructdummy__api_html_a092fe1f0d12b091dad21e6dd7c717aa3"></a>
<a id="astructdummy__api_html_a35fcbed7d17542ef32c80a09177cb1b5"></a>
<a id="astructdummy__api_html_a3a6110e3de2300931ac5e0aeabbd7311"></a>
<a id="astructdummy__api_html_a9f535aaf72c9e6781cceffdd019b3f85"></a>
<a id="astructdummy__api_html_ade5d5f20076909da1e9ea7a819192cf1"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_DUMMY_H_
#define ZEPHYR_INCLUDE_NET_DUMMY_H_

#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>

#ifdef __cplusplus
extern "C" {
#endif


struct dummy_api {
        struct net_if_api iface_api;

        int (*send)(const struct device *dev, struct net_pkt *pkt);

        enum net_verdict (*recv)(struct net_if *iface, struct net_pkt *pkt);

        int (*start)(const struct device *dev);

        int (*stop)(const struct device *dev);
};

/* Make sure that the network interface API is properly setup inside
 * dummy API struct (it is the first one).
 */
BUILD_ASSERT(offsetof(struct dummy_api, iface_api) == 0);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_DUMMY_H_ */
```

## 48.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

确保网络接口 API 正确放置在虚拟接口（Dummy）API 结构体内，即作为其第一个成员。

### 注释 3：原第 69 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DUMMY_H_`。

## 48.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dummy_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [dummy_api](../device_power_control_model_reference/P007_dummy_api_结构体.md)
- [iface_api](../device_power_control_model_reference/P007_dummy_api_结构体.md#ade5d5f20076909da1e9ea7a819192cf1)
- [send](../device_power_control_model_reference/P007_dummy_api_结构体.md#a3a6110e3de2300931ac5e0aeabbd7311)
- [device](../device_reference/P002_设备对象结构.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [recv](../device_power_control_model_reference/P007_dummy_api_结构体.md#a35fcbed7d17542ef32c80a09177cb1b5)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [start](../device_power_control_model_reference/P007_dummy_api_结构体.md#a9f535aaf72c9e6781cceffdd019b3f85)
- [stop](../device_power_control_model_reference/P007_dummy_api_结构体.md#a092fe1f0d12b091dad21e6dd7c717aa3)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [dummy_api::stop](../device_power_control_model_reference/P007_dummy_api_结构体.md#a092fe1f0d12b091dad21e6dd7c717aa3)
- [dummy_api::recv](../device_power_control_model_reference/P007_dummy_api_结构体.md#a35fcbed7d17542ef32c80a09177cb1b5)
- [dummy_api::send](../device_power_control_model_reference/P007_dummy_api_结构体.md#a3a6110e3de2300931ac5e0aeabbd7311)
- [dummy_api::start](../device_power_control_model_reference/P007_dummy_api_结构体.md#a9f535aaf72c9e6781cceffdd019b3f85)
- [dummy_api::iface_api](../device_power_control_model_reference/P007_dummy_api_结构体.md#ade5d5f20076909da1e9ea7a819192cf1)

---

[上一章](P047_led.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P049_ec_host_cmd.h_源码浏览.md)
