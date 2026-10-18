---
id: learning.zephyr-docs.api-source-configuration-reference.page-44
title: it8xxx2-i2c.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-i2c_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_it8xxx2-i2c.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-i2c_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-i2c_8h.html)。

## 44.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>

```c
/*
 * Copyright (c) 2022 ITE Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_I2C_IT8XXX2_I2C_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_I2C_IT8XXX2_I2C_H_


#define IT8XXX2_ECPM_CGCTRL4R_OFF       0x09
/*
 * The clock gate offsets combine the register offset from ECPM_BASE and the
 * mask within that register into one value. These are used for
 * clock_enable_peripheral() and clock_disable_peripheral()
 */
#define CGC_OFFSET_SMBF         ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x80)
#define CGC_OFFSET_SMBE         ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x40)
#define CGC_OFFSET_SMBD         ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x20)
#define CGC_OFFSET_SMBC         ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x10)
#define CGC_OFFSET_SMBB         ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x08)
#define CGC_OFFSET_SMBA         ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x04)

/* I2C channel switch selection */
#define I2C_CHA_LOCATE          0
#define I2C_CHB_LOCATE          1
#define I2C_CHC_LOCATE          2
#define I2C_CHD_LOCATE          3
#define I2C_CHE_LOCATE          4
#define I2C_CHF_LOCATE          5

#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_I2C_IT8XXX2_I2C_H_ */
```

## 44.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 ITE Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

时钟门控偏移量将相对于 `ECPM_BASE` 的寄存器偏移量及该寄存器内的掩码组合为一个值，供 `clock_enable_peripheral()` 和 `clock_disable_peripheral()` 使用。

### 注释 3：原第 23 行

I2C 通道切换选择。

### 注释 4：原第 31 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_I2C_IT8XXX2_I2C_H_`。

## 44.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-i2c_8h.html)

---

[上一章](P043_it51xxx_pwm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P045_ite-it51xxx-clock.h_源码浏览.md)
