---
id: learning.zephyr-docs.posix-system-model-reference.page-4
title: hostent_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhostent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_hostent\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhostent.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/netdb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a439d6e5efa18bc14aab63b14a12ae371"></a>

```c
char * h_name
```

相关声明：[h_name](#a439d6e5efa18bc14aab63b14a12ae371)。

<a id="r_ac266a0b528443e9479f2d8e1680b5e78"></a>

```c
char ** h_aliases
```

相关声明：[h_aliases](#ac266a0b528443e9479f2d8e1680b5e78)。

<a id="r_a405ebb31a6922898809635b03f0faf06"></a>

```c
int h_addrtype
```

相关声明：[h_addrtype](#a405ebb31a6922898809635b03f0faf06)。

<a id="r_ab9db18bfcc6adfc9c944b0c06ec2dccc"></a>

```c
int h_length
```

相关声明：[h_length](#ab9db18bfcc6adfc9c944b0c06ec2dccc)。

<a id="r_a4ff8499f29c5111435d6ed4adccfb621"></a>

```c
char ** h_addr_list
```

相关声明：[h_addr_list](#a4ff8499f29c5111435d6ed4adccfb621)。

## 4.2\_详细说明（Detailed Documentation）

<a id="a4ff8499f29c5111435d6ed4adccfb621"></a>

### `h_addr_list`

```c
char** hostent::h_addr_list
```

<a id="a405ebb31a6922898809635b03f0faf06"></a>

### `h_addrtype`

```c
int hostent::h_addrtype
```

<a id="ac266a0b528443e9479f2d8e1680b5e78"></a>

### `h_aliases`

```c
char** hostent::h_aliases
```

<a id="ab9db18bfcc6adfc9c944b0c06ec2dccc"></a>

### `h_length`

```c
int hostent::h_length
```

<a id="a439d6e5efa18bc14aab63b14a12ae371"></a>

### `h_name`

```c
char* hostent::h_name
```

本数据类型文档由以下文件生成：

- `zephyr/posix/netdb.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/posix/netdb.h](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_group_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_if_nameindex_结构体.md)
