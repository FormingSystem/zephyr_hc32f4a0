<!-- SPDX-License-Identifier: Apache-2.0 -->

# 本项目的 Python 环境

每个克隆使用根目录 `.venv`。不跟随共享工程的虚拟环境，也不把环境目录放进 Git；跟随仓库的是依赖描述和创建脚本。专题机制与单元实验见 [venv 大纲](../../../learning/python/venv/大纲.md)。

第一次接触环境隔离，从 [venv 第一章](../../../learning/python/venv/P01_创建并认识虚拟环境.md)顺序阅读。实验与解释都在对应章节内，材料原件集中保存；练习使用 build/learning-tools/venv-textbook，不修改本项目根 .venv。

## 安装入口与依赖来源

[requirements-dev.txt](../../../requirements-dev.txt) 汇总当前 Zephyr 基础、构建测试、运行测试依赖和 [requirements-tools.txt](../../../requirements-tools.txt)。后者固定 west 1.5.0、pyOCD 0.45.1。源码及 SDK 版本见 [dependencies.lock.json](../../../dependencies.lock.json)。

在根目录 UCRT64 Bash 中执行；SDK 已登记时可省略 --sdk：

```bash
read -r -p "请输入已安装的 SDK 目录: " SDK_DIR
py -3.12 scripts/setup_environment.py --sdk "$SDK_DIR"
source .venv/Scripts/activate
python -c "import sys; print(sys.executable)"
python -m pip check
python scripts/project_env.py doctor
```

解释器应位于当前根目录 .venv/Scripts。Windows Python 创建的是 Scripts 布局，即使使用 Bash 也如此。Linux 使用 .venv/bin 和合适的 python3；本轮实际验证为 Windows Python 3.12。

## 环境与工具链是两层

激活只切换 Python 包和命令搜索路径。`project_env.py` 再为本条工程命令固定 SDK、Zephyr 和受控模块。完整工具安装、源码选择与故障定位见[环境说明](../../environment.md)。

`learning/requirements-tools.txt` 只供通用教学，不是完整固件构建依赖；实验环境也不能覆盖根 .venv。

## 更新与迁移

依赖变更后重新运行 setup_environment.py，它复用已有环境并安装声明的版本；然后执行 pip check、project_env.py doctor/check。虚拟环境搬家后应重建，SDK 的个人位置仅保存在忽略的 .local 中。新 GitHub 克隆步骤见[发布与重建](../../distribution.md)。

[工程入口](../../README.md) · [学习中心](../../../learning/README.md)
