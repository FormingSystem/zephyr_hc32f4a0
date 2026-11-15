---
id: learning.zephyr-docs.api-file-reference.page-162
title: zephyr__dt-bindings__dma__infineon-xmc4xxx-dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第162章\_zephyr\_\_dt-bindings\_\_dma\_\_infineon-xmc4xxx-dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 162.1\_宏定义（Macros）

<a id="r_a3c4acabda14da40580e0a2b27ee65460"></a>

```c
#define XMC4XXX_DMA_REQUEST_SOURCE_POS 0
```

相关声明：[XMC4XXX_DMA_REQUEST_SOURCE_POS](#a3c4acabda14da40580e0a2b27ee65460)。

<a id="r_a4df66f182189c3ae0983cdbbf9ae441c"></a>

```c
#define XMC4XXX_DMA_REQUEST_SOURCE_MASK 0xf
```

相关声明：[XMC4XXX_DMA_REQUEST_SOURCE_MASK](#a4df66f182189c3ae0983cdbbf9ae441c)。

<a id="r_a770a813125a4338de8e409d4c9056c16"></a>

```c
#define XMC4XXX_DMA_LINE_POS 4
```

相关声明：[XMC4XXX_DMA_LINE_POS](#a770a813125a4338de8e409d4c9056c16)。

<a id="r_a6675bcb092ce91d47fa5b47142ca45f4"></a>

```c
#define XMC4XXX_DMA_LINE_MASK 0xf
```

相关声明：[XMC4XXX_DMA_LINE_MASK](#a6675bcb092ce91d47fa5b47142ca45f4)。

<a id="r_a7545b103c79e582bec92c59571c2aee5"></a>

```c
#define XMC4XXX_DMA_GET_REQUEST_SOURCE(mx)
```

相关声明：[XMC4XXX_DMA_GET_REQUEST_SOURCE](#a7545b103c79e582bec92c59571c2aee5)。

<a id="r_a27d5d96c050301bfc22b52fe7f5483db"></a>

```c
#define XMC4XXX_DMA_GET_LINE(mx)
```

相关声明：[XMC4XXX_DMA_GET_LINE](#a27d5d96c050301bfc22b52fe7f5483db)。

<a id="r_afa54bae091f586404ae79cfa97db6d36"></a>

```c
#define XMC4XXX_SET_CONFIG(line, rs)
```

相关声明：[XMC4XXX_SET_CONFIG](#afa54bae091f586404ae79cfa97db6d36)。

## 162.2\_详细说明（Detailed Documentation）

<a id="a27d5d96c050301bfc22b52fe7f5483db"></a>

### `XMC4XXX_DMA_GET_LINE`

```c
#define XMC4XXX_DMA_GET_LINE ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_DMA_LINE_POS) & XMC4XXX_DMA_LINE_MASK)
```

<a id="a7545b103c79e582bec92c59571c2aee5"></a>

### `XMC4XXX_DMA_GET_REQUEST_SOURCE`

```c
#define XMC4XXX_DMA_GET_REQUEST_SOURCE ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_DMA_REQUEST_SOURCE_POS) & XMC4XXX_DMA_REQUEST_SOURCE_MASK)
```

<a id="a6675bcb092ce91d47fa5b47142ca45f4"></a>

### `XMC4XXX_DMA_LINE_MASK`

```c
#define XMC4XXX_DMA_LINE_MASK 0xf
```

<a id="a770a813125a4338de8e409d4c9056c16"></a>

### `XMC4XXX_DMA_LINE_POS`

```c
#define XMC4XXX_DMA_LINE_POS 4
```

<a id="a4df66f182189c3ae0983cdbbf9ae441c"></a>

### `XMC4XXX_DMA_REQUEST_SOURCE_MASK`

```c
#define XMC4XXX_DMA_REQUEST_SOURCE_MASK 0xf
```

<a id="a3c4acabda14da40580e0a2b27ee65460"></a>

### `XMC4XXX_DMA_REQUEST_SOURCE_POS`

```c
#define XMC4XXX_DMA_REQUEST_SOURCE_POS 0
```

<a id="afa54bae091f586404ae79cfa97db6d36"></a>

### `XMC4XXX_SET_CONFIG`

```c
#define XMC4XXX_SET_CONFIG ( line, rs )
```

展开值（Value）：

```c
((line) << XMC4XXX_DMA_LINE_POS | (rs) << XMC4XXX_DMA_REQUEST_SOURCE_POS)
```


## 162.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P372_infineon-xmc4xxx-dma.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="ainfineon-xmc4xxx-dma_8h_html_a6675bcb092ce91d47fa5b47142ca45f4"></a>
<a id="ainfineon-xmc4xxx-dma_8h_html_a770a813125a4338de8e409d4c9056c16"></a>
<a id="ainfineon-xmc4xxx-dma_8h_html_a3c4acabda14da40580e0a2b27ee65460"></a>
<a id="ainfineon-xmc4xxx-dma_8h_html_a4df66f182189c3ae0983cdbbf9ae441c"></a>

---

[上一章](P161_zephyr__posix__arpa__inet.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P163_zephyr__dt-bindings__gpio__infineon-xmc4xxx-gpio.h_文件参考.md)
