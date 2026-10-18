---
id: learning.zephyr-docs.sca.sca-eclair
title: ECLAIR分析
kind: reference
status: maintained
domains: [zephyr, sca]
source_url: https://docs.zephyrproject.org/latest/develop/sca/eclair.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第10章\_ECLAIR分析

原文：[ECLAIR support](https://docs.zephyrproject.org/latest/develop/sca/eclair.html)。读取日期：2026-10-12，`latest`。

[Bugseng ECLAIR](https://www.bugseng.com/eclair/) 是经过认证的静态分析工具和软件验证平台。用途包括编码规则检查，尤其 MISRA 与 BARR-C 规范；软件度量计算；软件组件独立性与**免受干扰（Freedom from Interference）**检查；以及自动发现重要类别的软件错误。

> 译注：**汽车工业软件可靠性协会（Motor Industry Software Reliability Association，MISRA）**的规范规定软件编码要求；BARR-C 是 Barr Group 的嵌入式 C 编码规范名称。工具能够检查规则，不代表仅执行默认分析就证明应用符合全部规则或取得认证。

## 10.1\_安装与许可前提

必须安装 ECLAIR，并让其命令在操作系统 `PATH` 搜索路径中可见。可在 Bash 的任意目录检查版本：

```sh
eclair -version
```

使用时需要有效许可证或试用许可证，试用申请见 [ECLAIR试用页面](https://www.bugseng.com/eclair/free-trial)。

## 10.2\_运行默认分析

在准备好工具链及模块依赖的 Zephyr 源码根，用 Bash 执行 `west build`，加入 CMake 参数 `-DZEPHYR_SCA_VARIANT=eclair`：

```sh
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=eclair
```

默认只使用预定义规则集 `first_analysis`，即从项目规则中选择少量项目，检查分析环境是否正常工作。若要用其他规则集，需额外配置。

> 译注：命令中的 `mimxrt1064_evk` 是原例板目标。遇到工具、许可或构建错误，先修复对应前提，再判断是否真正运行分析；本次没有执行命令。

## 10.3\_配置文件与命令行选项

ECLAIR 接入可以用 CMake 选项文件配置，也可以直接传命令行参数。自行准备选项文件后，由 `ECLAIR_OPTIONS_FILE` 指定：

```sh
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=eclair -DECLAIR_OPTIONS_FILE=my_options.cmake
```

这里的 `my_options.cmake` 是用户提供的 CMake 文件，不是运行命令自动生成的文件。没有配置文件时默认仍是 `first_analysis`。

在命令行覆盖选项时，使用 `-DOption=ON` 或 `-DOption=OFF`，例如启用 **静态分析结果交换格式（Static Analysis Results Interchange Format，SARIF）**报告：

```sh
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=eclair -DECLAIR_REPORTS_SARIF=ON
```

## 10.4\_预定义规则集

Zephyr 规模较大，官方将[编码指南](../contributing/P009_编码准则.md)的检查划成五组，方便在个人机器上运行。**单翻译单元（Single Translation Unit，STU）**表示独立分析一个源码经预处理后的编译单元；**整个程序（Whole Program，WP）**分析则跨单元检查整体关系。

下表第一列是 ECLAIR 预定义规则集名称，第三列是选择它的 CMake 布尔配置项，用 `ON` 或 `OFF` 控制；中间一列解释各组实际检查范围。

| 规则集 | 内容 | CMake开关 |
| --- | --- | --- |
| `first_analysis` | 默认的小规模规则选择，用于确认环境正常。 | `ECLAIR_RULESET_FIRST_ANALYSIS` |
| `STU` | 可分别分析各翻译单元而验证的项目编码规则。 | `ECLAIR_RULESET_STU` |
| `STU_heavy` | 较复杂、耗时较多的单翻译单元规则。 | `ECLAIR_RULESET_STU_HEAVY` |
| `WP` | 全部整个程序层面的项目规则；MISRA 称这一层为 system。 | `ECLAIR_RULESET_WP` |
| `std_lib` | 关于 C 标准库的项目编码规则。 | `ECLAIR_RULESET_STD_LIB` |

另有 `zephyr_guidelines` 规则集，包含编码指南列出的全部主要规则，对应 `ECLAIR_RULESET_ZEPHYR_GUIDELINES`。

## 10.5\_使用自定义规则集

若需要自己的规则，而不使用 Zephyr 预定义集合：

1. 设置 `ECLAIR_RULESET_USER=ON`。
2. 自行创建名为 `analysis_<RULESET>.ecl` 的 ECLAIR 规则文件。
3. 用 `ECLAIR_USER_RULESET_NAME` 提供该规则集名称。
4. 若文件不在应用源码目录，用 `ECLAIR_USER_RULESET_PATH` 指定位置；它接受相对路径和完整路径。

`<RULESET>` 是实际规则集名的占位，名称与文件应对应。以上三个设置分别控制启用自定义规则、规则名和查找位置。

## 10.6\_附加报告格式

默认生成 `ecd` 文件；还可生成电子表格、文字文档、网页及其他分析交换格式。`DOC` 是 Word 文档格式，**开放文档文本（OpenDocument Text，ODT）**是开放文档格式，`XLSX` 是电子表格文件格式，**超文本标记语言（HyperText Markup Language，HTML）**用于网页报告。

下列 CMake 布尔配置项分别决定附加输出哪些报告；配置项与该行左侧的内容、格式一一对应。

| 报告内容与格式 | CMake开关 |
| --- | --- |
| 软件度量的电子表格 | `ECLAIR_METRICS_TAB` |
| 发现问题的电子表格 | `ECLAIR_REPORTS_TAB` |
| 发现问题的 SARIF 报告 | `ECLAIR_REPORTS_SARIF` |
| 纯文本摘要 | `ECLAIR_SUMMARY_TXT` |
| DOC 摘要 | `ECLAIR_SUMMARY_DOC` |
| ODT 摘要 | `ECLAIR_SUMMARY_ODT` |
| HTML 网页摘要 | `ECLAIR_SUMMARY_HTML` |
| 纯文本详细报告 | `ECLAIR_FULL_TXT` |
| DOC 详细报告 | `ECLAIR_FULL_DOC` |
| ODT 详细报告 | `ECLAIR_FULL_ODT` |
| HTML 网页详细报告 | `ECLAIR_FULL_HTML` |

## 10.7\_详细报告的区域显示范围

文本与 DOC 详细报告还可控制显示所有区域，或者仅显示首个区域。下表列出各报告形式对应的 CMake 布尔配置项：

| 报告形式 | 全部区域 | 首个区域 |
| --- | --- | --- |
| DOC | `ECLAIR_FULL_DOC_ALL_AREAS` | `ECLAIR_FULL_DOC_FIRST_AREA` |
| 纯文本 | `ECLAIR_FULL_TXT_ALL_AREAS` | `ECLAIR_FULL_TXT_FIRST_AREA` |

> 译注：这里的“区域（Area）”沿用 ECLAIR 的报告术语，控制详细诊断展示范围；它不是 Zephyr 的硬件内存分区。原文未进一步定义区域划分，应按所用工具版本的报告说明解释。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Parasoft分析](P009_Parasoft分析.md) · [本模块主线目录](../reading/sca.md) · [全部主线](../reading/README.md) · [下一篇：IAR_C_STAT分析](P011_IAR_C_STAT分析.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Parasoft分析](P009_Parasoft分析.md) · [返回大纲](大纲.md) · [下一章：IAR_C_STAT分析](P011_IAR_C_STAT分析.md)

</details>

<!-- reading-navigation:end -->
