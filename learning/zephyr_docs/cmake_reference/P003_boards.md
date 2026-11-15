---
id: learning.zephyr-docs.cmake-reference.module.boards
title: boards
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/boards.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_boards

原文：[boards](https://docs.zephyrproject.org/latest/build/cmake-ref/module/boards.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:boards"></a>

验证开发板（Board），并设置 `boards` 目标（Target）。本 CMake 模块验证 `BOARD` 参数，并将其拆分为 `<BOARD>` 和 `<BOARD_REVISION>`。

如果找不到所指定开发板的实现，将报告错误并打印有效开发板列表。如果用户给出的是开发板别名（Board Alias），模块会将其改为实际开发板名称。如果名称已弃用，则改为新名称，并打印弃用警告。

## 3.1\_必需变量（Required Variables）

- [BOARD](P027_BOARD.md)。

## 3.2\_可选变量（Optional Variables）

- [BOARD_ROOT](P031_BOARD_ROOT.md)。
- [ARCH_ROOT](P026_ARCH_ROOT.md)。

## 3.3\_输出变量（Variables）

本模块完成后定义以下变量：

- [BOARD](P027_BOARD.md)。
- [BOARD_REVISION](P030_BOARD_REVISION.md)。
- [BOARD_QUALIFIERS](P029_BOARD_QUALIFIERS.md)。
- [NORMALIZED_BOARD_QUALIFIERS](P044_NORMALIZED_BOARD_QUALIFIERS.md)。
- [NORMALIZED_BOARD_TARGET](P045_NORMALIZED_BOARD_TARGET.md)。
- [BOARD_DIR](P028_BOARD_DIR.md)。
- [ARCH_DIR](P025_ARCH_DIR.md)。
- [BOARD_ROOT](P031_BOARD_ROOT.md)。

## 3.4\_目标（Targets）

本模块完成后定义 `boards` 目标；调用它会打印有效开发板列表。

## 3.5\_可选环境变量（Optional Environment Variables）

`ZEPHYR_BOARD_ALIASES`：指向包含开发板别名的 CMake 文件。

## 3.6\_使用示例（Example Usage）

原示例的注释说明，`BOARD` 通常在命令行给出，例如 `west build -b nrf52840dk/nrf52840`。随后加载模块，打印开发板名称、规范化目标和开发板文件目录。

```cmake
# BOARD is normally given on the command line, for example:
#   west build -b nrf52840dk/nrf52840
include(boards)

message(STATUS "Building for ${BOARD} (${NORMALIZED_BOARD_TARGET})")
message(STATUS "Board files are in ${BOARD_DIR}")
```

## 3.7\_原文相关链接

- [variable:BOARD](P027_BOARD.md#variable:BOARD)
- [variable:BOARD_ROOT](P031_BOARD_ROOT.md#variable:BOARD_ROOT)
- [variable:ARCH_ROOT](P026_ARCH_ROOT.md#variable:ARCH_ROOT)
- [variable:BOARD_REVISION](P030_BOARD_REVISION.md#variable:BOARD_REVISION)
- [variable:BOARD_QUALIFIERS](P029_BOARD_QUALIFIERS.md#variable:BOARD_QUALIFIERS)
- [variable:NORMALIZED_BOARD_QUALIFIERS](P044_NORMALIZED_BOARD_QUALIFIERS.md#variable:NORMALIZED_BOARD_QUALIFIERS)
- [variable:NORMALIZED_BOARD_TARGET](P045_NORMALIZED_BOARD_TARGET.md#variable:NORMALIZED_BOARD_TARGET)
- [variable:BOARD_DIR](P028_BOARD_DIR.md#variable:BOARD_DIR)
- [variable:ARCH_DIR](P025_ARCH_DIR.md#variable:ARCH_DIR)
- [envvar-ZEPHYR_BOARD_ALIASES](https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-ZEPHYR_BOARD_ALIASES)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：arch](P002_arch.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：configuration_files](P004_configuration_files.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P002_arch.md) · [返回大纲](大纲.md) · [下一章](P004_configuration_files.md)

</details>

<!-- reading-navigation:end -->
