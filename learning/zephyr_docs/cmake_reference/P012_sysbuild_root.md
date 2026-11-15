---
id: learning.zephyr-docs.cmake-reference.module.sysbuild_root
title: sysbuild_root
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/sysbuild_root.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_sysbuild_root

原文：[sysbuild_root](https://docs.zephyrproject.org/latest/build/cmake-ref/module/sysbuild_root.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:sysbuild_root"></a>

将 Zephyr 根目录转换为绝对路径（Absolute Path），供 Sysbuild 使用。本模块以 `APP_DIR` 为基准，把以下根目录列表（Root List）中的全部相对路径（Relative Path）转换为绝对路径：

- [ARCH_ROOT](P026_ARCH_ROOT.md)。
- [BOARD_ROOT](P031_BOARD_ROOT.md)。
- [MODULE_EXT_ROOT](P043_MODULE_EXT_ROOT.md)。
- [SCA_ROOT](P052_SCA_ROOT.md)。
- [SNIPPET_ROOT](P053_SNIPPET_ROOT.md)。
- [SOC_ROOT](P054_SOC_ROOT.md)。

若某个根目录变量已定义，本模块会检查其路径列表、转换其中的相对路径并更新列表。若未定义，加载本模块后仍然未定义。转换后的路径放入 CMake 缓存（CMake Cache），使其能够正确传递到镜像构建（Image Build）。

> 译注：这里描述构建工具在读者当前工作区内解析路径的行为，不要求在文档、源码或版本控制中写入某台机器的固定绝对位置。

## 12.1\_原文相关链接

- [variable:APP_DIR](P023_APP_DIR.md#variable:APP_DIR)
- [variable:ARCH_ROOT](P026_ARCH_ROOT.md#variable:ARCH_ROOT)
- [variable:BOARD_ROOT](P031_BOARD_ROOT.md#variable:BOARD_ROOT)
- [variable:MODULE_EXT_ROOT](P043_MODULE_EXT_ROOT.md#variable:MODULE_EXT_ROOT)
- [variable:SCA_ROOT](P052_SCA_ROOT.md#variable:SCA_ROOT)
- [variable:SNIPPET_ROOT](P053_SNIPPET_ROOT.md#variable:SNIPPET_ROOT)
- [variable:SOC_ROOT](P054_SOC_ROOT.md#variable:SOC_ROOT)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：sysbuild_kconfig](P011_sysbuild_kconfig.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：native_simulator_sb_extensions](P013_native_simulator_sb_extensions.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P011_sysbuild_kconfig.md) · [返回大纲](大纲.md) · [下一章](P013_native_simulator_sb_extensions.md)

</details>

<!-- reading-navigation:end -->
