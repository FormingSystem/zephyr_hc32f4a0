---
id: learning.zephyr-docs.west.west_why
title: west的历史与设计缘由
kind: reference
status: maintained
domains: [zephyr, west]
source_url: https://docs.zephyrproject.org/latest/develop/west/why.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_west的历史与设计缘由

原文：[History and Motivation](https://docs.zephyrproject.org/latest/develop/west/why.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

Zephyr 引入 west，是为了满足两个基本需求：能够同时处理多个 **Git 仓库（Git Repositories）**；为基本 Zephyr 工作流程提供可扩展且易用的**命令行接口（Command-line Interface）**。在开发 west 的过程中，项目还明确了一组设计约束，以避开此类工具常见的问题。

## 15.1\_需求

将 Zephyr 代码库拆分为多个仓库的全部动机不在本页讨论范围内；但基本需求，以及为何没有采用现有工具而是开发新工具，需要在这里说明。

- **R1：**将外部维护的代码保存在主 `zephyr` 仓库之外、独立维护的仓库中，同时不要求使用者逐一手动克隆外部仓库。
- **R2：**提供一个 Zephyr 使用者和发行版维护者都能使用、从中受益并加以扩展的工具。
- **R3：**允许使用者和下游发行版覆盖或移除仓库，而无须修改 `zephyr` 仓库。
- **R4：**同时支持**持续跟踪（Continuous Tracking）**和基于提交、可进行**二分定位（Bisectable）**的项目更新。

## 15.2\_为何开发专用工具

west 的部分功能类似于 [Git子模块（Git Submodules）](https://git-scm.com/book/en/v2/Git-Tools-Submodules)和 [Google repo](https://gerrit.googlesource.com/git-repo/)。west 初始设计与开发时评估过已有工具，但没有发现适合 Zephyr 需求的方案；其中详细考察了以下两种。

**Google repo：**

- 不能妥善支持将 `zephyr` 用作**清单仓库（Manifest Repository）**，涉及 R4。
- 只支持 Python 2。
- 与 Windows 配合不佳。
- 假定代码评审使用 Gerrit。

**Git子模块：**

- 不能完整满足 R1：外部维护的仓库仍需要位于主 `zephyr` Git 树内。
- 不支持 R3：下游副本必须删除或替换子模块定义。
- 不支持持续跟踪外部仓库的最新 `HEAD`，涉及 R4。
- 要求硬编码外部仓库的路径或位置。

> 译注：以上是官方原文记录的初始设计时期评估理由，保留其历史语境；不应把“只支持 Python 2”等结论当作这些工具当前版本的能力清单。

## 15.3\_为何使用多个Git仓库

Zephyr 希望提供部署复杂**物联网（Internet of Things，IoT）**应用所需的全部构件。因此，Zephyr 项目远不止一个**实时操作系统内核（RTOS Kernel）**，而是多个协同工作的组件的集合。在这个背景下，项目以统一方式管理多个 Git 仓库有以下理由：

- 清楚分离 Zephyr 原创代码与引入的项目、库。
- 避免原创代码与引入代码之间的许可证不兼容问题。
- 缩小核心 Zephyr 代码库的规模和范围；可选组件放在额外仓库中，而不是直接导入主源码树。
- 满足**功能安全（Safety）**与**信息安全（Security）**认证的需要。
- 强化组件模块化。
- 支持仅针对部分已支持开发板与**片上系统（System on Chip，SoC）**开展**树外开发（Out-of-tree Development）**。

west 工作区如何管理多个 Git 仓库，见[基本概念](P002_基本概念.md)。

## 15.4\_设计约束

west 遵循以下约束：

- **可选（Optional）：**始终可以退回直接使用底层命令行工具，即不通过 west 使用 Zephyr；不过，构建系统仍可能要求安装 west 并能够找到它。直接操作不一定总是方便。如果 west 提供的所有功能本来都能方便地获得，也就没有开发它的理由。
- **与CMake兼容（Compatible with CMake）：**构建、烧录、调试以及模拟器支持，始终应兼容直接使用 CMake 的方式。
- **跨平台（Cross-platform）：**west 使用 Python 3 编写，可在 Zephyr 支持的所有平台上工作。
- **可作为库使用（Usable as a Library）：**在可行的情况下，west 功能以能供其他程序独立使用的库实现，另以命令行接口封装这些库。west 本身是名为 `west` 的 Python 包，各库实现为子包。
- **谨慎增加功能（Conservative about Features）：**没有充分且有说服力的动机，就不接受新功能。
- **行为有明确规范（Clearly Specified）：**west 封装其他命令时，其行为需要清楚定义并记录。这使它能与第三方工具协作，也让 Zephyr 开发者能够查明 west 背后实际执行了什么。

更多细节与讨论见[Zephyr议题#6205](https://github.com/zephyrproject-rtos/zephyr/issues/6205)。

## 15.5\_为什么west update使用分离HEAD

[更新流程](P011_内置命令.md)中所述的**分离HEAD（Detached HEAD）**让一些使用者感到困惑，甚至受挫。一个常见问题是：为什么 `west update` 默认不让已有本地分支继续处于检出状态？本节说明这一默认行为的原因，以及管理本地改动项目的其他选择。

`west update` 有两个核心要求：

1. **安全性（Safety）：**命令不应丢失使用者的任何工作。
2. **确定性（Determinism）：**两个人对同一份清单运行 `west update`，应得到完全相同的[工作区（Workspace）](P002_基本概念.md)内容。

使用分离 HEAD 有助于保障安全性。更新流程在项目中执行 `git checkout --detach` 以获得分离 HEAD，通常不会丢失工作：

- 如果工作已经安全提交到某个本地 Git 分支，该分支会保持原样，详情可查 `git help checkout`。
- 如果有尚未提交的工作，Git 会在可行时将其安全保留在**工作树（Working Tree）**中。
- 如果无法保留，整个命令会失败；可以先决定如何处理这些工作，再重新运行 `west update`。

分离 HEAD 也有助于保证确定性：

- 必须精确检出清单指定的**项目修订（Project Revision）**，才能让工作区文件符合主清单。如果 west 默认不检出清单修订，工作区就可能与工作副本中清单文件所表达的预期悄然不同；更糟的是，这种差异取决于运行 `west update` 之前分支中究竟有什么。
- 它与[清单导入（Manifest Imports）](P013_west清单文件.md)还有细微关联。如果项目中有一份或多份清单会被 `west update` 导入，west 必须将这些文件检出到工作树，才能解析完整的导入清单。如果让项目继续检出某个分支，工作树里的清单可能已经过时；west 若据此完成导入，过程可能意外失败，或产生其他不确定的结果。

west 不会直接检出 `manifest-rev` 分支，原因见[该分支的说明](P004_工作区.md)。

这个默认行为早已确定，使用者也已依赖它，因此现在不适合更改。如果它不符合需求，还有其他方式运行 `west update`。运行 `west help update`，阅读**检出分支行为（checked out branch behavior）**选项组的说明，例如：

- 正在项目中积极编写代码，希望在上游清单可能发生变化后仍保持更新，可使用 `west update --rebase`。
- 希望保留一些本地代码，只要该项目的上游修订还没有向前推进到更新版本，就继续保留它们，可使用 `west update --keep-descendants`。

如果希望在工作区中以更短的输入调用这些命令，可以使用[west命令别名](P006_命令别名.md)。也可以向 [west仓库](https://github.com/zephyrproject-rtos/west)发送**拉取请求（Pull Request，PR）**，为这一选项组贡献新的选项。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：west官方总入口](P014_west官方总入口.md) · [本模块主线目录](../reading/west.md) · [全部主线](../reading/README.md) · [下一篇：west的PythonAPI](P016_west的PythonAPI.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：west官方总入口](P014_west官方总入口.md) · [下一章：west的PythonAPI](P016_west的PythonAPI.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
