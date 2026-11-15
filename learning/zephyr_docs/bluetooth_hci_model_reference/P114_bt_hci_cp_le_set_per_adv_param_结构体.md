---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-114
title: bt_hci_cp_le_set_per_adv_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__per__adv__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_bt\_hci\_cp\_le\_set\_per\_adv\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__per__adv__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 114.1\_数据成员（Data Fields）

<a id="r_a2b61031952b3893add7677d3802e368b"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#a2b61031952b3893add7677d3802e368b)。

<a id="r_af01696ef6bf02e7db37d45a0c9852ef5"></a>

```c
uint16_t min_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_interval](#af01696ef6bf02e7db37d45a0c9852ef5)。

<a id="r_a1a2a69ea6e310710892184ced472eb8a"></a>

```c
uint16_t max_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_interval](#a1a2a69ea6e310710892184ced472eb8a)。

<a id="r_a879ea10e1ab217b4aa49dfcf3b394691"></a>

```c
uint16_t props
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[props](#a879ea10e1ab217b4aa49dfcf3b394691)。

## 114.2\_详细说明（Detailed Documentation）

<a id="a2b61031952b3893add7677d3802e368b"></a>

### `handle`

```c
uint8_t bt_hci_cp_le_set_per_adv_param::handle
```

<a id="a1a2a69ea6e310710892184ced472eb8a"></a>

### `max_interval`

```c
uint16_t bt_hci_cp_le_set_per_adv_param::max_interval
```

<a id="af01696ef6bf02e7db37d45a0c9852ef5"></a>

### `min_interval`

```c
uint16_t bt_hci_cp_le_set_per_adv_param::min_interval
```

<a id="a879ea10e1ab217b4aa49dfcf3b394691"></a>

### `props`

```c
uint16_t bt_hci_cp_le_set_per_adv_param::props
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 114.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P113_bt_hci_cp_le_set_per_adv_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md)
