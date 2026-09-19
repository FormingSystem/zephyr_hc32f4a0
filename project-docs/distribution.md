<!-- SPDX-License-Identifier: Apache-2.0 -->

# 发布到新 GitHub 后如何让别人重建

当前交付形态是完整源码仓库。别人克隆后拥有 Zephyr、板级支持、CMSIS_6 和 HAL；编译工具按清单安装即可。无需把自己的 SDK 或 .venv 打包上传。本文给出发布准备和接收者流程，不代表已经创建或推送了新 GitHub 仓库。

## 随 Git 分发的契约

| 提交 | 本机生成，不提交 |
| --- | --- |
| 固件源码、模块源码及原许可证 | SDK、Python 安装目录、下载缓存 |
| dependencies.lock.json、requirements-dev.txt、requirements-tools.txt | .venv、pip 缓存 |
| project-west.yml、scripts/west-commands.yml | 仓库父目录的 .west/config |
| setup_environment.py、project_env.py、configure_west.py | .local/environment.json |
| code-workspace、教学与项目文档 | .vscode 本机设置、build、原始硬件资料 |

上游根 west.yml 保留来源内容；本项目初始化明确指定 project-west.yml。发布前核对 .gitignore 和暂存区，确保未跟踪个人路径、凭据、虚拟环境、下载包。许可证和来源记录必须随对应源码保留。

## 接收者从空目录开始

先按[环境文档](environment.md)安装主机工具和匹配 SDK，然后在 UCRT64 Bash 中：

```bash
read -r -p "请输入发布者提供的 GitHub 仓库 URL: " REPO_URL
mkdir hc32-workspace
cd hc32-workspace
git clone "$REPO_URL" zephyr_hc32f4a0
cd zephyr_hc32f4a0
read -r -p "请输入已安装的 SDK 目录: " SDK_DIR
py -3.12 scripts/setup_environment.py --sdk "$SDK_DIR"
source .venv/Scripts/activate
python scripts/configure_west.py
python scripts/project_env.py exec west manifest --path
python scripts/project_env.py doctor
python scripts/project_env.py check
python scripts/project_env.py build
python scripts/project_env.py test
```

hc32-workspace 是自选的新目录名，若已存在请选择另一个空目录，不在已有 Git 仓库里再套工作区。clone 和 pip 安装需要访问发布源；配置 west 本身不下载工具。仓库内生成 .venv、父目录生成 .west 是正常现象。得到 HC32 ELF、源码来源审计通过和 QEMU 软件测试通过，才完成软件环境验收；实板步骤按[硬件记录](hardware.md)另做。

不需要 west zephyr-export：项目入口已显式固定当前 Zephyr。不要运行不带项目清单选择的上游 west init/update 流程来补依赖。

## 发布者如何准备一个可审查版本

1. 更新 README、源码基线与移植状态，核对实际 SDK、Python、west/pyOCD 版本。
2. 用根目录环境运行 doctor、check、build --pristine、test；核对忽略项与待提交内容。
3. 发布前另取干净克隆验证上面的安装流程。当前工作区测试不能代替新机器验证。
4. 按项目 Git 规范拆分提交，选择并记录发布 tag。新 GitHub URL、访问权限和推送目标由发布者确定后再发布。

若更换正式仓库地址，也要同步 README 或协作约定里声明的远程地址；本轮未擅自改现有 origin。可先 `git remote -v` 查看，再按实际发布决策配置远程。不要将未经确认的新地址写成所有人的安装指令。

## 可重复到什么程度

Git 提交固定源码；dependencies.lock.json 记录模块与 SDK 基线；requirements-tools.txt 固定关键项目工具，但 Zephyr Python 依赖仍含范围。需要严格版本发布时，对每种受支持 OS/Python 组合单独生成并验证约束，不把某一台 Windows 的 pip freeze 当成通用锁。

维护者可保存本次环境清单到忽略目录：

```bash
python -m pip freeze > build/python-environment.txt
python scripts/project_env.py doctor > build/environment-report.txt
```

这些是证据快照，只有经过干净环境复建后才能升级为正式安装约束。SDK 安装包版本与官方校验值也应核对。CI 负责按公开依赖安装和构建，缓存只加速，不能成为唯一依赖来源。

## 将来想把仓库变小怎么办

可另外设计 manifest 仓库，让 west projects 分别引用 Zephyr fork、CMSIS 和 HAL 的固定提交；那时 west update 才负责获取这些独立源码。迁移还必须调整 source_path、CMake 模块发现、源码审计、CI 和许可证记录，并验证干净克隆。

这是未来架构选择，不是现在把 projects 填上游默认项目就能完成的开关。west 管理源码版本，不会因此变成 SDK 或系统包管理器。当前单仓库方案已经允许别人重建，不必先拆仓库。
