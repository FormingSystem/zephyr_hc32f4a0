---
id: learning.zephyr-docs.api-source-supplement-reference.page-79
title: gmap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gmap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_gmap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gmap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gmap_8h.html)。

## 79.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00040"></a>
<a id="l00047"></a>
<a id="l00054"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00071"></a>
<a id="l00077"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00094"></a>
<a id="l00100"></a>
<a id="l00106"></a>
<a id="l00112"></a>
<a id="l00118"></a>
<a id="l00125"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="foldopen00167"></a>
<a id="l00167"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__gmap_html_ga0fe87d6d1412c15564ba7de29e3d7a48"></a>
<a id="agroup__bt__gmap_html_ga3a79c408b283864616a522b1f04cacaf"></a>
<a id="agroup__bt__gmap_html_ga3ef43378bad84bbcd726e318cf0bc145"></a>
<a id="agroup__bt__gmap_html_ga55ecab78bcd6de6c294abdc20ad10e56"></a>
<a id="agroup__bt__gmap_html_ga75211707bbdceff35235c353dc8c7609"></a>
<a id="agroup__bt__gmap_html_ga956efe257f06b627615a0a82d44db919"></a>
<a id="agroup__bt__gmap_html_ga9c1145ad5334e14d4978b6d7d3c84b6c"></a>
<a id="agroup__bt__gmap_html_gab54963e226753d44085a7d1f5dccdef6"></a>
<a id="agroup__bt__gmap_html_gacc4853bf69d0a13353fc941aa7e4e190"></a>
<a id="agroup__bt__gmap_html_gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e"></a>
<a id="agroup__bt__gmap_html_gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88"></a>
<a id="agroup__bt__gmap_html_gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604"></a>
<a id="agroup__bt__gmap_html_gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231"></a>
<a id="agroup__bt__gmap_html_gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045"></a>
<a id="agroup__bt__gmap_html_gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08"></a>
<a id="agroup__bt__gmap_html_gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c"></a>
<a id="agroup__bt__gmap_html_gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8"></a>
<a id="agroup__bt__gmap_html_gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1"></a>
<a id="agroup__bt__gmap_html_gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e"></a>
<a id="agroup__bt__gmap_html_gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331"></a>
<a id="agroup__bt__gmap_html_gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b"></a>
<a id="agroup__bt__gmap_html_gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6"></a>
<a id="agroup__bt__gmap_html_gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251"></a>
<a id="agroup__bt__gmap_html_gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091"></a>
<a id="agroup__bt__gmap_html_gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630"></a>
<a id="agroup__bt__gmap_html_gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__gmap__cb_html"></a>
<a id="astructbt__gmap__cb_html_a72c25ae277e04d419f41733d0b11aefc"></a>
<a id="astructbt__gmap__feat_html"></a>
<a id="astructbt__gmap__feat_html_a0ef9878ffcd04a6b88cc8364173cfc10"></a>
<a id="astructbt__gmap__feat_html_a3793984ce81ff90aab8eb6ad635e24d5"></a>
<a id="astructbt__gmap__feat_html_a7e57da1f8aa0a6ac8e7f929f5ba7e9cd"></a>
<a id="astructbt__gmap__feat_html_a918d35e89da086321d728f61deb0c962"></a>
<a id="autil__macro_8h_html"></a>

```c


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_GMAP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_GMAP_H_


#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

enum bt_gmap_role {
        BT_GMAP_ROLE_UGG = BIT(0U),
        BT_GMAP_ROLE_UGT = BIT(1U),
        BT_GMAP_ROLE_BGS = BIT(2U),
        BT_GMAP_ROLE_BGR = BIT(3U),
};

enum bt_gmap_ugg_feat {
        BT_GMAP_UGG_FEAT_MULTIPLEX = BIT(0U),
        BT_GMAP_UGG_FEAT_96KBPS_SOURCE = BIT(1U),
        BT_GMAP_UGG_FEAT_MULTISINK = BIT(2U),
};

enum bt_gmap_ugt_feat {
        BT_GMAP_UGT_FEAT_SOURCE = BIT(0U),
        BT_GMAP_UGT_FEAT_80KBPS_SOURCE = BIT(1U),
        BT_GMAP_UGT_FEAT_SINK = BIT(2U),
        BT_GMAP_UGT_FEAT_64KBPS_SINK = BIT(3U),
        BT_GMAP_UGT_FEAT_MULTIPLEX = BIT(4U),
        BT_GMAP_UGT_FEAT_MULTISINK = BIT(5U),
        BT_GMAP_UGT_FEAT_MULTISOURCE = BIT(6U),
};

enum bt_gmap_bgs_feat {
        BT_GMAP_BGS_FEAT_96KBPS = BIT(0U),
};

enum bt_gmap_bgr_feat {
        BT_GMAP_BGR_FEAT_MULTISINK = BIT(0U),
        BT_GMAP_BGR_FEAT_MULTIPLEX = BIT(1U),
};

struct bt_gmap_feat {
        enum bt_gmap_ugg_feat ugg_feat;
        enum bt_gmap_ugt_feat ugt_feat;
        enum bt_gmap_bgs_feat bgs_feat;
        enum bt_gmap_bgr_feat bgr_feat;
};

struct bt_gmap_cb {
        void (*discover)(struct bt_conn *conn, int err, enum bt_gmap_role role,
                         struct bt_gmap_feat features);
};

int bt_gmap_cb_register(const struct bt_gmap_cb *cb);

int bt_gmap_discover(struct bt_conn *conn);

int bt_gmap_register(enum bt_gmap_role role, struct bt_gmap_feat features);

int bt_gmap_set_role(enum bt_gmap_role role, struct bt_gmap_feat features);

#ifdef __cplusplus
}
#endif /* end of bt_gmap */

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_GMAP_H_ */
```

## 79.2\_可见注释译文（Comments）

### 注释 1：原第 245 行

`bt_gmap` 分组结束。

### 注释 2：原第 248 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_GMAP_H_`。

## 79.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gmap_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_gmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga55ecab78bcd6de6c294abdc20ad10e56)
- [BT_GMAP_ROLE_UGG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_GMAP_ROLE_UGT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b)
- [BT_GMAP_ROLE_BGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6)
- [BT_GMAP_ROLE_BGR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091)
- [bt_gmap_ugg_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3ef43378bad84bbcd726e318cf0bc145)
- [BT_GMAP_UGG_FEAT_MULTIPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e)
- [BT_GMAP_UGG_FEAT_96KBPS_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331)
- [BT_GMAP_UGG_FEAT_MULTISINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1)
- [bt_gmap_ugt_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga0fe87d6d1412c15564ba7de29e3d7a48)
- [BT_GMAP_UGT_FEAT_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231)
- [BT_GMAP_UGT_FEAT_80KBPS_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88)
- [BT_GMAP_UGT_FEAT_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c)
- [BT_GMAP_UGT_FEAT_64KBPS_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604)
- [BT_GMAP_UGT_FEAT_MULTIPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e)
- [BT_GMAP_UGT_FEAT_MULTISINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08)
- [BT_GMAP_UGT_FEAT_MULTISOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045)
- [bt_gmap_bgs_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga3a79c408b283864616a522b1f04cacaf)
- [BT_GMAP_BGS_FEAT_96KBPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8)
- [bt_gmap_bgr_feat](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga9c1145ad5334e14d4978b6d7d3c84b6c)
- [BT_GMAP_BGR_FEAT_MULTISINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630)
- [BT_GMAP_BGR_FEAT_MULTIPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6)
- [bt_gmap_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md)
- [ugg_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md#a7e57da1f8aa0a6ac8e7f929f5ba7e9cd)
- [ugt_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md#a3793984ce81ff90aab8eb6ad635e24d5)
- [bgs_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md#a0ef9878ffcd04a6b88cc8364173cfc10)
- [bgr_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md#a918d35e89da086321d728f61deb0c962)
- [bt_gmap_cb](../bluetooth_service_model_reference/P068_bt_gmap_cb_结构体.md)
- [discover](../bluetooth_service_model_reference/P068_bt_gmap_cb_结构体.md#a72c25ae277e04d419f41733d0b11aefc)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_gmap_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gacc4853bf69d0a13353fc941aa7e4e190)
- [bt_gmap_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gab54963e226753d44085a7d1f5dccdef6)
- [bt_gmap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga75211707bbdceff35235c353dc8c7609)
- [bt_gmap_set_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga956efe257f06b627615a0a82d44db919)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [bt_gmap_cb::discover](../bluetooth_service_model_reference/P068_bt_gmap_cb_结构体.md#a72c25ae277e04d419f41733d0b11aefc)
- [bt_gmap_feat::bgs_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md#a0ef9878ffcd04a6b88cc8364173cfc10)
- [bt_gmap_feat::ugt_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md#a3793984ce81ff90aab8eb6ad635e24d5)
- [bt_gmap_feat::ugg_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md#a7e57da1f8aa0a6ac8e7f929f5ba7e9cd)
- [bt_gmap_feat::bgr_feat](../bluetooth_service_model_reference/P069_bt_gmap_feat_结构体.md#a918d35e89da086321d728f61deb0c962)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P078_generic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P080_gmap_lc3_preset.h_源码浏览.md)
