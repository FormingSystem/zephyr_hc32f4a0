---
id: learning.zephyr-docs.external_modules.page-30
title: Zephelin性能分析
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/zephelin.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="zephelin"></a>
<a id="external-module-zephelin"></a>

# 第30章\_Zephelin性能分析

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/zephelin.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 30.1\_简介（Introduction）

<a id="id2"></a>

[Zephyr性能分析库（Zephyr Profiling Library，ZPL）](https://github.com/antmicro/zephelin)简称Zephelin，用于采集、报告运行时性能指标，对Zephyr应用进行性能分析（Profiling）和细节分析，尤其关注人工智能／机器学习（Artificial Intelligence / Machine Learning，AI/ML）推理负载。

<a id="id8"></a>

<a id="id10"></a>

它也简化 [LiteRT](https://ai.google.dev/edge/litert)、[microTVM](https://tvm.apache.org/docs/) 等AI运行时分析，帮助发现瓶颈与优化机会。

功能包括：

- 跟踪Zephyr应用在硬件上的执行过程。
- 经UART、USB或调试适配器等后端取得跟踪数据（Trace）。
- 输出公共跟踪格式（Common Trace Format，CTF）和跟踪事件格式（Trace Event Format，TEF）。
- 提供从设备采集跟踪数据的脚本。
- 收集内存读数，包括栈、堆、内核堆及内存块池（Memory Slab）；传感器读数，例如芯片温度；线程分析的CPU占用；AI运行时读数，例如LiteRT张量内存区（Tensor Arena）使用量。
- 显示LiteRT或microTVM中已执行神经网络层的输入、输出和权重维度、层参数，以及各层消耗的时间和资源。
- 支持编译阶段及运行阶段配置。
- 可选择性能分析层级（Profiling Tier），控制采集哪些子系统及数据量。

<a id="id6"></a>

上述信息都可以用 [Zephelin跟踪查看器](https://antmicro.github.io/zephelin-trace-viewer)分析。

<a id="usage-with-zephyr"></a>

## 30.2\_在Zephyr中使用（Usage With Zephyr）

将以下条目加入Zephyr[模块](../modules/P001_模块与外部项目.md#modules)子清单，例如 `zephyr/submanifests/zephelin.yaml`，运行 `west update`；也可加入原文 `west.yaml` 项目列表：

```yaml
manifest:
  projects:
    - name: zephelin
      url: https://github.com/antmicro/zephelin
      revision: main
      path: modules/zephelin # adjust the path as needed
```

<a id="id4"></a>

更多说明见 [Zephelin文档](https://antmicro.github.io/zephelin/)。

<a id="references"></a>

## 30.3\_参考资料（References）


<a id="id1"></a>

1. [Zephelin仓库](https://github.com/antmicro/zephelin)。

<a id="id3"></a>

2. [文档](https://antmicro.github.io/zephelin/)。

<a id="id5"></a>

3. [跟踪查看器](https://antmicro.github.io/zephelin-trace-viewer)。

<a id="id7"></a>

4. [LiteRT](https://ai.google.dev/edge/litert)。

<a id="id9"></a>

5. [TVM文档](https://tvm.apache.org/docs/)。


对应官方文档源码：[doc/develop/manifest/external/zephelin.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/zephelin.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/zephelin.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：zenoh_pico](P029_zenoh_pico.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：Zephyr科学计算库](P031_Zephyr科学计算库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P029_zenoh_pico.md) · [返回大纲](大纲.md) · [下一章](P031_Zephyr科学计算库.md)

</details>

<!-- reading-navigation:end -->
