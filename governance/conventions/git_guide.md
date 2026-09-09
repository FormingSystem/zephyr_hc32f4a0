<!--
SPDX-FileCopyrightText: Copyright (c) 2026 FormingSystem
SPDX-License-Identifier: Apache-2.0
-->

# Git 协作与提交规范

本项目继承 `linux-note` 的中文提交格式、可验证提交与快进主线规则。代码结构、构建检查和许可证按本项目维护；移植到 Zephyr 上游时另行遵守上游提交格式。

## 初始化本地配置

在本项目根目录使用 Python 3.10 或更新版本：

```powershell
python scripts/git_setup.py
python scripts/git_setup.py --check
```

脚本仅配置自身所在独立仓库的本地 Git 配置：

| 配置 | 值 | 用途 |
| --- | --- | --- |
| `core.hooksPath` | `.githooks` | 启用版本化提交检查 |
| `commit.template` | `governance/templates/git_commit_message.txt` | 使用中文提交模板 |
| `core.autocrlf` | `false` | 由 `.gitattributes` 决定行尾 |
| `core.longpaths` | `true` | 支持 Windows 长路径 |
| `pull.ff` | `only` | 拉取不创建意外合并提交 |
| `fetch.prune` | `true` | 清理已删除远端分支的跟踪引用 |

脚本拒绝将父级 Zephyr 仓库识别为本项目，不修改全局配置、远程连接、用户名或邮箱。重复运行得到相同配置；`--check` 只读检查。

Git for Windows 自带运行钩子所需的 `sh`。钩子优先寻找激活环境、仓库及上两级目录的 `.venv`，随后寻找 PATH 中的 `python`、`python3`。Linux 使用相同钩子和 Python 校验器。

## 分支和历史

`master` 是通过验证后交付的主线。开发使用短期任务分支，例如 `feat/soc-hc32f4a0`、`fix/board-clock`、`docs/debugging`。并行修改同一仓库时使用独立 worktree，避免共享暂存区。

```sh
git fetch origin
git rebase origin/master
git switch master
git merge --ff-only <任务分支>
```

新建且远端为空的仓库先建立初始提交，之后才存在 `origin/master` 可供变基。只通过普通 push 交付已验证提交；推送被拒绝时先检查远端变化。

已经推送或交付的提交通过 `revert` 撤销，不执行 `reset`、强制移动主线或强推。未交付任务分支的临时修正可以整理为 `fixup` 并在合入前 autosquash。一个提交形成一个可独立验证、审查和回退的结果，实现所需文档与测试随实现一起维护。

## 提交信息

```text
<类型>[(<项目>[/<模块>])]!?: <中文结果>
```

允许类型为 `feat`、`fix`、`refactor`、`perf`、`security`、`content`、`docs`、`test`、`build`、`ci`、`release`、`revert`、`chore`。

范围可省略，也可填写一层或两层。范围没有项目名单和语言限制，不能包含空白、括号、冒号或多余斜杠。结果说明必须包含汉字，`!` 表示破坏性变更。例如：

```text
feat(board/uyup): 增加核心板启动配置
fix(soc/clock): 按12MHz晶振修正PLL参数
docs: 补充调试器恢复步骤
```

标题足够表达结果时可以没有正文。需要补充验证、风险或多个结果时，正文每个非空行必须采用 `- 描述` 列表。

有效的人工 `Signed-off-by: 姓名 <邮箱>` 尾注予以保留。代理不得代替人类添加签署，也不得添加 `Co-authored-by`。人工独立提交允许没有 `Assisted-by`；代理参与的提交必须且只能包含一行 `Assisted-by: Agent:model [tool ...]`，填写实际代理和模型信息。校验器不修改提交信息，也不会自动增加上述尾注。

尾注组成提交信息末尾的连续段落，并与标题或正文之间留一个空行。除这里明确允许的 `Signed-off-by`、`Assisted-by` 外，正文仍需采用列表；新增尾注类型须先更新校验规则。

## 提交前检查

```sh
python scripts/git_setup.py --check
python -m unittest discover -s tests/tooling -p 'test_*.py' -v
git diff --check
git status --short
git diff
git add <明确路径>
git diff --cached --check
git diff --cached
```

构建和实板验证按根目录 README 中的当前入口执行。主机工具测试或 QEMU 成功不代表 HC32 实板已启动。提交前记录实际运行结果及尚未执行的硬件验证。

直接执行的 Shell 钩子以 `100755` 模式提交；Windows 首次暂存钩子后用 `git update-index --chmod=+x .githooks/commit-msg` 设置。Python 工具统一通过解释器调用。不得用 `git add .`、`git add -A` 或 `git commit -a` 混入未审查文件。

构建目录、虚拟环境、固件输出、日志、凭据和机器专属路径不进入仓库。不能直接复制父级 Zephyr 的 `.git`，也不能复制来源仓库的用户身份、远端或工作区状态。
