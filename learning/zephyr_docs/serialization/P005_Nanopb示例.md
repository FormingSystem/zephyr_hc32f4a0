---
id: learning.zephyr-docs.serialization.page-5
title: Nanopb示例
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/samples/modules/nanopb/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Nanopb示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/modules/nanopb/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 5.1\_概述（Overview）

这是一个使用 Nanopb 的简单协议缓冲区示例，将结构化数据序列化为与平台无关的原始缓冲区或数据流（Raw Buffer / Stream）。[查看官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/modules/nanopb)。

要编码／解码的结构化数据如下：

```protobuf
syntax = "proto3";

message SimpleMessage {
    int32 lucky_number = 1;
    bytes buffer = 2;
    int32 unlucky_number = 3;
}
```

## 5.2\_配置（Configuration）

本示例使用两个配置选项改变行为：

- `CONFIG_SAMPLE_BUFFER_SIZE` 设置 `buffer` 字段的大小。
- `CONFIG_SAMPLE_UNLUCKY_NUMBER` 启用或禁用 `unlucky_number` 字段。

## 5.3\_构建与运行（Building and Running）

按下面方式构建此应用：

```bash
west build -b qemu_x86 samples/modules/nanopb
west build -t run
```

> 译注：命令以已准备 Zephyr 工作区、主机工具链、west、Nanopb 模块及[protoc依赖](P004_Nanopb协议缓冲区.md)为前提，在实际 Zephyr 源码根执行。原目标为 QEMU x86，构建成功后才运行第二行；原页未给出预期输出，本文不补造运行结果，也未执行模拟器或实板验证。本仓库的[示例目录](../../../samples/modules/nanopb)只作源码对照。


<a id="nanopb"></a>
<a id="overview"></a>
<a id="configuration"></a>
<a id="building-and-running"></a>

[上一章](P004_Nanopb协议缓冲区.md) · [返回大纲](大纲.md) · [下一章](P006_JSON接口参考.md)
