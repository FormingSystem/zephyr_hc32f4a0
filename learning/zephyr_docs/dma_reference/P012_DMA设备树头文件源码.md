---
id: learning.zephyr-docs.dma-reference.page-12
title: DMA设备树头文件源码
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2dma_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_DMA设备树头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2dma_8h_source.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。原网页省略了用于生成接口文档的部分注释，因此原行号会跳跃；这里的“全部可见代码”不等于包含所有文档注释的原始文件。接口说明、参数与返回值见[对应头文件参考](P011_DMA设备树头文件参考.md)及[本册大纲](大纲.md)。

## 12.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00025"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00164"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="foldopen00175"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="foldopen00259"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00268"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>

```c


/*
 * Copyright (c) 2020, Linaro Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DEVICETREE_DMA_H_
#define ZEPHYR_INCLUDE_DEVICETREE_DMA_H_

#ifdef __cplusplus
extern "C" {
#endif


#define DT_DMAS_CTLR_BY_IDX(node_id, idx) DT_PHANDLE_BY_IDX(node_id, dmas, idx)

#define DT_DMAS_CTLR_BY_NAME(node_id, name) \
        DT_PHANDLE_BY_NAME(node_id, dmas, name)

#define DT_DMAS_CTLR(node_id) DT_DMAS_CTLR_BY_IDX(node_id, 0)

#define DT_INST_DMAS_CTLR_BY_IDX(inst, idx) \
        DT_DMAS_CTLR_BY_IDX(DT_DRV_INST(inst), idx)

#define DT_INST_DMAS_CTLR_BY_NAME(inst, name) \
        DT_DMAS_CTLR_BY_NAME(DT_DRV_INST(inst), name)

#define DT_INST_DMAS_CTLR(inst) DT_INST_DMAS_CTLR_BY_IDX(inst, 0)

#define DT_DMAS_CELL_BY_IDX(node_id, idx, cell) \
        DT_PHA_BY_IDX(node_id, dmas, idx, cell)

#define DT_INST_DMAS_CELL_BY_IDX(inst, idx, cell) \
        DT_PHA_BY_IDX(DT_DRV_INST(inst), dmas, idx, cell)

#define DT_DMAS_CELL_BY_NAME(node_id, name, cell) \
        DT_PHA_BY_NAME(node_id, dmas, name, cell)

#define DT_DMAS_CELL_BY_NAME_OR(node_id, name, cell, default_value) \
        DT_PHA_BY_NAME_OR(node_id, dmas, name, cell, default_value)

#define DT_INST_DMAS_CELL_BY_NAME(inst, name, cell) \
        DT_DMAS_CELL_BY_NAME(DT_DRV_INST(inst), name, cell)

#define DT_DMAS_HAS_IDX(node_id, idx) \
        IS_ENABLED(DT_CAT4(node_id, _P_dmas_IDX_, idx, _EXISTS))

#define DT_INST_DMAS_HAS_IDX(inst, idx) \
        DT_DMAS_HAS_IDX(DT_DRV_INST(inst), idx)

#define DT_DMAS_HAS_NAME(node_id, name) \
        DT_PROP_HAS_NAME(node_id, dmas, name)

#define DT_INST_DMAS_HAS_NAME(inst, name) \
        DT_DMAS_HAS_NAME(DT_DRV_INST(inst), name)


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DEVICETREE_DMA_H_ */
```

## 12.2\_可见注释译文（Comments）

1. 版权为2020年Linaro Ltd.，许可证为Apache-2.0；法律署名原样保留。

2. 结束ZEPHYR_INCLUDE_DEVICETREE_DMA_H_头文件包含保护（Header Include Guard）。

## 12.3\_源码跟踪译注

> 译注——编译期映射：DT_DMAS_CTLR_*得到控制器节点标识符；DT_DMAS_CELL_*得到绑定所命名单元的值；DT_INST_*先通过DT_DRV_INST(inst)取得设备实例节点。DT_DMAS_HAS_*只检查元素存在性，不能代替设备就绪检查或通道申请。完整示例和参数见[DMA设备树宏](P008_DMA设备树宏.md)。

仓库相对定位：[include/zephyr/devicetree/dma.h](../../../include/zephyr/devicetree/dma.h)；本次核对的[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/dma.h)摘要见[来源记录](../SOURCES.md)。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致；不能把这种一致性推广到以后滚动更新的main。

本批未构建、烧录、擦写或实板运行；代码阅读和文档核验不代表硬件操作通过。

## 12.4\_原页交叉引用（Cross References）

- [查看此文件参考说明](P011_DMA设备树头文件参考.md)

---

[上一章](P011_DMA设备树头文件参考.md) · [返回大纲](大纲.md)
