---
id: learning.zephyr-docs.west.west_index
title: west官方总入口
kind: reference
status: maintained
domains: [zephyr, west]
source_url: https://docs.zephyrproject.org/latest/develop/west/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="west"></a>

# 第14章\_west官方总入口

原文：[West (Zephyr’s meta-tool)](https://docs.zephyrproject.org/latest/develop/west/index.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

Zephyr 项目提供名为 `west` 的多用途命令行工具，如同一把瑞士军刀。west 在[独立仓库](https://github.com/zephyrproject-rtos/west)中开发。名称缘由见本章脚注。

west 的**内置命令（Built-in Commands）**提供多仓库管理系统，部分功能受到 Google Repo 工具和 **Git 子模块（Git Submodules）**的启发。west 也支持**可插拔扩展（Pluggability）**：可以编写自己的 **west 扩展命令（West Extension Commands）**来增加功能。Zephyr 利用这一机制，为应用程序的构建、烧录、调试等操作提供便利。

## 14.1\_命令形式与帮助

与 `git`、`docker` 类似，顶层 `west` 命令先接受通用选项，再接受要运行的子命令，随后是该子命令的选项和参数：

```text
west [common-opts] <command> [opts] <args>
```

从 west v0.8 开始，也可以采用以下形式运行：

```text
python3 -m west [common-opts] <command> [opts] <args>
```

> 译注：以上是官方命令语法示意，不是直接复制执行的完整操作。`common-opts` 表示通用选项，`command` 表示子命令，后面的 `opts` 和 `args` 分别是子命令选项与参数；尖括号和方括号用于描述语法。使用前先按[安装west](P001_安装west.md)准备工具。

运行 `west --help`（简写为 `west -h`）可查看可用命令的顶层帮助；运行 `west <command> -h` 可查看某个命令的详细帮助。

## 14.2\_官方文档目录

以下保持官方目录顺序，已完成的译文使用相对路径链接：

1. [安装west（Installing west）](P001_安装west.md)。
2. [west发行说明（West Release Notes）](P017_west发行说明.md)。
3. [west故障排查（Troubleshooting West）](P005_故障排查.md)。
4. [基本概念（Basics）](P002_基本概念.md)。
5. [内置命令（Built-in commands）](P011_内置命令.md)。
6. [工作区（Workspaces）](P004_工作区.md)。
7. [west清单文件（West Manifests）](P013_west清单文件.md)。
8. [配置（Configuration）](P003_配置.md)。
9. [west命令别名（West aliases）](P006_命令别名.md)。
10. [扩展命令机制（Extensions）](P012_扩展命令机制.md)。
11. [构建、烧录与调试（Building, Flashing and Debugging）](P007_构建烧录与调试.md)。
12. [二进制镜像签名（Signing Binaries）](P009_二进制镜像签名.md)。
13. [其他Zephyr扩展命令（Additional Zephyr extension commands）](P008_其他Zephyr扩展命令.md)。
14. [west的历史与设计缘由（History and Motivation）](P015_west的历史与设计缘由.md)。
15. [不使用west（Using Zephyr without west）](P010_不使用west.md)。

west 的 **Python 应用程序编程接口（Python API）**详情见[west的PythonAPI（West APIs）](P016_west的PythonAPI.md)。

## 14.3\_脚注

原文脚注 [1]：Zephyr 是拉丁文 [Zephyrus](https://en.wiktionary.org/wiki/Zephyrus) 的英语名称，指古希腊神话中的西风之神。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：west清单文件](P013_west清单文件.md) · [本模块主线目录](../reading/west.md) · [全部主线](../reading/README.md) · [下一篇：west的历史与设计缘由](P015_west的历史与设计缘由.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：west清单文件](P013_west清单文件.md) · [下一章：west的历史与设计缘由](P015_west的历史与设计缘由.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
