---
id: learning.zephyr-docs.api-platform-topic-reference.page-131
title: Xen 支持
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__support.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第131章\_Xen 支持

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__support.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen 虚拟机监控器（Hypervisor）支持。

<a id="details"></a>

Xen 虚拟机监控器支持（Xen Hypervisor Support）。用于将 Zephyr 作为 Xen 客户机（Guest）或 Xen Dom0 运行的接口（Interfaces）。

<a id="header-groups"></a>
<a id="groups"></a>

## 131.1\_主题（Topics）

<a id="r_xen_5Fdom0"></a>

相关声明：[Xen Dom0 控制](../api_topic_reference/P105_Xen Dom0 控制.md)。

从特权域管理 Xen 域（Domain）和主机资源。

<a id="r_xen_5Fhvm"></a>

相关声明：[Xen硬件虚拟机（HVM）的操作。](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html)。

通过 HVM 超级调用（Hypercall）配置 Xen 硬件虚拟机（HVM）客户机参数。

<a id="r_xen_5Fxsm_5Fflask"></a>

相关声明：[Xen 安全模块 FLASK（Xen XSM FLASK）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html)。

加载 Xen 安全策略，管理 FLASK 强制执行模式，将上下文转换为安全标识符（SID），管理对象上下文（ocontexts），以及执行其他 FLASK 相关任务。

<a id="r_xen_5Fdevice_5Fmodel"></a>

相关声明：[Xen 设备模型（Device model）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html)。

管理 Xen I/O 请求服务器及相关的设备模型状态。

<a id="r_xen_5Fevent_5Fchannels"></a>

相关声明：[Xen 事件通道（Event channels）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html)。

从 Zephyr 分配、绑定和处理 Xen 事件通道。

<a id="r_xen_5Fregions"></a>

相关声明：[Xen 扩展区域（Extended regions）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html)。

从 Xen 扩展内存区域分配、释放和映射缓冲区。

<a id="r_xen_5Fgrant_5Ftables"></a>

相关声明：[Xen 授权表（Grant tables）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html)。

与其他域共享内存，并映射其他域的内存授权（Foreign grants）。

<a id="r_xen_5Finternal"></a>

相关声明：[Xen 内部支持（Internal support）](../api_topic_reference/P106_Xen 内部支持（Internal support）.md)。

共享 Zephyr Xen 支持代码所用的底层辅助工具。

<a id="r_xen_5Fmemory_5Fmanagement"></a>

相关声明：[Xen 内存管理（Memory management）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html)。

管理域的物理映射（Physmaps）和由 Xen 拥有的资源。

<a id="r_xen_5Fversion_5Fqueries"></a>

相关声明：[Xen版本查询（Version Queries）。](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html)。

查询向当前域公开的 Xen 虚拟机监控器版本。


## 131.2\_原页交叉引用（Cross References）

- [Xen Dom0 控制](../api_topic_reference/P105_Xen Dom0 控制.md)
- [Xen硬件虚拟机（HVM）的操作。](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html)
- [Xen 安全模块 FLASK（Xen XSM FLASK）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html)
- [Xen 设备模型（Device model）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html)
- [Xen 事件通道（Event channels）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html)
- [Xen 扩展区域（Extended regions）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html)
- [Xen 授权表（Grant tables）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html)
- [Xen 内部支持（Internal support）](../api_topic_reference/P106_Xen 内部支持（Internal support）.md)
- [Xen 内存管理（Memory management）](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__memory__management.html)
- [Xen版本查询（Version Queries）。](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html)

<a id="header-details"></a>

---

[上一章](P130_Xen 控制台驱动（Console driver）.md) · [返回大纲](大纲.md)
