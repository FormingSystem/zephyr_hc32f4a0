---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-407
title: bt_hci_rp_read_codecs_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__codecs__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第407章\_bt\_hci\_rp\_read\_codecs\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__codecs__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 407.1\_数据成员（Data Fields）

<a id="r_a2e9866d0f9fb42b54c406a9ea5890913"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a2e9866d0f9fb42b54c406a9ea5890913)。

<a id="r_a098563f274de085ac97415f1b5e15f3c"></a>

```c
uint8_t codecs [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[codecs](#a098563f274de085ac97415f1b5e15f3c)。

## 407.2\_详细说明（Detailed Documentation）

<a id="a098563f274de085ac97415f1b5e15f3c"></a>

### `codecs`

```c
uint8_t bt_hci_rp_read_codecs_v2::codecs[0]
```

<a id="a2e9866d0f9fb42b54c406a9ea5890913"></a>

### `status`

```c
uint8_t bt_hci_rp_read_codecs_v2::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 407.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P406_bt_hci_rp_read_codecs_结构体.md) · [返回大纲](大纲.md) · [下一章](P408_bt_hci_rp_read_conn_accept_timeout_结构体.md)
