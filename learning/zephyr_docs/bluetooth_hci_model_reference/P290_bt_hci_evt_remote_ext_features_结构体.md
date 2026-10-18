---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-290
title: bt_hci_evt_remote_ext_features_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__remote__ext__features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第290章\_bt\_hci\_evt\_remote\_ext\_features\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__remote__ext__features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 290.1\_数据成员（Data Fields）

<a id="r_a4f1d489aaa5626e485d34a9ae4cf9a34"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a4f1d489aaa5626e485d34a9ae4cf9a34)。

<a id="r_a0191b80b4f4d5360972faa6d5edf5055"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a0191b80b4f4d5360972faa6d5edf5055)。

<a id="r_aeece2b8d46f4a3713d63df29058f2d9c"></a>

```c
uint8_t page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[page](#aeece2b8d46f4a3713d63df29058f2d9c)。

<a id="r_afa577407f4ded5404394f42e7c73e10b"></a>

```c
uint8_t max_page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_page](#afa577407f4ded5404394f42e7c73e10b)。

<a id="r_a084199f8e30669c2a1a631af26c0d69a"></a>

```c
uint8_t features [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[features](#a084199f8e30669c2a1a631af26c0d69a)。

## 290.2\_详细说明（Detailed Documentation）

<a id="a084199f8e30669c2a1a631af26c0d69a"></a>

### `features`

```c
uint8_t bt_hci_evt_remote_ext_features::features[8]
```

<a id="a0191b80b4f4d5360972faa6d5edf5055"></a>

### `handle`

```c
uint16_t bt_hci_evt_remote_ext_features::handle
```

<a id="afa577407f4ded5404394f42e7c73e10b"></a>

### `max_page`

```c
uint8_t bt_hci_evt_remote_ext_features::max_page
```

<a id="aeece2b8d46f4a3713d63df29058f2d9c"></a>

### `page`

```c
uint8_t bt_hci_evt_remote_ext_features::page
```

<a id="a4f1d489aaa5626e485d34a9ae4cf9a34"></a>

### `status`

```c
uint8_t bt_hci_evt_remote_ext_features::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 290.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P289_bt_hci_evt_pin_code_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P291_bt_hci_evt_remote_features_结构体.md)
