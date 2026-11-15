---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-189
title: bt_hci_cp_write_ext_inquiry_response_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__ext__inquiry__response.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第189章\_bt\_hci\_cp\_write\_ext\_inquiry\_response\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__ext__inquiry__response.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

写入扩展查询响应（Write Extended Inquiry Response）的 HCI 命令参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

写入扩展查询响应（Write Extended Inquiry Response）的 HCI 命令参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 189.1\_数据成员（Data Fields）

<a id="r_a755167d683df6c408de57122847bfce0"></a>

```c
uint8_t fec_required
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fec_required](#a755167d683df6c408de57122847bfce0)。

是否需要前向纠错编码（Forward Error Correction，FEC）。

<a id="r_ae9c89c1f4cac0f16d41b926dc6abc898"></a>

```c
uint8_t eir [240]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[eir](#ae9c89c1f4cac0f16d41b926dc6abc898)。

扩展查询响应数据（Extended Inquiry Response Data）。

## 189.2\_详细说明（Detailed Documentation）

<a id="ae9c89c1f4cac0f16d41b926dc6abc898"></a>

### `eir`

```c
uint8_t bt_hci_cp_write_ext_inquiry_response::eir[240]
```

扩展查询响应数据（Extended Inquiry Response Data）。

<a id="a755167d683df6c408de57122847bfce0"></a>

### `fec_required`

```c
uint8_t bt_hci_cp_write_ext_inquiry_response::fec_required
```

是否需要前向纠错编码（Forward Error Correction，FEC）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 189.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P188_bt_hci_cp_write_default_link_policy_settings_结构体.md) · [返回大纲](大纲.md) · [下一章](P190_bt_hci_cp_write_inquiry_mode_结构体.md)
