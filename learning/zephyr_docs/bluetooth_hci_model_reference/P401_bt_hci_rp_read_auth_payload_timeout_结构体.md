---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-401
title: bt_hci_rp_read_auth_payload_timeout_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__auth__payload__timeout.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第401章\_bt\_hci\_rp\_read\_auth\_payload\_timeout\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__auth__payload__timeout.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 401.1\_数据成员（Data Fields）

<a id="r_a3eadeab880eb75c914be654dbc685f3f"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a3eadeab880eb75c914be654dbc685f3f)。

<a id="r_ab53b7e03c68dcd040e38fdc7429b2d3b"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ab53b7e03c68dcd040e38fdc7429b2d3b)。

<a id="r_ab4092720dad9a01f4e179eb2f0112aed"></a>

```c
uint16_t auth_payload_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[auth_payload_timeout](#ab4092720dad9a01f4e179eb2f0112aed)。

## 401.2\_详细说明（Detailed Documentation）

<a id="ab4092720dad9a01f4e179eb2f0112aed"></a>

### `auth_payload_timeout`

```c
uint16_t bt_hci_rp_read_auth_payload_timeout::auth_payload_timeout
```

<a id="ab53b7e03c68dcd040e38fdc7429b2d3b"></a>

### `handle`

```c
uint16_t bt_hci_rp_read_auth_payload_timeout::handle
```

<a id="a3eadeab880eb75c914be654dbc685f3f"></a>

### `status`

```c
uint8_t bt_hci_rp_read_auth_payload_timeout::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 401.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P400_bt_hci_rp_pin_code_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P402_bt_hci_rp_read_bd_addr_结构体.md)
