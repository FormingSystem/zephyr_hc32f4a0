---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-24
title: bt_hci_cp_le_add_dev_to_rl_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__add__dev__to__rl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_bt\_hci\_cp\_le\_add\_dev\_to\_rl\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__add__dev__to__rl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a3daf2041f04381a56c2cbcd4bb33f4c0"></a>

```c
bt_addr_le_t peer_id_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_id_addr](#a3daf2041f04381a56c2cbcd4bb33f4c0)。

<a id="r_aedc27c868a7a4cbd3c175f67db4e3242"></a>

```c
uint8_t peer_irk [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[peer_irk](#aedc27c868a7a4cbd3c175f67db4e3242)。

<a id="r_ab5caa38e6eeab09b4a69084b1890317b"></a>

```c
uint8_t local_irk [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[local_irk](#ab5caa38e6eeab09b4a69084b1890317b)。

## 24.2\_详细说明（Detailed Documentation）

<a id="ab5caa38e6eeab09b4a69084b1890317b"></a>

### `local_irk`

```c
uint8_t bt_hci_cp_le_add_dev_to_rl::local_irk[16]
```

<a id="a3daf2041f04381a56c2cbcd4bb33f4c0"></a>

### `peer_id_addr`

```c
bt_addr_le_t bt_hci_cp_le_add_dev_to_rl::peer_id_addr
```

<a id="aedc27c868a7a4cbd3c175f67db4e3242"></a>

### `peer_irk`

```c
uint8_t bt_hci_cp_le_add_dev_to_rl::peer_irk[16]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_bt_hci_cp_le_add_dev_to_per_adv_list_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_bt_hci_cp_le_big_create_sync_结构体.md)
