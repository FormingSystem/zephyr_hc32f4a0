---
id: learning.zephyr-docs.modem-wireless-model-reference.page-48
title: modem_cellular_board_init_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__board__init.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_modem\_cellular\_board\_init\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__board__init.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将开发板提供的初始化脚本（Init Script）绑定到调制解调器实例的描述符。

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

<a id="details"></a>

将开发板提供的初始化脚本绑定到调制解调器实例的描述符，通过 `MODEM_CELLULAR_BOARD_INIT_DEFINE` 注册。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_a9cb679dd7826435256334e55c163c9fc"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#a9cb679dd7826435256334e55c163c9fc)。

<a id="r_a4e1bb0a376530c370edf8e0d993b0e28"></a>

```c
const struct modem_chat_script * script
```

相关声明：[modem_chat_script](P055_modem_chat_script_结构体.md)、[script](#a4e1bb0a376530c370edf8e0d993b0e28)。

## 48.2\_详细说明（Detailed Documentation）

<a id="a9cb679dd7826435256334e55c163c9fc"></a>

### `dev`

```c
const struct device* modem_cellular_board_init::dev
```

<a id="a4e1bb0a376530c370edf8e0d993b0e28"></a>

### `script`

```c
const struct modem_chat_script* modem_cellular_board_init::script
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/modem_cellular.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/modem_cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [modem_chat_script](P055_modem_chat_script_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_modem_backend_uart_isr_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_modem_cellular_config_scripts_结构体.md)
