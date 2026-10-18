---
id: learning.zephyr-docs.cmake-reference.module.basic_settings
title: basic_settings
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/basic_settings.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_basic_settings

原文：[basic_settings](https://docs.zephyrproject.org/latest/build/cmake-ref/module/basic_settings.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:basic_settings"></a>

设置 Zephyr 工程的基本设置（Basic Settings），其中包括 Sysbuild 定义的配置设置。

Sysbuild 是 Zephyr 使用的更高层构建系统（Higher-level Build System），允许用户为给定系统构建多个示例。为实现这一点，Sysbuild 通过设置专用构建变量来管理其他 Zephyr CMake 构建系统。

本 CMake 模块将 Sysbuild 缓存变量（Cache Variable）加载为 `sysbuild_cache` 目标的目标属性（Target Property），确保引号和列表能够正确保留。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：kernel](P006_kernel.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：extensions：CMake扩展命令](P008_extensions.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P006_kernel.md) · [返回大纲](大纲.md) · [下一章](P008_extensions.md)

</details>

<!-- reading-navigation:end -->
