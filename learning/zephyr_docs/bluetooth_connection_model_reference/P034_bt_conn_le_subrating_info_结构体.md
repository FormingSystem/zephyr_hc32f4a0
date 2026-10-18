---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-34
title: bt_conn_le_subrating_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__subrating__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_bt\_conn\_le\_subrating\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__subrating__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 连接的子速率信息。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 连接的子速率信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a23736535309f38695a2e432c5c80bbe1"></a>

```c
uint16_t factor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[factor](#a23736535309f38695a2e432c5c80bbe1)。

连接子速率因子（Connection subrate factor）。

<a id="r_a0a6d1eae73f76382f1a9415c01761c19"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#a0a6d1eae73f76382f1a9415c01761c19)。

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件数量（Underlying connection events）。

## 34.2\_详细说明（Detailed Documentation）

<a id="a0a6d1eae73f76382f1a9415c01761c19"></a>

### `continuation_number`

```c
uint16_t bt_conn_le_subrating_info::continuation_number
```

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件数量（Underlying connection events）。

<a id="a23736535309f38695a2e432c5c80bbe1"></a>

### `factor`

```c
uint16_t bt_conn_le_subrating_info::factor
```

连接子速率因子（Connection subrate factor）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_bt_conn_le_subrate_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_bt_conn_le_tx_power_结构体.md)
