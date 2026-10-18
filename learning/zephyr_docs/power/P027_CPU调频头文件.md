---
id: learning.zephyr-docs.power.cpufreqapi-4
title: CPU调频头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cpu__freq_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第27章\_CPU调频头文件

原文：[cpu__freq_8h](https://docs.zephyrproject.org/latest/doxygen/html/cpu__freq_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/cpu_freq/cpu_freq.h` 是中央处理器（Central Processing Unit，CPU）调频应用程序编程接口（Application Programming Interface，API）的主头文件。

## 27.1\_包含关系

```c
#include <zephyr/types.h>
#include <zephyr/cpu_freq/pstate.h>
```

[查看官方头文件源码](https://docs.zephyrproject.org/latest/doxygen/html/cpu__freq_8h_source.html)。

## 27.2\_函数声明

```c
int cpu_freq_pstate_set(const struct pstate *state);
```

请求处理器设置给定的性能状态（Performance State，P-state）。参数、返回值及 CPU 不变约束见[CPU调频接口](P023_CPU调频接口.md)。

---

[上一章：性能状态结构](P026_性能状态结构.md) · [下一章：CPU调频策略头文件](P028_CPU调频策略头文件.md) · [返回大纲](大纲.md)
