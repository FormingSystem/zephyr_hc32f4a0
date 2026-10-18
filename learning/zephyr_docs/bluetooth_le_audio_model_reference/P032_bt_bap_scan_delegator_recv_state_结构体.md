---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-32
title: bt_bap_scan_delegator_recv_state_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__scan__delegator__recv__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_bt\_bap\_scan\_delegator\_recv\_state\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__scan__delegator__recv__state.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

表示广播音频扫描服务（BASS）的接收状态。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

表示广播音频扫描服务（BASS）的接收状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_a1755a6332c86aeaf624d3c540037772a"></a>

```c
uint8_t src_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src_id](#a1755a6332c86aeaf624d3c540037772a)。

音频源 ID（Source ID）。

<a id="r_a6153ea6bbfe7057c39f6b652a4e6e34e"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a6153ea6bbfe7057c39f6b652a4e6e34e)。

蓝牙地址（Bluetooth Address）。

<a id="r_aa03e02a1832950e4a53ff2fe803c14a6"></a>

```c
uint8_t adv_sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_sid](#aa03e02a1832950e4a53ff2fe803c14a6)。

广播集 ID（Advertising Set ID）。

<a id="r_a30fbad06780fd7bca9aacdf14ecaf4a0"></a>

```c
enum bt_bap_pa_state pa_sync_state
```

相关声明：[bt_bap_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac551e9b0d53fd50f3a9e9c08447f0296)、[pa_sync_state](#a30fbad06780fd7bca9aacdf14ecaf4a0)。

周期性广播同步状态。

<a id="r_ac770a5ad001f73d3acaf2b36827f9343"></a>

```c
enum bt_bap_big_enc_state encrypt_state
```

相关声明：[bt_bap_big_enc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5e0b0f70d247e131fa542fae16826a22)、[encrypt_state](#ac770a5ad001f73d3acaf2b36827f9343)。

广播等时组（Broadcast Isochronous Group，BIG）的加密状态。

<a id="r_abaa80f30cf2e84ee873d18eaedd4159d"></a>

```c
uint32_t broadcast_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[broadcast_id](#abaa80f30cf2e84ee873d18eaedd4159d)。

24 位广播 ID。

<a id="r_a1c268bb7b340c874935f186c0ba2a253"></a>

```c
uint8_t bad_code [BT_ISO_BROADCAST_CODE_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bad_code](#a1c268bb7b340c874935f186c0ba2a253)、[BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)。

错误的广播码（Bad Broadcast Code）。

<a id="r_aa97765bdbaa43a280645eb62c0035b82"></a>

```c
uint8_t num_subgroups
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subgroups](#aa97765bdbaa43a280645eb62c0035b82)。

子组数量。

<a id="r_a49030d5859dfc21e9a4478b6ed20994e"></a>

```c
struct bt_bap_bass_subgroup subgroups [0]
```

相关声明：[bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)、[subgroups](#a49030d5859dfc21e9a4478b6ed20994e)。

子组专用信息。

## 32.2\_详细说明（Detailed Documentation）

<a id="a6153ea6bbfe7057c39f6b652a4e6e34e"></a>

### `addr`

```c
bt_addr_le_t bt_bap_scan_delegator_recv_state::addr
```

蓝牙地址（Bluetooth Address）。

<a id="aa03e02a1832950e4a53ff2fe803c14a6"></a>

### `adv_sid`

```c
uint8_t bt_bap_scan_delegator_recv_state::adv_sid
```

广播集 ID（Advertising Set ID）。

<a id="a1c268bb7b340c874935f186c0ba2a253"></a>

### `bad_code`

```c
uint8_t bt_bap_scan_delegator_recv_state::bad_code[BT_ISO_BROADCAST_CODE_SIZE]
```

错误的广播码（Bad Broadcast Code）。

仅当 `encrypt_state` 为 `BT_BAP_BIG_ENC_STATE_BCODE_REQ` 时有效。

<a id="abaa80f30cf2e84ee873d18eaedd4159d"></a>

### `broadcast_id`

```c
uint32_t bt_bap_scan_delegator_recv_state::broadcast_id
```

24 位广播 ID。

<a id="ac770a5ad001f73d3acaf2b36827f9343"></a>

### `encrypt_state`

```c
enum bt_bap_big_enc_state bt_bap_scan_delegator_recv_state::encrypt_state
```

广播等时组（Broadcast Isochronous Group，BIG）的加密状态。

<a id="aa97765bdbaa43a280645eb62c0035b82"></a>

### `num_subgroups`

```c
uint8_t bt_bap_scan_delegator_recv_state::num_subgroups
```

子组数量。

<a id="a30fbad06780fd7bca9aacdf14ecaf4a0"></a>

### `pa_sync_state`

```c
enum bt_bap_pa_state bt_bap_scan_delegator_recv_state::pa_sync_state
```

周期性广播同步状态。

<a id="a1755a6332c86aeaf624d3c540037772a"></a>

### `src_id`

```c
uint8_t bt_bap_scan_delegator_recv_state::src_id
```

音频源 ID（Source ID）。

<a id="a49030d5859dfc21e9a4478b6ed20994e"></a>

### `subgroups`

```c
struct bt_bap_bass_subgroup bt_bap_scan_delegator_recv_state::subgroups[ 0]
```

子组专用信息。

如果 `bt_bap_bass_subgroup::bis_sync` 值为 `BT_BAP_BIS_SYNC_FAILED`，则表示 BIG 同步失败。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_bap_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac551e9b0d53fd50f3a9e9c08447f0296)
- [bt_bap_big_enc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5e0b0f70d247e131fa542fae16826a22)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)
- [bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)
- [BT_BAP_BIG_ENC_STATE_BCODE_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2)
- [bt_bap_bass_subgroup::bis_sync](P013_bt_bap_bass_subgroup_结构体.md#ac8061995eb73ba30e335e37714396ff5)
- [BT_BAP_BIS_SYNC_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga2a2e4a06f6e39360458fe2e4d0b66833)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_bt_bap_scan_delegator_mod_src_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_bt_bap_stream_结构体.md)
