---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-14
title: bt_bap_broadcast_assistant_add_src_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__assistant__add__src__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_bt\_bap\_broadcast\_assistant\_add\_src\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__assistant__add__src__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

向广播音频扫描服务（Broadcast Audio Scan Service，BASS）服务器添加音频源的参数。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

向广播音频扫描服务（Broadcast Audio Scan Service，BASS）服务器添加音频源的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a2b04d75ca9a740a7d819eae1bcc5cba7"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a2b04d75ca9a740a7d819eae1bcc5cba7)。

广播者（Advertiser）的地址。

<a id="r_a390cd8d887cd256ee74b39b9b516cac4"></a>

```c
uint8_t adv_sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_sid](#a390cd8d887cd256ee74b39b9b516cac4)。

广播集（Advertising Set）的 SID。

<a id="r_ad9af814e8a232230d4ee97c459f47747"></a>

```c
bool pa_sync
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[pa_sync](#ad9af814e8a232230d4ee97c459f47747)。

是否同步到周期性广播（Periodic Advertisements）。

<a id="r_ae50b6b5a3f2c92f01e7070c605b37dde"></a>

```c
uint32_t broadcast_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[broadcast_id](#ae50b6b5a3f2c92f01e7070c605b37dde)。

24 位广播 ID（Broadcast ID）。

<a id="r_acaecbbf7b3c96fe5ca53f90e92fa1e5e"></a>

```c
uint16_t pa_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pa_interval](#acaecbbf7b3c96fe5ca53f90e92fa1e5e)。

周期性广播间隔，单位为毫秒。

<a id="r_a17b67d65b6840c3d4480027b7deb31a5"></a>

```c
uint8_t num_subgroups
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subgroups](#a17b67d65b6840c3d4480027b7deb31a5)。

子组数量。

<a id="r_ab8423e5cce4a6c9ac142221d2e816763"></a>

```c
struct bt_bap_bass_subgroup * subgroups
```

相关声明：[bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)、[subgroups](#ab8423e5cce4a6c9ac142221d2e816763)。

指向子组数组的指针。

## 14.2\_详细说明（Detailed Documentation）

<a id="a2b04d75ca9a740a7d819eae1bcc5cba7"></a>

### `addr`

```c
bt_addr_le_t bt_bap_broadcast_assistant_add_src_param::addr
```

广播者（Advertiser）的地址。

<a id="a390cd8d887cd256ee74b39b9b516cac4"></a>

### `adv_sid`

```c
uint8_t bt_bap_broadcast_assistant_add_src_param::adv_sid
```

广播集（Advertising Set）的 SID。

<a id="ae50b6b5a3f2c92f01e7070c605b37dde"></a>

### `broadcast_id`

```c
uint32_t bt_bap_broadcast_assistant_add_src_param::broadcast_id
```

24 位广播 ID（Broadcast ID）。

<a id="a17b67d65b6840c3d4480027b7deb31a5"></a>

### `num_subgroups`

```c
uint8_t bt_bap_broadcast_assistant_add_src_param::num_subgroups
```

子组数量。

<a id="acaecbbf7b3c96fe5ca53f90e92fa1e5e"></a>

### `pa_interval`

```c
uint16_t bt_bap_broadcast_assistant_add_src_param::pa_interval
```

周期性广播间隔，单位为毫秒。

未知时使用 `BT_BAP_PA_INTERVAL_UNKNOWN`。

<a id="ad9af814e8a232230d4ee97c459f47747"></a>

### `pa_sync`

```c
bool bt_bap_broadcast_assistant_add_src_param::pa_sync
```

是否同步到周期性广播（Periodic Advertisements）。

<a id="ab8423e5cce4a6c9ac142221d2e816763"></a>

### `subgroups`

```c
struct bt_bap_bass_subgroup* bt_bap_broadcast_assistant_add_src_param::subgroups
```

指向子组数组的指针。

可将 `bt_bap_bass_subgroup::bis_sync` 设为 `BT_BAP_BIS_SYNC_NO_PREF`，由广播接收端决定同步到哪个 BIS。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)
- [bt_bap_bass_subgroup::bis_sync](P013_bt_bap_bass_subgroup_结构体.md#ac8061995eb73ba30e335e37714396ff5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_bt_bap_bass_subgroup_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_bt_bap_broadcast_assistant_cb_结构体.md)
