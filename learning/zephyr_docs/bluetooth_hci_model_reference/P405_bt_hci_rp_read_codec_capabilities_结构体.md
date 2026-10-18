---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-405
title: bt_hci_rp_read_codec_capabilities_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__codec__capabilities.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第405章\_bt\_hci\_rp\_read\_codec\_capabilities\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__codec__capabilities.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 405.1\_数据成员（Data Fields）

<a id="r_ac224ea998e3af12f97232288266da8d2"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ac224ea998e3af12f97232288266da8d2)。

<a id="r_a71b7df63502bf42a26868e69893ddcfe"></a>

```c
uint8_t num_capabilities
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_capabilities](#a71b7df63502bf42a26868e69893ddcfe)。

<a id="r_ae0c84013512c461f3b6231162d6f3020"></a>

```c
uint8_t capabilities [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[capabilities](#ae0c84013512c461f3b6231162d6f3020)。

## 405.2\_详细说明（Detailed Documentation）

<a id="ae0c84013512c461f3b6231162d6f3020"></a>

### `capabilities`

```c
uint8_t bt_hci_rp_read_codec_capabilities::capabilities[0]
```

<a id="a71b7df63502bf42a26868e69893ddcfe"></a>

### `num_capabilities`

```c
uint8_t bt_hci_rp_read_codec_capabilities::num_capabilities
```

<a id="ac224ea998e3af12f97232288266da8d2"></a>

### `status`

```c
uint8_t bt_hci_rp_read_codec_capabilities::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 405.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P404_bt_hci_rp_read_class_of_device_结构体.md) · [返回大纲](大纲.md) · [下一章](P406_bt_hci_rp_read_codecs_结构体.md)
