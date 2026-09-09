<!--
SPDX-FileCopyrightText: Copyright (c) 2026 FormingSystem
SPDX-License-Identifier: Apache-2.0
-->

# Git 基础框架来源

本项目的 Git 工作流以 [linux-note](https://github.com/FormingSystem/linux_note) 仓库的提交 `5fd52c4a37e484079b694daeb8af848898281fb1` 为来源基线。继承范围是中文提交、范围语法、列表正文、提交模板、版本化钩子、显式检查暂存区、短期分支和快进主线。

| 本项目文件 | 来源或实现方式 | 许可证 |
| --- | --- | --- |
| `.githooks/commit-msg` | 从来源仓库同路径钩子改编，入口改为调用独立 Python 校验器 | GPL-2.0-only |
| `governance/templates/git_commit_message.txt` | 从来源仓库同路径模板改编，替换项目示例并说明尾注 | GPL-2.0-only |
| `scripts/check_commit_message.py` | 独立实现可测试的提交格式校验器 | Apache-2.0 |
| `scripts/git_setup.py` | 独立实现本仓库本地 Git 配置和根目录检查 | Apache-2.0 |
| `tests/tooling/test_git_workflow.py` | 独立实现真实 Git 钩子、配置幂等性和父仓库保护测试 | Apache-2.0 |
| `.gitattributes`、`.gitignore`、`.editorconfig` | 按固件工程重新编写，采用来源仓库的 LF 管理原则 | Apache-2.0 |
| Git 协作规范和本来源记录 | 根据继承原则编写本项目说明 | Apache-2.0 |

来源仓库的 `LICENSE` 原文保存在 `LICENSES/GPL-2.0-only.txt`。GPL 文件属于本地开发工具，不编入固件。仓库原创代码的 Apache-2.0 声明不改变这些文件以及未来导入第三方代码的许可证。

来源钩子以非 ASCII 字符判断中文，重音字母或表情也会通过。本项目改为检查汉字 Unicode 区间，同时保留一层或两层任意语言范围、可选列表正文；新增有效人工签署与单条代理协助尾注的检查。校验器只验证格式，无法替代人类确认作者身份和签署真实性。

没有复制来源仓库的 `.git`、Git 历史、远端、本地身份配置、工作树状态或用户内容。知识库目录、Obsidian 配置、`format.sh` 及其元数据/标题/链接格式工具、MarkBook 发布流水线和 Loop 应用配置不属于固件工程的 Git 基础框架。
