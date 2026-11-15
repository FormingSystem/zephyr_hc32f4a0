---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-44
title: bt_hci_cp_le_frame_space_update_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__frame__space__update.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_bt\_hci\_cp\_le\_frame\_space\_update\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__frame__space__update.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_a6f8ae56a870c76d06e47aa15d22ca341"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a6f8ae56a870c76d06e47aa15d22ca341)。

<a id="r_a9854593fb39c71bfd5ee3da6f606dd7f"></a>

```c
uint16_t frame_space_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frame_space_min](#a9854593fb39c71bfd5ee3da6f606dd7f)。

<a id="r_ab449a9514f175ad73942582f07cdf792"></a>

```c
uint16_t frame_space_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frame_space_max](#ab449a9514f175ad73942582f07cdf792)。

<a id="r_a10fb9f808dec017325861c983beb6bc9"></a>

```c
uint8_t phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phys](#a10fb9f808dec017325861c983beb6bc9)。

<a id="r_acbb6b64086a5710449b4d4e228575325"></a>

```c
uint16_t spacing_types
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[spacing_types](#acbb6b64086a5710449b4d4e228575325)。

## 44.2\_详细说明（Detailed Documentation）

<a id="ab449a9514f175ad73942582f07cdf792"></a>

### `frame_space_max`

```c
uint16_t bt_hci_cp_le_frame_space_update::frame_space_max
```

<a id="a9854593fb39c71bfd5ee3da6f606dd7f"></a>

### `frame_space_min`

```c
uint16_t bt_hci_cp_le_frame_space_update::frame_space_min
```

<a id="a6f8ae56a870c76d06e47aa15d22ca341"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_frame_space_update::handle
```

<a id="a10fb9f808dec017325861c983beb6bc9"></a>

### `phys`

```c
uint8_t bt_hci_cp_le_frame_space_update::phys
```

<a id="acbb6b64086a5710449b4d4e228575325"></a>

### `spacing_types`

```c
uint16_t bt_hci_cp_le_frame_space_update::spacing_types
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_bt_hci_cp_le_generate_dhkey_结构体.md)
