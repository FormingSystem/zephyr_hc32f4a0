---
id: learning.zephyr-docs.system-service-model-reference.page-41
title: gdb_mem_region_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_gdb\_mem\_region\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述一个内存区域。

```c
#include <zephyr/debug/gdbstub.h>
```

<a id="details"></a>

描述一个内存区域。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a463465123fd373996a857b38c71474b3"></a>

```c
uintptr_t start
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[start](#a463465123fd373996a857b38c71474b3)。

内存区域的起始地址。

<a id="r_a16001ef766b3c5775c1d1b2c59575b74"></a>

```c
uintptr_t end
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[end](#a16001ef766b3c5775c1d1b2c59575b74)。

内存区域的结束地址。

<a id="r_ad8ae6acf6950428a9846a25fb0219eeb"></a>

```c
uint16_t attributes
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[attributes](#ad8ae6acf6950428a9846a25fb0219eeb)。

内存区域属性。

<a id="r_aa714bde657eb3572367a924298dd927f"></a>

```c
uint8_t alignment
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[alignment](#aa714bde657eb3572367a924298dd927f)。

读写对齐要求；使用默认对齐时为 0。

## 41.2\_详细说明（Detailed Documentation）

<a id="aa714bde657eb3572367a924298dd927f"></a>

### `alignment`

```c
uint8_t gdb_mem_region::alignment
```

读写对齐要求；使用默认对齐时为 0。

<a id="ad8ae6acf6950428a9846a25fb0219eeb"></a>

### `attributes`

```c
uint16_t gdb_mem_region::attributes
```

内存区域属性。

<a id="a16001ef766b3c5775c1d1b2c59575b74"></a>

### `end`

```c
uintptr_t gdb_mem_region::end
```

内存区域的结束地址。

<a id="a463465123fd373996a857b38c71474b3"></a>

### `start`

```c
uintptr_t gdb_mem_region::start
```

内存区域的起始地址。

本数据类型文档由以下文件生成：

- `zephyr/debug/gdbstub.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/debug/gdbstub.h](../debug_headers_reference/P006_GDB调试桩头文件源码.md)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_fs_mgmt_hash_checksum_group_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_img_gr_upload_结构体.md)
