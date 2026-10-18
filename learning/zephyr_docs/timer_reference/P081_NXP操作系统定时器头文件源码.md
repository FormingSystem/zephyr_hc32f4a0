---
id: learning.zephyr-docs.timer_reference.systemtimer-81
title: NXP操作系统定时器头文件源码
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__os__timer_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第81章\_NXP操作系统定时器头文件源码

原文：[nxp__os__timer_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/nxp__os__timer_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保存官方源码浏览页的全部可见代码、版权和许可，仅移除网页行号及行尾空白。中文文件参考见[上一章](P080_NXP操作系统定时器头文件参考.md)。

## 81.1\_完整可见源码

```c
/*
 * Copyright (c) 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_TIMER_NXP_OS_TIMER_H
#define ZEPHYR_INCLUDE_DRIVERS_TIMER_NXP_OS_TIMER_H

#ifdef __cplusplus
extern "C" {
#endif

bool z_nxp_os_timer_ignore_timer_wakeup(void);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_TIMER_NXP_OS_TIMER_H */
```

## 81.2\_源码注释与阅读说明

源码声明`bool z_nxp_os_timer_ignore_timer_wakeup(void);`，无参数，返回布尔值（Boolean）。原页没有给出真／假值的进一步契约，也没有函数实现。头文件保护与C++条件包装按原样保留。

---

[上一章：NXP操作系统定时器头文件参考](P080_NXP操作系统定时器头文件参考.md) · [下一章：系统定时器驱动头文件参考](P082_系统定时器驱动头文件参考.md) · [返回大纲](大纲.md)
