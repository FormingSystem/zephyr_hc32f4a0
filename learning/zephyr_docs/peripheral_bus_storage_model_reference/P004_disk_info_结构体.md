---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-4
title: disk_info_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdisk__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_disk\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdisk__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

磁盘信息（Disk Info）。

```c
#include <zephyr/drivers/disk.h>
```

<a id="details"></a>

磁盘信息（Disk Info）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_ab3413d8809d5181c671e1890a4662ba2"></a>

```c
sys_dnode_t node
```

相关声明：[sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)、[node](#ab3413d8809d5181c671e1890a4662ba2)。

内部使用的链表节点。

<a id="r_ac8ce763ca2514e4c4f4f8e0e04547ed3"></a>

```c
const char * name
```

相关声明：[name](#ac8ce763ca2514e4c4f4f8e0e04547ed3)。

磁盘名称（Disk name）。

<a id="r_a329a571f988718fd4737b8974d4f7ada"></a>

```c
const struct disk_operations * ops
```

相关声明：[disk_operations](P005_disk_operations_结构体.md)、[ops](#a329a571f988718fd4737b8974d4f7ada)。

磁盘操作（Disk Operations）。

<a id="r_ae316915bd577f22dc9d353fc4b2f04bb"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#ae316915bd577f22dc9d353fc4b2f04bb)。

与此磁盘关联的设备。

<a id="r_accc0a618e4d939543f6ffc553b45e3b2"></a>

```c
uint16_t refcnt
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[refcnt](#accc0a618e4d939543f6ffc553b45e3b2)。

内部使用的磁盘引用计数（Reference count）。

## 4.2\_详细说明（Detailed Documentation）

<a id="ae316915bd577f22dc9d353fc4b2f04bb"></a>

### `dev`

```c
const struct device* disk_info::dev
```

与此磁盘关联的设备。

<a id="ac8ce763ca2514e4c4f4f8e0e04547ed3"></a>

### `name`

```c
const char* disk_info::name
```

磁盘名称（Disk name）。

<a id="ab3413d8809d5181c671e1890a4662ba2"></a>

### `node`

```c
sys_dnode_t disk_info::node
```

内部使用的链表节点。

<a id="a329a571f988718fd4737b8974d4f7ada"></a>

### `ops`

```c
const struct disk_operations* disk_info::ops
```

磁盘操作（Disk Operations）。

<a id="accc0a618e4d939543f6ffc553b45e3b2"></a>

### `refcnt`

```c
uint16_t disk_info::refcnt
```

内部使用的磁盘引用计数（Reference count）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/disk.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/drivers/disk.h](https://docs.zephyrproject.org/latest/doxygen/html/disk_8h_source.html)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [disk_operations](P005_disk_operations_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_devmux_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_disk_operations_结构体.md)
