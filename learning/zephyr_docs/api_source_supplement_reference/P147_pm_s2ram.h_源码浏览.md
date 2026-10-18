---
id: learning.zephyr-docs.api-source-supplement-reference.page-147
title: pm_s2ram.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pm__s2ram_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第147章\_pm\_s2ram.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pm__s2ram_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P065_挂起到RAM头文件.md)。

## 147.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="agroup__pm__s2ram_html_ga61b569a4b9053443c9b82b0ea1bfae53"></a>
<a id="agroup__pm__s2ram_html_ga6b82cf263c595b0d5cb353759000615c"></a>
<a id="agroup__pm__s2ram_html_ga88bb5cb4d2eb2c6014f0bad0e891ae1f"></a>
<a id="agroup__pm__s2ram_html_ga93f351a7dafa34ccdffd7e97763ab34b"></a>

```c
/*
 * Copyright (c) 2022, Carlo Caione <ccaione@baylibre.com>
 */


#ifndef ZEPHYR_INCLUDE_ARCH_COMMON_PM_S2RAM_H_
#define ZEPHYR_INCLUDE_ARCH_COMMON_PM_S2RAM_H_

#ifdef _ASMLANGUAGE
GTEXT(arch_pm_s2ram_suspend);
#else

#ifdef __cplusplus
extern "C" {
#endif

typedef int (*pm_s2ram_system_off_fn_t)(void);

int arch_pm_s2ram_suspend(pm_s2ram_system_off_fn_t system_off);

void pm_s2ram_mark_set(void);

bool pm_s2ram_mark_check_and_clear(void);

#ifdef __cplusplus
}
#endif

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_ARCH_COMMON_PM_S2RAM_H_ */
```

## 147.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022, Carlo Caione <ccaione@baylibre.com>。

### 注释 2：原第 92 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 3：原第 94 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_COMMON_PM_S2RAM_H_`。

## 147.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P065_挂起到RAM头文件.md)
- [arch_pm_s2ram_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html#ga6b82cf263c595b0d5cb353759000615c)
- [pm_s2ram_system_off_fn_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html#ga61b569a4b9053443c9b82b0ea1bfae53)
- [pm_s2ram_mark_set](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html#ga88bb5cb4d2eb2c6014f0bad0e891ae1f)
- [pm_s2ram_mark_check_and_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__pm__s2ram.html#ga93f351a7dafa34ccdffd7e97763ab34b)

---

[上一章](P146_policy.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P148_psci.h_源码浏览.md)
