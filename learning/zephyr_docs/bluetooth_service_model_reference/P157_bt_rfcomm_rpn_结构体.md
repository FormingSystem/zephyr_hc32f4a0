---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-157
title: bt_rfcomm_rpn_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__rpn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第157章\_bt\_rfcomm\_rpn\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__rpn.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RFCOMM远程端口协商（Remote Port Negotiation，RPN）结构。

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

<a id="details"></a>

RFCOMM远程端口协商（Remote Port Negotiation，RPN）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 157.1\_数据成员（Data Fields）

<a id="r_afacd73edbb63e3ade9573100967faffa"></a>

```c
uint8_t dlci
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dlci](#afacd73edbb63e3ade9573100967faffa)。

<a id="r_aad2f64edcb82e864293869474d20fa81"></a>

```c
uint8_t baud_rate
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[baud_rate](#aad2f64edcb82e864293869474d20fa81)。

<a id="r_acd61f81d3de1fe4da58fd5ee0d4e5e77"></a>

```c
uint8_t line_settings
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[line_settings](#acd61f81d3de1fe4da58fd5ee0d4e5e77)。

<a id="r_ae0db46df73fae846cb53f8a0cf01350a"></a>

```c
uint8_t flow_control
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flow_control](#ae0db46df73fae846cb53f8a0cf01350a)。

<a id="r_ae637cd243e9b016231b5071e171b6b54"></a>

```c
uint8_t xon_char
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[xon_char](#ae637cd243e9b016231b5071e171b6b54)。

<a id="r_adc651e1ac74d616fd03b07a647139296"></a>

```c
uint8_t xoff_char
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[xoff_char](#adc651e1ac74d616fd03b07a647139296)。

<a id="r_a9eaac13558a5be2fed82084e0bb7a20a"></a>

```c
uint16_t param_mask
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[param_mask](#a9eaac13558a5be2fed82084e0bb7a20a)。

## 157.2\_详细说明（Detailed Documentation）

<a id="aad2f64edcb82e864293869474d20fa81"></a>

### `baud_rate`

```c
uint8_t bt_rfcomm_rpn::baud_rate
```

<a id="afacd73edbb63e3ade9573100967faffa"></a>

### `dlci`

```c
uint8_t bt_rfcomm_rpn::dlci
```

<a id="ae0db46df73fae846cb53f8a0cf01350a"></a>

### `flow_control`

```c
uint8_t bt_rfcomm_rpn::flow_control
```

<a id="acd61f81d3de1fe4da58fd5ee0d4e5e77"></a>

### `line_settings`

```c
uint8_t bt_rfcomm_rpn::line_settings
```

<a id="a9eaac13558a5be2fed82084e0bb7a20a"></a>

### `param_mask`

```c
uint16_t bt_rfcomm_rpn::param_mask
```

<a id="adc651e1ac74d616fd03b07a647139296"></a>

### `xoff_char`

```c
uint8_t bt_rfcomm_rpn::xoff_char
```

<a id="ae637cd243e9b016231b5071e171b6b54"></a>

### `xon_char`

```c
uint8_t bt_rfcomm_rpn::xon_char
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/rfcomm.h`

## 157.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/rfcomm.h](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P156_bt_rfcomm_dlc_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P158_bt_rfcomm_server_结构体.md)
