---
id: learning.zephyr-docs.dt-pwm-binding-reference.page-4
title: PWM绑定常量头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pwm_2pwm_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_PWM绑定常量头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pwm_2pwm_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P003_PWM绑定常量头文件参考.md)和[公共API](../hardware/P255_PWM公共接口.md)。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。


<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2019 Vestas Wind Systems A/S
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PWM_PWM_H_
<a id="l00007"></a>#define ZEPHYR_INCLUDE_DT_BINDINGS_PWM_PWM_H_
<a id="l00008"></a>
<a id="l00013"></a>
<a id="l00020"></a>
<a id="l00022"></a>#define PWM_NSEC(x)     (x)
<a id="l00024"></a>#define PWM_USEC(x)     (PWM_NSEC(x) * 1000UL)
<a id="l00026"></a>#define PWM_MSEC(x)     (PWM_USEC(x) * 1000UL)
<a id="l00028"></a>#define PWM_SEC(x)      (PWM_MSEC(x) * 1000UL)
<a id="l00030"></a>#define PWM_HZ(x)       (PWM_SEC(1UL) / (x))
<a id="l00032"></a>#define PWM_KHZ(x)      (PWM_HZ((x) * 1000UL))
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00045"></a>#define PWM_POLARITY_NORMAL     (0 &lt;&lt; 0)
<a id="l00046"></a>
<a id="l00048"></a>#define PWM_POLARITY_INVERTED   (1 &lt;&lt; 0)
<a id="l00049"></a>
<a id="l00051"></a>#define PWM_POLARITY_MASK       0x1
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PWM_PWM_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2019 Vestas Wind Systems A/S；Apache-2.0许可证原文保留。

2. 结束PWM绑定头文件的包含保护ZEPHYR_INCLUDE_DT_BINDINGS_PWM_PWM_H_。

## 4.3\_原页符号提示（Symbol Descriptions）

原网页没有独立的符号提示条目。

## 4.4\_源码跟踪译注

> 译注——周期换算：PWM_NSEC原样返回参数，USEC／MSEC／SEC逐级乘1000UL；PWM_HZ通过1000000000UL除以频率生成纳秒周期，PWM_KHZ先把千赫兹换算为赫兹。因此频率辅助宏的结果仍是周期，不是频率值。常见整数常量输入会执行整数除法，不能保证无截断；零频率、乘法溢出和实际定时器分辨率均不由这些宏检查。

> 译注——极性标志：正常极性（Normal Polarity）为高电平有效脉冲，反向极性（Inverted Polarity）为低电平有效脉冲；常量分别为0与1，内部PWM_POLARITY_MASK为0x1。原文所说低8位是标志布局说明，不表示该头文件定义了八种极性，也不表示所有驱动都支持所有标志。头文件引用运行时API只是说明使用位置，不会自行配置硬件。

> 译注——版本边界：本批核对三份官方头文件及PWM、I2C控制器公共绑定并记录摘要；三个源码浏览页的非注释代码与读取的官方原始头文件一致。latest、滚动main与仓库参照版本不自动相同。仓库源码链接仅用于定位；本次没有生成设备树、构建固件或操作硬件。

头文件相对定位：[include/zephyr/dt-bindings/pwm/pwm.h](../../../include/zephyr/dt-bindings/pwm/pwm.h)，关联实现／接口：[dts/bindings/pwm/pwm-controller.yaml](../../../dts/bindings/pwm/pwm-controller.yaml)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/pwm/pwm.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/pwm/pwm-controller.yaml)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未生成设备树、输出PWM波形、执行I2C传输或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_PWM绑定常量头文件参考.md)

---

[上一章](P003_PWM绑定常量头文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_I2C绑定常量头文件参考.md)
