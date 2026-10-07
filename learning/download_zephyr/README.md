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

P005 已单独重写为操作说明：从读者解压的原生 Zephyr 文件追到 SDK/GCC 发布依据，解释 CMake 变量与 SDK 发现流程，下载并接入 ARM 工具链，完成应用编译。全章使用 G 盘原生源码和 MPS2 目标解释构建，HC32 的移植条件单独说明。该章的实测与未覆盖范围见[验证记录](VALIDATION.md)。其他章节仍按参考草稿阅读。

按顺序学习可从[阅读大纲](大纲.md)进入；操作前先看[环境与目录约定](环境与目录约定.md)。各章首部均有可点击目录，Linux 主机与其他方案的对照讲解仍保留。

实际操作先读[UCRT64 与 Zephyr 下载教程](../P01_zephyr_make_project/大纲.md)，使用 `G:\zephyr_practice\zephyr-main` 完成复现。

访问 GitHub 前先读[本地代理配置](代理配置.md)：以 v2rayN 混合端口 `10808` 为例，说明 Git 配置、浏览器下载 ZIP 和小请求测试。

| 顺序 | 参考材料 |
| --- | --- |
| 1 | [Zephyr 指定芯片的最小化下载方案](P001_如何下载zephyr.md) |
| 2 | [从零理解：我们到底怎样把 Zephyr 源码下载下来](P002_零基础获得zephyr.md) |
| 3 | [Zephyr 环境下载：ZIP 优先、Git 按需补全](P003_国内如何更快下载zephyr.md) |
| 4 | [从 `west.yml` 判断：一款 MCU 到底需要下载哪些 Zephyr ZIP](P004_如何从west.yml获得需要下载的包.md) |
| 5 | [从 Zephyr 源码版本选择 SDK、下载 ARM 工具链并完成编译](P005_SDK和交叉编译器下载说明.md) |
| 6 | [Host 端工具：Python、CMake、Ninja、west、DTC 到底分别干什么](P006_环境依赖需要安装的工具.md) |
