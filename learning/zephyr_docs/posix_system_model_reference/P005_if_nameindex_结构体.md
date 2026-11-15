---
id: learning.zephyr-docs.posix-system-model-reference.page-5
title: if_nameindex_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structif__nameindex.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_if\_nameindex\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structif__nameindex.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/net/if.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a614c64e1c7abc1e2752860b14061f479"></a>

```c
unsigned int if_index
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[if_index](#a614c64e1c7abc1e2752860b14061f479)。

<a id="r_ab9d0f12e108f5f7ad0fccc951a4211b2"></a>

```c
char * if_name
```

相关声明：[if_name](#ab9d0f12e108f5f7ad0fccc951a4211b2)。

## 5.2\_详细说明（Detailed Documentation）

<a id="a614c64e1c7abc1e2752860b14061f479"></a>

### `if_index`

```c
unsigned int if_nameindex::if_index
```

<a id="ab9d0f12e108f5f7ad0fccc951a4211b2"></a>

### `if_name`

```c
char* if_nameindex::if_name
```

本数据类型文档由以下文件生成：

- `zephyr/posix/net/if.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/posix/net/if.h](https://docs.zephyrproject.org/latest/doxygen/html/if_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_hostent_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_linger_结构体.md)
