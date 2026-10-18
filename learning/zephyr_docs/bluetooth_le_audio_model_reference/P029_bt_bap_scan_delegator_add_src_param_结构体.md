---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-29
title: bt_bap_scan_delegator_add_src_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__scan__delegator__add__src__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_bt\_bap\_scan\_delegator\_add\_src\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__scan__delegator__add__src__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

`bt_bap_scan_delegator_add_src()` 的参数。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

`bt_bap_scan_delegator_add_src()` 的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_a751106648b8f040747b5ffb804932798"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a751106648b8f040747b5ffb804932798)。

周期性广播者地址（Periodic Advertiser Address）。

<a id="r_a80817dd3bc046d76baabd62e470ad797"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a80817dd3bc046d76baabd62e470ad797)。

广播者 SID。

<a id="r_a0945a707a9a50a152220463ba1678de0"></a>

```c
enum bt_bap_pa_state pa_state
```

相关声明：[bt_bap_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac551e9b0d53fd50f3a9e9c08447f0296)、[pa_state](#a0945a707a9a50a152220463ba1678de0)。

周期性广播同步状态（Periodic Advertising Sync State）。

<a id="r_a502d263982995c99559714f07d74443f"></a>

```c
enum bt_bap_big_enc_state encrypt_state
```

相关声明：[bt_bap_big_enc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5e0b0f70d247e131fa542fae16826a22)、[encrypt_state](#a502d263982995c99559714f07d74443f)。

广播等时组（Broadcast Isochronous Group，BIG）的加密状态。

<a id="r_a8e8eda4139e460800c6195b4c5f246e2"></a>

```c
uint32_t broadcast_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[broadcast_id](#a8e8eda4139e460800c6195b4c5f246e2)。

24 位广播 ID。

<a id="r_a12bed26ffdc9d4683a5fcdf512a194eb"></a>

```c
uint8_t num_subgroups
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subgroups](#a12bed26ffdc9d4683a5fcdf512a194eb)。

子组数量。

<a id="r_ac64d1608bede3b9fbac5f86488a3ac79"></a>

```c
struct bt_bap_bass_subgroup subgroups [0]
```

相关声明：[bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)、[subgroups](#ac64d1608bede3b9fbac5f86488a3ac79)。

子组专用信息。

## 29.2\_详细说明（Detailed Documentation）

<a id="a751106648b8f040747b5ffb804932798"></a>

### `addr`

```c
bt_addr_le_t bt_bap_scan_delegator_add_src_param::addr
```

周期性广播者地址（Periodic Advertiser Address）。

<a id="a8e8eda4139e460800c6195b4c5f246e2"></a>

### `broadcast_id`

```c
uint32_t bt_bap_scan_delegator_add_src_param::broadcast_id
```

24 位广播 ID。

<a id="a502d263982995c99559714f07d74443f"></a>

### `encrypt_state`

```c
enum bt_bap_big_enc_state bt_bap_scan_delegator_add_src_param::encrypt_state
```

广播等时组（Broadcast Isochronous Group，BIG）的加密状态。

<a id="a12bed26ffdc9d4683a5fcdf512a194eb"></a>

### `num_subgroups`

```c
uint8_t bt_bap_scan_delegator_add_src_param::num_subgroups
```

子组数量。

<a id="a0945a707a9a50a152220463ba1678de0"></a>

### `pa_state`

```c
enum bt_bap_pa_state bt_bap_scan_delegator_add_src_param::pa_state
```

周期性广播同步状态（Periodic Advertising Sync State）。

通常是 `BT_BAP_PA_STATE_NOT_SYNCED` 或 `BT_BAP_PA_STATE_SYNCED`。

<a id="a80817dd3bc046d76baabd62e470ad797"></a>

### `sid`

```c
uint8_t bt_bap_scan_delegator_add_src_param::sid
```

广播者 SID。

<a id="ac64d1608bede3b9fbac5f86488a3ac79"></a>

### `subgroups`

```c
struct bt_bap_bass_subgroup bt_bap_scan_delegator_add_src_param::subgroups[ 0]
```

子组专用信息。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 29.3\_原页交叉引用（Cross References）

- [bt_bap_scan_delegator_add_src()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6eb2a782d761da12d112356cfe723ff0)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bap_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac551e9b0d53fd50f3a9e9c08447f0296)
- [bt_bap_big_enc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5e0b0f70d247e131fa542fae16826a22)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)
- [BT_BAP_PA_STATE_NOT_SYNCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf)
- [BT_BAP_PA_STATE_SYNCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_bt_bap_qos_cfg_pref_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_bt_bap_scan_delegator_cb_结构体.md)
