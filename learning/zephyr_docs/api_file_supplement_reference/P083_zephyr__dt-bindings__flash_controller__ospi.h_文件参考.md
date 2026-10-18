---
id: learning.zephyr-docs.api-file-supplement-reference.page-83
title: zephyr__dt-bindings__flash_controller__ospi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ospi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_zephyr\_\_dt-bindings\_\_flash\_controller\_\_ospi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ospi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 83.1\_宏定义（Macros）

<a id="define-members-0"></a>

### OctoSPI 外设的 OSPI 定义（OSPI Definitions）

注意，可用的组合（Combinations）包括：采用单倍传输速率（Single Transfer Rate，STR）的 SPI 模式、采用 STR 的 OPI 模式，以及采用双倍传输速率（Double Transfer Rate，DTR）的 OPI 模式。

<a id="r_aa05908cb55f8b2c2b075fa5fe63295d6"></a>

```c
#define OSPI_SPI_MODE 1
```

相关声明：[OSPI_SPI_MODE](#aa05908cb55f8b2c2b075fa5fe63295d6)。

<a id="r_a16b26e6d0f41ec784419f650580bab70"></a>

```c
#define OSPI_DUAL_MODE 2
```

相关声明：[OSPI_DUAL_MODE](#a16b26e6d0f41ec784419f650580bab70)。

<a id="r_a9baa648178c8018dc3371df3ec62ad46"></a>

```c
#define OSPI_QUAD_MODE 4
```

相关声明：[OSPI_QUAD_MODE](#a9baa648178c8018dc3371df3ec62ad46)。

<a id="r_a3a5249c447488edc0bd67e69ffbb2323"></a>

```c
#define OSPI_OPI_MODE 8
```

相关声明：[OSPI_OPI_MODE](#a3a5249c447488edc0bd67e69ffbb2323)。

<a id="r_a05dc6d0a9546bb2ddad1b519cf663a3b"></a>

```c
#define OSPI_STR_TRANSFER 1
```

相关声明：[OSPI_STR_TRANSFER](#a05dc6d0a9546bb2ddad1b519cf663a3b)。

<a id="r_adc6ece270c248515bc36b7e73b32fedd"></a>

```c
#define OSPI_DTR_TRANSFER 2
```

相关声明：[OSPI_DTR_TRANSFER](#adc6ece270c248515bc36b7e73b32fedd)。

## 83.2\_详细说明（Detailed Documentation）

<a id="adc6ece270c248515bc36b7e73b32fedd"></a>

### `OSPI_DTR_TRANSFER`

```c
#define OSPI_DTR_TRANSFER 2
```

<a id="a16b26e6d0f41ec784419f650580bab70"></a>

### `OSPI_DUAL_MODE`

```c
#define OSPI_DUAL_MODE 2
```

<a id="a3a5249c447488edc0bd67e69ffbb2323"></a>

### `OSPI_OPI_MODE`

```c
#define OSPI_OPI_MODE 8
```

<a id="a9baa648178c8018dc3371df3ec62ad46"></a>

### `OSPI_QUAD_MODE`

```c
#define OSPI_QUAD_MODE 4
```

<a id="aa05908cb55f8b2c2b075fa5fe63295d6"></a>

### `OSPI_SPI_MODE`

```c
#define OSPI_SPI_MODE 1
```

<a id="a05dc6d0a9546bb2ddad1b519cf663a3b"></a>

### `OSPI_STR_TRANSFER`

```c
#define OSPI_STR_TRANSFER 1
```


## 83.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/ospi_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P082_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt_callbacks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P084_zephyr__drivers__sensor__pat9136.h_文件参考.md)
