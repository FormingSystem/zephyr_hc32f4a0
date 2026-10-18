---
id: learning.zephyr-docs.cmake-reference.module.sysbuild_kconfig
title: sysbuild_kconfig
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/sysbuild_kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_sysbuild_kconfig

原文：[sysbuild_kconfig](https://docs.zephyrproject.org/latest/build/cmake-ref/module/sysbuild_kconfig.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:sysbuild_kconfig"></a>

本模块处理 Sysbuild 自身的 Kconfig 配置。Sysbuild 拥有自己的 Kconfig 树，以应用的 `Kconfig.sysbuild` 文件为根，并置于 `SB_CONFIG_` 命名空间（Namespace），因此不会与镜像（Image）自己的 `CONFIG_` 选项冲突。参见 Kconfig 命名空间说明。

本模块定位 Sysbuild 配置文件并对其运行 Kconfig，同时定义 `sysbuild_menuconfig` 和 `sysbuild_guiconfig` 构建目标；它们编辑 Sysbuild 自身的配置，而不是任何一个镜像的配置。

配置输入文件优先在 `SB_APPLICATION_CONFIG_DIR` 中查找，随后回退到 `APPLICATION_CONFIG_DIR`，由以下变量控制：

- [SB_CONF_FILE](P049_SB_CONF_FILE.md)。
- [SB_EXTRA_CONF_FILE](P050_SB_EXTRA_CONF_FILE.md)。

## 11.1\_原文相关链接

- [sysbuild-kconfig-namespacing](https://docs.zephyrproject.org/latest/build/sysbuild/index.html#sysbuild-kconfig-namespacing)
- [variable:SB_APPLICATION_CONFIG_DIR](P048_SB_APPLICATION_CONFIG_DIR.md#variable:SB_APPLICATION_CONFIG_DIR)
- [variable:APPLICATION_CONFIG_DIR](P021_APPLICATION_CONFIG_DIR.md#variable:APPLICATION_CONFIG_DIR)
- [variable:SB_CONF_FILE](P049_SB_CONF_FILE.md#variable:SB_CONF_FILE)
- [variable:SB_EXTRA_CONF_FILE](P050_SB_EXTRA_CONF_FILE.md#variable:SB_EXTRA_CONF_FILE)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：sysbuild_extensions](P010_sysbuild_extensions.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：sysbuild_root](P012_sysbuild_root.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P010_sysbuild_extensions.md) · [返回大纲](大纲.md) · [下一章](P012_sysbuild_root.md)

</details>

<!-- reading-navigation:end -->
