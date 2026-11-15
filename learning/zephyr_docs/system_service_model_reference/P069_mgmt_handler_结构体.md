---
id: learning.zephyr-docs.system-service-model-reference.page-69
title: mgmt_handler_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmgmt__handler.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_mgmt\_handler\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmgmt__handler.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单个命令ID的读取处理程序和写入处理程序（Read / Write Handler）。

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

<a id="details"></a>

单个命令 ID 对应的读取和写入处理函数。使用用户自定义载荷类型时，将 `use_custom_payload` 设为 `true`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_a7cc4917fa24afef79f1a8de8549a21e4"></a>

```c
mgmt_handler_fn mh_read
```

相关声明：[mgmt_handler_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gaaafc2c73e1616340e29df6a1ba94c241)、[mh_read](#a7cc4917fa24afef79f1a8de8549a21e4)。

读取处理函数（Read handler）。

<a id="r_a1bc6b52645f6eb1d0e0b0c695d972c15"></a>

```c
mgmt_handler_fn mh_write
```

相关声明：[mgmt_handler_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gaaafc2c73e1616340e29df6a1ba94c241)、[mh_write](#a1bc6b52645f6eb1d0e0b0c695d972c15)。

写入处理函数（Write handler）。

## 69.2\_详细说明（Detailed Documentation）

<a id="a7cc4917fa24afef79f1a8de8549a21e4"></a>

### `mh_read`

```c
mgmt_handler_fn mgmt_handler::mh_read
```

读取处理函数（Read handler）。

<a id="a1bc6b52645f6eb1d0e0b0c695d972c15"></a>

### `mh_write`

```c
mgmt_handler_fn mgmt_handler::mh_write
```

写入处理函数（Write handler）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/mgmt/mgmt.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/mgmt/mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h_source.html)
- [mgmt_handler_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gaaafc2c73e1616340e29df6a1ba94c241)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_mgmt_group_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_os_mgmt_bootloader_info_data_结构体.md)
