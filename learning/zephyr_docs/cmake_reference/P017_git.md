---
id: learning.zephyr-docs.cmake-reference.module.git
title: git
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/git.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_git

原文：[git](https://docs.zephyrproject.org/latest/build/cmake-ref/module/git.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:git"></a>

<a id="command:git_describe"></a>

本模块为 Zephyr 构建系统提供与 Git 仓库交互的函数。

## 17.1\_命令（Commands）

`git_describe` 获取与目录或文件关联的简短 Git 描述（Git Description）。

```cmake
git_describe(<file|dir> OUTPUT)
```

函数在给定目录中运行 `git describe --abbrev=12 --always`；若给出文件，则在该文件所在目录运行。两种情况下，结果都存入所指定的输出变量。

- `file|dir`：要针对其运行 Git 命令的文件或目录。
- `OUTPUT`：保存 Git 描述的变量名称。若 Git 命令失败或未找到 Git，不设置此变量。

Git 命令失败时，函数输出错误状态消息；Git 命令产生警告时，输出警告状态消息。

## 17.2\_使用示例（Example Usage）

加载模块，获取当前源目录的 Git 描述；仅在输出变量已定义时打印：

```cmake
include(git)

git_describe(${CMAKE_CURRENT_SOURCE_DIR} GIT_DESCRIPTION)
if(DEFINED GIT_DESCRIPTION)
  message(STATUS "Git description: ${GIT_DESCRIPTION}")
endif()
```

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：west](P016_west.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：yaml](P018_yaml.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P016_west.md) · [返回大纲](大纲.md) · [下一章](P018_yaml.md)

</details>

<!-- reading-navigation:end -->
