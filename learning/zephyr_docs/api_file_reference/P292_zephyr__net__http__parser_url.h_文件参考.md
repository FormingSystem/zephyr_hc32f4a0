---
id: learning.zephyr-docs.api-file-reference.page-292
title: zephyr__net__http__parser_url.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/parser__url_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第292章\_zephyr\_\_net\_\_http\_\_parser\_url.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/parser__url_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <sys/types.h>
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/net/http/parser_state.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 292.1\_数据结构（Data Structures）

<a id="r_http_5Fparser_5Furl"></a>

```c
struct http_parser_url
```

相关声明：[http_parser_url](../network_application_model_reference/P034_http_parser_url_结构体.md)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 292.2\_枚举（Enumerations）

<a id="r_a9ca1f91c2958091e2ac9e9b2f903d4eb"></a>

```c
enum http_parser_url_fields { UF_SCHEMA = 0 , UF_HOST = 1 , UF_PORT = 2 , UF_PATH = 3 , UF_QUERY = 4 , UF_FRAGMENT = 5 , UF_USERINFO = 6 , UF_MAX = 7 }
```

相关声明：[http_parser_url_fields](#a9ca1f91c2958091e2ac9e9b2f903d4eb)、[UF_SCHEMA](#a9ca1f91c2958091e2ac9e9b2f903d4ebab2b8b31b30d6bc897dde653f6cc9f06c)、[UF_HOST](#a9ca1f91c2958091e2ac9e9b2f903d4ebaf2aeb0b896645bd8100ca0f1e263a12f)、[UF_PORT](#a9ca1f91c2958091e2ac9e9b2f903d4eba357b6dc1326ed55be377b0d839e8ca0f)、[UF_PATH](#a9ca1f91c2958091e2ac9e9b2f903d4eba86b9abfa220db7b834490d8b36e915af)、[UF_QUERY](#a9ca1f91c2958091e2ac9e9b2f903d4ebabc8500a49ccad1cd91d66d1eefb503cc)、[UF_FRAGMENT](#a9ca1f91c2958091e2ac9e9b2f903d4eba32fb35461b96b6872f1427b2d51d1c30)、[UF_USERINFO](#a9ca1f91c2958091e2ac9e9b2f903d4ebacb4a85c6a7d6cd0b64ec6e91e7ba8689)、[UF_MAX](#a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 292.3\_函数（Functions）

<a id="r_a9f477f452dcabd0d22f4a96ce0bfda57"></a>

```c
enum state parse_url_char (enum state s, const char ch)
```

相关声明：[state](P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[parse_url_char](#a9f477f452dcabd0d22f4a96ce0bfda57)、[state](P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

<a id="r_a64e907d36fbcc883033c6bbe5a78b1b3"></a>

```c
void http_parser_url_init (struct http_parser_url *u)
```

相关声明：[http_parser_url_init](#a64e907d36fbcc883033c6bbe5a78b1b3)、[http_parser_url](../network_application_model_reference/P034_http_parser_url_结构体.md)。

<a id="r_aeb269310a348fd68fd001b30b690fc83"></a>

```c
int http_parser_parse_url (const char *buf, size_t buflen, int is_connect, struct http_parser_url *u)
```

相关声明：[http_parser_parse_url](#aeb269310a348fd68fd001b30b690fc83)、[http_parser_url](../network_application_model_reference/P034_http_parser_url_结构体.md)。

## 292.4\_详细说明（Detailed Documentation）

<a id="a9ca1f91c2958091e2ac9e9b2f903d4eb"></a>

### `http_parser_url_fields`

```c
enum http_parser_url_fields
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UF_SCHEMA` |  |
| `UF_HOST` |  |
| `UF_PORT` |  |
| `UF_PATH` |  |
| `UF_QUERY` |  |
| `UF_FRAGMENT` |  |
| `UF_USERINFO` |  |
| `UF_MAX` |  |

<a id="aeb269310a348fd68fd001b30b690fc83"></a>

### `http_parser_parse_url()`

```c
int http_parser_parse_url ( const char * buf, size_t buflen, int is_connect, struct http_parser_url * u )
```

<a id="a64e907d36fbcc883033c6bbe5a78b1b3"></a>

### `http_parser_url_init()`

```c
void http_parser_url_init ( struct http_parser_url * u)
```

<a id="a9f477f452dcabd0d22f4a96ce0bfda57"></a>

### `parse_url_char()`

```c
enum state parse_url_char ( enum state s, const char ch )
```


## 292.5\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/net/http/parser_state.h](../api_source_runtime_reference/P047_parser_state.h_源码浏览.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/parser__url_8h_source.html)
- [http_parser_url](../network_application_model_reference/P034_http_parser_url_结构体.md)
- [state](P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a9ca1f91c2958091e2ac9e9b2f903d4ebab2b8b31b30d6bc897dde653f6cc9f06c"></a>
<a id="a9ca1f91c2958091e2ac9e9b2f903d4ebaf2aeb0b896645bd8100ca0f1e263a12f"></a>
<a id="a9ca1f91c2958091e2ac9e9b2f903d4eba357b6dc1326ed55be377b0d839e8ca0f"></a>
<a id="a9ca1f91c2958091e2ac9e9b2f903d4eba86b9abfa220db7b834490d8b36e915af"></a>
<a id="a9ca1f91c2958091e2ac9e9b2f903d4ebabc8500a49ccad1cd91d66d1eefb503cc"></a>
<a id="a9ca1f91c2958091e2ac9e9b2f903d4eba32fb35461b96b6872f1427b2d51d1c30"></a>
<a id="a9ca1f91c2958091e2ac9e9b2f903d4ebacb4a85c6a7d6cd0b64ec6e91e7ba8689"></a>
<a id="a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P291_zephyr__net__http__parser_state.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P293_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a77951.h_文件参考.md)
