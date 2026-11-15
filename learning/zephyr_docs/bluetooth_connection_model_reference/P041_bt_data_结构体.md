---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-41
title: bt_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_bt\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙数据（Bluetooth Data）。

```c
#include <zephyr/bluetooth/data.h>
```

<a id="details"></a>

蓝牙数据（Bluetooth data）。描述可编码到广播数据（Advertising data）中的不同广播数据类型（AD Types）。用于构建传给 `bt_le_adv_start` 函数的数组。可使用 `BT_DATA` 定义辅助声明 `bt_data` 数组的元素。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a984aecb40a4993ffa113be53942db065"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a984aecb40a4993ffa113be53942db065)。

扫描响应数据或广播数据的类型（Scan response／Advertisement data type）。

<a id="r_abda19091a1b8f99d385f11772ef34d5f"></a>

```c
uint8_t data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_len](#abda19091a1b8f99d385f11772ef34d5f)。

扫描响应数据或广播数据的长度（Scan response／Advertisement data length）。

<a id="r_ac80ec10101ad69a86f703a4e652c7826"></a>

```c
const uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ac80ec10101ad69a86f703a4e652c7826)。

指向扫描响应或广播数据（Scan response／Advertisement data）的指针。

## 41.2\_详细说明（Detailed Documentation）

<a id="ac80ec10101ad69a86f703a4e652c7826"></a>

### `data`

```c
const uint8_t* bt_data::data
```

指向扫描响应或广播数据（Scan response／Advertisement data）的指针。

<a id="abda19091a1b8f99d385f11772ef34d5f"></a>

### `data_len`

```c
uint8_t bt_data::data_len
```

扫描响应数据或广播数据的长度（Scan response／Advertisement data length）。

<a id="a984aecb40a4993ffa113be53942db065"></a>

### `type`

```c
uint8_t bt_data::type
```

扫描响应数据或广播数据的类型（Scan response／Advertisement data type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/data.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad2e3caef88d52d720e8e4d21df767b02)
- [BT_DATA](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html#a8481217e632522e1f322de87d745f8f0)
- [bt_data](P041_bt_data_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_bt_conn_sco_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_bt_df_adv_cte_tx_param_结构体.md)
