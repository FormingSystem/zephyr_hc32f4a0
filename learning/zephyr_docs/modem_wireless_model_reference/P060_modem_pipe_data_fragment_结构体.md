---
id: learning.zephyr-docs.modem-wireless-model-reference.page-60
title: modem_pipe_data_fragment_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__pipe__data__fragment.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_modem\_pipe\_data\_fragment\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__pipe__data__fragment.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多部分数据（Multi-Part Data）的片段。

```c
#include <zephyr/modem/pipe.h>
```

<a id="details"></a>

多部分数据（Multi-Part Data）的片段。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_a15f0c5d1e9838a583e66da62bf42bb96"></a>

```c
const uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a15f0c5d1e9838a583e66da62bf42bb96)。

数据指针。

<a id="r_a74684f59922bbd7f6a75da01c1558661"></a>

```c
size_t size
```

相关声明：[size](#a74684f59922bbd7f6a75da01c1558661)。

`data` 中的数据长度。

## 60.2\_详细说明（Detailed Documentation）

<a id="a15f0c5d1e9838a583e66da62bf42bb96"></a>

### `data`

```c
const uint8_t* modem_pipe_data_fragment::data
```

数据指针。

<a id="a74684f59922bbd7f6a75da01c1558661"></a>

### `size`

```c
size_t modem_pipe_data_fragment::size
```

`data` 中的数据长度。

本数据类型文档由以下文件生成：

- `zephyr/modem/pipe.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/modem/pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_modem_cmux_dlci_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_modem_ubx_结构体.md)
