---
id: learning.zephyr-docs.timer_reference.rtcext-21
title: MCUXSNVS实时时钟扩展源码
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcux__snvs__rtc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第21章\_MCUXSNVS实时时钟扩展源码

原文：[mcux__snvs__rtc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/mcux__snvs__rtc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保存官方源码浏览页的全部可见代码、版权和许可，仅移除网页行号及行尾空白。中文接口说明见[参考页](P020_MCUXSNVS实时时钟扩展参考.md)。

## 21.1\_完整可见源码

原代码、类型和条件编译均保持原样。

```c
/*
 * Copyright (c) 2021 Basalte bv
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_RTC_MCUX_SNVS_H_
#define ZEPHYR_INCLUDE_DRIVERS_RTC_MCUX_SNVS_H_

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

int mcux_snvs_rtc_set(const struct device *dev, uint32_t ticks);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_RTC_MCUX_SNVS_H_ */
```

## 21.2\_阅读说明

原页只有设备包含项、设置计数值的函数声明和C++条件包装，没有函数实现。参数`ticks`保持`uint32_t`类型；成功返回非负值（Non-negative）的约定见前一章。

---

[上一章：MCUXSNVS实时时钟扩展参考](P020_MCUXSNVS实时时钟扩展参考.md) · [下一章：计数器公共接口](P022_计数器公共接口.md) · [返回大纲](大纲.md)
