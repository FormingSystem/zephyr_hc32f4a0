---
id: learning.zephyr-docs.linker-reference.page-8
title: GNU链接器适配头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-gcc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_GNU链接器适配头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-gcc_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P007_GNU链接器适配头文件参考.md)和[公共API](P007_GNU链接器适配头文件参考.md)。

## 8.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00186"></a>
<a id="foldopen00211"></a>
<a id="amm_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2013-2014, Wind River Systems, Inc.
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>#ifndef ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_GCC_H_
<a id="l00016"></a>#define ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_GCC_H_
<a id="l00017"></a>
<a id="l00018"></a>#include &lt;zephyr/kernel/mm.h&gt;
<a id="l00019"></a>
<a id="l00020"></a>#if defined(CONFIG_ARM)
<a id="l00021"></a>        #if defined(CONFIG_BIG_ENDIAN)
<a id="l00022"></a>                #define OUTPUT_FORMAT_ "elf32-bigarm"
<a id="l00023"></a>        #else
<a id="l00024"></a>                #define OUTPUT_FORMAT_ "elf32-littlearm"
<a id="l00025"></a>        #endif
<a id="l00026"></a>        OUTPUT_FORMAT(OUTPUT_FORMAT_)
<a id="l00027"></a>#elif defined(CONFIG_ARM64)
<a id="l00028"></a>        OUTPUT_FORMAT("elf64-littleaarch64")
<a id="l00029"></a>#elif defined(CONFIG_ARC)
<a id="l00030"></a>        #if defined(CONFIG_ISA_ARCV3) &amp;&amp; defined(CONFIG_64BIT)
<a id="l00031"></a>                OUTPUT_FORMAT("elf64-littlearc64")
<a id="l00032"></a>        #elif defined(CONFIG_ISA_ARCV3) &amp;&amp; !defined(CONFIG_64BIT)
<a id="l00033"></a>                OUTPUT_FORMAT("elf32-littlearc64")
<a id="l00034"></a>        #else
<a id="l00035"></a>                OUTPUT_FORMAT("elf32-littlearc", "elf32-bigarc", "elf32-littlearc")
<a id="l00036"></a>        #endif
<a id="l00037"></a>#elif defined(CONFIG_X86)
<a id="l00038"></a>        #if defined(CONFIG_X86_64)
<a id="l00039"></a>                OUTPUT_FORMAT("elf64-x86-64")
<a id="l00040"></a>                OUTPUT_ARCH("i386:x86-64")
<a id="l00041"></a>        #else
<a id="l00042"></a>                OUTPUT_FORMAT("elf32-i386", "elf32-i386", "elf32-i386")
<a id="l00043"></a>                OUTPUT_ARCH("i386")
<a id="l00044"></a>        #endif
<a id="l00045"></a>#elif defined(CONFIG_RISCV)
<a id="l00046"></a>        OUTPUT_ARCH("riscv")
<a id="l00047"></a>#ifdef CONFIG_64BIT
<a id="l00048"></a>        OUTPUT_FORMAT("elf64-littleriscv")
<a id="l00049"></a>#else
<a id="l00050"></a>        OUTPUT_FORMAT("elf32-littleriscv")
<a id="l00051"></a>#endif
<a id="l00052"></a>#elif defined(CONFIG_XTENSA)
<a id="l00053"></a>        /* Not needed */
<a id="l00054"></a>#elif defined(CONFIG_MIPS)
<a id="l00055"></a>        OUTPUT_ARCH("mips")
<a id="l00056"></a>#elif defined(CONFIG_ARCH_POSIX)
<a id="l00057"></a>        /* Not needed */
<a id="l00058"></a>#elif defined(CONFIG_SPARC)
<a id="l00059"></a>        OUTPUT_FORMAT("elf32-sparc")
<a id="l00060"></a>#elif defined(CONFIG_RX)
<a id="l00061"></a>        OUTPUT_FORMAT("elf32-rx-le")
<a id="l00062"></a>#elif defined(CONFIG_OPENRISC)
<a id="l00063"></a>        OUTPUT_FORMAT("elf32-or1k")
<a id="l00064"></a>#elif defined(CONFIG_HEXAGON)
<a id="l00065"></a>        OUTPUT_FORMAT("elf32-hexagon")
<a id="l00066"></a>#elif defined(CONFIG_TRICORE)
<a id="l00067"></a>        OUTPUT_FORMAT("elf32-tricore")
<a id="l00068"></a>#else
<a id="l00069"></a>        #error Arch not supported.
<a id="l00070"></a>#endif
<a id="l00071"></a>
<a id="l00072"></a>/*
<a id="l00073"></a> * The GROUP_START() and GROUP_END() macros are used to define a group
<a id="l00074"></a> * of sections located in one memory area, such as RAM, ROM, etc.
<a id="l00075"></a> * The &lt;where&gt; parameter is the name of the memory area.
<a id="l00076"></a> */
<a id="l00077"></a>#define GROUP_START(where)
<a id="l00078"></a>#define GROUP_END(where)
<a id="l00079"></a>
<a id="l00096"></a>#if defined(CONFIG_ARCH_POSIX)
<a id="l00097"></a>#define GROUP_LINK_IN(where)
<a id="l00098"></a>#elif !defined(K_MEM_IS_VM_KERNEL)
<a id="l00099"></a>#define GROUP_LINK_IN(where) &gt; where
<a id="l00100"></a>#endif
<a id="l00101"></a>
<a id="l00120"></a>#if defined(CONFIG_ARCH_POSIX)
<a id="l00121"></a>#define GROUP_ROM_LINK_IN(vregion, lregion)
<a id="l00122"></a>#elif defined(K_MEM_IS_VM_KERNEL)
<a id="l00123"></a>#define GROUP_ROM_LINK_IN(vregion, lregion) &gt; vregion AT &gt; lregion
<a id="l00124"></a>#else
<a id="l00125"></a>#define GROUP_ROM_LINK_IN(vregion, lregion) &gt; lregion
<a id="l00126"></a>#endif
<a id="l00127"></a>
<a id="l00140"></a>#if defined(CONFIG_ARCH_POSIX)
<a id="l00141"></a>#define GROUP_DATA_LINK_IN(vregion, lregion)
<a id="l00142"></a>#elif defined(CONFIG_XIP) || defined(K_MEM_IS_VM_KERNEL)
<a id="l00143"></a>#define GROUP_DATA_LINK_IN(vregion, lregion) &gt; vregion AT &gt; lregion
<a id="l00144"></a>#else
<a id="l00145"></a>#define GROUP_DATA_LINK_IN(vregion, lregion) &gt; vregion
<a id="l00146"></a>#endif
<a id="l00147"></a>
<a id="l00158"></a>#if defined(CONFIG_ARCH_POSIX)
<a id="l00159"></a>#define GROUP_NOLOAD_LINK_IN(vregion, lregion)
<a id="l00160"></a>#elif defined(K_MEM_IS_VM_KERNEL)
<a id="l00161"></a>#define GROUP_NOLOAD_LINK_IN(vregion, lregion) &gt; vregion AT &gt; lregion
<a id="l00162"></a>#elif defined(CONFIG_XIP)
<a id="l00163"></a>#define GROUP_NOLOAD_LINK_IN(vregion, lregion) &gt; vregion AT &gt; vregion
<a id="l00164"></a>#else
<a id="l00165"></a>#define GROUP_NOLOAD_LINK_IN(vregion, lregion) &gt; vregion
<a id="l00166"></a>#endif
<a id="l00167"></a>
<a id="l00181"></a>#ifdef K_MEM_IS_VM_KERNEL
<a id="l00182"></a>/* If we have a virtual memory map we need ALIGN_WITH_INPUT in all sections */
<a id="l00183"></a>#define SECTION_PROLOGUE(name, options, align) \
<a id="l00184"></a>        name options : ALIGN_WITH_INPUT align
<a id="l00185"></a>#else
<a id="l00186"></a>#define SECTION_PROLOGUE(name, options, align) \
<a id="l00187"></a>        name options : align
<a id="l00188"></a>#endif
<a id="l00189"></a>
<a id="l00207"></a>#if defined(CONFIG_XIP)
<a id="l00208"></a>#define SECTION_DATA_PROLOGUE(name, options, align) \
<a id="l00209"></a>        name options : ALIGN_WITH_INPUT
<a id="l00210"></a>#else
<a id="l00211"></a>#define SECTION_DATA_PROLOGUE(name, options, align) \
<a id="l00212"></a>        SECTION_PROLOGUE(name, options, align)
<a id="l00213"></a>#endif
<a id="l00214"></a>
<a id="l00215"></a>#define COMMON_SYMBOLS *(COMMON)
<a id="l00216"></a>
<a id="l00217"></a>#endif /* ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_GCC_H_ */
</code></pre>

## 8.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2013-2014, Wind River Systems, Inc.；Apache-2.0许可证原文保留。

2. 此处不需要设置（Not Needed）。

3. 此处不需要设置（Not Needed）。

4. GROUP_START()和GROUP_END()用于定义位于同一内存区域（如RAM、ROM等）的一组段。where参数是内存区域名称。

5. 存在虚拟内存映射时，所有段都需要ALIGN_WITH_INPUT。

6. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_GCC_H_。

## 8.3\_原页符号提示（Symbol Descriptions）

### `mm.h`

符号定位：[mm.h](https://docs.zephyrproject.org/latest/doxygen/html/mm_8h.html)。

## 8.4\_源码跟踪译注

> 译注——两类地址：虚拟内存地址（Virtual Memory Address，VMA）表示段的运行地址，装载内存地址（Load Memory Address，LMA）表示装载镜像位置。GROUP_DATA_LINK_IN在XIP或K_MEM_IS_VM_KERNEL分支生成> vregion AT > lregion，普通分支只指定vregion。宏描述布局，不执行启动复制；需要由启动代码消费相应符号。

> 译注——虚拟内核条件：实际GNU宏判断K_MEM_IS_VM_KERNEL。kernel/internal/mm.h在K_MEM_VIRT_OFFSET非0时定义它，并拒绝同时启用XIP；不要把只启用CONFIG_MMU与地址存在偏移混为一谈。此分支不定义单参数GROUP_LINK_IN，要求明确VMA与LMA；CONFIG_ARCH_POSIX分支的区域放置宏为空。

> 译注——NOLOAD与对齐：GROUP_NOLOAD_LINK_IN在虚拟内核分支指定vregion和lregion，在XIP分支使用> vregion AT > vregion，其他分支只指定vregion。GCC的SECTION_DATA_PROLOGUE在XIP下输出ALIGN_WITH_INPUT且未引用传入align实参；非XIP下转交SECTION_PROLOGUE。应核对实际分支，不能认为每种适配都以相同方式使用三个参数。

> 译注——版本边界：本批记录八份链接器头文件、设备树绑定、三份链接器CMake文件、日志链接片段及两份内存管理头文件，共十五份官方源码摘要。八个源码浏览页的非注释代码与本次读取的原始头文件逐项核对；滚动main、latest与本仓库参照版本不自动等同。本次未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

头文件相对定位：[include/zephyr/linker/linker-tool-gcc.h](../../../include/zephyr/linker/linker-tool-gcc.h)，关联实现／接口：[include/zephyr/linker/linker-tool-gcc.h](../../../include/zephyr/linker/linker-tool-gcc.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/linker/linker-tool-gcc.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/linker/linker-tool-gcc.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

## 8.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P007_GNU链接器适配头文件参考.md)
- [zephyr/kernel/mm.h](https://docs.zephyrproject.org/latest/doxygen/html/mm_8h.html)

---

[上一章](P007_GNU链接器适配头文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_LLD链接器适配头文件参考.md)
