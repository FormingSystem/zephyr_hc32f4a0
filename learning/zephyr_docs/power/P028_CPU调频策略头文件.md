---
id: learning.zephyr-docs.power.cpufreqapi-5
title: CPU调频策略头文件
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cpu__freq_2policy_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第28章\_CPU调频策略头文件

原文：[cpu__freq_2policy_8h](https://docs.zephyrproject.org/latest/doxygen/html/cpu__freq_2policy_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/cpu_freq/policy.h` 是中央处理器（Central Processing Unit，CPU）调频策略（Frequency Scaling Policy）的头文件。

## 28.1\_包含关系

```c
#include <zephyr/types.h>
#include <zephyr/cpu_freq/pstate.h>
```

[查看官方头文件源码](https://docs.zephyrproject.org/latest/doxygen/html/cpu__freq_2policy_8h_source.html)。

## 28.2\_函数声明

```c
int cpu_freq_policy_select_pstate(const struct pstate **pstate_out);
void cpu_freq_policy_reset(void);
const struct pstate *cpu_freq_policy_pstate_set(const struct pstate *state);
```

| 函数 | 用途 |
| --- | --- |
| [`cpu_freq_policy_select_pstate()`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq__policy.html#ga0ad945b87d8577d6a004d6fc3a17451a) | 从调频策略取得下一个性能状态（Performance State，P-state） |
| [`cpu_freq_policy_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq__policy.html#gab1cbd1fc42786f84cd8d6dbe28abfb55) | 重置策略使用的数据结构 |
| [`cpu_freq_policy_pstate_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq__policy.html#ga506a85924a8c49805b476f694df7117d) | 按策略设置调频性能状态 |

参数、返回值及子系统自动调用约束见[CPU调频策略接口](P024_CPU调频策略接口.md)。

---

[上一章：CPU调频头文件](P027_CPU调频头文件.md) · [下一章：性能状态头文件](P029_性能状态头文件.md) · [返回大纲](大纲.md)
