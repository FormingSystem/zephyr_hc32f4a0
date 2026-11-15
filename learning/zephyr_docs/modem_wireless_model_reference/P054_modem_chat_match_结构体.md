---
id: learning.zephyr-docs.modem-wireless-model-reference.page-54
title: modem_chat_match_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__match.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_modem\_chat\_match\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__match.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调制解调器交互匹配项（Modem Chat Match）。

```c
#include <zephyr/modem/chat.h>
```

<a id="details"></a>

调制解调器交互匹配项（Modem Chat Match）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_ad1bed20d70285a465663d9babc3fb3e2"></a>

```c
const uint8_t * match
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[match](#ad1bed20d70285a465663d9babc3fb3e2)。

匹配内容数组（Match array）。

<a id="r_a7fd423890bea11c65f326ace831233fc"></a>

```c
const uint8_t * separators
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[separators](#a7fd423890bea11c65f326ace831233fc)。

分隔字符数组（Separators array）。

<a id="r_a11f6e35cd2fd2166ac95adace6ec5c54"></a>

```c
modem_chat_match_callback callback
```

相关声明：[modem_chat_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae689e92c91d414f968267e290e5246bd)、[callback](#a11f6e35cd2fd2166ac95adace6ec5c54)。

匹配成功时执行的回调。

<a id="r_afe00a3c87a68d9f7f889f7a0d3cc4150"></a>

```c
uint8_t match_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[match_size](#afe00a3c87a68d9f7f889f7a0d3cc4150)。

匹配内容的大小。

<a id="r_a7c80555e1bf33504cef7be6c0f9db383"></a>

```c
uint8_t separators_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[separators_size](#a7c80555e1bf33504cef7be6c0f9db383)。

分隔字符数组的大小。

<a id="r_adb8c0ee17d317192432198949d116259"></a>

```c
bool wildcards
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[wildcards](#adb8c0ee17d317192432198949d116259)。

若调制解调器交互实例应在匹配时使用通配符（wildcards），则设置此项。

<a id="r_aa7f414d867fdcb2f34a9e4bd3c9b0eeb"></a>

```c
bool partial
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[partial](#aa7f414d867fdcb2f34a9e4bd3c9b0eeb)。

若匹配成功时脚本不应进入下一步，则设置此项。

## 54.2\_详细说明（Detailed Documentation）

<a id="a11f6e35cd2fd2166ac95adace6ec5c54"></a>

### `callback`

```c
modem_chat_match_callback modem_chat_match::callback
```

匹配成功时执行的回调。

<a id="ad1bed20d70285a465663d9babc3fb3e2"></a>

### `match`

```c
const uint8_t* modem_chat_match::match
```

匹配内容数组（Match array）。

<a id="afe00a3c87a68d9f7f889f7a0d3cc4150"></a>

### `match_size`

```c
uint8_t modem_chat_match::match_size
```

匹配内容的大小。

<a id="aa7f414d867fdcb2f34a9e4bd3c9b0eeb"></a>

### `partial`

```c
bool modem_chat_match::partial
```

若匹配成功时脚本不应进入下一步，则设置此项。

<a id="a7fd423890bea11c65f326ace831233fc"></a>

### `separators`

```c
const uint8_t* modem_chat_match::separators
```

分隔字符数组（Separators array）。

<a id="a7c80555e1bf33504cef7be6c0f9db383"></a>

### `separators_size`

```c
uint8_t modem_chat_match::separators_size
```

分隔字符数组的大小。

<a id="adb8c0ee17d317192432198949d116259"></a>

### `wildcards`

```c
bool modem_chat_match::wildcards
```

若调制解调器交互实例应在匹配时使用通配符（wildcards），则设置此项。

本数据类型文档由以下文件生成：

- `zephyr/modem/chat.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/modem/chat.h](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [modem_chat_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#gae689e92c91d414f968267e290e5246bd)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_modem_chat_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_modem_chat_script_结构体.md)
