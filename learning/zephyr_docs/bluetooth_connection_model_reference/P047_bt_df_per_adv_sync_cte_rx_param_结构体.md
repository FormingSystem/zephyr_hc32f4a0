---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-47
title: bt_df_per_adv_sync_cte_rx_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__per__adv__sync__cte__rx__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_bt\_df\_per\_adv\_sync\_cte\_rx\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__per__adv__sync__cte__rx__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

无连接接收（Connectionless Reception）的恒定音调扩展参数。

```c
#include <zephyr/bluetooth/direction.h>
```

<a id="details"></a>

无连接接收的恒定音调扩展参数（Constant Tone Extension parameters for connectionless reception）。注意（Note）：`cte_type` 是位域，用于指明应用预期的 CTE 类型，参见 `bt_df_cte_type`。若 `cte_type` 中未设置 `BT_DF_CTE_TYPE_AOA` 位，则不要求提供 `slot_durations`、`num_ant_ids` 和 `ant_ids` 成员，也不会检查它们的值是否正确。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_a1740d3f41dddd755fc1e04216c8070e5"></a>

```c
uint8_t cte_types
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_types](#a1740d3f41dddd755fc1e04216c8070e5)。

允许的恒定音调扩展类型位域（CTE types bitfield）。

<a id="r_abff68c9f2e42e3fe6e8b155f5390f219"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#abff68c9f2e42e3fe6e8b155f5390f219)。

天线切换时隙（Antenna switching slots），参见 `bt_df_antenna_switching_slot`。

<a id="r_ac64232b5e9b2c6acfadfca1c95fd1021"></a>

```c
uint8_t max_cte_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_cte_count](#ac64232b5e9b2c6acfadfca1c95fd1021)。

最多接收的恒定音调扩展数量（CTEs）。

<a id="r_ae358cbd7b1dd59a7d0a931c8a5fbd94d"></a>

```c
uint8_t num_ant_ids
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_ant_ids](#ae358cbd7b1dd59a7d0a931c8a5fbd94d)。

天线切换模式长度（Antenna switch pattern length）。

<a id="r_ac83de1a86fef076d6c8fc6bccbe49a64"></a>

```c
const uint8_t * ant_ids
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#ac83de1a86fef076d6c8fc6bccbe49a64)。

天线切换模式（Antenna switch pattern）。

## 47.2\_详细说明（Detailed Documentation）

<a id="ac83de1a86fef076d6c8fc6bccbe49a64"></a>

### `ant_ids`

```c
const uint8_t* bt_df_per_adv_sync_cte_rx_param::ant_ids
```

天线切换模式（Antenna switch pattern）。

<a id="a1740d3f41dddd755fc1e04216c8070e5"></a>

### `cte_types`

```c
uint8_t bt_df_per_adv_sync_cte_rx_param::cte_types
```

允许的恒定音调扩展类型位域（CTE types bitfield）。

允许值由 `bt_df_cte_type` 定义，但不包含 `BT_DF_CTE_TYPE_NONE`。

<a id="ac64232b5e9b2c6acfadfca1c95fd1021"></a>

### `max_cte_count`

```c
uint8_t bt_df_per_adv_sync_cte_rx_param::max_cte_count
```

最多接收的恒定音调扩展数量（CTEs）。

最小值为 `1`，最大值为 `10`；`0` 表示持续接收（Receive continuously）。

<a id="ae358cbd7b1dd59a7d0a931c8a5fbd94d"></a>

### `num_ant_ids`

```c
uint8_t bt_df_per_adv_sync_cte_rx_param::num_ant_ids
```

天线切换模式长度（Antenna switch pattern length）。

<a id="abff68c9f2e42e3fe6e8b155f5390f219"></a>

### `slot_durations`

```c
uint8_t bt_df_per_adv_sync_cte_rx_param::slot_durations
```

天线切换时隙（Antenna switching slots），参见 `bt_df_antenna_switching_slot`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/direction.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/direction.h](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_df_antenna_switching_slot](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a546598ce9a81161ad1ba098a7b1a8df4)
- [bt_df_cte_type](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_bt_df_conn_iq_samples_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_bt_df_per_adv_sync_iq_samples_report_结构体.md)
