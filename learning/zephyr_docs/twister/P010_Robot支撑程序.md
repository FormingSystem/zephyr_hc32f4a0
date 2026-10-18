---
id: learning.zephyr-docs.twister.harness-robot
title: Robot支撑程序
kind: reference
status: maintained
domains: [zephyr, twister]
source_url: https://docs.zephyrproject.org/latest/develop/twister/harness/robot.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第10章\_Robot支撑程序

原文：[Robot](https://docs.zephyrproject.org/latest/develop/twister/harness/robot.html)。读取日期：2026-10-12，`latest`。

Zephyr 支持 [Robot Framework](https://robotframework.org/) 自动化测试框架。Robot 文件以人类可读的文本描述交互场景，可用于模拟或硬件测试；当前 Zephyr 集成支持 [Renode](https://renode.io/)、QEMU 与原生模拟器。

## 10.1\_运行与编写Robot测试

在准备好模拟环境和构建依赖的 Zephyr 源码根，用 Twister 执行套件，例如：

```sh
$ west twister --platform hifive1 --test samples/subsys/shell/shell_module/sample.shell.shell_module.robot
```

> 译注：`$` 是提示符，不输入；`hifive1` 是原例平台。命令需要对应源码版本仍提供该场景及适配，本次没有执行。

框架自身的**关键字（Keyword）**是组合测试步骤的具名操作，列表见 [Robot官方文档](https://robotframework.org/robotframework/)。Renode 中编写与执行 Robot 测试的方法、常用关键字及其实现源码入口，见 [Renode测试文档](https://renode.readthedocs.io/en/latest/introduction/testing.html)。

可以直接在 Robot 套件文件中定义新关键字，也可以用外部 Python 库扩展，或像 Renode 一样通过 **XML远程过程调用（XML Remote Procedure Call，XML-RPC）**动态提供关键字。扩展方法见 [Extending Robot Framework](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#extending-robot-framework)。这里 XML 是**可扩展标记语言（Extensible Markup Language）**，用于远程调用的数据表示。

## 10.2\_只选择一个套件

不运行一整组测试，而只选择某个场景时，原文使用：

```sh
$ west twister -p qemu_riscv32 -s arch.shared_interrupt
```

`-p` 选择 `qemu_riscv32` 平台，`-s` 选择 `arch.shared_interrupt` 场景。是否实际由 Robot 执行，还取决于该场景自己的 `harness` 配置。

## 10.3\_配置字段

`robot` **测试支撑程序（Harness）**用于在 QEMU、原生模拟器、Renode 中执行 Robot 套件。在 `harness_config` 下提供：

| 字段 | 含义 |
| --- | --- |
| `robot_testsuite` | 要运行的一个或多个 Robot 套件文件路径，默认空。 |
| `robot_option` | 传给 Robot Framework 的一个或多个选项，默认空。 |

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：控制台支撑程序](P009_控制台支撑程序.md) · [本模块主线目录](../reading/twister.md) · [全部主线](../reading/README.md) · [下一篇：功耗测试支撑程序](P011_功耗测试支撑程序.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：控制台支撑程序](P009_控制台支撑程序.md) · [下一章：功耗测试支撑程序](P011_功耗测试支撑程序.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
