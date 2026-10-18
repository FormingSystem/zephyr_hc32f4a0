---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-45
title: bt_df_conn_cte_tx_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__conn__cte__tx__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_bt\_df\_conn\_cte\_tx\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__conn__cte__tx__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接模式下传输 CTE 的恒定音调扩展参数。

```c
#include <zephyr/bluetooth/direction.h>
```

<a id="details"></a>

连接模式下传输 CTE 的恒定音调扩展参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_af78df8115d2fac5b8f6132b48a56bc1c"></a>

```c
uint8_t cte_types
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_types](#af78df8115d2fac5b8f6132b48a56bc1c)。

允许的恒定音调扩展类型位域（CTE types bitfield），参见 `bt_df_cte_type`。

<a id="r_ad49bc64170e8ee4741aa01393284e7de"></a>

```c
uint8_t num_ant_ids
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_ant_ids](#ad49bc64170e8ee4741aa01393284e7de)。

天线切换模式数量（Number of antenna switch pattern）。

<a id="r_a9df1dac6180e77a4c7abc80890346c4a"></a>

```c
const uint8_t * ant_ids
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ant_ids](#a9df1dac6180e77a4c7abc80890346c4a)。

天线切换模式（Antenna switch pattern）。

## 45.2\_详细说明（Detailed Documentation）

<a id="a9df1dac6180e77a4c7abc80890346c4a"></a>

### `ant_ids`

```c
const uint8_t* bt_df_conn_cte_tx_param::ant_ids
```

天线切换模式（Antenna switch pattern）。

<a id="af78df8115d2fac5b8f6132b48a56bc1c"></a>

### `cte_types`

```c
uint8_t bt_df_conn_cte_tx_param::cte_types
```

允许的恒定音调扩展类型位域（CTE types bitfield），参见 `bt_df_cte_type`。

可使用所有枚举成员，但 `BT_DF_CTE_TYPE_NONE` 除外。

<a id="ad49bc64170e8ee4741aa01393284e7de"></a>

### `num_ant_ids`

```c
uint8_t bt_df_conn_cte_tx_param::num_ant_ids
```

天线切换模式数量（Number of antenna switch pattern）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/direction.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/direction.h](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_df_cte_type](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_bt_df_conn_cte_rx_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_bt_df_conn_iq_samples_report_结构体.md)
