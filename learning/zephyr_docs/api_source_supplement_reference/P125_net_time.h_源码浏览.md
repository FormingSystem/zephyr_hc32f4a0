---
id: learning.zephyr-docs.api-source-supplement-reference.page-125
title: net_time.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_net\_time.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h.html)。

## 125.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="aclock_8h_html"></a>
<a id="agroup__net__time_html_gaf1da332e3909fca30de991cc2f950e56"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>

```c
/*
 * Copyright (c) 2023 Zephyr Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_NET_TIME_H_
#define ZEPHYR_INCLUDE_NET_NET_TIME_H_

/* Include required for NSEC_PER_* constants. */
#include <zephyr/sys/clock.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef int64_t net_time_t;

#define NET_TIME_MAX INT64_MAX

#define NET_TIME_MIN INT64_MIN

#define NET_TIME_SEC_MAX (NET_TIME_MAX / NSEC_PER_SEC)

#define NET_TIME_SEC_MIN (NET_TIME_MIN / NSEC_PER_SEC)

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_NET_TIME_H_ */
```

## 125.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Zephyr Project。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

为使用 `NSEC_PER_*` 常量而必需的包含项。

### 注释 3：原第 125 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_TIME_H_`。

## 125.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h.html)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)

---

[上一章](P124_net_log.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P126_nordic-nrf-ficr-nrf54h20.h_源码浏览.md)
