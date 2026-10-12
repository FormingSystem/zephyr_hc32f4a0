---
id: zephyr-vscode-existing-environment-action-guide
title: Zephyr IDE 按结果定位的行动指南
kind: engineering
status: maintained
domains: [zephyr, vscode, cmake, west]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_从当前结果找到下一步

本页用于已经打开工程后的排错。首次接入按 [主教程](P001_VSCode_Zephyr_IDE接入已有工程_Windows.md)；设置和按钮找不到时先看 [入口地图](RESET_WALKTHROUGH.md)。主线固定为 VS Code 打开 `G:/zephyr_practice/zephyr-main`，west 根为 `G:/zephyr_practice`。本文不再另建 ide-local-cmsis 或 ide-reset-mps2 路线。

## 1.1\_先确定失败发生在哪一层

| 当前可见结果 | 下一步检查 | 正确结果 |
| --- | --- | --- |
| 设置页找不到 Add Project/Add Build | 打开命令面板，搜索 Zephyr IDE 对应动作 | 进入添加应用/构建向导；这不是设置项 |
| 环境路径已填写，Projects 仍为空 | 先核对扫描，再 Add Project 选择应用目录 | 出现 hello_world；不是导入每个内核/驱动目录 |
| Build None 或 buildConfigs 为空 | 为活动 hello_world 执行 Add Build Configuration | 创建并选中 ide-mps2 |
| 还没出现 CMake 日志便提示先 West Update | 查看插件登记的源码、venv 与准备标记 | 扫描已识别实际环境；构建可以进入 CMake |
| 终端在 git fetch、Counting objects | 当前是仓库更新任务 | 有意维护依赖才等待；它不是编译日志 |
| 已进入 CMake 后失败 | 看第一条具体错误与本次命令 | 应用、板、Python、SDK、模块路径一致 |
| ELF 已生成但编辑器标红 | 查 C/C++ 读取的编译数据库 | 数据库对应当前 Build 的板和宏 |

## 1.2\_设置路径后，仍需登记和扫描

在 `Preferences: Open Workspace Settings (JSON)` 打开的文件中，核对 `zephyr-ide.venvFolder` 指向已有 `.venv` 根；`zephyr-ide.toolchainDirectory` 指向**直接包含 SDK 安装目录的父目录**。具体 SDK 根需要包含 `sdk_version`，实际解压层级以磁盘为准。不要把旧示例扁平路径直接当成当前实际路径。

已有登记但未激活时，执行 `Zephyr IDE: Select Existing West Workspace`。尚未登记时，按主教程从 `Zephyr IDE: Setup Workspace from External Directory` 选择 `G:/zephyr_practice`，再选 **Mark workspace as already set up**。随后执行 **Zephyr IDE: Configure Existing Environment (Scan Zephyr Dir/Version)**。

扫描应取得 `G:/zephyr_practice/zephyr-main` 与正确 venv。若扫描失败，检查父目录 `.west/config` 的 `manifest.path` 与 `manifest.file`，以及该 venv 中 west 是否可用。成功扫描但准备标记仍不一致时，才核对 `Zephyr IDE: Skip West Setup`；它只设置插件标记，不下载依赖、不证明依赖完整。

修改路径后检查新任务的实际日志。旧终端与旧 CMakeCache 不会因为 JSON 保存自动变为新环境。不要为了刷新状态重复初始化 `.west` 或点击全量 West Update。

## 1.3\_应用目录、Build 名和输出目录是三个值

按 `Ctrl+P` 打开 `G:/zephyr_practice/zephyr-main/.vscode/zephyr-ide.json`。它是插件项目配置，区别于 `.vscode/settings.json` 和应用里的 `CMakeUserPresets.json`。

| 字段 | 主线值 | 含义 |
| --- | --- | --- |
| Project 的 `relPath` | `samples/hello_world` | 应用源文件所在目录 |
| Build 的 `name` 与对象键 | `ide-mps2` | 读者创建的构建标识 |
| Build 的 `board` | `mps2/an386` | west 的板目标 |
| Build 的 `relPath` | `build/learning-tools/zephyr-vscode/hello_world` | 生成文件目录，基于 VS Code 打开的源码根 |
| Build 的 `westBuildArgs` | `[]` | west build 层的额外参数 |
| Build 的 `westBuildCMakeArgs` | 按主教程配置 | `--` 后交给 CMake 的参数 |

如果没有这个 Build，先运行添加向导。不要在磁盘上新建 projects/buildConfigs/ide-mps2 文件夹来补 JSON 对象。已有多组 Build 时核对当前活动项，保留其他配置。

## 1.4\_SDK、CMSIS、自有 HAL 分别检查

SDK 提供目标编译器；CMSIS 是清单管理的源码模块；自有 HAL 是独立模块目录。它们没有一个共同的“选择包”设置。

- 查 west 能管理哪些项目：在当前 west 工作区运行 `west list`；核对 `west.yml` 及其导入清单中的 name、path、revision。目录存在不等于当前清单管理它。
- 下载或同步某个已声明项目：核对本地修改后使用 `west update cmsis_6` 这样的项目名。它是写操作；不需要为一次普通 Build 重复执行。
- 本主线 CMSIS 使用已有 west 自动模块发现。`G:/zephyr_practice/hal_xhsc-zephyr` 是自有 HAL 的主线位置；追加到构建使用 `EXTRA_ZEPHYR_MODULES`，前提是该目录有正确的 `zephyr/module.yml` 与构建接入内容。
- `ZEPHYR_MODULES` 会替换自动发现的完整模块列表。旧 ide-local-cmsis 示例仅是单模块诊断，不再作为默认接入方式；不能据此删掉其他板/功能所需模块。

JSON 参数数组里每项是一个字符串；向导或终端中的输入则是命令行文本。两种地方的引号规则不同，不能把用于 shell 的单引号不加区分地嵌入每个 JSON 数组项。修改后查看最终命令和 CMakeCache；新增或移除模块参数后，对已确认专用输出目录重新配置。

如果 `west update cmsis_6` 报目标修订变成 `^commit` 而不是 `^{commit}`，按 [CMSIS 选择与下载教程](../P01_zephyr_make_project/P004_CMSIS选择与下载_Windows.md) 中的 Windows Python/MSYS2 Git 案例检查 Git 实现和调用路径。先核对提交及实际参数，不用修改清单版本来掩盖参数传递问题。

## 1.5\_点击 Build 后看证据，不只看状态灯

活动应用应为 hello_world、Build 应为 ide-mps2。执行 `Zephyr IDE: Build` 后，从日志核对应用、板、输出、Python 和编译器。输出目录中的 `CMakeCache.txt`、`zephyr_modules.txt`、`zephyr/.config` 与 `zephyr/zephyr.dts` 用于核对这次输入；本次任务成功退出并生成新的 `zephyr/zephyr.elf` 才能说明链接完成。

普通 `.c` 修改使用增量 Build。修改板、SDK、模块路径或 CMake 参数后，按需要使用 Build Pristine；先确认清理的是本章独立输出目录。首次构建只用 Build，烧录和调试另需板级支持、runner 与探针。

构建成功后，C/C++ 的 `C_Cpp.default.compileCommands` 指向 `${workspaceFolder}/build/learning-tools/zephyr-vscode/hello_world/compile_commands.json`。运行 `C/C++: Log Diagnostics` 核对读取路径，再验证符号跳转。不要为消除红线在源码里伪造 CONFIG 宏。

## 1.6\_核验边界

当前说明依据已安装 4.1.1 的命令、配置 Schema 和实现，以及当前文件路径核对。旧截图不能证明 GUI 全流程成功，相关声明已撤回。可独立复核的历史命令行构建记录、当前文档/PPT检查，以及尚未执行的操作分别记录在 [VALIDATION](VALIDATION.md)。
