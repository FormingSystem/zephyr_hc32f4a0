<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 学习中心

这里保存项目环境所需的补充教学知识和实验。知识讲解采用可迁移的普通项目场景；读完以后，你应能解释命令修改了什么、判断配置是否生效，并回到本项目调整用法。本项目具体采用什么版本、路径和配置，记录在 [project-docs/](../project-docs/README.md)。

## 从哪里开始

每个专题按章节顺序阅读，讲解和本单元实验都在正文内。源码、配置与测试原件放在各主题 labs，供复制和对照；不再另设一条综合实训路线。

面向已有 C/C++ 和嵌入式开发经验、尚未系统使用 Python 环境隔离与 west 的读者。“从零”针对专题知识，不要求重学编程语法。先核对[实验准备](P00_实验准备.md)，然后根据任务选择：

| 你遇到的问题 | 阅读路线 | 完成标志 |
| --- | --- | --- |
| 不同项目需要不同 Python 包版本 | [venv 大纲](python/venv/大纲.md) | 两个环境同时运行不同版本，第三个环境可重建 |
| 多个代码仓库必须使用配套版本 | [west 大纲](west/大纲.md) | 自建多仓库清单并写一个可运行的新命令 |
| 新增 C 文件或可复用模块怎样参与编译 | [CMake 大纲](cmake/大纲.md) | 定位漏实现链接错误，验证模块开关 |
| VS Code 怎样构建、打断点和单步 | [编辑器与调试大纲](vscode/大纲.md) | 用 GDB 观察变量变化，理解实板调试链路 |
| 怎样选芯片、适配 PCB 接线并验证 | [板级配置大纲](board/大纲.md) | 找到 Kconfig/DTS 输入，区分编译、模拟与实板证据 |

west 安装承接 venv 前两章的环境与 pip 知识；已经掌握这些方法的读者可直接读 west。
CMake 主机实验先于 VS Code 单步；板级 P01、P02、P03 依次学习，P03 的模块运行实验还承接 CMake P02 中已讲过的源码。Zephyr 模块与板级实验先完成准备章中的项目工具准备。
当前工程 west 初始化及新 GitHub 克隆步骤分别见[项目 west](../project-docs/west/README.md)、[发布与重建](../project-docs/distribution.md)。

## 文件放在哪里

```text
learning/
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

生成的环境、仓库与运行证据统一放在根目录 `build/learning-tools/`，不提交。

新主题使用英文目录名，正文用 `PXX_中文主题.md`，大纲说明先后顺序；可执行源文件放到主题的 `labs/`。需要分析特定版本的第三方源码时，再创建该主题的 `source_reading/`，注明版本、出处和修改边界。不要把实验产物、环境目录、个人凭据混进教材。

每个实验至少给出：目的、前提、当前位置、命令、预期输出、失败原因、修改挑战和清理范围。脚本辅助建立重复数据，关键工具命令仍由读者亲手执行。
