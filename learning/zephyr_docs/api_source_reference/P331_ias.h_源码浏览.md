---
id: learning.zephyr-docs.api-source-reference.page-331
title: ias.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ias_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第331章\_ias.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ias_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ias_8h.html)。

## 331.1\_原始可见代码（Source Code）

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
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__ias_html_ga2628386523390e044e4a32fb2cf3e7b5"></a>
<a id="agroup__bt__ias_html_ga481a20cbe9b3f128f8737f75535d2bfe"></a>
<a id="agroup__bt__ias_html_ga66fdc1a1664e34c9292312518e9bc754"></a>
<a id="agroup__bt__ias_html_gabdaf2045e939bc71c060ee195494c9f0"></a>
<a id="agroup__bt__ias_html_gad810c9d74701dc48c12e4545bded95a4"></a>
<a id="agroup__bt__ias_html_ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd"></a>
<a id="agroup__bt__ias_html_ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997"></a>
<a id="agroup__bt__ias_html_ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__ias__cb_html"></a>
<a id="astructbt__ias__cb_html_ad2974bbd16e8d4425370a57f62601af5"></a>
<a id="astructbt__ias__cb_html_ae0719b1f44f094ff0bbd3abea2bfdf15"></a>
<a id="astructbt__ias__cb_html_aeffe89f9e5a9b87efbdd0af471de980d"></a>
<a id="astructbt__ias__client__cb_html"></a>
<a id="astructbt__ias__client__cb_html_a325ad34a67f9d9948740eb87862945b7"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Codecoup
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_IAS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_IAS_H_


#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif

enum bt_ias_alert_lvl {
        BT_IAS_ALERT_LVL_NO_ALERT,

        BT_IAS_ALERT_LVL_MILD_ALERT,

        BT_IAS_ALERT_LVL_HIGH_ALERT,
};

struct bt_ias_cb {
        void (*no_alert)(void);

        void (*mild_alert)(void);

        void (*high_alert)(void);
};

int bt_ias_local_alert_stop(void);

#define BT_IAS_CB_DEFINE(_name)                                                                    \
        static const STRUCT_SECTION_ITERABLE(bt_ias_cb, _CONCAT(bt_ias_cb_, _name))

struct bt_ias_client_cb {
        void (*discover)(struct bt_conn *conn, int err);
};

int bt_ias_client_alert_write(struct bt_conn *conn, enum bt_ias_alert_lvl level);

int bt_ias_discover(struct bt_conn *conn);

int bt_ias_client_cb_register(const struct bt_ias_client_cb *cb);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_IAS_H_ */
```

## 331.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Codecoup。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 120 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_IAS_H_`。

## 331.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ias_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [bt_ias_alert_lvl](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#gabdaf2045e939bc71c060ee195494c9f0)
- [BT_IAS_ALERT_LVL_NO_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997)
- [BT_IAS_ALERT_LVL_MILD_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd)
- [BT_IAS_ALERT_LVL_HIGH_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653)
- [bt_ias_cb](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md)
- [no_alert](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md#ae0719b1f44f094ff0bbd3abea2bfdf15)
- [mild_alert](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md#aeffe89f9e5a9b87efbdd0af471de980d)
- [high_alert](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md#ad2974bbd16e8d4425370a57f62601af5)
- [bt_ias_local_alert_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#gad810c9d74701dc48c12e4545bded95a4)
- [bt_ias_client_cb](../bluetooth_service_model_reference/P095_bt_ias_client_cb_结构体.md)
- [discover](../bluetooth_service_model_reference/P095_bt_ias_client_cb_结构体.md#a325ad34a67f9d9948740eb87862945b7)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_ias_client_alert_write](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga66fdc1a1664e34c9292312518e9bc754)
- [bt_ias_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga2628386523390e044e4a32fb2cf3e7b5)
- [bt_ias_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga481a20cbe9b3f128f8737f75535d2bfe)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [bt_ias_cb::high_alert](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md#ad2974bbd16e8d4425370a57f62601af5)
- [bt_ias_cb::no_alert](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md#ae0719b1f44f094ff0bbd3abea2bfdf15)
- [bt_ias_cb::mild_alert](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md#aeffe89f9e5a9b87efbdd0af471de980d)
- [bt_ias_client_cb::discover](../bluetooth_service_model_reference/P095_bt_ias_client_cb_结构体.md#a325ad34a67f9d9948740eb87862945b7)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P330_iar.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P332_ibi.h_源码浏览.md)
