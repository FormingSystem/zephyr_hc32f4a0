---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-184
title: bt_hci_cp_write_auth_payload_timeout_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__auth__payload__timeout.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第184章\_bt\_hci\_cp\_write\_auth\_payload\_timeout\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__auth__payload__timeout.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 184.1\_数据成员（Data Fields）

<a id="r_ad99d5b9f416f11492ac0f412b400aeb6"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ad99d5b9f416f11492ac0f412b400aeb6)。

<a id="r_a385c88012b09ec561b9ba7edaadeb574"></a>

```c
uint16_t auth_payload_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[auth_payload_timeout](#a385c88012b09ec561b9ba7edaadeb574)。

## 184.2\_详细说明（Detailed Documentation）

<a id="a385c88012b09ec561b9ba7edaadeb574"></a>

### `auth_payload_timeout`

```c
uint16_t bt_hci_cp_write_auth_payload_timeout::auth_payload_timeout
```

<a id="ad99d5b9f416f11492ac0f412b400aeb6"></a>

### `handle`

```c
uint16_t bt_hci_cp_write_auth_payload_timeout::handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 184.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P183_bt_hci_cp_vs_write_tx_power_level_结构体.md) · [返回大纲](大纲.md) · [下一章](P185_bt_hci_cp_write_class_of_device_结构体.md)
