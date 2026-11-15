---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-128
title: bt_hci_cp_le_subrate_request_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__subrate__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第128章\_bt\_hci\_cp\_le\_subrate\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__subrate__request.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 128.1\_数据成员（Data Fields）

<a id="r_a2595419182358e3386a0fb6e523a3dda"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a2595419182358e3386a0fb6e523a3dda)。

<a id="r_a18ba526d8a843ad9c74c22d0899d9c1f"></a>

```c
uint16_t subrate_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_min](#a18ba526d8a843ad9c74c22d0899d9c1f)。

<a id="r_a5c95a2bea462fb72d34d6314046041b7"></a>

```c
uint16_t subrate_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_max](#a5c95a2bea462fb72d34d6314046041b7)。

<a id="r_a04ccc83303baabf30b663983883e7e77"></a>

```c
uint16_t max_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_latency](#a04ccc83303baabf30b663983883e7e77)。

<a id="r_ab32a92ed52266c6b7d6d9ab08787e770"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#ab32a92ed52266c6b7d6d9ab08787e770)。

<a id="r_a60bcbe27605063725422a0b1c35f21e7"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#a60bcbe27605063725422a0b1c35f21e7)。

## 128.2\_详细说明（Detailed Documentation）

<a id="ab32a92ed52266c6b7d6d9ab08787e770"></a>

### `continuation_number`

```c
uint16_t bt_hci_cp_le_subrate_request::continuation_number
```

<a id="a2595419182358e3386a0fb6e523a3dda"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_subrate_request::handle
```

<a id="a04ccc83303baabf30b663983883e7e77"></a>

### `max_latency`

```c
uint16_t bt_hci_cp_le_subrate_request::max_latency
```

<a id="a5c95a2bea462fb72d34d6314046041b7"></a>

### `subrate_max`

```c
uint16_t bt_hci_cp_le_subrate_request::subrate_max
```

<a id="a18ba526d8a843ad9c74c22d0899d9c1f"></a>

### `subrate_min`

```c
uint16_t bt_hci_cp_le_subrate_request::subrate_min
```

<a id="a60bcbe27605063725422a0b1c35f21e7"></a>

### `supervision_timeout`

```c
uint16_t bt_hci_cp_le_subrate_request::supervision_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 128.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P127_bt_hci_cp_le_start_encryption_结构体.md) · [返回大纲](大纲.md) · [下一章](P129_bt_hci_cp_le_terminate_big_结构体.md)
