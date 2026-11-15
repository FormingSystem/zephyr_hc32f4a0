---
id: learning.zephyr-official-intro.macos
title: macOS 补充配置
kind: reference
status: maintained
domains: [zephyr, documentation]
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 本文件为中文翻译；章节编号、导航和明确标出的译注为本地新增。 -->

# 第8章\_macOS补充配置

原文：[macOS alternative setup instructions](https://docs.zephyrproject.org/latest/develop/getting_started/installation_mac.html)。译文基线：2026-10-12 的 `latest` 页面。主安装步骤在[入门指南](P002_入门指南.md)，本页补充可执行文件限制与另一种包管理器的注意事项。

## 8.1\_关于Gatekeeper的重要说明

从 macOS 10.15 Catalina 开始，由系统终端或其他终端模拟器启动的应用，也受与 Dock 启动应用相同的系统安全策略约束。这意味着，通过浏览器下载可执行程序后，macOS 默认可能不允许你直接在终端运行它们。

原文提供两种处理方式：

**方式一：移除目标目录的隔离属性。** 在 macOS 终端中执行：

```bash
xattr -r -d com.apple.quarantine ./path/to/folder
```

将 `./path/to/folder` 替换为相对于当前终端目录、包含需要运行的可执行程序的目录。

**方式二：给选定终端配置开发工具权限。** 打开“系统偏好设置 → 安全性与隐私 → 隐私”，向下找到“开发者工具”，解锁后勾选所使用的终端模拟器。这一设置会作用于由该终端启动的所有可执行程序。

上述说明不适用于通过 Homebrew 安装的可执行程序，因为 `brew` 会自动解除隔离；但对于多数[工具链](https://docs.zephyrproject.org/latest/develop/toolchains/index.html)来说，这些说明是相关的。

> 译注：这里将原文目录占位符改成相对路径形式，必须换成已确认来源的目标工具目录；`-r` 会递归处理目录内容。系统界面的译名和位置可能随 macOS 版本变化，本页保留来源的菜单描述，不表示在当前机器上执行过这些操作。

## 8.2\_MacPorts用户补充说明

本指南没有正式支持 MacPorts，但可以用它代替 Homebrew，获取 macOS 上所需的全部依赖。为正确安装 Python 依赖，你还可能需要安装 `rust` 和 `cargo`。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Linux 主机依赖](P007_Linux主机依赖.md) · [本模块主线目录](../reading/getting_started.md) · [全部主线](../reading/README.md) · [下一篇：Windows 补充配置](P009_Windows补充配置.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Linux主机依赖](P007_Linux主机依赖.md) · [返回大纲](大纲.md) · [下一章：Windows补充配置](P009_Windows补充配置.md)

</details>

<!-- reading-navigation:end -->
