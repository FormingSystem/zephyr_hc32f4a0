---
id: learning.zephyr-docs.api-file-supplement-reference.page-4
title: zephyr__arch__tricore__arch.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arch_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_arch\_\_tricore\_\_arch.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/arch_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TriCore专用内核接口（Kernel Interface）的头文件。

<a id="details"></a>

```c
#include <zephyr/arch/tricore/thread.h>
#include <zephyr/arch/tricore/exception.h>
#include <zephyr/arch/tricore/error.h>
#include <zephyr/arch/tricore/irq.h>
#include <zephyr/arch/tricore/cr.h>
#include <zephyr/arch/common/sys_io.h>
#include <zephyr/arch/common/sys_bitops.h>
#include <zephyr/arch/common/ffs.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

TriCore 专用内核接口头文件（Kernel Interface Header）。本头文件包含 TriCore 特定的内核接口，由内核接口的架构抽象头文件（Architecture-Abstraction Header）`include/zephyr/arch/cpu.h` 包含。


## 4.1\_原页交叉引用（Cross References）

- [zephyr/arch/tricore/thread.h](../api_source_supplement_reference/P012_thread.h_源码浏览.md)
- [zephyr/arch/tricore/exception.h](../api_source_configuration_reference/P114_exception.h_源码浏览.md)
- [zephyr/arch/tricore/error.h](../api_source_reference/P363_error.h_源码浏览.md)
- [zephyr/arch/tricore/irq.h](../api_source_supplement_reference/P010_irq.h_源码浏览.md)
- [zephyr/arch/tricore/cr.h](https://docs.zephyrproject.org/latest/doxygen/html/cr_8h_source.html)
- [zephyr/arch/common/sys_io.h](../device_reference/P024_通用架构IO头文件源码.md)
- [zephyr/arch/common/sys_bitops.h](../device_reference/P026_通用内存位操作头文件源码.md)
- [zephyr/arch/common/ffs.h](../numeric_reference/P007_置位扫描头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P013_arch.h_源码浏览.md)

<a id="header-details"></a>

---

[上一章](P003_zephyr__arch__tricore__syscall.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__interrupt-controller__bcm2835-armctrl.h_文件参考.md)
