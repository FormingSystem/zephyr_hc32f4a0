---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-221
title: bt_hci_evt_io_capa_resp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__io__capa__resp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第221章\_bt\_hci\_evt\_io\_capa\_resp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__io__capa__resp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 221.1\_数据成员（Data Fields）

<a id="r_adac9c9f3999099fd460651e3b012fd0f"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#adac9c9f3999099fd460651e3b012fd0f)。

<a id="r_a851eae620ad90067957d4dec2f04efbe"></a>

```c
uint8_t capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[capability](#a851eae620ad90067957d4dec2f04efbe)。

<a id="r_ab12325d1536fe6a75d0a137bea301e8f"></a>

```c
uint8_t oob_data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[oob_data](#ab12325d1536fe6a75d0a137bea301e8f)。

<a id="r_a160cb3aea96bf698520e11673a40b2d7"></a>

```c
uint8_t authentication
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[authentication](#a160cb3aea96bf698520e11673a40b2d7)。

## 221.2\_详细说明（Detailed Documentation）

<a id="a160cb3aea96bf698520e11673a40b2d7"></a>

### `authentication`

```c
uint8_t bt_hci_evt_io_capa_resp::authentication
```

<a id="adac9c9f3999099fd460651e3b012fd0f"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_evt_io_capa_resp::bdaddr
```

<a id="a851eae620ad90067957d4dec2f04efbe"></a>

### `capability`

```c
uint8_t bt_hci_evt_io_capa_resp::capability
```

<a id="ab12325d1536fe6a75d0a137bea301e8f"></a>

### `oob_data`

```c
uint8_t bt_hci_evt_io_capa_resp::oob_data
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 221.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P220_bt_hci_evt_io_capa_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P222_bt_hci_evt_le_adv_set_terminated_结构体.md)
