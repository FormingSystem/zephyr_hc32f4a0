---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-225
title: bt_hci_evt_le_big_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__big__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第225章\_bt\_hci\_evt\_le\_big\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__big__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 225.1\_数据成员（Data Fields）

<a id="r_ad6787806a3622b3bd3da4512bb8ddffe"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ad6787806a3622b3bd3da4512bb8ddffe)。

<a id="r_a14eaa705f1df38337722a41e8189f807"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#a14eaa705f1df38337722a41e8189f807)。

<a id="r_a2847d5fc997f80a3e21b7e03d80c9574"></a>

```c
uint8_t sync_delay [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sync_delay](#a2847d5fc997f80a3e21b7e03d80c9574)。

<a id="r_a2727d329c37e3b3644cfad02d86abb55"></a>

```c
uint8_t latency [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[latency](#a2727d329c37e3b3644cfad02d86abb55)。

<a id="r_abfa6d6bc135350737451e053aa7d212c"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#abfa6d6bc135350737451e053aa7d212c)。

<a id="r_ae77364aafe179588f7b8414292e35f5e"></a>

```c
uint8_t nse
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nse](#ae77364aafe179588f7b8414292e35f5e)。

<a id="r_a2327e42013033767af233d1c2c3acc56"></a>

```c
uint8_t bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bn](#a2327e42013033767af233d1c2c3acc56)。

<a id="r_a6c295870732d65002ec21b4b607e7c0b"></a>

```c
uint8_t pto
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pto](#a6c295870732d65002ec21b4b607e7c0b)。

<a id="r_a07163dee904412d6d8faca8563a944d9"></a>

```c
uint8_t irc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irc](#a07163dee904412d6d8faca8563a944d9)。

<a id="r_a8b433ac376e347bf391d4dd804c469f3"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#a8b433ac376e347bf391d4dd804c469f3)。

<a id="r_a0b0d19d442ed8f1025165c435786ba09"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#a0b0d19d442ed8f1025165c435786ba09)。

<a id="r_a995c8fe06ec087f16b771c38171745b1"></a>

```c
uint8_t num_bis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_bis](#a995c8fe06ec087f16b771c38171745b1)。

<a id="r_af1c8bd66c3dba70df22f8655b4f27925"></a>

```c
uint16_t handle [0]
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#af1c8bd66c3dba70df22f8655b4f27925)。

## 225.2\_详细说明（Detailed Documentation）

<a id="a14eaa705f1df38337722a41e8189f807"></a>

### `big_handle`

```c
uint8_t bt_hci_evt_le_big_complete::big_handle
```

<a id="a2327e42013033767af233d1c2c3acc56"></a>

### `bn`

```c
uint8_t bt_hci_evt_le_big_complete::bn
```

<a id="af1c8bd66c3dba70df22f8655b4f27925"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_big_complete::handle[0]
```

<a id="a07163dee904412d6d8faca8563a944d9"></a>

### `irc`

```c
uint8_t bt_hci_evt_le_big_complete::irc
```

<a id="a0b0d19d442ed8f1025165c435786ba09"></a>

### `iso_interval`

```c
uint16_t bt_hci_evt_le_big_complete::iso_interval
```

<a id="a2727d329c37e3b3644cfad02d86abb55"></a>

### `latency`

```c
uint8_t bt_hci_evt_le_big_complete::latency[3]
```

<a id="a8b433ac376e347bf391d4dd804c469f3"></a>

### `max_pdu`

```c
uint16_t bt_hci_evt_le_big_complete::max_pdu
```

<a id="ae77364aafe179588f7b8414292e35f5e"></a>

### `nse`

```c
uint8_t bt_hci_evt_le_big_complete::nse
```

<a id="a995c8fe06ec087f16b771c38171745b1"></a>

### `num_bis`

```c
uint8_t bt_hci_evt_le_big_complete::num_bis
```

<a id="abfa6d6bc135350737451e053aa7d212c"></a>

### `phy`

```c
uint8_t bt_hci_evt_le_big_complete::phy
```

<a id="a6c295870732d65002ec21b4b607e7c0b"></a>

### `pto`

```c
uint8_t bt_hci_evt_le_big_complete::pto
```

<a id="ad6787806a3622b3bd3da4512bb8ddffe"></a>

### `status`

```c
uint8_t bt_hci_evt_le_big_complete::status
```

<a id="a2847d5fc997f80a3e21b7e03d80c9574"></a>

### `sync_delay`

```c
uint8_t bt_hci_evt_le_big_complete::sync_delay[3]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 225.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P224_bt_hci_evt_le_advertising_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P226_bt_hci_evt_le_big_sync_established_结构体.md)
