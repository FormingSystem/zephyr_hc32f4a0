---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-174
title: bt_tbs_client_call_state_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__client__call__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第174章\_bt\_tbs\_client\_call\_state\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__client__call__state.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存呼叫状态（Call State）的结构。

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

<a id="details"></a>

保存呼叫状态（Call State）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 174.1\_数据成员（Data Fields）

<a id="r_a3d6eb4dda7adcd16c04ebbd41242c292"></a>

```c
uint8_t index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[index](#a3d6eb4dda7adcd16c04ebbd41242c292)。

通话索引。

<a id="r_a3e758ad6d0b35f26f43584e50c9a9895"></a>

```c
uint8_t state
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](#a3e758ad6d0b35f26f43584e50c9a9895)。

通话状态，参见 `BT_TBS_CALL_STATE_*`。

<a id="r_a57ed9dd726faa3c219e1c858ad6659d9"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a57ed9dd726faa3c219e1c858ad6659d9)。

通话标志，参见 `BT_TBS_CALL_FLAG_*`。

## 174.2\_详细说明（Detailed Documentation）

<a id="a57ed9dd726faa3c219e1c858ad6659d9"></a>

### `flags`

```c
uint8_t bt_tbs_client_call_state::flags
```

通话标志，参见 `BT_TBS_CALL_FLAG_*`。

<a id="a3d6eb4dda7adcd16c04ebbd41242c292"></a>

### `index`

```c
uint8_t bt_tbs_client_call_state::index
```

通话索引。

<a id="a3e758ad6d0b35f26f43584e50c9a9895"></a>

### `state`

```c
uint8_t bt_tbs_client_call_state::state
```

通话状态，参见 `BT_TBS_CALL_STATE_*`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/tbs.h`

## 174.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/tbs.h](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P173_bt_tbs_client_call_结构体.md) · [返回大纲](大纲.md) · [下一章](P175_bt_tbs_client_cb_结构体.md)
