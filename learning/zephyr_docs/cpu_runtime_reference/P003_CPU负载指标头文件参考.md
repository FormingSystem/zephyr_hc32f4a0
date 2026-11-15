---
id: learning.zephyr-docs.cpu-runtime-reference.page-3
title: CPU负载指标头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cpu__load__metric_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_CPU负载指标头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cpu__load__metric_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入 CPU 负载、线程分析器、函数插桩源码和线程运行统计参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

已弃用的 CPU 负载指标（CPU Load Metric）头文件。

<a id="details"></a>

```c
#include <zephyr/sys/cpu_load.h>
```

查看此文件的源码。

已弃用的 CPU 负载指标头文件。

**已弃用（Deprecated）**：请改为包含 `<zephyr/sys/cpu_load.h>`。`cpu_load_metric_get()` 函数仍保留在该头文件中，作为 `cpu_load_get_cpu()` 的已弃用包装函数（Wrapper）。

## 3.1\_源码定位与版本边界

相对源码定位：[CPU负载头文件](../../../include/zephyr/sys/cpu_load.h)、[CPU负载实现](../../../lib/os/cpu_load/cpu_load.c)、[测量后端配置](../../../lib/os/cpu_load/Kconfig)、[线程分析器](../../../subsys/debug/thread_analyzer/thread_analyzer.c)、[线程类型头文件](../../../include/zephyr/kernel/thread.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注依据本批保存摘要的官方 main 文件，独立于官方正文。源码使用相对路径定位；本地源码版本若不同，应以来源记录中的版本边界核对。

> 译注——源码核对：cpu_load_get_cpu和cpu_load_get返回千分比（Per Mille）0～1000，失败返回负errno；先检查负值再转换单位。CPU_LOAD_PERMILLE_TO_PERCENT只是除以10，整数输入会舍去小数，不负责错误检查。旧cpu_load_metric_get返回整数百分比，并固定传入reset=true，迁移接口时单位和采样窗口都要明确。

> 译注——源码核对：兼容头文件（Compatibility Header）现在只包含zephyr/sys/cpu_load.h，不提供独立的测量实现。已弃用不等于已删除；旧包装函数仍位于新头文件中。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.2\_原页交叉引用（Cross References）

- [zephyr/sys/cpu_load.h](P002_CPU负载头文件源码.md)
- [查看此文件的源码](P004_CPU负载指标头文件源码.md)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000102)
- [zephyr/sys/cpu_load.h](P001_CPU负载头文件参考.md)
- [cpu_load_metric_get()](../observability/P049_CPU负载接口.md#ga3333539cf7d8a6916cbbec9cd1f5bf59)
- [cpu_load_get_cpu()](../observability/P049_CPU负载接口.md#gab8e384170b8fc3c253a30e3490ebb34f)

<a id="header-details"></a>

---

[上一章](P002_CPU负载头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_CPU负载指标头文件源码.md)
