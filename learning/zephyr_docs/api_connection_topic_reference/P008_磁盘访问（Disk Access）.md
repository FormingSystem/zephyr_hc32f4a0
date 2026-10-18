---
id: learning.zephyr-docs.api-connection-topic-reference.page-8
title: 磁盘访问（Disk Access）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_磁盘访问（Disk Access）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

磁盘接口。

<a id="details"></a>

磁盘接口（Interfaces for disks）。自 Zephyr 1.6 起提供；API 版本为 1.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 8.1\_主题（Topics）

<a id="r_disk_5Fdriver_5Finterface_5Fext"></a>

相关声明：[设备专用磁盘访问 API 扩展（Device-specific Disk Access API extensions）](../api_topic_reference/P031_设备专用磁盘访问 API 扩展（Device-specific Disk Access API extensions）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 8.2\_文件（Files）

<a id="r_disk_2Eh"></a>

```c
file disk.h
```

相关声明：[disk.h](../peripheral_bus_storage_header_reference/P003_zephyr__drivers__disk.h_头文件参考.md)。

磁盘（Disk）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.3\_数据结构（Data Structures）

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

## 8.4\_宏定义（Macros）

<a id="r_ga7e75d3121989e64a8c6e218409e8fe95"></a>

```c
#define DISK_IOCTL_GET_SECTOR_COUNT 1
```

相关声明：[DISK_IOCTL_GET_SECTOR_COUNT](#ga7e75d3121989e64a8c6e218409e8fe95)。

`disk_access_ioctl()` 可用的命令码（Command codes）。

<a id="r_ga03dcb39dd5be7144d8f6ae76b7415e9a"></a>

```c
#define DISK_IOCTL_GET_SECTOR_SIZE 2
```

相关声明：[DISK_IOCTL_GET_SECTOR_SIZE](#ga03dcb39dd5be7144d8f6ae76b7415e9a)。

获取磁盘扇区（Sector）的大小，单位为字节。

<a id="r_ga7ffc5d075a4e8d6eb659ee4ea73e62a0"></a>

```c
#define DISK_IOCTL_RESERVED 3
```

相关声明：[DISK_IOCTL_RESERVED](#ga7ffc5d075a4e8d6eb659ee4ea73e62a0)。

保留（Reserved）。

<a id="r_ga2444e2a2884f9e0d6dd93aedc5d654ac"></a>

```c
#define DISK_IOCTL_GET_ERASE_BLOCK_SZ 4
```

相关声明：[DISK_IOCTL_GET_ERASE_BLOCK_SZ](#ga2444e2a2884f9e0d6dd93aedc5d654ac)。

构成一个 Flash 擦除块（Erase block）的扇区数量。

<a id="r_ga656aaa245cc142f3ff82a003bb307d62"></a>

```c
#define DISK_IOCTL_CTRL_SYNC 5
```

相关声明：[DISK_IOCTL_CTRL_SYNC](#ga656aaa245cc142f3ff82a003bb307d62)。

将缓存中的读写操作提交到磁盘。

<a id="r_ga9def34b23915a3ce6c9a8a746d3d1372"></a>

```c
#define DISK_IOCTL_CTRL_INIT 6
```

相关声明：[DISK_IOCTL_CTRL_INIT](#ga9def34b23915a3ce6c9a8a746d3d1372)。

初始化磁盘。

<a id="r_gaf13b377592baace863070fee450bd5be"></a>

```c
#define DISK_IOCTL_CTRL_DEINIT 7
```

相关声明：[DISK_IOCTL_CTRL_DEINIT](#gaf13b377592baace863070fee450bd5be)。

反初始化磁盘。

<a id="r_ga123275f83eb2c3573b86a3f44fadf53c"></a>

```c
#define DISK_IOCTL_GET_CARD_CID 8
```

相关声明：[DISK_IOCTL_GET_CARD_CID](#ga123275f83eb2c3573b86a3f44fadf53c)。

获取卡标识寄存器（Card Identification register，CID）的值。

<a id="r_gae1730a7bf4ca0210bc8eefe3b590623a"></a>

```c
#define DISK_STATUS_OK 0x00
```

相关声明：[DISK_STATUS_OK](#gae1730a7bf4ca0210bc8eefe3b590623a)。

`disk_access_status()` 可能返回的位掩码。

<a id="r_ga533eb718a946ba60e0ad6e0e4fd4f75a"></a>

```c
#define DISK_STATUS_UNINIT 0x01
```

相关声明：[DISK_STATUS_UNINIT](#ga533eb718a946ba60e0ad6e0e4fd4f75a)。

磁盘状态：未初始化（Uninitialized）。

<a id="r_ga1c70c8182b3497f606091f19c142be59"></a>

```c
#define DISK_STATUS_NOMEDIA 0x02
```

相关声明：[DISK_STATUS_NOMEDIA](#ga1c70c8182b3497f606091f19c142be59)。

磁盘状态：无介质（No media）。

<a id="r_ga0a5ba8f4be6241f62a969ea56c26f7e3"></a>

```c
#define DISK_STATUS_WR_PROTECT 0x04
```

相关声明：[DISK_STATUS_WR_PROTECT](#ga0a5ba8f4be6241f62a969ea56c26f7e3)。

磁盘状态：写保护（Write protected）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.5\_函数（Functions）

<a id="r_gaa11586a0b8ae6f2f0c142cec0df0c5fa"></a>

```c
int disk_access_register (struct disk_info *disk)
```

相关声明：[disk_access_register](#gaa11586a0b8ae6f2f0c142cec0df0c5fa)、[disk_info](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md)。

注册磁盘。

<a id="r_gada802c6be65186009162a25f391dfb71"></a>

```c
int disk_access_unregister (struct disk_info *disk)
```

相关声明：[disk_access_unregister](#gada802c6be65186009162a25f391dfb71)、[disk_info](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md)。

注销磁盘。

## 8.6\_详细说明（Detailed Documentation）

<a id="gaf13b377592baace863070fee450bd5be"></a>

### `DISK_IOCTL_CTRL_DEINIT`

```c
#define DISK_IOCTL_CTRL_DEINIT 7
```

```c
#include <zephyr/drivers/disk.h>
```

反初始化磁盘。

此输入／输出控制操作（IOCTL）用于反初始化磁盘；如果磁盘支持热插拔，就可以将其从系统中移除。磁盘使用采用引用计数（reference counting），因此，对给定磁盘必须发出与 `DISK_IOCTL_CTRL_INIT` 调用次数相同数量的 `DISK_IOCTL_CTRL_DEINIT`，才能将其反初始化。

此宏的 `buf` 参数可选地接受一个布尔值指针。该值为 true 时，表示应忽略全部引用计数，强制停止磁盘。请求强制停止时，磁盘驱动必须报告成功，但此操作本身是不安全的。

<a id="ga9def34b23915a3ce6c9a8a746d3d1372"></a>

### `DISK_IOCTL_CTRL_INIT`

```c
#define DISK_IOCTL_CTRL_INIT 6
```

```c
#include <zephyr/drivers/disk.h>
```

初始化磁盘。

磁盘用于 I/O 之前必须发出此 IOCTL。它采用引用计数，因此只有对尚未初始化磁盘的第一次成功调用才会初始化 I/O 设备。

<a id="ga656aaa245cc142f3ff82a003bb307d62"></a>

### `DISK_IOCTL_CTRL_SYNC`

```c
#define DISK_IOCTL_CTRL_SYNC 5
```

```c
#include <zephyr/drivers/disk.h>
```

将缓存中的读写操作提交到磁盘。

<a id="ga123275f83eb2c3573b86a3f44fadf53c"></a>

### `DISK_IOCTL_GET_CARD_CID`

```c
#define DISK_IOCTL_GET_CARD_CID 8
```

```c
#include <zephyr/drivers/disk.h>
```

获取卡标识寄存器（Card Identification register，CID）的值。

传入缓冲区的长度必须为四个 32 位整数，以保存从卡中读取的卡标识（CID）寄存器值。

<a id="ga2444e2a2884f9e0d6dd93aedc5d654ac"></a>

### `DISK_IOCTL_GET_ERASE_BLOCK_SZ`

```c
#define DISK_IOCTL_GET_ERASE_BLOCK_SZ 4
```

```c
#include <zephyr/drivers/disk.h>
```

构成一个 Flash 擦除块（Erase block）的扇区数量。

<a id="ga7e75d3121989e64a8c6e218409e8fe95"></a>

### `DISK_IOCTL_GET_SECTOR_COUNT`

```c
#define DISK_IOCTL_GET_SECTOR_COUNT 1
```

```c
#include <zephyr/drivers/disk.h>
```

`disk_access_ioctl()` 可用的命令码（Command codes）。

获取磁盘扇区（sectors）数量。

<a id="ga03dcb39dd5be7144d8f6ae76b7415e9a"></a>

### `DISK_IOCTL_GET_SECTOR_SIZE`

```c
#define DISK_IOCTL_GET_SECTOR_SIZE 2
```

```c
#include <zephyr/drivers/disk.h>
```

获取磁盘扇区（Sector）的大小，单位为字节。

<a id="ga7ffc5d075a4e8d6eb659ee4ea73e62a0"></a>

### `DISK_IOCTL_RESERVED`

```c
#define DISK_IOCTL_RESERVED 3
```

```c
#include <zephyr/drivers/disk.h>
```

保留（Reserved）。

此项以前名为 `DISK_IOCTL_GET_DISK_SIZE`。

<a id="ga1c70c8182b3497f606091f19c142be59"></a>

### `DISK_STATUS_NOMEDIA`

```c
#define DISK_STATUS_NOMEDIA 0x02
```

```c
#include <zephyr/drivers/disk.h>
```

磁盘状态：无介质（No media）。

<a id="gae1730a7bf4ca0210bc8eefe3b590623a"></a>

### `DISK_STATUS_OK`

```c
#define DISK_STATUS_OK 0x00
```

```c
#include <zephyr/drivers/disk.h>
```

`disk_access_status()` 可能返回的位掩码。

磁盘状态正常（okay）。

<a id="ga533eb718a946ba60e0ad6e0e4fd4f75a"></a>

### `DISK_STATUS_UNINIT`

```c
#define DISK_STATUS_UNINIT 0x01
```

```c
#include <zephyr/drivers/disk.h>
```

磁盘状态：未初始化（Uninitialized）。

<a id="ga0a5ba8f4be6241f62a969ea56c26f7e3"></a>

### `DISK_STATUS_WR_PROTECT`

```c
#define DISK_STATUS_WR_PROTECT 0x04
```

```c
#include <zephyr/drivers/disk.h>
```

磁盘状态：写保护（Write protected）。

<a id="gaa11586a0b8ae6f2f0c142cec0df0c5fa"></a>

### `disk_access_register()`

```c
int disk_access_register ( struct disk_info * disk)
```

```c
#include <zephyr/drivers/disk.h>
```

注册磁盘。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] disk` | 指向磁盘信息结构体（disk info structure）的指针。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="gada802c6be65186009162a25f391dfb71"></a>

### `disk_access_unregister()`

```c
int disk_access_unregister ( struct disk_info * disk)
```

```c
#include <zephyr/drivers/disk.h>
```

注销磁盘。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] disk` | 指向磁盘信息结构体（disk info structure）的指针。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。


## 8.7\_原页交叉引用（Cross References）

- [设备专用磁盘访问 API 扩展（Device-specific Disk Access API extensions）](../api_topic_reference/P031_设备专用磁盘访问 API 扩展（Device-specific Disk Access API extensions）.md)
- [disk.h](../peripheral_bus_storage_header_reference/P003_zephyr__drivers__disk.h_头文件参考.md)
- [disk_info](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md)
- [disk_operations](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md)
- [disk_access_ioctl()](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ga152d85821d73644fea7ffde27b7c953c)
- [disk_access_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gac5348a854fe68a607672118c91346133)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_瑞萨 RA BSP 时钟输出分频常量（Clock Clkout Divider Constants）.md) · [返回大纲](大纲.md) · [下一章](P009_分布式交换架构（Distributed Switch Architecture，DSA）。.md)
