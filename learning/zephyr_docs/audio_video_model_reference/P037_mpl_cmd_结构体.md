---
id: learning.zephyr-docs.audio-video-model-reference.page-37
title: mpl_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpl__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_mpl\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpl__cmd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

媒体播放器命令（Media Player Command）。

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

<a id="details"></a>

媒体播放器命令（Media Player Command）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a5cb29ca9e5a6b8249c69cc975b345e2f"></a>

```c
uint8_t opcode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[opcode](#a5cb29ca9e5a6b8249c69cc975b345e2f)。

操作码（opcode）。

<a id="r_aca5e50b9f883a3c81f10ad51032a31f9"></a>

```c
bool use_param
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[use_param](#aca5e50b9f883a3c81f10ad51032a31f9)。

是否使用 `mpl_cmd::param`。

<a id="r_ade5ed4d0ff2aeb192b8ed6b586c9bc9e"></a>

```c
int32_t param
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[param](#ade5ed4d0ff2aeb192b8ed6b586c9bc9e)。

32 位有符号参数。

## 37.2\_详细说明（Detailed Documentation）

<a id="a5cb29ca9e5a6b8249c69cc975b345e2f"></a>

### `opcode`

```c
uint8_t mpl_cmd::opcode
```

操作码（opcode）。

参见 `MEDIA_PROXY_OP_*` 取值。

<a id="ade5ed4d0ff2aeb192b8ed6b586c9bc9e"></a>

### `param`

```c
int32_t mpl_cmd::param
```

32 位有符号参数。

参数值取决于 `mpl_cmd::opcode`。

<a id="aca5e50b9f883a3c81f10ad51032a31f9"></a>

### `use_param`

```c
bool mpl_cmd::use_param
```

是否使用 `mpl_cmd::param`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/media_proxy.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/media_proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_mpipe_value_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_mpl_cmd_ntf_结构体.md)
