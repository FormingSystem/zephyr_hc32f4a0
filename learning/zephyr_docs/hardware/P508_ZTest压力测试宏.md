---
id: learning.zephyr-docs.hardware.ztestmac-5
title: ZTest压力测试宏
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第508章\_ZTest压力测试宏

原文：[group__ztest__ztress](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html)。读取日期：2026-10-13，`latest`。

`ztress` 是 **Zephyr 测试框架（Zephyr Testing Framework，ZTest）**中的**压力测试（Stress Testing）**模块。它在不同线程和可选定时器上下文中反复调用用户处理函数，通过随机等待增加执行交错。`ztress` 是模块专用名称，不是需要另行扩写的缩写。

公开头文件为 `zephyr/ztress.h`，仓库内位置为 `subsys/testsuite/ztest/include/zephyr/ztress.h`。原页显示的构建机绝对包含路径在这里改为公开头文件名。

## 508.1\_初始化上下文描述

**执行上下文（Execution Context）**规定处理函数在哪里运行、采用什么优先级及何时完成。[`ztress_context_data`](P517_压力测试上下文结构.md) 是上下文数据结构，原页提供该类型入口；字段类型见结构参考。

[`ZTRESS_CONTEXT_INITIALIZER`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gab5e8bbcecd77db06e7a90631fc0c202b) 初始化上下文结构，进一步含义与线程描述宏相同。

```c
#define ZTRESS_CONTEXT_INITIALIZER(_handler, _user_data, _exec_cnt, _preempt_cnt, _t)
```

| 参数 | 含义 |
| --- | --- |
| `_handler` | 处理函数（Handler） |
| `_user_data` | 传给处理函数的用户数据 |
| `_exec_cnt` | 执行次数限制 |
| `_preempt_cnt` | 被抢占次数限制；抢占（Preemption）指更高优先级上下文打断当前上下文 |
| `_t` | 初始超时 |

```c
{ \
        .handler = (_handler), \
        .user_data = (_user_data), \
        .exec_cnt = (_exec_cnt), \
        .preempt_cnt = (_preempt_cnt), \
        .t = (_t) \
}
```

## 508.2\_设置并运行压力测试

[`ZTRESS_EXECUTE`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga6acc3a50e0eff7360873006482f5c8e9) 初始化全部上下文，然后调用 [`ztress_execute`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf706f1af4c42f5925d7545dadf5548fd)。

```c
#define ZTRESS_EXECUTE(...)
```

参数 `...` 是由 [`ZTRESS_TIMER`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gabab05b8db44a7024ce23cb34bf999e42) 与 [`ZTRESS_THREAD`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaed561641541e8ced6866f2f1227f21c0) 描述的上下文列表。如果使用定时器上下文，它**必须是第一个参数**。每个线程上下文按列出顺序分配优先级，先列出的线程优先级最高，之后依次降低。

原文说明，包括定时器上下文在内的最大支持数量由 Kconfig 的 `ZTRESS_MAX_THREADS` 选项配置。

下面保留官方展开。内部 `Z_ZTRESS_TIMER_CONTEXT_VALIDATE` 检查定时器位置，`Z_ZTRESS_HAS_TIMER` 判断是否存在定时器，`Z_ZTRESS_GET_HANDLER_DATA` 提取描述数据；`FOR_EACH` 遍历可变参数，[`ARRAY_SIZE`](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a) 取得数组元素数，`__VA_ARGS__` 表示可变参数。`zassert_equal` 是相等断言宏，用于检查执行函数返回值为 `0`。

```c
        do {                                                    \
        Z_ZTRESS_TIMER_CONTEXT_VALIDATE(__VA_ARGS__);                                   \
        int has_timer = Z_ZTRESS_HAS_TIMER(__VA_ARGS__);                                \
        struct ztress_context_data _ctx_data1[] = {                                     \
                FOR_EACH(Z_ZTRESS_GET_HANDLER_DATA, (,), __VA_ARGS__)                   \
        };                                                                              \
        size_t cnt = ARRAY_SIZE(_ctx_data1) - has_timer;                                \
        static struct ztress_context_data _ctx_data[ARRAY_SIZE(_ctx_data1)];            \
        for (size_t i = 0; i < ARRAY_SIZE(_ctx_data1); i++) {                           \
                _ctx_data[i] = _ctx_data1[i];                                           \
        }                                                                               \
        int exec_err = ztress_execute(has_timer ? &_ctx_data[0] : NULL,                 \
                                 &_ctx_data[has_timer], cnt);                           \
                                                                                        \
        zassert_equal(exec_err, 0, "ztress_execute failed (err: %d)", exec_err);        \
} while (0)
```

## 508.3\_线程上下文描述

[`ZTRESS_THREAD`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaed561641541e8ced6866f2f1227f21c0) 描述在**线程上下文（Thread Context）**执行的处理函数。线程优先级取决于它在 [`ZTRESS_EXECUTE`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga6acc3a50e0eff7360873006482f5c8e9) 参数列表中的位置。

```c
#define ZTRESS_THREAD(handler, user_data, exec_cnt, preempt_cnt, init_timeout)
```

线程会睡眠一段随机时间，还会进行随机时长的**忙等待（Busy Wait）**，进一步增加测试随机性。

| 参数 | 含义与完成规则 |
| --- | --- |
| `handler` | [`ztress_handler`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga633439263754bf08baee06c37dddab40) 类型的用户处理函数 |
| `user_data` | 传给处理函数的用户数据 |
| `exec_cnt` | 完成测试所需的处理函数执行次数；为 `0` 时不计入完成条件 |
| `preempt_cnt` | 完成测试所需的该上下文被抢占次数；为 `0` 时不计入完成条件 |
| `init_timeout` | 初始退避时间基准（Backoff Time Base），类型为 [`k_timeout_t`](../timer_reference/P087_内核超时类型.md)；测试期间会调整以优化处理器负载，实际睡眠超时随机化 |

[`k_timeout_t`](../timer_reference/P087_内核超时类型.md) 是 Zephyr 超时类型。展开中的 [`ZTRESS_ID_THREAD`](https://docs.zephyrproject.org/latest/doxygen/html/ztress_8h.html#a8752d529cfc4d77b1dd71c4572fd63c3) 是线程上下文种类标识。

```c
(ZTRESS_ID_THREAD, handler, user_data, exec_cnt, preempt_cnt, init_timeout)
```

## 508.4\_定时器上下文描述

[`ZTRESS_TIMER`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gabab05b8db44a7024ce23cb34bf999e42) 描述内核定时器 [`k_timer`](https://docs.zephyrproject.org/latest/doxygen/html/structk__timer.html) 处理函数的执行上下文，通常是**中断上下文（Interrupt Context）**。这个上下文会抢占集合中的其他上下文。

```c
#define ZTRESS_TIMER(handler, user_data, exec_cnt, init_timeout)
```

**注意：**一组上下文中最多只能有一个 [`k_timer`](https://docs.zephyrproject.org/latest/doxygen/html/structk__timer.html) 上下文，而且它必须是 [`ZTRESS_EXECUTE`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga6acc3a50e0eff7360873006482f5c8e9) 的第一个参数。

| 参数 | 含义 |
| --- | --- |
| `handler` | [`ztress_handler`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga633439263754bf08baee06c37dddab40) 类型的用户处理函数 |
| `user_data` | 传给处理函数的用户数据 |
| `exec_cnt` | 完成测试所需执行次数；为 `0` 时不计入完成条件 |
| `init_timeout` | [`k_timeout_t`](../timer_reference/P087_内核超时类型.md) 类型的初始退避时间基准，运行中会调整以优化处理器负载；实际定时器超时随机化 |

展开中 [`ZTRESS_ID_K_TIMER`](https://docs.zephyrproject.org/latest/doxygen/html/ztress_8h.html#a937803e1398db7d0e10ea60c9c9ef642) 为内核定时器上下文种类标识，被抢占次数位置固定为 `0`。

```c
(ZTRESS_ID_K_TIMER, handler, user_data, exec_cnt, 0, init_timeout)
```

## 508.5\_用户处理函数

[`ztress_handler`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga633439263754bf08baee06c37dddab40) 是在已配置上下文之一中调用的用户处理函数类型。

```c
typedef bool (*ztress_handler)(void *user_data, uint32_t cnt, bool last, int prio);
```

| 参数 | 含义 |
| --- | --- |
| `user_data` | 上下文描述中提供的用户数据 |
| `cnt` | 当前执行计数，从 `0` 开始 |
| `last` | 为 [`true`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7) 表示这是最后一次执行，原因可能是完成条件已满足、测试超时或测试已中止 |
| `prio` | 上下文优先级，从 `0` 开始，`0` 表示最高优先级 |

返回 `true` 继续测试；返回 [`false`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727) 停止执行**当前上下文**。

## 508.6\_执行、超时与中止

[`ztress_execute()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf706f1af4c42f5925d7545dadf5548fd) 执行上下文，直到全部完成要求满足，或达到 [`ztress_set_timeout()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga5b3069bb2aa35ddc64c46c18d2e30091) 设置的超时，或被 [`ztress_abort()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga57f171e230fba462b3dea6b2d3cf71f6) 中止。测试完成时会在内部调用 [`ztress_report()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf4db2092eee17d863c9810333ba4c870) 打印报告。

```c
int ztress_execute(struct ztress_context_data *timer_data,
                    struct ztress_context_data *thread_data, size_t cnt);
```

参数 `timer_data` 为定时器上下文，不使用定时器时传空指针 `NULL`；`thread_data` 为按优先级从高到低排列的线程上下文描述列表；`cnt` 为线程上下文数量。配置无效返回 `-EINVAL`，测试成功执行返回 `0`。

[`ztress_set_timeout()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga5b3069bb2aa35ddc64c46c18d2e30091) 设置测试超时：

```c
void ztress_set_timeout(k_timeout_t t);
```

参数 `t` 为超时。达到超时时，无论完成条件是否满足都会终止测试。**此设置在多次执行之间持续有效。**

[`ztress_abort()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga57f171e230fba462b3dea6b2d3cf71f6) 中止正在进行的压力测试：

```c
void ztress_abort(void);
```

## 508.7\_报告与上次运行统计

[`ztress_report()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf4db2092eee17d863c9810333ba4c870) 打印上一次测试报告，包含各上下文的执行次数、被抢占次数、初始及调整后的超时，以及测试期间的**中央处理器（Central Processing Unit，CPU）**负载。

```c
void ztress_report(void);
```

下列三个查询函数都接收上下文标识 `id`，其中 `0` 表示最高优先级上下文。

```c
int ztress_exec_count(uint32_t id);
int ztress_preempt_count(uint32_t id);
uint32_t ztress_optimized_ticks(uint32_t id);
```

[`ztress_exec_count()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b) 返回上次测试中指定上下文的执行次数；[`ztress_preempt_count()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga4406b828d170bc19065aaf65aeb4613e) 返回其被抢占次数；[`ztress_optimized_ticks()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gacbbdb8e7bad532d6dd20c486b3256e21) 返回优化后的超时时间基准。

可以用优化结果更新初始值，让后续测试更快达到合适的 CPU 负载；原文说明这样可立即达到优化的负载水平。

---

[上一章：ZTest测试定义宏](P507_ZTest测试定义宏.md) · [下一章：测试预期结果记录](P509_测试预期结果记录.md) · [返回大纲](大纲.md)
