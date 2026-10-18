---
id: learning.zephyr-docs.system-service-model-reference.page-72
title: os_mgmt_info_append_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__info__append.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_os\_mgmt\_info\_append\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__info__append.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_OS_MGMT_INFO_APPEND通知回调中提供的结构。

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h>
```

<a id="details"></a>

MGMT_EVT_OP_OS_MGMT_INFO_APPEND通知回调中提供的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_a6c43c79ab799b7b585453ead48f3c1a3"></a>

```c
uint32_t * format_bitmask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[format_bitmask](#a6c43c79ab799b7b585453ead48f3c1a3)。

来自已处理命令的格式位掩码；相应位在处理后应清除。注意，如果指定了 `all_format_specified`，此处的对应位不会置位。

<a id="r_abf016939fbc1d0aaba9712dfacf2d04f"></a>

```c
bool all_format_specified
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[all_format_specified](#abf016939fbc1d0aaba9712dfacf2d04f)。

如果提供了表示全部内容的 `a` 指定符，则为 `true`。

<a id="r_a1fb38ad80f92519c649aab7ef258095b"></a>

```c
uint8_t * output
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[output](#a1fb38ad80f92519c649aab7ef258095b)。

应向其中追加响应的输出缓冲区。

<a id="r_acd3e277aef6b3bc69346996c073f993b"></a>

```c
uint16_t * output_length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[output_length](#acd3e277aef6b3bc69346996c073f993b)。

输出缓冲区中响应的当前大小；追加数据后必须更新为追加后的响应大小。

<a id="r_ae96963a00ef4b15099cf36399a159382"></a>

```c
uint16_t buffer_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[buffer_size](#ae96963a00ef4b15099cf36399a159382)。

输出缓冲区的大小，包含空字符终止符。如果输出响应会超过此大小，函数必须中止并返回 `false`，以向客户端报告内存错误。

<a id="r_acc89541b668ff791a1927c549d36b1b2"></a>

```c
bool * prior_output
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[prior_output](#acc89541b668ff791a1927c549d36b1b2)。

指示此前是否已有输出；如果已经输出响应，必须设为 `true`。

## 72.2\_详细说明（Detailed Documentation）

<a id="abf016939fbc1d0aaba9712dfacf2d04f"></a>

### `all_format_specified`

```c
bool os_mgmt_info_append::all_format_specified
```

如果提供了表示全部内容的 `a` 指定符，则为 `true`。

<a id="ae96963a00ef4b15099cf36399a159382"></a>

### `buffer_size`

```c
uint16_t os_mgmt_info_append::buffer_size
```

输出缓冲区的大小，包含空字符终止符。如果输出响应会超过此大小，函数必须中止并返回 `false`，以向客户端报告内存错误。

<a id="a6c43c79ab799b7b585453ead48f3c1a3"></a>

### `format_bitmask`

```c
uint32_t* os_mgmt_info_append::format_bitmask
```

来自已处理命令的格式位掩码；相应位在处理后应清除。注意，如果指定了 `all_format_specified`，此处的对应位不会置位。

<a id="a1fb38ad80f92519c649aab7ef258095b"></a>

### `output`

```c
uint8_t* os_mgmt_info_append::output
```

应向其中追加响应的输出缓冲区。

如果 `prior_output` 为 `true`，必须在输出响应前添加一个空格。

<a id="acd3e277aef6b3bc69346996c073f993b"></a>

### `output_length`

```c
uint16_t* os_mgmt_info_append::output_length
```

输出缓冲区中响应的当前大小；追加数据后必须更新为追加后的响应大小。

<a id="acc89541b668ff791a1927c549d36b1b2"></a>

### `prior_output`

```c
bool* os_mgmt_info_append::prior_output
```

指示此前是否已有输出；如果已经输出响应，必须设为 `true`。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_os_mgmt_client_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_os_mgmt_info_check_结构体.md)
