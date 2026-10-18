---
id: learning.zephyr-docs.api-source-reference.page-565
title: mpipe_workqueue.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__workqueue_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第565章\_mpipe\_workqueue.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__workqueue_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__workqueue_8h.html)。

## 565.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="agroup__mpipe__workqueue_html_gad175f6e485cce50815afc57ec5c46f55"></a>
<a id="ap4wq_8h_html"></a>
<a id="astructk__p4wq_html"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_WORKQUEUE_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_WORKQUEUE_H_


#include <zephyr/sys/p4wq.h>

extern struct k_p4wq *const mpipe_p4wq;


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_WORKQUEUE_H_ */
```

## 565.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 78 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_WORKQUEUE_H_`。

## 565.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__workqueue_8h.html)
- [zephyr/sys/p4wq.h](../p4_work_reference/P001_P4工作队列头文件参考.md)
- [k_p4wq](../p4_work_reference/P003_P4工作队列结构.md)
- [mpipe_p4wq](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__workqueue.html#gad175f6e485cce50815afc57ec5c46f55)
- [p4wq.h](../p4_work_reference/P001_P4工作队列头文件参考.md)

---

[上一章](P564_mpipe_value.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P566_msg.h_源码浏览.md)
