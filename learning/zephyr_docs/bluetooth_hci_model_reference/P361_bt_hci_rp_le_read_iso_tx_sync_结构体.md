---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-361
title: bt_hci_rp_le_read_iso_tx_sync_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__iso__tx__sync.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第361章\_bt\_hci\_rp\_le\_read\_iso\_tx\_sync\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__iso__tx__sync.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 361.1\_数据成员（Data Fields）

<a id="r_a188ef5dba77c754c46094135cc52641c"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a188ef5dba77c754c46094135cc52641c)。

<a id="r_a8c0003043d3896b1ff93dc33dccc76b4"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a8c0003043d3896b1ff93dc33dccc76b4)。

<a id="r_af2a02f68aa0a757757c490e707954952"></a>

```c
uint16_t seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[seq](#af2a02f68aa0a757757c490e707954952)。

<a id="r_a35520a3e50afc03ed969b6c5ca9e15d9"></a>

```c
uint32_t timestamp
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp](#a35520a3e50afc03ed969b6c5ca9e15d9)。

<a id="r_a29770c3172d5e45409392aa8ffc835ef"></a>

```c
uint8_t offset [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[offset](#a29770c3172d5e45409392aa8ffc835ef)。

## 361.2\_详细说明（Detailed Documentation）

<a id="a8c0003043d3896b1ff93dc33dccc76b4"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_read_iso_tx_sync::handle
```

<a id="a29770c3172d5e45409392aa8ffc835ef"></a>

### `offset`

```c
uint8_t bt_hci_rp_le_read_iso_tx_sync::offset[3]
```

<a id="af2a02f68aa0a757757c490e707954952"></a>

### `seq`

```c
uint16_t bt_hci_rp_le_read_iso_tx_sync::seq
```

<a id="a188ef5dba77c754c46094135cc52641c"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_iso_tx_sync::status
```

<a id="a35520a3e50afc03ed969b6c5ca9e15d9"></a>

### `timestamp`

```c
uint32_t bt_hci_rp_le_read_iso_tx_sync::timestamp
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 361.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P360_bt_hci_rp_le_read_iso_link_quality_结构体.md) · [返回大纲](大纲.md) · [下一章](P362_bt_hci_rp_le_read_local_features_结构体.md)
