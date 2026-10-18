---
id: learning.zephyr-docs.modem-wireless-model-reference.page-57
title: modem_chat_script_completion_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__script__completion__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_modem\_chat\_script\_completion\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__script__completion__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已完成脚本（Script）的附加信息。

```c
#include <zephyr/modem/chat.h>
```

<a id="details"></a>

已完成脚本（Script）的附加信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_a2e6ec071adec5565d4248e9ba1232c3b"></a>

```c
const struct modem_chat_script * script
```

相关声明：[modem_chat_script](P055_modem_chat_script_结构体.md)、[script](#a2e6ec071adec5565d4248e9ba1232c3b)。

当时正在执行的脚本。

<a id="r_a96294f87215db5d14432d208d1bad960"></a>

```c
const struct modem_chat_script_chat * script_chat
```

相关声明：[modem_chat_script_chat](P056_modem_chat_script_chat_结构体.md)、[script_chat](#a96294f87215db5d14432d208d1bad960)。

最后执行或跳过的脚本交互步骤；空脚本可为 `NULL`。

## 57.2\_详细说明（Detailed Documentation）

<a id="a2e6ec071adec5565d4248e9ba1232c3b"></a>

### `script`

```c
const struct modem_chat_script* modem_chat_script_completion_info::script
```

当时正在执行的脚本。

<a id="a96294f87215db5d14432d208d1bad960"></a>

### `script_chat`

```c
const struct modem_chat_script_chat* modem_chat_script_completion_info::script_chat
```

最后执行或跳过的脚本交互步骤；空脚本可为 `NULL`。

本数据类型文档由以下文件生成：

- `zephyr/modem/chat.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/modem/chat.h](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h_source.html)
- [modem_chat_script](P055_modem_chat_script_结构体.md)
- [modem_chat_script_chat](P056_modem_chat_script_chat_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_modem_chat_script_chat_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_modem_cmux_config_结构体.md)
