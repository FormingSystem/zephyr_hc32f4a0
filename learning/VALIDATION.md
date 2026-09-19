<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 教学验证记录

验证日期：2026-09-19。本页记录 venv/west 教学验收范围，下文“本轮未执行”只针对本页对应批次。

## 实测基线

| 项目 | 本次版本 |
| --- | --- |
| 主机 | Windows 11，10.0.26200 |
| Python | 3.12.10 |
| pip | 25.0.1（该基础解释器创建环境时的版本） |
| west | 1.5.0 |
| setuptools | 80.9.0 |
| Git | UCRT64 主线为 MSYS2 Git 2.55.0；早期验证使用 Git for Windows 2.55.0.windows.3 |
| Bash | MSYS2 Bash 5.3.15，MSYSTEM=UCRT64 |

工具直接依赖写在 [requirements-tools.txt](requirements-tools.txt)。它不锁全部传递依赖；新机器若需精确保存测试环境，应额外记录安装结果和分发文件。教学脚本使用 Python 标准库以及 west 安装时所依赖的 PyYAML。

## 读者如何自行验收

当前位置：仓库根目录。UCRT64 Bash：

```bash
export MSYS="${MSYS:+$MSYS }noglob"
py -3.12 -m venv build/learning-tools/tools
build/learning-tools/tools/Scripts/python.exe -m pip install -r learning/requirements-tools.txt
build/learning-tools/tools/Scripts/python.exe -u learning/check_labs.py
build/learning-tools/tools/Scripts/python.exe learning/check_docs.py
```

自动验收要求 Python 3.11 及以上，因为文档检查使用标准库 tomllib；章节示例与种子生成器本身可使用 3.10 及以上。工具已安装时不用重复创建。不要对验收脚本使用 Python `-O`，它会关闭断言。

实验检查创建随机运行目录，不覆盖已有手工实验；成功以 `ALL CHECKS PASSED` 结束。它只在生成的独立 Git 仓库中创建教学提交，不提交本教程仓库。每次输出保留证据的位置；不自动删除，方便读者观察。检查过程中不使用用户的 west/pip 获取配置，并通过本地 wheel 安装业务依赖；可编辑安装测试在临时环境中复用已安装的构建后端文件，以免为重复检查联网下载。手工教学流程仍采用正常 pip 安装后端。

## 已覆盖的行为

| 专题 | 检查项目与可观察结果 |
| --- | --- |
| venv 身份 | 不激活时前缀不同，激活变量可为空；另核对 Bash 激活/退出及激活 A 时直接调用 B |
| 包隔离 | A/B 分别输出 v1/v2；B 卸载不改变 A；未安装时导入失败 |
| 重建与约束 | freeze 后在新环境重装；矛盾版本要求失败；pip check 通过 |
| 配置与导入 | site 配置设置/读取/删除、环境变量可见；同名文件遮蔽导致预期导入失败 |
| 可编辑安装 | 修改开发副本后新进程读取新输出 |
| west 初始化 | 本地 init 后项目未获取；update 后应用输出 5；重复种子名称拒绝覆盖；从本地清单地址以 -m/--mr 克隆初始化 |
| 版本与冻结 | 默认游离 HEAD；本地开发提交不同于 manifest-rev；冻结记录后者；新工作区按冻结重建 |
| 本地分支 | 普通 update 离开开发分支；重新 switch 后开发文件仍在 |
| 配置与组 | local 覆盖隔离的 global；启用组再更新才克隆；停用不删除目录；相对 remote/defaults 重构后地址等价 |
| 导入与扩展 | 自仓库拆分导入、普通项目导入版本边界；禁用、缺失检查、非法参数、增加计数选项 |
| 相对路径 | 整个本地实验目录移动到含空格/中文的新路径后，强制重新获取与运行仍成功 |

在项目主仓库通过 UCRT64 Bash 重新执行自动实验与主线命令。人工命令块核对与结构审阅记录在 [REVIEW.md](REVIEW.md)。

本轮同时运行 `scripts/project.py check`：使用工程原有 Python 环境及 Git for Windows 时，41 项工具测试、pyOCD 离线检查和差异检查通过。初次让工程检查使用 MSYS2 Git 时，6 项失败、8 项报错，原因是现有工程检查把 Git 输出的 MSYS 路径当作 Windows 路径。教程实验可以使用 MSYS2 Git 加准备章的 noglob 设置；工程维护检查仍沿用项目原有 Git for Windows，两者均从 Bash 发起。本次没有修改工程检查器或系统全局 PATH。

## 验证边界

UCRT64 Bash 在 Windows 本机实测；Linux/macOS 系统本身未实测，跨平台替换规则作静态核对。没有安装/验证 Zephyr SDK、硬件构建、烧录、远程 Git 认证、不同 Python 大版本或第三方带本地扩展包。主线以小型纯 Python 包验证环境隔离，不能据此推导所有平台的二进制包兼容性。

在线官方文档会更新；新特性须以安装版本帮助为准。来源与下载材料采用范围见 [REFERENCES.md](REFERENCES.md)。
