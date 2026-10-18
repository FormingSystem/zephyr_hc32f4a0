---
id: learning.zephyr-docs.kconfig-reference.page-250
title: "`modules/tflite-micro`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第250章\_`modules/tflite-micro`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/tflite-micro` 的 2 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_TENSORFLOW_LITE_MICRO"></a>

## 250.1 `CONFIG_TENSORFLOW_LITE_MICRO`

**提示（Prompt）**：TensorFlow Lite Micro 支持（TensorFlow Lite Micro Support）

**说明（Help）**

此选项启用 TensorFlow Lite Micro 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
0
```

**主动选择（Selects）**

```text
CONFIG_REQUIRES_FULL_LIBCPP
```

**定义位置（Location）**：[`modules/tflite-micro/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/tflite-micro/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_REQUIRES_FULL_LIBCPP`](P198_lib_配置项参考_2.md#CONFIG_REQUIRES_FULL_LIBCPP)。

<a id="CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS"></a>

## 250.2 `CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`

**提示（Prompt）**：使用经优化 CMSIS-NN 内核的 TensorFlow Lite Micro（optimized CMSIS-NN kernels）

**说明（Help）**

此选项在使用 TensorFlow Lite Micro 时，添加对 CMSIS-NN 优化内核（optimized kernels）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TENSORFLOW_LITE_MICRO && CONFIG_CPU_CORTEX_M && 0
```

**主动选择（Selects）**

```text
CONFIG_CMSIS_NN
CONFIG_CMSIS_NN_ACTIVATION
CONFIG_CMSIS_NN_BASICMATH
CONFIG_CMSIS_NN_CONCATENATION
CONFIG_CMSIS_NN_CONVOLUTION
CONFIG_CMSIS_NN_FULLYCONNECTED
CONFIG_CMSIS_NN_NNSUPPORT
CONFIG_CMSIS_NN_POOLING
CONFIG_CMSIS_NN_RESHAPE
CONFIG_CMSIS_NN_SOFTMAX
CONFIG_CMSIS_NN_SVD
CONFIG_CMSIS_NN_LSTM
CONFIG_CMSIS_NN_TRANSPOSE
CONFIG_CMSIS_NN_PAD
```

**定义位置（Location）**：[`modules/tflite-micro/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/tflite-micro/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_TENSORFLOW_LITE_MICRO`](P250_modules_tflite-micro_配置项参考.md#CONFIG_TENSORFLOW_LITE_MICRO)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_CMSIS_NN_ACTIVATION`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_ACTIVATION)、[`CONFIG_CMSIS_NN_BASICMATH`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_BASICMATH)、[`CONFIG_CMSIS_NN_CONCATENATION`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_CONCATENATION)、[`CONFIG_CMSIS_NN_CONVOLUTION`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_CONVOLUTION)、[`CONFIG_CMSIS_NN_FULLYCONNECTED`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_FULLYCONNECTED)、[`CONFIG_CMSIS_NN_NNSUPPORT`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_NNSUPPORT)、[`CONFIG_CMSIS_NN_POOLING`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_POOLING)、[`CONFIG_CMSIS_NN_RESHAPE`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_RESHAPE)、[`CONFIG_CMSIS_NN_SOFTMAX`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_SOFTMAX)、[`CONFIG_CMSIS_NN_SVD`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_SVD)、[`CONFIG_CMSIS_NN_LSTM`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_LSTM)、[`CONFIG_CMSIS_NN_TRANSPOSE`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_TRANSPOSE)、[`CONFIG_CMSIS_NN_PAD`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_PAD)。

<!-- kconfig-navigation -->

[上一章](P249_modules_segger_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P251_modules_trusted-firmware-a_配置项参考.md)
