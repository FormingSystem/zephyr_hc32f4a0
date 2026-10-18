---
id: learning.zephyr-docs.dt-bus-binding-reference.page-4
title: SPI绑定常量头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2spi_2spi_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_SPI绑定常量头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2spi_2spi_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P003_SPI绑定常量头文件参考.md)和[公共API](../hardware/P318_SPI公共接口.md)。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。


<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2021 Intel Corporation
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SPI_SPI_H_
<a id="l00007"></a>#define ZEPHYR_INCLUDE_DT_BINDINGS_SPI_SPI_H_
<a id="l00008"></a>
<a id="l00013"></a>
<a id="l00021"></a>#define SPI_FULL_DUPLEX         (0U &lt;&lt; 11)
<a id="l00022"></a>#define SPI_HALF_DUPLEX         (1U &lt;&lt; 11)
<a id="l00024"></a>
<a id="l00037"></a>#define SPI_FRAME_FORMAT_MOTOROLA       (0U &lt;&lt; 15)
<a id="l00038"></a>#define SPI_FRAME_FORMAT_TI             (1U &lt;&lt; 15)
<a id="l00040"></a>
<a id="l00044"></a>
<a id="l00045"></a>#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SPI_SPI_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2021 Intel Corporation；Apache-2.0许可证原文保留。

2. 结束SPI绑定头文件的包含保护ZEPHYR_INCLUDE_DT_BINDINGS_SPI_SPI_H_。

## 4.3\_原页符号提示（Symbol Descriptions）

原网页没有独立的符号提示条目。

## 4.4\_源码跟踪译注

> 译注——位编码与绑定：全双工值为0、半双工值为1U<<11（2048）；Motorola帧格式为0、TI格式为1U<<15（32768）。官方spi-device公共绑定的duplex和frame-format分别使用这些枚举，默认都是0，建议在DTS中使用宏名表达含义。数值并不代表所有控制器都实现相应模式。

> 译注——配置路径：SPI_CONFIG_DT把调用方operation_、duplex、frame-format以及CPOL、CPHA等属性按位或合并到operation。半双工与帧格式是独立字段，CPOL／CPHA控制时钟极性与相位，不能用TI或Motorola格式替代它们。按位或合并也不能清除调用方已经置1的位，因此默认值0不等于强制覆盖其他配置。

> 译注——传输时序：本页关于三线与CS行为保留官方概述。TI格式中的CS脉冲描述是帧格式规则，不表示配置任意GPIO片选就可模拟全部TI时序；实际连接方式、控制器能力与驱动支持仍需对应平台资料和运行时结果确认。

> 译注——版本边界：本批记录三个绑定头文件、GPIO与SPI驱动公共头文件、宏工具头文件和两个公共绑定，共八份官方源码摘要；三个源码浏览页的非注释内容与读取的原始头文件一致。latest、滚动main与仓库参照版本不自动相同。相对链接用于源码跟踪，本次未生成设备树、构建固件或操作硬件。

头文件相对定位：[include/zephyr/dt-bindings/spi/spi.h](../../../include/zephyr/dt-bindings/spi/spi.h)，关联实现／接口：[include/zephyr/drivers/spi.h](../../../include/zephyr/drivers/spi.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/spi/spi.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/spi.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未生成设备树、配置GPIO、执行SPI传输或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_SPI绑定常量头文件参考.md)

---

[上一章](P003_SPI绑定常量头文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_设备树绑定工具头文件参考.md)
