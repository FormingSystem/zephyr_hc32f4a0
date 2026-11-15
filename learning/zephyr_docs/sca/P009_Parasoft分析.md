---
id: learning.zephyr-docs.sca.sca-cpptest
title: Parasoft分析
kind: reference
status: maintained
domains: [zephyr, sca]
source_url: https://docs.zephyrproject.org/latest/develop/sca/cpptest.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第9章\_Parasoft分析

原文：[Parasoft C/C++test support](https://docs.zephyrproject.org/latest/develop/sca/cpptest.html)。读取日期：2026-10-12，`latest`。

[Parasoft C/C++test](https://www.parasoft.com/products/parasoft-c-ctest/) 是 C/C++ 软件测试与静态分析工具，属于商业软件，使用时须取得商业许可证。完整用法见 [Parasoft产品文档](https://docs.parasoft.com/)。

## 9.1\_生成构建数据文件

使用前确保 `cpptestscan` 可通过 `PATH` 命令搜索路径找到。调用 `west build` 时传入 CMake 参数 `-DZEPHYR_SCA_VARIANT=cpptest`：

```sh
west build -b qemu_cortex_m3 zephyr/samples/hello_world -- -DZEPHYR_SCA_VARIANT=cpptest
```

> 译注：原例在包含 `zephyr/` 子目录的工作区根用 Bash 执行，需要对应工具链、依赖和可用的 C/C++test。若在 Zephyr 源码根执行，应用路径改为 `samples/hello_world`。`qemu_cortex_m3` 是原例构建目标，不是本项目芯片目标。

该流程生成 **构建数据文件（Build Data File，BDF）**：`build/sca/cpptest/cpptestscan.bdf`。

## 9.2\_导入并生成报告

详细选项仍以 C/C++test 文档为准。原文给出的导入、报告命令示例如下：

```sh
cpptestcli -data out -localsettings local.conf -bdf build/sca/cpptest/cpptestscan.bdf -config "builtin://Recommended Rules" -report out/report
```

> 译注：在上一节命令的工作目录执行，前提是 BDF 已生成，且 `local.conf` 是按工具文档自行准备的设置文件。`out` 是命令指定的工作数据目录，`out/report` 是报告位置；`builtin://Recommended Rules` 是内置规则集标识，保持原样，不是本机文件路径。

可能还需把 `bdf.import.c.compiler.exec`、`bdf.import.cpp.compiler.exec` 和 `bdf.import.linker.exec` 设置为 west 构建实际使用的 C 编译器、C++ 编译器与链接器。

本次只提供译文，没有生成 BDF 或报告。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Coverity分析](P008_Coverity分析.md) · [本模块主线目录](../reading/sca.md) · [全部主线](../reading/README.md) · [下一篇：ECLAIR分析](P010_ECLAIR分析.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Coverity分析](P008_Coverity分析.md) · [返回大纲](大纲.md) · [下一章：ECLAIR分析](P010_ECLAIR分析.md)

</details>

<!-- reading-navigation:end -->
