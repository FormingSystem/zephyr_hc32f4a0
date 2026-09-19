<!-- SPDX-License-Identifier: Apache-2.0 -->

# 当前工程的源码与工具环境

本文记录工程实际入口；工具本身的机制见 [learning](../learning/README.md)。所有命令从仓库根目录的 UCRT64 Bash 执行。源码基线见 [dependencies.lock.json](../dependencies.lock.json)。

## 哪些东西由谁提供

| 层 | 当前来源 | 如何选择与验证 |
| --- | --- | --- |
| Zephyr 内核、构建系统、板卡、驱动 | 本仓库受控源码 | project.py 检查根目录与编译数据库 |
| CMSIS_6、华大 HAL | modules/hal 下受控快照 | lock 记录来源；应用与入口限定模块集合 |
| Python 构建/测试包 | 本仓库 .venv | requirements-dev.txt 汇总依赖；pip check |
| west / pyOCD | .venv 中安装 | requirements-tools.txt 固定 1.5.0 / 0.45.1 |
| ARM 编译器、SDK QEMU | 外部 Zephyr SDK 1.0.1 | .local/environment.json 登记；doctor 核对 |
| Git、CMake、Ninja、dtc、gperf | 主机安装 | doctor 查可执行文件与版本 |
| 主机 C 实验的 GCC/GDB | MSYS2 UCRT64 | gcc --version、gdb --version |
| VS Code 插件 | 编辑器安装 | 工作区推荐扩展；不代替编译器 |

`requirements-dev.txt` 引入 Zephyr 的 base、build-test、run-test 依赖以及项目工具依赖。上游若声明版本范围，安装结果可能随时间变化；它不是所有平台通用的完整传递依赖锁。

## 第一次安装与日常进入

先安装 Windows Python 3.12、Git for Windows、CMake、Ninja、dtc、gperf 与 lock 指定的 SDK ARM 工具链及 QEMU。系统工具安装参考[官方准备说明](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)，SDK 取自[官方发布](https://github.com/zephyrproject-rtos/sdk-ng/releases)；选择本项目版本，按对应平台包安装。不要重复照抄上游源码下载流程。

UCRT64 提供 Bash，工程 Python 使用 Windows Python。主机 C 实验另需 UCRT64 GCC/GDB，可在 UCRT64 终端按需安装：

```bash
pacman -S --needed mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-gdb
```

已安装 SDK 后执行：

```bash
read -r -p "请输入已安装的 SDK 目录: " SDK_DIR
py -3.12 scripts/setup_environment.py --sdk "$SDK_DIR"
source .venv/Scripts/activate
python scripts/configure_west.py
python scripts/project_env.py doctor
python scripts/project_env.py check
python scripts/project_env.py build
python scripts/project_env.py test
```

可以输入自己机器的 SDK 路径；不要把示例作者的路径抄进仓库。setup 不下载 SDK、不修改全局 Python，不自动改 Git 配置。它创建或复用根目录 .venv、安装依赖、执行 pip check，将 SDK 路径和编辑器本机设置写入被忽略的 .local、.vscode。项目 Git 钩子初始化是独立的 `python scripts/git_setup.py`。

以后每次新终端只需：

```bash
source .venv/Scripts/activate
python scripts/project_env.py doctor
python scripts/project_env.py build
```

也可不激活，直接使用 `.venv/Scripts/python.exe scripts/project_env.py build`。Linux 使用满足版本要求的 python3 创建环境，解释器与激活路径分别换成 .venv/bin/python、.venv/bin/activate；Linux/macOS 分支尚未在本轮实测。

## 入口究竟配置了什么

[setup_environment.py](../scripts/setup_environment.py) 管安装；[project_env.py](../scripts/project_env.py) 管每条命令运行时的环境；[project.py](../scripts/project.py) 管工程动作。后者通过 exec 入口也可包装 CMake、west、Twister、课程脚本。

project_env.py 总是定位当前克隆的 .venv，SDK 优先读 .local 配置，再读 ZEPHYR_SDK_INSTALL_DIR。它设置 ZEPHYR_BASE、ZEPHYR_MODULES、ZEPHYR_TOOLCHAIN_VARIANT，清除会串入其他工程的 PYTHONPATH 和额外模块环境变量。Windows 下补充已安装的用户/系统 PATH，并优先使用 Git for Windows，避免 MSYS Git 路径输出与 Windows Python 混用。

应用 [samples/bringup/CMakeLists.txt](../samples/bringup/CMakeLists.txt) 也明确绑定当前源码与模块。新增模块按 [CMake P02](../learning/cmake/P02_接入Zephyr模块.md) 在应用声明，不依赖终端里遗留的环境变量。

## 迁移、重建和故障

.venv 不可作为可搬运工具包；换电脑或移动克隆后，保留依赖文件，重新创建环境并安装。先退出旧环境，把旧 .venv 移到自己确认的备份位置，再运行 setup；不要删除未核对的目录。已有 .local SDK 路径有效时可省略 --sdk。

`python -m pip check` 查包依赖一致性；doctor 查工程环境；check 查工具逻辑与离线调试配置；build 查 HC32 编译；test 查 QEMU 软件运行。它们是不同证据，最后两项也不能证明真实 PCB 正确。

若 .venv 缺失，入口明确失败，不借用相邻工程的环境。若 SDK 版本不符，安装正确版本后重新 --sdk。若 VS Code 记住其他 Python，在 Python: Select Interpreter 中选择本仓库 .venv。带注释的既有 settings.json 不被 setup 自动重写，按提示手工选择解释器与工具链路径。

原 PowerShell 入口保留兼容；新机器主线使用上述 Bash + Python。发布时提交哪些配置见[发布说明](distribution.md)。
