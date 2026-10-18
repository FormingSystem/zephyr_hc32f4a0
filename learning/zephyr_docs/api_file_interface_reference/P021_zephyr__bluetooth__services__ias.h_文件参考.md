---
id: learning.zephyr-docs.api-file-interface-reference.page-21
title: zephyr__bluetooth__services__ias.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ias_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_bluetooth\_\_services\_\_ias.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ias_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_bt_5Fias_5Fcb"></a>

```c
struct bt_ias_cb
```

相关声明：[bt_ias_cb](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md)。

即时警报服务（Immediate Alert Service）的回调结构。

<a id="r_bt_5Fias_5Fclient_5Fcb"></a>

```c
struct bt_ias_client_cb
```

相关声明：[bt_ias_client_cb](../bluetooth_service_model_reference/P095_bt_ias_client_cb_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="r_ga5dee0ec206e8ddbb9bc33c8df824fcb0"></a>

```c
#define BT_IAS_CB_DEFINE(_name)
```

相关声明：[BT_IAS_CB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga5dee0ec206e8ddbb9bc33c8df824fcb0)。

为即时警报（Immediate Alert）事件注册回调结构体。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 21.3\_枚举（Enumerations）

<a id="r_gabdaf2045e939bc71c060ee195494c9f0"></a>

```c
enum bt_ias_alert_lvl { BT_IAS_ALERT_LVL_NO_ALERT , BT_IAS_ALERT_LVL_MILD_ALERT , BT_IAS_ALERT_LVL_HIGH_ALERT }
```

相关声明：[bt_ias_alert_lvl](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#gabdaf2045e939bc71c060ee195494c9f0)、[BT_IAS_ALERT_LVL_NO_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997)、[BT_IAS_ALERT_LVL_MILD_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd)、[BT_IAS_ALERT_LVL_HIGH_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.4\_函数（Functions）

<a id="r_gad810c9d74701dc48c12e4545bded95a4"></a>

```c
int bt_ias_local_alert_stop (void)
```

相关声明：[bt_ias_local_alert_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#gad810c9d74701dc48c12e4545bded95a4)。

在本地停止警报的方法。

<a id="r_ga66fdc1a1664e34c9292312518e9bc754"></a>

```c
int bt_ias_client_alert_write (struct bt_conn *conn, enum bt_ias_alert_lvl level)
```

相关声明：[bt_ias_client_alert_write](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga66fdc1a1664e34c9292312518e9bc754)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_ias_alert_lvl](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#gabdaf2045e939bc71c060ee195494c9f0)。

设置警报级别（alert level）。

<a id="r_ga2628386523390e044e4a32fb2cf3e7b5"></a>

```c
int bt_ias_discover (struct bt_conn *conn)
```

相关声明：[bt_ias_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga2628386523390e044e4a32fb2cf3e7b5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现即时警报服务（Immediate Alert Service）。

<a id="r_ga481a20cbe9b3f128f8737f75535d2bfe"></a>

```c
int bt_ias_client_cb_register (const struct bt_ias_client_cb *cb)
```

相关声明：[bt_ias_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga481a20cbe9b3f128f8737f75535d2bfe)、[bt_ias_client_cb](../bluetooth_service_model_reference/P095_bt_ias_client_cb_结构体.md)。

注册即时警报客户端（Immediate Alert Client）回调。


## 21.5\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P331_ias.h_源码浏览.md)
- [bt_ias_cb](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md)
- [bt_ias_client_cb](../bluetooth_service_model_reference/P095_bt_ias_client_cb_结构体.md)
- [BT_IAS_CB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga5dee0ec206e8ddbb9bc33c8df824fcb0)
- [bt_ias_alert_lvl](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#gabdaf2045e939bc71c060ee195494c9f0)
- [BT_IAS_ALERT_LVL_NO_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997)
- [BT_IAS_ALERT_LVL_MILD_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd)
- [BT_IAS_ALERT_LVL_HIGH_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653)
- [bt_ias_local_alert_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#gad810c9d74701dc48c12e4545bded95a4)
- [bt_ias_client_alert_write](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga66fdc1a1664e34c9292312518e9bc754)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_ias_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga2628386523390e044e4a32fb2cf3e7b5)
- [bt_ias_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html#ga481a20cbe9b3f128f8737f75535d2bfe)

---

[上一章](P020_zephyr__bluetooth__mesh__health_srv.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__video__types.h_文件参考.md)
