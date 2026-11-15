---
id: learning.zephyr-docs.board-samples.page-80
title: Neutron微控制器机器学习推理
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/tflm_neutron/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="tflite-neutron"></a>

# 第80章\_NXP Neutron 上的微控制器 TensorFlow Lite（TensorFlow Lite for Microcontrollers on NXP Neutron）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/tflm_neutron/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/tflm_neutron/README.rst/..)

<a id="overview"></a>

## 80.1 概述（Overview）

本示例展示如何使用 TFLM 框架及 NXP Neutron 神经网络处理单元（Neural Processing Unit，NPU）进行图像分类推理（Inference）。

> 译注——输入来源：TFLM 是微控制器版 TensorFlow Lite（TensorFlow Lite for Microcontrollers）。本次 main_functions.cpp 使用编译进固件的 image_data.h，main.c 默认只运行一次推理；本页不包含摄像头采集流程，也没有随文的独立原始图片附件。

示例运行一个基于 MobileNet、已转换成 TFLite FlatBuffer 的模型；模型作为 C 头文件数组编译进应用。Neutron NPU 通过在 TFLM `MicroMutableOpResolver` 中注册的自定义 `NEUTRON_GRAPH` 算子，加速受支持的算子。

<a id="supported-platforms"></a>

## 80.2 支持的平台（Supported Platforms）

本示例支持具有 Neutron NPU 的以下 NXP 平台：

- MIMXRT798S，即 i.MX RT700 系列。

- FRDM-MCXN947，即 MCXN 系列。

构建时通过 CMakeLists.txt 选择平台专用模型。

<a id="generating-neutron-converted-model"></a>

## 80.3 生成经 Neutron 转换的模型（Generating Neutron-converted model）

按以下步骤为 Neutron NPU 转换量化 TFLite 模型，并生成本示例使用的头文件。

<a id="software-requirements"></a>

### 80.3.1 软件要求（Software requirements）

- [eIQ Toolkit](https://www.nxp.com/design/software/development-software/eiq-ml-development-environment/eiq-toolkit-for-end-to-end-model-development:EIQ-TOOLKIT)，适用于 Windows 和 Linux。

- GCC、Python 和 Git 依赖。

<a id="converting-the-model-using-neutron-converter"></a>

### 80.3.2 使用 neutron-converter 转换模型

安装 eIQ Toolkit 后，`neutron-converter` 位于工具包安装目录下，例如相对于 eIQ Toolkit v1.15.1 安装根目录的 `bin/neutron-converter/MCU_SDK_25.03.00`。将该工具所在目录加入可执行文件搜索路径。

> 译注——可移植路径：这里按读者要求，将原文包含盘符的安装位置改写为相对工具包安装根目录的路径，保留示例版本与子目录信息。读者使用自己的安装位置，不要求仓库或工具位于特定磁盘；模型转换命令中的文件名相对实际执行目录解析。

为 Neutron NPU 转换量化 TFLite 模型：

```text
neutron-converter --input model_quant.tflite --output model_npu.tflite \
--target imxrt700 --use-sequencer
```

`neutron-converter` 以一个 TFLite 文件为输入，生成另一个 TFLite 文件；其中，Neutron NPU 支持的算子被替换为自定义 `NeutronGraph` 算子，未转换的层仍在 Cortex-M33 内核上运行。

<a id="converting-to-c-array"></a>

### 80.3.3 转换为 C 数组（Converting to C array）

使用 `xxd` 将 TFLite 模型及输入／输出数据转换为 C 头文件：

```text
xxd -c 16 -i model_npu.tflite model_npu.tflite.h
xxd -c 16 -i input_data.bin input_data.h
xxd -c 16 -i output_data.bin output_data.h
```

也可以给 `neutron-converter` 传入 `--dump-header-file-input` 和 `--dump-header-file-output` 参数，直接生成头文件。

<a id="synchronizing-to-this-sample"></a>

### 80.3.4 同步到本示例（Synchronizing to this sample）

将生成的头文件复制到相应模型目录：

> 译注——集成并非只改文件名：本次实现读取 model.hpp 中的 g_model，并使用 image_data.h 和 labels.h。xxd 默认根据输入文件名生成数组标识符，因此还需核对模型数组名称、输入尺寸／类型、量化参数与标签顺序；将任意头文件重命名为 model.hpp 不保证可编译或推理正确。

- RT700 使用：`src/models/rt700/model.hpp`。

- MCXN 使用：`src/models/mcxn/model.hpp`。

<a id="building-and-running"></a>

## 80.4 构建与运行（Building and running）

> 译注——执行前提：west 构建命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工作区、工具链、模块与具体板；下载按板文档核对。主机网络和模型转换步骤另按相应小节的执行环境处理。本次未构建、烧录或运行硬件实验。

将 tflite-micro 模块加入 west 清单并拉取：

```text
west config manifest.project-filter -- +tflite-micro
west update
```

<a id="fetching-nxp-neutron-blobs"></a>

### 80.4.1 获取 NXP Neutron 二进制文件（Fetching NXP Neutron blobs）

本示例需要 `hal_nxp` 模块提供的 NXP Neutron NPU 驱动及固件二进制文件（Binary blobs）；构建前先获取：

> 译注——依赖范围：west update 获取 tflite-micro 模块，west blobs fetch hal_nxp 另行获取驱动和固件二进制文件；这两步不等价。本次 CMake 在缺少 libNeutronDriver.a 时直接报错；tests.yaml 标为 build_only 且由 CONFIG_TAINT_BLOBS 过滤，因此测试条目存在不意味着已运行推理。

```text
west blobs fetch hal_nxp
```

为 RT700 开发板构建示例：

> 译注——原文目标名称与本次测试配置：下面原始命令的 mimxrt798s/mimxrt700_evk 与当前 tests.yaml 不一致；测试清单使用 mimxrt700_evk/mimxrt798s/cm33_cpu0。MCXN 原命令 frdm_mcxn947/mcxn947 也缺少测试清单中的 /cpu0。原命令保留，实际构建按对应版本有效的完整板目标选择。

```text
# From the root of the zephyr repository
west build -b mimxrt798s/mimxrt700_evk samples/boards/nxp/tflm_neutron
```

随后烧录镜像：

```text
west flash
```

<a id="building-for-mcxn"></a>

### 80.4.2 为 MCXN 构建（Building for MCXN）

```text
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947 samples/boards/nxp/tflm_neutron
```

<a id="sample-output"></a>

## 80.5 输出示例（Sample output）

应用在控制台打印排名前五的分类结果，以及相应置信度百分比：

> 译注——结果边界：ship、automobile、bird、cat、deer 分别是船、汽车、鸟、猫、鹿。百分比是此模型对内置输入的输出分数，不是数据集准确率。本次源码在 setup／Invoke 失败后仍可能由 main.c 打印末尾 Inference complete!，应检查初始化、Invoke 状态及 Top 5 结果，不能仅以最终一行认定成功。

```text
=== TFLM NXP Neutron Starting ===

Inference #1
----------------------------------------
Running inference...
Inference complete

Top 5 Results:
----------------------------------------
1. ship                           99.61%
2. automobile                      0.00%
3. bird                            0.00%
4. cat                             0.00%
5. deer                            0.00%
----------------------------------------

Inference complete!
```

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/tflm_neutron/src/main.c)；[CMakeLists.txt](../../../samples/boards/nxp/tflm_neutron/CMakeLists.txt)；[src/main_functions.cpp](../../../samples/boards/nxp/tflm_neutron/src/main_functions.cpp)；[tests.yaml](../../../samples/boards/nxp/tflm_neutron/tests.yaml)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/tflm_neutron/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/tflm_neutron/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/tflm_neutron/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P079_S32网络控制器.md) · [返回大纲](大纲.md) · [下一章](P081_NXP示例目录.md)
