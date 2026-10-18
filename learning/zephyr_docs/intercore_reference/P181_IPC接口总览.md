---
id: learning.zephyr-docs.intercore_reference.ipchostref-181
title: IPC接口总览
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ipc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第181章\_IPC接口总览

原文：[group__ipc](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc.html)。读取日期：2026-10-13，`latest`。

本页是处理器间通信（Inter-Processor Communication，IPC）的应用程序编程接口（Application Programming Interface，API）主题总览。原页面只提供下列八个子主题；这不是某一家芯片的专用接口页。

RPMsg 指远程消息传递（Remote Processor Messaging）。各主题对应的中文译文均已在本参考册中，可直接通过相对链接打开。

## 181.1\_八个接口主题

| 主题 | 原页说明 |
| --- | --- |
| [IPC 服务接口](P111_IPC服务公共接口.md) | 处理器间通信服务的公共接口 |
| [IPC 服务 RPMsg 接口](P124_IPC的RPMsg公共层接口.md) | IPC 服务的 RPMsg 公共层接口 |
| [IPC 服务后端](P115_IPC服务后端接口.md) | 服务后端（Backend）接口 |
| [IPC 服务静态虚拟环接口](P129_IPC静态虚拟环接口.md) | 静态虚拟环（Static VRINGs）的接口 |
| [ICMsg IPC 库接口](P135_ICMsg基础接口.md) | 核间消息传递（Inter-core Messaging，ICMsg）库接口 |
| [ICMsg 多端点 IPC 库接口](P140_ICMsg多端点接口.md) | ICMsg 的多端点扩展（Multi-endpoint Extension） |
| [数据包缓冲区接口](P144_核间数据包缓冲区接口.md) | 数据包缓冲区（Packet Buffer）接口；原页名称为 Packed Buffer API |
| [RPMsg 服务接口](P121_RPMsg服务公共接口.md) | RPMsg 服务的公共接口 |

---

[上一章：RPMsg命令行后端完整头文件](P180_RPMsg命令行后端完整头文件.md) · [下一章：IntelADSP主机IPC头文件参考](P182_IntelADSP主机IPC头文件参考.md) · [返回大纲](大纲.md)
