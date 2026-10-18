---
id: learning.zephyr-docs.api-platform-topic-reference.page-62
title: 基础元素（Base Elements）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__base.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_基础元素（Base Elements）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__base.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与媒体类型无关的元素，用于塑造处理图的结构，而非处理其中的数据。

<a id="details"></a>

与媒体类型无关（Media-Agnostic）的元素，用于组织处理图（Graph）的结构，而非改变数据。基础插件（Base Plugin）包含不属于任何媒体领域（Media Domain）的元素。它们不检查缓冲区内容，而是约束链接（Link）可以承载的内容、将图拆分为分支或分配到不同线程，或者让应用程序成为图的一端。所有媒体领域都需要这些元素，因此将它们集中放置，避免各领域重复实现。

- `caps_filter` 约束其所在链接的能力（Capability）。
- `tee` 将每个缓冲区推送到图的每个分支（Branch）。
- `queue` 将其下游元素分离到独立线程（Thread）中。
- `app_src` 作为源（Source），注入应用程序推送的数据。
- `app_sink` 作为汇（Sink），将到达的数据交给应用程序。

<a id="header-groups"></a>
<a id="groups"></a>

## 62.1\_主题（Topics）

<a id="r_mpipe_5Fapp_5Fsink"></a>

相关声明：[应用接收端（Application sinks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html)。

将管线缓冲区交给应用程序的元素。

<a id="r_mpipe_5Fapp_5Fsrc"></a>

相关声明：[应用源（Application sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html)。

将应用数据注入管线的元素。

<a id="r_mpipe_5Fcaps_5Ffilter"></a>

相关声明：[能力过滤器（Caps Filters）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html)。

对协商得到的能力施加约束的变换元素。

<a id="r_mpipe_5Fqueue"></a>

相关声明：[队列（Queues）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html)。

管线层面的线程化元素。

<a id="r_mpipe_5Ftee"></a>

相关声明：[分流器（Tee）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html)。

管线分支元素：具有一个接收端口（Sink pad）和 N 个源端口（Source pad）。

<a id="header-files"></a>
<a id="files"></a>

## 62.2\_文件（Files）

<a id="r_mpipe_5Fbase_2Eh"></a>

```c
file mpipe_base.h
```

相关声明：[mpipe_base.h](../api_file_reference/P230_zephyr__mpipe__base__mpipe_base.h_文件参考.md)。

基础插件（Base Plugin）。


## 62.3\_原页交叉引用（Cross References）

- [应用接收端（Application sinks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html)
- [应用源（Application sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html)
- [能力过滤器（Caps Filters）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__caps__filter.html)
- [队列（Queues）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html)
- [分流器（Tee）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html)
- [mpipe_base.h](../api_file_reference/P230_zephyr__mpipe__base__mpipe_base.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P061_多媒体管线（Multimedia Pipeline）.md) · [返回大纲](大纲.md) · [下一章](P063_框架（Framework）.md)
