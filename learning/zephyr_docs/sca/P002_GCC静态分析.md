---
id: learning.zephyr-docs.sca.sca-gcc
title: GCC静态分析
kind: reference
status: maintained
domains: [zephyr, sca]
source_url: https://docs.zephyrproject.org/latest/develop/sca/gcc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第2章\_GCC静态分析

原文：[GCC static analysis support](https://docs.zephyrproject.org/latest/develop/sca/gcc.html)。读取日期：2026-10-12，`latest`。

**GNU编译器集合（GNU Compiler Collection，GCC）**从第 10 版引入静态分析，通过 `-fanalyzer` 启用。相较传统编译警告，这个选项执行更深入、开销也更大的代码分析。

## 2.1\_通过构建启用分析

调用 `west build` 时传入 CMake 设置 `-DZEPHYR_SCA_VARIANT=gcc`：

```sh
west build -b qemu_x86 samples/userspace/hello_world_user -- -DZEPHYR_SCA_VARIANT=gcc
```

> 译注：在已准备工具链与依赖的 Zephyr 源码根，用 Bash 执行。`qemu_x86` 是官方模拟目标，命令选择 `hello_world_user` 用户空间示例；这里执行的是构建分析，不代表启动模拟器，更不代表 HC32 实板运行。构建失败先按实际编译或配置错误排查。

## 2.2\_配置分析器选项

GCC 分析器可用特定选项控制，官方参考分别说明[分析行为](https://gcc.gnu.org/onlinedocs/gcc/Static-Analyzer-Options.html)和[诊断信息格式](https://gcc.gnu.org/onlinedocs/gcc/Diagnostic-Message-Formatting-Options.html)。

`GCC_SCA_OPTS` 是以分号分隔的 GCC 分析选项列表，可在 CMake 命令行传入，也可设为环境变量。下面示例输出 **JSON（JavaScript Object Notation，数据交换格式）**诊断，并设置分析详细程度：

```sh
west build -b stm32h573i_dk samples/hello_world -- -DZEPHYR_SCA_VARIANT=gcc -DGCC_SCA_OPTS="-fdiagnostics-format=json;-fanalyzer-verbosity=3"
```

分析器持续开发，新版可能增加选项或修复行为；版本变化见 [GCC StaticAnalyzer说明](https://gcc.gnu.org/wiki/StaticAnalyzer)。

## 2.3\_选择较新的分析器版本

Zephyr 所用工具链未必包含最新 GCC 分析器。原文提供改用较新 [GNU Arm Embedded工具链](https://docs.zephyrproject.org/latest/develop/toolchains/gnu_arm_embedded.html)的方式：

```sh
west build -b stm32h573i_dk samples/hello_world -- -DZEPHYR_SCA_VARIANT=gcc -DZEPHYR_TOOLCHAIN_VARIANT=gnuarmemb -DGNUARMEMB_TOOLCHAIN_PATH=...
```

> 译注：`GNUARMEMB_TOOLCHAIN_PATH=...` 中的省略号是实际工具链根目录的替换项，不能直接执行。工具链须先安装并适配当前目标；这次构建选用的编译器也随之改变，不只是为旧编译器增加一个分析开关。已有构建目录含工具链缓存时，应按[west构建说明](https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html#west-building)重新配置适当目录。本次没有安装或切换工具链。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：静态代码分析入口](P001_静态代码分析入口.md) · [本模块主线目录](../reading/sca.md) · [全部主线](../reading/README.md) · [下一篇：Clang静态分析](P003_Clang静态分析.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：静态代码分析入口](P001_静态代码分析入口.md) · [返回大纲](大纲.md) · [下一章：Clang静态分析](P003_Clang静态分析.md)

</details>

<!-- reading-navigation:end -->
