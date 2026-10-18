---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-41
title: bt_hci_cp_le_enh_tx_test_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__enh__tx__test.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_bt\_hci\_cp\_le\_enh\_tx\_test\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__enh__tx__test.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a0b7883b36d511c6da1bac543f1aae446"></a>

```c
uint8_t tx_ch
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_ch](#a0b7883b36d511c6da1bac543f1aae446)。

<a id="r_af1e27be0ad23887c0e71024739b00f8d"></a>

```c
uint8_t test_data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[test_data_len](#af1e27be0ad23887c0e71024739b00f8d)。

<a id="r_a9ccb91be1554172d6c724e438508bfe5"></a>

```c
uint8_t pkt_payload
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pkt_payload](#a9ccb91be1554172d6c724e438508bfe5)。

<a id="r_a718442db29c5ac455c3e2aac9844cdd0"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a718442db29c5ac455c3e2aac9844cdd0)。

## 41.2\_详细说明（Detailed Documentation）

<a id="a718442db29c5ac455c3e2aac9844cdd0"></a>

### `phy`

```c
uint8_t bt_hci_cp_le_enh_tx_test::phy
```

<a id="a9ccb91be1554172d6c724e438508bfe5"></a>

### `pkt_payload`

```c
uint8_t bt_hci_cp_le_enh_tx_test::pkt_payload
```

<a id="af1e27be0ad23887c0e71024739b00f8d"></a>

### `test_data_len`

```c
uint8_t bt_hci_cp_le_enh_tx_test::test_data_len
```

<a id="a0b7883b36d511c6da1bac543f1aae446"></a>

### `tx_ch`

```c
uint8_t bt_hci_cp_le_enh_tx_test::tx_ch
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_bt_hci_cp_le_enh_rx_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_bt_hci_cp_le_ext_create_conn_结构体.md)
