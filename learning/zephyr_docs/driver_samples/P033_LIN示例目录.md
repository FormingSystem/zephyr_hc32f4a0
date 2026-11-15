---
id: learning.zephyr-docs.driver_samples.page-33
title: LIN示例目录
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/lin/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="local-interconnect-network-lin"></a>

# 第33章\_LIN示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/lin/index.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 33.1\_示例范围

这些示例演示如何使用[局部互联网络（Local Interconnect Network，LIN）](../hardware/P072_本地互连网络.md#lin)驱动API。

| 示例 | 功能 |
| --- | --- |
| [通过LIN使用NCV7430 LED控制器](P034_LIN灯光控制器示例.md#lin-ncv7430) | 使用Zephyr LIN API控制NCV7430 LED控制器 |
| [NCV7430模拟LIN响应节点](P035_LIN模拟响应节点示例.md#lin-ncv7430-responder) | 将NCV7430 LED控制器的总线行为模拟为一个LIN响应节点 |

> 译注——两端角色：前者是命令节点（Commander），后者是响应节点（Responder）的模拟实现。这里的“模拟”仍通过真实LIN总线通信，具体接线与运行方式见各自译文。


对应官方文档源码：[samples/drivers/lin/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lin/index.rst)。

> 译注——源码版本：本仓库参照版本尚无该文档，请按上方官方来源跟踪相应版本；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P032_指纹传感器示例.md) · [返回大纲](大纲.md) · [下一章](P034_LIN灯光控制器示例.md)
