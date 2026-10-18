---
id: learning.zephyr-docs.system-service-model-reference.page-49
title: img_mgmt_upload_action_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__upload__action.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_img\_mgmt\_upload\_action\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__upload__action.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述处理上传请求（Upload Request）时要执行的操作。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

<a id="details"></a>

描述处理上传请求（Upload Request）时要执行的操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_a4b1d3625ade4e4392094ace41ec4aa01"></a>

```c
unsigned long long size
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[size](#a4b1d3625ade4e4392094ace41ec4aa01)。

映像的总大小。

<a id="r_aac493000e6989735531492f15edb6108"></a>

```c
int write_bytes
```

相关声明：[write_bytes](#aac493000e6989735531492f15edb6108)。

要写入 Flash 的映像字节数。

<a id="r_a6c9248e3c21325ed99ff8cf765f3ac82"></a>

```c
int area_id
```

相关声明：[area_id](#a6c9248e3c21325ed99ff8cf765f3ac82)。

要写入的 Flash 区域。

<a id="r_a7661db4343ebf6f7d040e3e87d3611aa"></a>

```c
bool proceed
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[proceed](#a7661db4343ebf6f7d040e3e87d3611aa)。

是否处理请求；偏移量不正确时为 `false`。

<a id="r_abe9c3503c6d58cf3b7ad637cd4fec852"></a>

```c
bool erase
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[erase](#abe9c3503c6d58cf3b7ad637cd4fec852)。

是否擦除目标 Flash 区域。

## 49.2\_详细说明（Detailed Documentation）

<a id="a6c9248e3c21325ed99ff8cf765f3ac82"></a>

### `area_id`

```c
int img_mgmt_upload_action::area_id
```

要写入的 Flash 区域。

<a id="abe9c3503c6d58cf3b7ad637cd4fec852"></a>

### `erase`

```c
bool img_mgmt_upload_action::erase
```

是否擦除目标 Flash 区域。

<a id="a7661db4343ebf6f7d040e3e87d3611aa"></a>

### `proceed`

```c
bool img_mgmt_upload_action::proceed
```

是否处理请求；偏移量不正确时为 `false`。

<a id="a4b1d3625ade4e4392094ace41ec4aa01"></a>

### `size`

```c
unsigned long long img_mgmt_upload_action::size
```

映像的总大小。

<a id="aac493000e6989735531492f15edb6108"></a>

### `write_bytes`

```c
int img_mgmt_upload_action::write_bytes
```

要写入 Flash 的映像字节数。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_img_mgmt_state_slot_encode_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_img_mgmt_upload_check_结构体.md)
