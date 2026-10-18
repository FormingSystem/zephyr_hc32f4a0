---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-53
title: bt_hci_cp_le_per_adv_create_sync_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__per__adv__create__sync.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_bt\_hci\_cp\_le\_per\_adv\_create\_sync\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__per__adv__create__sync.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_aff300f352ec5f0fece90f88db811ef75"></a>

```c
uint8_t options
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[options](#aff300f352ec5f0fece90f88db811ef75)。

<a id="r_ab5c4debe1babb98c60c1f1bfdf55359a"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#ab5c4debe1babb98c60c1f1bfdf55359a)。

<a id="r_a3a0a0bc1bd5014f2ede0c4ef6cc30d24"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a3a0a0bc1bd5014f2ede0c4ef6cc30d24)。

<a id="r_a554552684fa2a8d0022f9e31ade9c222"></a>

```c
uint16_t skip
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[skip](#a554552684fa2a8d0022f9e31ade9c222)。

<a id="r_a46ea01403f68d42a315ff629374b2a95"></a>

```c
uint16_t sync_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_timeout](#a46ea01403f68d42a315ff629374b2a95)。

<a id="r_a905b2a9166dd668df5929f0866769576"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a905b2a9166dd668df5929f0866769576)。

## 53.2\_详细说明（Detailed Documentation）

<a id="a3a0a0bc1bd5014f2ede0c4ef6cc30d24"></a>

### `addr`

```c
bt_addr_le_t bt_hci_cp_le_per_adv_create_sync::addr
```

<a id="a905b2a9166dd668df5929f0866769576"></a>

### `cte_type`

```c
uint8_t bt_hci_cp_le_per_adv_create_sync::cte_type
```

<a id="aff300f352ec5f0fece90f88db811ef75"></a>

### `options`

```c
uint8_t bt_hci_cp_le_per_adv_create_sync::options
```

<a id="ab5c4debe1babb98c60c1f1bfdf55359a"></a>

### `sid`

```c
uint8_t bt_hci_cp_le_per_adv_create_sync::sid
```

<a id="a554552684fa2a8d0022f9e31ade9c222"></a>

### `skip`

```c
uint16_t bt_hci_cp_le_per_adv_create_sync::skip
```

<a id="a46ea01403f68d42a315ff629374b2a95"></a>

### `sync_timeout`

```c
uint16_t bt_hci_cp_le_per_adv_create_sync::sync_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_bt_hci_cp_le_past_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md)
