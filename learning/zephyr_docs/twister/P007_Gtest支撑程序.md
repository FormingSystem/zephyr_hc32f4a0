---
id: learning.zephyr-docs.twister.harness-gtest
title: Gtest支撑程序
kind: reference
status: maintained
domains: [zephyr, twister]
source_url: https://docs.zephyrproject.org/latest/develop/twister/harness/gtest.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第7章\_Gtest支撑程序

原文：[Gtest](https://docs.zephyrproject.org/latest/develop/twister/harness/gtest.html)。读取日期：2026-10-12，`latest`。

如果已有使用 **GoogleTest（gTest，C++测试框架）**编写的测试，并且不希望把它们改写为 **Zephyr测试框架（Zephyr Test Framework，Ztest）**，可以选用 `gtest` **测试支撑程序（Harness）**。

> 译注：在场景配置中通过 `harness: gtest` 选择，Twister 根据 gTest 输出解释测试结果。原页面没有列出额外配置项；它说明的是复用已有测试框架的入口，不是本次已移植或运行了某组 gTest 用例。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Ctest支撑程序](P006_Ctest支撑程序.md) · [本模块主线目录](../reading/twister.md) · [全部主线](../reading/README.md) · [下一篇：Pytest支撑程序](P008_Pytest支撑程序.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Ctest支撑程序](P006_Ctest支撑程序.md) · [下一章：Pytest支撑程序](P008_Pytest支撑程序.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
