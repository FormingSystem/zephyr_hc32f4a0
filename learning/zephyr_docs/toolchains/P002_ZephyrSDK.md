---
id: learning.zephyr-docs.toolchains.sdk
title: Zephyr SDK
kind: engineering
status: maintained
domains: [zephyr, toolchains]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="toolchain-zephyr-sdk"></a>

# 第2章\_Zephyr SDK

原文：[Zephyr SDK](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)。读取日期：2026-10-12，`latest`。

Zephyr **软件开发工具包（Software Development Kit，SDK）**包含面向各受支持架构的 GNU 和 LLVM 工具链，也包含定制的 QEMU、OpenOCD 等主机工具。

强烈建议使用 SDK；在某些情况下，它甚至是必需的，例如对某些架构执行 QEMU 测试。

## 2.1\_支持的架构

SDK 支持以下目标架构：

- ARC：32 位和 64 位；ARCv1、ARCv2、ARCv3。
- ARM：32 位和 64 位；ARMv6、ARMv7、ARMv8；A/R/M 系列。
- Microblaze：32 位。
- MIPS：32 位和 64 位。
- RISC-V：32 位和 64 位；RV32I、RV32E、RV64I。
- RX。
- SPARC：32 位和 64 位；SPARC V8、SPARC V9。
- x86：32 位和 64 位。
- Xtensa。

## 2.2\_安装包与变量

SDK 支持 Linux、macOS 和 Windows 这些主要操作系统，以压缩文件发布。为便于分发，预先打包了三种可下载形式：

| 安装包变体 | 主机工具 | 随包提供的工具链 |
| --- | --- | --- |
| `gnu` | 有 | 所有受支持架构的 GNU 工具，包括 Binutils、GCC 和 GDB |
| `llvm` | 有 | LLVM/Clang |
| `minimal` | 有 | 无 |

安装过程包括解压下载的安装包，并运行其中的 setup 脚本。

不论下载哪一种包，安装时都会提示选择要安装的工具链。如果 setup 脚本所在的本地目录没有所选工具链，脚本会在安装过程中下载。也可以预先把 GNU 和 LLVM 安装包下载、解压到同一目录树，从而在执行 setup 时无须再下载这两种工具链。

后文提供各操作系统的具体步骤。

如果没有选择其他工具链，构建系统会寻找 Zephyr SDK 并使用其中的工具链。将 `ZEPHYR_TOOLCHAIN_VARIANT` 环境变量设为 `zephyr`，可以明确要求这一选择。

SDK 安装在后文列出的默认位置之外时，如果希望自动发现，就必须运行 setup 脚本，将 SDK 注册到 CMake 包注册表。若不想注册，可以使用 `ZEPHYR_SDK_INSTALL_DIR` 指向 SDK 安装目录。

这个变量也可以指向包含多套 SDK 的父目录，让构建系统自动选择。例如设为 `/company/tools`，其中包含：

```text
/company/tools/zephyr-sdk-0.13.2
/company/tools/zephyr-sdk-a.b.c
/company/tools/zephyr-sdk-x.y.z
```

这样既能把多套 SDK 放在一个位置，也允许 Zephyr 构建系统选用适当版本。

> 译注：`minimal` 是不附带目标工具链的 SDK 包，不是某一种单独的交叉编译器。SDK 根目录与编译器可执行文件目录也不同：前者供 SDK 发现，后者由选中的架构工具链使用。前面的版本目录仅用于演示多版本布局，不是本页推荐安装的版本。

## 2.3\_版本兼容性

通常应把本页指定的 SDK 版本视作相应 Zephyr 版本的推荐版本。完整兼容关系见 [Zephyr SDK 版本兼容矩阵](https://github.com/zephyrproject-rtos/sdk-ng/wiki/Zephyr-Version-Compatibility#zephyr-sdk-version-compatibility-matrix)。

## 2.4\_安装Zephyr SDK

需要时可以把以下命令中的 `1.0.1` 换成其他版本；全部发行版本见 [SDK Releases](https://github.com/zephyrproject-rtos/sdk-ng/releases)。

以下步骤使用 GNU SDK 安装包，其中包含所有受支持架构的 GNU 工具链和主机工具。使用 LLVM SDK 时，把安装包文件名后缀 `_gnu` 换为 `_llvm`。

如果要卸载 SDK，只需删除其安装目录。

> 译注：下面保留官方独立安装示例及其终端。已有 SDK 时先检查其版本与兼容性，再决定是否复用；Windows 示例的 `%HOMEPATH%` 应按自己的工作区位置理解。本次翻译没有执行安装或卸载。

### 2.4.1\_Linux

先在 Linux 终端下载并校验安装包：

```bash
# Linux shell；下载目录为用户主目录。
cd ~
wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v1.0.1/zephyr-sdk-1.0.1_linux-x86_64_gnu.tar.xz
wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v1.0.1/sha256.sum | shasum --check --ignore-missing
```

主机为 64 位 Arm，例如 Raspberry Pi 时，将 `x86_64` 换为 `aarch64`，下载对应的 Linux SDK。

解压安装包：

```bash
# Linux shell；仍在下载目录。
tar xvf zephyr-sdk-1.0.1_linux-x86_64_gnu.tar.xz
```

建议解压到 `$HOME`、`$HOME/.local`、`$HOME/.local/opt`、`$HOME/bin`、`/opt` 或 `/usr/local`。

压缩包内含 `zephyr-sdk-<version>` 目录；例如在 `$HOME` 解压后，安装路径为 `$HOME/zephyr-sdk-<version>`。

运行 setup 脚本：

```bash
# Linux shell；从解压目录的父目录进入 SDK。
cd zephyr-sdk-1.0.1
./setup.sh
```

解压后只需运行一次 setup。如果完成初始化之后移动了 SDK 目录，必须重新运行 setup。

最后安装 udev 规则，使普通用户可以烧录多数受支持开发板：

```bash
# Linux shell；此示例对应用户主目录下的 x86-64 Linux SDK。
sudo cp ~/zephyr-sdk-1.0.1/hosttools/sysroots/x86_64-pokysdk-linux/usr/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d
sudo udevadm control --reload
```

> 译注：注意这里 SDK 1.0.1 的路径包含 `hosttools`。入门补充页的旧例子没有这一层；以实际 SDK 文件布局为准。主机架构为 AArch64 时也要确认对应的 sysroot 目录，不能直接套用 x86-64 路径。

### 2.4.2\_macOS

在 macOS 终端下载并校验：

```bash
# macOS shell；下载目录为用户主目录。
cd ~
curl -L -O https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v1.0.1/zephyr-sdk-1.0.1_macos-aarch64_gnu.tar.xz
curl -L https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v1.0.1/sha256.sum | shasum --check --ignore-missing
```

在同一目录解压：

```bash
tar xvf zephyr-sdk-1.0.1_macos-aarch64_gnu.tar.xz
```

推荐位置同样为 `$HOME`、`$HOME/.local`、`$HOME/.local/opt`、`$HOME/bin`、`/opt` 或 `/usr/local`。安装包自带 `zephyr-sdk-<version>` 顶层目录，因此在用户主目录解压后的路径为 `$HOME/zephyr-sdk-<version>`。

运行 setup：

```bash
# macOS shell；从解压目录的父目录进入 SDK。
cd zephyr-sdk-1.0.1
./setup.sh
```

解压后只需运行一次；初始化后若移动 SDK，须重新运行。

### 2.4.3\_Windows

以普通用户打开 `cmd.exe` 窗口，下载 SDK：

```bat
:: Windows cmd.exe；以下使用官方的用户主目录示例。
cd %HOMEPATH%
wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v1.0.1/zephyr-sdk-1.0.1_windows-x86_64_gnu.7z
```

解压：

```bat
:: Windows cmd.exe；仍在下载目录。
7z x zephyr-sdk-1.0.1_windows-x86_64_gnu.7z
```

建议解压到 `%HOMEPATH%` 或 `%PROGRAMFILES%`。压缩包包含 `zephyr-sdk-<version>` 目录，因此解压到 `%HOMEPATH%` 后，安装位置为 `%HOMEPATH%\zephyr-sdk-<version>`。

运行 setup：

```bat
:: Windows cmd.exe；从解压目录的父目录进入 SDK。
cd zephyr-sdk-1.0.1
setup.cmd
```

解压后只需运行一次；初始化完成后移动 SDK 目录，必须重新运行。

> 译注：官方下载工具、解压工具和版本检查的前提在[入门指南](../getting_started/P002_入门指南.md)。setup 的交互内容与所选 SDK 包和版本有关；应确认工具链已实际安装，再进行构建。本文为翻译，不把命令列出视为安装成功记录。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：工具链入口](P001_工具链入口.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：环境变量](P003_环境变量.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：工具链入口](P001_工具链入口.md) · [返回大纲](大纲.md) · [下一章：环境变量](P003_环境变量.md)

</details>

<!-- reading-navigation:end -->
