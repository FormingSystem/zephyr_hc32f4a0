---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-181
title: bt_vcp_vol_ctlr_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__vcp__vol__ctlr__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第181章\_bt\_vcp\_vol\_ctlr\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__vcp__vol__ctlr__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存音量控制器（Volume Controller）回调的结构。

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

<a id="details"></a>

保存音量控制器（Volume Controller）回调的结构体。可通过 `bt_vcp_vol_ctlr_cb_register()` 注册这些回调供使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 181.1\_数据成员（Data Fields）

<a id="r_ac3b89f35b79d35384f9ead31cf15ac4e"></a>

```c
void(* state )(struct bt_vcp_vol_ctlr *vol_ctlr, int err, uint8_t volume, uint8_t mute)
```

相关声明：[state](#ac3b89f35b79d35384f9ead31cf15ac4e)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mute](#aa2cd77992831eef7e59d3e4a01a0e542)。

音量控制规范（Volume Control Profile）音量状态的回调函数。

<a id="r_a4df90987abe0e53894e4064b3487c2bb"></a>

```c
void(* flags )(struct bt_vcp_vol_ctlr *vol_ctlr, int err, uint8_t flags)
```

相关声明：[flags](#a4df90987abe0e53894e4064b3487c2bb)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

音量控制规范（Volume Control Profile）音量标志的回调函数。

<a id="r_ada8fe8d838d6d2c983d746e7e7ed1171"></a>

```c
void(* discover )(struct bt_vcp_vol_ctlr *vol_ctlr, int err, uint8_t vocs_count, uint8_t aics_count)
```

相关声明：[discover](#ada8fe8d838d6d2c983d746e7e7ed1171)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_vcp_vol_ctlr_discover()` 的回调函数。

<a id="r_ac986e0c5cb49395fe8581f5b1dae1a88"></a>

```c
void(* vol_down )(struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

相关声明：[vol_down](#ac986e0c5cb49395fe8581f5b1dae1a88)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)。

`bt_vcp_vol_ctlr_vol_down()` 的回调函数。

<a id="r_ae1beaa5d0a61c630fa90b4a5236ce743"></a>

```c
void(* vol_up )(struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

相关声明：[vol_up](#ae1beaa5d0a61c630fa90b4a5236ce743)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)。

`bt_vcp_vol_ctlr_vol_up()` 的回调函数。

<a id="r_aa2cd77992831eef7e59d3e4a01a0e542"></a>

```c
void(* mute )(struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

相关声明：[mute](#aa2cd77992831eef7e59d3e4a01a0e542)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)。

`bt_vcp_vol_ctlr_mute()` 的回调函数。

<a id="r_a6a217e0d8cbcc56e5128d5b7acdaac6d"></a>

```c
void(* unmute )(struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

相关声明：[unmute](#a6a217e0d8cbcc56e5128d5b7acdaac6d)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)。

`bt_vcp_vol_ctlr_unmute()` 的回调函数。

<a id="r_a770e300127b8357f1e76f0cca21b74e5"></a>

```c
void(* vol_down_unmute )(struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

相关声明：[vol_down_unmute](#a770e300127b8357f1e76f0cca21b74e5)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)。

`bt_vcp_vol_ctlr_vol_down_unmute()` 的回调函数。

<a id="r_af4ca636d19c83694f9b86102404b0538"></a>

```c
void(* vol_up_unmute )(struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

相关声明：[vol_up_unmute](#af4ca636d19c83694f9b86102404b0538)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)。

`bt_vcp_vol_ctlr_vol_up_unmute()` 的回调函数。

<a id="r_abe7cf51858428db6b953a21a6ba40f83"></a>

```c
void(* vol_set )(struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

相关声明：[vol_set](#abe7cf51858428db6b953a21a6ba40f83)、[bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)。

`bt_vcp_vol_ctlr_vol_set()` 的回调函数。

<a id="r_af6407bb0652539608f0100f02cfaadd1"></a>

```c
struct bt_vocs_cb vocs_cb
```

相关声明：[bt_vocs_cb](P185_bt_vocs_cb_结构体.md)、[vocs_cb](#af6407bb0652539608f0100f02cfaadd1)。

音量偏移控制服务（Volume Offset Control Service）回调。

<a id="r_a430b1ee27c9bf7d6c7f8498748d91b21"></a>

```c
struct bt_aics_cb aics_cb
```

相关声明：[bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)、[aics_cb](#a430b1ee27c9bf7d6c7f8498748d91b21)。

音频输入控制服务（Audio Input Control Service）回调。

## 181.2\_详细说明（Detailed Documentation）

<a id="a430b1ee27c9bf7d6c7f8498748d91b21"></a>

### `aics_cb`

```c
struct bt_aics_cb bt_vcp_vol_ctlr_cb::aics_cb
```

音频输入控制服务（Audio Input Control Service）回调。

<a id="ada8fe8d838d6d2c983d746e7e7ed1171"></a>

### `discover`

```c
void(* bt_vcp_vol_ctlr_cb::discover) (struct bt_vcp_vol_ctlr *vol_ctlr, int err, uint8_t vocs_count, uint8_t aics_count)
```

`bt_vcp_vol_ctlr_discover()` 的回调函数。

发现过程（Discovery procedure）完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `vocs_count` | 远端音量呈现器（Volume Renderer）上的音量偏移控制服务（VOCS）实例数量。 |
| `aics_count` | 远端音量呈现器（Volume Renderer）上的音频输入控制服务（AICS）实例数量。 |

<a id="a4df90987abe0e53894e4064b3487c2bb"></a>

### `flags`

```c
void(* bt_vcp_vol_ctlr_cb::flags) (struct bt_vcp_vol_ctlr *vol_ctlr, int err, uint8_t flags)
```

音量控制规范（Volume Control Profile）音量标志的回调函数。

作为音量控制器远程读取此值时调用；音量呈现器更改此值时也会调用。

非零值表示音量呈现器启动后，其音量已被更改。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `flags` | 音量呈现器（Volume Renderer）的标志。 |

<a id="aa2cd77992831eef7e59d3e4a01a0e542"></a>

### `mute`

```c
void(* bt_vcp_vol_ctlr_cb::mute) (struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

`bt_vcp_vol_ctlr_mute()` 的回调函数。

静音（mute）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

<a id="ac3b89f35b79d35384f9ead31cf15ac4e"></a>

### `state`

```c
void(* bt_vcp_vol_ctlr_cb::state) (struct bt_vcp_vol_ctlr *vol_ctlr, int err, uint8_t volume, uint8_t mute)
```

音量控制规范（Volume Control Profile）音量状态的回调函数。

作为音量控制器远程读取此值时调用；当音量呈现器或音量控制器更改此值，并向音量控制器发送通知时，也会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `volume` | 音量呈现器（Volume Renderer）的音量。 |
| `mute` | 音量呈现器（Volume Renderer）的静音设置。 |

<a id="a6a217e0d8cbcc56e5128d5b7acdaac6d"></a>

### `unmute`

```c
void(* bt_vcp_vol_ctlr_cb::unmute) (struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

`bt_vcp_vol_ctlr_unmute()` 的回调函数。

取消静音（unmute）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

<a id="af6407bb0652539608f0100f02cfaadd1"></a>

### `vocs_cb`

```c
struct bt_vocs_cb bt_vcp_vol_ctlr_cb::vocs_cb
```

音量偏移控制服务（Volume Offset Control Service）回调。

<a id="ac986e0c5cb49395fe8581f5b1dae1a88"></a>

### `vol_down`

```c
void(* bt_vcp_vol_ctlr_cb::vol_down) (struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

`bt_vcp_vol_ctlr_vol_down()` 的回调函数。

降低音量（volume down）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

<a id="a770e300127b8357f1e76f0cca21b74e5"></a>

### `vol_down_unmute`

```c
void(* bt_vcp_vol_ctlr_cb::vol_down_unmute) (struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

`bt_vcp_vol_ctlr_vol_down_unmute()` 的回调函数。

降低音量并取消静音（volume down and unmute）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

<a id="abe7cf51858428db6b953a21a6ba40f83"></a>

### `vol_set`

```c
void(* bt_vcp_vol_ctlr_cb::vol_set) (struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

`bt_vcp_vol_ctlr_vol_set()` 的回调函数。

设置绝对音量（set absolute volume）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

<a id="ae1beaa5d0a61c630fa90b4a5236ce743"></a>

### `vol_up`

```c
void(* bt_vcp_vol_ctlr_cb::vol_up) (struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

`bt_vcp_vol_ctlr_vol_up()` 的回调函数。

提高音量（volume up）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

<a id="af4ca636d19c83694f9b86102404b0538"></a>

### `vol_up_unmute`

```c
void(* bt_vcp_vol_ctlr_cb::vol_up_unmute) (struct bt_vcp_vol_ctlr *vol_ctlr, int err)
```

`bt_vcp_vol_ctlr_vol_up_unmute()` 的回调函数。

提高音量并取消静音（volume up and unmute）过程完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/vcp.h`

## 181.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/vcp.h](https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h_source.html)
- [bt_vcp_vol_ctlr](P180_bt_vcp_vol_ctlr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_vcp_vol_ctlr_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gac18d43a0785155c1131249f95554f2de)
- [bt_vcp_vol_ctlr_vol_down()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga03e073e29920f4a530d2f8851b4b8df4)
- [bt_vcp_vol_ctlr_vol_up()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga908eb20727e1d68ed569badfd13ff896)
- [bt_vcp_vol_ctlr_mute()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga106b7f826adec665b4f0ac3d5e82b867)
- [bt_vcp_vol_ctlr_unmute()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga4e95c3fb071cb94fbe75f88e96d34b36)
- [bt_vocs_cb](P185_bt_vocs_cb_结构体.md)
- [bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)
- [bt_vcp_vol_ctlr_cb_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga7861d0c3426870c015106e8e170004a3)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P180_bt_vcp_vol_ctlr_结构体.md) · [返回大纲](大纲.md) · [下一章](P182_bt_vcp_vol_rend_cb_结构体.md)
