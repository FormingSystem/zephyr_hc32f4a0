---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-93
title: bt_hci_cp_le_set_data_len_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__data__len.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_bt\_hci\_cp\_le\_set\_data\_len\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__data__len.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 93.1\_数据成员（Data Fields）

<a id="r_a874869090428a7f380c5466353573eba"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a874869090428a7f380c5466353573eba)。

<a id="r_ac579e84a004a09813bbe0ed61db11931"></a>

```c
uint16_t tx_octets
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_octets](#ac579e84a004a09813bbe0ed61db11931)。

<a id="r_a15285a4e8bf8e359bb326de4b30ba8f1"></a>

```c
uint16_t tx_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_time](#a15285a4e8bf8e359bb326de4b30ba8f1)。

## 93.2\_详细说明（Detailed Documentation）

<a id="a874869090428a7f380c5466353573eba"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_set_data_len::handle
```

<a id="ac579e84a004a09813bbe0ed61db11931"></a>

### `tx_octets`

```c
uint16_t bt_hci_cp_le_set_data_len::tx_octets
```

<a id="a15285a4e8bf8e359bb326de4b30ba8f1"></a>

### `tx_time`

```c
uint16_t bt_hci_cp_le_set_data_len::tx_time
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 93.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P094_bt_hci_cp_le_set_default_phy_结构体.md)
