<!-- SPDX-License-Identifier: Apache-2.0 -->

# venv 配套实验材料

本目录存放教材使用的原件，不是一套另行跳转执行的综合实验。按 P01～P04 连续阅读；每章在正文展示当章所需代码、操作、解释与恢复步骤，后章承接前章已经建立的状态。

| 材料 | 在教材中何时使用 |
| --- | --- |
| package_v1、package_v2 | P02：观察两版源码、制作 wheel、分别安装 |
| application/main.py | P02 的问候应用参考实现 |
| application/requirements.txt、requirements-v1.txt | P03：记录第一版安装要求 |
| application/tests/test_greeting.py | P04：两项行为检查的完整原件 |
| inspect_environment.py | 可选的维护用环境信息汇总；P01 用短代码逐项观察，不要求先读这个汇总器 |

读者的复制品和环境放在 build/learning-tools/venv-textbook；不要在本目录打包、安装环境或改坏原件。章节中的源码允许自行输入，目录中的原件便于核对。自动回归脚本用于维护材料，不能替代正文实验。

[开始阅读第一章](../P01_创建并认识虚拟环境.md) · [专题大纲](../大纲.md)
