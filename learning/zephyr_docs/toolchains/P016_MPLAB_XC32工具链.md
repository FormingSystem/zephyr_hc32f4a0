---
id: learning.zephyr-docs.toolchains.page-16
title: MPLAB_XC32工具链
kind: reference
status: maintained
domains: [zephyr, toolchains, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/xc32_toolchain.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mplab-xc32"></a>
<a id="toolchain-xc32"></a>

# 第16章\_MPLAB\_XC32工具链

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/toolchains/xc32_toolchain.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 16.1\_安装与工具链变量

下载并安装适合当前操作系统的 [MPLAB XC32编译器（Compiler）](https://www.microchip.com/en-us/tools-resources/develop/mplab-xc-compilers)。

按[环境变量说明](P003_环境变量.md#env-vars)设置：

- [`ZEPHYR_TOOLCHAIN_VARIANT`](P003_环境变量.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) 为 `xc32`。
- `XC32_TOOLCHAIN_PATH` 为工具链安装目录。

## 16.2\_检查当前环境

以下是原文的交互式Shell会话，用来确认当前环境变量是否正确。实际 `XC32_TOOLCHAIN_PATH` 可以不同。Linux／macOS使用Shell变量，Windows使用cmd变量语法；提示符及echo后面的输出行不作为命令复制。

```text
# Linux, macOS:
$ echo $ZEPHYR_TOOLCHAIN_VARIANT
xc32
$ echo $XC32_TOOLCHAIN_PATH
/opt/microchip/xc32/v5.00

# Windows:
> echo %ZEPHYR_TOOLCHAIN_VARIANT%
xc32
> echo %XC32_TOOLCHAIN_PATH%
C:\Microchip\xc32\v5.00
```

> 译注——目录检查：应确认变体输出为xc32、路径对应已安装版本。[官方generic.cmake](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/cmake/toolchain/xc32/generic.cmake)检查XC32_TOOLCHAIN_PATH并形成bin/xc32-工具前缀。目录不存在时先修正安装或变量，不能以示例版本目录代替实际安装。

## 16.3\_Microchip器件系列包

针对Microchip片上系统（System on Chip，SoC），把 `XC_PACK_DIR` 设为包含已安装Microchip器件系列包（Device Family Pack，DFP）的根目录。

**注意：**Zephyr通过XC_PACK_DIR查找与所选SoC匹配的DFP，并将需要的 `-mdfp` 和 `-mprocessor` 参数传给XC32工具链。

原文示例：

```text
# Linux, macOS:
$ export XC_PACK_DIR=/home/path/.packs/microchip

# Windows:
> set XC_PACK_DIR=C:\Users\path\.mchp_packs\Microchip
```

> 译注——两类安装位置：编译器根由XC32_TOOLCHAIN_PATH指定，器件包根由XC_PACK_DIR指定，两者不能互换。原例中的path是占位用户目录；应换成读者实际安装器件包的根目录，并确认存在目标SoC对应包。这些工具目录不限定仓库位置。


对应官方文档源码：[doc/develop/toolchains/xc32_toolchain.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/toolchains/xc32_toolchain.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/toolchains/xc32_toolchain.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

<a id="index-0"></a>
<a id="index-1"></a>
<a id="index-2"></a>
<a id="index-3"></a>
<a id="index-4"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Intel_oneAPI工具包](P015_Intel_oneAPI工具包.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P015_Intel_oneAPI工具包.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
