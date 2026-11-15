---
id: learning.zephyr-docs.network-service-model-reference.page-29
title: loopback_disk_access_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structloopback__disk__access.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_loopback\_disk\_access\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structloopback__disk__access.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

活动回环磁盘设备（Loopback Disk Device）的上下文对象。

```c
#include <zephyr/drivers/loopback_disk.h>
```

<a id="details"></a>

活动回环磁盘设备（Loopback Disk Device）的上下文对象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_a958b6ae459ade33487c01fa5e60c31b3"></a>

```c
struct disk_info info
```

相关声明：[disk_info](https://docs.zephyrproject.org/latest/doxygen/html/structdisk__info.html)、[info](#a958b6ae459ade33487c01fa5e60c31b3)。

<a id="r_ae34d1252cb853510aef1c173bb540fb2"></a>

```c
const char * file_path
```

相关声明：[file_path](#ae34d1252cb853510aef1c173bb540fb2)。

<a id="r_ae290129bd48f42de5acd28876af95c3e"></a>

```c
struct fs_file_t file
```

相关声明：[fs_file_t](../storage/P038_文件系统文件对象.md)、[file](#ae290129bd48f42de5acd28876af95c3e)。

<a id="r_a3e71921671d406734dd0125e3478abc2"></a>

```c
size_t num_sectors
```

相关声明：[num_sectors](#a3e71921671d406734dd0125e3478abc2)。

## 29.2\_详细说明（Detailed Documentation）

<a id="ae290129bd48f42de5acd28876af95c3e"></a>

### `file`

```c
struct fs_file_t loopback_disk_access::file
```

<a id="ae34d1252cb853510aef1c173bb540fb2"></a>

### `file_path`

```c
const char* loopback_disk_access::file_path
```

<a id="a958b6ae459ade33487c01fa5e60c31b3"></a>

### `info`

```c
struct disk_info loopback_disk_access::info
```

<a id="a3e71921671d406734dd0125e3478abc2"></a>

### `num_sectors`

```c
size_t loopback_disk_access::num_sectors
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/loopback_disk.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/drivers/loopback_disk.h](https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h_source.html)
- [disk_info](https://docs.zephyrproject.org/latest/doxygen/html/structdisk__info.html)
- [fs_file_t](../storage/P038_文件系统文件对象.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_lcp_options_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_mdio_driver_api_结构体.md)
