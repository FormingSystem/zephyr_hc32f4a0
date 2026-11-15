---
id: learning.zephyr-docs.modem-wireless-model-reference.page-55
title: modem_chat_script_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__script.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_modem\_chat\_script\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__script.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调制解调器交互脚本（Modem Chat Script）。

```c
#include <zephyr/modem/chat.h>
```

<a id="details"></a>

调制解调器交互脚本（Modem Chat Script）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_aca3b75a494273d8c06cf943153dd7dc8"></a>

```c
const char * name
```

相关声明：[name](#aca3b75a494273d8c06cf943153dd7dc8)。

脚本名称。

<a id="r_a5f329ecadd721d88e423074f00005114"></a>

```c
const struct modem_chat_script_chat * script_chats
```

相关声明：[modem_chat_script_chat](P056_modem_chat_script_chat_结构体.md)、[script_chats](#a5f329ecadd721d88e423074f00005114)。

脚本交互步骤（script chats）数组。

<a id="r_a3ac30e3ba1842cf53747721592f16cd4"></a>

```c
uint16_t script_chats_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[script_chats_size](#a3ac30e3ba1842cf53747721592f16cd4)。

脚本交互步骤数组中的元素数量。

<a id="r_a2b586e1ff80c22d8ff45829f3e2e7b17"></a>

```c
const struct modem_chat_match * abort_matches
```

相关声明：[modem_chat_match](P054_modem_chat_match_结构体.md)、[abort_matches](#a2b586e1ff80c22d8ff45829f3e2e7b17)。

中止匹配项（abort matches）数组。

<a id="r_aa56bdf520b0f385bc6410b2c6aa2e8d4"></a>

```c
uint16_t abort_matches_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[abort_matches_size](#aa56bdf520b0f385bc6410b2c6aa2e8d4)。

中止匹配项数组中的元素数量。

<a id="r_a73f4c3892052f827c10ea466c9a75954"></a>

```c
modem_chat_script_callback callback
```

相关声明：[modem_chat_script_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga1a0680c65972b58ea065b98a78095540)、[callback](#a73f4c3892052f827c10ea466c9a75954)。

脚本执行终止时调用的回调。

<a id="r_a0b9a9d3d44a8624728e16922cbdfd662"></a>

```c
uint32_t timeout
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timeout](#a0b9a9d3d44a8624728e16922cbdfd662)。

脚本必须在此超时时间内终止执行，单位为秒。

## 55.2\_详细说明（Detailed Documentation）

<a id="a2b586e1ff80c22d8ff45829f3e2e7b17"></a>

### `abort_matches`

```c
const struct modem_chat_match* modem_chat_script::abort_matches
```

中止匹配项（abort matches）数组。

<a id="aa56bdf520b0f385bc6410b2c6aa2e8d4"></a>

### `abort_matches_size`

```c
uint16_t modem_chat_script::abort_matches_size
```

中止匹配项数组中的元素数量。

<a id="a73f4c3892052f827c10ea466c9a75954"></a>

### `callback`

```c
modem_chat_script_callback modem_chat_script::callback
```

脚本执行终止时调用的回调。

<a id="aca3b75a494273d8c06cf943153dd7dc8"></a>

### `name`

```c
const char* modem_chat_script::name
```

脚本名称。

<a id="a5f329ecadd721d88e423074f00005114"></a>

### `script_chats`

```c
const struct modem_chat_script_chat* modem_chat_script::script_chats
```

脚本交互步骤（script chats）数组。

<a id="a3ac30e3ba1842cf53747721592f16cd4"></a>

### `script_chats_size`

```c
uint16_t modem_chat_script::script_chats_size
```

脚本交互步骤数组中的元素数量。

<a id="a0b9a9d3d44a8624728e16922cbdfd662"></a>

### `timeout`

```c
uint32_t modem_chat_script::timeout
```

脚本必须在此超时时间内终止执行，单位为秒。

本数据类型文档由以下文件生成：

- `zephyr/modem/chat.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/modem/chat.h](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h_source.html)
- [modem_chat_script_chat](P056_modem_chat_script_chat_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_chat_match](P054_modem_chat_match_结构体.md)
- [modem_chat_script_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga1a0680c65972b58ea065b98a78095540)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_modem_chat_match_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_modem_chat_script_chat_结构体.md)
