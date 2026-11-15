---
id: learning.zephyr-docs.sca.sca-clang
title: Clang静态分析
kind: reference
status: maintained
domains: [zephyr, sca]
source_url: https://docs.zephyrproject.org/latest/develop/sca/clang.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第3章\_Clang静态分析

原文：[Clang static analyzer support](https://docs.zephyrproject.org/latest/develop/sca/clang.html)。读取日期：2026-10-12，`latest`。

**Clang静态分析器（Clang Static Analyzer）**建立在 Clang 与 LLVM 之上。Clang 包含一组可复用 C++ 库，供构建源码级工具；严格说来，分析器属于 Clang，其分析引擎本身也是可供不同调用方复用的库。

## 3.1\_为什么使用analyze-build

LLVM 提供专用工具 `scan-build`、`analyze-build`，也支持调用 `clang` 时传入 `--analyze`：

| 方式 | 行为及对Zephyr的影响 |
| --- | --- |
| `scan-build` | 适合通过简单 Makefile 的 `CC` 编译器变量构建的项目；它包装并替换编译器调用，以执行分析。 |
| `analyze-build` | 属于 `scan-build` 工具组，只依赖 `compile_commands.json` **编译命令数据库（Compilation Database）**分析各源码文件。 |
| `clang --analyze` | 执行分析而不生成目标文件，后续无法链接；在 Zephyr 中第一次链接失败就会终止整个流程。 |

由于 Zephyr 的构建流程较复杂，使用 `analyze-build` 是这里最简单的接入方式。详情见 [Clang静态分析器文档](https://clang.llvm.org/docs/ClangStaticAnalyzer.html)。

## 3.2\_安装分析工具

原文说明 LLVM 二进制工具集包含 `scan-build` 及其子工具 `analyze-build`。确保二者所在目录进入 `PATH`，即操作系统查找可执行程序的搜索路径。

也可以从 [Python包索引中的scan-build](https://pypi.org/project/scan-build/)安装独立 Python 包：

```sh
pip install scan-build
```

> 译注：在选定的 Python 环境中执行，工作目录不限；本项目已有虚拟环境时应先激活它，确保安装工具的环境与构建可见的环境一致。不同 LLVM 发行包拆分可能不同，应检查实际命令是否存在，不能只凭已安装 `clang` 推断所有辅助工具都已提供。

## 3.3\_运行与报告

**原文前提：**项目必须使用 LLVM 工具链构建，并生成 `compile_commands.json` 数据库。

从 Zephyr 源码根，在 Bash 中传入 LLVM 工具链参数以及 `-DZEPHYR_SCA_VARIANT=clang`：

```sh
west build -b qemu_x86 samples/userspace/hello_world_user -- -DZEPHYR_TOOLCHAIN_VARIANT=host/llvm -DLLVM_TOOLCHAIN_PATH=... -DZEPHYR_SCA_VARIANT=clang
```

> 译注：先把 `LLVM_TOOLCHAIN_PATH=...` 替换为已安装工具链根。`host/llvm` 是原文使用的工具链选择值，`qemu_x86` 是示例板目标；构建失败时先确认目标与工具链是否匹配，再检查分析器。此命令没有实际执行。

默认生成 HTML 网页报告，也可以选择 **静态分析结果交换格式（Static Analysis Results Interchange Format，SARIF）**、**属性列表（Property List，plist）**等输出。

## 3.4\_配置分析参数

完整选项见 `analyze-build` 与 `scan-build` 的命令帮助，例如：

```sh
analyze-build --help
```

默认已启用 `--analyze-headers`，会分析 `#include` 文件中的函数。

`CLANG_SCA_OPTS` 是分号分隔的 `analyze-build` 选项列表，可由 CMake 命令行或环境变量提供。下面请求 SARIF 和详细输出：

```sh
west build -b stm32h573i_dk samples/hello_world -- -DZEPHYR_TOOLCHAIN_VARIANT=host/llvm -DLLVM_TOOLCHAIN_PATH=... -DZEPHYR_SCA_VARIANT=clang -DCLANG_SCA_OPTS="--sarif;--verbose"
```

> 译注：原文叙述中的分析选项有排版用长横线，本译文写作可识别的两个半角连字符；原代码块保持不变。分号列表用引号保护，避免被 Bash 当作多条命令。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：GCC静态分析](P002_GCC静态分析.md) · [本模块主线目录](../reading/sca.md) · [全部主线](../reading/README.md) · [下一篇：Sparse静态分析](P004_Sparse静态分析.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：GCC静态分析](P002_GCC静态分析.md) · [返回大纲](大纲.md) · [下一章：Sparse静态分析](P004_Sparse静态分析.md)

</details>

<!-- reading-navigation:end -->
