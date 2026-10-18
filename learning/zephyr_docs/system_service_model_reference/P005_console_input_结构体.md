---
id: learning.zephyr-docs.system-service-model-reference.page-5
title: console_input_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structconsole__input.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_console\_input\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structconsole__input.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

控制台输入（Console Input）的表示。

```c
#include <zephyr/drivers/console/console.h>
```

<a id="details"></a>

控制台输入（Console input）的表示形式。此结构体表示来自控制台的一行输入，记录的行必须以空字符终止。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a2c13a1e2a4895cf1d51c8ce7879af927"></a>

```c
uint8_t is_mcumgr: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_mcumgr](#a2c13a1e2a4895cf1d51c8ce7879af927)。

是否为 mcumgr 命令。

<a id="r_a33bf8ba6d114ec99219c134c0f6c3474"></a>

```c
char line [CONFIG_CONSOLE_INPUT_MAX_LINE_LEN]
```

相关声明：[line](#a33bf8ba6d114ec99219c134c0f6c3474)。

记录输入行的缓冲区。

## 5.2\_详细说明（Detailed Documentation）

<a id="a2c13a1e2a4895cf1d51c8ce7879af927"></a>

### `is_mcumgr`

```c
uint8_t console_input::is_mcumgr
```

是否为 mcumgr 命令。

<a id="a33bf8ba6d114ec99219c134c0f6c3474"></a>

### `line`

```c
char console_input::line[CONFIG_CONSOLE_INPUT_MAX_LINE_LEN]
```

记录输入行的缓冲区。

本数据类型文档由以下文件生成：

- `zephyr/drivers/console/console.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/drivers/console/console.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2console_2console_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_cobs_encoder_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_dap_link_context_结构体.md)
