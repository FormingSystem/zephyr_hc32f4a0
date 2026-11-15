---
id: learning.zephyr-docs.functional-safety.page-8
title: 创建首条RTOS需求
kind: reference
status: maintained
domains: [zephyr, safety, documentation]
source_url: https://docs.zephyrproject.org/latest/safety/safety_requirements/getting_started/create_your_first_requirement.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="create-your-first-zephyr-rtos-requirement"></a>

<a id="create-first-safety-requirements"></a>

# 第8章\_创建首条 Zephyr RTOS 需求（Create your first Zephyr RTOS requirement）

原文：[官方页面](https://docs.zephyrproject.org/latest/safety/safety_requirements/getting_started/create_your_first_requirement.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="repository-overview"></a>

## 8.1 仓库概览（Repository Overview）

Zephyr 使用 [StrictDoc](https://github.com/strictdoc-project/strictdoc) 在 `reqmgmt` 仓库中管理需求，仓库包含：

> 译注——操作位置：以下编辑发生在读者检出的 `reqmgmt` 需求仓库中。文件编辑可使用任意文本编辑器；命令在该仓库根目录的 UCRT64 Bash 或 Linux Bash 中执行，先满足[需求管理入门](P007_需求管理入门.md)的工具版本前提。本文不要求把需求仓库复制到中文翻译目录，也不在此启动服务。

- `docs/`：StrictDoc 格式的需求文档。

- `tools/`：实用脚本和配置。

- `strictdoc.toml`：StrictDoc 项目配置。

- `tasks.py`：使用 Invoke 的任务自动化脚本。

<a id="step-1-create-or-edit-a-requirement-file"></a>

## 8.2 第一步：创建或编辑需求文件

进入仓库的 `docs/` 目录。

<a id="folder-overview"></a>

### 8.2.1 文件夹概览（Folder Overview）

`docs/` 包含所有采用 StrictDoc 格式编写的需求文档。

`docs/` 下有两个子目录，组织如下：

- `system_requirements/`：高层系统需求，描述 Zephyr RTOS 的整体目标、约束和预期行为。

  - `system_requirements.sgra`：包含语法（GRAMMAR），定义需求的正式结构。

  - `index.sdoc`：包含实际的需求陈述。

- `software_requirements/`：组件级需求，每个文件对应一个子系统或模块。

  - `software_requirements.sgra`：包含所有软件需求的语法（GRAMMAR）。

  - 一组 `.sdoc` 片段文件，共同组成完整的软件需求文档，例如：

    - `interrupts.sdoc`

    - `queues.sdoc`

    - `semaphore.sdoc`

    - `threads.sdoc`

文件按模块组织，方便贡献者分别处理不同部分。可以编辑已有 `.sdoc` 文件，也可以新建文件。下面是一个基本需求块示例：

```text
[REQUIREMENT]
UID: ZEP-SRS-17-1
STATUS: Draft
TYPE: Functional
COMPONENT: File System
TITLE: Create file
STATEMENT: >>>
Zephyr shall provide file create capabilities for files on the file system.
<<<
```

将 UID 设为 `TBD`，以便 StrictDoc 在后续步骤自动生成。

> 译注——原示例与文字不一致：上方原始代码已经写了 `UID: ZEP-SRS-17-1`，而紧随其后的文字要求 `TBD`；后面的输出又示意为 `ZEP-SRS-17-2`。这些原样保留，不表示工具会将已有 UID 自动递增改写。示例中的 Draft 为草稿、Functional 为功能性、File System 为文件系统、Create file 为创建文件；陈述的中文含义是“Zephyr 应提供在文件系统上创建文件的能力”。实际新需求先按工具与仓库规则准备标识，再检查生成结果，不要复制一个已存在的 UID。

<a id="step-2-save-the-file"></a>

## 8.3 第二步：保存文件

将文件保存在 `docs/` 下的系统需求或软件需求子目录中。新文件应取有意义的名称，通常体现所属组件或功能。

<a id="step-3-assign-a-uid-automatically"></a>

## 8.4 第三步：自动分配 UID

在仓库根目录执行以下命令：

```text
strictdoc manage auto-uid .
```

此命令将：

- 遍历项目目录。

- 查找包含 `UID: TBD` 的需求。

- 为每条需求分配唯一标识符。

<a id="step-4-verify-the-uid-assignment"></a>

## 8.5 第四步：检查 UID 分配

重新打开文件，应看到类似内容：

```text
UID: ZEP-SRS-17-2
STATUS: Draft
TYPE: Functional
COMPONENT: File System
TITLE: Create file
STATEMENT: >>>
Zephyr shall provide file create capabilities for files on the file system.
<<<
```

注意：UID 格式可在 `strictdoc.toml` 中配置。

> 译注——配置与生成结果：这是原页对配置方式的说明，当前上游配置文件差异见[入门页译注](P007_需求管理入门.md)。执行 auto-uid 后，应重新打开实际需求文件并检查差异，确认标识唯一且引用关系正确；未得到有效结果时先核对所用版本与需求语法，不继续提交重复标识。

<a id="optional-generate-html-documentation"></a>

## 8.6 可选：生成 HTML 文档

构建需求的 HTML 文档版本：

```text
strictdoc export .
```

这会在 `output/` 目录生成可浏览文档。

<a id="optional-launch-the-web-editor"></a>

## 8.7 可选：启动 Web 编辑器

交互式浏览和编辑需求：

```text
strictdoc server .
```

此命令启动本地 Web 界面，用于编辑和评审需求。

<a id="summary"></a>

## 8.8 小结（Summary）

- 在 `docs/` 中创建或编辑需求，并使用 `UID: TBD`。

- 运行 `strictdoc manage auto-uid .` 分配 UID。

- 可按需生成 HTML 文档或启动 Web 编辑器。

StrictDoc 帮助 Zephyr 跨平台维护结构化、可追溯、可编辑的需求。

对应官方文档源码：[doc/safety/safety_requirements/getting_started/create_your_first_requirement.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/safety/safety_requirements/getting_started/create_your_first_requirement.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/safety/safety_requirements/getting_started/create_your_first_requirement.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未安装或运行需求工具、生成认证材料或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：需求管理入门](P007_需求管理入门.md) · [本模块主线目录](../reading/functional_safety.md) · [全部主线](../reading/README.md) · [下一篇：需求目录](P009_需求目录.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P007_需求管理入门.md) · [返回大纲](大纲.md) · [下一章](P009_需求目录.md)

</details>

<!-- reading-navigation:end -->
