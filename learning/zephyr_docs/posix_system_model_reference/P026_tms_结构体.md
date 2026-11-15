---
id: learning.zephyr-docs.posix-system-model-reference.page-26
title: tms_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtms.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_tms\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtms.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/sys/times.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_a2522ba0b91f98baeb8f2b7249f367b7c"></a>

```c
clock_t tms_utime
```

相关声明：[clock_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3b55f88f25d2c571de53a365ad658426)、[tms_utime](#a2522ba0b91f98baeb8f2b7249f367b7c)。

<a id="r_a60d97d80205a34858387314fb00cc4c0"></a>

```c
clock_t tms_stime
```

相关声明：[clock_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3b55f88f25d2c571de53a365ad658426)、[tms_stime](#a60d97d80205a34858387314fb00cc4c0)。

<a id="r_adc1a7576a7287de70b7611047829ab6f"></a>

```c
clock_t tms_cutime
```

相关声明：[clock_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3b55f88f25d2c571de53a365ad658426)、[tms_cutime](#adc1a7576a7287de70b7611047829ab6f)。

<a id="r_ad21f41a18aff2813fe6154154f1f9522"></a>

```c
clock_t tms_cstime
```

相关声明：[clock_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3b55f88f25d2c571de53a365ad658426)、[tms_cstime](#ad21f41a18aff2813fe6154154f1f9522)。

## 26.2\_详细说明（Detailed Documentation）

<a id="ad21f41a18aff2813fe6154154f1f9522"></a>

### `tms_cstime`

```c
clock_t tms::tms_cstime
```

<a id="adc1a7576a7287de70b7611047829ab6f"></a>

### `tms_cutime`

```c
clock_t tms::tms_cutime
```

<a id="a60d97d80205a34858387314fb00cc4c0"></a>

### `tms_stime`

```c
clock_t tms::tms_stime
```

<a id="a2522ba0b91f98baeb8f2b7249f367b7c"></a>

### `tms_utime`

```c
clock_t tms::tms_utime
```

本数据类型文档由以下文件生成：

- `zephyr/posix/sys/times.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/posix/sys/times.h](https://docs.zephyrproject.org/latest/doxygen/html/times_8h_source.html)
- [clock_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3b55f88f25d2c571de53a365ad658426)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_tm_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_ucontext_t_结构体.md)
