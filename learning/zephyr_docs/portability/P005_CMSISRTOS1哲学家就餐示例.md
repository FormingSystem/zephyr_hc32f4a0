---
id: learning.zephyr-docs.portability.page-5
title: CMSISRTOS1哲学家就餐示例
kind: reference
status: maintained
domains: [zephyr, portability, cmsis]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/portability/cmsis_rtos_v1/philosophers/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_CMSISRTOS1哲学家就餐示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/portability/cmsis_rtos_v1/philosophers/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 5.1\_概述（Overview）

本示例使用 CMSIS RTOS V1 API 解决哲学家就餐问题（Dining Philosophers Problem），这是经典的多线程同步（Multi-Thread Synchronization）问题。原文说明，此实现展示不同优先级的可抢占线程（Preemptible Thread）与协作式线程（Cooperative Thread），以及 Zephyr 中 CMSIS RTOS V1 实现提供的互斥量（Mutex）、信号量（Semaphore）和线程睡眠（Thread Sleeping）。

哲学家总是先取编号较小的叉子，即先 `f1` 再 `f2`；用完按相反顺序归还，即先 `f2` 再 `f1`。拿到两把叉子后进入进餐状态（EATING），否则处于思考状态（THINKING）。显示中还包含过渡状态，例如饥饿但拿不到叉子时的 STARVING，以及已持有一把叉子、等待另一把时的 HOLDING ONE FORK。

每位哲学家都会随机交替进入 EATING 和 THINKING 状态。

## 5.2\_构建与运行（Building and Running）

本项目向控制台输出信息，原页给出的 QEMU 构建及运行命令如下：

```sh
west build -b qemu_x86 samples/philosophers
west build -t run
```

译注——原文路径纠错：上述 `samples/philosophers` 是通用哲学家示例目录，不是本 CMSIS-RTOS1 示例。当前官方源码和 `prj.conf` 位于 `samples/subsys/portability/cmsis_rtos_v1/philosophers/`，配置启用 `CONFIG_CMSIS_RTOS_V1`。准备好对应工具链和 QEMU 后，在 Zephyr 源码根目录可按下列补充命令选择正确示例；构建目录采用相对位置，避免沿用另一应用的构建缓存。

```sh
west build -d build/cmsis-v1-philosophers -b qemu_x86 samples/subsys/portability/cmsis_rtos_v1/philosophers
west build -d build/cmsis-v1-philosophers -t run
```

这些是依据源码补充的命令，原文代码块完整保留；本次未执行构建或模拟运行。

## 5.3\_示例输出（Sample Output）

```text
Philosopher 0 [C:-2]  THINKING [  500 ms ]
Philosopher 1 [C:-1]  THINKING [  375 ms ]
Philosopher 2 [P: 0]  THINKING [  575 ms ]
Philosopher 3 [P: 1]   EATING  [  525 ms ]
Philosopher 4 [P: 2]  THINKING [  800 ms ]
Philosopher 5 [P: 3]   EATING  [  625 ms ]

Demo Description
----------------
An implementation of a solution to the Dining Philosophers
problem (a classic multi-thread synchronization problem) using
CMSIS RTOS V1 APIs. This particular implementation demonstrates the
usage of multiple preemptible threads of differing
priorities, as well as semaphores and thread sleeping.
```

输出中的 `Demo Description` 说明该程序用 CMSIS RTOS V1 API 演示哲学家就餐、多种优先级的可抢占线程、信号量及线程睡眠。`Philosopher` 表示哲学家线程，方括号中包含调度／优先级标签和本次状态持续时间；EATING 为进餐，THINKING 为思考，HOLDING ONE FORK 为持有一把叉子。原日志中的调度标签与数值保留供对照，实际值以所用兼容层及运行版本为准。

按 `CTRL+A`，再按 `x` 退出 QEMU。

译注——源码跟踪：示例默认创建 6 个哲学家线程，先取全局编号较小的叉子，使最后一个线程先取 0 号叉子，避免形成相反的资源获取顺序。当前源码在定义 `FORKS`、`SEMAPHORES` 和 `MUTEXES` 之前就包含 `phil_obj_abstract.h`；若这些宏未由构建参数预先定义，头文件中的 `#if FORKS == SEMAPHORES` 会按两个未定义标识符均为 0 判断为真。因此，不能只看后面的 `#define FORKS MUTEXES` 或源文件注释就断言编入的是互斥量分支，需检查预处理顺序和实际构建定义。原文介绍及日志不等于所有可选编译分支都已实测。修改 `NUM_PHIL` 还需检查对应对象及线程属性数组，不能仅改数量宏就认为任意数量均可用。


译注核对来源：[samples/subsys/portability/cmsis_rtos_v1/philosophers/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/cmsis_rtos_v1/philosophers/src/main.c)、[samples/subsys/portability/cmsis_rtos_v1/philosophers/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/portability/cmsis_rtos_v1/philosophers/prj.conf)、[samples/subsys/portability/cmsis_rtos_v1/philosophers/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/portability/cmsis_rtos_v1/philosophers/tests.yaml)、[samples/subsys/portability/cmsis_rtos_v1/philosophers/src/phil_obj_abstract.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/portability/cmsis_rtos_v1/philosophers/src/phil_obj_abstract.h)。

本仓库的[对应源码](../../../samples/subsys/portability/cmsis_rtos_v1/philosophers/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="cmsis-rtos-v1"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>

[上一章](P004_CMSISRTOS1示例目录.md) · [返回大纲](大纲.md) · [下一章](P006_CMSISRTOS1定时同步示例.md)
