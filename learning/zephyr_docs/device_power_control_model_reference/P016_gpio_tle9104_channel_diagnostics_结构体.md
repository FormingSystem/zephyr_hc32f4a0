---
id: learning.zephyr-docs.device-power-control-model-reference.page-16
title: gpio_tle9104_channel_diagnostics_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__tle9104__channel__diagnostics.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_gpio\_tle9104\_channel\_diagnostics\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__tle9104__channel__diagnostics.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/mfd/tle9104.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a85b90c4dbf15bfbefb6646de10b6c634"></a>

```c
enum tle9104_on_state_diagnostics on: 3
```

相关声明：[tle9104_on_state_diagnostics](https://docs.zephyrproject.org/latest/doxygen/html/mfd_2tle9104_8h.html#aa40748ba46d1bc413f8bf3caa5d7b4b0)、[on](#a85b90c4dbf15bfbefb6646de10b6c634)。

<a id="r_adbc7944242d212933d510881541f9d66"></a>

```c
enum tle9104_off_state_diagnostics off: 2
```

相关声明：[tle9104_off_state_diagnostics](https://docs.zephyrproject.org/latest/doxygen/html/mfd_2tle9104_8h.html#acd342488b1a9b0e2b4a0e79a1441d8e3)、[off](#adbc7944242d212933d510881541f9d66)。

## 16.2\_详细说明（Detailed Documentation）

<a id="adbc7944242d212933d510881541f9d66"></a>

### `off`

```c
enum tle9104_off_state_diagnostics gpio_tle9104_channel_diagnostics::off
```

<a id="a85b90c4dbf15bfbefb6646de10b6c634"></a>

### `on`

```c
enum tle9104_on_state_diagnostics gpio_tle9104_channel_diagnostics::on
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/mfd/tle9104.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mfd/tle9104.h](https://docs.zephyrproject.org/latest/doxygen/html/mfd_2tle9104_8h_source.html)
- [tle9104_on_state_diagnostics](https://docs.zephyrproject.org/latest/doxygen/html/mfd_2tle9104_8h.html#aa40748ba46d1bc413f8bf3caa5d7b4b0)
- [tle9104_off_state_diagnostics](https://docs.zephyrproject.org/latest/doxygen/html/mfd_2tle9104_8h.html#acd342488b1a9b0e2b4a0e79a1441d8e3)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_gpio_rx_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_ifx_cat1_clock_结构体.md)
