---
id: learning.zephyr-docs.linker-reference.page-10
title: LLD链接器适配头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-lld_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_LLD链接器适配头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-lld_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P009_LLD链接器适配头文件参考.md)和[公共API](P009_LLD链接器适配头文件参考.md)。

## 10.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00039"></a>
<a id="foldopen00058"></a>
<a id="alinker-tool-gcc_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2023, Google, Inc.
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>#ifndef ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_LLD_H_
<a id="l00016"></a>#define ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_LLD_H_
<a id="l00017"></a>
<a id="l00018"></a>#include &lt;zephyr/linker/linker-tool-gcc.h&gt;
<a id="l00019"></a>
<a id="l00038"></a>#undef SECTION_PROLOGUE
<a id="l00039"></a>#define SECTION_PROLOGUE(name, options, align) \
<a id="l00040"></a>        name options : align
<a id="l00041"></a>
<a id="l00057"></a>#undef SECTION_DATA_PROLOGUE
<a id="l00058"></a>#define SECTION_DATA_PROLOGUE(name, options, align) \
<a id="l00059"></a>        SECTION_PROLOGUE(name, options, align)
<a id="l00060"></a>
<a id="l00061"></a>#endif /* ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_LLD_H_ */
</code></pre>

## 10.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2023, Google, Inc.；Apache-2.0许可证原文保留。

2. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_LINKER_LINKER_TOOL_LLD_H_。

## 10.3\_原页符号提示（Symbol Descriptions）

### `linker-tool-gcc.h`

GCC 工具链的链接器定义（GCC Toolchain Linker Definitions）。

符号定位：[linker-tool-gcc.h](P007_GNU链接器适配头文件参考.md)。

## 10.4\_源码跟踪译注

> 译注——继承与覆写：LLD头文件先包含GCC宏集，再#undef并重定义SECTION_PROLOGUE与SECTION_DATA_PROLOGUE；数据段开头最终同样展开为name options : align。其他区域放置宏来自GCC适配，因此阅读LLD页时也需参考GCC条件分支。

> 译注——旧路径说明：原注释中的cmake/linker/lld/target_baremetal.cmake在本次官方读取时返回404。当前cmake/linker/lld/linker_flags.cmake包含cmake/linker/ld/linker_flags.cmake，后者在baremetal属性中配置-N。原文保留，当前文件相对链接与摘要列在来源记录；这不是要求读者创建那个旧文件。

> 译注——两类地址：虚拟内存地址（Virtual Memory Address，VMA）表示段的运行地址，装载内存地址（Load Memory Address，LMA）表示装载镜像位置。GROUP_DATA_LINK_IN在XIP或K_MEM_IS_VM_KERNEL分支生成> vregion AT > lregion，普通分支只指定vregion。宏描述布局，不执行启动复制；需要由启动代码消费相应符号。

> 译注——版本边界：本批记录八份链接器头文件、设备树绑定、三份链接器CMake文件、日志链接片段及两份内存管理头文件，共十五份官方源码摘要。八个源码浏览页的非注释代码与本次读取的原始头文件逐项核对；滚动main、latest与本仓库参照版本不自动等同。本次未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

头文件相对定位：[include/zephyr/linker/linker-tool-lld.h](../../../include/zephyr/linker/linker-tool-lld.h)，关联实现／接口：[include/zephyr/linker/linker-tool-lld.h](../../../include/zephyr/linker/linker-tool-lld.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/linker/linker-tool-lld.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/linker/linker-tool-lld.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

## 10.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P009_LLD链接器适配头文件参考.md)
- [zephyr/linker/linker-tool-gcc.h](P007_GNU链接器适配头文件参考.md)

---

[上一章](P009_LLD链接器适配头文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_MWDT链接器适配头文件参考.md)
