---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-356
title: bt_hci_rp_le_read_chan_map_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__chan__map.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第356章\_bt\_hci\_rp\_le\_read\_chan\_map\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__chan__map.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 356.1\_数据成员（Data Fields）

<a id="r_a73a51f243bf4881f9024ba67cf2426ad"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a73a51f243bf4881f9024ba67cf2426ad)。

<a id="r_a8fcec46574f5601bf0837aae8f745b38"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a8fcec46574f5601bf0837aae8f745b38)。

<a id="r_a2899c53f17ba2293b95477ba25fd1b3d"></a>

```c
uint8_t ch_map [5]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch_map](#a2899c53f17ba2293b95477ba25fd1b3d)。

## 356.2\_详细说明（Detailed Documentation）

<a id="a2899c53f17ba2293b95477ba25fd1b3d"></a>

### `ch_map`

```c
uint8_t bt_hci_rp_le_read_chan_map::ch_map[5]
```

<a id="a8fcec46574f5601bf0837aae8f745b38"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_read_chan_map::handle
```

<a id="a73a51f243bf4881f9024ba67cf2426ad"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_chan_map::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 356.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P357_bt_hci_rp_le_read_chan_tx_power_结构体.md)
