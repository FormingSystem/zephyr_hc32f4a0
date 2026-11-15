---
id: learning.zephyr-official-intro.design
title: 官方入门译文编排与覆盖设计
kind: reference
status: maintained
domains: [zephyr, documentation]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 官方入门译文编排与覆盖设计

本次采用内容新增模式。用户已将范围扩大为整个 Zephyr 官方文档，包括 API 自动生成参考、全部开发板说明和全部示例，并选择按模块分批完成。第一批为 Introduction 及入门相关页面。阅读契约为官方文档译文与参考页，不将原文改写成原创实验教材，不按教材技能机械增加实验或重排原文推理。原有学习材料保持原样，入口增加译文导航。

## 范围与章节职责

| 编号 | 官方页面 | 中文章节职责 |
| --- | --- | --- |
| P001 | Introduction | 完整介绍系统定位、架构、功能、社区和资源 |
| P002 | Getting Started Guide | 保留 Ubuntu、macOS、Windows 全部分支，贯通环境、源码、构建和烧录 |
| P003 | Beyond the Getting Started Guide | 解释环境与工具链替代配置、更新、别名、模拟和原生运行 |
| P004 | Blinky | 保留硬件要求、构建错误、设备树例子与相关入口 |
| P005 | Hello World | 保留 QEMU 构建、输出和退出方法 |
| P006 | Glossary of Terms | 翻译全部词条，保持英文检索顺序 |
| P007 | Install Linux Host Dependencies | 保留四类发行版与工具升级分支 |
| P008 | macOS alternative setup instructions | 保留 Gatekeeper 和 MacPorts 说明 |
| P009 | Windows alternative setup instructions | 保留 WSL 历史版本条件并标注时效边界 |

第一批主线依赖为 P001 → P002 → P004/P005；P003 承接 P002。P006 按需查询，P007—P009 是操作系统补充说明，不要求顺序执行所有系统分支。整站内核、驱动、API、开发板手册、SDK 手工安装和应用开发均属于后续翻译范围；在译文完成前保留官方入口，并在页面清单中标为待翻译。第一批完成不等于整站完成。

## 术语与内容保护

- 产品、架构、工具、配置项和路径保留原名；kernel、subsystem、application image 分别统一为内核、子系统、应用镜像。
- board name、board revision、board qualifiers、board target 分别为开发板名称、开发板修订版本、开发板限定符、开发板目标；不混成同一个“板名”。
- workspace、manifest、module 分别为工作区、清单、模块；保留 west project 与 Zephyr module 的不同定义。
- flash 动词译为烧录，Flash 存储器名称保留；native_sim 是 Linux 原生模拟器，文件名 zephyr.exe 不表示 Windows 程序。
- 忠实保留原文代码及版本号。明确过时或与同批页面冲突的内容紧邻加“译注”，不悄悄修订原文，不冒充上游更新。
- 原文注释可译为中文，参数、路径和执行次序不因翻译改变；网页折叠的各系统标签展开为独立小节。
- 文档位于 F 盘仓库。原文的 zephyrproject 是独立官方示例路径；本项目实验位于 G 盘，两套路径不交叉拼接。用户已经有实验工程时复用既有教程，不再次初始化工作区。

## 验证边界

以 2026-10-12 读取的 latest 网页为翻译基线，记录 URL、页面生成日期与 HTML 摘要；不将本地源码版本号或查询时的 main 提交冒充网页构建提交。逐项核对原文标题、列表、命令和提示。运行文档结构、链接、连续阅读风险及术语候选审计，人工说明参考页和忠实翻译带来的保留项。不安装依赖、不更新源码、不构建、不烧录。
