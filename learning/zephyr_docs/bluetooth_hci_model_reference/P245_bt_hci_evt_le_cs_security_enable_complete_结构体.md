---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-245
title: bt_hci_evt_le_cs_security_enable_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__security__enable__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第245章\_bt\_hci\_evt\_le\_cs\_security\_enable\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__security__enable__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 245.1\_数据成员（Data Fields）

<a id="r_aaf2de8591b18cd36709f7ef755bee917"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aaf2de8591b18cd36709f7ef755bee917)。

<a id="r_aaa96a8944598914e4439249ba489f726"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#aaa96a8944598914e4439249ba489f726)。

## 245.2\_详细说明（Detailed Documentation）

<a id="aaa96a8944598914e4439249ba489f726"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_cs_security_enable_complete::handle
```

<a id="aaf2de8591b18cd36709f7ef755bee917"></a>

### `status`

```c
uint8_t bt_hci_evt_le_cs_security_enable_complete::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 245.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P246_bt_hci_evt_le_cs_subevent_result_结构体.md)
