---
id: learning.zephyr-docs.hardware.ztestapi-1
title: ZTest基准测试接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第501章\_ZTest基准测试接口

原文：[group__ztest__benchmark](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html)。读取日期：2026-10-13，`latest`。

**Zephyr 测试框架（Zephyr Testing Framework，ZTest）**提供**基准测试（Benchmark）**接口，按固定迭代次数、固定运行时长或手工标记的测量区间采集结果。接口头文件为 `zephyr/benchmark.h`。

> 译注：原页显示的是官方构建环境中的绝对头文件路径。这里使用公开包含名 `zephyr/benchmark.h`；源码仓库内的位置是 `subsys/testsuite/ztest/include/zephyr/benchmark.h`，无需复制构建机器的路径。

## 501.1\_固定迭代次数的基准测试

[`ZTEST_BENCHMARK`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#gaf5f904c376be7111cfaf1e21a5a99bd4) 定义一个包含准备和清理函数的基准测试。**准备（Setup）**和**清理（Teardown）**分别由 `setup_fn`、`teardown_fn` 参数提供。

<a id="gaf5f904c376be7111cfaf1e21a5a99bd4"></a>

```c
#define ZTEST_BENCHMARK(suite_name, benchmark, samples, setup_fn, teardown_fn)
```

| 参数 | 官方说明译文 |
| --- | --- |
| `suite_name` | 基准测试所属套件的名称 |
| `benchmark` | 基准测试名称 |
| `samples` | 运行该基准测试的迭代次数 |
| `setup_fn` | 基准测试之前运行的函数 |
| `teardown_fn` | 基准测试之后运行的函数 |

原始展开如下。`Z_ZTEST_BENCHMARK_FN`、`Z_ZTEST_BENCHMARK_NODE`、`Z_ZTEST_BENCHMARK_SUITE_NODE` 分别构造测试函数、注册节点和套件节点的名称；[`STRUCT_SECTION_ITERABLE`](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f) 将对象放入可遍历的链接段；`__noinline` 禁止函数内联。`ztest_benchmark` 是普通基准测试的记录结构，保存名称、迭代次数、函数和所属套件。

```c
static __noinline void Z_ZTEST_BENCHMARK_FN(suite_name, benchmark)(void);               \
static const STRUCT_SECTION_ITERABLE(ztest_benchmark,                                   \
                                     Z_ZTEST_BENCHMARK_NODE(suite_name, benchmark)) =   \
{                                                                                       \
        .name = #benchmark,                                                             \
        .iterations = samples,                                                          \
        .setup = setup_fn,                                                              \
        .run = Z_ZTEST_BENCHMARK_FN(suite_name, benchmark),                             \
        .teardown = teardown_fn,                                                        \
        .suite = &Z_ZTEST_BENCHMARK_SUITE_NODE(suite_name),                             \
};                                                                                      \
static __noinline void Z_ZTEST_BENCHMARK_FN(suite_name, benchmark)(void)
```

## 501.2\_手工标记测量区间

[`ZTEST_BENCHMARK_MANUAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#ga417b014ee9999e53bd138de4a92c61ee) 定义**手工采样基准测试（Manually Sampled Benchmark）**。框架和普通基准测试一样，每次迭代执行一次函数体；函数体通过 [`ztest_benchmark_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#ga25c60beeee5d8cec5b0b45cb2eca9601) 与 [`ztest_benchmark_end()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#gaa6ab8cc7668e2ffc23fa978d4194cbac) 自行确定要测量的部分。

<a id="ga417b014ee9999e53bd138de4a92c61ee"></a>

```c
#define ZTEST_BENCHMARK_MANUAL(suite_name, benchmark, samples, setup_fn, teardown_fn)
```

| 参数 | 官方说明译文 |
| --- | --- |
| `suite_name` | 所属套件名称 |
| `benchmark` | 基准测试名称 |
| `samples` | 基准测试迭代次数 |
| `setup_fn` | **每次迭代之前**运行的函数 |
| `teardown_fn` | **每次迭代之后**运行的函数 |

原始展开中的 `ztest_benchmark_manual` 是手工采样记录类型，`Z_ZTEST_BENCHMARK_MANUAL_NODE` 用来构造该记录的节点名称。

```c
static __noinline void Z_ZTEST_BENCHMARK_FN(suite_name, benchmark)(void);               \
static STRUCT_SECTION_ITERABLE(ztest_benchmark_manual,                                  \
                               Z_ZTEST_BENCHMARK_MANUAL_NODE(suite_name, benchmark)) =  \
{                                                                                       \
        .name = #benchmark,                                                             \
        .iterations = samples,                                                          \
        .setup = setup_fn,                                                              \
        .run = Z_ZTEST_BENCHMARK_FN(suite_name, benchmark),                             \
        .teardown = teardown_fn,                                                        \
        .suite = &Z_ZTEST_BENCHMARK_SUITE_NODE(suite_name),                             \
};                                                                                      \
static __noinline void Z_ZTEST_BENCHMARK_FN(suite_name, benchmark)(void)
```

官方示例在测量开始之前调用 `prepare()` 做准备，只测量 `operation_under_test()` 表示的被测操作；这两个名字是示例占位函数。`my_suite`、`my_benchmark` 分别为示例套件名和基准测试名，`NULL` 表示未提供准备/清理函数。

<a id="ga25c60beeee5d8cec5b0b45cb2eca9601"></a>

<a id="gaa6ab8cc7668e2ffc23fa978d4194cbac"></a>

```c
ZTEST_BENCHMARK_MANUAL(my_suite, my_benchmark, 1000, NULL, NULL)
{
        prepare();
        ztest_benchmark_start();
        operation_under_test();
        ztest_benchmark_end();
}
```

这种方式适合测量起止位置不与函数体起止位置重合的区间，框架无法自行给这些区间计时。两个标记函数都可以安全地从**中断服务例程（Interrupt Service Routine，ISR）**调用，因此测量甚至可以跨**执行上下文（Execution Context）**：要测量从中断到被它唤醒的线程的延迟，可以在 ISR 调用 [`ztest_benchmark_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#ga25c60beeee5d8cec5b0b45cb2eca9601)，在被唤醒线程中调用 [`ztest_benchmark_end()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#gaa6ab8cc7668e2ffc23fa978d4194cbac)。

若某次迭代的函数体没有记录任何测量区间，该迭代就不贡献样本。

## 501.3\_定义基准测试套件

[`ZTEST_BENCHMARK_SUITE`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#gae0a805abbadf430418c256dcc03f95b1) 定义一个基准测试**套件（Suite）**，将多个基准测试组织在一起。

<a id="gae0a805abbadf430418c256dcc03f95b1"></a>

```c
#define ZTEST_BENCHMARK_SUITE(suite, setup_fn, teardown_fn)
```

`suite` 为套件名称，`setup_fn` 为套件开始之前执行的函数，`teardown_fn` 为套件结束之后执行的函数。下面展开中的 `ztest_benchmark_suite` 是套件记录类型：

```c
static const STRUCT_SECTION_ITERABLE(ztest_benchmark_suite,                     \
                                     Z_ZTEST_BENCHMARK_SUITE_NODE(suite)) =     \
{                                                                               \
        .name = #suite,                                                         \
        .setup = setup_fn,                                                      \
        .teardown = teardown_fn,                                                \
}
```

## 501.4\_按持续时间运行

[`ZTEST_BENCHMARK_TIMED`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#ga0f1d1daa73aa6db26ac91f9f17a19646) 定义带准备与清理函数的**定时基准测试（Timed Benchmark）**。

<a id="ga0f1d1daa73aa6db26ac91f9f17a19646"></a>

```c
#define ZTEST_BENCHMARK_TIMED(testsuite, benchmark, duration, setup_fn, teardown_fn)
```

| 参数 | 官方说明译文 |
| --- | --- |
| `testsuite` | 基准测试所属套件名称 |
| `benchmark` | 基准测试名称 |
| `duration` | 基准测试运行时长，单位为**毫秒（Millisecond，ms）** |
| `setup_fn` | 基准测试之前运行的函数 |
| `teardown_fn` | 基准测试之后运行的函数 |

展开中的 `ztest_benchmark_timed` 是定时测试记录类型，`Z_ZTEST_BENCHMARK_TIMED_NODE` 构造其节点名称，`duration_ms` 字段保存毫秒时长。

```c
static __noinline void Z_ZTEST_BENCHMARK_FN(testsuite, benchmark)(void);                \
static const STRUCT_SECTION_ITERABLE(ztest_benchmark_timed,                             \
                                Z_ZTEST_BENCHMARK_TIMED_NODE(testsuite, benchmark)) =   \
{                                                                                       \
        .duration_ms = duration,                                                        \
        .name = #benchmark,                                                             \
        .setup = setup_fn,                                                              \
        .run = Z_ZTEST_BENCHMARK_FN(testsuite, benchmark),                              \
        .teardown = teardown_fn,                                                        \
        .suite = &Z_ZTEST_BENCHMARK_SUITE_NODE(testsuite),                              \
};                                                                                      \
static __noinline void Z_ZTEST_BENCHMARK_FN(testsuite, benchmark)(void)
```

## 501.5\_测量区间的开始与结束

[`ztest_benchmark_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#ga25c60beeee5d8cec5b0b45cb2eca9601) 开始手工基准测试当前迭代的测量区间：取得当前**时间戳（Timestamp）**，函数体在此调用之前完成的工作不计入测量。

```c
void ztest_benchmark_start(void);
```

它可以安全地在 ISR 中调用，因为只记录时间戳；起点位于中断上下文的测量区间可直接在那里标记。样本本身等函数体返回后才计算。**在 [`ZTEST_BENCHMARK_MANUAL()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#ga417b014ee9999e53bd138de4a92c61ee) 函数体之外发出的调用会被忽略。**

[`ztest_benchmark_end()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#gaa6ab8cc7668e2ffc23fa978d4194cbac) 结束手工基准测试当前迭代的测量区间，并记录当前时间戳。

```c
void ztest_benchmark_end(void);
```

若此前没有调用 [`ztest_benchmark_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__benchmark.html#ga25c60beeee5d8cec5b0b45cb2eca9601)，就没有可结束的区间，此次调用会被忽略。它也可以安全地在 ISR 中调用：和开始标记一样，只有函数体返回到线程上下文后，测量区间才会交给统计处理。

---

[上一章：FFF测试扩展接口](P500_FFF测试扩展接口.md) · [下一章：ZTest测试框架接口](P502_ZTest测试框架接口.md) · [返回大纲](大纲.md)
