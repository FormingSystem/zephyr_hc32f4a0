---
id: learning.zephyr-docs.cmake-reference.variable.app_build_version
title: APP_BUILD_VERSION
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/variable/APP_BUILD_VERSION.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_APP_BUILD_VERSION

原文：[APP_BUILD_VERSION](https://docs.zephyrproject.org/latest/build/cmake-ref/variable/APP_BUILD_VERSION.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="variable:APP_BUILD_VERSION"></a>

在所有上下文中用作应用的构建版本（Build Version）。

默认情况下，如果应用位于 Git 仓库中，版本由在应用目录运行 `git describe --abbrev=12 --always` 的结果生成。原文将这个字符串描述为最近标签（Tag）、标签之后的提交数量以及缩写提交哈希（Abbreviated Commit Hash）。

可以在 `CMakeLists.txt` 或命令行中把 CMake 变量 `APP_BUILD_VERSION` 设置为所需字符串，覆盖默认值。例如：`cmake -DAPP_BUILD_VERSION="v3.3.0-18-g2c85d92" ...`。

作为 `version` 模块的输入：在外部设置时，允许为本次构建指定自定义的应用构建版本。

作为 `version` 模块的输出：最终的应用构建版本，可以是显式设置的值，也可以是由 Git 自动生成的值。

另见 `BUILD_VERSION`。

## 22.1\_原文相关链接

- [app-version-details](https://docs.zephyrproject.org/latest/build/version/index.html#app-version-details)
- [variable:BUILD_VERSION](P034_BUILD_VERSION.md#variable:BUILD_VERSION)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：APPLICATION_CONFIG_DIR](P021_APPLICATION_CONFIG_DIR.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：APP_DIR](P023_APP_DIR.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P021_APPLICATION_CONFIG_DIR.md) · [返回大纲](大纲.md) · [下一章](P023_APP_DIR.md)

</details>

<!-- reading-navigation:end -->
