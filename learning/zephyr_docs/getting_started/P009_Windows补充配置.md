---
id: learning.zephyr-official-intro.windows
title: Windows 补充配置
kind: reference
status: maintained
domains: [zephyr, documentation]
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 本文件为中文翻译；章节编号、导航和明确标出的译注为本地新增。 -->

# 第9章\_Windows补充配置

原文：[Windows alternative setup instructions](https://docs.zephyrproject.org/latest/develop/getting_started/installation_win.html)。译文基线：2026-10-12 的 `latest` 页面。Windows 原生安装路线在[入门指南](P002_入门指南.md)；本页是官方保留的 WSL 补充说明。

## 9.1\_Windows 10与WSL

如果运行较新的 Windows 10，可以使用系统内置功能，在标准命令提示符中直接运行 Ubuntu 二进制程序。借助适用于 Linux 的 Windows 子系统（Windows Subsystem for Linux，WSL），可使用 Zephyr **软件开发工具包（Software Development Kit，SDK）** 等软件，而不必自行配置虚拟机。

> 原文警告：Windows 10 1803 存在导致 CMake 无法正常工作的缺陷，已在 1809 及后续版本中修复。详情见 [Zephyr Issue 10420](https://github.com/zephyrproject-rtos/zephyr/issues/10420)。

按原文的两步操作：

1. [安装 WSL](https://learn.microsoft.com/en-us/windows/wsl/install)。
2. 按[安装 Linux 主机依赖](P007_Linux主机依赖.md)中的 Ubuntu 分支操作。

> 原文说明：要让 Zephyr SDK 正常工作，需要 Windows 10 build 15002 或更高版本。可以在系统设置的“关于你的电脑”中查看构建版本；如果使用更旧的版本，可能需要安装 Creator’s Update。

> 译注：上述 Windows 构建号和 Creator’s Update 属于原文保留的历史条件，不是本次为最新 SDK 重新确认的支持矩阵。现代 WSL 的安装与版本要求应以 Microsoft 文档和所用 SDK 为准；“不必自行配置虚拟机”也不表示 WSL 2 的底层不使用虚拟化。若要从 WSL 烧录硬件，还应按入门指南处理 **通用串行总线（Universal Serial Bus，USB）** 设备可见性。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：macOS 补充配置](P008_macOS补充配置.md) · [本模块主线目录](../reading/getting_started.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：macOS补充配置](P008_macOS补充配置.md) · [返回大纲](大纲.md) · [返回整套文档入口](../README.md)

</details>

<!-- reading-navigation:end -->
