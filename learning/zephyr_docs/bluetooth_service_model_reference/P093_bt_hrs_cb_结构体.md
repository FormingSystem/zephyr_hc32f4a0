---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-93
title: bt_hrs_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hrs__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_bt\_hrs\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hrs__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

心率服务（Heart Rate Service）的回调结构。

```c
#include <zephyr/bluetooth/services/hrs.h>
```

<a id="details"></a>

心率服务（Heart Rate Service）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 93.1\_数据成员（Data Fields）

<a id="r_a7374b6196a258e874628c703b2e5ad35"></a>

```c
void(* ntf_changed )(bool enabled)
```

相关声明：[ntf_changed](#a7374b6196a258e874628c703b2e5ad35)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

心率通知（Heart rate notifications）状态已改变。

<a id="r_ade0afff87b9ba420f5bfacd73a947dc4"></a>

```c
int(* ctrl_point_write )(uint8_t request)
```

相关声明：[ctrl_point_write](#ade0afff87b9ba420f5bfacd73a947dc4)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

心率控制点（Heart rate control point）写入回调。

## 93.2\_详细说明（Detailed Documentation）

<a id="ade0afff87b9ba420f5bfacd73a947dc4"></a>

### `ctrl_point_write`

```c
int(* bt_hrs_cb::ctrl_point_write) (uint8_t request)
```

心率控制点（Heart rate control point）写入回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `request` | 控制点请求代码。 |

**说明（Note）**：注意：如果服务器支持能量消耗（Energy Expended）功能，应用必须实现并支持 `BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ` 请求代码。

**返回（Returns）**：返回值：成功处理控制点请求时返回 0；不支持时返回 `-ENOTSUP`。如果有多个监听器，可使用 `-ENOTSUP` 将处理交给其他监听器；其他负值错误码会立即导致错误响应。

<a id="a7374b6196a258e874628c703b2e5ad35"></a>

### `ntf_changed`

```c
void(* bt_hrs_cb::ntf_changed) (bool enabled)
```

心率通知（Heart rate notifications）状态已改变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enabled` | 已启用通知时此标志为 `true`，已禁用通知时为 `false`。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/hrs.h`

## 93.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/hrs.h](https://docs.zephyrproject.org/latest/doxygen/html/hrs_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#ga4ff20fff68b19602a8857d29f8dd822d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P092_bt_hid_host_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P094_bt_ias_cb_结构体.md)
