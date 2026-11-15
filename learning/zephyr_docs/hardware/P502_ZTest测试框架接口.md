---
id: learning.zephyr-docs.hardware.ztestapi-2
title: ZTest测试框架接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ztest.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第502章\_ZTest测试框架接口

原文：[group__ztest](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest.html)。读取日期：2026-10-13，`latest`。

本页是 **Zephyr 测试框架（Zephyr Testing Framework，ZTest）**的官方接口目录，列出断言、假设、预期检查、模拟、测试定义和压力测试六组工具。

## 502.1\_接口主题

以下完整保留原页的主题名称和描述。中文说明对应各模块在测试中的用途，具体行为由相应接口参考给出。

| 官方主题 | 中文名称及原文说明 |
| --- | --- |
| [Ztest assertion macros](P503_ZTest断言宏.md) | ZTest 断言宏（Assertion Macros）：提供使用 ZTest 时的断言 |
| [Ztest assumption macros](P504_ZTest假设宏.md) | ZTest 假设宏（Assumption Macros）：提供使用 ZTest 时的假设检查 |
| [Ztest expectation macros](P505_ZTest预期检查宏.md) | ZTest 预期检查宏（Expectation Macros）：提供使用 ZTest 时的预期检查 |
| [Ztest mocking support](P506_ZTest模拟支持.md) | ZTest 模拟支持（Mocking Support）：提供单元测试使用的简单模拟函数 |
| [Ztest testing macros](P507_ZTest测试定义宏.md) | ZTest 测试宏（Testing Macros）：通过辅助宏和其他测试结构简化测试过程 |
| [Ztest ztress macros](P508_ZTest压力测试宏.md) | ZTest 压力测试宏（Ztress Macros）：提供使用 ZTest 时的测试压力支持 |

> 译注：`ztress` 是此压力测试模块的专用名称，不将其扩写为不存在的英文缩写。

---

[上一章：ZTest基准测试接口](P501_ZTest基准测试接口.md) · [下一章：ZTest断言宏](P503_ZTest断言宏.md) · [返回大纲](大纲.md)
