---
id: learning.zephyr-docs.api-platform-topic-reference.page-63
title: 框架（Framework）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__framework.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_框架（Framework）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__framework.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象模型、协商过程和运行时。

<a id="details"></a>

对象模型（Object Model）、协商（Negotiation）和运行时（Runtime）。应用程序声明所需元素，将元素链接成处理图（Graph），再通过状态机（State Machine）驱动该图。框架负责在相邻元素间协商数据格式、确定缓冲区配置，并将缓冲区从一个元素传递到下一个元素。对象（Objects）是所有类型都嵌入的基础；元素（Elements）组成处理图；端口（Pad）连接两个元素；能力结构（Capability Structure）描述跨链接传递的内容，分派（Dispatches）承载协商过程；流水线（Pipelines）运行最终结果。

**无动态分配（No Dynamic Allocation）**

框架不分配内存。元素和流水线是应用程序拥有的对象；缓冲区来自启动流水线时确定大小的池（Pools）；协商路径上的每个类型都具有固定大小（Fixed-Size），并按值保存（Held by Value）。因此，即便媒体流运行数小时，也不会使框架从未访问过的堆（Heap）产生碎片。需要临时工作内存（Scratch Memory）的元素在初始化时从应用程序取得该内存，方式与取得池和栈（Stacks）相同。协商在执行状态变更的线程上运行，该线程需要足够大的栈。

**指针参数（Pointer Parameters）**

除非参数自身的文档说明 `NULL` 的含义，例如“传入 `NULL` 可重置为 `ANY`”或“不使用时传入 `NULL`”，否则指针参数不得为 `NULL`。在其他位置传入 `NULL` 属于编程错误（Programming Error），不是运行时条件：调用者应交出自己拥有的对象，因此没有可恢复的状态，也没有有用的错误可报告。此类错误由断言（Assertion）捕获；关闭 `CONFIG_ASSERT` 后，断言不产生开销。

值参数（Values）有所不同。当参数承载数据而非对象时，例如可能为空的能力（Capability），或应用程序选择其值的属性（Property），API 会验证该值并返回负的错误号（Negative `errno`），因为流水线能够报告这种错误并继续运行。

<a id="header-groups"></a>
<a id="groups"></a>

## 63.1\_主题（Topics）

<a id="r_mpipe_5Fbin"></a>

相关声明：[容器（Bins）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html)。

包含其他元素的元素。

<a id="r_mpipe_5Fbuffer"></a>

相关声明：[缓冲区（Buffers）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html)。

用于承载数据的对象，以及这些对象的提供者。

<a id="r_mpipe_5Fstructure"></a>

相关声明：[能力结构（Capability Structure）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html)。

描述一种媒体能力的固定大小容器。

<a id="r_mpipe_5Fdispatch"></a>

相关声明：[分派（Dispatches）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html)。

元素（Elements）之间交换的查询和事件。

<a id="r_mpipe_5Felement"></a>

相关声明：[元素（Elements）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html)。

构成管线的单元。

<a id="r_mpipe_5Fmessage"></a>

相关声明：[消息（Messages）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html)。

元素向应用程序反馈的内容。

<a id="r_mpipe_5Fobject"></a>

相关声明：[对象（Objects）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html)。

为每一种类型提供身份和属性的公共基类。

<a id="r_mpipe_5Fpad"></a>

相关声明：[连接端口（Pad）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html)。

两个元素相连接的位置。

<a id="r_mpipe_5Fparser"></a>

相关声明：[解析器（Parsers）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html)。

将无固定结构的字节流切分为帧的元素。

<a id="r_mpipe_5Fpipeline"></a>

相关声明：[管线（Pipelines）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html)。

顶层容器，以及实际运行处理图的对象。

<a id="r_mpipe_5Fsink"></a>

相关声明：[接收端（Sinks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html)。

消耗缓冲区并终结数据流的元素。

<a id="r_mpipe_5Fsrc"></a>

相关声明：[源（Sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html)。

产生缓冲区并驱动协商过程的元素。

<a id="r_mpipe_5Fthread"></a>

相关声明：[线程（Threads）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html)。

一种 `k_thread`，其栈来自池，且栈的生命周期长于该线程。

<a id="r_mpipe_5Ftransform"></a>

相关声明：[变换元素（Transforms）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html)。

同时具有输入与输出、处于协商过程中间环节的元素。

<a id="r_mpipe_5Fvalue"></a>

相关声明：[值容器（Value Container）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html)。

一个带类型的标量或范围，是能力描述中的最小组成部分。

<a id="r_mpipe_5Fworkqueue"></a>

相关声明：[工作队列（Workqueues）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__workqueue.html)。

可选择将元素的工作卸载到共享工作线程上。


## 63.2\_原页交叉引用（Cross References）

- [容器（Bins）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html)
- [缓冲区（Buffers）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html)
- [能力结构（Capability Structure）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html)
- [分派（Dispatches）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html)
- [元素（Elements）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html)
- [消息（Messages）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html)
- [对象（Objects）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html)
- [连接端口（Pad）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html)
- [解析器（Parsers）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html)
- [管线（Pipelines）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html)
- [接收端（Sinks）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html)
- [源（Sources）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html)
- [线程（Threads）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [变换元素（Transforms）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html)
- [值容器（Value Container）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html)
- [工作队列（Workqueues）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__workqueue.html)
- [CONFIG_ASSERT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT)

<a id="header-details"></a>
<a id="mpipe_no_alloc"></a>
<a id="mpipe_null"></a>

---

[上一章](P062_基础元素（Base Elements）.md) · [返回大纲](大纲.md) · [下一章](P064_插件（Plugins）.md)
