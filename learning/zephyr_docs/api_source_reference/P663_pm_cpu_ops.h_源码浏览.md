---
id: learning.zephyr-docs.api-source-reference.page-663
title: pm_cpu_ops.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pm__cpu__ops_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第663章\_pm\_cpu\_ops.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pm__cpu__ops_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P064_CPU电源操作头文件.md)。

## 663.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00036"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__power__management__cpu__api_html_ga65dfe4b0c47af092c50c0022227ac8eb"></a>
<a id="agroup__power__management__cpu__api_html_ga68c37acfc53eee990c34398ca0f1a3f5"></a>
<a id="agroup__power__management__cpu__api_html_gaa6de91e837b262f432b4a80ef5e2b781"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>

```c
/*
 * Copyright 2021 Carlo Caione <ccaione@baylibre.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_PM_CPU_OPS_H_
#define ZEPHYR_INCLUDE_DRIVERS_PM_CPU_OPS_H_


#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

#define SYS_WARM_RESET 0

#define SYS_COLD_RESET 1

int pm_cpu_off(void);

int pm_cpu_on(unsigned long cpuid, uintptr_t entry_point);

int pm_system_reset(unsigned char reset);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_PM_CPU_OPS_H_ */
```

## 663.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2021 Carlo Caione <ccaione@baylibre.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 82 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PM_CPU_OPS_H_`。

## 663.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P064_CPU电源操作头文件.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [pm_cpu_off](https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html#gaa6de91e837b262f432b4a80ef5e2b781)
- [pm_cpu_on](https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html#ga68c37acfc53eee990c34398ca0f1a3f5)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [pm_system_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__power__management__cpu__api.html#ga65dfe4b0c47af092c50c0022227ac8eb)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P662_pm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P664_pmu.h_源码浏览.md)
