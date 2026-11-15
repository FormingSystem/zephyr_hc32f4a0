---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-24
title: bt_conn_le_min_conn_interval_group_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__min__conn__interval__group.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_bt\_conn\_le\_min\_conn\_interval\_group\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__min__conn__interval__group.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

支持的最小连接间隔组（Minimum Supported Connection Interval Group）。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

最小支持连接间隔组（Minimum supported connection interval group）。每组表示一个受支持连接间隔的等差序列：`min`、`min + stride`、`min + 2 * stride`、……、`min + n * stride`，其中 `min + n * stride <= max`。例如：`min = 10`（1250 微秒）、`max = 60`（7500 微秒）、`stride = 5`（625 微秒），对应支持的间隔为 1250、1875、2500、……、6875、7500 微秒。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a44c7e6e9983d607fdde9cafe8cb595e1"></a>

```c
uint16_t min_125us
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_125us](#a44c7e6e9983d607fdde9cafe8cb595e1)。

组内间隔范围下限（Lower bound）。

<a id="r_a3d48e4889d3e039fc19da55c40efc911"></a>

```c
uint16_t max_125us
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_125us](#a3d48e4889d3e039fc19da55c40efc911)。

组内间隔范围上限（Upper bound）。

<a id="r_aed08c6c6bbe9f4bfae0a5e0c8ad6e9f3"></a>

```c
uint16_t stride_125us
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[stride_125us](#aed08c6c6bbe9f4bfae0a5e0c8ad6e9f3)。

连续两个受支持间隔之间的增量（Increment）。

## 24.2\_详细说明（Detailed Documentation）

<a id="a3d48e4889d3e039fc19da55c40efc911"></a>

### `max_125us`

```c
uint16_t bt_conn_le_min_conn_interval_group::max_125us
```

组内间隔范围上限（Upper bound）。

单位（Unit）：125 微秒（Microseconds）。

范围（Range）：`BT_HCI_LE_SCI_INTERVAL_MIN_125US`–`BT_HCI_LE_SCI_INTERVAL_MAX_125US`。

<a id="a44c7e6e9983d607fdde9cafe8cb595e1"></a>

### `min_125us`

```c
uint16_t bt_conn_le_min_conn_interval_group::min_125us
```

组内间隔范围下限（Lower bound）。

单位（Unit）：125 微秒（Microseconds）。

范围（Range）：`BT_HCI_LE_SCI_INTERVAL_MIN_125US`–`BT_HCI_LE_SCI_INTERVAL_MAX_125US`。

<a id="aed08c6c6bbe9f4bfae0a5e0c8ad6e9f3"></a>

### `stride_125us`

```c
uint16_t bt_conn_le_min_conn_interval_group::stride_125us
```

连续两个受支持间隔之间的增量（Increment）。

单位（Unit）：125 微秒（Microseconds）。

范围（Range）：`BT_HCI_LE_SCI_STRIDE_MIN_125US`–`BT_HCI_LE_SCI_INTERVAL_MAX_125US`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_HCI_LE_SCI_INTERVAL_MIN_125US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a292c11301eed063f4b9cfec645881a47)
- [BT_HCI_LE_SCI_INTERVAL_MAX_125US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a14c9d4eab8b8fe650ea2950d0c3a703f)
- [BT_HCI_LE_SCI_STRIDE_MIN_125US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aea8e6814082534c65773ceb291d60c49)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_bt_conn_le_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_bt_conn_le_min_conn_interval_info_结构体.md)
