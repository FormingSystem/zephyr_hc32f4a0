---
id: learning.zephyr-docs.system-service-model-reference.page-26
title: enum_mgmt_detail_output_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structenum__mgmt__detail__output.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_enum\_mgmt\_detail\_output\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structenum__mgmt__detail__output.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_ENUM_MGMT_DETAILS通知回调中提供的结构。使用详情命令（Detail Command）时，每个命令组调用该回调一次，可借此在响应中返回附加信息或字段。

```c
#include <zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt_callbacks.h>
```

<a id="details"></a>

MGMT_EVT_OP_ENUM_MGMT_DETAILS通知回调中提供的结构。使用详情命令（Detail Command）时，每个命令组调用该回调一次，可借此在响应中返回附加信息或字段。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_a787c1a41fbe135b85176d3b0bb6ccd92"></a>

```c
const struct mgmt_group * group
```

相关声明：[mgmt_group](P068_mgmt_group_结构体.md)、[group](#a787c1a41fbe135b85176d3b0bb6ccd92)。

当前正在枚举的管理组（group）。

<a id="r_a140d1f5cd4e4f7a88c5a1da98a927161"></a>

```c
zcbor_state_t * zse
```

相关声明：[zse](#a140d1f5cd4e4f7a88c5a1da98a927161)。

当前用于输出组信息的 zcbor 编码器，可用它向组信息中添加额外字段。

## 26.2\_详细说明（Detailed Documentation）

<a id="a787c1a41fbe135b85176d3b0bb6ccd92"></a>

### `group`

```c
const struct mgmt_group* enum_mgmt_detail_output::group
```

当前正在枚举的管理组（group）。

<a id="a140d1f5cd4e4f7a88c5a1da98a927161"></a>

### `zse`

```c
zcbor_state_t* enum_mgmt_detail_output::zse
```

当前用于输出组信息的 zcbor 编码器，可用它向组信息中添加额外字段。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt_callbacks.h`

## 26.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_ENUM_MGMT_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__enum__mgmt.html#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf)
- [zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt__callbacks_8h_source.html)
- [mgmt_group](P068_mgmt_group_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_elf64_sym_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_flash_area_结构体.md)
