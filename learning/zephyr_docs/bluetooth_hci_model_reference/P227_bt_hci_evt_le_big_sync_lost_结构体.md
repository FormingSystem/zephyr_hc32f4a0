---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-227
title: bt_hci_evt_le_big_sync_lost_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__big__sync__lost.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第227章\_bt\_hci\_evt\_le\_big\_sync\_lost\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__big__sync__lost.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 227.1\_数据成员（Data Fields）

<a id="r_ae59a9c18363f7aee67563494d98aa971"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#ae59a9c18363f7aee67563494d98aa971)。

<a id="r_a02b724a60e71805088aefca9989ad878"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#a02b724a60e71805088aefca9989ad878)。

## 227.2\_详细说明（Detailed Documentation）

<a id="ae59a9c18363f7aee67563494d98aa971"></a>

### `big_handle`

```c
uint8_t bt_hci_evt_le_big_sync_lost::big_handle
```

<a id="a02b724a60e71805088aefca9989ad878"></a>

### `reason`

```c
uint8_t bt_hci_evt_le_big_sync_lost::reason
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 227.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P226_bt_hci_evt_le_big_sync_established_结构体.md) · [返回大纲](大纲.md) · [下一章](P228_bt_hci_evt_le_big_terminate_结构体.md)
