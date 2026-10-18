---
id: learning.zephyr-docs.basic_samples.page-74
title: TensorFlowLiteMicro魔杖示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/modules/tflite-micro/magic_wand/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="tflite-magicwand"></a>

# 第74章\_TensorFlowLiteMicro魔杖示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/modules/tflite-micro/magic_wand/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 74.1 概述（Overview）

此示例演示如何使用TensorFlow Lite Micro运行一个20KB的神经网络模型，根据加速度计（Accelerometer）数据识别手势（Gesture）。

> 注意：本README及示例改编自[面向Zephyr的TensorFlow魔杖（Magic Wand）示例](https://github.com/tensorflow/tflite-micro-arduino-examples/tree/main/examples/magic_wand)和[Antmicro关于使用Renode仿真TensorFlow的教程](https://github.com/antmicro/litex-vexriscv-tensorflow-lite-demo)。

<a id="building-and-running"></a>

## 74.2 构建与运行（Building and Running）

将`tflite-micro`模块加入West清单（Manifest）选择范围并获取模块：

```sh
west config manifest.project-filter -- +tflite-micro
west update
```

可按以下方式为[LiteX VexRiscv](https://docs.zephyrproject.org/latest/boards/enjoydigital/litex_vexriscv/doc/index.html#litex_vexriscv)构建应用，以便在Renode中仿真：

```sh
west build -b litex_vexriscv samples/modules/tflite-micro/magic_wand
```

构建完成后，按照[Renode的GitHub说明](https://github.com/renode/renode/blob/master/README.md)，[下载并以软件包形式安装Renode 1.12或更高版本](https://github.com/renode/renode/releases/)，然后启动模拟器：

```sh
renode -e "set zephyr_elf @./build/zephyr/zephyr.elf; s @./samples/modules/tflite-micro/magic_wand/renode/litex-vexriscv-tflite.resc"
```

<a id="sample-output"></a>

### 74.2.1 示例输出（Sample Output）

Renode仿真的LiteX/VexRiscv开发板接收一组数据，应用将其识别为交替出现的圆环（Ring）和斜线（Slope）手势。

```text
Got accelerometer, label: accel-0

RING:
          *
       *     *
     *         *
    *           *
     *         *
       *     *
          *

SLOPE:
        *
       *
      *
     *
    *
   *
  *
 * * * * * * * *

RING:
          *
       *     *
     *         *
    *           *
     *         *
       *     *
          *

SLOPE:
        *
       *
      *
     *
    *
   *
  *
 * * * * * * * *
```

> 译注——输入来源：上述流程由仿真环境向加速度计设备提供手势数据，所示ASCII图形是官方预期输出。它不表示本次翻译实际采集了物理传感器数据，也不代表所有开发板都可直接复用相同的输入与启动脚本。

<a id="modifying-sample-for-your-own-project"></a>

## 74.3 修改示例用于自己的项目（Modifying Sample for Your Own Project）

创建自己的TensorFlow项目时，建议复制两个TensorFlow示例之一并修改。要将TensorFlow纳入构建，必须在`prj.conf`中启用以下Kconfig选项：

```cfg
CONFIG_CPP=y
CONFIG_REQUIRES_FULL_LIBC=y
CONFIG_TENSORFLOW_LITE_MICRO=y
```

<a id="training"></a>

## 74.4 训练（Training）

按照`train/`目录中的说明训练自己的模型，以便在示例中使用。


> 译注——实现依据：[samples/modules/tflite-micro/magic_wand/renode/litex-vexriscv-tflite.resc](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/magic_wand/renode/litex-vexriscv-tflite.resc)、[samples/modules/tflite-micro/magic_wand/train/README.md](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/magic_wand/train/README.md)。这些链接对应本次核对的官方main来源，内容会随分支变化，所保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库源码仅用于版本对照。

对应官方文档源码：[samples/modules/tflite-micro/magic_wand/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/magic_wand/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/modules/tflite-micro/magic_wand/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P073_TensorFlowLiteMicro问候示例.md) · [返回大纲](大纲.md) · [下一章](P075_TensorFlowLiteMicro与EthosU示例.md)
