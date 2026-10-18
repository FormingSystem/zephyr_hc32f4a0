---
id: learning.zephyr-docs.api-source-reference.page-198
title: npm10xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2regulator_2npm10xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第198章\_npm10xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2regulator_2npm10xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P109_nPM10xx稳压器设备树头文件.md)。

## 198.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00023"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00047"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00062"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_REGULATOR_NPM10XX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_REGULATOR_NPM10XX_H_

#include <zephyr/sys/util_macro.h>


#define NPM10XX_BUCK_PWRMODE_Msk  BIT_MASK(2)
#define NPM10XX_BUCK_PASSTHRU_Msk (BIT_MASK(2) << 2)
#define NPM10XX_BUCK_PWRMODE_LP   BIT(0)
#define NPM10XX_BUCK_PWRMODE_ULP  BIT(1)
#define NPM10XX_BUCK_PASSTHRU_OFF BIT(2)
#define NPM10XX_BUCK_PASSTHRU_ON  BIT(3)

#define NPM10XX_LDO_MODE_Msk BIT_MASK(2)
#define NPM10XX_LDO_MODE_LDO BIT(0)
#define NPM10XX_LDO_MODE_LS  BIT(1)

#define NPM10XX_REG_GPIO_Msk      (BIT_MASK(4) << 4)
#define NPM10XX_REG_GPIO_EN       BIT(4)
#define NPM10XX_BUCK_GPIO_PWRMODE BIT(5)
#define NPM10XX_BUCK_GPIO_ALTVOUT BIT(6)
#define NPM10XX_REG_GPIO_NONE     BIT(7)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_REGULATOR_NPM10XX_H_ */
```

## 198.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 76 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_REGULATOR_NPM10XX_H_`。

## 198.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P109_nPM10xx稳压器设备树头文件.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P197_max20362.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P199_npm13xx.h_源码浏览.md)
