<!-- SPDX-License-Identifier: Apache-2.0 -->

# west 配套材料

正文 P01～P05 是唯一教学路线，每章就地给出当章操作、源码、解释与恢复。本目录提供原件与准备工具，不要求初学者先执行一套包含后续知识的综合实验。

| 材料 | 用途 |
| --- | --- |
| seed_workspace.py | 准备本地源仓库及版本，不执行 west |
| init_workspace.py | 处理教材位于外层工作区中的初始化条件，内部调用真正的 west init |
| templates/west-basic.yml | P01 正文的两个项目清单，不带分组和扩展 |
| templates/west.yml.in、west-v2.yml | 包含后续分组与扩展的完整配置参考；P01 正文只启用两个必要项目 |
| templates/west-commands.yml、commands/inventory.py | P04 的命令注册与完整实现 |
| solutions/inventory_count.py | P04 添加计数选项后的对照实现 |
| verify_release.py | P05 正文完整展示的只读交付检查，核对声明、Git 提交及应用行为 |
| test_workspace.py | P05 的维护回归参考，检查工作区定位、下载、版本及应用；前四章不要求提前理解测试编排 |

实验目录是 build/learning-tools/west/textbook-01，工具环境另放 west-textbook-tools。材料生成器拒绝覆盖已有同名实验，请换名复练。原件不保存读者的临时提交和本机配置。

[第一章](../P01_建立第一个多仓库工作区.md) · [大纲](../大纲.md)
