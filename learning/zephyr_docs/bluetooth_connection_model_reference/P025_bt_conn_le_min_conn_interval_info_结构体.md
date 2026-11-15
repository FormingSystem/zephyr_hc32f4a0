---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-25
title: bt_conn_le_min_conn_interval_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__min__conn__interval__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_bt\_conn\_le\_min\_conn\_interval\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__min__conn__interval__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

支持的最小连接间隔信息。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

支持的最小连接间隔信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_aa39299ca32657e9f684e88875e7517dc"></a>

```c
uint16_t min_supported_conn_interval_us
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_supported_conn_interval_us](#aa39299ca32657e9f684e88875e7517dc)。

最小支持连接间隔（Minimum supported connection interval）。

<a id="r_ac0d63f57518324d81509fea51fcefa60"></a>

```c
uint8_t num_groups
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_groups](#ac0d63f57518324d81509fea51fcefa60)。

间隔组数量（Number of interval groups）。

<a id="r_ad9e6ae7c5632e4cc2a5e5eda52d2e0e8"></a>

```c
struct bt_conn_le_min_conn_interval_group groups [41]
```

相关声明：[bt_conn_le_min_conn_interval_group](P024_bt_conn_le_min_conn_interval_group_结构体.md)、[groups](#ad9e6ae7c5632e4cc2a5e5eda52d2e0e8)。

支持的连接间隔组数组（Supported connection interval groups）。

## 25.2\_详细说明（Detailed Documentation）

<a id="ad9e6ae7c5632e4cc2a5e5eda52d2e0e8"></a>

### `groups`

```c
struct bt_conn_le_min_conn_interval_group bt_conn_le_min_conn_interval_info::groups[41]
```

支持的连接间隔组数组（Supported connection interval groups）。

多个组可用于表示不连续的范围，或步长不同的范围（Differently-strided ranges）。

<a id="aa39299ca32657e9f684e88875e7517dc"></a>

### `min_supported_conn_interval_us`

```c
uint16_t bt_conn_le_min_conn_interval_info::min_supported_conn_interval_us
```

最小支持连接间隔（Minimum supported connection interval）。

单位（Unit）：微秒（Microseconds）。

范围（Range）：`BT_HCI_LE_MIN_SUPP_CONN_INT_MIN_US`–`BT_HCI_LE_MIN_SUPP_CONN_INT_MAX_US`。

<a id="ac0d63f57518324d81509fea51fcefa60"></a>

### `num_groups`

```c
uint8_t bt_conn_le_min_conn_interval_info::num_groups
```

间隔组数量（Number of interval groups）。

范围（Range）：`0`–`BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS`。

值为零时，控制器仅支持取整的连接间隔值（Rounded ConnInterval Values，RCV）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn_le_min_conn_interval_group](P024_bt_conn_le_min_conn_interval_group_结构体.md)
- [BT_HCI_LE_MIN_SUPP_CONN_INT_MIN_US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ac5dd60afc8c8bff309090fca1b6875aa)
- [BT_HCI_LE_MIN_SUPP_CONN_INT_MAX_US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ac6ae380e312559c82742975cf5ed742f)
- [BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gadcb74ad947485dd81dfd59a82d3b0db6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_bt_conn_le_min_conn_interval_group_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_bt_conn_le_path_loss_reporting_param_结构体.md)
