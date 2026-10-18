---
id: learning.zephyr-docs.twister.harness-ctest
title: Ctest支撑程序
kind: reference
status: maintained
domains: [zephyr, twister]
source_url: https://docs.zephyrproject.org/latest/develop/twister/harness/ctest.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第6章\_Ctest支撑程序

原文：[Ctest](https://docs.zephyrproject.org/latest/develop/twister/harness/ctest.html)。读取日期：2026-10-12，`latest`。

本页给出 **Ctest测试支撑程序（Ctest Harness）**的附加参数配置。CTest 是 CMake 配套的测试执行工具；整体运行和结果处理仍由 Twister 管理。

`harness_config` 下的 `ctest_args` 是传给 ctest 的额外参数列表，默认空。例如 `ctest_args: ['--repeat until-pass:5']` 传入重复执行选项。

命令行的 `--ctest-args` 可以多次使用，以向 ctest 传入多个参数。

> 译注：`ctest_args` 属于配置文件，`--ctest-args` 属于 Twister 命令行；原文示例的排版弯引号在此改为可用于配置的直引号。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Twister状态](P005_Twister状态.md) · [本模块主线目录](../reading/twister.md) · [全部主线](../reading/README.md) · [下一篇：Gtest支撑程序](P007_Gtest支撑程序.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Twister状态](P005_Twister状态.md) · [下一章：Gtest支撑程序](P007_Gtest支撑程序.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
