---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-352
title: bt_hci_rp_le_read_all_local_supported_features_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__all__local__supported__features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第352章\_bt\_hci\_rp\_le\_read\_all\_local\_supported\_features\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__all__local__supported__features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 352.1\_数据成员（Data Fields）

<a id="r_ac4aeb5159bb91c8faf9d12461b005e89"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ac4aeb5159bb91c8faf9d12461b005e89)。

<a id="r_a3e200ffc8a5ecafc5e7173f1a48fe6b1"></a>

```c
uint8_t max_page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_page](#a3e200ffc8a5ecafc5e7173f1a48fe6b1)。

<a id="r_a8cecb341ec3dfb335940af0a6e4751c6"></a>

```c
uint8_t features [248]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[features](#a8cecb341ec3dfb335940af0a6e4751c6)。

## 352.2\_详细说明（Detailed Documentation）

<a id="a8cecb341ec3dfb335940af0a6e4751c6"></a>

### `features`

```c
uint8_t bt_hci_rp_le_read_all_local_supported_features::features[248]
```

<a id="a3e200ffc8a5ecafc5e7173f1a48fe6b1"></a>

### `max_page`

```c
uint8_t bt_hci_rp_le_read_all_local_supported_features::max_page
```

<a id="ac4aeb5159bb91c8faf9d12461b005e89"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_all_local_supported_features::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 352.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P351_bt_hci_rp_le_rand_结构体.md) · [返回大纲](大纲.md) · [下一章](P353_bt_hci_rp_le_read_ant_info_结构体.md)
