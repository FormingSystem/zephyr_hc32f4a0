---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-14
title: 性能监控单元（PMU）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_性能监控单元（PMU）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_pmu_5Fcounter_5Fconfig"></a>

```c
struct pmu_counter_config
```

相关声明：[pmu_counter_config](../kernel_runtime_model_reference/P013_pmu_counter_config_结构体.md)。

性能监测单元（PMU）计数器的配置条目。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_ga58bd852a407f51acb9c744779322febe"></a>

```c
#define PMU_MAX_COUNTERS 8
```

相关声明：[PMU_MAX_COUNTERS](#ga58bd852a407f51acb9c744779322febe)。

此 API 能描述的逻辑事件计数器（Logical Event Counters）最大数量。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.3\_函数（Functions）

<a id="r_gaad18df75ad3e5928f6a15e92acb4899c"></a>

```c
int pmu_init (void)
```

相关声明：[pmu_init](#gaad18df75ad3e5928f6a15e92acb4899c)。

初始化当前逻辑 CPU 的性能监视单元（PMU）。

<a id="r_gaa6301bd3af19d347ae4210be8dfe20e6"></a>

```c
uint32_t pmu_num_counters (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pmu_num_counters](#gaa6301bd3af19d347ae4210be8dfe20e6)。

<a id="r_ga6cc9827c689699f6a33ad2c782a6b22a"></a>

```c
void pmu_get_info (pmu_info_t *info)
```

相关声明：[pmu_get_info](#ga6cc9827c689699f6a33ad2c782a6b22a)、[pmu_info_t](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md)。

将当前逻辑 CPU 的性能监视单元标识信息（PMU Identification）填入 `info`。

<a id="r_ga3093c22c8e423cddd786c8555fcb7c80"></a>

```c
int pmu_counter_config (uint32_t counter, pmu_evt_t event)
```

相关声明：[pmu_counter_config](#ga3093c22c8e423cddd786c8555fcb7c80)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pmu_evt_t](../api_file_mesh_interrupt_reference/P021_zephyr__arch__pmu.h_文件参考.md#a1e81090eaba4c1aa7009fe85f5bf2f6a)。

将硬件事件计数器（Hardware Event Counter）`counter` 映射到架构事件（Architectural Event）`event`。

<a id="r_ga1b740b0f45c4435cdf3219a5bb3058f7"></a>

```c
void pmu_counter_enable (uint32_t counter)
```

相关声明：[pmu_counter_enable](#ga1b740b0f45c4435cdf3219a5bb3058f7)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使能硬件事件计数器（Hardware Event Counter）`counter` 的计数。

<a id="r_ga788901c9f07cadaf4768b48536af7eac"></a>

```c
void pmu_counter_disable (uint32_t counter)
```

相关声明：[pmu_counter_disable](#ga788901c9f07cadaf4768b48536af7eac)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用硬件事件计数器（Hardware Event Counter）`counter` 的计数。

<a id="r_ga928fc146e105f2250fe6f971e2f67a00"></a>

```c
void pmu_counter_enable_all (void)
```

相关声明：[pmu_counter_enable_all](#ga928fc146e105f2250fe6f971e2f67a00)。

使能所有已实现的事件计数器（Event Counters），以及适用时的周期计数器（Cycle Counter）。

<a id="r_ga6df789669765f445f865c8f6435bb679"></a>

```c
void pmu_counter_disable_all (void)
```

相关声明：[pmu_counter_disable_all](#ga6df789669765f445f865c8f6435bb679)。

禁用所有事件计数器（Event Counters），以及适用时的周期计数器（Cycle Counter）。

<a id="r_gab4d1ae5b2c4351a0d0c69d9477357c0e"></a>

```c
uint64_t pmu_counter_read (uint32_t counter)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[pmu_counter_read](#gab4d1ae5b2c4351a0d0c69d9477357c0e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取硬件事件计数器（Hardware Event Counter）`counter` 的当前值。

<a id="r_ga4b1050bae21c638c9b2dad291461cfdf"></a>

```c
void pmu_counter_reset (uint32_t counter)
```

相关声明：[pmu_counter_reset](#ga4b1050bae21c638c9b2dad291461cfdf)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将硬件事件计数器（Hardware Event Counter）`counter` 清零。

<a id="r_gafe7fb7ed9a8646ecfc40d2c7c443b35f"></a>

```c
void pmu_counter_reset_all (void)
```

相关声明：[pmu_counter_reset_all](#gafe7fb7ed9a8646ecfc40d2c7c443b35f)。

将所有硬件事件计数器（Hardware Event Counters）清零。具体行为由实现定义，可能包含周期计数器策略（Cycle Counter Policies）。

<a id="r_gaaa6b497c1d6e3b0af8ef6f04cbdf0d98"></a>

```c
uint64_t pmu_cycle_count (void)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[pmu_cycle_count](#gaaa6b497c1d6e3b0af8ef6f04cbdf0d98)。

读取架构周期计数寄存器（Architectural Cycle Count Register），前提是已实现。

<a id="r_gac3299a44c61e0d28d974ea6aa2e9ffbc"></a>

```c
void pmu_cycle_reset (void)
```

相关声明：[pmu_cycle_reset](#gac3299a44c61e0d28d974ea6aa2e9ffbc)。

将周期计数寄存器（Cycle Count Register）清零；具体行为由实现定义。

<a id="r_ga12a5201eb9df8c7f83496847526e63ad"></a>

```c
void pmu_start (void)
```

相关声明：[pmu_start](#ga12a5201eb9df8c7f83496847526e63ad)。

开始计数：全局使能性能监视单元（PMU）；具体行为由实现定义。

<a id="r_ga3fa69d6fabe2389dc23ab3b54b72bc6d"></a>

```c
void pmu_stop (void)
```

相关声明：[pmu_stop](#ga3fa69d6fabe2389dc23ab3b54b72bc6d)。

停止计数：全局禁用性能监视单元（PMU）；具体行为由实现定义。

<a id="r_ga35a447da13644c22f4e7148547cbdc9d"></a>

```c
bool pmu_counter_overflow (uint32_t counter)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pmu_counter_overflow](#ga35a447da13644c22f4e7148547cbdc9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

返回硬件事件计数器（Hardware Event Counter）`counter` 自标志被清除以来是否发生过溢出（Overflow）。

<a id="r_ga29dc5718b7d83eaaf1c52645394394ef"></a>

```c
void pmu_counter_clear_overflow (uint32_t counter)
```

相关声明：[pmu_counter_clear_overflow](#ga29dc5718b7d83eaaf1c52645394394ef)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

清除硬件事件计数器（Hardware Event Counter）`counter` 的溢出标志（Overflow Flag）。

## 14.4\_详细说明（Detailed Documentation）

<a id="ga58bd852a407f51acb9c744779322febe"></a>

### `PMU_MAX_COUNTERS`

```c
#define PMU_MAX_COUNTERS 8
```

```c
#include <zephyr/arch/pmu.h>
```

此 API 能描述的逻辑事件计数器（Logical Event Counters）最大数量。

具体后端（Backend）实际实现的活动硬件计数器可能更少。

<a id="ga29dc5718b7d83eaaf1c52645394394ef"></a>

### `pmu_counter_clear_overflow()`

```c
void pmu_counter_clear_overflow ( uint32_t counter)
```

```c
#include <zephyr/arch/pmu.h>
```

清除硬件事件计数器（Hardware Event Counter）`counter` 的溢出标志（Overflow Flag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 事件计数器索引（Event Counter Index），范围为 `[0, pmu_num_counters())`。 |

<a id="ga3093c22c8e423cddd786c8555fcb7c80"></a>

### `pmu_counter_config()`

```c
int pmu_counter_config ( uint32_t counter, pmu_evt_t event )
```

```c
#include <zephyr/arch/pmu.h>
```

将硬件事件计数器（Hardware Event Counter）`counter` 映射到架构事件（Architectural Event）`event`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 事件计数器索引（Event Counter Index），位于 `[0, pmu_num_counters())` 范围内。 |
| `event` | 事件选择器（Event Selector）；若存在架构补充定义，则使用其中的 `pmu_evt_t`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ga788901c9f07cadaf4768b48536af7eac"></a>

### `pmu_counter_disable()`

```c
void pmu_counter_disable ( uint32_t counter)
```

```c
#include <zephyr/arch/pmu.h>
```

禁用硬件事件计数器（Hardware Event Counter）`counter` 的计数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 事件计数器索引（Event Counter Index），范围为 `[0, pmu_num_counters())`。 |

<a id="ga6df789669765f445f865c8f6435bb679"></a>

### `pmu_counter_disable_all()`

```c
void pmu_counter_disable_all ( void )
```

```c
#include <zephyr/arch/pmu.h>
```

禁用所有事件计数器（Event Counters），以及适用时的周期计数器（Cycle Counter）。

<a id="ga1b740b0f45c4435cdf3219a5bb3058f7"></a>

### `pmu_counter_enable()`

```c
void pmu_counter_enable ( uint32_t counter)
```

```c
#include <zephyr/arch/pmu.h>
```

使能硬件事件计数器（Hardware Event Counter）`counter` 的计数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 事件计数器索引（Event Counter Index），范围为 `[0, pmu_num_counters())`。 |

<a id="ga928fc146e105f2250fe6f971e2f67a00"></a>

### `pmu_counter_enable_all()`

```c
void pmu_counter_enable_all ( void )
```

```c
#include <zephyr/arch/pmu.h>
```

使能所有已实现的事件计数器（Event Counters），以及适用时的周期计数器（Cycle Counter）。

<a id="ga35a447da13644c22f4e7148547cbdc9d"></a>

### `pmu_counter_overflow()`

```c
bool pmu_counter_overflow ( uint32_t counter)
```

```c
#include <zephyr/arch/pmu.h>
```

返回硬件事件计数器（Hardware Event Counter）`counter` 自标志被清除以来是否发生过溢出（Overflow）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 事件计数器索引（Event Counter Index），范围为 `[0, pmu_num_counters())`。 |

**返回（Returns）**：返回值：有待处理溢出（Overflow Pending）时返回 `true`；否则，或性能监视单元（PMU）不可用时，返回 `false`。

<a id="gab4d1ae5b2c4351a0d0c69d9477357c0e"></a>

### `pmu_counter_read()`

```c
uint64_t pmu_counter_read ( uint32_t counter)
```

```c
#include <zephyr/arch/pmu.h>
```

读取硬件事件计数器（Hardware Event Counter）`counter` 的当前值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 事件计数器索引（Event Counter Index），范围为 `[0, pmu_num_counters())`。 |

**返回（Returns）**：返回值：计数器值（Counter Value）；PMU 不可用或计数器超出范围时返回 0。

<a id="ga4b1050bae21c638c9b2dad291461cfdf"></a>

### `pmu_counter_reset()`

```c
void pmu_counter_reset ( uint32_t counter)
```

```c
#include <zephyr/arch/pmu.h>
```

将硬件事件计数器（Hardware Event Counter）`counter` 清零。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 事件计数器索引（Event Counter Index），范围为 `[0, pmu_num_counters())`。 |

<a id="gafe7fb7ed9a8646ecfc40d2c7c443b35f"></a>

### `pmu_counter_reset_all()`

```c
void pmu_counter_reset_all ( void )
```

```c
#include <zephyr/arch/pmu.h>
```

将所有硬件事件计数器（Hardware Event Counters）清零。具体行为由实现定义，可能包含周期计数器策略（Cycle Counter Policies）。

<a id="gaaa6b497c1d6e3b0af8ef6f04cbdf0d98"></a>

### `pmu_cycle_count()`

```c
uint64_t pmu_cycle_count ( void )
```

```c
#include <zephyr/arch/pmu.h>
```

读取架构周期计数寄存器（Architectural Cycle Count Register），前提是已实现。

**返回（Returns）**：返回值：周期计数（Cycle Count）；不可用时返回 0。

<a id="gac3299a44c61e0d28d974ea6aa2e9ffbc"></a>

### `pmu_cycle_reset()`

```c
void pmu_cycle_reset ( void )
```

```c
#include <zephyr/arch/pmu.h>
```

将周期计数寄存器（Cycle Count Register）清零；具体行为由实现定义。

<a id="ga6cc9827c689699f6a33ad2c782a6b22a"></a>

### `pmu_get_info()`

```c
void pmu_get_info ( pmu_info_t * info)
```

```c
#include <zephyr/arch/pmu.h>
```

将当前逻辑 CPU 的性能监视单元标识信息（PMU Identification）填入 `info`。

`info` 不得为 `NULL`。仅在此 CPU 上成功执行 `pmu_init` 后，各字段才有意义；具体内容由后端定义，参见架构相关的 `pmu_info_t`。

<a id="gaad18df75ad3e5928f6a15e92acb4899c"></a>

### `pmu_init()`

```c
int pmu_init ( void )
```

```c
#include <zephyr/arch/pmu.h>
```

初始化当前逻辑 CPU 的性能监视单元（PMU）。

与架构无关（Architecture-neutral）的硬件性能计数器接口。各后端为受支持的架构实现这些函数，例如 AArch64 上的 ARMv8-A PMUv3、未来的 ARMv8-R／Cortex-R52、RISC-V 硬件性能监视控制状态寄存器（HPM CSRs）等。

架构事件码（Architectural Event Codes）由架构补充接口定义。例如启用 `CONFIG_ARM64` 时，使用 `<zephyr/arch/arm64/pmuv3.h>` 中的 `pmu_evt_t`。

内核启动期间不会初始化性能监视单元（PMU）。在此 CPU 上调用其他 `pmu_*()` 函数前，请调用 `pmu_init()`。

对每个要使用计数器的逻辑 CPU，在该 CPU 上调用任何其他 `pmu_*()` API 前，先调用一次。成功后此操作是幂等的（Idempotent）：若此 CPU 已成功初始化，后续调用返回 0；若此 CPU 已记录为没有可用 PMU，则返回 `-ENOTSUP`。

PMU 控制和计数器均按 CPU 独立维护（Per-CPU）。在对称多处理（SMP）系统上，仅在目标 CPU 上运行时使用 PMU。例如，通过 `k_thread_cpu_pin()` 固定线程，需要启用 `CONFIG_SCHED_CPU_MASK`；或者通过 `k_thread_cpu_mask_enable()`／`k_thread_cpu_mask_disable()` 约束 CPU 亲和性（Affinity），避免测量期间迁移。

不存在 `SYS_INIT` 钩子（Hook）；由调用方决定何时探测，例如在基准测试开始时。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOTSUP` | 没有性能监视单元（PMU），或在此 CPU 的当前异常级别（Exception Level）不可用。 |

<a id="gaa6301bd3af19d347ae4210be8dfe20e6"></a>

### `pmu_num_counters()`

```c
uint32_t pmu_num_counters ( void )
```

```c
#include <zephyr/arch/pmu.h>
```

**返回（Returns）**：返回值：此 CPU 上的事件计数器数量（Number of Event Counters）；PMU 不可用时返回 0。

<a id="ga12a5201eb9df8c7f83496847526e63ad"></a>

### `pmu_start()`

```c
void pmu_start ( void )
```

```c
#include <zephyr/arch/pmu.h>
```

开始计数：全局使能性能监视单元（PMU）；具体行为由实现定义。

<a id="ga3fa69d6fabe2389dc23ab3b54b72bc6d"></a>

### `pmu_stop()`

```c
void pmu_stop ( void )
```

```c
#include <zephyr/arch/pmu.h>
```

停止计数：全局禁用性能监视单元（PMU）；具体行为由实现定义。


## 14.5\_原页交叉引用（Cross References）

- [pmu_counter_config](../kernel_runtime_model_reference/P013_pmu_counter_config_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pmu_info_t](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md)
- [pmu_evt_t](../api_file_mesh_interrupt_reference/P021_zephyr__arch__pmu.h_文件参考.md#a1e81090eaba4c1aa7009fe85f5bf2f6a)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/arch/pmu.h](../api_file_mesh_interrupt_reference/P021_zephyr__arch__pmu.h_文件参考.md)
- [k_thread_cpu_pin()](../thread_core_reference/P001_线程公共接口.md#gae9ebd9845e14ed02944ab9282a185c03)
- [k_thread_cpu_mask_enable()](../thread_core_reference/P001_线程公共接口.md#ga306587604a7496db8059bd395fd90fc0)
- [k_thread_cpu_mask_disable()](../thread_core_reference/P001_线程公共接口.md#ga89e6c07ac112da75b2ef115d1a557d44)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_数据报分组层路径 MTU 发现 API（Datagram PLPMTUD API）.md) · [返回大纲](大纲.md)
