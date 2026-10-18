---
id: learning.zephyr-docs.cmake-reference.variable.module_ext_root
title: MODULE_EXT_ROOT
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/variable/MODULE_EXT_ROOT.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_MODULE_EXT_ROOT

原文：[MODULE_EXT_ROOT](https://docs.zephyrproject.org/latest/build/cmake-ref/variable/MODULE_EXT_ROOT.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="variable:MODULE_EXT_ROOT"></a>

包含模块外部根目录（Module External Root）的目录列表。这些目录保存 Zephyr 模块的 CMake 与 Kconfig 衔接代码（Glue Code），用于模块本身没有携带这些代码的情况。

另见 `sysbuild_root`，了解 Sysbuild 如何为镜像构建（Image Build）解析这些目录。

## 43.1\_原文相关链接

- [module:sysbuild_root](P012_sysbuild_root.md#module:sysbuild_root)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：LLEXT_REMOVE_FLAGS](P042_LLEXT_REMOVE_FLAGS.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：NORMALIZED_BOARD_QUALIFIERS](P044_NORMALIZED_BOARD_QUALIFIERS.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P042_LLEXT_REMOVE_FLAGS.md) · [返回大纲](大纲.md) · [下一章](P044_NORMALIZED_BOARD_QUALIFIERS.md)

</details>

<!-- reading-navigation:end -->
