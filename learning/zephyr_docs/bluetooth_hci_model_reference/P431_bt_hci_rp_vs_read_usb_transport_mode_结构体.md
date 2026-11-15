---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-431
title: bt_hci_rp_vs_read_usb_transport_mode_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__usb__transport__mode.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第431章\_bt\_hci\_rp\_vs\_read\_usb\_transport\_mode\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__usb__transport__mode.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 431.1\_数据成员（Data Fields）

<a id="r_a7fdfe43b633c153fd9e7cf1f470b435f"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a7fdfe43b633c153fd9e7cf1f470b435f)。

<a id="r_a25070132401d9b3d3dcd3f325f66da64"></a>

```c
uint8_t num_supported_modes
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_supported_modes](#a25070132401d9b3d3dcd3f325f66da64)。

<a id="r_aec8f1c7acd972d00b8f1070ed444b155"></a>

```c
uint8_t supported_mode [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[supported_mode](#aec8f1c7acd972d00b8f1070ed444b155)。

## 431.2\_详细说明（Detailed Documentation）

<a id="a25070132401d9b3d3dcd3f325f66da64"></a>

### `num_supported_modes`

```c
uint8_t bt_hci_rp_vs_read_usb_transport_mode::num_supported_modes
```

<a id="a7fdfe43b633c153fd9e7cf1f470b435f"></a>

### `status`

```c
uint8_t bt_hci_rp_vs_read_usb_transport_mode::status
```

<a id="aec8f1c7acd972d00b8f1070ed444b155"></a>

### `supported_mode`

```c
uint8_t bt_hci_rp_vs_read_usb_transport_mode::supported_mode[0]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 431.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P430_bt_hci_rp_vs_read_tx_power_level_结构体.md) · [返回大纲](大纲.md) · [下一章](P432_bt_hci_rp_vs_read_version_info_结构体.md)
