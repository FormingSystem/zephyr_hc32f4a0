---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-3
title: zephyr__llext__elf.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/elf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_llext\_\_elf.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可执行与可链接格式（ELF）规范定义的数据结构和常量。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

可执行与可链接格式规范（ELF Specification）定义的数据结构与常量。参考文档见：[ELF 参考文档](https://refspecs.linuxfoundation.org/elf/)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_elf32_5Fehdr"></a>

```c
struct elf32_ehdr
```

相关声明：[elf32_ehdr](../system_service_model_reference/P016_elf32_ehdr_结构体.md)。

32位可执行与可链接格式（ELF）的文件头。

<a id="r_elf64_5Fehdr"></a>

```c
struct elf64_ehdr
```

相关声明：[elf64_ehdr](../system_service_model_reference/P021_elf64_ehdr_结构体.md)。

64位可执行与可链接格式（ELF）的文件头。

<a id="r_elf32_5Fshdr"></a>

```c
struct elf32_shdr
```

相关声明：[elf32_shdr](../system_service_model_reference/P019_elf32_shdr_结构体.md)。

32位节头（Section Header）。

<a id="r_elf64_5Fshdr"></a>

```c
struct elf64_shdr
```

相关声明：[elf64_shdr](../system_service_model_reference/P024_elf64_shdr_结构体.md)。

64位节头（Section Header）。

<a id="r_elf32_5Fsym"></a>

```c
struct elf32_sym
```

相关声明：[elf32_sym](../system_service_model_reference/P020_elf32_sym_结构体.md)。

32位符号表条目（Symbol Table Entry）。

<a id="r_elf64_5Fsym"></a>

```c
struct elf64_sym
```

相关声明：[elf64_sym](../system_service_model_reference/P025_elf64_sym_结构体.md)。

64位符号表条目（Symbol Table Entry）。

<a id="r_elf32_5Frel"></a>

```c
struct elf32_rel
```

相关声明：[elf32_rel](../system_service_model_reference/P017_elf32_rel_结构体.md)。

32位ELF的重定位条目（Relocation Entry）。

<a id="r_elf32_5Frela"></a>

```c
struct elf32_rela
```

相关声明：[elf32_rela](../system_service_model_reference/P018_elf32_rela_结构体.md)。

32位ELF中带加数（Addend）的重定位条目。

<a id="r_elf64_5Frel"></a>

```c
struct elf64_rel
```

相关声明：[elf64_rel](../system_service_model_reference/P022_elf64_rel_结构体.md)。

64位ELF的重定位条目（Relocation Entry）。

<a id="r_elf64_5Frela"></a>

```c
struct elf64_rela
```

相关声明：[elf64_rela](../system_service_model_reference/P023_elf64_rela_结构体.md)。

64位ELF中带加数（Addend）的重定位条目。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_gae407130db14180c6737390604ba7c1fe"></a>

```c
#define EI_NIDENT 16
```

相关声明：[EI_NIDENT](../llext/P012_ELF常量与类型.md#gae407130db14180c6737390604ba7c1fe)。

ELF 标识块（ELF Identifier Block）。

<a id="r_ga2a91046a80fd753ce3dbfb109212761d"></a>

```c
#define ET_REL 1
```

相关声明：[ET_REL](../llext/P012_ELF常量与类型.md#ga2a91046a80fd753ce3dbfb109212761d)。

可重定位 ELF（Relocatable ELF），尚未链接（Unlinked）。

<a id="r_ga942478985eb016311380dee473cc8c3e"></a>

```c
#define ET_EXEC 2
```

相关声明：[ET_EXEC](../llext/P012_ELF常量与类型.md#ga942478985eb016311380dee473cc8c3e)。

可执行 ELF（Executable ELF），不采用位置无关代码／位置无关可执行文件（PIC/PIE）。

<a id="r_ga4373ea3b3d512434ebe2213829b6751b"></a>

```c
#define ET_DYN 3
```

相关声明：[ET_DYN](../llext/P012_ELF常量与类型.md#ga4373ea3b3d512434ebe2213829b6751b)。

动态 ELF（Dynamic ELF），即采用位置无关代码／位置无关可执行文件（PIC/PIE）的可执行文件，或共享库（Shared Library）。

<a id="r_ga2b9430d26ba60f7a9d65c8d43e54f213"></a>

```c
#define ET_CORE 4
```

相关声明：[ET_CORE](../llext/P012_ELF常量与类型.md#ga2b9430d26ba60f7a9d65c8d43e54f213)。

核心转储（Core Dump）。

<a id="r_ga1566f4c14cff9f4b539b00af54d62dbb"></a>

```c
#define SHT_NULL 0x0
```

相关声明：[SHT_NULL](../llext/P012_ELF常量与类型.md#ga1566f4c14cff9f4b539b00af54d62dbb)。

ELF 节类型（ELF Section Types）。

<a id="r_ga4bff22edbae51353ba9b3572d424b91a"></a>

```c
#define SHT_PROGBITS 0x1
```

相关声明：[SHT_PROGBITS](../llext/P012_ELF常量与类型.md#ga4bff22edbae51353ba9b3572d424b91a)。

程序数据（Program Data）。

<a id="r_ga4add7784e43ec3d3b9c09d3ffc476a81"></a>

```c
#define SHT_SYMTAB 0x2
```

相关声明：[SHT_SYMTAB](../llext/P012_ELF常量与类型.md#ga4add7784e43ec3d3b9c09d3ffc476a81)。

符号表（Symbol Table）。

<a id="r_gaf4b916dc4ca5016fb5c374068002a532"></a>

```c
#define SHT_STRTAB 0x3
```

相关声明：[SHT_STRTAB](../llext/P012_ELF常量与类型.md#gaf4b916dc4ca5016fb5c374068002a532)。

字符串表（String Table）。

<a id="r_gabf2fc2781a2869352c2ffa0555f34118"></a>

```c
#define SHT_RELA 0x4
```

相关声明：[SHT_RELA](../llext/P012_ELF常量与类型.md#gabf2fc2781a2869352c2ffa0555f34118)。

带加数的重定位条目（Relocation Entries with Addends）。

<a id="r_ga820ff00317949be2ea1fd634a17dc13e"></a>

```c
#define SHT_NOBITS 0x8
```

相关声明：[SHT_NOBITS](../llext/P012_ELF常量与类型.md#ga820ff00317949be2ea1fd634a17dc13e)。

没有文件映像的程序数据（Program Data with No File Image）。

<a id="r_ga2aea2ed985f81f13a157fe2da02a621a"></a>

```c
#define SHT_REL 0x9
```

相关声明：[SHT_REL](../llext/P012_ELF常量与类型.md#ga2aea2ed985f81f13a157fe2da02a621a)。

不带加数的重定位条目（Relocation Entries without Addends）。

<a id="r_gaa9949aedf49107f6a07e618d5d791d40"></a>

```c
#define SHT_DYNSYM 0xB
```

相关声明：[SHT_DYNSYM](../llext/P012_ELF常量与类型.md#gaa9949aedf49107f6a07e618d5d791d40)。

动态链接符号表（Dynamic Linking Symbol Table）。

<a id="r_gaa0269f148b09419d27be6289b4ce026f"></a>

```c
#define SHT_INIT_ARRAY 0xe
```

相关声明：[SHT_INIT_ARRAY](../llext/P012_ELF常量与类型.md#gaa0269f148b09419d27be6289b4ce026f)。

初始化函数指针数组（Array of Pointers to Init Functions）。

<a id="r_ga09b4d64e68fc2a9ac211589c377ed76a"></a>

```c
#define SHT_FINI_ARRAY 0xf
```

相关声明：[SHT_FINI_ARRAY](../llext/P012_ELF常量与类型.md#ga09b4d64e68fc2a9ac211589c377ed76a)。

终止函数指针数组（Array of Pointers to Termination Functions）。

<a id="r_gaa7326ce59e1988302584ba6ac9772c32"></a>

```c
#define SHT_PREINIT_ARRAY 0x10
```

相关声明：[SHT_PREINIT_ARRAY](../llext/P012_ELF常量与类型.md#gaa7326ce59e1988302584ba6ac9772c32)。

早期初始化函数指针数组（Array of Pointers to Early Init Functions）。

<a id="r_ga025c79223b0fee4676337d660f76b59b"></a>

```c
#define SHF_WRITE 0x1
```

相关声明：[SHF_WRITE](../llext/P012_ELF常量与类型.md#ga025c79223b0fee4676337d660f76b59b)。

ELF 节标志（ELF Section Flags）。

<a id="r_ga38476fe4ed88ac83ba86a4e103199a86"></a>

```c
#define SHF_ALLOC 0x2
```

相关声明：[SHF_ALLOC](../llext/P012_ELF常量与类型.md#ga38476fe4ed88ac83ba86a4e103199a86)。

该节存在于内存中（Section Present in Memory）。

<a id="r_gab3780594e35fbbc6e5028bcb921d0a76"></a>

```c
#define SHF_EXECINSTR 0x4
```

相关声明：[SHF_EXECINSTR](../llext/P012_ELF常量与类型.md#gab3780594e35fbbc6e5028bcb921d0a76)。

该节包含可执行指令（Executable Instructions）。

<a id="r_ga2484a824af96dca3fb77c4fb8898e83b"></a>

```c
#define SHF_TLS 0x400
```

相关声明：[SHF_TLS](../llext/P012_ELF常量与类型.md#ga2484a824af96dca3fb77c4fb8898e83b)。

该节保存线程局部存储（Thread-local Storage）。

<a id="r_gac28c1d15309ad8127ac3e7cb984bc195"></a>

```c
#define SHF_MASKOS 0x0ff00000
```

相关声明：[SHF_MASKOS](../llext/P012_ELF常量与类型.md#gac28c1d15309ad8127ac3e7cb984bc195)。

操作系统特定标志（OS-specific Flags）。

<a id="r_ga95aa40c864bee18890240242b7da94f6"></a>

```c
#define SHF_LLEXT_HAS_RELOCS 0x00100000
```

相关声明：[SHF_LLEXT_HAS_RELOCS](../llext/P012_ELF常量与类型.md#ga95aa40c864bee18890240242b7da94f6)。

该节是重定位目标（Target for Relocations）。

<a id="r_gaa5c0c2a95b20eb3cb19e7fc2c7f530d3"></a>

```c
#define SHF_BASIC_TYPE_MASK (SHF_WRITE | SHF_ALLOC | SHF_EXECINSTR)
```

相关声明：[SHF_BASIC_TYPE_MASK](../llext/P012_ELF常量与类型.md#gaa5c0c2a95b20eb3cb19e7fc2c7f530d3)、[SHF_WRITE](../llext/P012_ELF常量与类型.md#ga025c79223b0fee4676337d660f76b59b)、[SHF_ALLOC](../llext/P012_ELF常量与类型.md#ga38476fe4ed88ac83ba86a4e103199a86)、[SHF_EXECINSTR](../llext/P012_ELF常量与类型.md#gab3780594e35fbbc6e5028bcb921d0a76)。

用于选择基本节标志（Basic Section Flags）的掩码（Mask）。

<a id="r_gab2f25695673c5f1c4ec723e595288411"></a>

```c
#define SHN_UNDEF 0
```

相关声明：[SHN_UNDEF](../llext/P012_ELF常量与类型.md#gab2f25695673c5f1c4ec723e595288411)。

ELF 节编号（ELF Section Numbers）。

<a id="r_gac663b490fedc8aeab91bf941772ba306"></a>

```c
#define SHN_LORESERVE 0xff00
```

相关声明：[SHN_LORESERVE](../llext/P012_ELF常量与类型.md#gac663b490fedc8aeab91bf941772ba306)。

保留节编号（Reserved Section Numbers）的起始值。

<a id="r_ga322030426afae1a37a8ba1ab86a39066"></a>

```c
#define SHN_ABS 0xfff1
```

相关声明：[SHN_ABS](../llext/P012_ELF常量与类型.md#ga322030426afae1a37a8ba1ab86a39066)。

绝对符号（Absolute Symbols）的特殊值。

<a id="r_ga3d62721d3fe66370be9ec0ca0764ec7b"></a>

```c
#define SHN_COMMON 0xfff2
```

相关声明：[SHN_COMMON](../llext/P012_ELF常量与类型.md#ga3d62721d3fe66370be9ec0ca0764ec7b)。

公共块（Common Block）。

<a id="r_gaaac4804ef07b9da1d840d951469692f0"></a>

```c
#define SHN_HIRESERVE 0xffff
```

相关声明：[SHN_HIRESERVE](../llext/P012_ELF常量与类型.md#gaaac4804ef07b9da1d840d951469692f0)。

保留节编号（Reserved Section Numbers）的结束值。

<a id="r_gaa15a54cc9c881e4d54daedc9d984c2fc"></a>

```c
#define STT_NOTYPE 0
```

相关声明：[STT_NOTYPE](../llext/P012_ELF常量与类型.md#gaa15a54cc9c881e4d54daedc9d984c2fc)。

符号表条目类型（Symbol Table Entry Types）。

<a id="r_gac236cc313291ed38ecb346a8b4bde6b2"></a>

```c
#define STT_OBJECT 1
```

相关声明：[STT_OBJECT](../llext/P012_ELF常量与类型.md#gac236cc313291ed38ecb346a8b4bde6b2)。

数据或对象（Data or Object）。

<a id="r_ga9cdfedf900935f23f6e409ce378dc1d2"></a>

```c
#define STT_FUNC 2
```

相关声明：[STT_FUNC](../llext/P012_ELF常量与类型.md#ga9cdfedf900935f23f6e409ce378dc1d2)。

函数（Function）。

<a id="r_ga9e9a3c0fa59c3fc896f8e4c1872c6af1"></a>

```c
#define STT_SECTION 3
```

相关声明：[STT_SECTION](../llext/P012_ELF常量与类型.md#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)。

节（Section）。

<a id="r_ga983395f99446fa4d398c4e902bec34c6"></a>

```c
#define STT_FILE 4
```

相关声明：[STT_FILE](../llext/P012_ELF常量与类型.md#ga983395f99446fa4d398c4e902bec34c6)。

文件名（File Name）。

<a id="r_ga0067af965ad01b11be77380eed14efb8"></a>

```c
#define STT_COMMON 5
```

相关声明：[STT_COMMON](../llext/P012_ELF常量与类型.md#ga0067af965ad01b11be77380eed14efb8)。

公共块（Common Block）。

<a id="r_gaebb605da5285a99f7475cb17214955a2"></a>

```c
#define STT_LOOS 10
```

相关声明：[STT_LOOS](../llext/P012_ELF常量与类型.md#gaebb605da5285a99f7475cb17214955a2)。

操作系统特定范围（OS-specific）的起始值。

<a id="r_ga6de042ae014d95d7b9e0649e0ecfff8e"></a>

```c
#define STT_HIOS 12
```

相关声明：[STT_HIOS](../llext/P012_ELF常量与类型.md#ga6de042ae014d95d7b9e0649e0ecfff8e)。

操作系统特定范围（OS-specific）的结束值。

<a id="r_gaeb49b6a738078d32e5979885e26c4ddf"></a>

```c
#define STT_LOPROC 13
```

相关声明：[STT_LOPROC](../llext/P012_ELF常量与类型.md#gaeb49b6a738078d32e5979885e26c4ddf)。

处理器特定范围（Processor-specific）的起始值。

<a id="r_ga5bf951d9b37f10dfe17a1bd6b4489599"></a>

```c
#define STT_HIPROC 15
```

相关声明：[STT_HIPROC](../llext/P012_ELF常量与类型.md#ga5bf951d9b37f10dfe17a1bd6b4489599)。

处理器特定范围（Processor-specific）的结束值。

<a id="r_ga72c40de459931e6f1d041201dc7398b1"></a>

```c
#define STB_LOCAL 0
```

相关声明：[STB_LOCAL](../llext/P012_ELF常量与类型.md#ga72c40de459931e6f1d041201dc7398b1)。

符号表条目绑定属性（Symbol Table Entry Bindings）。

<a id="r_ga8091960a6799bf71a7494551dac1a2e8"></a>

```c
#define STB_GLOBAL 1
```

相关声明：[STB_GLOBAL](../llext/P012_ELF常量与类型.md#ga8091960a6799bf71a7494551dac1a2e8)。

全局符号（Global Symbol）。

<a id="r_gad4247ded90f9371e3c4d2f7dda260c93"></a>

```c
#define STB_WEAK 2
```

相关声明：[STB_WEAK](../llext/P012_ELF常量与类型.md#gad4247ded90f9371e3c4d2f7dda260c93)。

弱符号（Weak Symbol）。

<a id="r_gab764e4fb4280d76967bf382a17d5b1d1"></a>

```c
#define STB_LOOS 10
```

相关声明：[STB_LOOS](../llext/P012_ELF常量与类型.md#gab764e4fb4280d76967bf382a17d5b1d1)。

操作系统特定范围（OS-specific）的起始值。

<a id="r_ga934c6e5a5405f46e343d8493a4f8f6d7"></a>

```c
#define STB_HIOS 12
```

相关声明：[STB_HIOS](../llext/P012_ELF常量与类型.md#ga934c6e5a5405f46e343d8493a4f8f6d7)。

操作系统特定范围（OS-specific）的结束值。

<a id="r_ga4f4d0360fcb960e31e119973a472010e"></a>

```c
#define STB_LOPROC 13
```

相关声明：[STB_LOPROC](../llext/P012_ELF常量与类型.md#ga4f4d0360fcb960e31e119973a472010e)。

处理器特定范围（Processor-specific）的起始值。

<a id="r_ga5fa61266452365ab0e2d2ad32b87043e"></a>

```c
#define STB_HIPROC 15
```

相关声明：[STB_HIPROC](../llext/P012_ELF常量与类型.md#ga5fa61266452365ab0e2d2ad32b87043e)。

处理器特定范围（Processor-specific）的结束值。

<a id="r_ga3b84f3e0e035d1264115f5c76227c5eb"></a>

```c
#define ELF32_ST_BIND(i)
```

相关声明：[ELF32_ST_BIND](../llext/P012_ELF常量与类型.md#ga3b84f3e0e035d1264115f5c76227c5eb)。

从 32 位 `st_info` 提取符号绑定属性（Symbol Binding）。

<a id="r_ga54dd2783f11c5f926d8db9250e1baa35"></a>

```c
#define ELF32_ST_TYPE(i)
```

相关声明：[ELF32_ST_TYPE](../llext/P012_ELF常量与类型.md#ga54dd2783f11c5f926d8db9250e1baa35)。

从 32 位 `st_info` 提取符号类型（Symbol Type）。

<a id="r_ga630907a2afaf3aea5441635416cdb037"></a>

```c
#define ELF64_ST_BIND(i)
```

相关声明：[ELF64_ST_BIND](../llext/P012_ELF常量与类型.md#ga630907a2afaf3aea5441635416cdb037)。

从 32 位 `st_info` 提取符号绑定属性（Symbol Binding）。

<a id="r_ga46a82febd2ecb9d8a0cd39810370a11b"></a>

```c
#define ELF64_ST_TYPE(i)
```

相关声明：[ELF64_ST_TYPE](../llext/P012_ELF常量与类型.md#ga46a82febd2ecb9d8a0cd39810370a11b)。

从 32 位 `st_info` 提取符号类型（Symbol Type）。

<a id="r_ga8d1ac0f35a8999a4a8a3350ca95ab54b"></a>

```c
#define ELF32_R_SYM(i)
```

相关声明：[ELF32_R_SYM](../llext/P012_ELF常量与类型.md#ga8d1ac0f35a8999a4a8a3350ca95ab54b)。

从 `r_info` 提取重定位符号索引（Relocation Symbol Index）。

<a id="r_gaa4ffd69f2c1c03229686bfa3a898db00"></a>

```c
#define ELF32_R_TYPE(i)
```

相关声明：[ELF32_R_TYPE](../llext/P012_ELF常量与类型.md#gaa4ffd69f2c1c03229686bfa3a898db00)。

从 `r_info` 提取重定位类型（Relocation Type）。

<a id="r_gab8a1253bfcc928f9aa9d4177d84f6830"></a>

```c
#define ELF64_R_SYM(i)
```

相关声明：[ELF64_R_SYM](../llext/P012_ELF常量与类型.md#gab8a1253bfcc928f9aa9d4177d84f6830)。

从 `r_info` 提取重定位符号（Relocation Symbol）。

<a id="r_ga51aeadee885873fec9a218c058fe9e09"></a>

```c
#define ELF64_R_TYPE(i)
```

相关声明：[ELF64_R_TYPE](../llext/P012_ELF常量与类型.md#ga51aeadee885873fec9a218c058fe9e09)。

从 `r_info` 提取重定位类型（Relocation Type）。

<a id="r_ga8d3fc5bbbc767d0e484843f6831659cf"></a>

```c
#define ELF_R_SYM ELF64_R_SYM
```

相关声明：[ELF_R_SYM](../llext/P012_ELF常量与类型.md#ga8d3fc5bbbc767d0e484843f6831659cf)、[ELF64_R_SYM](../llext/P012_ELF常量与类型.md#gab8a1253bfcc928f9aa9d4177d84f6830)。

获取重定位符号（Relocation Symbol）的机器字长适配宏别名（Machine-sized Macro Alias）。

<a id="r_gae91c561e4921f0a1cf5868d775ac3243"></a>

```c
#define ELF_R_TYPE ELF64_R_TYPE
```

相关声明：[ELF_R_TYPE](../llext/P012_ELF常量与类型.md#gae91c561e4921f0a1cf5868d775ac3243)、[ELF64_R_TYPE](../llext/P012_ELF常量与类型.md#ga51aeadee885873fec9a218c058fe9e09)。

获取重定位类型（Relocation Type）的机器字长适配宏别名（Machine-sized Macro Alias）。

<a id="r_ga5370d61077b153ba6b515994e185b9f8"></a>

```c
#define ELF_ST_BIND ELF64_ST_BIND
```

相关声明：[ELF_ST_BIND](../llext/P012_ELF常量与类型.md#ga5370d61077b153ba6b515994e185b9f8)、[ELF64_ST_BIND](../llext/P012_ELF常量与类型.md#ga630907a2afaf3aea5441635416cdb037)。

获取符号绑定属性（Symbol Bind）的机器字长适配宏别名（Machine-sized Macro Alias）。

<a id="r_ga972d66fcb6578448641a95d7a321dc4b"></a>

```c
#define ELF_ST_TYPE ELF64_ST_TYPE
```

相关声明：[ELF_ST_TYPE](../llext/P012_ELF常量与类型.md#ga972d66fcb6578448641a95d7a321dc4b)、[ELF64_ST_TYPE](../llext/P012_ELF常量与类型.md#ga46a82febd2ecb9d8a0cd39810370a11b)。

获取符号类型（Symbol Type）的机器字长适配宏别名（Machine-sized Macro Alias）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_ga55f1dc601c95381307fddd5969969634"></a>

```c
typedef uint32_t elf32_addr
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)。

无符号程序地址（Unsigned Program Address）。

<a id="r_ga141d58f50804ef53e0d9bd13fcb36424"></a>

```c
typedef uint16_t elf32_half
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)。

无符号中等宽度整数（Unsigned Medium Integer）。

<a id="r_gabb40eb5ffbe88010885da1c8c7b869e3"></a>

```c
typedef uint32_t elf32_off
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[elf32_off](../llext/P012_ELF常量与类型.md#gabb40eb5ffbe88010885da1c8c7b869e3)。

无符号文件偏移量（Unsigned File Offset）。

<a id="r_ga1325c85290908b89a9c2b9bdd1aa2efd"></a>

```c
typedef int32_t elf32_sword
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[elf32_sword](../llext/P012_ELF常量与类型.md#ga1325c85290908b89a9c2b9bdd1aa2efd)。

有符号整数（Signed Integer）。

<a id="r_gac786571f50a02299b19c1a16d658ea72"></a>

```c
typedef uint32_t elf32_word
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)。

无符号整数（Unsigned Integer）。

<a id="r_ga42c555ace34b21c1773c9e59228e9929"></a>

```c
typedef uint64_t elf64_addr
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)。

无符号程序地址（Unsigned Program Address）。

<a id="r_ga3358e1392fd861af8a7c8248519717a0"></a>

```c
typedef uint16_t elf64_half
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)。

无符号中等宽度整数（Unsigned Medium Integer）。

<a id="r_ga7f982d835a34713a84907873f9e058a9"></a>

```c
typedef uint64_t elf64_off
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[elf64_off](../llext/P012_ELF常量与类型.md#ga7f982d835a34713a84907873f9e058a9)。

无符号文件偏移量（Unsigned File Offset）。

<a id="r_ga31413d6e89616f2d0356abd533b0c5a1"></a>

```c
typedef int32_t elf64_sword
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[elf64_sword](../llext/P012_ELF常量与类型.md#ga31413d6e89616f2d0356abd533b0c5a1)。

有符号整数（Signed Integer）。

<a id="r_gaabf3a740e51b02fbaf40bedfba35e476"></a>

```c
typedef uint32_t elf64_word
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)。

无符号整数（Unsigned Integer）。

<a id="r_ga3e687a252b2bb6ed11ea9bc2fa6b728e"></a>

```c
typedef int64_t elf64_sxword
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[elf64_sxword](../llext/P012_ELF常量与类型.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e)。

有符号长整数（Signed Long Integer）。

<a id="r_ga68e4179ac3b1c52c28c6e3e5c2a1838a"></a>

```c
typedef uint64_t elf64_xword
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)。

无符号长整数（Unsigned Long Integer）。

<a id="r_gab39a1763256a6b9ccccf8b89836cd192"></a>

```c
typedef struct elf64_ehdr elf_ehdr_t
```

相关声明：[elf64_ehdr](../system_service_model_reference/P021_elf64_ehdr_结构体.md)、[elf_ehdr_t](../llext/P012_ELF常量与类型.md#gab39a1763256a6b9ccccf8b89836cd192)。

LLEXT 目前未使用的动态功能（Dynamic Features）。

<a id="r_gab3695edd628cf868dc4f0d618f86bcbd"></a>

```c
typedef struct elf64_shdr elf_shdr_t
```

相关声明：[elf64_shdr](../system_service_model_reference/P024_elf64_shdr_结构体.md)、[elf_shdr_t](../llext/P012_ELF常量与类型.md#gab3695edd628cf868dc4f0d618f86bcbd)。

适配机器字长的节头结构体（Machine-sized Section Header Structure）。

<a id="r_gad5c63f362ef6b26db73c37980d731c93"></a>

```c
typedef struct elf64_phdr elf_phdr_t
```

相关声明：[elf_phdr_t](../llext/P012_ELF常量与类型.md#gad5c63f362ef6b26db73c37980d731c93)。

适配机器字长的程序头结构体（Machine-sized Program Header Structure）。

<a id="r_ga9f98ad5b44106cacfd013f43f29a2eff"></a>

```c
typedef elf64_addr elf_addr
```

相关声明：[elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)、[elf_addr](../llext/P012_ELF常量与类型.md#ga9f98ad5b44106cacfd013f43f29a2eff)。

适配机器字长的程序地址（Machine-sized Program Address）。

<a id="r_gacb3487f81221d562af45632df161c64e"></a>

```c
typedef elf64_half elf_half
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[elf_half](../llext/P012_ELF常量与类型.md#gacb3487f81221d562af45632df161c64e)。

适配机器字长的小整数（Machine-sized Small Integer）。

<a id="r_ga25ad092196ba8d073be66dc7629f8bc3"></a>

```c
typedef elf64_xword elf_word
```

相关声明：[elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)、[elf_word](../llext/P012_ELF常量与类型.md#ga25ad092196ba8d073be66dc7629f8bc3)。

适配机器字长的整数（Machine-sized Integer）。

<a id="r_gafdcf88be776ec490cf1ec7c286f6202f"></a>

```c
typedef struct elf64_rel elf_rel_t
```

相关声明：[elf64_rel](../system_service_model_reference/P022_elf64_rel_结构体.md)、[elf_rel_t](../llext/P012_ELF常量与类型.md#gafdcf88be776ec490cf1ec7c286f6202f)。

适配机器字长的重定位结构体（Machine-sized Relocation Struct）。

<a id="r_gad5dd8960a2fbfc74cdcd016b5c2c7cea"></a>

```c
typedef struct elf64_rela elf_rela_t
```

相关声明：[elf64_rela](../system_service_model_reference/P023_elf64_rela_结构体.md)、[elf_rela_t](../llext/P012_ELF常量与类型.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)。

适配机器字长的带加数重定位结构体（Machine-sized Relocation Struct with Addend）。

<a id="r_ga144fdcc270b75a371880da097968555e"></a>

```c
typedef struct elf64_sym elf_sym_t
```

相关声明：[elf64_sym](../system_service_model_reference/P025_elf64_sym_结构体.md)、[elf_sym_t](../llext/P012_ELF常量与类型.md#ga144fdcc270b75a371880da097968555e)。

适配机器字长的符号结构体（Machine-sized Symbol Struct）。


## 3.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P221_elf.h_源码浏览.md)
- [elf32_ehdr](../system_service_model_reference/P016_elf32_ehdr_结构体.md)
- [elf64_ehdr](../system_service_model_reference/P021_elf64_ehdr_结构体.md)
- [elf32_shdr](../system_service_model_reference/P019_elf32_shdr_结构体.md)
- [elf64_shdr](../system_service_model_reference/P024_elf64_shdr_结构体.md)
- [elf32_sym](../system_service_model_reference/P020_elf32_sym_结构体.md)
- [elf64_sym](../system_service_model_reference/P025_elf64_sym_结构体.md)
- [elf32_rel](../system_service_model_reference/P017_elf32_rel_结构体.md)
- [elf32_rela](../system_service_model_reference/P018_elf32_rela_结构体.md)
- [elf64_rel](../system_service_model_reference/P022_elf64_rel_结构体.md)
- [elf64_rela](../system_service_model_reference/P023_elf64_rela_结构体.md)
- [EI_NIDENT](../llext/P012_ELF常量与类型.md#gae407130db14180c6737390604ba7c1fe)
- [ET_REL](../llext/P012_ELF常量与类型.md#ga2a91046a80fd753ce3dbfb109212761d)
- [ET_EXEC](../llext/P012_ELF常量与类型.md#ga942478985eb016311380dee473cc8c3e)
- [ET_DYN](../llext/P012_ELF常量与类型.md#ga4373ea3b3d512434ebe2213829b6751b)
- [ET_CORE](../llext/P012_ELF常量与类型.md#ga2b9430d26ba60f7a9d65c8d43e54f213)
- [SHT_NULL](../llext/P012_ELF常量与类型.md#ga1566f4c14cff9f4b539b00af54d62dbb)
- [SHT_PROGBITS](../llext/P012_ELF常量与类型.md#ga4bff22edbae51353ba9b3572d424b91a)
- [SHT_SYMTAB](../llext/P012_ELF常量与类型.md#ga4add7784e43ec3d3b9c09d3ffc476a81)
- [SHT_STRTAB](../llext/P012_ELF常量与类型.md#gaf4b916dc4ca5016fb5c374068002a532)
- [SHT_RELA](../llext/P012_ELF常量与类型.md#gabf2fc2781a2869352c2ffa0555f34118)
- [SHT_NOBITS](../llext/P012_ELF常量与类型.md#ga820ff00317949be2ea1fd634a17dc13e)
- [SHT_REL](../llext/P012_ELF常量与类型.md#ga2aea2ed985f81f13a157fe2da02a621a)
- [SHT_DYNSYM](../llext/P012_ELF常量与类型.md#gaa9949aedf49107f6a07e618d5d791d40)
- [SHT_INIT_ARRAY](../llext/P012_ELF常量与类型.md#gaa0269f148b09419d27be6289b4ce026f)
- [SHT_FINI_ARRAY](../llext/P012_ELF常量与类型.md#ga09b4d64e68fc2a9ac211589c377ed76a)
- [SHT_PREINIT_ARRAY](../llext/P012_ELF常量与类型.md#gaa7326ce59e1988302584ba6ac9772c32)
- [SHF_WRITE](../llext/P012_ELF常量与类型.md#ga025c79223b0fee4676337d660f76b59b)
- [SHF_ALLOC](../llext/P012_ELF常量与类型.md#ga38476fe4ed88ac83ba86a4e103199a86)
- [SHF_EXECINSTR](../llext/P012_ELF常量与类型.md#gab3780594e35fbbc6e5028bcb921d0a76)
- [SHF_TLS](../llext/P012_ELF常量与类型.md#ga2484a824af96dca3fb77c4fb8898e83b)
- [SHF_MASKOS](../llext/P012_ELF常量与类型.md#gac28c1d15309ad8127ac3e7cb984bc195)
- [SHF_LLEXT_HAS_RELOCS](../llext/P012_ELF常量与类型.md#ga95aa40c864bee18890240242b7da94f6)
- [SHF_BASIC_TYPE_MASK](../llext/P012_ELF常量与类型.md#gaa5c0c2a95b20eb3cb19e7fc2c7f530d3)
- [SHN_UNDEF](../llext/P012_ELF常量与类型.md#gab2f25695673c5f1c4ec723e595288411)
- [SHN_LORESERVE](../llext/P012_ELF常量与类型.md#gac663b490fedc8aeab91bf941772ba306)
- [SHN_ABS](../llext/P012_ELF常量与类型.md#ga322030426afae1a37a8ba1ab86a39066)
- [SHN_COMMON](../llext/P012_ELF常量与类型.md#ga3d62721d3fe66370be9ec0ca0764ec7b)
- [SHN_HIRESERVE](../llext/P012_ELF常量与类型.md#gaaac4804ef07b9da1d840d951469692f0)
- [STT_NOTYPE](../llext/P012_ELF常量与类型.md#gaa15a54cc9c881e4d54daedc9d984c2fc)
- [STT_OBJECT](../llext/P012_ELF常量与类型.md#gac236cc313291ed38ecb346a8b4bde6b2)
- [STT_FUNC](../llext/P012_ELF常量与类型.md#ga9cdfedf900935f23f6e409ce378dc1d2)
- [STT_SECTION](../llext/P012_ELF常量与类型.md#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)
- [STT_FILE](../llext/P012_ELF常量与类型.md#ga983395f99446fa4d398c4e902bec34c6)
- [STT_COMMON](../llext/P012_ELF常量与类型.md#ga0067af965ad01b11be77380eed14efb8)
- [STT_LOOS](../llext/P012_ELF常量与类型.md#gaebb605da5285a99f7475cb17214955a2)
- [STT_HIOS](../llext/P012_ELF常量与类型.md#ga6de042ae014d95d7b9e0649e0ecfff8e)
- [STT_LOPROC](../llext/P012_ELF常量与类型.md#gaeb49b6a738078d32e5979885e26c4ddf)
- [STT_HIPROC](../llext/P012_ELF常量与类型.md#ga5bf951d9b37f10dfe17a1bd6b4489599)
- [STB_LOCAL](../llext/P012_ELF常量与类型.md#ga72c40de459931e6f1d041201dc7398b1)
- [STB_GLOBAL](../llext/P012_ELF常量与类型.md#ga8091960a6799bf71a7494551dac1a2e8)
- [STB_WEAK](../llext/P012_ELF常量与类型.md#gad4247ded90f9371e3c4d2f7dda260c93)
- [STB_LOOS](../llext/P012_ELF常量与类型.md#gab764e4fb4280d76967bf382a17d5b1d1)
- [STB_HIOS](../llext/P012_ELF常量与类型.md#ga934c6e5a5405f46e343d8493a4f8f6d7)
- [STB_LOPROC](../llext/P012_ELF常量与类型.md#ga4f4d0360fcb960e31e119973a472010e)
- [STB_HIPROC](../llext/P012_ELF常量与类型.md#ga5fa61266452365ab0e2d2ad32b87043e)
- [ELF32_ST_BIND](../llext/P012_ELF常量与类型.md#ga3b84f3e0e035d1264115f5c76227c5eb)
- [ELF32_ST_TYPE](../llext/P012_ELF常量与类型.md#ga54dd2783f11c5f926d8db9250e1baa35)
- [ELF64_ST_BIND](../llext/P012_ELF常量与类型.md#ga630907a2afaf3aea5441635416cdb037)
- [ELF64_ST_TYPE](../llext/P012_ELF常量与类型.md#ga46a82febd2ecb9d8a0cd39810370a11b)
- [ELF32_R_SYM](../llext/P012_ELF常量与类型.md#ga8d1ac0f35a8999a4a8a3350ca95ab54b)
- [ELF32_R_TYPE](../llext/P012_ELF常量与类型.md#gaa4ffd69f2c1c03229686bfa3a898db00)
- [ELF64_R_SYM](../llext/P012_ELF常量与类型.md#gab8a1253bfcc928f9aa9d4177d84f6830)
- [ELF64_R_TYPE](../llext/P012_ELF常量与类型.md#ga51aeadee885873fec9a218c058fe9e09)
- [ELF_R_SYM](../llext/P012_ELF常量与类型.md#ga8d3fc5bbbc767d0e484843f6831659cf)
- [ELF_R_TYPE](../llext/P012_ELF常量与类型.md#gae91c561e4921f0a1cf5868d775ac3243)
- [ELF_ST_BIND](../llext/P012_ELF常量与类型.md#ga5370d61077b153ba6b515994e185b9f8)
- [ELF_ST_TYPE](../llext/P012_ELF常量与类型.md#ga972d66fcb6578448641a95d7a321dc4b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)
- [elf32_off](../llext/P012_ELF常量与类型.md#gabb40eb5ffbe88010885da1c8c7b869e3)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [elf32_sword](../llext/P012_ELF常量与类型.md#ga1325c85290908b89a9c2b9bdd1aa2efd)
- [elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)
- [elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)
- [elf64_off](../llext/P012_ELF常量与类型.md#ga7f982d835a34713a84907873f9e058a9)
- [elf64_sword](../llext/P012_ELF常量与类型.md#ga31413d6e89616f2d0356abd533b0c5a1)
- [elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [elf64_sxword](../llext/P012_ELF常量与类型.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e)
- [elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)
- [elf_ehdr_t](../llext/P012_ELF常量与类型.md#gab39a1763256a6b9ccccf8b89836cd192)
- [elf_shdr_t](../llext/P012_ELF常量与类型.md#gab3695edd628cf868dc4f0d618f86bcbd)
- [elf_phdr_t](../llext/P012_ELF常量与类型.md#gad5c63f362ef6b26db73c37980d731c93)
- [elf_addr](../llext/P012_ELF常量与类型.md#ga9f98ad5b44106cacfd013f43f29a2eff)
- [elf_half](../llext/P012_ELF常量与类型.md#gacb3487f81221d562af45632df161c64e)
- [elf_word](../llext/P012_ELF常量与类型.md#ga25ad092196ba8d073be66dc7629f8bc3)
- [elf_rel_t](../llext/P012_ELF常量与类型.md#gafdcf88be776ec490cf1ec7c286f6202f)
- [elf_rela_t](../llext/P012_ELF常量与类型.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)
- [elf_sym_t](../llext/P012_ELF常量与类型.md#ga144fdcc270b75a371880da097968555e)
- [https://refspecs.linuxfoundation.org/elf/](https://refspecs.linuxfoundation.org/elf/)

<a id="header-details"></a>

---

[上一章](P002_zephyr__dt-bindings__sensor__lsm6dsvxxx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__opamp__infineon-autanalog-ctb.h_文件参考.md)
