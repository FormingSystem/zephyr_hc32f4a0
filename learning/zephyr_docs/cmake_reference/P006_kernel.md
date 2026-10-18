---
id: learning.zephyr-docs.cmake-reference.module.kernel
title: kernel
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/kernel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_kernel

原文：[kernel](https://docs.zephyrproject.org/latest/build/cmake-ref/module/kernel.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:kernel"></a>

<a id="variable:ZEPHYR_LIBS"></a>

<a id="variable:ZEPHYR_INTERFACE_LIBS"></a>

<a id="variable:GENERATED_APP_SOURCE_FILES"></a>

<a id="variable:GENERATED_KERNEL_OBJECT_FILES"></a>

<a id="variable:GENERATED_KERNEL_SOURCE_FILES"></a>

<a id="variable:code_data_relocation_target"></a>

<a id="variable:app"></a>

这是 Zephyr 内核（Kernel）的主要 CMake 模块。它负责创建 Zephyr 库（Library）和可执行文件（Executable），创建名为 `Zephyr-Kernel` 的 CMake 工程，并定义配置待构建库时所用的属性（Property）。

## 6.1\_变量（Variables）

加载本模块后，定义以下全局变量：

- `ZEPHYR_LIBS`：应链接的全部 Zephyr CMake 库的全局列表；`zephyr_library()` 向列表追加库。
- `ZEPHYR_INTERFACE_LIBS`：应链接的全部 Zephyr 接口库（Interface Library）的全局列表；`zephyr_interface_library_named()` 向列表追加库。
- `GENERATED_APP_SOURCE_FILES`：在 Zephyr 完成一次链接后生成的源文件，例如 `dev_handles.c`。
- `GENERATED_KERNEL_OBJECT_FILES`：在符号地址确定后生成的目标文件（Object File），例如内存管理单元（Memory Management Unit，MMU）表。
- `GENERATED_KERNEL_SOURCE_FILES`：在符号地址确定后生成的源文件，例如 `isr_tables.c`。

## 6.2\_目标（Targets）

- `code_data_relocation_target`：用于代码与数据重定位（Code/Data Relocation）的自定义目标。
- `app`：包含全部应用代码的 CMake 库，由入口 `${APPLICATION_SOURCE_DIR}/CMakeLists.txt` 修改。

## 6.3\_用法（Usage）

不应直接加载本模块，应通过 `find_package(Zephyr)` 加载。本模块自身不会加载任何 Zephyr CMake 模块。

## 6.4\_原文相关链接

- [command:zephyr-library](P008_extensions.md#command:zephyr-library)
- [command:zephyr-interface-library-named](P008_extensions.md#command:zephyr-interface-library-named)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：soc](P005_soc.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：basic_settings](P007_basic_settings.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P005_soc.md) · [返回大纲](大纲.md) · [下一章](P007_basic_settings.md)

</details>

<!-- reading-navigation:end -->
