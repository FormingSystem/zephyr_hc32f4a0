---
id: learning.zephyr-docs.serialization.page-4
title: Nanopb协议缓冲区
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/services/serialization/nanopb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Nanopb协议缓冲区

原文：[官方页面](https://docs.zephyrproject.org/latest/services/serialization/nanopb.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 4.1\_概述

[Nanopb](https://jpa.kapsi.fi/nanopb/) 是 Google [Protocol Buffers](https://protobuf.dev/) 的 C 语言实现。

> 译注：Protocol Buffers 通常简称 Protobuf，中文可称“协议缓冲区”，是一种描述结构化消息并生成编码／解码代码的序列化机制。Nanopb 是实现名称，不另造英文全称。

## 4.2\_依赖要求（Requirements）

Nanopb 使用协议缓冲区编译器（Protocol Buffer Compiler）生成源文件和头文件。请确保已安装 `protoc`，且环境中可以找到这个可执行程序。

### Ubuntu

使用 `apt` 安装依赖：

```bash
sudo apt install protobuf-compiler
```

### macOS

使用 `brew` 安装依赖：

```bash
brew install protobuf
```

### Windows

使用 `choco` 安装依赖：

```powershell
choco install protoc
```

> 译注：以上是三个系统的备选安装分支，按实际主机选择；Windows 分支要求已有 Chocolatey。它们安装主机上的消息编译器，不是在目标板上执行。本轮仅翻译，未执行安装。

## 4.3\_配置（Configuration）

确保在 `CMakeLists.txt` 中按下面方式包含 Nanopb：

```cmake
list(APPEND CMAKE_MODULE_PATH ${ZEPHYR_BASE}/modules/nanopb)
include(nanopb)
```

可通过 CMake 函数 `zephyr_nanopb_sources()` 添加 proto 文件。它确保在构建指定目标前生成所需的头文件和源文件。

Nanopb 提供[生成器选项](https://jpa.kapsi.fi/nanopb/docs/reference.html#generator-options)（Generator Options），可用于配置消息或字段，例如设定固定大小或完全跳过某个字段。

内部 CMake 生成器还有一项扩展：使用 CMake 变量自动配置 `*.options.in` 文件。

用法示例见官方 [`samples/modules/nanopb/src/simple.options.in`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/nanopb/src/simple.options.in) 和 [`samples/modules/nanopb/CMakeLists.txt`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/nanopb/CMakeLists.txt)。

> 译注：本仓库的[选项模板](../../../samples/modules/nanopb/src/simple.options.in)和[CMake文件](../../../samples/modules/nanopb/CMakeLists.txt)可作相对路径的源码跟踪入口，版本以当前仓库为准。继续阅读[Nanopb示例](P005_Nanopb示例.md)。


<a id="nanopb"></a>
<a id="nanopb-reference"></a>
<a id="requirements"></a>
<a id="tab-0-VWJ1bnR1"></a>
<a id="tab-0-bWFjT1M="></a>
<a id="tab-0-V2luZG93cw=="></a>
<a id="panel-0-VWJ1bnR1"></a>
<a id="panel-0-bWFjT1M="></a>
<a id="panel-0-V2luZG93cw=="></a>
<a id="configuration"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CBOR序列化](P003_CBOR序列化.md) · [本模块主线目录](../reading/serialization.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P003_CBOR序列化.md) · [返回大纲](大纲.md) · [下一章](P005_Nanopb示例.md)

</details>

<!-- reading-navigation:end -->
