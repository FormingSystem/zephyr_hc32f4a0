---
id: learning.zephyr-docs.observability.cpu-load
title: CPU负载
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/services/cpu_load/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="cpu-load"></a>

# 第7章\_CPU负载

原文：[CPU load](https://docs.zephyrproject.org/latest/services/cpu_load/index.html)。读取日期：2026-10-12，`latest`。

**中央处理器（Central Processing Unit，CPU）** 负载模块统计处理器处于非空闲状态的时间比例，通过 Kconfig 选择项 `CPU_LOAD_BACKEND` 选择两个测量后端之一。

## 7.1\_测量后端

`CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS` 使用调度器按 CPU 统计的运行时间推导负载，可跨架构使用并支持多 CPU。

`CONFIG_CPU_LOAD_BACKEND_IDLE_HOOK` 使用架构在 CPU 进入和退出空闲状态前后调用的钩子测量。它比调度统计后端开销更小，并可使用[计数器设备](../hardware/P017_计数器.md)提高精度；计数器路径仅支持单 CPU。任何提供空闲钩子、具有 `CONFIG_ARCH_HAS_CPU_IDLE_HOOKS` 的架构均可使用该后端。相比[线程分析器](P003_线程分析器.md)，它把中断上下文时间也计入，所以原文认为它更准确。此后端不依赖追踪子系统。

## 7.2\_读取与周期报告

`cpu_load_get()` 读取当前 CPU，`cpu_load_get_cpu()` 读取指定 CPU。两者返回千分比 `0…1000`，并支持重置测量窗口。用 `CPU_LOAD_PERMILLE_TO_PERCENT` 转成整数百分比。

也可通过日志周期性报告负载，周期由 `CONFIG_CPU_LOAD_LOG_PERIODICALLY` 设置。使用示例见[按需 CPU 调频](https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/on_demand/README.html#cpu_freq_on_demand)，接口见 [CPU 负载 API](P049_CPU负载接口.md)。

## 7.3\_使用计数器设备

空闲钩子后端默认使用 `k_cycle_get_32()`。需要更高精度时，启用 `CONFIG_CPU_LOAD_USE_COUNTER` 并在设备树 `/chosen` 中指定设备：

```dts
chosen {
  zephyr,cpu-load-counter = &counter_device;
};
```

> 译注：`counter_device` 是原例节点标签，需要对应实际可用的计数器；仅添加 chosen 引用不会创建计数器驱动。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：符号表](P006_符号表.md) · [本模块主线目录](../reading/observability.md) · [全部主线](../reading/README.md) · [下一篇：格式化输出](P008_格式化输出.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：符号表](P006_符号表.md) · [下一章：格式化输出](P008_格式化输出.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
