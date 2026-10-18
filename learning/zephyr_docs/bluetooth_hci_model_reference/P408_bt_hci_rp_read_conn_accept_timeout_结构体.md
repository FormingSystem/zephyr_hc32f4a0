---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-408
title: bt_hci_rp_read_conn_accept_timeout_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__conn__accept__timeout.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第408章\_bt\_hci\_rp\_read\_conn\_accept\_timeout\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__conn__accept__timeout.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 408.1\_数据成员（Data Fields）

<a id="r_afeb5888722ee368e02c6b27b75ab2a70"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#afeb5888722ee368e02c6b27b75ab2a70)。

<a id="r_a01ca30c92311ec1df19a4cf835ea74cf"></a>

```c
uint16_t conn_accept_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_accept_timeout](#a01ca30c92311ec1df19a4cf835ea74cf)。

## 408.2\_详细说明（Detailed Documentation）

<a id="a01ca30c92311ec1df19a4cf835ea74cf"></a>

### `conn_accept_timeout`

```c
uint16_t bt_hci_rp_read_conn_accept_timeout::conn_accept_timeout
```

<a id="afeb5888722ee368e02c6b27b75ab2a70"></a>

### `status`

```c
uint8_t bt_hci_rp_read_conn_accept_timeout::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 408.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P407_bt_hci_rp_read_codecs_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P409_bt_hci_rp_read_ctlr_delay_结构体.md)
