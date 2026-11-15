---
id: learning.zephyr-docs.toolchains.page-15
title: Intel_oneAPI工具包
kind: reference
status: maintained
domains: [zephyr, toolchains, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/intel_oneapi_toolkit.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="intel-oneapi-toolkit"></a>
<a id="toolchain-intel-oneapi-toolkit"></a>

# 第15章\_Intel\_oneAPI工具包

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/toolchains/intel_oneapi_toolkit.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 15.1\_下载与环境设置

下载 [Intel oneAPI基础工具包（Base Toolkit）](https://software.intel.com/content/www/us/en/develop/tools/oneapi/all-toolkits.html)。

原文假定工具安装在 `/opt/intel/oneApi`，用以下方式设置环境。代码保留Linux／macOS的Shell分支及Windows的cmd分支；`>` 是原会话提示符。

```bash
# Linux, macOS:
export ONEAPI_TOOLCHAIN_PATH=/opt/intel/oneapi
source $ONEAPI_TOOLCHAIN_PATH/compiler/latest/env/vars.sh

# Windows:
> set ONEAPI_TOOLCHAIN_PATH=C:\Users\Intel\oneapi
```

> 译注——路径和大小写：原文前一句写oneApi，命令路径写oneapi；在区分大小写的系统上应以实际安装目录为准。原Windows路径中的Intel是官方示例用户目录，不是仓库作者路径，也不要求读者按此用户名安装。ONEAPI_TOOLCHAIN_PATH指工具安装根，和仓库所在位置无关；后续路径都从该根解析。

## 15.2\_完整oneAPI环境与Python影响

若要设置完整oneAPI环境，原文使用：

```bash
source  /opt/intel/oneapi/setvars.sh
```

上述操作还会把Python环境切换为工具链使用的环境，可能与Zephyr所用Python环境冲突。

> 译注——操作结果：source在当前Shell加载脚本，修改的是当前进程环境及其后续子进程，并非单纯显示工具位置。应在同一终端核对实际Python及依赖，再运行Zephyr构建；若环境发生冲突，先回到明确的工具环境设置步骤处理，而不是继续安装到未知Python中。

最后，将 [`ZEPHYR_TOOLCHAIN_VARIANT`](P003_环境变量.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) 设置为 `oneApi`。

> 译注——变量与源码：[官方oneApi/generic.cmake](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/cmake/toolchain/oneApi/generic.cmake)会读取ONEAPI_ROOT或ONEAPI_TOOLCHAIN_PATH，再根据主机系统选择编译器路径。oneApi是Zephyr使用的变体拼写；不要将产品名称的大小写直接替换到变量值中。本页保留官方分支，没有实测这些系统。


对应官方文档源码：[doc/develop/toolchains/intel_oneapi_toolkit.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/toolchains/intel_oneapi_toolkit.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/toolchains/intel_oneapi_toolkit.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

<a id="index-0"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Hexagon_LLVM工具链](P014_Hexagon_LLVM工具链.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：MPLAB_XC32工具链](P016_MPLAB_XC32工具链.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P014_Hexagon_LLVM工具链.md) · [返回大纲](大纲.md) · [下一章](P016_MPLAB_XC32工具链.md)

</details>

<!-- reading-navigation:end -->
