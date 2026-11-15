---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-90
title: bt_hfp_hf_current_call_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__hf__current__call.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_bt\_hfp\_hf\_current\_call\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__hf__current__call.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

当前呼叫（Current Call）的信息。

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

<a id="details"></a>

当前通话信息。此结构体包含当前通话的完整信息，包括索引、方向、状态、模式、多方通话状态、电话号码及号码类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 90.1\_数据成员（Data Fields）

<a id="r_a9f72915247e66423303a77e6d5382d47"></a>

```c
uint8_t index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[index](#a9f72915247e66423303a77e6d5382d47)。

通话索引标识符（Call index identifier）。

<a id="r_a69968974df79327c5dabd58f1804df2e"></a>

```c
enum bt_hfp_hf_call_dir dir
```

相关声明：[bt_hfp_hf_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga6c2ba70d70c8f9d6d569662086985c85)、[dir](#a69968974df79327c5dabd58f1804df2e)。

通话方向：呼入或呼出（incoming/outgoing）。

<a id="r_a8c2b49def7926a992e84c175eca3aa2e"></a>

```c
enum bt_hfp_hf_call_status status
```

相关声明：[bt_hfp_hf_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga810c80de5baf92feb23650374b60bcee)、[status](#a8c2b49def7926a992e84c175eca3aa2e)。

通话的当前状态。

<a id="r_ae4f1cd6e24e2ef79a009bba9b30c53ee"></a>

```c
enum bt_hfp_hf_call_mode mode
```

相关声明：[bt_hfp_hf_call_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga38619377f146492993ee9a92a487af50)、[mode](#ae4f1cd6e24e2ef79a009bba9b30c53ee)。

通话模式：语音、数据或传真（voice/data/fax）。

<a id="r_aa25db76c59d82c16c0a1db1f509104f8"></a>

```c
bool multiparty
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[multiparty](#aa25db76c59d82c16c0a1db1f509104f8)。

若此通话属于多方会议通话（multiparty conference），则为 `true`。

<a id="r_ac384ffbde33c521f305f1283520e0c66"></a>

```c
const char * number
```

相关声明：[number](#ac384ffbde33c521f305f1283520e0c66)。

电话号码字符串；不可用时为 `NULL`。

<a id="r_a6cefa6a215650f8380a54cda44ce5f19"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a6cefa6a215650f8380a54cda44ce5f19)。

电话号码类型的格式标识符。

## 90.2\_详细说明（Detailed Documentation）

<a id="a69968974df79327c5dabd58f1804df2e"></a>

### `dir`

```c
enum bt_hfp_hf_call_dir bt_hfp_hf_current_call::dir
```

通话方向：呼入或呼出（incoming/outgoing）。

<a id="a9f72915247e66423303a77e6d5382d47"></a>

### `index`

```c
uint8_t bt_hfp_hf_current_call::index
```

通话索引标识符（Call index identifier）。

<a id="ae4f1cd6e24e2ef79a009bba9b30c53ee"></a>

### `mode`

```c
enum bt_hfp_hf_call_mode bt_hfp_hf_current_call::mode
```

通话模式：语音、数据或传真（voice/data/fax）。

<a id="aa25db76c59d82c16c0a1db1f509104f8"></a>

### `multiparty`

```c
bool bt_hfp_hf_current_call::multiparty
```

若此通话属于多方会议通话（multiparty conference），则为 `true`。

<a id="ac384ffbde33c521f305f1283520e0c66"></a>

### `number`

```c
const char* bt_hfp_hf_current_call::number
```

电话号码字符串；不可用时为 `NULL`。

<a id="a8c2b49def7926a992e84c175eca3aa2e"></a>

### `status`

```c
enum bt_hfp_hf_call_status bt_hfp_hf_current_call::status
```

通话的当前状态。

<a id="a6cefa6a215650f8380a54cda44ce5f19"></a>

### `type`

```c
uint8_t bt_hfp_hf_current_call::type
```

电话号码类型的格式标识符。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/hfp_hf.h`

## 90.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/hfp_hf.h](https://docs.zephyrproject.org/latest/doxygen/html/hfp__hf_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hfp_hf_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga6c2ba70d70c8f9d6d569662086985c85)
- [bt_hfp_hf_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga810c80de5baf92feb23650374b60bcee)
- [bt_hfp_hf_call_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga38619377f146492993ee9a92a487af50)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P089_bt_hfp_hf_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P091_bt_hid_device_cb_结构体.md)
