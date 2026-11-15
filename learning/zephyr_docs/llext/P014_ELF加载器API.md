---
id: learning.zephyr-docs.llext.api-14
title: ELF加载器API
kind: reference
status: maintained
domains: [zephyr, llext, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__llext__loader__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_ELF加载器API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__loader__apis.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 14.1\_概述

本页描述 `ELF` 加载器上下文（`ELF` Loader Context）、缓冲区寿命和存储类型。

## 14.2\_关联声明与说明

<a id="r_buf_5Floader_2Eh"></a>

```c
file buf_loader.h
```

LLEXT 缓冲区加载器实现。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/buf__loader_8h.html)。

<a id="r_fs_5Floader_2Eh"></a>

```c
file fs_loader.h
```

LLEXT 文件系统加载器实现。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/fs__loader_8h.html)。

## 14.3\_关联声明与说明

<a id="r_llext_5Fbuf_5Floader"></a>

```c
struct llext_buf_loader
```

从内存缓冲区读取数据的 [`llext_loader`](P025_扩展加载器上下文.md) 实现。

[详细说明](P021_缓冲区加载器.md)。

<a id="r_llext_5Ffs_5Floader"></a>

```c
struct llext_fs_loader
```

从文件系统（File System）读取数据的 [`llext_loader`](P025_扩展加载器上下文.md) 实现。

[详细说明](P023_文件系统加载器.md)。

<a id="r_llext_5Floader"></a>

```c
struct llext_loader
```

可链接加载扩展的加载器上下文（Loader Context）。

[详细说明](P025_扩展加载器上下文.md)。

<a id="r_llext_5Fsemihost_5Floader"></a>

```c
struct llext_semihost_loader
```

通过半主机（Semihosting）读取数据的 [`llext_loader`](P025_扩展加载器上下文.md) 实现。

[详细说明](P026_半主机加载器.md)。

## 14.4\_LLEXT\_BUF\_LOADER

<a id="ga9ca06c7c3e57f5284ce44c62f5cc2c02"></a>
<a id="r_ga9ca06c7c3e57f5284ce44c62f5cc2c02"></a>

```c
#define LLEXT_BUF_LOADER( _buf, _buf_len )
```

展开值（Value）：

```c
Z_LLEXT_BUF_LOADER(_buf, _buf_len,                                                         \
                   IS_ENABLED(CONFIG_LLEXT_STORAGE_WRITABLE) ?                             \
                        LLEXT_STORAGE_WRITABLE : LLEXT_STORAGE_PERSISTENT)
```

```c
#include <zephyr/llext/buf_loader.h>
```

[`llext_buf_loader`](P021_缓冲区加载器.md) 结构体的初始化器。

所提供缓冲区的存储类型取决于 [`CONFIG_LLEXT_STORAGE_WRITABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLEXT_STORAGE_WRITABLE) 选项：定义此选项时将缓冲区视为可写，否则视为持久存储（Persistent Storage）。

可以考虑使用下面列出的替代宏之一。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_buf` | 包含 `ELF` 二进制的缓冲区。 |
| `_buf_len` | 缓冲区长度，单位为字节。 |

**参见（See Also）**：另见 [`LLEXT_TEMPORARY_BUF_LOADER`](#ga8485b4dfecbd2eff3e21b5958d5e8699)、[`LLEXT_PERSISTENT_BUF_LOADER`](#ga2c2214bcf1506f1209476619e42114b3)、[`LLEXT_WRITABLE_BUF_LOADER`](#gac726727897e02bca0bf5d32f4c66be55)。

## 14.5\_LLEXT\_FS\_LOADER

<a id="ga25a394fb7f7f93cfe3ab92d8ed4a6bff"></a>
<a id="r_ga25a394fb7f7f93cfe3ab92d8ed4a6bff"></a>

```c
#define LLEXT_FS_LOADER( _filename)
```

展开值（Value）：

```c
{                                                                                          \
        .loader =                                                                          \
                {                                                                          \
                        .prepare = llext_fs_prepare,                                       \
                        .read = llext_fs_read,                                             \
                        .seek = llext_fs_seek,                                             \
                        .peek = NULL,                                                      \
                        .finalize = llext_fs_finalize,                                     \
                        .storage = LLEXT_STORAGE_TEMPORARY,                                \
                },                                                                         \
        .is_open = false,                                                                  \
        .name = (_filename),                                                               \
}
```

```c
#include <zephyr/llext/fs_loader.h>
```

[`llext_fs_loader`](P023_文件系统加载器.md) 结构体的初始化器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_filename` | 扩展文件的绝对路径（Absolute Path）。 |

> 译注：这里的“绝对路径”是 API 对目标文件路径的语义要求，不是作者电脑的仓库地址。调用者应根据运行环境和挂载点构造实际路径；源码、译文和资源之间的本地引用仍使用相对路径。

## 14.6\_LLEXT\_PERSISTENT\_BUF\_LOADER

<a id="ga2c2214bcf1506f1209476619e42114b3"></a>
<a id="r_ga2c2214bcf1506f1209476619e42114b3"></a>

```c
#define LLEXT_PERSISTENT_BUF_LOADER( _buf, _buf_len )
```

展开值（Value）：

```c
Z_LLEXT_BUF_LOADER(_buf, _buf_len, LLEXT_STORAGE_PERSISTENT)
```

```c
#include <zephyr/llext/buf_loader.h>
```

为持久、只读缓冲区初始化 [`llext_buf_loader`](P021_缓冲区加载器.md) 结构体。

保证扩展处于已加载状态的整个期间都能访问指定缓冲区中的 `ELF` 数据。只要加载过程不需要修改数据，LLEXT 子系统就可以直接访问这些 `ELF` 数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_buf` | 包含 `ELF` 二进制的缓冲区。 |
| `_buf_len` | 缓冲区长度，单位为字节。 |

## 14.7\_LLEXT\_SEMIHOST\_LOADER

<a id="ga28c2ad64c0b54fdea6130916ca35aec5"></a>
<a id="r_ga28c2ad64c0b54fdea6130916ca35aec5"></a>

```c
#define LLEXT_SEMIHOST_LOADER( _filename)
```

展开值（Value）：

```c
{                                                                                          \
        .loader =                                                                          \
                {                                                                          \
                        .prepare = llext_semihost_prepare,                                 \
                        .read = llext_semihost_read,                                       \
                        .seek = llext_semihost_seek,                                       \
                        .peek = NULL,                                                      \
                        .finalize = llext_semihost_finalize,                               \
                        .storage = LLEXT_STORAGE_TEMPORARY,                                \
                },                                                                         \
        .filename = (_filename),                                                           \
        .fd = -1,                                                                          \
}
```

```c
#include <zephyr/llext/semihost_loader.h>
```

[`llext_semihost_loader`](P026_半主机加载器.md) 结构体的初始化器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_filename` | 扩展文件的路径。 |

## 14.8\_LLEXT\_TEMPORARY\_BUF\_LOADER

<a id="ga8485b4dfecbd2eff3e21b5958d5e8699"></a>
<a id="r_ga8485b4dfecbd2eff3e21b5958d5e8699"></a>

```c
#define LLEXT_TEMPORARY_BUF_LOADER( _buf, _buf_len )
```

展开值（Value）：

```c
Z_LLEXT_BUF_LOADER(_buf, _buf_len, LLEXT_STORAGE_TEMPORARY)
```

```c
#include <zephyr/llext/buf_loader.h>
```

为临时缓冲区（Temporary Buffer）初始化 [`llext_buf_loader`](P021_缓冲区加载器.md) 结构体。

指定缓冲区中的 `ELF` 数据只在 `llext_load`() 期间可用。LLEXT 子系统会在加载时把所有必需数据复制到内部缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_buf` | 包含 `ELF` 二进制的缓冲区。 |
| `_buf_len` | 缓冲区长度，单位为字节。 |

## 14.9\_LLEXT\_WRITABLE\_BUF\_LOADER

<a id="gac726727897e02bca0bf5d32f4c66be55"></a>
<a id="r_gac726727897e02bca0bf5d32f4c66be55"></a>

```c
#define LLEXT_WRITABLE_BUF_LOADER( _buf, _buf_len )
```

展开值（Value）：

```c
Z_LLEXT_BUF_LOADER(_buf, _buf_len, LLEXT_STORAGE_WRITABLE)
```

```c
#include <zephyr/llext/buf_loader.h>
```

为持久、可写缓冲区初始化 [`llext_buf_loader`](P021_缓冲区加载器.md) 结构体。

保证扩展处于已加载状态的整个期间都能访问指定缓冲区中的 `ELF` 数据。LLEXT 子系统可以直接访问和修改这些数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_buf` | 包含 `ELF` 二进制的缓冲区。 |
| `_buf_len` | 缓冲区长度，单位为字节。 |

## 14.10\_llext\_storage\_type

<a id="ga8e04f364aef19cf45843cc97cc702f24"></a>
<a id="r_ga8e04f364aef19cf45843cc97cc702f24"></a>

```c
enum llext_storage_type
```

```c
#include <zephyr/llext/loader.h>
```

待加载 `ELF` 数据的存储类型（Storage Type）。

本枚举定义待加载 `ELF` 数据的存储类型。存储类型决定 LLEXT 子系统在加载过程中可以尝试哪些内存优化。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LLEXT_STORAGE_TEMPORARY` | `ELF` 数据只在 `llext_load`() 期间可用；即使加载器支持通过 `llext_peek`() 直接访问内存，缓冲区内容在此后也会被丢弃。 LLEXT 会在自己的堆中为所有必需数据分配副本。 |
| `LLEXT_STORAGE_PERSISTENT` | `ELF` 数据存于只读缓冲区，保证扩展处于已加载状态的整个期间始终可访问。 LLEXT 可以直接复用缓冲区中的常量数据，但如果需要应用重定位，仍可能分配副本。 |
| `LLEXT_STORAGE_WRITABLE` | `ELF` 数据存于可写内存缓冲区，保证扩展处于已加载状态的整个期间始终可访问。 LLEXT 可以自由修改和复用缓冲区数据，因此扩展卸载后，在下一次调用 `llext_load`() 前应重新初始化缓冲区内容。 |

**原文注意（Note）**：即使选择限制最少的选项，LLEXT 仍可能为了遵守硬件内存保护、对齐规则（Alignment Rules）等约束，把 `ELF` 数据复制到独立内存区域。BSS 等不占文件空间的节也会在 LLEXT 堆中分配。

## 14.11\_源码对照与相关阅读

译注：本仓库的[loader.h](../../../include/zephyr/llext/loader.h)可用于跟踪声明与实现。此相对路径从本文位置解析，不绑定盘符或用户名；本仓库参照源码不自动等同于网页 latest 的版本。

[加载流程](P004_加载扩展.md) · [管理API](P011_扩展管理API.md) · [ELF检查接口](P013_ELF检查API.md) · [加载器上下文](P025_扩展加载器上下文.md) · [符号表](P028_符号表.md)。

<a id="header-files"></a>
<a id="files"></a>
<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__llext__loader__apis_html_gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b"></a>
<a id="agroup__llext__loader__apis_html_gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__llext__loader__apis_html_gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6"></a>
<a id="gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0"></a>
<a id="gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b"></a>

[上一章](P013_ELF检查API.md) · [返回大纲](大纲.md) · [下一章](P015_导出符号API.md)
