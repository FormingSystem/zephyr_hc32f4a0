---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-203
title: bt_hci_evt_auth_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__auth__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第203章\_bt\_hci\_evt\_auth\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__auth__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 203.1\_数据成员（Data Fields）

<a id="r_ae2b4b5bcc7195247626004d46ee22dd5"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ae2b4b5bcc7195247626004d46ee22dd5)。

<a id="r_a7a78803e156218f138866fbb13fdadce"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a7a78803e156218f138866fbb13fdadce)。

## 203.2\_详细说明（Detailed Documentation）

<a id="a7a78803e156218f138866fbb13fdadce"></a>

### `handle`

```c
uint16_t bt_hci_evt_auth_complete::handle
```

<a id="ae2b4b5bcc7195247626004d46ee22dd5"></a>

### `status`

```c
uint8_t bt_hci_evt_auth_complete::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 203.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P202_bt_hci_driver_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P204_bt_hci_evt_auth_payload_timeout_exp_结构体.md)
