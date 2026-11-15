---
id: learning.zephyr-docs.contributing.page-1
title: 参与Zephyr开发
kind: reference
status: maintained
domains: [zephyr, contribution, documentation]
source_url: https://docs.zephyrproject.org/latest/contribute/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="contributing-to-zephyr"></a>
<a id="contribute-to-zephyr"></a>

# 第1章\_参与Zephyr开发

原文：[官方页面](https://docs.zephyrproject.org/latest/contribute/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

社区贡献是项目的基础。无论提交代码、改进文档，还是提出新功能，都是项目所重视的工作。本页汇集有助于参与贡献的资源和指南。

<a id="general-guidelines"></a>

## 1.1\_通用指南（General Guidelines）

- [贡献指南（Contribution Guidelines）](P002_贡献指南.md#contribute-guidelines)：介绍参与 Zephyr 的总体流程与要求。首次贡献者必须阅读，其中说明怎样使贡献具备被项目考虑接纳并可能合入的条件。
- [贡献者职责（Contributor Expectations）](P003_贡献者职责.md#contributor-expectations)：另一份必读文档，说明所有贡献者应遵循的行为要求。
- [审查者职责（Reviewer Expectations）](P004_审查者职责.md#reviewer-expectations)：另一份必读文档，说明审查项目贡献时的行为要求。
- [编码准则（Coding Guidelines）](P009_编码准则.md#coding-guidelines)：代码贡献应遵循的一组准则，用于保持代码库的一致性和可读性。
- [编码风格指南（Coding Style Guidelines）](../coding_style/P001_代码风格指南.md#coding-style)：代码贡献应遵循的风格规则，同样用于保持一致性和可读性。
- [提案与征求意见稿（Proposals and RFCs）](P007_提案与征求意见稿.md#rfcs)：介绍何时、如何为新功能和项目变更提交征求意见稿（Request for Comments，RFC）。
- [修改其他开发者的贡献](P006_修改他人的贡献.md#modifying-contributions)：说明修改他人贡献及处理停滞拉取请求的方法。
- [拉取请求生命周期策略（Pull Request Lifecycle Policy）](P005_拉取请求生命周期.md#pr-lifecycle-policy)：让开放的拉取请求（Pull Request，PR）集中在持续推进且有望合入的工作上。

<a id="documentation"></a>

## 1.2\_文档（Documentation）

良好的文档推动 Zephyr 项目发展。无论作为代码贡献的一部分还是独立工作，文档贡献都很有价值。

- [文档编写指南（Documentation Guidelines）](P010_文档编写指南.md#doc-guidelines)：介绍使用 reStructuredText（reST）标记语言和 Sphinx 文档生成器编写文档的基本规则。
- [文档生成（Documentation Generation）](P011_文档生成.md#zephyr-doc)：编写时查看渲染效果很有帮助，此页介绍如何在本机构建 Zephyr 文档。

<a id="dealing-with-external-components"></a>

## 1.3\_处理外部组件（Dealing with External Components）

- [贡献外部组件（Contributing External Components）](P012_外部组件贡献.md#external-contributions)：其他开源项目可能已经具备适合加入 Zephyr 的基础能力或功能，项目建议并鼓励复用。本页详细介绍何时以及如何导入外部源码。
- [贡献外部工具（Contributing External Tooling）](P012_外部组件贡献.md#external-tooling)：编译、代码分析、测试或模拟所用的外部工具也能帮助项目，本节介绍相应要求。
- [二进制文件（Binary Blobs）](P008_二进制文件.md#bin-blobs)：某些能力可能只能依靠以二进制形式分发的可执行代码提供，本页介绍[贡献这类二进制文件](P008_二进制文件.md#blobs-process)的流程与指南。

<a id="need-help-along-the-way"></a>

## 1.4\_需要帮助时（Need Help Along the Way?）

如果对贡献流程有疑问，可以向 Zephyr 社区求助：加入 [Discord](https://chat.zephyrproject.org) 频道，或使用[开发者邮件列表（Developer Mailing List）](https://lists.zephyrproject.org/g/devel)。


对应官方文档源码：[doc/contribute/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/contribute/index.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/contribute/index.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/contributing.md) · [全部主线](../reading/README.md) · [下一篇：贡献指南](P002_贡献指南.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[返回大纲](大纲.md) · [下一章](P002_贡献指南.md)

</details>

<!-- reading-navigation:end -->
