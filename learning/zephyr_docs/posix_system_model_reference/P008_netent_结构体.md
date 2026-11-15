---
id: learning.zephyr-docs.posix-system-model-reference.page-8
title: netent_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnetent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_netent\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnetent.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/netdb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_ad6d1687141f88ffde193f198b2c36735"></a>

```c
char * n_name
```

相关声明：[n_name](#ad6d1687141f88ffde193f198b2c36735)。

<a id="r_ab872aa2c431de28a5a72fc0cae693f0b"></a>

```c
char ** n_aliases
```

相关声明：[n_aliases](#ab872aa2c431de28a5a72fc0cae693f0b)。

<a id="r_ae04a32bad76f6bd5cc350179ea88a1ee"></a>

```c
int n_addrtype
```

相关声明：[n_addrtype](#ae04a32bad76f6bd5cc350179ea88a1ee)。

<a id="r_a108f91da08bdf576c768429286b0f5c1"></a>

```c
uint32_t n_net
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[n_net](#a108f91da08bdf576c768429286b0f5c1)。

## 8.2\_详细说明（Detailed Documentation）

<a id="ae04a32bad76f6bd5cc350179ea88a1ee"></a>

### `n_addrtype`

```c
int netent::n_addrtype
```

<a id="ab872aa2c431de28a5a72fc0cae693f0b"></a>

### `n_aliases`

```c
char** netent::n_aliases
```

<a id="ad6d1687141f88ffde193f198b2c36735"></a>

### `n_name`

```c
char* netent::n_name
```

<a id="a108f91da08bdf576c768429286b0f5c1"></a>

### `n_net`

```c
uint32_t netent::n_net
```

本数据类型文档由以下文件生成：

- `zephyr/posix/netdb.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/posix/netdb.h](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_mq_attr_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_passwd_结构体.md)
