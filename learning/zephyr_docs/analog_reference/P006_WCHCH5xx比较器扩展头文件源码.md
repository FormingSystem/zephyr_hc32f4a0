---
id: learning.zephyr-docs.analog_reference.analogheader-6
title: WCHCH5xx比较器扩展头文件源码
kind: reference
status: maintained
domains: [zephyr, analog_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/comparator__wch__ch5xx_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第6章\_WCHCH5xx比较器扩展头文件源码

原文：[comparator__wch__ch5xx_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/comparator__wch__ch5xx_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览页的全部可见代码、版权和许可，仅去除网页行号与行尾空白。接口的中文解释见[参考页](P005_WCHCH5xx比较器扩展头文件参考.md)。

## 6.1\_完整可见源码

原代码中的条件编译、类型、赋值和函数声明均按原样保留。

```c
/*
 * SPDX-FileCopyrightText: 2026 SMILE (smile.eu)
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_COMPARATOR_WCH_CH5XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_COMPARATOR_WCH_CH5XX_H_

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

enum comp_nref_level {
        COMP_NREF_LEVEL_50 = 0,
        COMP_NREF_LEVEL_100,
        COMP_NREF_LEVEL_150,
        COMP_NREF_LEVEL_200,
        COMP_NREF_LEVEL_250,
        COMP_NREF_LEVEL_300,
        COMP_NREF_LEVEL_350,
        COMP_NREF_LEVEL_400,
        COMP_NREF_LEVEL_450,
        COMP_NREF_LEVEL_500,
        COMP_NREF_LEVEL_550,
        COMP_NREF_LEVEL_600,
        COMP_NREF_LEVEL_650,
        COMP_NREF_LEVEL_700,
        COMP_NREF_LEVEL_750,
        COMP_NREF_LEVEL_800,
};

int comparator_wch_set_nref_level(const struct device *dev, enum comp_nref_level level);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_COMPARATOR_WCH_CH5XX_H_ */
```

## 6.2\_阅读说明

负端参考电平（Negative Reference Level）枚举的首项`COMP_NREF_LEVEL_50`编码为0，其余按顺序递增。Doxygen源码浏览页未显示各成员的电压注释，其中文含义保存在前一章的完整对照表；这里不把译注插入原代码。

---

[上一章：WCHCH5xx比较器扩展头文件参考](P005_WCHCH5xx比较器扩展头文件参考.md) · [下一章：运算放大器公共头文件参考](P007_运算放大器公共头文件参考.md) · [返回大纲](大纲.md)
