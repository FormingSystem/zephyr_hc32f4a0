---
id: learning.zephyr-docs.api-file-system-power-reference.page-46
title: ____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztress.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztress_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_ztest\_\_include\_\_zephyr\_\_ztress.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ztress_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr测试框架（Testing Framework）的ztress宏。

<a id="details"></a>

```c
#include <zephyr/sys/util.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

Zephyr测试框架（Testing Framework）的ztress宏。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 46.1\_数据结构（Data Structures）

<a id="r_ztress_5Fcontext_5Fdata"></a>

```c
struct ztress_context_data
```

相关声明：[ztress_context_data](../hardware/P517_压力测试上下文结构.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 46.2\_宏定义（Macros）

<a id="r_a8752d529cfc4d77b1dd71c4572fd63c3"></a>

```c
#define ZTRESS_ID_THREAD 0
```

相关声明：[ZTRESS_ID_THREAD](#a8752d529cfc4d77b1dd71c4572fd63c3)。

<a id="r_a937803e1398db7d0e10ea60c9c9ef642"></a>

```c
#define ZTRESS_ID_K_TIMER 1
```

相关声明：[ZTRESS_ID_K_TIMER](#a937803e1398db7d0e10ea60c9c9ef642)。

<a id="r_gabab05b8db44a7024ce23cb34bf999e42"></a>

```c
#define ZTRESS_TIMER(handler, user_data, exec_cnt, init_timeout)
```

相关声明：[ZTRESS_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gabab05b8db44a7024ce23cb34bf999e42)。

`k_timer` 处理程序执行上下文（Handler Execution Context）的描述符。

<a id="r_gaed561641541e8ced6866f2f1227f21c0"></a>

```c
#define ZTRESS_THREAD(handler, user_data, exec_cnt, preempt_cnt, init_timeout)
```

相关声明：[ZTRESS_THREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaed561641541e8ced6866f2f1227f21c0)。

线程执行上下文（Thread Execution Context）的描述符。

<a id="r_gab5e8bbcecd77db06e7a90631fc0c202b"></a>

```c
#define ZTRESS_CONTEXT_INITIALIZER(_handler, _user_data, _exec_cnt, _preempt_cnt, _t)
```

相关声明：[ZTRESS_CONTEXT_INITIALIZER](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gab5e8bbcecd77db06e7a90631fc0c202b)。

初始化上下文结构体（Context Structure）。

<a id="r_ga6acc3a50e0eff7360873006482f5c8e9"></a>

```c
#define ZTRESS_EXECUTE(...)
```

相关声明：[ZTRESS_EXECUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga6acc3a50e0eff7360873006482f5c8e9)。

设置并运行压力测试（Stress Test）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 46.3\_类型定义（Typedefs）

<a id="r_ga633439263754bf08baee06c37dddab40"></a>

```c
typedef bool(* ztress_handler) (void *user_data, uint32_t cnt, bool last, int prio)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ztress_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga633439263754bf08baee06c37dddab40)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在已配置的某个上下文（Context）中调用的用户处理程序（User Handler）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 46.4\_函数（Functions）

<a id="r_gaf706f1af4c42f5925d7545dadf5548fd"></a>

```c
int ztress_execute (struct ztress_context_data *timer_data, struct ztress_context_data *thread_data, size_t cnt)
```

相关声明：[ztress_execute](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf706f1af4c42f5925d7545dadf5548fd)、[ztress_context_data](../hardware/P517_压力测试上下文结构.md)、[ztress_context_data](../hardware/P517_压力测试上下文结构.md)。

执行上下文（Execute Contexts）。

<a id="r_ga57f171e230fba462b3dea6b2d3cf71f6"></a>

```c
void ztress_abort (void)
```

相关声明：[ztress_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga57f171e230fba462b3dea6b2d3cf71f6)。

中止正在进行的压力测试（Stress Test）。

<a id="r_ga5b3069bb2aa35ddc64c46c18d2e30091"></a>

```c
void ztress_set_timeout (k_timeout_t t)
```

相关声明：[ztress_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga5b3069bb2aa35ddc64c46c18d2e30091)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

设置测试超时时间（Test Timeout）。

<a id="r_gaf4db2092eee17d863c9810333ba4c870"></a>

```c
void ztress_report (void)
```

相关声明：[ztress_report](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf4db2092eee17d863c9810333ba4c870)。

打印上次测试报告（Last Test Report）。

<a id="r_ga99eeabcc672fc5ec0b83ce5b8fb4ec5b"></a>

```c
int ztress_exec_count (uint32_t id)
```

相关声明：[ztress_exec_count](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取给定上下文（Context）在上次测试中的执行次数（Executions）。

<a id="r_ga4406b828d170bc19065aaf65aeb4613e"></a>

```c
int ztress_preempt_count (uint32_t id)
```

相关声明：[ztress_preempt_count](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga4406b828d170bc19065aaf65aeb4613e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取给定上下文（Context）在上次测试中的被抢占次数（Preemptions）。

<a id="r_gacbbdb8e7bad532d6dd20c486b3256e21"></a>

```c
uint32_t ztress_optimized_ticks (uint32_t id)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[ztress_optimized_ticks](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gacbbdb8e7bad532d6dd20c486b3256e21)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取给定上下文（Context）在上次测试中优化后的超时基值（Optimized Timeout Base）。

## 46.5\_详细说明（Detailed Documentation）

<a id="a937803e1398db7d0e10ea60c9c9ef642"></a>

### `ZTRESS_ID_K_TIMER`

```c
#define ZTRESS_ID_K_TIMER 1
```

<a id="a8752d529cfc4d77b1dd71c4572fd63c3"></a>

### `ZTRESS_ID_THREAD`

```c
#define ZTRESS_ID_THREAD 0
```


## 46.6\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P059_ztress.h_源码浏览.md)
- [ztress_context_data](../hardware/P517_压力测试上下文结构.md)
- [ZTRESS_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gabab05b8db44a7024ce23cb34bf999e42)
- [k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)
- [ZTRESS_THREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaed561641541e8ced6866f2f1227f21c0)
- [ZTRESS_CONTEXT_INITIALIZER](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gab5e8bbcecd77db06e7a90631fc0c202b)
- [ZTRESS_EXECUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga6acc3a50e0eff7360873006482f5c8e9)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ztress_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga633439263754bf08baee06c37dddab40)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ztress_execute](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf706f1af4c42f5925d7545dadf5548fd)
- [ztress_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga57f171e230fba462b3dea6b2d3cf71f6)
- [ztress_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga5b3069bb2aa35ddc64c46c18d2e30091)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [ztress_report](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf4db2092eee17d863c9810333ba4c870)
- [ztress_exec_count](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b)
- [ztress_preempt_count](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga4406b828d170bc19065aaf65aeb4613e)
- [ztress_optimized_ticks](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gacbbdb8e7bad532d6dd20c486b3256e21)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P045_zephyr__drivers__usb_c__usbc_ppc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P047_zephyr__zvfs__eventfd.h_文件参考.md)
