---
id: learning.zephyr-docs.hardware.adcsamples-1
title: ADC采样序列示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/adc/adc_sequence/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="adc_sequence"></a>

# 第440章\_ADC采样序列示例

原文：[Analog-to-Digital Converter (ADC) sequence sample](https://docs.zephyrproject.org/latest/samples/drivers/adc/adc_sequence/README.html)。读取日期：2026-10-13，`latest`。

## 440.1\_概述

本示例演示通过采样序列（Sampling Sequence）使用**模数转换器（Analog-to-Digital Converter，ADC）**驱动应用程序接口（Application Programming Interface，API）。

根据目标开发板，示例按序列设置从两个通道读取 ADC 样本，并将读数输出到控制台。**读取整个序列只调用一次 [`adc_read()`](P463_ADC公共接口参考.md)。**如果能取得所用参考源的电压，就把原始读数转换成毫伏（Millivolt）。

示例按照设备树（Devicetree）配置构造 ADC 设备并设置通道。接口介绍见[ADC 驱动文档](https://docs.zephyrproject.org/latest/hardware/peripherals/adc.html#adc-api)。

## 440.2\_设备树准备

确认 ADC 已启用，即 `status = "okay";`。每个通道都应作为 ADC 的子节点，按需要设置增益（Gain）、参考源（Reference）、采集时间（Acquisition Time）以及使用时的过采样（Oversampling）。

还需要为目标 ADC 提供设备树别名（Devicetree Alias）`adc0`。原文所链接的配置例子为 [boards/nrf52840dk_nrf52840.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/adc/adc_dt/boards/nrf52840dk_nrf52840.overlay)。译注：原链接实际指向 `adc_dt` 示例中的覆盖文件，这里保留该来源路径。

## 440.3\_在Nordic nRF52840上构建和运行

以下命令为 [nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk) 构建并烧录（Flash），在 Zephyr 仓库根目录的开发终端执行：

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/adc/adc_sequence
west flash
```

为其他开发板构建时，将 `nrf52840dk/nrf52840` 替换为目标板名称，并提供对应的设备树覆盖文件。

## 440.4\_示例输出

每秒应重复输出类似下面的内容。日志中的 `ADC_0` 为 ADC 设备名称；通道 0 和通道 1 各列出 5 个序列样本，等号左侧为原始读数，右侧为毫伏值。

```text
ADC sequence reading [1]:
- ADC_0, channel 0, 5 sequence samples:
- - 36 = 65mV
- - 35 = 63mV
- - 36 = 65mV
- - 35 = 63mV
- - 36 = 65mV
- ADC_0, channel 1, 5 sequence samples:
- - 0 = 0mV
- - 0 = 0mV
- - 1 = 1mV
- - 0 = 0mV
- - 1 = 1mV
```

如果不支持所用 ADC，则输出错误消息。

另见[ADC 接口参考](P463_ADC公共接口参考.md)和[示例源代码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/adc/adc_sequence)。

---

[上一章：ADC设备树示例](P439_ADC设备树示例.md) · [下一章：ADC通用流示例](P441_ADC通用流示例.md) · [返回大纲](大纲.md)
