---
id: learning.zephyr-docs.posix-system-model-reference.page-20
title: sigset_t_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsigset__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_sigset\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsigset__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a0017a77af9e5cdca8f1e0ffd4b7e086e"></a>

```c
unsigned long sig [DIV_ROUND_UP((32+CONFIG_POSIX_RTSIG_MAX)+1, BITS_PER_LONG)]
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[sig](#a0017a77af9e5cdca8f1e0ffd4b7e086e)、[DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)、[BITS_PER_LONG](../util_reference/P001_通用工具公共接口.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)。

## 20.2\_详细说明（Detailed Documentation）

<a id="a0017a77af9e5cdca8f1e0ffd4b7e086e"></a>

### `sig`

```c
unsigned long sigset_t::sig[DIV_ROUND_UP((32+CONFIG_POSIX_RTSIG_MAX)+1, BITS_PER_LONG)]
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_signal.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [BITS_PER_LONG](../util_reference/P001_通用工具公共接口.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_siginfo_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_stack_t_结构体.md)
