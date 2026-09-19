<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# west 本地多仓库实验

本实验用应用、算术库、可选文档模拟多仓库组合，不依赖 Zephyr、板卡或网络 Git 服务。

从[第一章](../P01_建立第一个多仓库工作区.md)准备工具环境，再在本仓库根目录执行：

```text
python learning/west/labs/seed_workspace.py --name demo-01
```

Python 须为 3.10 及以上，Git 应支持 `init -b`（2.28 及以上）。生成脚本只使用 Python 标准库和 Git；随后使用的 west 基线是 1.5.0。

脚本创建 `build/learning-tools/west/demo-01/remotes/` 和 `workspace/manifest/`，初始化独立 Git 历史，使用教学提交身份；不修改用户全局 Git 设置，不推送，不替你执行 init/update。名称存在时拒绝覆盖，改新名字即可重复实验。

| 源文件 | 作用与修改入口 |
| --- | --- |
| [init_workspace.py](init_workspace.py) | 在外层已有 .west 时，从中立目录运行真实 init，保护外层配置 |
| [seed_workspace.py](seed_workspace.py) | 创建两版算术库、消费应用和文档源仓库，保存提交标识 |
| [west.yml.in](templates/west.yml.in) | 清单模板；用相对于各消费项目仓库的路径获取本地源仓库 |
| [west-commands.yml](templates/west-commands.yml) | 声明命令名、Python 文件和类之间的映射 |
| [inventory.py](templates/commands/inventory.py) | 完整只读扩展，支持 JSON 与缺失检查 |

目录中 `revisions.json` 保存本轮算术库 v1/v2 的提交标识；每次生成的标识可能不同。本地 Git 地址使用相对路径，保留 remotes 与 workspace 的层次即可整体搬动实验目录，不写入作者机器路径。应用通过自己的 Python 搜索路径读取相邻仓库代码，west 不负责这个运行时整合，类比到 C/C++ 就是取源码与把源码接入构建是两件事。

实验副本才是运行时读取的位置。修改模板影响下一次生成；修改当前 workspace/manifest 中的文件影响当前工作区。清理前保存自己在副本里的开发提交，不要误删仓库正式 `labs/`。自动检查方式见[验证记录](../../VALIDATION.md)。
