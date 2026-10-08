---
id: zephyr-vscode-validation
title: Zephyr IDE 教程验证记录
kind: reference
status: maintained
domains: [documentation, zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 验证记录

## 2026-10-08：提交前复核

文档检查覆盖 104 篇资料，零错误；暂存的 JSON 可解析、48 页 PPT 包完整，暂存差异检查通过。项目入口 `scripts/project_env.py check` 的 58 项工具测试、pyOCD 离线配置检查和项目差异检查全部通过。首次测试因当前 PowerShell 的 PATH 缺少 Git for Windows 的 sh 而失败；仅为检查进程补入已有 `E:/git/Git/usr/bin` 后重跑通过，没有修改系统 PATH 或测试代码，也没有打开硬件探针。临时 UI 可访问性文本归档到忽略的 `.local/zephyr-ide-publish/ui-text`，不随教程发布。

## 2026-10-08：真实 GUI 清空、接入、编译和配置截图

新增 [实机操作](RESET_WALKTHROUGH.md) 与 [配置参考](CONFIGURATION_REFERENCE.md)，共引用 72 张本机原始截图。现行设置覆盖检查：package.json 共 43 键，35 个现行、8 个废弃，逐键均出现在参考正文。项目 Schema 的工程/Build/Runner/安装声明及 Twister 兼容字段分别说明；没有公开向导的字段未伪造界面。版本、定义及源文件 SHA-256 留在 `assets/reset_demo/configuration-inventory.json`。

已执行：备份旧配置，GUI Unregister、Clear Projects；文件工具清理插件 JSON/相关设置，GUI 保存已有 venv/SDK 设置、外部目录登记、Mark as Complete、Configure Existing Environment；Add Project、Add Build、编辑器修正输出目录和 PowerShell 参数引号；实际点击 Build 完成 136/136。不是所有重置操作都用鼠标，文件操作已在实录明确标注。

结果：BOARD=mps2/an386；已有 SDK 1.0.1 的 arm-zephyr-eabi-gcc.exe；模块仅现有 cmsis_6；输出 `G:/zephyr_practice/zephyr-main/build/learning-tools/zephyr-vscode/ide-reset-demo/zephyr/zephyr.elf`，382892 字节，报告 FLASH 18488 B、RAM 6440 B。Workspace UI 显示 Zephyr 4.5.0。Kconfig Sources 确认默认板 defconfig 与应用 prj.conf；全部为空的额外 conf/overlay 列表没有妨碍默认发现。

临时 demo-auto Runner 仅用于截图，没有绑定活动 Build；修改 Revert 后已通过 UI 删除。Manager 的包/工具链/样例/命令选择器只查看并取消。没有执行 west update、pip/SDK 安装、Kconfig 编辑保存、Twister、SCA、QEMU、Flash、Debug、Attach 或 F12 验证。既有 48 页 PPT 保留，本次新增内容作为 MD 实机图解附录，不宣称已扩入 PPT。

原始备份：`G:/zephyr_practice/zephyr-main/.local/zephyr-ide-reset-20261008`。实际 settings 与项目配置另存为 commands/12、13；项目副本与 G 盘实际配置均通过本机 4.1.1 JSON Schema 检查。所有正文截图链接已核对存在。`learning/check_docs.py` 检查 104 篇资料、35 个章节和 19 个 Python 源文件，零错误；作用范围内 `git diff --check` 通过。

## 2026-10-07：已有环境行动指南与真实配置位置修正

新增 ACTION_GUIDE.md，从现有环境恢复、磁盘文件位置、空 buildConfigs 的完整替换讲到显式 CMSIS 6 构建、日志核对及可选下载过滤。重新读取 G 盘实际 zephyr-ide.json，确认 hello_world 的 buildConfigs 为空；ide-mps2 不是预先存在的配置。明确它是 JSON 键而非文件夹，区别应用内 CMakeUserPresets.json。新增项目结构和 Bash 诊断命令材料，现共 11 份。

本轮普通 PowerShell 使用现有 Python 3.12.10/west 1.5.0、SDK 1.0.1 和显式 ZEPHYR_MODULES=cmsis_6，在 G 盘独立 action-guide-check 输出完成 136 步构建，退出码 0，生成 ELF 与 109 条编译数据库记录。zephyr_modules.txt 只有指定的现有 cmsis_6。首次命令未给完整 -D 参数加引号，PowerShell 将盘符路径拆开导致配置失败；改用整个参数的单引号后在同一专用目录重新配置成功。这一错误与诊断方法写入指南。本轮没有运行 west update 或 pip，没有重建 venv，没有修改 G 盘用户 JSON、preset、插件状态或 west 过滤设置。

JSON 示例通过当前插件 Schema，文中完整字段与样例一致；Bash 诊断命令与正文一致且 bash -n 通过，仅普通 PowerShell 等价命令实际构建。102 篇资料检查零错误。同步修正 48 页 PPT 的状态恢复、真实文件路径及 JSON 层级说明，包结构/字体/几何/回读、PowerPoint 原生渲染通过，零文本溢出，改动页目检，231 部件原生重建一致。

仍未在 VS Code 实际点击配置/Build/F12，也未操作硬件。PPT SHA-256：`bd73e3659f8c5b969011329da64b558f1e1bcb43297e7aa1bb783e30fcbf9603`。中间文件在 `.local/zephyr-ide-action-guide/`。

## 2026-10-07：按第一次导入的点击顺序扩写

PPT 从 36 页扩为 48 页，Markdown 按文件夹核对、正常启动 VS Code、工作区 JSON、外部目录登记、已有环境扫描、Add Project、Add Build、输出目录、构建日志和源码浏览展开。新增现有 settings 的完整合并示例及构建后示例；命令/配置材料共 9 份。补齐 Board Picker 的 Zephyr Directory Only，修正 Open Workspace Config 只打开插件配置面板的说明，JSON 改用资源管理器或 Ctrl+P 直接打开。

本轮重读本机 4.1.1 的向导实现并对照官方命令参考。5 份 JSON 均可解析，项目示例通过当前插件 JSON Schema；4 份命令文本与正文一致。101 篇资料的章节、元信息及本地链接检查零错误。48 页通过包结构、字体、几何和 Artifact Tool 回读检查；PowerPoint 原生渲染全部页面、目检总览及重点页，文本边界零溢出。原生源同步重建后 231 个 ZIP 部件内容逐项一致。

本轮没有重复固件构建，沿用下方已记录的普通 PowerShell 等价构建结果；没有在 VS Code 实际点击扫描、Add Project、Add Build 或 F12，没有改写 G 盘配置和插件记录，也没有硬件操作。三个 Mermaid 图未改变，沿用前轮渲染验证。正式 PPT SHA-256：`a8c28e936f5b3002723b3a71607b825d9a754e9b085c1aee3d540f0f3a44a99f`。本轮中间文件位于忽略目录 `.local/zephyr-ide-walkthrough/`。

## 2026-10-07：改为直接登记已有环境

根据用户反馈，将主线改为正常打开 VS Code、配置已有 venv/SDK 路径、登记 west 根并跳过安装，再执行 `Configure Existing Environment (Scan Zephyr Dir/Version)`。终端继承降为可选诊断；不要求日常从 UCRT64 启动。

本轮重新读取本机已更新的 IDE for Zephyr **4.1.1**：`configure-existing-environment` 命令调用 `Ps` 设置已有 venv 的执行环境、`Ts` 用 west list 和 VERSION 发现源码，再保存安装记录；这条命令没有 pip install、west init 或 west update 调用。外部目录登记的 mark-as-setup 分支不进入普通安装流程。扫描成功不代表检查过所有 Python 依赖。

普通 PowerShell 下，按插件实现将已有 venv Scripts 加入 PATH，并传入识别到的 Zephyr 根与 SDK 父目录，在独立 `build/learning-tools/zephyr-vscode/desktop-check` 目录完成 136 步 hello_world/mps2-an386 构建。使用已有 Python 3.12.10、west 1.5.0、SDK 1.0.1、系统 CMake 4.4.4、WinGet Ninja 与 DTC 1.6.1，没有从 UCRT64 继承 PATH，也没有下载安装。这是插件环境传递方式的等价验证，未在 VS Code 实际点击登记、扫描或构建按钮。

36 页 PPT 重新经过包结构、字体、几何与回读检查；原生渲染零文本溢出，改动页逐页目检。Markdown、图源、备注、命令与原生重建源同步。下方首次交付保留当时 4.1.0 和 UCRT64 验证的历史记录，该轮正式 PPT 摘要为 `0725da8f7a9f55834acbc8fead3ecb8247b2a7382c817de05d429166a1fdec11`。未改写用户 G 盘 JSON 或插件安装记录，未执行硬件操作。

## 首次交付记录

日期：2026-10-07。交付目录为 `F:/git_storage/zephyr_hc32f4a0/learning/zephyr_vscode`，已核对所属 F 盘 Git 根。C 盘同名旧副本未用于修改。

## 本机环境与依据

| 对象 | 本轮读取结果 |
| --- | --- |
| IDE for Zephyr | `mylonics.zephyr-ide` 4.1.0；读取 package.json、配置 schema 和扩展实现 |
| Zephyr | G 盘 `zephyr-main`，4.5.0-rc1；提交 `25c8f4a23988dd3b2cfb463613622738298c2d6c` |
| west 根 | `G:/zephyr_practice`；manifest.path 为 `zephyr-main`，manifest.file 为 `west.yml` |
| Python 与 west | 源码根既有 `.venv`；Python 3.12.10，west 1.5.0 |
| SDK 与 GCC | `G:/zephyr_practice/zephyr-sdk-1.0.1`；ARM GCC 14.3.0 |
| 主机工具 | MSYS2 UCRT64；构建日志中的 CMake 4.4.3、DTC 1.8.1 |

在线文档与本机版本来源列在正文 1.15。界面配图来自插件官方文档，不充当本机操作证据。插件 4.1.0 已核对以下行为：SDK 父目录设置、venv 路径、外部环境读取、Add Project 的应用检查、Build relPath 解析，以及 `.west` 托管分支继续执行 setup 的行为。

## 已完成的验证

- 执行正文 1.10 / `commands/05-build-cli.txt` 的等价构建：官方 `samples/hello_world`、板 `mps2/an386`、G 盘 SDK 和既有 venv，输出目录为 `build/learning-tools/zephyr-vscode/hello_world`。本轮新目录构建完成 136 步，进程退出码为 0。
- 已生成 ELF、CMakeCache、最终 Kconfig、设备树及编译数据库。数据库共 109 条，包含本次 `samples/hello_world/src/main.c`。
- 4 份 Bash 命令与 Markdown 对应代码一致，`bash -n` 通过；3 份 JSON 可解析，项目示例通过当前 4.1.0 的 JSON Schema 验证。
- 正式 PPT 为 36 页、16:9；通过包关系、字体、几何和 Artifact Tool 回读检查。PowerPoint 原生打开并导出全部 36 页，逐页目检并复核调整页；文字边界检测为 0 溢出。
- 保留系列芯片封面、主讲人及母版署名；正文自动页码、连续原生代码区和真实 120% 段落行距已写入 PPT。
- 正式 PPT 已同步原生源并重建；184 个 ZIP 部件逐项内容一致。
- 3 个 Mermaid 图完成浅色/暗色、HTML 标签开关共 12 次渲染。流程图节点最低对比度分别为 10.83 和 10.17；时序图另行目检。图源与正文一致。
- 完成资料元信息、章节编号、本地链接、Python 语法检查；结果由仓库 `learning/check_docs.py` 核对。

## 未覆盖的操作

本轮没有在 VS Code 界面实际点击 Add Project、Add Build 或 Build，也没有实际执行 F12 / C/C++ 诊断。这些步骤依据本机插件定义、实现和官方文档编写，不能把命令行构建通过当作 GUI 全流程实测。

没有运行插件托管 setup、重新安装 SDK、重建 venv、执行 west update、修改用户 G 盘 `.vscode` 配置或创建练习应用；只有构建过程新增本章 G 盘输出目录。未执行 QEMU、Flash、Debug 或 HC32 硬件操作。

验证中间文件保存在仓库忽略目录 `.local/p012-zephyr-ide/`。其中目录名来自制作时的临时编号，正式专题独立编号为 P001。正式 PPT 的最终摘要为 `a07fa9067a55b83662ca8f82841d47e9fc0cf1ec364f57f081b1db6eac25f947`。
