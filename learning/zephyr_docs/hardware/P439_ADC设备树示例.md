---
id: learning.zephyr-docs.hardware.adcsamples-0
title: ADC设备树示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/adc/adc_dt/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="adc_dt"></a>

# 第439章\_ADC设备树示例

原文：[Analog-to-Digital Converter (ADC) with devicetree](https://docs.zephyrproject.org/latest/samples/drivers/adc/adc_dt/README.html)。读取日期：2026-10-13，`latest`。

## 439.1\_概述

本示例演示**模数转换器（Analog-to-Digital Converter，ADC）**驱动应用程序接口（Application Programming Interface，API）的用法。根据目标开发板，它从一个或多个通道读取样本，并将结果打印到控制台。如果能够取得所用参考源的电压，就把原始读数转换成毫伏（Millivolt）。

ADC 通道的引脚取决于开发板；具体信息应查看开发板或微控制器（Microcontroller Unit，MCU）的数据手册。接口介绍见[ADC 驱动文档](https://docs.zephyrproject.org/latest/hardware/peripherals/adc.html#adc-api)。

## 439.2\_设备树准备

ADC 外设和引脚复用（Pin Multiplexing，Pinmux）在开发板的设备树源文件（Devicetree Source，DTS，即 `.dts` 文件）中配置。确认 ADC 已启用，也就是 `status = "okay";`。

此外，示例要求在 `zephyr,user` 节点的 `io-channels` 属性中指定 ADC 通道。这通常通过设备树覆盖文件（Devicetree Overlay）完成。示例 `boards` 子目录中针对 `nucleo_l073rz` 的覆盖文件可以调整用于其他开发板。

通道配置也必须在设备树中的 ADC 控制器子节点里给出，包括增益（Gain）、参考源（Reference）、采集时间（Acquisition Time），以及 ADC 分辨率（Resolution）和使用时的过采样（Oversampling）设置。示例见 [boards/nrf52840dk_nrf52840.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/adc/adc_dt/boards/nrf52840dk_nrf52840.overlay)。

## 439.3\_在ST Nucleo L073RZ上构建和运行

以下命令用于 [Nucleo L073RZ](https://docs.zephyrproject.org/latest/boards/st/nucleo_l073rz/doc/index.html#nucleo_l073rz)，在 Zephyr 仓库根目录的开发终端执行，依次构建并烧录（Flash）：

```shell
west build -b nucleo_l073rz samples/drivers/adc/adc_dt
west flash
```

为其他开发板构建时，将 `nucleo_l073rz` 替换为目标板名称，并提供对应的设备树覆盖文件。

## 439.4\_示例输出

每秒应重复输出类似下面的内容。`ADC_0` 是日志中的 ADC 设备名称，`channel 7` 表示通道 7；原始读数 36 换算为 65 mV。

```text
ADC reading:
- ADC_0, channel 7: 36 = 65mV
```

如果不支持所用 ADC，则输出错误消息。

另见[ADC 接口参考](P463_ADC公共接口参考.md)和[示例源代码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/adc/adc_dt)。

---

[上一章：I2C实时IO回环示例](P438_I2C实时IO回环示例.md) · [下一章：ADC采样序列示例](P440_ADC采样序列示例.md) · [返回大纲](大纲.md)
