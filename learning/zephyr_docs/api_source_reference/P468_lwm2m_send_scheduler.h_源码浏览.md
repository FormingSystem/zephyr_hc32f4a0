---
id: learning.zephyr-docs.api-source-reference.page-468
title: lwm2m_send_scheduler.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第468章\_lwm2m\_send\_scheduler.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h.html)。

## 468.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="alwm2m_8h_html"></a>
<a id="alwm2m__send__scheduler_8h_html_a896f3773c77143e90858bdeab8ba326a"></a>
<a id="alwm2m__send__scheduler_8h_html_acc3495441c7fb3391211a360d0602431"></a>
<a id="alwm2m__send__scheduler_8h_html_ae71df037474bca27032fd7d395f84f04"></a>
<a id="astdbool_8h_html"></a>
<a id="astructlwm2m__obj__path_html"></a>
<a id="astructlwm2m__time__series__elem_html"></a>

```c
/*
 * Copyright (c) 2025 Clunky Machines
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_LWM2M_SEND_SCHEDULER_H_
#define ZEPHYR_INCLUDE_NET_LWM2M_SEND_SCHEDULER_H_

#include <stdbool.h>
#include <zephyr/net/lwm2m.h>

int lwm2m_send_sched_init(void);

bool lwm2m_send_sched_cache_filter(const struct lwm2m_obj_path *path,
                                   const struct lwm2m_time_series_elem *element);

void lwm2m_send_sched_handle_registration_event(void);

#endif /* ZEPHYR_INCLUDE_NET_LWM2M_SEND_SCHEDULER_H_ */
```

## 468.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Clunky Machines。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_LWM2M_SEND_SCHEDULER_H_`。

## 468.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/net/lwm2m.h](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h.html)
- [lwm2m_send_sched_init](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h.html#ae71df037474bca27032fd7d395f84f04)
- [lwm2m_send_sched_cache_filter](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h.html#acc3495441c7fb3391211a360d0602431)
- [lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)
- [lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)
- [lwm2m_send_sched_handle_registration_event](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h.html#a896f3773c77143e90858bdeab8ba326a)
- [lwm2m.h](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h.html)

---

[上一章](P467_lvgl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P469_m2-memory-connector.h_源码浏览.md)
