---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-429
title: bt_hci_rp_vs_read_supported_features_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__supported__features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第429章\_bt\_hci\_rp\_vs\_read\_supported\_features\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__supported__features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 429.1\_数据成员（Data Fields）

<a id="r_a40468d71ba659d8ef593d82aca0bc583"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a40468d71ba659d8ef593d82aca0bc583)。

<a id="r_a0459b49e864d3069d4ba818ef2ed59ca"></a>

```c
uint8_t features [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[features](#a0459b49e864d3069d4ba818ef2ed59ca)。

## 429.2\_详细说明（Detailed Documentation）

<a id="a0459b49e864d3069d4ba818ef2ed59ca"></a>

### `features`

```c
uint8_t bt_hci_rp_vs_read_supported_features::features[8]
```

<a id="a40468d71ba659d8ef593d82aca0bc583"></a>

### `status`

```c
uint8_t bt_hci_rp_vs_read_supported_features::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 429.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P428_bt_hci_rp_vs_read_supported_commands_结构体.md) · [返回大纲](大纲.md) · [下一章](P430_bt_hci_rp_vs_read_tx_power_level_结构体.md)
