---
id: zephyr-vscode-index
title: VS Code Zephyr IDE 教程导航
kind: reference
status: maintained
domains: [zephyr, vscode, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# VS Code Zephyr IDE 教程

已经有源码、SDK 和 Python 环境时，从这里把应用接入 **Mylonics IDE for Zephyr**。教程按本机插件 4.1.1 核对，以 G 盘现有环境为实验对象，先完成官方 hello_world 编译，再配置源码跳转。

**需要看实际鼠标操作：先读 [清空后重新导入的实机截图](RESET_WALKTHROUGH.md)。需要查每个选项：读 [全部配置入口逐项截图说明](CONFIGURATION_REFERENCE.md)。** 两篇合计引用 72 张本机截图，覆盖 35 个现行设置、8 个旧兼容键及工程/构建/Runner/Manager 配置。2026-10-08 已实际点击 IDE Build 成功，未运行 west update、pip 或 SDK 安装。

[行动指南](ACTION_GUIDE.md) 保留命令诊断与机制说明；其中“空 buildConfigs”描述此前状态。本次清空后已新增并验证 `build/ide-reset-mps2`，当前状态以实机截图篇为准。

首次接入可读 [完整 Markdown](P001_VSCode_Zephyr_IDE接入已有工程_Windows.md)，按步骤操作；[48 页 PPT](P001_VSCode_Zephyr_IDE接入已有工程_Windows.pptx) 用来讲解与复习。完整命令和配置在 [commands](commands/README.md)，实际验证范围见 [VALIDATION](VALIDATION.md)。

| 你要完成的事情 | Markdown | PPT 页码 |
| --- | --- | --- |
| 分清源码、应用、west 根与工具 | 1.1—1.3 | 2—7 |
| 正常打开、配置路径并登记环境 | 1.4—1.6 | 8—22 |
| 添加应用、板目标和输出目录 | 1.7—1.9 | 23—32 |
| 构建并核对产物 | 1.10 | 33—38 |
| 配置 C/C++ 源码浏览 | 1.11 | 39—40 |
| 日常重开、可选维护与自己的应用 | 1.12—1.13 | 41—45 |
| 排错与完成检查 | 1.14—1.15 | 46—48 |

主线直接从桌面打开 VS Code，配置 JSON 后登记并扫描已有环境，不要求 UCRT64 启动或重装环境。终端继承与依赖更新作为可选分支。

## 文件说明

```text
zephyr_vscode/
  P001_...Windows.md     手把手正文
  P001_...Windows.pptx   48 页可编辑演示文稿
  commands/             Bash 命令与 JSON 配置片段
  assets/               官方界面示意、来源和 Mermaid 图源
  slides/               初始作者源与正式 PPT 原生重建源
  VALIDATION.md         实测结果与未覆盖范围
```

资料目录是 `F:/git_storage/zephyr_hc32f4a0/learning/zephyr_vscode`，实验源码目录是 `G:/zephyr_practice/zephyr-main`。不要在资料目录执行本章构建命令。
