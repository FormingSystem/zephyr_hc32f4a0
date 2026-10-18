---
id: learning.zephyr-docs.api-source-reference.page-411
title: irq_nextlevel.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第411章\_irq\_nextlevel.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h.html)。

## 411.1\_原始可见代码（Source Code）

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
<a id="l00044"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="foldopen00108"></a>
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
<a id="foldopen00130"></a>
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
<a id="airq__nextlevel_8h_html_a335d42cf95c25ab8564475c4b4c3ead9"></a>
<a id="airq__nextlevel_8h_html_a7e0e5fe59eae08878a8f243dd9301633"></a>
<a id="airq__nextlevel_8h_html_aa7178acd1058940b83c7c7500217bc01"></a>
<a id="airq__nextlevel_8h_html_ad694fcad4c3fba0d2794cdc34ddcd1bb"></a>
<a id="airq__nextlevel_8h_html_af41789f946ebb445f4a402009ed2e8bb"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>

```c
/*
 * Copyright (c) 2017 Intel corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IRQ_NEXTLEVEL_H_
#define ZEPHYR_INCLUDE_IRQ_NEXTLEVEL_H_

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_MULTI_LEVEL_INTERRUPTS) || defined(__DOXYGEN__)
typedef void (*irq_next_level_func_t)(const struct device *dev,
                                      unsigned int irq);
typedef unsigned int (*irq_next_level_get_state_t)(const struct device *dev);
typedef void (*irq_next_level_priority_t)(const struct device *dev,
                                          unsigned int irq, unsigned int prio,
                                          uint32_t flags);
typedef int (*irq_next_level_get_line_state_t)(const struct device *dev,
                                               unsigned int irq);

struct irq_next_level_api {
        irq_next_level_func_t intr_enable;
        irq_next_level_func_t intr_disable;
        irq_next_level_get_state_t intr_get_state;
        irq_next_level_priority_t intr_set_priority;
        irq_next_level_get_line_state_t intr_get_line_state;
};

static inline void irq_enable_next_level(const struct device *dev,
                                         uint32_t irq)
{
        const struct irq_next_level_api *api =
                (const struct irq_next_level_api *)dev->api;

        api->intr_enable(dev, irq);
}

static inline void irq_disable_next_level(const struct device *dev,
                                          uint32_t irq)
{
        const struct irq_next_level_api *api =
                (const struct irq_next_level_api *)dev->api;

        api->intr_disable(dev, irq);
}

static inline unsigned int irq_is_enabled_next_level(const struct device *dev)
{
        const struct irq_next_level_api *api =
                (const struct irq_next_level_api *)dev->api;

        return api->intr_get_state(dev);
}

static inline void irq_set_priority_next_level(const struct device *dev,
                                               uint32_t irq,
                                               uint32_t prio, uint32_t flags)
{
        const struct irq_next_level_api *api =
                (const struct irq_next_level_api *)dev->api;

        if (api->intr_set_priority) {
                api->intr_set_priority(dev, irq, prio, flags);
        }
}

static inline unsigned int irq_line_is_enabled_next_level(const struct device *dev,
                                                          unsigned int irq)
{
        const struct irq_next_level_api *api =
                (const struct irq_next_level_api *)dev->api;

        return api->intr_get_line_state(dev, irq);
}

#endif /* CONFIG_MULTI_LEVEL_INTERRUPTS */
#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_IRQ_NEXTLEVEL_H_ */
```

## 411.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Intel corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 139 行

条件编译配置（Configuration）标记：`CONFIG_MULTI_LEVEL_INTERRUPTS`。

### 注释 3：原第 144 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_IRQ_NEXTLEVEL_H_`。

## 411.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [irq_enable_next_level](https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h.html#a335d42cf95c25ab8564475c4b4c3ead9)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [irq_disable_next_level](https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h.html#ad694fcad4c3fba0d2794cdc34ddcd1bb)
- [irq_is_enabled_next_level](https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h.html#aa7178acd1058940b83c7c7500217bc01)
- [irq_set_priority_next_level](https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h.html#af41789f946ebb445f4a402009ed2e8bb)
- [irq_line_is_enabled_next_level](https://docs.zephyrproject.org/latest/doxygen/html/irq__nextlevel_8h.html#a7e0e5fe59eae08878a8f243dd9301633)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

---

[上一章](P410_ipv4_nat.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P412_is31fl3733.h_源码浏览.md)
