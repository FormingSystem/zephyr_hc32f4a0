---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-25
title: symbol.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/symbol_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_symbol.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/symbol_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/symbol_8h.html)。

## 25.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00032"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="foldopen00239"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="foldopen00274"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="foldopen00291"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructgroup_html"></a>
<a id="astructllext__const__symbol_html"></a>
<a id="astructllext__const__symbol_html_a8e18aab091d8aa99b94eed2e215400f9"></a>
<a id="astructllext__const__symbol_html_ac0bb3e3c67e91f790a1284f3ebc260b2"></a>
<a id="astructllext__const__symbol_html_afe01c08dff4f9334a95a9be23aede72b"></a>
<a id="astructllext__symbol_html"></a>
<a id="astructllext__symbol_html_ae827718e18c718002eeb0cc3a3ae0ab3"></a>
<a id="astructllext__symbol_html_ae9d19614618dc3c000f3c4e71dbda5ac"></a>
<a id="astructllext__symtable_html"></a>
<a id="astructllext__symtable_html_a1e65bbdadb52a27b60e835994357cca1"></a>
<a id="astructllext__symtable_html_ac03152f3cb9d1881feed1d840dd024d9"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_LLEXT_SYMBOL_H_
#define ZEPHYR_INCLUDE_LLEXT_SYMBOL_H_

#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif


struct llext_const_symbol {
        union {
                const char *const name;

                const uintptr_t slid;
        };

        const void *const addr;
};
BUILD_ASSERT(sizeof(struct llext_const_symbol) == 2 * sizeof(uintptr_t));

struct llext_symbol {
        const char *name;

        void *addr;
};


struct llext_symtable {
        size_t sym_cnt;

        struct llext_symbol *syms;
};


struct z_llext_discarded_const_symbol {
        const char *const name;

        const char *const group;
};

#define Z_LLEXT_DISCARD_STRTAB Z_GENERIC_SECTION(llext_discarded_exports_strtab)

#ifdef CONFIG_LLEXT
#define Z_MARKUP_NOT_EXPORTED_SYMBOL(grp, sym_ident, sym_name)          \
        static const char Z_LLEXT_DISCARD_STRTAB __used                         \
                __llext_sym_name_ ## sym_name[] = STRINGIFY(sym_name);          \
        static const char Z_LLEXT_DISCARD_STRTAB __used                         \
                __llext_sym_group_ ## sym_name[] = STRINGIFY(grp);              \
        static const struct z_llext_discarded_const_symbol                      \
                Z_GENERIC_SECTION(llext_discarded_exports_table) __used         \
                __llext_sym_discarded_ ## sym_name = {                          \
                        .name = __llext_sym_name_ ## sym_name,                  \
                        .group = __llext_sym_group_ ## sym_name,                \
        };
#else /* CONFIG_LLEXT */
/* No extension support in this build */
#define Z_MARKUP_NOT_EXPORTED_SYMBOL(grp, sym_ident, sym_name)
#endif /* CONFIG_LLEXT */


#ifdef LL_EXTENSION_BUILD
/* Extension build: add exported symbols to llext table */
#define Z_LL_EXTENSION_SYMBOL_NAMED(sym_ident, sym_name)                        \
        static const struct llext_const_symbol                                  \
                        Z_GENERIC_SECTION(.exported_sym) __used                 \
                        __llext_sym_ ## sym_name = {                            \
                .name = STRINGIFY(sym_name), .addr = (const void *)&sym_ident,  \
        }
#else
/* No-op when not building an extension */
#define Z_LL_EXTENSION_SYMBOL_NAMED(sym_ident, sym_name)
#endif

#define LL_EXTENSION_SYMBOL_NAMED(sym_ident, sym_name)                          \
        Z_LL_EXTENSION_SYMBOL_NAMED(sym_ident, sym_name)

#define LL_EXTENSION_SYMBOL(x) Z_LL_EXTENSION_SYMBOL_NAMED(x, x)

#if defined(LL_EXTENSION_BUILD)
/* Extension build: EXPORT_SYMBOL maps to LL_EXTENSION_SYMBOL */
#define Z_EXPORT_SYMBOL_NAMED(sym_ident, sym_name)                              \
        Z_LL_EXTENSION_SYMBOL_NAMED(sym_ident, sym_name)
#elif defined(CONFIG_LLEXT_EXPORT_BUILTINS_BY_SLID)
/* SLID-enabled LLEXT application: export symbols, names in separate section */
#define Z_EXPORT_SYMBOL_NAMED(sym_ident, sym_name)                              \
        static const char Z_GENERIC_SECTION(llext_exports_strtab) __used        \
                __llext_sym_name_ ## sym_name[] = STRINGIFY(sym_name);          \
        static const STRUCT_SECTION_ITERABLE(llext_const_symbol,                \
                                             __llext_sym_ ## sym_name) = {      \
                .name = __llext_sym_name_ ## sym_name,                          \
                .addr = (const void *)&sym_ident,                               \
        }
#elif defined(CONFIG_LLEXT)
/* LLEXT application: export symbols */
#define Z_EXPORT_SYMBOL_NAMED(sym_ident, sym_name)                              \
        static const STRUCT_SECTION_ITERABLE(llext_const_symbol,                \
                                             __llext_sym_ ## sym_name) = {      \
                .name = STRINGIFY(sym_name), .addr = (const void *)&sym_ident,  \
        }
#else
/* No extension support in this build */
#define Z_EXPORT_SYMBOL_NAMED(sym_ident, sym_name)
#endif

#if defined(LL_EXTENSION_BUILD)
/* Extension build: No Kconfig conditionals */
#define Z_EXPORT_SYMBOL_NAMED_IN_GROUP(group, sym_ident, sym_name)              \
        Z_EXPORT_SYMBOL_NAMED(sym_ident, sym_name)
#else
/* LLEXT application: Export if relevant group is enabled */
#define Z_EXPORT_SYMBOL_NAMED_IN_GROUP(group, sym_ident, sym_name)              \
        COND_CODE_1(CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_ ## group,                 \
                (Z_EXPORT_SYMBOL_NAMED(sym_ident, sym_name)),                   \
                (Z_MARKUP_NOT_EXPORTED_SYMBOL(group, sym_ident, sym_name)))
#endif /* defined(LL_EXTENSION_BUILD) */

#define EXPORT_SYMBOL_NAMED(sym_ident, sym_name)                                \
        Z_EXPORT_SYMBOL_NAMED_IN_GROUP(UNASSIGNED, sym_ident, sym_name)

#define EXPORT_SYMBOL(x) EXPORT_SYMBOL_NAMED(x, x)

#define EXPORT_GROUP_SYMBOL_NAMED(group, sym_ident, sym_name)                   \
        Z_EXPORT_SYMBOL_NAMED_IN_GROUP(group, sym_ident, sym_name)

#define EXPORT_GROUP_SYMBOL(group, sym_ident) \
        EXPORT_GROUP_SYMBOL_NAMED(group, sym_ident, sym_ident)


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_LLEXT_SYMBOL_H_ */
```

## 25.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 138 行

条件编译配置（Configuration）标记：`CONFIG_LLEXT`。

### 注释 3：原第 139 行

本次构建不支持扩展（extension）。

### 注释 4：原第 141 行

条件编译配置（Configuration）标记：`CONFIG_LLEXT`。

### 注释 5：原第 147 行

扩展构建（extension build）：将导出符号（exported symbols）添加到 LLEXT 表。

### 注释 6：原第 155 行

未构建扩展时不执行操作（no-op）。

### 注释 7：原第 187 行

扩展构建：将 `EXPORT_SYMBOL` 映射到 `LL_EXTENSION_SYMBOL`。

### 注释 8：原第 191 行

启用 SLID 的可加载扩展（LLEXT）应用：导出符号，名称放在独立节（section）中。

### 注释 9：原第 201 行

LLEXT 应用：导出符号。

### 注释 10：原第 208 行

本次构建不支持扩展（extension）。

### 注释 11：原第 214 行

扩展构建：不使用 Kconfig 条件判断。

### 注释 12：原第 218 行

LLEXT 应用：启用相关分组时导出。

### 注释 13：原第 223 行

条件表达式：`defined(LL_EXTENSION_BUILD)`。

### 注释 14：原第 303 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LLEXT_SYMBOL_H_`。

## 25.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/symbol_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [llext_const_symbol](../llext/P022_常量符号.md)
- [name](../llext/P022_常量符号.md#a8e18aab091d8aa99b94eed2e215400f9)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [slid](../llext/P022_常量符号.md#afe01c08dff4f9334a95a9be23aede72b)
- [addr](../llext/P022_常量符号.md#ac0bb3e3c67e91f790a1284f3ebc260b2)
- [llext_symbol](../llext/P027_动态符号.md)
- [name](../llext/P027_动态符号.md#ae827718e18c718002eeb0cc3a3ae0ab3)
- [addr](../llext/P027_动态符号.md#ae9d19614618dc3c000f3c4e71dbda5ac)
- [llext_symtable](../llext/P028_符号表.md)
- [sym_cnt](../llext/P028_符号表.md#a1e65bbdadb52a27b60e835994357cca1)
- [syms](../llext/P028_符号表.md#ac03152f3cb9d1881feed1d840dd024d9)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [llext_const_symbol::name](../llext/P022_常量符号.md#a8e18aab091d8aa99b94eed2e215400f9)
- [llext_const_symbol::addr](../llext/P022_常量符号.md#ac0bb3e3c67e91f790a1284f3ebc260b2)
- [llext_const_symbol::slid](../llext/P022_常量符号.md#afe01c08dff4f9334a95a9be23aede72b)
- [llext_symbol::name](../llext/P027_动态符号.md#ae827718e18c718002eeb0cc3a3ae0ab3)
- [llext_symbol::addr](../llext/P027_动态符号.md#ae9d19614618dc3c000f3c4e71dbda5ac)
- [llext_symtable::sym_cnt](../llext/P028_符号表.md#a1e65bbdadb52a27b60e835994357cca1)
- [llext_symtable::syms](../llext/P028_符号表.md#ac03152f3cb9d1881feed1d840dd024d9)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P024_sensor.h_源码浏览.md) · [返回大纲](大纲.md)
