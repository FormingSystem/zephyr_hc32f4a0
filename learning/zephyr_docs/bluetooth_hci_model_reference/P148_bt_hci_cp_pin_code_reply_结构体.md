---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-148
title: bt_hci_cp_pin_code_reply_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__pin__code__reply.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第148章\_bt\_hci\_cp\_pin\_code\_reply\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__pin__code__reply.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 148.1\_数据成员（Data Fields）

<a id="r_a627800dcb580110be785576dfcc49bb1"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a627800dcb580110be785576dfcc49bb1)。

<a id="r_aa0cbf668608c3eb4998356ad7b18c01a"></a>

```c
uint8_t pin_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pin_len](#aa0cbf668608c3eb4998356ad7b18c01a)。

<a id="r_afc4ed5ae429087f4692af716d6b56997"></a>

```c
uint8_t pin_code [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pin_code](#afc4ed5ae429087f4692af716d6b56997)。

## 148.2\_详细说明（Detailed Documentation）

<a id="a627800dcb580110be785576dfcc49bb1"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_pin_code_reply::bdaddr
```

<a id="afc4ed5ae429087f4692af716d6b56997"></a>

### `pin_code`

```c
uint8_t bt_hci_cp_pin_code_reply::pin_code[16]
```

<a id="aa0cbf668608c3eb4998356ad7b18c01a"></a>

### `pin_len`

```c
uint8_t bt_hci_cp_pin_code_reply::pin_len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 148.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P147_bt_hci_cp_pin_code_neg_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P149_bt_hci_cp_read_auth_payload_timeout_结构体.md)
