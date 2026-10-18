---
id: learning.zephyr-docs.toolchains.tc_atfe
title: Arm嵌入式工具链（ATfE）
kind: reference
status: maintained
domains: [zephyr, toolchains]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/arm_toolchain_for_embedded.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_Arm嵌入式工具链（ATfE）

原文：[Arm嵌入式工具链（ATfE）](https://docs.zephyrproject.org/latest/develop/toolchains/arm_toolchain_for_embedded.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

Arm 嵌入式工具链（Arm Toolchain for Embedded，ATfE）是 Arm 提供的 C/C++ 工具链，基于自由开源的 LLVM 编译器基础设施（LLVM Compiler Infrastructure），并使用面向裸机目标（Bare-metal Target）的 Picolib C 库。

ATfE 经过专门调优，特别关注较新的 Arm 产品（2024年之后）的性能，例如64位 Arm 架构（AArch64），以及 M 配置向量扩展（M-Profile Vector Extension，MVE，一种32位 Armv8.1-M 扩展）。

## 8.1\_安装（Installation）

下载适合当前操作系统的 [Arm 嵌入式工具链构建版本](https://developer.arm.com/Tools%20and%20Software/Arm%20Toolchain%20for%20Embedded)，并解压到文件系统中。

设置以下[环境变量](P003_环境变量.md)：

- `ZEPHYR_TOOLCHAIN_VARIANT` 设为 `host/llvm`。
- `LLVM_TOOLCHAIN_PATH` 设为工具链安装目录。

可以按以下 shell 会话示例，检查当前环境中的变量设置。读者系统中的 `LLVM_TOOLCHAIN_PATH` 值可能不同。

Ubuntu：

```console
echo $ZEPHYR_TOOLCHAIN_VARIANT
host/llvm
echo $LLVM_TOOLCHAIN_PATH
/home/you/Downloads/ATfE
```

macOS：

```console
echo $ZEPHYR_TOOLCHAIN_VARIANT
host/llvm
echo $LLVM_TOOLCHAIN_PATH
/home/you/Downloads/ATfE
```

Windows 命令提示符：

```console
> echo %ZEPHYR_TOOLCHAIN_VARIANT%
host/llvm
> echo %LLVM_TOOLCHAIN_PATH%
C:\ATfE
```

也可以在为 Zephyr 应用生成构建系统时，将 `ZEPHYR_TOOLCHAIN_VARIANT` 和 `LLVM_TOOLCHAIN_PATH` 设为 CMake 变量：

```bash
west build ... -- -DZEPHYR_TOOLCHAIN_VARIANT=host/llvm -DLLVM_TOOLCHAIN_PATH=...
```

> 译注：上面的会话块包含命令和预期输出，不能把输出行作为命令执行。`/home/you/Downloads/ATfE` 和 `C:\ATfE` 是原页示意安装目录，实际路径取决于读者的安装位置；`...` 也需替换为实际构建参数。

## 8.2\_工具链设置（Toolchain Settings）

LLVM 与 GNU 工具具有广泛兼容性，因此使用任何 LLVM 工具链构建时，都需要指定一些设置，让编译器知道应使用哪些工具。

**链接器（Linker）：**

- `CONFIG_LLVM_USE_LLD=y`：使用 LLVM 链接器。
- `CONFIG_LLVM_USE_LD=y`：使用 GNU LD 链接器。

**运行时库（Runtime Library）：**

- `CONFIG_COMPILER_RT_RTLIB=y`：使用 LLVM 运行时库。
- `CONFIG_LIBGCC_RTLIB=y`：使用 LibGCC 运行时库。

同时选择 LLVM 链接器和 LLVM 运行时库的示例：

```bash
west build ... -- -DZEPHYR_TOOLCHAIN_VARIANT=host/llvm -DLLVM_TOOLCHAIN_PATH=... -DCONFIG_LLVM_USE_LLD=y -DCONFIG_COMPILER_RT_RTLIB=y
```

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Arm Compiler 6](P007_ArmCompiler6.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：自定义CMake工具链](P009_自定义CMake工具链.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P007_ArmCompiler6.md) · [返回大纲](大纲.md) · [下一章](P009_自定义CMake工具链.md)

</details>

<!-- reading-navigation:end -->
