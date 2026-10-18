---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-283
title: bt_hci_evt_mesh_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__mesh.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第283章\_bt\_hci\_evt\_mesh\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__mesh.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 283.1\_数据成员（Data Fields）

<a id="r_aaa8104b855bba787c69851ae7872a03e"></a>

```c
uint8_t prefix
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prefix](#aaa8104b855bba787c69851ae7872a03e)。

<a id="r_ac0186d74e355c90c866dda51605b85ac"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#ac0186d74e355c90c866dda51605b85ac)。

## 283.2\_详细说明（Detailed Documentation）

<a id="aaa8104b855bba787c69851ae7872a03e"></a>

### `prefix`

```c
uint8_t bt_hci_evt_mesh::prefix
```

<a id="ac0186d74e355c90c866dda51605b85ac"></a>

### `subevent`

```c
uint8_t bt_hci_evt_mesh::subevent
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 283.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P282_bt_hci_evt_link_key_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P284_bt_hci_evt_mesh_adv_complete_结构体.md)
