---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-247
title: bt_hci_evt_le_cs_subevent_result_continue_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__subevent__result__continue.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第247章\_bt\_hci\_evt\_le\_cs\_subevent\_result\_continue\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__subevent__result__continue.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 247.1\_数据成员（Data Fields）

<a id="r_a4126bebec093f6f4d1a22b43abec6b1c"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a4126bebec093f6f4d1a22b43abec6b1c)。

<a id="r_adefb9ad1f998460a6d235ebd39bbfe4a"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#adefb9ad1f998460a6d235ebd39bbfe4a)。

<a id="r_a3e5b1e8a247fff36c06447c9ff7c3bb8"></a>

```c
uint8_t procedure_done_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[procedure_done_status](#a3e5b1e8a247fff36c06447c9ff7c3bb8)。

<a id="r_a49cf181c8518fb3015a0c54f7558aa8c"></a>

```c
uint8_t subevent_done_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_done_status](#a49cf181c8518fb3015a0c54f7558aa8c)。

<a id="r_a1801aeaac839831198e17b7d96a5532a"></a>

```c
uint8_t subevent_abort_reason: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_abort_reason](#a1801aeaac839831198e17b7d96a5532a)。

<a id="r_a3c7ac056a5898710ffbc0776ef551b4b"></a>

```c
uint8_t procedure_abort_reason: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[procedure_abort_reason](#a3c7ac056a5898710ffbc0776ef551b4b)。

<a id="r_a2f8e1f634e28100815c881a463b51f2c"></a>

```c
uint8_t num_antenna_paths
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antenna_paths](#a2f8e1f634e28100815c881a463b51f2c)。

<a id="r_af127774b52c4e088f628999136b6cd7c"></a>

```c
uint8_t num_steps_reported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_steps_reported](#af127774b52c4e088f628999136b6cd7c)。

<a id="r_abbddd0e27178e49abe6eef62bc094a16"></a>

```c
uint8_t steps []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[steps](#abbddd0e27178e49abe6eef62bc094a16)。

## 247.2\_详细说明（Detailed Documentation）

<a id="adefb9ad1f998460a6d235ebd39bbfe4a"></a>

### `config_id`

```c
uint8_t bt_hci_evt_le_cs_subevent_result_continue::config_id
```

<a id="a4126bebec093f6f4d1a22b43abec6b1c"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_cs_subevent_result_continue::conn_handle
```

<a id="a2f8e1f634e28100815c881a463b51f2c"></a>

### `num_antenna_paths`

```c
uint8_t bt_hci_evt_le_cs_subevent_result_continue::num_antenna_paths
```

<a id="af127774b52c4e088f628999136b6cd7c"></a>

### `num_steps_reported`

```c
uint8_t bt_hci_evt_le_cs_subevent_result_continue::num_steps_reported
```

<a id="a3c7ac056a5898710ffbc0776ef551b4b"></a>

### `procedure_abort_reason`

```c
uint8_t bt_hci_evt_le_cs_subevent_result_continue::procedure_abort_reason
```

<a id="a3e5b1e8a247fff36c06447c9ff7c3bb8"></a>

### `procedure_done_status`

```c
uint8_t bt_hci_evt_le_cs_subevent_result_continue::procedure_done_status
```

<a id="abbddd0e27178e49abe6eef62bc094a16"></a>

### `steps`

```c
uint8_t bt_hci_evt_le_cs_subevent_result_continue::steps[]
```

<a id="a1801aeaac839831198e17b7d96a5532a"></a>

### `subevent_abort_reason`

```c
uint8_t bt_hci_evt_le_cs_subevent_result_continue::subevent_abort_reason
```

<a id="a49cf181c8518fb3015a0c54f7558aa8c"></a>

### `subevent_done_status`

```c
uint8_t bt_hci_evt_le_cs_subevent_result_continue::subevent_done_status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 247.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P246_bt_hci_evt_le_cs_subevent_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md)
