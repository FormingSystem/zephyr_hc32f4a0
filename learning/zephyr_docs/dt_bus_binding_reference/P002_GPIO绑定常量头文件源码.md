---
id: learning.zephyr-docs.dt-bus-binding-reference.page-2
title: GPIO绑定常量头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2gpio_2gpio_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_GPIO绑定常量头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2gpio_2gpio_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_GPIO绑定常量头文件参考.md)和[公共API](../hardware/P266_GPIO公共接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。


<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2019 Piotr Mienkowski
<a id="l00003"></a> * Copyright (c) 2018 Linaro Limited
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_GPIO_H_
<a id="l00008"></a>#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_GPIO_H_
<a id="l00009"></a>
<a id="l00014"></a>
<a id="l00016"></a>#define GPIO_DT_FLAGS_MASK 0x7F
<a id="l00017"></a>
<a id="l00022"></a>
<a id="l00024"></a>#define GPIO_ACTIVE_LOW         (1 &lt;&lt; 0)
<a id="l00026"></a>#define GPIO_ACTIVE_HIGH        (0 &lt;&lt; 0)
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>/* Configures GPIO output in single-ended mode (open drain or open source). */
<a id="l00038"></a>#define GPIO_SINGLE_ENDED       (1 &lt;&lt; 1)
<a id="l00039"></a>/* Configures GPIO output in push-pull mode */
<a id="l00040"></a>#define GPIO_PUSH_PULL          (0 &lt;&lt; 1)
<a id="l00041"></a>
<a id="l00042"></a>/* Indicates single ended open drain mode (wired AND). */
<a id="l00043"></a>#define GPIO_LINE_OPEN_DRAIN    (1 &lt;&lt; 2)
<a id="l00044"></a>/* Indicates single ended open source mode (wired OR). */
<a id="l00045"></a>#define GPIO_LINE_OPEN_SOURCE   (0 &lt;&lt; 2)
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00055"></a>#define GPIO_OPEN_DRAIN         (GPIO_SINGLE_ENDED | GPIO_LINE_OPEN_DRAIN)
<a id="l00063"></a>#define GPIO_OPEN_SOURCE        (GPIO_SINGLE_ENDED | GPIO_LINE_OPEN_SOURCE)
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00071"></a>
<a id="l00073"></a>#define GPIO_PULL_UP            (1 &lt;&lt; 4)
<a id="l00074"></a>
<a id="l00076"></a>#define GPIO_PULL_DOWN          (1 &lt;&lt; 5)
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00083"></a>#define GPIO_INT_WAKEUP         (1 &lt;&lt; 6)
<a id="l00084"></a>
<a id="l00085"></a>/* Note: Bits 15 downto 8 are reserved for SoC specific flags. */
<a id="l00086"></a>
<a id="l00090"></a>
<a id="l00091"></a>#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_GPIO_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2019 Piotr Mienkowski；Copyright (c) 2018 Linaro Limited；Apache-2.0许可证原文保留。

2. 将GPIO输出配置为单端模式（Single-ended Mode），即开漏（Open Drain）或开源极（Open Source）。

3. 将GPIO输出配置为推挽模式（Push-pull Mode）。

4. 表示单端开漏模式，即线与（Wired AND）。

5. 表示单端开源极模式，即线或（Wired OR）。

6. 注意：位15至位8保留给片上系统（System on Chip，SoC）专用标志。

7. 结束GPIO绑定头文件的包含保护（Include Guard）ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_GPIO_H_。

## 2.3\_原页符号提示（Symbol Descriptions）

原网页没有独立的符号提示条目。

## 2.4\_源码跟踪译注

> 译注——有效电平与物理电平：GPIO_ACTIVE_LOW设定位0，GPIO_ACTIVE_HIGH为0；它们约定逻辑有效状态，不直接设定输出电压，也不包含输入／输出方向。逻辑读写接口考虑ACTIVE_LOW，带raw后缀的物理电平接口忽略这一逻辑反转；方向、输出初始化与中断触发模式另由驱动接口配置。

> 译注——驱动与偏置：GPIO_OPEN_DRAIN组合单端驱动位1与开漏选择位2，GPIO_OPEN_SOURCE组合单端驱动位1与取值为0的开源极选择位2。开源极（Open Source）在这里是相对于开漏的输出模式名称，不是开放源代码。上拉、下拉分别占位4、位5；当前GPIO公共配置实现含有不能同时启用二者的断言，断言是否保留取决于构建配置，不能将其理解为各驱动始终返回统一错误。

> 译注——标志布局与唤醒：GPIO_DT_FLAGS_MASK为0x7F，覆盖位0至6；源码另将位8至15保留给SoC专用标志，这个掩码不包含全部厂商位。GPIO_INT_WAKEUP占位6；gpio_pin_interrupt_configure_dt仅从设备树标志中合入该唤醒位，其他设备树标志在该中断配置路径被忽略。常量本身不保证控制器支持唤醒，也不替代中断使能与电源管理配置。

> 译注——版本边界：本批记录三个绑定头文件、GPIO与SPI驱动公共头文件、宏工具头文件和两个公共绑定，共八份官方源码摘要；三个源码浏览页的非注释内容与读取的原始头文件一致。latest、滚动main与仓库参照版本不自动相同。相对链接用于源码跟踪，本次未生成设备树、构建固件或操作硬件。

头文件相对定位：[include/zephyr/dt-bindings/gpio/gpio.h](../../../include/zephyr/dt-bindings/gpio/gpio.h)，关联实现／接口：[include/zephyr/drivers/gpio.h](../../../include/zephyr/drivers/gpio.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/gpio/gpio.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/gpio.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未生成设备树、配置GPIO、执行SPI传输或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_GPIO绑定常量头文件参考.md)

---

[上一章](P001_GPIO绑定常量头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_SPI绑定常量头文件参考.md)
