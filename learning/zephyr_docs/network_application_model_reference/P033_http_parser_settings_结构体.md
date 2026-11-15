---
id: learning.zephyr-docs.network-application-model-reference.page-33
title: http_parser_settings_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__parser__settings.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_http\_parser\_settings\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__parser__settings.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/net/http/parser.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_ac44144daecc8e8adbd477b7e6a794e26"></a>

```c
http_cb on_message_begin
```

相关声明：[http_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)、[on_message_begin](#ac44144daecc8e8adbd477b7e6a794e26)。

<a id="r_a9c24dfa900b49bf3439bbfba572b42fb"></a>

```c
http_data_cb on_url
```

相关声明：[http_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#a1aab76595c275d0615cbea1cee1807c8)、[on_url](#a9c24dfa900b49bf3439bbfba572b42fb)。

<a id="r_a6d0f0203f3461a8889ad471de119c993"></a>

```c
http_data_cb on_status
```

相关声明：[http_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#a1aab76595c275d0615cbea1cee1807c8)、[on_status](#a6d0f0203f3461a8889ad471de119c993)。

<a id="r_acfb3fd7947c5ff3e16649c71aa13bff2"></a>

```c
http_data_cb on_header_field
```

相关声明：[http_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#a1aab76595c275d0615cbea1cee1807c8)、[on_header_field](#acfb3fd7947c5ff3e16649c71aa13bff2)。

<a id="r_a2af4e9085fa79ee52b31e626179bc561"></a>

```c
http_data_cb on_header_value
```

相关声明：[http_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#a1aab76595c275d0615cbea1cee1807c8)、[on_header_value](#a2af4e9085fa79ee52b31e626179bc561)。

<a id="r_a743b24c8f33e0f1cf60a96c824c42071"></a>

```c
http_cb on_headers_complete
```

相关声明：[http_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)、[on_headers_complete](#a743b24c8f33e0f1cf60a96c824c42071)。

<a id="r_aaa145d7c24c91f471b2079ecb6368ae4"></a>

```c
http_data_cb on_body
```

相关声明：[http_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#a1aab76595c275d0615cbea1cee1807c8)、[on_body](#aaa145d7c24c91f471b2079ecb6368ae4)。

<a id="r_afdd5beef93a4a7b32bc61ae088da64d2"></a>

```c
http_cb on_message_complete
```

相关声明：[http_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)、[on_message_complete](#afdd5beef93a4a7b32bc61ae088da64d2)。

<a id="r_a497cf8f9d68e06e54684b71ee0f9f828"></a>

```c
http_cb on_chunk_header
```

相关声明：[http_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)、[on_chunk_header](#a497cf8f9d68e06e54684b71ee0f9f828)。

<a id="r_ac1c8453573094795ef41d4ba26e78846"></a>

```c
http_cb on_chunk_complete
```

相关声明：[http_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)、[on_chunk_complete](#ac1c8453573094795ef41d4ba26e78846)。

## 33.2\_详细说明（Detailed Documentation）

<a id="aaa145d7c24c91f471b2079ecb6368ae4"></a>

### `on_body`

```c
http_data_cb http_parser_settings::on_body
```

<a id="ac1c8453573094795ef41d4ba26e78846"></a>

### `on_chunk_complete`

```c
http_cb http_parser_settings::on_chunk_complete
```

<a id="a497cf8f9d68e06e54684b71ee0f9f828"></a>

### `on_chunk_header`

```c
http_cb http_parser_settings::on_chunk_header
```

<a id="acfb3fd7947c5ff3e16649c71aa13bff2"></a>

### `on_header_field`

```c
http_data_cb http_parser_settings::on_header_field
```

<a id="a2af4e9085fa79ee52b31e626179bc561"></a>

### `on_header_value`

```c
http_data_cb http_parser_settings::on_header_value
```

<a id="a743b24c8f33e0f1cf60a96c824c42071"></a>

### `on_headers_complete`

```c
http_cb http_parser_settings::on_headers_complete
```

<a id="ac44144daecc8e8adbd477b7e6a794e26"></a>

### `on_message_begin`

```c
http_cb http_parser_settings::on_message_begin
```

<a id="afdd5beef93a4a7b32bc61ae088da64d2"></a>

### `on_message_complete`

```c
http_cb http_parser_settings::on_message_complete
```

<a id="a6d0f0203f3461a8889ad471de119c993"></a>

### `on_status`

```c
http_data_cb http_parser_settings::on_status
```

<a id="a9c24dfa900b49bf3439bbfba572b42fb"></a>

### `on_url`

```c
http_data_cb http_parser_settings::on_url
```

本数据类型文档由以下文件生成：

- `zephyr/net/http/parser.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/net/http/parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h_source.html)
- [http_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)
- [http_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#a1aab76595c275d0615cbea1cee1807c8)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_http_parser_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_http_parser_url_结构体.md)
