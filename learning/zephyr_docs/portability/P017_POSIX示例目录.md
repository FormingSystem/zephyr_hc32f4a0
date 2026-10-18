---
id: learning.zephyr-docs.portability.page-17
title: POSIX示例目录
kind: reference
status: maintained
domains: [zephyr, portability, posix]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/posix.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_POSIX示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/posix.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 17.1\_示例范围

这些示例展示如何在 Zephyr 中使用[可移植操作系统接口（Portable Operating System Interface，POSIX）API](P010_POSIX文档入口.md#posix-support)。

| 官方示例 | 用途 |
| --- | --- |
| [环境变量（Environment Variables）](P018_POSIX环境变量示例.md#posix-env) | 从 Zephyr 应用中操作环境变量。 |
| [eventfd()](P019_eventfd事件通知示例.md#posix-eventfd) | 创建用于事件通知（Event Notification）的文件描述符（File Descriptor）。 |
| [带时钟初始化的 gettimeofday()](P020_系统时间与SNTP示例.md#posix-gettimeofday) | 通过简单网络时间协议（Simple Network Time Protocol，SNTP）初始化时钟，然后调用 gettimeofday()。 |
| [POSIX 哲学家就餐](P021_POSIX哲学家就餐示例.md#posix-philosophers) | 使用 POSIX API 实现哲学家就餐问题（Dining Philosophers Problem）的解决方案。 |
| [uname()](P022_uname系统信息示例.md#posix-uname) | 获取系统信息并输出到控制台。 |

> 译注：本页是官方示例目录；各示例的依赖、构建命令和输出见对应译文。目录收录某个接口，并不意味着所有宿主系统或每一种 POSIX 配置都支持它。


<a id="posix-api"></a>

[上一章](P016_POSIX附加配置选项.md) · [返回大纲](大纲.md) · [下一章](P018_POSIX环境变量示例.md)
