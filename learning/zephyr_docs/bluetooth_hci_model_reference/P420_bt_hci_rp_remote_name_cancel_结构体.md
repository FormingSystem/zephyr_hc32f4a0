---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-420
title: bt_hci_rp_remote_name_cancel_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__remote__name__cancel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第420章\_bt\_hci\_rp\_remote\_name\_cancel\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__remote__name__cancel.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 420.1\_数据成员（Data Fields）

<a id="r_ac7fadee392b126cb50cef7a6336926cb"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ac7fadee392b126cb50cef7a6336926cb)。

<a id="r_a455432799a1272f88b2b00a35a2e7ef5"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a455432799a1272f88b2b00a35a2e7ef5)。

## 420.2\_详细说明（Detailed Documentation）

<a id="a455432799a1272f88b2b00a35a2e7ef5"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_rp_remote_name_cancel::bdaddr
```

<a id="ac7fadee392b126cb50cef7a6336926cb"></a>

### `status`

```c
uint8_t bt_hci_rp_remote_name_cancel::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 420.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P419_bt_hci_rp_read_tx_power_level_结构体.md) · [返回大纲](大纲.md) · [下一章](P421_bt_hci_rp_sniff_subrating_结构体.md)
