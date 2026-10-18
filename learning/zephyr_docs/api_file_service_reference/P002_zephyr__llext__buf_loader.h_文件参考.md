---
id: learning.zephyr-docs.api-file-service-reference.page-2
title: zephyr__llext__buf_loader.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/buf__loader_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_llext\_\_buf\_loader.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/buf__loader_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可链接可加载扩展（LLEXT）的缓冲区加载器实现。

<a id="details"></a>

```c
#include <zephyr/llext/loader.h>
```

查看此文件的源码。

可链接可加载扩展（LLEXT）的缓冲区加载器实现。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_llext_5Fbuf_5Floader"></a>

```c
struct llext_buf_loader
```

相关声明：[llext_buf_loader](../llext/P021_缓冲区加载器.md)。

从内存缓冲区读取的llext_loader实现。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga9ca06c7c3e57f5284ce44c62f5cc2c02"></a>

```c
#define LLEXT_BUF_LOADER(_buf, _buf_len)
```

相关声明：[LLEXT_BUF_LOADER](../llext/P014_ELF加载器API.md#ga9ca06c7c3e57f5284ce44c62f5cc2c02)。

`llext_buf_loader` 结构体的初始化器（Initializer）。

<a id="r_ga8485b4dfecbd2eff3e21b5958d5e8699"></a>

```c
#define LLEXT_TEMPORARY_BUF_LOADER(_buf, _buf_len)
```

相关声明：[LLEXT_TEMPORARY_BUF_LOADER](../llext/P014_ELF加载器API.md#ga8485b4dfecbd2eff3e21b5958d5e8699)。

为临时缓冲区（Temporary Buffer）初始化 `llext_buf_loader` 结构体。

<a id="r_ga2c2214bcf1506f1209476619e42114b3"></a>

```c
#define LLEXT_PERSISTENT_BUF_LOADER(_buf, _buf_len)
```

相关声明：[LLEXT_PERSISTENT_BUF_LOADER](../llext/P014_ELF加载器API.md#ga2c2214bcf1506f1209476619e42114b3)。

为持久只读缓冲区（Persistent Read-Only Buffer）初始化 `llext_buf_loader` 结构体。

<a id="r_gac726727897e02bca0bf5d32f4c66be55"></a>

```c
#define LLEXT_WRITABLE_BUF_LOADER(_buf, _buf_len)
```

相关声明：[LLEXT_WRITABLE_BUF_LOADER](../llext/P014_ELF加载器API.md#gac726727897e02bca0bf5d32f4c66be55)。

为持久可写缓冲区（Persistent Writable Buffer）初始化 `llext_buf_loader` 结构体。


## 2.3\_原页交叉引用（Cross References）

- [zephyr/llext/loader.h](../api_source_supplement_reference/P100_loader.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P079_buf_loader.h_源码浏览.md)
- [llext_buf_loader](../llext/P021_缓冲区加载器.md)
- [llext_loader](../llext/P025_扩展加载器上下文.md)
- [LLEXT_BUF_LOADER](../llext/P014_ELF加载器API.md#ga9ca06c7c3e57f5284ce44c62f5cc2c02)
- [LLEXT_TEMPORARY_BUF_LOADER](../llext/P014_ELF加载器API.md#ga8485b4dfecbd2eff3e21b5958d5e8699)
- [LLEXT_PERSISTENT_BUF_LOADER](../llext/P014_ELF加载器API.md#ga2c2214bcf1506f1209476619e42114b3)
- [LLEXT_WRITABLE_BUF_LOADER](../llext/P014_ELF加载器API.md#gac726727897e02bca0bf5d32f4c66be55)

<a id="header-details"></a>

---

[上一章](P001_zephyr__mgmt__hawkbit__autohandler.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__clock_control__clock_control_silabs.h_文件参考.md)
