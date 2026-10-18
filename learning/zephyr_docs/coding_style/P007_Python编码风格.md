---
id: learning.zephyr-docs.coding-style.page-7
title: Python编码风格
kind: reference
status: maintained
domains: [zephyr, documentation, style]
source_url: https://docs.zephyrproject.org/latest/contribute/style/python.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Python编码风格

原文：[官方页面](https://docs.zephyrproject.org/latest/contribute/style/python.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 7.1\_风格和格式化工具

Python 代码遵循 [PEP 8](https://peps.python.org/pep-0008/)。Zephyr 采用 [Ruff 格式化工具（Ruff formatter）](https://docs.astral.sh/ruff/formatter/)，其格式选择具有明确约定，目标是提升一致性、通用性和可读性，并减少 Git 差异（diff）。

```sh
ruff check --select I --fix <file> # Sort imports
ruff format <file>
```

> 译注：原例中的 `<file>` 表示要处理的 Python 文件，执行时替换为实际相对路径；不要把尖括号占位符原样交给 shell。第一行注释 `Sort imports` 表示“对导入语句排序”，第二行进行代码格式化。使用前须已有 Ruff 及待处理文件，本批没有运行格式化操作。

## 7.2\_Ruff 配置（Configuration）

采用 Ruff 默认配置，并作以下调整：

- 行长限制为 100 列。
- 允许使用单引号 `'` 或双引号 `"`。
- 行结束符使用 Unix 默认的 `\n`。

## 7.3\_排除项（Exclusions）

由于引入该格式化工具时已有大量旧代码，持续集成（Continuous Integration，CI）中的格式检查只对新添加的 Python 文件强制执行。

当前排除的文件列在 [`.ruff-excludes.toml`](https://github.com/zephyrproject-rtos/zephyr/blob/main/.ruff-excludes.toml) 的 `[format]` 部分。修改排除列表中的文件时，鼓励将该文件移出列表并应用格式化；这一格式变更应放在单独的提交中。


对应官方文档源码：[doc/contribute/style/python.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/contribute/style/python.rst)。

本仓库的[对应源码](../../../doc/contribute/style/python.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="python-style-guidelines"></a>
<a id="python-style"></a>
<a id="ruff-configuration"></a>
<a id="excluded-files"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：命名规范](P006_命名规范.md) · [本模块主线目录](../reading/coding_style.md) · [全部主线](../reading/README.md) · [下一篇：Doxygen注释规范](P008_Doxygen注释规范.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P006_命名规范.md) · [返回大纲](大纲.md) · [下一章](P008_Doxygen注释规范.md)

</details>

<!-- reading-navigation:end -->
