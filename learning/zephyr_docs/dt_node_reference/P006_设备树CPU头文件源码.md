---
id: learning.zephyr-docs.dt-node-reference.page-6
title: 设备树CPU头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2cpu_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_设备树CPU头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2cpu_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P005_设备树CPU头文件参考.md)和[公共API](P003_设备树CPU节点宏.md)。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00103"></a>
<a id="foldopen00119"></a>
<a id="foldopen00136"></a>
<a id="foldopen00152"></a>
<a id="foldopen00170"></a>
<a id="foldopen00190"></a>
<a id="adevicetree_8h_html"></a>
<a id="autil__macro_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
<a id="l00003"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00004"></a> */
<a id="l00005"></a>
<a id="l00010"></a>#ifndef ZEPHYR_INCLUDE_DEVICETREE_CPU_H_
<a id="l00011"></a>#define ZEPHYR_INCLUDE_DEVICETREE_CPU_H_
<a id="l00012"></a>
<a id="l00013"></a>#ifdef __cplusplus
<a id="l00014"></a>extern "C" {
<a id="l00015"></a>#endif
<a id="l00016"></a>
<a id="l00017"></a>#include &lt;zephyr/devicetree.h&gt;
<a id="l00018"></a>#include &lt;zephyr/sys/util_macro.h&gt;
<a id="l00019"></a>
<a id="l00025"></a>
<a id="l00074"></a>#define DT_FOREACH_CPU(fn) DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_INTERNAL, fn)
<a id="l00075"></a>
<a id="l00103"></a>#define DT_FOREACH_CPU_SEP(fn, sep)                                                                \
<a id="l00104"></a>        DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_SEP_INTERNAL, fn, sep)
<a id="l00105"></a>
<a id="l00119"></a>#define DT_FOREACH_CPU_VARGS(fn, ...)                                                              \
<a id="l00120"></a>        DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_VARGS_INTERNAL, fn, __VA_ARGS__)
<a id="l00121"></a>
<a id="l00136"></a>#define DT_FOREACH_CPU_SEP_VARGS(fn, sep, ...)                                                     \
<a id="l00137"></a>        DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_SEP_VARGS_INTERNAL, fn, sep,          \
<a id="l00138"></a>                               __VA_ARGS__)
<a id="l00139"></a>
<a id="l00152"></a>#define DT_FOREACH_CPU_STATUS_OKAY(fn)                                                             \
<a id="l00153"></a>        DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_STATUS_OKAY_INTERNAL, fn)
<a id="l00154"></a>
<a id="l00170"></a>#define DT_FOREACH_CPU_STATUS_OKAY_SEP(fn, sep)                                                    \
<a id="l00171"></a>        DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_STATUS_OKAY_SEP_INTERNAL, fn, sep)
<a id="l00172"></a>
<a id="l00190"></a>#define DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS(fn, sep, ...)                                         \
<a id="l00191"></a>        DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS_INTERNAL, fn,   \
<a id="l00192"></a>                               sep, __VA_ARGS__)
<a id="l00193"></a>
<a id="l00195"></a>#define DT_FOREACH_CPU_INTERNAL(node_id, fn)                                                       \
<a id="l00196"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, device_type), (fn(node_id)), ())
<a id="l00197"></a>
<a id="l00198"></a>#define DT_FOREACH_CPU_VARGS_INTERNAL(node_id, fn, ...)                                            \
<a id="l00199"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, device_type), \
<a id="l00200"></a>                    (fn(node_id, __VA_ARGS__)), ())
<a id="l00201"></a>
<a id="l00202"></a>#define DT_FOREACH_CPU_SEP_INTERNAL(node_id, fn, sep)                                              \
<a id="l00203"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, device_type), \
<a id="l00204"></a>                    (fn(node_id) DT_DEBRACKET_INTERNAL sep), ())
<a id="l00205"></a>
<a id="l00206"></a>#define DT_FOREACH_CPU_SEP_VARGS_INTERNAL(node_id, fn, sep, ...)                                   \
<a id="l00207"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, device_type), \
<a id="l00208"></a>                    (fn(node_id, __VA_ARGS__) DT_DEBRACKET_INTERNAL sep), ())
<a id="l00209"></a>
<a id="l00210"></a>#define DT_FOREACH_CPU_STATUS_OKAY_INTERNAL(node_id, fn)                                           \
<a id="l00211"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, device_type), \
<a id="l00212"></a>                    (COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(node_id), (fn(node_id)), ())), ())
<a id="l00213"></a>
<a id="l00214"></a>#define DT_FOREACH_CPU_STATUS_OKAY_SEP_INTERNAL(node_id, fn, sep)                                  \
<a id="l00215"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, device_type), \
<a id="l00216"></a>                    (COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(node_id), \
<a id="l00217"></a>                                  (fn(node_id) DT_DEBRACKET_INTERNAL sep), ())), \
<a id="l00218"></a>                    ())
<a id="l00219"></a>
<a id="l00220"></a>#define DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS_INTERNAL(node_id, fn, sep, ...)                       \
<a id="l00221"></a>        COND_CODE_1(DT_NODE_HAS_PROP(node_id, device_type), \
<a id="l00222"></a>                    (COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(node_id), \
<a id="l00223"></a>                                  (fn(node_id, __VA_ARGS__) DT_DEBRACKET_INTERNAL sep), ())), \
<a id="l00224"></a>                    ())
<a id="l00226"></a>
<a id="l00230"></a>
<a id="l00231"></a>#ifdef __cplusplus
<a id="l00232"></a>}
<a id="l00233"></a>#endif
<a id="l00234"></a>
<a id="l00235"></a>#endif /* ZEPHYR_INCLUDE_DEVICETREE_CPU_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权：Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries。版权归Qualcomm Technologies, Inc.及／或其子公司；Apache-2.0许可证原文保留。

2. 结束头文件包含保护（Include Guard）ZEPHYR_INCLUDE_DEVICETREE_CPU_H_。

## 6.3\_原页符号提示（Symbol Descriptions）

### `devicetree.h`

设备树（Devicetree）主头文件。

符号定位：[devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)。

### `util_macro.h`

宏工具（Macro Utilities）。

符号定位：[util_macro.h](../util_reference/P004_宏工具头文件参考.md)。

## 6.4\_源码跟踪译注

> 译注——原文与筛选实现：原文描述只处理device_type值为cpu的子节点；本次cpu.h的内部宏实际只使用DT_NODE_HAS_PROP(node_id, device_type)检查该属性是否存在，没有在宏中比较字符串值。正常CPU绑定约束应与原文约定配合，但不能把宏自身描述为对任意输入都进行了值校验。示例power-states没有该属性，所以会被跳过。

> 译注——遍历范围：宏通过DT_FOREACH_CHILD_VARGS遍历/cpus的直接子节点，不递归枚举任意后代，也不是运行时CPU枚举函数。普通版本不筛选status，STATUS_OKAY版本才进一步使用DT_NODE_HAS_STATUS_OKAY；它遵循Zephyr设备树对缺省status的规则，不应把“未写status”直接判成disabled。

> 译注——参数和顺序：fn是宏名，单参数版本接收节点标识；VARGS版本把调用者额外参数接在节点标识之后。按最终设备树顺序展开，不保证按reg数值排序，也不代表运行时核心上线或调度顺序。/cpus节点、生成头文件及宏定义必须在当前构建上下文可用。

> 译注——尾随分隔符：SEP内部实现为fn(...)后接DT_DEBRACKET_INTERNAL sep，因此每次保留的节点都会带分隔符，最后一次也有。传入逗号须写(,)，分号可写(;)。这与只在相邻元素之间插入分隔符的常见遍历形式不同，组合表达式前应核对语法。

> 译注——版本与范围：本册仅翻译所列官方页面。CPU和依赖顺序源码去掉注释与展示空白后与本次官方头文件一致；总线和chosen展开式结合本次devicetree.h及生成脚本核对。相对源码定位用于跟踪，不把任意本地基线视为与滚动main相同。本次未编译展开示例或进行CPU、总线、初始化及实板实验。

头文件相对定位：[include/zephyr/devicetree/cpu.h](../../../include/zephyr/devicetree/cpu.h)，关联实现／接口：[include/zephyr/devicetree.h](../../../include/zephyr/devicetree.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/cpu.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未编译或执行CPU、总线、初始化、宏边界及实板实验。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_设备树CPU头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P005_设备树CPU头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_依赖顺序头文件参考.md)
