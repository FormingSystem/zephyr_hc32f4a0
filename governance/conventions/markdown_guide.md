---
id: repository.markdown-guide
title: Markdown 文档格式规范
kind: reference
status: maintained
domains: [repository, documentation]
---

<!-- SPDX-FileCopyrightText: Copyright (c) 2026 FormingSystem -->
<!-- SPDX-License-Identifier: GPL-2.0-only -->

# 第1章\_Markdown\_文档格式规范

本规范继承 linux-note 的 Markdown 格式约定；固定来源、继承范围和本项目适配见[来源记录](../architecture/markdown_provenance.md)。

## 1.1\_适用范围

适用于本项目自有的学习材料、项目说明和治理文档。**不得为了统一格式修改 Zephyr 原生 Markdown 或其他第三方文档。** 文件是否属于自有内容以来源记录和 Git 历史为准，不能仅凭扩展名或所在目录判断。

2026-10-05 用户将资料规范化范围扩展到 `learning/`：统一章节命名、导航与 Markdown/PPT 职责，具体约定见 [learning 资料编写约定](../../learning/资料编写约定.md)。此范围不包含 Zephyr 原生文档；其他自有文档只同步受影响的链接，不执行全仓批量格式化。

## 1.2\_文件与元数据

- `learning/` 章节按用户 2026-10-05 的资料规范统一使用 `P001_主题.md`，公共准备为 `P000`；配套 PPT 同编号同题名，平台流程用 `_Windows` / `_Linux` 后缀。其他自有文档保留既有 `PXX_NAME.md` 规则，非章节文件使用稳定语义名称。
- 目录使用稳定英文 `snake_case` 名称；路径避免空格、中文标点、全角符号、连续下划线和首尾下划线。`C++`、`u-boot`、版本号中的 `.` 等有语义的半角符号可以保留。
- 正式文档在文件首部提供 YAML Front Matter，包含稳定的 `id`、中文 `title`、`kind`、`status` 和 `domains`。已有 `id` 不因标题或阅读顺序变化重算。
- `kind` 按内容职责选择：`concept`、`mechanism`、`subsystem`、`interface`、`engineering`、`platform`、`lab`、`project`、`source`、`investigation`、`reference`、`track`、`publication`。专题大纲使用 `track`，操作教程使用 `engineering`。
- `status` 使用 `draft`、`evolving`、`maintained` 或 `archived`；格式整理不会自动提高内容的核验状态。

```yaml
---
id: zephyr-download-example
title: 下载环境准备
kind: engineering
status: evolving
domains: [zephyr, tools]
---
```

## 1.3\_标题与阅读序号

| 层级 | Markdown 源码形式 | 计数规则 |
| --- | --- | --- |
| H1 | `# 第1章\_标题` | 章节号与 `PXX_` 文件名一致；独立单篇从第 1 章开始 |
| H2 | `## 1.1\_标题` | 在所属 H1 内递增 |
| H3 | `### 1.1.1\_标题` | 在所属 H2 内递增 |
| H4 | `#### (1)\_标题` | 在所属 H3 内重新计数 |
| H5 | `##### 1)\_标题` | 在所属 H4 内重新计数 |
| H6 | `###### a)\_标题` | 在所属 H5 内重新计数，超过 26 项后用 `aa)`、`ab)` |

标题使用 ATX 的 `#` 形式，层级连续，不超过 H6。每级序号在父标题内重新计数，不因材料尚为草稿而删除阅读序号。

标题源码中的下划线统一转义为 `\_`，包括技术名称中原有的下划线。标题文字采用来源约定的下划线分隔方式；正文、代码、URL 和文件路径中的下划线不按标题规则改写。

## 1.4\_正文与引用

保持中文笔记风格，按需要说明概念、背景、操作步骤和结论。中文正文标记重点时，粗体与前后普通正文尽量留半角空格，如 `正文 **重点** 正文`；紧邻标点时不强行加空格，避免整段加粗。

Markdown 链接、图片优先使用相对路径。移动、改名或修改标题后，同步检查 Markdown、Obsidian 链接及锚点；目标不唯一时不猜测替换。

列表、表格和代码块与相邻正文留空行；命令块标明实际语言。格式整理必须保留命令、代码、路径、图片和技术结论，不把代码围栏里的 `#` 当成正文标题。

## 1.5\_本项目检查方式

在本仓库根目录运行：

```bash
python learning/check_docs.py
git diff --check -- learning/P01_zephyr_make_project learning/download_zephyr
```

第一项检查教学文档的链接、元数据和章节编号；第二项检查本次自有下载文档的空白差异。仍需人工核对标题层级、可读性及修改范围。

来源仓库使用 `format.sh` 管理标题、元数据、路径和链接。本次继承格式规则，不复制其针对整个知识库运行的格式化与安装工具；本仓库没有该命令入口，不应直接套用来源的全仓格式化命令。
