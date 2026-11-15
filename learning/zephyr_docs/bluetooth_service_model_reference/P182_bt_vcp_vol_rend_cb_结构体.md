---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-182
title: bt_vcp_vol_rend_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__vcp__vol__rend__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第182章\_bt\_vcp\_vol\_rend\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__vcp__vol__rend__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存音量呈现器（Volume Renderer）回调的结构。

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

<a id="details"></a>

保存音量呈现器（Volume Renderer）回调的结构体。可通过 `bt_vcp_vol_rend_register()` 注册这些回调供使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 182.1\_数据成员（Data Fields）

<a id="r_a05f84d8a2deedbc426ef22b89c87bd40"></a>

```c
void(* state )(struct bt_conn *conn, int err, uint8_t volume, uint8_t mute)
```

相关声明：[state](#a05f84d8a2deedbc426ef22b89c87bd40)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

音量控制服务（Volume Control Service）音量状态的回调函数。

<a id="r_a3413d33fa8c3362ded6ec81533c27c86"></a>

```c
void(* flags )(struct bt_conn *conn, int err, uint8_t flags)
```

相关声明：[flags](#a3413d33fa8c3362ded6ec81533c27c86)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

音量控制服务（Volume Control Service）标志的回调函数。

## 182.2\_详细说明（Detailed Documentation）

<a id="a3413d33fa8c3362ded6ec81533c27c86"></a>

### `flags`

```c
void(* bt_vcp_vol_rend_cb::flags) (struct bt_conn *conn, int err, uint8_t flags)
```

音量控制服务（Volume Control Service）标志的回调函数。

作为服务器在本地读取此值时调用；作为客户端远程读取此值时调用；服务器或客户端更改此值时也会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 如果变化由远端设备引起，则为指向该远端设备连接的指针；否则为 `NULL`。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `flags` | 音量控制服务（Volume Control Service）服务器的标志。 |

<a id="a05f84d8a2deedbc426ef22b89c87bd40"></a>

### `state`

```c
void(* bt_vcp_vol_rend_cb::state) (struct bt_conn *conn, int err, uint8_t volume, uint8_t mute)
```

音量控制服务（Volume Control Service）音量状态的回调函数。

通过 `bt_vcp_vol_rend_get_state()` 在本地读取此值时调用；当音量呈现器或远端音量控制器更改状态时，也会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 如果变化由远端设备引起，则为指向该远端设备连接的指针；否则为 `NULL`。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `volume` | 音量控制服务（Volume Control Service）服务器的音量。 |
| `mute` | 音量控制服务（Volume Control Service）服务器的静音设置。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/vcp.h`

## 182.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/vcp.h](https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_vcp_vol_rend_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga752d8ff54a4b8c8c854a9c693617e64d)
- [bt_vcp_vol_rend_get_state()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga9d1ac028abc88549ea18b6a0c585c781)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P181_bt_vcp_vol_ctlr_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P183_bt_vcp_vol_rend_register_param_结构体.md)
