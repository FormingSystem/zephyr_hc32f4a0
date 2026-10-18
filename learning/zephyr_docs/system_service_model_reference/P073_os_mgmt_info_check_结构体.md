---
id: learning.zephyr-docs.system-service-model-reference.page-73
title: os_mgmt_info_check_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__info__check.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_os\_mgmt\_info\_check\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__info__check.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_OS_MGMT_INFO_CHECK通知回调中提供的结构。

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

<a id="details"></a>

MGMT_EVT_OP_OS_MGMT_INFO_CHECK通知回调中提供的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 73.1\_数据成员（Data Fields）

<a id="r_aa5da5de4bfd4f9f54319458c3c8a5fbb"></a>

```c
struct zcbor_string * format
```

相关声明：[format](#aa5da5de4bfd4f9f54319458c3c8a5fbb)。

来自 mcumgr 客户端的输入格式字符串。

<a id="r_a068e3425bf3a12b043f26b0d6dd07267"></a>

```c
uint32_t * format_bitmask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[format_bitmask](#a068e3425bf3a12b043f26b0d6dd07267)。

指定应包含哪些输出值的位掩码。

<a id="r_a7aae2f1feb1adfdc18f11a671c3bad26"></a>

```c
uint16_t * valid_formats
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[valid_formats](#a7aae2f1feb1adfdc18f11a671c3bad26)。

已解析的有效格式字符数量；每解析一个有效字符，都必须递增 1。

<a id="r_a09c4371a4bfa20192411fff922747a2c"></a>

```c
bool * custom_os_name
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[custom_os_name](#a09c4371a4bfa20192411fff922747a2c)。

如果操作系统名称由外部代码提供，需要设为 `true`。

## 73.2\_详细说明（Detailed Documentation）

<a id="a09c4371a4bfa20192411fff922747a2c"></a>

### `custom_os_name`

```c
bool* os_mgmt_info_check::custom_os_name
```

如果操作系统名称由外部代码提供，需要设为 `true`。

<a id="aa5da5de4bfd4f9f54319458c3c8a5fbb"></a>

### `format`

```c
struct zcbor_string* os_mgmt_info_check::format
```

来自 mcumgr 客户端的输入格式字符串。

<a id="a068e3425bf3a12b043f26b0d6dd07267"></a>

### `format_bitmask`

```c
uint32_t* os_mgmt_info_check::format_bitmask
```

指定应包含哪些输出值的位掩码。

<a id="a7aae2f1feb1adfdc18f11a671c3bad26"></a>

### `valid_formats`

```c
uint16_t* os_mgmt_info_check::valid_formats
```

已解析的有效格式字符数量；每解析一个有效字符，都必须递增 1。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h`

## 73.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_OS_MGMT_INFO_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5)
- [zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P072_os_mgmt_info_append_结构体.md) · [返回大纲](大纲.md) · [下一章](P074_os_mgmt_reset_data_结构体.md)
