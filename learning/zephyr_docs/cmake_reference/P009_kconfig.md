---
id: learning.zephyr-docs.cmake-reference.module.kconfig
title: kconfig
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_kconfig

原文：[kconfig](https://docs.zephyrproject.org/latest/build/cmake-ref/module/kconfig.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:kconfig"></a>

<a id="variable:KCONFIG_ROOT"></a>

<a id="variable:AUTOCONF_H"></a>

<a id="variable:DOTCONFIG"></a>

<a id="variable:EXTRA_KCONFIG_TARGETS"></a>

<a id="variable:EXTRA_KCONFIG_TARGET_COMMAND_FOR_&lt;target&gt;"></a>

本模块包含 Kconfig 配置逻辑，并提供以下目标（Target）：

- `menuconfig`：运行 Kconfig 的 `menuconfig` 工具。
- `guiconfig`：运行 Kconfig 的 `guiconfig` 工具。
- `hardenconfig`：运行 Kconfig 的 `hardenconfig` 工具。
- `traceconfig`：运行 Kconfig 的 `traceconfig` 工具。

## 9.1\_变量（Variables）

加载本模块后，定义以下全局变量：

| 变量 | 含义与默认值 |
| --- | --- |
| `KCONFIG_ROOT` | Kconfig 根文件的路径；默认 `${ZEPHYR_BASE}/Kconfig` |
| `AUTOCONF_H` | 生成的 autoconf 头文件路径；默认 `${PROJECT_BINARY_DIR}/include/generated/zephyr/autoconf.h` |
| `DOTCONFIG` | 生成的 `.config` 文件路径；默认 `${PROJECT_BINARY_DIR}/.config` |
| `EXTRA_KCONFIG_TARGETS` | 要添加的额外 Kconfig 目标列表 |
| `EXTRA_KCONFIG_TARGET_COMMAND_FOR_<target>` | 额外 Kconfig 目标要运行的命令 |

本模块读取的 Kconfig 配置片段（Kconfig Fragment）由 `CONF_FILE` 和 `EXTRA_CONF_FILE` 选择；这两个变量由 `configuration_files` 模块解析。

## 9.2\_原文相关链接

- [variable:CONF_FILE](P035_CONF_FILE.md#variable:CONF_FILE)
- [variable:EXTRA_CONF_FILE](P039_EXTRA_CONF_FILE.md#variable:EXTRA_CONF_FILE)
- [module:configuration_files](P004_configuration_files.md#module:configuration_files)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：extensions：CMake扩展命令](P008_extensions.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：sysbuild_extensions](P010_sysbuild_extensions.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P008_extensions.md) · [返回大纲](大纲.md) · [下一章](P010_sysbuild_extensions.md)

</details>

<!-- reading-navigation:end -->
