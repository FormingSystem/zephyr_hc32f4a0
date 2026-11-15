---
id: learning.zephyr-docs.toolchains.page-12
title: Cadence_XCC工具链
kind: reference
status: maintained
domains: [zephyr, toolchains, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/cadence_xcc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="cadence-tensilica-xtensa-c-c-compiler-xcc"></a>
<a id="toolchain-cadence-xcc"></a>

# 第12章\_Cadence\_XCC工具链

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/toolchains/cadence_xcc.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 12.1\_取得与安装工具链

取得针对实际片上系统（System on Chip，SoC）的Tensilica软件开发工具包（Software Development Toolkit）。通常包含两部分：Xtensa Xplorer提供必要的可执行程序和库；安装在Xplorer之上的SoC专用附加包（Add-on）使编译器能够为该SoC生成代码。

先安装Xtensa Xplorer，再安装SoC附加包，具体按Cadence提供的SDK安装说明执行。不同SDK可能提供两套编译器：基于GNU编译器集合（GNU Compiler Collection，GCC）的 `xt-xcc` 及相关工具，或基于Clang的 `xt-clang` 及相关工具。

必须取得SDK使用许可证（License），或能够访问远程许可证服务器（Licensing Server）。

## 12.2\_设置环境变量

按[环境变量说明](P003_环境变量.md#env-vars)设置：

- [`ZEPHYR_TOOLCHAIN_VARIANT`](P003_环境变量.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) 为 `xcc` 或 `xt-clang`。
- `XTENSA_TOOLCHAIN_PATH` 为工具链安装目录。
- SoC标识（SoC ID）与SDK版本有两种指定方式，原文要求二选一，不同时使用。

为单个SoC构建时，`XTENSA_CORE` 指定应用目标SoC标识，`TOOLCHAIN_VER` 指定Xtensa SDK版本。

为多个SoC构建时，针对每个SoC和开发板组合，设置 `XTENSA_CORE_{normalized_board_target}` 为目标SoC标识；原文正文写 `TOOLCHAIN_VAR_{normalized_board_target}` 来指定SDK版本。

> 译注——变量拼写：原文后面的多SoC例子实际使用TOOLCHAIN_VER前缀。所读[官方接入代码](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/cmake/toolchain/xcc/common.cmake)通过zephyr_get读取 `TOOLCHAIN_VER_${NORMALIZED_BOARD_TARGET}` 或 `TOOLCHAIN_VER`，而非TOOLCHAIN_VAR前缀。配置时应采用VER拼写；此处保留原文差异以便对照。normalized_board_target是规范化后的板目标名称，例中的斜杠转为下划线。

## 12.3\_单SoC与多SoC示例

原文假定SDK装在 `/opt/xtensa`，用于 `intel_adsp/ace15_mtpm` 应用开发。以下均为Linux Shell示例，工具安装路径和版本按读者实际安装修改；它们不是仓库克隆位置要求。

单SoC：

```bash
# Linux
export ZEPHYR_TOOLCHAIN_VARIANT=xt-clang
export XTENSA_TOOLCHAIN_PATH=/opt/xtensa/XtDevTools/install/tools/
export XTENSA_CORE=ace10_LX7HiFi4_2022_10
export TOOLCHAIN_VER=RI-2022.10-linux
```

多SoC：

```bash
# Linux
export ZEPHYR_TOOLCHAIN_VARIANT=xt-clang
export XTENSA_TOOLCHAIN_PATH=/opt/xtensa/XtDevTools/install/tools/
export TOOLCHAIN_VER_intel_adsp_ace15_mtpm=RI-2022.10-linux
export XTENSA_CORE_intel_adsp_ace15_mtpm=ace10_LX7HiFi4_2022_10
```

## 12.4\_Clang编译器的历史问题

使用基于Clang的编译器时，将 [`ZEPHYR_TOOLCHAIN_VARIANT`](P003_环境变量.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) 设为 `xt-clang`。该编译器可能包含旧LLVM缺陷，产生如下错误：

```text
/tmp/file.s: Assembler messages:
/tmp/file.s:20: Error: file number 1 already allocated
clang-3.9: error: Xtensa-as command failed with exit code 1
```

若遇到此错误，将 `XCC_NO_G_FLAG` 设为 `1`，例如：

```bash
# Linux
export XCC_NO_G_FLAG=1
```

> 译注——错误对照：file number 1 already allocated表示汇编文件编号1已被占用，随后Xtensa-as命令以退出码1失败。这里保留原错误日志与针对该错误的设置，不将它作为所有版本的默认选项。环境设置作用于当前Shell及其子进程；失败时先核对工具版本、目标配置和许可证，再按对应错误处理。


对应官方文档源码：[doc/develop/toolchains/cadence_xcc.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/toolchains/cadence_xcc.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/toolchains/cadence_xcc.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

<a id="index-0"></a>
<a id="index-1"></a>
<a id="index-2"></a>
<a id="index-3"></a>
<a id="index-4"></a>
<a id="index-5"></a>
<a id="index-6"></a>
<a id="index-7"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：嵌入式链接器（ELD）](P011_嵌入式链接器ELD.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：ARC_MetaWare工具链](P013_ARC_MetaWare工具链.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P011_嵌入式链接器ELD.md) · [返回大纲](大纲.md) · [下一章](P013_ARC_MetaWare工具链.md)

</details>

<!-- reading-navigation:end -->
