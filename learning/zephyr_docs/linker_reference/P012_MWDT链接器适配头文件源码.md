---
id: learning.zephyr-docs.linker-reference.page-12
title: MWDT链接器适配头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-mwdt_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_MWDT链接器适配头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-mwdt_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P011_MWDT链接器适配头文件参考.md)和[公共API](P011_MWDT链接器适配头文件参考.md)。

## 12.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。


<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2020, Synopsys, Inc.
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>#ifndef ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_MWDT_H_
<a id="l00016"></a>#define ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_MWDT_H_
<a id="l00017"></a>
<a id="l00018"></a>/*
<a id="l00019"></a> * mwdt linker doesn't have the following directives
<a id="l00020"></a> */
<a id="l00021"></a>#define ASSERT(x, y)
<a id="l00022"></a>#define SUBALIGN(x) ALIGN(x)
<a id="l00023"></a>
<a id="l00024"></a>/*
<a id="l00025"></a> * The GROUP_START() and GROUP_END() macros are used to define a group
<a id="l00026"></a> * of sections located in one memory area, such as RAM, ROM, etc.
<a id="l00027"></a> * The &lt;where&gt; parameter is the name of the memory area.
<a id="l00028"></a> */
<a id="l00029"></a>#define GROUP_START(where)
<a id="l00030"></a>#define GROUP_END(where)
<a id="l00031"></a>
<a id="l00032"></a>/*
<a id="l00033"></a> * The GROUP_LINK_IN() macro is located at the end of the section
<a id="l00034"></a> * description and tells the linker that this section is located in
<a id="l00035"></a> * the memory area specified by &lt;where&gt; argument.
<a id="l00036"></a> */
<a id="l00037"></a>#define GROUP_LINK_IN(where) &gt; where
<a id="l00038"></a>
<a id="l00045"></a>#define GROUP_ROM_LINK_IN(vregion, lregion) &gt; lregion
<a id="l00046"></a>
<a id="l00047"></a>/*
<a id="l00048"></a> * As GROUP_LINK_IN(), but takes a second argument indicating the
<a id="l00049"></a> * memory region (e.g. "ROM") for the load address.  Used for
<a id="l00050"></a> * initialized data sections that on XIP platforms must be copied at
<a id="l00051"></a> * startup.
<a id="l00052"></a> *
<a id="l00053"></a> * And, because output directives in GNU ld are "sticky", this must
<a id="l00054"></a> * also be used on the first section *after* such an initialized data
<a id="l00055"></a> * section, specifying the same memory region (e.g. "RAM") for both
<a id="l00056"></a> * vregion and lregion.
<a id="l00057"></a> */
<a id="l00058"></a>#ifdef CONFIG_XIP
<a id="l00059"></a>#define GROUP_DATA_LINK_IN(vregion, lregion) &gt; vregion AT &gt; lregion
<a id="l00060"></a>#else
<a id="l00061"></a>#define GROUP_DATA_LINK_IN(vregion, lregion) &gt; vregion
<a id="l00062"></a>#endif
<a id="l00063"></a>
<a id="l00068"></a>#ifdef CONFIG_XIP
<a id="l00069"></a>#define GROUP_NOLOAD_LINK_IN(vregion, lregion) &gt; vregion AT &gt; vregion
<a id="l00070"></a>#else
<a id="l00071"></a>#define GROUP_NOLOAD_LINK_IN(vregion, lregion) &gt; vregion
<a id="l00072"></a>#endif
<a id="l00073"></a>
<a id="l00074"></a>/*
<a id="l00075"></a> * The SECTION_PROLOGUE() macro is used to define the beginning of a section.
<a id="l00076"></a> * The &lt;name&gt; parameter is the name of the section, and the &lt;option&gt; parameter
<a id="l00077"></a> * is to include any special options such as (NOLOAD). Page alignment has its
<a id="l00078"></a> * own parameter since it needs abstraction across the different toolchains.
<a id="l00079"></a> * If not required, the &lt;options&gt; and &lt;align&gt; parameters should be left blank.
<a id="l00080"></a> */
<a id="l00081"></a>#define SECTION_PROLOGUE(name, options, align) name options : align
<a id="l00082"></a>
<a id="l00083"></a>/*
<a id="l00084"></a> * As for SECTION_PROLOGUE(), except that this one must (!) be used
<a id="l00085"></a> * for data sections which on XIP platforms will have differing
<a id="l00086"></a> * virtual and load addresses (i.e. they'll be copied into RAM at
<a id="l00087"></a> * program startup).  Such a section must (!) also use
<a id="l00088"></a> * GROUP_LINK_IN_LMA to specify the correct output load address.
<a id="l00089"></a> */
<a id="l00090"></a>#ifdef CONFIG_XIP
<a id="l00091"></a>#define SECTION_DATA_PROLOGUE(name, options, align) \
<a id="l00092"></a>        name options ALIGN(8) : align
<a id="l00093"></a>#else
<a id="l00094"></a>#define SECTION_DATA_PROLOGUE(name, options, align) name options : align
<a id="l00095"></a>
<a id="l00096"></a>#endif
<a id="l00097"></a>
<a id="l00098"></a>#define SORT_BY_NAME(x) SORT(x)
<a id="l00099"></a>
<a id="l00100"></a>#endif /* ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_MWDT_H_ */
</code></pre>

## 12.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2020, Synopsys, Inc.；Apache-2.0许可证原文保留。

2. MWDT链接器不具备下面这些指令。

3. GROUP_START()和GROUP_END()用于定义位于同一内存区域（如RAM、ROM等）的一组段。where参数是内存区域名称。

4. GROUP_LINK_IN()位于段描述末尾，告诉链接器该段应放入where参数指定的内存区域。

5. 与GROUP_LINK_IN()类似，但增加第二个参数，指定装载地址所属的内存区域，例如ROM。用于XIP平台启动时必须复制的已初始化数据段。原注释进一步说明：GNU ld的输出放置指令会持续影响后续段，所以紧随此类已初始化数据段之后的第一个段也必须使用此形式，将vregion与lregion都指定为相同区域，例如RAM。

6. SECTION_PROLOGUE()定义段的开头。name是段名，option用于加入特殊选项，例如(NOLOAD)。页对齐拥有独立参数，以便抽象不同工具链之间的差异；不需要时将options与align参数留空。

7. 与SECTION_PROLOGUE()类似，但在XIP平台上，对虚拟地址与装载地址不同、启动时将复制到RAM的数据段必须使用此宏。原注释要求还必须使用GROUP_LINK_IN_LMA指定正确的输出装载地址；实际定义名称差异见本页译注。

8. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_MWDT_H_。

## 12.3\_原页符号提示（Symbol Descriptions）

## 12.4\_源码跟踪译注

> 译注——适配差异：MWDT将ASSERT展开为空、将SUBALIGN(x)映射为ALIGN(x)，GROUP_START／END也为空；不能把源码出现ASSERT当作该工具链实际执行了断言。GROUP_ROM_LINK_IN使用lregion而忽略vregion；原描述写作region，译注明确实际参数。原页面Metware拼写保留说明，工具链通常称MetaWare。

> 译注——原注释旧名称：SECTION_DATA_PROLOGUE的源码注释要求配合GROUP_LINK_IN_LMA，但本头文件实际定义的是GROUP_DATA_LINK_IN。XIP下数据段开头附带ALIGN(8)，并由GROUP_DATA_LINK_IN生成运行区域和装载区域关系。原注释关于GNU ld放置指令会延续影响后续段的描述照译，不把它当成每种链接器的统一语义保证。

> 译注——版本边界：本批记录八份链接器头文件、设备树绑定、三份链接器CMake文件、日志链接片段及两份内存管理头文件，共十五份官方源码摘要。八个源码浏览页的非注释代码与本次读取的原始头文件逐项核对；滚动main、latest与本仓库参照版本不自动等同。本次未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

头文件相对定位：[include/zephyr/linker/linker-tool-mwdt.h](../../../include/zephyr/linker/linker-tool-mwdt.h)，关联实现／接口：[include/zephyr/linker/linker-tool-mwdt.h](../../../include/zephyr/linker/linker-tool-mwdt.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/linker/linker-tool-mwdt.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/linker/linker-tool-mwdt.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

## 12.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P011_MWDT链接器适配头文件参考.md)

---

[上一章](P011_MWDT链接器适配头文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_链接器devnull区域头文件参考.md)
