---
id: learning.zephyr-docs.api-platform-topic-reference.page-2
title: Aesc Silicon 时钟域标识符（Clock domain identifiers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__aesc__clock__controller.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Aesc Silicon 时钟域标识符（Clock domain identifiers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__aesc__clock__controller.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Aesc Silicon ElemRV-H片上系统（SoC）的时钟域标识符。

<a id="details"></a>

Aesc Silicon ElemRV-H 片上系统（SoC）的时钟域标识（Clock Domain Identifiers）。这些标识用作 `aesc,clock-controller` 节点唯一的时钟说明符单元（Clock Specifier Cell），例如：

```c
clocks = <&clkctrl HYDROGEN_CLK_SYSTEM>;
```

每个标识都是从零开始的时钟域索引（Zero-Based Index），与 SoC 中时钟域列表的顺序一致。

<a id="header-files"></a>
<a id="files"></a>

## 2.1\_文件（Files）

<a id="r_aesc-clock-controller_2Eh"></a>

```c
file aesc-clock-controller.h
```

相关声明：[aesc-clock-controller.h](../api_file_configuration_reference/P003_zephyr__dt-bindings__clock__aesc-clock-controller.h_文件参考.md)。

Aesc Silicon ElemRV-H片上系统（SoC）的时钟域标识符。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga12317625f005f4a5a6516b6faaeab379"></a>

```c
#define HYDROGEN_CLK_SYSTEM 0
```

相关声明：[HYDROGEN_CLK_SYSTEM](#ga12317625f005f4a5a6516b6faaeab379)。

系统时钟域（System Clock Domain），驱动 CPU 和外设总线（Peripheral Bus）。

<a id="r_gaca5cc0d017ff82fb3f22b6a8718ab324"></a>

```c
#define HYDROGEN_CLK_DEBUG 1
```

相关声明：[HYDROGEN_CLK_DEBUG](#gaca5cc0d017ff82fb3f22b6a8718ab324)。

调试时钟域（Debug Clock Domain），驱动调试模块（Debug Module）。

## 2.3\_详细说明（Detailed Documentation）

<a id="gaca5cc0d017ff82fb3f22b6a8718ab324"></a>

### `HYDROGEN_CLK_DEBUG`

```c
#define HYDROGEN_CLK_DEBUG 1
```

```c
#include <zephyr/dt-bindings/clock/aesc-clock-controller.h>
```

调试时钟域（Debug Clock Domain），驱动调试模块（Debug Module）。

<a id="ga12317625f005f4a5a6516b6faaeab379"></a>

### `HYDROGEN_CLK_SYSTEM`

```c
#define HYDROGEN_CLK_SYSTEM 0
```

```c
#include <zephyr/dt-bindings/clock/aesc-clock-controller.h>
```

系统时钟域（System Clock Domain），驱动 CPU 和外设总线（Peripheral Bus）。


## 2.4\_原页交叉引用（Cross References）

- [aesc-clock-controller.h](../api_file_configuration_reference/P003_zephyr__dt-bindings__clock__aesc-clock-controller.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_cbvprintf 处理标志（Processing Flags）.md) · [返回大纲](大纲.md) · [下一章](P003_蓝牙 API（Bluetooth APIs）.md)
