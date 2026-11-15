---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-351
title: bt_hci_rp_le_rand_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__rand.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第351章\_bt\_hci\_rp\_le\_rand\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__rand.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 351.1\_数据成员（Data Fields）

<a id="r_a73320168836caa3caf724282402e80de"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a73320168836caa3caf724282402e80de)。

<a id="r_a3f706af9d2baf9e2b199242a28cec9e5"></a>

```c
uint8_t rand [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rand](#a3f706af9d2baf9e2b199242a28cec9e5)。

## 351.2\_详细说明（Detailed Documentation）

<a id="a3f706af9d2baf9e2b199242a28cec9e5"></a>

### `rand`

```c
uint8_t bt_hci_rp_le_rand::rand[8]
```

<a id="a73320168836caa3caf724282402e80de"></a>

### `status`

```c
uint8_t bt_hci_rp_le_rand::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 351.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P350_bt_hci_rp_le_per_adv_sync_transfer_结构体.md) · [返回大纲](大纲.md) · [下一章](P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md)
