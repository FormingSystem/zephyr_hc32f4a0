---
id: learning.zephyr-docs.api-source-reference.page-706
title: renesas-rzt2m-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rzt2m-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第706章\_renesas-rzt2m-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rzt2m-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rzt2m-pinctrl_8h.html)。

## 706.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
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

```c
/*
 * Copyright (c) 2023 Antmicro <www.antmicro.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_RZT2M_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_RZT2M_PINCTRL_H_

#define RZT2M_PINMUX(port, pin, func) ((port << 16) | (pin << 8) | func)

#define UART0TX_P16_5   RZT2M_PINMUX(16, 5, 1)
#define UART0RX_P16_6   RZT2M_PINMUX(16, 6, 2)

#define UART3TX_P18_0   RZT2M_PINMUX(18, 0, 4)
#define UART3RX_P17_7   RZT2M_PINMUX(17, 7, 4)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_RZT2M_PINCTRL_H_ */
```

## 706.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Antmicro <www.antmicro.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 18 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_RZT2M_PINCTRL_H_`。

## 706.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rzt2m-pinctrl_8h.html)

---

[上一章](P705_renesas-rzt2m-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P707_renesas,ra-sdram.h_源码浏览.md)
