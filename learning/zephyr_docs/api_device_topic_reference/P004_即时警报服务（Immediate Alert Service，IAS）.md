---
id: learning.zephyr-docs.api-device-topic-reference.page-4
title: 即时警报服务（Immediate Alert Service，IAS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_即时警报服务（Immediate Alert Service，IAS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

即时警报服务（Immediate Alert Service，IAS）

<a id="details"></a>

即时警报服务（Immediate Alert Service，IAS）。实验性 API（Experimental）：用户应注意，这些 API 可能随着开发推进而变化。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

## 4.2\_宏定义（Macros）

<a id="r_ga5dee0ec206e8ddbb9bc33c8df824fcb0"></a>

```c
#define BT_IAS_CB_DEFINE(_name)
```

相关声明：[BT_IAS_CB_DEFINE](#ga5dee0ec206e8ddbb9bc33c8df824fcb0)。

为即时警报（Immediate Alert）事件注册回调结构体。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_gabdaf2045e939bc71c060ee195494c9f0"></a>

```c
enum bt_ias_alert_lvl { BT_IAS_ALERT_LVL_NO_ALERT , BT_IAS_ALERT_LVL_MILD_ALERT , BT_IAS_ALERT_LVL_HIGH_ALERT }
```

相关声明：[bt_ias_alert_lvl](#gabdaf2045e939bc71c060ee195494c9f0)、[BT_IAS_ALERT_LVL_NO_ALERT](#ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997)、[BT_IAS_ALERT_LVL_MILD_ALERT](#ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd)、[BT_IAS_ALERT_LVL_HIGH_ALERT](#ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_gad810c9d74701dc48c12e4545bded95a4"></a>

```c
int bt_ias_local_alert_stop (void)
```

相关声明：[bt_ias_local_alert_stop](#gad810c9d74701dc48c12e4545bded95a4)。

在本地停止警报的方法。

<a id="r_ga66fdc1a1664e34c9292312518e9bc754"></a>

```c
int bt_ias_client_alert_write (struct bt_conn *conn, enum bt_ias_alert_lvl level)
```

相关声明：[bt_ias_client_alert_write](#ga66fdc1a1664e34c9292312518e9bc754)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_ias_alert_lvl](#gabdaf2045e939bc71c060ee195494c9f0)。

设置警报级别（alert level）。

<a id="r_ga2628386523390e044e4a32fb2cf3e7b5"></a>

```c
int bt_ias_discover (struct bt_conn *conn)
```

相关声明：[bt_ias_discover](#ga2628386523390e044e4a32fb2cf3e7b5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现即时警报服务（Immediate Alert Service）。

<a id="r_ga481a20cbe9b3f128f8737f75535d2bfe"></a>

```c
int bt_ias_client_cb_register (const struct bt_ias_client_cb *cb)
```

相关声明：[bt_ias_client_cb_register](#ga481a20cbe9b3f128f8737f75535d2bfe)、[bt_ias_client_cb](../bluetooth_service_model_reference/P095_bt_ias_client_cb_结构体.md)。

注册即时警报客户端（Immediate Alert Client）回调。

## 4.5\_详细说明（Detailed Documentation）

<a id="ga5dee0ec206e8ddbb9bc33c8df824fcb0"></a>

### `BT_IAS_CB_DEFINE`

```c
#define BT_IAS_CB_DEFINE ( _name)
```

```c
#include <zephyr/bluetooth/services/ias.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(bt_ias_cb, _CONCAT(bt_ias_cb_, _name))
```

为即时警报（Immediate Alert）事件注册回调结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 回调结构体名称（Callback Structure Name）。 |

<a id="gabdaf2045e939bc71c060ee195494c9f0"></a>

### `bt_ias_alert_lvl`

```c
enum bt_ias_alert_lvl
```

```c
#include <zephyr/bluetooth/services/ias.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_IAS_ALERT_LVL_NO_ALERT` | 设备不应发出警报。 |
| `BT_IAS_ALERT_LVL_MILD_ALERT` | 设备必须发出警报。 |
| `BT_IAS_ALERT_LVL_HIGH_ALERT` | 设备应以所能提供的最强方式发出警报。 |

<a id="ga66fdc1a1664e34c9292312518e9bc754"></a>

### `bt_ias_client_alert_write()`

```c
int bt_ias_client_alert_write ( struct bt_conn * conn, enum bt_ias_alert_lvl level )
```

```c
#include <zephyr/bluetooth/services/ias.h>
```

设置警报级别（alert level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `level` | 要写入的警报级别（alert level）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回错误码。

<a id="ga481a20cbe9b3f128f8737f75535d2bfe"></a>

### `bt_ias_client_cb_register()`

```c
int bt_ias_client_cb_register ( const struct bt_ias_client_cb * cb)
```

```c
#include <zephyr/bluetooth/services/ias.h>
```

注册即时警报客户端（Immediate Alert Client）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（callback structure）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回错误码。

<a id="ga2628386523390e044e4a32fb2cf3e7b5"></a>

### `bt_ias_discover()`

```c
int bt_ias_discover ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/services/ias.h>
```

发现即时警报服务（Immediate Alert Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回错误码。

<a id="gad810c9d74701dc48c12e4545bded95a4"></a>

### `bt_ias_local_alert_stop()`

```c
int bt_ias_local_alert_stop ( void )
```

```c
#include <zephyr/bluetooth/services/ias.h>
```

在本地停止警报的方法。

**返回（Returns）**：返回值：成功时返回 0，出错时返回错误码。


## 4.6\_原页交叉引用（Cross References）

- [bt_ias_cb](../bluetooth_service_model_reference/P094_bt_ias_cb_结构体.md)
- [bt_ias_client_cb](../bluetooth_service_model_reference/P095_bt_ias_client_cb_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/services/ias.h](../api_file_interface_reference/P021_zephyr__bluetooth__services__ias.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructbt__ias__cb_html"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997"></a>
<a id="ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd"></a>
<a id="ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_BQ274XX API主题.md) · [返回大纲](大纲.md) · [下一章](P005_蓝牙 Mesh 分段与重组配置客户端模型（SAR Configuration Client Model）.md)
