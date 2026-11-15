---
id: learning.zephyr-docs.kconfig-reference.page-220
title: "`modules/cmsis-nn`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第220章\_`modules/cmsis-nn`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/cmsis-nn` 的 14 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CMSIS_NN"></a>

## 220.1 `CONFIG_CMSIS_NN`

**提示（Prompt）**：CMSIS-NN 库支持（Library Support）

**说明（Help）**

启用 CMSIS-NN 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M
```

**主动选择（Selects）**

```text
CONFIG_CMSIS_DSP
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_CMSIS_DSP`](P009_module_cmsis-dsp_zephyr_配置项参考.md#CONFIG_CMSIS_DSP)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)。

<a id="CONFIG_CMSIS_NN_ACTIVATION"></a>

## 220.2 `CONFIG_CMSIS_NN_ACTIVATION`

**提示（Prompt）**：激活（Activation）

**说明（Help）**

启用激活层（activation layers）的神经网络（NN）库。可执行的激活层包括修正线性单元（Rectified Linear Unit，ReLU）、sigmoid 和 tanh。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)。

<a id="CONFIG_CMSIS_NN_BASICMATH"></a>

## 220.3 `CONFIG_CMSIS_NN_BASICMATH`

**提示（Prompt）**：神经网络基础数学运算（Basic Math for NN）

**说明（Help）**

启用基础数学运算的神经网络（NN）库，提供逐元素加法和乘法（element-wise add and multiplication）函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)。

<a id="CONFIG_CMSIS_NN_CONCATENATION"></a>

## 220.4 `CONFIG_CMSIS_NN_CONCATENATION`

**提示（Prompt）**：拼接（Concatenation）

**说明（Help）**

启用拼接层（concatenation layers）的神经网络（NN）库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)。

<a id="CONFIG_CMSIS_NN_CONVOLUTION"></a>

## 220.5 `CONFIG_CMSIS_NN_CONVOLUTION`

**提示（Prompt）**：卷积（Convolution）

**说明（Help）**

卷积（convolution）、逐深度卷积（depthwise convolution）及其变体函数的集合。卷积分为 `im2col` 和通用矩阵乘法（GEMM）两个步骤实现。GEMM 使用与 CMSIS-DSP `arm_mat_mult` 相似的选项执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**弱选择（Implies）**

```text
CONFIG_CMSIS_NN_NNSUPPORT
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)、[`CONFIG_CMSIS_NN_NNSUPPORT`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_NNSUPPORT)。

<a id="CONFIG_CMSIS_NN_FULLYCONNECTED"></a>

## 220.6 `CONFIG_CMSIS_NN_FULLYCONNECTED`

**提示（Prompt）**：全连接（Fully Connected）

**说明（Help）**

全连接（fully-connected）和矩阵乘法（matrix multiplication）函数的集合。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**弱选择（Implies）**

```text
CONFIG_CMSIS_NN_NNSUPPORT
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)、[`CONFIG_CMSIS_NN_NNSUPPORT`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_NNSUPPORT)。

<a id="CONFIG_CMSIS_NN_LSTM"></a>

## 220.7 `CONFIG_CMSIS_NN_LSTM`

**提示（Prompt）**：长短期记忆（Long Short-Term Memory）

**说明（Help）**

启用长短期记忆（Long Short-Term Memory）的神经网络（NN）库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)。

<a id="CONFIG_CMSIS_NN_NNSUPPORT"></a>

## 220.8 `CONFIG_CMSIS_NN_NNSUPPORT`

**提示（Prompt）**：神经网络支持（NN Support）

**说明（Help）**

关闭时，默认行为是包含全部表（tables）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**被弱选择（Implied by）**

```text
CONFIG_CMSIS_NN_CONVOLUTION
CONFIG_CMSIS_NN_FULLYCONNECTED
CONFIG_CMSIS_NN_POOLING
CONFIG_CMSIS_NN_SVD
CONFIG_CMSIS_NN_CONVOLUTION
CONFIG_CMSIS_NN_FULLYCONNECTED
CONFIG_CMSIS_NN_POOLING
CONFIG_CMSIS_NN_SVD
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)、[`CONFIG_CMSIS_NN_CONVOLUTION`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_CONVOLUTION)、[`CONFIG_CMSIS_NN_FULLYCONNECTED`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_FULLYCONNECTED)、[`CONFIG_CMSIS_NN_POOLING`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_POOLING)、[`CONFIG_CMSIS_NN_SVD`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_SVD)。

<a id="CONFIG_CMSIS_NN_PAD"></a>

## 220.9 `CONFIG_CMSIS_NN_PAD`

**提示（Prompt）**：连接端口（Pad）

**说明（Help）**

启用填充层（pad layers）的神经网络（NN）库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)。

<a id="CONFIG_CMSIS_NN_POOLING"></a>

## 220.10 `CONFIG_CMSIS_NN_POOLING`

**提示（Prompt）**：池化（Pooling）

**说明（Help）**

启用池化层（pooling layers），包括最大池化（max pooling）和平均池化（average pooling）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**弱选择（Implies）**

```text
CONFIG_CMSIS_NN_NNSUPPORT
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)、[`CONFIG_CMSIS_NN_NNSUPPORT`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_NNSUPPORT)。

<a id="CONFIG_CMSIS_NN_RESHAPE"></a>

## 220.11 `CONFIG_CMSIS_NN_RESHAPE`

**提示（Prompt）**：形状重排（Reshape）

**说明（Help）**

启用形状重排层（reshape layers）的神经网络（NN）库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)。

<a id="CONFIG_CMSIS_NN_SOFTMAX"></a>

## 220.12 `CONFIG_CMSIS_NN_SOFTMAX`

**提示（Prompt）**：Softmax 归一化指数

**说明（Help）**

启用 softmax 层的神经网络（NN）库，采用基于 `exp2` 的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)。

<a id="CONFIG_CMSIS_NN_SVD"></a>

## 220.13 `CONFIG_CMSIS_NN_SVD`

**提示（Prompt）**：SVD

**说明（Help）**

启用原文称为“单值分解滤波器层”（Single Value Decomposition Filter layers）的神经网络（NN）库。

译注：此处展开名称按原文保留；原文使用 Single，不在翻译中静默改写为其他名称。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**弱选择（Implies）**

```text
CONFIG_CMSIS_NN_NNSUPPORT
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)、[`CONFIG_CMSIS_NN_NNSUPPORT`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN_NNSUPPORT)。

<a id="CONFIG_CMSIS_NN_TRANSPOSE"></a>

## 220.14 `CONFIG_CMSIS_NN_TRANSPOSE`

**提示（Prompt）**：转置（Transpose）

**说明（Help）**

启用转置层（transpose layers）的神经网络（NN）库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_NN
```

**被选择（Selected by）**

```text
CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS
```

**定义位置（Location）**：[`modules/cmsis-nn/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-nn/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → cmsis-nn（模块路径 `modules/lib/cmsis-nn`，相对于 west 工作区顶层目录） → CMSIS-NN 库支持（Library Support）

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_NN`](P220_modules_cmsis-nn_配置项参考.md#CONFIG_CMSIS_NN)、[`CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TENSORFLOW_LITE_MICRO_CMSIS_NN_KERNELS)。

<!-- kconfig-navigation -->

[上一章](P219_modules_cmsis-dsp_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P221_modules_cmsis_6_配置项参考.md)
