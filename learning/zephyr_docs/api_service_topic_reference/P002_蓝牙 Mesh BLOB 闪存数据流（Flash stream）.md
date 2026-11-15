---
id: learning.zephyr-docs.api-service-topic-reference.page-2
title: 蓝牙 Mesh BLOB 闪存数据流（Flash stream）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__io__flash.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_蓝牙 Mesh BLOB 闪存数据流（Flash stream）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__io__flash.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 2.1\_文件（Files）

<a id="r_blob_5Fio_5Fflash_2Eh"></a>

```c
file blob_io_flash.h
```

相关声明：[blob_io_flash.h](../api_file_supplement_reference/P009_zephyr__bluetooth__mesh__blob_io_flash.h_文件参考.md)。

蓝牙Mesh BLOB闪存流（Flash Stream）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fblob_5Fio_5Fflash"></a>

```c
struct bt_mesh_blob_io_flash
```

相关声明：[bt_mesh_blob_io_flash](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md)。

二进制大对象闪存流（BLOB Flash Stream）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_ga8d99fd3dc35230447f7e7ef9f2c4bc81"></a>

```c
int bt_mesh_blob_io_flash_init (struct bt_mesh_blob_io_flash *flash, uint8_t area_id, off_t offset)
```

相关声明：[bt_mesh_blob_io_flash_init](#ga8d99fd3dc35230447f7e7ef9f2c4bc81)、[bt_mesh_blob_io_flash](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

初始化闪存流（Flash Stream）。

## 2.4\_详细说明（Detailed Documentation）

<a id="ga8d99fd3dc35230447f7e7ef9f2c4bc81"></a>

### `bt_mesh_blob_io_flash_init()`

```c
int bt_mesh_blob_io_flash_init ( struct bt_mesh_blob_io_flash * flash, uint8_t area_id, off_t offset )
```

```c
#include <zephyr/bluetooth/mesh/blob_io_flash.h>
```

初始化闪存流（Flash Stream）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `flash` | 闪存流（Flash Stream）。 |
| `area_id` | 闪存分区标识（Flash Partition Identifier）；参见 `flash_area_open`。 |
| `offset` | 闪存区域内偏移（Offset into the Flash Area），单位为字节（Bytes）。 |

返回（Returns）：成功时为 0，否则为负错误码（Negative Error Code）。


## 2.5\_原页交叉引用（Cross References）

- [blob_io_flash.h](../api_file_supplement_reference/P009_zephyr__bluetooth__mesh__blob_io_flash.h_文件参考.md)
- [bt_mesh_blob_io_flash](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [flash_area_open](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga6fe2593210688eb85e03bea5f96ea2f7)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_电池 API（Battery APIs）.md) · [返回大纲](大纲.md) · [下一章](P003_心跳（Heartbeat）.md)
