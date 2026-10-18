---
id: learning.zephyr-docs.cmake-reference.module.soc
title: soc
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/soc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_soc

原文：[soc](https://docs.zephyrproject.org/latest/build/cmake-ref/module/soc.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:soc"></a>

根据 Kconfig 设置配置片上系统（System on Chip，SoC）。本 CMake 模块依据所选 SoC 的 Kconfig 设置，在构建系统中设置下列变量。

## 5.1\_变量（Variables）

本模块完成后定义：

- `SOC_FULL_DIR`：SoC 文件所在的完整目录。
- `SOC_DIRECTORIES`：包含该 SoC 的 SoC 文件所在目录列表。
- `SOC_TOOLCHAIN_NAME`：SoC 的可选工具链名称（Toolchain Name）。

模块设置的其他未列出变量仅供内部使用，可能不经提前通知就被删除、重命名或改变用途。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：configuration_files](P004_configuration_files.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：kernel](P006_kernel.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P004_configuration_files.md) · [返回大纲](大纲.md) · [下一章](P006_kernel.md)

</details>

<!-- reading-navigation:end -->
