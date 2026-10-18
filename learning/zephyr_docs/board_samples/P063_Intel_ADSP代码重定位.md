---
id: learning.zephyr-docs.board-samples.page-63
title: Intel_ADSP代码重定位
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/intel/adsp/code_relocation/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="intel_adsp_code_relocation"></a>

# 第63章\_代码重定位（Code relocation）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/intel/adsp/code_relocation/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/intel/adsp/code_relocation/README.rst/..)

<a id="overview"></a>

## 63.1 概述（Overview）

这个简单示例展示 Intel ADSP CAVS 开发板（v18 与 v25）的代码重定位功能，关键在于自定义链接器文件。rimage（用于签名镜像的工具）要求 ELF 文件的 TEXT、DATA 和 BSS 段连续排列，因此链接脚本进行了一些处理以满足这一要求。

> 译注——链接段术语：TEXT 是代码段，DATA 是已初始化数据段，BSS 是零初始化数据段；ELF 是可执行与可链接格式（Executable and Linkable Format）。BSS 的运行时空间不意味着镜像中保存同样大小的零字节。自定义脚本与 zephyr_code_relocate() 配置共同决定布局，不能只移动 C 函数声明就得到这里的结果。

<a id="building-and-running"></a>

## 63.2 构建与运行（Building and Running）

> 译注——执行前提：本节 west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链及对应板。构建目录由工具生成，下载与启动方式按具体板文档核对。本次仅核对文档和源码，未执行构建、烧录或硬件实验。

可按以下方式构建并执行应用：

> 译注——命令边界：原文这一段实际上只给出 west build，没有提供加载、启动或执行命令。构建成功只能确认生成镜像，执行还需对应 Intel ADSP 板支持的加载流程，本次没有执行实板验证。

```text
west build -b intel_adsp/cavs25 samples/boards/intel/adsp/code_relocation
```

<a id="sample-output"></a>

### 63.2.1 输出示例（Sample Output）

> 译注——源码布局：CMake 将 reloc.c 的 literal／text 放入 SRAM2，data／rodata 放入 SRAM3，bss 放入 SRAM4；自定义链接脚本还将全部 BSS 放入 SRAM4，并配合平台链接与镜像处理保持所需布局。日志中的 main location、reloc location、maybe_bss location 分别是函数和变量地址；0x9e 与 0xbe 涉及该平台的地址别名，具体数值会随镜像布局变化，不是主机文件路径。

```text
main location: 0xbe0105e4
Calling relocated code
Relocated code! reloc location 0xbe008010
maybe_bss location: 0x9e004218 maybe_bss value: 0
```

> 译注——源码入口：[main.c](../../../samples/boards/intel/adsp/code_relocation/src/main.c)；[prj.conf](../../../samples/boards/intel/adsp/code_relocation/prj.conf)；[CMakeLists.txt](../../../samples/boards/intel/adsp/code_relocation/CMakeLists.txt)；[linker_xtensa_intel_adsp_cavs.ld](../../../samples/boards/intel/adsp/code_relocation/linker_xtensa_intel_adsp_cavs.ld)。链接相对本篇定位，仓库参照版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/intel/adsp/code_relocation/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/intel/adsp/code_relocation/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/intel/adsp/code_relocation/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P062_Infineon示例目录.md) · [返回大纲](大纲.md) · [下一章](P064_Intel示例目录.md)
