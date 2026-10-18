---
id: learning.zephyr-docs.api-source-device-reference.page-34
title: section_tags.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/section__tags_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_section\_tags.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/section__tags_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P379_zephyr__linker__section_tags.h_文件参考.md)。

## 34.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="asections_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/* Macros for tagging symbols and putting them in the correct sections. */

/*
 * Copyright (c) 2013-2014, Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_LINKER_SECTION_TAGS_H_
#define ZEPHYR_INCLUDE_LINKER_SECTION_TAGS_H_

#include <zephyr/toolchain.h>

#if !defined(_ASMLANGUAGE)

#include <zephyr/linker/sections.h>

#define __noinit                __in_section_unique(_NOINIT_SECTION_NAME)
#define __noinit_named(name)    __in_section_unique_named(_NOINIT_SECTION_NAME, name)
#define __irq_vector_table      Z_GENERIC_SECTION(_IRQ_VECTOR_TABLE_SECTION_NAME)
#define __sw_isr_table          Z_GENERIC_SECTION(_SW_ISR_TABLE_SECTION_NAME)

#ifdef CONFIG_SHARED_INTERRUPTS
#define __shared_sw_isr_table   Z_GENERIC_SECTION(_SHARED_SW_ISR_TABLE_SECTION_NAME)
#endif /* CONFIG_SHARED_INTERRUPTS */

/* Attribute macros to place code and data into IMR memory */
#define __imr __in_section_unique(imr)
#define __imrdata __in_section_unique(imrdata)

#if defined(CONFIG_ARM)
#define __kinetis_flash_config_section __in_section_unique(_KINETIS_FLASH_CONFIG_SECTION_NAME)
#define __ti_ccfg_section Z_GENERIC_SECTION(_TI_CCFG_SECTION_NAME)
#define __itcm_section Z_GENERIC_SECTION(_ITCM_SECTION_NAME)
#define __dtcm_data_section Z_GENERIC_SECTION(_DTCM_DATA_SECTION_NAME)
#define __dtcm_bss_section Z_GENERIC_SECTION(_DTCM_BSS_SECTION_NAME)
#define __dtcm_noinit_section Z_GENERIC_SECTION(_DTCM_NOINIT_SECTION_NAME)
#define __ocm_data_section Z_GENERIC_SECTION(_OCM_DATA_SECTION_NAME)
#define __ocm_bss_section Z_GENERIC_SECTION(_OCM_BSS_SECTION_NAME)
#define __imx_boot_conf_section Z_GENERIC_SECTION(_IMX_BOOT_CONF_SECTION_NAME)
#define __imx_boot_data_section Z_GENERIC_SECTION(_IMX_BOOT_DATA_SECTION_NAME)
#define __imx_boot_ivt_section Z_GENERIC_SECTION(_IMX_BOOT_IVT_SECTION_NAME)
#define __imx_boot_dcd_section Z_GENERIC_SECTION(_IMX_BOOT_DCD_SECTION_NAME)
#define __imx_boot_container_section Z_GENERIC_SECTION(_IMX_BOOT_CONTAINER_SECTION_NAME)
#define __stm32_backup_sram_section Z_GENERIC_SECTION(_STM32_BACKUP_SRAM_SECTION_NAME)

/*
 * Deprecated aliases, provided for backwards compatibility.
 * These aliases will be removed in Zephyr v4.5.
 */
#define __ccm_data_section __dtcm_data_section __DEPRECATED_MACRO
#define __ccm_bss_section __dtcm_bss_section __DEPRECATED_MACRO
#define __ccm_noinit_section __dtcm_noinit_section __DEPRECATED_MACRO
#endif /* CONFIG_ARM */

#if defined(CONFIG_NOCACHE_MEMORY)
#define __nocache __in_section_unique(_NOCACHE_SECTION_NAME)
#define __nocache_load __in_section_unique(_NOCACHE_LOAD_SECTION_NAME)
#define __nocache_noinit __nocache
#else
#define __nocache
#define __nocache_load
#define __nocache_noinit __noinit
#endif /* CONFIG_NOCACHE_MEMORY */

#if defined(CONFIG_KERNEL_COHERENCE)
#define __incoherent __in_section_unique(cached)
#if defined(CONFIG_USERSPACE)
#define __stackmem Z_GENERIC_SECTION(.user_stacks)
#else
#define __stackmem __incoherent
#endif /* CONFIG_USERSPACE */
#define __kstackmem __incoherent
#else
#define __incoherent
#define __stackmem Z_GENERIC_SECTION(.user_stacks)
#define __kstackmem __noinit
#endif /* CONFIG_KERNEL_COHERENCE */

#if defined(CONFIG_LINKER_USE_BOOT_SECTION)
#define __boot_func     Z_GENERIC_DOT_SECTION(BOOT_TEXT_SECTION_NAME)
#define __boot_data     Z_GENERIC_DOT_SECTION(BOOT_DATA_SECTION_NAME)
#define __boot_rodata   Z_GENERIC_DOT_SECTION(BOOT_RODATA_SECTION_NAME)
#define __boot_bss      Z_GENERIC_DOT_SECTION(BOOT_BSS_SECTION_NAME)
#define __boot_noinit   Z_GENERIC_DOT_SECTION(BOOT_NOINIT_SECTION_NAME)
#else
#define __boot_func
#define __boot_data
#define __boot_rodata
#define __boot_bss
#define __boot_noinit   __noinit
#endif /* CONFIG_LINKER_USE_BOOT_SECTION */

#if defined(CONFIG_LINKER_USE_ONDEMAND_SECTION)
#define __ondemand_func Z_GENERIC_DOT_SECTION(ONDEMAND_TEXT_SECTION_NAME)
#define __ondemand_rodata       Z_GENERIC_DOT_SECTION(ONDEMAND_RODATA_SECTION_NAME)
#else
#define __ondemand_func
#define __ondemand_rodata
#endif /* CONFIG_LINKER_USE_ONDEMAND_SECTION */

#define __isr

/* Symbol table section */
#if defined(CONFIG_SYMTAB)
#define __symtab_info           Z_GENERIC_SECTION(_SYMTAB_INFO_SECTION_NAME)
#define __symtab_entry          Z_GENERIC_SECTION(_SYMTAB_ENTRY_SECTION_NAME)
#endif /* CONFIG_SYMTAB */

#endif /* !_ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_LINKER_SECTION_TAGS_H_ */
```

## 34.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

用于标记符号（Tagging Symbols）并将其放入正确区段（Sections）的宏。

### 注释 2：原第 3 行

版权（Copyright）：© 2013-2014, Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 25 行

条件编译配置（Configuration）标记：`CONFIG_SHARED_INTERRUPTS`。

### 注释 4：原第 27 行

将代码和数据放入隔离内存区域（IMR Memory）的属性宏（Attribute Macros）。

### 注释 5：原第 47 行

为向后兼容（Backwards Compatibility）而提供的已弃用别名（Deprecated Aliases）。这些别名将在 Zephyr v4.5 中移除。

### 注释 6：原第 54 行

条件编译配置（Configuration）标记：`CONFIG_ARM`。

### 注释 7：原第 64 行

条件编译配置（Configuration）标记：`CONFIG_NOCACHE_MEMORY`。

### 注释 8：原第 72 行

条件编译配置（Configuration）标记：`CONFIG_USERSPACE`。

### 注释 9：原第 78 行

条件编译配置（Configuration）标记：`CONFIG_KERNEL_COHERENCE`。

### 注释 10：原第 92 行

条件编译配置（Configuration）标记：`CONFIG_LINKER_USE_BOOT_SECTION`。

### 注释 11：原第 100 行

条件编译配置（Configuration）标记：`CONFIG_LINKER_USE_ONDEMAND_SECTION`。

### 注释 12：原第 104 行

符号表区段（Symbol Table Section）。

### 注释 13：原第 108 行

条件编译配置（Configuration）标记：`CONFIG_SYMTAB`。

### 注释 14：原第 110 行

条件编译表达式：`!_ASMLANGUAGE`。

### 注释 15：原第 112 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LINKER_SECTION_TAGS_H_`。

## 34.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P379_zephyr__linker__section_tags.h_文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/linker/sections.h](../api_file_supplement_reference/P106_zephyr__linker__sections.h_文件参考.md)
- [sections.h](../api_file_supplement_reference/P106_zephyr__linker__sections.h_文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P033_gd32f3x0.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P035_st-zio-header.h_源码浏览.md)
