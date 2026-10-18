---
id: learning.zephyr-docs.board-samples.page-57
title: AXI时钟配置模块
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/amd/xclk_wiz/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="xclk-wiz"></a>

# 第57章\_AXI 时钟配置模块（AXI Clocking Wizard）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/amd/xclk_wiz/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/amd/xclk_wiz/README.rst/..)

<a id="overview"></a>

## 57.1 概述（Overview）

本示例展示 Xilinx AXI Clocking Wizard 驱动（`xlnx,clkx5-wiz-1.0`）在 AMD Versal Gen 2（Telluride／VERSAL_NET）上实现的三个早期访问（Early-Access，EA）`clock_control` API 项目：

- EA1：`clock_control_on`／`clock_control_off`，启用或关闭时钟输出。

- EA2：`clock_control_set_rate`，动态重配置 CLKOUT 频率。

- EA3：`clock_control_get_rate`，读回已设置的输出频率。

示例以第一个 AXI Clocking Wizard 实例（地址 `0xb2000000` 的 `clk_wiz_0`）的 CLKOUT0 为目标，依次尝试 100 MHz、200 MHz 和 300 MHz 目标频率。

> 译注——设备选择：本次应用实际通过 DT_COMPAT_GET_ANY_STATUS_OKAY(xlnx_clkx5_wiz_1_0) 取得一个启用的兼容节点。原文地址对应示例硬件；有多个实例时应明确所选设备，不能仅凭节点标签 clk_wiz_0 假定应用必然使用该地址。

当另一个 CLKOUT 处于活动状态时，`clock_control_set_rate` 会保留共享 MMCM VCO，只修改所选输出的分频器。请求频率必须能由当前 VCO 精确生成；否则调用失败，且不改变 MMCM 配置。

> 译注——时钟术语：MMCM 为混合模式时钟管理器（Mixed-Mode Clock Manager），VCO 为压控振荡器（Voltage-Controlled Oscillator）。多个输出共享 VCO；本次驱动检查其他活动输出后，要求所选分频器能精确产生目标频率，不能把请求值当成已成功设置的频率。

<a id="hardware-requirements"></a>

## 57.2 硬件要求（Hardware Requirements）

- AMD Versal Gen 2（VEK385 或等效型号）开发板。

- Vivado 比特流（Bitstream），其中已实例化的 AXI Clocking Wizard IP 位于：

  `0xb2000000`，输入参考时钟为 100 MHz。

- 用于串行输出的 JTAG 或 UART 连接。

<a id="building-and-running"></a>

## 57.3 构建与运行（Building and Running）

> 译注——执行前提：本节 west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链及对应板。构建目录由工具生成，下载与启动方式按具体板文档核对。本次仅核对文档和源码，未执行构建、烧录或硬件实验。

```text
west build -b versal2_apu samples/boards/amd/xclk_wiz
west flash   # or load via XSDB / JTAG
```

<a id="sample-output"></a>

## 57.4 输出示例（Sample Output）

> 译注——读回结果：Initial／Requesting／Actual 分别是初始频率、请求频率和驱动读回频率，单位 Hz。成功读回说明寄存器配置结果，不等同于用仪器测得引脚实际时钟频率。

```text
Clocking Wizard sample application
Device: clock-controller@b2000000, testing CLKOUT0
Initial CLKOUT0 rate: 100000000 Hz
CLKOUT0 enabled (clock_control_on OK)
Requesting CLKOUT0 = 100000000 Hz ...
Actual  CLKOUT0 = 100000000 Hz
Requesting CLKOUT0 = 200000000 Hz ...
Actual  CLKOUT0 = 200000000 Hz
Requesting CLKOUT0 = 300000000 Hz ...
Actual  CLKOUT0 = 300000000 Hz
CLKOUT0 disabled (clock_control_off OK)
```

<a id="configuration"></a>

## 57.5 配置（Configuration）

- 一个 `misc_clk_0` 固定时钟（Fixed-clock）节点，作为 100 MHz 参考。

- 一个地址位于 `0xb2000000` 的 `clk_wiz_0` 时钟控制器节点。

根据开发板硬件设计中配置的输出数量，调整覆盖文件中的 `xlnx,num-out-clks`。父时钟声明的频率必须与 Clocking Wizard 的硬件参考时钟频率一致。

> 译注——软硬件一致性：设备树描述不会创建 FPGA 中的时钟 IP。地址、参考频率与输出数量须和已加载的比特流一致；EA 是本页三个功能项目的标记，不等于对全部 clock_control 接口稳定性作统一声明。

<a id="related-files"></a>

## 57.6 相关文件（Related Files）

- 驱动：`drivers/clock_control/clock_control_xclk_wiz.c`

- DTS 绑定：`dts/bindings/clock/xlnx,clkx5-wiz-1.0.yaml`

- Kconfig：`drivers/clock_control/Kconfig.xclk_wiz`

<a id="see-also"></a>

## 57.7 另请参阅（See also）

[时钟控制（Clock Control）](../timer_reference/P092_时钟控制公共接口.md)

> 译注——源码入口：[main.c](../../../samples/boards/amd/xclk_wiz/src/main.c)；[prj.conf](../../../samples/boards/amd/xclk_wiz/prj.conf)；[clock_control_xclk_wiz.c](../../../drivers/clock_control/clock_control_xclk_wiz.c)；[xlnx,clkx5-wiz-1.0.yaml](../../../dts/bindings/clock/xlnx,clkx5-wiz-1.0.yaml)。链接相对本篇定位，仓库参照版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/amd/xclk_wiz/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/amd/xclk_wiz/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/amd/xclk_wiz/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P056_96Boards示例目录.md) · [返回大纲](大纲.md) · [下一章](P058_AMD示例目录.md)
