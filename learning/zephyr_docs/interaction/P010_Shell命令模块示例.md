---
id: learning.zephyr-docs.interaction.page-10
title: Shell命令模块示例
kind: reference
status: maintained
domains: [zephyr, shell, input]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/shell/shell_module/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Shell命令模块示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/shell/shell_module/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 10.1\_概述

这个简单应用演示如何通过 Shell API 编写和注册命令。

| 功能 | 原示例的演示方式 |
| --- | --- |
| 注册静态命令（Static Commands） | `version` 打印内核版本 |
| 按条件注册命令（Conditional Registration） | `login`、`logout` 的注册取决于 [`CONFIG_SHELL_START_OBSCURED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_START_OBSCURED) |
| 注册动态命令（Dynamic Commands） | 参见 `dynamic` 命令及 [`samples/subsys/shell/shell_module/src/dynamic_cmd.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/src/dynamic_cmd.c) |
| 注册字典命令（Dictionary Commands） | `dictionary` 实现一组字典子命令 |
| 设置旁路回调（Bypass Callback） | `bypass` 演示旁路处理 |
| 设置登录命令（Login Command） | `login`、`logout` 分别实现登录和退出机制 |
| 用星号隐藏用户输入（Obscured Input） | `login`、`logout` 演示该功能的启用和关闭 |

译注：最后一项按原文说明保留；当前登录代码在成功登录后调用 `shell_obscure_set(sh, false)` 关闭隐藏，在退出时设置为 `true`，重新进入隐藏密码的登录状态。源码中的默认密码及比较函数仅为演示，源码也明确不推荐用于生产环境；星号显示本身不等于传输加密。

## 10.2\_远程Shell

可以通过系统构建（System Build，sysbuild）生成远程 Shell（Remote Shell）示例。它允许通过主核 Shell 接口执行远程核命令；`remote_shell` 作为远程核命令树的根命令。

译注：远程核模式需要所选多核目标及相应 sysbuild／设备树配置支持；下面普通 QEMU 和单板构建命令不会自动证明远程核路径已启用。

## 10.3\_要求与构建

目标需配置 Shell 接口，并通过其任一后端（Backend）暴露接口。本示例可针对多个平台构建。

### 仿真目标（Emulation Targets）

以下主机命令在 Zephyr 源码根目录执行，构建 `qemu_x86` 应用；已有工具链及依赖模块是前提：

```sh
west build -b qemu_x86 samples/subsys/shell/shell_module
west build -t run
```

运行后控制台显示 Shell 接口和提示符，此时即可交互。

### 实板（On-Hardware）

原文给出的实板命令如下。目标板及其烧录工具需已就绪，成功构建后再烧录：

```sh
west build -b nrf52840dk/nrf52840 samples/subsys/shell/shell_module
west flash
```

## 10.4\_示例输出

```text
uart:~$
  bypass              clear               date
  demo                device              devmem
  dynamic             help                history
  kernel              log                 log_test
  rem                 resize              retval
  section_cmd         shell               shell_uart_release
  stats               version
uart:~$ demo
demo - Demo commands
Subcommands:
  dictionary  : Dictionary commands
  hexdump     : Hexdump params command.
  params      : Print params command.
  ping        : Ping command.
  board       : Show board name command.
uart:~$ dynamic
dynamic - Demonstrate dynamic command usage.
Subcommands:
  add      : Add a new dynamic command.
            Example usage: [ dynamic add test ] will add a dynamic command
            'test'.
            In this example, command name length is limited to 32 chars. You can
            add up to 20 commands. Commands are automatically sorted to ensure
            correct shell completion.
  execute  : Execute a command.
  remove   : Remove a command.
  show     : Show all added dynamic commands.
uart:~$
```

输出保留原样以便与终端核对。`demo` 下的 `dictionary`、`hexdump`、`params`、`ping`、`board` 分别用于字典命令、参数十六进制转储、打印参数、Ping 和显示开发板名称。`dynamic add test` 会添加名为 `test` 的动态命令；本例名称长度限制为 32 个字符，最多添加 20 个命令，并自动排序以保证补全顺序。`execute`、`remove`、`show` 分别执行、移除和显示已添加的动态命令。

## 10.5\_更多说明

Shell 子系统的详细说明和参阅入口均见[Shell指南](P001_Shell命令行.md)。


译注核对来源：[samples/subsys/shell/shell_module/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/src/main.c)、[samples/subsys/shell/shell_module/src/dynamic_cmd.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/src/dynamic_cmd.c)、[samples/subsys/shell/shell_module/src/login_cmd.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/src/login_cmd.c)、[samples/subsys/shell/shell_module/sysbuild.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module/sysbuild.cmake)。

本仓库的[对应示例源码](../../../samples/subsys/shell/shell_module/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行构建、写内存／闪存或硬件操作。

<a id="shell-module"></a>
<a id="overview"></a>
<a id="remote-shell"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="emulation-targets"></a>
<a id="on-hardware"></a>
<a id="sample-output"></a>
<a id="details-on-shell-subsystem"></a>
<a id="see-also"></a>

[上一章](P009_Shell示例目录.md) · [返回大纲](大纲.md) · [下一章](P011_文件系统Shell示例.md)
