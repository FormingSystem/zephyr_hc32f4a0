---
id: learning.zephyr-docs.api-file-supplement-reference.page-138
title: zephyr__dt-bindings__flash_controller__xspi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xspi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第138章\_zephyr\_\_dt-bindings\_\_flash\_controller\_\_xspi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/xspi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 138.1\_宏定义（Macros）

<a id="define-members-0"></a>

### xSPI 外设的 XSPI 定义（XSPI Definitions）

注意，原文表述为“SPI 模式不可能仅采用单倍传输速率（STR）”。

> 译注：原文为“Note that SPI mode impossible in STR transfer rate only”，其 `impossible` 与 `only` 的组合存在语义歧义；本页保留该表述，不据此推断硬件允许的传输模式组合。

<a id="r_af46f316833f2edf8ad528c2247050f7b"></a>

```c
#define XSPI_SPI_MODE 1
```

相关声明：[XSPI_SPI_MODE](#af46f316833f2edf8ad528c2247050f7b)。

<a id="r_a6b13657beb90f13af580a7ffce42af33"></a>

```c
#define XSPI_DUAL_MODE 2
```

相关声明：[XSPI_DUAL_MODE](#a6b13657beb90f13af580a7ffce42af33)。

<a id="r_a707d8a21a2b53d6b9d5ccbcb830bec39"></a>

```c
#define XSPI_QUAD_MODE 4
```

相关声明：[XSPI_QUAD_MODE](#a707d8a21a2b53d6b9d5ccbcb830bec39)。

<a id="r_a31cb4ace810add7d7b9bd9b18114f83e"></a>

```c
#define XSPI_OCTO_MODE 8
```

相关声明：[XSPI_OCTO_MODE](#a31cb4ace810add7d7b9bd9b18114f83e)。

<a id="r_aaba9227de2cc14e8e8215391c8e8d569"></a>

```c
#define XSPI_STR_TRANSFER 1
```

相关声明：[XSPI_STR_TRANSFER](#aaba9227de2cc14e8e8215391c8e8d569)。

<a id="r_a779d385b42986b752d93b0de74b52015"></a>

```c
#define XSPI_DTR_TRANSFER 2
```

相关声明：[XSPI_DTR_TRANSFER](#a779d385b42986b752d93b0de74b52015)。

## 138.2\_详细说明（Detailed Documentation）

<a id="a779d385b42986b752d93b0de74b52015"></a>

### `XSPI_DTR_TRANSFER`

```c
#define XSPI_DTR_TRANSFER 2
```

<a id="a6b13657beb90f13af580a7ffce42af33"></a>

### `XSPI_DUAL_MODE`

```c
#define XSPI_DUAL_MODE 2
```

<a id="a31cb4ace810add7d7b9bd9b18114f83e"></a>

### `XSPI_OCTO_MODE`

```c
#define XSPI_OCTO_MODE 8
```

<a id="a707d8a21a2b53d6b9d5ccbcb830bec39"></a>

### `XSPI_QUAD_MODE`

```c
#define XSPI_QUAD_MODE 4
```

<a id="af46f316833f2edf8ad528c2247050f7b"></a>

### `XSPI_SPI_MODE`

```c
#define XSPI_SPI_MODE 1
```

<a id="aaba9227de2cc14e8e8215391c8e8d569"></a>

### `XSPI_STR_TRANSFER`

```c
#define XSPI_STR_TRANSFER 1
```


## 138.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/xspi_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P137_zephyr__dt-bindings__dma__silabs__xg29-dma.h_文件参考.md) · [返回大纲](大纲.md)
