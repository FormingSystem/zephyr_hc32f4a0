---
id: learning.zephyr-docs.api-source-reference.page-919
title: wifi_nm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__nm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第919章\_wifi\_nm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wifi__nm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/wifi__nm_8h.html)。

## 919.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
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
<a id="l00080"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="agroup__wifi__nm_html_ga26edd4cbb045a87613b79f8edd8e9dbb"></a>
<a id="agroup__wifi__nm_html_ga467b630fa57bb5587c0237b9cdf403ff"></a>
<a id="agroup__wifi__nm_html_ga6a598af94e36a1f4ade05d7a18c019f5"></a>
<a id="agroup__wifi__nm_html_ga781238fda024558c8ccb4cd8877467ed"></a>
<a id="agroup__wifi__nm_html_ga813b6b6cc227115e83b8e632dd39e6f3"></a>
<a id="agroup__wifi__nm_html_ga963f646981e9a64c9e61659e40c9880e"></a>
<a id="agroup__wifi__nm_html_gaa89e5acfa5eebc9267aa7ed2ce3adc39"></a>
<a id="agroup__wifi__nm_html_gadba91c7f3ef5027f7d2a01229372a1a1"></a>
<a id="agroup__wifi__nm_html_gafea087a6c50d6ad05933ef62546868d6"></a>
<a id="agroup__wifi__nm_html_ggadba91c7f3ef5027f7d2a01229372a1a1a43ada3c4512ea29c8a40ec9780d47afa"></a>
<a id="agroup__wifi__nm_html_ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468"></a>
<a id="agroup__wifi__nm_html_ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructwifi__mgmt__ops_html"></a>
<a id="astructwifi__nm__instance_html"></a>
<a id="astructwifi__nm__instance_html_a02184a7739d4b9a31b6142df3e0463c0"></a>
<a id="astructwifi__nm__instance_html_a65e73ea84dfd64dc17f0af03477362ae"></a>
<a id="astructwifi__nm__instance_html_a9789018a431b6c78bbbbed1bbaf634af"></a>
<a id="astructwifi__nm__mgd__iface_html"></a>
<a id="astructwifi__nm__mgd__iface_html_abd10caf51a7890d24af51c91a58f1e4d"></a>
<a id="astructwifi__nm__mgd__iface_html_adf401562151097f8be118fc609e7f86a"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="awifi__mgmt_8h_html"></a>

```c


/*
 * Copyright (c) 2023 Nordic Semiconductor ASA.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_WIFI_NM_H_
#define ZEPHYR_INCLUDE_NET_WIFI_NM_H_

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/wifi_mgmt.h>

#ifdef __cplusplus
extern "C" {
#endif

enum wifi_nm_iface_type {
        WIFI_TYPE_STA = 0,
        WIFI_TYPE_SAP,
        WIFI_TYPE_MAX,
};

struct wifi_nm_mgd_iface {
        unsigned char type;
        struct net_if *iface;
};

struct wifi_nm_instance {
        const char *name;
        const struct wifi_mgmt_ops *ops;
        struct wifi_nm_mgd_iface mgd_ifaces[CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES];
};


#define WIFI_NM_NAME(name) wifi_nm_##name

#define DEFINE_WIFI_NM_INSTANCE(_name, _ops)            \
        static STRUCT_SECTION_ITERABLE(wifi_nm_instance, WIFI_NM_NAME(_name)) = { \
                .name = STRINGIFY(_name),               \
                .ops = _ops,                            \
                .mgd_ifaces = {},               \
        }


struct wifi_nm_instance *wifi_nm_get_instance(const char *name);

struct wifi_nm_instance *wifi_nm_get_instance_iface(struct net_if *iface);

unsigned char wifi_nm_get_type_iface(struct net_if *iface);

bool wifi_nm_iface_is_sta(struct net_if *iface);

bool wifi_nm_iface_is_sap(struct net_if *iface);

int wifi_nm_register_mgd_iface(struct wifi_nm_instance *nm, struct net_if *iface);

int wifi_nm_register_mgd_type_iface(struct wifi_nm_instance *nm,
                enum wifi_nm_iface_type type, struct net_if *iface);

int wifi_nm_unregister_mgd_iface(struct wifi_nm_instance *nm, struct net_if *iface);


#ifdef __cplusplus
}
#endif
#endif /* ZEPHYR_INCLUDE_NET_WIFI_NM_H_ */
```

## 919.2\_可见注释译文（Comments）

### 注释 1：原第 9 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 170 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_WIFI_NM_H_`。

## 919.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/wifi__nm_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html)
- [wifi_nm_iface_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gadba91c7f3ef5027f7d2a01229372a1a1)
- [WIFI_TYPE_STA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468)
- [WIFI_TYPE_SAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345)
- [WIFI_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ggadba91c7f3ef5027f7d2a01229372a1a1a43ada3c4512ea29c8a40ec9780d47afa)
- [wifi_nm_mgd_iface](../network_core_model_reference/P179_wifi_nm_mgd_iface_结构体.md)
- [type](../network_core_model_reference/P179_wifi_nm_mgd_iface_结构体.md#adf401562151097f8be118fc609e7f86a)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [iface](../network_core_model_reference/P179_wifi_nm_mgd_iface_结构体.md#abd10caf51a7890d24af51c91a58f1e4d)
- [wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)
- [name](../network_core_model_reference/P178_wifi_nm_instance_结构体.md#a9789018a431b6c78bbbbed1bbaf634af)
- [wifi_mgmt_ops](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md)
- [ops](../network_core_model_reference/P178_wifi_nm_instance_结构体.md#a65e73ea84dfd64dc17f0af03477362ae)
- [mgd_ifaces](../network_core_model_reference/P178_wifi_nm_instance_结构体.md#a02184a7739d4b9a31b6142df3e0463c0)
- [wifi_nm_get_instance](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga781238fda024558c8ccb4cd8877467ed)
- [wifi_nm_get_instance_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga813b6b6cc227115e83b8e632dd39e6f3)
- [wifi_nm_get_type_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga6a598af94e36a1f4ade05d7a18c019f5)
- [wifi_nm_iface_is_sta](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gaa89e5acfa5eebc9267aa7ed2ce3adc39)
- [wifi_nm_iface_is_sap](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga963f646981e9a64c9e61659e40c9880e)
- [wifi_nm_register_mgd_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga26edd4cbb045a87613b79f8edd8e9dbb)
- [wifi_nm_register_mgd_type_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gafea087a6c50d6ad05933ef62546868d6)
- [wifi_nm_unregister_mgd_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga467b630fa57bb5587c0237b9cdf403ff)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [wifi_nm_instance::mgd_ifaces](../network_core_model_reference/P178_wifi_nm_instance_结构体.md#a02184a7739d4b9a31b6142df3e0463c0)
- [wifi_nm_instance::ops](../network_core_model_reference/P178_wifi_nm_instance_结构体.md#a65e73ea84dfd64dc17f0af03477362ae)
- [wifi_nm_instance::name](../network_core_model_reference/P178_wifi_nm_instance_结构体.md#a9789018a431b6c78bbbbed1bbaf634af)
- [wifi_nm_mgd_iface::iface](../network_core_model_reference/P179_wifi_nm_mgd_iface_结构体.md#abd10caf51a7890d24af51c91a58f1e4d)
- [wifi_nm_mgd_iface::type](../network_core_model_reference/P179_wifi_nm_mgd_iface_结构体.md#adf401562151097f8be118fc609e7f86a)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html)

---

[上一章](P918_wifi_credentials.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P920_wifi_utils.h_源码浏览.md)
