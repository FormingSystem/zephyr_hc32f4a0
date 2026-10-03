---
id: repository.markdown-provenance
title: Markdown 格式规范继承记录
kind: reference
status: maintained
domains: [repository, documentation]
---

<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_Markdown\_格式规范继承记录

2026-10-03 按开发者要求，从 linux-note 继承 Markdown 格式规则，并明确排除 Zephyr 原生 Markdown。目标规范为 [Markdown 文档格式规范](../conventions/markdown_guide.md)。

## 1.1\_固定来源

来源仓库为 [FormingSystem/linux_note](https://github.com/FormingSystem/linux_note)，核对节点为 `d2a942520db0b5dd0ab9d8e71225119e1bbf5042`。核对时以下来源文件没有未提交修改。

| 来源文件 | 继承或核对内容 |
| --- | --- |
| `AGENTS.md` 1.4—1.7 | 相对链接、粗体间距、文档命名、元数据、标题层级与序号、下划线转义、链接维护 |
| `scripts/format_markdown.sh` | H1—H6 计数方式、标题分隔形式、代码围栏排除原则 |
| `scripts/format_metadata.sh` | 稳定 ID、元数据字段及 kind/status 取值 |
| `format.sh` | 来源工具的全仓默认范围和环境依赖，用于判断本项目是否适合直接导入 |

来源许可证为 GPL-2.0-only；继承规则的规范文档保留该许可证，全文见本仓库 `LICENSES/GPL-2.0-only.txt`。本来源记录和工程自身的检查程序保持各自原有许可证。

## 1.2\_项目适配与边界

- 继承格式规则，不继承 linux-note 的知识库目录布局、发布流程、Obsidian 配置或全仓格式化工具。此前 Git 框架继承记录仍描述当时的 Git 专项范围。
- 自有文档采用新规则；Zephyr、CMSIS 和厂商代码随附文档保持来源格式。本次只整理两个下载专题及本次规范，不扩大到已有的其他自有教材。
- 保留现有章节文件名、稳定 ID 和技术正文；H1 保留文档标题的含义，章节号按文件名确定，不用文件名覆盖作者已写好的标题。
- 将原先跳过 H2 的开头小节提升为 H2 后统一编号，避免产生无父标题的三级小节；正文顺序、命令块和附件路径保持不变。
- `learning/check_docs.py` 同时识别本次继承的标题形式与尚未迁移的自有教材旧形式，避免因局部整理强制修改其他专题；这不表示旧形式是新文档的推荐格式。

## 1.3\_本次验证

核对两个下载专题的代码围栏内容和非标题正文，确认排版不改变命令或技术含义；检查标题层级、连续编号、元数据、本地链接及 Git 差异。格式检查不代替代理连接、软件安装、完整下载或实板验证。
