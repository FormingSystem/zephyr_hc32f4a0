---
id: learning.zephyr-docs.cmake-reference.variable.sb_conf_file
title: SB_CONF_FILE
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/variable/SB_CONF_FILE.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_SB_CONF_FILE

原文：[SB_CONF_FILE](https://docs.zephyrproject.org/latest/build/cmake-ref/variable/SB_CONF_FILE.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="variable:SB_CONF_FILE"></a>

Sysbuild 的 Kconfig 配置文件或文件列表。

默认使用 `APPLICATION_CONFIG_DIR` 下存在的 `sysbuild.conf`。Sysbuild 按需启用（Opt-in），因此这个文件是可选的。

其中的设置覆盖 Sysbuild 自身 Kconfig 树中的默认值。路径相对于 `APP_DIR`。另见 `sysbuild_kconfig`、`APPLICATION_CONFIG_DIR` 和 `APP_DIR`。

## 49.1\_原文相关链接

- [variable:APPLICATION_CONFIG_DIR](P021_APPLICATION_CONFIG_DIR.md#variable:APPLICATION_CONFIG_DIR)
- [variable:APP_DIR](P023_APP_DIR.md#variable:APP_DIR)
- [module:sysbuild_kconfig](P011_sysbuild_kconfig.md#module:sysbuild_kconfig)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：SB_APPLICATION_CONFIG_DIR](P048_SB_APPLICATION_CONFIG_DIR.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：SB_EXTRA_CONF_FILE](P050_SB_EXTRA_CONF_FILE.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P048_SB_APPLICATION_CONFIG_DIR.md) · [返回大纲](大纲.md) · [下一章](P050_SB_EXTRA_CONF_FILE.md)

</details>

<!-- reading-navigation:end -->
