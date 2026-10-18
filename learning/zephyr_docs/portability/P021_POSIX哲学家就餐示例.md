---
id: learning.zephyr-docs.portability.page-21
title: POSIX哲学家就餐示例
kind: reference
status: maintained
domains: [zephyr, portability, posix]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/philosophers/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_POSIX哲学家就餐示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/philosophers/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 21.1\_概述

本示例使用[可移植操作系统接口（Portable Operating System Interface，POSIX）API](P010_POSIX文档入口.md#posix-support) 实现 Zephyr 的[哲学家就餐（Dining Philosophers）示例](../basic_samples/P030_哲学家就餐示例.md#dining-philosophers)。源码位于 `samples/subsys/portability/posix/philosophers`。

> 译注：当前实现用 POSIX 线程（POSIX Threads）表示哲学家，以 `pthread_mutex_t` 互斥量（Mutex）表示叉子。每个线程先取得编号较小的叉子，再取得编号较大的叉子；最后一个哲学家先取 0 号叉子，以打破所有线程同时按环形顺序等待的条件。当前 `prj.conf` 配置六个线程和六把互斥量，并通过编译期断言检查这些资源数量一致。

## 21.2\_构建与运行

本项目向控制台输出信息，可按下列方式在 QEMU 上构建和运行。

> 译注：从所使用的 Zephyr 源码根目录执行，需要已经配置好目标工具链和 QEMU 运行环境；命令中的路径相对于源码根目录。

```bash
west build -b qemu_riscv64 samples/subsys/portability/posix/philosophers
west build -t run
```

### 21.2.1\_示例输出

```text
Philosopher 0 [P: 3]  HOLDING ONE FORK
Philosopher 1 [P: 2]  HOLDING ONE FORK
Philosopher 2 [P: 1]  EATING  [ 1900 ms ]
Philosopher 3 [P: 0]  THINKING [ 2500 ms ]
Philosopher 4 [C:-1]  THINKING [ 2200 ms ]
Philosopher 5 [C:-2]  THINKING [ 1700 ms ]
```

按 `CTRL+A x` 退出 QEMU。

> 译注：即先按 Ctrl+A，再按 x。输出中的 `P` 为抢占式（Preemptible）、`C` 为协作式（Cooperative）调度类别，数字是程序转换后显示的 Zephyr 优先级。`HOLDING ONE FORK`、`EATING`、`THINKING` 分别表示持有一把叉子、正在进餐、正在思考。原页保留的是历史输出；本次读取的源码用 `get_random_delay(..., 25)` 产生 25～800 ms 的延迟，不能要求与旧日志中的 1900 ms、2500 ms 等数值一致。

## 21.3\_调试

与原始哲学家示例一样，POSIX 版本也默认启用 [`CONFIG_DEBUG_THREAD_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_THREAD_INFO)。

```bash
west build -b <board_name> samples/philosophers
west debug
```

> 译注：原页此处仍写 `samples/philosophers`，它会选择原始示例。若要调试本章 POSIX 版本，应改用下面的相对路径；将 `<board_name>` 替换为已准备调试条件的目标板，并确保对应调试运行器（Debug Runner）可用。保留上面的原命令是为了对照官方页面，不表示两者是同一个应用。

```bash
west build -b <board_name> samples/subsys/portability/posix/philosophers
west debug
```

## 21.4\_补充信息

更多信息请参阅[哲学家就餐示例](../basic_samples/P030_哲学家就餐示例.md#dining-philosophers)。


译注核对来源：[samples/subsys/portability/posix/philosophers/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/philosophers/src/main.c)、[samples/subsys/portability/posix/philosophers/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/philosophers/prj.conf)、[samples/subsys/portability/posix/philosophers/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/philosophers/tests.yaml)、[samples/subsys/portability/posix/philosophers/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/philosophers/Kconfig)。

本仓库的[对应源码](../../../samples/subsys/portability/posix/philosophers/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="posix-philosophers"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>
<a id="debugging"></a>
<a id="additional-information"></a>

[上一章](P020_系统时间与SNTP示例.md) · [返回大纲](大纲.md) · [下一章](P022_uname系统信息示例.md)
