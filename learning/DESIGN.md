<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 教学设计与维护约定

本次在现有完整 Zephyr 工程中新增工具专题。`learning/` 保存项目环境需要补充的通用教学知识和实验；`project-docs/` 保存本项目实际采用的版本、配置、路径和流程。用户指定的两个原空目录补为项目接入说明并链接教程，不复制通用正文。已有 Zephyr 课程继续围绕本项目源码维护，其他未提交资料保持原样。本文件是作者工作蓝图，不是读者先修材料。

## 读者起点与成果

读者已有 C/C++、嵌入式开发与基本命令行经验；零基础只针对 Python 环境隔离、Python 包管理和 west。无需重讲函数、文件目录或编程语法。对理解 west 必需的 Git 状态作简短对齐，不铺开 Git 入门课程。UCRT64 Bash 与 Windows Python 为实测主线；准备章给出 Linux/macOS 的解释器路径和激活差异。教学运行数据统一写入 `build/learning-tools/`，不接触外部 Zephyr 工作区。

## 章节依赖与契约

| 章节 | 承接与问题 | 场景、增加的模型 | 可验收结果与后续问题 |
| --- | --- | --- | --- |
| venv P01 | 从零：为什么两项目需要不同依赖 | 解释器→模块→包→环境；创建、激活、退出 | 用解释器路径和前缀证明隔离，下一步安装包 |
| venv P02 | 环境已建立，安装去了哪里 | 两个版本的同名本地包；构建、安装、导入 | 两个进程同时输出不同版本，下一步复制环境需求 |
| venv P03 | 本机能运行，同事怎样重建 | 依赖声明、快照、配置层次、离线包目录 | 新环境重建并解释配置覆盖，下一步诊断错误 |
| venv P04 | 路径与声明已经建立，为什么仍失败 | 解释器身份、命名遮蔽、基础 Python、边界 | 按证据排查并选择项目/命令行工具管理方式 |
| west P01 | 从零：多个仓库如何配套 | Git 提交、清单、工作区；本地初始化和更新 | 不用 Zephyr 得到可运行双仓库程序 |
| west P02 | 能下载，为什么不能直接 pull | 清单 revision、当前 HEAD、跟踪引用 | 切换依赖版本、开发分支、冻结并重建 |
| west P03 | 多项目开始需要裁剪和组合 | YAML 字段、配置作用域、分组、导入 | 修改生效位置、启停项目、拆分清单 |
| west P04 | 需要自己的团队命令 | 扩展发现、参数解析、执行、错误退出 | 修改 inventory 命令、复验输出和禁用行为 |
| west P05 | 单人实验如何迁移至协作 | 审查、提交边界、发布记录、故障恢复 | 独立添加项目并定位常见失败 |

公共模型按模块递进，平台只比较解释器路径、激活与文本写入差异，不复制两套原理。venv 不声称隔离操作系统；west 不声称安装 Python 包或编译程序。

## 术语依赖与证据计划

| 首次进入 | 名称与类型 | 朴素含义及边界 | 证据入口 |
| --- | --- | --- | --- |
| venv P01 | interpreter、module、package、venv（模块名） | 执行程序、可导入代码、安装分发单位、隔离包目录；环境不是虚拟机 | Python 3.12 venv 官方文档、inspect_environment.py 输出 |
| venv P01 | PATH、sys.executable、prefix（环境变量或属性） | 命令查找顺序、实际执行文件、环境根；激活不等于创建 | Python 文档和直接路径实验 |
| venv P02 | pip（工具名）、wheel（分发格式）、build backend | 安装器、可安装归档、产生归档的工具；构建与安装分开 | pip / Packaging 官方文档、两个本地包 |
| venv P03 | requirements、constraints、configuration、lock | 安装要求、版本限制、工具选项、完整锁定；freeze 不等于跨平台锁 | pip 官方文档、重建实验 |
| west P01 | Git、commit、repository、branch、tag、HEAD | 工具、快照、历史容器、可移动名称、发布标记、当前提交 | git 帮助、本地种子仓库 |
| west P01 | west（工具名）、workspace、manifest、YAML | 多仓库协调器、目录树、配套表、配置文件格式 | west 官方文档与实际命令 |
| west P02 | revision、manifest-rev、detached HEAD | 配套版本表达式、解析后的跟踪引用、不在本地分支的状态 | 固定 west 版本实验和帮助 |
| west P03 | remote、group-filter、import | 地址前缀、活动项目筛选、合并清单；停用不删除 | 实验验证字段含义 |
| west P04 | extension、WestCommand、parser、API | 用户命令、扩展基类、参数解析器、程序调用接口 | 本仓库完整代码及 west 扩展文档 |

## 验收边界

所有主线命令在隔离的运行目录执行，检查真实输出和失败退出码。记录解释器、pip、west、Git 与操作系统版本。脚本通过不能替代章节冷读：每章需要无需点击链接即可解释对象、因果、正常路径、失败及恢复。官方链接就近提供依据；版本敏感结论优先由安装版本帮助和实验交叉验证。

后续主题采用 `<topic>/大纲.md`、`PXX_中文主题.md`、`labs/`。只有实际需要逐行分析上游实现时才新增 `source_reading/`；当前实验自有源码直接保存在各主题 `labs/`，不复制第三方源码。
