---
id: learning.west.labs.readme
title: west 配套材料
kind: reference
status: maintained
domains: [documentation]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# west 配套材料

正文 P001～P005 是唯一教学路线，每章就地给出当章操作、源码、解释与恢复。本目录提供原件与准备工具，不要求初学者先执行一套包含后续知识的综合实验。

| 材料 | 用途 |
| --- | --- |
| seed_workspace.py | 准备本地源仓库及版本，不执行 west |
| init_workspace.py | 处理学习资料位于外层工作区中的初始化条件，内部调用真正的 west init |
| templates/west-basic.yml | P001 正文的两个项目清单，不带分组和扩展 |
| templates/west.yml.in、west-v2.yml | 包含后续分组与扩展的完整配置参考；P001 正文只启用两个必要项目 |
| templates/west-commands.yml、commands/inventory.py | P004 的命令注册与完整实现 |
| solutions/inventory_count.py | P004 添加计数选项后的对照实现 |
| templates/commands/repo_audit.py | P004 完整展示并逐段解释的团队策略扩展；默认不登记，由读者增加 userdata 和描述文件条目后调用 |
| verify_release.py | P005 正文完整展示的只读交付检查，核对声明、Git 提交及应用行为 |
| test_workspace.py | P005 的维护回归参考，检查工作区定位、下载、版本及应用；前四章不要求提前理解测试编排 |
| test_policy.py | 维护者回归，验证标准字段与 userdata 的规则差异、Git 执行、自定义策略成功与失败、命令登记和内建查询 |

实验目录是 build/learning-tools/west/textbook-01，工具环境另放 west-textbook-tools。材料生成器拒绝覆盖已有同名实验，请换名复练。原件不保存读者的临时提交和本机配置。

维护者从学习资料根目录运行 `python learning/west/labs/test_policy.py`，解释器须已安装 west 1.5.0。完整源码按调用阶段注释：unittest 先调用 setUpClass，创建唯一 policy-* 实验、执行真实 init/update，再复制基础声明；每项测试的 setUp 写本次配置和命令登记，command 用固定 cwd/environment 启动真实子进程并记录输出；断言同时核对退出码和错误内容；tearDown 恢复该新副本的库文件和暂存状态。整个过程不写读者的 textbook-01，测试目录与 policy-evidence.log 保留。用例中的 reset 只撤销这次隔离副本对 arithmetic.py 的暂存，不改变提交。此脚本用于维护回归，不能替代逐章实验和读者理解。

[第一章](../P001_建立第一个多仓库工作区.md) · [大纲](../大纲.md)
