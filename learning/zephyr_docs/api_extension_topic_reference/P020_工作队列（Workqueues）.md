---
id: learning.zephyr-docs.api-extension-topic-reference.page-20
title: 工作队列（Workqueues）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__workqueue.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_工作队列（Workqueues）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__workqueue.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可选择将元素的工作卸载到共享工作线程上。

<a id="details"></a>

可选地将元素工作（Element Work）卸载到共享工作线程（Shared Worker Threads）。默认情况下，哪个线程将缓冲区推送给元素，元素就在哪个线程上执行工作，因此整条处理链会在流水线线程（Pipeline Thread）上从头到尾执行。工作适合并行处理的元素可以将工作提交到这个共享池（Shared Pool），由工作线程执行，从而使对称多处理（SMP）目标上的多个元素同时推进。该池采用 Zephyr P4WQ，因此每个工作项（Work Item）携带自己的优先级（Priority）和截止时间（Deadline），而不继承固定的队列优先级。只有启用 `CONFIG_MPIPE_WORKQUEUE` 时，此池才存在。

<a id="header-files"></a>
<a id="files"></a>

## 20.1\_文件（Files）

<a id="r_mpipe_5Fworkqueue_2Eh"></a>

```c
file mpipe_workqueue.h
```

相关声明：[mpipe_workqueue.h](../api_file_configuration_reference/P057_zephyr__mpipe__mpipe_workqueue.h_文件参考.md)。

用于元素级工作并行（Element-Level Work Parallelism）的共享P4WQ池。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 20.2\_变量（Variables）

<a id="r_gad175f6e485cce50815afc57ec5c46f55"></a>

```c
struct k_p4wq *const mpipe_p4wq
```

相关声明：[k_p4wq](../p4_work_reference/P003_P4工作队列结构.md)、[mpipe_p4wq](#gad175f6e485cce50815afc57ec5c46f55)。

共享的 mpipe P4WQ 池实例（Shared Pool Instance）。

## 20.3\_详细说明（Detailed Documentation）

<a id="gad175f6e485cce50815afc57ec5c46f55"></a>

### `mpipe_p4wq`

```c
struct k_p4wq* const mpipe_p4wq
```

声明属性：`extern`。

```c
#include <zephyr/mpipe/mpipe_workqueue.h>
```

共享的 mpipe P4WQ 池实例（Shared Pool Instance）。

进程范围的 P4WQ 池（Process-Wide Pool），由所有需要并行执行内部工作的元素（Elements）共享。


## 20.4\_原页交叉引用（Cross References）

- [mpipe_workqueue.h](../api_file_configuration_reference/P057_zephyr__mpipe__mpipe_workqueue.h_文件参考.md)
- [k_p4wq](../p4_work_reference/P003_P4工作队列结构.md)
- [CONFIG_MPIPE_WORKQUEUE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_WORKQUEUE)

<a id="header-details"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P019_MH-Z19B API主题.md) · [返回大纲](大纲.md) · [下一章](P021_nPM10xx OTP 接口.md)
