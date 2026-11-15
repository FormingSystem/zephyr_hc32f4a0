---
id: learning.zephyr-docs.hardware.adc
title: ADC模数转换
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/adc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第9章\_ADC模数转换

原文：[Analog-to-Digital Converter (ADC)](https://docs.zephyrproject.org/latest/hardware/peripherals/adc.html)。读取日期：2026-10-12，`latest`。

本页是**模数转换器（Analog-to-Digital Converter，ADC）**的官方接口与示例入口。原文“概述”标题下没有额外正文。

## 9.1\_接口参考

见 [ADC 接口](P463_ADC公共接口参考.md)。

## 9.2\_相关示例

- [ADC 电源管理](https://docs.zephyrproject.org/latest/samples/boards/st/power_mgmt/adc/README.html)：在 STM32 的低功耗场景使用 ADC。
- [ADC 序列采样](P440_ADC采样序列示例.md)：通过采样序列读取 ADC 通道的模拟输入。
- [使用设备树的 ADC](P439_ADC设备树示例.md)：读取 ADC 通道模拟输入。
- [AutAnalog ADC FIR与FIFO](https://docs.zephyrproject.org/latest/samples/boards/infineon/autanalog/fir_fifo/README.html)：结合 FIR 滤波和 **先进先出（First In, First Out，FIFO）** 批量采集读取 AutAnalog ADC 通道。
- [FRDM-MCXA156 LPDAC、OPAMP与LPADC](P099_FRDM模拟信号链示例.md)：放大运算放大器输入，再用 ADC 采样。
- [通用 ADC 流](P441_ADC通用流示例.md)：以流方式取得 ADC 数据。
- [电力传输分析器](https://docs.zephyrproject.org/latest/samples/boards/google/twinkie_v2/pda/README.html)：实现基础 Power Delivery 分析器，判断 **通用串行总线（Universal Serial Bus，USB）** 设备是否正在充电。

> 译注：本入口列出的开发板专用示例不代表可直接用于 HC32；外链 **应用程序编程接口（Application Programming Interface，API）** 和示例正文各自记录翻译状态。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：GPIO与输入设备入口](P008_GPIO与输入入口.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：DAC数模转换](P010_DAC数模转换.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：GPIO与输入入口](P008_GPIO与输入入口.md) · [下一章：DAC数模转换](P010_DAC数模转换.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
