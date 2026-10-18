---
id: learning.zephyr-docs.api-source-reference.page-321
title: hooks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第321章\_hooks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html)。

## 321.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="ahooks_8h_html_a5ee95ec1991b2083210194fe485b3a02"></a>
<a id="ahooks_8h_html_a684e5461ecf7657b5ab646cdb9e41a51"></a>
<a id="ahooks_8h_html_ad3d12da84a31f3d4db5621635f5df687"></a>
<a id="ahooks_8h_html_ad6e8df1eefd1add03ad8379802bd989e"></a>
<a id="ahooks_8h_html_ad8a7ba989faae8d2f35ddbad9f5b4233"></a>
<a id="ahooks_8h_html_adc333ec5f401d3d8311a496736bd1aa4"></a>
<a id="ahooks_8h_html_adc6098773fbea0f7ba1575f4a47649b1"></a>
<a id="ahooks_8h_html_aed3aa074849066c29086ea37f8f9ef8a"></a>

```c
/*
 * Copyright (c) 2024 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_PLATFORM_HOOKS_H_
#define ZEPHYR_INCLUDE_PLATFORM_HOOKS_H_


#if defined(CONFIG_SOC_EARLY_RESET_HOOK) || defined(__DOXYGEN__)
void soc_early_reset_hook(void);
#else
#define soc_early_reset_hook() do { } while (0)
#endif

#if defined(CONFIG_SOC_RESET_HOOK) || defined(__DOXYGEN__)
void soc_reset_hook(void);
#else
#define soc_reset_hook() do { } while (0)
#endif

#if defined(CONFIG_SOC_PREP_HOOK) || defined(__DOXYGEN__)
void soc_prep_hook(void);
#else
#define soc_prep_hook() do { } while (0)
#endif

#if defined(CONFIG_SOC_EARLY_INIT_HOOK) || defined(__DOXYGEN__)
void soc_early_init_hook(void);
#else
#define soc_early_init_hook() do { } while (0)
#endif

#if defined(CONFIG_SOC_LATE_INIT_HOOK) || defined(__DOXYGEN__)
void soc_late_init_hook(void);
#else
#define soc_late_init_hook() do { } while (0)
#endif

#if defined(CONFIG_SOC_PER_CORE_INIT_HOOK) || defined(__DOXYGEN__)
void soc_per_core_init_hook(void);
#else
#define soc_per_core_init_hook() do { } while (0)
#endif

#if defined(CONFIG_BOARD_EARLY_INIT_HOOK) || defined(__DOXYGEN__)
void board_early_init_hook(void);
#else
#define board_early_init_hook() do { } while (0)
#endif

#if defined(CONFIG_BOARD_LATE_INIT_HOOK) || defined(__DOXYGEN__)
void board_late_init_hook(void);
#else
#define board_late_init_hook() do { } while (0)
#endif

#endif /* ZEPHYR_INCLUDE_PLATFORM_HOOKS_H_ */
```

## 321.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 122 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PLATFORM_HOOKS_H_`。

## 321.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html)
- [soc_early_reset_hook](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html#ad8a7ba989faae8d2f35ddbad9f5b4233)
- [soc_reset_hook](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html#ad6e8df1eefd1add03ad8379802bd989e)
- [soc_prep_hook](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html#adc333ec5f401d3d8311a496736bd1aa4)
- [soc_early_init_hook](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html#a5ee95ec1991b2083210194fe485b3a02)
- [soc_late_init_hook](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html#ad3d12da84a31f3d4db5621635f5df687)
- [soc_per_core_init_hook](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html#aed3aa074849066c29086ea37f8f9ef8a)
- [board_early_init_hook](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html#a684e5461ecf7657b5ab646cdb9e41a51)
- [board_late_init_hook](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html#adc6098773fbea0f7ba1575f4a47649b1)

---

[上一章](P320_histogram.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P322_hostname.h_源码浏览.md)
