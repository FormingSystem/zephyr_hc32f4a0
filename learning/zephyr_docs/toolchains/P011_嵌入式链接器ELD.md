---
id: learning.zephyr-docs.toolchains.tc_eld
title: 嵌入式链接器（ELD）
kind: reference
status: maintained
domains: [zephyr, toolchains]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/eld.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_嵌入式链接器（ELD）

原文：[嵌入式链接器（ELD）](https://docs.zephyrproject.org/latest/develop/toolchains/eld.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

嵌入式链接器（Embedded Linker，ELD）是 Qualcomm 开源、基于 LLVM 且兼容 GNU 的链接器。用 LLVM 工具链构建 Zephyr 时，例如使用 Arm 嵌入式工具链或主机 Clang，可以用它替代 LLD 或 GNU ld。ELD 本身的详细说明见 [ELD用户指南](https://qualcomm.github.io/eld/)和[官方仓库](https://github.com/qualcomm/eld)。

ELD 只提供链接器 `ld.eld`；编译源文件仍需要独立的 C/C++ 工具链。

## 11.1\_安装（Installation）

有三种取得 ELD 的方式：

1. **每日构建的二进制发行版（Nightly Binary Release）：**[ELD发行页](https://github.com/qualcomm/eld/releases)发布预构建的 `ld.eld`。
2. **从源码构建（Build from Source）：**按照 [ELD README](https://github.com/qualcomm/eld#building-eld-and-running-tests)，基于 LLVM 源码树构建 ELD。集成的 `llvm-project` 构建会在构建树的 `bin/` 目录生成 `ld.eld`。
3. **通过cpullvm取得完整工具链：**[cpullvm工具链](https://github.com/qualcomm/cpullvm-toolchain)是面向 Arm、AArch64 和 RISC-V 嵌入式目标的完整 LLVM 工具链，除 Clang、运行时库和头文件外，还同时包含 `ld.eld` 与 `ld.lld`。[cpullvm发行页](https://github.com/qualcomm/cpullvm-toolchain/releases)提供 Linux 与 Windows 的预构建压缩包。官方页记录 cpullvm 22.1.1 已在 ELD 的持续集成（Continuous Integration，CI）中用 Zephyr 测试。

前两种方式只提供 `ld.eld`；要构建 Zephyr，仍需单独准备包含 Clang、运行时库和头文件的 LLVM 工具链。

验证安装的示例会话：

```console
$ ld.eld --version
eld 22.0 (GNU Compatible linker)
```

要求 ELD 22.0 或更新版本。

## 11.2\_使用（Usage）

通过 `host/llvm` 工具链变体（Toolchain Variant）选择 ELD。将 `LLVM_TOOLCHAIN_PATH` 指向 LLVM 工具链，例如 cpullvm 安装目录，或在 `bin/` 目录／`PATH` 中能找到 `ld.eld` 的其他工具链；再将 `CONFIG_LLVM_USE_ELD` 设为 `y`。

例如：

```bash
west build ... -- -DZEPHYR_TOOLCHAIN_VARIANT=host/llvm \
                  -DLLVM_TOOLCHAIN_PATH=<path-to-llvm-toolchain> \
                  -DCONFIG_LLVM_USE_ELD=y
```

配置 LLVM 工具链的更多信息见 [Arm嵌入式工具链（ATfE）](P008_Arm嵌入式工具链.md)或 [Zephyr SDK](P002_ZephyrSDK.md)。`PATH` 的设置方式见[环境变量](P003_环境变量.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：IAR Arm工具链](P010_IARArm工具链.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：Cadence_XCC工具链](P012_Cadence_XCC工具链.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P010_IARArm工具链.md) · [返回大纲](大纲.md) · [下一章](P012_Cadence_XCC工具链.md)

</details>

<!-- reading-navigation:end -->
