---
id: learning.zephyr-docs.fatal-irq-reference.page-11
title: CPU空闲接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__idle__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_CPU空闲接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__idle__apis.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入致命错误、中断、CPU空闲与浮点上下文参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

<a id="details"></a>



<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.1\_函数（Functions）

<a id="r_ga7b25e1bed511a813b32fbd0f91b09356"></a>

```c
static void k_cpu_idle (void)
```

相关声明：[k_cpu_idle](#ga7b25e1bed511a813b32fbd0f91b09356)。

使 CPU 进入空闲状态（CPU Idle）。

<a id="r_gadf88ece6447b65b7d0d2f3a70ab4fe8f"></a>

```c
static void k_cpu_atomic_idle (unsigned int key)
```

相关声明：[k_cpu_atomic_idle](#gadf88ece6447b65b7d0d2f3a70ab4fe8f)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

以原子方式使 CPU 进入空闲状态（Atomic Idle）。

## 11.2\_详细说明（Detailed Documentation）

<a id="gadf88ece6447b65b7d0d2f3a70ab4fe8f"></a>

### `k_cpu_atomic_idle()`

```c
void k_cpu_atomic_idle ( unsigned int key)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel.h>
```

以原子方式使 CPU 进入空闲状态（Atomic Idle）。

与 `k_cpu_idle()` 类似，但调用时必须已经锁定中断。

使能中断与进入低功耗模式是原子的：处理器进入低功耗模式之前，不会出现中断已经使能的一段时间窗口。

从低功耗模式唤醒后，中断锁定状态会按相当于 `irq_unlock(key)` 的方式恢复。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 通过 `irq_lock()` 获得的中断锁定键。 |

<a id="ga7b25e1bed511a813b32fbd0f91b09356"></a>

### `k_cpu_idle()`

```c
void k_cpu_idle ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel.h>
```

使 CPU 进入空闲状态（CPU Idle）。

此函数让 CPU 保持空闲，直到某个事件将其唤醒。

在通常的系统中，只有空闲线程（Idle Thread）应负责使 CPU 空闲并触发任何形式的电源管理。不过，在更受限制的系统中，例如单线程系统，唯一的线程可能需要自行承担这一职责。

说明（Note）：某些架构会在函数返回前无条件解除中断屏蔽。

## 11.3\_源码定位与版本边界

相对源码定位：[include/zephyr/kernel.h](../../../include/zephyr/kernel.h)、[kernel/idle.c](../../../kernel/idle.c)、[arch/arm/core/cortex_m/cpu_idle.c](../../../arch/arm/core/cortex_m/cpu_idle.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。仓库源码使用相对链接；本地版本如有差异，应核对源码与来源摘要，不能把源码对照视为目标开发板已经实测。

> 译注——源码核对：CPU空闲（CPU Idle）接口直接进入架构空闲操作，与使当前线程阻塞并允许调度的k_sleep不同。调用者须遵守原页关于锁定、竞态和恢复中断状态的要求，不能把它作为普通应用延时接口。

> 译注——源码核对：本次Cortex-M非原子空闲路径采用WFI；原子空闲路径采用WFE，并在唤醒后按传入键恢复中断状态。架构基线、BASEPRI／PRIMASK处理和SoC钩子会影响具体步骤，钩子还可能使等待指令被跳过。因此接口调用不保证进入特定深度的低功耗状态或某个固定唤醒延迟。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 11.4\_原页交叉引用（Cross References）

- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [irq_unlock(key)](P007_中断服务接口.md#ga646045943b3b2a130738bcc48867bf57)
- [irq_lock()](P007_中断服务接口.md#ga19fdde73c3b02fcca6cf1d1e67631228)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_中断卸载头文件源码.md) · [返回大纲](大纲.md) · [下一章](P012_浮点上下文接口.md)
