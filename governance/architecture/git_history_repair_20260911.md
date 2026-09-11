<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 2026-09-11 Git 历史修正记录

本次由开发者明确要求“git规则修改和git历史修改”，并要求将已完成的工作区和暂存区改动按类型提交、推送。
该授权属于[Git 规范 1.7](../conventions/git_guide.md)的历史迁移例外，不改变日常提交禁止擅自改写历史的规则。
专题扩写暂缓，本次归档既有成果。

## 原因与修正范围

原主线共 7 条提交，前 6 条含来源钩子不接受的独立 Assisted-by 尾注。
当时自写的 Python 校验器主动允许尾注，导致提交没有被拦截；原始来源钩子和现在恢复的钩子会拒绝这些消息。
钩子只检查语法，不能根据标题自动判断内容类型、范围是否准确或一个提交是否混合多个独立结果。

本次删除违规消息尾注；把新增工程能力的 chore 改为 feat，把实际修改工作区解释器的 docs 改为 fix，
按真实归属补充范围。范围原本可省略，不能把没有括号误报为钩子失效原因。
原 723fa2c06 分为工程知识介绍、私人环境入口、学习路线三项，分别使用 content、docs、docs；
共享导航和状态文件按对应内容分块，第三项完成后的文件树与原提交完全相同。
其余节点只修正消息和父节点关联；作者、提交者及时间保持原值，文件许可和代码内容不变。
原 d79a7bff3 的消息已合规，只因祖先变化取得新的提交标识。

## 备份与校验

迁移前对所有本地引用建立完整 bundle，并用 git bundle verify 校验通过；
工作区差异、暂存区差异及未跟踪候选文件另有本机备份与 SHA-256 清单。
完整备份位于被忽略的 .local/publish-20260911/history-backup/all-before-rewrite.bundle，
其 SHA-256 为 `8db1fc97cae00d0cbeac87f254eb268e917be376a768445826e83cd6c9867ffd`。
备份包含迁移前已完成的 8 条新提交；备份本体、脚本、原始日志与私人配置不纳入 Git。

本地历史迁移通过带预期旧值的引用事务一次生效。每个原节点对应的新最终节点具有相同 tree 标识，
拆分后的中间节点也检查差异归属；真实索引、未暂存差异和未跟踪路径列表在事务前后保持一致。
迁移后的 9 条历史提交及当轮已完成的 8 条新提交均逐条执行现行 commit-msg 钩子并通过，
没有关闭钩子或放宽来源格式；消息语义和拆分粒度另行审查。

## 已发布节点对照

| 迁移前节点 | 迁移后节点 | 当前结果 |
| --- | --- | --- |
| `08ce3be8a39af9c214d2b45a8871ddb9c38cd755` | `c44dd1bd4c6abdf71e5af542088ec9a30e3593ae` | feat(repository/bootstrap): 初始化独立工程与构建调试入口 |
| `4928dd4dc87839c498479ba2d69e147b38d8fe44` | `fb2fe5a0a7678651699aa21ed2bbb1b1a7f1614d` | fix(build/environment): 修正开发仓库目录与并列依赖定位 |
| `b0bd5ee270042dcd2b007ad0d65025e1a8629ead` | `9aebb8f6daf82e4d87cb56a355f276fabdede055` | feat(hc32f4a0): 导入完整源码并实现基础板级移植 |
| `304db4f1d373b3ac365ae17c7a3a174b8a5406c6` | `fd79985e1bf6bbfa2a101e95c555194070002cad` | fix(build/environment): 使用仓库虚拟环境并记录独立构建验证 |
| `309885db9884200ef07cf329c264704993d95293` | `388f616e754f8e6a9150d54cd3f16fbe82e9fe6e` | docs(repository/navigation): 统一工程文档目录与资料导航 |
| `723fa2c0661360ac151a572a9defc25f57f8c5b4` | `8cb8a613797ffb48e3af1d4cad162f30b3a3c6ae` | content(knowledge/zephyr): 解释工程运行构建与HC32移植职责 |
| `723fa2c0661360ac151a572a9defc25f57f8c5b4` | `712466f3ac9fd88cebf96e75747ba1f919886be1` | docs(repository/environment): 明确私人配置与芯片资料缓存边界 |
| `723fa2c0661360ac151a572a9defc25f57f8c5b4` | `f66f25596de9dbe158f5de9874044512125a4ba7` | docs(learning/roadmap): 建立14组88专题的学习与实验路线 |
| `d79a7bff3115163d79e4462ed7044cb26ed6bc04` | `3f6d306aceb3cf74245ea7508cab9488363de635` | fix(repository/git): 恢复linux-note提交规则与原始校验 |

上表共 7 个旧节点映射到 9 个新节点。历史实验记录中的旧提交号表示当时实际运行起点，
保留原值，通过本表追溯；不能把旧报告的起点替换成新节点，假装该实验曾在迁移后执行。
当轮新增提交的祖先引用随之迁移，内容及消息保持不变。
本次未再运行硬件；构建、软件回归与主机检查的已有结果见[项目状态](../../project-docs/porting-status.md)。

## 远端更新边界

发布只更新本项目远端 master，以远端原值 `d79a7bff3115163d79e4462ed7044cb26ed6bc04`
作为 --force-with-lease 的精确预期值；远端若已有其他更新则拒绝覆盖。
远端 Dependabot 分支、拉取请求引用及其他引用不在迁移范围内，不执行镜像推送或批量删除。
以后已有旧克隆需依据本记录核对主线变化，再整理自己的未提交和未发布工作；不自动重写其他克隆。
