---
id: learning.zephyr-docs.api-source-reference.page-323
title: hrs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hrs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第323章\_hrs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hrs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hrs_8h.html)。

## 323.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="agroup__bt__hrs_html_ga0e3d298d984e2504957ca655f142e45b"></a>
<a id="agroup__bt__hrs_html_ga4b250a12dc6e975589f21ca1391c5b38"></a>
<a id="agroup__bt__hrs_html_gad725bf460319ca796c166a5f91e38bb6"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__hrs__cb_html"></a>
<a id="astructbt__hrs__cb_html_a7374b6196a258e874628c703b2e5ad35"></a>
<a id="astructbt__hrs__cb_html_ade0afff87b9ba420f5bfacd73a947dc4"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_HRS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_HRS_H_


#include <stdint.h>

#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ 0x01

struct bt_hrs_cb {
        void (*ntf_changed)(bool enabled);

        int (*ctrl_point_write)(uint8_t request);

        sys_snode_t _node;
};

int bt_hrs_cb_register(struct bt_hrs_cb *cb);

int bt_hrs_cb_unregister(struct bt_hrs_cb *cb);

int bt_hrs_notify(uint16_t heartrate);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_HRS_H_ */
```

## 323.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 105 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_HRS_H_`。

## 323.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hrs_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_hrs_cb](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md)
- [ntf_changed](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md#a7374b6196a258e874628c703b2e5ad35)
- [ctrl_point_write](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md#ade0afff87b9ba420f5bfacd73a947dc4)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_hrs_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#ga4b250a12dc6e975589f21ca1391c5b38)
- [bt_hrs_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#gad725bf460319ca796c166a5f91e38bb6)
- [bt_hrs_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#ga0e3d298d984e2504957ca655f142e45b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_hrs_cb::ntf_changed](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md#a7374b6196a258e874628c703b2e5ad35)
- [bt_hrs_cb::ctrl_point_write](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md#ade0afff87b9ba420f5bfacd73a947dc4)

---

[上一章](P322_hostname.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P324_htu31d.h_源码浏览.md)
