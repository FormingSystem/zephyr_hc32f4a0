---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-72
title: bt_iso_big_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__big__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_bt\_iso\_big\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__big__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存广播等时组（Broadcast Isochronous Group）回调的结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

保存广播等时组回调（Broadcast Isochronous Group callbacks）的结构。可使用 `bt_iso_big_register_cb()` 注册这些回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_ac84e00545dbb330311482eb5abd4a78b"></a>

```c
void(* started )(struct bt_iso_big *big)
```

相关声明：[started](#ac84e00545dbb330311482eb5abd4a78b)、[bt_iso_big](P071_bt_iso_big_结构体.md)。

广播等时组（BIG）已启动，所有流均已准备好传输数据。

<a id="r_a43d6ee745f7852460f843ced33c777c2"></a>

```c
void(* stopped )(struct bt_iso_big *big, uint8_t reason)
```

相关声明：[stopped](#a43d6ee745f7852460f843ced33c777c2)、[bt_iso_big](P071_bt_iso_big_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

广播等时组（BIG）已停止，所有流均无法传输数据。

## 72.2\_详细说明（Detailed Documentation）

<a id="ac84e00545dbb330311482eb5abd4a78b"></a>

### `started`

```c
void(* bt_iso_big_cb::started) (struct bt_iso_big *big)
```

广播等时组（BIG）已启动，所有流均已准备好传输数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `big` | 已启动的广播等时组（BIG）。 |

<a id="a43d6ee745f7852460f843ced33c777c2"></a>

### `stopped`

```c
void(* bt_iso_big_cb::stopped) (struct bt_iso_big *big, uint8_t reason)
```

广播等时组（BIG）已停止，所有流均无法传输数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `big` | 已停止的广播等时组（BIG）。 |
| `reason` | 广播等时组（BIG）停止的原因，参见 `BT_HCI_ERR_*` 值。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_iso_big](P071_bt_iso_big_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_iso_big_register_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8a01a56e4a4555ed65a67065facfca76)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_bt_iso_big_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_bt_iso_big_create_param_结构体.md)
