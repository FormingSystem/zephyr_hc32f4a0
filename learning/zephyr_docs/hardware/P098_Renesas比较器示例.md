---
id: learning.zephyr-docs.hardware.analogsamp-1
title: Renesas比较器示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/boards/renesas/comparator/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="renesas_comparator"></a>

# 第98章\_Renesas比较器示例

原文：[Renesas comparator](https://docs.zephyrproject.org/latest/samples/boards/renesas/comparator/README.html)。读取日期：2026-10-13，`latest`。

## 98.1\_观察比较器输出

本示例用于监测Renesas板上的 **比较器（Comparator）**输出，并使用 **发光二极管（Light-Emitting Diode，LED）**显示结果。输出为高时LED0点亮，输出为低时LED0熄灭。

## 98.2\_参考与比较输入

IVREF参考输入连接到DA0的内部输出；DA0属于 **数模转换器（Digital-to-Analog Converter，DAC）**模块。原文默认DA0约为1.75 V，并将其描述为满量程电压的一半。这是原示例的设置说明，不是对任意板参考电压的保证。

对于IVCOMP比较输入，原文给出两种接法：将IVCMP3接到板载SW0按钮（在 `ek_ra8m1` 上是P600）；或把IVCMP3接到外部待比较电压。IVREF、IVCOMP和IVCMP3在这里保留为原文硬件信号名称，不是主机文件或程序变量路径。

## 98.3\_构建与烧录

准备Zephyr环境、对应RA板工具链与烧录工具，并按实际板说明完成所选接法。从实验Zephyr源码根目录，在Ubuntu Bash或已准备好的UCRT64 Bash中执行：

```shell
west build -b ek_ra8m1 samples/boards/renesas/comparator
west flash
```

`samples/boards/renesas/comparator` 是官方示例目录。先确认构建成功，再烧录；无法初始化设备时应回查目标板、比较器和DAC配置，不能先把LED无变化判为输入比较错误。

## 98.4\_两种接法的预期状态

原文第一种接法使IVCMP3连接到带 **上拉（Pull-Up）**的SW0：未按按钮时，比较器输出高、LED0亮；按下按钮时，比较器输出低、LED0灭。

第二种接法将IVCMP3连接到另一参考电压：原文描述输入高时比较器输出高、LED0亮，输入低时比较器输出低、LED0灭。这里的高低应结合相对于比较参考的电压理解，不是为外部电压源定义一个通用的固定数值。

本次未连接输入电压、按动板载按钮、构建烧录或实际测量LED和比较器输出。

[上一章：运算放大器示例入口](P097_运算放大器示例入口.md) · [下一章：FRDM模拟信号链示例](P099_FRDM模拟信号链示例.md) · [返回大纲](大纲.md)
