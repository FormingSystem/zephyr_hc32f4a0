---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-42
title: bt_df_adv_cte_tx_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__adv__cte__tx__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_bt\_df\_adv\_cte\_tx\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__adv__cte__tx__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

无连接传输（Connectionless Transmission）的恒定音调扩展（Constant Tone Extension，CTE）参数。

```c
#include <zephyr/bluetooth/direction.h>
```

<a id="details"></a>

无连接发送的恒定音调扩展参数（Constant Tone Extension parameters for connectionless transmission）。此结构保存配置周期广播（Periodic advertising）中的 CTE 发送所需的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a2ab62db4279338e05cd9e5c222c3aab2"></a>

```c
uint8_t cte_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_len](#a2ab62db4279338e05cd9e5c222c3aab2)。

恒定音调扩展长度（CTE length），以 8 微秒为单位。

<a id="r_a4af32abbb603d1b7a533771a23d6e9ee"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a4af32abbb603d1b7a533771a23d6e9ee)。

恒定音调扩展类型（CTE type）。

<a id="r_a288d635221a752b231033803acddd261"></a>

```c
uint8_t cte_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_count](#a288d635221a752b231033803acddd261)。

每个周期广播间隔内发送的恒定音调扩展数量（CTE count）。

<a id="r_ac974c5bb804912f5940b2ede5f6394a1"></a>

```c
uint8_t num_ant_ids
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_ant_ids](#ac974c5bb804912f5940b2ede5f6394a1)。

切换模式（Switch pattern）中的天线标识符数量（Antenna IDs）。

<a id="r_ac1f251cb2205ce345dc3815b53f13918"></a>

```c
uint8_t * ant_ids
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#ac1f251cb2205ce345dc3815b53f13918)。

模式中的天线标识符列表（Antenna ID list）。

## 42.2\_详细说明（Detailed Documentation）

<a id="ac1f251cb2205ce345dc3815b53f13918"></a>

### `ant_ids`

```c
uint8_t* bt_df_adv_cte_tx_param::ant_ids
```

模式中的天线标识符列表（Antenna ID list）。

<a id="a288d635221a752b231033803acddd261"></a>

### `cte_count`

```c
uint8_t bt_df_adv_cte_tx_param::cte_count
```

每个周期广播间隔内发送的恒定音调扩展数量（CTE count）。

<a id="a2ab62db4279338e05cd9e5c222c3aab2"></a>

### `cte_len`

```c
uint8_t bt_df_adv_cte_tx_param::cte_len
```

恒定音调扩展长度（CTE length），以 8 微秒为单位。

<a id="a4af32abbb603d1b7a533771a23d6e9ee"></a>

### `cte_type`

```c
uint8_t bt_df_adv_cte_tx_param::cte_type
```

恒定音调扩展类型（CTE type）。

允许值由 `bt_df_cte_type` 定义，但不包含 `BT_DF_CTE_TYPE_NONE` 和 `BT_DF_CTE_TYPE_ALL`。

<a id="ac974c5bb804912f5940b2ede5f6394a1"></a>

### `num_ant_ids`

```c
uint8_t bt_df_adv_cte_tx_param::num_ant_ids
```

切换模式（Switch pattern）中的天线标识符数量（Antenna IDs）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/direction.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/direction.h](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_df_cte_type](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_bt_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_bt_df_conn_cte_req_params_结构体.md)
