---
id: learning.zephyr-docs.dsp.page-3
title: CMSISDSP移动平均示例
kind: reference
status: maintained
domains: [zephyr, dsp]
source_url: https://docs.zephyrproject.org/latest/samples/modules/cmsis_dsp/moving_average/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_CMSISDSP移动平均示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/modules/cmsis_dsp/moving_average/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 3.1\_概述（Overview）

本示例展示如何使用 CMSIS-DSP 库计算信号的移动平均（Moving Average）。

原文说明，它可以在 Zephyr 支持的任意开发板上运行；不过 CMSIS-DSP 专门针对 Arm Cortex-A 和 Cortex-M 处理器进行优化。

移动平均滤波器（Moving Average Filter）常用于平滑带噪声的数据。它可以实现为有限冲激响应滤波器（Finite Impulse Response Filter，FIR），所有滤波系数均取 `1/N`；`N` 是抽头数（Number of Taps），也就是移动平均窗口的大小。

示例使用包含 32 个样本的简单输入信号，以 10 个样本为一个窗口计算移动平均。只需调用一次 CMSIS-DSP 的 `arm_fir_q31()`，即可完成输出计算并在控制台显示结果。

> 原文注意：为便于比较 CMSIS-DSP 在 Arm 处理器和其他体系结构上的效率，示例会输出计算移动平均所用的时间及周期数（Cycles）。

译注——窗口与定点数：当前示例输入为 0～31 的斜坡，历史状态初始化为 0。开始时不足 10 个历史样本的部分补零，除数仍为 10，所以前几项输出为 0.00、0.10、0.30、0.60，而不是按已有样本数重新求平均。`q31_t` 使用有符号 Q31 定点数（Fixed-Point）表示；源码先把输入 `i` 左移 24 位，相当于在 Q31 数值中保存 `i/128`，输出显示时再除以 `2^24` 恢复示例显示尺度。不能直接把整数 31 当作 Q31 格式中的数值 31 输入。

## 3.2\_依赖要求（Requirements）

CMSIS-DSP 是可选模块，必须显式加入 Zephyr 工作区：

```sh
west config manifest.project-filter -- +cmsis-dsp
west update cmsis-dsp
```

译注：以上命令在已有 west 工作区中运行。第一条设置清单项目过滤规则以包含 `cmsis-dsp`，第二条取得该模块；它们不是安装目标工具链。已有 `manifest.project-filter` 自定义规则时，先查看现有设置再合并所需规则，避免无意覆盖其他项目筛选。示例源码本身由 Zephyr 仓库提供，CMSIS-DSP 库由相应模块提供。

## 3.3\_构建与运行（Building and Running）

示例可按以下方式构建并运行：

```sh
west build -b qemu_cortex_m0 samples/modules/cmsis_dsp/moving_average
west build -t run
```

译注：在 Zephyr 源码根目录执行，先准备该目标工具链、QEMU 和上一节模块。示例的 `prj.conf` 启用 `CONFIG_CMSIS_DSP`、完整 C 库及浮点打印支持。这里直接调用 CMSIS-DSP 的 `arm_fir_q31()`，不要把它误认为本示例已经演示了全部 zDSP 通用接口。

示例输出移动平均计算所用的周期数，以及输入信号每个 10 样本窗口的平均值：

```text
*** Booting Zephyr OS build v3.6.0-224-gb55824751d6c ***
Time: 244 us (244 cycles)
Input[00]:  0  0  0  0  0  0  0  0  0  0 | Output[00]:   0.00
Input[01]:  0  0  0  0  0  0  0  0  0  1 | Output[01]:   0.10
Input[02]:  0  0  0  0  0  0  0  0  1  2 | Output[02]:   0.30
Input[03]:  0  0  0  0  0  0  0  1  2  3 | Output[03]:   0.60
...
Input[30]: 21 22 23 24 25 26 27 28 29 30 | Output[30]:  25.50
Input[31]: 22 23 24 25 26 27 28 29 30 31 | Output[31]:  26.50
```

原日志中的 `Time` 为耗时，`Input` 为参与该输出计算的窗口内容，`Output` 为平均值。最后一项使用 22～31，平均值为 26.50。

译注——缓冲区与测量边界：当前源码为 MVE（M-profile Vector Extension，M 系列向量扩展）实现需要的额外状态区预留空间，系数数组向 4 个元素的倍数补齐，并对相关数组作 16 字节对齐。不要仅按 10 个抽头和 32 个样本随意缩减缓冲区。计时在 `arm_fir_q31()` 前后调用 `k_cycle_get_32()`，再用 `k_cyc_to_us_floor32()` 转换为微秒，未计入初始化和控制台打印。该周期计数对应平台时钟实现，原页 `244 us (244 cycles)` 是特定历史运行值，不能用来证明其他芯片或当前配置具有相同性能。本次没有执行构建或性能测试。


译注核对来源：[samples/modules/cmsis_dsp/moving_average/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/cmsis_dsp/moving_average/src/main.c)、[samples/modules/cmsis_dsp/moving_average/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/cmsis_dsp/moving_average/prj.conf)、[samples/modules/cmsis_dsp/moving_average/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/cmsis_dsp/moving_average/tests.yaml)、[modules/cmsis-dsp/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/cmsis-dsp/Kconfig)。

本仓库的[对应源码](../../../samples/modules/cmsis_dsp/moving_average/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行模块下载、固件构建、模拟运行或性能测试。

<a id="cmsis-dsp-moving-average"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>

[上一章](P002_CMSISDSP示例目录.md) · [返回大纲](大纲.md)
