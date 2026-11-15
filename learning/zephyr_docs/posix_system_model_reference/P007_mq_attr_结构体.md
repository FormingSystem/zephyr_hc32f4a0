---
id: learning.zephyr-docs.posix-system-model-reference.page-7
title: mq_attr_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmq__attr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_mq\_attr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmq__attr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/mqueue.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a19c05fa88c6d1126120d800647ddb0dd"></a>

```c
long mq_flags
```

相关声明：[mq_flags](#a19c05fa88c6d1126120d800647ddb0dd)。

<a id="r_aa535e1fa6c07c1d189e720ba15f9af08"></a>

```c
long mq_maxmsg
```

相关声明：[mq_maxmsg](#aa535e1fa6c07c1d189e720ba15f9af08)。

<a id="r_ae975d1d907081c1e53b079c981c32209"></a>

```c
long mq_msgsize
```

相关声明：[mq_msgsize](#ae975d1d907081c1e53b079c981c32209)。

<a id="r_a08cfd508cef817ba351c1af8d9af50f5"></a>

```c
long mq_curmsgs
```

相关声明：[mq_curmsgs](#a08cfd508cef817ba351c1af8d9af50f5)。

## 7.2\_详细说明（Detailed Documentation）

<a id="a08cfd508cef817ba351c1af8d9af50f5"></a>

### `mq_curmsgs`

```c
long mq_attr::mq_curmsgs
```

<a id="a19c05fa88c6d1126120d800647ddb0dd"></a>

### `mq_flags`

```c
long mq_attr::mq_flags
```

<a id="aa535e1fa6c07c1d189e720ba15f9af08"></a>

### `mq_maxmsg`

```c
long mq_attr::mq_maxmsg
```

<a id="ae975d1d907081c1e53b079c981c32209"></a>

### `mq_msgsize`

```c
long mq_attr::mq_msgsize
```

本数据类型文档由以下文件生成：

- `zephyr/posix/mqueue.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/posix/mqueue.h](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_linger_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_netent_结构体.md)
