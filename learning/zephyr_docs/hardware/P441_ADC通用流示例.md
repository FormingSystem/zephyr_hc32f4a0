---
id: learning.zephyr-docs.hardware.adcsamples-2
title: ADC通用流示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/adc/adc_stream/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="adc_stream"></a>

# 第441章\_ADC通用流示例

原文：[Generic ADC stream](https://docs.zephyrproject.org/latest/samples/drivers/adc/adc_stream/README.html)。读取日期：2026-10-13，`latest`。

## 441.1\_概述

本示例演示**模数转换器（Analog-to-Digital Converter，ADC）**流应用程序接口（Stream Application Programming Interface，Stream API）的用法，通过数据流取得 ADC 数据。

## 441.2\_构建与运行

示例支持一个 ADC，必须在设备树（Devicetree）中为它设置别名（Alias）`adc0`。例如，下面把 `adc0` 指向 ADC 节点标签 `ad4052`：

```dts
/ {
       aliases {
                       adc0 = &ad4052;
               };
       };
```

确认设备树中已经提供该别名后，在 Zephyr 仓库根目录的开发终端构建并烧录（Flash）：

```shell
west build -b <board to use> samples/drivers/adc/adc_stream
west flash
```

`<board to use>` 是目标开发板名称的占位符，执行前应替换为实际构建目标；不要将尖括号原样输入终端。

## 441.3\_示例输出

官方示例输出如下，包含 ADC 设备名称、数据及以纳秒（Nanosecond，ns）表示的时间值。`adc405@0` 是原日志中的设备名，保留原样。

```text
ADC data for adc405@0 (0.000074) 942995000ns
ADC data for adc405@0 (0.000446) 963059000ns
ADC data for adc405@0 (0.000297) 983124000ns
ADC data for adc405@0 (0.000446) 1003189000ns
```

另见[ADC 接口参考](P463_ADC公共接口参考.md)和[示例源代码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/adc/adc_stream)。

---

[上一章：ADC采样序列示例](P440_ADC采样序列示例.md) · [下一章：RTIO的I2C标志](P442_RTIO的I2C标志.md) · [返回大纲](大纲.md)
