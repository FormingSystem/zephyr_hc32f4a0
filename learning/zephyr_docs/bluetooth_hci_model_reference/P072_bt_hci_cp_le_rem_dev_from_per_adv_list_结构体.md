---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-72
title: bt_hci_cp_le_rem_dev_from_per_adv_list_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__rem__dev__from__per__adv__list.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_bt\_hci\_cp\_le\_rem\_dev\_from\_per\_adv\_list\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__rem__dev__from__per__adv__list.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_adc420288f6a79c1a92f57241d3da3d81"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#adc420288f6a79c1a92f57241d3da3d81)。

<a id="r_a6629f3ececf586792a14f3c028cc8e8c"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a6629f3ececf586792a14f3c028cc8e8c)。

## 72.2\_详细说明（Detailed Documentation）

<a id="adc420288f6a79c1a92f57241d3da3d81"></a>

### `addr`

```c
bt_addr_le_t bt_hci_cp_le_rem_dev_from_per_adv_list::addr
```

<a id="a6629f3ececf586792a14f3c028cc8e8c"></a>

### `sid`

```c
uint8_t bt_hci_cp_le_rem_dev_from_per_adv_list::sid
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_bt_hci_cp_le_rem_dev_from_fal_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_bt_hci_cp_le_rem_dev_from_rl_结构体.md)
