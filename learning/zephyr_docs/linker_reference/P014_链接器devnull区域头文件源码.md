---
id: learning.zephyr-docs.linker-reference.page-14
title: 链接器devnull区域头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linker-devnull_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_链接器devnull区域头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/linker-devnull_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P013_链接器devnull区域头文件参考.md)和[公共API](P013_链接器devnull区域头文件参考.md)。

## 14.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。


<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2023 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00007"></a>/*
<a id="l00008"></a> * DESCRIPTION
<a id="l00009"></a> * Platform independent set of macros for creating a memory segment for
<a id="l00010"></a> * aggregating data that shall be kept in the elf file but not in the binary.
<a id="l00011"></a> */
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_LINKER_LINKER_DEVNULL_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_LINKER_LINKER_DEVNULL_H_
<a id="l00015"></a>
<a id="l00016"></a>#if defined(CONFIG_LINKER_DEVNULL_MEMORY)
<a id="l00017"></a>
<a id="l00018"></a>#if defined(CONFIG_XIP)
<a id="l00019"></a>#if (!defined(ROM_ADDR) &amp;&amp; !defined(ROM_BASE)) || !defined(ROM_SIZE)
<a id="l00020"></a>#error "ROM_SIZE, ROM_ADDR or ROM_BASE not defined"
<a id="l00021"></a>#endif
<a id="l00022"></a>#endif /* CONFIG_XIP */
<a id="l00023"></a>
<a id="l00024"></a>#if (!defined(RAM_ADDR) &amp;&amp; !defined(RAM_BASE)) || !defined(RAM_SIZE)
<a id="l00025"></a>#error "RAM_SIZE, RAM_ADDR or RAM_BASE not defined"
<a id="l00026"></a>#endif
<a id="l00027"></a>
<a id="l00028"></a>#if defined(CONFIG_XIP) &amp;&amp; !defined(ROM_ADDR)
<a id="l00029"></a>#define ROM_ADDR ROM_BASE
<a id="l00030"></a>#endif
<a id="l00031"></a>
<a id="l00032"></a>#if !defined(RAM_ADDR)
<a id="l00033"></a>#define RAM_ADDR RAM_BASE
<a id="l00034"></a>#endif
<a id="l00035"></a>
<a id="l00036"></a>#define ROM_END_ADDR (ROM_ADDR + ROM_SIZE)
<a id="l00037"></a>#define DEVNULL_SIZE CONFIG_LINKER_DEVNULL_MEMORY_SIZE
<a id="l00038"></a>#define ROM_DEVNULL_END_ADDR (ROM_END_ADDR + DEVNULL_SIZE)
<a id="l00039"></a>#define MAX_ADDR UINT32_MAX
<a id="l00040"></a>
<a id="l00041"></a>/* Determine where to put the devnull region. It should be adjacent to the ROM
<a id="l00042"></a> * region. If ROM starts after RAM or the distance between ROM and RAM is big
<a id="l00043"></a> * enough to fit the devnull region then devnull region is placed just after
<a id="l00044"></a> * the ROM region. If it cannot be done then the devnull region is placed before
<a id="l00045"></a> * the ROM region. It is possible that the devnull region cannot be placed
<a id="l00046"></a> * adjacent to the ROM (e.g. ROM starts at 0 and RAM follows ROM). In that
<a id="l00047"></a> * case compilation fails and the devnull region is not supported in that
<a id="l00048"></a> * configuration.
<a id="l00049"></a> */
<a id="l00050"></a>#if !defined(CONFIG_XIP)
<a id="l00051"></a>
<a id="l00052"></a>#if RAM_ADDR &gt;= DEVNULL_SIZE
<a id="l00053"></a>#define DEVNULL_ADDR (RAM_ADDR - DEVNULL_SIZE)
<a id="l00054"></a>#else
<a id="l00055"></a>#define DEVNULL_ADDR (RAM_ADDR + RAM_SIZE)
<a id="l00056"></a>#endif
<a id="l00057"></a>
<a id="l00058"></a>#else /* CONFIG_XIP */
<a id="l00059"></a>
<a id="l00060"></a>#if ((ROM_ADDR &gt; RAM_ADDR) &amp;&amp; ((MAX_ADDR - ROM_END_ADDR) &gt;= DEVNULL_SIZE)) || \
<a id="l00061"></a>        ((ROM_END_ADDR + DEVNULL_SIZE) &lt;= RAM_ADDR)
<a id="l00062"></a>#define DEVNULL_ADDR ROM_END_ADDR
<a id="l00063"></a>#elif ROM_ADDR &gt; DEVNULL_SIZE
<a id="l00064"></a>#define DEVNULL_ADDR (ROM_ADDR - DEVNULL_SIZE)
<a id="l00065"></a>#else
<a id="l00066"></a>#error "Cannot place devnull segment adjacent to ROM region."
<a id="l00067"></a>#endif
<a id="l00068"></a>
<a id="l00069"></a>#endif /* CONFIG_XIP */
<a id="l00070"></a>
<a id="l00071"></a>#define DEVNULL_REGION DEVNULL_ROM
<a id="l00072"></a>
<a id="l00073"></a>#endif /* CONFIG_LINKER_DEVNULL_MEMORY */
<a id="l00074"></a>
<a id="l00075"></a>#endif /* ZEPHYR_INCLUDE_LINKER_LINKER_DEVNULL_H_ */
</code></pre>

## 14.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2023 Nordic Semiconductor ASA；Apache-2.0许可证原文保留。

2. 说明：一组与平台无关的宏，用于建立一个内存段，汇集应保留在ELF文件中、但不应进入二进制镜像的数据。

3. 结束CONFIG_XIP条件块。

4. 确定devnull区域位置，使其邻接ROM区域。若ROM在RAM之后开始，或ROM与RAM之间的距离足以容纳devnull，则放在ROM后面；否则放在ROM之前。可能无法将其放在ROM旁边，例如ROM从0开始且RAM紧随ROM，此时构建报错，该配置不支持devnull区域。

5. 切换到CONFIG_XIP分支。

6. 结束CONFIG_XIP条件块。

7. 结束CONFIG_LINKER_DEVNULL_MEMORY条件块。

8. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_LINKER_LINKER_DEVNULL_H_。

## 14.3\_原页符号提示（Symbol Descriptions）

## 14.4\_源码跟踪译注

> 译注——保留ELF、排除二进制：devnull是链接时用于特定段的虚拟区域名称，不是操作系统的/dev/null，也不是将内容从ELF彻底删除。common-rom-logging.ld在CONFIG_LOG_FMT_SECTION_STRIP且DEVNULL_REGION存在时，把相应日志段标为COPY并放入DEVNULL_REGION；这与/DISCARD/不同，仍需下游镜像生成规则配合。

> 译注——条件与位置：此头文件只在CONFIG_LINKER_DEVNULL_MEMORY启用时提供区域常量。XIP分支尝试将区域放到ROM之后，否则放到ROM之前，不能满足条件时#error；非XIP分支按RAM_ADDR与DEVNULL_SIZE关系选择RAM之前或之后。原长注释主要描述ROM情形，不能忽略非XIP分支。未定义ROM／RAM地址、基址或大小时按相应条件报错；区域常量不会保留真实硬件容量。

> 译注——版本边界：本批记录八份链接器头文件、设备树绑定、三份链接器CMake文件、日志链接片段及两份内存管理头文件，共十五份官方源码摘要。八个源码浏览页的非注释代码与本次读取的原始头文件逐项核对；滚动main、latest与本仓库参照版本不自动等同。本次未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

头文件相对定位：[include/zephyr/linker/linker-devnull.h](../../../include/zephyr/linker/linker-devnull.h)，关联实现／接口：[include/zephyr/linker/linker-devnull.h](../../../include/zephyr/linker/linker-devnull.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/linker/linker-devnull.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/linker/linker-devnull.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

## 14.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P013_链接器devnull区域头文件参考.md)

---

[上一章](P013_链接器devnull区域头文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_链接器符号定义头文件参考.md)
