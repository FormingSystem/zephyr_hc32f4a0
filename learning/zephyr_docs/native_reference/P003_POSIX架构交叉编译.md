---
id: learning.zephyr-docs.native-reference.page-3
title: POSIX架构交叉编译
kind: reference
status: maintained
domains: [zephyr, boards, posix]
source_url: https://docs.zephyrproject.org/latest/boards/native/native_sim/doc/cross_compile.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_POSIX架构交叉编译

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/native/native_sim/doc/cross_compile.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="cross-compiling-the-posix-architecture"></a>
<a id="posix-arch-cross-compile"></a>

`native_sim` 及其他基于 POSIX 架构的目标，主要用于开发期间在工作站上调试和插桩（Instrumentation）。但有时在一台机器上构建、到另一台机器上运行也有用。如果两台机器的处理器架构不同，就需要交叉编译（Cross-compilation）。

> 原文警告：`native_sim` 是开发和调试辅助工具，旨在实现可重现运行，便于插桩与访问执行状态。出于安全原因，绝不应交付在 `native_sim` 中运行生产代码的最终产品。

<a id="preparing-your-host"></a>

## 3.1\_准备宿主机

> 原文注意：本指南说明如何配置 Ubuntu 24.04 x86_64 开发机，以便交叉编译32位 ARM（arm 或 armhf）及64位 ARM（aarch64）目标，并利用该环境构建。交叉编译环境有多种配置方式，宿主或目标架构也可能不同，因此可以把此指南作为参考。

首先需要在开发机上安装交叉编译工具链（Cross-compiling Toolchain）。在 Ubuntu 24.04 x86_64 中，安装 `gcc-aarch64-linux-gnu` 软件包可支持64位 ARM 构建。它将工具链二进制安装为 `/usr/bin/aarch64-linux-gnu-*`，库和头文件安装到 `/usr/aarch64-linux-gnu/`。

同样，对于32位 armhf，`gcc-arm-linux-gnueabihf` 软件包将二进制安装为 `/usr/bin/arm-linux-gnueabihf-*`，库和头文件安装到 `/usr/arm-linux-gnueabihf/`。

> 原文注意：在 Ubuntu 24.04 中，`gcc-multilib` 与 `gcc-aarch64-linux-gnu` 冲突，而 x86_64 上的32位构建指南要求安装前者。这不一定构成问题，因为 `gcc-multilib` 主要是元软件包（Meta-package）；真正需要的是它的依赖包。可先安装 `gcc-multilib` 和 `g++-multilib`，再删除这两个包但保留依赖，也可直接安装依赖。务必不要随后把这些依赖一起删除。

译注：这里的 `/usr/...` 均为官方 Ubuntu 软件包安装位置，不是文档仓库路径；实际工具链布局不同时，应使用对应工具链前缀。

<a id="building"></a>

## 3.2\_构建

向 CMake 传入以下选项：

| 选项 | 设置与含义 |
| --- | --- |
| `ZEPHYR_TOOLCHAIN_VARIANT` | 设置为 `cross-compile`，选择交叉编译工具链变体 |
| `NATIVE_TARGET_HOST` | 设置为目标机器架构：本例64位 ARM 使用 `aarch64`，32位 ARM 使用 `arm` |
| `CROSS_COMPILE` | 设置为交叉编译工具链前缀（Toolchain Prefix），本例为 `/usr/bin/aarch64-linux-gnu-` 或 `/usr/bin/arm-linux-gnueabihf-` |
| `SYSROOT_DIR` | 按所用编译器的需要，设置为编译器系统根目录（Sysroot）路径 |

本例为 aarch64 构建 `hello_world` 示例：

```shell
west build -b native_sim//64 samples/hello_world -- -DNATIVE_TARGET_HOST=aarch64 -DZEPHYR_TOOLCHAIN_VARIANT=cross-compile -DCROSS_COMPILE=/usr/bin/aarch64-linux-gnu-
```

或者为32位 armhf 构建：

```shell
west build -b native_sim samples/hello_world -- -DNATIVE_TARGET_HOST=arm -DZEPHYR_TOOLCHAIN_VARIANT=cross-compile -DCROSS_COMPILE=/usr/bin/arm-linux-gnueabihf-
```

现在生成了可执行文件 `zephyr/zephyr.exe`，可以复制到目标机器并运行。

<a id="a-quick-test-executing-it-in-your-host"></a>

## 3.3\_快速测试：在宿主机执行

也可以在开发宿主机上执行交叉编译后的程序。为此需要 [QEMU 用户空间仿真器（User-space Emulator）](https://www.qemu.org/docs/master/user/main.html)，在 Ubuntu 24.04 中可通过 `qemu-user` 软件包安装。

64位 ARM 版本运行方式如下：

```shell
$ qemu-aarch64 -L /usr/aarch64-linux-gnu/ build/zephyr/zephyr.exe
# Press Ctrl+C to exit
```

32位 ARM 版本运行方式如下：

```shell
$ qemu-armhf -L /usr/arm-linux-gnueabihf/ build/zephyr/zephyr.exe
# Press Ctrl+C to exit
```

代码中的 `$` 表示shell提示符，`Press Ctrl+C to exit` 表示按 `Ctrl+C` 退出。

---

[上一章](P002_POSIX架构.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P004_Native_Simulator本机模拟器.md)
