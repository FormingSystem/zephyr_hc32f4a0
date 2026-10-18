---
id: learning.zephyr-docs.modem-wireless-model-reference.page-56
title: modem_chat_script_chat_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__script__chat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_modem\_chat\_script\_chat\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__script__chat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调制解调器交互脚本中的交互项（Modem Chat Script Chat）。

```c
#include <zephyr/modem/chat.h>
```

<a id="details"></a>

调制解调器交互脚本中的交互项（Modem Chat Script Chat）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_a92c038d56623b4f4b26c64b537e7ce8a"></a>

```c
const uint8_t * request
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[request](#a92c038d56623b4f4b26c64b537e7ce8a)。

要发送给调制解调器的请求。

<a id="r_ad87948ff4e6441c118ee269bf6458aa0"></a>

```c
uint16_t request_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[request_size](#ad87948ff4e6441c118ee269bf6458aa0)。

请求大小。

<a id="r_a5cab9c3a31624c8ffb490b70285f86ee"></a>

```c
const struct modem_chat_match * response_matches
```

相关声明：[modem_chat_match](P054_modem_chat_match_结构体.md)、[response_matches](#a5cab9c3a31624c8ffb490b70285f86ee)。

此请求的预期响应。

<a id="r_afaaa9a7bc1842dfb65156fff2d91cfa0"></a>

```c
uint16_t response_matches_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[response_matches_size](#afaaa9a7bc1842dfb65156fff2d91cfa0)。

预期响应数组中的元素数量。

<a id="r_a21647c746e9b2da52b7093afccf08268"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#a21647c746e9b2da52b7093afccf08268)。

交互脚本进入下一步之前的超时时间，单位为毫秒。

<a id="r_a27be66d0a39b1956e7ca5a00e2be17f6"></a>

```c
modem_chat_run_check run_check
```

相关声明：[modem_chat_run_check](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga372f3ffe3960a1bd3aa59a377656c262)、[run_check](#a27be66d0a39b1956e7ca5a00e2be17f6)。

返回应执行还是跳过请求的回调。

## 56.2\_详细说明（Detailed Documentation）

<a id="a92c038d56623b4f4b26c64b537e7ce8a"></a>

### `request`

```c
const uint8_t* modem_chat_script_chat::request
```

要发送给调制解调器的请求。

<a id="ad87948ff4e6441c118ee269bf6458aa0"></a>

### `request_size`

```c
uint16_t modem_chat_script_chat::request_size
```

请求大小。

<a id="a5cab9c3a31624c8ffb490b70285f86ee"></a>

### `response_matches`

```c
const struct modem_chat_match* modem_chat_script_chat::response_matches
```

此请求的预期响应。

<a id="afaaa9a7bc1842dfb65156fff2d91cfa0"></a>

### `response_matches_size`

```c
uint16_t modem_chat_script_chat::response_matches_size
```

预期响应数组中的元素数量。

<a id="a27be66d0a39b1956e7ca5a00e2be17f6"></a>

### `run_check`

```c
modem_chat_run_check modem_chat_script_chat::run_check
```

返回应执行还是跳过请求的回调。

<a id="a21647c746e9b2da52b7093afccf08268"></a>

### `timeout`

```c
uint16_t modem_chat_script_chat::timeout
```

交互脚本进入下一步之前的超时时间，单位为毫秒。

本数据类型文档由以下文件生成：

- `zephyr/modem/chat.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/modem/chat.h](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_chat_match](P054_modem_chat_match_结构体.md)
- [modem_chat_run_check](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga372f3ffe3960a1bd3aa59a377656c262)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_modem_chat_script_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_modem_chat_script_completion_info_结构体.md)
