---
id: learning.zephyr-docs.dt-pwm-binding-reference.page-2
title: PWM设备树头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwms_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_PWM设备树头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pwms_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_PWM设备树头文件参考.md)和[公共API](../hardware/P264_设备树PWM宏.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00052"></a>
<a id="foldopen00082"></a>
<a id="foldopen00136"></a>
<a id="foldopen00183"></a>
<a id="foldopen00208"></a>
<a id="foldopen00225"></a>
<a id="foldopen00249"></a>
<a id="foldopen00266"></a>
<a id="foldopen00291"></a>
<a id="foldopen00311"></a>
<a id="foldopen00332"></a>
<a id="foldopen00344"></a>
<a id="foldopen00364"></a>
<a id="foldopen00376"></a>
<a id="foldopen00385"></a>
<a id="foldopen00395"></a>
<a id="foldopen00406"></a>
<a id="foldopen00424"></a>
<a id="foldopen00435"></a>
<a id="foldopen00453"></a>
<a id="foldopen00465"></a>

<pre><code class="language-c"><a id="l00001"></a>
<a id="l00005"></a>
<a id="l00006"></a>/*
<a id="l00007"></a> * Copyright (c) 2020, Linaro Ltd.
<a id="l00008"></a> *
<a id="l00009"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00010"></a> */
<a id="l00011"></a>
<a id="l00012"></a>#ifndef ZEPHYR_INCLUDE_DEVICETREE_PWMS_H_
<a id="l00013"></a>#define ZEPHYR_INCLUDE_DEVICETREE_PWMS_H_
<a id="l00014"></a>
<a id="l00015"></a>#ifdef __cplusplus
<a id="l00016"></a>extern "C" {
<a id="l00017"></a>#endif
<a id="l00018"></a>
<a id="l00025"></a>
<a id="l00052"></a>#define DT_PWMS_CTLR_BY_IDX(node_id, idx) \
<a id="l00053"></a>        DT_PHANDLE_BY_IDX(node_id, pwms, idx)
<a id="l00054"></a>
<a id="l00082"></a>#define DT_PWMS_CTLR_BY_NAME(node_id, name) \
<a id="l00083"></a>        DT_PHANDLE_BY_NAME(node_id, pwms, name)
<a id="l00084"></a>
<a id="l00092"></a>#define DT_PWMS_CTLR(node_id) DT_PWMS_CTLR_BY_IDX(node_id, 0)
<a id="l00093"></a>
<a id="l00136"></a>#define DT_PWMS_CELL_BY_IDX(node_id, idx, cell) \
<a id="l00137"></a>        DT_PHA_BY_IDX(node_id, pwms, idx, cell)
<a id="l00138"></a>
<a id="l00183"></a>#define DT_PWMS_CELL_BY_NAME(node_id, name, cell) \
<a id="l00184"></a>        DT_PHA_BY_NAME(node_id, pwms, name, cell)
<a id="l00185"></a>
<a id="l00193"></a>#define DT_PWMS_CELL(node_id, cell) DT_PWMS_CELL_BY_IDX(node_id, 0, cell)
<a id="l00194"></a>
<a id="l00208"></a>#define DT_PWMS_CHANNEL_BY_IDX(node_id, idx) \
<a id="l00209"></a>        DT_PWMS_CELL_BY_IDX(node_id, idx, channel)
<a id="l00210"></a>
<a id="l00225"></a>#define DT_PWMS_CHANNEL_BY_NAME(node_id, name) \
<a id="l00226"></a>        DT_PWMS_CELL_BY_NAME(node_id, name, channel)
<a id="l00227"></a>
<a id="l00234"></a>#define DT_PWMS_CHANNEL(node_id) DT_PWMS_CHANNEL_BY_IDX(node_id, 0)
<a id="l00235"></a>
<a id="l00249"></a>#define DT_PWMS_PERIOD_BY_IDX(node_id, idx) \
<a id="l00250"></a>        DT_PWMS_CELL_BY_IDX(node_id, idx, period)
<a id="l00251"></a>
<a id="l00266"></a>#define DT_PWMS_PERIOD_BY_NAME(node_id, name) \
<a id="l00267"></a>        DT_PWMS_CELL_BY_NAME(node_id, name, period)
<a id="l00268"></a>
<a id="l00275"></a>#define DT_PWMS_PERIOD(node_id) DT_PWMS_PERIOD_BY_IDX(node_id, 0)
<a id="l00276"></a>
<a id="l00291"></a>#define DT_PWMS_FLAGS_BY_IDX(node_id, idx) \
<a id="l00292"></a>        DT_PHA_BY_IDX_OR(node_id, pwms, idx, flags, 0)
<a id="l00293"></a>
<a id="l00311"></a>#define DT_PWMS_FLAGS_BY_NAME(node_id, name) \
<a id="l00312"></a>        DT_PHA_BY_NAME_OR(node_id, pwms, name, flags, 0)
<a id="l00313"></a>
<a id="l00320"></a>#define DT_PWMS_FLAGS(node_id) DT_PWMS_FLAGS_BY_IDX(node_id, 0)
<a id="l00321"></a>
<a id="l00332"></a>#define DT_INST_PWMS_CTLR_BY_IDX(inst, idx) \
<a id="l00333"></a>        DT_PWMS_CTLR_BY_IDX(DT_DRV_INST(inst), idx)
<a id="l00334"></a>
<a id="l00344"></a>#define DT_INST_PWMS_CTLR_BY_NAME(inst, name) \
<a id="l00345"></a>        DT_PWMS_CTLR_BY_NAME(DT_DRV_INST(inst), name)
<a id="l00346"></a>
<a id="l00354"></a>#define DT_INST_PWMS_CTLR(inst) DT_INST_PWMS_CTLR_BY_IDX(inst, 0)
<a id="l00355"></a>
<a id="l00364"></a>#define DT_INST_PWMS_CELL_BY_IDX(inst, idx, cell) \
<a id="l00365"></a>        DT_PWMS_CELL_BY_IDX(DT_DRV_INST(inst), idx, cell)
<a id="l00366"></a>
<a id="l00376"></a>#define DT_INST_PWMS_CELL_BY_NAME(inst, name, cell) \
<a id="l00377"></a>        DT_PWMS_CELL_BY_NAME(DT_DRV_INST(inst), name, cell)
<a id="l00378"></a>
<a id="l00385"></a>#define DT_INST_PWMS_CELL(inst, cell) \
<a id="l00386"></a>        DT_INST_PWMS_CELL_BY_IDX(inst, 0, cell)
<a id="l00387"></a>
<a id="l00395"></a>#define DT_INST_PWMS_CHANNEL_BY_IDX(inst, idx) \
<a id="l00396"></a>        DT_INST_PWMS_CELL_BY_IDX(inst, idx, channel)
<a id="l00397"></a>
<a id="l00406"></a>#define DT_INST_PWMS_CHANNEL_BY_NAME(inst, name) \
<a id="l00407"></a>        DT_INST_PWMS_CELL_BY_NAME(inst, name, channel)
<a id="l00408"></a>
<a id="l00415"></a>#define DT_INST_PWMS_CHANNEL(inst) DT_INST_PWMS_CHANNEL_BY_IDX(inst, 0)
<a id="l00416"></a>
<a id="l00424"></a>#define DT_INST_PWMS_PERIOD_BY_IDX(inst, idx) \
<a id="l00425"></a>        DT_INST_PWMS_CELL_BY_IDX(inst, idx, period)
<a id="l00426"></a>
<a id="l00435"></a>#define DT_INST_PWMS_PERIOD_BY_NAME(inst, name) \
<a id="l00436"></a>        DT_INST_PWMS_CELL_BY_NAME(inst, name, period)
<a id="l00437"></a>
<a id="l00444"></a>#define DT_INST_PWMS_PERIOD(inst) DT_INST_PWMS_PERIOD_BY_IDX(inst, 0)
<a id="l00445"></a>
<a id="l00453"></a>#define DT_INST_PWMS_FLAGS_BY_IDX(inst, idx) \
<a id="l00454"></a>        DT_INST_PWMS_CELL_BY_IDX(inst, idx, flags)
<a id="l00455"></a>
<a id="l00465"></a>#define DT_INST_PWMS_FLAGS_BY_NAME(inst, name) \
<a id="l00466"></a>        DT_INST_PWMS_CELL_BY_NAME(inst, name, flags)
<a id="l00467"></a>
<a id="l00474"></a>#define DT_INST_PWMS_FLAGS(inst) DT_INST_PWMS_FLAGS_BY_IDX(inst, 0)
<a id="l00475"></a>
<a id="l00479"></a>
<a id="l00480"></a>#ifdef __cplusplus
<a id="l00481"></a>}
<a id="l00482"></a>#endif
<a id="l00483"></a>
<a id="l00484"></a>#endif  /* ZEPHYR_INCLUDE_DEVICETREE_PWMS_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2020, Linaro Ltd.；Apache-2.0许可证原文保留。

2. 结束PWM设备树头文件的包含保护（Include Guard）ZEPHYR_INCLUDE_DEVICETREE_PWMS_H_。

## 2.3\_原页符号提示（Symbol Descriptions）

原网页没有独立的符号提示条目。

## 2.4\_源码跟踪译注

> 译注——对象与参数：消费节点的pwms属性引用PWM控制器并携带说明符（Specifier）；CTLR返回节点标识符，不是运行时设备指针。idx为属性条目的逻辑索引，name对应pwm-names名称的小写字母及下划线形式，二者都不是硬件通道号；channel才是说明符中的通道参数单元。参数单元的数目和名字由控制器的具体绑定决定，公共绑定仅要求#pwm-cells，不强制每种控制器都采用相同布局。

> 译注——缺省值边界：DT_PWMS_FLAGS_BY_IDX和DT_PWMS_FLAGS_BY_NAME使用DT_PHA_BY_IDX_OR／DT_PHA_BY_NAME_OR，flags不存在时缺省0；普通CELL、CHANNEL、PERIOD读取没有同样的缺省值。尤其当前源码中的DT_INST_PWMS_FLAGS_BY_IDX／BY_NAME直接调用DT_INST_PWMS_CELL_BY_IDX／BY_NAME，并未复用节点版的_OR回退，原始API返回值注释仍声称缺少单元时为0，与当前实际展开存在差异；不能认为两组flags宏在缺少单元时完全等价。

> 译注——周期与运行：period读取既有设备树单元，不进行定时器时钟或周期计数换算；按PWM约定其单位为纳秒（Nanoseconds）。宏不会启动波形、设置引脚复用、验证设备就绪或检查目标驱动能否实现该周期。实例inst属于DT_DRV_COMPAT对应的消费节点，不是PWM控制器编号。

> 译注——版本边界：本批核对三份官方头文件及PWM、I2C控制器公共绑定并记录摘要；三个源码浏览页的非注释代码与读取的官方原始头文件一致。latest、滚动main与仓库参照版本不自动相同。仓库源码链接仅用于定位；本次没有生成设备树、构建固件或操作硬件。

头文件相对定位：[include/zephyr/devicetree/pwms.h](../../../include/zephyr/devicetree/pwms.h)，关联实现／接口：[dts/bindings/pwm/pwm-controller.yaml](../../../dts/bindings/pwm/pwm-controller.yaml)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/pwms.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/pwm/pwm-controller.yaml)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未生成设备树、输出PWM波形、执行I2C传输或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_PWM设备树头文件参考.md)

---

[上一章](P001_PWM设备树头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_PWM绑定常量头文件参考.md)
