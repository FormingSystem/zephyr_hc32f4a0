---
id: learning.zephyr-docs.dt-peripheral-reference.page-6
title: CAN设备树头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2can_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_CAN设备树头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2can_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P005_CAN设备树头文件参考.md)和[公共API](../hardware/P373_CAN设备树宏.md)。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00075"></a>
<a id="foldopen00118"></a>
<a id="foldopen00130"></a>
<a id="foldopen00140"></a>

<pre><code class="language-c"><a id="l00001"></a>
<a id="l00005"></a>
<a id="l00006"></a>/*
<a id="l00007"></a> * Copyright (c) 2022 Vestas Wind Systems A/S
<a id="l00008"></a> *
<a id="l00009"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00010"></a> */
<a id="l00011"></a>
<a id="l00012"></a>#ifndef ZEPHYR_INCLUDE_DEVICETREE_CAN_H_
<a id="l00013"></a>#define ZEPHYR_INCLUDE_DEVICETREE_CAN_H_
<a id="l00014"></a>
<a id="l00015"></a>#ifdef __cplusplus
<a id="l00016"></a>extern "C" {
<a id="l00017"></a>#endif
<a id="l00018"></a>
<a id="l00025"></a>
<a id="l00075"></a>#define DT_CAN_TRANSCEIVER_MIN_BITRATE(node_id, min)                                    \
<a id="l00076"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, phys),                                    \
<a id="l00077"></a>                    MAX(DT_PROP_OR(DT_PHANDLE(node_id, phys), min_bitrate, 0), min),    \
<a id="l00078"></a>                    MAX(DT_PROP_OR(DT_CHILD(node_id, can_transceiver), min_bitrate, min), min))
<a id="l00079"></a>
<a id="l00118"></a>#define DT_CAN_TRANSCEIVER_MAX_BITRATE(node_id, max)                                    \
<a id="l00119"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, phys),                                    \
<a id="l00120"></a>                    MIN(DT_PROP(DT_PHANDLE(node_id, phys), max_bitrate), max),          \
<a id="l00121"></a>                    MIN(DT_PROP_OR(DT_CHILD(node_id, can_transceiver), max_bitrate, max), max))
<a id="l00122"></a>
<a id="l00130"></a>#define DT_INST_CAN_TRANSCEIVER_MIN_BITRATE(inst, min) \
<a id="l00131"></a>        DT_CAN_TRANSCEIVER_MIN_BITRATE(DT_DRV_INST(inst), min)
<a id="l00132"></a>
<a id="l00140"></a>#define DT_INST_CAN_TRANSCEIVER_MAX_BITRATE(inst, max) \
<a id="l00141"></a>        DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_DRV_INST(inst), max)
<a id="l00142"></a>
<a id="l00146"></a>
<a id="l00147"></a>#ifdef __cplusplus
<a id="l00148"></a>}
<a id="l00149"></a>#endif
<a id="l00150"></a>
<a id="l00151"></a>#endif /* ZEPHYR_INCLUDE_DEVICETREE_CAN_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2022 Vestas Wind Systems A/S；Apache-2.0许可证原文保留。

2. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_DEVICETREE_CAN_H_。

## 6.3\_原页符号提示（Symbol Descriptions）

原网页没有独立的符号提示条目。

## 6.4\_源码跟踪译注

> 译注——下限取大、上限取小：MIN_BITRATE返回收发器下限与调用方min的较大值，MAX_BITRATE返回收发器上限与调用方max的较小值，相当于组合双方支持范围的边界；宏不会设置CAN比特率，也不会自动检查合并后的下限是否超过上限。

> 译注——两条描述路径：控制器有phys属性时读取它引用的首个收发器节点；此分支min-bitrate缺失默认0，但max-bitrate使用DT_PROP，没有缺失回退。没有phys属性时读取名为can-transceiver的子节点，并分别使用调用方min／max作为默认值。不能只根据两个宏的名称对称就推断它们对缺失属性的行为相同。

> 译注——版本边界：本批记录四份设备树头文件、gen_defines.py和zephyr,displays绑定，共六份官方源码摘要；四个源码浏览页的非注释代码与本次读取的原始头文件一致。latest、滚动main和本仓库参照版本不自动等同。本次未构建设备树、配置引脚、执行SPI／CAN传输、初始化显示设备或操作硬件。

头文件相对定位：[include/zephyr/devicetree/can.h](../../../include/zephyr/devicetree/can.h)，关联实现／接口：[include/zephyr/devicetree/can.h](../../../include/zephyr/devicetree/can.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/can.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/can.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建设备树、配置引脚、执行SPI／CAN传输、初始化显示设备或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_CAN设备树头文件参考.md)

---

[上一章](P005_CAN设备树头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_显示设备树头文件参考.md)
