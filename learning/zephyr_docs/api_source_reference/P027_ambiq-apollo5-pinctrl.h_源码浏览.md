---
id: learning.zephyr-docs.api-source-reference.page-27
title: ambiq-apollo5-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo5-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_ambiq-apollo5-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo5-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo5-pinctrl_8h.html)。

## 27.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00020"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>

```c
/*
 * Copyright (c) 2025 Ambiq Micro Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO5_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO5_PINCTRL_H_




#define APOLLO5_ALT_FUNC_POS 0
#define APOLLO5_ALT_FUNC_MASK 0xf

#define APOLLO5_PIN_NUM_POS 4
#define APOLLO5_PIN_NUM_MASK 0xff

#define APOLLO5_PINMUX(pin_num, alt_func)       \
        (pin_num << APOLLO5_PIN_NUM_POS |       \
         alt_func << APOLLO5_ALT_FUNC_POS)



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO5_PINCTRL_H_ */
```

## 27.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Ambiq Micro Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 64 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO5_PINCTRL_H_`。

## 27.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo5-pinctrl_8h.html)

---

[上一章](P026_ambiq-apollo4-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P028_ameba_dma.h_源码浏览.md)
