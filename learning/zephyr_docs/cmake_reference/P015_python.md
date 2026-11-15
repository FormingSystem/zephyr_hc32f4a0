---
id: learning.zephyr-docs.cmake-reference.module.python
title: python
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/python.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_python

原文：[python](https://docs.zephyrproject.org/latest/build/cmake-ref/module/python.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:python"></a>

为 Zephyr 构建系统查找并配置 Python，确保存在兼容的 Python 版本，并设置必要的环境变量（Environment Variable）和 CMake 变量。

## 15.1\_变量（Variables）

`PYTHON_MINIMUM_REQUIRED` 指定所需的最低 Python 版本。本 CMake 模块完成后定义 `PYTHON_EXECUTABLE`。

## 15.2\_查找过程（Search Process）

模块按以下顺序查找 Python：

1. 使用已定义的 `Python3_EXECUTABLE`。
2. 使用已定义的 `WEST_PYTHON`。
3. 在系统 `PATH` 和虚拟环境（Virtual Environment）中查找 `python` 或 `python3`。
4. 使用 CMake 的 `find_package(Python3)` 机制。

模块会验证找到的 Python 是否满足最低版本要求。

## 15.3\_Windows 专用配置

在 Windows 系统中，模块将环境变量 `PYTHONIOENCODING` 设为 `utf-8`，确保从 CMake 调用 Python 时具有一致的编码行为。

## 15.4\_使用示例（Example Usage）

加载模块后，使用 `PYTHON_EXECUTABLE` 调用 Python 脚本：

```cmake
include(python)

# Now PYTHON_EXECUTABLE can be used to invoke Python scripts
execute_process(COMMAND ${PYTHON_EXECUTABLE} my_script.py)
```

## 15.5\_原文相关链接

- [variable:PYTHON_MINIMUM_REQUIRED](P047_PYTHON_MINIMUM_REQUIRED.md#variable:PYTHON_MINIMUM_REQUIRED)
- [variable:PYTHON_EXECUTABLE](P046_PYTHON_EXECUTABLE.md#variable:PYTHON_EXECUTABLE)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：doc](P014_doc.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：west](P016_west.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P014_doc.md) · [返回大纲](大纲.md) · [下一章](P016_west.md)

</details>

<!-- reading-navigation:end -->
