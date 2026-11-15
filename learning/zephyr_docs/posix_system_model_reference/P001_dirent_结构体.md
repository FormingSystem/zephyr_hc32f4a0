---
id: learning.zephyr-docs.posix-system-model-reference.page-1
title: dirent_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdirent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_dirent\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdirent.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/sys/dirent.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_ae4afde6b22d291bf27193ad4fe20b0bf"></a>

```c
unsigned int d_ino
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[d_ino](#ae4afde6b22d291bf27193ad4fe20b0bf)。

<a id="r_a493ff210982a02728c1b177139bfdb47"></a>

```c
char d_name [NAME_MAX+1]
```

相关声明：[d_name](#a493ff210982a02728c1b177139bfdb47)。

## 1.2\_详细说明（Detailed Documentation）

<a id="ae4afde6b22d291bf27193ad4fe20b0bf"></a>

### `d_ino`

```c
unsigned int dirent::d_ino
```

<a id="a493ff210982a02728c1b177139bfdb47"></a>

### `d_name`

```c
char dirent::d_name[NAME_MAX+1]
```

本数据类型文档由以下文件生成：

- `zephyr/posix/sys/dirent.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/posix/sys/dirent.h](https://docs.zephyrproject.org/latest/doxygen/html/sys_2dirent_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_fd_op_vtable_结构体.md)
