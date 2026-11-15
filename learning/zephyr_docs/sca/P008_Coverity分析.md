---
id: learning.zephyr-docs.sca.sca-coverity
title: Coverity分析
kind: reference
status: maintained
domains: [zephyr, sca]
source_url: https://docs.zephyrproject.org/latest/develop/sca/coverity.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第8章\_Coverity分析

原文：[Coverity](https://docs.zephyrproject.org/latest/develop/sca/coverity.html)。读取日期：2026-10-12，`latest`。

**Coverity Scan** 是 Black Duck 提供的服务，向在该服务注册产品的开源开发者提供项目分析结果。Zephyr 的这项接入只在 [scan.coverity.com](https://scan.coverity.com) 服务及其提供的工具发行包上测试过。

## 8.1\_生成构建数据

先安装 Coverity 工具发行包，并使其程序能由 `PATH` 命令搜索路径找到。随后在 `west build` 中指定 CMake 参数 `-DZEPHYR_SCA_VARIANT=coverity`：

```sh
west build -b qemu_cortex_m3 samples/hello_world -- -DZEPHYR_SCA_VARIANT=coverity
```

> 译注：在具备工具链与模块依赖的 Zephyr 源码根，用 Bash 执行。原例构建 `qemu_cortex_m3` 的 Hello World，不会由这条命令启动目标固件。若找不到 Coverity 工具，应先修复安装和搜索路径，不能把普通构建成功视作已经生成扫描数据。

默认结果位于 `build/sca/coverity`。也可设置 `COVERITY_OUTPUT_DIR`，为多次及增量扫描选择共同的结果目录。

## 8.2\_分析结果

按 [Coverity Scan官网](https://scan.coverity.com)的说明上传结果并进行后续分析。

> 译注：这里翻译的是官方服务工作流；本次没有安装工具、执行扫描或上传任何工程数据。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CodeChecker分析](P007_CodeChecker分析.md) · [本模块主线目录](../reading/sca.md) · [全部主线](../reading/README.md) · [下一篇：Parasoft分析](P009_Parasoft分析.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：CodeChecker分析](P007_CodeChecker分析.md) · [返回大纲](大纲.md) · [下一章：Parasoft分析](P009_Parasoft分析.md)

</details>

<!-- reading-navigation:end -->
