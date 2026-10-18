---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-123
title: bt_le_per_adv_sync_subevent_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__subevent__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_bt\_le\_per\_adv\_sync\_subevent\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__subevent__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与特定周期广播子事件（Periodic Advertising Subevent）同步的参数。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

同步到指定周期广播子事件的参数（Periodic advertising subevent synchronization parameters）。此结构用于同步到周期广播子事件的一个子集，包含周期广播属性、要同步的子事件数量以及控制器应同步的子事件列表。注意（Note）：用于 `bt_le_per_adv_sync_subevent` 函数，控制同步行为。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 123.1\_数据成员（Data Fields）

<a id="r_a6b23cd4b7e6a3f1d65b9a7eff85bcfb4"></a>

```c
uint16_t properties
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[properties](#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4)。

周期广播属性（Periodic Advertising Properties）。

<a id="r_a867c66bf09461a4369da3d250701d2ae"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#a867c66bf09461a4369da3d250701d2ae)。

要同步的子事件数量（Number of subevents）。

<a id="r_a5ac4e81ddd63797f921105748344c125"></a>

```c
uint8_t * subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevents](#a5ac4e81ddd63797f921105748344c125)。

要同步的子事件（Subevents）。

## 123.2\_详细说明（Detailed Documentation）

<a id="a867c66bf09461a4369da3d250701d2ae"></a>

### `num_subevents`

```c
uint8_t bt_le_per_adv_sync_subevent_params::num_subevents
```

要同步的子事件数量（Number of subevents）。

<a id="a6b23cd4b7e6a3f1d65b9a7eff85bcfb4"></a>

### `properties`

```c
uint16_t bt_le_per_adv_sync_subevent_params::properties
```

周期广播属性（Periodic Advertising Properties）。

位 6 表示包含发射功率（TxPower），其余位保留供将来使用（RFU）。

<a id="a5ac4e81ddd63797f921105748344c125"></a>

### `subevents`

```c
uint8_t* bt_le_per_adv_sync_subevent_params::subevents
```

要同步的子事件（Subevents）。

数组必须包含 `num_subevents` 个元素。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 123.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_per_adv_sync_subevent](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga731f4b37a9e5cc13a6816ea23f751b0b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P122_bt_le_per_adv_sync_state_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P124_bt_le_per_adv_sync_synced_info_结构体.md)
