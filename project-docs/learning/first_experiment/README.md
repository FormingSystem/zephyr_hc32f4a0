<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# T06 第一个带证据的软件实验

阅读[从断言到可核对的实验结果](P01_从断言到实验结果.md)，实际执行一次正常、故障与恢复实验。
前置为 T02 的对象边界和 T05 的开发环境；正文重新解释测试框架与主机工具各自的职责。

实验源码在 [tests/learning/first_evidence](../../../tests/learning/first_evidence)，
公共入口为 [scripts/learning/run.py](../../../scripts/learning/run.py)。
正文已完成；在 mps2/an386 模拟目标构建并运行：正常 2/2 通过、故障 1/2 通过且返回非零、恢复 2/2 通过。
没有操作 HC32 开发板。

本组读完后，后续 T07 将解释为什么一个应用需要这些文件；其正文尚未交付。
返回[学习路线](../README.md)。
