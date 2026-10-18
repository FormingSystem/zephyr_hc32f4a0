---
id: learning.zephyr-docs.cmake-reference.module.native_simulator_sb_extensions
title: native_simulator_sb_extensions
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/native_simulator_sb_extensions.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_native_simulator_sb_extensions

原文：[native_simulator_sb_extensions](https://docs.zephyrproject.org/latest/build/cmake-ref/module/native_simulator_sb_extensions.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:native_simulator_sb_extensions"></a>

<a id="command:native-simulator-set-final-executable"></a>

<a id="command:native-simulator-set-child-images"></a>

<a id="command:native-simulator-set-primary-mcu-index"></a>

本模块提供面向原生模拟器（Native Simulator）`native_sim` 目标的 Sysbuild 扩展命令。开发板或应用的 `sysbuild.cmake` 使用它们，将多个镜像（Image）构建成单一原生模拟器可执行文件。开发板目标既不是原生模拟器、也不是 `bsim` 类型时，这些命令不执行操作（No-op）。

## 13.1\_设置最终可执行文件

`native_simulator_set_final_executable(<final_image>)`

添加构建目标，把 `<final_image>` 生成的可执行文件复制到顶层的 `zephyr/zephyr.exe`。需要时，预期已经调用 `native_simulator_set_child_images()`，将 `<final_image>` 配置为把其他依赖镜像组合到自身中。

这样，用户以及 Twister、bsim 测试脚本等工具就能在与非 Sysbuild 构建相同的位置找到最终可执行文件。

## 13.2\_设置子镜像

`native_simulator_set_child_images(<final_image> <child_image>)`

把 `<child_image>` 设置为 `<final_image>` 的依赖，并配置最终镜像，使其把子镜像组合进最终可执行文件。

## 13.3\_设置主 MCU 索引

`native_simulator_set_primary_mcu_index(<image> [<image2> ...])`

若设置了 `SB_CONFIG_NATIVE_SIMULATOR_PRIMARY_MCU_INDEX`，将它传播到每个给定镜像的 `CONFIG_NATIVE_SIMULATOR_PRIMARY_MCU_INDEX`。MCU 指微控制器（Microcontroller Unit）。

## 13.4\_原文相关链接

- [native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)
- [bsim-boards](../bsim_reference/P001_Bsim开发板设计.md#bsim-boards)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：sysbuild_root](P012_sysbuild_root.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：doc](P014_doc.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P012_sysbuild_root.md) · [返回大纲](大纲.md) · [下一章](P014_doc.md)

</details>

<!-- reading-navigation:end -->
