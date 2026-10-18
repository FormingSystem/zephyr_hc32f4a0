---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-412
title: bt_hci_rp_read_link_policy_settings_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__link__policy__settings.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第412章\_bt\_hci\_rp\_read\_link\_policy\_settings\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__link__policy__settings.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 412.1\_数据成员（Data Fields）

<a id="r_ad73d8ed381f8bbc4914c38bb0ebcae01"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ad73d8ed381f8bbc4914c38bb0ebcae01)。

<a id="r_a4ec0cdfa8ae48d9ed8ae2d46f16a9638"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a4ec0cdfa8ae48d9ed8ae2d46f16a9638)。

<a id="r_a69fe8085d161bf87051a52dc9c511156"></a>

```c
uint16_t link_policy_settings
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[link_policy_settings](#a69fe8085d161bf87051a52dc9c511156)。

## 412.2\_详细说明（Detailed Documentation）

<a id="a4ec0cdfa8ae48d9ed8ae2d46f16a9638"></a>

### `handle`

```c
uint16_t bt_hci_rp_read_link_policy_settings::handle
```

<a id="a69fe8085d161bf87051a52dc9c511156"></a>

### `link_policy_settings`

```c
uint16_t bt_hci_rp_read_link_policy_settings::link_policy_settings
```

<a id="ad73d8ed381f8bbc4914c38bb0ebcae01"></a>

### `status`

```c
uint8_t bt_hci_rp_read_link_policy_settings::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 412.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P411_bt_hci_rp_read_encryption_key_size_结构体.md) · [返回大纲](大纲.md) · [下一章](P413_bt_hci_rp_read_link_supervision_timeout_结构体.md)
