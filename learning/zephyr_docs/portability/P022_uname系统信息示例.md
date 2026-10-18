---
id: learning.zephyr-docs.portability.page-22
title: uname系统信息示例
kind: reference
status: maintained
domains: [zephyr, portability, posix]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/uname/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_uname系统信息示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/uname/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 22.1\_概述

本示例调用 POSIX [`uname()`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/uname.html) 函数获取系统信息（System Information），并将其输出到控制台。此外，示例将 `uname` 加入命令行解释器（Shell），根据命令选项显示相应系统信息。

## 22.2\_构建与运行

本项目向控制台输出信息，可按下列方式在 QEMU 上构建和运行。

> 译注：从所使用的 Zephyr 源码根目录执行，前提是已经准备目标工具链与 QEMU。路径不绑定作者机器的仓库位置。

```bash
west build -b qemu_x86 samples/subsys/portability/posix/uname
west build -t run
```

作为对照，如果宿主操作系统（Host OS）符合 POSIX，例如 Linux，也可以直接为宿主构建：

```bash
cd samples/subsys/portability/posix/uname
make -f Makefile.host
```

`make` 的输出文件位于 `samples/subsys/portability/posix/uname/build`。

> 译注：宿主路线需要 C 编译器和 `make`；上述 `cd` 从源码根目录出发。当前 `Makefile.host` 将程序生成在样例目录下的 `build/uname`。该程序读取宿主系统信息，不会启动 Zephyr Shell，也不会把宿主系统报告成 Zephyr。

## 22.3\_示例输出

```text
Printing everything in utsname...
sysname[7]: Zephyr
nodename[7]: zephyr
release[13]: 3.5.99
version[61]: zephyr-v3.5.0-3515-g10156f5f1d9c Jan  9 2024 22:23:04
machine[4]: x86


uart:~$ uname -a
Zephyr zephyr 3.5.99 zephyr-v3.5.0-3515-g10156f5f1d9c Jan  9 2024 22:23:04 x86 qemu_x86
uart:~$ uname -smi
Zephyr x86 qemu_x86
```

> 译注：`struct utsname` 中的 `sysname`、`nodename`、`release`、`version` 和 `machine` 分别表示系统名称、节点名称、发行版本、版本信息和机器类型。源码使用 `sizeof` 打印方括号中的值，它表示对应成员数组的容量，不能当作实际字符串长度。版本、日期、机器和开发板名称是原页的历史示例值。

> 译注：当前官方 Shell 实现通过 `POSIX_CMD_ADD` 把命令注册到 `posix` 子命令组，实际入口如下。原页旧日志中的裸 `uname` 命令保留用于版本对照。

```text
uart:~$ posix uname -a
uart:~$ posix uname -smi
```

`-a` 选择实现提供的全部信息；`-s` 选择内核名称（Kernel Name），`-m` 选择机器硬件名称（Machine Hardware Name），`-i` 选择硬件平台（Hardware Platform），当前实现从 `CONFIG_BOARD` 取得平台名称。这一段为根据官方源码补充的译注。


译注核对来源：[samples/subsys/portability/posix/uname/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/uname/src/main.c)、[samples/subsys/portability/posix/uname/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/uname/prj.conf)、[samples/subsys/portability/posix/uname/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/uname/tests.yaml)、[samples/subsys/portability/posix/uname/Makefile.host](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/uname/Makefile.host)、[subsys/portability/posix/shell/uname.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/portability/posix/shell/uname.c)、[subsys/portability/posix/shell/posix_shell.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/portability/posix/shell/posix_shell.h)、[subsys/portability/posix/shell/posix_shell.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/portability/posix/shell/posix_shell.c)。

本仓库的[对应源码](../../../samples/subsys/portability/posix/uname/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="posix-uname"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>

[上一章](P021_POSIX哲学家就餐示例.md) · [返回大纲](大纲.md) · [下一章](P023_可移植性示例目录.md)
