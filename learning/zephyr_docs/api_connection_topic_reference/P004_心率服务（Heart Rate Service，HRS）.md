---
id: learning.zephyr-docs.api-connection-topic-reference.page-4
title: 心率服务（Heart Rate Service，HRS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_心率服务（Heart Rate Service，HRS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

心率服务（Heart Rate Service，HRS）

<a id="details"></a>

心率服务（Heart Rate Service，HRS）。实验性 API（Experimental）：用户应注意，这些 API 可能随着开发推进而变化。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fhrs_5Fcb"></a>

```c
struct bt_hrs_cb
```

相关声明：[bt_hrs_cb](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md)。

心率服务（Heart Rate Service）的回调结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga4ff20fff68b19602a8857d29f8dd822d"></a>

```c
#define BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ 0x01
```

相关声明：[BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ](#ga4ff20fff68b19602a8857d29f8dd822d)。

服务器（Server）应从零开始重新累计能量消耗（Energy Expended）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga4b250a12dc6e975589f21ca1391c5b38"></a>

```c
int bt_hrs_cb_register (struct bt_hrs_cb *cb)
```

相关声明：[bt_hrs_cb_register](#ga4b250a12dc6e975589f21ca1391c5b38)、[bt_hrs_cb](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md)。

注册心率服务回调（Heart Rate Service Callback）。

<a id="r_gad725bf460319ca796c166a5f91e38bb6"></a>

```c
int bt_hrs_cb_unregister (struct bt_hrs_cb *cb)
```

相关声明：[bt_hrs_cb_unregister](#gad725bf460319ca796c166a5f91e38bb6)、[bt_hrs_cb](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md)。

注销心率服务回调（Heart Rate Service Callback）。

<a id="r_ga0e3d298d984e2504957ca655f142e45b"></a>

```c
int bt_hrs_notify (uint16_t heartrate)
```

相关声明：[bt_hrs_notify](#ga0e3d298d984e2504957ca655f142e45b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通知心率测量值（Heart Rate Measurement）。

## 4.4\_详细说明（Detailed Documentation）

<a id="ga4ff20fff68b19602a8857d29f8dd822d"></a>

### `BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ`

```c
#define BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ 0x01
```

```c
#include <zephyr/bluetooth/services/hrs.h>
```

服务器（Server）应从零开始重新累计能量消耗（Energy Expended）。

<a id="ga4b250a12dc6e975589f21ca1391c5b38"></a>

### `bt_hrs_cb_register()`

```c
int bt_hrs_cb_register ( struct bt_hrs_cb * cb)
```

```c
#include <zephyr/bluetooth/services/hrs.h>
```

注册心率服务回调（Heart Rate Service Callback）。

此函数注册回调，在发生与心率服务相关的特定事件时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体的指针。所指内存必须一直有效，直到注销为止。 |

**返回（Returns）**：返回值：成功时返回 0；`cb` 为 `NULL` 时返回 `-EINVAL`。

<a id="gad725bf460319ca796c166a5f91e38bb6"></a>

### `bt_hrs_cb_unregister()`

```c
int bt_hrs_cb_unregister ( struct bt_hrs_cb * cb)
```

```c
#include <zephyr/bluetooth/services/hrs.h>
```

注销心率服务回调（Heart Rate Service Callback）。

此函数从心率服务注销回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体的指针。 |

**返回（Returns）**：返回值：成功时返回 0；`cb` 为 `NULL` 时返回 `-EINVAL`；已注册回调中未找到 `cb` 时返回 `-ENOENT`。

<a id="ga0e3d298d984e2504957ca655f142e45b"></a>

### `bt_hrs_notify()`

```c
int bt_hrs_notify ( uint16_t heartrate)
```

```c
#include <zephyr/bluetooth/services/hrs.h>
```

通知心率测量值（Heart Rate Measurement）。

向所有当前订阅方发送一条 GATT 通知（notification）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `heartrate` | 测得的心率，单位为每分钟心跳次数（beats per minute）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回错误码。


## 4.5\_原页交叉引用（Cross References）

- [bt_hrs_cb](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/bluetooth/services/hrs.h](../api_file_service_reference/P015_zephyr__bluetooth__services__hrs.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_蓝牙H_4 UART驱动的厂商扩展接口（Vendor Extension Interface）。.md) · [返回大纲](大纲.md) · [下一章](P005_蓝牙 Mesh 二进制大对象（BLOB）传输服务器模型 API.md)
