---
id: learning.zephyr-docs.dt-overview-reference.page-7
title: 选定SRAM头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sram_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_选定SRAM头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sram_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P006_选定SRAM头文件参考.md)和[公共API](P005_选定SRAM区域宏.md)。

## 7.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="asys_2util_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>
<a id="l00005"></a>
<a id="l00006"></a>/*
<a id="l00007"></a> * Copyright (c) 2026 Nordic Semiconductor ASA
<a id="l00008"></a> *
<a id="l00009"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00010"></a> */
<a id="l00011"></a>
<a id="l00012"></a>#ifndef ZEPHYR_INCLUDE_DEVICETREE_SRAM_H_
<a id="l00013"></a>#define ZEPHYR_INCLUDE_DEVICETREE_SRAM_H_
<a id="l00014"></a>
<a id="l00015"></a>#ifdef CONFIG_SRAM_DEPRECATED_KCONFIG_SET
<a id="l00016"></a>#include &lt;zephyr/sys/util.h&gt;
<a id="l00017"></a>#endif
<a id="l00018"></a>
<a id="l00019"></a>#ifdef __cplusplus
<a id="l00020"></a>extern "C" {
<a id="l00021"></a>#endif
<a id="l00022"></a>
<a id="l00028"></a>
<a id="l00034"></a>#ifdef CONFIG_SRAM_DEPRECATED_KCONFIG_SET
<a id="l00035"></a>#define DT_CHOSEN_SRAM_ADDR CONFIG_SRAM_BASE_ADDRESS
<a id="l00036"></a>#else
<a id="l00037"></a>#define DT_CHOSEN_SRAM_ADDR DT_REG_ADDR(DT_CHOSEN(zephyr_sram))
<a id="l00038"></a>#endif
<a id="l00039"></a>
<a id="l00045"></a>#ifdef CONFIG_SRAM_DEPRECATED_KCONFIG_SET
<a id="l00046"></a>#define DT_CHOSEN_SRAM_SIZE (CONFIG_SRAM_SIZE * 1024)
<a id="l00047"></a>#else
<a id="l00048"></a>#define DT_CHOSEN_SRAM_SIZE DT_REG_SIZE(DT_CHOSEN(zephyr_sram))
<a id="l00049"></a>#endif
<a id="l00050"></a>
<a id="l00054"></a>
<a id="l00055"></a>#ifdef __cplusplus
<a id="l00056"></a>}
<a id="l00057"></a>#endif
<a id="l00058"></a>
<a id="l00059"></a>#endif  /* ZEPHYR_INCLUDE_DEVICETREE_SRAM_H_ */
</code></pre>

## 7.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2026 Nordic Semiconductor ASA；Apache-2.0许可证原文保留。

2. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_DEVICETREE_SRAM_H_。

## 7.3\_原页符号提示（Symbol Descriptions）

### `util.h`

杂项工具（Miscellaneous Utilities）。

符号定位：[util.h](../util_reference/P002_通用工具头文件参考.md)。

## 7.4\_源码跟踪译注

> 译注——地址对象：DT_CHOSEN_SRAM_ADDR中的“绝对地址”（Absolute Address）指目标芯片存储地址，不是电脑文件系统路径。设备树分支通过DT_CHOSEN(zephyr_sram)解析/chosen的zephyr,sram，再由DT_REG_ADDR／DT_REG_SIZE读取第0个reg区域；不会汇总其他SRAM节点或同一节点的所有reg条目，也不直接返回可解引用的C指针。

> 译注——两条配置分支：参考页展示设备树分支，源码页还保留CONFIG_SRAM_DEPRECATED_KCONFIG_SET分支，分别采用CONFIG_SRAM_BASE_ADDRESS和CONFIG_SRAM_SIZE * 1024。后者把旧配置中的1024字节单位换算成字节（Bytes）。arch/Kconfig在旧地址或大小与所选设备树值不同时启用此兼容分支并选择DEPRECATED；新配置应以zephyr,sram节点描述为准。

> 译注——存在性与使用边界：原文“if it exists”不是缺少节点时返回0的保证。设备树分支直接展开DT_CHOSEN和reg访问器，没有运行时失败返回值或自动回退；调用位置应确保所选节点及对应reg信息存在。宏只提供声明的地址和长度，不分配内存、不初始化RAM，也不证明链接后的代码或数据已经放入该区域。

> 译注——版本边界：本批记录七份官方源码／绑定的读取摘要；两个源码浏览页的非注释代码与本次读取的对应原始头文件一致。latest和main会滚动变化，本仓库参照源码与它们不自动视为相同版本；本次未编译示例、构建固件或执行硬件实验。

头文件相对定位：[include/zephyr/devicetree/sram.h](../../../include/zephyr/devicetree/sram.h)，关联实现／接口：[arch/Kconfig](../../../arch/Kconfig)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/sram.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/Kconfig)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未编译示例、构建固件、测量电池或执行硬件实验。

## 7.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P006_选定SRAM头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P006_选定SRAM头文件参考.md) · [返回大纲](大纲.md)
