---
id: learning.zephyr-docs.dt-peripheral-reference.page-2
title: GPIO设备树头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2gpio_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_GPIO设备树头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2gpio_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_GPIO设备树头文件参考.md)和[公共API](../hardware/P290_设备树GPIO宏.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00058"></a>
<a id="foldopen00069"></a>
<a id="foldopen00113"></a>
<a id="foldopen00124"></a>
<a id="foldopen00169"></a>
<a id="foldopen00180"></a>
<a id="foldopen00221"></a>
<a id="foldopen00266"></a>
<a id="foldopen00311"></a>
<a id="foldopen00325"></a>
<a id="foldopen00336"></a>
<a id="foldopen00349"></a>
<a id="foldopen00360"></a>

<pre><code class="language-c"><a id="l00001"></a>
<a id="l00005"></a>
<a id="l00006"></a>/*
<a id="l00007"></a> * Copyright (c) 2020, Linaro Ltd.
<a id="l00008"></a> * Copyright (c) 2020 Nordic Semiconductor
<a id="l00009"></a> *
<a id="l00010"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00011"></a> */
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_DEVICETREE_GPIO_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_DEVICETREE_GPIO_H_
<a id="l00015"></a>
<a id="l00016"></a>#ifdef __cplusplus
<a id="l00017"></a>extern "C" {
<a id="l00018"></a>#endif
<a id="l00019"></a>
<a id="l00031"></a>
<a id="l00058"></a>#define DT_GPIO_CTLR_BY_IDX(node_id, gpio_pha, idx) \
<a id="l00059"></a>        DT_PHANDLE_BY_IDX(node_id, gpio_pha, idx)
<a id="l00060"></a>
<a id="l00069"></a>#define DT_GPIO_CTLR(node_id, gpio_pha) \
<a id="l00070"></a>        DT_GPIO_CTLR_BY_IDX(node_id, gpio_pha, 0)
<a id="l00071"></a>
<a id="l00113"></a>#define DT_GPIO_PIN_BY_IDX(node_id, gpio_pha, idx) \
<a id="l00114"></a>        DT_PHA_BY_IDX(node_id, gpio_pha, idx, pin)
<a id="l00115"></a>
<a id="l00124"></a>#define DT_GPIO_PIN(node_id, gpio_pha) \
<a id="l00125"></a>        DT_GPIO_PIN_BY_IDX(node_id, gpio_pha, 0)
<a id="l00126"></a>
<a id="l00169"></a>#define DT_GPIO_FLAGS_BY_IDX(node_id, gpio_pha, idx) \
<a id="l00170"></a>        DT_PHA_BY_IDX_OR(node_id, gpio_pha, idx, flags, 0)
<a id="l00171"></a>
<a id="l00180"></a>#define DT_GPIO_FLAGS(node_id, gpio_pha) \
<a id="l00181"></a>        DT_GPIO_FLAGS_BY_IDX(node_id, gpio_pha, 0)
<a id="l00182"></a>
<a id="l00221"></a>#define DT_NUM_GPIO_HOGS(node_id) \
<a id="l00222"></a>        COND_CODE_1(IS_ENABLED(DT_CAT(node_id, _GPIO_HOGS_EXISTS)), \
<a id="l00223"></a>                    (DT_CAT(node_id, _GPIO_HOGS_NUM)), (0))
<a id="l00224"></a>
<a id="l00266"></a>#define DT_GPIO_HOG_PIN_BY_IDX(node_id, idx) \
<a id="l00267"></a>        DT_CAT4(node_id, _GPIO_HOGS_IDX_, idx, _VAL_pin)
<a id="l00268"></a>
<a id="l00311"></a>#define DT_GPIO_HOG_FLAGS_BY_IDX(node_id, idx) \
<a id="l00312"></a>        COND_CODE_1(IS_ENABLED(DT_CAT4(node_id, _GPIO_HOGS_IDX_, idx, _VAL_flags_EXISTS)), \
<a id="l00313"></a>                    (DT_CAT4(node_id, _GPIO_HOGS_IDX_, idx, _VAL_flags)), (0))
<a id="l00314"></a>
<a id="l00325"></a>#define DT_INST_GPIO_PIN_BY_IDX(inst, gpio_pha, idx) \
<a id="l00326"></a>        DT_GPIO_PIN_BY_IDX(DT_DRV_INST(inst), gpio_pha, idx)
<a id="l00327"></a>
<a id="l00336"></a>#define DT_INST_GPIO_PIN(inst, gpio_pha) \
<a id="l00337"></a>        DT_INST_GPIO_PIN_BY_IDX(inst, gpio_pha, 0)
<a id="l00338"></a>
<a id="l00349"></a>#define DT_INST_GPIO_FLAGS_BY_IDX(inst, gpio_pha, idx) \
<a id="l00350"></a>        DT_GPIO_FLAGS_BY_IDX(DT_DRV_INST(inst), gpio_pha, idx)
<a id="l00351"></a>
<a id="l00360"></a>#define DT_INST_GPIO_FLAGS(inst, gpio_pha) \
<a id="l00361"></a>        DT_INST_GPIO_FLAGS_BY_IDX(inst, gpio_pha, 0)
<a id="l00362"></a>
<a id="l00366"></a>
<a id="l00367"></a>#ifdef __cplusplus
<a id="l00368"></a>}
<a id="l00369"></a>#endif
<a id="l00370"></a>
<a id="l00371"></a>#endif  /* ZEPHYR_INCLUDE_DEVICETREE_GPIO_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2020, Linaro Ltd.；Copyright (c) 2020 Nordic Semiconductor。Apache-2.0许可证原文保留。

2. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_DEVICETREE_GPIO_H_。

## 2.3\_原页符号提示（Symbol Descriptions）

原网页没有独立的符号提示条目。

## 2.4\_源码跟踪译注

> 译注——三种返回对象：CTLR系列返回GPIO控制器节点标识，PIN读取绑定中名为pin的单元，FLAGS读取名为flags的单元，缺少该单元时回退为0。节点标识不是struct device指针，引脚编号也不是电平读数；flags为0不证明条目有效、控制器就绪或引脚已配置。

> 译注——预占项属于hog节点：DT_NUM_GPIO_HOGS读取传入节点的_GPIO_HOGS元数据，统计该gpio-hog节点中预占GPIO描述符的数量，不是其父GPIO控制器拥有的所有hog子节点数量。没有元数据时数量为0，PIN_BY_IDX没有同样的零值回退；访问前仍需使用有效索引。gen_defines.py逐项遍历node.gpio_hogs生成这些值。

> 译注——实例与默认索引：INST接口通过DT_DRV_INST(inst)取得消费节点，再读取该节点的GPIO属性；它不把inst当成GPIO控制器编号。省略BY_IDX的版本固定选择索引0。这些宏读取编译期描述，不调用gpio_pin_configure，也不完成GPIO hog初始化。

> 译注——版本边界：本批记录四份设备树头文件、gen_defines.py和zephyr,displays绑定，共六份官方源码摘要；四个源码浏览页的非注释代码与本次读取的原始头文件一致。latest、滚动main和本仓库参照版本不自动等同。本次未构建设备树、配置引脚、执行SPI／CAN传输、初始化显示设备或操作硬件。

头文件相对定位：[include/zephyr/devicetree/gpio.h](../../../include/zephyr/devicetree/gpio.h)，关联实现／接口：[scripts/dts/gen_defines.py](../../../scripts/dts/gen_defines.py)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/gpio.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/gen_defines.py)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建设备树、配置引脚、执行SPI／CAN传输、初始化显示设备或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_GPIO设备树头文件参考.md)

---

[上一章](P001_GPIO设备树头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_SPI设备树头文件参考.md)
