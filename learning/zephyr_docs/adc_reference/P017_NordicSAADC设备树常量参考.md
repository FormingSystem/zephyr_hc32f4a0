---
id: learning.zephyr-docs.adc_reference.adcheadernordic-17
title: NordicSAADC设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf-saadc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第17章\_NordicSAADC设备树常量参考

原文：[nrf-saadc_8h](https://docs.zephyrproject.org/latest/doxygen/html/nrf-saadc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/nrf-saadc.h` 提供Nordic逐次逼近模数转换器（Successive Approximation Analog-to-Digital Converter，SAADC）的输入选择宏（Macro）。其中 `NRF_SAADC_GND` 不只是一个输入编号，还关系到单端读取（Single-Ended Reading）是否保留负值。

## 17.1\_输入常量与偏移

下表保留原页全部32个宏和原始表达式。GND、测试偏移和AVSS项有原文说明；其余中文为标识符释义译注。电源节点的VDD、AVDD、DVDD、VDDL、DECB、VSS、VDDAO及VDDRF拼写保持原样，不据此推定所有芯片均支持全部选项。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `NRF_SAADC_AIN0` | `0` | 模拟输入（Analog Input）AIN0 |
| `NRF_SAADC_AIN1` | `1` | 模拟输入（Analog Input）AIN1 |
| `NRF_SAADC_AIN2` | `2` | 模拟输入（Analog Input）AIN2 |
| `NRF_SAADC_AIN3` | `3` | 模拟输入（Analog Input）AIN3 |
| `NRF_SAADC_AIN4` | `4` | 模拟输入（Analog Input）AIN4 |
| `NRF_SAADC_AIN5` | `5` | 模拟输入（Analog Input）AIN5 |
| `NRF_SAADC_AIN6` | `6` | 模拟输入（Analog Input）AIN6 |
| `NRF_SAADC_AIN7` | `7` | 模拟输入（Analog Input）AIN7 |
| `NRF_SAADC_AIN8` | `8` | 模拟输入（Analog Input）AIN8 |
| `NRF_SAADC_AIN9` | `9` | 模拟输入（Analog Input）AIN9 |
| `NRF_SAADC_AIN10` | `10` | 模拟输入（Analog Input）AIN10 |
| `NRF_SAADC_AIN11` | `11` | 模拟输入（Analog Input）AIN11 |
| `NRF_SAADC_AIN12` | `12` | 模拟输入（Analog Input）AIN12 |
| `NRF_SAADC_AIN13` | `13` | 模拟输入（Analog Input）AIN13 |
| `NRF_SAADC_GND` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET - 1)` | 将ADC负输入短接到地（Ground，GND） |
| `NRF_SAADC_AIN_TEST_SHIM_OFFSET` | `64` | 配置测试（TEST）SAADC输入所使用的偏移量（Offset） |
| `NRF_SAADC_AVSS` | `(NRF_SAADC_AIN_TEST_SHIM_OFFSET + 0)` | 将AVSS配置为通道输入所使用的符号 |
| `NRF_SAADC_AIN_VDD_SHIM_OFFSET` | `128` | VDD类输入的偏移常量；原页未另作说明 |
| `NRF_SAADC_VDD` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 0)` | VDD输入 |
| `NRF_SAADC_VDDDIV2` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 1)` | VDD二分之一输入 |
| `NRF_SAADC_AVDD` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 2)` | AVDD输入 |
| `NRF_SAADC_DVDD` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 3)` | DVDD输入 |
| `NRF_SAADC_VDDHDIV5` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 4)` | VDDH五分之一输入 |
| `NRF_SAADC_VDDL` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 5)` | VDDL输入 |
| `NRF_SAADC_DECB` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 6)` | DECB输入 |
| `NRF_SAADC_VSS` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 7)` | VSS输入 |
| `NRF_SAADC_VDDAO3V0` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 8)` | VDDAO3V0输入 |
| `NRF_SAADC_VDDAO1V8` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 9)` | VDDAO1V8输入 |
| `NRF_SAADC_VDDAO0V8` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 10)` | VDDAO0V8输入 |
| `NRF_SAADC_VDDRF` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 11)` | VDDRF输入 |
| `NRF_SAADC_VBAT` | `(NRF_SAADC_AIN_VDD_SHIM_OFFSET + 12)` | 电池电压（Battery Voltage，VBAT）输入 |
| `NRF_SAADC_AIN_DISABLED` | `255 /* UINT8_MAX */` | 禁用输入（Input Disabled）；255为8位无符号整数最大值，原注释为UINT8_MAX |

## 17.2\_负输入接地的硬件单端模式

`NRF_SAADC_GND` 将ADC负输入短接到地。nRF SAADC硬件只支持差分读取（Differential Reading）；其单端模式（Single-Ended Mode，SE）实际上也是差分模式，只是负输入短接到地（Ground，GND）。要使用nRF SAADC的这种SE模式，应将负输入设置为 `NRF_SAADC_GND`：

```dts
zephyr,input-positive = <NRF_SAADC_AIN3>;
zephyr,input-negative = <NRF_SAADC_GND>;
```

这里的 `zephyr,input-positive` 为正输入属性，`zephyr,input-negative` 为负输入属性。

## 17.3\_驱动仿真的Zephyr单端模式

nRF SAADC驱动也支持利用硬件SE模式仿真Zephyr定义的“单端”模式。在这个模式下，**软件会把负读数钳位到0**，从而模拟Zephyr对单端ADC行为的定义。要这样使用，只定义正输入：

```dts
zephyr,input-positive = <NRF_SAADC_AIN3>;
```

因此，显式设置接地负输入与只提供正输入，是原文区分的两种配置方式；负读数钳位（Clamping）属于后一种方式的驱动行为。完整可见定义见[源码页](P018_NordicSAADC设备树常量源码.md)。

---

[上一章：NordicADC设备树常量源码](P016_NordicADC设备树常量源码.md) · [下一章：NordicSAADC设备树常量源码](P018_NordicSAADC设备树常量源码.md) · [返回大纲](大纲.md)
