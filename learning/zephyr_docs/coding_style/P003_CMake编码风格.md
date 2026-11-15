---
id: learning.zephyr-docs.coding-style.page-3
title: CMake编码风格
kind: reference
status: maintained
domains: [zephyr, documentation, style]
source_url: https://docs.zephyrproject.org/latest/contribute/style/cmake.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_CMake编码风格

原文：[官方页面](https://docs.zephyrproject.org/latest/contribute/style/cmake.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 3.1\_风格检查

持续集成（Continuous Integration，CI）中的 `CMakeStyle` 合规检查会强制检查本指南的一部分规则。也可以在本地通过 `scripts/cmake/cmake_style.py` 运行相同检查；传入目录时，脚本会递归查找 `CMakeLists.txt` 和 `*.cmake` 文件。

```sh
pip install tree-sitter tree-sitter-cmake
./scripts/cmake/cmake_style.py path/to/CMakeLists.txt
./scripts/cmake/cmake_style.py drivers/
```

> 译注：以上为官方命令示例，从 Zephyr 源码根目录执行。`pip install` 安装检查器的 Python 依赖；后两行分别检查一个指定文件和一个目录。先使用工程已有的 Python 环境，安装成功后再执行所需的检查分支；`path/to/CMakeLists.txt` 是待替换的示例路径。本批没有执行安装或修改源码格式。

## 3.2\_通用格式（General Formatting）

- 缩进使用 2 个空格。避免制表符，以保证不同环境中的显示一致。
- 尽可能将每行限制在 100 列以内。
- 使用空行分隔 CMake 文件中逻辑上不同的部分。
- 命令名与左圆括号之间不加空格：使用 `if(...)`，不使用 `if (...)`。

```cmake
# Good:
if(ENABLE_TESTS)
  add_subdirectory(tests)
endif()

# Bad:
if (ENABLE_TESTS)
  add_subdirectory(tests)
endif()
```

## 3.3\_命令与语法（Commands and Syntax）

**命令使用小写。** CMake 命令始终使用小写，例如 `add_executable` 和 `find_package`，以提高可读性并保持一致。

```cmake
# Good:
add_library(my_lib STATIC src/my_lib.cpp)

# Bad:
ADD_LIBRARY(my_lib STATIC src/my_lib.cpp)
```

CMake 模块定义的命令，以及 Zephyr 或系统构建（sysbuild）对既有大小写混合命令的扩展，是这一规则的例外。这些命令采用 `Module_Action` 命名形式，必须保留其规范大小写。例如，Zephyr 的 `ExternalZephyrProject_Add` 扩展了 CMake 的 `ExternalProject_Add`。`CMakeStyle` 不会把这些命令当作违反小写规则的情况。对小写命令的扩展仍保持小写，例如 sysbuild 的 `sysbuild_add_dependencies` 扩展了 `add_dependencies`。

**每个文件参数单独占一行。** 将文件参数拆成多行，便于浏览并识别各个源文件或条目。

```cmake
# Good:
target_sources(my_target PRIVATE
  src/file1.cpp
  src/file2.cpp
)

 # Bad:
target_sources(my_target PRIVATE src/file1.cpp src/file2.cpp)
```

## 3.4\_变量命名（Variable Naming）

**缓存变量（cache variable）或跨 CMake 文件共享的变量使用大写。** 使用 `option` 或 `set(... CACHE ...)` 定义缓存变量时，采用 `UPPERCASE` 名称。

```cmake
option(ENABLE_TESTS "Enable test suite" ON)
set(CMAKE_CXX_STANDARD 17 CACHE STRING "C++ standard version")
```

**局部变量使用小写。** CMake 文件内部的局部变量采用小写或蛇形命名法（snake_case）。

```cmake
set(output_dir "${CMAKE_BINARY_DIR}/output")
```

**前缀保持一致。** 使用一致的变量前缀来避免名称冲突，尤其是在大型项目中。

```cmake
set(MYPROJECT_SRC_DIR "${CMAKE_SOURCE_DIR}/src")
```

## 3.5\_引号（Quoting）

**字符串和变量加引号。** 字符串字面量和变量始终加引号，以避免意外行为，尤其是处理可能包含空格的路径或参数时。

```cmake
# Good:
set(my_path "${CMAKE_SOURCE_DIR}/include")

# Bad:
set(my_path ${CMAKE_SOURCE_DIR}/include)
```

**布尔值不加引号。** `ON`、`OFF`、`TRUE` 和 `FALSE` 等布尔值不要加引号。

```cmake
option(BUILD_SHARED_LIBS "Build shared libraries" OFF)
```

## 3.6\_避免硬编码路径（Avoid Hardcoding Paths）

使用 CMake 变量，例如 `CMAKE_SOURCE_DIR`、`CMAKE_BINARY_DIR` 和 `CMAKE_CURRENT_SOURCE_DIR`，而不是把路径写死。

```cmake
set(output_dir "${CMAKE_BINARY_DIR}/bin")
```

## 3.7\_条件逻辑（Conditional Logic）

使用 `if`、`elseif` 和 `else` 时正确缩进，并以 `endif()` 结束。

```cmake
if(ENABLE_TESTS)
  add_subdirectory(tests)
endif()
```

## 3.8\_注释说明（Documentation）

使用注释说明 CMake 文件中的复杂逻辑。

```cmake
# Find LlvmLld components required for building with llvm
find_package(LlvmLld 14.0.0 REQUIRED)
```

> 译注——原例中的英文文字：`Good` 表示推荐写法，`Bad` 表示不符合本页规则的写法；`Enable test suite` 为“启用测试套件”，`C++ standard version` 为“C++ 标准版本”，`Build shared libraries` 为“构建共享库”。最后一段注释为“查找使用 LLVM 构建所需的 LlvmLld 组件”。保留原代码和英文参数，便于与上游逐项对照。


对应官方文档源码：[doc/contribute/style/cmake.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/contribute/style/cmake.rst)。

本仓库的[对应源码](../../../doc/contribute/style/cmake.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="cmake-style-guidelines"></a>
<a id="cmake-style"></a>
<a id="general-formatting"></a>
<a id="commands-and-syntax"></a>
<a id="variable-naming"></a>
<a id="quoting"></a>
<a id="avoid-hardcoding-paths"></a>
<a id="conditional-logic"></a>
<a id="documentation"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：C语言编码风格](P002_C语言编码风格.md) · [本模块主线目录](../reading/coding_style.md) · [全部主线](../reading/README.md) · [下一篇：设备树编码风格](P004_设备树编码风格.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P002_C语言编码风格.md) · [返回大纲](大纲.md) · [下一章](P004_设备树编码风格.md)

</details>

<!-- reading-navigation:end -->
