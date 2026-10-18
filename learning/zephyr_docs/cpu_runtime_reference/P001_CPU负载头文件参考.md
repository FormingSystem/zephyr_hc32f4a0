---
id: learning.zephyr-docs.cpu-runtime-reference.page-1
title: CPU负载头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cpu__load_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_CPU负载头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cpu__load_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入 CPU 负载、线程分析器、函数插桩源码和线程运行统计参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ga21c1e9efe2f4ba8f40a3e9dd1f32b52e"></a>

```c
#define CPU_LOAD_PERMILLE_TO_PERCENT(permille)
```

相关声明：[CPU_LOAD_PERMILLE_TO_PERCENT](../observability/P049_CPU负载接口.md#ga21c1e9efe2f4ba8f40a3e9dd1f32b52e)。

将千分比（Per Mille）形式的 CPU 负载转换为整数百分比（Whole Percent）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_ga83f2e3099de11b8e6b66395ae69f394a"></a>

```c
typedef void(* cpu_load_cb_t) (uint8_t percent)
```

相关声明：[cpu_load_cb_t](../observability/P049_CPU负载接口.md#ga83f2e3099de11b8e6b66395ae69f394a)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_gab8e384170b8fc3c253a30e3490ebb34f"></a>

```c
int cpu_load_get_cpu (unsigned int cpu_id, bool reset)
```

相关声明：[cpu_load_get_cpu](../observability/P049_CPU负载接口.md#gab8e384170b8fc3c253a30e3490ebb34f)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

获取指定 CPU 的负载（CPU Load）。

<a id="r_gaf44501a292aeef7749b68c706b34119f"></a>

```c
int cpu_load_get (bool reset)
```

相关声明：[cpu_load_get](../observability/P049_CPU负载接口.md#gaf44501a292aeef7749b68c706b34119f)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

获取当前 CPU 的负载。

<a id="r_ga28a73232eb45cdf6ce057e1e4c84190d"></a>

```c
void cpu_load_on_enter_idle (void)
```

相关声明：[cpu_load_on_enter_idle](../observability/P049_CPU负载接口.md#ga28a73232eb45cdf6ce057e1e4c84190d)。

进入 CPU 空闲状态（Idle）时调用的钩子（Hook）。

<a id="r_ga8a8c97914a72b6eb5a7e1862710a0c6d"></a>

```c
void cpu_load_on_exit_idle (void)
```

相关声明：[cpu_load_on_exit_idle](../observability/P049_CPU负载接口.md#ga8a8c97914a72b6eb5a7e1862710a0c6d)。

退出 CPU 空闲状态时调用的钩子。

<a id="r_gabc95920fb1a666b1496618cf5afbfbff"></a>

```c
void cpu_load_log_control (bool enable)
```

相关声明：[cpu_load_log_control](../observability/P049_CPU负载接口.md#gabc95920fb1a666b1496618cf5afbfbff)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

控制周期性 CPU 负载报告。

<a id="r_gaec80c70d8dd6ea130edde48618ed2463"></a>

```c
int cpu_load_cb_reg (cpu_load_cb_t cb, uint8_t threshold_percent)
```

相关声明：[cpu_load_cb_reg](../observability/P049_CPU负载接口.md#gaec80c70d8dd6ea130edde48618ed2463)、[cpu_load_cb_t](../observability/P049_CPU负载接口.md#ga83f2e3099de11b8e6b66395ae69f394a)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

可选的回调注册：当负载大于或等于阈值（Threshold）时调用回调。

<a id="r_ga3333539cf7d8a6916cbbec9cd1f5bf59"></a>

```c
static int cpu_load_metric_get (int cpu_id)
```

相关声明：[cpu_load_metric_get](../observability/P049_CPU负载接口.md#ga3333539cf7d8a6916cbbec9cd1f5bf59)。

获取指定 CPU 的负载百分比。

## 1.4\_源码定位与版本边界

相对源码定位：[CPU负载头文件](../../../include/zephyr/sys/cpu_load.h)、[CPU负载实现](../../../lib/os/cpu_load/cpu_load.c)、[测量后端配置](../../../lib/os/cpu_load/Kconfig)、[线程分析器](../../../subsys/debug/thread_analyzer/thread_analyzer.c)、[线程类型头文件](../../../include/zephyr/kernel/thread.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注依据本批保存摘要的官方 main 文件，独立于官方正文。源码使用相对路径定位；本地源码版本若不同，应以来源记录中的版本边界核对。

> 译注——源码核对：cpu_load_get_cpu和cpu_load_get返回千分比（Per Mille）0～1000，失败返回负errno；先检查负值再转换单位。CPU_LOAD_PERMILLE_TO_PERCENT只是除以10，整数输入会舍去小数，不负责错误检查。旧cpu_load_metric_get返回整数百分比，并固定传入reset=true，迁移接口时单位和采样窗口都要明确。

> 译注——源码核对：reset=true在取得当前读数后更新目标CPU的测量窗口（Measurement Window）。运行统计后端更新自身保存的active_prev和wall_prev，并不清零调度器的累计计数；多个调用者读取同一CPU并重置时会共享这个窗口。周期报告也逐CPU调用reset=true，会影响手动读取的区间。

> 译注——源码核对：周期回调从k_timer到期函数（Expiry Function）执行，CONFIG_CPU_LOAD_LOG_PERIODICALLY须为正值；注册回调本身不会启动独立采样线程。当前实现先把千分比除以10，再与0～100的阈值比较，每个达到阈值的CPU都可能触发回调；回调参数只有百分比，没有CPU编号。

> 译注——源码核对：运行统计后端（Runtime Statistics Backend）按非空闲周期差值除以总周期差值计算负载；空闲钩子后端（Idle Hook Backend）按经过时间减去空闲时间计算。可选硬件计数器路径受!SMP限制，不能把这一限制推广到整个空闲钩子实现；本次源码已有按CPU保存的空闲窗口。Kconfig仍有单CPU概括文字，应结合实际条件与实现核对。

> 译注——源码核对：cpu_load_log_control(true)在正的报告周期下先重置所有CPU测量窗口，再启动定时器；false停止报告，不等于停止后端统计。周期配置为0时此函数直接返回。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.5\_原页交叉引用（Cross References）

- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h_source.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码](P002_CPU负载头文件源码.md)
- [CPU_LOAD_PERMILLE_TO_PERCENT](../observability/P049_CPU负载接口.md#ga21c1e9efe2f4ba8f40a3e9dd1f32b52e)
- [cpu_load_cb_t](../observability/P049_CPU负载接口.md#ga83f2e3099de11b8e6b66395ae69f394a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cpu_load_get_cpu](../observability/P049_CPU负载接口.md#gab8e384170b8fc3c253a30e3490ebb34f)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [cpu_load_get](../observability/P049_CPU负载接口.md#gaf44501a292aeef7749b68c706b34119f)
- [cpu_load_on_enter_idle](../observability/P049_CPU负载接口.md#ga28a73232eb45cdf6ce057e1e4c84190d)
- [cpu_load_on_exit_idle](../observability/P049_CPU负载接口.md#ga8a8c97914a72b6eb5a7e1862710a0c6d)
- [cpu_load_log_control](../observability/P049_CPU负载接口.md#gabc95920fb1a666b1496618cf5afbfbff)
- [cpu_load_cb_reg](../observability/P049_CPU负载接口.md#gaec80c70d8dd6ea130edde48618ed2463)
- [cpu_load_metric_get](../observability/P049_CPU负载接口.md#ga3333539cf7d8a6916cbbec9cd1f5bf59)

---

[返回大纲](大纲.md) · [下一章](P002_CPU负载头文件源码.md)
