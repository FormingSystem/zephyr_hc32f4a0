---
id: learning.zephyr-docs.posix-system-model-reference.page-34
title: zvfs_stat_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzvfs__stat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zvfs\_stat\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structzvfs__stat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ZFD_IOCTL_STAT ioctl调用结果的结构。

```c
#include <zephyr/sys/fdtable.h>
```

<a id="details"></a>

`ZFD_IOCTL_STAT` ioctl 调用结果的结构体，包含目前支持的所有详细信息字段。定义此结构体是为了避免对 POSIX 的依赖。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a2e1288c3dd903b7200d9d8dba07454f4"></a>

```c
off_t size
```

相关声明：[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[size](#a2e1288c3dd903b7200d9d8dba07454f4)。

<a id="r_a24a28a774b55ce0a335ca58539a94877"></a>

```c
uint32_t mode
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mode](#a24a28a774b55ce0a335ca58539a94877)。

## 34.2\_详细说明（Detailed Documentation）

<a id="a24a28a774b55ce0a335ca58539a94877"></a>

### `mode`

```c
uint32_t zvfs_stat::mode
```

<a id="a2e1288c3dd903b7200d9d8dba07454f4"></a>

### `size`

```c
off_t zvfs_stat::size
```

本数据类型文档由以下文件生成：

- `zephyr/sys/fdtable.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h_source.html)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_zvfs_pollfd_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_sigval_联合体.md)
