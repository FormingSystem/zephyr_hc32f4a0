---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-432
title: bt_hci_rp_vs_read_version_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__version__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第432章\_bt\_hci\_rp\_vs\_read\_version\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__version__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 432.1\_数据成员（Data Fields）

<a id="r_a7cdff04c26d2f5864a07fc0a7c31a89a"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a7cdff04c26d2f5864a07fc0a7c31a89a)。

<a id="r_a7e69f89d5562205f780dc05128b5d46a"></a>

```c
uint16_t hw_platform
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[hw_platform](#a7e69f89d5562205f780dc05128b5d46a)。

<a id="r_abd4ea8df7b338e48490ceafae1b8e6be"></a>

```c
uint16_t hw_variant
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[hw_variant](#abd4ea8df7b338e48490ceafae1b8e6be)。

<a id="r_a24ad5440e85d2e91c0495a3b06ac7469"></a>

```c
uint8_t fw_variant
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fw_variant](#a24ad5440e85d2e91c0495a3b06ac7469)。

<a id="r_a147b0b73db111465549196ed67ca60d6"></a>

```c
uint8_t fw_version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fw_version](#a147b0b73db111465549196ed67ca60d6)。

<a id="r_a47b4d799df9aeca67f6136264e13ef16"></a>

```c
uint16_t fw_revision
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fw_revision](#a47b4d799df9aeca67f6136264e13ef16)。

<a id="r_a43fc428c7ea444be2100e970b444f51a"></a>

```c
uint32_t fw_build
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[fw_build](#a43fc428c7ea444be2100e970b444f51a)。

## 432.2\_详细说明（Detailed Documentation）

<a id="a43fc428c7ea444be2100e970b444f51a"></a>

### `fw_build`

```c
uint32_t bt_hci_rp_vs_read_version_info::fw_build
```

<a id="a47b4d799df9aeca67f6136264e13ef16"></a>

### `fw_revision`

```c
uint16_t bt_hci_rp_vs_read_version_info::fw_revision
```

<a id="a24ad5440e85d2e91c0495a3b06ac7469"></a>

### `fw_variant`

```c
uint8_t bt_hci_rp_vs_read_version_info::fw_variant
```

<a id="a147b0b73db111465549196ed67ca60d6"></a>

### `fw_version`

```c
uint8_t bt_hci_rp_vs_read_version_info::fw_version
```

<a id="a7e69f89d5562205f780dc05128b5d46a"></a>

### `hw_platform`

```c
uint16_t bt_hci_rp_vs_read_version_info::hw_platform
```

<a id="abd4ea8df7b338e48490ceafae1b8e6be"></a>

### `hw_variant`

```c
uint16_t bt_hci_rp_vs_read_version_info::hw_variant
```

<a id="a7cdff04c26d2f5864a07fc0a7c31a89a"></a>

### `status`

```c
uint8_t bt_hci_rp_vs_read_version_info::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 432.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md) · [返回大纲](大纲.md) · [下一章](P433_bt_hci_rp_vs_write_tx_power_level_结构体.md)
