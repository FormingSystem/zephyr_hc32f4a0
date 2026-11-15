---
id: learning.zephyr-docs.api-file-system-power-reference.page-21
title: zephyr__kernel__smp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_kernel\_\_smp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdbool.h>
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 21.1\_类型定义（Typedefs）

<a id="r_abc49de5bf9e70f48e39f41c413f7cc74"></a>

```c
typedef void(* smp_init_fn) (void *arg)
```

相关声明：[smp_init_fn](#abc49de5bf9e70f48e39f41c413f7cc74)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.2\_函数（Functions）

<a id="r_a33eb24503679583d853db1c4dc7e3812"></a>

```c
void k_smp_cpu_start (int id, smp_init_fn fn, void *arg)
```

相关声明：[k_smp_cpu_start](#a33eb24503679583d853db1c4dc7e3812)、[smp_init_fn](#abc49de5bf9e70f48e39f41c413f7cc74)。

启动 CPU（Start a CPU）。

<a id="r_a39b4f48857baef688ee646bac36c882d"></a>

```c
void k_smp_cpu_resume (int id, smp_init_fn fn, void *arg, bool reinit_timer, bool invoke_sched)
```

相关声明：[k_smp_cpu_resume](#a39b4f48857baef688ee646bac36c882d)、[smp_init_fn](#abc49de5bf9e70f48e39f41c413f7cc74)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

恢复此前已挂起的 CPU（Resume a Suspended CPU）。

## 21.3\_详细说明（Detailed Documentation）

<a id="abc49de5bf9e70f48e39f41c413f7cc74"></a>

### `smp_init_fn`

```c
typedef void(* smp_init_fn) (void *arg)
```

<a id="a39b4f48857baef688ee646bac36c882d"></a>

### `k_smp_cpu_resume()`

```c
void k_smp_cpu_resume ( int id, smp_init_fn fn, void * arg, bool reinit_timer, bool invoke_sched )
```

恢复此前已挂起的 CPU（Resume a Suspended CPU）。

本函数的工作方式类似 `k_smp_cpu_start`，但不会重新初始化内核用于跟踪目标 CPU 的内部数据。因此，必须先前已经为目标 CPU 调用过 `k_smp_cpu_start`，而且必须能够确认其已进入空闲／关闭状态（Idle/Off State）；该状态的检测由平台层（Platform Layers）提供。例如，平台层要求保留中断栈或空闲栈（Interrupt or Idle Stack）中的数据时，可使用本函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 目标 CPU 的 ID。 |
| `fn` | 恢复上下文（Context）之前要调用的函数。 |
| `arg` | 传递给 `fn` 的参数（Argument）。 |
| `reinit_timer` | 需要重新初始化定时器（Timer）时为 `true`。 |
| `invoke_sched` | CPU 启动后需要调用调度器（Scheduler）时为 `true`。 |

**说明（Note）**：**注意（Note）：**不得对正在运行的 CPU 使用本函数。目标 CPU 必须处于挂起状态（Suspended State），或架构允许其执行恢复流程（Resume Process）的特定状态。平台层（Platform Layers）必须提供这些状态的检测。

<a id="a33eb24503679583d853db1c4dc7e3812"></a>

### `k_smp_cpu_start()`

```c
void k_smp_cpu_start ( int id, smp_init_fn fn, void * arg )
```

启动 CPU（Start a CPU）。

本例程用于手动启动由 `id` 指定的 CPU。可以用它重启此前已停止或断电（Stopped or Powered Down）的 CPU，也可用于其他场景。CPU 完成初始化后，即可参与线程调度与执行（Thread Scheduling and Execution）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 目标 CPU 的 ID。 |
| `fn` | 允许调度器（Scheduler）运行之前要调用的函数。 |
| `arg` | 传递给 `fn` 的参数（Argument）。 |

**说明（Note）**：**注意（Note）：**不得对正在运行的 CPU 使用本函数。目标 CPU 必须处于关闭状态（Off State），或架构允许其执行上电流程（Power-up Process）的特定状态。平台层必须提供这些状态的检测。本函数会初始化每 CPU 内核结构（Per-CPU Kernel Structs），以及多处理器（MP）操作所需的定时器。如果不需要这些初始化，请使用 `k_smp_cpu_resume`。


## 21.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P426_smp.h_源码浏览.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [state(s)](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P020_zephyr__drivers__interrupt_controller__intc_xmc4xxx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__bluetooth__classic__l2cap_br.h_文件参考.md)
