---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-427
title: bt_hci_rp_vs_read_static_addrs_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__static__addrs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第427章\_bt\_hci\_rp\_vs\_read\_static\_addrs\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__static__addrs.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 427.1\_数据成员（Data Fields）

<a id="r_af3ddb349e82e7a5edcb86300c8d8a548"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#af3ddb349e82e7a5edcb86300c8d8a548)。

<a id="r_a482a0984602d4d59ef9572d4e1053a99"></a>

```c
uint8_t num_addrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_addrs](#a482a0984602d4d59ef9572d4e1053a99)。

<a id="r_af8175d96852a67ebcfa4da5019e618e9"></a>

```c
struct bt_hci_vs_static_addr a [0]
```

相关声明：[bt_hci_vs_static_addr](P449_bt_hci_vs_static_addr_结构体.md)、[a](#af8175d96852a67ebcfa4da5019e618e9)。

## 427.2\_详细说明（Detailed Documentation）

<a id="af8175d96852a67ebcfa4da5019e618e9"></a>

### `a`

```c
struct bt_hci_vs_static_addr bt_hci_rp_vs_read_static_addrs::a[0]
```

<a id="a482a0984602d4d59ef9572d4e1053a99"></a>

### `num_addrs`

```c
uint8_t bt_hci_rp_vs_read_static_addrs::num_addrs
```

<a id="af3ddb349e82e7a5edcb86300c8d8a548"></a>

### `status`

```c
uint8_t bt_hci_rp_vs_read_static_addrs::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 427.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_vs_static_addr](P449_bt_hci_vs_static_addr_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md) · [返回大纲](大纲.md) · [下一章](P428_bt_hci_rp_vs_read_supported_commands_结构体.md)
