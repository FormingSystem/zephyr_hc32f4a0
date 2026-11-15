---
id: learning.zephyr-docs.twister.harness-shell
title: Shell支撑程序
kind: reference
status: maintained
domains: [zephyr, twister]
source_url: https://docs.zephyrproject.org/latest/develop/twister/harness/shell.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第15章\_Shell支撑程序

原文：[Shell](https://docs.zephyrproject.org/latest/develop/twister/harness/shell.html)。读取日期：2026-10-12，`latest`。

`shell` **测试支撑程序（Harness）**执行目标设备的 **命令解释器（Shell）**命令并解析输出，底层使用 pytest 框架与 Twister 的 pytest 支撑程序。

## 15.1\_直接配置命令

`harness_config.shell_commands` 是命令及预期输出的列表，默认空。每项的 `command` 指定设备端命令，`expected` 指定输出匹配模式。例如：

```yaml
harness_config:
  shell_commands:
  - command: "kernel cycles"
    expected: "cycles: .* hw cycles"
  - command: "kernel version"
    expected: "Zephyr version .*"
  - command: "kernel sleep 100"
```

这些是 Zephyr 设备端 Shell 命令，分别读取内核周期、版本或请求休眠；不是让主机终端执行同名命令。未提供 `expected` 时，仍执行命令并记录输出，但不按该字段验证预期文本。

## 15.2\_从文件读取命令

`shell_commands_file` 指定保存测试参数的文件，配置默认空。文件本身包含命令与预期输出列表，例如：

```yaml
- command: "mpu mtest 1"
  expected: "The value is: 0x.*"
- command: "mpu mtest 2"
  expected: "The value is: 0x.*"
```

原例中的 `mpu mtest` 是目标应用应提供的测试命令，涉及**内存保护单元（Memory Protection Unit，MPU）**测试；使用前应确认固件确实注册了该命令及其行为。

未指定文件时，支撑程序使用测试目录内的默认文件 `test_shell.yml`。同时提供两种配置时，`shell_commands` 优先于 `shell_commands_file`。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：BabbleSim支撑程序](P014_BabbleSim支撑程序.md) · [本模块主线目录](../reading/twister.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：BabbleSim支撑程序](P014_BabbleSim支撑程序.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
