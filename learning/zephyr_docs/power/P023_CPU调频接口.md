---
id: learning.zephyr-docs.power.cpufreqapi-0
title: CPU调频接口
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第23章\_CPU调频接口

原文：[group__subsys__cpu__freq](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__cpu__freq.html)。读取日期：2026-10-13，`latest`。

本页给出中央处理器（Central Processing Unit，CPU）动态调频（Dynamic Frequency Scaling）应用程序编程接口（Application Programming Interface，API）。自 Zephyr 4.3 提供，接口版本为 0.8.0。主头文件是 `zephyr/cpu_freq/cpu_freq.h`。

## 23.1\_接口分组

- [CPU调频策略接口](P024_CPU调频策略接口.md)：调频策略（Policy）。
- [性能状态接口](P025_性能状态接口.md)：性能状态（Performance State，P-state）。
- [CPU调频头文件](P027_CPU调频头文件.md)：主头文件声明。

## 23.2\_请求设置性能状态

```c
int cpu_freq_pstate_set(const struct pstate *state);
```

请求处理器设置给定的性能状态，由片上系统（System on Chip，SoC）实现。该接口封装改变当前 CPU 性能状态所需的硬件与 SoC 专用调用。

参数 [`state`](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90) 是指向[性能状态结构](P026_性能状态结构.md)的指针。请求被成功接收时返回 `0`，失败返回负错误码 `-errno`。

调用者必须保证执行过程中当前 CPU 不变。从中断服务程序（Interrupt Service Routine，ISR）调用，或在单 CPU 系统上调用时，自然满足这一限制。在对称多处理（Symmetric Multiprocessing，SMP）系统的线程中调用时，必须禁用中断或调度器，以确保当前 CPU 不会改变。

**接口不保证性能状态立即生效，甚至不保证最终一定被设置。**返回成功表示请求接收成功。

---

[上一章：CPU调频温度上限示例](P022_CPU调频温度上限示例.md) · [下一章：CPU调频策略接口](P024_CPU调频策略接口.md) · [返回大纲](大纲.md)
