---
id: learning.zephyr-docs.api-file-reference.page-147
title: zephyr__dt-bindings__misc__ifx_cyw20829.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__cyw20829_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第147章\_zephyr\_\_dt-bindings\_\_misc\_\_ifx\_cyw20829.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ifx__cyw20829_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 147.1\_宏定义（Macros）

<a id="r_ab5ab076f3a6725715d7b6de08adeede5"></a>

```c
#define SRAM0_SAHB_BASE 0x20000000
```

相关声明：[SRAM0_SAHB_BASE](#ab5ab076f3a6725715d7b6de08adeede5)。

<a id="r_a55afd8be624b89f5e8e5b637e6b74acd"></a>

```c
#define SRAM0_CBUS_BASE 0x04000000
```

相关声明：[SRAM0_CBUS_BASE](#a55afd8be624b89f5e8e5b637e6b74acd)。

<a id="r_a46ca92a8d5a7ae3c7188036216d7d768"></a>

```c
#define BOOTSTRAP_SIZE DT_SIZE_K(16)
```

相关声明：[BOOTSTRAP_SIZE](#a46ca92a8d5a7ae3c7188036216d7d768)。

<a id="r_a060ab9fe92fcb323f540eade9cdb4695"></a>

```c
#define BOOTSTRAP_BASE_OFFSET (DT_SIZE_K(256) - BOOTSTRAP_SIZE)
```

相关声明：[BOOTSTRAP_BASE_OFFSET](#a060ab9fe92fcb323f540eade9cdb4695)、[BOOTSTRAP_SIZE](#a46ca92a8d5a7ae3c7188036216d7d768)。

<a id="r_a7a4a77195720e98bf9d4b634548f52e3"></a>

```c
#define BOOTSTRAP_SAHB_BASE (SRAM0_SAHB_BASE + BOOTSTRAP_BASE_OFFSET)
```

相关声明：[BOOTSTRAP_SAHB_BASE](#a7a4a77195720e98bf9d4b634548f52e3)、[SRAM0_SAHB_BASE](#ab5ab076f3a6725715d7b6de08adeede5)、[BOOTSTRAP_BASE_OFFSET](#a060ab9fe92fcb323f540eade9cdb4695)。

<a id="r_ac93a6947075c798cd8a1c1214613b938"></a>

```c
#define BOOTSTRAP_CBUS_BASE (SRAM0_CBUS_BASE + BOOTSTRAP_BASE_OFFSET)
```

相关声明：[BOOTSTRAP_CBUS_BASE](#ac93a6947075c798cd8a1c1214613b938)、[SRAM0_CBUS_BASE](#a55afd8be624b89f5e8e5b637e6b74acd)、[BOOTSTRAP_BASE_OFFSET](#a060ab9fe92fcb323f540eade9cdb4695)。

<a id="r_ade6f29a1d3e5bd550ae6527640d8ab0d"></a>

```c
#define SRAM0_SIZE (DT_SIZE_K(256) - BOOTSTRAP_SIZE)
```

相关声明：[SRAM0_SIZE](#ade6f29a1d3e5bd550ae6527640d8ab0d)、[BOOTSTRAP_SIZE](#a46ca92a8d5a7ae3c7188036216d7d768)。

## 147.2\_详细说明（Detailed Documentation）

<a id="a060ab9fe92fcb323f540eade9cdb4695"></a>

### `BOOTSTRAP_BASE_OFFSET`

```c
#define BOOTSTRAP_BASE_OFFSET (DT_SIZE_K(256) - BOOTSTRAP_SIZE)
```

<a id="ac93a6947075c798cd8a1c1214613b938"></a>

### `BOOTSTRAP_CBUS_BASE`

```c
#define BOOTSTRAP_CBUS_BASE (SRAM0_CBUS_BASE + BOOTSTRAP_BASE_OFFSET)
```

<a id="a7a4a77195720e98bf9d4b634548f52e3"></a>

### `BOOTSTRAP_SAHB_BASE`

```c
#define BOOTSTRAP_SAHB_BASE (SRAM0_SAHB_BASE + BOOTSTRAP_BASE_OFFSET)
```

<a id="a46ca92a8d5a7ae3c7188036216d7d768"></a>

### `BOOTSTRAP_SIZE`

```c
#define BOOTSTRAP_SIZE DT_SIZE_K(16)
```

<a id="a55afd8be624b89f5e8e5b637e6b74acd"></a>

### `SRAM0_CBUS_BASE`

```c
#define SRAM0_CBUS_BASE 0x04000000
```

<a id="ab5ab076f3a6725715d7b6de08adeede5"></a>

### `SRAM0_SAHB_BASE`

```c
#define SRAM0_SAHB_BASE 0x20000000
```

<a id="ade6f29a1d3e5bd550ae6527640d8ab0d"></a>

### `SRAM0_SIZE`

```c
#define SRAM0_SIZE (DT_SIZE_K(256) - BOOTSTRAP_SIZE)
```


## 147.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P343_ifx_cyw20829.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P146_zephyr__dt-bindings__clock__ifx_clock_source_psoc4xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P148_zephyr__dt-bindings__pinctrl__imx8qm-pinctrl.h_文件参考.md)
