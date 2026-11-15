---
id: learning.zephyr-docs.portability.page-9
title: CMSISRTOS2定时同步示例
kind: reference
status: maintained
domains: [zephyr, portability, cmsis]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_CMSISRTOS2定时同步示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 9.1\_概述（Overview）

本示例展示如何使用 CMSIS RTOS V2 API 提供的定时器（Timer）和消息队列（Message Queue）。

原文描述：主线程创建一个可抢占线程（Preemptive Thread），由它向消息队列写入消息；定时器到期后，主线程读取消息。

译注——当前源码差异：本次核对的 `main.c` 没有创建这个额外的发送线程；名为 `send_msg_thread()` 的函数由 `main()` 直接调用，并不因为名字含 `thread` 就成为独立线程。主线程通过 `osMessageQueuePut()` 写入队列，定时器回调 `read_msg_callback()` 通过 `osMessageQueueGet()` 读取；不是主线程在定时器到期后执行读取。这里保留原文描述，并将实际调用关系分开说明。

## 9.2\_构建与运行（Building and Running Project）

本项目向控制台输出信息，原页给出的 QEMU 构建和运行命令如下：

```sh
west build -b qemu_x86 samples/philosophers
west build -t run
```

译注——原文路径纠错：原命令指向 `samples/philosophers`，不能用它运行本定时同步示例。当前示例位于 `samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/`，其 `prj.conf` 启用 `CONFIG_CMSIS_RTOS_V2`。在已准备好工具链和 QEMU 的 Zephyr 源码根目录，补充调用方式如下：

```sh
west build -d build/cmsis-v2-timer -b qemu_x86 samples/subsys/portability/cmsis_rtos_v2/timer_synchronization
west build -d build/cmsis-v2-timer -t run
```

补充命令依据当前官方源码路径编写，本次未执行构建或运行。

## 9.3\_示例输出（Sample Output）

```text
Wrote to message queue: 5
Read from message queue: 5

Wrote to message queue: 6
Read from message queue: 6

Wrote to message queue: 7
Read from message queue: 7

Wrote to message queue: 8
Read from message queue: 8

Wrote to message queue: 9
Read from message queue: 9

Wrote to message queue: 10
Read from message queue: 10

Wrote to message queue: 11
Read from message queue: 11

Wrote to message queue: 12
Read from message queue: 12

Wrote to message queue: 13
Read from message queue: 13

Wrote to message queue: 14
Read from message queue: 14

Wrote to message queue: 15
Read from message queue: 15

Sample execution successful
```

`Wrote to message queue` 表示已写入消息队列，`Read from message queue` 表示从队列读出；最后的 `Sample execution successful` 表示示例执行成功。

按 `CTRL+A`，再按 `x` 退出 QEMU。

译注——输出与时序：当前源码将队列容量设为 1，发送使用 `osWaitForever`，队列满时等待回调取走消息，因此可观察到写入和读取交替。当前初值为 5，计数器初值为 10，先发送一次，再在 `while (--counter)` 中发送 9 次，对应值 5～14；原页日志延续到 15，与当前代码不一致，译文保留该日志而不将其改写成实测结果。最后还会等待一次延时，让末条消息有机会被读取，再停止并删除定时器。


译注核对来源：[samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/src/main.c)、[samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/prj.conf)、[samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/tests.yaml)。

本仓库的[对应源码](../../../samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="cmsis-rtos-v2-sync"></a>
<a id="overview"></a>
<a id="building-and-running-project"></a>
<a id="sample-output"></a>

[上一章](P008_CMSISRTOS2哲学家就餐示例.md) · [返回大纲](大纲.md) · [下一章](P010_POSIX文档入口.md)
