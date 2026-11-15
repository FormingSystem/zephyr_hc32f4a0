---
id: learning.zephyr-docs.cpu-runtime-reference.page-4
title: CPU负载指标头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cpu__load__metric_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_CPU负载指标头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cpu__load__metric_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P003_CPU负载指标头文件参考.md)和[公共API](../observability/P049_CPU负载接口.md)。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="acpu__load_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2025 Analog Devices, Inc.
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>#ifndef ZEPHYR_INCLUDE_SYS_CPU_LOAD_METRIC_H_
<a id="l00017"></a>#define ZEPHYR_INCLUDE_SYS_CPU_LOAD_METRIC_H_
<a id="l00018"></a>
<a id="l00019"></a>#include &lt;zephyr/sys/cpu_load.h&gt;
<a id="l00020"></a>
<a id="l00021"></a>#endif /* ZEPHYR_INCLUDE_SYS_CPU_LOAD_METRIC_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2025 Analog Devices, Inc.；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SYS_CPU_LOAD_METRIC_H_头文件包含保护结束。

## 4.3\_原页符号提示（Symbol Descriptions）

### `cpu_load.h`

符号定位：[cpu_load.h](P001_CPU负载头文件参考.md)。

## 4.4\_源码跟踪译注

> 译注——cpu_load_get_cpu和cpu_load_get返回千分比（Per Mille）0～1000，失败返回负errno；先检查负值再转换单位。CPU_LOAD_PERMILLE_TO_PERCENT只是除以10，整数输入会舍去小数，不负责错误检查。旧cpu_load_metric_get返回整数百分比，并固定传入reset=true，迁移接口时单位和采样窗口都要明确。

> 译注——兼容头文件（Compatibility Header）现在只包含zephyr/sys/cpu_load.h，不提供独立的测量实现。已弃用不等于已删除；旧包装函数仍位于新头文件中。

头文件相对定位：[include/zephyr/sys/cpu_load_metric.h](../../../include/zephyr/sys/cpu_load_metric.h)，关联实现／接口：[include/zephyr/sys/cpu_load.h](../../../include/zephyr/sys/cpu_load.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/cpu_load_metric.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/cpu_load.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_CPU负载指标头文件参考.md)
- [zephyr/sys/cpu_load.h](P001_CPU负载头文件参考.md)

---

[上一章](P003_CPU负载指标头文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_线程分析器头文件参考.md)
