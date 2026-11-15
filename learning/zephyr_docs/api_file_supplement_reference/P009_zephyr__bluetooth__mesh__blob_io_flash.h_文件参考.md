---
id: learning.zephyr-docs.api-file-supplement-reference.page-9
title: zephyr__bluetooth__mesh__blob_io_flash.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/blob__io__flash_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_bluetooth\_\_mesh\_\_blob\_io\_flash.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/blob__io__flash_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh BLOB闪存流（Flash Stream）API的头文件。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

蓝牙Mesh BLOB闪存流（Flash Stream）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fblob_5Fio_5Fflash"></a>

```c
struct bt_mesh_blob_io_flash
```

相关声明：[bt_mesh_blob_io_flash](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md)。

二进制大对象闪存流（BLOB Flash Stream）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.2\_函数（Functions）

<a id="r_ga8d99fd3dc35230447f7e7ef9f2c4bc81"></a>

```c
int bt_mesh_blob_io_flash_init (struct bt_mesh_blob_io_flash *flash, uint8_t area_id, off_t offset)
```

相关声明：[bt_mesh_blob_io_flash_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__io__flash.html#ga8d99fd3dc35230447f7e7ef9f2c4bc81)、[bt_mesh_blob_io_flash](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

初始化闪存流（Flash Stream）。


## 9.3\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/blob__io__flash_8h_source.html)
- [bt_mesh_blob_io_flash](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md)
- [bt_mesh_blob_io_flash_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__io__flash.html#ga8d99fd3dc35230447f7e7ef9f2c4bc81)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)

<a id="header-details"></a>

---

[上一章](P008_zephyr__retention__blinfo.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__bluetooth__controller.h_文件参考.md)
