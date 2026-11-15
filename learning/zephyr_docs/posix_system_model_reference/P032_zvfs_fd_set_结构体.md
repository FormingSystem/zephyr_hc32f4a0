---
id: learning.zephyr-docs.posix-system-model-reference.page-32
title: zvfs_fd_set_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzvfs__fd__set.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zvfs\_fd\_set\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structzvfs__fd__set.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/fdtable.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_aa057869d6cee9109890d42f74c84fe19"></a>

```c
uint32_t bitset [1]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bitset](#aa057869d6cee9109890d42f74c84fe19)。

## 32.2\_详细说明（Detailed Documentation）

<a id="aa057869d6cee9109890d42f74c84fe19"></a>

### `bitset`

```c
uint32_t zvfs_fd_set::bitset[1]
```

本数据类型文档由以下文件生成：

- `zephyr/sys/fdtable.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_zsock_tls_cert_verify_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_zvfs_pollfd_结构体.md)
