---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-17
title: bt_conn_le_cs_procedure_enable_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__procedure__enable__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_bt\_conn\_le\_cs\_procedure\_enable\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__procedure__enable__complete.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a2e290c25ec5af8b0259d45f04d6c543d"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#a2e290c25ec5af8b0259d45f04d6c543d)。

<a id="r_acc1d12d347e1b02b2eea562ea064a40b"></a>

```c
enum bt_conn_le_cs_procedure_enable_state state
```

相关声明：[bt_conn_le_cs_procedure_enable_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3653de72793f775e33fd9eb04c3e7a2)、[state](#acc1d12d347e1b02b2eea562ea064a40b)。

<a id="r_a3fa8ad4dd264eb4e2489dea9c1048d22"></a>

```c
enum bt_conn_le_cs_tone_antenna_config_selection tone_antenna_config_selection
```

相关声明：[bt_conn_le_cs_tone_antenna_config_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab7acdbdf273fc760799cf0d8cf71591c)、[tone_antenna_config_selection](#a3fa8ad4dd264eb4e2489dea9c1048d22)。

<a id="r_aeb918e438cd02296c7f693757268f6bf"></a>

```c
int8_t selected_tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[selected_tx_power](#aeb918e438cd02296c7f693757268f6bf)。

<a id="r_ae990a10c468ec62fbaf9325c94733c7c"></a>

```c
uint32_t subevent_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[subevent_len](#ae990a10c468ec62fbaf9325c94733c7c)。

<a id="r_a40b03220932852b6b51d65f557c21f17"></a>

```c
uint8_t subevents_per_event
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevents_per_event](#a40b03220932852b6b51d65f557c21f17)。

<a id="r_a77a2bd8ee384c4567321a09f6b64782c"></a>

```c
uint16_t subevent_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subevent_interval](#a77a2bd8ee384c4567321a09f6b64782c)。

<a id="r_a4129ab9519ba140ffb198aa9a5cde6ac"></a>

```c
uint16_t event_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[event_interval](#a4129ab9519ba140ffb198aa9a5cde6ac)。

<a id="r_a8511deef97f19c53ddaa4dec8492658f"></a>

```c
uint16_t procedure_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[procedure_interval](#a8511deef97f19c53ddaa4dec8492658f)。

<a id="r_ab83778fe2d1274e5658fd5f5f867314f"></a>

```c
uint16_t procedure_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[procedure_count](#ab83778fe2d1274e5658fd5f5f867314f)。

<a id="r_ad71825d71ab89baea138e41f9a3ff57e"></a>

```c
uint16_t max_procedure_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_procedure_len](#ad71825d71ab89baea138e41f9a3ff57e)。

## 17.2\_详细说明（Detailed Documentation）

<a id="a2e290c25ec5af8b0259d45f04d6c543d"></a>

### `config_id`

```c
uint8_t bt_conn_le_cs_procedure_enable_complete::config_id
```

<a id="a4129ab9519ba140ffb198aa9a5cde6ac"></a>

### `event_interval`

```c
uint16_t bt_conn_le_cs_procedure_enable_complete::event_interval
```

<a id="ad71825d71ab89baea138e41f9a3ff57e"></a>

### `max_procedure_len`

```c
uint16_t bt_conn_le_cs_procedure_enable_complete::max_procedure_len
```

<a id="ab83778fe2d1274e5658fd5f5f867314f"></a>

### `procedure_count`

```c
uint16_t bt_conn_le_cs_procedure_enable_complete::procedure_count
```

<a id="a8511deef97f19c53ddaa4dec8492658f"></a>

### `procedure_interval`

```c
uint16_t bt_conn_le_cs_procedure_enable_complete::procedure_interval
```

<a id="aeb918e438cd02296c7f693757268f6bf"></a>

### `selected_tx_power`

```c
int8_t bt_conn_le_cs_procedure_enable_complete::selected_tx_power
```

<a id="acc1d12d347e1b02b2eea562ea064a40b"></a>

### `state`

```c
enum bt_conn_le_cs_procedure_enable_state bt_conn_le_cs_procedure_enable_complete::state
```

<a id="a77a2bd8ee384c4567321a09f6b64782c"></a>

### `subevent_interval`

```c
uint16_t bt_conn_le_cs_procedure_enable_complete::subevent_interval
```

<a id="ae990a10c468ec62fbaf9325c94733c7c"></a>

### `subevent_len`

```c
uint32_t bt_conn_le_cs_procedure_enable_complete::subevent_len
```

<a id="a40b03220932852b6b51d65f557c21f17"></a>

### `subevents_per_event`

```c
uint8_t bt_conn_le_cs_procedure_enable_complete::subevents_per_event
```

<a id="a3fa8ad4dd264eb4e2489dea9c1048d22"></a>

### `tone_antenna_config_selection`

```c
enum bt_conn_le_cs_tone_antenna_config_selection bt_conn_le_cs_procedure_enable_complete::tone_antenna_config_selection
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn_le_cs_procedure_enable_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3653de72793f775e33fd9eb04c3e7a2)
- [bt_conn_le_cs_tone_antenna_config_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab7acdbdf273fc760799cf0d8cf71591c)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_bt_conn_le_cs_fae_table_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_bt_conn_le_cs_subevent_result_结构体.md)
