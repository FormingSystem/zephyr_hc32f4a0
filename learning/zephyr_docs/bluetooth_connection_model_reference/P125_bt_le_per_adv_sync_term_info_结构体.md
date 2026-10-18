---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-125
title: bt_le_per_adv_sync_term_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__term__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_bt\_le\_per\_adv\_sync\_term\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__term__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

周期广播同步（Periodic Advertising Sync）终止的信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

周期广播同步终止信息（Periodic advertising sync termination information）。此结构提供同步终止的相关信息，包括广播器地址、广播集标识符（SID）和终止原因。同步因本地请求、远端请求或数据缺失而终止时，通过回调提供这些信息；数据缺失可能由超出范围、失去同步等原因造成。注意（Note）：用于 `bt_le_per_adv_sync_cb` 结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 125.1\_数据成员（Data Fields）

<a id="r_a2b76ccd5e4c9933f2c05db2ec5b8e2fc"></a>

```c
const bt_addr_le_t * addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a2b76ccd5e4c9933f2c05db2ec5b8e2fc)。

广播器的低功耗地址及类型（Advertiser LE address and type）。

<a id="r_a7a5f2ecccaf698bad86f10d9a7d16189"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a7a5f2ecccaf698bad86f10d9a7d16189)。

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

<a id="r_a429b8b665eacbfe9db013a571b829bac"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#a429b8b665eacbfe9db013a571b829bac)。

周期广播终止原因（Periodic advertising termination cause），参见 `BT_HCI_ERR_*` 值。

## 125.2\_详细说明（Detailed Documentation）

<a id="a2b76ccd5e4c9933f2c05db2ec5b8e2fc"></a>

### `addr`

```c
const bt_addr_le_t* bt_le_per_adv_sync_term_info::addr
```

广播器的低功耗地址及类型（Advertiser LE address and type）。

<a id="a429b8b665eacbfe9db013a571b829bac"></a>

### `reason`

```c
uint8_t bt_le_per_adv_sync_term_info::reason
```

周期广播终止原因（Periodic advertising termination cause），参见 `BT_HCI_ERR_*` 值。

<a id="a7a5f2ecccaf698bad86f10d9a7d16189"></a>

### `sid`

```c
uint8_t bt_le_per_adv_sync_term_info::sid
```

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 125.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_GAP_SID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf05b7660d2ae85f64e2a220abf8e57d)
- [BT_GAP_SID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafa6f803fe3ada07030fb1f2f725940c4)
- [bt_le_per_adv_sync_cb](P118_bt_le_per_adv_sync_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P124_bt_le_per_adv_sync_synced_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P126_bt_le_per_adv_sync_transfer_param_结构体.md)
