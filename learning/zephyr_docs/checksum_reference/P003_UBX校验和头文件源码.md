---
id: learning.zephyr-docs.checksum-reference.page-3
title: UBX校验和头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/checksum_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_UBX校验和头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/checksum_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P002_UBX校验和头文件参考.md)和[公共API](P002_UBX校验和头文件参考.md)。

## 3.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00015"></a>
<a id="foldopen00025"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2025 Croxel Inc.
<a id="l00003"></a> * Copyright (c) 2025 CogniPilot Foundation
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00008"></a>#ifndef ZEPHYR_INCLUDE_MODEM_UBX_CHECKSUM_H_
<a id="l00009"></a>#define ZEPHYR_INCLUDE_MODEM_UBX_CHECKSUM_H_
<a id="l00010"></a>
<a id="l00012"></a>
<a id="l00013"></a>#define UBX_CSUM_A(...) UBX_CSUM_A_(__VA_ARGS__)
<a id="l00014"></a>
<a id="l00015"></a>#define UBX_CSUM_A_(...) UBX_CSUM_A_I(__VA_ARGS__,                                                 \
<a id="l00016"></a>                                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
<a id="l00017"></a>
<a id="l00018"></a>#define UBX_CSUM_A_I(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,                                      \
<a id="l00019"></a>                     a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ...)                        \
<a id="l00020"></a>        ((a1) + (a2) + (a3) + (a4) + (a5) + (a6) + (a7) + (a8) + (a9) + (a10) +                    \
<a id="l00021"></a>         (a11) + (a12) + (a13) + (a14) + (a15) + (a16) + (a17) + (a18) + (a19) + (a20)) &amp; 0xFF
<a id="l00022"></a>
<a id="l00023"></a>#define UBX_CSUM_B(...) UBX_CSUM_B_(__VA_ARGS__)
<a id="l00024"></a>
<a id="l00025"></a>#define UBX_CSUM_B_(...) UBX_CSUM_B_I(NUM_VA_ARGS(__VA_ARGS__), __VA_ARGS__,                       \
<a id="l00026"></a>                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
<a id="l00027"></a>
<a id="l00028"></a>#define UBX_CSUM_B_I(len, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,                                 \
<a id="l00029"></a>                     a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ...)                        \
<a id="l00030"></a>        (((len) * a1) + ((len - 1) * a2) + ((len - 2) * a3) + ((len - 3) * a4) +                   \
<a id="l00031"></a>         ((len - 4) * a5) + ((len - 5) * a6) + ((len - 6) * a7) + ((len - 7) * a8) +               \
<a id="l00032"></a>         ((len - 8) * a9) + ((len - 9) * a10) + ((len - 10) * a11) + ((len - 11) * a12) +          \
<a id="l00033"></a>         ((len - 12) * a13) + ((len - 13) * a14) + ((len - 14) * a15) + ((len - 15) * a16) +       \
<a id="l00034"></a>         ((len - 16) * a17) + ((len - 17) * a18) + ((len - 18) * a19) + ((len - 19) * a20)) &amp; 0xFF
<a id="l00035"></a>
<a id="l00036"></a>#define UBX_CSUM(...) UBX_CSUM_A(__VA_ARGS__), UBX_CSUM_B(__VA_ARGS__)
<a id="l00037"></a>
<a id="l00038"></a>#endif /* ZEPHYR_INCLUDE_MODEM_UBX_CHECKSUM_H_ */
</code></pre>

## 3.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2025 Croxel Inc.；Copyright (c) 2025 CogniPilot Foundation；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_MODEM_UBX_CHECKSUM_H_头文件包含保护结束。

## 3.3\_原页符号提示（Symbol Descriptions）

原网页没有独立的符号提示条目。

## 3.4\_源码跟踪译注

> 译注——此checksum.h位于include/zephyr/modem/ubx，专用于UBX校验和的编译期宏，不是CRC公共头文件，也不是接受指针和长度的运行时流式计算函数。本文只翻译官方头文件所展示的宏及原始说明。

> 译注——UBX_CSUM_A按输入元素求和后取低8位；UBX_CSUM_B按元素位置进行加权求和后取低8位。UBX_CSUM展开为以逗号分隔的两个表达式，供两个校验字节使用，不是单一16位返回值。

> 译注——当前内部宏显式接收a1至a20并用零补足参数；传入超过20项不能当作支持任意长度，尾部可变参数不会被求和表达式完整消费。调用者应遵守实际宏范围，不把它推广为通用数组处理。

> 译注——原宏表达式、掩码、参数括号和求值方式保持原样。部分展开未对整个表达式额外加括号，且组合宏会复用参数；不要传入带副作用的表达式或假定任意嵌套运算都不受C运算符优先级影响。NUM_VA_ARGS来自宏工具，调用环境必须提供相应定义。

头文件定位：[include/zephyr/modem/ubx/checksum.h](../../../include/zephyr/modem/ubx/checksum.h)，关联实现／接口：[include/zephyr/modem/ubx/checksum.h](../../../include/zephyr/modem/ubx/checksum.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/modem/ubx/checksum.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/modem/ubx/checksum.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P002_UBX校验和头文件参考.md)

---

[上一章](P002_UBX校验和头文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_位反转接口.md)
