---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-436
title: bt_hci_sco_hdr_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__sco__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第436章\_bt\_hci\_sco\_hdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__sco__hdr.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 436.1\_数据成员（Data Fields）

<a id="r_a4b4c915bec966c17567c14e2df9c1581"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a4b4c915bec966c17567c14e2df9c1581)。

<a id="r_a158f67c3743684c28728b62db5cf2590"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a158f67c3743684c28728b62db5cf2590)。

## 436.2\_详细说明（Detailed Documentation）

<a id="a4b4c915bec966c17567c14e2df9c1581"></a>

### `handle`

```c
uint16_t bt_hci_sco_hdr::handle
```

<a id="a158f67c3743684c28728b62db5cf2590"></a>

### `len`

```c
uint8_t bt_hci_sco_hdr::len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 436.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P435_bt_hci_rp_write_conn_accept_timeout_结构体.md) · [返回大纲](大纲.md) · [下一章](P437_bt_hci_setup_params_结构体.md)
