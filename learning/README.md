---
id: learning.readme
title: 学习中心
kind: reference
status: maintained
domains: [documentation]
---

<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 学习中心

这里提供从零准备 Zephyr 环境、理解构建工具并逐步开展实验的 Markdown 笔记、PPT 和配套材料。Windows 主线的实验源码目录为 `G:\zephyr_practice\zephyr-main`，在 UCRT64 Bash 中写作 `/g/zephyr_practice/zephyr-main`。源码下载、依赖安装、编译、调试及后续移植都围绕这份源码展开。实验会逐步加入 HC32 板级支持、厂商模块、构建与调试工具和文档，最终形成能够独立开发和维护的完整工程。每个文件或工具都在对应实验中创建并解释，不要求起步时已经具备最终目录。

环境材料统一目录，文件名后缀区分 [Windows](P01_zephyr_make_project/环境与依赖导航.md)与 [Linux](P01_zephyr_make_project/P001_官方环境安装与源码准备_Linux.md)，先查[官方工具依据](P01_zephyr_make_project/主机工具与官方安装来源.md)。Linux 教程使用 **Ubuntu 22.04 LTS**，按正文补齐工具版本并采用独立的官方工作区示例，不能照搬 Windows 盘符、UCRT64 路径或 venv 布局。PPT 的统一目录和最新文件名见[专题大纲](P01_zephyr_make_project/大纲.md)。

默认使用 UCRT64 Bash，保持 Linux 命令习惯。只有 Zephyr 官方明确采用 PowerShell 的 Windows 下载/安装步骤，以及 setup.cmd 等 Windows 专用脚本和其 Windows 管理操作，才切换到 PowerShell。普通下载、摘要校验、解压、版本检查、Python/venv 与 CMake 工程操作仍用 UCRT64，不能仅因调用 Windows 可执行程序就整段改成 PowerShell。Ubuntu 22.04 使用原生 Linux Bash。每段标明终端和目录，切换时重新进入目录，临时变量不互相继承。

## 怎样使用正文、PPT 和视频

第一次学习时按 Markdown 的章节导航阅读，在正文指定位置完成实验并检查结果。PPT 用于配合视频讲清关键关系、复习阶段与典型操作；安装分支、完整命令、输出解释和排错细节以 Markdown 为完整入口。没有配套 PPT 的专题仍可按正文独立学习，不用等待演示材料。

```mermaid
flowchart LR
    A["读 MD<br/>理解前提"] --> B["按正文操作<br/>核对结果"]
    B --> C["看 PPT 和视频<br/>复盘重点"]
    C --> D["回到正文<br/>查细节与排错"]
```

文件统一三位编号，配套 Markdown/PPT 同编号同题名；平台差异使用文件名后缀。章节内的导航对应实验阶段，目录中不另分 Windows/Linux 文件夹。维护规则见[资料编写约定](资料编写约定.md)。

## 从哪里开始

每个专题按章节顺序阅读，讲解和本单元实验都在正文内。源码、配置与测试原件放在各主题 labs，供复制和对照；不再另设一条综合实训路线。

面向已有 C/C++ 和嵌入式开发经验、尚未系统使用 Python 环境隔离与 west 的读者。“从零”针对专题知识，不要求重学编程语法。先核对[实验准备](P000_实验准备.md)，然后根据任务选择：

| 你遇到的问题 | 阅读路线 | 完成标志 |
| --- | --- | --- |
| Windows 上怎样安装终端、国内换源并下载源码 | [Zephyr 下载与工程准备](P01_zephyr_make_project/大纲.md) | 工具可用、源码取得成功，能区分源码快照与 Git 历史 |
| 源码下载后，怎样选 SDK 包并安装构建依赖 | [下载 SDK 与安装依赖包](P01_zephyr_make_project/环境与依赖导航.md) | 主机工具与 Python/venv、SDK、CMSIS/HAL 按依据取得并逐项核验 |
| Zephyr 怎样读取 SDK、模块和板的 CMake 配置 | [P003 CMake 接口体系](P01_zephyr_make_project/P003_Zephyr的CMake接口体系_Windows.md) | 从 hello_world 和图示理解构建架构，再看输入、SDK、模块、保存范围与官方依据 |
| 怎样确认芯片型号及 CMSIS/HAL 下载依据 | [型号与依赖选择](P01_zephyr_make_project/环境与依赖导航.md#chip-selection) | 丝印/BOM/手册对应 board/SoC，区分官方清单依赖与新增移植依赖 |
| 环境准备之后，怎样编译并新增开发板 | [编译示例与新增开发板](P01_zephyr_make_project/P007_编译示例与新增开发板_Windows.md) | 先认识并编译官方 MPS2，再逐文件新增 AN386 练习板、逐层接入 UYUP HC32 并核验 |
| 不同项目需要不同 Python 包版本 | [venv 大纲](python/venv/大纲.md) | 两个环境同时运行不同版本，第三个环境可重建 |
| 多个代码仓库必须使用配套版本 | [west 大纲](west/大纲.md) | 自建多仓库清单并写一个可运行的新命令 |
| 新增 C 文件或可复用模块怎样参与编译 | [CMake 大纲](cmake/大纲.md) | 定位漏实现链接错误，验证模块开关 |
| VS Code 怎样构建、打断点和单步 | [编辑器与调试大纲](vscode/大纲.md) | 用 GDB 观察变量变化，理解实板调试链路 |
| 怎样选芯片、适配 PCB 接线并验证 | [板级配置大纲](board/大纲.md) | 找到 Kconfig/DTS 输入，区分编译、模拟与实板证据 |

west 安装承接 venv 前两章的环境与 pip 知识；已经掌握这些方法的读者可直接读 west。
CMake 主机实验先于 VS Code 单步；板级 P001、P002、P003 依次学习，P003 的模块运行实验还承接 CMake P002 中已讲过的源码。Zephyr 模块与板级实验先完成准备章中的项目工具准备。
先完成原生 `mps2/an386` 编译，确认工具、源码和模块能配合，再开展 HC32 移植。板级 P001/P002 属于移植完成后的配置练习，进入条件写在章节开头；原生源码下载成功不等于已经具备 HC32 支持。

## 文件放在哪里

```text
learning/
  P01_zephyr_make_project/  Windows/Linux 环境、共用实验、截图和演示文稿源码
  download_zephyr/      下载方案参考草稿，版本与命令待进一步核验
  python/venv/          教程、大纲、labs 实验源码
  west/                教程、大纲、labs 实验源码
  cmake/               源文件、普通库与 Zephyr 模块实验
  vscode/              主机调试工作区与 GDB 命令文件
  board/               Kconfig、设备树、Twister/QEMU 教程与配置片段
  requirements-tools.txt  已验证的工具直接依赖版本
  check_labs.py        自动验收主线及关键失败场景
  VALIDATION.md        实测环境、通过项目与未覆盖范围
  DESIGN.md            面向维护者的教学设计
  BUILD_BOARD_VALIDATION.md  构建、调试与板级实验验收边界
```

配套材料按[实验准备](P000_实验准备.md)放入实验源码目录下的 `learning/`。练习副本与运行证据放在 `G:\zephyr_practice\zephyr-main\build\learning-tools\`；SDK 保存在源码外的工具目录。资料保存位置不决定实验命令的执行位置。

新主题使用英文目录名，正文用 `PXX_中文主题.md`，大纲说明先后顺序；可执行源文件放到主题的 `labs/`。需要分析特定版本的第三方源码时，再创建该主题的 `source_reading/`，注明版本、出处和修改边界。不要把实验产物、环境目录、个人凭据混进学习资料。

每个实验至少给出：目的、前提、当前位置、命令、预期输出、失败原因、修改挑战和清理范围。脚本辅助建立重复数据，关键工具命令仍由读者亲手执行。

当前工具路线的准备章及 venv、west、CMake、VS Code、板级配置正文均已按逐步教学方式整理：操作块标出位置，代码与配置配有注释，路线图帮助接回当前步骤。各专题的实际实验覆盖范围仍以 VALIDATION.md 和 BUILD_BOARD_VALIDATION.md 为准；已写明的图形操作或实板流程不自动表示维护者已经实测。
