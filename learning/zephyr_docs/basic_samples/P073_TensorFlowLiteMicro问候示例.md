---
id: learning.zephyr-docs.basic_samples.page-73
title: TensorFlowLiteMicro问候示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/modules/tflite-micro/hello_world/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="tflite-hello-world"></a>

# 第73章\_TensorFlowLiteMicro问候示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/modules/tflite-micro/hello_world/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 73.1 概述（Overview）

此TensorFlow示例应用拟合正弦波（Sine wave），演示使用TensorFlow Lite Micro最基础的方法。

示例包含的模型经过训练，用于拟合正弦函数；应用生成x值，同时打印模型预测的y值。x从0迭代到接近2π的值。

示例还包含完整的端到端流程：训练模型，将它转换为TensorFlow Lite Micro可用的形式，然后在微控制器上执行推理（Inference）。

示例有两个版本：一个使用TensorFlow Lite Micro参考算子内核（Reference kernels），另一个使用CMSIS-NN优化算子内核（Optimized kernels）。

> 注意：本README及示例改编自[面向Zephyr的TensorFlow Hello World示例](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/hello_world)。

<a id="building-and-running"></a>

## 73.2 构建与运行（Building and Running）

由于不依赖任何传感器，本示例应该能在大多数开发板上工作。

将`tflite-micro`模块加入West清单（Manifest）选择范围并获取模块：

```sh
west config manifest.project-filter -- +tflite-micro
west update
```

使用参考算子内核的应用可按以下方式在QEMU中构建并执行：

```sh
west build -b qemu_x86 samples/modules/tflite-micro/hello_world
west build -t run
```

依次按`CTRL+A`、`x`退出QEMU。

CMSIS-NN版本可在任何基于Arm(R) Cortex(R)-M处理器核的平台上构建并执行，例如基于Arm Corstone(TM)-300软件的平台。Corstone-300参考实现可以作为[MPS3 FPGA原型开发板（MPS3 FPGA prototyping board）](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/mps3)的FPGA位流文件（Bitfile）下载，也可以作为能够在主机上仿真的[固定虚拟平台（Fixed Virtual Platform，FVP）](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)下载。

> 译注——外部下载链接：上面两条Arm旧网址在本次直接检查时未通过证书验证；经网页通道复核，MPS3旧链接跳转到通用工具与软件入口，FVP旧链接跳转到固定虚拟平台入口。这里保留官方原引用，但尚未确认旧目标页面的完整内容及当前下载包。

假定已下载、安装Corstone-300 FVP，并将其加入环境变量[`PATH`](../toolchains/P003_环境变量.md#envvar-PATH)，可以使用以下命令构建与测试：

```console
$ west build -p auto -b mps3/corstone300/fvp samples/modules/tflite-micro/hello_world/ -T sample.tensorflow.helloworld.cmsis_nn
$ FVP_Corstone_SSE-300_Ethos-U55 build/zephyr/zephyr.elf
```

> 译注——原页排版：原RST中的这两条命令使用了未被正确识别的Markdown围栏，此处恢复为代码块；命令内容保持原样。行首`$`是终端提示符，实际输入时不包含它。相对路径从Zephyr仓库根目录解析。

<a id="sample-output"></a>

### 73.2.1 示例输出（Sample Output）

```text
...

x_value: 1.0995567*2^1, y_value: 1.6951603*2^-1

x_value: 1.2566366*2^1, y_value: 1.1527088*2^-1

x_value: 1.4137159*2^1, y_value: 1.1527088*2^-2

x_value: 1.5707957*2^1, y_value: -1.0849024*2^-6

x_value: 1.7278753*2^1, y_value: -1.0509993*2^-2

...
```

修改后的示例打印10对“生成的x值—预测的y值”。如果希望看到正弦曲线的完整周期，应增加`main.c`中的循环次数。

> 译注——循环次数：当前实现的`NUM_LOOPS`为10，完整周期划分由`kInferencesPerCycle`控制，其值为20。这里保留官方输出示例，未将其作为当前模拟器实测结果。

<a id="modifying-sample-for-your-own-project"></a>

## 73.3 修改示例用于自己的项目（Modifying Sample for Your Own Project）

创建自己的TensorFlow项目时，建议复制两个TensorFlow示例之一并修改。要将TensorFlow纳入构建，必须在`prj.conf`中启用以下Kconfig选项：

```cfg
CONFIG_CPP=y
CONFIG_REQUIRES_FULL_LIBC=y
CONFIG_TENSORFLOW_LITE_MICRO=y
```

CMSIS-NN版本演示如何在TensorFlow Lite Micro中使用CMSIS-NN优化算子内核，所设置的选项如下。注意，只有Arm Cortex-M处理器核，即设置了`CPU_CORTEX_M`的情况下，才设置该选项。

```cfg
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS=y
```

<a id="training"></a>

## 73.4 训练（Training）

按照`train/`目录中的说明训练自己的模型，以便在示例中使用。


> 译注——实现依据：[samples/modules/tflite-micro/hello_world/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/hello_world/src/main.c)、[samples/modules/tflite-micro/hello_world/src/constants.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/hello_world/src/constants.c)、[samples/modules/tflite-micro/hello_world/train/README.md](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/hello_world/train/README.md)。这些链接对应本次核对的官方main来源，内容会随分支变化，所保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库源码仅用于版本对照。

对应官方文档源码：[samples/modules/tflite-micro/hello_world/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/hello_world/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/modules/tflite-micro/hello_world/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/modules/tflite-micro/hello_world/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。

<a id="index-0"></a>

[上一章](P072_TensorFlowLiteMicro示例目录.md) · [返回大纲](大纲.md) · [下一章](P074_TensorFlowLiteMicro魔杖示例.md)
