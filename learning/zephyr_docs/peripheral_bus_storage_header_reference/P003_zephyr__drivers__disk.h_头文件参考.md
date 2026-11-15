---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-3
title: zephyr__drivers__disk.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/disk_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_disk.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/disk_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

磁盘（Disk）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/dlist.h>
```

查看此文件的源码。

磁盘驱动 API 的主头文件。此文件包含磁盘访问接口。除磁盘外，Flash、RAM 磁盘等其他存储介质也可实现此接口，供 USB 大容量存储（Mass Storage）、文件系统（Filesystems）等上层使用者访问。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_disk_5Finfo"></a>

```c
struct disk_info
```

相关声明：[disk_info](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md)。

磁盘信息（Disk Info）。

<a id="r_disk_5Foperations"></a>

```c
struct disk_operations
```

相关声明：[disk_operations](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md)。

磁盘操作（Disk Operations）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga7e75d3121989e64a8c6e218409e8fe95"></a>

```c
#define DISK_IOCTL_GET_SECTOR_COUNT 1
```

相关声明：[DISK_IOCTL_GET_SECTOR_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga7e75d3121989e64a8c6e218409e8fe95)。

`disk_access_ioctl()` 可用的命令码（Command codes）。

<a id="r_ga03dcb39dd5be7144d8f6ae76b7415e9a"></a>

```c
#define DISK_IOCTL_GET_SECTOR_SIZE 2
```

相关声明：[DISK_IOCTL_GET_SECTOR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga03dcb39dd5be7144d8f6ae76b7415e9a)。

获取磁盘扇区（Sector）的大小，单位为字节。

<a id="r_ga7ffc5d075a4e8d6eb659ee4ea73e62a0"></a>

```c
#define DISK_IOCTL_RESERVED 3
```

相关声明：[DISK_IOCTL_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga7ffc5d075a4e8d6eb659ee4ea73e62a0)。

保留（Reserved）。

<a id="r_ga2444e2a2884f9e0d6dd93aedc5d654ac"></a>

```c
#define DISK_IOCTL_GET_ERASE_BLOCK_SZ 4
```

相关声明：[DISK_IOCTL_GET_ERASE_BLOCK_SZ](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga2444e2a2884f9e0d6dd93aedc5d654ac)。

构成一个 Flash 擦除块（Erase block）的扇区数量。

<a id="r_ga656aaa245cc142f3ff82a003bb307d62"></a>

```c
#define DISK_IOCTL_CTRL_SYNC 5
```

相关声明：[DISK_IOCTL_CTRL_SYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga656aaa245cc142f3ff82a003bb307d62)。

将缓存中的读写操作提交到磁盘。

<a id="r_ga9def34b23915a3ce6c9a8a746d3d1372"></a>

```c
#define DISK_IOCTL_CTRL_INIT 6
```

相关声明：[DISK_IOCTL_CTRL_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga9def34b23915a3ce6c9a8a746d3d1372)。

初始化磁盘。

<a id="r_gaf13b377592baace863070fee450bd5be"></a>

```c
#define DISK_IOCTL_CTRL_DEINIT 7
```

相关声明：[DISK_IOCTL_CTRL_DEINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gaf13b377592baace863070fee450bd5be)。

反初始化磁盘。

<a id="r_ga123275f83eb2c3573b86a3f44fadf53c"></a>

```c
#define DISK_IOCTL_GET_CARD_CID 8
```

相关声明：[DISK_IOCTL_GET_CARD_CID](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga123275f83eb2c3573b86a3f44fadf53c)。

获取卡标识寄存器（Card Identification register，CID）的值。

<a id="r_gae1730a7bf4ca0210bc8eefe3b590623a"></a>

```c
#define DISK_STATUS_OK 0x00
```

相关声明：[DISK_STATUS_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gae1730a7bf4ca0210bc8eefe3b590623a)。

`disk_access_status()` 可能返回的位掩码。

<a id="r_ga533eb718a946ba60e0ad6e0e4fd4f75a"></a>

```c
#define DISK_STATUS_UNINIT 0x01
```

相关声明：[DISK_STATUS_UNINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga533eb718a946ba60e0ad6e0e4fd4f75a)。

磁盘状态：未初始化（Uninitialized）。

<a id="r_ga1c70c8182b3497f606091f19c142be59"></a>

```c
#define DISK_STATUS_NOMEDIA 0x02
```

相关声明：[DISK_STATUS_NOMEDIA](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga1c70c8182b3497f606091f19c142be59)。

磁盘状态：无介质（No media）。

<a id="r_ga0a5ba8f4be6241f62a969ea56c26f7e3"></a>

```c
#define DISK_STATUS_WR_PROTECT 0x04
```

相关声明：[DISK_STATUS_WR_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga0a5ba8f4be6241f62a969ea56c26f7e3)。

磁盘状态：写保护（Write protected）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_gaa11586a0b8ae6f2f0c142cec0df0c5fa"></a>

```c
int disk_access_register (struct disk_info *disk)
```

相关声明：[disk_access_register](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gaa11586a0b8ae6f2f0c142cec0df0c5fa)、[disk_info](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md)。

注册磁盘。

<a id="r_gada802c6be65186009162a25f391dfb71"></a>

```c
int disk_access_unregister (struct disk_info *disk)
```

相关声明：[disk_access_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gada802c6be65186009162a25f391dfb71)、[disk_info](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md)。

注销磁盘。


## 3.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/sys/dlist.h](../dlist_reference/P003_双向链表头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/disk_8h_source.html)
- [disk_info](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md)
- [disk_operations](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md)
- [DISK_IOCTL_GET_SECTOR_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga7e75d3121989e64a8c6e218409e8fe95)
- [disk_access_ioctl()](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ga152d85821d73644fea7ffde27b7c953c)
- [DISK_IOCTL_GET_SECTOR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga03dcb39dd5be7144d8f6ae76b7415e9a)
- [DISK_IOCTL_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga7ffc5d075a4e8d6eb659ee4ea73e62a0)
- [DISK_IOCTL_GET_ERASE_BLOCK_SZ](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga2444e2a2884f9e0d6dd93aedc5d654ac)
- [DISK_IOCTL_CTRL_SYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga656aaa245cc142f3ff82a003bb307d62)
- [DISK_IOCTL_CTRL_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga9def34b23915a3ce6c9a8a746d3d1372)
- [DISK_IOCTL_CTRL_DEINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gaf13b377592baace863070fee450bd5be)
- [DISK_IOCTL_GET_CARD_CID](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga123275f83eb2c3573b86a3f44fadf53c)
- [DISK_STATUS_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gae1730a7bf4ca0210bc8eefe3b590623a)
- [disk_access_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gac5348a854fe68a607672118c91346133)
- [DISK_STATUS_UNINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga533eb718a946ba60e0ad6e0e4fd4f75a)
- [DISK_STATUS_NOMEDIA](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga1c70c8182b3497f606091f19c142be59)
- [DISK_STATUS_WR_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga0a5ba8f4be6241f62a969ea56c26f7e3)
- [disk_access_register](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gaa11586a0b8ae6f2f0c142cec0df0c5fa)
- [disk_access_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gada802c6be65186009162a25f391dfb71)

<a id="header-details"></a>

---

[上一章](P002_zephyr__drivers__misc__devmux__devmux.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__drivers__espi.h_头文件参考.md)
