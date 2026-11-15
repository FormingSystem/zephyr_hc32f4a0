---
id: learning.zephyr-docs.posix-system-model-reference.page-13
title: pthread_condattr_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpthread__condattr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_pthread\_condattr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpthread__condattr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_ac8f29de493f72c650ea59c71305c3e96"></a>

```c
clockid_t clock
```

相关声明：[clockid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h.html#a6bb3206700910111f26e946bfbf0f2af)、[clock](#ac8f29de493f72c650ea59c71305c3e96)。

## 13.2\_详细说明（Detailed Documentation）

<a id="ac8f29de493f72c650ea59c71305c3e96"></a>

### `clock`

```c
clockid_t pthread_condattr::clock
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_types.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)
- [clockid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h.html#a6bb3206700910111f26e946bfbf0f2af)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_pthread_barrierattr_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_pthread_mutexattr_结构体.md)
