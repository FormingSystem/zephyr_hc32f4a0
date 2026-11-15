---
id: learning.zephyr-docs.dt-memory-attribute-reference.page-10
title: Arm内存属性头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/memory-attr-arm_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Arm内存属性头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/memory-attr-arm_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P009_Arm内存属性头文件参考.md)和[公共API](P018_Arm_MPU内存类型宏.md)。

## 10.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="amemory-attr_8h_html"></a>
<a id="autil__macro_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2023 Carlo Caione &lt;ccaione@baylibre.com&gt;
<a id="l00003"></a> * Copyright 2025 Arm Limited and/or its affiliates &lt;open-source-office@arm.com&gt;
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_ATTR_MEMORY_ATTR_ARM_H_
<a id="l00015"></a>#define ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_ATTR_MEMORY_ATTR_ARM_H_
<a id="l00016"></a>
<a id="l00017"></a>#include &lt;zephyr/sys/util_macro.h&gt;
<a id="l00018"></a>#include &lt;zephyr/dt-bindings/memory-attr/memory-attr.h&gt;
<a id="l00019"></a>
<a id="l00028"></a>
<a id="l00029"></a>/*
<a id="l00030"></a> * Architecture specific ARM MPU related attributes.
<a id="l00031"></a> *
<a id="l00032"></a> * This list is to seamlessly support the MPU regions configuration using DT and
<a id="l00033"></a> * the `zephyr,memory-attr` property.
<a id="l00034"></a> *
<a id="l00035"></a> * This is legacy and it should NOT be extended further. If new MPU region
<a id="l00036"></a> * types must be added, these must rely on the generic memory attributes.
<a id="l00037"></a> */
<a id="l00038"></a>
<a id="l00040"></a>#define DT_MEM_ARM_MASK   DT_MEM_ARCH_ATTR_MASK
<a id="l00041"></a>#define DT_MEM_ARM(x)     ((x) &lt;&lt; DT_MEM_ARCH_ATTR_SHIFT)
<a id="l00042"></a>
<a id="l00043"></a>#define ATTR_MPU_RAM         BIT(0)
<a id="l00044"></a>#define ATTR_MPU_RAM_NOCACHE BIT(1)
<a id="l00045"></a>#define ATTR_MPU_FLASH       BIT(2)
<a id="l00046"></a>#define ATTR_MPU_PPB         BIT(3)
<a id="l00047"></a>#define ATTR_MPU_IO          BIT(4)
<a id="l00048"></a>#define ATTR_MPU_EXTMEM      BIT(5)
<a id="l00049"></a>#define ATTR_MPU_RAM_PXN     BIT(6)
<a id="l00050"></a>#define ATTR_MPU_DEVICE      BIT(7)
<a id="l00051"></a>#define ATTR_MPU_RAM_WT      BIT(8)
<a id="l00053"></a>
<a id="l00061"></a>#define DT_MEM_ARM_GET(x) ((x) &amp; DT_MEM_ARM_MASK)
<a id="l00062"></a>
<a id="l00064"></a>#define DT_MEM_ARM_MPU_RAM         DT_MEM_ARM(ATTR_MPU_RAM)
<a id="l00066"></a>#define DT_MEM_ARM_MPU_RAM_NOCACHE DT_MEM_ARM(ATTR_MPU_RAM_NOCACHE)
<a id="l00068"></a>#define DT_MEM_ARM_MPU_FLASH       DT_MEM_ARM(ATTR_MPU_FLASH)
<a id="l00070"></a>#define DT_MEM_ARM_MPU_PPB         DT_MEM_ARM(ATTR_MPU_PPB)
<a id="l00072"></a>#define DT_MEM_ARM_MPU_IO          DT_MEM_ARM(ATTR_MPU_IO)
<a id="l00074"></a>#define DT_MEM_ARM_MPU_EXTMEM      DT_MEM_ARM(ATTR_MPU_EXTMEM)
<a id="l00076"></a>#define DT_MEM_ARM_MPU_RAM_PXN     DT_MEM_ARM(ATTR_MPU_RAM_PXN)
<a id="l00078"></a>#define DT_MEM_ARM_MPU_DEVICE      DT_MEM_ARM(ATTR_MPU_DEVICE)
<a id="l00080"></a>#define DT_MEM_ARM_MPU_RAM_WT      DT_MEM_ARM(ATTR_MPU_RAM_WT)
<a id="l00082"></a>#define DT_MEM_ARM_MPU_UNKNOWN     DT_MEM_ARCH_ATTR_UNKNOWN
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_ATTR_MEMORY_ATTR_ARM_H_ */
</code></pre>

## 10.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>；Apache-2.0许可证原文保留。另有Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>。

2. 架构专用的Arm MPU相关属性。这份列表用于通过设备树（DT）和zephyr,memory-attr属性支持MPU区域配置。它属于旧式定义（Legacy），不应继续扩展；如果需要新增MPU区域类型，必须依赖通用内存属性。

3. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_ATTR_MEMORY_ATTR_ARM_H_。

## 10.3\_原页符号提示（Symbol Descriptions）

### `memory-attr.h`

通用设备树内存属性定义（Generic Devicetree Memory Attribute Definitions）。

符号定位：[memory-attr.h](P005_通用内存属性头文件参考.md)。

### `util_macro.h`

宏工具（Macro Utilities）。

符号定位：[util_macro.h](../util_reference/P004_宏工具头文件参考.md)。

## 10.4\_源码跟踪译注

> 译注——三类字段：zephyr,memory-attr使用32位属性值，通用字段为位15:0，软件字段为位19:16，架构字段为位31:20。通用、软件及架构的UNKNOWN分别占位15、19、31；UNKNOWN是一个显式标志，不能把0或未设置某一位一概解释为UNKNOWN。各字段的掩码（Mask）和移位量（Shift）见通用头文件源码。

> 译注——提取后仍在原位：本册各GET宏均执行按位与，没有右移。例如DT_MEM_SW_GET(DT_MEM_SW_ALLOC_DMA)仍为BIT(18)，不是原始低位常量ATTR_SW_ALLOC_DMA的BIT(2)。DT_MEM_ARM、DT_MEM_ARM64、DT_MEM_RISCV和DT_MEM_XTENSA等内部编码宏将低位属性移入架构字段；不要把已经编码的DT_MEM_*常量再次移位。

> 译注——声明与消费：这些绑定头文件定义属性编码，实际处理取决于启用的子系统和架构代码。subsys/mem_mgmt/mem_attr.c从状态为okay且具有zephyr,memory-attr的节点生成区域表，记录名称、第0个reg的地址与大小及完整属性值。属性声明本身不会分配内存、启用缓存、建立内存管理单元（Memory Management Unit，MMU）映射或赋予硬件原本不具备的DMA能力。

> 译注——旧式MPU编码：Arm头文件中的RAM、RAM_NOCACHE、FLASH、PPB、IO、EXTMEM、RAM_PXN、DEVICE和RAM_WT编码移入架构字段。本页仅描述Zephyr设备树编码，不是直接可写入MPU寄存器的硬件位。官方注释明确禁止继续扩展这套旧式类型，新的MPU区域类型应使用通用内存属性；保留现有定义不等于建议新代码继续增加此类常量。

> 译注——版本边界：本批记录六份绑定头文件及内存属性／属性堆的两个公共头文件、两份实现文件，共十份官方源码摘要。六个源码浏览页的非注释代码与本次读取的对应原始头文件一致；滚动main、latest和本仓库参照源码不自动视为同版本。本次未编译示例、配置MPU／MMU、建立内存堆或执行硬件实验。

头文件相对定位：[include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h)，关联实现／接口：[subsys/mem_mgmt/mem_attr.c](../../../subsys/mem_mgmt/mem_attr.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/mem_attr.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未编译示例、配置MPU／MMU、建立内存堆或执行硬件实验。

## 10.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P009_Arm内存属性头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/dt-bindings/memory-attr/memory-attr.h](P005_通用内存属性头文件参考.md)

---

[上一章](P009_Arm内存属性头文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_Arm64内存属性头文件参考.md)
