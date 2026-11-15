---
id: learning.zephyr-docs.api-source-reference.page-871
title: tmap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tmap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第871章\_tmap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tmap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tmap_8h.html)。

## 871.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00043"></a>
<a id="l00051"></a>
<a id="l00058"></a>
<a id="l00065"></a>
<a id="l00072"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__tmap_html_ga0b51b305d5a5d87df9f4082951bd28a5"></a>
<a id="agroup__bt__tmap_html_ga2c93d1bce7db000cef76c42e5cab48cb"></a>
<a id="agroup__bt__tmap_html_ga4ef8a550bb374a5f257860082e1411d4"></a>
<a id="agroup__bt__tmap_html_gacb52c3e4c56f6b042398ac992628d521"></a>
<a id="agroup__bt__tmap_html_gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22"></a>
<a id="agroup__bt__tmap_html_gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501"></a>
<a id="agroup__bt__tmap_html_gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6"></a>
<a id="agroup__bt__tmap_html_gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308"></a>
<a id="agroup__bt__tmap_html_gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d"></a>
<a id="agroup__bt__tmap_html_gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__tmap__cb_html"></a>
<a id="astructbt__tmap__cb_html_a22ee1b605448a3707d8086de30572def"></a>
<a id="asys_2util_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_TMAP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_TMAP_H_


#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>

enum bt_tmap_role {
        BT_TMAP_ROLE_CG = BIT(0U),
        BT_TMAP_ROLE_CT = BIT(1U),
        BT_TMAP_ROLE_UMS = BIT(2U),
        BT_TMAP_ROLE_UMR = BIT(3U),
        BT_TMAP_ROLE_BMS = BIT(4U),
        BT_TMAP_ROLE_BMR = BIT(5U),
};

struct bt_tmap_cb {
        void (*discovery_complete)(enum bt_tmap_role role, struct bt_conn *conn, int err);
};

int bt_tmap_register(enum bt_tmap_role role);

int bt_tmap_discover(struct bt_conn *conn, const struct bt_tmap_cb *tmap_cb);

void bt_tmap_set_role(enum bt_tmap_role role);


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_TMAP_H_ */
```

## 871.2\_可见注释译文（Comments）

### 注释 1：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_TMAP_H_`。

## 871.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tmap_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_tmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga4ef8a550bb374a5f257860082e1411d4)
- [BT_TMAP_ROLE_CG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_TMAP_ROLE_CT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d)
- [BT_TMAP_ROLE_UMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501)
- [BT_TMAP_ROLE_UMR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22)
- [BT_TMAP_ROLE_BMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308)
- [BT_TMAP_ROLE_BMR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8)
- [bt_tmap_cb](../bluetooth_service_model_reference/P178_bt_tmap_cb_结构体.md)
- [discovery_complete](../bluetooth_service_model_reference/P178_bt_tmap_cb_结构体.md#a22ee1b605448a3707d8086de30572def)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_tmap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga2c93d1bce7db000cef76c42e5cab48cb)
- [bt_tmap_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#gacb52c3e4c56f6b042398ac992628d521)
- [bt_tmap_set_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga0b51b305d5a5d87df9f4082951bd28a5)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [bt_tmap_cb::discovery_complete](../bluetooth_service_model_reference/P178_bt_tmap_cb_结构体.md#a22ee1b605448a3707d8086de30572def)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P870_tls_credentials.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P872_tmp108.h_源码浏览.md)
