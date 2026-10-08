---
id: zephyr-vscode-existing-environment-action-guide
title: 已有环境直接构建的行动指南
kind: engineering
status: evolving
domains: [zephyr, vscode, cmake, west]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_已有环境直接构建的行动指南

2026-10-08 补充：[实机重置与重新导入截图](RESET_WALKTHROUGH.md) 已实际点击 Build 成功；[全部配置参考](CONFIGURATION_REFERENCE.md) 逐项说明设置与其他管理入口。下文对空 buildConfigs 的描述保留为此前问题的诊断起点，当前已创建 `build/ide-reset-mps2`。

本文从“源码、SDK、Python、必要模块已经在磁盘上”开始，处理 IDE for Zephyr 导入后仍提示环境未准备好、要求 west update、找不到 CMSIS 等问题。目标是让现有工具完成一次明确的构建，不重做环境安装。首次接入的逐屏步骤见 [完整教程](P001_VSCode_Zephyr_IDE接入已有工程_Windows.md)。

适用基线：Windows、本机 Mylonics IDE for Zephyr 4.1.1、G 盘 Zephyr 4.5.0-rc1。资料在 F 盘；VS Code 打开 `G:/zephyr_practice/zephyr-main`。应用使用官方原有的 `samples/hello_world`，板使用 `mps2/an386`，不要求连接硬件。这个结果不代表 HC32 板级移植完成。

## 1.1\_先判断卡在哪一步

**环境已经装好，与插件已经正确记录这个环境，是两个条件。** 不要看到 setup 或 update 就重新安装。先按屏幕上的实际内容选一行：

| 当前现象 | 它说明什么 | 现在做什么 |
| --- | --- | --- |
| 终端任务标题是 `west update`，有 fetching、Counting objects | 当前在同步源码仓库，还没编译应用 | 停止不需要的更新任务，进入 1.3 恢复插件状态 |
| 提示先运行 West Update，连 CMake 输出都没有 | 插件准备状态挡住了构建入口 | 核对环境扫描，然后 Skip West Setup |
| 提示 `Zephyr environment configured`，左侧仍 Not Updated | 扫描成功，但可见状态不一致 | Skip West Setup；必要时保存文件后 Reload Window |
| 左下角 `Build None`，应用下只有 Add Build | 应用已登记，还没创建或选中构建配置 | 按 1.4 打开实际 JSON 并新增 Build |
| 已出现 CMake、Board、SDK 等日志后报错 | 构建工具已运行，开始定位具体输入 | 按 1.6 核对路径和第一条错误 |
| 构建成功，但编辑器标红 CONFIG 宏 | 语言服务可能还没拿到本次构建参数 | 按 1.7 配置编译数据库 |

用户截图中的更新进程已经失败退出，就不用再停止一次。旧通知可以关闭。若另一条更新任务仍在运行，在“终端 → 终止任务”里只终止对应 West Update 任务，避免它完成或失败时再次改写插件状态。

## 1.2\_谁负责环境、源码和构建

你安装的是 **Mylonics 发布的第三方 IDE for Zephyr**，扩展 ID 为 `mylonics.zephyr-ide`；Zephyr 官方提供的 west 与构建系统是它调用的工具。插件的状态提示不等同于构建工具的诊断。[Mylonics 工具说明](https://mylonics.com/tools/)

下面按真正的调用顺序理解：点击 Build 后，插件先检查自己保存的环境状态，再取活动 Project/Build，形成 `west build` 命令。west 调用 CMake；CMake 在同一进程内加载应用和 Zephyr 脚本，生成 Ninja 构建文件；Ninja 再调用编译器。

| 输入 | 写入或选择的位置 | 读取者及作用 |
| --- | --- | --- |
| 已有 Python venv | `.vscode/settings.json` 的 `zephyr-ide.venvFolder` | 插件选择构建脚本使用的 Python 环境 |
| 已有 SDK 搜索目录 | 同文件的 `zephyr-ide.toolchainDirectory` | 插件扫描其下 SDK 安装，并向任务提供环境 |
| west 根、Zephyr 源码及准备状态 | 外部目录登记、已有环境扫描、Skip West Setup | 插件自己的安装记录，决定环境和按钮是否可用 |
| 应用、板、输出目录 | `.vscode/zephyr-ide.json` 的 Project / Build | 插件生成构建命令 |
| 本次使用哪些模块目录 | Build 的 `westBuildCMakeArgs` 中的 `ZEPHYR_MODULES` | Zephyr 的 CMake 模块发现逻辑 |
| 下载哪些仓库与版本 | `west.yml` 和 `.west/config` 的过滤设置 | west update；不是 CMake 自动求解的应用依赖 |
| 当前编译宏、头文件与编译器 | 工具生成的 `compile_commands.json` | C/C++ 语言服务 |

这些配置会保留在各自文件或插件记录中，直到你修改或删除。CMake 还把配置结果缓存到输出目录；改输入后不能只看旧缓存。临时终端的 activate/export 只影响当前进程及其子进程，不会自动改写其他已经打开的终端。

## 1.3\_恢复已有环境，不启动下载

**位置：正常从桌面启动的 VS Code，打开 G 盘源码根。** 不必先启动 UCRT64。先通过 `Ctrl+P` 打开 `.vscode/settings.json`，核对已有两项；如果已经正确，不用重写其他设置：

```json
{
  "zephyr-ide.venvFolder": "G:/zephyr_practice/zephyr-main/.venv",
  "zephyr-ide.toolchainDirectory": "G:/zephyr_practice"
}
```

这是最小字段示意，合并到原有对象中。venvFolder 填 venv 根，SDK 设置填 SDK 的父目录。不要在 settings.json 顶层写 `ZEPHYR_SDK_INSTALL_DIR` 或 `westUpdated`，它们不是这两个用途的 VS Code 设置。

1. 左侧已有 `zephyr_practice` 工作区时，使用现有登记。若没有活动环境，执行 `Zephyr IDE: Select Existing West Workspace`，选择 `G:/zephyr_practice`。完全没有登记才按完整教程 1.6 添加外部目录，选 Mark workspace as already set up。
2. 按 `Ctrl+Shift+P`，执行 `Zephyr IDE: Configure Existing Environment (Scan Zephyr Dir/Version)`。成功提示中的源码必须是 `G:/zephyr_practice/zephyr-main`。它读取已有 venv、运行 west list、读取 VERSION，不执行下载。
3. **已经出现上述成功提示，就不用反复扫描。** 若左侧仍为 Not Updated，执行 `Zephyr IDE: Skip West Setup`。本机实现只把活动环境的 `westUpdated` 设为 true 并保存，不运行 west update 或 pip。
4. 若状态仍未刷新，先保存编辑文件，再执行 `Developer: Reload Window`。重新核对活动环境。不要点击左侧 West Update 那一行来“刷新”；它绑定的动作就是执行更新。

这一步完成后，预期左侧为 Updated；即使名称叫 Updated，也只表示插件保存的状态，不证明所有模块都曾下载。真实依赖以构建结果为准。

为什么更新失败后会更乱？4.1.1 的更新入口先把 `westUpdated` 清成 false，并清空已识别的 Zephyr 路径，再运行更新命令。网络失败后，它可能留下“未更新且源码路径丢失”的记录。恢复顺序应为扫描实际路径，再处理准备标记。仅 Skip 不会帮你修复丢失的源码路径；仅有模块目录也不会自动消除插件状态门槛。

若扫描只找到 Python、没有找到 Zephyr，停止这里的跳过流程，先检查登记的是包含 `.west/config` 的父目录，且 `[manifest]` 中 `path = zephyr-main`、`file = west.yml`。若 west list 报具体清单或导入错误，针对那份清单修复；不把“跳过状态”当作缺失依赖的替代品。[扫描与跳过命令](https://zephyr-ide.mylonics.com/reference/commands/)

## 1.4\_打开真实文件，再创建缺少的Build

**先认准磁盘上的文件。** 本机刚读取到的插件文件是：

```text
G:\zephyr_practice\zephyr-main\.vscode\zephyr-ide.json
```

在 VS Code 按 Ctrl+P，粘贴上面的完整路径并回车。或者在 Windows 资源管理器地址栏进入 `G:\zephyr_practice\zephyr-main\.vscode`，打开 zephyr-ide.json。不要进入 samples/hello_world 寻找这个文件，也不要创建名为 projects、buildConfigs 或 ide-mps2 的文件夹。

之前写的 `projects → hello_world → buildConfigs → ide-mps2` 是 JSON 内的键层级，不是磁盘路径。**ide-mps2 是教程建议创建的名字，不是官方自带的配置。** 本机当前实际文件里，hello_world 已存在，但内容仍是 `"buildConfigs": {}`。因此旧教程要求查找 ide-mps2 对象的前提尚未满足。

这次给出直接编辑文件的操作，避免先在多个面板里寻找入口。前提是当前这个 Build 列表确实为空。按 Ctrl+F 搜索 `"buildConfigs"`，确认它属于 hello_world，然后把这一项：

```json
"buildConfigs": {}
```

替换为下面完整字段。**只替换这个字段，保留原文件前面的 toolchains、runnerProfiles 和后面的 twisterConfigs、confFiles。** 原字段后若有逗号，也保留；示例本身省略了与相邻字段连接的逗号。

```json
"buildConfigs": {
  "ide-local-cmsis": {
    "name": "ide-local-cmsis",
    "relPath": "build/learning-tools/zephyr-vscode/ide-local-cmsis",
    "board": "mps2/an386",
    "westBuildArgs": [],
    "westBuildCMakeArgs": [
      "-DZEPHYR_MODULES=G:/zephyr_practice/modules/hal/cmsis_6",
      "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"
    ],
    "confFiles": {
      "config": [],
      "overlay": []
    }
  }
}
```

这里的 ide-local-cmsis 是本次新建的 Build 名，你保存之前它并不存在。如果 buildConfigs 后来已经有其他内容，则把新对象作为其中并列的一项合并，不覆盖现有 Build。完整项目结构参考 [10-local-cmsis-project.json](commands/10-local-cmsis-project.json)，同样不要求整文件覆盖。

按 Ctrl+S 保存，确认没有 JSON 语法错误。观察插件 hello_world 下是否出现 ide-local-cmsis；必要时保存文件后 Reload Window。运行 `Zephyr IDE: Set Active Project` 选择 hello_world，再运行 `Zephyr IDE: Set Active Build` 选择 ide-local-cmsis，底部应不再是 Build None。

如果根本没有 hello_world 项目，先 Add Project 选择 `G:/zephyr_practice/zephyr-main/samples/hello_world`，再回到这个文件。文件存在却没有新 Build 时，先检查保存位置和 JSON 语法，不要再装环境。

你截图中的 `samples/hello_world/CMakeUserPresets.json` 是另一种配置：由 CMake 的 preset 入口读取。它不会自动变成这个插件的 Build 条目。Zephyr IDE 当前这条构建入口读取 zephyr-ide.json；两份文件名称和存放位置不同，不要把上面的字段粘入 CMakeUserPresets.json。原有 preset 中的路径也需要独立核对，本指南没有改写或执行它。

## 1.5\_明确使用现有CMSIS，区分路径和下载需求

本机 `G:/zephyr_practice/modules/hal/cmsis_6` 是已有的 Zephyr 配套 CMSIS 6 模块，包含 `zephyr/module.yml`；当前官方 west.yml 指定修订为 `1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8`。不要为了本步骤重新下载。CMSIS-Core、CMSIS-DSP、CMSIS-NN、厂商设备头与 HAL 用途不同，名字相似不代表都需要。

上一节已经把模块路径写进新 Build 的 westBuildCMakeArgs，这里解释它为什么生效，不需要再粘贴第二份对象。应用的 relPath 是 samples/hello_world，Build 的 relPath 是生成文件目录；它们都从 VS Code 打开的源码根计算。

`ZEPHYR_MODULES` 是 **本次构建的完整显式模块列表**，会替代默认通过 west 得到的模块列表。本次 hello_world/mps2-an386 已用单独 CMSIS 6 验证；它不是任意应用的通用依赖列表。以后增加真正需要的模块，把其根目录用分号追加到同一个参数字符串，保留完整引号。CMSIS 自己的 module.yml 由模块提供，不需要读者自建。

调用过程是：应用 `find_package(Zephyr ...)` 加载 Zephyr 配置；`cmake/modules/zephyr_module.cmake` 读取 ZEPHYR_MODULES，调用 `scripts/zephyr_module.py` 检查模块描述；生成 `zephyr_modules.txt` 等记录；模块名 cmsis_6 再关联源码中原有的 `modules/cmsis_6/CMakeLists.txt`，把 CMSIS Core 头文件加入构建。`cmake-ext: true` 表示构建入口由 Zephyr 侧提供，不能拿一个任意 CMSIS 包随便替换。

如果想保留自动发现的其他模块、只追加或替换同名模块，改用 `EXTRA_ZEPHYR_MODULES`。本次先使用一种明确的选择方式，不同时混配两个列表。取消显式列表时移除对应 -D 参数，并对确认无源码的输出目录重新配置，例如 Build Pristine；只删除 JSON 字段不保证旧 CMakeCache 已失效。[官方模块规则](https://docs.zephyrproject.org/latest/develop/modules.html)

同文件顶层 `toolchains` 对本例可保留 `arm-zephyr-eabi`；它控制插件的目标工具链需求，**不控制 west 下载 CMSIS/HAL**。如果其他应用需要别的架构，保留其实际条目。已装 SDK 的其他架构无需删除。

## 1.6\_点击Build，并按实际阶段排错

**位置：VS Code。** 确认活动 Project 为 hello_world、Build 为 ide-local-cmsis，然后执行 `Zephyr IDE: Build`。第一轮会执行配置、代码生成、编译和链接，耗时比增量构建长；这是本地工作。看到 git fetch/pip install 则属于另外的安装或更新流程，不是这条构建的必需动作。

| 日志或生成记录 | 本次应该看到什么 |
| --- | --- |
| Application | G 盘源码下 samples/hello_world |
| Board | mps2，qualifiers 为 an386 |
| Python | 现有 .venv/Scripts/python.exe |
| SDK / compiler | zephyr-sdk-1.0.1 与其 gnu/arm-zephyr-eabi 工具链 |
| 输出目录 | build/learning-tools/zephyr-vscode/ide-local-cmsis |
| 输出根的 zephyr_modules.txt | cmsis_6 指向现有 G 盘模块 |
| 最终结果 | 本次任务成功退出，生成新的 zephyr/zephyr.elf |

“无法自识别”必须落到一个具体输入。Windows PATH 找 CMake/Ninja/DTC；插件设置找 Python 与 SDK；清单找源码；ZEPHYR_MODULES 找 CMSIS；BOARD 选择板。它们没有一个共享的“自动识别成功”开关。

| 具体故障 | 修正位置，避免重复安装 |
| --- | --- |
| CMake/Ninja 命令不存在 | 看插件新建终端的 PATH；已有 Windows 工具目录加入 PATH 后重开 VS Code。只在 UCRT64 profile 中配置的 PATH 不会自然出现在桌面启动的进程里 |
| Python 包缺失 | 检查日志的解释器是否来自指定 venv；确认后只补缺的包 |
| 找不到板 | 检查识别的源码路径、board.yml 和选择值；模块参数不会自动生成板级适配 |
| HAS_CMSIS_CORE 不满足、模块未找到 | 检查完整 -D 参数是否到达 CMake，以及模块根和 module.yml；先排路径，不先下载全部模块 |
| `Ignoring extra path`，缓存中模块路径只剩 `G:` | 参数被 shell 拆开。命令行必须把整个 `-D名称=路径` 作为一个带引号的参数传入；JSON 中每项本身就是一个字符串 |
| 改路径仍读到旧目录 | 查看 CMakeCache，修正配置输入，对专用输出做 Pristine 或使用新 Build 目录 |
| 只有 Ccache 未找到 | 它是可选编译缓存工具；后面继续配置和编译时，不据此判定 SDK 不可用 |

不要把 `.vscode/settings.json` 的路径改正确，就认为一个已经运行的终端或旧构建目录自动更新了。核对实际日志才能确定输入生效。

如果 IDE 仍失败，可以执行 [11-local-cmsis-build.txt](commands/11-local-cmsis-build.txt) 的等价命令，对照同一应用、板和模块。完整命令也列在下面。该文件注明 Windows UCRT64 Bash，仅用于排错，不要求日常从 UCRT64 启动 VS Code。它写入独立的 `action-guide-cli` 输出，不触碰 IDE 构建目录。命令行通过只能证明该调用环境可构建，不能冒充 IDE 按钮已验证。

```bash
# 终端：Windows UCRT64 Bash；前提：已有 venv、SDK、CMSIS 6。
# 用于 IDE 失败时对照；无需用这个终端启动 VS Code。
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
export ZEPHYR_BASE='G:/zephyr_practice/zephyr-main'
export ZEPHYR_SDK_INSTALL_DIR='G:/zephyr_practice/zephyr-sdk-1.0.1'
west build -b mps2/an386 samples/hello_world \
  -d build/learning-tools/zephyr-vscode/action-guide-cli \
  -- '-DZEPHYR_MODULES=G:/zephyr_practice/modules/hal/cmsis_6' \
  '-DCMAKE_EXPORT_COMPILE_COMMANDS=ON'
```

## 1.7\_构建成功后再处理编辑器标红

打开 `.vscode/settings.json`，找到已有 `C_Cpp.default.compileCommands`，替换其值，不增加重复字段：

```json
"C_Cpp.default.compileCommands": "${workspaceFolder}/build/learning-tools/zephyr-vscode/ide-local-cmsis/compile_commands.json"
```

这个设置供 Microsoft C/C++ 使用。若选用 clangd，应按其配置方法设置，避免同时启用两套语义分析。运行 `C/C++: Log Diagnostics` 核对数据库，然后打开 main.c 观察。CONFIG_BOARD_TARGET 等宏来自构建生成的配置，编辑器未读到数据库时会标红；不要为消除红线在 main.c 手写这些宏。

切换 Build 时也检查数据库路径。下次正常打开同一个源码根、选同一环境和 Build，修改 C 文件后直接 Build。普通源文件修改不需要 west update、重新扫描、重建 venv 或 Pristine。

## 1.8\_确实需要更新依赖时才控制下载范围

west update 根据活动清单同步仓库，不先解析应用的 Kconfig/CMake 来推导最小下载集合。官方默认清单覆盖大量板和功能，所以它的默认更新范围远大于本例。CMake 能按输入构建应用，但不能从一个 CMakeLists.txt 唯一推断用户要选择的板、SDK、Python 和输出目录。[west 的工作方式](https://docs.zephyrproject.org/latest/develop/west/basics.html)

已有必要模块时，到 1.7 就结束。以后确实需要补齐某一项，可在已激活 venv 的终端使用带项目名的更新，例如 `west update cmsis_6`。它会同步到清单指定修订，也可能影响现有检出；不要把它当作只读检查。

如果希望以后普通更新排除 DSP 与 NN，可按下面的 **可选维护操作** 处理。先读现值；已有过滤规则时合并修改，不能覆盖其他项目所需规则。过滤在整个 west 工作区生效，不只影响一个 Build。

```bash
# 终端：Windows UCRT64 Bash；前提：已有本章 venv 与 west 工作区。
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
west config --local manifest.project-filter
```

尚未设置时查询可能没有输出并返回非零，这不代表环境坏了。确认本工作区不需要 DSP/NN，且没有需保留的原规则时，才写：

```bash
# 终端：Windows UCRT64 Bash；写入整个 west 工作区的本地过滤设置。
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
west config --local manifest.project-filter -- '-cmsis-dsp,-cmsis-nn'
west config --local manifest.project-filter
```

此命令只改 `.west/config`，不会立即下载或删除文件。之后默认 west update 和自动模块发现会受到项目活动状态影响；显式指定项目的操作另按 west 规则处理。恢复时写回原值；原先没有此配置，才用 `west config --local -d manifest.project-filter` 删除本地项。这里不附带执行全量更新。[官方过滤说明](https://docs.zephyrproject.org/latest/develop/west/manifest.html#active-and-inactive-projects)

`westNarrowUpdate` 减少获取的 Git 历史，并不筛选应用模块。Kconfig 关闭某功能控制编译，不等于下载过滤。`ZEPHYR_MODULES` 固定构建模块，不会阻止另一个 West Update 任务。以后扩展应用时，要分别维护所需依赖和构建配置。

## 1.9\_证据与验证范围

插件依据为本机 `mylonics.zephyr-ide-4.1.1/package.json` 和 `dist/extension.js`：`configure-existing-environment` 发现环境并设置标记；`mark-west-as-ready` 实现 Skip West Setup；`kc` 的构建入口检查 westUpdated；`nP` 更新前清除状态。界面仍显示旧状态有多种可能，单张截图不能确认是刷新缺陷还是另一任务覆盖了状态。

Zephyr 依据为 G 盘源码的 `west.yml`、`cmake/modules/zephyr_module.cmake`、`scripts/zephyr_module.py`、`modules/cmsis_6/CMakeLists.txt`，对应官方文档源码 `doc/develop/modules.rst`、`doc/develop/west/basics.rst`。在线 latest 文档可能继续变化，以本章本机版本和实际输出为边界。

本轮构建和资料检查结果记录在 [VALIDATION](VALIDATION.md)。行动指南提供配置样例，未替读者覆盖 G 盘 `.vscode` 文件或修改 west 过滤配置。插件按钮、F12、烧录和调试的验证状态单独列出，不与命令行验证混算。
