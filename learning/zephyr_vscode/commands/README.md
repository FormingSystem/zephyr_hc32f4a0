---
id: zephyr-vscode-commands
title: Zephyr IDE 可复制操作索引
kind: reference
status: maintained
domains: [zephyr, vscode, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 可复制操作

与 [正文](../P001_VSCode_Zephyr_IDE接入已有工程_Windows.md) 配合使用。TXT 中是 Windows UCRT64 Bash 命令，JSON 是编辑器配置内容；二者不能混贴。

| 文件 | 对应正文 | 用法与影响 |
| --- | --- | --- |
| [01-check-environment.txt](01-check-environment.txt) | 1.2 | 只读核对 Python、west、SDK 和工作区 |
| [02-launch-vscode.txt](02-launch-vscode.txt) | 1.12 | 可选诊断：激活已有 venv 并从终端启动 VS Code；主线无需执行 |
| [03-settings.json](03-settings.json) | 1.5 | 合并到 G 盘源码根的 `.vscode/settings.json` |
| [04-zephyr-ide.example.json](04-zephyr-ide.example.json) | 1.9 | 插件项目结构示例，核对后合并，不覆盖已有项目 |
| [05-build-cli.txt](05-build-cli.txt) | 1.10 | 等价命令行构建；写入本章独立 build 目录 |
| [06-cpp-settings.json](06-cpp-settings.json) | 1.11 | 构建成功后合并到 settings.json，指定编译数据库 |
| [07-create-app.txt](07-create-app.txt) | 1.13 | 目标不存在时复制官方示例为练习应用 |
| [08-settings-existing.json](08-settings-existing.json) | 1.5.1 | 在用户原有设置上合并环境路径的完整示例 |
| [09-settings-after-build.json](09-settings-after-build.json) | 1.11 | 首次构建成功后，替换编译数据库路径的完整示例 |
| [10-local-cmsis-project.json](10-local-cmsis-project.json) | 行动指南 1.4 | 完整结构参考；新增 ide-local-cmsis，保留用户原有字段 |
| [11-local-cmsis-build.txt](11-local-cmsis-build.txt) | 行动指南 1.6 | 等价诊断构建，只使用现有 CMSIS 6，不下载 |
| [12_gui_verified_settings.json](12_gui_verified_settings.json) | 实机截图 1.3 | 本次 GUI 编译成功后的设置副本；核对现有设置后合并 |
| [13_gui_verified_project.json](13_gui_verified_project.json) | 实机截图 1.8 | 本次实际 Build 配置；含已验证的 PowerShell 参数引号和独立输出目录 |

`03` 与 `06` 是同一个设置文件的不同阶段内容，不要直接顺次覆盖文件。`04` 的应用路径与输出路径以 VS Code 打开的 G 盘 `zephyr-main` 为基准。界面步骤和每段操作的预期结果均在正文。


`08` 与 `03` 是两种编辑参照，按原文件内容选择；`09` 是构建后的状态示例。三个文件都不应直接覆盖后来新增的自定义设置。
