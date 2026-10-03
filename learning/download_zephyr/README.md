---
id: zephyr-download-notes-index
title: Zephyr 下载方案参考草稿
kind: track
status: draft
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_Zephyr\_下载方案参考草稿

本目录保留源码精简、ZIP 与 Git、清单依赖、SDK 和主机工具的六篇讨论材料。原有内容按主题分组收纳，操作环境统一适配为 Windows x64 上的 UCRT64 Bash；示例中的模块名、版本与路径不等同于当前工程配置，命令尚未整体实测。

按顺序学习可从[阅读大纲](大纲.md)进入；操作前先看[环境与目录约定](环境与目录约定.md)。各章首部均有可点击目录，Linux 主机与其他方案的对照讲解仍保留。

实际操作先读[UCRT64 与 Zephyr 下载教程](../P01_zephyr_make_project/大纲.md)，安装本仓库使用[当前工程环境说明](../../project-docs/environment.md)。

访问 GitHub 前先读[本地代理配置](代理配置.md)：以 v2rayN 混合端口 `10808` 为例，说明 Git 配置、浏览器下载 ZIP 和小请求测试。

| 顺序 | 参考材料 |
| --- | --- |
| 1 | [Zephyr 指定芯片的最小化下载方案](P01_如何下载zephyr.md) |
| 2 | [从零理解：我们到底怎样把 Zephyr 源码下载下来](P02_零基础获得zephyr.md) |
| 3 | [Zephyr 环境下载：ZIP 优先、Git 按需补全](P03_国内如何更快下载zephyr.md) |
| 4 | [从 `west.yml` 判断：一款 MCU 到底需要下载哪些 Zephyr ZIP](P04_如何从west.yml获得需要下载的包.md) |
| 5 | [Zephyr SDK 与 ARM 交叉编译工具链：HC32F4A0 到底需要下载什么](P05_SDK和交叉编译器下载说明.md) |
| 6 | [Host 端工具：Python、CMake、Ninja、west、DTC 到底分别干什么](P06_环境依赖需要安装的工具.md) |
