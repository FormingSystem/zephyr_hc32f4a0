---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-235
title: bt_hci_evt_le_conn_param_req_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__conn__param__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第235章\_bt\_hci\_evt\_le\_conn\_param\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__conn__param__req.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 235.1\_数据成员（Data Fields）

<a id="r_a4746a001a070f152a3c1c870a7e74df1"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a4746a001a070f152a3c1c870a7e74df1)。

<a id="r_a9a9dfc026feb46337b0a36920204b24e"></a>

```c
uint16_t interval_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_min](#a9a9dfc026feb46337b0a36920204b24e)。

<a id="r_a0ed70d1a89f270073f78823d38af6ac9"></a>

```c
uint16_t interval_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_max](#a0ed70d1a89f270073f78823d38af6ac9)。

<a id="r_a9f61f0a3e6b6d2e2c6af2f4aef625b75"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#a9f61f0a3e6b6d2e2c6af2f4aef625b75)。

<a id="r_ae34de4a3d3e3e4686391eb9d9585dc87"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#ae34de4a3d3e3e4686391eb9d9585dc87)。

## 235.2\_详细说明（Detailed Documentation）

<a id="a4746a001a070f152a3c1c870a7e74df1"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_conn_param_req::handle
```

<a id="a0ed70d1a89f270073f78823d38af6ac9"></a>

### `interval_max`

```c
uint16_t bt_hci_evt_le_conn_param_req::interval_max
```

<a id="a9a9dfc026feb46337b0a36920204b24e"></a>

### `interval_min`

```c
uint16_t bt_hci_evt_le_conn_param_req::interval_min
```

<a id="a9f61f0a3e6b6d2e2c6af2f4aef625b75"></a>

### `latency`

```c
uint16_t bt_hci_evt_le_conn_param_req::latency
```

<a id="ae34de4a3d3e3e4686391eb9d9585dc87"></a>

### `timeout`

```c
uint16_t bt_hci_evt_le_conn_param_req::timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 235.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P234_bt_hci_evt_le_conn_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P236_bt_hci_evt_le_conn_rate_change_结构体.md)
