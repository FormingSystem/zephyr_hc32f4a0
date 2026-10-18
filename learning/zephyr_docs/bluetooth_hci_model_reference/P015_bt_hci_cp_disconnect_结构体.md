---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-15
title: bt_hci_cp_disconnect_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__disconnect.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_bt\_hci\_cp\_disconnect\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__disconnect.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a9cb5bcd135082c37a19cce57ffa123ff"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a9cb5bcd135082c37a19cce57ffa123ff)。

<a id="r_a8e10edb1e700c1ef38f39bf20b9b374f"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#a8e10edb1e700c1ef38f39bf20b9b374f)。

## 15.2\_详细说明（Detailed Documentation）

<a id="a9cb5bcd135082c37a19cce57ffa123ff"></a>

### `handle`

```c
uint16_t bt_hci_cp_disconnect::handle
```

<a id="a8e10edb1e700c1ef38f39bf20b9b374f"></a>

### `reason`

```c
uint8_t bt_hci_cp_disconnect::reason
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_bt_hci_cp_connect_cancel_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_bt_hci_cp_exit_sniff_mode_结构体.md)
