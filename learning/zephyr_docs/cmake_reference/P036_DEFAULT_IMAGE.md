---
id: learning.zephyr-docs.cmake-reference.variable.default_image
title: DEFAULT_IMAGE
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/variable/DEFAULT_IMAGE.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_DEFAULT_IMAGE

原文：[DEFAULT_IMAGE](https://docs.zephyrproject.org/latest/build/cmake-ref/variable/DEFAULT_IMAGE.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="variable:DEFAULT_IMAGE"></a>

Sysbuild 中主应用镜像（Main Application Image）的名称。

这个镜像通过 `APP_TYPE MAIN` 添加，并在 `domains.yaml` 中被报告为默认域（Default Domain）。可在 `sysbuild.cmake` 中使用此变量引用主镜像，无须硬编码其名称。另见 `ExternalZephyrProject_Add()`。

## 36.1\_原文相关链接

- [command:externalzephyrproject-add-application](P010_sysbuild_extensions.md#command:externalzephyrproject-add-application)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CONF_FILE](P035_CONF_FILE.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：DTC_OVERLAY_FILE](P037_DTC_OVERLAY_FILE.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P035_CONF_FILE.md) · [返回大纲](大纲.md) · [下一章](P037_DTC_OVERLAY_FILE.md)

</details>

<!-- reading-navigation:end -->
