---
id: learning.zephyr-docs.api-navigation-reference.page-1
title: C_API参考入口
kind: reference
status: maintained
domains: [zephyr, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/index.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_C_API参考入口

原文：[Zephyr 官方 API 页面](https://docs.zephyrproject.org/latest/doxygen/html/index.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="md__2____w_2zephyr_2zephyr_2doc_2__doxygen_2mainpage"></a>
<a id="autotoc_md1"></a>
<a id="autotoc_md2"></a>
<a id="autotoc_md3"></a>

这是 Zephyr 实时操作系统（RTOS）的 C API 参考文档，包含 Zephyr 应用程序和子系统可用的全部函数、宏与数据结构，直接从源代码生成。

## 1.1\_按主题浏览 API（Browse the API by topic）

API 按主题（Topics）组织为层次结构，覆盖操作系统的主要领域。可以从以下主要分类开始，也可以浏览完整主题列表。

| 主题（Topic） | 内容（Description） |
| --- | --- |
| [内核（Kernel）](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__apis.html) | 线程、调度、同步、定时器，以及其他 RTOS 核心原语（Primitives）。 |
| [设备驱动（Device Drivers）](https://docs.zephyrproject.org/latest/doxygen/html/group__io__interfaces.html) | 面向外设且独立于具体硬件的接口，包括 GPIO、I2C、SPI、传感器等。 |
| [操作系统服务（Operating System Services）](https://docs.zephyrproject.org/latest/doxygen/html/group__os__services.html) | 网络、蓝牙、存储、日志，以及其他构建在内核之上的服务。 |
| [设备树（Devicetree）](../dt_overview_reference/P001_设备树API总览.md) | 在构建时读取系统硬件描述的宏。 |
| [设备模型（Device Model）。](../device_reference/P001_设备模型公共接口.md) | 将驱动与其管理的硬件实例关联起来的抽象。 |
| [内存管理（Memory Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mem__mgmt.html) | 堆（Heap）、内存片（Memory slab）和内存映射接口。 |
| [实用工具（Utilities）](https://docs.zephyrproject.org/latest/doxygen/html/group__utilities.html) | 通用辅助功能，包括数据结构 API。 |
| [测试（Testing）](../hardware/P499_测试API目录.md) | Ztest 框架及相关测试辅助功能。 |

## 1.2\_其他浏览方式（Other ways to explore）

- 数据结构（Data Structures）：全部已编写文档的结构体（struct）与联合体（union）的索引。
- 文件（Files）：逐个头文件浏览 API。
- 弃用清单（Deprecated List）：计划移除的 API 及其替代方式。
- 使用搜索框按名称查找任何已编写文档的符号。

## 1.3\_查找其他资料（Looking for something else?）

本网站仅涵盖 C API。有关指南、示例、支持的开发板及其他内容，请访问 Zephyr 项目主文档。

## 1.4\_原页交叉引用（Cross References）

- [Zephyr RTOS](https://zephyrproject.org)
- [主题（Topics）](https://docs.zephyrproject.org/latest/doxygen/html/topics.html)
- [完整主题列表](https://docs.zephyrproject.org/latest/doxygen/html/topics.html)
- [内核（Kernel）](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__apis.html)
- [设备驱动（Device Drivers）](https://docs.zephyrproject.org/latest/doxygen/html/group__io__interfaces.html)
- [操作系统服务（Operating System Services）](https://docs.zephyrproject.org/latest/doxygen/html/group__os__services.html)
- [设备树（Devicetree）](../dt_overview_reference/P001_设备树API总览.md)
- [设备模型（Device Model）。](../device_reference/P001_设备模型公共接口.md)
- [内存管理（Memory Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__mem__mgmt.html)
- [实用工具（Utilities）](https://docs.zephyrproject.org/latest/doxygen/html/group__utilities.html)
- [测试（Testing）](../hardware/P499_测试API目录.md)
- [数据结构（Data Structures）](../api_directory_indices/P001_数据结构总表.md)
- [文件（Files）](../api_directory_indices/P291_文件总表.md)
- [弃用清单（Deprecated List）](P003_弃用接口清单.md)
- [Zephyr 项目文档](https://docs.zephyrproject.org/latest/)

---

[返回大纲](大纲.md) · [下一章](P002_相关文档索引.md)
