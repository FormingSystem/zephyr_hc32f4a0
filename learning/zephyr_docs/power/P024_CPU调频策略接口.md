---
id: learning.zephyr-docs.power.cpufreqapi-1
title: CPU调频策略接口
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq__policy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第24章\_CPU调频策略接口

原文：[group__subsys__cpu__freq__policy](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq__policy.html)。读取日期：2026-10-13，`latest`。

本页给出中央处理器（Central Processing Unit，CPU）调频策略（Frequency Scaling Policy）的应用程序编程接口（Application Programming Interface，API）。自 Zephyr 4.3 提供，接口版本为 0.8.0，使用头文件 `zephyr/cpu_freq/policy.h`。下列函数由 Kconfig 选定的策略实现。

## 24.1\_选择下一个性能状态

```c
int cpu_freq_policy_select_pstate(const struct pstate **pstate_out);
```

获取策略选定的下一个性能状态（Performance State，P-state）。`pstate_out` 是输出参数，通过它返回指向性能状态结构的指针。成功返回 `0`，失败返回非零值。

调用者必须保证当前 CPU 不变。从中断服务程序（Interrupt Service Routine，ISR）调用，或在单 CPU 系统中调用时，该限制自然成立。从对称多处理（Symmetric Multiprocessing，SMP）系统的线程调用时，必须禁用中断或调度器，以保证当前 CPU 不变。

## 24.2\_重置策略数据

```c
void cpu_freq_policy_reset(void);
```

重置策略所需的数据结构。CPU 调频子系统自动调用本函数，应用代码不应直接调用。

## 24.3\_按策略应用性能状态

```c
const struct pstate *cpu_freq_policy_pstate_set(const struct pstate *state);
```

接收此前调用 [`cpu_freq_policy_select_pstate()`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq__policy.html#ga0ad945b87d8577d6a004d6fc3a17451a) 得到的性能状态，并尝试按策略应用它。策略可以应用所选状态、改用其他状态，或者完全忽略请求。

[`state`](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90) 指向一个性能状态。函数返回指向已应用状态的指针；没有应用任何状态时返回 `NULL`。

本函数由 CPU 调频子系统自动调用，应用代码不应直接调用。相关头文件见[CPU调频策略头文件](P028_CPU调频策略头文件.md)。

---

[上一章：CPU调频接口](P023_CPU调频接口.md) · [下一章：性能状态接口](P025_性能状态接口.md) · [返回大纲](大纲.md)
