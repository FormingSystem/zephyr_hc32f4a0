<!-- SPDX-License-Identifier: Apache-2.0 -->

# 当前工程如何配置 west

west 是 Python 命令行程序；工作区清单描述源码仓库组合，扩展命令负责构建、测试等操作。先区分“安装 west”与“告诉 west 当前工程在哪里”。通用原理和无需联网的小实验见 [west 大纲](../../learning/west/大纲.md)。

首次学习请先做 [west 手把手实训](../../learning/west/labs/README.md)：用本地源仓库亲手执行初始化、同步、升级、分组、新增仓库和扩展修改，并运行四项验收。工具初次安装需要网络，之后源码操作在本地进行。实训 .west 与工程父目录 .west 分开，不能把教学清单覆盖到当前工程。

## 本工程采用的布局

本仓库已经跟踪完整 Zephyr、CMSIS_6 和华大 HAL 源码。SDK、Python 解释器、Python 包仍由本机安装。当前采用“工作区包含一个完整源码仓库”的标准布局：

```text
workspace/              自选工作区目录，本身不是 Git 仓库
  .west/config          本机生成，在工程仓库外
  zephyr_hc32f4a0/       Git 仓库根，日常命令从这里执行
    .git/
    project-west.yml    本项目清单，提交
    west.yml            保留的上游清单，不是当前入口
    scripts/west-commands.yml
    modules/hal/cmsis_6/
    modules/hal/xhsc/
    .venv/              本机生成，不提交
```

[project-west.yml](../../project-west.yml) 的 `projects: []` 有意为空：需要的模块已经在当前 Git 仓库中，不应再下载另一套。`self.west-commands` 注册当前源码的 build、boards、twister 等扩展。`self.path` 给采用远程 manifest 初始化的布局提供目录名，不会重命名现有克隆。

## 第一次配置

先完成[环境安装](../environment.md)，在仓库根目录的 UCRT64 Bash 中执行：

```bash
source .venv/Scripts/activate
python scripts/configure_west.py
python scripts/project_env.py exec west topdir
python scripts/project_env.py exec west config manifest.path
python scripts/project_env.py exec west manifest --path
python scripts/project_env.py exec west manifest --validate
python scripts/project_env.py exec west list
python scripts/project_env.py exec west help build
```

预期 topdir 指向当前克隆的父目录；manifest.path 是实际克隆目录名；清单是仓库内的 project-west.yml；list 只有 manifest 自身。克隆目录名为 zephyr_hc32f4a0 时，脚本在父目录生成 ../.west/config：

```ini
[manifest]
path = zephyr_hc32f4a0
file = project-west.yml
[zephyr]
base = zephyr_hc32f4a0
```

这些路径相对于工作区根目录。脚本根据实际克隆目录名填写，可以重复执行；父目录已有其他 manifest 配置时拒绝覆盖。父目录自身为 Git 仓库、或者工程内残留 .west 时也会拒绝，要求先检查布局。它不删除工作区，不修改上游 west.yml。

这是 `west init -l --mf project-west.yml .` 使用的父工作区拓扑；辅助脚本让已克隆工程的本机配置可检查、可重复。两种入口择一使用，初始化成功后不要反复 init。特别注意 --mf：省略它会选到保留的上游 west.yml。

west 官方不支持工作区根同时作为 Git 仓库；即使某个版本暂时能运行，也不作为本项目发布约定。[官方布局说明](https://docs.zephyrproject.org/latest/develop/west/workspaces.html)

现有本机克隆保留原源码目录，仅在父目录登记 .west。新机器建议先建专门的 workspace 再 clone，以免多个无关仓库共用父目录；本工作区只有当前 manifest，没有额外项目获取。若父目录已有别的 west 工作区，应另外选择空工作区克隆，不覆盖它。

## 平时如何使用

```bash
python scripts/project_env.py exec west boards
python scripts/project_env.py build
python scripts/project_env.py exec west build -b uyup_rpi_a/hc32f4a0pitb -d build/west-bringup samples/bringup
python scripts/project_env.py exec python scripts/verify_hc32_image.py --build-dir build/west-bringup
```

日常固件优先用 project_env.py build：它沿用项目的 CMake/Ninja 流程，构建后自动审计 HC32 ELF 和源码来源。west build 是理解扩展命令的构建实验，输出独立目录；上面最后一条命令显式补做项目审计。应用把源码根写入 CMake 缓存，两种构建路径都能验证同一个来源。构建命令后参数 `--` 再传 CMake 变量，换板或换关键配置时使用新的构建目录或 `-p always`。

`project_env.py` 固定本仓库 Python、Zephyr 源码、两个受控模块和本机 SDK。激活 .venv 只改变 Python 命令搜索路径，不会自动完成这些工程配置。因此主线命令保留这层入口。

## 更新源码与发布给别人

当前 `west update` 不下载额外项目，也不会替你更新 manifest 仓库自身。更新本工程用 Git；变更前保留自己的修改，再选择合适的拉取或合并方式。干净分支可使用 `git pull --ff-only`。依赖文件变动后重新执行 setup_environment.py，SDK 基线变动后安装相应 SDK 并重新登记。

不要将根目录上游 west.yml 切成活动清单来“补工具”：它描述更广的 Zephyr 模块集合，不能安装 CMake、系统 Python 或 SDK。本项目源码基线以 [dependencies.lock.json](../../dependencies.lock.json) 为准。

新 GitHub 仓库的提交范围、其他人的完整克隆步骤，以及以后拆成多仓库时要改什么，见[发布与重建](../distribution.md)。教学工作区仍在 build/learning-tools/west 内，清单和历史独立，不覆盖本工程 .west。

[工程入口](../README.md) · [学习中心](../../learning/README.md)
