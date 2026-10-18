---
id: learning.zephyr-docs.api-source-reference.page-848
title: syna-sr100-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/syna-sr100-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第848章\_syna-sr100-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/syna-sr100-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/syna-sr100-pinctrl_8h.html)。

## 848.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>

```c
/*
 * Copyright (c) 2025 Synaptics, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SYNA_SR100_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SYNA_SR100_PINCTRL_H_

#define SRXXX_CTRL_SHIFT 0U
#define SRXXX_CTRL_MASK  0x07U
#define SRXXX_BIT_SHIFT  3U
#define SRXXX_BIT_MASK   0x1FU
#define SRXXX_MODE_SHIFT 8U
#define SRXXX_MODE_MASK  0x07U
#define SRXXX_MASK_SHIFT 11U
#define SRXXX_MASK_MASK  0x0FU
#define SRXXX_REG_SHIFT  16U
#define SRXXX_REG_MASK   0xFFU
#define SRXXX_CFG_SHIFT  24U
#define SRXXX_CFG_MASK   0xFFU

#define SRXXX_PINMUX(ctrl, reg, bit, mode, mask, cfg)       \
        ((((ctrl) & SRXXX_CTRL_MASK) << SRXXX_CTRL_SHIFT) | \
         (((reg)  & SRXXX_REG_MASK)  << SRXXX_REG_SHIFT)  | \
         (((bit)  & SRXXX_BIT_MASK)  << SRXXX_BIT_SHIFT)  | \
         (((mode) & SRXXX_MODE_MASK) << SRXXX_MODE_SHIFT) | \
         (((mask) & SRXXX_MASK_MASK) << SRXXX_MASK_SHIFT) | \
         (((cfg)  & SRXXX_CFG_MASK)  << SRXXX_CFG_SHIFT))

#define SRXXX_GLOBAL_PINMUX(reg, bit, mode, cfg)        SRXXX_PINMUX(0, reg, bit, mode, 7, cfg)
#define SRXXX_AON_PINMUX(reg, bit, mode, cfg)           SRXXX_PINMUX(1, reg, bit, mode, 7, cfg)
#define SRXXX_LPS_PINMUX(reg, bit, mode, cfg)           SRXXX_PINMUX(2, reg, bit, mode, 7, cfg)
#define SRXXX_SWIRE_PINMUX(bit, mode)                   SRXXX_PINMUX(3, 0, bit, mode, 1, 0)

#define SRXXX_PORT_PINMUX(reg, bit, mode, mask)         SRXXX_PINMUX(4, reg, bit, mode, mask, 0)
#define SRXXX_FIXED_PINMUX(cfg)                         SRXXX_PINMUX(0, 0, 0, 0, 0, cfg)

#define SRXXX_PINMUX_CTRL(pinmux)       (((pinmux) >> SRXXX_CTRL_SHIFT) & SRXXX_CTRL_MASK)
#define SRXXX_PINMUX_REG(pinmux)        (((pinmux) >> SRXXX_REG_SHIFT) & SRXXX_REG_MASK)
#define SRXXX_PINMUX_BIT(pinmux)        (((pinmux) >> SRXXX_BIT_SHIFT) & SRXXX_BIT_MASK)
#define SRXXX_PINMUX_MODE(pinmux)       (((pinmux) >> SRXXX_MODE_SHIFT) & SRXXX_MODE_MASK)
#define SRXXX_PINMUX_MASK(pinmux)       (((pinmux) >> SRXXX_MASK_SHIFT) & SRXXX_MASK_MASK)
#define SRXXX_PINMUX_CFG(pinmux)        (((pinmux) >> SRXXX_CFG_SHIFT) & SRXXX_CFG_MASK)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SYNA_SR100_PINCTRL_H_ */
```

## 848.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Synaptics, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 100 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SYNA_SR100_PINCTRL_H_`。

## 848.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/syna-sr100-pinctrl_8h.html)

---

[上一章](P847_sx126x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P849_syna_sr100_clock.h_源码浏览.md)
