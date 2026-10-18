---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-219
title: bt_hci_evt_inquiry_result_with_rssi_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__inquiry__result__with__rssi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第219章\_bt\_hci\_evt\_inquiry\_result\_with\_rssi\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__inquiry__result__with__rssi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 219.1\_数据成员（Data Fields）

<a id="r_af955dd1660f83e41e6d1b2b5aecf8133"></a>

```c
bt_addr_t addr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[addr](#af955dd1660f83e41e6d1b2b5aecf8133)。

<a id="r_a0a5c188d0d40b4259cbeb613c0dd12cf"></a>

```c
uint8_t pscan_rep_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pscan_rep_mode](#a0a5c188d0d40b4259cbeb613c0dd12cf)。

<a id="r_a09914ee9998c0b59cb35ed74d08aa4f2"></a>

```c
uint8_t reserved
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#a09914ee9998c0b59cb35ed74d08aa4f2)。

<a id="r_ad9b4920e2864ed8350de038dffe64574"></a>

```c
uint8_t cod [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cod](#ad9b4920e2864ed8350de038dffe64574)。

<a id="r_a1ee08f85103581994a88345cc94d7494"></a>

```c
uint16_t clock_offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[clock_offset](#a1ee08f85103581994a88345cc94d7494)。

<a id="r_a6d19e6400d7015db7122516e570d7989"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a6d19e6400d7015db7122516e570d7989)。

## 219.2\_详细说明（Detailed Documentation）

<a id="af955dd1660f83e41e6d1b2b5aecf8133"></a>

### `addr`

```c
bt_addr_t bt_hci_evt_inquiry_result_with_rssi::addr
```

<a id="a1ee08f85103581994a88345cc94d7494"></a>

### `clock_offset`

```c
uint16_t bt_hci_evt_inquiry_result_with_rssi::clock_offset
```

<a id="ad9b4920e2864ed8350de038dffe64574"></a>

### `cod`

```c
uint8_t bt_hci_evt_inquiry_result_with_rssi::cod[3]
```

<a id="a0a5c188d0d40b4259cbeb613c0dd12cf"></a>

### `pscan_rep_mode`

```c
uint8_t bt_hci_evt_inquiry_result_with_rssi::pscan_rep_mode
```

<a id="a09914ee9998c0b59cb35ed74d08aa4f2"></a>

### `reserved`

```c
uint8_t bt_hci_evt_inquiry_result_with_rssi::reserved
```

<a id="a6d19e6400d7015db7122516e570d7989"></a>

### `rssi`

```c
int8_t bt_hci_evt_inquiry_result_with_rssi::rssi
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 219.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P218_bt_hci_evt_inquiry_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P220_bt_hci_evt_io_capa_req_结构体.md)
