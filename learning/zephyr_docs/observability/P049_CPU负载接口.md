---
id: learning.zephyr-docs.observability.debugapi-0
title: CPU负载接口
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__load.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第49章\_CPU负载接口

原文：[group__cpu__load](https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__load.html)。读取日期：2026-10-13，`latest`。

## 49.1\_测量模型与头文件

本模块监测**中央处理器（Central Processing Unit，CPU）负载**，即CPU处于非空闲状态的时间占比。通过Kconfig选择两种测量后端（Backend）：

| 配置项 | 后端特性 |
| --- | --- |
| [`CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS) | 根据调度器的逐CPU运行时间统计（Runtime Statistics）计算负载，可跨架构移植并支持多个CPU |
| [`CONFIG_CPU_LOAD_BACKEND_IDLE_HOOK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_BACKEND_IDLE_HOOK) | 使用架构的空闲钩子（Idle Hook）测量，开销较低；可选硬件计数器提高精度，但硬件计数器路径仅支持单CPU。适用于发出空闲钩子、具有 [`CONFIG_ARCH_HAS_CPU_IDLE_HOOKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_CPU_IDLE_HOOKS) 能力的架构 |

无论采用哪种后端，负载读取接口均以**千分比（Per Mille）**报告，范围0～1000。

```c
#include <zephyr/sys/cpu_load.h>
```

## 49.2\_千分比转百分比

<a id="ga21c1e9efe2f4ba8f40a3e9dd1f32b52e"></a>

宏 `CPU_LOAD_PERMILLE_TO_PERCENT(permille)` 将千分比CPU负载转换为整数百分比（Whole Percent）。官方宏值为：

```c
((permille) / 10)
```

## 49.3\_读取负载

<a id="gab8e384170b8fc3c253a30e3490ebb34f"></a>

<a id="gaf44501a292aeef7749b68c706b34119f"></a>

```c
int cpu_load_get_cpu(unsigned int cpu_id, bool reset);
int cpu_load_get(bool reset);
```

[`cpu_load_get_cpu()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__load.html#gab8e384170b8fc3c253a30e3490ebb34f) 获取参数 `cpu_id` 指定CPU索引的负载，[`cpu_load_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__load.html#gaf44501a292aeef7749b68c706b34119f) 获取当前CPU负载。参数 `reset` 控制读取后是否重置测量窗口（Measurement Window）。

两者成功均返回0～1000的千分比负载；失败返回负的错误码（Negative errno Code）。

## 49.4\_空闲钩子与周期报告

<a id="ga28a73232eb45cdf6ce057e1e4c84190d"></a>

<a id="ga8a8c97914a72b6eb5a7e1862710a0c6d"></a>

<a id="gabc95920fb1a666b1496618cf5afbfbff"></a>

```c
void cpu_load_on_enter_idle(void);
void cpu_load_on_exit_idle(void);
void cpu_load_log_control(bool enable);
```

[`cpu_load_on_enter_idle()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__load.html#ga28a73232eb45cdf6ce057e1e4c84190d) 在进入CPU空闲时调用，[`cpu_load_on_exit_idle()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__load.html#ga8a8c97914a72b6eb5a7e1862710a0c6d) 在退出空闲时调用。两者仅由空闲钩子后端使用，从架构空闲路径调用。

[`cpu_load_log_control()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__load.html#gabc95920fb1a666b1496618cf5afbfbff) 控制定期CPU负载报告。报告日志默认启用；`enable=true` 启用，`enable=false` 禁用。

## 49.5\_负载阈值回调

回调（Callback）类型与注册函数如下：

<a id="ga83f2e3099de11b8e6b66395ae69f394a"></a>

<a id="gaec80c70d8dd6ea130edde48618ed2463"></a>

```c
typedef void (*cpu_load_cb_t)(uint8_t percent);
int cpu_load_cb_reg(cpu_load_cb_t cb, uint8_t threshold_percent);
```

可选注册负载达到或超过阈值时触发的回调。`cb` 是回调函数指针，传入 `NULL` 取消回调。参数 `threshold_percent` 为0～100的百分比阈值；负载大于或等于它时触发。

成功注册或取消返回 `0`；阈值无效返回 `-EINVAL`。

## 49.6\_已弃用的百分比接口

<a id="ga3333539cf7d8a6916cbbec9cd1f5bf59"></a>

```c
static inline int cpu_load_metric_get(int cpu_id);
```

该函数取得指定CPU的百分比负载。`cpu_id` 为CPU索引，成功返回0～100，失败返回负错误码。

**此接口已弃用（Deprecated），改用 [`cpu_load_get_cpu()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cpu__load.html#gab8e384170b8fc3c253a30e3490ebb34f)。**新接口返回千分比，原接口返回百分比，替换时必须同时处理单位差异。

---

[上一章：STMESP日志解复用头文件](P048_STMESP日志解复用头文件.md) · [下一章：线程分析器接口](P050_线程分析器接口.md) · [返回大纲](大纲.md)
