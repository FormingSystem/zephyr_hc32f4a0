---
id: learning.zephyr-docs.testing.page-9
title: Pytest测试Shell应用
kind: reference
status: maintained
domains: [zephyr, testing, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/testsuite/pytest/shell/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="pytest_shell"></a>

# 第9章\_Pytest测试Shell应用

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/testsuite/pytest/shell/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/testsuite/pytest/shell/README.rst/..)。

<a id="overview"></a>

## 9.1 概述（Overview）

本示例工程展示如何使用与Twister测试运行器（Test Runner）集成的pytest测试框架。

一个简单应用提供基本的Zephyr命令行接口（Shell）。Twister先构建应用，再在子进程中调用pytest，执行`pytest/test_shell.py`中的测试。第一个测试验证`help`命令是否给出有效响应，第二个测试验证应用能否返回所用内核版本的信息。这两个测试都使用`pytest-twister-harness`插件定义的`shell`测试夹具（Fixture）。关于插件的更多信息，参见[与pytest集成的说明](../twister/P003_集成pytest测试框架.md#integration-with-pytest)。

<a id="requirements"></a>

## 9.2 要求（Requirements）

具有通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）控制台的开发板或目标环境，可以是硬件、`native_sim`或QEMU。

<a id="building-and-running"></a>

## 9.3 构建与运行（Building and Running）

通过Twister构建并运行示例：

> 译注——命令前提：下例针对native_sim，在已准备Zephyr开发依赖、native_sim工具链及pytest测试插件的Linux Bash中，以Zephyr源码根目录执行。开头的`$`是终端提示符，不属于命令。Twister负责构建和运行测试；若构建、启动或测试失败，应检查对应阶段的日志，不能只根据应用启动成功认定测试通过。

```sh
$ ./scripts/twister -vv --platform native_sim -T samples/subsys/testsuite/pytest/shell
```

<a id="sample-output"></a>

### 9.3.1 示例输出（Sample Output）

```text
...
samples/subsys/testsuite/pytest/shell/pytest/test_shell.py::test_shell_print_help
INFO: send "help" command
DEBUG: #: uart:~$ help
DEBUG: #: Please press the <Tab> button to see all available commands.
DEBUG: #: You can also use the <Tab> button to prompt or auto-complete all commands or its subcommands.
DEBUG: #: You can try to call commands with <-h> or <--help> parameter for more information.
DEBUG: #: Shell supports following meta-keys:
DEBUG: #: Ctrl + (a key from: abcdefklnpuw)
DEBUG: #: Alt  + (a key from: bf)
DEBUG: #: Please refer to shell documentation for more details.
DEBUG: #: Available commands:
DEBUG: #: clear    :Clear screen.
DEBUG: #: device   :Device commands
DEBUG: #: devmem   :Read/write physical memory
DEBUG: #:             Usage:
DEBUG: #:             Read memory at address with optional width:
DEBUG: #:             devmem address [width]
DEBUG: #:             Write memory at address with mandatory width and value:
DEBUG: #:             devmem address <width> <value>
DEBUG: #: help     :Prints the help message.
DEBUG: #: history  :Command history.
DEBUG: #: kernel   :Kernel commands
DEBUG: #: rem      :Ignore lines beginning with 'rem '
DEBUG: #: resize   :Console gets terminal screen size or assumes default in case the
DEBUG: #:             readout fails. It must be executed after each terminal width change
DEBUG: #:             to ensure correct text display.
DEBUG: #: retval   :Print return value of most recent command
DEBUG: #: shell    :Useful, not Unix-like shell commands.
DEBUG: #: uart:~$
INFO: response is valid
PASSED
samples/subsys/testsuite/pytest/shell/pytest/test_shell.py::test_shell_print_version
INFO: send "kernel version" command
DEBUG: #: uart:~$ kernel version
DEBUG: #: Zephyr version 3.5.99
DEBUG: #: uart:~$
INFO: response is valid
PASSED
...
```

> 译注——实际断言与配置：当前`pytest/test_shell.py`检查`help`返回结果中存在`Available commands:`，并检查版本响应某行包含`Zephyr version`，没有断言版本必须等于原日志中的3.5.99。当前`tests.yaml`还包含关闭VT100颜色的pytest变体和独立的Shell测试工具（Shell Harness）变体；后者通过命令及匹配表达式检查输出，与上面两个pytest函数分别配置。原日志中的`PASSED`是官方示例，不表示本文已执行这些测试。


> 译注——配置与实现依据：[samples/subsys/testsuite/pytest/shell/tests.yaml](../../../samples/subsys/testsuite/pytest/shell/tests.yaml)、[samples/subsys/testsuite/pytest/shell/pytest/test_shell.py](../../../samples/subsys/testsuite/pytest/shell/pytest/test_shell.py)。本地参照采用相对链接，其版本可能与所核对的官方main快照不同，文件摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/subsys/testsuite/pytest/shell/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/testsuite/pytest/shell/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/testsuite/pytest/shell/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/subsys/testsuite/pytest/shell/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P008_基准测试示例.md) · [返回大纲](大纲.md)
