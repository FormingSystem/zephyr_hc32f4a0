---
id: learning.zephyr-docs.api-file-reference.page-290
title: zephyr__net__http__parser.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第290章\_zephyr\_\_net\_\_http\_\_parser.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <sys/types.h>
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/net/http/method.h>
#include <zephyr/net/http/parser_state.h>
#include <zephyr/net/http/parser_url.h>
#include <stdbool.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 290.1\_数据结构（Data Structures）

<a id="r_http_5Fcontent_5Frange"></a>

```c
struct http_content_range
```

相关声明：[http_content_range](../network_application_model_reference/P028_http_content_range_结构体.md)。

<a id="r_http_5Fparser"></a>

```c
struct http_parser
```

相关声明：[http_parser](../network_application_model_reference/P032_http_parser_结构体.md)。

<a id="r_http_5Fparser_5Fsettings"></a>

```c
struct http_parser_settings
```

相关声明：[http_parser_settings](../network_application_model_reference/P033_http_parser_settings_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 290.2\_宏定义（Macros）

<a id="r_abfeef6f3e39791acc311791feda09d27"></a>

```c
#define HTTP_PARSER_VERSION_MAJOR 2
```

相关声明：[HTTP_PARSER_VERSION_MAJOR](#abfeef6f3e39791acc311791feda09d27)。

<a id="r_ab8479153443ca4fe95b3de5adb0224de"></a>

```c
#define HTTP_PARSER_VERSION_MINOR 7
```

相关声明：[HTTP_PARSER_VERSION_MINOR](#ab8479153443ca4fe95b3de5adb0224de)。

<a id="r_afb999672cce2ebd7f952bd3f28d8f5e5"></a>

```c
#define HTTP_PARSER_VERSION_PATCH 1
```

相关声明：[HTTP_PARSER_VERSION_PATCH](#afb999672cce2ebd7f952bd3f28d8f5e5)。

<a id="r_a356ebaa93536e6f94c2948a1416697c7"></a>

```c
#define HTTP_PARSER_ERRNO(p)
```

相关声明：[HTTP_PARSER_ERRNO](#a356ebaa93536e6f94c2948a1416697c7)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 290.3\_类型定义（Typedefs）

<a id="r_a1aab76595c275d0615cbea1cee1807c8"></a>

```c
typedef int(* http_data_cb) (struct http_parser *, const char *at, size_t length)
```

相关声明：[http_data_cb](#a1aab76595c275d0615cbea1cee1807c8)、[http_parser](../network_application_model_reference/P032_http_parser_结构体.md)。

<a id="r_aa0f8424a6e7d3dd0b2f3b6358b57f1a1"></a>

```c
typedef int(* http_cb) (struct http_parser *)
```

相关声明：[http_cb](#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)、[http_parser](../network_application_model_reference/P032_http_parser_结构体.md)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 290.4\_枚举（Enumerations）

<a id="r_af9d6d304f8c255158175951b434cfa7a"></a>

```c
enum http_parser_type { HTTP_REQUEST , HTTP_RESPONSE , HTTP_BOTH }
```

相关声明：[http_parser_type](#af9d6d304f8c255158175951b434cfa7a)、[HTTP_REQUEST](#af9d6d304f8c255158175951b434cfa7aa9f727b57e9e9c1651ee0df29aa1b1713)、[HTTP_RESPONSE](#af9d6d304f8c255158175951b434cfa7aa132597b93208763e8e81c4a4a0e8a642)、[HTTP_BOTH](#af9d6d304f8c255158175951b434cfa7aadac18fbd072752213fd5308bb5fc8684)。

<a id="r_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>

```c
enum flags { F_CHUNKED = 1 << 0 , F_CONNECTION_KEEP_ALIVE = 1 << 1 , F_CONNECTION_CLOSE = 1 << 2 , F_CONNECTION_UPGRADE = 1 << 3 , F_TRAILING = 1 << 4 , F_UPGRADE = 1 << 5 , F_SKIPBODY = 1 << 6 , F_CONTENTLENGTH = 1 << 7 }
```

相关声明：[flags](#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[F_CHUNKED](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a092619f8f7babc8fc3fa7533e78c3c29)、[F_CONNECTION_KEEP_ALIVE](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a5c5e8921e5747d1128ad9611a6d4a782)、[F_CONNECTION_CLOSE](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a133e98dc07339e6c1605f32fc4fd6c78)、[F_CONNECTION_UPGRADE](#ab6b306ef981f5e21bb41ea2c2dbe8cd9af0eea4f6920c6ff5c68cdd1f2e27d044)、[F_TRAILING](#ab6b306ef981f5e21bb41ea2c2dbe8cd9aa75b5b1dcec2decaa7386264d4e1dc29)、[F_UPGRADE](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a600ff486c803dcf2ec13453bdaf1100c)、[F_SKIPBODY](#ab6b306ef981f5e21bb41ea2c2dbe8cd9ae71592851a69f477b80b1947399c1740)、[F_CONTENTLENGTH](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a9b2f205685c9ce94d3d73148de48decb)。

<a id="r_a14687aec2341ce0e62db2e543dd1da64"></a>

```c
enum http_errno { HPE_OK , HPE_CB_message_begin , HPE_CB_url , HPE_CB_header_field , HPE_CB_header_value , HPE_CB_headers_complete , HPE_CB_body , HPE_CB_message_complete , HPE_CB_status , HPE_CB_chunk_header , HPE_CB_chunk_complete , HPE_INVALID_EOF_STATE , HPE_HEADER_OVERFLOW , HPE_CLOSED_CONNECTION , HPE_INVALID_VERSION , HPE_INVALID_STATUS , HPE_INVALID_METHOD , HPE_INVALID_URL , HPE_INVALID_HOST , HPE_INVALID_PORT , HPE_INVALID_PATH , HPE_INVALID_QUERY_STRING , HPE_INVALID_FRAGMENT , HPE_LF_EXPECTED , HPE_INVALID_HEADER_TOKEN , HPE_INVALID_CONTENT_LENGTH , HPE_UNEXPECTED_CONTENT_LENGTH , HPE_INVALID_CHUNK_SIZE , HPE_INVALID_CONTENT_RANGE , HPE_UNEXPECTED_CONTENT_RANGE , HPE_INVALID_CONSTANT , HPE_INVALID_INTERNAL_STATE , HPE_STRICT , HPE_PAUSED , HPE_UNKNOWN }
```

相关声明：[http_errno](#a14687aec2341ce0e62db2e543dd1da64)、[HPE_OK](#a14687aec2341ce0e62db2e543dd1da64adf532f653497f3085108a5e1f097aa8e)、[HPE_CB_message_begin](#a14687aec2341ce0e62db2e543dd1da64a5b44995fcd173cf38a88fc3ceaf0cb41)、[HPE_CB_url](#a14687aec2341ce0e62db2e543dd1da64ae15b73f73f8aad8c5e39d03b29414f9b)、[HPE_CB_header_field](#a14687aec2341ce0e62db2e543dd1da64ade6f685cd47ad03c836aeee97efff1ed)、[HPE_CB_header_value](#a14687aec2341ce0e62db2e543dd1da64aceed4040be7acf32b6bceb3aace8405e)、[HPE_CB_headers_complete](#a14687aec2341ce0e62db2e543dd1da64a5d82bb467f93eed296d892408c44816a)、[HPE_CB_body](#a14687aec2341ce0e62db2e543dd1da64a5dc4b0888f48cd87fc3ded374ffac8a2)、[HPE_CB_message_complete](#a14687aec2341ce0e62db2e543dd1da64ae0f56ef0ecc6638fb0594d130a1ee490)、[HPE_CB_status](#a14687aec2341ce0e62db2e543dd1da64a9adad03852eddb1f361abe9d856a1a0f)、[HPE_CB_chunk_header](#a14687aec2341ce0e62db2e543dd1da64a69ccadce5be8074b104b19aa74dce556)、[HPE_CB_chunk_complete](#a14687aec2341ce0e62db2e543dd1da64a008e232118d6133c4dbdd9770d926694)、[HPE_INVALID_EOF_STATE](#a14687aec2341ce0e62db2e543dd1da64a4103809c185fee62b11c188ff0eab39a)、[HPE_HEADER_OVERFLOW](#a14687aec2341ce0e62db2e543dd1da64a5270cdc2f8af1802ccf3a2f33fde9307)、[HPE_CLOSED_CONNECTION](#a14687aec2341ce0e62db2e543dd1da64a7fbc6a25f20237b1cc795db489312e8e)、[HPE_INVALID_VERSION](#a14687aec2341ce0e62db2e543dd1da64a5a1b7ae13c36ef37fd52b2b68112b501)、[HPE_INVALID_STATUS](#a14687aec2341ce0e62db2e543dd1da64aa4a2007f1dc03bf22aff5ca8885f6b59)、[HPE_INVALID_METHOD](#a14687aec2341ce0e62db2e543dd1da64ac031cfd48285e22ddec18964f6281f6e)、[HPE_INVALID_URL](#a14687aec2341ce0e62db2e543dd1da64ad92573bf62e7b0a13d398926a984fa9d)、[HPE_INVALID_HOST](#a14687aec2341ce0e62db2e543dd1da64a6391e880280eda55707145bda1170294)、[HPE_INVALID_PORT](#a14687aec2341ce0e62db2e543dd1da64a3e7c3b8a95f34bbd40ea047fcd43ffa5)、[HPE_INVALID_PATH](#a14687aec2341ce0e62db2e543dd1da64a69e17a8b5a35b9f93ea914224c2d4f2a)、[HPE_INVALID_QUERY_STRING](#a14687aec2341ce0e62db2e543dd1da64a383ef24f0ac59de1c128ca776d813865)、[HPE_INVALID_FRAGMENT](#a14687aec2341ce0e62db2e543dd1da64afa80e3a0c0dd1c93cf0a11cacbd59079)、[HPE_LF_EXPECTED](#a14687aec2341ce0e62db2e543dd1da64af9f23325bd502239af0326a0b407b41d)、[HPE_INVALID_HEADER_TOKEN](#a14687aec2341ce0e62db2e543dd1da64ac0348f1ca04bf4d882affcd0249336b5)、[HPE_INVALID_CONTENT_LENGTH](#a14687aec2341ce0e62db2e543dd1da64a18b873c41a1d7aa9ee9486f719aa7509)、[HPE_UNEXPECTED_CONTENT_LENGTH](#a14687aec2341ce0e62db2e543dd1da64a2406df24d500b1228fc5ef4a8d60e7c3)、[HPE_INVALID_CHUNK_SIZE](#a14687aec2341ce0e62db2e543dd1da64a36842cc306c491da8c42023be68585e9)、[HPE_INVALID_CONTENT_RANGE](#a14687aec2341ce0e62db2e543dd1da64ab725a62450a5246e98fb5deeb0a250b5)、[HPE_UNEXPECTED_CONTENT_RANGE](#a14687aec2341ce0e62db2e543dd1da64af880c7a160717f01bba7bb98169c5011)、[HPE_INVALID_CONSTANT](#a14687aec2341ce0e62db2e543dd1da64a1b9ec4aeef6f168f9d711c27a0c6faa8)、[HPE_INVALID_INTERNAL_STATE](#a14687aec2341ce0e62db2e543dd1da64abb98b653c0972e3e22bc5ff8b57d0d55)、[HPE_STRICT](#a14687aec2341ce0e62db2e543dd1da64a7f92de0f01b2d0e37209854069183f16)、[HPE_PAUSED](#a14687aec2341ce0e62db2e543dd1da64aed64f2a65634183e8f708ac80af3f6f2)、[HPE_UNKNOWN](#a14687aec2341ce0e62db2e543dd1da64a36cb81d8c40b00602b558f82a38eaecc)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 290.5\_函数（Functions）

<a id="r_a2559b4d373c7f0d85c77a2a3c308a5ee"></a>

```c
unsigned long http_parser_version (void)
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[http_parser_version](#a2559b4d373c7f0d85c77a2a3c308a5ee)。

<a id="r_ab8ae8e721c5c9f7309e94c174c72a940"></a>

```c
void http_parser_init (struct http_parser *parser, enum http_parser_type type)
```

相关声明：[http_parser_init](#ab8ae8e721c5c9f7309e94c174c72a940)、[http_parser](../network_application_model_reference/P032_http_parser_结构体.md)、[http_parser_type](#af9d6d304f8c255158175951b434cfa7a)。

<a id="r_a76d2e1f7225617f6941042fc95d888fe"></a>

```c
void http_parser_settings_init (struct http_parser_settings *settings)
```

相关声明：[http_parser_settings_init](#a76d2e1f7225617f6941042fc95d888fe)、[http_parser_settings](../network_application_model_reference/P033_http_parser_settings_结构体.md)。

<a id="r_a54f1346f15b326f6308a3ff7f0f75b52"></a>

```c
size_t http_parser_execute (struct http_parser *parser, const struct http_parser_settings *settings, const char *data, size_t len)
```

相关声明：[http_parser_execute](#a54f1346f15b326f6308a3ff7f0f75b52)、[http_parser](../network_application_model_reference/P032_http_parser_结构体.md)、[http_parser_settings](../network_application_model_reference/P033_http_parser_settings_结构体.md)。

<a id="r_a903c39c3abea292860780856ba90d560"></a>

```c
int http_should_keep_alive (const struct http_parser *parser)
```

相关声明：[http_should_keep_alive](#a903c39c3abea292860780856ba90d560)、[http_parser](../network_application_model_reference/P032_http_parser_结构体.md)。

<a id="r_abb207665b6ff41700e5bbb260b580cb6"></a>

```c
const char * http_method_str (enum http_method m)
```

相关声明：[http_method_str](#abb207665b6ff41700e5bbb260b580cb6)、[http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)。

<a id="r_acce1b9056442d75d4d609e797bcce2fd"></a>

```c
const char * http_errno_name (enum http_errno err)
```

相关声明：[http_errno_name](#acce1b9056442d75d4d609e797bcce2fd)、[http_errno](#a14687aec2341ce0e62db2e543dd1da64)。

<a id="r_a88adfab20d97366aac1fe05aa7dde7da"></a>

```c
const char * http_errno_description (enum http_errno err)
```

相关声明：[http_errno_description](#a88adfab20d97366aac1fe05aa7dde7da)、[http_errno](#a14687aec2341ce0e62db2e543dd1da64)。

<a id="r_aa3764343ba4d2bb13fe39b05425633ba"></a>

```c
void http_parser_pause (struct http_parser *parser, int paused)
```

相关声明：[http_parser_pause](#aa3764343ba4d2bb13fe39b05425633ba)、[http_parser](../network_application_model_reference/P032_http_parser_结构体.md)。

<a id="r_a5156a631a251516a6e78b17e1faadbb2"></a>

```c
int http_body_is_final (const struct http_parser *parser)
```

相关声明：[http_body_is_final](#a5156a631a251516a6e78b17e1faadbb2)、[http_parser](../network_application_model_reference/P032_http_parser_结构体.md)。

## 290.6\_详细说明（Detailed Documentation）

<a id="a356ebaa93536e6f94c2948a1416697c7"></a>

### `HTTP_PARSER_ERRNO`

```c
#define HTTP_PARSER_ERRNO ( p)
```

展开值（Value）：

```c
((enum http_errno) (p)->http_errno)
```

<a id="abfeef6f3e39791acc311791feda09d27"></a>

### `HTTP_PARSER_VERSION_MAJOR`

```c
#define HTTP_PARSER_VERSION_MAJOR 2
```

<a id="ab8479153443ca4fe95b3de5adb0224de"></a>

### `HTTP_PARSER_VERSION_MINOR`

```c
#define HTTP_PARSER_VERSION_MINOR 7
```

<a id="afb999672cce2ebd7f952bd3f28d8f5e5"></a>

### `HTTP_PARSER_VERSION_PATCH`

```c
#define HTTP_PARSER_VERSION_PATCH 1
```

<a id="aa0f8424a6e7d3dd0b2f3b6358b57f1a1"></a>

### `http_cb`

```c
typedef int(* http_cb) (struct http_parser *)
```

<a id="a1aab76595c275d0615cbea1cee1807c8"></a>

### `http_data_cb`

```c
typedef int(* http_data_cb) (struct http_parser *, const char *at, size_t length)
```

<a id="ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>

### `flags`

```c
enum flags
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `F_CHUNKED` |  |
| `F_CONNECTION_KEEP_ALIVE` |  |
| `F_CONNECTION_CLOSE` |  |
| `F_CONNECTION_UPGRADE` |  |
| `F_TRAILING` |  |
| `F_UPGRADE` |  |
| `F_SKIPBODY` |  |
| `F_CONTENTLENGTH` |  |

<a id="a14687aec2341ce0e62db2e543dd1da64"></a>

### `http_errno`

```c
enum http_errno
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HPE_OK` |  |
| `HPE_CB_message_begin` |  |
| `HPE_CB_url` |  |
| `HPE_CB_header_field` |  |
| `HPE_CB_header_value` |  |
| `HPE_CB_headers_complete` |  |
| `HPE_CB_body` |  |
| `HPE_CB_message_complete` |  |
| `HPE_CB_status` |  |
| `HPE_CB_chunk_header` |  |
| `HPE_CB_chunk_complete` |  |
| `HPE_INVALID_EOF_STATE` |  |
| `HPE_HEADER_OVERFLOW` |  |
| `HPE_CLOSED_CONNECTION` |  |
| `HPE_INVALID_VERSION` |  |
| `HPE_INVALID_STATUS` |  |
| `HPE_INVALID_METHOD` |  |
| `HPE_INVALID_URL` |  |
| `HPE_INVALID_HOST` |  |
| `HPE_INVALID_PORT` |  |
| `HPE_INVALID_PATH` |  |
| `HPE_INVALID_QUERY_STRING` |  |
| `HPE_INVALID_FRAGMENT` |  |
| `HPE_LF_EXPECTED` |  |
| `HPE_INVALID_HEADER_TOKEN` |  |
| `HPE_INVALID_CONTENT_LENGTH` |  |
| `HPE_UNEXPECTED_CONTENT_LENGTH` |  |
| `HPE_INVALID_CHUNK_SIZE` |  |
| `HPE_INVALID_CONTENT_RANGE` |  |
| `HPE_UNEXPECTED_CONTENT_RANGE` |  |
| `HPE_INVALID_CONSTANT` |  |
| `HPE_INVALID_INTERNAL_STATE` |  |
| `HPE_STRICT` |  |
| `HPE_PAUSED` |  |
| `HPE_UNKNOWN` |  |

<a id="af9d6d304f8c255158175951b434cfa7a"></a>

### `http_parser_type`

```c
enum http_parser_type
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_REQUEST` |  |
| `HTTP_RESPONSE` |  |
| `HTTP_BOTH` |  |

<a id="a5156a631a251516a6e78b17e1faadbb2"></a>

### `http_body_is_final()`

```c
int http_body_is_final ( const struct http_parser * parser)
```

<a id="a88adfab20d97366aac1fe05aa7dde7da"></a>

### `http_errno_description()`

```c
const char * http_errno_description ( enum http_errno err)
```

<a id="acce1b9056442d75d4d609e797bcce2fd"></a>

### `http_errno_name()`

```c
const char * http_errno_name ( enum http_errno err)
```

<a id="abb207665b6ff41700e5bbb260b580cb6"></a>

### `http_method_str()`

```c
const char * http_method_str ( enum http_method m)
```

<a id="a54f1346f15b326f6308a3ff7f0f75b52"></a>

### `http_parser_execute()`

```c
size_t http_parser_execute ( struct http_parser * parser, const struct http_parser_settings * settings, const char * data, size_t len )
```

<a id="ab8ae8e721c5c9f7309e94c174c72a940"></a>

### `http_parser_init()`

```c
void http_parser_init ( struct http_parser * parser, enum http_parser_type type )
```

<a id="aa3764343ba4d2bb13fe39b05425633ba"></a>

### `http_parser_pause()`

```c
void http_parser_pause ( struct http_parser * parser, int paused )
```

<a id="a76d2e1f7225617f6941042fc95d888fe"></a>

### `http_parser_settings_init()`

```c
void http_parser_settings_init ( struct http_parser_settings * settings)
```

<a id="a2559b4d373c7f0d85c77a2a3c308a5ee"></a>

### `http_parser_version()`

```c
unsigned long http_parser_version ( void )
```

<a id="a903c39c3abea292860780856ba90d560"></a>

### `http_should_keep_alive()`

```c
int http_should_keep_alive ( const struct http_parser * parser)
```


## 290.7\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/net/http/method.h](../api_source_supplement_reference/P111_method.h_源码浏览.md)
- [zephyr/net/http/parser_state.h](../api_source_runtime_reference/P047_parser_state.h_源码浏览.md)
- [zephyr/net/http/parser_url.h](https://docs.zephyrproject.org/latest/doxygen/html/parser__url_8h_source.html)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h_source.html)
- [http_content_range](../network_application_model_reference/P028_http_content_range_结构体.md)
- [http_parser](../network_application_model_reference/P032_http_parser_结构体.md)
- [http_parser_settings](../network_application_model_reference/P033_http_parser_settings_结构体.md)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aparser_8h_html_a14687aec2341ce0e62db2e543dd1da64"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ab6b306ef981f5e21bb41ea2c2dbe8cd9a092619f8f7babc8fc3fa7533e78c3c29"></a>
<a id="ab6b306ef981f5e21bb41ea2c2dbe8cd9a5c5e8921e5747d1128ad9611a6d4a782"></a>
<a id="ab6b306ef981f5e21bb41ea2c2dbe8cd9a133e98dc07339e6c1605f32fc4fd6c78"></a>
<a id="ab6b306ef981f5e21bb41ea2c2dbe8cd9af0eea4f6920c6ff5c68cdd1f2e27d044"></a>
<a id="ab6b306ef981f5e21bb41ea2c2dbe8cd9aa75b5b1dcec2decaa7386264d4e1dc29"></a>
<a id="ab6b306ef981f5e21bb41ea2c2dbe8cd9a600ff486c803dcf2ec13453bdaf1100c"></a>
<a id="ab6b306ef981f5e21bb41ea2c2dbe8cd9ae71592851a69f477b80b1947399c1740"></a>
<a id="ab6b306ef981f5e21bb41ea2c2dbe8cd9a9b2f205685c9ce94d3d73148de48decb"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64adf532f653497f3085108a5e1f097aa8e"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a5b44995fcd173cf38a88fc3ceaf0cb41"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64ae15b73f73f8aad8c5e39d03b29414f9b"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64ade6f685cd47ad03c836aeee97efff1ed"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64aceed4040be7acf32b6bceb3aace8405e"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a5d82bb467f93eed296d892408c44816a"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a5dc4b0888f48cd87fc3ded374ffac8a2"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64ae0f56ef0ecc6638fb0594d130a1ee490"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a9adad03852eddb1f361abe9d856a1a0f"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a69ccadce5be8074b104b19aa74dce556"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a008e232118d6133c4dbdd9770d926694"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a4103809c185fee62b11c188ff0eab39a"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a5270cdc2f8af1802ccf3a2f33fde9307"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a7fbc6a25f20237b1cc795db489312e8e"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a5a1b7ae13c36ef37fd52b2b68112b501"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64aa4a2007f1dc03bf22aff5ca8885f6b59"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64ac031cfd48285e22ddec18964f6281f6e"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64ad92573bf62e7b0a13d398926a984fa9d"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a6391e880280eda55707145bda1170294"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a3e7c3b8a95f34bbd40ea047fcd43ffa5"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a69e17a8b5a35b9f93ea914224c2d4f2a"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a383ef24f0ac59de1c128ca776d813865"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64afa80e3a0c0dd1c93cf0a11cacbd59079"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64af9f23325bd502239af0326a0b407b41d"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64ac0348f1ca04bf4d882affcd0249336b5"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a18b873c41a1d7aa9ee9486f719aa7509"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a2406df24d500b1228fc5ef4a8d60e7c3"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a36842cc306c491da8c42023be68585e9"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64ab725a62450a5246e98fb5deeb0a250b5"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64af880c7a160717f01bba7bb98169c5011"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a1b9ec4aeef6f168f9d711c27a0c6faa8"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64abb98b653c0972e3e22bc5ff8b57d0d55"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a7f92de0f01b2d0e37209854069183f16"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64aed64f2a65634183e8f708ac80af3f6f2"></a>
<a id="a14687aec2341ce0e62db2e543dd1da64a36cb81d8c40b00602b558f82a38eaecc"></a>
<a id="af9d6d304f8c255158175951b434cfa7aa9f727b57e9e9c1651ee0df29aa1b1713"></a>
<a id="af9d6d304f8c255158175951b434cfa7aa132597b93208763e8e81c4a4a0e8a642"></a>
<a id="af9d6d304f8c255158175951b434cfa7aadac18fbd072752213fd5308bb5fc8684"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P289_zephyr__posix__netpacket__packet.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P291_zephyr__net__http__parser_state.h_文件参考.md)
