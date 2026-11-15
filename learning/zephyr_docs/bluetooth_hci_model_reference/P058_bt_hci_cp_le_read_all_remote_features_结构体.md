---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-58
title: bt_hci_cp_le_read_all_remote_features_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__read__all__remote__features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_bt\_hci\_cp\_le\_read\_all\_remote\_features\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__read__all__remote__features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a2baf8df3a24b1b883768278459a156c7"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a2baf8df3a24b1b883768278459a156c7)。

<a id="r_aa8cf7318871819cf425aa59ca15cc86d"></a>

```c
uint8_t pages_requested
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pages_requested](#aa8cf7318871819cf425aa59ca15cc86d)。

## 58.2\_详细说明（Detailed Documentation）

<a id="a2baf8df3a24b1b883768278459a156c7"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_read_all_remote_features::handle
```

<a id="aa8cf7318871819cf425aa59ca15cc86d"></a>

### `pages_requested`

```c
uint8_t bt_hci_cp_le_read_all_remote_features::pages_requested
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_bt_hci_cp_le_procedure_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_bt_hci_cp_le_read_chan_map_结构体.md)
