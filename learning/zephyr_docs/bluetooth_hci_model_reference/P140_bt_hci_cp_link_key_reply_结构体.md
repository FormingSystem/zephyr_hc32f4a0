---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-140
title: bt_hci_cp_link_key_reply_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__link__key__reply.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第140章\_bt\_hci\_cp\_link\_key\_reply\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__link__key__reply.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 140.1\_数据成员（Data Fields）

<a id="r_ab5221952fbcfe413d7c3bd3a441a9b17"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#ab5221952fbcfe413d7c3bd3a441a9b17)。

<a id="r_a2af0b4b55a5ffcff0221da841ba0cbba"></a>

```c
uint8_t link_key [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[link_key](#a2af0b4b55a5ffcff0221da841ba0cbba)。

## 140.2\_详细说明（Detailed Documentation）

<a id="ab5221952fbcfe413d7c3bd3a441a9b17"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_link_key_reply::bdaddr
```

<a id="a2af0b4b55a5ffcff0221da841ba0cbba"></a>

### `link_key`

```c
uint8_t bt_hci_cp_link_key_reply::link_key[16]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 140.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P139_bt_hci_cp_link_key_neg_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P141_bt_hci_cp_mesh_结构体.md)
