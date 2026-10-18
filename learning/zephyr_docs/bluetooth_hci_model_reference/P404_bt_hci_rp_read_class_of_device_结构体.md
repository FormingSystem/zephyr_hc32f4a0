---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-404
title: bt_hci_rp_read_class_of_device_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__class__of__device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第404章\_bt\_hci\_rp\_read\_class\_of\_device\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__class__of__device.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 404.1\_数据成员（Data Fields）

<a id="r_a221d175e8016fd04151c4969d1134910"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a221d175e8016fd04151c4969d1134910)。

<a id="r_ac6483440d3095de548f477cd845c0cee"></a>

```c
uint8_t class_of_device [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[class_of_device](#ac6483440d3095de548f477cd845c0cee)。

## 404.2\_详细说明（Detailed Documentation）

<a id="ac6483440d3095de548f477cd845c0cee"></a>

### `class_of_device`

```c
uint8_t bt_hci_rp_read_class_of_device::class_of_device[3]
```

<a id="a221d175e8016fd04151c4969d1134910"></a>

### `status`

```c
uint8_t bt_hci_rp_read_class_of_device::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 404.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P403_bt_hci_rp_read_buffer_size_结构体.md) · [返回大纲](大纲.md) · [下一章](P405_bt_hci_rp_read_codec_capabilities_结构体.md)
