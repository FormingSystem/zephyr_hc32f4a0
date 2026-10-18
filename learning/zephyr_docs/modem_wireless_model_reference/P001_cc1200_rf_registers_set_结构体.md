---
id: learning.zephyr-docs.modem-wireless-model-reference.page-1
title: cc1200_rf_registers_set_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcc1200__rf__registers__set.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_cc1200\_rf\_registers\_set\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcc1200__rf__registers__set.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/ieee802154/cc1200.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_ac545acd56ecb378b707601a8dd9ac767"></a>

```c
uint32_t chan_center_freq0
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[chan_center_freq0](#ac545acd56ecb378b707601a8dd9ac767)。

<a id="r_a14ef1dca5b9aabf2f235420ab79af6e1"></a>

```c
uint16_t channel_spacing
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[channel_spacing](#a14ef1dca5b9aabf2f235420ab79af6e1)。

<a id="r_ac11f879ac5f72cbc5ab5eea35e3b954d"></a>

```c
uint8_t registers [100]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[registers](#ac11f879ac5f72cbc5ab5eea35e3b954d)。

## 1.2\_详细说明（Detailed Documentation）

<a id="ac545acd56ecb378b707601a8dd9ac767"></a>

### `chan_center_freq0`

```c
uint32_t cc1200_rf_registers_set::chan_center_freq0
```

<a id="a14ef1dca5b9aabf2f235420ab79af6e1"></a>

### `channel_spacing`

```c
uint16_t cc1200_rf_registers_set::channel_spacing
```

<a id="ac11f879ac5f72cbc5ab5eea35e3b954d"></a>

### `registers`

```c
uint8_t cc1200_rf_registers_set::registers[100]
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/ieee802154/cc1200.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/drivers/ieee802154/cc1200.h](https://docs.zephyrproject.org/latest/doxygen/html/cc1200_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_cellular_driver_api_结构体.md)
