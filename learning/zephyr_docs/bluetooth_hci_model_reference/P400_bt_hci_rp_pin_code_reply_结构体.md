---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-400
title: bt_hci_rp_pin_code_reply_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__pin__code__reply.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第400章\_bt\_hci\_rp\_pin\_code\_reply\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__pin__code__reply.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 400.1\_数据成员（Data Fields）

<a id="r_a3f167661b8d3f63ab12e6f64fb33986b"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a3f167661b8d3f63ab12e6f64fb33986b)。

<a id="r_afc7c991fd8050e8aae56b8587b5ee01d"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#afc7c991fd8050e8aae56b8587b5ee01d)。

## 400.2\_详细说明（Detailed Documentation）

<a id="afc7c991fd8050e8aae56b8587b5ee01d"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_rp_pin_code_reply::bdaddr
```

<a id="a3f167661b8d3f63ab12e6f64fb33986b"></a>

### `status`

```c
uint8_t bt_hci_rp_pin_code_reply::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 400.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P399_bt_hci_rp_pin_code_neg_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P401_bt_hci_rp_read_auth_payload_timeout_结构体.md)
