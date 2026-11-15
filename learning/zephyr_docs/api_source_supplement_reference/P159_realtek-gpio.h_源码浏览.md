---
id: learning.zephyr-docs.api-source-supplement-reference.page-159
title: realtek-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/realtek-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第159章\_realtek-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/realtek-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/realtek-gpio_8h.html)。

## 159.1\_原始可见代码（Source Code）

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
<a id="l00012"></a>
<a id="l00014"></a>
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (c) 2024 Realtek Semiconductor Corporation, SIBG-SD7
 * Author: Lin Yu-Cheng <lin_yu_cheng@realtek.com>
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_REALTEK_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_REALTEK_GPIO_H_

#define RTS5912_GPIO_INDETEN  BIT(8)
#define RTS5912_GPIO_OUTDRV   BIT(9)
#define RTS5912_GPIO_SLEWRATE BIT(10)
#define RTS5912_GPIO_SCHEN    BIT(11)

#define RTS5912_GPIO_VOLTAGE_POS     12
#define RTS5912_GPIO_VOLTAGE_MASK    GENMASK(13, 12)
#define RTS5912_GPIO_VOLTAGE_DEFAULT (0U << RTS5912_GPIO_VOLTAGE_POS)
#define RTS5912_GPIO_VOLTAGE_1V8     (1U << RTS5912_GPIO_VOLTAGE_POS)
#define RTS5912_GPIO_VOLTAGE_3V3     (2U << RTS5912_GPIO_VOLTAGE_POS)
#define RTS5912_GPIO_VOLTAGE_5V0     (3U << RTS5912_GPIO_VOLTAGE_POS)

#define RTS5912_GPIO_MFCTRL_POS  14
#define RTS5912_GPIO_MFCTRL_MASK GENMASK(15, 14)
#define RTS5912_GPIO_MFCTRL_0    (0U << RTS5912_GPIO_MFCTRL_POS)
#define RTS5912_GPIO_MFCTRL_1    (1U << RTS5912_GPIO_MFCTRL_POS)
#define RTS5912_GPIO_MFCTRL_2    (2U << RTS5912_GPIO_MFCTRL_POS)
#define RTS5912_GPIO_MFCTRL_3    (3U << RTS5912_GPIO_MFCTRL_POS)
#define RTS5912_GPIO_INTR_MASK   (1U << 21 | 1U << 22 | 1U << 24 | 1U << 25 | 1U << 26)


#define RTS5912_GPIO000 &gpioa 0
#define RTS5912_GPIO001 &gpioa 1
#define RTS5912_GPIO002 &gpioa 2
#define RTS5912_GPIO003 &gpioa 3
#define RTS5912_GPIO004 &gpioa 4
#define RTS5912_GPIO009 &gpioa 9
#define RTS5912_GPIO013 &gpioa 13
#define RTS5912_GPIO014 &gpioa 14
#define RTS5912_GPIO015 &gpioa 15
#define RTS5912_GPIO016 &gpiob 0
#define RTS5912_GPIO017 &gpiob 1
#define RTS5912_GPIO018 &gpiob 2
#define RTS5912_GPIO019 &gpiob 3
#define RTS5912_GPIO020 &gpiob 4
#define RTS5912_GPIO021 &gpiob 5
#define RTS5912_GPIO022 &gpiob 6
#define RTS5912_GPIO023 &gpiob 7
#define RTS5912_GPIO025 &gpiob 9
#define RTS5912_GPIO026 &gpiob 10
#define RTS5912_GPIO027 &gpiob 11
#define RTS5912_GPIO028 &gpiob 12
#define RTS5912_GPIO029 &gpiob 13
#define RTS5912_GPIO030 &gpiob 14
#define RTS5912_GPIO031 &gpiob 15
#define RTS5912_GPIO040 &gpioc 8
#define RTS5912_GPIO041 &gpioc 9
#define RTS5912_GPIO042 &gpioc 10
#define RTS5912_GPIO043 &gpioc 11
#define RTS5912_GPIO044 &gpioc 12
#define RTS5912_GPIO045 &gpioc 13
#define RTS5912_GPIO046 &gpioc 14
#define RTS5912_GPIO047 &gpioc 15
#define RTS5912_GPIO048 &gpiod 0
#define RTS5912_GPIO049 &gpiod 1
#define RTS5912_GPIO050 &gpiod 2
#define RTS5912_GPIO051 &gpiod 3
#define RTS5912_GPIO052 &gpiod 4
#define RTS5912_GPIO053 &gpiod 5
#define RTS5912_GPIO055 &gpiod 7
#define RTS5912_GPIO056 &gpiod 8
#define RTS5912_GPIO057 &gpiod 9
#define RTS5912_GPIO058 &gpiod 10
#define RTS5912_GPIO059 &gpiod 11
#define RTS5912_GPIO060 &gpiod 12
#define RTS5912_GPIO061 &gpiod 13
#define RTS5912_GPIO064 &gpioe 0
#define RTS5912_GPIO065 &gpioe 1
#define RTS5912_GPIO066 &gpioe 2
#define RTS5912_GPIO067 &gpioe 3
#define RTS5912_GPIO068 &gpioe 4
#define RTS5912_GPIO069 &gpioe 5
#define RTS5912_GPIO070 &gpioe 6
#define RTS5912_GPIO071 &gpioe 7
#define RTS5912_GPIO074 &gpioe 10
#define RTS5912_GPIO075 &gpioe 11
#define RTS5912_GPIO076 &gpioe 12
#define RTS5912_GPIO077 &gpioe 13
#define RTS5912_GPIO078 &gpioe 14
#define RTS5912_GPIO079 &gpioe 15
#define RTS5912_GPIO080 &gpiof 0
#define RTS5912_GPIO081 &gpiof 1
#define RTS5912_GPIO083 &gpiof 3
#define RTS5912_GPIO084 &gpiof 4
#define RTS5912_GPIO085 &gpiof 5
#define RTS5912_GPIO086 &gpiof 6
#define RTS5912_GPIO087 &gpiof 7
#define RTS5912_GPIO088 &gpiof 8
#define RTS5912_GPIO089 &gpiof 9
#define RTS5912_GPIO090 &gpiof 10
#define RTS5912_GPIO091 &gpiof 11
#define RTS5912_GPIO092 &gpiof 12
#define RTS5912_GPIO093 &gpiof 13
#define RTS5912_GPIO094 &gpiof 14
#define RTS5912_GPIO095 &gpiof 15
#define RTS5912_GPIO096 &gpiog 0
#define RTS5912_GPIO097 &gpiog 1
#define RTS5912_GPIO099 &gpiog 3
#define RTS5912_GPIO100 &gpiog 4
#define RTS5912_GPIO101 &gpiog 5
#define RTS5912_GPIO102 &gpiog 6
#define RTS5912_GPIO103 &gpiog 7
#define RTS5912_GPIO104 &gpiog 8
#define RTS5912_GPIO105 &gpiog 9
#define RTS5912_GPIO106 &gpiog 10
#define RTS5912_GPIO107 &gpiog 11
#define RTS5912_GPIO108 &gpiog 12
#define RTS5912_GPIO109 &gpiog 13
#define RTS5912_GPIO111 &gpiog 15
#define RTS5912_GPIO112 &gpioh 0
#define RTS5912_GPIO113 &gpioh 1
#define RTS5912_GPIO114 &gpioh 2
#define RTS5912_GPIO115 &gpioh 3
#define RTS5912_GPIO117 &gpioh 5
#define RTS5912_GPIO118 &gpioh 6
#define RTS5912_GPIO119 &gpioh 7
#define RTS5912_GPIO120 &gpioh 8
#define RTS5912_GPIO121 &gpioh 9
#define RTS5912_GPIO122 &gpioh 10
#define RTS5912_GPIO123 &gpioh 11
#define RTS5912_GPIO124 &gpioh 12
#define RTS5912_GPIO125 &gpioh 13
#define RTS5912_GPIO126 &gpioh 14
#define RTS5912_GPIO127 &gpioh 15
#define RTS5912_GPIO128 &gpioi 0
#define RTS5912_GPIO130 &gpioi 2
#define RTS5912_GPIO131 &gpioi 3


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_REALTEK_GPIO_H_ */
```

## 159.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

版权（Copyright）：© 2024 Realtek Semiconductor Corporation, SIBG-SD7。

作者（Author）：Lin Yu-Cheng <lin_yu_cheng@realtek.com>。

### 注释 2：原第 166 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_REALTEK_GPIO_H_`。

## 159.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/realtek-gpio_8h.html)

---

[上一章](P158_ra_pwm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P160_renesas-ra-gpio-ioport.h_源码浏览.md)
