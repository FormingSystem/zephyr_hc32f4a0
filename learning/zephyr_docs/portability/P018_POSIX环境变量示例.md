---
id: learning.zephyr-docs.portability.page-18
title: POSIX环境变量示例
kind: reference
status: maintained
domains: [zephyr, portability, posix]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/env/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_POSIX环境变量示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/env/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 18.1\_概述

本示例在 C 程序中调用 POSIX `setenv()` 函数设置若干环境变量（Environment Variable），随后打印全部环境变量。

当读者为 `ALERT` 环境变量设置新值时，程序将其打印到标准输出（Standard Output），然后调用 `unsetenv()` 清除该变量。

## 18.2\_构建与运行

本项目向控制台输出信息，可按下列方式在 QEMU 上构建和运行。

> 译注：以下 `west` 命令从所使用的 Zephyr 源码根目录执行，需要已有可用的 west 工作区、目标工具链及 QEMU 运行环境。路径相对于该源码根目录，不要求采用作者的仓库位置。

```bash
west build -b qemu_riscv32 samples/subsys/portability/posix/env
west build -t run
```

### 18.2.1\_示例输出

以下是某次特定 Zephyr 构建的输出示例。

```text
BOARD=qemu_riscv32
BUILD_VERSION=zephyr-v3.5.0-5372-g3a46f2d052c7
ALERT=
```

> 译注：`BOARD` 与 `BUILD_VERSION` 来自构建配置，版本字符串是官方页面保留的历史输出。当前程序用 `pthread_create()` 创建工作线程，先等待一秒供命令行解释器（Shell）启动，再设置变量并打印；不能据此把旧版本号当作当前构建结果。

### 18.2.2\_设置环境变量

下列 Shell 命令可创建新的环境变量，或更新已有变量关联的值。

本示例的 C 代码显示 `ALERT` 关联的值后，会立即取消该变量的设置。

```text
uart:~$ posix env set ALERT="Happy Friday!"
uart:~$ ALERT="Happy Friday!"
uart:~$ posix env set HOME="127.0.0.1"
uart:~$
```

> 译注：带 `uart:~$` 提示符的命令输入到运行中的 Zephyr Shell。这里的 `HOME` 是目标应用环境中的演示变量，不是让读者修改宿主终端的家目录变量。源码每秒检查一次 `ALERT`；只有读取成功且字符串非空时才打印并调用 `unsetenv()`。因此，“立即取消”指打印后的动作，不表示在输入命令的瞬间就完成检测。

### 18.2.3\_读取环境变量

下列 Shell 命令显示一个环境变量关联的值。

```text
uart:~$ posix env get BOARD
qemu_riscv32
```

不指定变量名时，下列命令显示全部环境变量及其关联值。

```text
uart:~$ posix env get
BOARD=qemu_riscv32
BUILD_VERSION=zephyr-v3.5.0-5372-g3a46f2d052c7
ALERT=
```

> 译注：官方页面分别展示各命令的输出，不应把这些片段视为严格连续的一次会话。按前面的设置步骤实际执行后，变量集合可能包含 `HOME`，而已处理的 `ALERT` 会被删除。这里保留原输出用于对照。

### 18.2.4\_取消环境变量设置

下列 Shell 命令用于删除环境变量。

```text
uart:~$ posix env unset BOARD
```


译注核对来源：[samples/subsys/portability/posix/env/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/env/src/main.c)、[samples/subsys/portability/posix/env/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/env/prj.conf)、[samples/subsys/portability/posix/env/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/env/tests.yaml)。

本仓库的[对应源码](../../../samples/subsys/portability/posix/env/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="posix-env"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>
<a id="setting-environment-variables"></a>
<a id="getting-environment-variables"></a>
<a id="unsetting-environment-variables"></a>

[上一章](P017_POSIX示例目录.md) · [返回大纲](大纲.md) · [下一章](P019_eventfd事件通知示例.md)
