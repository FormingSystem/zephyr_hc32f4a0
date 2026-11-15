---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-185
title: bt_hci_cp_write_class_of_device_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__class__of__device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第185章\_bt\_hci\_cp\_write\_class\_of\_device\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__class__of__device.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 185.1\_数据成员（Data Fields）

<a id="r_acc3b940de1a5da095e8a4f18e69229f2"></a>

```c
uint8_t class_of_device [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[class_of_device](#acc3b940de1a5da095e8a4f18e69229f2)。

## 185.2\_详细说明（Detailed Documentation）

<a id="acc3b940de1a5da095e8a4f18e69229f2"></a>

### `class_of_device`

```c
uint8_t bt_hci_cp_write_class_of_device::class_of_device[3]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 185.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P184_bt_hci_cp_write_auth_payload_timeout_结构体.md) · [返回大纲](大纲.md) · [下一章](P186_bt_hci_cp_write_conn_accept_timeout_结构体.md)
