---
id: learning.zephyr-docs.api-file-system-power-reference.page-25
title: zephyr__drivers__loopback_disk.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_drivers\_\_loopback\_disk.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/disk.h>
#include <zephyr/fs/fs_interface.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.1\_数据结构（Data Structures）

<a id="r_loopback_5Fdisk_5Faccess"></a>

```c
struct loopback_disk_access
```

相关声明：[loopback_disk_access](../network_service_model_reference/P029_loopback_disk_access_结构体.md)。

活动回环磁盘设备（Loopback Disk Device）的上下文对象。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.2\_函数（Functions）

<a id="r_a17a5f2ad1706fd7c3a8dcdbda2753b9c"></a>

```c
int loopback_disk_access_register (struct loopback_disk_access *ctx, const char *file_path, const char *disk_access_name)
```

相关声明：[loopback_disk_access_register](#a17a5f2ad1706fd7c3a8dcdbda2753b9c)、[loopback_disk_access](../network_service_model_reference/P029_loopback_disk_access_结构体.md)。

注册回环磁盘设备（Loopback Disk Device）。

<a id="r_af3dca356272ee28c2865592d73d2563d"></a>

```c
int loopback_disk_access_unregister (struct loopback_disk_access *ctx)
```

相关声明：[loopback_disk_access_unregister](#af3dca356272ee28c2865592d73d2563d)、[loopback_disk_access](../network_service_model_reference/P029_loopback_disk_access_结构体.md)。

注销此前注册的回环磁盘设备（Loopback Disk Device）。

## 25.3\_详细说明（Detailed Documentation）

<a id="a17a5f2ad1706fd7c3a8dcdbda2753b9c"></a>

### `loopback_disk_access_register()`

```c
int loopback_disk_access_register ( struct loopback_disk_access * ctx, const char * file_path, const char * disk_access_name )
```

注册回环磁盘设备（Loopback Disk Device）。

注册一个新的回环磁盘设备（Loopback Disk Device），由指定路径的文件提供后端存储（Backing File）。

所有参数（`ctx`、`file_path` 和 `disk_access_name`）指向的数据，都必须持续有效直到注销该磁盘访问（Disk Access）。`file_path` 和 `disk_access_name` 若为字符串字面量（String Literals），自然满足此要求；但对 `ctx`，以及动态构造的 `file_path`、`disk_access_name`，必须特别注意其生命周期。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 预先分配的上下文结构体（Preallocated Context Structure）。 |
| `file_path` | 后端存储文件路径（Path to Backing File）。 |
| `disk_access_name` | 创建的磁盘访问名称（Disk Access Name），供 `disk_access_*()` 函数使用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时（On Success）； |
| `<0` | 负 `errno` 错误码，具体取决于后端存储文件（Backing File）的文件系统。 |

<a id="af3dca356272ee28c2865592d73d2563d"></a>

### `loopback_disk_access_unregister()`

```c
int loopback_disk_access_unregister ( struct loopback_disk_access * ctx)
```

注销此前注册的回环磁盘设备（Loopback Disk Device）。

清理磁盘访问（Disk Access）使用的资源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 此前传递给一次成功的 `loopback_disk_access_register()` 调用的上下文结构体（Context Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时（On Success）； |
| `<0` | 负 `errno` 错误码，具体取决于后端存储文件（Backing File）的文件系统。 |


## 25.4\_原页交叉引用（Cross References）

- [zephyr/drivers/disk.h](../peripheral_bus_storage_source_reference/P003_zephyr__drivers__disk.h_头文件源码.md)
- [zephyr/fs/fs_interface.h](../api_source_system_reference/P012_fs_interface.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P450_loopback_disk.h_源码浏览.md)
- [loopback_disk_access](../network_service_model_reference/P029_loopback_disk_access_结构体.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P024_zephyr__drivers__interrupt_controller__loapic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__dt-bindings__clock__mchp_pic32cm_jh_clock.h_文件参考.md)
