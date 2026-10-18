---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-21
title: zephyr__arch__pmu.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_arch\_\_pmu.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

硬件性能监测单元（Performance Monitoring Unit，PMU）的API。

<a id="details"></a>

```c
#include <zephyr/autoconf.h>
#include <stdint.h>
#include <stdbool.h>
```

查看此文件的源码。

硬件性能监测单元（Performance Monitoring Unit，PMU）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_pmu_5Finfo_5Ft"></a>

```c
struct pmu_info_t
```

相关声明：[pmu_info_t](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md)。

没有架构补充实现（Arch Supplement）时使用的pmu_info_t占位类型。

<a id="r_pmu_5Fcounter_5Fconfig"></a>

```c
struct pmu_counter_config
```

相关声明：[pmu_counter_config](../kernel_runtime_model_reference/P013_pmu_counter_config_结构体.md)。

性能监测单元（PMU）计数器的配置条目。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="r_ga58bd852a407f51acb9c744779322febe"></a>

```c
#define PMU_MAX_COUNTERS 8
```

相关声明：[PMU_MAX_COUNTERS](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga58bd852a407f51acb9c744779322febe)。

此 API 能描述的逻辑事件计数器（Logical Event Counters）最大数量。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 21.3\_类型定义（Typedefs）

<a id="r_a1e81090eaba4c1aa7009fe85f5bf2f6a"></a>

```c
typedef uint32_t pmu_evt_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pmu_evt_t](#a1e81090eaba4c1aa7009fe85f5bf2f6a)。

当架构补充接口未定义 `pmu_evt_t` 时使用的架构／后端事件选择器（Architectural/Backend Event Selector）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.4\_函数（Functions）

<a id="r_gaad18df75ad3e5928f6a15e92acb4899c"></a>

```c
int pmu_init (void)
```

相关声明：[pmu_init](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gaad18df75ad3e5928f6a15e92acb4899c)。

初始化当前逻辑 CPU 的性能监视单元（PMU）。

<a id="r_gaa6301bd3af19d347ae4210be8dfe20e6"></a>

```c
uint32_t pmu_num_counters (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pmu_num_counters](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gaa6301bd3af19d347ae4210be8dfe20e6)。

<a id="r_ga6cc9827c689699f6a33ad2c782a6b22a"></a>

```c
void pmu_get_info (pmu_info_t *info)
```

相关声明：[pmu_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga6cc9827c689699f6a33ad2c782a6b22a)、[pmu_info_t](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md)。

将当前逻辑 CPU 的性能监视单元标识信息（PMU Identification）填入 `info`。

<a id="r_ga3093c22c8e423cddd786c8555fcb7c80"></a>

```c
int pmu_counter_config (uint32_t counter, pmu_evt_t event)
```

相关声明：[pmu_counter_config](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga3093c22c8e423cddd786c8555fcb7c80)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pmu_evt_t](#a1e81090eaba4c1aa7009fe85f5bf2f6a)。

将硬件事件计数器（Hardware Event Counter）`counter` 映射到架构事件（Architectural Event）`event`。

<a id="r_ga1b740b0f45c4435cdf3219a5bb3058f7"></a>

```c
void pmu_counter_enable (uint32_t counter)
```

相关声明：[pmu_counter_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga1b740b0f45c4435cdf3219a5bb3058f7)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使能硬件事件计数器（Hardware Event Counter）`counter` 的计数。

<a id="r_ga788901c9f07cadaf4768b48536af7eac"></a>

```c
void pmu_counter_disable (uint32_t counter)
```

相关声明：[pmu_counter_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga788901c9f07cadaf4768b48536af7eac)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用硬件事件计数器（Hardware Event Counter）`counter` 的计数。

<a id="r_ga928fc146e105f2250fe6f971e2f67a00"></a>

```c
void pmu_counter_enable_all (void)
```

相关声明：[pmu_counter_enable_all](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga928fc146e105f2250fe6f971e2f67a00)。

使能所有已实现的事件计数器（Event Counters），以及适用时的周期计数器（Cycle Counter）。

<a id="r_ga6df789669765f445f865c8f6435bb679"></a>

```c
void pmu_counter_disable_all (void)
```

相关声明：[pmu_counter_disable_all](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga6df789669765f445f865c8f6435bb679)。

禁用所有事件计数器（Event Counters），以及适用时的周期计数器（Cycle Counter）。

<a id="r_gab4d1ae5b2c4351a0d0c69d9477357c0e"></a>

```c
uint64_t pmu_counter_read (uint32_t counter)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[pmu_counter_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gab4d1ae5b2c4351a0d0c69d9477357c0e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取硬件事件计数器（Hardware Event Counter）`counter` 的当前值。

<a id="r_ga4b1050bae21c638c9b2dad291461cfdf"></a>

```c
void pmu_counter_reset (uint32_t counter)
```

相关声明：[pmu_counter_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga4b1050bae21c638c9b2dad291461cfdf)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将硬件事件计数器（Hardware Event Counter）`counter` 清零。

<a id="r_gafe7fb7ed9a8646ecfc40d2c7c443b35f"></a>

```c
void pmu_counter_reset_all (void)
```

相关声明：[pmu_counter_reset_all](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gafe7fb7ed9a8646ecfc40d2c7c443b35f)。

将所有硬件事件计数器（Hardware Event Counters）清零。具体行为由实现定义，可能包含周期计数器策略（Cycle Counter Policies）。

<a id="r_gaaa6b497c1d6e3b0af8ef6f04cbdf0d98"></a>

```c
uint64_t pmu_cycle_count (void)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[pmu_cycle_count](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gaaa6b497c1d6e3b0af8ef6f04cbdf0d98)。

读取架构周期计数寄存器（Architectural Cycle Count Register），前提是已实现。

<a id="r_gac3299a44c61e0d28d974ea6aa2e9ffbc"></a>

```c
void pmu_cycle_reset (void)
```

相关声明：[pmu_cycle_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gac3299a44c61e0d28d974ea6aa2e9ffbc)。

将周期计数寄存器（Cycle Count Register）清零；具体行为由实现定义。

<a id="r_ga12a5201eb9df8c7f83496847526e63ad"></a>

```c
void pmu_start (void)
```

相关声明：[pmu_start](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga12a5201eb9df8c7f83496847526e63ad)。

开始计数：全局使能性能监视单元（PMU）；具体行为由实现定义。

<a id="r_ga3fa69d6fabe2389dc23ab3b54b72bc6d"></a>

```c
void pmu_stop (void)
```

相关声明：[pmu_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga3fa69d6fabe2389dc23ab3b54b72bc6d)。

停止计数：全局禁用性能监视单元（PMU）；具体行为由实现定义。

<a id="r_ga35a447da13644c22f4e7148547cbdc9d"></a>

```c
bool pmu_counter_overflow (uint32_t counter)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pmu_counter_overflow](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga35a447da13644c22f4e7148547cbdc9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

返回硬件事件计数器（Hardware Event Counter）`counter` 自标志被清除以来是否发生过溢出（Overflow）。

<a id="r_ga29dc5718b7d83eaaf1c52645394394ef"></a>

```c
void pmu_counter_clear_overflow (uint32_t counter)
```

相关声明：[pmu_counter_clear_overflow](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga29dc5718b7d83eaaf1c52645394394ef)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

清除硬件事件计数器（Hardware Event Counter）`counter` 的溢出标志（Overflow Flag）。

## 21.5\_详细说明（Detailed Documentation）

<a id="a1e81090eaba4c1aa7009fe85f5bf2f6a"></a>

### `pmu_evt_t`

```c
typedef uint32_t pmu_evt_t
```

当架构补充接口未定义 `pmu_evt_t` 时使用的架构／后端事件选择器（Architectural/Backend Event Selector）。


## 21.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P664_pmu.h_源码浏览.md)
- [pmu_info_t](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md)
- [pmu_counter_config](../kernel_runtime_model_reference/P013_pmu_counter_config_结构体.md)
- [PMU_MAX_COUNTERS](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga58bd852a407f51acb9c744779322febe)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pmu_init](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gaad18df75ad3e5928f6a15e92acb4899c)
- [pmu_num_counters](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gaa6301bd3af19d347ae4210be8dfe20e6)
- [pmu_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga6cc9827c689699f6a33ad2c782a6b22a)
- [pmu_counter_config](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga3093c22c8e423cddd786c8555fcb7c80)
- [pmu_counter_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga1b740b0f45c4435cdf3219a5bb3058f7)
- [pmu_counter_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga788901c9f07cadaf4768b48536af7eac)
- [pmu_counter_enable_all](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga928fc146e105f2250fe6f971e2f67a00)
- [pmu_counter_disable_all](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga6df789669765f445f865c8f6435bb679)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [pmu_counter_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gab4d1ae5b2c4351a0d0c69d9477357c0e)
- [pmu_counter_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga4b1050bae21c638c9b2dad291461cfdf)
- [pmu_counter_reset_all](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gafe7fb7ed9a8646ecfc40d2c7c443b35f)
- [pmu_cycle_count](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gaaa6b497c1d6e3b0af8ef6f04cbdf0d98)
- [pmu_cycle_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gac3299a44c61e0d28d974ea6aa2e9ffbc)
- [pmu_start](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga12a5201eb9df8c7f83496847526e63ad)
- [pmu_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga3fa69d6fabe2389dc23ab3b54b72bc6d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [pmu_counter_overflow](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga35a447da13644c22f4e7148547cbdc9d)
- [pmu_counter_clear_overflow](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga29dc5718b7d83eaaf1c52645394394ef)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P020_zephyr__dt-bindings__display__panel.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__sw_isr_table.h_文件参考.md)
