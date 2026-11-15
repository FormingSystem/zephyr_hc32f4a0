---
id: learning.zephyr-docs.memory-retention-reference.page-3
title: NVMEM设备树头文件源码
kind: reference
status: maintained
domains: [zephyr, storage, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2nvmem_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_NVMEM设备树头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2nvmem_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P002_NVMEM设备树头文件参考.md)和[公共API](../storage/P018_NVMEM设备树辅助宏.md)。

## 3.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。


<pre><code class="language-c"><a id="l00001"></a>
<a id="l00006"></a>
<a id="l00007"></a>/*
<a id="l00008"></a> * Copyright (c) 2024, Andriy Gelman
<a id="l00009"></a> * Copyright (c) 2025, Basalte bv
<a id="l00010"></a> *
<a id="l00011"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00012"></a> */
<a id="l00013"></a>
<a id="l00014"></a>#ifndef ZEPHYR_INCLUDE_DEVICETREE_NVMEM_H_
<a id="l00015"></a>#define ZEPHYR_INCLUDE_DEVICETREE_NVMEM_H_
<a id="l00016"></a>
<a id="l00017"></a>#ifdef __cplusplus
<a id="l00018"></a>extern "C" {
<a id="l00019"></a>#endif
<a id="l00020"></a>
<a id="l00028"></a>
<a id="l00056"></a>#define DT_NVMEM_CELLS_HAS_IDX(node_id, idx) DT_PROP_HAS_IDX(node_id, nvmem_cells, idx)
<a id="l00057"></a>
<a id="l00085"></a>#define DT_NVMEM_CELLS_HAS_NAME(node_id, name) DT_PROP_HAS_NAME(node_id, nvmem_cells, name)
<a id="l00086"></a>
<a id="l00109"></a>#define DT_NUM_NVMEM_CELLS(node_id) DT_PROP_LEN(node_id, nvmem_cells)
<a id="l00110"></a>
<a id="l00148"></a>#define DT_NVMEM_CELL_BY_IDX(node_id, idx) DT_PHANDLE_BY_IDX(node_id, nvmem_cells, idx)
<a id="l00149"></a>
<a id="l00162"></a>#define DT_NVMEM_CELL(node_id) DT_NVMEM_CELL_BY_IDX(node_id, 0)
<a id="l00163"></a>
<a id="l00201"></a>#define DT_NVMEM_CELL_BY_NAME(node_id, name) DT_PHANDLE_BY_NAME(node_id, nvmem_cells, name)
<a id="l00202"></a>
<a id="l00214"></a>#define DT_INST_NVMEM_CELLS_HAS_IDX(inst, idx) DT_NVMEM_CELLS_HAS_IDX(DT_DRV_INST(inst), idx)
<a id="l00215"></a>
<a id="l00228"></a>#define DT_INST_NVMEM_CELLS_HAS_NAME(inst, name) DT_NVMEM_CELLS_HAS_NAME(DT_DRV_INST(inst), name)
<a id="l00229"></a>
<a id="l00239"></a>#define DT_INST_NUM_NVMEM_CELLS(inst) DT_NUM_NVMEM_CELLS(DT_DRV_INST(inst))
<a id="l00240"></a>
<a id="l00252"></a>#define DT_INST_NVMEM_CELL_BY_IDX(inst, idx) DT_NVMEM_CELL_BY_IDX(DT_DRV_INST(inst), idx)
<a id="l00253"></a>
<a id="l00265"></a>#define DT_INST_NVMEM_CELL(inst) DT_INST_NVMEM_CELL_BY_IDX(inst, 0)
<a id="l00266"></a>
<a id="l00280"></a>#define DT_INST_NVMEM_CELL_BY_NAME(inst, name) DT_NVMEM_CELL_BY_NAME(DT_DRV_INST(inst), name)
<a id="l00281"></a>
<a id="l00318"></a>#define DT_MTD_FROM_NVMEM_CELL(node_id) DT_GPARENT(node_id)
<a id="l00319"></a>
<a id="l00323"></a>
<a id="l00324"></a>#ifdef __cplusplus
<a id="l00325"></a>}
<a id="l00326"></a>#endif
<a id="l00327"></a>
<a id="l00328"></a>#endif /* ZEPHYR_INCLUDE_DEVICETREE_NVMEM_H_ */
</code></pre>

## 3.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2024, Andriy Gelman；Copyright (c) 2025, Basalte bv。Apache-2.0许可证原文保留。

2. 结束头文件包含保护ZEPHYR_INCLUDE_DEVICETREE_NVMEM_H_。

## 3.3\_原页符号提示（Symbol Descriptions）

## 3.4\_源码跟踪译注

> 译注——阅读关系：详细宏参数和原始设备树示例见[已有设备树辅助宏](../storage/P018_NVMEM设备树辅助宏.md)。本页补齐头文件参考，源码页保留完整展开式；这些宏在编译阶段处理节点标识和属性，不在运行时读取存储数据。

> 译注——节点与控制器：原文两个DT_INST_NVMEM_CELL_BY_*摘要使用controller phandle措辞，但实际展开调用DT_NVMEM_CELL_BY_*，取得的是数据单元节点。要取得底层存储控制器，DT_MTD_FROM_NVMEM_CELL使用DT_GPARENT取得祖父节点；它依赖既定设备树层级，不是递归搜索任意祖先。

> 译注——索引和名称：idx是nvmem-cells属性中的逻辑索引，不是存储字节偏移；name是由nvmem-cell-names形成的标识符形式，不是运行时字符串。DT_INST_*把inst交给DT_DRV_INST，依赖当前驱动的DT_DRV_COMPAT定义。第零项辅助宏不检查数组非空，NUM宏也不自动在属性缺失时返回0；使用方应先核对属性与所需索引／名称存在。

头文件相对定位：[include/zephyr/devicetree/nvmem.h](../../../include/zephyr/devicetree/nvmem.h)，关联实现／接口：[include/zephyr/nvmem.h](../../../include/zephyr/nvmem.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/nvmem.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/nvmem.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未编译或执行存储写入、掉电、低功耗、非法参数及实板实验。

## 3.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P002_NVMEM设备树头文件参考.md)

---

[上一章](P002_NVMEM设备树头文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_保留内存头文件源码.md)
