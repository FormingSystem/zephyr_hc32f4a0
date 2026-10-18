---
id: learning.zephyr-docs.llext.api-12
title: ELF常量与类型
kind: reference
status: maintained
domains: [zephyr, llext, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__llext__elf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_ELF常量与类型

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__elf.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 12.1\_概述

本页列出可执行与可链接格式（Executable and Linkable Format，`ELF`）的常量与数据类型。

## 12.2\_关联声明与说明

<a id="r_elf32_5Fehdr"></a>

```c
struct elf32_ehdr
```

32 位`ELF`头（`ELF` Header）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__ehdr.html)。

<a id="r_elf64_5Fehdr"></a>

```c
struct elf64_ehdr
```

64 位`ELF`头（`ELF` Header）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__ehdr.html)。

<a id="r_elf32_5Fshdr"></a>

```c
struct elf32_shdr
```

32 位节头（Section Header）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__shdr.html)。

<a id="r_elf64_5Fshdr"></a>

```c
struct elf64_shdr
```

64 位节头（Section Header）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__shdr.html)。

<a id="r_elf32_5Fsym"></a>

```c
struct elf32_sym
```

32 位符号表条目（Symbol Table Entry）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__sym.html)。

<a id="r_elf64_5Fsym"></a>

```c
struct elf64_sym
```

64 位符号表条目（Symbol Table Entry）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__sym.html)。

<a id="r_elf32_5Frel"></a>

```c
struct elf32_rel
```

32 位 `ELF` 的重定位条目（Relocation Entry）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__rel.html)。

<a id="r_elf32_5Frela"></a>

```c
struct elf32_rela
```

32 位 `ELF` 中带加数的重定位条目（Relocation Entry with Addend）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__rela.html)。

<a id="r_elf64_5Frel"></a>

```c
struct elf64_rel
```

64 位 `ELF` 的重定位条目（Relocation Entry）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__rel.html)。

<a id="r_elf64_5Frela"></a>

```c
struct elf64_rela
```

64 位 `ELF` 中带加数的重定位条目（Relocation Entry with Addend）。

[详细说明](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__rela.html)。

## 12.3\_EI\_NIDENT

<a id="gae407130db14180c6737390604ba7c1fe"></a>
<a id="r_gae407130db14180c6737390604ba7c1fe"></a>

```c
#define EI_NIDENT 16
```

```c
#include <zephyr/llext/elf.h>
```

`ELF` 标识块（Identifier Block）。

4 字节魔数（Magic，原文记作 .`ELF`）；1 字节类别（无效、32 位、64 位）；1 字节字节序（Endianness：无效、LSB 小端、MSB 大端）；1 字节版本（1）；1 字节操作系统应用二进制接口（OS ABI：0 无、1 HP-UX、2 NetBSD、3 Linux）；1 字节 ABI（0）；7 字节填充（Padding）。

> 译注：原文用 .`ELF` 表示魔数；`ELF` 文件开头的实际四个字节为 0x7f、E、L、F。“1 字节 ABI”一项按原文保留。

## 12.4\_ELF32\_R\_SYM

<a id="ga8d1ac0f35a8999a4a8a3350ca95ab54b"></a>
<a id="r_ga8d1ac0f35a8999a4a8a3350ca95ab54b"></a>

```c
#define ELF32_R_SYM( i)
```

展开值（Value）：

```c
((i) >> 8)
```

```c
#include <zephyr/llext/elf.h>
```

从 `r_info` 取得重定位符号索引（Relocation Symbol Index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `i` | `r_info` 的值。 |

## 12.5\_ELF32\_R\_TYPE

<a id="gaa4ffd69f2c1c03229686bfa3a898db00"></a>
<a id="r_gaa4ffd69f2c1c03229686bfa3a898db00"></a>

```c
#define ELF32_R_TYPE( i)
```

展开值（Value）：

```c
((i) & 0xff)
```

```c
#include <zephyr/llext/elf.h>
```

从 `r_info` 取得重定位类型（Relocation Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `i` | `r_info` 的值。 |

## 12.6\_ELF32\_ST\_BIND

<a id="ga3b84f3e0e035d1264115f5c76227c5eb"></a>
<a id="r_ga3b84f3e0e035d1264115f5c76227c5eb"></a>

```c
#define ELF32_ST_BIND( i)
```

展开值（Value）：

```c
((i) >> 4)
```

```c
#include <zephyr/llext/elf.h>
```

从 32 位 `ELF` 的 `st_info` 取得符号绑定（Symbol Binding）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `i` | `st_info` 的值。 |

> 译注：这里的“32 位”指 `ELF` 类别；不表示 `st_info` 字段自身占 32 位。

## 12.7\_ELF32\_ST\_TYPE

<a id="ga54dd2783f11c5f926d8db9250e1baa35"></a>
<a id="r_ga54dd2783f11c5f926d8db9250e1baa35"></a>

```c
#define ELF32_ST_TYPE( i)
```

展开值（Value）：

```c
((i) & 0xf)
```

```c
#include <zephyr/llext/elf.h>
```

从 32 位 `ELF` 的 `st_info` 取得符号类型（Symbol Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `i` | `st_info` 的值。 |

> 译注：这里的“32 位”指 `ELF` 类别；不表示 `st_info` 字段自身占 32 位。

## 12.8\_ELF64\_R\_SYM

<a id="gab8a1253bfcc928f9aa9d4177d84f6830"></a>
<a id="r_gab8a1253bfcc928f9aa9d4177d84f6830"></a>

```c
#define ELF64_R_SYM( i)
```

展开值（Value）：

```c
((i) >> 32)
```

```c
#include <zephyr/llext/elf.h>
```

从 `r_info` 取得重定位符号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `i` | `r_info` 的值。 |

> 译注：原文简称“symbol”，展开式实际从 `r_info` 取出符号索引。

## 12.9\_ELF64\_R\_TYPE

<a id="ga51aeadee885873fec9a218c058fe9e09"></a>
<a id="r_ga51aeadee885873fec9a218c058fe9e09"></a>

```c
#define ELF64_R_TYPE( i)
```

展开值（Value）：

```c
((i) & 0xffffffff)
```

```c
#include <zephyr/llext/elf.h>
```

从 `r_info` 取得重定位类型（Relocation Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `i` | `r_info` 的值。 |

## 12.10\_ELF64\_ST\_BIND

<a id="ga630907a2afaf3aea5441635416cdb037"></a>
<a id="r_ga630907a2afaf3aea5441635416cdb037"></a>

```c
#define ELF64_ST_BIND( i)
```

展开值（Value）：

```c
((i) >> 4)
```

```c
#include <zephyr/llext/elf.h>
```

从 32 位 `ELF` 的 `st_info` 取得符号绑定（Symbol Binding）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `i` | `st_info` 的值。 |

> 译注：原文此处写作“32bit `st_info`”，但宏名及展开对应 `ELF64`。此处保留原文措辞并指出该差异；不应将其误读为只能用于 `ELF32`。

## 12.11\_ELF64\_ST\_TYPE

<a id="ga46a82febd2ecb9d8a0cd39810370a11b"></a>
<a id="r_ga46a82febd2ecb9d8a0cd39810370a11b"></a>

```c
#define ELF64_ST_TYPE( i)
```

展开值（Value）：

```c
((i) & 0xf)
```

```c
#include <zephyr/llext/elf.h>
```

从 32 位 `ELF` 的 `st_info` 取得符号类型（Symbol Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `i` | `st_info` 的值。 |

> 译注：原文此处写作“32bit `st_info`”，但宏名及展开对应 `ELF64`。此处保留原文措辞并指出该差异。

## 12.12\_ELF\_R\_SYM

<a id="ga8d3fc5bbbc767d0e484843f6831659cf"></a>
<a id="r_ga8d3fc5bbbc767d0e484843f6831659cf"></a>

```c
#define ELF_R_SYM ELF64_R_SYM
```

```c
#include <zephyr/llext/elf.h>
```

按机器位宽选择、用于取得重定位符号的宏别名。

> 译注：下列机器位宽别名在原网页中展示 `ELF64` 分支，不表示所有目标都使用 64 位 `ELF`；见本章源码对照。

## 12.13\_ELF\_R\_TYPE

<a id="gae91c561e4921f0a1cf5868d775ac3243"></a>
<a id="r_gae91c561e4921f0a1cf5868d775ac3243"></a>

```c
#define ELF_R_TYPE ELF64_R_TYPE
```

```c
#include <zephyr/llext/elf.h>
```

按机器位宽选择、用于取得重定位类型的宏别名。

## 12.14\_ELF\_ST\_BIND

<a id="ga5370d61077b153ba6b515994e185b9f8"></a>
<a id="r_ga5370d61077b153ba6b515994e185b9f8"></a>

```c
#define ELF_ST_BIND ELF64_ST_BIND
```

```c
#include <zephyr/llext/elf.h>
```

按机器位宽选择、用于取得符号绑定的宏别名。

> 译注：本页按 Doxygen 构建分支展示 64 位别名。本仓库相对链接中的 elf.h 在 `CONFIG_64BIT` 或 __DOXYGEN__ 条件下选择 `ELF64`，否则选择 `ELF32`；实际工程须以自身版本和配置为准。

## 12.15\_ELF\_ST\_TYPE

<a id="ga972d66fcb6578448641a95d7a321dc4b"></a>
<a id="r_ga972d66fcb6578448641a95d7a321dc4b"></a>

```c
#define ELF_ST_TYPE ELF64_ST_TYPE
```

```c
#include <zephyr/llext/elf.h>
```

按机器位宽选择、用于取得符号类型的宏别名。

> 译注：机器位宽别名的选择与目标配置有关，不能只依据文档生成时展示的 `ELF64` 分支。

## 12.16\_ET\_CORE

<a id="ga2b9430d26ba60f7a9d65c8d43e54f213"></a>
<a id="r_ga2b9430d26ba60f7a9d65c8d43e54f213"></a>

```c
#define ET_CORE 4
```

```c
#include <zephyr/llext/elf.h>
```

核心转储（Core Dump）。

## 12.17\_ET\_DYN

<a id="ga4373ea3b3d512434ebe2213829b6751b"></a>
<a id="r_ga4373ea3b3d512434ebe2213829b6751b"></a>

```c
#define ET_DYN 3
```

```c
#include <zephyr/llext/elf.h>
```

动态 `ELF`：采用位置无关代码／位置无关可执行文件（Position-independent Code / Executable，PIC/PIE）的可执行文件，或共享库（Shared Library）。

## 12.18\_ET\_EXEC

<a id="ga942478985eb016311380dee473cc8c3e"></a>
<a id="r_ga942478985eb016311380dee473cc8c3e"></a>

```c
#define ET_EXEC 2
```

```c
#include <zephyr/llext/elf.h>
```

不采用 PIC/PIE 的可执行 `ELF`。

## 12.19\_ET\_REL

<a id="ga2a91046a80fd753ce3dbfb109212761d"></a>
<a id="r_ga2a91046a80fd753ce3dbfb109212761d"></a>

```c
#define ET_REL 1
```

```c
#include <zephyr/llext/elf.h>
```

可重定位、尚未链接的 `ELF`（Relocatable `ELF`）。

## 12.20\_SHF\_ALLOC

<a id="ga38476fe4ed88ac83ba86a4e103199a86"></a>
<a id="r_ga38476fe4ed88ac83ba86a4e103199a86"></a>

```c
#define SHF_ALLOC 0x2
```

```c
#include <zephyr/llext/elf.h>
```

此节存在于内存中。

## 12.21\_SHF\_BASIC\_TYPE\_MASK

<a id="gaa5c0c2a95b20eb3cb19e7fc2c7f530d3"></a>
<a id="r_gaa5c0c2a95b20eb3cb19e7fc2c7f530d3"></a>

```c
#define SHF_BASIC_TYPE_MASK (SHF_WRITE | SHF_ALLOC | SHF_EXECINSTR)
```

```c
#include <zephyr/llext/elf.h>
```

用于选取基本节标志的掩码（Mask）。

## 12.22\_SHF\_EXECINSTR

<a id="gab3780594e35fbbc6e5028bcb921d0a76"></a>
<a id="r_gab3780594e35fbbc6e5028bcb921d0a76"></a>

```c
#define SHF_EXECINSTR 0x4
```

```c
#include <zephyr/llext/elf.h>
```

此节包含可执行指令。

## 12.23\_SHF\_LLEXT\_HAS\_RELOCS

<a id="ga95aa40c864bee18890240242b7da94f6"></a>
<a id="r_ga95aa40c864bee18890240242b7da94f6"></a>

```c
#define SHF_LLEXT_HAS_RELOCS 0x00100000
```

```c
#include <zephyr/llext/elf.h>
```

此节是重定位的目标。

## 12.24\_SHF\_MASKOS

<a id="gac28c1d15309ad8127ac3e7cb984bc195"></a>
<a id="r_gac28c1d15309ad8127ac3e7cb984bc195"></a>

```c
#define SHF_MASKOS 0x0ff00000
```

```c
#include <zephyr/llext/elf.h>
```

操作系统专用标志（OS-specific Flags）。

## 12.25\_SHF\_TLS

<a id="ga2484a824af96dca3fb77c4fb8898e83b"></a>
<a id="r_ga2484a824af96dca3fb77c4fb8898e83b"></a>

```c
#define SHF_TLS 0x400
```

```c
#include <zephyr/llext/elf.h>
```

此节保存线程局部存储（Thread-local Storage，TLS）。

## 12.26\_SHF\_WRITE

<a id="ga025c79223b0fee4676337d660f76b59b"></a>
<a id="r_ga025c79223b0fee4676337d660f76b59b"></a>

```c
#define SHF_WRITE 0x1
```

```c
#include <zephyr/llext/elf.h>
```

`ELF` 节标志（Section Flags）。

此节可写。

## 12.27\_SHN\_ABS

<a id="ga322030426afae1a37a8ba1ab86a39066"></a>
<a id="r_ga322030426afae1a37a8ba1ab86a39066"></a>

```c
#define SHN_ABS 0xfff1
```

```c
#include <zephyr/llext/elf.h>
```

绝对符号（Absolute Symbol）的特殊值。

## 12.28\_SHN\_COMMON

<a id="ga3d62721d3fe66370be9ec0ca0764ec7b"></a>
<a id="r_ga3d62721d3fe66370be9ec0ca0764ec7b"></a>

```c
#define SHN_COMMON 0xfff2
```

```c
#include <zephyr/llext/elf.h>
```

公共块（Common Block）。

## 12.29\_SHN\_HIRESERVE

<a id="gaaac4804ef07b9da1d840d951469692f0"></a>
<a id="r_gaaac4804ef07b9da1d840d951469692f0"></a>

```c
#define SHN_HIRESERVE 0xffff
```

```c
#include <zephyr/llext/elf.h>
```

保留节编号范围的末端。

## 12.30\_SHN\_LORESERVE

<a id="gac663b490fedc8aeab91bf941772ba306"></a>
<a id="r_gac663b490fedc8aeab91bf941772ba306"></a>

```c
#define SHN_LORESERVE 0xff00
```

```c
#include <zephyr/llext/elf.h>
```

保留节编号范围的起点。

## 12.31\_SHN\_UNDEF

<a id="gab2f25695673c5f1c4ec723e595288411"></a>
<a id="r_gab2f25695673c5f1c4ec723e595288411"></a>

```c
#define SHN_UNDEF 0
```

```c
#include <zephyr/llext/elf.h>
```

`ELF` 节编号（Section Numbers）。

未定义节。

## 12.32\_SHT\_DYNSYM

<a id="gaa9949aedf49107f6a07e618d5d791d40"></a>
<a id="r_gaa9949aedf49107f6a07e618d5d791d40"></a>

```c
#define SHT_DYNSYM 0xB
```

```c
#include <zephyr/llext/elf.h>
```

动态链接符号表（Dynamic Linking Symbol Table）。

## 12.33\_SHT\_FINI\_ARRAY

<a id="ga09b4d64e68fc2a9ac211589c377ed76a"></a>
<a id="r_ga09b4d64e68fc2a9ac211589c377ed76a"></a>

```c
#define SHT_FINI_ARRAY 0xf
```

```c
#include <zephyr/llext/elf.h>
```

终止函数指针数组（Termination Function Pointer Array）。

## 12.34\_SHT\_INIT\_ARRAY

<a id="gaa0269f148b09419d27be6289b4ce026f"></a>
<a id="r_gaa0269f148b09419d27be6289b4ce026f"></a>

```c
#define SHT_INIT_ARRAY 0xe
```

```c
#include <zephyr/llext/elf.h>
```

初始化函数指针数组。

## 12.35\_SHT\_NOBITS

<a id="ga820ff00317949be2ea1fd634a17dc13e"></a>
<a id="r_ga820ff00317949be2ea1fd634a17dc13e"></a>

```c
#define SHT_NOBITS 0x8
```

```c
#include <zephyr/llext/elf.h>
```

没有文件映像（File Image）的程序数据。

## 12.36\_SHT\_NULL

<a id="ga1566f4c14cff9f4b539b00af54d62dbb"></a>
<a id="r_ga1566f4c14cff9f4b539b00af54d62dbb"></a>

```c
#define SHT_NULL 0x0
```

```c
#include <zephyr/llext/elf.h>
```

`ELF` 节类型（Section Types）。

未使用的节。

## 12.37\_SHT\_PREINIT\_ARRAY

<a id="gaa7326ce59e1988302584ba6ac9772c32"></a>
<a id="r_gaa7326ce59e1988302584ba6ac9772c32"></a>

```c
#define SHT_PREINIT_ARRAY 0x10
```

```c
#include <zephyr/llext/elf.h>
```

早期初始化函数指针数组。

## 12.38\_SHT\_PROGBITS

<a id="ga4bff22edbae51353ba9b3572d424b91a"></a>
<a id="r_ga4bff22edbae51353ba9b3572d424b91a"></a>

```c
#define SHT_PROGBITS 0x1
```

```c
#include <zephyr/llext/elf.h>
```

程序数据（Program Data）。

## 12.39\_SHT\_REL

<a id="ga2aea2ed985f81f13a157fe2da02a621a"></a>
<a id="r_ga2aea2ed985f81f13a157fe2da02a621a"></a>

```c
#define SHT_REL 0x9
```

```c
#include <zephyr/llext/elf.h>
```

不带加数（Addend）的重定位条目。

## 12.40\_SHT\_RELA

<a id="gabf2fc2781a2869352c2ffa0555f34118"></a>
<a id="r_gabf2fc2781a2869352c2ffa0555f34118"></a>

```c
#define SHT_RELA 0x4
```

```c
#include <zephyr/llext/elf.h>
```

带加数（Addend）的重定位条目。

## 12.41\_SHT\_STRTAB

<a id="gaf4b916dc4ca5016fb5c374068002a532"></a>
<a id="r_gaf4b916dc4ca5016fb5c374068002a532"></a>

```c
#define SHT_STRTAB 0x3
```

```c
#include <zephyr/llext/elf.h>
```

字符串表（String Table）。

## 12.42\_SHT\_SYMTAB

<a id="ga4add7784e43ec3d3b9c09d3ffc476a81"></a>
<a id="r_ga4add7784e43ec3d3b9c09d3ffc476a81"></a>

```c
#define SHT_SYMTAB 0x2
```

```c
#include <zephyr/llext/elf.h>
```

符号表（Symbol Table）。

## 12.43\_STB\_GLOBAL

<a id="ga8091960a6799bf71a7494551dac1a2e8"></a>
<a id="r_ga8091960a6799bf71a7494551dac1a2e8"></a>

```c
#define STB_GLOBAL 1
```

```c
#include <zephyr/llext/elf.h>
```

全局符号（Global Symbol）。

## 12.44\_STB\_HIOS

<a id="ga934c6e5a5405f46e343d8493a4f8f6d7"></a>
<a id="r_ga934c6e5a5405f46e343d8493a4f8f6d7"></a>

```c
#define STB_HIOS 12
```

```c
#include <zephyr/llext/elf.h>
```

操作系统专用范围的末端。

## 12.45\_STB\_HIPROC

<a id="ga5fa61266452365ab0e2d2ad32b87043e"></a>
<a id="r_ga5fa61266452365ab0e2d2ad32b87043e"></a>

```c
#define STB_HIPROC 15
```

```c
#include <zephyr/llext/elf.h>
```

处理器专用范围的末端。

## 12.46\_STB\_LOCAL

<a id="ga72c40de459931e6f1d041201dc7398b1"></a>
<a id="r_ga72c40de459931e6f1d041201dc7398b1"></a>

```c
#define STB_LOCAL 0
```

```c
#include <zephyr/llext/elf.h>
```

符号表条目的绑定方式（Symbol Table Entry Binding）。

局部符号（Local Symbol）。

## 12.47\_STB\_LOOS

<a id="gab764e4fb4280d76967bf382a17d5b1d1"></a>
<a id="r_gab764e4fb4280d76967bf382a17d5b1d1"></a>

```c
#define STB_LOOS 10
```

```c
#include <zephyr/llext/elf.h>
```

操作系统专用范围的起点。

## 12.48\_STB\_LOPROC

<a id="ga4f4d0360fcb960e31e119973a472010e"></a>
<a id="r_ga4f4d0360fcb960e31e119973a472010e"></a>

```c
#define STB_LOPROC 13
```

```c
#include <zephyr/llext/elf.h>
```

处理器专用范围的起点。

## 12.49\_STB\_WEAK

<a id="gad4247ded90f9371e3c4d2f7dda260c93"></a>
<a id="r_gad4247ded90f9371e3c4d2f7dda260c93"></a>

```c
#define STB_WEAK 2
```

```c
#include <zephyr/llext/elf.h>
```

弱符号（Weak Symbol）。

## 12.50\_STT\_COMMON

<a id="ga0067af965ad01b11be77380eed14efb8"></a>
<a id="r_ga0067af965ad01b11be77380eed14efb8"></a>

```c
#define STT_COMMON 5
```

```c
#include <zephyr/llext/elf.h>
```

公共块（Common Block）。

## 12.51\_STT\_FILE

<a id="ga983395f99446fa4d398c4e902bec34c6"></a>
<a id="r_ga983395f99446fa4d398c4e902bec34c6"></a>

```c
#define STT_FILE 4
```

```c
#include <zephyr/llext/elf.h>
```

文件名（File Name）。

## 12.52\_STT\_FUNC

<a id="ga9cdfedf900935f23f6e409ce378dc1d2"></a>
<a id="r_ga9cdfedf900935f23f6e409ce378dc1d2"></a>

```c
#define STT_FUNC 2
```

```c
#include <zephyr/llext/elf.h>
```

函数（Function）。

## 12.53\_STT\_HIOS

<a id="ga6de042ae014d95d7b9e0649e0ecfff8e"></a>
<a id="r_ga6de042ae014d95d7b9e0649e0ecfff8e"></a>

```c
#define STT_HIOS 12
```

```c
#include <zephyr/llext/elf.h>
```

操作系统专用范围的末端。

## 12.54\_STT\_HIPROC

<a id="ga5bf951d9b37f10dfe17a1bd6b4489599"></a>
<a id="r_ga5bf951d9b37f10dfe17a1bd6b4489599"></a>

```c
#define STT_HIPROC 15
```

```c
#include <zephyr/llext/elf.h>
```

处理器专用范围的末端。

## 12.55\_STT\_LOOS

<a id="gaebb605da5285a99f7475cb17214955a2"></a>
<a id="r_gaebb605da5285a99f7475cb17214955a2"></a>

```c
#define STT_LOOS 10
```

```c
#include <zephyr/llext/elf.h>
```

操作系统专用范围的起点。

## 12.56\_STT\_LOPROC

<a id="gaeb49b6a738078d32e5979885e26c4ddf"></a>
<a id="r_gaeb49b6a738078d32e5979885e26c4ddf"></a>

```c
#define STT_LOPROC 13
```

```c
#include <zephyr/llext/elf.h>
```

处理器专用范围的起点。

## 12.57\_STT\_NOTYPE

<a id="gaa15a54cc9c881e4d54daedc9d984c2fc"></a>
<a id="r_gaa15a54cc9c881e4d54daedc9d984c2fc"></a>

```c
#define STT_NOTYPE 0
```

```c
#include <zephyr/llext/elf.h>
```

符号表条目的类型。

没有类型。

## 12.58\_STT\_OBJECT

<a id="gac236cc313291ed38ecb346a8b4bde6b2"></a>
<a id="r_gac236cc313291ed38ecb346a8b4bde6b2"></a>

```c
#define STT_OBJECT 1
```

```c
#include <zephyr/llext/elf.h>
```

数据或对象（Data or Object）。

## 12.59\_STT\_SECTION

<a id="ga9e9a3c0fa59c3fc896f8e4c1872c6af1"></a>
<a id="r_ga9e9a3c0fa59c3fc896f8e4c1872c6af1"></a>

```c
#define STT_SECTION 3
```

```c
#include <zephyr/llext/elf.h>
```

节（Section）。

## 12.60\_elf32\_addr

<a id="ga55f1dc601c95381307fddd5969969634"></a>
<a id="r_ga55f1dc601c95381307fddd5969969634"></a>

```c
typedef uint32_t elf32_addr
```

```c
#include <zephyr/llext/elf.h>
```

无符号程序地址（Unsigned Program Address）。

## 12.61\_elf32\_half

<a id="ga141d58f50804ef53e0d9bd13fcb36424"></a>
<a id="r_ga141d58f50804ef53e0d9bd13fcb36424"></a>

```c
typedef uint16_t elf32_half
```

```c
#include <zephyr/llext/elf.h>
```

无符号中等长度整数（Unsigned Medium Integer）。

## 12.62\_elf32\_off

<a id="gabb40eb5ffbe88010885da1c8c7b869e3"></a>
<a id="r_gabb40eb5ffbe88010885da1c8c7b869e3"></a>

```c
typedef uint32_t elf32_off
```

```c
#include <zephyr/llext/elf.h>
```

无符号文件偏移量。

## 12.63\_elf32\_sword

<a id="ga1325c85290908b89a9c2b9bdd1aa2efd"></a>
<a id="r_ga1325c85290908b89a9c2b9bdd1aa2efd"></a>

```c
typedef int32_t elf32_sword
```

```c
#include <zephyr/llext/elf.h>
```

有符号整数（Signed Integer）。

## 12.64\_elf32\_word

<a id="gac786571f50a02299b19c1a16d658ea72"></a>
<a id="r_gac786571f50a02299b19c1a16d658ea72"></a>

```c
typedef uint32_t elf32_word
```

```c
#include <zephyr/llext/elf.h>
```

无符号整数（Unsigned Integer）。

## 12.65\_elf64\_addr

<a id="ga42c555ace34b21c1773c9e59228e9929"></a>
<a id="r_ga42c555ace34b21c1773c9e59228e9929"></a>

```c
typedef uint64_t elf64_addr
```

```c
#include <zephyr/llext/elf.h>
```

无符号程序地址（Unsigned Program Address）。

## 12.66\_elf64\_half

<a id="ga3358e1392fd861af8a7c8248519717a0"></a>
<a id="r_ga3358e1392fd861af8a7c8248519717a0"></a>

```c
typedef uint16_t elf64_half
```

```c
#include <zephyr/llext/elf.h>
```

无符号中等长度整数（Unsigned Medium Integer）。

## 12.67\_elf64\_off

<a id="ga7f982d835a34713a84907873f9e058a9"></a>
<a id="r_ga7f982d835a34713a84907873f9e058a9"></a>

```c
typedef uint64_t elf64_off
```

```c
#include <zephyr/llext/elf.h>
```

无符号文件偏移量。

## 12.68\_elf64\_sword

<a id="ga31413d6e89616f2d0356abd533b0c5a1"></a>
<a id="r_ga31413d6e89616f2d0356abd533b0c5a1"></a>

```c
typedef int32_t elf64_sword
```

```c
#include <zephyr/llext/elf.h>
```

有符号整数（Signed Integer）。

## 12.69\_elf64\_sxword

<a id="ga3e687a252b2bb6ed11ea9bc2fa6b728e"></a>
<a id="r_ga3e687a252b2bb6ed11ea9bc2fa6b728e"></a>

```c
typedef int64_t elf64_sxword
```

```c
#include <zephyr/llext/elf.h>
```

有符号长整数（Signed Long Integer）。

## 12.70\_elf64\_word

<a id="gaabf3a740e51b02fbaf40bedfba35e476"></a>
<a id="r_gaabf3a740e51b02fbaf40bedfba35e476"></a>

```c
typedef uint32_t elf64_word
```

```c
#include <zephyr/llext/elf.h>
```

无符号整数（Unsigned Integer）。

## 12.71\_elf64\_xword

<a id="ga68e4179ac3b1c52c28c6e3e5c2a1838a"></a>
<a id="r_ga68e4179ac3b1c52c28c6e3e5c2a1838a"></a>

```c
typedef uint64_t elf64_xword
```

```c
#include <zephyr/llext/elf.h>
```

无符号长整数（Unsigned Long Integer）。

## 12.72\_elf\_addr

<a id="ga9f98ad5b44106cacfd013f43f29a2eff"></a>
<a id="r_ga9f98ad5b44106cacfd013f43f29a2eff"></a>

```c
typedef elf64_addr elf_addr
```

```c
#include <zephyr/llext/elf.h>
```

与机器位宽匹配的程序地址。

## 12.73\_elf\_ehdr\_t

<a id="gab39a1763256a6b9ccccf8b89836cd192"></a>
<a id="r_gab39a1763256a6b9ccccf8b89836cd192"></a>

```c
typedef struct elf64_ehdr elf_ehdr_t
```

```c
#include <zephyr/llext/elf.h>
```

LLEXT 当前未使用动态特性（Dynamic Features）。

与机器位宽匹配的 `ELF` 头结构体（`ELF` Header）。

## 12.74\_elf\_half

<a id="gacb3487f81221d562af45632df161c64e"></a>
<a id="r_gacb3487f81221d562af45632df161c64e"></a>

```c
typedef elf64_half elf_half
```

```c
#include <zephyr/llext/elf.h>
```

与机器位宽配套的小整数类型。

## 12.75\_elf\_phdr\_t

<a id="gad5c63f362ef6b26db73c37980d731c93"></a>
<a id="r_gad5c63f362ef6b26db73c37980d731c93"></a>

```c
typedef struct elf64_phdr elf_phdr_t
```

```c
#include <zephyr/llext/elf.h>
```

与机器位宽匹配的程序头结构体（Program Header）。

## 12.76\_elf\_rel\_t

<a id="gafdcf88be776ec490cf1ec7c286f6202f"></a>
<a id="r_gafdcf88be776ec490cf1ec7c286f6202f"></a>

```c
typedef struct elf64_rel elf_rel_t
```

```c
#include <zephyr/llext/elf.h>
```

与机器位宽匹配的重定位结构体。

## 12.77\_elf\_rela\_t

<a id="gad5dd8960a2fbfc74cdcd016b5c2c7cea"></a>
<a id="r_gad5dd8960a2fbfc74cdcd016b5c2c7cea"></a>

```c
typedef struct elf64_rela elf_rela_t
```

```c
#include <zephyr/llext/elf.h>
```

与机器位宽匹配、带加数的重定位结构体。

## 12.78\_elf\_shdr\_t

<a id="gab3695edd628cf868dc4f0d618f86bcbd"></a>
<a id="r_gab3695edd628cf868dc4f0d618f86bcbd"></a>

```c
typedef struct elf64_shdr elf_shdr_t
```

```c
#include <zephyr/llext/elf.h>
```

与机器位宽匹配的节头结构体。

## 12.79\_elf\_sym\_t

<a id="ga144fdcc270b75a371880da097968555e"></a>
<a id="r_ga144fdcc270b75a371880da097968555e"></a>

```c
typedef struct elf64_sym elf_sym_t
```

```c
#include <zephyr/llext/elf.h>
```

与机器位宽匹配的符号结构体。

## 12.80\_elf\_word

<a id="ga25ad092196ba8d073be66dc7629f8bc3"></a>
<a id="r_ga25ad092196ba8d073be66dc7629f8bc3"></a>

```c
typedef elf64_xword elf_word
```

```c
#include <zephyr/llext/elf.h>
```

与机器位宽匹配的整数。

## 12.81\_源码对照与相关阅读

译注：本仓库的[elf.h](../../../include/zephyr/llext/elf.h)可用于跟踪声明与实现。此相对路径从本文位置解析，不绑定盘符或用户名；本仓库参照源码不自动等同于网页 latest 的版本。

[加载流程](P004_加载扩展.md) · [管理API](P011_扩展管理API.md) · [ELF检查接口](P013_ELF检查API.md) · [加载器上下文](P025_扩展加载器上下文.md) · [符号表](P028_符号表.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

[上一章](P011_扩展管理API.md) · [返回大纲](大纲.md) · [下一章](P013_ELF检查API.md)
