---
id: learning.zephyr-docs.platform-security-model-reference.page-17
title: mcontext_t_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcontext__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_mcontext\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcontext__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_ae2977e51fe658ca375e4f2ee8994bdcb"></a>

```c
unsigned long gregs [32]
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[gregs](#ae2977e51fe658ca375e4f2ee8994bdcb)。

<a id="r_a3dbbd980d01e9f843e842f09217c522d"></a>

```c
unsigned long flags
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[flags](#a3dbbd980d01e9f843e842f09217c522d)。

## 17.2\_详细说明（Detailed Documentation）

<a id="a3dbbd980d01e9f843e842f09217c522d"></a>

### `flags`

```c
unsigned long mcontext_t::flags
```

<a id="ae2977e51fe658ca375e4f2ee8994bdcb"></a>

### `gregs`

```c
unsigned long mcontext_t::gregs[32]
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_signal.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_its_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_msi_vector_结构体.md)
