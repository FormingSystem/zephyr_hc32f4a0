---
id: learning.zephyr-docs.twister.twister-statuses
title: Twister状态
kind: reference
status: maintained
domains: [zephyr, twister]
source_url: https://docs.zephyrproject.org/latest/develop/twister/twister_statuses.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第5章\_Twister状态

原文：[Twister Status](https://docs.zephyrproject.org/latest/develop/twister/twister_statuses.html)。读取日期：2026-10-12，`latest`。

## 5.1\_状态描述哪些对象

**Twister状态（Twister Status）**统一描述测试支撑程序、用例、套件与实例目前所处的状态。运行结束后，大部分读者主要关心用例和实例的最终结果。

下面先区分这四种对象，避免把报告中的同一名称理解成不同层级。

| 名称 | 含义 |
| --- | --- |
| **测试支撑程序（Harness）** | Twister 内部的 Python 类，用于捕获并分析外部程序的输出。它不出现在最终报告中，所以下文不列出其状态。 |
| **测试用例（TestCase，Case）** | 验证某项断言的一段代码，是 Zephyr 测试的最小单元。 |
| **测试套件（TestSuite，Suite）** | 一组用例，可通过 `testcase.yaml` 按套件调整 Twister 行为。这些用例应有足够共同点，适合由 Twister 统一处理。 |
| **测试实例（TestInstance，Instance）** | 某套件与某个平台的组合。Twister 通常报告实例的结果，即使报告中将它们称作“Suites”。 |

适用于套件的状态也适用于实例。本页不需要继续区分二者，因此后文出现“套件”时也包含实例。更完整的层级关系见 [Twister测试运行器](P001_Twister测试运行器.md)。

## 5.2\_可出现的状态

下表的“代码内名称”用于 Twister 内部及日志；“报告名称”用于 **JavaScript对象表示法（JavaScript Object Notation，JSON）**格式的结果报告。✓ 表示该对象可以具有此状态，✕ 表示不适用。

| 代码内名称 | 报告名称 | 中文含义与解释 | 套件 | 用例 |
| --- | --- | --- | --- | --- |
| `FILTER` | `filtered` | **已过滤（Filtered）**：静态或运行时过滤器将测试排除出要使用的测试列表。 | ✓ | ✓ |
| `NOTRUN` | `not run` | **未运行（Not Run）**：已经正确构建，但当前配置下不可运行。 | ✓ | ✓ |
| `BLOCK` | `blocked` | **受阻（Blocked）**：套件中的错误或崩溃导致本用例没有运行。 | ✕ | ✓ |
| `SKIP` | `skipped` | **已跳过（Skipped）**：因上述情况以外的其他原因跳过。 | ✓ | ✓ |
| `ERROR` | `error` | **执行错误（Error）**：执行测试本身的过程发生错误。 | ✓ | ✓ |
| `FAIL` | `failed` | **失败（Failed）**：测试结果不符合预期。 | ✓ | ✓ |
| `PASS` | `passed` | **通过（Passed）**：测试结果符合预期。 | ✓ | ✓ |

另有两个 Twister 内部使用的**非终止状态（Non-terminal Status）**：`NONE` 是用例及套件的初始状态，`STARTED` 表示用例正在进行。这两种状态不应出现在最终报告中；如果最终报告文件里仍有它们，说明 Twister 的处理存在问题。

## 5.3\_用例与套件状态的合法组合

下表按“行是用例、列是套件”阅读。✓ 表示合法组合；✕ 表示正常运行不应出现，即该列状态的套件不应包含该行状态的用例。

| 用例状态↓ / 套件状态→ | `FILTER` | `ERROR` | `FAIL` | `PASS` | `NOTRUN` | `SKIP` |
| --- | --- | --- | --- | --- | --- | --- |
| `FILTER` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `ERROR` | ✕ | ✓ | ✕ | ✕ | ✕ | ✕ |
| `BLOCK` | ✕ | ✓ | ✓ | ✕ | ✕ | ✕ |
| `FAIL` | ✕ | ✓ | ✓ | ✕ | ✕ | ✕ |
| `PASS` | ✕ | ✓ | ✓ | ✓ | ✕ | ✕ |
| `NOTRUN` | ✕ | ✕ | ✕ | ✕ | ✓ | ✕ |
| `SKIP` | ✕ | ✓ | ✓ | ✓ | ✕ | ✓ |

按套件状态逐项解释如下：

- `FILTER`：整个套件被静态过滤出本次运行，因此内部用例都应是 `FILTER`。
- `ERROR`：执行套件时遇到问题，至少有一个用例为 `ERROR` 或 `BLOCK`。该结果优先于其他用例结果；其他允许并存的终止状态以矩阵为准。
- `FAIL`：至少一个用例未满足断言，而且没有达到套件应判为 `ERROR` 的条件；在这个前提下，失败优先于其余用例结果。
- `PASS`：套件正常通过，不能含 `BLOCK`、`ERROR` 或 `FAIL` 用例，因为这些状态都说明执行出现问题。
- `NOTRUN`：整个套件只构建、未执行。是否能够运行是按套件决定的，因此内部用例都必须为 `NOTRUN`。
- `SKIP`：整个套件在运行时跳过，内部用例也必须全部为 `SKIP`。

> 译注：原文对 `ERROR` 套件称“所有有效终止状态均可包含”，但同页矩阵明确排除了 `FILTER` 和 `NOTRUN`。这里按完整矩阵限定“允许并存”，避免把概述理解成没有条件的任意组合。用例状态表示其自身结果，套件状态表示汇总结果；已有通过用例与套件最终失败并不矛盾。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Twister黑盒测试](P004_Twister黑盒测试.md) · [本模块主线目录](../reading/twister.md) · [全部主线](../reading/README.md) · [下一篇：Ctest支撑程序](P006_Ctest支撑程序.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Twister黑盒测试](P004_Twister黑盒测试.md) · [下一章：Ctest支撑程序](P006_Ctest支撑程序.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
