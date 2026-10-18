---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-160
title: bt_hci_cp_read_tx_power_level_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__read__tx__power__level.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第160章\_bt\_hci\_cp\_read\_tx\_power\_level\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__read__tx__power__level.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 160.1\_数据成员（Data Fields）

<a id="r_a1c268364fc80b9478d70b7eb997d9825"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a1c268364fc80b9478d70b7eb997d9825)。

<a id="r_a1920e671ec2deda1daf47f06a86d2881"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a1920e671ec2deda1daf47f06a86d2881)。

## 160.2\_详细说明（Detailed Documentation）

<a id="a1c268364fc80b9478d70b7eb997d9825"></a>

### `handle`

```c
uint16_t bt_hci_cp_read_tx_power_level::handle
```

<a id="a1920e671ec2deda1daf47f06a86d2881"></a>

### `type`

```c
uint8_t bt_hci_cp_read_tx_power_level::type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 160.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P159_bt_hci_cp_read_rssi_结构体.md) · [返回大纲](大纲.md) · [下一章](P161_bt_hci_cp_reject_conn_req_结构体.md)
