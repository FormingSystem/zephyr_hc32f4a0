---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-125
title: bt_nus_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__nus__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_bt\_nus\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__nus__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于接收NUS服务（NUS Service）事件通知的回调。

```c
#include <zephyr/bluetooth/services/nus.h>
```

<a id="details"></a>

用于接收NUS服务（NUS Service）事件通知的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 125.1\_数据成员（Data Fields）

<a id="r_a3fc8fcca9d16f18c506ad13d2356e32c"></a>

```c
void(* notif_enabled )(bool enabled, void *ctx)
```

相关声明：[notif_enabled](#a3fc8fcca9d16f18c506ad13d2356e32c)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ctx](#ab28ef9120ed04be0c7dbdd5c76556864)。

通知订阅（notifications subscription）发生变化。

<a id="r_ad95d3bb5f927c25058c4ec6a89c665a4"></a>

```c
void(* received )(struct bt_conn *conn, const void *data, uint16_t len, void *ctx)
```

相关声明：[received](#ad95d3bb5f927c25058c4ec6a89c665a4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ctx](#ab28ef9120ed04be0c7dbdd5c76556864)。

收到的数据（Received Data）。

<a id="r_ab28ef9120ed04be0c7dbdd5c76556864"></a>

```c
void * ctx
```

相关声明：[ctx](#ab28ef9120ed04be0c7dbdd5c76556864)。

内部成员。

## 125.2\_详细说明（Detailed Documentation）

<a id="ab28ef9120ed04be0c7dbdd5c76556864"></a>

### `ctx`

```c
void* bt_nus_cb::ctx
```

内部成员。

作为回调参数传入的用户上下文（user context）。

<a id="a3fc8fcca9d16f18c506ad13d2356e32c"></a>

### `notif_enabled`

```c
void(* bt_nus_cb::notif_enabled) (bool enabled, void *ctx)
```

通知订阅（notifications subscription）发生变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enabled` | 已启用通知时此标志为 `true`，已禁用通知时为 `false`。 |
| `ctx` | 在回调结构体中提供的用户上下文。 |

<a id="ad95d3bb5f927c25058c4ec6a89c665a4"></a>

### `received`

```c
void(* bt_nus_cb::received) (struct bt_conn *conn, const void *data, uint16_t len, void *ctx)
```

收到的数据（Received Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 对端连接对象。 |
| `data` | 指向接收数据缓冲区的指针。 |
| `len` | 接收数据的大小，单位为字节。 |
| `ctx` | 在回调结构体中提供的用户上下文。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/nus.h`

## 125.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/nus.h](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P124_bt_micp_mic_dev_register_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P126_bt_nus_inst_结构体.md)
