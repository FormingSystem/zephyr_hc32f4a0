---
id: learning.zephyr-docs.cmake-reference.module.arch
title: arch
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/arch.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_arch

原文：[arch](https://docs.zephyrproject.org/latest/build/cmake-ref/module/arch.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:arch"></a>

根据 Kconfig 设置与架构根目录（Architecture Root）配置架构（Architecture）。本 CMake 模块依据开发板目录和架构根目录，在构建系统中设置下列变量。如果没有当前架构的实现，将报告错误。

## 2.1\_变量（Variables）

本模块完成后定义以下变量：
- [ARCH](P024_ARCH.md)。
- [ARCH_DIR](P025_ARCH_DIR.md)。
- [ARCH_ROOT](P026_ARCH_ROOT.md)。

## 2.2\_原文相关链接

- [variable:ARCH](P024_ARCH.md#variable:ARCH)
- [variable:ARCH_DIR](P025_ARCH_DIR.md#variable:ARCH_DIR)
- [variable:ARCH_ROOT](P026_ARCH_ROOT.md#variable:ARCH_ROOT)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CMake参考总览](P001_CMake参考总览.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：boards](P003_boards.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P001_CMake参考总览.md) · [返回大纲](大纲.md) · [下一章](P003_boards.md)

</details>

<!-- reading-navigation:end -->
