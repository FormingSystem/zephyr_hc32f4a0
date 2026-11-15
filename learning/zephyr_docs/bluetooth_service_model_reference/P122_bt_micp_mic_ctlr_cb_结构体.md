---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-122
title: bt_micp_mic_ctlr_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__micp__mic__ctlr__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第122章\_bt\_micp\_mic\_ctlr\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__micp__mic__ctlr__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存麦克风控制器（Microphone Controller）回调的结构。

```c
#include <zephyr/bluetooth/audio/micp.h>
```

<a id="details"></a>

保存麦克风控制器回调的结构体。可通过 `bt_micp_mic_ctlr_cb_register()` 注册这些回调供使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 122.1\_数据成员（Data Fields）

<a id="r_a21786359322dbd6f814929293a69482f"></a>

```c
void(* mute )(struct bt_micp_mic_ctlr *mic_ctlr, int err, uint8_t mute)
```

相关声明：[mute](#a21786359322dbd6f814929293a69482f)、[bt_micp_mic_ctlr](P121_bt_micp_mic_ctlr_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

麦克风控制规范（Microphone Control Profile）静音状态的回调函数。

<a id="r_a2359b88344bf36c3a491b0126dac006b"></a>

```c
void(* discover )(struct bt_micp_mic_ctlr *mic_ctlr, int err, uint8_t aics_count)
```

相关声明：[discover](#a2359b88344bf36c3a491b0126dac006b)、[bt_micp_mic_ctlr](P121_bt_micp_mic_ctlr_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_micp_mic_ctlr_discover()` 的回调函数。

<a id="r_ae15fb539599feab59041e30a121021f0"></a>

```c
void(* mute_written )(struct bt_micp_mic_ctlr *mic_ctlr, int err)
```

相关声明：[mute_written](#ae15fb539599feab59041e30a121021f0)、[bt_micp_mic_ctlr](P121_bt_micp_mic_ctlr_结构体.md)。

麦克风控制规范（Microphone Control Profile）静音或取消静音操作的回调函数。

<a id="r_a03afd3a79838c15be9262f441a3d338b"></a>

```c
void(* unmute_written )(struct bt_micp_mic_ctlr *mic_ctlr, int err)
```

相关声明：[unmute_written](#a03afd3a79838c15be9262f441a3d338b)、[bt_micp_mic_ctlr](P121_bt_micp_mic_ctlr_结构体.md)。

麦克风控制规范（Microphone Control Profile）静音或取消静音操作的回调函数。

<a id="r_a6bd92f744f203736ec04d17a632b16c1"></a>

```c
struct bt_aics_cb aics_cb
```

相关声明：[bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)、[aics_cb](#a6bd92f744f203736ec04d17a632b16c1)。

音频输入控制服务（AICS）客户端回调。

## 122.2\_详细说明（Detailed Documentation）

<a id="a6bd92f744f203736ec04d17a632b16c1"></a>

### `aics_cb`

```c
struct bt_aics_cb bt_micp_mic_ctlr_cb::aics_cb
```

音频输入控制服务（AICS）客户端回调。

<a id="a2359b88344bf36c3a491b0126dac006b"></a>

### `discover`

```c
void(* bt_micp_mic_ctlr_cb::discover) (struct bt_micp_mic_ctlr *mic_ctlr, int err, uint8_t aics_count)
```

`bt_micp_mic_ctlr_discover()` 的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mic_ctlr` | 麦克风控制器（Microphone Controller）实例指针。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |
| `aics_count` | 对端设备上的音频输入控制服务（AICS）实例数量。 |

<a id="a21786359322dbd6f814929293a69482f"></a>

### `mute`

```c
void(* bt_micp_mic_ctlr_cb::mute) (struct bt_micp_mic_ctlr *mic_ctlr, int err, uint8_t mute)
```

麦克风控制规范（Microphone Control Profile）静音状态的回调函数。

读取此值时调用；当麦克风设备或麦克风控制器更改此值时，也会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mic_ctlr` | 麦克风控制器（Microphone Controller）实例指针。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。对于通知，此值始终为 0。 |
| `mute` | 麦克风控制服务（Microphone Control Service）的静音设置。 |

<a id="ae15fb539599feab59041e30a121021f0"></a>

### `mute_written`

```c
void(* bt_micp_mic_ctlr_cb::mute_written) (struct bt_micp_mic_ctlr *mic_ctlr, int err)
```

麦克风控制规范（Microphone Control Profile）静音或取消静音操作的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mic_ctlr` | 麦克风控制器（Microphone Controller）实例指针。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |

<a id="a03afd3a79838c15be9262f441a3d338b"></a>

### `unmute_written`

```c
void(* bt_micp_mic_ctlr_cb::unmute_written) (struct bt_micp_mic_ctlr *mic_ctlr, int err)
```

麦克风控制规范（Microphone Control Profile）静音或取消静音操作的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mic_ctlr` | 麦克风控制器（Microphone Controller）实例指针。 |
| `err` | 错误值。成功时为 0；失败时为 GATT 错误或 `errno`。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/micp.h`

## 122.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/micp.h](https://docs.zephyrproject.org/latest/doxygen/html/micp_8h_source.html)
- [bt_micp_mic_ctlr](P121_bt_micp_mic_ctlr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_micp_mic_ctlr_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga26187007ebf35ba2a5c57a076a3a7212)
- [bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)
- [bt_micp_mic_ctlr_cb_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga148ffcd0672adff9ccfaf35c522897c4)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P121_bt_micp_mic_ctlr_结构体.md) · [返回大纲](大纲.md) · [下一章](P123_bt_micp_mic_dev_cb_结构体.md)
