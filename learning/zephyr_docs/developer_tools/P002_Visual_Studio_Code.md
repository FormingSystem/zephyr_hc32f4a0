---
id: learning.zephyr-docs.developer-tools.vscode
title: Visual Studio Code
kind: reference
status: maintained
domains: [zephyr, tools, development]
source_url: https://docs.zephyrproject.org/latest/develop/tools/vscode.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Visual Studio Code

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/tools/vscode.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

<a id="vscode-ide"></a>

<a id="visual-studio-code"></a>

[Visual Studio Code](https://code.visualstudio.com/)（简称VS Code）是一款流行的跨平台集成开发环境（Integrated Development Environment，IDE），支持C项目，并具有丰富的扩展。

本指南说明如何在VS Code中配置Zephyr的[Blinky示例](../getting_started/P004_LED闪烁示例.md)。这些步骤已在Linux上测试；macOS和Windows的步骤应相同，但需要按实际情况调整路径。

<a id="get-vs-code"></a>

## 2.1\_获取VS Code

[下载VS Code](https://code.visualstudio.com/Download)并安装。通过左侧面板中的扩展市场（Extensions marketplace）安装所需扩展：搜索并安装[C/C++ Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack)。

<a id="initialize-a-new-workspace"></a>

## 2.2\_初始化新工作区

本指南详细介绍Blinky示例应用的配置方法；对于其他Zephyr项目和[工作区布局](../west/P004_工作区.md)，操作也类似。

开始之前，请按[入门指南](../getting_started/P002_入门指南.md)准备好可用的Zephyr开发环境。

<a id="open-the-project-in-vs-code"></a>

### 在VS Code中打开项目（Open the project in VS Code）

1. 从VS Code主菜单选择 **File → Open Folder**（文件→打开文件夹）。
2. 找到并选择Zephyr工作区。如果按入门指南操作，它是主目录（HOME）中的`zephyrproject`文件夹。
3. 如果出现提示，启用工作区信任（Workspace Trust）。

<a id="generate-compile-commands"></a>

### 生成编译命令（Generate compile commands）

为了支持代码导航和代码检查（Linting），必须先编译一次项目，生成`compile_commands.json`，向C/C++扩展提供所需信息，例如包含路径。可以在VS Code集成终端中执行：从顶部菜单或命令面板（`Ctrl+Shift+P`）选择 **Terminal → New Terminal**（终端→新建终端），然后输入：

```shell
$ cd zephyr
$ west build -p always -b native_sim/native/64 samples/basic/blinky
```

<a id="configure-the-c-c-extension"></a>

### 配置C/C++扩展（Configure the C/C++ extension）

现在需要将扩展指向生成的`compile_commands.json`，以启用VS Code的代码检查和代码导航。

1. 在顶部菜单打开 **File → Preferences → Settings**（文件→首选项→设置）。
2. 搜索 **C_Cpp > Default: Compile Commands**，将其值设置为`zephyr/build/compile_commands.json`。

此时代码中的检查错误应当消除，并且应能在代码间导航。

<a id="additional-resources"></a>

## 2.3\_其他资源

还有许多扩展可用于Zephyr和VS Code开发。本指南尚未介绍它们，可参考各自文档完成配置。

<a id="contribution-tooling"></a>

### 贡献辅助工具（Contribution tooling）

- [Checkpatch扩展](https://marketplace.visualstudio.com/items?itemName=idanp.checkpatch)
- [EditorConfig扩展](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)

<a id="documentation-languages-extensions"></a>

### 文档语言扩展（Documentation languages extensions）

- [reStructuredText扩展包](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext-pack)

<a id="ide-extensions"></a>

### IDE扩展（IDE extensions）

- [CMake扩展文档](https://code.visualstudio.com/docs/cpp/cmake-linux)
- [nRF Kconfig扩展](https://marketplace.visualstudio.com/items?itemName=nordic-semiconductor.nrf-kconfig)
- [nRF DeviceTree扩展](https://marketplace.visualstudio.com/items?itemName=nordic-semiconductor.nrf-devicetree)
- [GNU链接器映射文件（Linker Map files）扩展](https://marketplace.visualstudio.com/items?itemName=trond-snekvik.gnu-mapfiles)

<a id="additional-guides"></a>

### 其他指南（Additional guides）

- [如何使用现代可视化IDE开发Zephyr应用](https://github.com/beriberikix/zephyr-vscode-example)

> 注意（Note）：这些扩展的质量和维护程度可能各不相同。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：开发工具与IDE入口](P001_开发工具入口.md) · [本模块主线目录](../reading/developer_tools.md) · [全部主线](../reading/README.md) · [下一篇：IDE for Zephyr扩展](P003_IDE_for_Zephyr扩展.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：开发工具与IDE入口](P001_开发工具入口.md) · [返回大纲](大纲.md) · [下一章：IDE for Zephyr扩展](P003_IDE_for_Zephyr扩展.md)

</details>

<!-- reading-navigation:end -->
