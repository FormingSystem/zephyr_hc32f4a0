---
id: learning.zephyr-docs.portability.page-19
title: eventfd事件通知示例
kind: reference
status: maintained
domains: [zephyr, portability, posix]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/eventfd/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_eventfd事件通知示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/eventfd/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 19.1\_概述

本示例展示如何使用 POSIX `eventfd()` 函数创建可用于事件通知（Event Notification）的文件描述符（File Descriptor）。程序对返回的描述符执行写入／读取（write/read）调用，并将写入和读取的值输出到控制台。

> 译注：本段沿用官方页面的分类名称。当前官方 `tests.yaml` 将其描述为扩展 POSIX（Linux）API 示例；不能因为它位于 POSIX 示例目录，就认为所有符合 POSIX 的宿主都提供 `eventfd()`。源码调用 `eventfd(0, 0)`，依次写入 1、2、3、4，然后读取累计值 10；`writer()` 和 `reader()` 由主函数先后调用，并未创建两个并发线程。

## 19.2\_构建与运行

本项目向控制台输出信息，可按下列方式在 QEMU 上构建和运行。

> 译注：从所使用的 Zephyr 源码根目录执行 `west` 命令，前提是已有目标工具链及 QEMU 环境。示例配置启用 `CONFIG_EVENTFD`，并为其当前实现依赖的网络 API 提供配置；此处不要求读者连接外部事件服务器。

```bash
west build -b qemu_x86 samples/subsys/portability/posix/eventfd
west build -t run
```

作为对照，如果宿主操作系统（Host OS）符合 POSIX，例如 Linux，也可以直接为宿主构建：

```bash
cd samples/subsys/portability/posix/eventfd
make -f Makefile.host
```

`make` 的输出文件位于 `samples/subsys/portability/posix/eventfd/build`。

> 译注：宿主路线需使用提供 `eventfd()`、C 编译器和 `make` 的环境；上面的 `cd` 同样从 Zephyr 源码根目录出发。按当前 `Makefile.host`，`build` 是目录，实际生成文件为该目录中的 `eventfd`，即样例目录下的 `build/eventfd`。它是宿主程序，与 `west` 构建的 Zephyr 镜像不同。

## 19.3\_示例输出

```text
Writing 1 to efd
Writing 2 to efd
Writing 3 to efd
Writing 4 to efd
Completed write loop
About to read
Read 10 (0xa) from efd
Finished
```

> 译注：输出依次表示向描述符写入四个值、完成写循环、准备读取、读到十进制 10（十六进制 `0xa`），最后结束。这里是官方预期输出，不是本批翻译过程中运行生成的日志。


译注核对来源：[samples/subsys/portability/posix/eventfd/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/eventfd/src/main.c)、[samples/subsys/portability/posix/eventfd/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/eventfd/prj.conf)、[samples/subsys/portability/posix/eventfd/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/eventfd/tests.yaml)、[samples/subsys/portability/posix/eventfd/Makefile.host](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/eventfd/Makefile.host)。

本仓库的[对应源码](../../../samples/subsys/portability/posix/eventfd/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="posix-eventfd"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>

[上一章](P018_POSIX环境变量示例.md) · [返回大纲](大纲.md) · [下一章](P020_系统时间与SNTP示例.md)
