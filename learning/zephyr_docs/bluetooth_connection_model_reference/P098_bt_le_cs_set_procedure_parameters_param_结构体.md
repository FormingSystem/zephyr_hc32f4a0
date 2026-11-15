---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-98
title: bt_le_cs_set_procedure_parameters_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__set__procedure__parameters__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_bt\_le\_cs\_set\_procedure\_parameters\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__set__procedure__parameters__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 98.1\_数据成员（Data Fields）

<a id="r_a03e8b91ccc78b02faed1864e6b4ad885"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#a03e8b91ccc78b02faed1864e6b4ad885)。

<a id="r_a9b28e4b6f887201ca7f2188b07d37e4c"></a>

```c
uint16_t max_procedure_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_procedure_len](#a9b28e4b6f887201ca7f2188b07d37e4c)。

<a id="r_a967adc0e39da8e3ff96b998f3807542e"></a>

```c
uint16_t min_procedure_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_procedure_interval](#a967adc0e39da8e3ff96b998f3807542e)。

<a id="r_ac48eb6d0021c676738f17437fdcbc3e8"></a>

```c
uint16_t max_procedure_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_procedure_interval](#ac48eb6d0021c676738f17437fdcbc3e8)。

<a id="r_a7a00113e7849b604efc38d904fce0389"></a>

```c
uint16_t max_procedure_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_procedure_count](#a7a00113e7849b604efc38d904fce0389)。

<a id="r_ab45195cbf8021c861384ead2cedae8da"></a>

```c
uint32_t min_subevent_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_subevent_len](#ab45195cbf8021c861384ead2cedae8da)。

<a id="r_a0166c72225d70e7c1afc9cf9be613835"></a>

```c
uint32_t max_subevent_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_subevent_len](#a0166c72225d70e7c1afc9cf9be613835)。

<a id="r_a3f7c838bcfb9c0e3d7ad803aefdc33c4"></a>

```c
enum bt_conn_le_cs_tone_antenna_config_selection tone_antenna_config_selection
```

相关声明：[bt_conn_le_cs_tone_antenna_config_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab7acdbdf273fc760799cf0d8cf71591c)、[tone_antenna_config_selection](#a3f7c838bcfb9c0e3d7ad803aefdc33c4)。

<a id="r_a7f42131c93874c0be297752d8103b585"></a>

```c
enum bt_le_cs_procedure_phy phy
```

相关声明：[bt_le_cs_procedure_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9e008daa9c0c1702aa3b4479e7a37ca4)、[phy](#a7f42131c93874c0be297752d8103b585)。

<a id="r_abb995a318cf74ff7cbd8882ddfb155cc"></a>

```c
int8_t tx_power_delta
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power_delta](#abb995a318cf74ff7cbd8882ddfb155cc)。

<a id="r_aa1158161ee5e49217ad6a85b6c92d993"></a>

```c
uint8_t preferred_peer_antenna
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[preferred_peer_antenna](#aa1158161ee5e49217ad6a85b6c92d993)。

<a id="r_a2fb81c447beb1238cb88610589458816"></a>

```c
enum bt_le_cs_snr_control snr_control_initiator
```

相关声明：[bt_le_cs_snr_control](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf34c59887e8a6da0560b6428733fe8d0)、[snr_control_initiator](#a2fb81c447beb1238cb88610589458816)。

<a id="r_ab053facc218a6566a31e33d0831d385f"></a>

```c
enum bt_le_cs_snr_control snr_control_reflector
```

相关声明：[bt_le_cs_snr_control](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf34c59887e8a6da0560b6428733fe8d0)、[snr_control_reflector](#ab053facc218a6566a31e33d0831d385f)。

## 98.2\_详细说明（Detailed Documentation）

<a id="a03e8b91ccc78b02faed1864e6b4ad885"></a>

### `config_id`

```c
uint8_t bt_le_cs_set_procedure_parameters_param::config_id
```

<a id="a7a00113e7849b604efc38d904fce0389"></a>

### `max_procedure_count`

```c
uint16_t bt_le_cs_set_procedure_parameters_param::max_procedure_count
```

<a id="ac48eb6d0021c676738f17437fdcbc3e8"></a>

### `max_procedure_interval`

```c
uint16_t bt_le_cs_set_procedure_parameters_param::max_procedure_interval
```

<a id="a9b28e4b6f887201ca7f2188b07d37e4c"></a>

### `max_procedure_len`

```c
uint16_t bt_le_cs_set_procedure_parameters_param::max_procedure_len
```

<a id="a0166c72225d70e7c1afc9cf9be613835"></a>

### `max_subevent_len`

```c
uint32_t bt_le_cs_set_procedure_parameters_param::max_subevent_len
```

<a id="a967adc0e39da8e3ff96b998f3807542e"></a>

### `min_procedure_interval`

```c
uint16_t bt_le_cs_set_procedure_parameters_param::min_procedure_interval
```

<a id="ab45195cbf8021c861384ead2cedae8da"></a>

### `min_subevent_len`

```c
uint32_t bt_le_cs_set_procedure_parameters_param::min_subevent_len
```

<a id="a7f42131c93874c0be297752d8103b585"></a>

### `phy`

```c
enum bt_le_cs_procedure_phy bt_le_cs_set_procedure_parameters_param::phy
```

<a id="aa1158161ee5e49217ad6a85b6c92d993"></a>

### `preferred_peer_antenna`

```c
uint8_t bt_le_cs_set_procedure_parameters_param::preferred_peer_antenna
```

<a id="a2fb81c447beb1238cb88610589458816"></a>

### `snr_control_initiator`

```c
enum bt_le_cs_snr_control bt_le_cs_set_procedure_parameters_param::snr_control_initiator
```

<a id="ab053facc218a6566a31e33d0831d385f"></a>

### `snr_control_reflector`

```c
enum bt_le_cs_snr_control bt_le_cs_set_procedure_parameters_param::snr_control_reflector
```

<a id="a3f7c838bcfb9c0e3d7ad803aefdc33c4"></a>

### `tone_antenna_config_selection`

```c
enum bt_conn_le_cs_tone_antenna_config_selection bt_le_cs_set_procedure_parameters_param::tone_antenna_config_selection
```

<a id="abb995a318cf74ff7cbd8882ddfb155cc"></a>

### `tx_power_delta`

```c
int8_t bt_le_cs_set_procedure_parameters_param::tx_power_delta
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/cs.h`

## 98.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/cs.h](https://docs.zephyrproject.org/latest/doxygen/html/cs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_conn_le_cs_tone_antenna_config_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab7acdbdf273fc760799cf0d8cf71591c)
- [bt_le_cs_procedure_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9e008daa9c0c1702aa3b4479e7a37ca4)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bt_le_cs_snr_control](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf34c59887e8a6da0560b6428733fe8d0)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P097_bt_le_cs_set_default_settings_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P099_bt_le_cs_subevent_step_结构体.md)
