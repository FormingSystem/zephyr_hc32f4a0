---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-8
title: bt_mesh_blob_io_flash_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io__flash.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_bt\_mesh\_blob\_io\_flash\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io__flash.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

二进制大对象闪存流（BLOB Flash Stream）。

```c
#include <zephyr/bluetooth/mesh/blob_io_flash.h>
```

<a id="details"></a>

二进制大对象闪存流（BLOB Flash Stream）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_a3b506d86d9cc7fb7206f96cbdd2cd3fe"></a>

```c
uint8_t area_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[area_id](#a3b506d86d9cc7fb7206f96cbdd2cd3fe)。

要写入二进制大对象（BLOB）的闪存区域标识符（Flash area ID）。

<a id="r_a511648b9e653993aee99eda5efe3b1e9"></a>

```c
enum bt_mesh_blob_io_mode mode
```

相关声明：[bt_mesh_blob_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga2618fb7365f180a73a7eecd11cf2f962)、[mode](#a511648b9e653993aee99eda5efe3b1e9)。

当前流模式（Active stream mode）。

<a id="r_ac4eb40a7e53adce60c2fcd11eb0b6b57"></a>

```c
off_t offset
```

相关声明：[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[offset](#ac4eb40a7e53adce60c2fcd11eb0b6b57)。

在闪存区域（Flash area）内放置二进制大对象（BLOB）的偏移量，单位为字节。

<a id="r_a99227cd93d2b6230be7bd5cef9fb8232"></a>

```c
const struct flash_area * area
```

相关声明：[flash_area](https://docs.zephyrproject.org/latest/doxygen/html/structflash__area.html)、[area](#a99227cd93d2b6230be7bd5cef9fb8232)。

<a id="r_a24abc17719dd627e3e3d7c8e61d4c96f"></a>

```c
struct bt_mesh_blob_io io
```

相关声明：[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[io](#a24abc17719dd627e3e3d7c8e61d4c96f)。

## 8.2\_详细说明（Detailed Documentation）

<a id="a99227cd93d2b6230be7bd5cef9fb8232"></a>

### `area`

```c
const struct flash_area* bt_mesh_blob_io_flash::area
```

<a id="a3b506d86d9cc7fb7206f96cbdd2cd3fe"></a>

### `area_id`

```c
uint8_t bt_mesh_blob_io_flash::area_id
```

要写入二进制大对象（BLOB）的闪存区域标识符（Flash area ID）。

<a id="a24abc17719dd627e3e3d7c8e61d4c96f"></a>

### `io`

```c
struct bt_mesh_blob_io bt_mesh_blob_io_flash::io
```

<a id="a511648b9e653993aee99eda5efe3b1e9"></a>

### `mode`

```c
enum bt_mesh_blob_io_mode bt_mesh_blob_io_flash::mode
```

当前流模式（Active stream mode）。

<a id="ac4eb40a7e53adce60c2fcd11eb0b6b57"></a>

### `offset`

```c
off_t bt_mesh_blob_io_flash::offset
```

在闪存区域（Flash area）内放置二进制大对象（BLOB）的偏移量，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_io_flash.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_io_flash.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__io__flash_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_blob_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga2618fb7365f180a73a7eecd11cf2f962)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [flash_area](https://docs.zephyrproject.org/latest/doxygen/html/structflash__area.html)
- [bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_bt_mesh_blob_io_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_bt_mesh_blob_srv_结构体.md)
