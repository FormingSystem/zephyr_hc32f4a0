---
id: learning.zephyr-docs.basic_samples.page-75
title: TensorFlowLiteMicro与EthosU示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/modules/tflite-micro/tflm_ethosu/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="tflite-ethosu"></a>

# 第75章\_TensorFlowLiteMicro与EthosU示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/modules/tflite-micro/tflm_ethosu/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 75.1 概述（Overview）

本示例演示如何结合微控制器版TensorFlow Lite（TensorFlow Lite for Microcontrollers，TFLM）框架与Arm Ethos-U神经网络处理器（Neural processing unit，NPU）执行推理。

示例运行的模型下载自[Arm模型库（Arm model zoo）](https://github.com/ARM-software/ML-zoo)，并经过[Vela编译器（Vela compiler）](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela)优化。

Vela以一个TFLite文件为输入，输出另一个TFLite文件：其中Arm Ethos-U NPU支持的算子（Operator）被替换为Ethos-U自定义算子。在理想情况下，整个网络会被替换成一个Ethos-U自定义算子。

<a id="generating-vela-compiled-model"></a>

## 75.2 生成经Vela编译的模型（Generating Vela-compiled model）

按照以下步骤生成经Vela编译的模型与测试输入／输出数据。本示例使用[keyword_spotting_cnn_small_int8](https://github.com/Arm-Examples/ML-zoo/tree/master/models/keyword_spotting/cnn_small/model_package_tf/model_archive/TFLite/tflite_int8)模型。

> 注意：默认的Vela编译模型面向MPS3目标上的Arm Ethos-U55 NPU，配置为128个乘加单元（Multiply-accumulate，MAC）。单个模型可能增加数百KB的数据，因此不要为了其他目标而继续向代码库添加更多模型。

**步骤1：下载文件。** 从[keyword_spotting_cnn_small_int8](https://github.com/Arm-Examples/ML-zoo/tree/master/models/keyword_spotting/cnn_small/model_package_tf/model_archive/TFLite/tflite_int8)下载：

- `cnn_s_quantized.tflite`
- `testing_input/input/0.npy`
- `testing_output/identity/0.npy`

**步骤2：使用Vela针对Arm Ethos-U NPU优化模型。** 假设目标为128MAC的Arm Ethos-U55 NPU：

```console
$ vela cnn_s_quantized.tflite \
--output-dir . \
--accelerator-config ethos-u55-128 \
--system-config Ethos_U55_High_End_Embedded \
--memory-mode Shared_Sram
```

**步骤3：去掉不需要的文件头。** 原文说明`testing_input/input/0.npy`和`testing_output/0.npy`具有128字节文件头，集成到本示例之前必须去掉。

```console
$ dd if=testing_input/input/0.npy of=testing_input/input/0_no-header.npy bs=1 skip=128
$ dd if=testing_output/identity/0.npy of=testing_output/identity/0_no-header.npy bs=1 skip=128
```

> 译注——文件名与头长度：原文说明文字省略了输出路径中的`identity/`，上面的下载清单与`dd`命令使用完整路径。128字节是原文针对这组样本文件的说明，不能将它视为任意NumPy数组文件的固定头长度；替换输入数据时应先核对文件格式与实际头长度。命令行开头的`$`为提示符，实际输入时不包含它。

**步骤4：转换为C数组。**

```console
$ xxd -c 16 -i cnn_s_quantized.tflite cnn_s_quantized.tflite.h
$ xxd -c 16 -i cnn_s_quantized_vela.tflite cnn_s_quantized_vela.tflite.h
$ xxd -c 16 -i testing_input/input/0_no-header.npy testing_input/input/0_no-header.npy.h
$ xxd -c 16 -i testing_output/identity/0_no-header.npy testing_output/identity/0_no-header.npy.h
```

**步骤5：同步到本示例。** 将以下文件同步到示例的[`keyword_spotting_cnn_small_int8`](https://github.com/Arm-Examples/ML-zoo/tree/master/models/keyword_spotting/cnn_small/model_package_tf/model_archive/TFLite/tflite_int8)目录，文件对应关系如下：

- `cnn_s_quantized_vela.tflite.h` → `model.h`
- `testing_input/input/0_no-header.npy.h` → `input.h`
- `testing_output/identity/0_no-header.npy.h` → `output.h`

> 注意：如果运行未经Vela编译的模型（`CONFIG_TAINT_BLOBS_TFLM_ETHOSU=n`），则改为同步`cnn_s_quantized.tflite.h`。

> 译注——数组接口：当前模型目录位于示例下的`src/models/keyword_spotting_cnn_small_int8`。仅将`xxd`生成文件改名并不足以完成集成：当前代码引用`modelName`、`networkModelData`、`inputData`与`expectedOutputData`，模型头还定义张量内存池大小（`TENSOR_ARENA_SIZE`）、对齐和链接段属性。生成的新数组需要与这些接口及目标内存配置相匹配；保留适当的`MODEL_ATTR`、`INPUT_ATTR`等声明，不要用默认生成的标识直接覆盖后就假定可用。

<a id="building-and-running"></a>

## 75.3 构建与运行（Building and running）

将`tflite-micro`模块加入West清单（Manifest）选择范围并获取模块：

```sh
west config manifest.project-filter -- +tflite-micro
west update
```

应用可在任何具备Arm Ethos-U NPU能力的平台上构建并运行，例如Corstone(TM)-300或Corstone-320。

<a id="run-target-prerequisites"></a>

### 75.3.1 run目标的前提条件（Run target prerequisites）

使用CMake的`run`目标（`-t run`）时，为所用平台设置FVP二进制路径；对于Arm Ethos-U85 NPU，还要通过命令行接口（CLI）传递NPU配置：

```bash
# Arm Ethos-U55/U65 NPU (Corstone-300 FVP)
export ARMFVP_BIN_PATH=/path/to/FVP_Corstone_SSE-300_<ver>/models/Linux64_GCC-<gcc>/

# Arm Ethos-U85 (Corstone-320 FVP)
export ARMFVP_BIN_PATH=/path/to/FVP_Corstone_SSE-320_<ver>/models/Linux64_GCC-<gcc>/
export ARMFVP_EXTRA_FLAGS='-C;mps4_board.subsystem.ethosu.num_macs=2048'  # match chosen ETHOS_U85_* Kconfig
```

> 译注——可移植路径：上面的`/path/to/`、`<ver>`与`<gcc>`均为官方占位符，分别代表安装位置、版本及工具链标识，不是作者机器的固定地址，也不是可以原样执行的Shell参数。将FVP安装位置配置到读者自己的环境变量中，勿把某台机器的路径写进公共文档或项目配置。U85额外参数中的MAC数量必须与所选`ETHOS_U85_*` Kconfig配置相符。

<a id="build-and-run-on-the-fvp"></a>

### 75.3.2 在FVP上构建并运行（Build and run on the FVP）

官方页面给出的命令如下：

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SHARED_SRAM=y
-DCONFIG_ETHOS_U55_128=y
west build -t run
```

> 译注——命令换行：本页多段原命令把后续`-D`参数单独放在新行，却没有Shell续行符，直接逐行执行会将这些参数误当成命令。为便于对照，原块完整保留；下方及各后续示例附上仅修复续行的POSIX Shell写法。相对路径从Zephyr仓库根目录解析。

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SHARED_SRAM=y \
-DCONFIG_ETHOS_U55_128=y
west build -t run
```

<a id="vela-memory-modes-and-overlays"></a>

## 75.4 Vela内存模式与覆盖文件（Vela memory modes and overlays）

Vela支持多种Arm Ethos NPU内存放置模式（Memory placement mode）。示例在构建时通过`CONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_*`复现这些模式：

- `CONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SHARED_SRAM`
- `CONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_DEDICATED_SRAM`
- `CONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SRAM_ONLY`

**开发板覆盖文件（Board overlays）**用于将TensorFlow Lite缓冲区放到匹配的内存区域：

- `boards/mps3_corstone300_fvp.sram_only.overlay`
- `boards/mps4_corstone320_fvp.sram_only.overlay`
- `boards/mps3_corstone300_fvp.dedicated_sram.overlay`
- `boards/mps4_corstone320_fvp.dedicated_sram.overlay`

`Dedicated_Sram`还要求在覆盖文件中声明`ETHOSU_FAST`区域。

**构建示例（Example builds）**如下。原文将`Shared_Sram`标为默认模式：

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SHARED_SRAM=y
-DCONFIG_ETHOS_U55_128=y
west build -t run
```

译注——修复续行后的同参数命令：

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SHARED_SRAM=y \
-DCONFIG_ETHOS_U55_128=y
west build -t run
```

`Sram_Only`：Corstone-300上的Arm Ethos-U65 NPU。

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SRAM_ONLY=y
-DCONFIG_ETHOS_U65_256=y
-DDTC_OVERLAY_FILE=boards/mps3_corstone300_fvp.sram_only.overlay
west build -t run
```

译注——修复续行后的同参数命令：

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SRAM_ONLY=y \
-DCONFIG_ETHOS_U65_256=y \
-DDTC_OVERLAY_FILE=boards/mps3_corstone300_fvp.sram_only.overlay
west build -t run
```

`Dedicated_Sram`：Corstone-320上的Arm Ethos-U85 NPU。

```sh
# From the root of the zephyr repository
west build -b mps4/corstone320/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_DEDICATED_SRAM=y
-DCONFIG_ETHOS_U85_2048=y
-DDTC_OVERLAY_FILE=boards/mps4_corstone320_fvp.dedicated_sram.overlay
west build -t run
```

译注——修复续行后的同参数命令：

```sh
# From the root of the zephyr repository
west build -b mps4/corstone320/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_DEDICATED_SRAM=y \
-DCONFIG_ETHOS_U85_2048=y \
-DDTC_OVERLAY_FILE=boards/mps4_corstone320_fvp.dedicated_sram.overlay
west build -t run
```

> 注意：Arm Ethos-U55 NPU不支持`Dedicated_Sram`。必须确保模型使用的Vela模式与选定的构建模式一致。

> 译注——默认值与模型匹配：当前Kconfig选择项默认使用`CONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_HAL_DEFAULT`，即不覆盖硬件抽象层（Hardware abstraction layer，HAL）的默认区域映射。上面的命令显式选择`Shared_Sram`，不能据此断定省略参数时也选择相同模式。切换U55、U65、U85或MAC数量时，还应按照对应Vela参数重新准备模型；更改构建选项不会自动重新编译模型。切换这些配置宜使用不同的相对构建目录或干净构建。

<a id="memory-regions"></a>

## 75.5 内存区域（Memory regions）

Arm Ethos-U NPU命令流（Command stream）用区域索引（Region index，0—3）寻址内存区域，这些索引对应NPU配置中的`REGIONCFG`值。Vela在编译模型时分配索引，HAL再根据NPU类型，将各索引映射到物理AXI接口或`MEM_ATTR`条目。

本示例的映射由所选`CONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_*`选项定义。下表给出示例CMake与Kconfig逻辑所实现的区域索引分配：

| 模式（Mode） | 权重（weights） | 临时缓冲（scratch） | 快速临时缓冲（fast_scratch） | 命令流（cmd_stream） |
| --- | --- | --- | --- | --- |
| Shared_Sram | 3 | 0 | 0 | 3 |
| Dedicated_Sram | 3 | 3 | 0 | 3 |
| Sram_Only | 0 | 0 | 0 | 0 |

这些值在构建过程中由`zephyr_compile_definitions()`作为`NPU_REGIONCFG_n`与`NPU_QCONFIG`宏应用，确保HAL与驱动使用一致的区域配置：

- `NPU_REGIONCFG_0`：权重。
- `NPU_REGIONCFG_1`：临时缓冲。
- `NPU_REGIONCFG_2`：快速临时缓冲。
- `NPU_QCONFIG`：命令流区域。

**架构映射（Architectural mapping）**如下：

- **Arm Ethos-U55/U65 NPU**：区域0—1路由到AXI0（片上SRAM），区域2—3路由到AXI1（外部内存）。这一映射由架构固定。
- **Arm Ethos-U85 NPU**：区域0—3选择可编程的`MEM_ATTR[0-3]`条目。HAL默认将`MEM_ATTR[0-1]`映射到SRAM，将`MEM_ATTR[2-3]`映射到外部DDR。如果系统使用自定义内存拓扑，可以覆盖这些默认值。

使用`Dedicated_Sram`时，必须确保设备树覆盖文件中存在`ETHOSU_FAST`节点，为NPU的`fast_scratch`提供有效区域。

> 译注——配置帮助与实现差异：本次核对的`CMakeLists.txt`对`Sram_Only`实际定义的是`0 / 0 / 0 / 0`，与上表一致；但同版本Kconfig提示及帮助文字写为`1 / 0 / 0 / 1`。这里保留官方表格，并明确指出差异；排查生成配置时应同时核对实际编译宏。CMake使用全局的`zephyr_compile_definitions()`传播这些宏，使HAL编译也能看到相同覆盖值。

<a id="configuring-pmu-events-via-cmake"></a>

## 75.6 通过CMake配置PMU事件（Configuring PMU Events via CMake）

启用`CONFIG_SAMPLE_TFLM_ETHOSU_PMU`后，示例会报告每次推理的性能监控单元（Performance monitoring unit，PMU）计数器。可以设置`ETHOSU_PMU_EVENT_0..3`覆盖计数事件；硬件支持时还可设置4—7号事件。

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SHARED_SRAM=y
-DCONFIG_SAMPLE_TFLM_ETHOSU_PMU=y
-DETHOSU_PMU_EVENT_0=ETHOSU_PMU_AXI0_RD_DATA_BEAT_RECEIVED
-DETHOSU_PMU_EVENT_1=ETHOSU_PMU_AXI1_RD_DATA_BEAT_RECEIVED
west build -t run
```

译注——修复续行后的同参数命令：

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SHARED_SRAM=y \
-DCONFIG_SAMPLE_TFLM_ETHOSU_PMU=y \
-DETHOSU_PMU_EVENT_0=ETHOSU_PMU_AXI0_RD_DATA_BEAT_RECEIVED \
-DETHOSU_PMU_EVENT_1=ETHOSU_PMU_AXI1_RD_DATA_BEAT_RECEIVED
west build -t run
```

<a id="pmu-report-format"></a>

## 75.7 PMU报告格式（PMU report format）

启用后，示例在每次推理之后打印简短的PMU报告：

```text
Ethos-U PMU report:
ethosu_pmu_cycle_cntr : 134869
ethosu_pmu_cntr0 : 133577
ethosu_pmu_cntr1 : 0
ethosu_pmu_cntr2 : 111744
ethosu_pmu_cntr3 : 0
# (if supported, counters 4..7 are also printed.)
```

支持时还会打印4—7号计数器。原报告中的周期数与事件计数为示例值，不是本次翻译的性能测量结果。

<a id="timing-adapters-ta"></a>

## 75.8 时序适配器（Timing Adapters (TA)）

时序适配器（Timing Adapter，TA）允许在支持的平台（FVP或FPGA）上模拟内存带宽与延迟限制。使用`-DDTC_OVERLAY_FILE=...`显式应用TA覆盖文件；TA覆盖文件可与任何Vela内存模式组合，用来研究时序影响。

完整TA说明见[评估套件文档（Evaluation Kit docs）](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/main/docs/sections/timing_adapters.md)。

<a id="ta-overlay-with-sram-only-corstone-320"></a>

### 75.8.1 TA覆盖与Sram\_Only组合：Corstone-320（TA overlay with Sram\_Only (Corstone-320)）

```sh
# From the root of the zephyr repository
west build -b mps4/corstone320/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SRAM_ONLY=y
-DCONFIG_ETHOS_U85_2048=y
-DDTC_OVERLAY_FILE="boards/mps4_corstone320_fvp.ta.overlay;boards/mps4_corstone320_fvp.sram_only.overlay"
west build -t run
```

译注——修复续行后的同参数命令；保留包围分号分隔覆盖文件列表的引号：

```sh
# From the root of the zephyr repository
west build -b mps4/corstone320/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SRAM_ONLY=y \
-DCONFIG_ETHOS_U85_2048=y \
-DDTC_OVERLAY_FILE="boards/mps4_corstone320_fvp.ta.overlay;boards/mps4_corstone320_fvp.sram_only.overlay"
west build -t run
```

<a id="ta-overlay-only-corstone-300"></a>

### 75.8.2 仅添加TA覆盖：Corstone-300（TA overlay only (Corstone-300)）

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SHARED_SRAM=y
-DCONFIG_ETHOS_U55_128=y
-DDTC_OVERLAY_FILE=boards/mps3_corstone300_fvp.ta.overlay
west build -t run
```

译注——修复续行后的同参数命令：

```sh
# From the root of the zephyr repository
west build -b mps3/corstone300/fvp samples/modules/tflite-micro/tflm_ethosu -- -DCONFIG_SAMPLE_TFLM_ETHOSU_MEM_MODE_SHARED_SRAM=y \
-DCONFIG_ETHOS_U55_128=y \
-DDTC_OVERLAY_FILE=boards/mps3_corstone300_fvp.ta.overlay
west build -t run
```

<a id="trademarks"></a>

## 75.9 商标（Trademarks）

Arm、Ethos和Corstone是Arm Limited（或其子公司、关联公司）在美国及／或其他地区的注册商标或商标。

TensorFlow、TensorFlow徽标及任何相关标志均为Google Inc.的商标。


> 译注——实现依据：[samples/modules/tflite-micro/tflm_ethosu/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/tflm_ethosu/Kconfig)、[samples/modules/tflite-micro/tflm_ethosu/CMakeLists.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/tflm_ethosu/CMakeLists.txt)、[samples/modules/tflite-micro/tflm_ethosu/src/main.cpp](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/tflm_ethosu/src/main.cpp)、[samples/modules/tflite-micro/tflm_ethosu/src/models/keyword_spotting_cnn_small_int8/model.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/tflm_ethosu/src/models/keyword_spotting_cnn_small_int8/model.h)、[samples/modules/tflite-micro/tflm_ethosu/src/models/keyword_spotting_cnn_small_int8/input.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/tflm_ethosu/src/models/keyword_spotting_cnn_small_int8/input.h)、[samples/modules/tflite-micro/tflm_ethosu/src/models/keyword_spotting_cnn_small_int8/output.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/tflm_ethosu/src/models/keyword_spotting_cnn_small_int8/output.h)。这些链接对应本次核对的官方main来源，内容会随分支变化，所保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库源码仅用于版本对照。

对应官方文档源码：[samples/modules/tflite-micro/tflm_ethosu/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/tflite-micro/tflm_ethosu/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/modules/tflite-micro/tflm_ethosu/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P074_TensorFlowLiteMicro魔杖示例.md) · [返回大纲](大纲.md)
