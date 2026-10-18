---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-124
title: bt_le_per_adv_sync_synced_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__synced__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第124章\_bt\_le\_per\_adv\_sync\_synced\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__synced__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与周期广播（Periodic Advertising）成功同步的信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

周期广播成功同步的信息（Successful periodic advertising synchronization information）。此结构在周期广播同步成功建立后提供相关信息，包括广播器地址、广播集标识符（SID）、广播间隔、物理层（PHY）和同步状态，以及服务数据（Service data）、传递同步信息的对等设备等详情。使用周期广播响应，即通过 `CONFIG_BT_PER_ADV_SYNC_RSP` 配置时，还提供子事件信息和响应时序等附加详情。注意（Note）：用于 `bt_le_per_adv_sync_cb` 结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 124.1\_数据成员（Data Fields）

<a id="r_a7ca99b0596b08d153d3ba5310adab125"></a>

```c
const bt_addr_le_t * addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a7ca99b0596b08d153d3ba5310adab125)。

广播器的低功耗地址及类型（Advertiser LE address and type）。

<a id="r_a5489c3038f7fff596316a456fc8d580b"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a5489c3038f7fff596316a456fc8d580b)。

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

<a id="r_a5304e1826face35c506f3b8f6cad7df2"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a5304e1826face35c506f3b8f6cad7df2)。

周期广播间隔（Periodic advertising interval），为 N × 1.25 毫秒。

<a id="r_a8b7709011541e95ceaeac379cc3143bb"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a8b7709011541e95ceaeac379cc3143bb)。

广播器物理层（Advertiser PHY），参见 `bt_gap_le_phy`。

<a id="r_a0dd4b7646da0fadc48e94ff3dc91ef83"></a>

```c
bool recv_enabled
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[recv_enabled](#a0dd4b7646da0fadc48e94ff3dc91ef83)。

正在接收周期广播（Periodic advertisements）时为 `true`，否则为 `false`。

<a id="r_adee2bdafa86a0c3c1dfb4660e85396a3"></a>

```c
uint16_t service_data
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[service_data](#adee2bdafa86a0c3c1dfb4660e85396a3)。

传递同步信息时，由对等设备提供的服务数据（Service Data）。

<a id="r_ada4cda53aa87f29d54f6cd88134efe14"></a>

```c
struct bt_conn * conn
```

相关声明：[bt_conn](P002_bt_conn_结构体.md)、[conn](#ada4cda53aa87f29d54f6cd88134efe14)。

传递周期广播同步信息（Periodic advertising sync）的对等设备。

<a id="r_aaab25f36577948d55b6379abe0590c69"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#aaab25f36577948d55b6379abe0590c69)。

子事件数量（Number of Subevents）。

<a id="r_a9e01fb9462c4874a60ebc5359fe5df14"></a>

```c
uint8_t subevent_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_interval](#a9e01fb9462c4874a60ebc5359fe5df14)。

子事件间隔（Subevent interval），为 N × 1.25 毫秒。

<a id="r_a7bdec5d34b97602aa56c1006dbaf79c4"></a>

```c
uint8_t response_slot_delay
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_delay](#a7bdec5d34b97602aa56c1006dbaf79c4)。

响应时隙延迟（Response slot delay），为 N × 1.25 毫秒。

<a id="r_ae9a696dd9dc28b7505e406961ca89b9a"></a>

```c
uint8_t response_slot_spacing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_spacing](#ae9a696dd9dc28b7505e406961ca89b9a)。

响应时隙间距（Response slot spacing），为 N × 1.25 毫秒。译注：此处单位按原文保留。

## 124.2\_详细说明（Detailed Documentation）

<a id="a7ca99b0596b08d153d3ba5310adab125"></a>

### `addr`

```c
const bt_addr_le_t* bt_le_per_adv_sync_synced_info::addr
```

广播器的低功耗地址及类型（Advertiser LE address and type）。

<a id="ada4cda53aa87f29d54f6cd88134efe14"></a>

### `conn`

```c
struct bt_conn* bt_le_per_adv_sync_synced_info::conn
```

传递周期广播同步信息（Periodic advertising sync）的对等设备。

同步（Sync）在本地创建时，此项始终为 `NULL`。

<a id="a5304e1826face35c506f3b8f6cad7df2"></a>

### `interval`

```c
uint16_t bt_le_per_adv_sync_synced_info::interval
```

周期广播间隔（Periodic advertising interval），为 N × 1.25 毫秒。

<a id="aaab25f36577948d55b6379abe0590c69"></a>

### `num_subevents`

```c
uint8_t bt_le_per_adv_sync_synced_info::num_subevents
```

子事件数量（Number of Subevents）。

<a id="a8b7709011541e95ceaeac379cc3143bb"></a>

### `phy`

```c
uint8_t bt_le_per_adv_sync_synced_info::phy
```

广播器物理层（Advertiser PHY），参见 `bt_gap_le_phy`。

<a id="a0dd4b7646da0fadc48e94ff3dc91ef83"></a>

### `recv_enabled`

```c
bool bt_le_per_adv_sync_synced_info::recv_enabled
```

正在接收周期广播（Periodic advertisements）时为 `true`，否则为 `false`。

<a id="a7bdec5d34b97602aa56c1006dbaf79c4"></a>

### `response_slot_delay`

```c
uint8_t bt_le_per_adv_sync_synced_info::response_slot_delay
```

响应时隙延迟（Response slot delay），为 N × 1.25 毫秒。

<a id="ae9a696dd9dc28b7505e406961ca89b9a"></a>

### `response_slot_spacing`

```c
uint8_t bt_le_per_adv_sync_synced_info::response_slot_spacing
```

响应时隙间距（Response slot spacing），为 N × 1.25 毫秒。译注：此处单位按原文保留。

<a id="adee2bdafa86a0c3c1dfb4660e85396a3"></a>

### `service_data`

```c
uint16_t bt_le_per_adv_sync_synced_info::service_data
```

传递同步信息时，由对等设备提供的服务数据（Service Data）。

同步（Sync）在本地创建时，此项始终为 `0`。

<a id="a5489c3038f7fff596316a456fc8d580b"></a>

### `sid`

```c
uint8_t bt_le_per_adv_sync_synced_info::sid
```

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

<a id="a9e01fb9462c4874a60ebc5359fe5df14"></a>

### `subevent_interval`

```c
uint8_t bt_le_per_adv_sync_synced_info::subevent_interval
```

子事件间隔（Subevent interval），为 N × 1.25 毫秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 124.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_GAP_SID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf05b7660d2ae85f64e2a220abf8e57d)
- [BT_GAP_SID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafa6f803fe3ada07030fb1f2f725940c4)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gap_le_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga691d9793fd21c41b2c192d65cc2bf6c4)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_conn](P002_bt_conn_结构体.md)
- [CONFIG_BT_PER_ADV_SYNC_RSP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_RSP)
- [bt_le_per_adv_sync_cb](P118_bt_le_per_adv_sync_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P123_bt_le_per_adv_sync_subevent_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P125_bt_le_per_adv_sync_term_info_结构体.md)
