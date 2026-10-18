---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-63
title: bt_cts_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cts__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_bt\_cts\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cts__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

当前时间服务（Current Time Service，CTS）的回调结构体。

```c
#include <zephyr/bluetooth/services/cts.h>
```

<a id="details"></a>

当前时间服务（Current Time Service，CTS）的回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_accf7eb6620ae0f4b9693d238ecdde5b3"></a>

```c
void(* notification_changed )(bool enabled)
```

相关声明：[notification_changed](#accf7eb6620ae0f4b9693d238ecdde5b3)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

当前时间服务通知状态（Current Time Service notifications）已变化。

<a id="r_a1dd6b251b07537e81c010f654721cbf4"></a>

```c
int(* cts_time_write )(struct bt_cts_time_format *cts_time)
```

相关声明：[cts_time_write](#a1dd6b251b07537e81c010f654721cbf4)、[bt_cts_time_format](P065_bt_cts_time_format_结构体.md)。

对等设备请求更新当前时间（Current Time）。

<a id="r_ae4a374f95870bfa21b8c1d87e832fe48"></a>

```c
int(* fill_current_cts_time )(struct bt_cts_time_format *cts_time)
```

相关声明：[fill_current_cts_time](#ae4a374f95870bfa21b8c1d87e832fe48)、[bt_cts_time_format](P065_bt_cts_time_format_结构体.md)。

获取当前时间的回调（Current time callback）。

<a id="r_a32da52541c84f0116b5001b4fb07c3a8"></a>

```c
int(* cts_local_time_write )(const struct bt_cts_local_time *cts_local_time)
```

相关声明：[cts_local_time_write](#a32da52541c84f0116b5001b4fb07c3a8)、[bt_cts_local_time](P064_bt_cts_local_time_结构体.md)。

对等设备请求更新本地时间信息（Local Time Information）。

<a id="r_a306e843a06337a12832a5463ce6d1b43"></a>

```c
int(* fill_current_cts_local_time )(struct bt_cts_local_time *local_time)
```

相关声明：[fill_current_cts_local_time](#a306e843a06337a12832a5463ce6d1b43)、[bt_cts_local_time](P064_bt_cts_local_time_结构体.md)。

请求获取当前本地时间（Current local time）。

## 63.2\_详细说明（Detailed Documentation）

<a id="a32da52541c84f0116b5001b4fb07c3a8"></a>

### `cts_local_time_write`

```c
int(* bt_cts_cb::cts_local_time_write) (const struct bt_cts_local_time *cts_local_time)
```

对等设备请求更新本地时间信息（Local Time Information）。

应用负责存储新的本地时间（Local time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cts_local_time` | 请求写入的本地时间（Local time）。 |

**返回（Returns）**：返回值（Returns）：成功写入时为 `0`，失败时返回负错误码。

<a id="a1dd6b251b07537e81c010f654721cbf4"></a>

### `cts_time_write`

```c
int(* bt_cts_cb::cts_time_write) (struct bt_cts_time_format *cts_time)
```

对等设备请求更新当前时间（Current Time）。

应用负责存储新的时间（Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cts_time` | 请求写入的时间（Time）。 |

**返回（Returns）**：返回值（Returns）：成功写入时为 `0`，失败时返回负错误码。

<a id="a306e843a06337a12832a5463ce6d1b43"></a>

### `fill_current_cts_local_time`

```c
int(* bt_cts_cb::fill_current_cts_local_time) (struct bt_cts_local_time *local_time)
```

请求获取当前本地时间（Current local time）。

当前时间服务（CTS）使用此回调从应用获取本地时间信息（Local time information）。应用必须实现此回调，并提供 CTS 本地时间信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] local_time` | 待填充的当前本地时间结构（Current local time struct）。 |

**返回（Returns）**：返回值（Returns）：成功填充时为 `0`，失败时返回负错误码。

<a id="ae4a374f95870bfa21b8c1d87e832fe48"></a>

### `fill_current_cts_time`

```c
int(* bt_cts_cb::fill_current_cts_time) (struct bt_cts_time_format *cts_time)
```

获取当前时间的回调（Current time callback）。

触发当前时间读取请求（Current time Read request）或通知（Notification）时，当前时间服务（CTS）通过此回调从应用获取当前时间信息。应用必须实现此回调，并提供 CTS 格式的当前时间信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] cts_time` | 由应用填充的当前时间（Current time）。 |

**返回（Returns）**：返回值（Returns）：成功填充时为 `0`，失败时返回负错误码。

<a id="accf7eb6620ae0f4b9693d238ecdde5b3"></a>

### `notification_changed`

```c
void(* bt_cts_cb::notification_changed) (bool enabled)
```

当前时间服务通知状态（Current Time Service notifications）已变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enabled` | 启用通知（Notifications）时为 `true`，禁用时为 `false`。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/cts.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/cts.h](https://docs.zephyrproject.org/latest/doxygen/html/cts_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_cts_time_format](P065_bt_cts_time_format_结构体.md)
- [bt_cts_local_time](P064_bt_cts_local_time_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_bt_csip_set_member_svc_inst_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_bt_cts_local_time_结构体.md)
