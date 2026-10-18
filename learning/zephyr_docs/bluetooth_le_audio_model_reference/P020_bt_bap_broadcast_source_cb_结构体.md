---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-20
title: bt_bap_broadcast_source_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_bt\_bap\_broadcast\_source\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存广播音频源（Broadcast Source）回调的结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

保存广播音频源（Broadcast Source）回调的结构体。可使用 `bt_bap_broadcast_source_register_cb()` 注册这些回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a1108c983823ee3331d8343db4ec9c0c5"></a>

```c
void(* started )(struct bt_bap_broadcast_source *source)
```

相关声明：[started](#a1108c983823ee3331d8343db4ec9c0c5)、[bt_bap_broadcast_source](P019_bt_bap_broadcast_source_结构体.md)。

广播音频源已启动，其所有流均已准备好传输音频数据。

<a id="r_a66b62e90c1cdfa2c2963bafe99670f92"></a>

```c
void(* stopped )(struct bt_bap_broadcast_source *source, uint8_t reason)
```

相关声明：[stopped](#a66b62e90c1cdfa2c2963bafe99670f92)、[bt_bap_broadcast_source](P019_bt_bap_broadcast_source_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

广播音频源已停止，其所有流均未准备好传输音频数据。

## 20.2\_详细说明（Detailed Documentation）

<a id="a1108c983823ee3331d8343db4ec9c0c5"></a>

### `started`

```c
void(* bt_bap_broadcast_source_cb::started) (struct bt_bap_broadcast_source *source)
```

广播音频源已启动，其所有流均已准备好传输音频数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 已启动的广播音频源。 |

<a id="a66b62e90c1cdfa2c2963bafe99670f92"></a>

### `stopped`

```c
void(* bt_bap_broadcast_source_cb::stopped) (struct bt_bap_broadcast_source *source, uint8_t reason)
```

广播音频源已停止，其所有流均未准备好传输音频数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 已停止的广播音频源。 |
| `reason` | 广播音频源停止的原因，参见 `BT_HCI_ERR_*` 值。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_bap_broadcast_source](P019_bt_bap_broadcast_source_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bap_broadcast_source_register_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gac75ad00b8f9a1cd7048677a33b17acda)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_bt_bap_broadcast_source_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_bt_bap_broadcast_source_param_结构体.md)
