---
id: learning.zephyr-docs.llext.api-11
title: 扩展管理API
kind: reference
status: maintained
domains: [zephyr, llext, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__llext__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_扩展管理API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__apis.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 11.1\_概述

本页给出可链接加载扩展（Linkable Loadable Extensions，LLEXT）的管理应用程序编程接口（Application Programming Interface，API）。原文标注：自 3.5 版本起提供（Since），接口版本（Version）为 0.1.0。

## 11.2\_关联声明与说明

<a id="r_llext_5Felf"></a>

[ELF常量与数据类型](P012_ELF常量与类型.md)。

<a id="r_llext_5Finspect_5Fapis"></a>

[ELF检查接口](P013_ELF检查API.md)。

<a id="r_llext_5Floader_5Fapis"></a>

[ELF加载器上下文](P014_ELF加载器API.md)。

<a id="r_llext_5Fsymbols"></a>

[导出符号定义](P015_导出符号API.md)。

## 11.3\_关联声明与说明

<a id="r_llext"></a>

```c
struct llext
```

描述可链接加载扩展（Linkable Loadable Extension，LLEXT）的结构体。

[详细说明](P020_扩展对象.md)。

<a id="r_llext_5Fload_5Fparam"></a>

```c
struct llext_load_param
```

[`llext_load`](#ga0a4c3db30bc3ec7aa8a9b0e076af7157) 的高级参数（Advanced Parameters）。

[详细说明](P024_扩展加载参数.md)。

## 11.4\_LLEXT\_LOAD\_PARAM\_DEFAULT

<a id="ga15f6bd18c1693009be46641ce1b008c6"></a>
<a id="r_ga15f6bd18c1693009be46641ce1b008c6"></a>

```c
#define LLEXT_LOAD_PARAM_DEFAULT { .relocate_local = true, }
```

```c
#include <zephyr/llext/llext.h>
```

[`llext_load_param`](P024_扩展加载参数.md) 的默认初始化器（Default Initializer）。

## 11.5\_LLEXT\_MAX\_DEPENDENCIES

<a id="ga09b483779bce7612bfaba519e1ecb9e0"></a>
<a id="r_ga09b483779bce7612bfaba519e1ecb9e0"></a>

```c
#define LLEXT_MAX_DEPENDENCIES 8
```

```c
#include <zephyr/llext/llext.h>
```

可依赖的 LLEXT 扩展的最大数量。

## 11.6\_LLEXT\_MAX\_NAME\_LEN

<a id="ga9b01694abfb050daa3f99e197fecc1a3"></a>
<a id="r_ga9b01694abfb050daa3f99e197fecc1a3"></a>

```c
#define LLEXT_MAX_NAME_LEN 15
```

```c
#include <zephyr/llext/llext.h>
```

扩展名称的最大长度。

## 11.7\_llext\_entry\_fn\_t

<a id="ga0c27a8648deab424948eeb776a3de5ea"></a>
<a id="r_ga0c27a8648deab424948eeb776a3de5ea"></a>

```c
typedef void(* llext_entry_fn_t) (void *user_data)
```

```c
#include <zephyr/llext/llext.h>
```

扩展入口函数的签名（Entry Point Function Signature）。

## 11.8\_llext\_mem

<a id="ga9258a6fe4a45aa5dd48c80c7aa07b953"></a>
<a id="r_ga9258a6fe4a45aa5dd48c80c7aa07b953"></a>

```c
enum llext_mem
```

```c
#include <zephyr/llext/llext.h>
```

LLEXT 子系统保存或引用的内存区域（Memory Region）列表。

本枚举列出 LLEXT 子系统使用的各种内存区域类型。名称与常见 `ELF` 文件节（Section）的名称对应；但在加载时，标志相近的多个 `ELF` 节可能合并成一个内存区域。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LLEXT_MEM_TEXT` | 可执行代码（Executable Code）。 |
| `LLEXT_MEM_DATA` | 已初始化数据（Initialized Data）。 |
| `LLEXT_MEM_RODATA` | 只读数据（Read-only Data）。 |
| `LLEXT_MEM_BSS` | 未初始化数据（Uninitialized Data）。 |
| `LLEXT_MEM_EXPORT` | 导出符号表（Exported Symbol Table）。 |
| `LLEXT_MEM_SYMTAB` | 符号表（Symbol Table）。 |
| `LLEXT_MEM_STRTAB` | 符号名称字符串（Symbol Name Strings）。 |
| `LLEXT_MEM_SHSTRTAB` | 节名称字符串（Section Name Strings）。 |
| `LLEXT_MEM_PREINIT` | 早期初始化函数数组（Early Setup Function Array）。 |
| `LLEXT_MEM_INIT` | 初始化函数数组（Setup Function Array）。 |
| `LLEXT_MEM_FINI` | 清理函数数组（Cleanup Function Array）。 |
| `LLEXT_MEM_COUNT` | LLEXT 管理的区域数量。 |

> 译注：本页枚举表展示文档构建条件下的成员；同批源码浏览页还保留受 `CONFIG_LLEXT_VENEERS` 和 `CONFIG_LLEXT_RODATA_NO_RELOC` 控制的成员。实际成员及数值以工程配置后的头文件为准。

## 11.9\_arch\_elf\_relocate()

<a id="gaeaf6817a9f9c7ae66000cc960e8edf31"></a>
<a id="r_gaeaf6817a9f9c7ae66000cc960e8edf31"></a>

```c
int arch_elf_relocate ( struct llext_loader * ldr, struct llext * ext, elf_rela_t * rel, const elf_shdr_t * shdr )
```

```c
#include <zephyr/llext/llext.h>
```

架构专用的操作码更新函数（Architecture-specific Opcode Update）。

`ELF` 文件包含描述一系列重定位（Relocation）的节。这些重定位指示如何根据节、函数或对象等符号数据的实际放置位置改写操作码。重定位与架构有关，每种支持 LLEXT 的架构都必须实现此函数。原文还说明：参数 `sym_base_addr`、`sym_name` 可从 `sym` 参数计算得到，但为提高效率而冗余传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ldr` | 扩展加载器（Extension Loader）。 |
| `[in] ext` | 重定位所涉及的扩展。 |
| `[in] rel` | `ELF` 提供的重定位数据。 |
| `[in] shdr` | 当前正在定位的 `ELF` 节的节头（Section Header）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOTSUP` | 不支持的重定位。 |
| `-ENOEXEC` | 无效的重定位。 |

> 译注：原文提到 `sym_base_addr`、`sym_name` 和 `sym`，但当前展示的函数声明只有 `ldr`、`ext`、`rel`、`shdr`。上段保留原文说明；实际调用应遵循所用版本头文件的声明，不能追加这些已不在声明中的参数。

## 11.10\_llext\_add\_domain()

<a id="ga64b13edf15b7c233b49c9c8edff884e6"></a>
<a id="r_ga64b13edf15b7c233b49c9c8edff884e6"></a>

```c
int llext_add_domain ( struct llext * ext, struct k_mem_domain * domain )
```

```c
#include <zephyr/llext/llext.h>
```

将扩展加入内存域（Memory Domain）。

把覆盖扩展内存区域的内存分区（Memory Partition）加入内存域，使启用硬件内存保护时也能在用户态线程（User Mode Thread）中执行扩展。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ext` | 要加入内存域的扩展。 |
| `[in] domain` | 接收这些内存分区的内存域。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | [`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE) 选项未启用或不受支持。 |

**返回（Returns）**：成功返回 0，否则返回负错误码。

## 11.11\_llext\_bootstrap()

<a id="ga809f7a7976b4436dad31aa03d9ea3729"></a>
<a id="r_ga809f7a7976b4436dad31aa03d9ea3729"></a>

```c
void llext_bootstrap ( struct llext * ext, llext_entry_fn_t entry_fn, void * user_data )
```

```c
#include <zephyr/llext/llext.h>
```

初始化、执行并清理扩展。

在当前线程上下文中依次调用扩展自身的初始化函数、一个额外入口以及扩展的清理函数。

这是对 [`llext_bringup`](#ga01c0c23dba5ff1aa9da42c7895cc7fab) 和 [`llext_teardown`](#gae061bb6100ad394fcaca7751ff3dadba) 的便捷封装；其签名与 [`k_thread_entry_t`](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717) 相匹配，因此可通过 [`k_thread_create`](../thread_core_reference/P001_线程公共接口.md#gad5b0bff3102f1656089f5875d999a367) 直接作为新用户态或内核线程的入口启动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ext` | 要执行的扩展，作为 [`k_thread_create`](../thread_core_reference/P001_线程公共接口.md#gad5b0bff3102f1656089f5875d999a367) 的 `p1` 传入。 |
| `[in] entry_fn` | 扩展初始化后执行的线程主入口，作为 [`k_thread_create`](../thread_core_reference/P001_线程公共接口.md#gad5b0bff3102f1656089f5875d999a367) 的 `p2` 传入。 |
| `[in] user_data` | 传给 `entry_fn` 的参数，作为 [`k_thread_create`](../thread_core_reference/P001_线程公共接口.md#gad5b0bff3102f1656089f5875d999a367) 的 `p3` 传入。 |

## 11.12\_llext\_bringup()

<a id="ga01c0c23dba5ff1aa9da42c7895cc7fab"></a>
<a id="r_ga01c0c23dba5ff1aa9da42c7895cc7fab"></a>

```c
int llext_bringup ( struct llext * ext)
```

```c
#include <zephyr/llext/llext.h>
```

调用扩展的初始化函数（Bringup Functions）。

访问扩展中的任何符号前必须调用此函数。它在调用者上下文中执行扩展自身的初始化函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ext` | 要初始化的扩展。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EFAULT` | 检测到重定位问题。 |

**参见（See Also）**：另见 [`llext_bootstrap`](#ga809f7a7976b4436dad31aa03d9ea3729)。

**返回（Returns）**：成功返回 0，否则返回负错误码。

## 11.13\_llext\_by\_name()

<a id="gaad89b0b44cf5c9528c3f8a0ce37a8fbe"></a>
<a id="r_gaad89b0b44cf5c9528c3f8a0ce37a8fbe"></a>

```c
struct llext * llext_by_name ( const char * name)
```

```c
#include <zephyr/llext/llext.h>
```

按名称查找 LLEXT 扩展。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] name` | 扩展名称字符串。 |

**返回（Returns）**：返回扩展指针；未找到时返回 `NULL`。

## 11.14\_llext\_call\_fn()

<a id="gad50ad281c70093da99851723fc6af470"></a>
<a id="r_gad50ad281c70093da99851723fc6af470"></a>

```c
int llext_call_fn ( struct llext * ext, const char * sym_name )
```

```c
#include <zephyr/llext/llext.h>
```

按名称调用函数。

要求存在代表 `void` `fn`(`void`) 形式函数的符号，且该函数可以调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ext` | 要在其中调用函数的扩展。 |
| `[in] sym_name` | 扩展中的函数名，即导出符号。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOENT` | 未找到符号名。 |

## 11.15\_llext\_find\_section()

<a id="ga396bddb41c51415faf79e11fad44cb4e"></a>
<a id="r_ga396bddb41c51415faf79e11fad44cb4e"></a>

```c
ssize_t llext_find_section ( struct llext_loader * loader, const char * search_name )
```

```c
#include <zephyr/llext/llext.h>
```

定位文件中的 `ELF` 节。

在 `ELF` 文件中按名称查找节，并返回其偏移量（Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] loader` | 扩展加载器的数据与上下文。 |
| `[in] search_name` | 要查找的节名称。 |

**返回（Returns）**：返回节偏移量，或负错误码。

## 11.16\_llext\_find\_sym()

<a id="gac0982fad15a62723a5cad3f7edd6ba3e"></a>
<a id="r_gac0982fad15a62723a5cad3f7edd6ba3e"></a>

```c
const void * llext_find_sym ( const struct llext_symtable * sym_table, const char * sym_name )
```

```c
#include <zephyr/llext/llext.h>
```

查找任意符号的地址。

在 Zephyr 主二进制导出的符号列表或某个扩展的符号表中查找符号地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sym_table` | 要搜索的符号表；传入 `NULL` 时搜索 Zephyr 主符号表。 |
| `[in] sym_name` | 要查找的符号名。 |

**返回（Returns）**：返回符号的内存地址；未找到时返回 `NULL`。

## 11.17\_llext\_free\_inspection\_data()

<a id="ga54f3aaed749e8c6bad6fbecb1622ab06"></a>
<a id="r_ga54f3aaed749e8c6bad6fbecb1622ab06"></a>

```c
int llext_free_inspection_data ( struct llext_loader * ldr, struct llext * ext )
```

```c
#include <zephyr/llext/llext.h>
```

释放指定加载器和扩展中与检查（Inspection）有关的内存。

只有加载时通过 `llext_load_param::keep_section_info` 请求保留检查数据，才需要调用它；否则调用不执行任何操作（No-op）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ldr` | 扩展加载器（Extension Loader）。 |
| `[in] ext` | 扩展。 |

**返回（Returns）**：成功返回 0，否则返回负错误码。

## 11.18\_llext\_get\_fn\_table\_entry()

<a id="gaa0f67302420a2db7825c103250fe27c5"></a>
<a id="r_gaa0f67302420a2db7825c103250fe27c5"></a>

```c
ssize_t llext_get_fn_table_entry ( struct llext * ext, bool is_init, void ** ptr, size_t idx )
```

```c
#include <zephyr/llext/llext.h>
```

取得扩展某个初始化或清理函数的指针。

此系统调用（System Call）可取得完成扩展初始化或清理所需调用的各个函数的地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ext` | 要初始化的扩展。 |
| `[in] is_init` | `true` 表示取得初始化时调用的函数，`false` 表示取得清理函数。 |
| `[in,out] ptr` | 用于保存函数指针的指针变量的地址；可以传入 `NULL` 以查询已定义函数的数量。 |
| `[in] idx` | 要取得的函数索引；`ptr` 为 `NULL` 时忽略。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EFAULT` | 检测到重定位问题。 |
| `-ENOMEM` | 数组无法容纳于已分配缓冲区。 |

**参见（See Also）**：另见 [`llext_bootstrap`](#ga809f7a7976b4436dad31aa03d9ea3729)。

**返回（Returns）**：`ptr` 为 `NULL` 时返回函数数量；否则返回 0 或负错误码。

## 11.19\_llext\_get\_section\_header()

<a id="gae353754f9b27ad548b6919f903639d4e"></a>
<a id="r_gae353754f9b27ad548b6919f903639d4e"></a>

```c
int llext_get_section_header ( const struct llext_loader * loader, const struct llext * ext, const char * search_name, elf_shdr_t * shdr )
```

```c
#include <zephyr/llext/llext.h>
```

按名称提取 `ELF` 节头。

在 `ELF` 文件中按名称查找节，并取得完整节头。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] loader` | 扩展加载器的数据与上下文。 |
| `[in] ext` | 要搜索的扩展。 |
| `[in] search_name` | 要查找的节名称。 |
| `[out] shdr` | 保存节头的缓冲区。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOTSUP` | 不支持 peek 方法。 |
| `-ENOENT` | 未找到节。 |

## 11.20\_llext\_heap\_init()

<a id="ga1fa344ade4911a259e7b8ded51241d13"></a>
<a id="r_ga1fa344ade4911a259e7b8ded51241d13"></a>

```c
int llext_heap_init ( void * mem, size_t bytes )
```

```c
#include <zephyr/llext/llext.h>
```

动态初始化 LLEXT 堆（Heap）。

在运行时使用提供的内存块作为 LLEXT 堆。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mem` | 内存指针。 |
| `bytes` | 内存区域大小，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | [`CONFIG_LLEXT_HEAP_DYNAMIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLEXT_HEAP_DYNAMIC) 未启用或不受支持；或者该选项已启用，同时启用了 [`CONFIG_HARVARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HARVARD)。 |

**返回（Returns）**：成功返回 0，否则返回负错误码。

## 11.21\_llext\_heap\_init\_harvard()

<a id="gad78c7504f824d86471c2ca94b6e1c82c"></a>
<a id="r_gad78c7504f824d86471c2ca94b6e1c82c"></a>

```c
int llext_heap_init_harvard ( void * instr_mem, size_t instr_bytes, void * data_mem, size_t data_bytes )
```

```c
#include <zephyr/llext/llext.h>
```

为哈佛架构（Harvard Architecture）动态初始化 LLEXT 堆。

在运行时使用提供的内存块作为 LLEXT 的各个堆。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `instr_mem（原页显示 Instruction Memory APIs）` | 指令内存指针。 |
| `instr_bytes` | 指令内存区域大小，单位为字节。 |
| `data_mem` | 数据内存指针。 |
| `data_bytes` | 数据内存区域大小，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | [`CONFIG_LLEXT_HEAP_DYNAMIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLEXT_HEAP_DYNAMIC) 未启用或不受支持；或者该选项已启用，但未启用 [`CONFIG_HARVARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HARVARD)。 |

**返回（Returns）**：成功返回 0，否则返回负错误码。

> 译注：原网页参数表将第一个参数显示成“Instruction Memory APIs”，与声明中的 `instr_mem` 不一致。译文保留这一显示差异，并按声明指出其实际参数名。

## 11.22\_llext\_heap\_uninit()

<a id="gab20e01c13bdb344978a0fb9b5bd8531d"></a>
<a id="r_gab20e01c13bdb344978a0fb9b5bd8531d"></a>

```c
int llext_heap_uninit ( void )
```

```c
#include <zephyr/llext/llext.h>
```

将 LLEXT 堆标记为未初始化。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | [`CONFIG_LLEXT_HEAP_DYNAMIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLEXT_HEAP_DYNAMIC) 未启用或不受支持。 |
| `-EBUSY` | 堆不为空。 |

**返回（Returns）**：成功返回 0，否则返回负错误码。

## 11.23\_llext\_iterate()

<a id="ga0faf5a335199e63a424b122b03027c98"></a>
<a id="r_ga0faf5a335199e63a424b122b03027c98"></a>

```c
int llext_iterate ( int(* fn )(struct llext *ext, void *arg), void * arg )
```

```c
#include <zephyr/llext/llext.h>
```

遍历所有已加载的扩展。

对每个已登记的扩展调用所提供的回调函数（Callback Function），直到遍历完成或回调返回非 0 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fn` | 回调函数。 |
| `[in] arg` | 传给回调函数的私有参数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 没有已登记的扩展时返回。 |

**返回（Returns）**：返回最后一次回调调用的返回值。

## 11.24\_llext\_load()

<a id="ga0a4c3db30bc3ec7aa8a9b0e076af7157"></a>
<a id="r_ga0a4c3db30bc3ec7aa8a9b0e076af7157"></a>

```c
int llext_load ( struct llext_loader * loader, const char * name, struct llext ** ext, const struct llext_load_param * ldr_parm )
```

```c
#include <zephyr/llext/llext.h>
```

加载并链接扩展。

将相关 `ELF` 数据加载到内存，并提供用于操作这些数据的结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] loader` | 提供输入数据与上下文的扩展加载器。 |
| `[in] name` | 扩展的字符串标识符。 |
| `[out] ext` | 指向新分配的 [`llext`](P020_扩展对象.md) 结构体的指针。 |
| `[in] ldr_parm` | 可选的高级加载参数，可以为 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOMEM` | 内存不足。 |
| `-ENOEXEC` | 无效的 `ELF` 数据流。 |
| `-ENOTSUP` | 不支持的 `ELF` 特性。 |

**返回（Returns）**：成功时返回扩展此前的使用计数（Use Count），否则返回负错误码。

## 11.25\_llext\_relink\_dependency()

<a id="gab7c9e78852207c064b52b19bb924ccda"></a>
<a id="r_gab7c9e78852207c064b52b19bb924ccda"></a>

```c
int llext_relink_dependency ( struct llext * ext, unsigned int n_ext )
```

```c
#include <zephyr/llext/llext.h>
```

重新链接依赖，为挂起（Suspend）作准备。

在挂起与恢复（Suspend–Resume）场景中，若需把 LLEXT 上下文保存到非易失缓冲区，使用者可以保存大部分 LLEXT 支持数据，但必须使用 [`llext_restore`](#gad3c4daf1bf7f7e9f04451bcafc94173d)() 重新分配对象，同时恢复依赖指针。为保证依赖的保存与恢复保持一致，也为前者提供了本辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ext` | 扩展数组。 |
| `[in] n_ext` | 扩展数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOENT` | 未找到某些依赖。 |

**原文警告（Warning）**：这是实验性 API（Experimental API）的一部分，未来一定会改变！是否可用取决于默认关闭的 `CONFIG_LLEXT_EXPERIMENTAL`。

## 11.26\_llext\_restore()

<a id="gad3c4daf1bf7f7e9f04451bcafc94173d"></a>
<a id="r_gad3c4daf1bf7f7e9f04451bcafc94173d"></a>

```c
int llext_restore ( struct llext ** ext, struct llext_loader ** ldr, unsigned int n_ext )
```

```c
#include <zephyr/llext/llext.h>
```

从保存的数据恢复 LLEXT 上下文。

挂起时，使用者已经保存所有扩展和加载器描述符及相关对象，并调用 [`llext_relink_dependency`](#gab7c9e78852207c064b52b19bb924ccda)() 准备依赖指针。恢复时必须使用 `llext_alloc_metadata`() 重新分配所有对象，因此需要 LLEXT 核心提供支持。本函数接收指向已保存扩展副本和加载器副本的指针数组，重新分配所有对象并将它们加入全局扩展列表，同时将依赖指针重新链接到新分配的扩展。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] ext` | 扩展指针数组，其元素会替换为重新分配的副本。 |
| `[in,out] ldr` | 用于恢复节映射（Section Map）的加载器指针数组。 |
| `[in] n_ext` | 扩展数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOMEM` | 没有足够内存。 |
| `-EINVAL` | 保存的依赖超出范围。 |
| `-EFAULT` | 内部算法错误。 |

**原文警告（Warning）**：这是实验性 API（Experimental API）的一部分，未来一定会改变！是否可用取决于默认关闭的 `CONFIG_LLEXT_EXPERIMENTAL`。

## 11.27\_llext\_section\_count()

<a id="ga0b4a3969f1322bf77aaaa614be789bd9"></a>
<a id="r_ga0b4a3969f1322bf77aaaa614be789bd9"></a>

```c
static inline unsigned int llext_section_count ( const struct llext * ext)
```

```c
#include <zephyr/llext/llext.h>
```

取得扩展的 `ELF` 节数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ext` | 要检查的扩展。 |

**返回（Returns）**：返回节的数量。

## 11.28\_llext\_section\_headers()

<a id="ga2432e14161e327d2b1adb5bde5ce6a86"></a>
<a id="r_ga2432e14161e327d2b1adb5bde5ce6a86"></a>

```c
static inline const elf_shdr_t * llext_section_headers ( const struct llext * ext)
```

```c
#include <zephyr/llext/llext.h>
```

取得扩展的 `ELF` 节头。

只有加载扩展时设置了 `llext_load_param::keep_section_info`，节头才可用；可用期持续到为该扩展调用 [`llext_free_inspection_data`](#ga54f3aaed749e8c6bad6fbecb1622ab06) 为止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ext` | 要检查的扩展。 |

**返回（Returns）**：返回第一个节头的指针，节头总数由 [`llext_section_count`](#ga0b4a3969f1322bf77aaaa614be789bd9) 给出。

## 11.29\_llext\_teardown()

<a id="gae061bb6100ad394fcaca7751ff3dadba"></a>
<a id="r_gae061bb6100ad394fcaca7751ff3dadba"></a>

```c
int llext_teardown ( struct llext * ext)
```

```c
#include <zephyr/llext/llext.h>
```

调用扩展的清理函数（Teardown Functions）。

在调用者上下文中执行扩展自身的清理函数。本函数完成后，扩展不再可用，必须调用 [`llext_unload`](#gad3df7ed4d436846504c0047166eb929e) 将其完全卸载。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ext` | 要撤销初始化的扩展。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EFAULT` | 检测到重定位问题。 |

**参见（See Also）**：另见 [`llext_bootstrap`](#ga809f7a7976b4436dad31aa03d9ea3729)。

**返回（Returns）**：成功返回 0，否则返回负错误码。

## 11.30\_llext\_unload()

<a id="gad3df7ed4d436846504c0047166eb929e"></a>
<a id="r_gad3df7ed4d436846504c0047166eb929e"></a>

```c
int llext_unload ( struct llext ** ext)
```

```c
#include <zephyr/llext/llext.h>
```

卸载扩展。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ext` | 要卸载的扩展。 |

> 译注：本页原文没有给出此函数的返回值契约；不得据此补写为某个未经核对的固定返回值。

## 11.31\_源码对照与相关阅读

译注：本仓库的[llext.h](../../../include/zephyr/llext/llext.h)可用于跟踪声明与实现。此相对路径从本文位置解析，不绑定盘符或用户名；本仓库参照源码不自动等同于网页 latest 的版本。

[加载流程](P004_加载扩展.md) · [管理API](P011_扩展管理API.md) · [ELF检查接口](P013_ELF检查API.md) · [加载器上下文](P025_扩展加载器上下文.md) · [符号表](P028_符号表.md)。

<a id="header-groups"></a>
<a id="groups"></a>
<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953a812e884e2c4a3c6430d91998b75d7974"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953ab119ace11d5d6ca1dca32ef4ce4cef11"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953abfece5d78fbb60c5723eb39eb0df1c9d"></a>
<a id="gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P010_Shell加载器示例.md) · [返回大纲](大纲.md) · [下一章](P012_ELF常量与类型.md)
