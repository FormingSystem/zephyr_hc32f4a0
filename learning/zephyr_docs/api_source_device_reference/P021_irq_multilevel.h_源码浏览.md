---
id: learning.zephyr-docs.api-source-device-reference.page-21
title: irq_multilevel.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_irq\_multilevel.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html)。

## 21.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00062"></a>
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
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="foldopen00186"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="foldopen00200"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="foldopen00226"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="foldopen00252"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="foldopen00306"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="airq__multilevel_8h_html_a07a9a77e0d09a05f81d73da2d3f3388a"></a>
<a id="airq__multilevel_8h_html_a1aa1eaa367e7c8baa250900de4eb0daf"></a>
<a id="airq__multilevel_8h_html_a3b8df71a84ac972b89eb37684dcc7072"></a>
<a id="airq__multilevel_8h_html_a401e5249731398fdec30f8e51437f2fb"></a>
<a id="airq__multilevel_8h_html_a4022e57572b3bffb694bf25eef090cec"></a>
<a id="airq__multilevel_8h_html_a45afd68784e71521606e489d965b1c13"></a>
<a id="airq__multilevel_8h_html_a4b5e1b801ea817b0432a5c5e74f6bff7"></a>
<a id="airq__multilevel_8h_html_a79eb4433215c271fa61b9352855f93ca"></a>
<a id="airq__multilevel_8h_html_a8f22ab28ed1da7312fcd716eea59e400"></a>
<a id="airq__multilevel_8h_html_a9a94c2cecb8c8d3394c1ff5ed3cc4db3"></a>
<a id="airq__multilevel_8h_html_a9fb52147e972ee981050b47758dca73d"></a>
<a id="airq__multilevel_8h_html_ab1a4c5a542e4ad472dba609829c34bc4"></a>
<a id="airq__multilevel_8h_html_ae11c8cb9a832a5a8f514a52a12f133c4"></a>
<a id="airq__multilevel_8h_html_ae91094e0be680803d7bd79739029e390"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Meta
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IRQ_MULTILEVEL_H_
#define ZEPHYR_INCLUDE_IRQ_MULTILEVEL_H_

#ifndef _ASMLANGUAGE
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/util.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_MULTI_LEVEL_INTERRUPTS) || defined(__DOXYGEN__)

#if defined(CONFIG_2ND_LEVEL_INTERRUPTS)
BUILD_ASSERT(CONFIG_2ND_LEVEL_INTERRUPT_BITS > 0,
             "Second-level IRQ field must contain at least one bit");
#endif

#if defined(CONFIG_3RD_LEVEL_INTERRUPTS)
BUILD_ASSERT(CONFIG_3RD_LEVEL_INTERRUPT_BITS > 0,
             "Third-level IRQ field must contain at least one bit");
BUILD_ASSERT(CONFIG_1ST_LEVEL_INTERRUPT_BITS + CONFIG_2ND_LEVEL_INTERRUPT_BITS +
                             CONFIG_3RD_LEVEL_INTERRUPT_BITS <=
                     32,
             "Multilevel IRQ encoding exceeds 32 bits");
#elif defined(CONFIG_2ND_LEVEL_INTERRUPTS)
BUILD_ASSERT(CONFIG_1ST_LEVEL_INTERRUPT_BITS + CONFIG_2ND_LEVEL_INTERRUPT_BITS <= 32,
             "Multilevel IRQ encoding exceeds 32 bits");
#endif

/* Masks for fields in the numeric multilevel IRQ encoding. */
#define Z_IRQ_L1_MASK ((uint32_t)GENMASK(CONFIG_1ST_LEVEL_INTERRUPT_BITS - 1, 0))
#define Z_IRQ_L2_MASK                                                                              \
        ((uint32_t)GENMASK(CONFIG_1ST_LEVEL_INTERRUPT_BITS + CONFIG_2ND_LEVEL_INTERRUPT_BITS - 1,  \
                           CONFIG_1ST_LEVEL_INTERRUPT_BITS))
#if defined(CONFIG_3RD_LEVEL_INTERRUPTS) || defined(__DOXYGEN__)
#define Z_IRQ_L3_MASK                                                                              \
        ((uint32_t)GENMASK(CONFIG_1ST_LEVEL_INTERRUPT_BITS + CONFIG_2ND_LEVEL_INTERRUPT_BITS +     \
                                   CONFIG_3RD_LEVEL_INTERRUPT_BITS - 1,                            \
                           CONFIG_1ST_LEVEL_INTERRUPT_BITS + CONFIG_2ND_LEVEL_INTERRUPT_BITS))
#endif /* CONFIG_3RD_LEVEL_INTERRUPTS */

static inline unsigned int irq_get_level(unsigned int irq)
{
#ifdef CONFIG_3RD_LEVEL_INTERRUPTS
        if ((irq & Z_IRQ_L3_MASK) != 0U) {
                return 3;
        }
#endif /* CONFIG_3RD_LEVEL_INTERRUPTS */

        if ((irq & Z_IRQ_L2_MASK) != 0U) {
                return 2;
        }

        return 1;
}

static inline unsigned int irq_from_level_2(unsigned int irq)
{
        return FIELD_GET(Z_IRQ_L2_MASK, irq) - 1U;
}

#define IRQ_TO_L2(irq) FIELD_PREP(Z_IRQ_L2_MASK, (irq) + 1U)

static inline unsigned int irq_to_level_2(unsigned int irq)
{
        return IRQ_TO_L2(irq);
}

static inline unsigned int irq_parent_level_2(unsigned int irq)
{
        return FIELD_GET(Z_IRQ_L1_MASK, irq);
}

#if defined(CONFIG_3RD_LEVEL_INTERRUPTS) || defined(__DOXYGEN__)
static inline unsigned int irq_from_level_3(unsigned int irq)
{
        return FIELD_GET(Z_IRQ_L3_MASK, irq) - 1U;
}

#define IRQ_TO_L3(irq) FIELD_PREP(Z_IRQ_L3_MASK, (irq) + 1U)

static inline unsigned int irq_to_level_3(unsigned int irq)
{
        return IRQ_TO_L3(irq);
}

static inline unsigned int irq_parent_level_3(unsigned int irq)
{
        return irq_from_level_2(irq);
}
#endif /* CONFIG_3RD_LEVEL_INTERRUPTS */

static inline unsigned int irq_from_level(unsigned int irq, unsigned int level)
{
        if (level == 1) {
                return irq;
        } else if (level == 2) {
                return irq_from_level_2(irq);
        }
#ifdef CONFIG_3RD_LEVEL_INTERRUPTS
        else if (level == 3) {
                return irq_from_level_3(irq);
        }
#endif /* CONFIG_3RD_LEVEL_INTERRUPTS */

        /* level is higher than what's supported */
        __ASSERT_NO_MSG(false);
        return irq;
}

static inline unsigned int irq_to_level(unsigned int irq, unsigned int level)
{
        if (level == 1) {
                return irq;
        } else if (level == 2) {
                return irq_to_level_2(irq);
        }
#ifdef CONFIG_3RD_LEVEL_INTERRUPTS
        else if (level == 3) {
                return irq_to_level_3(irq);
        }
#endif /* CONFIG_3RD_LEVEL_INTERRUPTS */

        /* level is higher than what's supported */
        __ASSERT_NO_MSG(false);
        return irq;
}

static inline unsigned int irq_parent_level(unsigned int irq, unsigned int level)
{
        if (level == 1) {
                /* doesn't really make sense, but return anyway */
                return irq;
        } else if (level == 2) {
                return irq_parent_level_2(irq);
        }
#ifdef CONFIG_3RD_LEVEL_INTERRUPTS
        else if (level == 3) {
                return irq_parent_level_3(irq);
        }
#endif /* CONFIG_3RD_LEVEL_INTERRUPTS */

        /* level is higher than what's supported */
        __ASSERT_NO_MSG(false);
        return irq;
}

static inline unsigned int irq_get_intc_irq(unsigned int irq)
{
        const unsigned int level = irq_get_level(irq);

#ifdef CONFIG_3RD_LEVEL_INTERRUPTS
        __ASSERT_NO_MSG(level <= 3);
        if (level == 3) {
                return irq & (Z_IRQ_L1_MASK | Z_IRQ_L2_MASK);
        }
#else
        __ASSERT_NO_MSG(level <= 2);
#endif /* CONFIG_3RD_LEVEL_INTERRUPTS */

        if (level == 2) {
                return irq_parent_level_2(irq);
        }

        return irq;
}

static inline unsigned int irq_increment(unsigned int irq, unsigned int val)
{
        unsigned int mask;
        const unsigned int level = irq_get_level(irq);

        if (false) {
                /* so that it evaluates the next condition */
#ifdef CONFIG_3RD_LEVEL_INTERRUPTS
        } else if (level == 3) {
                mask = Z_IRQ_L3_MASK;
#endif /* CONFIG_3RD_LEVEL_INTERRUPTS */
        } else if (level == 2) {
                mask = Z_IRQ_L2_MASK;
        } else {
                mask = Z_IRQ_L1_MASK;
        }

        return (irq & ~mask) | FIELD_PREP(mask, FIELD_GET(mask, irq) + val);
}

#endif /* CONFIG_MULTI_LEVEL_INTERRUPTS */
#ifdef __cplusplus
}
#endif

#endif /* _ASMLANGUAGE */
#endif /* ZEPHYR_INCLUDE_IRQ_MULTILEVEL_H_ */
```

## 21.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Meta。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

数值形式多级中断请求编码（Numeric Multilevel IRQ Encoding）中各字段的掩码（Masks）。

### 注释 3：原第 52 行

条件编译配置（Configuration）标记：`CONFIG_3RD_LEVEL_INTERRUPTS`。

### 注释 4：原第 68 行

条件编译配置（Configuration）标记：`CONFIG_3RD_LEVEL_INTERRUPTS`。

### 注释 5：原第 190 行

条件编译配置（Configuration）标记：`CONFIG_3RD_LEVEL_INTERRUPTS`。

### 注释 6：原第 211 行

条件编译配置（Configuration）标记：`CONFIG_3RD_LEVEL_INTERRUPTS`。

### 注释 7：原第 213 行

级别（Level）高于支持的范围。

### 注释 8：原第 237 行

条件编译配置（Configuration）标记：`CONFIG_3RD_LEVEL_INTERRUPTS`。

### 注释 9：原第 239 行

级别（Level）高于支持的范围。

### 注释 10：原第 255 行

虽然没有实际意义，仍然返回（Return）。

### 注释 11：原第 264 行

条件编译配置（Configuration）标记：`CONFIG_3RD_LEVEL_INTERRUPTS`。

### 注释 12：原第 266 行

级别（Level）高于支持的范围。

### 注释 13：原第 289 行

条件编译配置（Configuration）标记：`CONFIG_3RD_LEVEL_INTERRUPTS`。

### 注释 14：原第 312 行

使其继续求值下一个条件（Condition）。

### 注释 15：原第 316 行

条件编译配置（Configuration）标记：`CONFIG_3RD_LEVEL_INTERRUPTS`。

### 注释 16：原第 326 行

条件编译配置（Configuration）标记：`CONFIG_MULTI_LEVEL_INTERRUPTS`。

### 注释 17：原第 331 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 18：原第 332 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_IRQ_MULTILEVEL_H_`。

## 21.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [irq_get_level](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a45afd68784e71521606e489d965b1c13)
- [irq_from_level_2](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a4022e57572b3bffb694bf25eef090cec)
- [FIELD_GET](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa49a456f06f7bdbedfcf3517e461947e)
- [irq_to_level_2](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a79eb4433215c271fa61b9352855f93ca)
- [IRQ_TO_L2](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)
- [irq_parent_level_2](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#ab1a4c5a542e4ad472dba609829c34bc4)
- [irq_from_level_3](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a401e5249731398fdec30f8e51437f2fb)
- [irq_to_level_3](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a3b8df71a84ac972b89eb37684dcc7072)
- [IRQ_TO_L3](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a1aa1eaa367e7c8baa250900de4eb0daf)
- [irq_parent_level_3](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#ae11c8cb9a832a5a8f514a52a12f133c4)
- [irq_from_level](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a07a9a77e0d09a05f81d73da2d3f3388a)
- [irq_to_level](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#ae91094e0be680803d7bd79739029e390)
- [irq_parent_level](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a8f22ab28ed1da7312fcd716eea59e400)
- [irq_get_intc_irq](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a9fb52147e972ee981050b47758dca73d)
- [irq_increment](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html#a4b5e1b801ea817b0432a5c5e74f6bff7)
- [FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P020_hci_vs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P022_lorem_ipsum.h_源码浏览.md)
