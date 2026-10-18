---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-93
title: bt_le_conn_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__conn__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_bt\_le\_conn\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__conn__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗蓝牙连接（LE Connection）的连接参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

低功耗蓝牙连接（LE Connection）的连接参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 93.1\_数据成员（Data Fields）

<a id="r_acd3b0a74402ca45402bab9ff54763e8d"></a>

```c
uint16_t interval_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_min](#acd3b0a74402ca45402bab9ff54763e8d)。

<a id="r_a6d5a2662a5f22ccc26c992829d21f22d"></a>

```c
uint16_t interval_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_max](#a6d5a2662a5f22ccc26c992829d21f22d)。

<a id="r_a3d21bd8363fa77dab83468ea319fef7d"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#a3d21bd8363fa77dab83468ea319fef7d)。

<a id="r_ac06c16eb02e7a9d8b414db07e829178a"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#ac06c16eb02e7a9d8b414db07e829178a)。

## 93.2\_详细说明（Detailed Documentation）

<a id="a6d5a2662a5f22ccc26c992829d21f22d"></a>

### `interval_max`

```c
uint16_t bt_le_conn_param::interval_max
```

<a id="acd3b0a74402ca45402bab9ff54763e8d"></a>

### `interval_min`

```c
uint16_t bt_le_conn_param::interval_min
```

<a id="a3d21bd8363fa77dab83468ea319fef7d"></a>

### `latency`

```c
uint16_t bt_le_conn_param::latency
```

<a id="ac06c16eb02e7a9d8b414db07e829178a"></a>

### `timeout`

```c
uint16_t bt_le_conn_param::timeout
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 93.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P092_bt_le_adv_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P094_bt_le_cs_create_config_params_结构体.md)
