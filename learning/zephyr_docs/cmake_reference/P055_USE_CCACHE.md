---
id: learning.zephyr-docs.cmake-reference.variable.use_ccache
title: USE_CCACHE
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/variable/USE_CCACHE.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_USE_CCACHE

原文：[USE_CCACHE](https://docs.zephyrproject.org/latest/build/cmake-ref/variable/USE_CCACHE.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="variable:USE_CCACHE"></a>

设为 `0` 时，即使安装了 ccache，也显式禁用它。

如果设为其他值，或者没有设置此变量，只要找到 ccache，就会在编译（Compilation）和链接（Linking）时使用它。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：SOC_ROOT](P054_SOC_ROOT.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：WEST](P056_WEST.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P054_SOC_ROOT.md) · [返回大纲](大纲.md) · [下一章](P056_WEST.md)

</details>

<!-- reading-navigation:end -->
