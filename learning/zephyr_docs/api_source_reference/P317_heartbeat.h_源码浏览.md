---
id: learning.zephyr-docs.api-source-reference.page-317
title: heartbeat.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第317章\_heartbeat.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h.html)。

## 317.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00068"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="agroup__bt__mesh__heartbeat_html_ga2e95d8f9d75f1bea13a9584d201fd713"></a>
<a id="agroup__bt__mesh__heartbeat_html_ga3013c3da6cc1a34b0c98c56fba7e7877"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__hb__cb_html"></a>
<a id="astructbt__mesh__hb__cb_html_aa3b85249e1a40842c0f937385a72103f"></a>
<a id="astructbt__mesh__hb__cb_html_aa979e024174fa19f047a26f94b54a9d3"></a>
<a id="astructbt__mesh__hb__cb_html_acc5559541f53e2987899433d4d434557"></a>
<a id="astructbt__mesh__hb__pub_html"></a>
<a id="astructbt__mesh__hb__pub_html_a08f32f66fb5c7c0011651633ad212bc9"></a>
<a id="astructbt__mesh__hb__pub_html_a0bf6205724b157fe374e24c024f240c9"></a>
<a id="astructbt__mesh__hb__pub_html_a7161896dd5e337b2b0ee671f59a2444a"></a>
<a id="astructbt__mesh__hb__pub_html_a82dd3457291cc4a939883590e27fdbfb"></a>
<a id="astructbt__mesh__hb__pub_html_aaeb4c9000088418d8688b4f2f964335a"></a>
<a id="astructbt__mesh__hb__pub_html_af8ed3029b088c7b45be4912eb0d9024d"></a>
<a id="astructbt__mesh__hb__sub_html"></a>
<a id="astructbt__mesh__hb__sub_html_a38252818d3a2e136e5dfc9bda847d0b0"></a>
<a id="astructbt__mesh__hb__sub_html_a41dd595eb6a0c980c49f84aca11b3ac2"></a>
<a id="astructbt__mesh__hb__sub_html_aae4eb4e77166dfb49a7341ae8fcb9e6e"></a>
<a id="astructbt__mesh__hb__sub_html_ab10708af9ddfd7a80c370d40d2146a8b"></a>
<a id="astructbt__mesh__hb__sub_html_ad66fd08eb09d475bef9c290fa7ae0a90"></a>
<a id="astructbt__mesh__hb__sub_html_af7b20a7337c31110b1ae38c7eacc071a"></a>
<a id="astructbt__mesh__hb__sub_html_afb9fba6c32257690539dd621e215708b"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c


/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEARTBEAT_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEARTBEAT_H_

#include <stdint.h>

#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>


#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_hb_pub {
        uint16_t dst;
        uint16_t count;
        uint8_t ttl;
        uint16_t feat;
        uint16_t net_idx;
        uint32_t period;
};

struct bt_mesh_hb_sub {
        uint32_t period;
        uint32_t remaining;
        uint16_t src;
        uint16_t dst;
        uint16_t count;
        uint8_t min_hops;
        uint8_t max_hops;
};

struct bt_mesh_hb_cb {
        void (*recv)(const struct bt_mesh_hb_sub *sub, uint8_t hops,
                     uint16_t feat);

        void (*sub_end)(const struct bt_mesh_hb_sub *sub);

        void (*pub_sent)(const struct bt_mesh_hb_pub *pub);
};

#define BT_MESH_HB_CB_DEFINE(_name)                                            \
        static const STRUCT_SECTION_ITERABLE(bt_mesh_hb_cb, _name)

void bt_mesh_hb_pub_get(struct bt_mesh_hb_pub *get);

void bt_mesh_hb_sub_get(struct bt_mesh_hb_sub *get);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEARTBEAT_H_ */
```

## 317.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 145 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEARTBEAT_H_`。

## 317.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_mesh_hb_pub](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [dst](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#aaeb4c9000088418d8688b4f2f964335a)
- [count](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#a7161896dd5e337b2b0ee671f59a2444a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ttl](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#a82dd3457291cc4a939883590e27fdbfb)
- [feat](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#a08f32f66fb5c7c0011651633ad212bc9)
- [net_idx](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#af8ed3029b088c7b45be4912eb0d9024d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [period](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#a0bf6205724b157fe374e24c024f240c9)
- [bt_mesh_hb_sub](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md)
- [period](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#af7b20a7337c31110b1ae38c7eacc071a)
- [remaining](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#ad66fd08eb09d475bef9c290fa7ae0a90)
- [src](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#afb9fba6c32257690539dd621e215708b)
- [dst](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#ab10708af9ddfd7a80c370d40d2146a8b)
- [count](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#a41dd595eb6a0c980c49f84aca11b3ac2)
- [min_hops](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#aae4eb4e77166dfb49a7341ae8fcb9e6e)
- [max_hops](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#a38252818d3a2e136e5dfc9bda847d0b0)
- [bt_mesh_hb_cb](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md)
- [recv](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md#aa3b85249e1a40842c0f937385a72103f)
- [sub_end](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md#aa979e024174fa19f047a26f94b54a9d3)
- [pub_sent](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md#acc5559541f53e2987899433d4d434557)
- [bt_mesh_hb_pub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html#ga2e95d8f9d75f1bea13a9584d201fd713)
- [bt_mesh_hb_sub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html#ga3013c3da6cc1a34b0c98c56fba7e7877)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_mesh_hb_cb::recv](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md#aa3b85249e1a40842c0f937385a72103f)
- [bt_mesh_hb_cb::sub_end](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md#aa979e024174fa19f047a26f94b54a9d3)
- [bt_mesh_hb_cb::pub_sent](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md#acc5559541f53e2987899433d4d434557)
- [bt_mesh_hb_pub::feat](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#a08f32f66fb5c7c0011651633ad212bc9)
- [bt_mesh_hb_pub::period](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#a0bf6205724b157fe374e24c024f240c9)
- [bt_mesh_hb_pub::count](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#a7161896dd5e337b2b0ee671f59a2444a)
- [bt_mesh_hb_pub::ttl](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#a82dd3457291cc4a939883590e27fdbfb)
- [bt_mesh_hb_pub::dst](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#aaeb4c9000088418d8688b4f2f964335a)
- [bt_mesh_hb_pub::net_idx](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md#af8ed3029b088c7b45be4912eb0d9024d)
- [bt_mesh_hb_sub::max_hops](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#a38252818d3a2e136e5dfc9bda847d0b0)
- [bt_mesh_hb_sub::count](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#a41dd595eb6a0c980c49f84aca11b3ac2)
- [bt_mesh_hb_sub::min_hops](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#aae4eb4e77166dfb49a7341ae8fcb9e6e)
- [bt_mesh_hb_sub::dst](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#ab10708af9ddfd7a80c370d40d2146a8b)
- [bt_mesh_hb_sub::remaining](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#ad66fd08eb09d475bef9c290fa7ae0a90)
- [bt_mesh_hb_sub::period](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#af7b20a7337c31110b1ae38c7eacc071a)
- [bt_mesh_hb_sub::src](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md#afb9fba6c32257690539dd621e215708b)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P316_health_srv.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P318_hid_device.h_源码浏览.md)
