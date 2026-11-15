---
id: learning.zephyr-docs.sca.sca-codechecker
title: CodeChecker分析
kind: reference
status: maintained
domains: [zephyr, sca]
source_url: https://docs.zephyrproject.org/latest/develop/sca/codechecker.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第7章\_CodeChecker分析

原文：[CodeChecker support](https://docs.zephyrproject.org/latest/develop/sca/codechecker.html)。读取日期：2026-10-12，`latest`。

[CodeChecker](https://codechecker.readthedocs.io/) 是**静态分析基础设施（Static Analysis Infrastructure）**，负责调用构建主机上已有的分析器并处理结果。可使用的工具包括 [Clang-Tidy](https://clang.llvm.org/extra/clang-tidy/)、[Clang Static Analyzer](https://clang-analyzer.llvm.org/) 和 [Cppcheck](https://cppcheck.sourceforge.io/)，各分析器的安装方法应查其自己的文档。

## 7.1\_安装与构建接入

CodeChecker 自身是 [Python包](https://pypi.org/project/codechecker/)，可安装为：

```sh
pip install codechecker
```

> 译注：在选定并已激活的 Python 环境中执行，当前位置不限。安装 CodeChecker 本身不表示上述每种分析器也已安装，实际使用哪个分析器，就应先准备它并使其命令可见。

在 Zephyr 源码根的 Bash 中，通过 `west build` 指定 CMake 参数 `-DZEPHYR_SCA_VARIANT=codechecker`：

```sh
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=codechecker
```

原例选择 `mimxrt1064_evk` 的 Blinky 应用，要求对应工具链与模块依赖已准备。构建或分析失败时，按错误消息分别核对编译环境和分析器安装；本次没有执行该命令。

## 7.2\_配置各命令阶段

CodeChecker 将工作分为分析、解析结果和存储等命令阶段。下表参数可以从 CMake 命令行传入，也可设置为环境变量。

配置文件支持 **JSON（JavaScript Object Notation，数据交换格式）**和 **YAML（YAML Ain't Markup Language，配置数据格式）**；结果清理涉及的 `plist` 是**属性列表（Property List）**文件。

| 参数 | 作用 |
| --- | --- |
| `CODECHECKER_ANALYZE_JOBS` | 分析使用的线程数，默认主机处理器数。 |
| `CODECHECKER_ANALYZE_OPTS` | 直接传给 `analyze` 命令的参数，例如 `--timeout;360`。 |
| `CODECHECKER_CLEANUP` | 在解析或存储后清理，删除所有 plist 文件。 |
| `CODECHECKER_CONFIG_FILE` | 传给所有命令的 JSON 或 YAML 配置文件。 |
| `CODECHECKER_EXPORT` | 用逗号分隔的报告类型列表，允许 `html,json,codeclimate,gerrit,baseline`。后三者是对应报告消费者或基线格式的标识，保持原值。 |
| `CODECHECKER_NAME` | 本次运行的元数据名称，默认 `zephyr`。 |
| `CODECHECKER_PARSE_EXIT_STATUS` | 默认情况下发现问题不会导致构建失败；启用此项可让分析中发现的问题使构建失败。 |
| `CODECHECKER_PARSE_OPTS` | 直接传给 `parse` 命令的参数，例如 `--verbose;debug`。 |
| `CODECHECKER_PARSE_SKIP` | 跳过分析结果解析，适用于只想存储结果的情况。 |
| `CODECHECKER_STORE` | 分析后执行 `store` 命令。 |
| `CODECHECKER_STORE_OPTS` | 直接传给 `store` 的参数，并隐含启用 `CODECHECKER_STORE`；例如 `--url;localhost:8001/Default`。 |
| `CODECHECKER_STORE_TAG` | 通过 `--tag` 向 `store` 提供标识。 |
| `CODECHECKER_TRIM_PATH_PREFIX` | 从分析结果中裁剪指定的路径前缀；默认添加 `west topdir` 返回的工作区根。 |

> 译注：最后一项原例使用固定用户主目录路径，此处以“工作区根”说明同一用途，避免把作者目录写成配置要求。裁剪报告路径不移动源码文件。默认不使构建失败，也不意味着没有发现问题，应实际查看报告。

## 7.3\_Twister中的默认值

由 **Twister测试运行器（Twister Test Runner）**运行 CodeChecker 时，下列值会有专门默认设置：

| 参数 | Twister默认值 |
| --- | --- |
| `CODECHECKER_ANALYZE_JOBS` | `1`。 |
| `CODECHECKER_NAME` | `<board target>:<testsuite name>`，即板目标与测试套件名。 |
| `CODECHECKER_STORE_TAG` | 应用源码目录中 `git describe` 的输出。 |

通过环境变量或附加参数可覆盖这些值。Twister 的组织与运行方式见[运行器译文大纲](../twister/大纲.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：设备树诊断](P006_设备树诊断.md) · [本模块主线目录](../reading/sca.md) · [全部主线](../reading/README.md) · [下一篇：Coverity分析](P008_Coverity分析.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：设备树诊断](P006_设备树诊断.md) · [返回大纲](大纲.md) · [下一章：Coverity分析](P008_Coverity分析.md)

</details>

<!-- reading-navigation:end -->
