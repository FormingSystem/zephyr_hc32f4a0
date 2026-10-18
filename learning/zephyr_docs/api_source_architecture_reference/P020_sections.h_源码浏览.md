---
id: learning.zephyr-docs.api-source-architecture-reference.page-20
title: sections.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sections_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_sections.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sections_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P106_zephyr__linker__sections.h_文件参考.md)。

## 20.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
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
<a id="asection__tags_8h_html"></a>

```c
/*
 * Copyright (c) 2013-2014, Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_LINKER_SECTIONS_H_
#define ZEPHYR_INCLUDE_LINKER_SECTIONS_H_

#define _TEXT_SECTION_NAME text
#define _RODATA_SECTION_NAME rodata
#define _CTOR_SECTION_NAME ctors
/* Linker issue with XIP where the name "data" cannot be used */
#define _DATA_SECTION_NAME datas
#define _BSS_SECTION_NAME bss
#define _NOINIT_SECTION_NAME noinit

#define _APP_SMEM_SECTION_NAME          app_smem
#define _APP_DATA_SECTION_NAME          app_datas
#define _APP_BSS_SECTION_NAME           app_bss
#define _APP_NOINIT_SECTION_NAME        app_noinit

#define _UNDEFINED_SECTION_NAME undefined

/* Interrupts */
#define _IRQ_VECTOR_TABLE_SECTION_NAME  .gnu.linkonce.irq_vector_table
#define _IRQ_VECTOR_TABLE_SECTION_SYMS  .gnu.linkonce.irq_vector_table*

#define _SW_ISR_TABLE_SECTION_NAME      .gnu.linkonce.sw_isr_table
#define _SW_ISR_TABLE_SECTION_SYMS      .gnu.linkonce.sw_isr_table*

#ifdef CONFIG_SHARED_INTERRUPTS
#define _SHARED_SW_ISR_TABLE_SECTION_NAME       .gnu.linkonce.shared_sw_isr_table
#define _SHARED_SW_ISR_TABLE_SECTION_SYMS       .gnu.linkonce.shared_sw_isr_table*
#endif /* CONFIG_SHARED_INTERRUPTS */

/* Architecture-specific sections */
#if defined(CONFIG_ARM)
#define _KINETIS_FLASH_CONFIG_SECTION_NAME  kinetis_flash_config
#define _TI_CCFG_SECTION_NAME           .ti_ccfg

#define _ITCM_SECTION_NAME              .itcm

#define _DTCM_DATA_SECTION_NAME         .dtcm_data
#define _DTCM_BSS_SECTION_NAME          .dtcm_bss
#define _DTCM_NOINIT_SECTION_NAME       .dtcm_noinit

#define _OCM_DATA_SECTION_NAME          .ocm_data
#define _OCM_BSS_SECTION_NAME           .ocm_bss
#endif

#define _IMX_BOOT_CONF_SECTION_NAME     .boot_hdr.conf
#define _IMX_BOOT_DATA_SECTION_NAME     .boot_hdr.data
#define _IMX_BOOT_IVT_SECTION_NAME      .boot_hdr.ivt
#define _IMX_BOOT_DCD_SECTION_NAME      .boot_hdr.dcd_data
#define _IMX_BOOT_CONTAINER_SECTION_NAME .boot_hdr.container

#define _STM32_BACKUP_SRAM_SECTION_NAME .stm32_backup_sram

#ifdef CONFIG_NOCACHE_MEMORY
#define _NOCACHE_SECTION_NAME nocache
#define _NOCACHE_LOAD_SECTION_NAME nocache_load
#define _NOCACHE_PAD_SECTION_NAME nocache_pad
#endif

/* Symbol table section */
#if defined(CONFIG_SYMTAB)
#define _SYMTAB_INFO_SECTION_NAME       .gnu.linkonce.symtab.info
#define _SYMTAB_ENTRY_SECTION_NAME      .gnu.linkonce.symtab.entry
#define _SYMTAB_SECTION_SYMS            .gnu.linkonce.symtab*
#endif /* CONFIG_SYMTAB */

#if defined(CONFIG_LINKER_USE_BOOT_SECTION)
#define BOOT_TEXT_SECTION_NAME          boot_text
#define BOOT_BSS_SECTION_NAME           boot_bss
#define BOOT_RODATA_SECTION_NAME        boot_rodata
#define BOOT_DATA_SECTION_NAME          boot_data
#define BOOT_NOINIT_SECTION_NAME        boot_noinit
#endif

#if defined(CONFIG_LINKER_USE_ONDEMAND_SECTION)
#define ONDEMAND_TEXT_SECTION_NAME      ondemand_text
#define ONDEMAND_RODATA_SECTION_NAME    ondemand_rodata
#endif

/* Short section references for use in ASM files */
#if defined(_ASMLANGUAGE)
/* Various text section names */
#define TEXT text

/* Various data type section names */
#define BSS bss
#define RODATA rodata
#define DATA data
#define NOINIT noinit

#if defined(CONFIG_LINKER_USE_BOOT_SECTION)
#define BOOT_TEXT                       BOOT_TEXT_SECTION_NAME
#define BOOT_BSS                        BOOT_BSS_SECTION_NAME
#define BOOT_RODATA                     BOOT_RODATA_SECTION_NAME
#define BOOT_DATA                       BOOT_DATA_SECTION_NAME
#define BOOT_NOINIT                     BOOT_NOINIT_SECTION_NAME
#else
#define BOOT_TEXT                       TEXT
#define BOOT_BSS                        BSS
#define BOOT_RODATA                     RODATA
#define BOOT_DATA                       DATA
#define BOOT_NOINIT                     NOINIT
#endif /* CONFIG_LINKER_USE_BOOT_SECTION */

#if defined(CONFIG_LINKER_USE_ONDEMAND_SECTION)
#define ONDEMAND_TEXT                   ONDEMAND_TEXT_SECTION_NAME
#define ONDEMAND_RODATA         ONDEMAND_RODATA_SECTION_NAME
#else
#define ONDEMAND_TEXT                   TEXT
#define ONDEMAND_RODATA         RODATA
#endif /* CONFIG_LINKER_USE_ONDEMAND_SECTION */

#endif /* _ASMLANGUAGE */

#include <zephyr/linker/section_tags.h>

#endif /* ZEPHYR_INCLUDE_LINKER_SECTIONS_H_ */
```

## 20.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2013-2014, Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

就地执行（XIP）场景中的链接器问题（Linker Issue）：不能使用名称 `data`。

### 注释 3：原第 33 行

中断（Interrupts）。

### 注释 4：原第 43 行

条件编译配置（Configuration）标记：`CONFIG_SHARED_INTERRUPTS`。

### 注释 5：原第 45 行

架构专用区段（Architecture-Specific Sections）。

### 注释 6：原第 74 行

符号表区段（Symbol Table Section）。

### 注释 7：原第 79 行

条件编译配置（Configuration）标记：`CONFIG_SYMTAB`。

### 注释 8：原第 94 行

供汇编文件（ASM Files）使用的区段简写引用（Short Section References）。

### 注释 9：原第 96 行

各种代码区段名称（Text Section Names）。

### 注释 10：原第 99 行

各种数据类型区段名称（Data Type Section Names）。

### 注释 11：原第 117 行

条件编译配置（Configuration）标记：`CONFIG_LINKER_USE_BOOT_SECTION`。

### 注释 12：原第 125 行

条件编译配置（Configuration）标记：`CONFIG_LINKER_USE_ONDEMAND_SECTION`。

### 注释 13：原第 127 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 14：原第 131 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LINKER_SECTIONS_H_`。

## 20.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P106_zephyr__linker__sections.h_文件参考.md)
- [zephyr/linker/section_tags.h](../api_file_reference/P379_zephyr__linker__section_tags.h_文件参考.md)
- [section_tags.h](../api_file_reference/P379_zephyr__linker__section_tags.h_文件参考.md)

---

[上一章](P019_sdp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P021_tc_util.h_源码浏览.md)
