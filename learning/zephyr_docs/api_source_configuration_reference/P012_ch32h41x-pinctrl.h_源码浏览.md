---
id: learning.zephyr-docs.api-source-configuration-reference.page-12
title: ch32h41x-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ch32h41x-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_ch32h41x-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ch32h41x-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ch32h41x-pinctrl_8h.html)。

## 12.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>

```c
/*
 * Copyright (c) 2026 Liu Changjie
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef __CH32H41X_PINCTRL_H__
#define __CH32H41X_PINCTRL_H__



#define CH32H41X_PINMUX_PORT_PA 0
#define CH32H41X_PINMUX_PORT_PB 1
#define CH32H41X_PINMUX_PORT_PC 2
#define CH32H41X_PINMUX_PORT_PD 3
#define CH32H41X_PINMUX_PORT_PE 4
#define CH32H41X_PINMUX_PORT_PF 5

#define CH32H41X_PINMUX_PORT_MASK 0x007
#define CH32H41X_PINMUX_PIN_MASK  0x078
#define CH32H41X_PINMUX_AF_MASK   0x780

#define CH32H41X_PINMUX(port, pin, af) ((CH32H41X_PINMUX_PORT_##port) | ((pin) << 3) | ((af) << 7))

/* USART1: AF7 */
#define USART1_TX_PA9_AF7  CH32H41X_PINMUX(PA, 9, 7)
#define USART1_RX_PA10_AF7 CH32H41X_PINMUX(PA, 10, 7)

/* USART8: AF11 */
#define USART8_TX_PB4_AF11 CH32H41X_PINMUX(PB, 4, 11)


#endif /* __CH32H41X_PINCTRL_H__ */
```

## 12.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Liu Changjie。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

USART1：复用功能 AF7。

### 注释 3：原第 68 行

USART8：复用功能 AF11。

### 注释 4：原第 74 行

头文件保护宏（Header guard）标记：`__CH32H41X_PINCTRL_H__`。

## 12.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ch32h41x-pinctrl_8h.html)

---

[上一章](P011_cfg.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P013_ch570-pinctrl.h_源码浏览.md)
