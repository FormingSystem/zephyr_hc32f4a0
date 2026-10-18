---
id: learning.zephyr-docs.api-source-reference.page-199
title: npm13xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2regulator_2npm13xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第199章\_npm13xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2regulator_2npm13xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P111_nPM13xx稳压器设备树头文件.md)。

## 199.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_REGULATOR_NPM13XX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_REGULATOR_NPM13XX_H_


#define NPM13XX_BUCK_MODE_AUTO 0x00U
#define NPM13XX_BUCK_MODE_PWM  0x01U
#define NPM13XX_BUCK_MODE_PFM  0x04U

#define NPM13XX_LDSW_MODE_LDO  0x02U
#define NPM13XX_LDSW_MODE_LDSW 0x03U

#define NPM13XX_GPIO_CHAN_NONE 0x00U
#define NPM13XX_GPIO_CHAN_0    0x01U
#define NPM13XX_GPIO_CHAN_1    0x02U
#define NPM13XX_GPIO_CHAN_2    0x03U
#define NPM13XX_GPIO_CHAN_3    0x04U
#define NPM13XX_GPIO_CHAN_4    0x05U


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_REGULATOR_NPM13XX_H_*/
```

## 199.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 65 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_REGULATOR_NPM13XX_H_`。

## 199.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P111_nPM13xx稳压器设备树头文件.md)

---

[上一章](P198_npm10xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P200_npm2100.h_源码浏览.md)
