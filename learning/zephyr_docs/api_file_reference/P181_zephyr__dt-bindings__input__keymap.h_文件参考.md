---
id: learning.zephyr-docs.api-file-reference.page-181
title: zephyr__dt-bindings__input__keymap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/keymap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第181章\_zephyr\_\_dt-bindings\_\_input\_\_keymap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/keymap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 181.1\_宏定义（Macros）

<a id="r_ab43c29335b0939bfa3e770c86d1622a0"></a>

```c
#define MATRIX_KEY(row, col, code)
```

相关声明：[MATRIX_KEY](#ab43c29335b0939bfa3e770c86d1622a0)。

## 181.2\_详细说明（Detailed Documentation）

<a id="ab43c29335b0939bfa3e770c86d1622a0"></a>

### `MATRIX_KEY`

```c
#define MATRIX_KEY ( row, col, code )
```

展开值（Value）：

```c
((((row) & 0xff) << 24) | (((col) & 0xff) << 16) | ((code) & 0xffff))
```


## 181.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P431_keymap.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P180_zephyr__kernel_structs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P182_zephyr__dt-bindings__clock__kinetis_mcg.h_文件参考.md)
